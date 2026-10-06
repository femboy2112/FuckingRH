import importlib.util
from pathlib import Path
import sys
import unittest
import mpmath as mp

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "suzuki_psi.py"
spec = importlib.util.spec_from_file_location("suzuki_psi", MODULE)
m = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = m
spec.loader.exec_module(m)


class SuzukiPsiBaselineTests(unittest.TestCase):
    def test_origin_and_evenness(self):
        self.assertEqual(m.psi_suzuki(0), 0)
        for t in [0.1, 0.5, 1.0, 2.0]:
            self.assertAlmostEqual(float(m.psi_suzuki(t)), float(m.psi_suzuki(-t)), places=14)

    def test_formula_regression_values(self):
        # Evaluator fixtures, not values claimed to be printed in Suzuki.
        expected = {
            "0.1": "0.05313043381777025410005234409146544",
            "0.5": "0.0401625803820866649861141479969911",
            "1":   "0.0440073052368525268602186064080838",
            "2":   "0.0533411241718556689631189360507922",
        }
        with mp.workdps(50):
            for t, want in expected.items():
                got = m.psi_suzuki(mp.mpf(t), dps=50)
                self.assertLess(abs(got - mp.mpf(want)), mp.mpf("1e-33"))

    def test_wavefront(self):
        # Exact event inclusion cannot be decided from a rounded log(q).
        with mp.workdps(70):
            eps = mp.mpf('1e-60')
            for q in [2, 10]:
                self.assertEqual(m.active_horizon(mp.log(q)-eps), q-1)
                self.assertEqual(m.active_horizon(mp.log(q)+eps), q)

    def test_unsorted_event_input(self):
        events = m.prime_power_events_up_to(10)
        self.assertEqual(m.psi_suzuki('1', events=events),
                         m.psi_suzuki('1', events=reversed(events)))

    def test_screw_precision_is_preserved(self):
        with mp.workdps(70):
            want = 2*m.psi_suzuki('0.1', dps=70)
        got = m.screw_kernel('0.1', '0.1', dps=70)
        with mp.workdps(70):
            self.assertLess(abs(got-want), mp.mpf('1e-65'))


if __name__ == "__main__":
    unittest.main()
