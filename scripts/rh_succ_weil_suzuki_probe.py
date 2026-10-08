#!/usr/bin/env python3
"""Finite controls for the succ -> full Weil/Suzuki derivation.

Uses exact step-cell translation overlaps and independently integrated Gamma
entries. All floating-point eigenvalues are finite observations, not certificates
of RH or of positivity on an infinite-dimensional interval. No zeta zeros enter.
Optional dependencies: numpy and scipy; see the research bundle requirements.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import json
import math
from pathlib import Path
import platform
import sys

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import eigh, toeplitz
from scipy.special import digamma, polygamma


EULER = 0.5772156649015328606
D0 = math.log(math.pi) - float(digamma(0.25))
F0 = float(polygamma(1, 0.25)) / 4.0


def events(limit):
    """Return log(n), Lambda(n)/sqrt(n), n for all prime powers <= limit."""
    prime = np.ones(limit + 1, dtype=bool)
    prime[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if prime[p]:
            prime[p * p::p] = False
    answer = []
    for p in np.flatnonzero(prime):
        n = int(p)
        while n <= limit:
            answer.append((math.log(n), math.log(int(p)) / math.sqrt(n), n))
            n *= int(p)
    return sorted(answer, key=lambda item: item[2])


def w(h):
    return math.exp(-h / 2.0) / (-math.expm1(-2.0 * h))


def f_exponential(t):
    """Sum exp(-a_j*t)/a_j^2; t=0 uses the trigamma identity.

    For t>0 the discarded exponential numerator is < exp(-40).
    This is a floating-point evaluation, not an interval enclosure.
    """
    if t == 0:
        return F0
    count = max(16, math.ceil(20 / t) + 2)
    a = 0.5 + 2 * np.arange(count, dtype=float)
    return float(np.sum(np.exp(-a * t) / a**2))


def gamma_matrix(A, cells):
    delta = 2 * A / cells
    first = np.empty(cells)
    first[0] = (2 / delta) * quad(
        lambda h: h * w(h) if h else 0.5,
        0, delta, epsabs=2e-12, epsrel=2e-12,
    )[0] + 2 * quad(w, delta, np.inf, epsabs=2e-12, epsrel=2e-12)[0]
    for lag in range(1, cells):
        lo, mid, hi = (lag - 1) * delta, lag * delta, (lag + 1) * delta
        left = quad(
            lambda h: w(h) * (h - lo) / delta if h else 1 / (2 * delta),
            lo, mid, epsabs=2e-12, epsrel=2e-12,
        )[0]
        right = quad(lambda h: w(h) * (hi - h) / delta,
                     mid, hi, epsabs=2e-12, epsrel=2e-12)[0]
        first[lag] = -left - right
    fs = np.array([f_exponential(k * delta) for k in range(cells + 1)])
    series_first = np.r_[2 * (fs[0] - fs[1]) / delta,
                         -(fs[:-2] - 2 * fs[1:-1] + fs[2:]) / delta]
    return toeplitz(first), float(np.max(np.abs(first - series_first)))


def matrices(A, cells, all_events):
    delta = 2 * A / cells
    active = [e for e in all_events if e[0] <= 2 * A]
    M = sum(e[1] for e in active)
    shift_first = np.zeros(cells)
    for h, weight, _ in active:
        q = h / delta
        k = math.floor(q)
        part = q - k
        if k < cells:
            shift_first[k] += weight * (1 - part)
        if k + 1 < cells:
            shift_first[k + 1] += weight * part
    prime_first = -shift_first
    prime_first[0] = 2 * M - 2 * shift_first[0]
    gamma, independent_error = gamma_matrix(A, cells)
    left = np.linspace(-A, A - delta, cells)
    right = left + delta
    C = 2 * (np.sinh(right / 2) - np.sinh(left / 2)) / math.sqrt(delta)
    S = 2 * (np.cosh(right / 2) - np.cosh(left / 2)) / math.sqrt(delta)
    P = gamma + toeplitz(prime_first) + 2 * np.outer(C, C)
    D = (D0 + 2 * M) * np.eye(cells) + 2 * np.outer(S, S)
    # Algebraically cancel the large diagonal prime mass before evaluating Q.
    cancelled_prime_first = -shift_first.copy()
    cancelled_prime_first[0] = -2 * shift_first[0]
    Q = gamma + toeplitz(cancelled_prime_first) - D0 * np.eye(cells)
    Q += 2 * np.outer(C, C) - 2 * np.outer(S, S)
    return P, D, Q, gamma, C, S, active, independent_error


def correlations(c):
    # Only the real part enters this real symmetric Weil form.
    return np.array([float(np.vdot(c[k:], c[:-k] if k else c).real)
                     for k in range(len(c))] + [0.0])


def correlation_at(h, delta, r):
    q = h / delta
    k = math.floor(q)
    if k >= len(r) - 1:
        return 0.0
    return (1 - (q - k)) * r[k] + (q - k) * r[k + 1]


def direct_weil(A, c, C, S, active):
    """Independent origin-renormalized explicit formula on cell functions."""
    delta = 2 * A / len(c)
    r = correlations(c)
    norm = r[0]
    integral = 0.0
    for k in range(len(c)):
        lo, hi = k * delta, (k + 1) * delta

        def integrand(h):
            if h == 0:
                return 0.5 * ((r[1] - norm) / delta + norm / 2)
            part = h / delta - k
            numerator = ((r[k] - norm) + part * (r[k + 1] - r[k])
                         + norm * (-math.expm1(-h / 2)))
            return numerator * w(h)

        integral += quad(integrand, lo, hi, epsabs=2e-11, epsrel=2e-11)[0]
    integral += quad(lambda h: -norm * math.exp(-h / 2) * w(h),
                     2 * A, np.inf, epsabs=2e-11, epsrel=2e-11)[0]
    arch = -(math.log(4 * math.pi) + EULER) * norm - 2 * integral
    prime = -2 * sum(a * correlation_at(h, delta, r) for h, a, _ in active)
    pole = 2 * abs(C @ c)**2 - 2 * abs(S @ c)**2
    return float(arch + prime + pole)


def psi_closed(T, all_events):
    ramp = sum(a * (T - h) for h, a, _ in all_events if h <= T)
    return (8 * (math.cosh(T / 2) - 1) - ramp
            + T / 2 * (float(digamma(0.25)) - math.log(math.pi))
            + F0 - f_exponential(T))


def psi_triangle(T, all_events):
    ramp = sum(a * (T - h) for h, a, _ in all_events if h <= T)
    first = quad(lambda h: (T * (-math.expm1(-h / 2)) - h) * w(h)
                 if h else T / 4 - 0.5,
                 0, T, epsabs=2e-12, epsrel=2e-12)[0]
    tail = quad(lambda h: -T * math.exp(-h / 2) * w(h),
                T, np.inf, epsabs=2e-12, epsrel=2e-12)[0]
    return (8 * (math.cosh(T / 2) - 1) - ramp
            - (math.log(4 * math.pi) + EULER) * T / 2 - first - tail)


def distinct_primes(n):
    ps = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            ps.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        ps.append(n)
    return ps


def b_omega(n, omega):
    answer = np.exp((omega - 0.5) * math.log(n))
    for p in distinct_primes(n):
        answer *= -np.expm1(-2 * omega * math.log(p))
    return answer


def finite_clock_control(rng):
    L, m = 6, 4
    v = rng.normal(size=L) + 1j * rng.normal(size=L)

    def dilate(x):
        out = np.zeros(m * len(x), dtype=complex)
        out[::m] = math.sqrt(m) * x
        return out

    dv = dilate(v)
    return {
        "L": L, "m": m,
        "normalized_haar_isometry_error": abs(float(np.mean(abs(dv)**2)
                                                   - np.mean(abs(v)**2))),
        "braid_max_error": float(np.max(abs(dilate(np.roll(v, 1))
                                              - np.roll(dv, m)))),
        "refinement_max_error": float(np.max(abs(dilate(np.tile(v, 3))
                                                   - np.tile(dv, 3)))),
    }


def local_rational_controls():
    """Exact transcription checks for Appendix A of SWS-007."""
    F = Fraction
    log2_lower3 = 2 * sum((F(1, (2 * j + 1) * 3**(2 * j + 1)) for j in range(3)), F(0))
    log2_lower4 = log2_lower3 + F(2, 7 * 3**7)
    log2_upper3 = log2_lower3 + F(2, 7 * 3**7) / (1 - F(1, 9))
    pi_lower = 16 * (F(1, 5) - F(1, 3 * 5**3)) - F(4, 239)
    pi_upper = (16 * (F(1, 5) - F(1, 3 * 5**3) + F(1, 5 * 5**5))
                - 4 * (F(1, 239) - F(1, 3 * 239**3)))
    gamma_upper = sum((F(1, j) for j in range(1, 33)), F(0)) - 5 * log2_lower4 - F(1, 66)
    exp_lower = sum((F(229, 200)**j / math.factorial(j) for j in range(9)), F(0))
    margin = F(4, 5) * F(6769, 1000) - F(672, 125) - F(1, 1000000)
    return {
        "pi_lower_exceeds_25_over_8": pi_lower > F(25, 8),
        "pi_upper_below_1571_over_500": pi_upper < F(1571, 500),
        "log2_lower_exceeds_277_over_400": log2_lower3 > F(277, 400),
        "log2_upper_below_347_over_500": log2_upper3 < F(347, 500),
        "gamma_upper_below_289_over_500": gamma_upper < F(289, 500),
        "exp_lower_exceeds_pi_upper_bound": exp_lower > F(1571, 500),
        "Gamma_first_term_exceeds_3999_over_1000": F(25600, 6401) > F(3999, 1000),
        "sinh_rank_bound_below_one_millionth": F(1, 6291072) < F(1, 1000000),
        "final_margin_exact_and_above_3_over_100": margin == F(39199, 1000000) and margin > F(3, 100),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rng = np.random.default_rng(2112)
    all_events = events(math.ceil(math.exp(12)))
    residuals = {"gamma_quadrature_vs_series": 0.0,
                 "square_vs_direct_weil": 0.0,
                 "large_scalar_cancellation": 0.0,
                 "box_vs_suzuki_triangle": 0.0,
                 "odd_haar_gamma": 0.0,
                 "embedded_box_horizon_identity": 0.0}
    scans = []
    for A in [1 / 128, 0.125, 0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 6.0]:
        for cells in [16, 32, 64]:
            P, D, Q, G, C, S, active, ge = matrices(A, cells, all_events)
            q_values, q_vectors = eigh(Q)
            ratios = eigh(D, P, eigvals_only=True)
            ratio_witness = float(ratios[-1])
            qmin = float(q_values[0])
            residuals["gamma_quadrature_vs_series"] = max(
                residuals["gamma_quadrature_vs_series"], ge)
            residuals["large_scalar_cancellation"] = max(
                residuals["large_scalar_cancellation"], float(np.max(abs(P - D - Q))))
            box = np.ones(cells) / math.sqrt(cells)
            odd = np.r_[-np.ones(cells // 2), np.ones(cells // 2)] / math.sqrt(cells)
            box_q = float(box @ Q @ box)
            residuals["box_vs_suzuki_triangle"] = max(
                residuals["box_vs_suzuki_triangle"], abs(box_q - psi_closed(2 * A, all_events) / A))
            odd_gamma = (3 * F0 - 4 * f_exponential(A) + f_exponential(2 * A)) / A
            residuals["odd_haar_gamma"] = max(
                residuals["odd_haar_gamma"], abs(float(odd @ G @ odd) - odd_gamma))
            if cells == 32:
                for c in [box, odd, q_vectors[:, 0],
                          rng.normal(size=cells) + 1j * rng.normal(size=cells)]:
                    c = c / np.linalg.norm(c)
                    exact = direct_weil(A, c, C, S, active)
                    residuals["square_vs_direct_weil"] = max(
                        residuals["square_vs_direct_weil"], abs(float(np.vdot(c, Q @ c).real) - exact))
            scans.append({"A": A, "cells": cells, "prime_power_events": len(active),
                          "minimum_Q_Ritz_value": qmin,
                          "maximum_D_over_P_Ritz_value": ratio_witness,
                          "box_Q": box_q, "P_condition_number": float(np.linalg.cond(P))})

    jet_error = 0.0
    event_lookup = {n: a for _, a, n in all_events}
    for n in range(1, 129):
        observed = float(np.imag(b_omega(n, 1e-8j)) / 1e-8)
        jet_error = max(jet_error, abs(observed - 2 * event_lookup.get(n, 0.0)))
    triangle_error = max(abs(psi_closed(t, all_events) - psi_triangle(t, all_events))
                         for t in [0.1, 0.5, math.log(2), 1.0, 2.0, 4.0])

    # Mutations must break an independently specified identity.
    A, cells = 1.0, 32
    P, D, Q, G, C, S, active, _ = matrices(A, cells, all_events)
    box = np.ones(cells) / math.sqrt(cells)
    exact = direct_weil(A, box, C, S, active)
    box_gamma = float(box @ G @ box)
    mutations = {
        "omit_origin_scalar_error": abs(float(box @ Q @ box) + D0 - exact),
        "compressed_shift_gamma_error": box_gamma / 2,
        "omit_triangle_half_error": abs(psi_triangle(1.0, all_events)),
        "prime_jet_half_error_at_2": math.log(2) / math.sqrt(2),
        # The artificial kernel is 4[1-cos(2t)cosh(t/4)]. It has unit
        # coefficients at frequencies +/-2 +/-i/4, not Suzuki's 1/gamma^2
        # weights and not actual zeta zeros. Its diagonal sign kills PSD.
        "fake_off_axis_cosine_kernel_value_at_pi": float(4 * (1 - math.cosh(0.25 * math.pi))),
    }

    # Exact embedding of a fixed step box into larger step-cell intervals.
    horizon = []
    fixed_A, fixed_cells = 0.25, 4
    p0, d0, q0, *_ = matrices(fixed_A, fixed_cells, all_events)
    fixed_box = np.ones(fixed_cells) / math.sqrt(fixed_cells)
    fixed_q = float(fixed_box @ q0 @ fixed_box)
    fixed_p = float(fixed_box @ p0 @ fixed_box)
    fixed_d = float(fixed_box @ d0 @ fixed_box)
    old_M = sum(a for h, a, _ in all_events if h <= 2 * fixed_A)
    for A in [0.25, 0.5, 1.0, 2.0, 4.0, 6.0]:
        increment = 2 * (sum(a for h, a, _ in all_events if h <= 2 * A) - old_M)
        larger_cells = round(2 * A / (2 * fixed_A / fixed_cells))
        larger_P, larger_D, larger_Q, *_ = matrices(A, larger_cells, all_events)
        embedded_box = np.zeros(larger_cells)
        start = (larger_cells - fixed_cells) // 2
        embedded_box[start:start + fixed_cells] = fixed_box
        observed_p = float(embedded_box @ larger_P @ embedded_box)
        observed_d = float(embedded_box @ larger_D @ embedded_box)
        observed_q = float(embedded_box @ larger_Q @ embedded_box)
        residuals["embedded_box_horizon_identity"] = max(
            residuals["embedded_box_horizon_identity"],
            abs(observed_p - fixed_p - increment),
            abs(observed_d - fixed_d - increment), abs(observed_q - fixed_q))
        horizon.append({"A": A, "Q_fixed_box": fixed_q,
                        "Q_from_larger_interval_matrix": observed_q,
                        "D_over_P_fixed_box": (fixed_d + increment) / (fixed_p + increment),
                        "P_fixed_box": fixed_p + increment})

    clock = finite_clock_control(rng)
    rational_checks = local_rational_controls()
    checks = {
        "all_identity_errors_below_1e_minus_8": max(residuals.values()) < 1e-8,
        "triangle_error_below_1e_minus_9": triangle_error < 1e-9,
        "prime_jet_error_below_1e_minus_10": jet_error < 1e-10,
        "clock_errors_below_1e_minus_12": max(v for k, v in clock.items() if k.endswith("error")) < 1e-12,
        "all_positive_mutation_errors_exceed_1e_minus_5": all(
            v > 1e-5 for k, v in mutations.items() if k.endswith("error") or "error_" in k),
        "fake_off_axis_control_is_negative": mutations["fake_off_axis_cosine_kernel_value_at_pi"] < 0,
        "all_nine_exact_rational_controls_pass": all(rational_checks.values()),
        "local_certificate_not_contradicted_by_finite_Ritz_values": all(
            s["minimum_Q_Ritz_value"] >= 0.03 for s in scans if s["A"] == 1 / 128),
    }
    result = {
        "claim_status": "finite floating-point controls and observations; no all-space positivity certificate",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "scipy": scipy.__version__, "platform": platform.platform(),
                        "executable": sys.executable},
        "source_inputs": {"zero_data_used": False, "random_seed": 2112,
                          "maximum_prime_power": all_events[-1][2]},
        "normalization": {"Fourier": "hat(v)(u)=integral v(t)exp(i*u*t)dt",
                          "translation_norm": "whole R after zero extension",
                          "D0": D0, "Gamma_F0": F0},
        "identity_residuals": residuals,
        "prime_first_jet_max_error": jet_error,
        "triangle_max_error": triangle_error,
        "finite_clock": clock,
        "local_certificate_exact_rational_controls": rational_checks,
        "mutation_controls": mutations,
        "checks": checks,
        "finite_Ritz_scans": scans,
        "fixed_box_horizon_observation": horizon,
        "limitations": [
            "No interval arithmetic: these are observations, not rigorous eigenvalue enclosures.",
            "Finite Q Ritz minima bound the true infimum from above.",
            "Finite generalized D/P maxima bound the full compact sign-operator norm from below.",
            "Near-one ratios alone cannot establish positivity; use the cancelled Q and a justified tail.",
            "The analytic local positivity theorem is proved in the accompanying note, not by this scan.",
        ],
    }
    payload = json.dumps(result, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
        print(json.dumps({"output": str(args.output), "checks": checks,
                          "identity_residuals": residuals}, indent=2))
    else:
        print(payload, end="")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
