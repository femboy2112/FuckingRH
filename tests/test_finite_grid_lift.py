import unittest
from fractions import Fraction
from flint import arb,ctx
from sympy import Matrix,Rational
from scripts.finite_grid_lift import (Event,canonical_times,events_for,exact_null_reduction,finite_lift_certificate,finite_lift_rational,psi_uniform_values,uniform_kernel)

class FiniteGridLiftTests(unittest.TestCase):
    def setUp(self):
        self.old=ctx.prec; ctx.prec=180
    def tearDown(self): ctx.prec=self.old

    def test_zero_and_duplicate_times_are_exactly_quotiented(self):
        self.assertEqual(canonical_times([0,'1/3',1,'1/3',0]),([Fraction(1,3),Fraction(1)],[None,0,1,0,None]))
        with self.assertRaises(ValueError): canonical_times([-1])

    def test_brownian_covariance_has_full_grid_rank(self):
        times=[Rational(1,7),Rational(3,5),Rational(11,4)]
        B=Matrix([[2*min(x,y) for y in times] for x in times])
        C=Matrix([[int(j<=i) for j in range(3)] for i in range(3)])
        steps=[times[0],times[1]-times[0],times[2]-times[1]]
        self.assertEqual(B,2*C*Matrix.diag(*steps)*C.T)
        self.assertEqual(B.rank(),3)
        self.assertEqual(B.det(),8*steps[0]*steps[1]*steps[2])

    def test_null_coupling_is_not_discarded(self):
        r=exact_null_reduction([[0,1],[1,0]],[[1,0],[0,0]])
        self.assertFalse(r['feasible']); self.assertIn('coupling',r['reason'])

    def test_negative_and_indefinite_null_blocks(self):
        self.assertFalse(exact_null_reduction([[0,0],[0,-1]],[[1,0],[0,0]])['feasible'])
        self.assertFalse(exact_null_reduction([[0,0,0],[0,0,1],[0,1,0]],[[1,0,0],[0,0,0],[0,0,0]])['feasible'])
        with self.assertRaises(ValueError): exact_null_reduction([[1,0],[0,1]],[[0,1],[1,0]])

    def test_positive_null_block_schur_complement(self):
        r=exact_null_reduction([[1,2],[2,1]],[[1,0],[0,0]])
        self.assertTrue(r['feasible']); self.assertEqual(r['K_reduced'],[[Fraction(-3)]])
        self.assertEqual(r['B_reduced'],[[Fraction(1)]])
        self.assertEqual(exact_null_reduction([[2,2],[2,2]],[[1,1],[1,1]])['rank_B'],1)

    def test_arbitrary_psd_B_complete_lift_path(self):
        self.assertEqual(finite_lift_rational([[0,1],[1,0]],[[1,0],[0,0]])['status'],'no_finite_lift')
        self.assertEqual(finite_lift_rational([[1,1],[1,1]],[[0,0],[0,0]])['status'],'certified_zero_lift')
        result=finite_lift_rational([[1,2],[2,1]],[[1,0],[0,0]])
        self.assertEqual(result['status'],'certified_positive_lift')
        self.assertGreaterEqual(Fraction(result['lower_exact']),Fraction(299,100))
        self.assertGreater(Fraction(result['upper_exact']),3)

    def test_known_lift_and_unambiguous_rayleigh_witness(self):
        K=[[arb(-2),arb(0)],[arb(0),arb(1)]]; B=[[arb(2),arb(0)],[arb(0),arb(2)]]
        r=finite_lift_certificate(K,B)
        self.assertEqual(r['status'],'certified_positive_lift')
        self.assertTrue(arb(r['rayleigh_enclosure']).contains(1))
        self.assertTrue(arb(r['upper'])>1)

    def test_exact_grid_event_equality(self):
        # k log(16)/4=log(2) at k=1: added event contributes exactly zero.
        values,_=psi_uniform_values(16,4,[])
        with_event,_=psi_uniform_values(16,4,[Event(2,2,2,100)])
        self.assertTrue(values[1].overlaps(with_event[1]))
        self.assertTrue(values[2]-with_event[2]>0)

    def test_actual_grid_positive_and_weight_mutation_detected(self):
        K,B=uniform_kernel(64,16)
        self.assertEqual(finite_lift_certificate(K,B)['status'],'certified_zero_lift')
        K,B=uniform_kernel(64,16,events_for(64,'increase_first'))
        self.assertEqual(finite_lift_certificate(K,B)['status'],'certified_positive_lift')

    def test_planted_event_is_invisible_then_negative(self):
        events=events_for(64); planted=events+[Event(65,2,2,10**8)]
        v,_=psi_uniform_values(64,16,events); w,_=psi_uniform_values(64,16,planted)
        self.assertTrue(all(a.overlaps(b) for a,b in zip(v,w)))
        future,_=psi_uniform_values(128,1,planted)
        self.assertTrue(future[-1]<0)

if __name__=='__main__': unittest.main()
