#!/usr/bin/env python3
"""Round006 master verification: the rational affine parent, the integer corner, and the exact
operator identities (von Mangoldt = transported successor boundary, log n = prime-jet occupancy,
stratified diagonal, inverse-FUCC valuation, Toeplitz/Hardy realization of the local carry filter).

Everything here is an EXACT algebraic identity on l^2(N); we verify it on a finite window {1..N}
and separate genuine defects (survive N->inf) from truncation artifacts (die as N->inf).

NO zeta zeros are used anywhere. RH is not touched; these are structural identities.
"""
import numpy as np
from sympy import primerange, factorint, isprime
import mpmath as mp
mp.mp.dps = 30

N = 120                      # window: basis state index i (0-based) <-> integer n = i+1
I = np.eye(N)
e = lambda i: (lambda v: (v.__setitem__(i, 1.0), v)[1])(np.zeros(N))  # unit vector e_i

def op_from_map(f):
    """Dense matrix of the operator sending |n> -> |f(n)> (or 0 if f(n) is None/out of range)."""
    M = np.zeros((N, N))
    for n in range(1, N + 1):
        m = f(n)
        if m is not None and 1 <= m <= N:
            M[m - 1, n - 1] = 1.0
    return M

# ---- generators compressed to the corner -------------------------------------------------
S  = op_from_map(lambda n: n + 1)        # successor  S|n>=|n+1>
St = S.T                                  # S* |n>=|n-1> (0 at n=1)
def V(a):   return op_from_map(lambda n: a * n)        # dilation by a
def Vt(a):  return op_from_map(lambda n: (n // a if n % a == 0 else None))  # V_a*

PRIMES = list(primerange(2, N + 1))
results = []
def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))

# ========================================================================================
# 1. AFFINE BRAID on Q (sampled on rationals): D_q T_a D_q^{-1} = T_{qa}, and T_a D_q = D_q T_{a/q}
# ========================================================================================
from fractions import Fraction as Fr
def braid_ok():
    # act on sample x in Q: D_q T_a D_q^{-1}|x> should be |x+qa>
    import random
    for _ in range(2000):
        x = Fr(random.randint(-20, 20), random.randint(1, 9))
        a = Fr(random.randint(-9, 9), random.randint(1, 7))
        q = Fr(random.randint(1, 9), random.randint(1, 9))
        lhs = q * ((x / q) + a)          # D_q T_a D_q^{-1} : x -> x/q -> x/q+a -> q(x/q+a)
        rhs = x + q * a                   # T_{qa}: x -> x+qa
        if lhs != rhs: return False
        # T_a D_q : x -> qx -> qx+a ;  D_q T_{a/q}: x -> x+a/q -> q(x+a/q)=qx+a
        if (q * x + a) != q * (x + a / q): return False
    return True
check("1. affine braid  D_q T_a D_q^-1 = T_qa  and  T_a D_q = D_q T_{a/q}", braid_ok())

# ========================================================================================
# 2. ISOMETRY + COMPRESSED INVERSE.  S*S=I, V_a*V_a=I (interior); V_a*|n>=|n/a| iff a|n
# ========================================================================================
# genuine bottom defect at |1>, truncation defect at top only
SSt = S @ St
check("2a. SS* = I - |1><1|  (E_S = SS* defect is the bottom boundary |1>)",
      np.allclose(I - SSt, np.outer(e(0), e(0))),
      f"||I-SS*-|1><1|||={np.linalg.norm(I-SSt-np.outer(e(0),e(0))):.2e}")
