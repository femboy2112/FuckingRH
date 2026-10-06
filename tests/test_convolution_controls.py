from fractions import Fraction as F
import importlib.util
from pathlib import Path
import unittest


PATH = Path(__file__).resolve().parents[1] / "scripts" / "convolution_controls.py"
SPEC = importlib.util.spec_from_file_location("convolution_controls", PATH)
c = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(c)


class ConvolutionControls(unittest.TestCase):
    def test_uniform_sum_cdf_recovers_independent_triangle_geometry(self):
        # Two Uniform[-1,1] variables have density (2-|x|)/4.
        self.assertEqual(c.uniform_sum_cdf([F(1), F(1)], F(1)), F(7, 8))
        self.assertEqual(c.uniform_sum_cdf([F(1), F(1)], F(-1)), F(1, 8))

    def test_borwein_support_contact_and_published_post_contact_value(self):
        self.assertEqual(c.borwein_plateau_ratio(F(1), [F(1, 3), F(1, 5)]), F(1))
        self.assertEqual(c.borwein_plateau_ratio(F(1), [F(1, 2), F(1, 2)]), F(1))
        # Basel-Baillie: integral sinc(x)^2 sinc(x/3) dx = 11*pi/24.
        self.assertEqual(c.borwein_plateau_ratio(F(1), [F(1), F(1, 3)]), F(11, 12))

    def test_gaussian_residual_fails_two_point_psd_with_interval_certificate(self):
        for primes, t in [([2], "1"), ([2, 3], "0.2"), ([2, 3, 5, 7], "0.1")]:
            self.assertTrue(c.log_residual_modulus_interval(primes, t) > 0)
            self.assertTrue(c.residual_pd_minor_interval(primes, t) < 0)
        self.assertTrue(c.residual_pd_minor_interval([], "1") == 0)

    def test_two_prime_transport_false_friend(self):
        self.assertEqual((2 ** 2 - 1) * (3 ** 2 - 1), 24)
        self.assertTrue(c.two_prime_gaussian_image_interval(2, 3, "0.1") < 0)

    def test_selfdual_mixture_multiplier_exact_offline_roots_and_reflection(self):
        self.assertEqual(c.gaussian_mixture_multiplier(F(-2)), 0)
        self.assertEqual(c.gaussian_mixture_multiplier(F(-8)), 0)
        for y in [F(1), F(3, 7), F(-3), F(16)]:
            self.assertEqual(c.gaussian_mixture_multiplier(y), c.gaussian_mixture_multiplier(16 / y))
        # Fourier coefficients at dilations 1,16,1/16 are permuted by c/a.
        coefficients = {F(1): F(10), F(16): F(16), F(1, 16): F(1)}
        self.assertEqual({1 / a: weight / a for a, weight in coefficients.items()}, coefficients)
        self.assertEqual(sum(coefficients.values()), 27)
        self.assertEqual(sum(weight / a for a, weight in coefficients.items()), 27)

    def test_functional_symmetry_does_not_exclude_negative_tent_sum(self):
        self.assertTrue(c.synthetic_quartet_at_period_interval("1", "0.25") < 0)
        # The on-line control has cos(2*pi)-1=0 exactly in the closed formula.
        self.assertTrue(c.synthetic_quartet_at_period_interval("1", "0") == 0)

    def test_arbitrary_finite_window_can_hide_negative_tail(self):
        T = F(10)
        for t in [F(-10), F(-3, 7), F(0), F(9), F(10)]:
            self.assertEqual(c.planted_tail(t, T), t * t)
        self.assertEqual(c.planted_tail(2 * T, T), -T * T)

    def test_sign_phases_preserve_variance_but_change_third_cumulant(self):
        # Exact geometric moments at r=1/2 are E K=1, E K^2=3, E K^3=13;
        # hence variance=2 and third central moment=6, independently obtained
        # by differentiating sum r^k=1/(1-r).
        self.assertEqual(c.geometric_cumulants_exact(F(1, 2)), (F(1), F(2), F(6)))
        plus = c.geometric_cumulants_exact(F(1, 2), F(3))
        minus = c.geometric_cumulants_exact(F(1, 2), F(-3))
        self.assertEqual(plus[1], minus[1])
        self.assertEqual(plus[2], -minus[2])
        self.assertNotEqual(plus[2], minus[2])


if __name__ == "__main__":
    unittest.main()
