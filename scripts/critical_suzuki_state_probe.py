#!/usr/bin/env python3
"""
Diagnostics for the discrete-conductor / Suzuki state-space program.

Checks, without using nontrivial zero locations:
  * the exact critical Archimedean profile and modal expansion;
  * the critical Gamma-ratio Laplace transform;
  * the inverse-SUCC modal sum rule;
  * the exact conductor Dirichlet factor zeta(s)/zeta(s+1);
  * completed critical factorization xi(s)/xi(s+1);
  * critical conductor mean/residual;
  * general subcritical Archimedean pole residues/signs;
  * conductor discrepancy at delta=1/2-omega.

This script is diagnostic. It does not prove RH.
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


def totients(nmax: int) -> list[int]:
    phi = list(range(nmax + 1))
    for p in range(2, nmax + 1):
        if phi[p] == p:
            for m in range(p, nmax + 1, p):
                phi[m] -= phi[m] // p
    return phi


def central_binomial_coeff(m: int) -> mp.mpf:
    return mp.binomial(2 * m, m) / mp.power(4, m)


def a_mode(m: int) -> mp.mpf:
    assert m >= 1
    return 2 * central_binomial_coeff(m - 1) - central_binomial_coeff(m)


def gcrit(x):
    x = mp.mpf(x)
    return 2 * x ** (-mp.mpf("0.5")) * (2 * x * x - 1) / mp.sqrt(1 - x * x)


def Kcrit(t):
    t = mp.mpf(t)
    return 2 * (2 * mp.e ** (-2 * t) - 1) / mp.sqrt(1 - mp.e ** (-2 * t))


def Kcrit_modal(t, M: int):
    t = mp.mpf(t)
    return -2 + 2 * mp.fsum(a_mode(m) * mp.e ** (-2 * m * t) for m in range(1, M + 1))


def Gcrit(s):
    s = mp.mpc(s)
    return (
        mp.sqrt(mp.pi)
        * (s - 1)
        / (s + 1)
        * mp.gamma(s / 2)
        / mp.gamma((s + 1) / 2)
    )


def Gcrit_modal(s, M: int):
    s = mp.mpc(s)
    return -2 / s + 2 * mp.fsum(a_mode(m) / (s + 2 * m) for m in range(1, M + 1))


def conductor_A(s):
    s = mp.mpc(s)
    return mp.zeta(s) / mp.zeta(s + 1)


def Gomega(s, omega):
    s = mp.mpc(s)
    omega = mp.mpf(omega)
    delta = mp.mpf("0.5") - omega
    return (
        mp.pi**omega
        * (s + delta)
        * (s + delta - 1)
        / ((s + 1 - delta) * (s - delta))
        * mp.gamma((s + delta) / 2)
        / mp.gamma((s + 1 - delta) / 2)
    )


def kappa0(omega):
    omega = mp.mpf(omega)
    return (
        2
        * omega
        * (1 - 2 * omega)
        * mp.pi ** (omega - mp.mpf("0.5"))
        * mp.gamma(mp.mpf("0.5") - omega)
    )


def kappam(omega, m: int):
    omega = mp.mpf(omega)
    return (
        mp.pi ** (omega - 1)
        * mp.sin(mp.pi * omega)
        * mp.gamma(m - omega)
        / mp.factorial(m - 1)
        * (2 * m + 1)
        / (m + mp.mpf("0.5") - omega)
    )


def b_delta_from_phi(n: int, phi_n: int, delta: float) -> mp.mpf:
    """
    For delta=0 this reduces to phi(n)/n.
    General b_delta is computed multiplicatively from n's prime support,
    using trial factorization adequate for diagnostic sizes.
    """
    d = mp.mpf(delta)
    x = n
    p = 2
    prod = mp.mpf(1)
    while p * p <= x:
        if x % p == 0:
            prod *= 1 - mp.power(p, -1 + 2 * d)
            while x % p == 0:
                x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        prod *= 1 - mp.power(x, -1 + 2 * d)
    return mp.power(n, -d) * prod


def check_critical_archimedean():
    print("=== exact critical Archimedean kernel ===")
    for t in [mp.mpf("0.02"), mp.mpf("0.1"), mp.mpf("0.7"), mp.mpf("2")]:
        exact = Kcrit(t)
        for M in [10, 100, 1000]:
            approx = Kcrit_modal(t, M)
            if M == 1000:
                print(
                    f"t={mp.nstr(t, 5)}  exact={mp.nstr(exact, 16)}  "
                    f"M=1000 error={mp.nstr(approx-exact, 8)}"
                )

    print("\n=== critical Laplace/Gamma ratio ===")
    for s in [mp.mpf("1.2"), mp.mpf("2"), mp.mpf("3"), mp.mpc(1, 0.7)]:
        integ = mp.quad(lambda t: mp.e ** (-s * t) * Kcrit(t), [0, 1, mp.inf])
        print(
            f"s={s}: integral-Gamma={mp.nstr(integ-Gcrit(s), 8)}"
        )

    print("\n=== inverse-SUCC completion sum rule ===")
    for M in [10, 100, 1000, 10000]:
        val = mp.fsum(a_mode(m) / (2 * m + 1) for m in range(1, M + 1))
        print(f"M={M:5d}: sum={mp.nstr(val, 18)}  deficit={mp.nstr(1-val, 8)}")


def check_critical_factorization():
    print("\n=== critical conductor x Archimedean = completed scattering ===")
    for s in [mp.mpf("1.2"), mp.mpf("2"), mp.mpf("3"), mp.mpc(1.3, 0.4)]:
        lhs = conductor_A(s) * Gcrit(s)
        rhs = xi(s) / xi(s + 1)
        print(
            f"s={s}: error={mp.nstr(lhs-rhs, 8)}"
        )

    c = 1 / mp.zeta(2)
    print("\n=== mean completion ===")
    for s in [mp.mpf("0.3"), mp.mpf("1"), mp.mpf("2")]:
        if s == 1:
            # removable limit of G/(s-1)
            val = mp.pi / 2
        else:
            val = Gcrit(s) / (s - 1)
        direct = mp.quad(
            lambda t: mp.e ** (-s * t) * 2 * mp.sqrt(1 - mp.e ** (-2 * t)),
            [0, 1, mp.inf],
        )
        print(f"s={s}: inverse-Laplace check={mp.nstr(val-direct, 8)}")
    print("c=1/zeta(2) =", mp.nstr(c, 18))


def check_conductor_summatory(Nmax: int = 200000):
    print("\n=== critical conductor mean/residual ===")
    phi = totients(Nmax)
    c = 1 / mp.zeta(2)
    S = mp.mpf(0)
    sample = {10, 100, 1000, 10000, 100000, Nmax}
    for n in range(1, Nmax + 1):
        S += mp.mpf(phi[n]) / n
        if n in sample:
            E = S - c * n
            print(
                f"N={n:7d}: E={mp.nstr(E, 12)}  "
                f"E/log N={mp.nstr(E/mp.log(max(n,2)), 10)}"
            )

    print("\n=== subcritical conductor discrepancy ===")
    for delta in [0.1, 0.2, 0.3, 0.4]:
        zeta_d = mp.zeta(2 - 2 * delta)
        C = 1 / ((1 - delta) * zeta_d)
        S = mp.mpf(0)
        max_ratio = mp.mpf(0)
        for n in range(1, Nmax + 1):
            S += b_delta_from_phi(n, phi[n], delta)
            if n >= 100:
                E = S - C * mp.power(n, 1 - delta)
                ratio = abs(E) / mp.power(n, delta)
                max_ratio = max(max_ratio, ratio)
        E = S - C * mp.power(Nmax, 1 - delta)
        print(
            f"delta={delta:.1f}: E(N)={mp.nstr(E, 12)}  "
            f"E/N^delta={mp.nstr(E/mp.power(Nmax,delta), 10)}  "
            f"max |E|/N^delta (N>=100)={mp.nstr(max_ratio, 10)}"
        )


def check_subcritical_modes():
    print("\n=== subcritical Archimedean poles/residues ===")
    for omega in [0.1, 0.25, 0.4]:
        om = mp.mpf(omega)
        delta = mp.mpf("0.5") - om
        eps = mp.mpf("1e-9")
        res0 = eps * Gomega(delta + eps, om)
        print(
            f"omega={omega:.2f}, delta={mp.nstr(delta,6)}: "
            f"res unstable={mp.nstr(res0, 14)}, "
            f"formula={mp.nstr(-kappa0(om),14)}"
        )
        for m in [1, 2, 3]:
            pole = -(delta + 2 * m)
            res = eps * Gomega(pole + eps, om)
            print(
                f"  m={m}: res={mp.nstr(res, 14)}, "
                f"formula={mp.nstr(kappam(om,m),14)}"
            )


def main():
    check_critical_archimedean()
    check_critical_factorization()
    check_subcritical_modes()
    # Factorization in b_delta_from_phi is O(N sqrt N) worst-case,
    # so keep default moderate for a portable repo diagnostic.
    check_conductor_summatory(20000)


if __name__ == "__main__":
    main()
