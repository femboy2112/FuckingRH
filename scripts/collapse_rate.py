#!/usr/bin/env python3
"""Collapse law of the finite-place-only stability radius (toward C84/directive-E theorem).

Finding: rad(E_L^+) = eps_+ ~ C * lambda0(L) / ||K1||_L,  C ~ 34 (empirical, ~const),
where lambda0 = smallest eigenvalue of the reduced K^circ at eps=0 (slowly decaying),
and ||K1|| = Frobenius norm of the tilt-derivative screw kernel K1 = screw(d/deps Psi),
d/deps Psi(t) = sum_{n<=e^t} Lambda(n) log n / sqrt n * (t - log n)  (an explicit Euler sum ~ e^{cL}).
So the window collapses ~ e^{-cL}, c~0.86, set by the prime-tilt sensitivity over the spectral floor.
Deps: numpy, mpmath.
"""
import numpy as np
from mpmath import mp, mpf, digamma, catalan, pi, log as mlog
mp.dps = 25
LIN = float((digamma(mpf(1)/4) - mlog(pi))/2); Cc = float(pi**2 + 8*catalan)

def mangoldt(X):
    X = int(X); s = np.ones(X+1, bool); s[:2] = False
    for i in range(2, int(X**0.5)+1):
        if s[i]: s[i*i::i] = False
    ns, lp = [], []
    for p in np.nonzero(s)[0]:
        pk, L = int(p), np.log(p)
        while pk <= X: ns.append(pk); lp.append(L); pk *= int(p)
    return np.array(ns, float), np.array(lp)

def lblock(t):
    z = np.exp(-2*t); s = 1/0.25**2; k = 1; term = 1
    while term > 1e-18 and k < 20000: term = z**k/(k+0.25)**2; s += term; k += 1
    return (Cc - np.exp(-t/2)*s)/4

def psigrid(T, dt, eps=0.0):
    ns, lp = mangoldt(int(np.exp(T))+2); ln = np.log(ns); w = lp/np.sqrt(ns)*ns**(-eps)
    M = int(round(T/dt)); out = np.empty(M+1)
    for k in range(M+1):
        a = k*dt
        if a == 0: out[k] = 0.0; continue
        m = ln <= a+1e-12; out[k] = 8*(np.cosh(a/2)-1) - np.sum(w[m]*(a-ln[m])) + LIN*a + lblock(a)
    return out, M

def dpsi(T, dt):
    ns, lp = mangoldt(int(np.exp(T))+2); ln = np.log(ns); w = lp/np.sqrt(ns)*ln
    M = int(round(T/dt)); out = np.empty(M+1)
    for k in range(M+1):
        a = k*dt
        if a == 0: out[k] = 0.0; continue
        m = ln <= a+1e-12; out[k] = np.sum(w[m]*(a-ln[m]))
    return out, M

def screw(psi, M):
    i = np.arange(M+1); D = np.abs(i[:, None]-i[None, :]); return psi[:, None]+psi[None, :]-psi[D]

if __name__ == "__main__":
    dt = 0.04
    red = lambda T, e: screw(psigrid(T, dt, e)[0], int(round(T/dt)))[1:, 1:]
    mineig = lambda T, e: np.linalg.eigvalsh(red(T, e)).min()
    def bisect(T):
        lo, hi = 0.0, 1e-3
        for _ in range(60):
            mid = (lo+hi)/2
            lo, hi = (mid, hi) if mineig(T, mid) > 0 else (lo, mid)
        return (lo+hi)/2
    print(" T   lambda0     ||K1||     eps_+        C=eps_+*||K1||/lambda0")
    for T in range(5, 11):
        lam0 = np.linalg.eigvalsh(red(T, 0.0)).min()
        d, M = dpsi(T, dt); K1 = screw(np.concatenate([[0.0], d[1:]]), M)[1:, 1:]
        nK1 = np.linalg.norm(K1); ep = bisect(T)
        print("  %2d  %.6f  %.3e  %.3e     %.2f" % (T, lam0, nK1, ep, ep*nK1/lam0))
    print("C ~ 34 (const) => eps_+ ~ C lambda0/||K1||; ||K1|| ~ e^{0.86 T} (Euler sum) => rad ~ e^{-cL}.")
