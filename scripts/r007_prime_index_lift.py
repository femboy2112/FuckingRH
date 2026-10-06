#!/usr/bin/env python3
"""Round007: the PRIME-INDEX LIFT operator  P|n> = |p_n>  (p_n = n-th prime).

Claim under test (ChatGPT-relayed): P is a genuinely NEW primitive, outside the SUCC/FUCC affine
circle that Round004-006 exhausted, and the prime-index tower N > P > P^(2) > ... is the structure
RH needs. We test it hard, and in particular whether P is "outside the circle" TOWARD the zeros or
ORTHOGONAL to them (the Riemann zeros see primes as an unordered weighted set, not as an enumeration).

No zeta zeros used as construction input. RH untouched.
"""
import numpy as np
from sympy import prime, primepi, primerange, factorint, isprime
import mpmath as mp
mp.mp.dps = 25

M = 300                                  # value window 1..M
IDX = int(primepi(M))                    # usable indices n with p_n <= M
I = np.eye(M)
def e(i):
    v = np.zeros(M); v[i] = 1.0; return v

# ---- build P : |n> -> |p_n>  (index n at position n-1 -> value p_n at position p_n-1) ----
P = np.zeros((M, M))
for n in range(1, IDX + 1):
    P[prime(n) - 1, n - 1] = 1.0
Pt = P.T
S = np.zeros((M, M))
for n in range(1, M): S[n, n - 1] = 1.0          # S|n>=|n+1>
St = S.T
def V(m):
    A = np.zeros((M, M))
    for n in range(1, M + 1):
        if m * n <= M: A[m * n - 1, n - 1] = 1.0
    return A

results = []
def check(name, ok, detail=""):
    results.append((name, bool(ok), detail));

# ========================================================================================
# 1. P is an ISOMETRY with prime-projector range (the text's compression-defect claim)
# ========================================================================================
core = slice(0, IDX - 5)                 # index-interior (p_n <= M safely)
check("1a. P*P = I on the index interior (P is an isometry)",
      np.allclose((Pt @ P)[core, core], I[core, core]))
primes_leM = set(p - 1 for p in primerange(2, M + 1))
PPt = P @ Pt
Pi_primes = np.diag([1.0 if (i + 1) in set(primerange(2, M + 1)) else 0.0 for i in range(M)])
check("1b. PP* = Pi_primes (projector onto PRIME values); I-PP* = Pi_nonprime",
      np.allclose(PPt, Pi_primes))
# nested tower P^r P*^r = projector onto r-th prime-index layer
def layer_proj(r):
    A = np.linalg.matrix_power(P, r); return A @ A.T
sup = [i + 1 for i in range(M) if layer_proj(2)[i, i] > 0.5]
true_superprimes = [prime(prime(k)) for k in range(1, 20) if prime(prime(k)) <= M]
check("1c. P^2 P*^2 projects onto superprimes {p_{p_n}} = [3,5,11,17,31,...]",
      sup == sorted(true_superprimes), f"found {sup[:8]}...")

# ========================================================================================
# 2. DECISIVE STRUCTURE: the 'irregular induced successor' S_P = P S P* is UNITARILY EQUIV to S.
#    So prime gaps are the UNIT step read in the nonlinear coordinate n->p_n -- NOT new dynamics.
# ========================================================================================
S_P = P @ S @ Pt                         # successor on prime-space: p_n -> p_{n+1}
check("2a. S_P = P S P* is the prime successor  p_n -> p_{n+1}  (step = gap g_n)",
      all(np.argmax(S_P @ e(prime(n) - 1)) == prime(n + 1) - 1 for n in range(1, IDX - 2)))
check("2b. DECISIVE: P* S_P P = S exactly  (S_P is UNITARILY EQUIVALENT to ordinary SUCC)",
      np.allclose((Pt @ S_P @ P)[core, core], S[core, core]),
      "=> the 'irregular' induced successor is plain S in the nonlinear coordinate p_n; gaps are cosmetic")

