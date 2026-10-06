import unittest
from math import gcd

import sympy as sp
from flint import arb, ctx

from scripts.round007_hostile import (
    braid_matrices, broken_factor_swap, bulk_rayleigh, evidence, fake_monoid_map,
    generator_events, label_mutation, permuted_carrier, random_coprime_generators,
)
from scripts.round007_squares import event_weights


class Round007HostileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ctx.prec = 180

    def test_composite_coprime_sections_do_not_detect_primes(self):
        generators = random_coprime_generators()
        self.assertEqual(generators, random_coprime_generators())
        self.assertTrue(all(not sp.isprime(g) for g in generators))
        self.assertTrue(all(gcd(a, b) == 1 for i, a in enumerate(generators)
                            for b in generators[:i]))
        events = generator_events(generators, 256)
        self.assertNotIn(2, events)
        self.assertTrue(all(g in events for g in generators))
        for g in generators:
            # Return-time arithmetic still holds in the composite model.
            self.assertEqual(g ** 3 - g ** 2, (g - 1) * g ** 2)

    def test_fake_monoid_destroyed_unitarity(self):
        mapping = fake_monoid_map()
        self.assertEqual(mapping * sp.Matrix([0, 0, 1, -1]), sp.zeros(3, 1))
        self.assertNotEqual(mapping.T * mapping, sp.eye(4))

    def test_deliberately_destroyed_factor_swap_changes_compressed_energy(self):
        canonical, asymmetric, swap = broken_factor_swap(8)
        self.assertEqual(swap * canonical, canonical)
        self.assertNotEqual(swap * asymmetric, asymmetric)
        self.assertEqual(canonical.T * canonical, sp.eye(8))
        mutated_energy = asymmetric.T * asymmetric
        self.assertNotEqual(mutated_energy, sp.eye(8))
        self.assertEqual(mutated_energy[1, 1], sp.Rational(5, 2))
        self.assertEqual(mutated_energy[3, 3], 2)
        self.assertNotEqual((asymmetric - swap * asymmetric).T *
                            (asymmetric - swap * asymmetric), sp.zeros(8))

    def test_permuted_carrier_breaks_monotone_jet_clock(self):
        order, carrier = permuted_carrier()
        self.assertEqual([n for n in order if n in (1, 2, 4, 8)], [1, 4, 2, 8])
        self.assertEqual(carrier[2, 3], 1)  # 4 -> 3, negative log-height step.
        self.assertEqual(sorted(order), list(range(1, 9)))

    def test_fixed_geometry_random_charge_changes_mangoldt(self):
        labels, mutated = label_mutation(32)
        actual = event_weights(32)
        self.assertEqual(sorted(mutated), sorted(actual))
        p = next(p for p in labels if labels[p] != p)
        self.assertFalse((mutated[p] - actual[p]).contains(0))

    def test_braid_and_failure_of_commuting_differentials(self):
        for p in (2, 3, 5):
            sv, vs, spv = braid_matrices(p)
            self.assertNotEqual(sv, vs)
            self.assertEqual(vs, spv)

    def test_residual_obstruction_survives_zero_or_changed_positive_weights(self):
        self.assertLess(bulk_rayleigh({}), 0)
        self.assertLess(bulk_rayleigh({6: arb(100)}), 0)
        self.assertLess(bulk_rayleigh(event_weights(32), linear=0), 0)

    def test_full_mutation_evidence_contains_certified_separations(self):
        result = evidence()
        self.assertTrue(result["coprime_generators"]["zeta_prime_event_identity_fails"])
        self.assertEqual(result["fake_monoid"]["rank"], 3)
        self.assertTrue(result["independently_completed_towers"]["local_target_unchanged_below_log_N"])
        self.assertEqual(len(result["negative_residual_witnesses"]), 5)


if __name__ == "__main__":
    unittest.main()
