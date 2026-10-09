#!/usr/bin/env python3
"""Independent spatial-Weil / spectral-delay comparison; no zeta zeros used.

The test is a translated compact tent in H^1_0, a domain to which the displayed
smooth-core identity extends by H^1 approximation. Analytic tail bounds are
reported; scipy quadrature estimates are diagnostics, not rigorous intervals.
"""
from __future__ import annotations

import argparse
import json
import math
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.special import digamma


def primes_up_to(n: int) -> list[int]:
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    return np.flatnonzero(sieve).tolist()


def prime_events(n: int) -> list[tuple[int, float]]:
    rows = []
    for p in primes_up_to(n):
        k = p
        while k <= n:
            rows.append((k, math.log(p)))
            k *= p
    return sorted(rows)


def correlation(h: float, width: float) -> float:
    x = abs(h) / width
    if x <= 1:
        return width * (2 / 3 - x * x + x ** 3 / 2)
    if x < 2:
        return width * (2 - x) ** 3 / 6
    return 0.0


def spectral_weight(u: float, width: float) -> float:
    # Fourier transform of (1-|t|/width)_+ is width*sinc(width*u/2)^2.
    return float(width ** 2 * np.sinc(width * u / (2 * np.pi)) ** 4)


def gamma_delay(u: float) -> float:
    return float(math.log(math.pi) - digamma(0.25 + 0.5j * u).real)


def delay(u: float, primes: list[int]) -> float:
    out = gamma_delay(u)
    for p in primes:
        ell, r = math.log(p), p ** -0.5
        poisson = (1 - r * r) / (1 - 2 * r * math.cos(u * ell) + r * r)
        out += ell * (poisson - 1)
    return out


def mass(primes: list[int]) -> float:
    return sum(math.log(p) / (math.sqrt(p) - 1) for p in primes)


def direct_weil(width: float, center: float) -> dict:
    f0 = 2 * width / 3
    m0 = 8 * (math.cosh(width / 2) - 1) / width
    c = m0 * math.cosh(center / 2)
    s = m0 * math.sinh(center / 2)
    poles = 2 * (c * c - s * s)
    events = prime_events(math.floor(math.exp(2 * width)))
    prime_pairing = -2 * sum(lam / math.sqrt(n) * correlation(math.log(n), width)
                             for n, lam in events)

    def origin_integrand(h: float) -> float:
        if h == 0:
            return f0 / 4
        weight = math.exp(-h / 2) / (-math.expm1(-2 * h))
        return weight * (correlation(h, width) - math.exp(-h / 2) * f0)

    low, low_error = quad(origin_integrand, 0, 2 * width,
                          points=[width], epsabs=2e-12, epsrel=2e-12)
    whole_integral = low - f0 * math.atanh(math.exp(-2 * width))
    gamma_pairing = -(math.log(4 * math.pi) + np.euler_gamma) * f0 - 2 * whole_integral
    return {
        "norm_squared": f0,
        "C": c, "S": s, "polar_pairing": poles,
        "prime_pairing": prime_pairing,
        "gamma_origin_pairing": float(gamma_pairing),
        "Q_spatial": float(poles + prime_pairing + gamma_pairing),
        "spatial_quad_error_estimate": float(2 * low_error),
        "active_prime_powers": [n for n, _ in events],
    }


