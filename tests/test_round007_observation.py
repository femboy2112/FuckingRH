import unittest
from flint import arb
from scripts.round007_observation import scalar_certificate,exact_zero_average_fixture

class ObservationTests(unittest.TestCase):
    def test_unconditional_positive_region(self):
        c=scalar_certificate()
        self.assertTrue(c['interval_inside_log2_log3'])
        self.assertTrue(arb(c['positive_weil_lower_coefficient'])>0)

    def test_zero_average_nonzero_function(self):
        e=exact_zero_average_fixture()
        self.assertEqual(e['average'],0)
        self.assertGreater(e['norm_square'],0)
        self.assertEqual(e['endpoint_values'],(0,0))
        self.assertEqual(e['endpoint_derivatives'],(0,0))

    def test_refining_the_cell_escapes_the_common_kernel(self):
        import sympy as sp
        x=sp.Symbol('x');h=sp.Rational(1,65536)
        b=(x-1)**3*(1+h-x)**3;f=sp.diff(b,x)
        left=sp.integrate(f,(x,1,1+h/2))
        right=sp.integrate(f,(x,1+h/2,1+h))
        self.assertGreater(left,0)
        self.assertLess(right,0)
        self.assertEqual(left+right,0)

if __name__=='__main__':unittest.main()
