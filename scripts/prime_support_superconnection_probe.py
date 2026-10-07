#!/usr/bin/env python3
"""
Finite controls for PRIME_SUPPORT_SUPERCONNECTION.md.

Builds the exterior/Fock supercharge
    Q = sum_p c_p^dagger tensor (S M_beta_p)
with normalized centered prime wakes beta_p on the common CRT clock.

Then H=(Q+Q*)^2 >= 0 and we short/eliminate all hidden even support degrees.

No zeta zeros are used.
"""

from __future__ import annotations
import itertools
import math
import numpy as np


def cyclic_shift(L: int) -> np.ndarray:
    S = np.zeros((L, L), dtype=complex)
    for n in range(L):
        S[(n + 1) % L, n] = 1
    return S


def normalized_prime_wake(L: int, p: int) -> np.ndarray:
    eps = np.array(
        [
            (1.0 if (n + 1) % p == 0 else 0.0)
            - (1.0 if n % p == 0 else 0.0)
            for n in range(L)
        ]
    )
    norm = math.sqrt(float(np.mean(eps * eps)))
    assert norm > 0
    return eps / norm


def fermion_creation(num_modes: int, mode: int) -> np.ndarray:
    """
    Jordan-Wigner exterior creation on Lambda(C^m).

    Fock basis is binary occupation in lexicographic bit order.
    """
    dim = 1 << num_modes
    C = np.zeros((dim, dim), dtype=complex)
    for idx in range(dim):
        bits = [(idx >> (num_modes - 1 - j)) & 1 for j in range(num_modes)]
        if bits[mode]:
            continue
        sign = -1 if (sum(bits[:mode]) % 2) else 1
        out = bits[:]
        out[mode] = 1
        out_idx = 0
        for bit in out:
            out_idx = (out_idx << 1) | bit
        C[out_idx, idx] = sign
    return C


def fock_degree(idx: int, num_modes: int) -> int:
    return sum((idx >> j) & 1 for j in range(num_modes))


def build_hamiltonian(primes: list[int], weights: list[float] | None = None):
    L = math.prod(primes)
    S = cyclic_shift(L)
    m = len(primes)
    dim_f = 1 << m
    if weights is None:
        weights = [1.0] * m
    assert len(weights) == m

    Q = np.zeros((dim_f * L, dim_f * L), dtype=complex)

    for i, (p, w) in enumerate(zip(primes, weights)):
        beta = normalized_prime_wake(L, p)
        E = S @ np.diag(beta)
        cdag = fermion_creation(m, i)
        Q += np.kron(cdag, math.sqrt(w) * E)

    D = Q + Q.conj().T
    H = D @ D
    return H, L


def short_to_vacuum(H: np.ndarray, L: int, m: int):
    """
    Generalized Schur complement of all hidden even exterior degrees onto degree 0.
    """
    vac = np.arange(0, L, dtype=int)

    even_hidden_fock = [
        idx
        for idx in range(1, 1 << m)
        if fock_degree(idx, m) % 2 == 0
    ]

    hidden = np.concatenate(
        [np.arange(idx * L, (idx + 1) * L, dtype=int) for idx in even_hidden_fock]
    )

    A = H[np.ix_(vac, vac)]
    if len(hidden) == 0:
        return A, A, np.empty((0, 0), dtype=complex)

    B = H[np.ix_(vac, hidden)]
    C = H[np.ix_(hidden, hidden)]
    Schur = A - B @ np.linalg.pinv(C, rcond=1e-11) @ B.conj().T
    return A, Schur, C


def two_prime_exact_check():
    primes = [2, 3]
    H, L = build_hamiltonian(primes)
    A, Schur, C = short_to_vacuum(H, L, len(primes))

    raw_mean = np.trace(A).real / L
    eff = np.linalg.eigvalsh((Schur + Schur.conj().T) / 2)
    expected = np.array([0.4, 0.4, 1.0, 1.0, 2.5, 2.5])

    print("=== two-prime exact control (2,3) ===")
    print("raw mean:", raw_mean)
    print("effective eigenvalues:", np.round(eff, 12))
    print("effective mean:", np.mean(eff))

    assert abs(raw_mean - 2.0) < 1e-11
    assert np.max(np.abs(eff - expected)) < 1e-10
    assert abs(np.mean(eff) - 1.3) < 1e-11
    assert np.min(eff) > 0


def three_prime_control():
    primes = [2, 3, 5]
    H, L = build_hamiltonian(primes)
    A, Schur, C = short_to_vacuum(H, L, len(primes))

    raw_mean = np.trace(A).real / L
    eff = np.linalg.eigvalsh((Schur + Schur.conj().T) / 2)

    print("\n=== three-prime control (2,3,5) ===")
    print("raw mean:", raw_mean)
    print("effective mean:", np.mean(eff))
    print("effective min/max:", eff[0], eff[-1])

    assert abs(raw_mean - 3.0) < 1e-10
    assert abs(np.mean(eff) - 1.6257142857142857) < 1e-9
    assert abs(eff[0] - 0.2) < 1e-9
    assert abs(eff[-1] - 5.0) < 1e-9
    assert np.min(eff) >= -1e-10


def two_prime_pointwise_identity():
    """
    Verify the exact local Lagrange/Schur identity
       a(n) - Omega(n)^2/a(n+1)
       = <v_n,v_(n+1)>^2/a(n+1)
    for the (2,3) normalized wakes.
    """
    L = 6
    b2 = normalized_prime_wake(L, 2)
    b3 = normalized_prime_wake(L, 3)

    lhs = []
    rhs = []

    for n in range(L):
        np1 = (n + 1) % L
        v = np.array([b2[n], b3[n]])
        vp = np.array([b2[np1], b3[np1]])
        a = float(v @ v)
        ap = float(vp @ vp)
        omega = float(vp[0] * v[1] - vp[1] * v[0])
        l = a - omega * omega / ap
        r = float(v @ vp) ** 2 / ap
        lhs.append(l)
        rhs.append(r)

    err = max(abs(x - y) for x, y in zip(lhs, rhs))
    print("\n=== pointwise wedge/parallel identity ===")
    print("max error:", err)
    assert err < 1e-12


def curvature_nonflat_control():
    """
    Bare multiplication wakes commute; SUCC-oriented legs do not.
    """
    L = 6
    S = cyclic_shift(L)
    b2 = normalized_prime_wake(L, 2)
    b3 = normalized_prime_wake(L, 3)

    M2 = np.diag(b2)
    M3 = np.diag(b3)
    E2 = S @ M2
    E3 = S @ M3

    flat = np.linalg.norm(M2 @ M3 - M3 @ M2)
    curved = np.linalg.norm(E2 @ E3 - E3 @ E2)

    print("\n=== flat/curved hostile control ===")
    print("bare CRT commutator:", flat)
    print("SUCC-oriented commutator:", curved)

    assert flat < 1e-12
    assert curved > 1e-8


def main():
    two_prime_exact_check()
    three_prime_control()
    two_prime_pointwise_identity()
    curvature_nonflat_control()
    print("\nALL PRIME-SUPPORT SUPERCONNECTION CONTROLS PASSED.")
    print("No RH conclusion is inferred.")


if __name__ == "__main__":
    main()