def integrate_delay(primes: list[int], width: float, cutoff: float) -> tuple[float, float, float]:
    values, errors = [], []
    # Resolve the sinc oscillations without asking one adaptive call to find them.
    step = math.pi / width
    edges = np.append(np.arange(0, cutoff, step), cutoff)
    for left, right in zip(edges[:-1], edges[1:]):
        value, error = quad(lambda u: delay(u, primes) * spectral_weight(u, width),
                            float(left), float(right), epsabs=1e-11, epsrel=2e-11,
                            limit=150)
        values.append(value)
        errors.append(error)
    integral = math.fsum(values) / math.pi
    quad_error = math.fsum(errors) / math.pi
    # For U>=1, |tau(u)| <= c_Gamma+4+log(3u)+2M_P;
    # |fhat(u)|^2 <= 16/(width^2*u^4). Integrate this explicit bound.
    c_gamma = gamma_delay(0)
    b = c_gamma + 4 + 2 * mass(primes)
    tail = 16 / (3 * math.pi * width ** 2 * cutoff ** 3) * (
        b + math.log(3 * cutoff) + 1 / 3)
    return integral, quad_error, tail


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--frequency-cutoff", type=float, default=4096.0)
    args = parser.parse_args()
    if args.frequency_cutoff < 1:
        parser.error("frequency cutoff must be at least 1")
    width, center, window = 0.8, 0.3, 1.2
    direct = direct_weil(width, center)
    c_gamma = gamma_delay(0)
    f0 = direct["norm_squared"]
    centered_checks = []
    for bound in [13, 29, 97]:
        primes = primes_up_to(bound)
        assert set(primes_up_to(math.floor(math.exp(2 * window)))) <= set(primes)
        value, error, tail = integrate_delay(primes, width, args.frequency_cutoff)
        q_spectral = direct["polar_pairing"] - value
        residual = abs(q_spectral - direct["Q_spatial"])
        assert residual <= tail + 25 * (error + direct["spatial_quad_error_estimate"]) + 2e-9
        # Independent exact correlation evaluation of all infinite tower tails.
        overlap = 0.0
        for p in primes:
            ell, r = math.log(p), p ** -0.5
            k = 1
            while k * ell < 2 * width:
                overlap += ell * r ** k * correlation(k * ell, width)
                k += 1
        mp = mass(primes)
        energy_prime = 2 * mp * f0 - 2 * overlap
        centered_prime = energy_prime - 2 * mp * f0
        assert abs(centered_prime - direct["prime_pairing"]) < 5e-13
        centered_checks.append({
            "prime_bound": bound, "primes": primes, "M_P": mp,
            "uncentered_prime_energy": energy_prime,
            "prime_bulk_counterterm": 2 * mp * f0,
            "centered_prime_pairing": centered_prime,
            "tau_at_zero": c_gamma + 2 * mp,
            "Q_spectral_truncated": q_spectral,
            "Q_residual": residual,
            "spectral_quad_error_estimate": error,
            "analytic_spectral_tail_bound": tail,
        })
    assert all(centered_checks[j + 1]["uncentered_prime_energy"] >
               centered_checks[j]["uncentered_prime_energy"] for j in range(2))
    wrong_origin = math.log(4) * f0
    wrong_pole = 2 * direct["S"] ** 2
    assert wrong_origin > 0.5 and wrong_pole > 0.02
    # The translated tent exercises both polar channels; their difference is
    # translation invariant, as is the correlation and the completed pairing.
    unshifted = direct_weil(width, 0.0)
    assert abs(unshifted["Q_spatial"] - direct["Q_spatial"]) < 2e-14
    # Adaptive source mutation: adding a fictitious primitive clock at log(6)
    # still produces a causal lossless local filter, but changes the full source.
    # The wider compact test makes that event visible; the first test does not.
    wide = direct_weil(1.1, 0.15)
    phantom_cost = 2 * math.log(6) / math.sqrt(6) * correlation(math.log(6), 1.1)
    fake_r, fake_q = 6 ** -0.5, 0.4 + 0.7j
    fake_w = np.exp(-fake_q * math.log(6))
    fake_transfer = (fake_w - fake_r) / (1 - fake_r * fake_w)
    assert abs(fake_transfer) < 1
    assert phantom_cost > 0.01
    assert wide["Q_spatial"] > 0 and wide["Q_spatial"] - phantom_cost < -0.01
    report = {
        "status": "PASS",
        "claim_scope": "One H1_0 test and three finite prime sets; no global sign or RH certification.",
        "construction_uses_zeta_zeros": False,
        "runtime": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "test": {"name": "translated_compact_tent", "half_width": width,
                 "center": center, "containing_window_half_width": window,
                 "frequency_cutoff": args.frequency_cutoff},
        "spatial": direct,
        "finite_prime_checks": centered_checks,
        "wrong_normalization_controls": {
            "origin_log4pi_instead_of_logpi_error": wrong_origin,
            "omitting_negative_S_channel_error": wrong_pole,
            "translation_invariance_residual": abs(unshifted["Q_spatial"] - direct["Q_spatial"]),
        },
        "adaptive_phantom_primitive_6_control": {
            "status": "FLOATING_POINT_DIAGNOSTIC; exact change given by the displayed correlation formula",
            "test_half_width": 1.1, "test_center": 0.15,
            "baseline_Q": wide["Q_spatial"],
            "spatial_quad_error_estimate": wide["spatial_quad_error_estimate"],
            "added_positive_filter_abs_transfer_at_0_4_plus_0_7i": float(abs(fake_transfer)),
            "exact_formula_for_subtracted_pairing": "2*log(6)/sqrt(6)*F(log(6))",
            "subtracted_pairing": phantom_cost,
            "mutated_Q": wide["Q_spatial"] - phantom_cost,
            "narrow_original_test_correlation_at_log6": correlation(math.log(6), width),
        },
        "error_policy": "Analytic Fourier-tail bound plus non-certified quadrature error estimates; assertions are numerical diagnostics.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print("PASS: spatial Weil / semilocal delay identity, three prime cutoffs, two normalization mutations")
    print(f"Q_spatial={direct['Q_spatial']:.15g}; largest residual="
          f"{max(row['Q_residual'] for row in centered_checks):.3g}")
    print("Each residual is checked against its stated analytic Fourier-tail bound and numerical quadrature estimate.")


if __name__ == "__main__":
    main()
