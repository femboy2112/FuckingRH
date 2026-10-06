"""Exact controls for the adelic/computation comparison; no zero input."""
from fractions import Fraction as Q
import unittest
import sympy as sp


class AdelicComparisonTests(unittest.TestCase):
    def test_half_density_degree_tent_integral_is_not_identity_evaluation(self):
        t = sp.symbols('t', positive=True)
        x = sp.symbols('x', real=True)
        integral = sp.integrate((t-x)*sp.cosh(x/2), (x, 0, t))
        self.assertEqual(sp.simplify(integral-4*(sp.cosh(t/2)-1)), 0)
        self.assertEqual(sp.simplify(sp.diff(2*integral, t, 2)-2*sp.cosh(t/2)), 0)
        self.assertEqual(sp.diff(t/2, t, 2), 0)

    def test_brownian_common_mode_is_not_a_radical(self):
        points = (Q(1), Q(2))
        matrix = [[abs(s)+abs(u)-abs(s-u) for u in points] for s in points]
        self.assertEqual(matrix, [[2, 2], [2, 4]])
        self.assertEqual(matrix[0][0]*matrix[1][1]-matrix[0][1]**2, 4)

    def test_both_nonzero_tower_quotient_signs_have_positive_lifts(self):
        r, c = sp.symbols('r c', real=True)
        den = 1-2*r*c+r*r
        phase = (r*c-r*r)/den
        minus = r/(1-r)-phase
        plus = r/(1+r)+phase
        self.assertEqual(sp.factor(minus-r*(1+r)*(1-c)/((1-r)*den)), 0)
        self.assertEqual(sp.factor(plus-r*(1-r)*(1+c)/((1+r)*den)), 0)
        # Nontriviality modulo |t|: a single ramp is zero before its
        # first event and strictly positive immediately afterward.
        ell, r0 = Q(2), Q(1, 2)
        self.assertEqual(ell*r0*max(Q(0), ell/2-ell), 0)
        self.assertGreater(ell*r0*max(Q(0), 3*ell/2-ell), 0)

    def test_canonical_semilocal_metric_increment_has_both_signs(self):
        for r in (Q(1, 2), Q(2, 3), Q(4, 5)):
            self.assertLess(r*r-2*r, 0)  # cos(theta)=1
            self.assertGreater(r*r+2*r, 0)  # cos(theta)=-1
            self.assertEqual(1+r*r-2*r, (1-r)**2)
            for c in (Q(-1), Q(0), Q(1)):
                self.assertGreaterEqual(1+r*r-2*r*c, (1-r)**2)

    def test_same_endpoint_action_arrows_forget_history(self):
        def compose(path):
            value = Q(1)
            for q in path:
                value *= q
            return value
        histories = ((Q(2), Q(3)), (Q(3), Q(2)), (Q(2), Q(1, 2), Q(6)))
        self.assertEqual(len(set(histories)), 3)
        self.assertEqual({compose(path) for path in histories}, {Q(6)})
        # A nonzero component cancels, so no distinct rational label
        # can act identically on that component.
        a = Q(7, 11)
        labels = (Q(2), Q(3), Q(6))
        self.assertEqual(len({q*a for q in labels}), len(labels))

    def test_product_formula_jet_cancellation_keeps_quadratic_energy(self):
        ell = sp.symbols('ell', nonzero=True, real=True)
        self.assertEqual(ell-ell, 0)
        self.assertEqual(ell**2+(-ell)**2, 2*ell**2)

    def test_euler_log_bookkeeping_supplies_inverse_tower_level(self):
        s, ell = sp.symbols('s ell', positive=True)
        for k in (1, 2, 3, 7):
            term = sp.exp(-k*ell*s)/k
            self.assertEqual(sp.simplify(-sp.diff(term, s)-ell*sp.exp(-k*ell*s)), 0)


if __name__ == '__main__':
    unittest.main()
