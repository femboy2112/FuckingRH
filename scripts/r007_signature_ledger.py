#!/usr/bin/env python3
"""Round007 probe A: signature ledger of the Suzuki screw kernel and its adelic pieces.

Suzuki (even, finite at each t>=0):
  Psi(t) = 8(cosh(t/2)-1)                                [POLE sector]
         - sum_{p^k<=e^t} (log p) p^{-k/2} (t - k log p)  [PRIME ramps, enter with a MINUS]
         + (t/2)(psi(1/4)-log pi)                         [ARCH linear]
         + (1/4)(C - e^{-t/2} Phi(e^{-2t},2,1/4)).        [ARCH lerch]
Screw kernel K_C[i,j] = C(t_i)+C(t_j)-C(|t_i-t_j|). RH <=> K_Psi >= 0 for all windows.

Questions (decisive):
  (1) is full K_Psi PSD on the window (RH holds on a finite window -> should be, modulo the trivial t=0 null)?
  (2) signature of each PIECE's screw kernel: which pieces are CND (PSD) and which carry negatives?
  (3) THE KEY ONE: as the window T grows, does the number of negative eigenvalues of the
      pole-sector kernel (and of Psi - prime - arch) stay BOUNDED (finite-rank obstruction, tractable)
      or GROW (the hard diverging wall)?
"""
import numpy as np
from mpmath import mp, mpf, digamma, catalan, pi, log as mlog
mp.dps = 25
LIN = float((digamma(mpf(1)/4) - mlog(pi)) / 2)
Cc  = float(pi**2 + 8*catalan)


def prime_powers(X):
    X = int(X); s = np.ones(X+1, bool); s[:2] = False
    for i in range(2, int(X**0.5)+1):
        if s[i]: s[i*i::i] = False
    out = []
    for p in np.nonzero(s)[0]:
        pk = int(p)
        while pk <= X:
            out.append((pk, float(np.log(p)))); pk *= int(p)
    return out


def lerch_block(t):
    z = np.exp(-2*t); ssum = 1/0.25**2; k = 1; term = 1.0
    while term > 1e-18 and k < 20000:
        term = z**k/(k+0.25)**2; ssum += term; k += 1
    return (Cc - np.exp(-t/2)*ssum)/4


def components(T, dt):
    M = int(round(T/dt)); tg = np.arange(M+1)*dt
    pole = np.array([8*(np.cosh(a/2)-1) for a in tg])
    archlin = LIN*tg
    archler = np.array([lerch_block(a) if a > 0 else lerch_block(1e-9) for a in tg])
    pp = prime_powers(int(np.exp(T))+2)
    prime = np.zeros(M+1)
    for k, a in enumerate(tg):
        prime[k] = -sum(lp*(pk**-0.5)*(a-np.log(pk)) for (pk, lp) in pp if np.log(pk) <= a+1e-12)
    arch = archlin + archler
    full = pole + prime + arch
    full[0] = pole[0] = prime[0] = arch[0] = 0.0   # Psi(0)=0 convention per piece's screw use
    return tg, dict(pole=pole, prime=prime, arch=arch, full=full)


def screw(C):
    M = len(C)-1; i = np.arange(M+1); D = np.abs(i[:, None]-i[None, :])
    return C[:, None] + C[None, :] - C[D]


def sig(K, tol=1e-7):
    w = np.linalg.eigvalsh(K); t = tol*max(1, abs(w).max())
    return int((w > t).sum()), int((w < -t).sum()), float(w.min()), float(w.max())


if __name__ == "__main__":
    dt = 0.05
    print("component screw-kernel signatures (pos, NEG, min_eig, max_eig), dt=0.05:")
    for T in (5, 6, 7, 8):
        tg, C = components(T, dt)
        print(f"\n T={T} (grid {len(tg)}):")
        for name in ("full", "pole", "prime", "arch"):
            p, n, mn, mx = sig(screw(C[name]))
            tag = ""
            if name == "full":  tag = "  <- RH-on-window: NEG should be 0 (nontrivial)"
            if name == "pole":  tag = "  <- expect rank-2 signature (1,1): NEG=1"
            print(f"   {name:6s}: (+{p:3d}, -{n:3d})  min={mn:+.3e} max={mx:+.3e}{tag}")

    print("\n(3) KEY: negative-eigenvalue count of each piece vs window T (bounded or growing?):")
    for name in ("pole", "prime", "arch"):
        row = []
        for T in (5, 6, 7, 8, 9):
            _, C = components(T, dt)
            _, n, _, _ = sig(screw(C[name]))
            row.append(n)
        print(f"   {name:6s}: NEG count at T=5,6,7,8,9 = {row}   "
              f"{'BOUNDED' if max(row)<=max(2,row[0]+1) else 'GROWING'}")
    print("\nReading: pole NEG bounded (=1, finite-rank) => obstruction is low-rank/tractable.")
    print("prime NEG count tells whether the minus-ramp prime sector's indefiniteness is finite-rank")
    print("or diverges with the window. RH open.")
