#!/usr/bin/env python3
"""Direct evaluator for Masatoshi Suzuki's RH-equivalent function Psi(t).

Primary source:
  M. Suzuki, J. London Math. Soc. 108 (2023), Eq. (1.1), Theorem 1.7.

RH iff Psi(t) >= 0 for every real t.

This is a finite-wavefront baseline evaluator, not a proof.
"""
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Iterable
import mpmath as mp


@dataclass(frozen=True)
class PrimePowerEvent:
    n: int
    prime: int

    @property
    def von_mangoldt(self) -> mp.mpf:
        return mp.log(self.prime)

    @property
    def log_n(self) -> mp.mpf:
        return mp.log(self.n)


def primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start:n + 1:p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if is_prime[i]]


def prime_power_events_up_to(n_max: int) -> list[PrimePowerEvent]:
    events: list[PrimePowerEvent] = []
    for p in primes_up_to(n_max):
        q = p
        while q <= n_max:
            events.append(PrimePowerEvent(q, p))
            if q > n_max // p:
                break
            q *= p
    events.sort(key=lambda e: e.n)
    return events


def psi_suzuki(
    t: float | mp.mpf,
    *,
    dps: int = 50,
    events: Iterable[PrimePowerEvent] | None = None,
) -> mp.mpf:
    """Evaluate Suzuki's even function Psi(t) from its prime/Archimedean formula."""
    with mp.workdps(dps):
        tt = abs(mp.mpf(t))
        if tt == 0:
            return mp.mpf("0")

        n_max = int(mp.floor(mp.e**tt))
        evs = list(events) if events is not None else prime_power_events_up_to(n_max)

        prime_ramp = mp.mpf("0")
        for event in evs:
            if event.n > n_max:
                break
            prime_ramp += (
                event.von_mangoldt
                / mp.sqrt(event.n)
                * (tt - event.log_n)
            )

        pole_term = 4 * (mp.e**(tt / 2) + mp.e**(-tt / 2) - 2)
        c = mp.pi**2 + 8 * mp.catalan
        gamma_linear = (
            tt / 2 * (mp.digamma(mp.mpf(1) / 4) - mp.log(mp.pi))
        )
        lerch_term = mp.mpf(1) / 4 * (
            c
            - mp.e**(-tt / 2)
            * mp.lerchphi(mp.e**(-2 * tt), 2, mp.mpf(1) / 4)
        )
        return pole_term - prime_ramp + gamma_linear + lerch_term


def screw_kernel(t: float, u: float, *, dps: int = 50) -> mp.mpf:
    """Krein screw kernel G_g for g=-Psi."""
    return (
        psi_suzuki(t, dps=dps)
        + psi_suzuki(u, dps=dps)
        - psi_suzuki(t - u, dps=dps)
    )


def active_horizon(t: float | mp.mpf) -> int:
    """Largest integer visible to Suzuki's moving prime wavefront at |t|."""
    return int(mp.floor(mp.e**abs(mp.mpf(t))))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("t", nargs="*", type=str)
    parser.add_argument("--dps", type=int, default=50)
    parser.add_argument("--events", action="store_true")
    args = parser.parse_args()

    ts = [mp.mpf(x) for x in args.t] if args.t else [
        mp.mpf("0"), mp.mpf("0.1"), mp.mpf("0.5"), mp.log(2),
        mp.mpf("1"), mp.mpf("2"), mp.mpf("3"), mp.mpf("5"),
    ]

    with mp.workdps(args.dps):
        max_t = max(abs(t) for t in ts)
        evs = prime_power_events_up_to(active_horizon(max_t))
        for t in ts:
            print(
                f"t={mp.nstr(t, 20):>22}  "
                f"horizon={active_horizon(t):>8}  "
                f"Psi={mp.nstr(psi_suzuki(t, dps=args.dps, events=evs), 35)}"
            )
        if args.events:
            for event in evs:
                print(
                    f"event n={event.n:<8} p={event.prime:<8} "
                    f"t=log(n)={mp.nstr(event.log_n, 25)}"
                )


if __name__ == "__main__":
    main()
