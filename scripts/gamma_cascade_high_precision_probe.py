"""High-precision numerical controls; analytic proofs are in the companion note.

This is not interval arithmetic and does not certify RH or an operator limit.
"""
import argparse
import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 90
A = mp.mpf(1) / 4
TOL = mp.mpf("1e-75")


def serial(x):
    if isinstance(x, mp.mpc):
        return {"re": mp.nstr(x.real, 30), "im": mp.nstr(x.imag, 30)}
    return mp.nstr(x, 30)


def stage(j, q):
    lam = 2 * j + mp.mpf("0.5")
    return (lam - q) / (lam + q)


def cascade(m, q):
    return mp.fprod(stage(j, q) for j in range(m))


def gamma_identity(m, q):
    return (mp.gamma(A + q / 2) * mp.rgamma(A - q / 2)
            * mp.gamma(m + A - q / 2) / mp.gamma(m + A + q / 2))


def rho(q):
    return mp.power(mp.pi, -q) * mp.gamma(A + q / 2) * mp.rgamma(A - q / 2)


def delay(m, omega):
    return mp.fsum(2 * (2*j + mp.mpf("0.5"))
                   / ((2*j + mp.mpf("0.5"))**2 + omega**2)
                   for j in range(m))


def delay_gamma(omega):
    return mp.log(mp.pi) - mp.re(mp.digamma(A + 1j * omega / 2))


def alpha_exact(omega):
    return mp.re(mp.digamma(A + 1j * omega / 2)) - mp.digamma(A)


def alpha_finite(m, omega):
    return mp.fsum(2 * omega**2 / ((2*j + mp.mpf("0.5"))
                   * ((2*j + mp.mpf("0.5"))**2 + omega**2))
                   for j in range(m))


def tail_bound(m, omega):
    return omega**2 / 4 * ((m + A)**(-3) + 1 / (2*(m + A)**2))


report = {"precision_decimal_digits": mp.mp.dps,
          "status": "numerical controls only; not interval enclosures",
          "gamma_convergence": [], "delay_convergence": [],
          "finite_part_controls": [], "prime_controls": []}

max_gamma_identity_error = mp.mpf(0)
max_boundary_modulus_error = mp.mpf(0)
max_delay_identity_error = mp.mpf(0)

q_samples = [mp.mpc("0.25", "0.7"), mp.mpc("1.2", "2.1"), mp.mpc("2", "0.4")]
cutoffs = [8, 32, 128, 512]
for q in q_samples:
    errors = []
    for m in cutoffs:
        b = cascade(m, q)
        residual = abs(b - gamma_identity(m, q))
        max_gamma_identity_error = max(max_gamma_identity_error, residual)
        assert residual < TOL
        normalized = mp.power(m / mp.pi, q) * b
        relative = normalized / rho(q) - 1
        errors.append(abs(relative))
        report["gamma_convergence"].append({
            "M": m, "q": serial(q), "abs_B_M": serial(abs(b)),
            "relative_error": serial(abs(relative)),
            "M_times_relative_error": serial(m * relative),
            "predicted_limit_q_over_4": serial(q / 4)})
    assert errors[-1] < errors[0]

