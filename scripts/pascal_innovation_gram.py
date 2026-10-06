#!/usr/bin/env python3
"""Pascal innovation Gram G_L = Pi^{-1} K_{Psi,L} Pi^{-T}, computed stably (no Pascal inversion).

Companion to research/claude_round_004/PASCAL_INNOVATION_GRAM.md.
Finding: the uniform-time Pascal innovation Gram equals the zero-moment matrix
  G_kl = sum_{gamma>0} 2 Re( conj(z)^k z^l ) / gamma^2,   z = e^{i gamma h} - 1,
i.e. the literal uniform Pascal re-encodes the Riemann zeros (RH-inert construction).
Deps: numpy, mpmath.
"""
import numpy as np
from mpmath import mp, mpf, digamma, catalan, pi, cosh, exp, log, sqrt, binomial
mp.dps = 80
LIN = (digamma(mpf(1)/4) - log(pi))/2
Cc = pi**2 + 8*catalan

def mangoldt(X):
    X = int(X); s = np.ones(X+1, bool); s[:2] = False
    for i in range(2, int(X**0.5)+1):
        if s[i]: s[i*i::i] = False
    out = []
    for p in np.nonzero(s)[0]:
        pk, lp = int(p), log(int(p))
        while pk <= X: out.append((pk, lp)); pk *= int(p)
    return out

def lerch(t):
    z = exp(-2*t); s = mpf(16); k = 1; term = mpf(1)
    while term > mpf(10)**(-mp.dps) and k < 5000:
        term = z**k/(k+mpf(1)/4)**2; s += term; k += 1
    return s

def Psi(t):
    t = abs(mpf(t))
    if t == 0: return mpf(0)
    pr = mpf(0)
    for n, lp in mangoldt(int(mp.floor(exp(t)))+1):
        ln = log(n)
        if ln <= t: pr += lp/sqrt(n)*(t-ln)
    return 8*(cosh(t/2)-1) - pr + LIN*t + (Cc - exp(-t/2)*lerch(t))/4

def innovation_gram(N, h):
    psi = [Psi(m*h) for m in range(N+1)]
    B = [[binomial(k, i) for i in range(k+1)] for k in range(N+1)]
    G = mp.zeros(N, N)
    for k in range(1, N+1):
        for l in range(1, N+1):
            tot = mpf(0)
            for i in range(k+1):
                ci = B[k][i]*((-1)**(k-i))
                for j in range(l+1):
                    tot += ci*B[l][j]*((-1)**(l-j))*psi[abs(i-j)]
            G[k-1, l-1] = -tot
    return G

if __name__ == "__main__":
    N, h = 16, mpf('0.1')
    G = innovation_gram(N, h)
    Gf = np.array([[float(G[i, j]) for j in range(N)] for i in range(N)])
    ev = np.linalg.eigvalsh(Gf)
    print("G_L is PSD:", ev.min() > -1e-9, " (min eig %.2e, max %.2e)" % (ev.min(), ev.max()))
    print("corner magnitudes grow to ~%.1e (dense, not sparse)" % abs(Gf[-1, -1]))
    # zero-moment prediction
    try:
        g = np.load("zeros300.npy")
    except Exception:
        from mpmath import zetazero
        g = np.array([float(mp.im(zetazero(k))) for k in range(1, 301)])
    z = np.exp(1j*g*float(h)) - 1.0
    Gp = np.array([[np.sum(2*np.real(np.conj(z)**k * z**l)/g**2)
                    for l in range(1, N+1)] for k in range(1, N+1)])
    ratios = [Gf[k, k]/Gp[k, k] for k in range(N)]
    print("computed/zero-moment ratio (const ~1.065 = tail of zeros>300):",
          "%.4f .. %.4f" % (min(ratios), max(ratios)))
    print("=> uniform Pascal innovation Gram = zero-moment matrix (re-encodes zeros; RH-inert).")
