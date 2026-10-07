#!/usr/bin/env python3
"""
Finite diagnostic: chronological carry Gram versus active/shadow conductor sectors.

Builds the already-established local carry carré-du-champ at every LCM
prime-power birth, lifts each event isometrically to the final LCM clock, and
weights it by the first-jet half-density weight log(p)/sqrt(p^k).

No zeta zeros are used.

Observed target:
  * carry history DOES create active<->shadow cross blocks in the exact-conductor
    Fourier basis;
  * but the naive arithmetic-only history Gram is "shadow-saturated": after
    eliminating every non-prime-power conductor, its generalized Schur
    complement on the first-jet prime-power sector is numerically zero for
    N <= 8.
This is a hostile control, not an RH proof.
"""

from __future__ import annotations
import math
import numpy as np


def lcm_upto(N: int) -> int:
    z = 1
    for n in range(1, N + 1):
        z = math.lcm(z, n)
    return z


def shift(L: int) -> np.ndarray:
    S = np.zeros((L, L), dtype=complex)
    for a in range(L):
        S[(a + 1) % L, a] = 1
    return S


def carry_carre(old_L: int, p: int) -> np.ndarray:
    """
    CARRY_p = (S-I) tensor |0><p-1|.
    Return CARRY^* CARRY in old-coordinate tensor new-digit ordering.
    """
    A = shift(old_L) - np.eye(old_L)
    e0 = np.zeros((p, 1))
    em = np.zeros((p, 1))
    e0[0, 0] = 1
    em[p - 1, 0] = 1
    C = np.kron(A, e0 @ em.T)
    return C.conj().T @ C


def digit_to_residue_permutation(old_L: int, p: int) -> np.ndarray:
    """
    Tensor index (a,b) -> residue n=a+b old_L mod p old_L.
    """
    M = p * old_L
    P = np.zeros((M, M))
    for a in range(old_L):
        for b in range(p):
            P[a + b * old_L, a * p + b] = 1
    return P


def isometric_pullback(M: int, L: int) -> np.ndarray:
    """
    Pullback along Z/L -> Z/M in standard Euclidean coordinates, normalized
    to be an isometry.
    """
    assert L % M == 0
    q = L // M
    J = np.zeros((L, M), dtype=complex)
    for x in range(L):
        J[x, x % M] = 1 / math.sqrt(q)
    return J


def dft(M: int) -> np.ndarray:
    n = np.arange(M)
    return np.exp(2j * np.pi * np.outer(n, n) / M) / math.sqrt(M)


def conductor_of_frequency(k: int, M: int) -> int:
    if k == 0:
        return 1
    return M // math.gcd(k, M)


def factor(n: int) -> dict[int, int]:
    x = n
    out: dict[int, int] = {}
    p = 2
    while p * p <= x:
        while x % p == 0:
            out[p] = out.get(p, 0) + 1
            x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def is_prime_power(n: int) -> bool:
    return n > 1 and len(factor(n)) == 1


def pinv_schur(G: np.ndarray, physical: np.ndarray, hidden: np.ndarray) -> np.ndarray:
    A = G[np.ix_(physical, physical)]
    if len(hidden) == 0:
        return A
    B = G[np.ix_(physical, hidden)]
    D = G[np.ix_(hidden, hidden)]
    return A - B @ np.linalg.pinv(D, rcond=1e-10) @ B.conj().T


def build_history_gram(N: int):
    Lfinal = lcm_upto(N)
    G = np.zeros((Lfinal, Lfinal), dtype=complex)
    old_L = 1
    events = []

    for m in range(2, N + 1):
        new_L = math.lcm(old_L, m)
        if new_L == old_L:
            continue

        p = new_L // old_L
        # m is necessarily p^k at an LCM birth.
        K_tensor = carry_carre(old_L, p)
        P = digit_to_residue_permutation(old_L, p)
        K_m = P @ K_tensor @ P.T

        J = isometric_pullback(new_L, Lfinal)
        weight = math.log(p) / math.sqrt(m)
        G += weight * (J @ K_m @ J.conj().T)
        events.append((m, p, old_L, new_L, weight))
        old_L = new_L

    F = dft(Lfinal)
    Ghat = F.conj().T @ G @ F
    cond = np.array([conductor_of_frequency(k, Lfinal) for k in range(Lfinal)])
    return Ghat, cond, events


def main():
    print("Chronological carry shadow probe (no zero data)")
    for N in [3, 4, 5, 7, 8]:
        G, cond, events = build_history_gram(N)
        M = len(cond)

        prime_phys = np.array(
            [i for i, d in enumerate(cond) if d <= N and is_prime_power(int(d))],
            dtype=int,
        )
        pset = set(prime_phys.tolist())
        all_other = np.array([i for i in range(M) if i not in pset], dtype=int)

        cross = np.linalg.norm(G[np.ix_(prime_phys, all_other)])
        rank_total = np.linalg.matrix_rank(G, tol=1e-8)
        rank_hidden = np.linalg.matrix_rank(G[np.ix_(all_other, all_other)], tol=1e-8)
        Sch = pinv_schur(G, prime_phys, all_other)
        sch_norm = np.linalg.norm(Sch)

        active_all = np.array([i for i, d in enumerate(cond) if d <= N], dtype=int)
        future_shadow = np.array([i for i, d in enumerate(cond) if d > N], dtype=int)
        Sch_active = pinv_schur(G, active_all, future_shadow)
        evals_active = np.linalg.eigvalsh((Sch_active + Sch_active.conj().T) / 2)
        rank_active_schur = int(np.sum(evals_active > 1e-8))

        print(
            f"N={N:2d} L={M:4d} births={len(events)} "
            f"cross(first-jet,hidden)={cross:.6g} "
            f"rank(G)={rank_total} rank(hidden)={rank_hidden} "
            f"||Schur_firstjet||={sch_norm:.3e} "
            f"rank(Schur_active-vs-future)={rank_active_schur}"
        )

        # Hostile-control expectations from the finite probe.
        assert cross > 1e-8
        assert rank_total == rank_hidden
        assert sch_norm < 1e-8

    print()
    print("OBSERVED CONTROL PASSED through N=8:")
    print("  carry chronology creates nonzero conductor cross-coupling,")
    print("  but the arithmetic-only history Gram is shadow-saturated:")
    print("  all first-jet prime-power measurement directions are already spanned")
    print("  by the non-prime-power sector, so the generalized Schur residual is zero.")
    print("This kills the naive carry-only shadow-renormalization candidate.")
    print("The Archimedean/completion channel or a different exact history observable is mandatory.")


if __name__ == "__main__":
    main()
