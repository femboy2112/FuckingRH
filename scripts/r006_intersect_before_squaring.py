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

def Cp_times(v, p, N, boundary="uniform"):
    """C_p v = (boundary)(I - p^{-1/2} V_p)^{-1} v, exact (V_p nilpotent on the window).
    boundary="uniform":   (I - S)    -- same successor boundary on every sheet (common mode)
    boundary="stratified":(I - S^p)  -- the sheet's UNIT step shadowed: Pi_{p,1} Stilde = S^p Pi_{p,1}
    """
    r = p**-0.5
    # (I - r V_p)^{-1} v = sum_{k>=0} r^k V_p^k v ; V_p: |n> -> |p n> (0 if p n > N)
    acc = v.copy(); term = v.copy()
    while True:
        nt = np.zeros(N)
        for i in np.nonzero(term)[0]:
            n = i + 1
            if p * n <= N:
                nt[p * n - 1] += r * term[i]
        if not nt.any(): break
        acc += nt; term = nt
    shift = 1 if boundary == "uniform" else p       # (I - S^shift)
    Sacc = np.zeros(N)
    if shift < N:
        Sacc[shift:] = acc[:N - shift]              # S^shift: |n>->|n+shift>, top falls off
    return acc - Sacc

def energies(v, P_primes, N, boundary):
    cols = [Cp_times(v, p, N, boundary) for p in P_primes]
    diag = sum(float(c @ c) for c in cols)
    tot_vec = np.sum(cols, axis=0)
    total = float(tot_vec @ tot_vec)
    return diag, total - diag, total

if __name__ == "__main__":
    print("INTERSECT BEFORE SQUARING -- do the cross terms renormalize the bulk divergence?\n")
    for boundary in ("uniform", "stratified"):
        tag = "(I-S)  common mode" if boundary == "uniform" else "(I-S^p)  prime-specific / stratified"
        print(f"########## boundary = {boundary}:  {tag} ##########")
        for vname in ("source |1>", "random unit"):
            print(f"--- test vector: {vname} ---")
            print(f"   {'N':>5} {'#primes':>8} {'DIAG':>12} {'CROSS':>12} {'TOTAL':>12} {'CROSS/DIAG':>11} {'DIAG/pi(N)':>11}")
            rng = np.random.default_rng(0)
            for N in (60, 120, 240, 480, 960):
                P = list(primerange(2, N + 1))
                v = np.zeros(N); v[0] = 1.0
                if vname != "source |1>":
                    v = rng.standard_normal(N); v /= np.linalg.norm(v)
                diag, cross, total = energies(v, P, N, boundary)
                print(f"   {N:5d} {len(P):8d} {diag:12.4f} {cross:12.4f} {total:12.4f} "
                      f"{cross/diag:11.4f} {diag/len(P):11.4f}")
            print()
    print("READING:")
    print(" UNIFORM (I-S): CROSS/DIAG GROWS ~pi(N) (14,27,48,88,158) -> TOTAL diverges QUADRATICALLY.")
    print(" STRATIFIED (I-S^p): CROSS/DIAG STILL GROWS ~pi(N)/2 (7,14,24,44,79) -> TOTAL STILL quadratic.")
    print("   Prime-specificity only HALVES the coefficient; it does NOT cure the divergence.")
    print(" WHY: every boundary (I-S^shift) shares the IDENTITY I (every sheet's range contains the")
    print("   source |1>), so coherent assembly adds it in phase. uniform shares v AND Sv (coeff~2),")
    print("   stratified shares only v (coeff~1) -- exactly the observed halving.")
    print(" DICHOTOMY (complete for these families): overlap->quadratic pi(N)^2; orthogonal(direct")
    print("   sum)->linear pi(N) (C98). BOTH diverge. The ONLY escape is DESTRUCTIVE (opposite-sign)")
    print("   interference, CROSS ~ -DIAG with DIAG tamed -- the signed Weil terms (prime + / Arch pole -), =RH.")
