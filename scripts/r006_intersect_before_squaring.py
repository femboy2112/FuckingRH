#!/usr/bin/env python3
"""Round006 decisive experiment: INTERSECT BEFORE SQUARING.

Round004/005 killed the DEAD order  B = (+)_p B_p  (direct sum of local squares): the energy
sum_p ||B_p v||^2 diverges in bulk (~ pi(N), C91/C98) and is renormalized only ANALYTICALLY
(the indefinite Archimedean pole), never by an algebraic Hilbert-space subtraction.

The Round006 NEW order dresses every prime sheet with the UNIVERSAL successor boundary (I-S)
(the non-commuting additive generator -- the only object NOT in the commutative multiplicative
algebra, hence the only possible source of RH content, C89/C94) and assembles BEFORE squaring:

    C_p := (I - S) (I - p^{-1/2} V_p)^{-1}         [ universal boundary x prime-p causal memory ]
    B_int := sum_{p<=P} C_p ,    energy = || B_int v ||^2 = DIAG + CROSS
        DIAG  = sum_{p<=P} ||C_p v||^2              (the dead direct-sum energy)
        CROSS = sum_{p!=q<=P} <C_p v, C_q v>        (the NEW cross-sheet terms)

THE TEST (directive s14): do the CROSS terms renormalize the divergent DIAG (crack), or does the
divergence return with CROSS bounded/small (no-go: the two orders differ but the escape fails)?

No zeta zeros used. RH untouched.
"""
import numpy as np
from sympy import primerange, factorint

def Cp_times(v, p, N):
    """C_p v = (I-S)(I - p^{-1/2} V_p)^{-1} v, exact (V_p nilpotent on the window)."""
    r = p**-0.5
    # (I - r V_p)^{-1} v = sum_{k>=0} r^k V_p^k v ; V_p: |n> -> |p n> (0 if p n > N)
    acc = v.copy(); term = v.copy(); k = 0
    while True:
        nt = np.zeros(N)
        idx = np.nonzero(term)[0]
        for i in idx:
            n = i + 1
            if p * n <= N:
                nt[p * n - 1] += r * term[i]
        if not nt.any(): break
        acc += nt; term = nt; k += 1
    # (I - S) acc :  acc - S acc,  S|n> = |n+1>
    Sacc = np.zeros(N)
    Sacc[1:] = acc[:-1]          # shift up; top falls off (truncation)
    Sacc[N-1] = 0.0 if N-1 >= 0 else 0.0
    return acc - Sacc

def energies(v, P_primes, N):
    cols = [Cp_times(v, p, N) for p in P_primes]
    diag = sum(float(c @ c) for c in cols)
    tot_vec = np.sum(cols, axis=0)
    total = float(tot_vec @ tot_vec)
    cross = total - diag
    return diag, cross, total

if __name__ == "__main__":
    print("INTERSECT BEFORE SQUARING -- does the universal-boundary cross term renormalize the bulk?\n")
    for vname in ("source |1>", "random unit"):
        print(f"--- test vector: {vname} ---")
        print(f"   {'N':>5} {'#primes':>8} {'DIAG':>12} {'CROSS':>12} {'TOTAL':>12} {'CROSS/DIAG':>11} {'DIAG/pi(N)':>11}")
        rng = np.random.default_rng(0)
        for N in (60, 120, 240, 480, 960):
            P = list(primerange(2, N + 1))
            if vname == "source |1>":
                v = np.zeros(N); v[0] = 1.0
            else:
                v = rng.standard_normal(N); v /= np.linalg.norm(v)
            diag, cross, total = energies(v, P, N)
            print(f"   {N:5d} {len(P):8d} {diag:12.4f} {cross:12.4f} {total:12.4f} "
                  f"{cross/diag:11.4f} {diag/len(P):11.4f}")
        print()
    print("READING:")
    print(" DIAG grows ~ linearly in #primes (bulk divergence, C91/C98) -> DIAG/pi(N) ~ const.")
    print(" If CROSS/DIAG -> 0 : cross terms do NOT renormalize the bulk; the divergence returns.")
    print("   => 'intersect before squaring' with a UNIFORM (common-mode) boundary FAILS to escape")
    print("      (consistent with C89: the universal boundary is RH-inert; and C98: the bulk")
    print("       renormalizer is the analytic Archimedean pole, not an algebraic cross term).")
    print(" If CROSS ~ -DIAG (ratio -> -1): the cross terms cancel the bulk -> would be a crack.")
