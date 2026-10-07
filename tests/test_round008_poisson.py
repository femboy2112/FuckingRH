import unittest

import sympy as sp
from flint import arb, ctx

from scripts.round008_poisson import (
    apply_rational, conductor_mask, conductor_projector, dual_injection_unscaled,
    fourier, gaussian_norm, pullback, refinement_character_checks,
    root_sum_remainder, theta, theta_refinement, theta_residual, packet_residual,
)


class FinitePoissonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ctx.prec = 192

    def test_exact_haar_refinement_and_dual_isometries(self):
        for L,M in [(1,2),(2,6),(4,12),(6,30),(10,60)]:
            r=M//L
            I=pullback(L,M)
            E=dual_injection_unscaled(L,M)
            self.assertEqual(I.T*I,r*sp.eye(L))
            self.assertEqual(E.T*E,sp.eye(L))
            self.assertTrue(refinement_character_checks(L,M))

    def test_exact_character_orthogonality(self):
        for L in [1,2,6,10,12]:
            for k in range(L):
                self.assertEqual(root_sum_remainder(L,[a*k for a in range(L)]).as_expr(),
                                 L if k==0 else 0)

    def test_naive_same_embedding_fails_exactly(self):
        for L,M in [(1,2),(2,6),(6,30)]:
            I=pullback(L,M)
            fL=sp.sqrt(L)*sp.eye(L)[:,0]
            fM=sp.sqrt(M)*sp.eye(M)[:,0]
            diff=fM-I*fL
            self.assertEqual(sp.simplify((diff.T*diff)[0]/M),
                             sp.simplify(2-2/sp.sqrt(M//L)))

    def test_conductor_projectors_and_no_proper_fourier_invariance(self):
        for L,ds in [(6,[1,2,3]),(12,[1,2,4]),(10,[5,10])]:
            P=conductor_projector(L,ds)
            Q=conductor_mask(L,ds)
            self.assertEqual(P*P,P)
            self.assertEqual(P.T,P)
            self.assertEqual(P.trace(),Q.trace())
            self.assertNotEqual(P,Q)
            self.assertTrue(0<P.trace()<L)

    def test_interval_theta_self_duality_holdouts(self):
        for L,t in [(1,arb(2)),(6,arb(3)/2),(12,arb(2)/7),(30,arb(7)/3)]:
            self.assertTrue(all(x.contains(0) for x in theta_residual(L,t)))

    def test_interval_refinement_requires_real_rescaling(self):
        for L,M,t in [(2,6,arb(5)/3),(6,30,arb(3)/2)]:
            coarse,dual=theta_refinement(L,M,t)
            self.assertTrue(all(x.contains(0) for x in coarse+dual))
            bad=theta(M,t)[0]-theta(L,t)[0]
            self.assertFalse(bad.contains(0))

    def test_mutations_fail_certifiably(self):
        L,t=6,arb(3)/2
        v,d=theta(L,t),theta(L,1/t)
        wrong=[x-y/t.sqrt() for x,y in zip(fourier(v,False),d)]
        self.assertTrue(any(not x.contains(0) for x in wrong))
        P=conductor_projector(L,[1,2,3])
        dropped=[x-y/t.sqrt() for x,y in zip(fourier(apply_rational(P,v)),
                                            apply_rational(P,d))]
        self.assertTrue(any(not x.contains(0) for x in dropped))
        badmesh=[x-y/t.sqrt() for x,y in zip(fourier(theta(L,L*t)),theta(L,L/t))]
        self.assertTrue(any(not x.contains(0) for x in badmesh))

    def test_gaussian_norm_calibration_not_universal_claim(self):
        target=1/arb(2).sqrt()
        self.assertTrue(abs(gaussian_norm(30)-target)<arb('1e-18'))
        self.assertTrue(gaussian_norm(1)-target>arb('0.1'))

    def test_gaussian_mellin_normalization_symbolically(self):
        t,s,n,L=sp.symbols('t s n L', positive=True)
        actual=sp.integrate(sp.exp(-sp.pi*t*n*n/L)*t**(s/2-1),(t,0,sp.oo))
        expected=sp.pi**(-s/2)*sp.gamma(s/2)*L**(s/2)*n**(-s)
        self.assertEqual(sp.simplify(actual-expected),0)

    def test_phase_sensitive_schwartz_holdout_and_sign_mutation(self):
        args=(6,arb(3)/2,arb(1)/3,arb(2)/5)
        self.assertTrue(all(x.contains(0) for x in packet_residual(*args)))
        self.assertTrue(any(not x.contains(0) for x in packet_residual(*args,True)))


if __name__ == "__main__":
    unittest.main()
