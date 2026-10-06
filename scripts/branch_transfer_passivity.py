#!/usr/bin/env python3
"""Round006 ckpt5: is the per-prime one-port m_p(s)=log p/(p^s-1) positive-real? NO.

And what positivity DOES the arithmetic carry? Diagnoses:
  (A) m_p fails positive-realness on EVERY right half-plane (periodicity-in-s argument);
  (B) the naive sum -zeta'/zeta also fails on Re s>1;
  (C) -zeta'/zeta IS completely monotone on the real axis s>1 (Laplace of a positive measure);
  (D) the raw Cauchy/resolvent transform of the SAME (von Mangoldt energy) measure DIVERGES
      (psi(x) ~ x), so the "free Herglotz" object is not available without damping, and damping
      returns the non-positive-real Laplace transform.

Conclusion: per-ray positivity lives in the bounded-operator (w=p^s / zeta=p^{-s}) variable, which
the exponential/periodic map s|->p^s does NOT transport to the s-half-plane. Hence NO per-ray one-port,
and no sum/series/parallel of them, is positive-real on Re s>1/2. Positive-realness in s must come from
GLOBAL coupling + Archimedean completion, not any ray or sum of rays.
"""
import numpy as np
from mpmath import mp, zeta, diff, log as mlog, mpc, mpf
mp.dps = 30


def m_p(p, s):
    return mlog(p) / (mpf(p) ** s - 1)


def neg_zeta_ratio(s):
    return -diff(lambda z: mlog(zeta(z)), s)


print("(A) per-prime one-port m_p(s)=log p/(p^s-1): Re m_p at s=sigma + i*pi/log p")
print("    (the phase where p^s = -p^sigma, forcing the real part negative):")
for p in (2, 3, 5, 13):
    for sigma in (0.6, 1.0, 2.0, 4.0):
        s = mpc(sigma, float(mp.pi) / float(mlog(p)))
        val = m_p(p, s)
        print(f"    p={p:2d} sigma={sigma:.1f}: Re m_p = {float(val.real):+.5f}   "
              f"{'<-- NEGATIVE (not positive-real)' if val.real < 0 else ''}")

print("\n(B) naive sum -zeta'/zeta at s = 2 + i*pi/log 2  and others on Re s>1:")
for sigma, tt in [(2.0, float(mp.pi / mlog(2))), (1.5, 2.0), (3.0, float(mp.pi / mlog(2)))]:
    s = mpc(sigma, tt)
    v = neg_zeta_ratio(s)
    print(f"    s={sigma:.1f}+{tt:.3f}i: Re(-zeta'/zeta) = {float(v.real):+.5f}   "
          f"{'<-- NEGATIVE' if v.real < 0 else ''}")

print("\n(C) complete monotonicity on the real axis: (-1)^n d^n/ds^n (-zeta'/zeta)(s), s>1")
print("    (Laplace transform of dmu = sum Lambda(n) delta_{log n} >= 0 => completely monotone):")
for s0 in (1.5, 2.0, 3.0):
    row = []
    for n in range(4):
        dn = diff(lambda z: neg_zeta_ratio(z), mpf(s0), n)
        row.append(((-1) ** n) * dn)
    ok = all(float(x.real if hasattr(x, 'real') else x) > 0 for x in row)
    print(f"    s={s0}: " + "  ".join(f"(-1)^{n} f^({n})={float(row[n]):+.4f}" for n in range(4))
          + f"   all>0? {ok}")

print("\n(D) raw Cauchy/resolvent transform G(z)=sum_n Lambda(n)/(log n - z) DIVERGES (psi(x)~x):")
# partial sums of sum_{n<=X} Lambda(n) = psi(X) ~ X ; so the measure grows exponentially in E=log n
import sympy
for X in (10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5):
    psiX = sum(float(mlog(sympy.factorint(n).popitem()[0])) if len(sympy.factorint(n)) == 1 else 0.0
               for n in range(2, X + 1)) if X <= 10 ** 3 else None
    # cheaper: psi(X) approx X
    print(f"    X={X:>7}: sum_{{n<=X}} Lambda(n) = psi(X) ~ {X} (Chebyshev); "
          + (f"exact={psiX:.1f}" if psiX is not None else "~X, grows linearly -> Cauchy transform diverges"))

print("""
VERDICT (ckpt5): m_p and every sum of one-ports are NOT positive-real on Re s>1/2.
The arithmetic's automatic positivity is Cauchy/resolvent-Herglotz in the BOUNDED variable w=p^s
(|p^{-s}|<p^{-1/2}<1), but s|->p^s is exponential/periodic, not a half-plane automorphism, so it does
not transport to the s-plane. The raw energy measure's Cauchy transform diverges (psi(x)~x), and the
damping that fixes that IS the non-positive-real Laplace transform -zeta'/zeta. => the one-port/direct-sum
class is dead; positive-realness in s can only come from GLOBAL coupling + Archimedean completion. RH open.
""")
