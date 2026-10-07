"""Exact finite Haar-clock identities; no eigenphase fitting or RH input.

Basis indices are 0-based. ``clock(n)`` sends e_j to e_(j+1 mod n).
The orthonormal coordinate embedding of Haar pullback has coefficients
1/sqrt(p); its range projector is rational, so most checks need no radicals.
All matrices below are deliberately small finite proof fixtures. The functions
do not build an LCM clock automatically.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import json
import math
from pathlib import Path
import random

import sympy as sp


Z = sp.Symbol("z")


def _parameters(p: int, L: int) -> tuple[int, int, int]:
    if not isinstance(p, int) or not sp.isprime(p) or L < 1:
        raise ValueError("p must be prime and L must be positive")
    M = L
    k = 1
    while M % p == 0:
        M //= p
        k += 1
    return p * L, k, M


def clock(n: int) -> sp.Matrix:
    if n < 1:
        raise ValueError("clock length must be positive")
    out = sp.zeros(n)
    for j in range(n):
        out[(j + 1) % n, j] = 1
    return out


def pullback(p: int, L: int) -> sp.Matrix:
    """Isometric pullback in orthonormal Haar coordinate bases."""
    n, _, _ = _parameters(p, L)
    return sp.Matrix(n, L, lambda a, b: 1 / sp.sqrt(p) if a % L == b else 0)


def old_projector(p: int, L: int) -> sp.Matrix:
    n, _, _ = _parameters(p, L)
    return sp.Matrix(n, n, lambda a, b: sp.Rational(1, p) if (a - b) % L == 0 else 0)


def innovation_projector(p: int, L: int) -> sp.Matrix:
    return sp.eye(p * L) - old_projector(p, L)


def ramanujan(q: int, d: int) -> sp.Integer:
    """c_q(d), via the exact divisor/Mobius identity."""
    if q < 1:
        raise ValueError("conductor must be positive")
    return sp.Integer(sum(s * sp.mobius(q // s) for s in sp.divisors(math.gcd(q, d))))


def conductor_projector(n: int, q: int) -> sp.Matrix:
    if q < 1 or n % q:
        raise ValueError("conductor q must divide clock length n")
    return sp.Matrix(n, n, lambda a, b: ramanujan(q, a - b) / n)


def innovation_conductors(p: int, L: int) -> tuple[int, ...]:
    _, k, M = _parameters(p, L)
    return tuple(p**k * int(d) for d in sp.divisors(M))


def difference_basis(p: int, L: int) -> sp.Matrix:
    """Forced rational basis e_(a+bL)-e_(a+(p-1)L), b<p-1."""
    n, _, _ = _parameters(p, L)
    D = sp.zeros(n, L * (p - 1))
    for b in range(p - 1):
        for a in range(L):
            D[a + b * L, a + b * L] = 1
            D[a + (p - 1) * L, a + b * L] = -1
    return D


def innovation_restriction(p: int, L: int) -> sp.Matrix:
    """Coordinate restriction in the explicit nonorthonormal difference basis.

    This is not a square root or a fitted Gram factorization. The first
    L(p-1) rows of D form the identity, hence give its exact left inverse.
    """
    D = difference_basis(p, L)
    return (clock(p * L) * D)[: L * (p - 1), :]


def carry_permutation(p: int, L: int) -> sp.Matrix:
    """Natural n=a+bL order -> tensor lexicographic (a,b), index ap+b."""
    n, _, _ = _parameters(p, L)
    K = sp.zeros(n)
    for a in range(L):
        for b in range(p):
            K[a * p + b, a + b * L] = 1
    return K


def carry_tensor_clock(p: int, L: int) -> sp.Matrix:
    _parameters(p, L)
    boundary = sp.zeros(L)
    boundary[0, L - 1] = 1
    return sp.kronecker_product(clock(L), sp.eye(p)) + sp.kronecker_product(
        boundary, clock(p) - sp.eye(p)
    )


@lru_cache(maxsize=None)
def root_sum(order: int, exponents: tuple[int, ...]) -> sp.Expr:
    """Sum exact powers of a primitive root, reduced modulo Phi_order.

    The return value is a canonical polynomial in z. No complex floating
    approximations or unordered spectral comparisons are used.
    """
    counts = Counter(e % order for e in exponents)
    poly = sp.Poly.from_dict({(e,): c for e, c in counts.items()}, Z, domain=sp.QQ)
    return poly.rem(sp.Poly(sp.cyclotomic_poly(order, Z), Z, domain=sp.QQ)).as_expr()


def character_exponents(p: int, L: int, r: int, j: int) -> tuple[int, ...]:
    n, _, _ = _parameters(p, L)
    if not 0 <= r < p or not 0 <= j < L:
        raise ValueError("character coordinates out of range")
    h = r + p * j
    return tuple((-h * x) % n for x in range(n))


def verify_character_intertwiner(p: int, L: int) -> bool:
    """Entrywise phase identities and exact geometric root sums.

    Character convention is exp(-2*pi*i*h*x/n); C has eigenvalue
    exp(+2*pi*i*h/n). Tensor factorization is into the digit character
    exp(-2*pi*i*r*b/p) and the chirped old mode exp(-2*pi*i*h*a/n).
    Orthogonality is checked once for each character difference modulo n.
    """
    n, _, _ = _parameters(p, L)
    for r in range(p):
        for j in range(L):
            h = r + p * j
            exponents = character_exponents(p, L, r, j)
            for x in range(n):
                a, b = x % L, x // L
                assert (exponents[x] + h * a + r * b * L) % n == 0
                assert (exponents[(x - 1) % n] - exponents[x] - h) % n == 0
            if r:
                # Fiber averages vanish, exactly placing this character in
                # ker(J*) rather than merely sharing an eigenvalue multiset.
                assert root_sum(n, tuple(exponents[b * L] for b in range(p))) == 0
    for delta in range(n):
        assert root_sum(n, tuple(delta * x for x in range(n))) == (n if delta == 0 else 0)
    return True


def crt_labels(p: int, L: int) -> tuple[tuple[int, int, int, int, int], ...]:
    """(c,a,h,r,d), with h=M*c+p^k*a (mod pL), conductor p^k*d."""
    n, k, M = _parameters(p, L)
    out = []
    for c in range(p**k):
        if c % p == 0:
            continue
        for a in range(M):
            h = (M * c + p**k * a) % n
            d = M // math.gcd(a, M)
            out.append((c, a, h, h % p, d))
    return tuple(out)


def verify_clock(p: int, L: int) -> dict:
    n, k, M = _parameters(p, L)
    C = clock(n)
    J = pullback(p, L)
    old = old_projector(p, L)
    E = innovation_projector(p, L)
    assert J.T * J == sp.eye(L)
    assert J * J.T == old
    assert C * J == J * clock(L)
    assert old * old == old and E * E == E
    sectors = [conductor_projector(n, q) for q in innovation_conductors(p, L)]
    assert sum(sectors, sp.zeros(n)) == E
    for i, P in enumerate(sectors):
        assert P * P == P and P.T == P and C * P == P * C
        assert sp.trace(P) == sp.totient(innovation_conductors(p, L)[i])
        for Q in sectors[:i]:
            assert P * Q == sp.zeros(n)
    D = difference_basis(p, L)
    R = innovation_restriction(p, L)
    assert C * D == D * R and E * D == D
    metric = D.T * D
    assert R.T * metric * R == metric
    expected = sp.Poly(sum(Z ** (L * b) for b in range(p)), Z)
    assert R.charpoly(Z).as_poly() == expected
    K = carry_permutation(p, L)
    assert K.T * K == sp.eye(n)
    assert K * C * K.T == carry_tensor_clock(p, L)
    assert verify_character_intertwiner(p, L)
    labels = crt_labels(p, L)
    assert {row[2] for row in labels} == {h for h in range(n) if h % p}
    assert len(labels) == n - L
    counts = Counter((r, d) for _, _, h, r, d in labels)
    for _, a, h, _, d in labels:
        assert n // math.gcd(h, n) == p**k * d
        assert math.gcd(h, M) == math.gcd(a, M)
    for r in range(1, p):
        for d in sp.divisors(M):
            assert counts[(r, d)] == p ** (k - 1) * sp.totient(d)
    return {
        "p": p,
        "L": L,
        "n": n,
        "k": k,
        "M": M,
        "innovation_dimension": n - L,
        "conductors": list(innovation_conductors(p, L)),
        "charpoly": str(expected.as_expr()),
        "per_digit_conductor_counts": [
            {"r": r, "d": d, "count": count}
            for (r, d), count in sorted(counts.items())
        ],
    }


def mutation_controls() -> dict:
    p, L = 3, 4
    n = p * L
    C = clock(n)
    old = old_projector(p, L)
    raw = sp.sqrt(p) * pullback(p, L)
    assert raw.T * raw == p * sp.eye(L)
    raw_range = raw * raw.T
    assert raw_range * raw_range != raw_range
    wrong = sp.Matrix(
        n,
        n,
        lambda a, b: sp.Rational(
            sum(d * abs(sp.mobius(3 // d)) for d in sp.divisors(math.gcd(3, a - b))), n
        ),
    )
    assert wrong * wrong != wrong
    missing = innovation_projector(p, L) - conductor_projector(n, p)
    assert missing.rank() == 6  # conductors 6 and 12, dimensions 2 and 4
    assert C != carry_tensor_clock(p, L)
    rng = random.Random(8008)
    signs = [rng.choice((-1, 1)) for _ in range(n)]
    phase = sp.diag(*signs)
    changed = phase * C * phase.T
    assert changed.charpoly(Z) == C.charpoly(Z)
    assert changed * old != old * changed
    return {
        "raw_count_embedding_isometry": False,
        "raw_count_gram_idempotent": False,
        "absolute_mobius_projector_idempotent": False,
        "pure_prime_only_missing_dimension": int(missing.rank()),
        "omit_carry_permutation_identity": False,
        "phase_seed": 8008,
        "phase_signs": signs,
        "phase_mutation_preserves_charpoly": True,
        "phase_mutation_preserves_old_subspace": False,
    }


def evidence() -> dict:
    return {
        "method": "Exact rational matrices, cyclotomic polynomial remainders, and modular exponent intertwiners",
        "scope": "Finite fixtures verify proved identities; no claim about RH or infinite positivity",
        "cases": [verify_clock(p, L) for p, L in [(2, 1), (3, 1), (2, 3), (2, 6), (3, 4), (3, 6), (5, 2)]],
        "mutations": mutation_controls(),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(evidence(), indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result)
    else:
        print(result, end="")
