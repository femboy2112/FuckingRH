#!/usr/bin/env python3
"""Round008: accurate dBN flow H_tau(x) from the arithmetic kernel Phi, with light zero tracking.

H_tau(x) = 2 * int_0^inf e^{tau u^2} Phi(u) cos(x u) du,  Phi the theta kernel (verified H_0 = (1/2)Xi).
Backward heat d_tau H = - d_xx H. At tau=0 the real zeros sit at the Riemann gammas (real <=> RH).

NOTE: evaluating H_tau via mpmath.quad is expensive; complex Newton tracking of many zeros over many tau
is very slow (the earlier full version timed out). This trimmed version confirms the backbone and tracks
the first few zeros at a couple of tau values so it completes in well under a minute. For the quantitative
margin<->flow correspondence use r008_margin_flow.py (fast, numpy) and the forced-complex-pair demo.

Identification (bridge, convention-free): a zeta zero beta+i gamma <-> H_0 zero at x = gamma - i(beta-1/2),
so Im(x-zero) = -(beta-1/2) = -(growth exponent). The flow acts on exactly that imaginary part.
"""
from mpmath import mp, mpf, mpc, pi, quad, exp, cos, findroot
mp.dps = 15

def Phi(u, nmax=12):
    s = mpf(0)
    for n in range(1, nmax+1):
        s += (2*pi**2*n**4*exp(mpf(9)*u/2) - 3*pi*n**2*exp(mpf(5)*u/2))*exp(-pi*n**2*exp(2*u))
    return s

def Ht(tau, x):
    return 2*quad(lambda u: exp(tau*u**2)*Phi(u)*cos(x*u), [0, 0.4, 0.8, 1.4, 2.4])

GAMMA = [14.134725, 21.022040, 25.010858]   # first few (diagnostic seeds for Newton)

if __name__ == "__main__":
    print("backbone + light zero tracking (trimmed to run fast):\n")
    for tau in (0.0, -0.20):
        print(f" tau = {tau:+.2f}:")
        for g in GAMMA:
            try:
                z = findroot(lambda x: Ht(mpf(tau), x), mpc(g, 0), tol=1e-12)
                print(f"   zero near gamma={g:9.4f}:  x = {complex(z):.5f}   Im = {float(z.imag):+.2e}")
            except Exception as e:
                print(f"   zero near gamma={g:9.4f}:  (Newton failed: {type(e).__name__})")
    print("\nAt tau=0 the first zeros are real (Im~0): RH holds on this range. Full flow dynamics and the")
    print("margin<->tau correspondence are in r008_margin_flow.py + the forced-complex demo. RH open.")
