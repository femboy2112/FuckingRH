"""Independent Gamma-continuum calibration, not RH positivity."""
import unittest
import mpmath as mp
from scripts.gamma_arch_continuum import (
    arch_symbol, compensated_symbol, levy_density, fake_source_control,
)


class GammaContinuousHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps=40

    def test_compensated_levy_equals_digamma(self):
        a0=arch_symbol(0)
        for t in (0, mp.mpf('.25'), 1, 3, 10):
            self.assertLess(abs(compensated_symbol(t)-(arch_symbol(t)-a0)),
                            mp.mpf('1e-16'))

    def test_positive_density_singular_but_integrable_after_compensation(self):
        for u in (mp.mpf('1e-6'),mp.mpf('.01'),1,10):
            self.assertGreater(levy_density(u),0)
        self.assertAlmostEqual(float(levy_density(mp.mpf('1e-8'))*mp.mpf('1e-8')), .5, places=7)

    def test_fake_six_source_does_not_turn_into_a_primitive_prime_event(self):
        for delta in (mp.mpf('0'),mp.mpf('.02')):
            direct,sos=fake_source_control(delta)
            self.assertLess(abs(direct-sos),mp.mpf('1e-35'))
        self.assertLess(fake_source_control(mp.mpf('.02'))[0],0)

    def test_positive_arch_defect_but_negative_base(self):
        self.assertLess(arch_symbol(0),0)
        for t in (mp.mpf('.5'),1,3,10):
            self.assertGreater(compensated_symbol(t),0)


if __name__=='__main__':unittest.main()
