import unittest

from flint import acb, arb, ctx
import sympy as sp

from scripts.round008_gamma import (
    carry_power, carry_step, gamma_multiplier, gamma_multiplier_cutoff,
    gamma_multiplier_tail_bound, heat_hankel, helical_heat_trace,
    hurwitz_ladder_determinant, ladder_determinant, relative_det2,
)


class GammaAndAffineTests(unittest.TestCase):
    def test_hurwitz_determinant_and_recurrence(self):
        with ctx.workdps(60):
            for s in (acb(arb(1)/2), acb(2), acb(arb(7)/3, 2), acb(1, 9)):
                d = ladder_determinant(s)
                self.assertTrue((d-hurwitz_ladder_determinant(s)).contains(0))
                self.assertTrue((s*ladder_determinant(s+2)-d).contains(0))
            self.assertTrue((ladder_determinant(2)-arb.pi().sqrt()).contains(0))
            for m in range(6):
                self.assertTrue(ladder_determinant(-2*m).is_zero())

    def test_gamma_cutoff_positive_tail(self):
        with ctx.workdps(60):
            for v, modes in ((1, 2), (3, 8), (17, 32), (100, 128)):
                tail = gamma_multiplier(v)-gamma_multiplier_cutoff(v, modes)
                upper = gamma_multiplier_tail_bound(v, modes)
                self.assertTrue(tail > 0)
                self.assertTrue(upper-tail > 0)
                # Shifted digamma checks the independently summed rational terms.
                a = arb(modes)+arb(1)/4
                exact_tail = acb(a, arb(v)/2).digamma().real-a.digamma()
                self.assertTrue((tail-exact_tail).contains(0))

    def test_relative_det2_normalization_and_product_tail(self):
        with ctx.workdps(60):
            s, base = arb(3), arb(1)
            target = relative_det2(s, base).real
            zeta_ratio = ladder_determinant(s)/ladder_determinant(base)
            corrected = zeta_ratio*(((s-base)/2)*(arb(2).log()+(base/2).digamma())).exp()
            self.assertTrue((relative_det2(s, base)-corrected).contains(0))
            modes = 64
            log_product = arb(0)
            for m in range(modes):
                x = (s-base)/(2*m+base)
                log_product += (1+x).log()-x
            omitted_log = log_product-target.log()
            a = 2*modes+base
            bound = (s-base)**2/2*(1/a**2+1/(2*a))
            self.assertTrue(omitted_log > 0)
            self.assertTrue(bound-omitted_log > 0)

    def test_gaussian_mellin_and_log_vector_norm(self):
        x, sigma = sp.symbols('x sigma', positive=True)
        mellin = sp.integrate(sp.exp(-sp.pi*x*x)*x**(sigma-1), (x, 0, sp.oo))
        self.assertEqual(sp.simplify(mellin-sp.gamma(sigma/2)/(2*sp.pi**(sigma/2))), 0)
        norm = sp.integrate(sp.exp(-2*x)*x**(2*sigma-1), (x, 0, sp.oo))
        self.assertEqual(sp.simplify(norm-sp.gamma(2*sigma)/2**(2*sigma)), 0)

    def test_positive_heat_gram_and_sharp_mode_rank(self):
        for n in range(1, 8):
            pts = [sp.Rational(1, 2**i) for i in range(1, n+1)]
            full = heat_hankel(pts)
            finite = heat_hankel(pts, n)
            self.assertGreater(full.det(), 0)
            self.assertGreater(finite.det(), 0)
            self.assertEqual(heat_hankel(pts, n-1).rank(), n-1)
            # Cauchy determinant; an exact formula separate from the Gram sum.
            product = sp.prod((pts[j]-pts[i])**2
                for i in range(n) for j in range(i+1, n))
            product /= sp.prod(1-x*y for x in pts for y in pts)
            self.assertEqual(full.det(), product)

    def test_gamma_mode_energy_integral(self):
        lam, v = sp.symbols('lam v', positive=True)
        u = sp.symbols('u', nonnegative=True)
        integral = sp.integrate(2*sp.exp(-lam*u)*(1-sp.cos(v*u)), (u, 0, sp.oo))
        self.assertEqual(sp.simplify(integral-2*v*v/(lam*(lam*lam+v*v))), 0)

    def test_unitary_normalization_and_opposite_local_jacobians(self):
        a, gamma = sp.symbols('a gamma', positive=True)
        self.assertEqual(sp.simplify(a*a**(-2*gamma)).subs(gamma, sp.Rational(1, 2)), 1)
        for p, k in ((2, 1), (3, 2), (5, 3)):
            q = sp.Integer(p)**k
            real_overlap = q**(-sp.Rational(1, 2))*1
            padic_overlap = q**(sp.Rational(1, 2))/q
            self.assertEqual(real_overlap, padic_overlap)
            self.assertEqual(q**(-sp.Rational(1, 2))*q**sp.Rational(1, 2), 1)
            self.assertNotEqual(q**(-sp.Rational(1, 2)), q**sp.Rational(1, 2))

    def test_lie_bracket_and_oscillator_translation(self):
        x, a = sp.symbols('x a', real=True)
        f = sp.Function('f')(x)
        P = lambda g: -sp.I*sp.diff(g, x)
        D = lambda g: -sp.I*(x*sp.diff(g, x)+g/2)
        H = lambda g: -sp.diff(g, x, 2)+(x*x-1)*g
        self.assertEqual(sp.simplify(D(P(f))-P(D(f))-sp.I*P(f)), 0)
        shift = lambda g: g.subs(x, x-a)
        self.assertEqual(sp.simplify(H(shift(f))-shift(H(f))-(2*a*x-a*a)*shift(f)), 0)

    def test_carry_cocycle_matches_iterated_steps(self):
        for L in (1, 2, 6, 12, 60):
            for r in range(L):
                pair = (r, -3)
                for k in range(2*L+1):
                    self.assertEqual(pair, carry_power(L, r, -3, k))
                    self.assertEqual(L*pair[1]+pair[0], L*(-3)+r+k)
                    pair = carry_step(L, *pair)
                self.assertEqual(carry_power(L, r, 0, L), (r, 1))

    def test_mehler_trace_complete_square(self):
        x, a, r = sp.symbols('x a r', real=True)
        y = x-a
        exponent = -((1+r*r)*(x*x+y*y)-4*r*x*y)/(2*(1-r*r))
        normal = -(1-r)/(1+r)*(x-a/2)**2-a*a*(1+r)/(4*(1-r))
        self.assertEqual(sp.factor(exponent-normal), 0)
        with ctx.workdps(50):
            for L in (2, 6, 12):
                t = arb(3)/5
                base = L/(1-(-2*t).exp())
                self.assertTrue((helical_heat_trace(L, 0, t)-base).contains(0))
                self.assertTrue(helical_heat_trace(L, 1, t).is_zero())
                coupled = helical_heat_trace(L, L, t)
                self.assertTrue(coupled > 0)
                self.assertTrue(base-coupled > 0)


if __name__ == '__main__':
    unittest.main()
