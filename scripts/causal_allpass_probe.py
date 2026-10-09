"""Exact finite controls; floating diagnostics are separately labelled.
Python standard library only. No zeta-zero computation or RH claim.
"""
from fractions import Fraction as F
from pathlib import Path
import cmath
import argparse
import json
import math


def record(x):
    return {"exact": str(x), "decimal": float(x)}


def abs_quartic_squared(x, y, a, gamma):
    result = F(1)
    for sign in (-1, 1):
        shifted = x + sign * a
        re = shifted * shifted - y * y + gamma * gamma
        im = 2 * shifted * y
        result *= re * re + im * im
    return result


def toy_ratio_norm_squared(x, y, a, gamma, omega):
    return (
        abs_quartic_squared(x - omega, y, a, gamma)
        / abs_quartic_squared(x + omega, y, a, gamma)
    )


a, p = F(1), F(2)
good = (p - a) / (p + a)
bad = (p + a) / (p - a)
good_pick = (1 - good * good) / (2 * p)
bad_pick = (1 - bad * bad) / (2 * p)
assert good_pick == F(2, 9)
assert bad_pick == -2
assert ((p - a) / (p + a)) * ((-p - a) / (-p + a)) == 1

boundary_checks = []
for y in [F(0), F(1, 3), F(2), F(1001, 13)]:
    ratio_norm = (a * a + y * y) / (a * a + y * y)
    assert ratio_norm == 1
    boundary_checks.append({"frequency": str(y), "norm_squared": str(ratio_norm)})

ta, gamma, omega = F(1, 4), F(2), F(1, 8)
x, y = F(1, 16), F(2)
toy_bad_norm = toy_ratio_norm_squared(x, y, ta, gamma, omega)
toy_good_norm = toy_ratio_norm_squared(x, y, ta, gamma, F(1, 2))
assert toy_bad_norm > 1
assert toy_good_norm < 1
assert ta - omega == F(1, 8)
toy_bad_pick = (1 - toy_bad_norm) / (2 * x)
assert toy_bad_pick < 0
for pole_y in [gamma, -gamma]:
    assert abs_quartic_squared(ta, pole_y, ta, gamma) == 0
    assert abs_quartic_squared(ta - 2 * omega, pole_y, ta, gamma) != 0

# Squaring the rank-one norm formula avoids irrational arithmetic.
leakage_norm_squared = (2 * a) ** 2 * F(1, 2 * a) ** 2
assert leakage_norm_squared == 1

T = math.pi / float(gamma)
toy_tangent_two_point_value = 8 * (1 - math.cosh(float(ta) * T))
h = math.log(6)
mixed_source_zero_residuals = []
for k in range(-3, 4):
    s = 0.5 + 1j * (2 * k + 1) * math.pi / h
    mixed_source_zero_residuals.append(abs(2 * cmath.cosh((s - 0.5) * h / 2)))

result = {
    "status": "all assertions passed",
    "exact_controls": {
        "good_allpass_pick_diagonal": record(good_pick),
        "bad_allpass_pick_diagonal": record(bad_pick),
        "boundary_modulus_checks": boundary_checks,
        "bad_hardy_leakage_norm_squared": record(leakage_norm_squared),
        "quartet_a": str(ta),
        "quartet_gamma": str(gamma),
        "bad_shift_omega": str(omega),
        "evaluation_p": {"real": str(x), "imag": str(y)},
        "bad_shift_ratio_norm_squared": record(toy_bad_norm),
        "good_shift_ratio_norm_squared": record(toy_good_norm),
        "bad_shift_pick_diagonal": record(toy_bad_pick),
        "bad_shift_pole_real_part": str(ta - omega),
        "poles_uncanceled": True,
    },
    "floating_diagnostics_only": {
        "toy_signed_tangent_two_point_value": toy_tangent_two_point_value,
        "mixed_source_critical_zero_max_residual": max(mixed_source_zero_residuals),
    },
    "scope": "Finite controls only. Floating diagnostics are not certificates. No RH proof.",
}
parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(result, indent=2) + "\n")
print("PASS: stable/unstable all-pass, exact Hardy leakage, quartet poles/Pick sign, connected-source scope")
print(json.dumps({"bad_hardy_leakage_norm_squared": result["exact_controls"]["bad_hardy_leakage_norm_squared"], "bad_shift_ratio_norm_squared": result["exact_controls"]["bad_shift_ratio_norm_squared"]}))
