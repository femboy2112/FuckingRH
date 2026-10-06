import unittest
from scripts.successor_geometry import (one, succ, add, mul, add_steps,
    mul_steps, frontiers, Edge, reduce_history, action, finite_arrow, compose_finite)


class SuccessorGeometryTests(unittest.TestCase):
    def test_small_step_counts_independent_of_recurrence(self):
        for n in range(9):
            for m in range(9):
                self.assertEqual(add_steps(n,m), (n+m,m,m+1))
                self.assertEqual(mul_steps(n,m), (n*m,n*m,n*m+2*m+1))

    def test_description_compression_pays_execution(self):
        p=one()
        for _ in range(3): p=succ(p)
        square=mul(p,p)
        self.assertEqual((square.value,square.work,square.length),(16,24,9))
        direct=one()
        for _ in range(15): direct=succ(direct)
        self.assertLess(square.length,direct.length)
        self.assertGreater(square.work,direct.work)

    def test_pareto_contains_geodesic_and_compressed_tradeoff(self):
        fs=frontiers(32)
        for n,ps in fs.items():
            self.assertTrue(all(p.work>=n for p in ps))
            self.assertTrue(any(p.work==n for p in ps))
            for p in ps:
                self.assertFalse(any(q!=p and q.length<=p.length and
                    q.work<=p.work and q.control<=p.control for q in ps))
        self.assertTrue(any(p.length<32 and p.work>32 for p in fs[32]))

    def test_operand_orientation_is_recorded(self):
        a=one(); b=succ(succ(one()))
        self.assertEqual(add(a,b).value,add(b,a).value)
        self.assertNotEqual(add(a,b).work,add(b,a).work)

    def test_groupoid_signed_cocycle_and_nontrivial_loop(self):
        e=Edge('direct',0,4,4,4,4)
        f=Edge('two_plus_two',0,4,6,8,5)
        loop=((f,1),(e,-1))
        self.assertEqual(action(loop),(2,4,1))
        self.assertEqual(action(((e,1),(e,-1))),(0,0,0))
        self.assertEqual(reduce_history(((e,1),(e,-1))),())
        self.assertEqual(len(reduce_history(loop)),2)
        self.assertEqual(action(((f,-1),)),tuple(-x for x in action(((f,1),))))

    def test_bad_histories_are_rejected(self):
        e=Edge('a',0,1,1,1,1); f=Edge('b',2,3,1,1,1)
        with self.assertRaises(ValueError): reduce_history(((e,1),(f,1)))
        with self.assertRaises(ValueError): reduce_history(((e,0),))
        with self.assertRaises(ValueError): reduce_history(((e,1),(e,-1),(f,1)))

    def test_finite_history_quotient_retains_only_residue(self):
        e=Edge('two_plus_two',0,4,6,8,5)
        a=finite_arrow(0,4,((e,1),))
        b=finite_arrow(4,0,((e,-1),))
        self.assertEqual(compose_finite(a,b),(0,0,(0,0,0)))
        self.assertEqual(a[2],(2,1,5))
        with self.assertRaises(ValueError):finite_arrow(0,3,((e,1),))


if __name__=='__main__': unittest.main()
