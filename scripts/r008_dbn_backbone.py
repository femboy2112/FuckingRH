#!/usr/bin/env python3
"""Round008: de Bruijn-Newman heat-flow backbone, built from the ARITHMETIC kernel Phi (no zeros used).

Polymath15 / Tao convention (self-checked below against known zeros, used only as a DIAGNOSTIC):
  Phi(u) = sum_{n>=1} (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) exp(-pi n^2 e^{2u}),   Phi even.
  H_t(x) = int_0^infty e^{t u^2} Phi(u) cos(x u) du.
  H_0(x) = (1/8) Xi(x/2)  (zeros of H_0 at x = 2*gamma_n, gamma_1=14.1347...) -- self-check prints them.
  PDE: d_t H = - d_xx H  (backward heat). RH <=> all zeros of H_0 real <=> Lambda <= 0 (Lambda>=0: Rodgers-Tao).

This script: compute Phi, H_t(x); locate real zeros as sign changes; verify the self-check scaling; then
scan t to watch real zeros (dis)appear -- the knife-edge near t=0 and Lehmer-type near-collisions.
"""
import numpy as np

def Phi(u, nmax=12):
    u = np.asarray(u, float)
    out = np.zeros_like(u)
    for n in range(1, nmax+1):
        out += (2*np.pi**2*n**4*np.exp(9*u/2) - 3*np.pi*n**2*np.exp(5*u/2))*np.exp(-np.pi*n**2*np.exp(2*u))
    return out

# integration grid in u (Phi super-exp-decays; even -> use [0,Umax] with factor 2)
U = np.linspace(0, 4.0, 8000)
dU = U[1]-U[0]
PHI = Phi(U)

def H(t, x):
    x = np.atleast_1d(np.asarray(x, float))
    w = np.exp(t*U**2)*PHI                      # weight in u
    # H_t(x) = 2 * int_0^inf w(u) cos(xu) du   (factor 2 from evenness; overall const irrelevant for zeros)
    M = np.cos(np.outer(x, U))                  # (len x, len U)
    return 2.0*(M*w).sum(axis=1)*dU

def real_zeros(t, xmax=60, nx=24000):
    xs = np.linspace(0.01, xmax, nx)
    h = H(t, xs)
    sign = np.sign(h)
    idx = np.where(sign[:-1]*sign[1:] < 0)[0]
    # linear interp for zero location
    zr = xs[idx] - h[idx]*(xs[idx+1]-xs[idx])/(h[idx+1]-h[idx])
    return zr

if __name__ == "__main__":
    print("self-check: Phi even?", np.allclose(Phi(np.array([0.3,0.7,1.0])), Phi(np.array([-0.3,-0.7,-1.0])), rtol=1e-6))
    z0 = real_zeros(0.0, xmax=90)
    print(f"H_0 first real zeros (x): {np.array2string(z0[:8], precision=4)}")
    print(f"  -> /2 (should be Riemann gammas 14.1347,21.0220,25.0109,30.4249,32.9351,...):")
    print(f"     {np.array2string(z0[:8]/2, precision=4)}")
    known = np.array([14.134725,21.022040,25.010858,30.424876,32.935062,37.586178,40.918719,43.327073])
    print(f"  max err vs gammas: {np.max(np.abs(np.sort(z0[:8])/2 - known)):.4f}")

    print("\n# real zeros of H_t below x=60 vs t (watch for zeros merging/vanishing as t decreases):")
    for t in (0.20, 0.10, 0.05, 0.0, -0.05, -0.10, -0.20):
        zr = real_zeros(t, xmax=60)
        print(f"   t={t:+.2f}: #real zeros (x<60) = {len(zr):3d}   first few: {np.array2string(zr[:5], precision=3)}")
    print("\n(As t decreases below Lambda, real zeros collide & leave the axis -> count drops. At t=0 the count")
    print(" is the true number of zeros below 60. RH <=> no complex zeros ever appear going down to t=0.)")
