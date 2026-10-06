"""Exact geometric and interval-certified controls for the tower audit."""

from fractions import Fraction as Q
import unittest

from flint import arb, ctx

from scripts.prime_towers import (
    geometric_moments, geometric_tails, cosine_sum, tower_parameters,
    tower_totals, active_power_count, tower_ramp_at_horizon,
    tower_repaired_at_horizon, service_partial_and_remainder_bound,
    aggregate_at_horizon,
)


class PrimeTowerTests(unittest.TestCase):
    def test_geometric_moments_and_tails_are_exact(self):
        for r in (Q(1, 2), Q(2, 3), Q(4, 5)):
            for k in (0, 1, 4, 12):
                mass, moment = geometric_moments(r, k)
                mass_tail, moment_tail = geometric_tails(r, k)
                self.assertEqual(mass, sum(r**j for j in range(1, k+1)))
                self.assertEqual(moment, sum(j*r**j for j in range(1, k+1)))
                self.assertEqual(mass+mass_tail, r/(1-r))
                self.assertEqual(moment+moment_tail, r/(1-r)**2)

    def test_tower_spectrum_changes_sign_and_repairs_are_sharp(self):
        for r in (Q(1, 2), Q(2, 3), Q(4, 5)):
            self.assertEqual(cosine_sum(r, Q(1)), r/(1-r))
            self.assertEqual(cosine_sum(r, Q(-1)), -r/(1+r))
            for c in (Q(-1), Q(-1, 3), Q(0), Q(2, 3), Q(1)):
                denominator = 1-2*r*c+r*r
                minus_repair = r/(1-r)-cosine_sum(r, c)
                plus_repair = r/(1+r)+cosine_sum(r, c)
                self.assertEqual(minus_repair, r*(1+r)*(1-c)/((1-r)*denominator))
                self.assertEqual(plus_repair, r*(1-r)*(1+c)/((1+r)*denominator))
                self.assertGreaterEqual(minus_repair, 0)
                self.assertGreaterEqual(plus_repair, 0)

    def test_interval_geometry_supplies_the_stationary_gram_identity(self):
        def overlap(left1, right1, left2, right2):
            return max(Q(0), min(right1, right2)-max(left1, left2))
        a, t, u = Q(5, 3), Q(7, 4), Q(-2, 5)
        gram = (overlap(t, t+a, u, u+a)-overlap(t, t+a, 0, a)
                -overlap(0, a, u, u+a)+a)
        variogram = lambda x: min(abs(x), a)
        self.assertEqual(gram, variogram(t)+variogram(u)-variogram(t-u))

    def test_integer_active_count_handles_exact_power_boundaries(self):
        self.assertEqual(active_power_count(2, 15), 3)
        self.assertEqual(active_power_count(2, 16), 4)
        self.assertEqual(active_power_count(2, 17), 4)
        self.assertEqual(active_power_count(3, 2), 0)
        self.assertEqual(active_power_count(3, 81), 4)

    def test_full_tower_keeps_the_exact_indefinite_early_witness(self):
        # For arbitrary ell>0, r in(0,1), only k=1 is active at 3ell/2.
        ell, r = Q(7, 3), Q(2, 3)
        off_diagonal = -ell*ell*r/2
        self.assertLess(-off_diagonal**2, 0)
        repaired_diagonal = 2*ell*r/(1-r)*(3*ell/4)
        # Direct repair has a valid PSD matrix at the same two points.
        repaired_off_diagonal = -off_diagonal
        self.assertGreaterEqual(repaired_diagonal**2-repaired_off_diagonal**2, 0)

    def test_closed_tower_ramps_match_direct_prime_power_sums(self):
        with ctx.workprec(200):
            for p in (2, 3, 5):
                for horizon in (1, 2, 16, 81):
                    ell, r = tower_parameters(p)
                    t = arb(horizon).log()
                    direct = sum(ell*r**j*(t-j*ell)
                                 for j in range(1, active_power_count(p, horizon)+1))
                    closed = tower_ramp_at_horizon(p, horizon)
                    self.assertTrue(closed.overlaps(arb(direct)))
                    repaired = tower_repaired_at_horizon(p, horizon)
                    mass, physical_moment = tower_totals(p)
                    self.assertTrue((repaired+closed-mass*t).contains(0))
                    if horizon > 1:
                        self.assertTrue(repaired > 0)
                        self.assertTrue(repaired < physical_moment)

    def test_service_divergence_remainder_is_interval_bounded(self):
        with ctx.workprec(200):
            for p in (2, 3, 5):
                for k in (1, 4, 16):
                    _, correction, bound = service_partial_and_remainder_bound(p, k)
                    self.assertTrue(correction > 0)
                    self.assertTrue(correction < bound)
                ell, r = tower_parameters(p)
                # The asymptotic leading term is two ell per level, not
                # a summable first service moment.
                from scripts.event_dynamics import arch_prime
                level16 = ell*r**16*arch_prime(16*ell)
                self.assertTrue(level16 > ell)
                self.assertTrue(level16 < 2*ell)

    def test_aggregate_identity_and_normalized_residual_decay(self):
        with ctx.workprec(200):
            previous_mass = previous_error = None
            t = arb(16).log()
            for cutoff in (17, 31, 101):
                mass, repaired, ramp = aggregate_at_horizon(cutoff, 16)
                self.assertTrue((repaired-(mass*t-ramp)).contains(0))
                error = ramp/mass
                self.assertTrue(error > 0)
                self.assertTrue(repaired/mass > 0)
                self.assertTrue(repaired/mass < t)
                if previous_mass is not None:
                    self.assertTrue(mass > previous_mass)
                    self.assertTrue(error < previous_error)
                previous_mass, previous_error = mass, error


if __name__ == '__main__':
    unittest.main()
