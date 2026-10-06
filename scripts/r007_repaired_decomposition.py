#!/usr/bin/env python3
"""Round007 probe B: repaired-tower decomposition and the rank of the residual obstruction.

Per prime p: h_p(t) = log p * sum_{k>=1} p^{-k/2} (|t| - k log p)_+ , slope M_p = log p/(sqrt p - 1).
Repaired tower D_p(t) = M_p|t| - h_p(t) >= 0 and (claim) CND -> screw kernel PSD. Verify.

Suzuki: Psi = 8(cosh(t/2)-1) - sum_p h_p + arch
      = sum_{p activated} D_p  +  B,
  B(t) = 8(cosh(t/2)-1) - (sum_{p activated} M_p)|t| + arch(t) - sum_{p not yet} h_p ... (within window
  only activated primes have h_p!=0, so B = pole - (sum_activated M_p)|t| + arch for t in window).

Decisive measurement: with the CND towers D_p pulled out, what is the NEGATIVE rank of the residual
bracket B's screw kernel, and does it stay BOUNDED (finite-rank => Pontryagin-kappa, tractable) or GROW
with the window (the hard diverging wall)?
"""
import numpy as np
from mpmath import mp, mpf, digamma, catalan, pi, log as mlog
mp.dps = 25
LIN = float((digamma(mpf(1)/4) - mlog(pi)) / 2)
Cc = float(pi**2 + 8*catalan)


def primes_upto(X):
    X = int(X); s = np.ones(X+1, bool); s[:2] = False
    for i in range(2, int(X**0.5)+1):
        if s[i]: s[i*i::i] = False
    return [int(p) for p in np.nonzero(s)[0]]


def lerch_block(t):
    z = np.exp(-2*t); ssum = 1/0.25**2; k = 1; term = 1.0
    while term > 1e-18 and k < 20000:
        term = z**k/(k+0.25)**2; ssum += term; k += 1
    return (Cc - np.exp(-t/2)*ssum)/4


def h_p(tg, p):
    lp = np.log(p); out = np.zeros_like(tg); k = 1
    while k*lp <= tg[-1]+1e-9:
        out += lp*p**(-k/2.0)*np.clip(tg-k*lp, 0, None); k += 1
    return out


def screw(C):
    M = len(C)-1; i = np.arange(M+1); D = np.abs(i[:, None]-i[None, :])
    K = C[:, None]+C[None, :]-C[D]; return K


def negrank(K, tol=1e-7):
    w = np.linalg.eigvalsh(K); t = tol*max(1, abs(w).max())
    return int((w < -t).sum()), float(w.min())


def build(T, dt):
    M = int(round(T/dt)); tg = np.arange(M+1)*dt
    pole = 8*(np.cosh(tg/2)-1)
    arch = LIN*tg + np.array([lerch_block(a) if a > 0 else lerch_block(1e-9) for a in tg])
    ps = [p for p in primes_upto(int(np.exp(T))+2)]
    activated = [p for p in ps if np.log(p) <= T+1e-9]
    SumD = np.zeros_like(tg); SumMabs = 0.0
    for p in activated:
        Mp = np.log(p)/(np.sqrt(p)-1.0)
        SumD += Mp*np.abs(tg) - h_p(tg, p)
        SumMabs += Mp
    B = pole - SumMabs*np.abs(tg) + arch
    Psi = pole - sum(h_p(tg, p) for p in activated) + arch
    for X in (pole, arch, SumD, B, Psi): X[0] = 0.0
    return tg, pole, arch, SumD, B, Psi, len(activated)


if __name__ == "__main__":
    dt = 0.05
    # sanity: a single repaired tower D_p is CND (PSD screw kernel)?
    print("sanity: single repaired tower D_p screw-kernel neg-rank (expect 0 => CND):")
    for p in (2, 3, 5, 7):
        tg = np.arange(0, 8+dt, dt)
        Mp = np.log(p)/(np.sqrt(p)-1.0)
        Dp = Mp*np.abs(tg) - h_p(tg, p); Dp[0] = 0.0
        nr, mn = negrank(screw(Dp))
        print(f"   p={p}: neg-rank={nr}  min_eig={mn:+.2e}  {'CND' if nr==0 else 'NOT CND'}")

    print("\nDECISIVE: neg-rank of residual bracket B (= pole - (sum M_p)|t| + arch) vs window T:")
    print("  (and of sum D_p, which should be CND=0; and full Psi, PSD on window):")
    for T in (5, 6, 7, 8, 9):
        tg, pole, arch, SumD, B, Psi, nact = build(T, dt)
        nrB, mnB = negrank(screw(B))
        nrD, _ = negrank(screw(SumD))
        nrP, mnP = negrank(screw(Psi))
        print(f"   T={T}: activated primes={nact:4d} | sumD neg-rank={nrD} | "
              f"B neg-rank={nrB:3d} (min {mnB:+.2e}) | Psi neg-rank={nrP} (min {mnP:+.2e})")
    print("\nReading: if B neg-rank stays BOUNDED -> the obstruction beyond the CND towers is finite-rank")
    print("(Pontryagin-kappa, de Branges-tractable). If it GROWS -> the hard diverging wall. RH open.")
