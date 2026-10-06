"""Exact factor-cone/current controls. No zero data and no fitted Gram matrices.

Run: python -m scripts.round007_factor_cone
"""
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json

import sympy as sp


def divisors(n):
    if n < 1:
        raise ValueError("positive integer required")
    return [a for a in range(1, n + 1) if n % a == 0]


def factor_pairs(N, remove_units=False):
    lo = 2 if remove_units else 1
    return [(a, b) for a in range(lo, N + 1)
            for b in range(lo, N // a + 1)]


def cone(n, a, exponent=Fraction(1, 2)):
    """Exact 1[log a <= exponent * log n], no floating thresholds."""
    if n < 1 or a < 1 or exponent <= 0:
        raise ValueError("positive arguments and exponent required")
    return int(a ** exponent.denominator <= n ** exponent.numerator)


def active(n, a, exponent=Fraction(1, 2)):
    return int(n % a == 0) * cone(n, a, exponent)


def current(n, a):
    """[F,S] coefficient at |n,a>, F=1[a|n]1[a^2<=n]."""
    return active(n + 1, a) - active(n, a)


def current_decomposition(n, a):
    boundary = int(n + 1 == a * a)
    bulk = cone(n, a) * (int((n + 1) % a == 0) - int(n % a == 0))
    return boundary, bulk


def factor_count(n):
    return sum(1 for a in divisors(n) if 2 <= a and a * a <= n)


def factor_lift(N, remove_units=False, normalized=False):
    """Fiber lift into canonical ab<=N, rows carry (a,b), columns n."""
    pairs = factor_pairs(N, remove_units)
    U = sp.zeros(len(pairs), N)
    for i, (a, b) in enumerate(pairs):
        n = a * b
        U[i, n - 1] = 1 / sp.sqrt(len(divisors(n))) if normalized else 1
    return pairs, U


def swap_matrix(pairs):
    index = {v: k for k, v in enumerate(pairs)}
    R = sp.zeros(len(pairs))
    for j, (a, b) in enumerate(pairs):
        R[index[b, a], j] = 1
    return R


def coordinate_incidence(N, remove_units=False):
    """Nearest-coordinate edges in the canonical product cone, forced unit weights."""
    pairs, U = factor_lift(N, remove_units)
    index = {v: k for k, v in enumerate(pairs)}
    edges = [(v, w) for v in pairs for w in ((v[0] + 1, v[1]),
                                            (v[0], v[1] + 1)) if w in index]
    B = sp.zeros(len(edges), len(pairs))
    for j, (v, w) in enumerate(edges):
        B[j, index[v]] = -1
        B[j, index[w]] = 1
    return pairs, edges, B, U


def compressed_coordinate_energy(N, remove_units=False):
    _, _, B, U = coordinate_incidence(N, remove_units)
    D = B * U
    return D.T * D


def factor_graph_offdiagonal(n, m, remove_units=False):
    if not 1 <= n < m:
        raise ValueError("require 1 <= n < m")
    h = m - n
    allowed = n % h == 0
    if remove_units:
        allowed = allowed and h >= 2 and n // h >= 2
    return -2 * int(allowed)


def same_factor_lift(N, unit=False):
    """Unnormalized active lift in ambient carrier x factor; enough outgoing rows."""
    labels = range(1 if unit else 2, isqrt(N) + 1)
    rows = [(n, a) for n in range(1, N + 2) for a in labels]
    index = {v: i for i, v in enumerate(rows)}
    L = sp.zeros(len(rows), N)
    S = sp.zeros(len(rows))
    for n, a in rows:
        if n <= N:
            L[index[n, a], n - 1] = active(n, a)
            S[index[n + 1, a], index[n, a]] = 1
    return rows, L, S


def same_factor_hop(n, h):
    return [a for a in divisors(gcd(n, h)) if a > 1 and a * a <= n]


def hyperbola_sum(N, f, g):
    r = isqrt(N)
    F = lambda x: sum(f(a) for a in range(1, x + 1))
    G = lambda x: sum(g(b) for b in range(1, x + 1))
    return (sum(f(a) * G(N // a) for a in range(1, r + 1))
            + sum(g(b) * F(N // b) for b in range(1, r + 1)) - F(r) * G(r))


def evidence():
    N = 24
    full = compressed_coordinate_energy(N)
    interior = compressed_coordinate_energy(N, True)
    boundary = []
    bulk = []
    for n in range(1, 100):
        for a in range(2, 11):
            b, v = current_decomposition(n, a)
            assert current(n, a) == b + v
            if b:
                boundary.append([n, a, b])
            if v:
                bulk.append([n, a, v])
    return {
        "status": "exact finite controls only; RH remains open",
        "canonical_horizon": N,
        "factor_dimension": len(factor_pairs(N)),
        "interior_factor_dimension": len(factor_pairs(N, True)),
        "ambient_square_boundary_examples": boundary,
        "divisibility_bulk_examples": bulk,
        "full_nearest_carrier_offdiagonal": [int(full[n - 1, n]) for n in range(1, N)],
        "interior_nearest_carrier_offdiagonal": [int(interior[n - 1, n]) for n in range(1, N)],
        "long_hop_examples": [{"n": n, "h": h, "preserved_factors": same_factor_hop(n, h)}
                              for n, h in [(12, 1), (12, 2), (12, 3), (36, 6)]],
        "factor_count": [{"n": n, "d": len(divisors(n)), "c": factor_count(n)}
                         for n in [2, 4, 8, 16, 18, 32]],
        "geometry_preserving_amplitude_exponents": ["0", "1/4", "1/2", "1"],
        "n16_fiber_square_scale": {str(b): str(sp.Integer(16) ** (-2 * b))
                                  for b in [sp.Rational(0), sp.Rational(1, 4),
                                            sp.Rational(1, 2), sp.Rational(1)]},
        "cone_exponent_mutation": {
            str(c): [[n, a] for n in range(1, 100) for a in range(2, 8)
                     if cone(n + 1, a, c) != cone(n, a, c)]
            for c in [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)]},
    }


if __name__ == "__main__":
    path = Path(__file__).resolve().parents[1] / "research/astra_round_007/evidence/factor_cone.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(evidence(), indent=2) + "\n")
    print(f"Exact factor-cone evidence written to {path}")
