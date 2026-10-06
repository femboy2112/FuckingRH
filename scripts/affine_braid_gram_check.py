#!/usr/bin/env python3
"""Numerical verification for AFFINE_BRAID_HALF_DENSITY_GRAM.md.

All identities checked here are EXACT and independent of RH:

  Lemma 1  affine braid              V_m S = S^m V_m           (ax+b relation)
  Thm   2  zeta Gram                 <zeta_u|zeta_s> = zeta(s+ubar)
           critical edge             ||zeta_sigma||^2 = zeta(2 sigma),  pole at sigma=1/2
  Thm   4  log-energy expectation    <zeta_u|H|zeta_s>/<..> = -zeta'/zeta(s+u)
  Lemma 3  cross-prime coupling      <m|F*F|n> = sum_{p m = q n} conj(a_p) a_q  (prime-swap graph)

Run: python3 scripts/affine_braid_gram_check.py
Deps: numpy, mpmath  (mpmath used only as an independent zeta / zeta' reference).
"""
import numpy as np
from mpmath import mp, mpc
mp.dps = 30


def _zeta(z):
    return complex(mp.zeta(mpc(z)))


# --------------------------------------------------------------------------
# Thm 2:  |zeta_s> = sum_n n^{-s}|n>  =>  <zeta_u|zeta_s> = sum_n n^{-(s+conj(u))}
# Compare the Dirichlet-sum overlap to mpmath's zeta(s+conj(u)) (independent).
# --------------------------------------------------------------------------
def overlap(s, u, N=200_000):
    n = np.arange(1, N + 1, dtype=np.float64)
    return np.sum(n ** (-(s + np.conj(u))))


print("=== Thm 2: <zeta_u|zeta_s> = zeta(s+ubar) ===")
for s, u in [(2.0, 1.5), (1.1, 1.1), (1.2 + 0.3j, 0.9 - 0.1j), (0.8 + 0.4j, 0.7 - 0.4j)]:
    lhs = overlap(complex(s), complex(u))
    rhs = _zeta(complex(s) + np.conj(complex(u)))
    print(f"  s={s}, u={u}: numeric={lhs:.8f}  zeta(s+ubar)={rhs:.8f}  |diff|={abs(lhs-rhs):.2e}")

# --------------------------------------------------------------------------
# Thm 2 (edge):  ||zeta_sigma||^2 = zeta(2 sigma); diverges at sigma=1/2.
# At sigma=1/2 the norm^2 is the HARMONIC series sum 1/n ~ ln N + gamma (log divergence),
# i.e. the pole of zeta at s=1.  (NOT 2*sqrt(N); that would be sum n^{-1/2}.)
# --------------------------------------------------------------------------
print("\n=== Thm 2 edge: ||zeta_sigma||^2 = zeta(2 sigma), pole at sigma=1/2 ===")
GAMMA = 0.5772156649015329
for sigma in [0.75, 0.6, 0.5, 0.45]:
    partials = []
    for N in [10**3, 10**4, 10**5, 10**6]:
        n = np.arange(1, N + 1, dtype=np.float64)
        partials.append(np.sum(n ** (-2 * sigma)))
    tag = f"zeta(2s)={_zeta(2*sigma).real:.5f} (converges)" if sigma > 0.5 else "DIVERGES"
    print(f"  sigma={sigma}: partials(1e3..1e6)={['%.4f' % v for v in partials]}  {tag}")
print(f"  sigma=0.5 is harmonic: ln(1e6)+gamma = {np.log(1e6)+GAMMA:.4f}  (matches last partial)")

# --------------------------------------------------------------------------
# Thm 4:  <zeta_u|H|zeta_s>/<..> = -zeta'/zeta(s+u) = sum_n Lambda(n) n^{-(s+u)}.
# --------------------------------------------------------------------------
def von_mangoldt_series(z, N=300_000):
    sieve = np.ones(N + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(N**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    total = mpc(0)
    for p in np.nonzero(sieve)[0]:
        pk, lp = int(p), mp.log(int(p))
        while pk <= N:
            total += lp * mpc(pk) ** (-z)
            pk *= int(p)
    return complex(total)


print("\n=== Thm 4: <zeta_u|H|zeta_s>/<..> = -zeta'/zeta(s+u) ===")
for z in [2.3 + 0.2j, 1.6]:
    lhs = von_mangoldt_series(mpc(z))
    rhs = complex(-mp.zeta(mpc(z), derivative=1) / mp.zeta(mpc(z)))
    print(f"  s+u={z}: sumLambda={lhs:.6f}  -zeta'/zeta={rhs:.6f}  |diff|={abs(lhs-rhs):.2e}")

# --------------------------------------------------------------------------
# Lemma 3:  <m|F*F|n> = sum_{p m = q n} conj(a_p) a_q  (prime-swap graph).
# F = sum_p a_p V_p,  V_p|n> = |pn>,  a_p = sqrt(log p) p^{-1/4} (critical k=1 weight).
# --------------------------------------------------------------------------
print("\n=== Lemma 3: <m|F*F|n> prime-swap matrix elements ===")
primes = [2, 3, 5, 7, 11, 13]
alpha = {p: np.sqrt(np.log(p)) * p**-0.25 for p in primes}


def matelem(m, n):
    tot = 0.0
    for p in primes:
        for q in primes:
            # <m|V_p^* V_q|n> = [ p m == q n ]
            if p * m == q * n:
                tot += alpha[p] * alpha[q]
    return tot


diag = sum(alpha[p] ** 2 for p in primes)
print(f"  predicted diagonal sum_p a_p^2 = {diag:.6f}")
for n in [1, 6, 12, 30]:
    print(f"   <{n}|F*F|{n}> = {matelem(n, n):.6f}")
print(f"  single swap 2->3 in 30: <45|F*F|30> = {matelem(45,30):.6f}  (a_2*a_3 = {alpha[2]*alpha[3]:.6f})")
print(f"  no single swap:         <35|F*F|30> = {matelem(35,30):.6f}  (expected 0)")

# --------------------------------------------------------------------------
# Lemma 1:  V_m S = S^m V_m   (S|n>=|n+1>, V_m|n>=|mn>).
# --------------------------------------------------------------------------
print("\n=== Lemma 1: V_m S = S^m V_m ===")
ok = all(
    m * (n + 1) == m * n + m  # V_m S|n> = |m(n+1)>  vs  S^m V_m|n> = |mn+m>
    for m in (2, 3, 5)
    for n in range(1, 21)
)
print(f"  V_m S = S^m V_m on basis 1..20, m in {{2,3,5}}: {ok}")