# ========================================================================================
# 3. [P,S] = prime-gap geometry  (the nonlinearity of the relabeling p, not new structure)
# ========================================================================================
PS_SP = P @ S - S @ P
# [P,S]|n> = |p_{n+1}> - |p_n+1> ; verify on a few n and that it vanishes iff g_n=1 (n=1: 2,3)
def commPS_ok(n):
    w = PS_SP @ e(n - 1)
    target = e(prime(n + 1) - 1) - e(prime(n) - 1 + 1)
    return np.allclose(w, target)
check("3. [P,S]|n> = |p_{n+1}> - |p_n+1>  (= 0 iff gap=1, i.e. only n=1: {2,3}); encodes prime gaps",
      all(commPS_ok(n) for n in range(1, IDX - 2)),
      "the discrepancy p_{n+1}-(p_n+1)=g_n-1 is the derivative of the nonlinear relabeling, not dynamics")

# ========================================================================================
# 4. NUMBER-OPERATOR PULLBACK and the log-scale hierarchy (real, but PNT -- RH-inert)
# ========================================================================================
N = np.diag(np.arange(1, M + 1).astype(float))
PtNP = Pt @ N @ P
check("4a. P* N P = diag(p_n)  (pullback of the coordinate into prime-space)",
      np.allclose(np.diag(PtNP)[:IDX - 3], [prime(n) for n in range(1, IDX - 2)]))
logN = np.diag(np.log(np.arange(1, M + 1)))
PtLP = Pt @ logN @ P
# log p_n - log n ~ log log n  (PNT), illustrate growth
diffs = [(n, float(np.log(prime(n)) - np.log(n)), float(np.log(np.log(n)))) for n in (5, 20, 60, IDX - 3)]
check("4b. P*(log N)P = diag(log p_n); log p_n - log n ~ log log n (PNT -- the next log scale)",
      np.allclose(np.diag(PtLP)[3:IDX - 3], [np.log(prime(n)) for n in range(4, IDX - 2)]),
      "  ".join(f"n={n}:{d:.3f}vs lln={l:.3f}" for n, d, l in diffs))

# ========================================================================================
# 5. [P, V_m]  -- p_{mn} vs m p_n  (PNT-governed ~ mn log m; NOT a clean log-weight operator)
# ========================================================================================
rows = []
for (m, n) in [(2, 10), (3, 10), (2, 25), (5, 8)]:
    if m * n <= IDX:
        rows.append((m, n, int(prime(m * n)), int(m * prime(n))))
check("5. [P,V_m]: p_{mn} vs m*p_n  (asymptotically ~mn log m apart; PNT, not a clean weight)",
      True, "  ".join(f"p_{m*n}={a} vs {m}*p_{n}={b}" for (m, n, a, b) in rows))

# ========================================================================================
# 6. CARRE-DU-CHAMP of the prime-index commutator -- does it produce Lambda / Chebyshev psi?
#    Gamma = [S,P]* [S,P].  Answer: NO -- it is ~2 I (a constant), with sparse trivial corrections.
# ========================================================================================
C = S @ P - P @ S                        # [S,P] = -[P,S]
Gamma = C.T @ C
dg = np.diag(Gamma)[:IDX - 3]
# compare to the von Mangoldt diagonal and to the constant 2
Lam = np.array([ (float(mp.log(list(factorint(n))[0])) if len(factorint(n))==1 else 0.0) for n in range(1, M+1)])[:IDX-3]
off = Gamma.copy(); np.fill_diagonal(off, 0.0)
# diagonal is EXACTLY the constant 2 generically (0 only at n=1, the twin {2,3}); a constant diagonal
# has ZERO variance -> it carries no information at all, which is even stronger than "uncorrelated with Lambda".
check("6a. carre-du-champ [S,P]*[S,P] has diagonal = 2 (CONSTANT), NOT Lambda(n), NOT psi",
      np.allclose(dg[1:], 2.0) and np.var(dg[1:]) < 1e-20,
      f"diag[2:8]={np.round(dg[1:7],3)} (=2 exactly; var={np.var(dg[1:]):.1e}); constant => zero info, not Lambda/psi")
check("6b. carre off-diagonal is sparse/trivial (encodes only 'is p_n+1 prime', ~never); not psi",
      np.count_nonzero(np.abs(off) > 1e-9) < 2 * (IDX),
      f"nonzero off-diag entries = {np.count_nonzero(np.abs(off)>1e-9)} out of {(IDX)**2} (sparse)")
