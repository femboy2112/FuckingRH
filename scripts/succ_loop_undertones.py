#!/usr/bin/env python3
"""Finite exact probes for SUCC-loop support conductors and harmonic undertones.

Standard library only. No zeta zeros are used. Nothing here proves RH.

Verifies:
  * rational-affine words may compose to identity while having a proper
    congruence support cylinder;
  * Leah's Collatz-side loop is identity on x == 1 (mod 2);
  * the L_N=lcm(1,...,N) tower has log-jump Lambda(N);
  * a residue cylinder mod m has exact-conductor energy phi(q)/m^2;
  * products of distinct-prime wake forms live purely at the product conductor;
  * the primorial wake has a large pointwise interaction crest but zero mean
    interaction over the full CRT clock.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, lcm, log, pi, cos, sin, prod
from collections import defaultdict
from typing import Iterable


@dataclass(frozen=True)
class Affine:
    a: Fraction
    b: Fraction
    name: str = ""

    @staticmethod
    def make(a: int, b: int = 0, d: int = 1, name: str = "") -> "Affine":
        return Affine(Fraction(a, d), Fraction(b, d),
                      name or f"({a}x+{b})/{d}")


def after(f: Affine, g: Affine) -> Affine:
    """Return f o g."""
    return Affine(f.a * g.a, f.a * g.b + f.b, f"{f.name} o {g.name}")


def integrality_cylinder(f: Affine) -> tuple[int, int] | None:
    """Solve f(n) in Z as n == r (mod m), or return None."""
    q = lcm(f.a.denominator, f.b.denominator)
    u = f.a.numerator * (q // f.a.denominator)
    v = f.b.numerator * (q // f.b.denominator)
    g = gcd(abs(u), q)
    if (-v) % g:
        return None
    u //= g
    rhs = (-v) // g
    m = q // g
    if m == 1:
        return 0, 1
    r = (rhs * pow(u % m, -1, m)) % m
    return r, m


def crt_pair(r1: int, m1: int, r2: int, m2: int) -> tuple[int, int] | None:
    g = gcd(m1, m2)
    if (r2 - r1) % g:
        return None
    M = lcm(m1, m2)
    a = m1 // g
    b = m2 // g
    rhs = (r2 - r1) // g
    t = 0 if b == 1 else (rhs * pow(a % b, -1, b)) % b
    return (r1 + m1 * t) % M, M


def word_support(word: Iterable[Affine]):
    """Return support cylinder, final affine map, and prefix cylinders."""
    cur = Affine(Fraction(1), Fraction(0), "id")
    support = (0, 1)
    prefixes = []
    for edge in word:
        cur = after(edge, cur)
        local = integrality_cylinder(cur)
        if local is None:
            return None, cur, prefixes
        support = crt_pair(*support, *local)
        if support is None:
            return None, cur, prefixes
        prefixes.append((cur, local, support))
    return support, cur, prefixes


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def prime_power_base(n: int) -> int | None:
    """Return p if n=p^k (k>=1), otherwise None."""
    if n < 2:
        return None
    if is_prime(n):
        return n
    for p in range(2, int(n**0.5) + 2):
        if not is_prime(p):
            continue
        x = p
        while x < n:
            x *= p
        if x == n:
            return p
    return None


def mangoldt(n: int) -> float:
    p = prime_power_base(n)
    return 0.0 if p is None else log(p)


def lcm_tower(N: int) -> list[int]:
    out = [1]
    L = 1
    for n in range(1, N + 1):
        L = lcm(L, n)
        out.append(L)
    return out


def euler_phi(n: int) -> int:
    out = n
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            out -= out // p
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        out -= out // x
    return out


def exact_conductor_of_character(k: int, M: int) -> int:
    """Conductor of n -> exp(2*pi*i*k*n/M)."""
    return 1 if k % M == 0 else M // gcd(k, M)


def dft(values: list[float]) -> list[complex]:
    M = len(values)
    out = []
    for k in range(M):
        z = 0j
        for n, v in enumerate(values):
            angle = -2.0 * pi * k * n / M
            z += v * complex(cos(angle), sin(angle))
        out.append(z / M)
    return out


def conductor_energy(values: list[float]) -> dict[int, float]:
    M = len(values)
    out: dict[int, float] = defaultdict(float)
    for k, z in enumerate(dft(values)):
        out[exact_conductor_of_character(k, M)] += abs(z) ** 2
    return dict(sorted(out.items()))


def cylinder(m: int, r: int) -> list[float]:
    return [1.0 if n % m == r % m else 0.0 for n in range(m)]


def prime_wake(n: int, p: int) -> float:
    """+1 on -1 mod p, -1 on 0 mod p, zero otherwise."""
    r = n % p
    if r == p - 1:
        return 1.0
    if r == 0:
        return -1.0
    return 0.0


def verify_collatz_loop() -> None:
    word = [
        Affine.make(4, 1, 1, "4x+1"),
        Affine.make(3, 1, 8, "(3x+1)/8"),
        Affine.make(2, -1, 3, "(2x-1)/3"),
    ]
    support, final, prefixes = word_support(word)
    assert final.a == 1 and final.b == 0
    assert support == (1, 2)
    print("Collatz-side loop:")
    print("  algebraic holonomy = identity")
    print("  arithmetic support = x == 1 (mod 2)")
    print("  support cost        = log 2")
    for j, (f, local, cumulative) in enumerate(prefixes, 1):
        print(f"  prefix {j}: {f.a}*x + {f.b}; local={local}; cumulative={cumulative}")


def verify_lcm_mangoldt(N: int = 100) -> None:
    L = lcm_tower(N)
    for n in range(2, N + 1):
        jump = log(L[n] / L[n - 1])
        assert abs(jump - mangoldt(n)) < 1e-12
    print(f"LCM/von-Mangoldt identity verified through N={N}.")


def verify_cylinder_spectrum(max_m: int = 20) -> None:
    for m in range(2, max_m + 1):
        vals = cylinder(m, 0)
        mean = 1.0 / m
        centered = [v - mean for v in vals]
        E = conductor_energy(centered)
        for q in range(2, m + 1):
            if m % q == 0:
                expected = euler_phi(q) / (m * m)
                assert abs(E.get(q, 0.0) - expected) < 1e-10
        assert abs(sum(E.values()) - mean * (1 - mean)) < 1e-10
    print(f"Residue-cylinder spectrum phi(q)/m^2 verified for m<={max_m}.")


def verify_prime_fusion(primes=(2, 3, 5, 7)) -> None:
    for size in range(2, len(primes) + 1):
        ps = primes[:size]
        M = prod(ps)
        vals = [prod(prime_wake(n, p) for p in ps) for n in range(M)]
        E = conductor_energy(vals)
        active = {d: e for d, e in E.items() if e > 1e-10}
        assert set(active) == {M}, (ps, active)
        assert abs(active[M] - (2.0**size) / M) < 1e-10
    print("Distinct-prime wake products verified to fuse to exact product conductor.")


def demo_primorial_crest(primes=(2, 3, 5, 7, 11, 13)) -> None:
    P = prod(primes)
    theta = sum(log(p) for p in primes)
    diag = sum(log(p) ** 2 for p in primes)
    crest = 0.5 * (theta * theta - diag)
    print(f"Primorial P={P}")
    print(f"  theta          = {theta:.12f}")
    print(f"  pair curvature = {crest:.12f}")
    print("  P-1: all wakes +1; P: all wakes -1")

    mean_cross = 0.0
    for n in range(P):
        s = 0.0
        d = 0.0
        for p in primes:
            u = (log(p) / (2.0**0.5)) * prime_wake(n, p)
            s += u
            d += u * u
        mean_cross += s * s - d
    mean_cross /= P
    assert abs(mean_cross) < 1e-10
    print(f"  mean pair curvature on Z/PZ = {mean_cross:.3e} (CRT-flat control)")


def main() -> None:
    verify_collatz_loop()
    verify_lcm_mangoldt()
    verify_cylinder_spectrum()
    verify_prime_fusion()
    demo_primorial_crest()


if __name__ == "__main__":
    main()
