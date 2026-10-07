#!/usr/bin/env python3
r"""
Round 009 / Pillar 3 -- Reflection positivity = the light cone; the integrate-and-fire "domino" flow.

Three faces of the SAME RH-equivalent, each matching a piece of the user's GR intuition. Everything is
standard (credit below); nothing is a proof; no zeta zeros are used as input (the off-line demo uses a
FREELY CHOSEN parameter r, not a real ordinate).

 (1) REFLECTION POSITIVITY.  Suzuki (JLMS 2023) Thm 1.2: RH <=> g=-Psi is a Krein screw function
     <=> the screw/covariance kernel  G_g(t,u) = Psi(t)+Psi(u)-Psi(t-u)  is positive semidefinite on
     every finite set.  Honest name: conditional-negative-definiteness / infinitely-divisible
     (Schoenberg-von Neumann 1941; Krein; Nakamura-Suzuki) -- the probabilistic face of "reflection
     positivity / positive-energy Hamiltonian" (Hilbert-Polya). We check PSD on a grid (DIAGNOSTIC
     consistency, NOT evidence for RH).

 (2) INTEGRATE-AND-FIRE "domino" dynamics (SCREW_SINC_LEVY_UNIFICATION.md section 7): Psi(t) is affine
     between prime events; at each event t=log(p^k) its slope jumps DOWN by Lambda(p^k)/p^{k/2}; RH <=>
     the reserve Psi never crosses zero.  "First domino sets the slope, the Archimedean reservoir bends
     it, the next prime fires."  The curvature is Psi'' = smooth Archimedean  -  impulsive prime train
     (the Weil kernel is -g''(t-u)).

 (3) THE LIGHT CONE as the on-line/off-line signature (FINITE_ZERO_SUZUKI_WEIL_TANGENT.md section 8):
     the finite Weil tangent Gram A(t,u)=sum e^{lambda(t-u)} is
       - on-line  lambda=+-i gamma  ->  2 cos(gamma(t-u))        : PSD rank<=2  (NULL / on the cone)
       - off-line {lambda,conj,-,-conj}, lambda=r+i gamma, r!=0 -> 4 cosh(r(t-u)) cos(gamma(t-u))
                                                                 : INDEFINITE  (TIMELIKE / off the cone)
     So RH <=> every mode is null (on the light cone); an off-line zero is a timelike (boost, cosh)
     mode and makes the Weil form indefinite.  r is the boost rapidity (= beta-1/2).

CREDIT: Suzuki 2023 (JLMS 108, Thm 1.2/1.7); Nakamura-Suzuki (infinite divisibility); Schoenberg-von
Neumann 1941 (CND); Weil 1952, Bombieri 2000 (quadratic form); Connes 1999; Lax-Phillips 1976,
Faddeev-Pavlov 1972 (literal light cone / finite propagation); Burnol (conductor operator, propagator);
Berry-Keating 1999 and Sierra 2014 (Dirac/Rindler light-cone Hamiltonian). "Causality <=> RH" (adelic
Lax-Phillips) is a PROGRAM, not a theorem.  RH IS OPEN.
"""

import os
import sys
import numpy as np
import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from suzuki_psi import psi_suzuki, screw_kernel, prime_power_events_up_to, active_horizon  # noqa: E402


def banner(t):
    print("\n" + "=" * 76 + "\n" + t + "\n" + "=" * 76)


