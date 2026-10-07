#!/usr/bin/env python3
"""Finite Galerkin probe for Suzuki's discrete-conductor Hankel operator.

This is a falsification/diagnostic instrument, not a proof engine by itself.
Every matrix is an honest Galerkin compression, so a rigorously established
matrix norm > 1 would imply the exact finite operator norm is > 1. A computed
norm < 1 is only a lower bound until a Galerkin-tail upper bound is supplied.

Target range: 0 < omega <= 1/2.
"""
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from functools import lru_cache

import numpy as np
from scipy import integrate, special


@dataclass(frozen=True)
class ProbeResult:
    a: float
    omega: float
    cells: int
    conductors: int
    lambda_min: float
    lambda_max: float
    norm_lower: float


def _primes_upto(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.isqrt(n)) + 1):
        if sieve[p]:
            sieve[p * p :: p] = False
    return np.flatnonzero(sieve).astype(int).tolist()


def conductor_weights(nmax: int, omega: float) -> np.ndarray:
    """b_omega(n)=n^(omega-1/2) prod_{p|n}(1-p^(-2 omega))."""
    b = np.zeros(nmax + 1, dtype=float)
    if nmax < 1:
        return b
    n = np.arange(1, nmax + 1, dtype=float)
    b[1:] = n ** (omega - 0.5)
    for p in _primes_upto(nmax):
        b[p::p] *= 1.0 - p ** (-2.0 * omega)
    return b


def k_omega(r: float, omega: float) -> float:
    """Universal causal Archimedean kernel K_omega(r), r>0."""
    if r <= 0.0:
        return 0.0

    if abs(omega - 0.5) <= 2e-15:
        e2 = math.exp(-2.0 * r)
        return 2.0 * (2.0 * e2 - 1.0) / math.sqrt(-math.expm1(-2.0 * r))

    x = math.exp(-r)
    one_minus_x2 = -math.expm1(-2.0 * r)
    pref = 2.0 * math.pi**omega / special.gamma(omega)

    term1 = x ** (2.0 - omega) * one_minus_x2 ** (omega - 1.0)
    aa = 1.5 - omega
    bb = omega
    tail_beta = special.beta(aa, bb) * special.betaincc(aa, bb, x * x)
    term2 = omega * x ** (omega - 1.0) * tail_beta
    g = pref * (term1 - term2)
    return math.exp(-0.5 * r) * g


def f2_omega(
    R: float, omega: float, *, epsabs: float, epsrel: float
) -> float:
    """Second causal primitive int_0^R (R-r) K_omega(r) dr.

    The substitution r=R*y^(1/omega) cancels the r^(omega-1) birth seam.
    """
    if R <= 0.0:
        return 0.0

    c0 = (2.0 * math.pi) ** omega / special.gamma(omega)
    endpoint_limit = c0 * R ** (omega + 1.0) / omega

    def transformed(y: float) -> float:
        if y <= 0.0:
            return endpoint_limit
        r = R * y ** (1.0 / omega)
        dr_dy = (R / omega) * y ** (1.0 / omega - 1.0)
        return (R - r) * k_omega(r, omega) * dr_dy

    value, _err = integrate.quad(
        transformed,
        0.0,
        1.0,
        epsabs=epsabs,
        epsrel=epsrel,
        limit=250,
    )
    return float(value)


