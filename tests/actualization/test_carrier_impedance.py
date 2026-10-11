"""Exact controls for the carrier-relative information diode.

Finite numbers here are calibration, not a proof of a physical or RH barrier.
The theorem over ALL real bounded probes follows by support, not sampling.
"""
import unittest
from fractions import Fraction

from actualization.carrier_impedance import (
    CarrierImpedanceError,
    bernoulli_posterior_plus,
    best_possible_posterior_error,
    quantum_helstrom_error_bounds,
    delayed_kernel, delayed_psi,
    finite_all_zero_prefix,
    late_witness,
    quadratic_kernel,
)


class CarrierImpedanceTests(unittest.TestCase):

    def test_delayed_kernel_identical_on_arbitrary_bounded_square(self):
        for bound in (0, 1, 2, 6, 15, 21):
            certificate = late_witness(bound)
            threshold = certificate["threshold"]
            amplitude = certificate["amplitude"]
            self.assertGreater(threshold, 2 * bound)
            self.assertTrue(certificate["same_all_real_carrier_probes_by_support"])
            self.assertTrue(certificate["global_reference_kernel_PSD_by_rank_one"])
            self.assertFalse(certificate["Euler_source_mutation_admissible"])
            self.assertFalse(certificate["RH_sign_proved"])
            for t in range(-bound, bound + 1):
                for u in range(-bound, bound + 1):
                    self.assertEqual(
                        delayed_kernel(t, u, threshold, amplitude),
                        quadratic_kernel(t, u),
                    )
            t_future = certificate["future_time"]
            self.assertEqual(delayed_psi(t_future, threshold, amplitude), -1)
            self.assertEqual(certificate["late_negative_diagonal"], -2)
            self.assertEqual(
                delayed_kernel(t_future, t_future, threshold, amplitude), -2,
            )

    def test_full_gram_sees_delayed_difference_beyond_carrier(self):
        x = late_witness(3)
        t = x["future_time"]
        self.assertEqual(quadratic_kernel(t, t), 2 * t * t)
        self.assertEqual(delayed_kernel(t, t, x["threshold"], x["amplitude"]), -2)
        # K(t,t) = 2*psi(t), so the infinite correlation map is faithful:
        # the missing feature is terminal finite access, not uniqueness.
        self.assertNotEqual(
            quadratic_kernel(t, t),
            delayed_kernel(t, t, x["threshold"], x["amplitude"]),
        )

    def test_finite_prefix_can_refute_but_cannot_certify_all_zero(self):
        for n in range(0, 100):
            report = finite_all_zero_prefix([0] * n)
            self.assertEqual(report["verdict"], "unresolved")
            self.assertFalse(report["positive_certificate"])
            self.assertEqual(
                finite_all_zero_prefix([0] * n + [1])["first_witness_index"], n + 1
            )

    def test_bayesian_channel_never_grants_finite_certainty(self):
        for n in range(0, 9):
            min_error = best_possible_posterior_error(n)
            self.assertEqual(
                bernoulli_posterior_plus([1] * n), 1 - min_error,
            )
            self.assertEqual(bernoulli_posterior_plus([0] * n), min_error)
            for mask in range(1 << n):
                bits = [(mask >> i) & 1 for i in range(n)]
                p = bernoulli_posterior_plus(bits)
                self.assertGreater(p, 0)
                self.assertLess(p, 1)
                self.assertGreaterEqual(min(p, 1-p), min_error)

    def test_log_likelihood_odds_increment_and_validation(self):
        prefix = (1, 0, 1, 0, 1)
        current = bernoulli_posterior_plus(prefix)
        odds = current / (1-current)
        up = bernoulli_posterior_plus(prefix + (1,))
        down = bernoulli_posterior_plus(prefix + (0,))
        self.assertEqual(up / (1-up), 2*odds)
        self.assertEqual(down / (1-down), odds/2)
        for invalid in ((1, 2), (True,), (1.0,), ("1",)):
            with self.assertRaises(CarrierImpedanceError):
                bernoulli_posterior_plus(invalid)
        for invalid in (True, -1, 1001, 1.3):
            with self.assertRaises(CarrierImpedanceError):
                late_witness(invalid)
        with self.assertRaises(CarrierImpedanceError):
            finite_all_zero_prefix([0, 0, 2])


    def test_quantum_hilbert_carrier_no_perfect_finite_discrimination(self):
        import math
        for n in range(1, 41):
            lower, upper = quantum_helstrom_error_bounds(n)
            overlap_squared = Fraction(1, 2**n)
            self.assertGreater(overlap_squared, 0)
            self.assertLess(overlap_squared, 1)
            self.assertGreater(lower, 0)
            self.assertLess(lower, upper)
            # Numerical check is only calibration; positivity is exact
            # from the rational bounds for every supported n.
            error = (2.0**(-n-1)) / (1 + math.sqrt(1 - 2.0**(-n)))
            self.assertLess(float(lower), error)
            self.assertLess(error, float(upper))
        for invalid in (0, -1, 4.1, True):
            with self.assertRaises(CarrierImpedanceError):
                quantum_helstrom_error_bounds(invalid)


if __name__ == "__main__":
    unittest.main()
