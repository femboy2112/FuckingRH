#!/usr/bin/env python3
r"""
Round 008 -- The prime-ray symbol M_a(xi): mean = counterterm, dips = where zeros hide.

Fourier-side reading of the frontier's prime-ray Dirichlet energy
    E_prime,a(v) = sum_{p^k<=e^{2a}} (log p / p^{k/2}) * || v - tau_{k log p} v ||^2.
Since tau_h has Fourier symbol e^{-i h xi} and ||v - tau_h v||^2 = (1/2pi) \int 4 sin^2(h xi/2)|vhat|^2,
    E_prime,a(v) = (1/2pi) \int M_a(xi) |vhat(xi)|^2 dxi,
    M_a(xi) = sum_{p^k<=e^{2a}} (log p / p^{k/2}) * 4 sin^2( (k log p) xi / 2 )   >= 0.

Three exact structural facts (all pure-prime; NO zeta zeros are used as input):

  (A) M_a(xi) >= 0 everywhere  -- the prime-ray Laplacian is PSD; the prime arithmetic contributes
      NO negativity.  (Confirms Round-008 flatness: the sign battle is not in the primes.)

  (B) mean_xi M_a(xi) = 2 * sum w_{p,k} = the prime part of Suzuki's global counterterm V_a.
      (Average of 4 sin^2 over xi is 2.)  So the counterterm is literally the MEAN of the symbol.

  (C) EXACT identity: mean - M_a(xi) = 2 * sum_n Lambda(n) n^{-1/2} cos(xi log n)
      = 2 * Re[ (-zeta'/zeta)(1/2 - i xi) ]  (truncated to n <= e^{2a}).
      So the symbol's fluctuation about its mean is literally twice the truncated -zeta'/zeta on the
      critical line.  Its ANALYTIC CONTINUATION has poles exactly at xi = +/- gamma (the nontrivial
      zero ordinates).  BUT a finite horizon does NOT resolve those poles: at a=3 the raw dips are
      dominated by small-prime beats (periods 2pi/log 2, 2pi/log 3, ...), nowhere near the first
      ordinate 14.13.  The zeros are a datum of the CONTINUATION, not of the finite/algebraic symbol
      -- this is Round-006 C103 (group completion != analytic continuation) seen on the symbol.

Conclusion (honest, RH-inert): the localized-Weil positivity, Fourier-side, becomes
    (Archimedean symbol ~ c|xi|)  +  (M_a(xi) - mean)  >=  smooth remainder,
i.e. the Archimedean |xi|-energy must cover the sign-indefinite prime-symbol fluctuation.  That is
the frontier wall made fully explicit.  It cannot be won by a uniform gap (frontier proven-negative
g(a)->0).  The resonances that would decide the sign sit in the continuation (at the zeros), outside
the finite symbol -- so no finite/algebraic computation here can see them.  This proves no RH progress.
"""

import numpy as np

trapz = getattr(np, "trapezoid", getattr(np, "trapz", None))  # NumPy 2.x renamed trapz -> trapezoid

# ---- diagnostic only: first zeta zero ordinates, NEVER used in any construction below ----
GAMMA_DIAG = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062]


def prime_powers(bound):
    b = int(bound)
    sieve = np.ones(b + 1, dtype=bool)
    sieve[:2] = False
    for q in range(2, int(b ** 0.5) + 1):
        if sieve[q]:
            sieve[q * q::q] = False
    primes = np.nonzero(sieve)[0]
    out = []
    for q in primes:
        pk, k = int(q), 1
        while pk <= bound:
            out.append((int(q), k, pk))
            k += 1
            pk *= int(q)
    return out


