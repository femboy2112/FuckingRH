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

    def test_published_formula_sanity_values(self):
        expected = {
            "0.1": "0.0531304338177702547603246599777518",
            "0.5": "0.0401625803820866649861141479969911",
            "1":   "0.0440073052368525268602186064080838",
            "2":   "0.0533411241718556689631189360507922",
        }
        with mp.workdps(50):
            for t, want in expected.items():
                got = m.psi_suzuki(mp.mpf(t), dps=50)
                self.assertLess(abs(got - mp.mpf(want)), mp.mpf("1e-33"))

    def test_wavefront(self):
        self.assertEqual(m.active_horizon(mp.log(2)), 2)
        self.assertEqual(m.active_horizon(mp.log(10)), 10)


if __name__ == "__main__":
    unittest.main()
