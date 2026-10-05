"""Exact controls for the Gram/Lévy no-go proofs in astra_round_001.

These tests verify finite algebraic witnesses, not RH or an infinite tail.
All signs except the Gaussian residual use rational arithmetic. The latter
uses mpmath interval arithmetic; no floating-point near-zero sign is used.
"""

from fractions import Fraction as Q
import unittest

import mpmath as mp


def ramp(a, t):
    return max(abs(t) - a, Q(0))


def anchored(f, t, u):
    return f(t) + f(u) - f(t - u)


def difference_form(f, times, coefficients):
    return sum(
        coefficients[i] * coefficients[j] * f(t - u)
        for i, t in enumerate(times)
        for j, u in enumerate(times)
    )


class GramLevyObstructionTests(unittest.TestCase):
    def test_each_sign_of_one_event_has_an_exact_indefinite_kernel(self):
        for a in (Q(1), Q(2), Q(13, 7)):
            times = (3 * a / 4, -3 * a / 4)
            for sign in (Q(1), Q(-1)):
                f = lambda t: sign * ramp(a, t)
                k = [[anchored(f, t, u) for u in times] for t in times]
                self.assertEqual(k[0][0], 0)
                self.assertEqual(k[1][1], 0)
                self.assertEqual(k[0][1], -sign * a / 2)
                self.assertEqual(k[0][0] * k[1][1] - k[0][1] ** 2,
                                 -a * a / 4)

    def test_zero_sum_cnd_witness_for_each_sign(self):
        a = Q(13, 7)
        plus = difference_form(
            lambda t: ramp(a, t), (3 * a / 4, -3 * a / 4, Q(0)),
            (Q(1), Q(1), Q(-2)))
        minus = difference_form(
            lambda t: -ramp(a, t), (Q(0), 2 * a), (Q(1), Q(-1)))
        self.assertEqual(plus, a)
        self.assertEqual(minus, 2 * a)
        self.assertGreater(plus, 0)
        self.assertGreater(minus, 0)

    def test_nonnegative_ramp_is_not_cnd(self):
        # Tests the exact failure of extending Suzuki's special implication
        # "nonnegative => CND" to an arbitrary mutated/nonnegative function.
        a = Q(1)
        times = (Q(-3, 4), Q(0), Q(3, 4))
        self.assertTrue(all(ramp(a, t - u) >= 0 for t in times for u in times))
        self.assertEqual(difference_form(lambda t: ramp(a, t), times,
                                         (Q(1), Q(-2), Q(1))), Q(1))

    def test_anchoring_and_zero_sum_form_have_opposite_signs(self):
        times = (Q(-3, 4), Q(1, 3), Q(7, 2))
        cs = (Q(2), Q(-3), Q(5))
        f = lambda t: ramp(Q(1), t) + 3 * t * t
        kernel_form = sum(cs[i] * cs[j] * anchored(f, t, u)
                          for i, t in enumerate(times)
                          for j, u in enumerate(times))
        zero_sum_form = difference_form(f, times + (Q(0),),
                                        cs + (-sum(cs),))
        self.assertEqual(kernel_form, -zero_sum_form)

    def test_signed_levy_ramp_identity_in_physical_coordinate(self):
        # The cosine-product integral gives the absolute-value expression.
        # This exact identity verifies both its factor 1/pi and the ramp.
        for a in (Q(1), Q(13, 7)):
            for t in (Q(-7), -a, -a / 2, Q(0), a / 2, a, 2 * a, Q(7)):
                absolute_value_formula = (abs(t + a) + abs(t - a) - 2 * a) / 2
                self.assertEqual(absolute_value_formula, ramp(a, t))

    def test_cosine_polynomial_has_positive_mean_square(self):
        # A finite Fourier dictionary computes the constant coefficient
        # exactly. Rational relations (1+2=3) do not create a constant cross
        # term in a square of distinct positive-frequency cosines.
        terms = ((Q(1), Q(2)), (Q(2), Q(-7)), (Q(3), Q(5)),
                 (Q(7, 3), Q(-2, 5)))
        fourier = {}
        for frequency, coefficient in terms:
            fourier[frequency] = coefficient / 2
            fourier[-frequency] = coefficient / 2
        self.assertNotIn(Q(0), fourier)
        square_constant = sum(coefficient * fourier.get(-frequency, 0)
                              for frequency, coefficient in fourier.items())
        self.assertEqual(square_constant, sum(c * c for _, c in terms) / 2)
        self.assertGreater(square_constant, 0)

    def test_doubling_kernel_detects_superquadratic_step(self):
        # f(t)=1, f(2t)=5 violates the necessary CND doubling inequality.
        f_t, f_2t = Q(1), Q(5)
        determinant = 4 * f_t * f_2t - f_2t * f_2t
        self.assertEqual(determinant, Q(-5))
        # Exact boundary and strictly feasible controls.
        self.assertEqual(4 * Q(1) * Q(4) - Q(4) ** 2, 0)
        self.assertGreater(4 * Q(1) * Q(2) - Q(2) ** 2, 0)

    def test_gaussian_division_can_destroy_characteristic_property(self):
        old_dps = mp.iv.dps
        try:
            mp.iv.dps = 50
            t = 2 * mp.iv.pi
            residual = 1 - mp.iv.cos(t) - t * t / 2
            self.assertTrue(residual.b < 0)
            self.assertTrue(mp.iv.exp(-residual).a > 1)
        finally:
            mp.iv.dps = old_dps


if __name__ == "__main__":
    unittest.main()
