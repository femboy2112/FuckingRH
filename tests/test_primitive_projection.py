from fractions import Fraction as F
import unittest
from scripts.primitive_projection import (dirichlet_log, factors, old_monoid,
    midpoint_distances, even_level_surplus)


class PrimitiveProjectionTests(unittest.TestCase):
    def test_euler_partition_recovers_only_towers(self):
        limit=256
        result=dirichlet_log({n:F(1) for n in range(1,limit+1)},limit)
        expected={}
        for n in range(2,limit+1):
            fs=factors(n)
            if len(fs)==1: expected[n]=F(1,next(iter(fs.values())))
        self.assertEqual(result,expected)

    def test_positive_partition_does_not_imply_positive_primitive(self):
        log=dirichlet_log({1:F(1),2:F(1)},32)
        self.assertEqual(log[2],1)
        self.assertEqual(log[4],F(-1,2))
        self.assertEqual(log[8],F(1,3))

    def test_old_support_cannot_create_new_prime_under_log(self):
        for p in [3,5,7,11]:
            a={n:F(1+(n%3),1) for n in range(2,257) if old_monoid(n,p)}
            a[1]=F(1)
            result=dirichlet_log(a,256)
            self.assertTrue(all(old_monoid(n,p) for n in result))
            self.assertNotIn(p,result)
            if p*p<=256:self.assertNotIn(p*p,result)

    def test_midpoint_count_and_unit_edge_case(self):
        primes=[n for n in range(2,200) if factors(n)=={n:1}]
        self.assertEqual(midpoint_distances(2),[])
        for p in primes:
            bad=sum(factors(q)=={q:1} for q in range(p+1,2*p))
            self.assertEqual(len(midpoint_distances(p)),p-1-bad)
            for d in midpoint_distances(p):
                self.assertEqual((p-d+p+d)//2,p)

    def test_even_moment_dual_separator_exact(self):
        for p in [3,5,7,11,19,101]:
            for d in midpoint_distances(p):
                m2=even_level_surplus(p,d,2)
                m4=even_level_surplus(p,d,4)
                self.assertGreater(m4-2*m2,0)
                self.assertGreater(m4-3*m2,0)  # symmetric sharper ratio k=2,l=4
        # Desired pair (1,1) is on the forbidden side of both separators.
        self.assertLess(F(1)-2*F(1),0)

    def test_old_tensor_moment_mutation_retains_support_not_positivity(self):
        a={1:F(1),2:F(2),3:F(1),6:F(1)}
        result=dirichlet_log(a,36)
        self.assertLess(result[6],0)
        self.assertNotIn(5,result)


if __name__=='__main__':unittest.main()
