#!/usr/bin/env python3
"""Round006 hostile controls (mandatory). Decisive computable controls for the inverse-affine program.
No zeta zeros used. RH untouched.

A/B/C  Z-ablation / remove the corner: bilateralize the successor (N->Z); E_S=I-UU*->0, so Lambda_op->0.
       The von-Mangoldt structure is a COMPRESSION ARTIFACT of the deleted 0.
G      Composite fake-prime V_6: the construction detects redundancy (V_6=V_2 V_3; Lambda(6)=0 automatically).
H      Wrong half-density: local unitarity selects exactly 1/2 (see r006_adelic_checks.py).
E/I    Naked overlap = GCD (r006_affine_corner.py s9); direct-sum bulk divergence (r006_intersect_before_squaring.py).
"""
import numpy as np
from sympy import factorint, primerange

# ---------------------------------------------------------------------------------------
# A/B/C  Z-ABLATION: on l^2(Z) the successor is the UNITARY bilateral shift; E_S vanishes.
# ---------------------------------------------------------------------------------------
print("="*88)
print("CONTROL A/B/C -- Z-ablation: bilateralize SUCC (N->Z). E_S=I-UU* -> 0, so Lambda_op -> 0.")
print("="*88)
M = 60                                   # window {-M,...,M}, index j = n+M
dim = 2*M+1
U = np.zeros((dim, dim))
for n in range(-M, M):                    # U|n>=|n+1> (bilateral; top falls off window only)
    U[(n+1)+M, n+M] = 1.0
ES_Z = np.eye(dim) - U @ U.T
core = slice(2, dim-2)                     # away from window edges
print(f"  on l^2(Z) window {{-{M}..{M}}}:  ||(I - U U*)||_interior = {np.linalg.norm(ES_Z[core,core]):.2e}  (E_S -> 0)")
print(f"  since Lambda_op = sum (log p) V_{{p^k}} E_S V_{{p^k}}* and E_S=0  ==>  Lambda_op = 0 on Z.")
print("  VERDICT: von Mangoldt / the prime signature exists ONLY because N deletes 0 (compression artifact).")

# Contrast: on N the successor keeps its rank-one defect.
N = 80
S = np.zeros((N, N))
for n in range(1, N): S[n, n-1] = 1.0       # S|n>=|n+1>, 0-indexed
ES_N = np.eye(N) - S @ S.T
print(f"  on l^2(N):  ||E_S - |1><1|||_interior = {np.linalg.norm((ES_N - np.outer(np.eye(N)[0],np.eye(N)[0]))[:N-5,:N-5]):.2e}  (E_S=|1><1| survives)")

# ---------------------------------------------------------------------------------------
# G  COMPOSITE FAKE-PRIME: V_6 is not a new generator; the construction gives Lambda(6)=0.
# ---------------------------------------------------------------------------------------
print("\n"+"="*88)
print("CONTROL G -- composite fake-prime V_6: redundancy is detected (V_6=V_2 V_3; Lambda(6)=0).")
print("="*88)
def Vop(a, n=N):
    M_ = np.zeros((n, n))
    for k in range(1, n+1):
        if a*k <= n: M_[a*k-1, k-1] = 1.0
    return M_
V2, V3, V6 = Vop(2), Vop(3), Vop(6)
print(f"  V_6 = V_2 V_3 (exact)?  {np.allclose(V6, V2 @ V3)}   and  V_2 V_3 = V_3 V_2 ? {np.allclose(V2@V3, V3@V2)}")
print(f"  range(V_6) = multiples of 6 = range(V_2) ^ range(V_3): V_6 V_6* = Q_2 Q_3 ? "
      f"{np.allclose(V6@V6.T, (V2@V2.T)@(V3@V3.T))}")
# Lambda over PRIMES only -> entry at n=6 is 0 because 6 is not a prime power
lam6 = 0.0
for p in primerange(2, N+1):
    k = 1
    while p**k <= N:
        if p**k == 6: lam6 += np.log(p)
        k += 1
print(f"  Lambda(6) from the prime-power sum = {lam6:.1f}  (6=2*3 is not p^k; factorint(6)={dict(factorint(6))})")
print("  VERDICT: treating V_6 as an independent 'prime' would inject a spurious log6|6><6|; the")
print("           correct sum over TRUE primes/powers assigns 0, so the construction is redundancy-aware.")

# ---------------------------------------------------------------------------------------
# J  QUOTIENT-HISTORY: averaging away the carry/branch history -> commutative circulant (RH-inert).
# ---------------------------------------------------------------------------------------
print("\n"+"="*88)
print("CONTROL J -- quotient-history: SUCC on Z/L is a circulant (convolution) => RH-inert (C94/C97).")
print("="*88)
L = 12
C = np.zeros((L, L))
for j in range(L): C[(j+1) % L, j] = 1.0     # cyclic successor on Z/L
# circulant <=> diagonalized by DFT <=> commutes with the shift <=> commutative algebra
F = np.fft.fft(np.eye(L), axis=0)/np.sqrt(L)
diagd = F.conj().T @ C @ F
offd = np.linalg.norm(diagd - np.diag(np.diag(diagd)))
print(f"  cyclic successor on Z/{L}: diagonalized by DFT? off-diagonal after Fourier = {offd:.2e}")
print(f"  => commutative convolution; carry survives only in the irregular branch lift to Z. RH-inert.")
print("\nDONE. Controls A/B/C, G, J decisive here; E/I in r006_affine_corner s9 + r006_intersect; H in r006_adelic_checks.")
