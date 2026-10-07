#!/usr/bin/env python3
"""
Hostile controls for the co-moving Suzuki / conductor frame.

Checks without using nontrivial zero locations:
  1. transported conductor convolution
       b_tilde_delta = (mu/id) * n^(-2 delta);
  2. shifted arithmetic Dirichlet factor
       sum b_tilde_delta(n) n^(-s) = zeta(s+2delta)/zeta(s+1);
  3. shifted arithmetic * shifted Archimedean = xi(s+2delta)/xi(s+1);
  4. meromorphic all-pass identity B_delta(s) B_delta(-s) = 1;
  5. monotone decrease of individual conductor weights as delta increases.

This is a diagnostic script. It does not prove RH.
"""

from __future__ import annotations

import math
import mpmath as mp

mp.mp.dps = 60


def xi(s):
    s = mp.mpc(s)
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def prime_support(n: int) -> list[int]:
    x = n
    out: list[int] = []
    p = 2
    while p * p <= x:
        if x % p == 0:
            out.append(p)
            while x % p == 0:
                x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        out.append(x)
    return out


def mobius(n: int) -> int:
    if n == 1:
        return 1
    x = n
    count = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            exponent = 0
            while x % p == 0:
                x //= p
                exponent += 1
            if exponent > 1:
                return 0
            count += 1
        p = 3 if p == 2 else p + 2
    if x > 1:
        count += 1
    return -1 if count % 2 else 1


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def b_delta(n: int, delta) -> mp.mpf:
    delta = mp.mpf(delta)
    value = mp.power(n, -delta)
    for p in prime_support(n):
        value *= 1 - mp.power(p, -1 + 2 * delta)
    return value


def b_tilde(delta, n: int) -> mp.mpf:
    delta = mp.mpf(delta)
    return b_delta(n, delta) * mp.power(n, -delta)


def b_tilde_convolution(delta, n: int) -> mp.mpf:
    delta = mp.mpf(delta)
    return mp.fsum(
        mp.mpf(mobius(d)) / d * mp.power(n // d, -2 * delta)
        for d in divisors(n)
    )


def B(delta, s):
    delta = mp.mpf(delta)
    s = mp.mpc(s)
    return xi(s + delta) / xi(s + 1 - delta)


def A_tilde(delta, s):
    delta = mp.mpf(delta)
    s = mp.mpc(s)
    return mp.zeta(s + 2 * delta) / mp.zeta(s + 1)


def G_tilde(delta, s):
    delta = mp.mpf(delta)
    s = mp.mpc(s)
    return (
        mp.power(mp.pi, mp.mpf("0.5") - delta)
        * (s + 2 * delta)
        * (s + 2 * delta - 1)
        / ((s + 1) * s)
        * mp.gamma((s + 2 * delta) / 2)
        / mp.gamma((s + 1) / 2)
    )


def B_tilde(delta, s):
    delta = mp.mpf(delta)
    s = mp.mpc(s)
    return xi(s + 2 * delta) / xi(s + 1)


def derivative_log_b(delta, n: int) -> mp.mpf:
    delta = mp.mpf(delta)
    result = -mp.log(n)
    for p in prime_support(n):
        q = mp.power(p, -1 + 2 * delta)
        result -= 2 * mp.log(p) * q / (1 - q)
    return result


def check_convolution():
    print("=== transported conductor convolution ===")
    worst = mp.mpf(0)
    for delta in map(mp.mpf, ["0", "0.1", "0.23", "0.4"]):
        for n in range(1, 101):
            err = abs(b_tilde(delta, n) - b_tilde_convolution(delta, n))
            worst = max(worst, err)
    print("max n<=100 error:", mp.nstr(worst, 8))


def check_dirichlet():
    print("\\n=== shifted arithmetic Dirichlet factor ===")
    for delta in map(mp.mpf, ["0.1", "0.23", "0.4"]):
        s = mp.mpc("1.7", "0.6")
        exact = A_tilde(delta, s)
        for N in [100, 1000, 10000]:
            approx = mp.fsum(
                b_tilde(delta, n) / mp.power(n, s)
                for n in range(1, N + 1)
            )
            if N == 10000:
                print(
                    "delta=", mp.nstr(delta, 4),
                    "N=10000 truncation error=", mp.nstr(abs(approx - exact), 8),
                )


def check_completion():
    print("\\n=== shifted completion identity ===")
    for delta in map(mp.mpf, ["0.1", "0.23", "0.4"]):
        s = mp.mpc("1.7", "0.6")
        err = abs(A_tilde(delta, s) * G_tilde(delta, s) - B_tilde(delta, s))
        print("delta=", mp.nstr(delta, 4), "error=", mp.nstr(err, 8))


def check_allpass():
    print("\\n=== meromorphic all-pass identity ===")
    for delta in map(mp.mpf, ["0", "0.1", "0.3", "0.49"]):
        s = mp.mpc("1.2", "0.8")
        err = abs(B(delta, s) * B(delta, -s) - 1)
        print("delta=", mp.nstr(delta, 4), "error=", mp.nstr(err, 8))


def check_monotonicity():
    print("\\n=== conductor-weight monotonicity ===")
    worst_derivative = -mp.inf
    for delta in map(mp.mpf, ["0", "0.1", "0.25", "0.4", "0.49"]):
        vals = []
        for n in range(2, 501):
            d = derivative_log_b(delta, n)
            vals.append(d)
            if d >= 0:
                raise AssertionError((delta, n, d))
        worst_derivative = max(worst_derivative, max(vals))
        print(
            "delta=", mp.nstr(delta, 4),
            "largest d/delta log b among 2<=n<=500 =",
            mp.nstr(max(vals), 8),
        )
    print("all sampled derivatives strictly negative")


def main():
    check_convolution()
    check_dirichlet()
    check_completion()
    check_allpass()
    check_monotonicity()


if __name__ == "__main__":
    main()
