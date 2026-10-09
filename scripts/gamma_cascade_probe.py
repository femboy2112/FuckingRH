"""Portable floating-point controls for GAMMA_CASCADE_AND_DELAY.md.

These are numerical diagnostics, not interval-certified enclosures.
"""
import argparse
import json
from pathlib import Path

import numpy as np
from scipy.special import digamma, gamma, loggamma, rgamma

A = 0.25
TOL = 5e-11
CUTOFFS = [8, 32, 128, 512]


def serial(z):
    if np.iscomplexobj(z):
        return {"re": float(np.real(z)), "im": float(np.imag(z))}
    return float(z)


def cascade(m, q):
    lam = 2*np.arange(m) + 0.5
    return np.prod((lam-q)/(lam+q))


def gamma_identity(m, q):
    return (gamma(A+q/2)*rgamma(A-q/2)
            * np.exp(loggamma(m+A-q/2)-loggamma(m+A+q/2)))


def rho(q):
    return np.exp(-q*np.log(np.pi))*gamma(A+q/2)*rgamma(A-q/2)


def delay(m, omega):
    lam = 2*np.arange(m)+0.5
    return np.sum(2*lam/(lam*lam+omega*omega))


def delay_gamma(omega):
    return np.log(np.pi)-np.real(digamma(A+0.5j*omega))


def alpha_exact(omega):
    return np.real(digamma(A+0.5j*omega))-digamma(A)


def alpha_finite(m, omega):
    lam = 2*np.arange(m)+0.5
    return np.sum(2*omega*omega/(lam*(lam*lam+omega*omega)))


def tail_bound(m, omega):
    return omega*omega/4*((m+A)**-3+1/(2*(m+A)**2))


report = {"arithmetic": "NumPy complex128 / SciPy special functions",
          "status": "floating-point controls; no interval enclosures",
          "gamma_convergence": [], "delay_convergence": [],
          "finite_part_controls": [], "prime_controls": []}
gamma_error = boundary_error = delay_error = 0.0
for q in [0.25+0.7j, 1.2+2.1j, 2+0.4j]:
    errors = []
    for m in CUTOFFS:
        b = cascade(m, q)
        err = abs(b-gamma_identity(m, q))
        gamma_error = max(gamma_error, err)
        assert err < TOL
        rel = (m/np.pi)**q*b/rho(q)-1
        errors.append(abs(rel))
        report["gamma_convergence"].append({
            "M": m, "q": serial(q), "abs_B_M": serial(abs(b)),
            "relative_error": serial(abs(rel)),
            "M_times_relative_error": serial(m*rel),
            "predicted_limit_q_over_4": serial(q/4)})
    assert errors[-1] < errors[0]

for omega in [0., 1., 3., 10.]:
    previous = -1.
    for m in CUTOFFS:
        err = abs(abs(cascade(m, 1j*omega))-1)
        boundary_error = max(boundary_error, err)
        assert err < TOL
        t = delay(m, omega)
        recurrence = np.real(digamma(m+A+0.5j*omega)-digamma(A+0.5j*omega))
        err = abs(t-recurrence)
        delay_error = max(delay_error, err)
        assert err < TOL
        a_m = alpha_finite(m, omega)
        assert abs(a_m-(delay(m,0)-t)) < TOL
        assert a_m >= previous-TOL
        previous = a_m
        tail = alpha_exact(omega)-a_m
        bound = tail_bound(m,omega)
        assert -TOL <= tail <= bound+TOL
        report["finite_part_controls"].append({
            "M": m, "omega": omega, "alpha_M": serial(a_m),
            "alpha": serial(alpha_exact(omega)), "tail": serial(tail),
            "analytic_upper_bound": serial(bound)})
        err = t-np.log(m/np.pi)-delay_gamma(omega)
        report["delay_convergence"].append({
            "M": m, "omega": omega, "renormalized_delay_error": serial(err),
            "M_times_error": serial(m*err), "predicted_limit": -0.25})

# Differentiate a finite response numerically, to check the phase convention.
omega = 0.7
step = 1e-5
derivative = (cascade(16,1j*(omega+step))-cascade(16,1j*(omega-step)))/(2*step)
phase_error = abs(-np.imag(derivative/cascade(16,1j*omega))-delay(16,omega))
assert phase_error < 1e-7
report["phase_sign_finite_difference_error"] = float(phase_error)

q0 = 0.4
report["wrong_normalizer_control"] = [
    {"M": m, "B_M": serial(cascade(m,q0)), "target": serial(rho(q0)),
     "correct": serial((m/np.pi)**q0*cascade(m,q0)),
     "wrong": serial((m/np.pi)**(-q0)*cascade(m,q0))} for m in CUTOFFS]
assert abs((512/np.pi)**(-q0)*cascade(512,q0)) < abs(rho(q0))/10

for p in [2,3,5,11]:
    r = p**-0.5
    ell = np.log(p)
    def local(q):
        return (1-r*np.exp(q*ell))/(1-r*np.exp(-q*ell))
    def stable(q):
        w = np.exp(-q*ell)
        return (w-r)/(1-r*w)
    for omega in [0.3,1.7]:
        q = 1j*omega
        assert abs(local(q)-np.exp(q*ell)*stable(q)) < TOL
        assert abs(abs(local(q))-1) < TOL
        pr = (1-r*r)/(1-2*r*np.cos(omega*ell)+r*r)
        derivative = (local(1j*(omega+step))-local(1j*(omega-step)))/(2*step)
        actual = -np.imag(derivative/local(q))
        theoretical = ell*(pr-1)
        assert abs(actual-theoretical) < 1e-7
        deficit = ell*((1+r)/(1-r)-pr)
        assert deficit >= 0
        k = np.arange(1,1001)
        partial = 2*ell*np.sum(r**k*(1-np.cos(k*omega*ell)))
        assert abs(deficit-partial) < TOL
        report["prime_controls"].append({
            "p": p, "omega": omega, "raw_delay": float(actual),
            "delay_deficit": float(deficit), "series_residual": float(abs(deficit-partial))})

report["max_exact_identity_errors"] = {
    "gamma_product": float(gamma_error), "unit_boundary_modulus": float(boundary_error),
    "delay_digamma_recurrence": float(delay_error)}
report["all_assertions_passed"] = True
parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
target = args.output
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps({"all_assertions_passed": True, "result_file": str(target),
                  "max_exact_identity_errors": report["max_exact_identity_errors"],
                  "phase_sign_finite_difference_error": float(phase_error)},indent=2))