def main():
    banner("1. Reflection positivity: screw kernel G_g(t,u)=Psi(t)+Psi(u)-Psi(t-u) PSD <=> RH")
    print("   (Suzuki 2023 Thm 1.2; CND/infinitely-divisible, Schoenberg-von Neumann 1941. DIAGNOSTIC,")
    print("    not evidence for RH.)")
    ts = [mp.mpf(x) / 10 for x in range(3, 31, 2)]   # t = 0.3,0.5,...,2.9
    dps = 30
    n = len(ts)
    G = mp.zeros(n, n)
    for i in range(n):
        for j in range(i, n):
            g = screw_kernel(ts[i], ts[j], dps=dps)
            G[i, j] = g
            G[j, i] = g
    Gnp = np.array([[float(G[i, j]) for j in range(n)] for i in range(n)])
    ev = np.linalg.eigvalsh(Gnp)
    print(f"   grid n={n} on t in [0.3,2.9];  min eig(G) = {ev.min():.3e}  (>=0 => PSD, screw/RH-consistent)")
    print(f"   eig range [{ev.min():.3e}, {ev.max():.3e}]")
    assert ev.min() > -1e-6

    banner("2. Integrate-and-fire: Psi slope jumps DOWN by Lambda(p^k)/p^{k/2} at each event t=log(p^k)")
    print("   (SCREW_SINC_LEVY section 7; the 'domino' flow. RH <=> reserve Psi never crosses 0.)")
    evs = prime_power_events_up_to(active_horizon(mp.mpf('3.5')))
    eps = mp.mpf('1e-5')
    print(f"   {'event p^k':>10} {'t=log(p^k)':>12} {'slope jump (right-left)':>24} {'-Lambda/sqrt(p^k)':>18}")
    for (pk, label) in [(2, '2'), (3, '3'), (4, '2^2'), (5, '5'), (7, '7'), (8, '2^3'), (9, '3^2')]:
        t0 = mp.log(pk)
        # one-sided slopes via finite differences that do NOT cross the kink
        sL = (psi_suzuki(t0 - eps, dps=40, events=evs) - psi_suzuki(t0 - 3 * eps, dps=40, events=evs)) / (2 * eps)
        sR = (psi_suzuki(t0 + 3 * eps, dps=40, events=evs) - psi_suzuki(t0 + eps, dps=40, events=evs)) / (2 * eps)
        jump = sR - sL
        # Lambda(p^k) = log p ; weight log p / p^{k/2}
        import sympy as sp
        fac = sp.factorint(pk)
        p = list(fac)[0]
        pred = -float(mp.log(p) / mp.sqrt(pk))
        print(f"   {label:>10} {float(t0):>12.5f} {float(jump):>24.5f} {pred:>18.5f}")
        assert abs(float(jump) - pred) < 5e-3
    # reserve stays positive (diagnostic)
    minPsi = min(float(psi_suzuki(mp.mpf(x) / 20, dps=35, events=evs)) for x in range(1, 70))
    print(f"   min Psi(t) over t in (0.05,3.5] = {minPsi:.5f}  (>0 => reserve never fires below 0: RH-consistent)")
    print("   Curvature Psi'' = smooth Archimedean  -  sum_{p^k} (Lambda/p^{k/2}) delta_{log p^k}  (= -g'', the Weil kernel).")

    banner("3. The light cone: on-line = NULL (PSD cos), off-line = TIMELIKE (indefinite cosh*cos)")
    print("   Finite Weil tangent Gram A(t,u)=sum e^{lambda(t-u)} on a grid. r,gamma FREELY CHOSEN")
    print("   (NOT zeta ordinates). on-line lambda=+-i gamma; off-line quartet lambda=r+-i gamma (r!=0).")
    tg = np.linspace(-2.0, 2.0, 24)
    TT = tg[:, None] - tg[None, :]
    gamma = 5.0
    # on-line pair: 2 cos(gamma (t-u))
    A_on = 2 * np.cos(gamma * TT)
    ev_on = np.linalg.eigvalsh(A_on)
    # off-line quartet: 4 cosh(r (t-u)) cos(gamma (t-u)),  r = boost rapidity (freely chosen)
    for r in [0.2, 0.5]:
        A_off = 4 * np.cosh(r * TT) * np.cos(gamma * TT)
        ev_off = np.linalg.eigvalsh(A_off)
        print(f"   off-line r={r}: eig range [{ev_off.min():+.3f}, {ev_off.max():+.3f}]  "
              f"=> {'INDEFINITE (timelike, off cone)' if ev_off.min() < -1e-6 else 'PSD?!'}")
        assert ev_off.min() < -1e-6
    print(f"   on-line  (r=0): eig range [{ev_on.min():+.3f}, {ev_on.max():+.3f}]  "
          f"=> {'PSD (null, ON the light cone)' if ev_on.min() > -1e-6 else 'indefinite?!'}")
    assert ev_on.min() > -1e-6
    print("   => RH <=> every zero is NULL (on the light cone, cos, PSD). Off-line = timelike boost")
    print("      (cosh rapidity r=beta-1/2) = a negative direction in the Weil form. (Lax-Phillips/Sierra.)")

    print("\nALL CHECKS PASSED.  Three faces of one RH-equivalent (reflection positivity / screw / light")
    print("cone). All standard (credit Suzuki 2023, Schoenberg-vN 1941, Weil, Connes, Lax-Phillips 1976,")
    print("Sierra 2014). 'Causality <=> RH' is a program, not a theorem. RH remains open. No zeta zeros used.")


if __name__ == "__main__":
    main()
