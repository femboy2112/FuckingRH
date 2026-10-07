import unittest
import sympy as sp
from flint import arb, ctx
from scripts.round008_transfer import (events, refinement_data, exact_boundary_checks,
                                      local_factor, mixed_product, controls)


class TransferTests(unittest.TestCase):
    def test_lcm_birth_schedule_and_dimensions(self):
        self.assertEqual(events(10), [(2,2,1),(3,3,1),(4,2,2),(5,5,1),(7,7,1),(8,2,3),(9,3,2)])
        length, rows = refinement_data(20)
        self.assertEqual(length, sp.ilcm(*range(1,21)))
        self.assertEqual(sum(row[4] for row in rows), length-1)

    def test_resolvent_rank_one_and_refinement(self):
        exact_boundary_checks()

    def test_local_telescope(self):
        x = sp.Symbol('x')
        for p in [2,3,5]:
            product = sp.prod(local_factor(x,p,k) for k in range(1,4))
            self.assertEqual(sp.cancel(product-(1-x**(p**3))/(1-x)), 0)

    def test_full_infinite_product_not_zeta(self):
        with ctx.workprec(160):
            value, tail = mixed_product(7,2)
            self.assertTrue(value*tail.exp() < arb.pi()**2/6)

    def test_mutations_and_nonlinear_escape(self):
        controls()
        g = sp.Symbol('g')
        from scripts.round008_transfer import refine_green
        for p in [2,3,5]:
            self.assertEqual(sp.cancel(1+1/refine_green(g,p)-(1+1/g)**p), 0)

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):
            events(0)
        with self.assertRaises(ValueError):
            mixed_product(10,0)


if __name__ == '__main__':
    unittest.main()
