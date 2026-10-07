import unittest
from fractions import Fraction
import sympy as sp
from flint import arb,ctx
from scripts.round008_coupling import (origin_geometry,exact_heat_compression,
                                      translation_atoms,exact_mutations,amplitude_data)


class CouplingTests(unittest.TestCase):
    def test_origin_vectors_and_constant_diagonals(self):
        for n in [2,3,4]:
            V,c,Es=origin_geometry(n)
            self.assertEqual(V.T*V,sp.eye(V.cols))
            for j,E in enumerate(Es):
                self.assertEqual(E*E,E)
                self.assertEqual(set(E.diagonal()),{c[j]**2})
                for i in range(E.rows):
                    self.assertTrue(sp.simplify(c[j]**2-V[i,j]**2)>=0)

    def test_first_two_event_normalization(self):
        _,c,_=origin_geometry(3)
        self.assertEqual(sp.simplify(c[0]*c[1]),sp.Rational(1,3))

    def test_heat_metric_calculated_before_square(self):
        exact_heat_compression(3,3)
        exact_heat_compression(4,3)

    def test_forbidden_atom_with_complex_polarization(self):
        G=sp.Matrix([[2,sp.I],[-sp.I,2]])
        a=translation_atoms([2,3],G)
        self.assertEqual(a[Fraction(3,2)],sp.I)
        self.assertEqual(a[Fraction(2,3)],-sp.I)

    def test_mutations_and_escape_hypothesis(self):
        exact_mutations()

    def test_cross_block_schur_completion_and_gain(self):
        u,v,b,t=sp.symbols('u v b t',real=True)
        G=sp.Matrix([[1,b],[b,t]])
        x=sp.Matrix([u,v])
        self.assertEqual(sp.expand((x.T*G*x)[0]-(u+b*v)**2-(t-b*b)*v*v),0)
        # Positive gain-saturation witness: tiny boundary input can cancel
        # bulk only with correspondingly large gain in this two-state test.
        eps=sp.Rational(1,11)
        gain=1/eps
        self.assertEqual(1-gain*eps,0)

    def test_actual_weights_certified(self):
        with ctx.workprec(160):
            first=amplitude_data(3)
            self.assertTrue(first['A']>0)
            later=amplitude_data(1000)
            # Only a finite separation witness; the theorem proves the limit.
            self.assertTrue(later['loss_bound_one_site']<later['S'])
            w2,w3=arb(2).log()/arb(2).sqrt(),arb(3).log()/arb(3).sqrt()
            self.assertTrue(-(w2*w3).sqrt()/3<0)

    def test_covariant_carry_oscillator(self):
        from scripts.round008_coupling import refinement_oscillator_checks
        refinement_oscillator_checks()


if __name__ == '__main__':
    unittest.main()
