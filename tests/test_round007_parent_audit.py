import unittest

from flint import acb, arb, ctx
import sympy as sp

from scripts.round007_parent_audit import (
    audit_certificates,
    exact_ldl_inertia,
    finite_completion,
    pole_kernel_decomposition,
    pole_positive_real_kernel,
    von_mangoldt_terms,
)


class ParentAuditTests(unittest.TestCase):
    def test_interval_sign_certificates(self):
        evidence = audit_certificates(60)
        self.assertEqual(evidence["pole_kernel_inertias_positive_negative"]["6"], (1, 5))

    def test_pole_kernel_exact_decomposition_and_inertia(self):
        for n in range(1, 9):
            points = list(range(2, n + 2))
            kernel = pole_positive_real_kernel(points)
            self.assertEqual(kernel, pole_kernel_decomposition(points))
            self.assertEqual(exact_ldl_inertia(kernel), (1, n - 1))

    def test_negative_constant_has_no_cayley_poles_but_many_negative_squares(self):
        s = sp.symbols("s")
        f = sp.Integer(-2)
        cayley = sp.cancel((f - 1) / (f + 1))
        self.assertEqual(cayley, 3)
        self.assertEqual(sp.denom(cayley), 1)
        for n in range(1, 7):
            points = range(1, n + 1)
            kernel = sp.Matrix([[-4 / sp.Rational(s + u - 1) for u in points] for s in points])
            self.assertEqual(exact_ldl_inertia(kernel), (0, n))

    def test_symmetric_entire_control_distinguishes_ratio_from_log_derivative(self):
        s = sp.symbols("s")
        exponent = (s - sp.Rational(1, 2)) ** 2
        self.assertEqual(sp.expand(exponent.subs(s, 1 - s) - exponent), 0)
        self.assertEqual(sp.diff(exponent, s), 2 * s - 1)
        self.assertEqual(sp.expand(exponent - exponent.subs(s, s + 1)), -2 * s)
        # At s=1+i*pi/2, log derivative has positive real part 1,
        # while the shift ratio exp(-2s) equals the negative real -exp(-2).
        point = 1 + sp.I * sp.pi / 2
        self.assertEqual(sp.re((2 * s - 1).subs(s, point)), 1)
        self.assertEqual(sp.exp((-2 * s).subs(s, point)), -sp.exp(-2))

    def test_digamma_series_telescopes_with_correct_resolvent_sign(self):
        for n in (1, 2, 17, 100):
            partial = sum(sp.Rational(1, 2 * j + 2) - sp.Rational(1, 2 * j + 4) for j in range(n))
            self.assertEqual(sp.Rational(1, 2) - partial, sp.Rational(1, 2 * n + 2))
        with ctx.workdps(50):
            self.assertTrue((acb(1).digamma().real / 2 + arb.const_euler() / 2).contains(0))

    def test_prime_power_events_and_removable_finite_completion(self):
        self.assertEqual(von_mangoldt_terms(10), [(2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2), (9, 3)])
        with ctx.workdps(50):
            self.assertTrue(finite_completion(acb(1), 200).is_finite())

    def test_specific_completion_has_certified_near_boundary_negative_gram(self):
        with ctx.workdps(60):
            points = [acb(arb(1) / 2 + arb(1) / 10**8, arb(j) / 1000) for j in range(6)]
            values = [finite_completion(s, 200) for s in points]
            kernel = [[(f + g.conjugate()) / (s + u.conjugate() - 1)
                       for u, g in zip(points, values)] for s, f in zip(points, values)]
            # A Hermitian matrix whose Gershgorin right edges are strictly
            # negative is negative definite. This is an interval certificate.
            for i in range(6):
                right_edge = kernel[i][i].real + sum(abs(kernel[i][j]) for j in range(6) if j != i)
                self.assertTrue(right_edge < 0)


if __name__ == "__main__":
    unittest.main()
