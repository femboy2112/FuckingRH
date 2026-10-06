from fractions import Fraction as Q
import unittest
from flint import arb, ctx
from scripts.primitive_projection import old_monoid
from scripts.finite_grid_lift import Event, events_for, uniform_kernel, finite_lift_certificate
from scripts.prime_moment_cone import run


class Round003HostileTests(unittest.TestCase):
    def test_first_two_moments_do_not_determine_inverse_tower_data(self):
        nodes=(2,4,6,8)
        minus=[Q(n,32) for n in (7,11,5,9)]
        plus=[Q(n,32) for n in (9,5,11,7)]
        self.assertTrue(all(old_monoid(n,5) for n in nodes))
        for k in range(3):
            self.assertEqual(sum(w*n**k for w,n in zip(minus,nodes)),
                             sum(w*n**k for w,n in zip(plus,nodes)))
        a=sum(w*Q(5,n) for w,n in zip(minus,nodes))-1
        b=sum(w*Q(5,n) for w,n in zip(plus,nodes))-1
        self.assertNotEqual(a,b)
        for weights in (minus,plus):
            m2=sum(w*Q(5,n) for w,n in zip(weights,nodes))-1
            m4=sum(w*Q(5,n)**2 for w,n in zip(weights,nodes))-1
            self.assertGreater(m4-2*m2,0)

    def test_whole_tower_weight_mutation_is_detected(self):
        with ctx.workprec(180):
            events=events_for(64)
            mutated=[Event(e.location,e.prime,e.weight_denominator,
                           20 if e.prime==3 else e.multiplier) for e in events]
            K,B=uniform_kernel(64,16,mutated)
            result=finite_lift_certificate(K,B)
            self.assertEqual(result['status'],'certified_positive_lift')
            self.assertGreater(Q(result['lower_exact']),0)

    def test_duplicate_event_and_archimedean_mutation_are_detected(self):
        with ctx.workprec(160):
            events=events_for(64)
            K,B=uniform_kernel(64,16,events+[events[0]])
            self.assertEqual(finite_lift_certificate(K,B)['status'],
                             'certified_positive_lift')
            # Change smooth quadratic term A(t)->A(t)-10t^2.
            K,B=uniform_kernel(64,16)
            h=arb(64).log()/16
            mutated=[[K[i][j]-20*(i+1)*(j+1)*h*h for j in range(16)]
                     for i in range(16)]
            self.assertEqual(finite_lift_certificate(mutated,B)['status'],
                             'certified_positive_lift')

    def test_one_level_interval_constructor_and_fresh_boundary(self):
        with ctx.workprec(160):
            records={r['p']:r for r in run(101)['records']}
            self.assertTrue(records[17]['feasible_level1'])
            self.assertFalse(records[19]['feasible_level1'])
            self.assertTrue(all(r['feasible_level1'] for p,r in records.items() if p>=23))


if __name__=='__main__':unittest.main()