def build_galerkin(
    a: float,
    omega: float,
    cells: int,
    *,
    epsabs: float = 2e-11,
    epsrel: float = 2e-10,
) -> tuple[np.ndarray, ProbeResult]:
    if not (a > 1.0):
        raise ValueError("a must be > 1 for the nontrivial finite Hankel probe")
    if not (0.0 < omega <= 0.5):
        raise ValueError("this frontier probe currently targets 0 < omega <= 1/2")
    if cells < 2:
        raise ValueError("cells must be >= 2")

    A = math.log(a)
    h = 2.0 * A / cells
    nmax = int(math.floor(a * a + 2e-13))
    b = conductor_weights(nmax, omega)
    logn = np.zeros(nmax + 1, dtype=float)
    if nmax >= 1:
        logn[1:] = np.log(np.arange(1, nmax + 1, dtype=float))

    @lru_cache(maxsize=None)
    def f2_cached(R_key: float) -> float:
        return f2_omega(
            R_key, omega, epsabs=epsabs, epsrel=epsrel
        )

    # Q is needed only on the 2*cells+1 uniform sum-grid points.
    q = np.zeros(2 * cells + 1, dtype=float)
    for k in range(2 * cells + 1):
        t = -2.0 * A + k * h
        if t <= 0.0:
            continue
        active = min(
            nmax, int(math.floor(math.exp(t) + 2e-13))
        )
        total = 0.0
        for n in range(1, active + 1):
            R = t - logn[n]
            if R > 5e-15:
                # R values come from one deterministic grid. Rounding is
                # far below the requested scalar quadrature tolerance.
                key = round(R, 15)
                total += b[n] * f2_cached(key)
        q[k] = total

    anti = (q[2:] - 2.0 * q[1:-1] + q[:-2]) / h
    H = np.empty((cells, cells), dtype=float)
    for i in range(cells):
        for j in range(cells):
            H[i, j] = anti[i + j]

    # Symmetry is exact algebraically; catch assembly/numerical mistakes.
    asym = float(np.max(np.abs(H - H.T)))
    if asym > 2e-11:
        raise RuntimeError(
            f"Galerkin matrix lost symmetry: max asymmetry={asym:g}"
        )

    eig = np.linalg.eigvalsh(H)
    lmin = float(eig[0])
    lmax = float(eig[-1])
    norm_lower = max(abs(lmin), abs(lmax))
    result = ProbeResult(
        a=a,
        omega=omega,
        cells=cells,
        conductors=nmax,
        lambda_min=lmin,
        lambda_max=lmax,
        norm_lower=norm_lower,
    )
    return H, result


def _csv_floats(s: str) -> list[float]:
    return [
        float(x.strip()) for x in s.split(",") if x.strip()
    ]


def _csv_ints(s: str) -> list[int]:
    return [
        int(x.strip()) for x in s.split(",") if x.strip()
    ]


def _print_result(r: ProbeResult) -> None:
    print(
        f"a={r.a:.12g} omega={r.omega:.12g} cells={r.cells:4d} "
        f"Ncond={r.conductors:5d}  "
        f"lambda_min={r.lambda_min:+.12g}  "
        f"lambda_max={r.lambda_max:+.12g}  "
        f"compression_norm={r.norm_lower:.12g}"
    )


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--a",
        type=float,
        default=1.5,
        help="multiplicative horizon a > 1",
    )
    ap.add_argument(
        "--omega",
        type=float,
        default=0.5,
        help="0 < omega <= 1/2",
    )
    ap.add_argument(
        "--cells",
        type=int,
        default=24,
        help="piecewise-constant Galerkin dimension",
    )
    ap.add_argument(
        "--refine",
        type=str,
        default="",
        help="comma-separated dimensions, e.g. 12,20,32,48",
    )
    ap.add_argument(
        "--scan-omega",
        type=str,
        default="",
        help="comma-separated omega values at fixed a/cells",
    )
    ap.add_argument("--epsabs", type=float, default=2e-11)
    ap.add_argument("--epsrel", type=float, default=2e-10)
    args = ap.parse_args()

    print("# finite Galerkin lower-bound probe")
    print(
        "# NOTE: compression_norm < 1 does NOT certify "
        "full-operator contraction."
    )
    print(
        "#       A rigorously enclosed compression_norm > 1 "
        "would certify failure."
    )

    if args.scan_omega:
        for omega in _csv_floats(args.scan_omega):
            _H, r = build_galerkin(
                args.a,
                omega,
                args.cells,
                epsabs=args.epsabs,
                epsrel=args.epsrel,
            )
            _print_result(r)
        return

    if args.refine:
        for cells in _csv_ints(args.refine):
            _H, r = build_galerkin(
                args.a,
                args.omega,
                cells,
                epsabs=args.epsabs,
                epsrel=args.epsrel,
            )
            _print_result(r)
        return

    _H, r = build_galerkin(
        args.a,
        args.omega,
        args.cells,
        epsabs=args.epsabs,
        epsrel=args.epsrel,
    )
    _print_result(r)


if __name__ == "__main__":
    main()