# V_p* survival = divisibility, sampled
ok = all((Vt(p) @ e(n - 1))[n // p - 1] == 1.0 for p in [2,3,5,7] for n in range(1, N+1)
         if n % p == 0 and n // p >= 1) and \
     all(np.allclose(Vt(p) @ e(n - 1), 0) for p in [2,3,5,7] for n in range(1, N+1) if n % p != 0)
check("2b. V_p*|n> = |n/p> iff p|n, else 0  (divisibility = inverse-FUCC survival)", ok)

# ========================================================================================
# 3. SELF-COMMUTATOR of the successor = the boundary |1><1|   ([S*,S] = |1><1|, mod truncation)
# ========================================================================================
comm = St @ S - S @ St
genuine = np.outer(e(0), e(0))                 # |1><1|
trunc   = np.outer(e(N-1), e(N-1))             # top-of-window artifact, dies as N->inf
check("3. [S*,S] = |1><1| - (top truncation)  -> |1><1| as N->inf",
      np.allclose(comm, genuine - trunc),
      f"genuine part exact; truncation atom at n={N} only")

# ========================================================================================
# 4. VON MANGOLDT = TRANSPORTED SUCCESSOR BOUNDARY
#    Lambda_op = sum_{p,k} (log p) V_{p^k} (I-SS*) V_{p^k}*  = diag(Lambda(n))
# ========================================================================================
E_S = I - SSt                                   # = |1><1| (genuine); rank 1
Lam = np.zeros((N, N))
for p in PRIMES:
    k = 1
    while p**k <= N:
        Vpk = V(p**k)
        Lam += np.log(p) * (Vpk @ E_S @ Vpk.T)
        k += 1
Lam_diag = np.diag(Lam)
def vonmangoldt(n):
    f = factorint(n)
    return float(mp.log(list(f)[0])) if len(f) == 1 else 0.0
true_Lam = np.array([vonmangoldt(n) for n in range(1, N + 1)])
offdiag = np.linalg.norm(Lam - np.diag(Lam_diag))
check("4. Lambda_op = sum (log p) V_{p^k}|1><1|V_{p^k}* = diag(Lambda(n))  [HEADLINE]",
      np.allclose(Lam_diag, true_Lam) and offdiag < 1e-12,
      f"max|diag-Lambda|={np.max(np.abs(Lam_diag-true_Lam)):.2e}, offdiag={offdiag:.2e}")

# ========================================================================================
# 5. LOG n = PRIME-JET OCCUPANCY.  H_log = sum_{p,k}(log p) V_{p^k}V_{p^k}* = diag(log n)
# ========================================================================================
Hlog = np.zeros((N, N))
for p in PRIMES:
    k = 1
    while p**k <= N:
        Vpk = V(p**k)
        Hlog += np.log(p) * (Vpk @ Vpk.T)       # Q_{p,k} = proj onto multiples of p^k
        k += 1
Hlog_diag = np.diag(Hlog)
true_log = np.log(np.arange(1, N + 1))
check("5. H_log = sum (log p) V_{p^k}V_{p^k}* = diag(log n)  (occupancy = log n)",
      np.allclose(Hlog_diag, true_log) and np.linalg.norm(Hlog - np.diag(Hlog_diag)) < 1e-12,
      f"max|diag-log n|={np.max(np.abs(Hlog_diag-true_log)):.2e}")

# relation: log n = sum_{d|n} Lambda(d)  (occupancy = sum of heads over divisors)
def divisor_sum_Lambda(n): return sum(vonmangoldt(d) for d in range(1, n+1) if n % d == 0)
check("5b. log n = sum_{d|n} Lambda(d)  (occupancy = divisor-sum of transported heads)",
      all(abs(divisor_sum_Lambda(n) - np.log(n)) < 1e-12 for n in range(1, N+1)))

# ========================================================================================
# 6. STRATIFIED DIAGONAL.  unit step on sheet (p,k) = displacement p^k in N
#    Pi_{p,k} Stilde = S^{p^k} Pi_{p,k}  with  Pi_{p,k}|m>=|p^k m>
# ========================================================================================
def strat_ok(p, k):
    pk = p**k
    Spk = np.linalg.matrix_power(S, pk)
    # LHS: m -> m+1 (sheet succ) -> p^k(m+1);  RHS: m -> p^k m -> + p^k
    for m in range(1, N):
        if pk * (m + 1) <= N:
            lhs = e(pk * (m + 1) - 1)                 # Pi_{p,k} Stilde |m>
            rhs = Spk @ e(pk * m - 1)                 # S^{p^k} Pi_{p,k} |m>
            if not np.allclose(lhs, rhs): return False
    return True
check("6. Pi_{p,k} Stilde = S^{p^k} Pi_{p,k}  (diagonal in geometry, displacement p^k in N)",
      all(strat_ok(p, k) for (p, k) in [(2,1),(2,2),(2,3),(3,1),(3,2),(5,1),(7,1),(11,1)]))

# ========================================================================================
# 7. INVERSE-FUCC SURVIVAL = p-ADIC VALUATION.  v_p(n) = max{k: (V_p*)^k|n> != 0}
# ========================================================================================
def survival_depth(p, n):
    v = e(n - 1); k = 0
    while True:
        w = Vt(p) @ v
        if np.allclose(w, 0): return k
        v = w; k += 1
check("7. v_p(n) = max{k:(V_p*)^k|n>!=0}  (inverse-FUCC survival depth = valuation)",
      all(survival_depth(p, n) == factorint(n).get(p, 0)
          for p in [2,3,5] for n in range(1, N + 1)))

# ========================================================================================
# 8. TOEPLITZ / HARDY REALIZATION of the local carry filter (Round005 C96 upgraded to an
#    exact compression identity).  B_p = (I-S)(I - p^{-1/2} S)^{-1}  = analytic Toeplitz with
#    symbol (1-z)/(1-r z), r=p^{-1/2}.  No Hankel correction (analytic symbol).
# ========================================================================================
def toeplitz_from_symbol_coeffs(c):
    """lower-triangular analytic Toeplitz: (T)_{i,j}=c[i-j] for i>=j."""
    T = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1):
            if i - j < len(c): T[i, j] = c[i - j]
    return T
def Bp_check(p):
    r = p**-0.5
    Bp_resolvent = (I - S) @ np.linalg.inv(I - r * S)    # (I-S)(I-rS)^{-1}
    # symbol (1-z)Sum r^k z^k = 1 - (1-r) Sum_{k>=1} r^{k-1} z^k
    c = [1.0] + [-(1 - r) * r**(k - 1) for k in range(1, N)]
    Bp_toeplitz = toeplitz_from_symbol_coeffs(c)
    # compare on the safe interior (away from top-window truncation of the resolvent)
    core = slice(0, N - 20)
    diff = np.linalg.norm((Bp_resolvent - Bp_toeplitz)[core, core])
    return diff
check("8a. B_p=(I-S)(I-p^-1/2 S)^-1 = analytic Toeplitz of (1-z)/(1-p^-1/2 z) (no Hankel corr.)",
      all(Bp_check(p) < 1e-9 for p in [2,3,5,7]),
      f"max interior ||resolvent - Toeplitz||={max(Bp_check(p) for p in [2,3,5,7]):.2e}")
# carry carre-du-champ: (I-S)*(I-S) = 2I - S - S*  (symbol |1-z|^2 = 2-2cos theta)
core = slice(1, N - 1)
D = (I - S)
check("8b. (I-S)*(I-S) = 2I - S - S*  (symbol |1-z|^2 = 2(1-cos theta))",
      np.allclose((D.T @ D)[core, core], (2*I - S - St)[core, core]))

# ========================================================================================
# 9. NAKED OVERLAP is the GCD/coprime shuffle (factorized, RH-inert) -- Pi*Pi = V_{p^k}* V_{q^l}
# ========================================================================================
def naked_overlap(p, k, q, l):
    return Vt(p**k) @ V(q**l)              # V_{p^k}* V_{q^l}
O = naked_overlap(2, 1, 3, 1)               # V_2* V_3 : |m> -> |3m/2> iff 2|3m iff 2|m
# it is a partial isometry supported on even m, sending m -> 3m/2 : a clean coprime shuffle
support = [n for n in range(1, N + 1) if not np.allclose(O @ e(n - 1), 0)]
images  = {n: int(np.argmax(O @ e(n - 1))) + 1 for n in support}
check("9. naked V_2*V_3 = coprime shuffle m->3m/2 on even m (factorized, GCD-type, RH-inert)",
      support == [n for n in range(1, N+1) if n % 2 == 0 and 3*n <= N] and   # 3m<=N: intermediate |3m> in window
      all(images[n] == 3 * n // 2 for n in support))

# ========================================================================================
# REPORT
# ========================================================================================
print("=" * 94)
print("ROUND 006 — rational affine parent / integer corner / exact identities".center(94))
print("=" * 94)
allok = True
for name, ok, detail in results:
    allok &= ok
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail: print(f"         {detail}")
print("=" * 94)
print(("ALL EXACT IDENTITIES VERIFIED" if allok else "SOME CHECK FAILED") +
      f"   (window N={N}, no zeta zeros used)")
print("Note: S*S=I and V_p*V_p=I hold on the N->inf corner; finite-window top atoms are truncation.")