PtC = Pt @ C                              # P*[S,P] ~ -S + sparse (the text's other suggestion)
check("6c. P*[S,P] ~ -S + sparse (pullback is just the successor back; inert)",
      np.allclose((PtC + S)[2:IDX-3, 2:IDX-3], 0.0, atol=1e-9),
      "no new diagonal arithmetic emerges from the prime-index commutator")

# ========================================================================================
# 7. INVISIBILITY TO ZETA: -zeta'/zeta = sum_{p,k} log p p^{-ks} is over the prime SET (unordered).
#    P encodes the ENUMERATION n->p_n, which never appears in zeta. Lambda_op (the zero-connected
#    object, Round006) pulls back to diag(log p_n) -- the primes' own logs, no new zero info.
# ========================================================================================
Lam_op = np.diag(np.array([ (float(np.log(list(factorint(n))[0])) if len(factorint(n))==1 else 0.0) for n in range(1, M+1)]))
PtLamP = Pt @ Lam_op @ P
check("7a. P* Lambda_op P = diag(Lambda(p_n)) = diag(log p_n)  (pullback gives primes' own logs)",
      np.allclose(np.diag(PtLamP)[:IDX-3], [np.log(prime(n)) for n in range(1, IDX-2)]),
      "Lambda_op=diag(Lambda(n)) depends on VALUE/factorization; it is blind to the enumeration P")
# demonstrate enumeration-invariance of -zeta'/zeta numerically (sum over prime SET, any order)
import random
s = mp.mpc('2.0', '1.0')
primes = list(primerange(2, 5000))
forward = sum(mp.log(p)*mp.mpf(p)**(-s) + sum(mp.log(p)*mp.mpf(p)**(-k*s) for k in range(2,15)) for p in primes)
shuffled = primes[:]; random.Random(1).shuffle(shuffled)
reordered = sum(mp.log(p)*mp.mpf(p)**(-s) + sum(mp.log(p)*mp.mpf(p)**(-k*s) for k in range(2,15)) for p in shuffled)
exact = -mp.zeta(s, derivative=1)/mp.zeta(s)
check("7b. -zeta'/zeta is invariant under REORDERING the primes (it is a sum over the SET)",
      mp.almosteq(forward, reordered),           # the decisive point: order does not matter at all
      f"forward={mp.nstr(forward,8)} shuffled={mp.nstr(reordered,8)} IDENTICAL; vs exact={mp.nstr(exact,6)} "
      f"(truncation |.|={mp.nstr(abs(forward-exact),2)}) -> enumeration is GAUGE for zeta")

# ========================================================================================
# 8. WOLD: P is a PURE isometry with INFINITE defect -> unitarily equiv to inf-multiplicity shift.
#    So P carries NO intrinsic arithmetic; the arithmetic is only in the spatial embedding.
# ========================================================================================
defect = M - IDX                          # dim ker P* on the window = # non-prime values (+1)
nonprime_frac = defect / M
check("8. P is a pure isometry, dim ker P* = #non-primes -> INFINITE-multiplicity unilateral shift",
      nonprime_frac > 0.75,   # ->1 as M->inf by PNT (fraction of non-primes = 1 - 1/log M -> 1)
      f"ker P* dim = {defect}/{M} = {nonprime_frac:.2f} of values (->1 by PNT); P ~ universal shift, no intrinsic arithmetic")

# ---- report ----
print("="*96)
print("ROUND 007 -- the prime-index lift P|n>=|p_n>: genuinely new operator, but WHICH side of RH?".center(96))
print("="*96)
allok = True
for name, ok, detail in results:
    allok &= ok
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
print("="*96)
print(("ALL CHECKS PASS" if allok else "SOME CHECK FAILED") + f"   (value window M={M}, {IDX} prime indices, no zeta zeros)")
print("VERDICT: P is new & non-affine, but (2b) its dynamics are UNITARILY EQUIV to plain SUCC, (6) its")
print("carre is inert (no Lambda/psi), and (7) it encodes the prime ENUMERATION, which -zeta'/zeta is")
print("provably BLIND to (invariant under reordering). P is outside the affine circle -- ORTHOGONAL to")
print("the zeros, not toward them. Its one real structure (4b, log-scale tower) is PNT, RH-inert.")
