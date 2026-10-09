#!/usr/bin/env python3
"""Zero-input probes for the arithmetic connection and its Poisson completion.

Exact algebra, finite character controls, and a proved theta-cutoff repair.
This is NOT a Weil-positivity certificate. No zero ordinate, root search,
scattering phase, or zero-built matrix is used. The finite Gauss phase below
is computed from the character itself.

Run from the repository root:
  python scripts/arithmetic_poisson_connection.py --output PATH
Dependencies: numpy, scipy, mpmath, sympy.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import platform
import sys

import mpmath as mp
import numpy as np
import scipy
from scipy.integrate import quad
import sympy as sp


BASE_COMMIT = "265bf38dfd6af7d5820396f7e80244122a4aa235"
KAPPA = (sp.sqrt(10 - 2 * sp.sqrt(5)) - 2) / (sp.sqrt(5) - 1)
RAW_SLOPE = 3 / (128 * math.sqrt(2) * math.pi**4)
DESIGN_CUTOFFS = [8, 32, 128]
HOLDOUT_CUTOFFS = [37, 101, 257]


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def chi5(n: int):
    return (sp.Integer(0), sp.Integer(1), sp.I, -sp.I, sp.Integer(-1))[n % 5]


def log_expand(value):
    return sp.simplify(sp.expand_log(sp.expand(value), force=True))


def connection_coefficients(a: list) -> list:
    """b=(a*log)*a^{-1}, by the finite triangular convolution recurrence.

    a[0] is ignored; a[1] must be 1. This does not insert a prime support rule.
    Arbitrary/nonmultiplicative inputs are allowed and retain composite atoms.
    """
    if a[1] != 1:
        raise ValueError("The normalized Dirichlet coefficient a(1) must be 1")
    b = [sp.Integer(0)] * len(a)
    for n in range(2, len(a)):
        previous = sum(b[d] * a[n // d] for d in divisors(n) if 1 < d < n)
        b[n] = log_expand(a[n] * sp.log(n) - previous)
    return b


def incidence_matrix(a: list) -> sp.Matrix:
    N = len(a) - 1
    return sp.Matrix(N, N, lambda i, j:
                     a[(i + 1) // (j + 1)] / sp.sqrt((i + 1) // (j + 1))
                     if (i + 1) % (j + 1) == 0 else 0)


def exact_algebra_controls() -> dict:
    N = 36
    ch = [chi5(n) for n in range(N + 1)]
    zeta_a = [sp.Integer(1)] * (N + 1)
    bz, bc = connection_coefficients(zeta_a), connection_coefficients(ch)

    def mangoldt(n):
        fac = sp.factorint(n)
        return sp.log(next(iter(fac))) if len(fac) == 1 else sp.Integer(0)

    zeta_ok = all(log_expand(bz[n] - mangoldt(n)) == 0 for n in range(2, N + 1))
    chi_ok = all(log_expand(bc[n] - ch[n] * mangoldt(n)) == 0
                 for n in range(2, N + 1))

    k = sp.Symbol("k", real=True)
    dh = [sp.Integer(0), sp.Integer(1), k, -k, sp.Integer(-1),
          sp.Integer(0), sp.Integer(1)]
    bd = connection_coefficients(dh)
    dh6_ok = log_expand(bd[6] - (1 + k**2) * sp.log(6)) == 0

    # Direct matrix calculation on a deliberately NONmultiplicative input.
    arbitrary = [sp.Integer(0), sp.Integer(1)] + [sp.Integer((n * n + 3) % 7 - 2)
                                                  for n in range(2, 13)]
    ba = connection_coefficients(arbitrary)
    A, B = incidence_matrix(arbitrary), incidence_matrix(ba)
    H = sp.diag(*[sp.log(n) for n in range(1, len(arbitrary))])
    residual = H * A - A * H - B * A
    connection_ok = all(log_expand(x) == 0 for x in residual)

    # The coefficient logarithm is also computed independently as log(I+J).
    J = A - sp.eye(A.rows)
    log_A = sp.zeros(A.rows)
    term = sp.eye(A.rows)
    for r in range(1, A.rows + 1):
        term = term * J
        log_A += sp.Rational((-1)**(r + 1), r) * term
    log_identity = H * log_A - log_A * H - B
    log_ok = all(log_expand(x) == 0 for x in log_identity)

    # Exact mixed-prime Gram: columns B e_1, B e_2, B e_3, B e_6.
    indices = [1, 2, 3, 6]
    columns = [{2*n: 1, 3*n: 1} for n in indices]
    G = sp.Matrix([[sum(c.get(r, 0) * d.get(r, 0) for r in set(c) | set(d))
                    for d in columns] for c in columns])
    expected = sp.Matrix([[2, 0, 0, 0], [0, 2, 1, 0],
                          [0, 1, 2, 0], [0, 0, 0, 2]])

    # Analytic continuation of autocorrelation is not a modulus square.
    # g(x)=x*1[-1,1], Fourier convention exp(+izx).
    correct = -4 / sp.E**2
    false_modulus_square = 4 / sp.E**2
    return {
        "coefficient_horizon": N,
        "zeta_connection_matches_Lambda_exactly": zeta_ok,
        "chi5_connection_matches_chi_Lambda_exactly": chi_ok,
        "arbitrary_input_matrix_identity_exact": connection_ok,
        "independent_finite_matrix_log_identity_exact": log_ok,
        "dh_b6_identity_exact": dh6_ok,
        "dh_b6_symbolic": "(1 + kappa**2) * log(6)",
        "chi_b6_exact": str(bc[6]),
        "commuting_dilation_gram_exact": G == expected,
        "commuting_dilation_gram": [[int(x) for x in row] for row in G.tolist()],
        "commuting_dilation_gram_eigenvalues": [
            int(x) for x, multiplicity in sorted(G.eigenvals().items())
            for _ in range(multiplicity)
        ],
        "synthetic_off_real_pairing": str(correct),
        "incorrect_modulus_square": str(false_modulus_square),
        "conjugation_mutation_rejected": bool(correct < 0 < false_modulus_square),
    }


def character_and_poisson_controls() -> dict:
    with mp.workdps(70):
        k = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
        v = [mp.mpc(0), mp.mpc(1), mp.j, -mp.j, mp.mpc(-1)]
        d = [mp.mpc(0), mp.mpc(1), k, -k, mp.mpc(-1)]

        def F(w):
            return [sum(w[r] * mp.exp(2j * mp.pi * r * a / 5) for r in range(5))
                    / mp.sqrt(5) for a in range(5)]

        tau = sum(v[r] * mp.exp(2j * mp.pi * r / 5) for r in range(5))
        omega = tau / (mp.j * mp.sqrt(5))
        fchi, fdh = F(v), F(d)
        fourier_chi = max(abs(fchi[r] - tau / mp.sqrt(5) * mp.conj(v[r]))
                          for r in range(5))
        fourier_dh = max(abs(fdh[r] - mp.j * d[r]) for r in range(5))

        # M_2 is pullback: (M_2 v)(r)=v(2r), so eigenvalue chi(2)=i.
        chi_eigen = max(abs(v[2*r % 5] - mp.j * v[r]) for r in range(5))
        dh_defect_sq = sum(abs(d[2*r % 5] - k * d[r])**2 for r in range(5))

        def theta(w, t):
            # Odd primitive mod-5 theta. The finite tail has Gaussian decay.
            return 2 * sum(w[n % 5] * n * mp.exp(-mp.pi * n*n * t / 5)
                           for n in range(1, 121))

        theta_rows = []
        for label, ttext in [("design", "0.2"), ("design", "0.7"),
                             ("design", "2"), ("holdout", "0.37"),
                             ("holdout", "1.3"), ("holdout", "3.7")]:
            t = mp.mpf(ttext)
            ch_error = abs(theta(v, t) - omega * t**(-mp.mpf("1.5"))
                           * theta([mp.conj(z) for z in v], 1/t))
            dh_error = abs(theta(d, t) - t**(-mp.mpf("1.5")) * theta(d, 1/t))
            theta_rows.append({"region": label, "t": ttext,
                               "chi_inversion_abs_error": mp.nstr(ch_error, 8),
                               "dh_inversion_abs_error": mp.nstr(dh_error, 8)})

        return {
            "working_decimal_digits": 70,
            "kappa": mp.nstr(k, 65),
            "gauss_root_phase": [mp.nstr(mp.re(omega), 50), mp.nstr(mp.im(omega), 50)],
            "kappa_radical_vs_gauss_error": mp.nstr(abs(k - mp.im(omega)/(1+mp.re(omega))), 8),
            "chi_fourier_error": mp.nstr(fourier_chi, 8),
            "dh_fourier_error": mp.nstr(fourier_dh, 8),
            "chi_multiplicative_eigenline_error": mp.nstr(chi_eigen, 8),
            "dh_multiplicative_defect_squared": mp.nstr(dh_defect_sq, 35),
            "dh_defect_formula_error": mp.nstr(abs(dh_defect_sq-2*(1+k*k)**2), 8),
            "dh_b6": mp.nstr((1+k*k)*mp.log(6), 50),
            "dh_halfdensity_b6": mp.nstr((1+k*k)*mp.log(6)/mp.sqrt(6), 50),
            "theta_inversion": theta_rows,
            "chi_passes_compatibility": chi_eigen == 0 and fourier_chi < mp.mpf("1e-60"),
            "dh_passes_poisson_but_fails_eigenline": fourier_dh < mp.mpf("1e-60") and dh_defect_sq > 1,
            "all_theta_residuals_below_1e_minus_60": all(
                mp.mpf(row[key]) < mp.mpf("1e-60") for row in theta_rows
                for key in ("chi_inversion_abs_error", "dh_inversion_abs_error")),
        }


def mutation_controls() -> dict:
    with mp.workdps(60):
        p, alpha, beta = mp.mpf(2), mp.mpf(1), mp.mpf("1.01")
        s = mp.mpc("1.7", "0.31")

        def R(z):
            return (1-alpha*p**(-z))/(1-beta*p**(-z))

        euler_fe_error = abs(R(s) - mp.conj(R(1-mp.conj(s))))
        ell = mp.log(2) * mp.mpf("1.01")
        shift_braid_defect = mp.exp(ell) - 2
        density_delta = mp.mpf("0.01")
        density_norm_ratio = 2**(-2*density_delta)
        charge = mp.mpf("0.01")
        derivative_residual = -charge*6**(-s) - charge*6**(s-1)
        return {
            "alpha2_mutation_still_completely_multiplicative": True,
            "alpha2_value": str(beta),
            "alpha2_unitary_eigenvalue_norm_defect": mp.nstr(abs(beta)-1, 20),
            "alpha2_fixed_completion_reflection_error_at_1p7_plus_0p31i": mp.nstr(euler_fe_error, 25),
            "clock_mutation": "ell_2 = 1.01 * log(2), entire tower",
            "clock_still_additive_on_prime_exponents": True,
            "clock_affine_translation_defect_exp_ell_minus_2": mp.nstr(shift_braid_defect, 25),
            "half_density_mutation": "R_n f(x)=n^(-0.51) f(x/n)",
            "half_density_squared_norm_ratio_at_2": mp.nstr(density_norm_ratio, 25),
            "fake_b6_charge": str(charge),
            "fake_b6_formal_source_defect": "b(6)=0.01 but chi(6)*Lambda(6)=0",
            "fake_b6_multiplier": "exp((0.01/log(6))*6**(-s))",
            "fake_b6_preserves_all_baseline_zeros_exactly": True,
            "fake_b6_reflection_log_derivative_residual": mp.nstr(abs(derivative_residual), 25),
            "all_listed_mutations_detected": bool(euler_fe_error > 0 and shift_braid_defect != 0
                                                   and density_norm_ratio != 1
                                                   and abs(derivative_residual) > 0),
            "interpretation": "Compatibility defects, not a computed Weil sign or an RH proof.",
        }


def phi(x):
    x = np.asarray(x)
    return (x**4 - 3*x**2/(2*np.pi))*np.exp(-np.pi*x*x)


def primitive_phi(x):
    return -x**3*np.exp(-np.pi*x*x)/(2*np.pi)


def completed_theta(x: float) -> float:
    """Poisson evaluation of the full phi-lift; no zeta/L function or zeros."""
    if x == 0:
        return 0.0
    if x < 1:
        return completed_theta(1/x) / x
    count = max(1, int(math.ceil(math.sqrt(80/math.pi)/x)))
    return float(np.sum(phi(x*np.arange(1, count+1))))


def prime_pair_gram(m, n):
    m, n = np.asarray(m), np.asarray(n)
    s = m*m + n*n
    return 3*m*m*n*n*(35*m*m*n*n - 6*s*s)/(32*np.pi**4*s**4.5)


def raw_theta_norm_squared(N: int) -> float:
    # Chunking keeps the largest temporary below O(128*N), not O(N**2).
    ns = np.arange(1, N+1, dtype=float)
    total = 0.0
    for start in range(1, N+1, 128):
        ms = np.arange(start, min(N+1, start+128), dtype=float)[:, None]
        total += float(np.sum(prime_pair_gram(ms, ns[None, :])))
    return total


def theta_error(N: int, *, endpoint: bool = False) -> tuple[float, float]:
    ns = np.arange(1, N+1, dtype=float)

    def integrand(y):
        if y == 0:
            return 0.0
        x = y/N
        observed = float(np.sum(phi(ns*x))) - primitive_phi(y)/x
        if endpoint:
            observed -= float(phi(y))/2
        difference = observed - completed_theta(x)
        return difference*difference/N

    # The theorem bounds the omitted tail by a Gaussian derivative tail.
    # These quadratures are observations, not certified interval enclosures.
    value, error = quad(integrand, 0, 8, epsabs=1e-17, epsrel=2e-10, limit=180)
    return value, error


def theta_completion_controls() -> dict:
    x = sp.Symbol("x", positive=True)
    gaussian = sp.exp(-sp.pi*x*x)
    phi_exact = (x**4 - 3*x*x/(2*sp.pi))*gaussian
    primitive_exact = -x**3*gaussian/(2*sp.pi)
    derivative_ok = sp.simplify(sp.diff(primitive_exact, x)-phi_exact) == 0
    D1g = x*sp.diff(gaussian, x)+gaussian
    pole_kill_ok = sp.simplify(x*sp.diff(D1g, x)/(4*sp.pi**2)-phi_exact) == 0
    mixed = []
    for m, n in [(2, 3), (2, 5), (5, 11)]:
        integral, err = quad(lambda t: float(phi(m*t)*phi(n*t)), 0, np.inf,
                             epsabs=1e-15, epsrel=1e-12)
        formula = float(prime_pair_gram(m, n))
        mixed.append({"m": m, "n": n, "formula": formula, "quadrature": integral,
                      "absolute_error": abs(integral-formula), "quad_error_estimate": err})
    rows = []
    for region, Ns in [("design", DESIGN_CUTOFFS), ("holdout", HOLDOUT_CUTOFFS)]:
        for N in Ns:
            raw = raw_theta_norm_squared(N)
            err, qe = theta_error(N)
            trap_err, trap_qe = theta_error(N, endpoint=True)
            rows.append({"region": region, "N": N, "raw_norm_squared": raw,
                         "raw_norm_squared_over_N": raw/N,
                         "renormalized_error_squared": err,
                         "N_times_renormalized_error_squared": N*err,
                         "endpoint_corrected_error_squared": trap_err,
                         "N_cubed_times_endpoint_error_squared": N**3*trap_err,
                         "quadrature_error_estimates": [qe, trap_qe]})
    largeN = 1024
    return {
        "primitive_derivative_exact": derivative_ok,
        "pole_annihilating_differential_identity_exact": pole_kill_ok,
        "raw_divergence_slope_exact": "3/(128*sqrt(2)*pi**4)",
        "raw_divergence_slope_decimal": RAW_SLOPE,
        "fresh_large_cutoff": {"N": largeN,
                               "raw_norm_squared_over_N": raw_theta_norm_squared(largeN)/largeN},
        "renormalized_error_limit_exact": "33/(2048*sqrt(2)*pi**4)",
        "renormalized_error_limit_decimal": 33/(2048*math.sqrt(2)*math.pi**4),
        "mixed_prime_gram_entries": mixed,
        "mixed_prime_entries_have_both_signs": mixed[0]["formula"] > 0 > mixed[1]["formula"],
        "gram_formula_matches_independent_quadrature": max(r["absolute_error"] for r in mixed) < 1e-12,
        "cutoff_rows": rows,
        "counterterm_coefficient_mutation_exact_asymptotic": "||Theta_N-lambda*F(Nx)/x||^2/N -> |1-lambda|^2*C",
        "finite_boundary": "Floating point observations verify the formulas, not their universal quantifiers; proofs are in CONSTRUCTION.md.",
    }


def muntz_lift_controls() -> dict:
    """Check a nonzero-moment lift against independent finite Euler summation.

    The comparison uses no zeta call, zero list, or scattering multiplier.
    """
    x, s = sp.symbols("x s")
    mellin_phi = s*(s-1)*sp.pi**(-s/2)*sp.gamma(s/2)/(8*sp.pi**2)
    moment_exact = sp.simplify(-sp.diff(mellin_phi, s).subs(s, 1))
    primitive_ok = sp.simplify(sp.diff(sp.erf(sp.sqrt(sp.pi)*x)/2, x)
                               - sp.exp(-sp.pi*x*x)) == 0
    moment_quad, moment_qe = quad(lambda u: -math.log(u)*float(phi(u)),
                                  0, np.inf, epsabs=1e-14, epsrel=1e-12)

    def completed_gaussian(x_value):
        if x_value == 0:
            return -0.5
        a = x_value if x_value >= 1 else 1/x_value
        count = max(1, int(math.ceil(math.sqrt(80/math.pi)/a)))
        theta = float(np.sum(np.exp(-np.pi*(a*np.arange(1, count+1))**2)))
        return theta-0.5/x_value if x_value >= 1 else -0.5+theta/x_value

    cutoff_rows = []
    for region, N in [("design", 8), ("design", 32), ("holdout", 101)]:
        ns = np.arange(1, N+1, dtype=float)
        def error_integrand(y, endpoint):
            if y == 0:
                return 0.0 if endpoint else 0.25/N
            xv = y/N
            finite = float(np.sum(np.exp(-np.pi*(ns*xv)**2)))
            finite -= math.erf(math.sqrt(math.pi)*y)/(2*xv)
            if endpoint:
                finite -= math.exp(-math.pi*y*y)/2
            return (finite-completed_gaussian(xv))**2/N
        base, base_qe = quad(lambda y: error_integrand(y, False), 0, 8,
                             epsabs=1e-16, epsrel=2e-9, limit=180)
        trap, trap_qe = quad(lambda y: error_integrand(y, True), 0, 8,
                             epsabs=1e-17, epsrel=2e-9, limit=180)
        cutoff_rows.append({"region": region, "N": N,
                            "renormalized_error_squared": base,
                            "endpoint_corrected_error_squared": trap,
                            "quadrature_error_estimates": [base_qe, trap_qe]})

    mellin_rows = []
    with mp.workdps(55):
        def scalar_euler_maclaurin(z):
            cutoff, order = 48, 28
            value = mp.fsum(mp.mpf(n)**(-z) for n in range(1, cutoff))
            value += mp.mpf(cutoff)**(1-z)/(z-1)+mp.mpf(cutoff)**(-z)/2
            value += mp.fsum(mp.bernoulli(2*k)/mp.factorial(2*k)
                             * mp.rf(z, 2*k-1)*mp.mpf(cutoff)**(-z-2*k+1)
                             for k in range(1, order+1))
            return value
        def theta_above_one(u):
            return mp.fsum(mp.exp(-mp.pi*(n*u)**2) for n in range(1, 17))
        for region, real, imag in [("design", "0.5", "0.7"),
                                   ("holdout", "0.37", "1.3"),
                                   ("holdout", "0.73", "2.1")]:
            z = mp.mpc(real, imag)
            lifted = -1/(2*z)+1/(2*(z-1))
            lifted += mp.quad(lambda u: theta_above_one(u)*(u**(z-1)+u**(-z)),
                              [1, 2, 4, mp.inf])
            independent = scalar_euler_maclaurin(z)*mp.pi**(-z/2)*mp.gamma(z/2)/2
            mellin_rows.append({"region": region, "s": str(z),
                                "muntz_gaussian_mellin": mp.nstr(lifted, 40),
                                "euler_maclaurin_times_gaussian_mellin": mp.nstr(independent, 40),
                                "absolute_error": mp.nstr(abs(lifted-independent), 10)})
    return {
        "gaussian_primitive_identity_exact": primitive_ok,
        "log_phi_moment_exact": str(moment_exact),
        "log_phi_moment_identity_exact": moment_exact == -1/(8*sp.pi**2),
        "log_phi_moment_quadrature": moment_quad,
        "log_phi_moment_quadrature_error_estimate": moment_qe,
        "log_phi_moment_matches_quadrature": abs(moment_quad+1/(8*math.pi**2)) < 1e-13,
        "gaussian_integral": "1/2 (nonzero)",
        "gaussian_cutoff_rows": cutoff_rows,
        "mellin_rows": mellin_rows,
        "euler_maclaurin_parameters": {"cutoff": 48, "order": 28, "dps": 55},
        "mellin_errors_below_1e_minus_40": all(mp.mpf(r["absolute_error"]) < mp.mpf("1e-40")
                                               for r in mellin_rows),
        "scope": "Finite checks of the moment-retaining lift; closed-domain and graph-core statements are proved in CONSTRUCTION.md, not inferred from these samples.",
    }


def canonical_box_bridge() -> dict:
    # Independent origin-renormalized Gamma integral versus the existing Suzuki
    # Lerch-function evaluator. Both sides use arithmetic, neither uses zeros.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from suzuki_psi import psi_suzuki, prime_power_events_up_to
    rows = []
    with mp.workdps(45):
        for Ttext in ["0.3", "1.1", "2.3", "4.1"]:
            T = mp.mpf(Ttext)
            def w(u):
                return mp.exp(-u/2)/(-mp.expm1(-2*u))
            energy = 2*mp.quad(lambda u: u*w(u) if u else mp.mpf("0.5"), [0, T])
            energy += 2*T*mp.quad(w, [T, mp.inf])
            constant = (mp.digamma(mp.mpf("0.25"))-mp.log(mp.pi))*T
            pole = 16*(mp.cosh(T/2)-1)
            events = prime_power_events_up_to(int(mp.floor(mp.exp(T))))
            prime = 2*sum(e.von_mangoldt/mp.sqrt(e.n)*(T-e.log_n) for e in events)
            arithmetic = energy+constant+pole-prime
            psi = 2*psi_suzuki(T, dps=45, events=events)
            rows.append({"T": Ttext, "geometric_box_form": mp.nstr(arithmetic, 35),
                         "twice_Suzuki_Psi": mp.nstr(psi, 35),
                         "absolute_error": mp.nstr(abs(arithmetic-psi), 8)})
    return {"normalization": "unnormalized indicator g=1[-T/2,T/2], Q(g)=2*Psi(T)",
            "rows": rows,
            "all_errors_below_1e_minus_35": all(mp.mpf(r["absolute_error"]) < mp.mpf("1e-35") for r in rows),
            "scope": "Arithmetic identity on four box tests; not all-test positivity."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    algebra = exact_algebra_controls()
    character = character_and_poisson_controls()
    mutations = mutation_controls()
    theta = theta_completion_controls()
    muntz = muntz_lift_controls()
    bridge = canonical_box_bridge()
    checks = {
        "exact_connection": algebra["zeta_connection_matches_Lambda_exactly"]
            and algebra["chi5_connection_matches_chi_Lambda_exactly"]
            and algebra["arbitrary_input_matrix_identity_exact"]
            and algebra["independent_finite_matrix_log_identity_exact"],
        "dh_exact_defect": algebra["dh_b6_identity_exact"]
            and character["dh_passes_poisson_but_fails_eigenline"],
        "character_poisson": character["chi_passes_compatibility"]
            and character["all_theta_residuals_below_1e_minus_60"],
        "mutation_instrument": mutations["all_listed_mutations_detected"]
            and algebra["conjugation_mutation_rejected"],
        "nonfactorization_counterexample": algebra["commuting_dilation_gram_exact"],
        "theta_completion_formulas": theta["primitive_derivative_exact"]
            and theta["pole_annihilating_differential_identity_exact"]
            and theta["gram_formula_matches_independent_quadrature"],
        "canonical_arithmetic_bridge": bridge["all_errors_below_1e_minus_35"],
        "moment_retaining_muntz_lift": muntz["gaussian_primitive_identity_exact"]
            and muntz["log_phi_moment_identity_exact"]
            and muntz["log_phi_moment_matches_quadrature"]
            and muntz["mellin_errors_below_1e_minus_40"],
    }
    result = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "base_commit": BASE_COMMIT,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "scipy": scipy.__version__, "mpmath": mp.__version__, "sympy": sp.__version__},
        "construction_inputs": ["integers", "divisibility", "logarithm", "Lebesgue measure",
                                "primitive character mod 5", "additive Fourier transform", "Gaussian"],
        "zero_data_used": False,
        "claim": "Arithmetic/Poisson compatibility, a convergent finite completion, and a closed moment-retaining lattice lift; no Weil positivity proof.",
        "exact_algebra": algebra, "character_module": character, "mutations": mutations,
        "theta_completion": theta, "muntz_lift": muntz, "canonical_box_bridge": bridge,
        "checks": checks, "all_checks_pass": all(checks.values()),
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"checks": checks, "all_checks_pass": all(checks.values()),
                      "output": str(args.output) if args.output else None}, indent=2))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
