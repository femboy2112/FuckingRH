"""Independent exact/interval controls for the Round003 moment-cone audit.

Universal claims are proved in reviews/MOMENT_ADVERSARY.md. These tests
check their algebra and finite threshold witnesses, not RH or asymptotics.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import factorial
import unittest

from flint import arb, ctx
from sympy import factor, isprime, symbols


def rising(x, n):
    value = Q(1)
    for j in range(n):
        value *= x + j
    return value


def midpoint_radii(p):
    return [d for d in range(1, p) if not isprime(p+d)]



def half_defect_exact_input(p, d):
    return ((arb(p)/arb(p-d)).sqrt() + (arb(p)/arb(p+d)).sqrt())/2-1


class Round003MomentAdversaryTests(unittest.TestCase):
    def test_pointwise_dual_identity_is_exact_for_rational_levels(self):
        # Three endpoints with weights 1/4,1/2,1/4 and center 5.
        nodes = (Q(2), Q(5), Q(8))
        weights = (Q(1, 4), Q(1, 2), Q(1, 4))
        self.assertEqual(sum(w*n for w,n in zip(weights,nodes)), 5)
        z = [Q(5)/n for n in nodes]
        m2 = sum(w*a for w,a in zip(weights,z))-1
        m4 = sum(w*a*a for w,a in zip(weights,z))-1
        self.assertEqual(m4-2*m2,
                         sum(w*(a-1)**2 for w,a in zip(weights,z)))
        self.assertGreater(m2, 0)
        self.assertGreater(m4-2*m2, 0)
        # This separating functional has negative value at target (1,1).
        self.assertLess(Q(1)-2*Q(1), 0)

    def test_midpoint_coefficient_ratios_give_exact_separators(self):
        for k,l in ((1,2), (2,4), (3,7)):
            ratios=[]
            for j in range(1, 13):
                ak=rising(Q(k,2),2*j)/factorial(2*j)
                al=rising(Q(l,2),2*j)/factorial(2*j)
                ratios.append(al/ak)
            self.assertEqual(ratios[0], Q(l*(l+2), k*(k+2)))
            self.assertTrue(all(a<b for a,b in zip(ratios, ratios[1:])))
        u=Q(2,5)
        g2=((1-u)**-1+(1+u)**-1)/2-1
        g4=((1-u)**-2+(1+u)**-2)/2-1
        self.assertEqual(g4-3*g2, 2*u**4/(1-u*u)**2)
        self.assertGreater(g4-3*g2, 0)

    def test_bounded_support_tangent_remainders_factor_exactly(self):
        y=symbols('y', positive=True)
        r1=1/y-1+(y*y-1)/2
        r2=1/y**2-1+(y*y-1)
        self.assertEqual(factor(r1-(y-1)**2*(y+2)/(2*y)), 0)
        self.assertEqual(factor(r2-(y-1)**2*(y+1)**2/y**2), 0)
        self.assertEqual(factor(r2-(2+2/(y*(y+2)))*r1), 0)
        self.assertEqual(factor((2+2/(y*(y+2))).diff(y)
                                +4*(y+1)/(y**2*(y+2)**2)), 0)
        with ctx.workprec(150):
            boundary=2+2/(arb(2).sqrt()*(arb(2).sqrt()+2))
            self.assertTrue(boundary.overlaps(1+arb(2).sqrt()))

    def test_deviation_coupling_reconstructs_three_endpoint_cell(self):
        # p=7, old-generated endpoints 2,6,12. Mean is exactly 7.
        p=Q(7)
        atoms={Q(2):Q(1,5), Q(6):Q(1,2), Q(12):Q(3,10)}
        self.assertEqual(sum(n*w for n,w in atoms.items()),p)
        upper=Q(12)
        reconstructed={n:Q(0) for n in atoms}
        total=Q(0)
        for a in (Q(2),Q(6)):
            beta=atoms[a]*(p-a)
            theta=beta*(upper-a)/((p-a)*(upper-p))
            total+=theta
            reconstructed[a]+=theta*(upper-p)/(upper-a)
            reconstructed[upper]+=theta*(p-a)/(upper-a)
        self.assertEqual(total,1)
        self.assertEqual(reconstructed,atoms)

    def test_first_level_threshold_is_not_monotone_in_small_primes(self):
        with ctx.workprec(160):
            results={}
            for p in (3,5,7,11,13,17,19,23):
                d=max(midpoint_radii(p))
                low=half_defect_exact_input(p,1)
                high=half_defect_exact_input(p,d)
                self.assertTrue(low<1)
                self.assertTrue(high<1 or high>1)
                results[p]=bool(high>1)
                self.assertEqual(d,p-2 if isprime(2*p-1) else p-1)
            self.assertEqual(results,{3:False,5:False,7:False,11:True,
                                      13:True,17:True,19:False,23:True})
            threshold=(111-arb(33).sqrt())/128
            self.assertTrue((arb(21)/23)**2>threshold)
            # This exact integer ratio increases for p>=23, proving the tail
            # criterion analytically; no prime-prefix extrapolation is used.

    def test_even_level_thresholds_use_exact_rational_defects(self):
        for p in (3,5,7,11,19):
            u=Q(max(midpoint_radii(p)),p)
            g2=u*u/(1-u*u)
            g4=u*u*(3-u*u)/(1-u*u)**2
            self.assertEqual(g2>=1,p>=5)
            self.assertEqual(g4>=1,p>=5)
        # The lower-bound condition is necessary for high levels.
        u=Q(1,3)
        g8=((1-u)**-4+(1+u)**-4)/2-1
        self.assertGreater(g8,1)

    def test_deletion_rearrangement_bound_uses_distinct_integers(self):
        with ctx.workprec(128):
            for n in (1,2,3,4):
                maximal=sum(1/arb(m).sqrt() for m in range(1,n+1))
                self.assertTrue(maximal<2*arb(n).sqrt())
                for subset in combinations(range(1,8),n):
                    value=sum(1/arb(m).sqrt() for m in subset)
                    if subset==tuple(range(1,n+1)):
                        self.assertTrue(value.overlaps(maximal))
                    else:
                        self.assertTrue(value<maximal)


    def test_log_jet_separator_handles_actual_negative_defects(self):
        # p=3, old-generated endpoints 2 and 4, equal masses, levels 2,4.
        # a0=log(2)/log(3)<2/3 follows from the exact integer inequality.
        self.assertLess(2**3, 3**2)
        a0=symbols('a0', positive=True)
        m2=Q(3,2)*a0-1
        m4=Q(27,16)*a0-1
        power_remainder=Q(3,16)*a0
        log_jensen_remainder=1-Q(3,2)*a0
        self.assertEqual(factor(m4-2*m2-power_remainder-log_jensen_remainder),0)
        self.assertEqual(factor(m4-2*m2-(1-Q(21,16)*a0)),0)
        self.assertEqual(Q(1)-Q(21,16)*Q(2,3),Q(1,8))
        with ctx.workprec(160):
            a=arb(2).log()/arb(3).log()
            self.assertTrue(3*a/2-1<0)
            self.assertTrue(1-21*a/16>arb(1)/8)


    def test_three_log_weight_levels_have_exact_positive_variance_obstruction(self):
        # Normalize out C=log3. Positive a_n=c_n logn/C on old nodes2,4
        # match levels2,4 exactly but necessarily overproduce level6.
        atoms={2:Q(2,9),4:Q(8,9)}
        moments={k:sum(a*Q(1,n)**(k//2) for n,a in atoms.items())
                 for k in (2,4,6)}
        self.assertEqual(moments[2],Q(1,3))
        self.assertEqual(moments[4],Q(1,9))
        self.assertEqual(moments[6],Q(1,24))
        self.assertGreater(moments[6],Q(1,27))
        self.assertEqual(moments[2]*moments[6]-moments[4]**2,Q(1,648))
        rho={n:a*Q(1,n)/moments[2] for n,a in atoms.items()}
        self.assertEqual(sum(rho.values()),1)
        self.assertEqual(sum(w*Q(1,n) for n,w in rho.items()),Q(1,3))
        variance=sum(w*(Q(1,n)-Q(1,3))**2 for n,w in rho.items())
        self.assertEqual(variance,Q(1,72))
        delta=Q(1,3)-Q(1,4)
        dual=lambda m: m[6]-2*Q(1,3)*m[4]+(Q(1,9)-delta**2)*m[2]
        self.assertGreater(dual(moments),0)
        self.assertEqual(dual({k:Q(1,3)**(k//2) for k in (2,4,6)}),
                         -delta**2/3)


if __name__ == '__main__':
    unittest.main()
