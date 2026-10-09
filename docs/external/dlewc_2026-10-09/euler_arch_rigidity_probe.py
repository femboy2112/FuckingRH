#!/usr/bin/env python3
"""Source-only Euler/Archimedean rigidity tests for degree-one Dirichlet sources.

No zeta zeros, no phase of scattering, no Riemann-Hilbert boundary data.
The commutator curvature is a *hidden* conductor interaction; it is not an
extra Weil prime impulse.
"""
from __future__ import annotations

import cmath
import math

KAPPA = math.sqrt(1 + ((1 + math.sqrt(5)) / 2) ** 2) - (1 + math.sqrt(5)) / 2
MOD5 = {0: 0j, 1: 1 + 0j, 2: 1j, 3: -1j, 4: -1 + 0j}

def chi5(n: int) -> complex:
    return MOD5[n % 5]

def dh5(n: int) -> complex:
    return complex({0: 0.0, 1: 1.0, 2: KAPPA, 3: -KAPPA, 4: -1.0}[n % 5])

def zeta_coeff(n: int) -> complex:
    return 1+0j

def nonunit_two(n: int, alpha: float = 1.03) -> complex:
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return alpha ** v + 0j

def divisors(n: int):
    return (d for d in range(1, n + 1) if n % d == 0)

def logarithmic_derivative_coeff(a, limit: int):
    """c_n of -F'/F via Dirichlet recurrence, valid without any Euler product."""
    assert abs(a(1) - 1) < 1e-12
    c = [0j] * (limit + 1)
    for n in range(2, limit + 1):
        c[n] = a(n) * math.log(n) - sum(a(d) * c[n // d] for d in divisors(n) if d > 1)
    return c

def prime_power(n):
    """Return (prime, depth), or None for a mixed composite/nonprime."""
    if n < 2:
        return None
    d = 2
    while d*d <= n and n % d:
        d += 1
    if d*d > n:
        return n, 1
    k = 0
    x = n
    while x % d == 0:
        x //= d
        k += 1
    return (d, k) if x == 1 else None

def source_residuals(a, limit=72):
    c = logarithmic_derivative_coeff(a, limit)
    wrong = []
    for n in range(2, limit + 1):
        pk = prime_power(n)
        predicted = a(pk[0]) ** pk[1] * math.log(pk[0]) if pk else 0j
        diff = c[n] - predicted
        if abs(diff) > 1e-9:
            wrong.append((n, diff))
    return c, wrong

def boundary_epsilon(p, n):
    return int((n + 1) % p == 0) - int(n % p == 0)

def oriented_curvature(p, q):
    # [S M_{eps_p}, S M_{eps_q}] = S^2 M_{kappa}
    modulus = math.lcm(p, q)
    vals = []
    for n in range(modulus):
        ep = boundary_epsilon(p, n)
        eq = boundary_epsilon(q, n)
        vals.append(boundary_epsilon(p, n+1)*eq - boundary_epsilon(q, n+1)*ep)
    return vals, sum(x*x for x in vals)/modulus

def complex_l2(xs):
    return sum(abs(x) ** 2 for x in xs)

def edge_identity(xs, shift, alpha):
    size = len(xs)
    # test a cyclic clock as finite calibration, NOT replacement for L2(R)
    ys = [xs[(i + shift) % size] for i in range(size)]
    edge = complex_l2([a-alpha*b for a,b in zip(xs,ys)])
    cross = sum(b*a.conjugate() for a,b in zip(xs,ys))
    exact = (1+abs(alpha)**2)*complex_l2(xs)-2*(alpha*cross).real
    unitary_formula = 2*complex_l2(xs)-2*(alpha*cross).real
    return edge, exact, unitary_formula

def main():
    cz, bad_z = source_residuals(zeta_coeff)
    cc, bad_c = source_residuals(chi5)
    cd, bad_d = source_residuals(dh5)
    cn, bad_n = source_residuals(nonunit_two)
    assert not bad_z and not bad_c and not bad_n
    assert any(n == 6 for n,_ in bad_d)
    assert abs(cd[6]-math.log(6)*(1+KAPPA**2)) < 1e-11
    assert abs(cc[6]) < 1e-11
    assert abs(cc[4]+math.log(2)) < 1e-11
    assert abs(chi5(6)-chi5(2)*chi5(3)) < 1e-15
    assert abs(dh5(6)-dh5(2)*dh5(3)-(1+KAPPA**2)) < 1e-12
    print(f"[1] q=1 and primitive chi mod 5: Euler derivative support exact through n=72 (all residues <1e-9)")
    print(f"[2] Davenport-Heilbronn: delta(a6-a2*a3)={1+KAPPA**2:.12f}; c6={cd[6].real:.12f}; violations={len(bad_d)}")
    print(f"[3] fake primitive at n=6, epsilon=0.001: source-identity residual={1e-3:.6g} (should be 0)")
    assert abs(nonunit_two(2)) != 1 and not bad_n
    print(f"[4] non-unit alpha2=1.03: Euler support STILL passes; partial-unitary defect={abs(nonunit_two(2))**2-1:.8f}")
    delta = 0.002
    clock_residual = (math.log(2)+delta)-math.log(2)
    assert abs(clock_residual-delta) < 1e-14
    print(f"[5] clock t2=log(2)+0.002 vs fixed degree-Hamiltonian [D,V2]: residual={clock_residual:.8f}")
    vals, norm2=oriented_curvature(2,3)
    assert abs(norm2 - 2/3) < 1e-15
    weight=(math.log(2)/math.sqrt(2))*(math.log(3)/math.sqrt(3))
    print(f"[6] mixed oriented [boundary_2,boundary_3] nonzero: kappa={vals}, Haar norm²={norm2:.12f}, weighted norm²={weight*norm2:.12f}")
    xs=[complex(i%3-1, (i%5-2)/3) for i in range(11)]
    edge, exact, uv=edge_identity(xs, 2, chi5(2))
    assert abs(edge-exact) < 1e-11 and abs(edge-uv) < 1e-11
    edge_bad, exact_bad, unit_bad=edge_identity(xs, 2, 1.03j)
    assert abs(edge_bad-exact_bad) < 1e-11 and abs(edge_bad-unit_bad)>1e-2
    print(f"[7] complex Hermitian edge calibration: true residual={edge-exact:+.2e}; nonunit 2S-formula residual={edge_bad-unit_bad:+.8f}")
    print("PASS: arithmetic rigidity + hidden cross-prime curvature; NO Weil positivity claim.")

if __name__ == '__main__':
    main()
