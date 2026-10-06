#!/usr/bin/env python3
"""
Zero-free diagnostics for the SUCC-lightcone gain cocycle.

Builds Lambda(n), psi(n), LCM refinement ratios b_n, local gains
g_n = exp((Lambda(n)-1)/2), and cumulative gain
G_N = exp((psi(N)-N)/2) without using zeta zeros.

This is a diagnostic/reproduction script, not an RH proof.
"""

from __future__ import annotations
import math
from typing import List


def spf_sieve(n: int) -> List[int]:
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, int(n**0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def von_mangoldt_table(nmax: int) -> List[float]:
    spf = spf_sieve(nmax)
    lam = [0.0] * (nmax + 1)
    for n in range(2, nmax + 1):
        p = spf[n]
        x = n
        while x % p == 0:
            x //= p
        if x == 1:
            lam[n] = math.log(p)
    return lam


def main(nmax: int = 100_000) -> None:
    lam = von_mangoldt_table(nmax)
    psi = 0.0
    logG = 0.0
    max_identity_error = 0.0

    samples = {10, 100, 1000, 10_000, nmax}

    print("N        psi(N)-N        log G_N          critical ratio")
    print("-" * 67)

    for n in range(1, nmax + 1):
        psi += lam[n]

        local_log_gain = 0.5 * (lam[n] - 1.0)
        logG += local_log_gain

        exact_logG = 0.5 * (psi - n)
        max_identity_error = max(max_identity_error, abs(logG - exact_logG))

        if n in samples:
            denom = math.sqrt(n) * (math.log(max(n, 2)) ** 2)
            ratio = abs(psi - n) / denom
            print(f"{n:<8d} {psi-n:>14.6f} {logG:>14.6f} {ratio:>18.6g}")

    print()
    print(f"max |sum local log-gain - (psi-N)/2| = {max_identity_error:.3e}")

    print("\nFirst local gain events:")
    for n in range(1, min(nmax, 30) + 1):
        g = math.exp(0.5 * (lam[n] - 1.0))
        tag = "prime-power" if lam[n] else "vacuum-only"
        print(f"n={n:2d}  Lambda={lam[n]:.9f}  g={g:.9f}  {tag}")


if __name__ == "__main__":
    main()
