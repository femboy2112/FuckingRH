#!/usr/bin/env python3
"""Round006 ckpt8: finite completion with pole-cancelling boundary, then the positivity test.

Build an explicit finite completed object, holomorphic on H_{1/2}, converging to xi'/xi on Re s>1,
and TEST whether it is positive-real (Re F_P >= 0) on H_{1/2}.  This is the crack-or-die experiment.

Cutoff-dependent boundary (Euler-Maclaurin pole counterterm):
    reg_P(s) := int_1^P x^{-s} dx = (1 - P^{1-s})/(s-1),
which -> 1/(s-1) on Re s>1 as P->infty, and = log P at s=1 (ENTIRE in s -- no pole).
    A_{inf,P}(s) := 1/s - (1/2)log pi + (1/2)psi(s/2) + reg_P(s).
    F_P(s) := A_{inf,P}(s) - sum_{p^k <= P} Lambda(p^k) (p^k)^{-s}.

F_P's "prime part" reg_P - sum_{n<=P} Lambda(n) n^{-s} = -int_1^P x^{-s} d(psi(x)-x) is exactly the
explicit-formula fluctuation; positivity of Re F_P on H_{1/2} is governed by the zeros. We measure it.

numpy/scipy float for the grid scan (double precision is ample to detect sign); mpmath only for the
xi'/xi convergence cross-check.
"""
import numpy as np
from scipy.special import digamma as sp_digamma
from sympy import primerange
from mpmath import mp, zeta, digamma, loggamma, diff, log as mlog, mpc, mpf, pi
mp.dps = 25
LOGPI = np.log(np.pi)


def mangoldt_powers(P):
    ns, Ls = [], []
    for p in primerange(2, P + 1):
        pk, k = p, 1
        while pk <= P:
            ns.append(pk); Ls.append(np.log(p)); pk *= p; k += 1
    return np.array(ns, float), np.array(Ls, float)


def reg_P(s, P):
    return (1 - P ** (1 - s)) / (s - 1)


def F_P_np(s, P, ns, Ls):
    # s: complex scalar or array
    A = 1 / s - LOGPI / 2 + sp_digamma(s / 2) / 2 + reg_P(s, P)
    prime = np.tensordot(Ls, ns[:, None] ** (-s), axes=(0, 0)) if np.ndim(s) else np.sum(Ls * ns ** (-s))
    return A - prime


# ---- convergence cross-check (mpmath) ----
def xi_log_deriv(s):
    def logxi(z):
        return (mlog(mpf(1) / 2) + mlog(z) + mlog(z - 1) - z * mlog(pi) / 2
                + loggamma(z / 2) + mlog(zeta(z)))
    return diff(logxi, s)


print("convergence F_P -> xi'/xi on Re s>1 (float F_P vs mpmath xi'/xi):")
for P in (200, 2000):
    ns, Ls = mangoldt_powers(P)
    for s in (2.0 + 1.0j, 1.3 + 4.0j):
        f = F_P_np(s, P, ns, Ls)
        x = complex(xi_log_deriv(mpc(s.real, s.imag)))
        print(f"  P={P:5d} s={s}: F_P={f: .5f}  xi'/xi={x: .5f}  err={abs(f-x):.2e}")

print("\nF_P holomorphic at s=1 (no pole):")
for P in (200, 2000):
    ns, Ls = mangoldt_powers(P)
    for eps in (0.05, 0.005):
        print(f"  P={P:5d} F_P(1+{eps}) = {F_P_np(1+eps+0j, P, ns, Ls): .4f}  (finite)")

print("\n=== POSITIVITY TEST: min Re F_P over grids in H_{1/2} ===")


def scan(P, ns, Ls, sig_lo, sig_hi, nsig=24, tmax=80, nt=400):
    sig = np.linspace(sig_lo, sig_hi, nsig)
    t = np.linspace(0.05, tmax, nt)
    S, T = np.meshgrid(sig, t, indexing='ij')
    s = (S + 1j * T).ravel()
    vals = np.array([F_P_np(z, P, ns, Ls) for z in s])
    re = vals.real
    k = int(np.argmin(re))
    return re.min(), (float(s[k].real), float(s[k].imag))


for P in (200, 2000, 20000):
    ns, Ls = mangoldt_powers(P)
    m_strip, a_strip = scan(P, ns, Ls, 0.52, 0.98)
    m_euler, a_euler = scan(P, ns, Ls, 1.02, 3.0)
    print(f"  P={P:6d}: min Re F_P on STRIP(1/2,1) = {m_strip:+.4f} at s={a_strip[0]:.3f}+{a_strip[1]:.2f}i;"
          f"  on Re s>1 = {m_euler:+.4f} at {a_euler[0]:.3f}+{a_euler[1]:.2f}i")

print("""
Reading: if min Re F_P < 0 in the strip and stays negative as P grows, the natural finite completion is
NOT positive-real on H_{1/2}; hypothesis (P) of Schur-Vitali FAILS for this family. The negative locus is
the explicit-formula fluctuation = the zeros talking. This is the wall, measured. RH open.
""")