for omega in map(mp.mpf, [0, 1, 3, 10]):
    previous_alpha = mp.mpf(-1)
    for m in cutoffs:
        boundary_residual = abs(abs(cascade(m, 1j * omega)) - 1)
        max_boundary_modulus_error = max(max_boundary_modulus_error, boundary_residual)
        assert boundary_residual < TOL
        t = delay(m, omega)
        recurrence = mp.re(mp.digamma(m + A + 1j*omega/2)
                           - mp.digamma(A + 1j*omega/2))
        residual = abs(t - recurrence)
        max_delay_identity_error = max(max_delay_identity_error, residual)
        assert residual < TOL
        a_m = alpha_finite(m, omega)
        assert abs(a_m - (delay(m, 0) - t)) < TOL
        assert a_m >= previous_alpha - TOL
        previous_alpha = a_m
        tail = alpha_exact(omega) - a_m
        bound = tail_bound(m, omega)
        assert tail >= -TOL
        assert tail <= bound + TOL
        report["finite_part_controls"].append({
            "M": m, "omega": serial(omega), "alpha_M": serial(a_m),
            "alpha": serial(alpha_exact(omega)), "tail": serial(tail),
            "analytic_upper_bound": serial(bound)})
        delay_error = t - mp.log(m / mp.pi) - delay_gamma(omega)
        report["delay_convergence"].append({
            "M": m, "omega": serial(omega),
            "renormalized_delay_error": serial(delay_error),
            "M_times_error": serial(m * delay_error),
            "predicted_limit": "-0.25"})

# Differentiate the finite response directly; this checks the chosen phase sign.
w0 = mp.mpf("0.7")
phase_slope = mp.im(mp.diff(lambda w: cascade(16, 1j*w), w0)
                    / cascade(16, 1j*w0))
assert abs(-phase_slope - delay(16, w0)) < TOL
report["direct_phase_derivative_error"] = serial(abs(-phase_slope - delay(16, w0)))

# Wrong orientation: normalizing by a delay instead of the required advance.
q0 = mp.mpf("0.4")
report["wrong_normalizer_control"] = []
for m in cutoffs:
    b = cascade(m, q0)
    correct = mp.power(m / mp.pi, q0) * b
    wrong = mp.power(m / mp.pi, -q0) * b
    report["wrong_normalizer_control"].append({
        "M": m, "B_M": serial(b), "target": serial(rho(q0)),
        "correct": serial(correct), "wrong": serial(wrong)})
assert abs(mp.power(512 / mp.pi, -q0) * cascade(512, q0)) < abs(rho(q0)) / 10

for p in [2, 3, 5, 11]:
    r = 1 / mp.sqrt(p)
    ell = mp.log(p)
    def local(q):
        return (1 - r*mp.exp(q*ell)) / (1 - r*mp.exp(-q*ell))
    def stable(q):
        w = mp.exp(-q*ell)
        return (w-r)/(1-r*w)
    for omega in [mp.mpf("0.3"), mp.mpf("1.7")]:
        q = 1j*omega
        assert abs(local(q) - mp.exp(q*ell)*stable(q)) < TOL
        assert abs(abs(local(q))-1) < TOL
        pr = (1-r*r)/(1-2*r*mp.cos(omega*ell)+r*r)
        actual = -mp.im(mp.diff(lambda w: local(1j*w), omega)/local(q))
        theoretical = ell*(pr-1)
        assert abs(actual-theoretical) < TOL
        deficit = ell*((1+r)/(1-r)-pr)
        assert deficit >= 0
        # Sum the convergent prime-power series with an explicit discarded-tail bound.
        kmax = 1000
        partial = 2*ell*mp.fsum(r**k*(1-mp.cos(k*omega*ell)) for k in range(1,kmax+1))
        error_bound = 4*ell*r**(kmax+1)/(1-r)
        assert abs(deficit-partial) <= error_bound + TOL
        report["prime_controls"].append({
            "p": p, "omega": serial(omega), "raw_delay": serial(actual),
            "delay_deficit": serial(deficit), "series_residual": serial(abs(deficit-partial))})

report["max_exact_identity_errors"] = {
    "gamma_product": serial(max_gamma_identity_error),
    "unit_boundary_modulus": serial(max_boundary_modulus_error),
    "delay_digamma_recurrence": serial(max_delay_identity_error)}
report["all_assertions_passed"] = True
parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
target = args.output
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"all_assertions_passed": True,
                  "result_file": str(target),
                  "max_exact_identity_errors": report["max_exact_identity_errors"],
                  "gamma_final": report["gamma_convergence"][-1],
                  "delay_final": report["delay_convergence"][-1]}, indent=2))
