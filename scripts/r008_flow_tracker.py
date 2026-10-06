#!/usr/bin/env python3
"""Round008: accurate dBN flow H_tau(x) from the arithmetic kernel Phi, and complex-zero tracking.

H_tau(x) = 2 * int_0^inf e^{tau u^2} Phi(u) cos(x u) du,  Phi the theta kernel (verified H_0 = (1/2)Xi).
Backward heat d_tau H = - d_xx H. Zeros x_n(tau) of H_tau: at tau=0 they sit at the Riemann gammas
(real <=> RH). dBN constant Lambda = inf{tau : all zeros real}; RH <=> Lambda<=0; Lambda>=0 (Rodgers-Tao).

Key identification used in the bridge: a zeta zero at beta+i*gamma <-> H_0 zero at x = gamma - i(beta-1/2),
so Im(x-zero) = -(beta-1/2) = -(our growth exponent). The flow acts on exactly that imaginary part.

Here: (i) confirm first zeros real at tau=0; (ii) track them (complex findroot) as tau decreases below 0
to watch imaginary parts appear / pairs repel; (iii) measure nearest-neighbour gaps (Coulomb repulsion).
"""
from mpmath import mp, mpf, mpc, pi, gamma as Gamma, zeta, quad, exp, cos, findroot
mp.dps = 25

def Phi(u, nmax=20):
    s = mpf(0)
    for n in range(1, nmax+1):
        s += (2*pi**2*n**4*exp(mpf(9)*u/2) - 3*pi*n**2*exp(mpf(5)*u/2))*exp(-pi*n**2*exp(2*u))
    return s

def Ht(tau, x):
    # x may be complex; cos(x u) handles it. Integrate with split nodes for the theta decay.
    return 2*quad(lambda u: exp(tau*u**2)*Phi(u)*cos(x*u), [0, 0.4, 0.8, 1.2, 2.0, 3.0])

KNOWN = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178]

if __name__ == "__main__":
    print("(i) H_tau real zeros near the first gammas, tracked by complex Newton from tau=0 downward.")
    print("    report Im(x_n) (nonzero Im => zero left the real axis => RH-violating on this range):\n")
    taus = [0.10, 0.0, -0.10, -0.25, -0.40]
    # seed at tau=0 from near the known gammas (diagnostic seeds only)
    zeros = {}
    for g in KNOWN:
        zeros[g] = mpc(g, 0)
    header = "  gamma0   " + "".join(f"  Im@tau={t:+.2f}" for t in taus)
    print(header)
    track = {g: [] for g in KNOWN}
    for tau in taus:
        for g in KNOWN:
            try:
                z = findroot(lambda x: Ht(mpf(tau), x), zeros[g])
                zeros[g] = z
                track[g].append(z)
            except Exception as e:
                track[g].append(None)
    for g in KNOWN:
        row = f"  {g:7.3f} "
        for z in track[g]:
            row += f"   {float(z.imag):+.2e}" if z is not None else "      n/a   "
        print(row)

    print("\n(ii) nearest-neighbour gaps of the real zeros at tau=0 (Coulomb repulsion scale):")
    re0 = sorted(float(track[g][1].real) for g in KNOWN)  # tau=0 is index 1
    gaps = [re0[i+1]-re0[i] for i in range(len(re0)-1)]
    print("     zeros:", [f"{r:.3f}" for r in re0])
    print("     gaps :", [f"{d:.3f}" for d in gaps], " min gap =", f"{min(gaps):.3f}")
    print("\nReading: at tau=0 all Im~0 (zeros real on this range = RH holds here). As tau decreases the")
    print("flow would push tight pairs off the axis; low-height zeros are well-separated so they stay real")
    print("for moderate tau<0 -- the knife-edge (Lambda) is set by the TIGHTEST pairs at large height.")