def main():
    a = 3.0
    bound = np.exp(2 * a)
    pks = prime_powers(bound)
    h = np.array([k * np.log(p) for (p, k, pk) in pks])        # displacements k log p
    w = np.array([np.log(p) / pk ** 0.5 for (p, k, pk) in pks])  # weights log p / p^{k/2}
    degree = w.sum()
    counterterm = 2 * degree
    print(f"a={a}, horizon e^(2a)={bound:.1f}, #prime-power edges={len(pks)}")
    print(f"prime-ray graph degree sum(w) = {degree:.6f}")
    print(f"prime part of Suzuki counterterm 2*sum(w) = {counterterm:.6f}")

    def M(xi):
        xi = np.atleast_1d(xi)[:, None]
        return (w[None, :] * 4.0 * np.sin(h[None, :] * xi / 2.0) ** 2).sum(axis=1)

    # ---- (A) PSD: M_a(xi) >= 0 ----
    xi_grid = np.linspace(0, 60, 240001)
    Mvals = M(xi_grid)
    print("\n(A) PSD check:  min M_a(xi) over [0,60] =", f"{Mvals.min():.3e}", "(>= 0: prime Laplacian PSD)")
    assert Mvals.min() >= -1e-9

    # ---- (B) mean of M_a = counterterm ----
    mean_num = trapz(Mvals, xi_grid) / (xi_grid[-1] - xi_grid[0])
    print(f"(B) window-mean of M_a over [0,60] = {mean_num:.6f}  vs  2*sum(w) = {counterterm:.6f}"
          f"   (rel.err {abs(mean_num-counterterm)/counterterm:.2%})")
    assert abs(mean_num - counterterm) / counterterm < 0.03

    # ---- Parseval cross-check: x-space correlation vs Fourier, for a smooth bump ----
    L = 2 * a + 4.0
    dx = 0.002
    xs = np.arange(-L, L, dx)
    v = np.where(np.abs(xs) < a, np.exp(-1.0 / np.maximum(a**2 - xs**2, 1e-12)), 0.0)  # C_c^inf bump in (-a,a)
    v /= np.sqrt(trapz(v * v, xs))                                                  # ||v||=1
    vhat = dx * np.fft.fft(v)
    xf = 2 * np.pi * np.fft.fftfreq(len(xs), d=dx)
    dxi = 2 * np.pi / (len(xs) * dx)   # uniform freq spacing; xf is UNSORTED (fftfreq wraps),
    #                                    so integrate by Riemann sum, never trapz.
    # correlation <v, tau_h v> two independent ways
    print("\nParseval cross-check  <v, tau_h v>  (x-space interp vs Fourier):")
    ok = True
    for hh in (np.log(2), np.log(3), np.log(5)):
        c_x = trapz(v * np.interp(xs - hh, xs, v, left=0, right=0), xs)
        c_f = dxi * np.sum(np.cos(hh * xf) * np.abs(vhat) ** 2) / (2 * np.pi)
        print(f"   h=log({int(round(np.exp(hh)))}): x-space={c_x:.6f}  fourier={c_f:.6f}  diff={abs(c_x-c_f):.1e}")
        ok = ok and abs(c_x - c_f) < 1e-3
    assert ok

    # assembled: E_prime(v) two ways
    E_x = sum(wi * (2 - 2 * trapz(v * np.interp(xs - hi, xs, v, left=0, right=0), xs))
              for wi, hi in zip(w, h))
    E_f = dxi * np.sum(M(xf) * np.abs(vhat) ** 2) / (2 * np.pi)
    print(f"\nE_prime,a(v):  x-space sum = {E_x:.6f}   Fourier \\int M|vhat|^2 = {E_f:.6f}   diff={abs(E_x-E_f):.1e}")
    assert abs(E_x - E_f) < 2e-2

    # ---- (C) EXACT: mean - M_a(xi) = 2 Re[(-zeta'/zeta)(1/2 - i xi)] (truncated) ----
    xi2 = np.linspace(0.5, 40, 200001)
    D = np.zeros_like(xi2)   # D(xi) = sum_n Lambda(n) n^{-1/2} cos(xi log n), built from PRIMES only
    for (p, k, pk) in pks:
        D += (np.log(p) / pk ** 0.5) * np.cos(xi2 * (k * np.log(p)))
    fluct = counterterm - M(xi2)
    err = np.max(np.abs(fluct - 2 * D))
    print(f"\n(C) identity  mean - M_a(xi) == 2*Re[(-zeta'/zeta)(1/2-i xi)]_trunc :  max|.|={err:.2e} (exact)")
    assert err < 1e-9
    # raw dips of the FINITE symbol are small-prime beats, NOT the ordinates:
    loc = (D[1:-1] > D[:-2]) & (D[1:-1] > D[2:]) & (D[1:-1] > 0.3 * D.max())
    peaks = sorted(xi2[np.nonzero(loc)[0] + 1].tolist())[:4]
    print("    raw dips of finite M_a at xi =", ", ".join(f"{t:.2f}" for t in peaks),
          "(small-prime beats 2pi/log2=%.2f, 2pi/log3=%.2f, ...)" % (2*np.pi/np.log(2), 2*np.pi/np.log(3)))
    print("    continuation poles (= zero ordinates, DIAGNOSTIC, NOT input):",
          ", ".join(f"{g:.2f}" for g in GAMMA_DIAG[:3]), "-- NOT resolved at finite horizon (C103).")

    print("\nALL CHECKS PASSED.  M_a>=0 (no prime negativity); mean(M_a)=counterterm (0.03%);")
    print("fluctuation = 2 Re[(-zeta'/zeta)(1/2-i xi)]_trunc, sign-indefinite.  The deciding")
    print("resonances live in the continuation (at the zeros), outside the finite symbol (C103).")
    print("The wall = Archimedean |xi|-energy must cover that fluctuation.  RH-inert; RH remains open.")


if __name__ == "__main__":
    main()
