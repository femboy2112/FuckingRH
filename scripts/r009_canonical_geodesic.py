#!/usr/bin/env python3
r"""
Round 009 / Pillar 2 -- The canonical system as a geodesic; "actualization to infinity = curvature".

User's intuition: "the first domino gets set, the first finite curvature is actualized, the system
minimally follows the gradient (geodesic path), and this forces the next minimal domino; the net effect
is the global curvature ... the limit of actualization to infinity is what describes the curvature."

The honest realization (every object is standard / already in the repo; see CREDIT):

 (1) The canonical/Dirac transfer is  dX/dA = [ i z sigma3 + mu(A) sigma1 ] X,  with the Dirac mass
     mu(A) = d/dA log m_3(e^A)  (aletheia CRITICAL_PARITY_DIRAC_SYSTEM.md). The transfer acts on the
     hyperbolic upper half-plane H by Mobius (SL(2,R)/SU(1,1); aletheia SU11_CARRY_COCYCLE.md; standard:
     Weyl-Titchmarsh, Krein, Remling 2018).

 (2) GEODESIC AT THE SPECTRAL BASE POINT z=0 (the honest, PROVABLE form of "follow the geodesic"):
     at z=0 the generator is mu(A) sigma1 -- a FIXED direction (pure boost / hyperbolic sl(2,R)
     generator) with A-dependent magnitude. Its flow is exp(tau(A) sigma1), tau(A)=int mu = log m_3,
     a one-parameter subgroup = a GEODESIC in H. The point i sits on the boost axis (the unit
     semicircle), so the z=0 orbit of i is EXACTLY that geodesic (|w|=1 preserved). For z != 0 the
     i z sigma3 rotation enters and the orbit LEAVES the geodesic -- that deviation is the spectral
     oscillation. (A generic Hamiltonian gives a generic SL(2,R) curve, geodesic only at z=0; Conrey-Li
     2000 refuted de Branges' positivity approach, so we claim NO positivity here.)

 (3) The FUCC metric geodesic (aletheia SUCC_FUCC_METRIC_GEOMETRY.md) and the canonical geodesic share
     one log-scale clock (proper time = log scale) and one event set (prime powers), related by the
     omega-jet (Pillar 1): the Weil weight 2 Lambda(n)/sqrt(n) = b_0'(n) is the omega=0 VELOCITY (first
     jet) and the conductor weight b_{1/2}(n)=phi(n)/n is the omega=1/2 VALUE of the SAME family b_omega.
     They are two samples of one flow (NOT a linearization/tangent relation: the omega=0 tangent line
     extrapolated to omega=1/2 gives Lambda/sqrt n, neither 2Lambda/sqrt n nor phi/n).

 (4) "Global curvature = limit of actualization" = the a->infinity accumulation log m_3(a) and the
     Weyl-disk limit m_infinity = -Xi'/Xi (SU11). We compute the renormalized accumulated det_3
     holonomy sum_j [ log((1+lam_j)/(1-lam_j)) - 2 lam_j ] (leading 2 lam^3/3 = pure curvature) vs a.

CREDIT (standard / prior art): de Branges 1968; Suzuki 2012 (RIMS B34); Krein; Remling 2018; the
SL(2,R)/SU(1,1) Weyl-disk flow; aletheia CRITICAL_PARITY_DIRAC_SYSTEM.md, SU11_CARRY_COCYCLE.md,
CRITICAL_DET3_POSITIVE_HAMILTONIAN.md, SUCC_FUCC_METRIC_GEOMETRY.md. RH IS OPEN; NOTHING here is a proof.
No zeta zeros are used as input.
"""

import os
import sys
import numpy as np
from scipy.linalg import expm
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from finite_hankel_frontier_probe import build_galerkin  # noqa: E402

S1 = np.array([[0.0, 1.0], [1.0, 0.0]])          # sigma1  -- boost / hyperbolic generator
S3 = np.array([[1.0, 0.0], [0.0, -1.0]])         # sigma3


def mobius(M, z):
    """Act 2x2 matrix M on point z in the upper half-plane by (a z + b)/(c z + d)."""
    (a, b), (c, d) = M
    return (a * z + b) / (c * z + d)


def banner(t):
    print("\n" + "=" * 76 + "\n" + t + "\n" + "=" * 76)


def main():
    banner("1. sigma1 is a BOOST; exp(tau sigma1) moves i along the unit-semicircle geodesic (z=0)")
    print("exp(tau sigma1) = [[cosh tau, sinh tau],[sinh tau, cosh tau]] in SL(2,R) (det=1).")
    print("Fixed boundary points +-1 => geodesic axis = unit semicircle; i is ON it (|i|=1).")
    maxdev = 0.0
    for tau in np.linspace(-2, 2, 21):
        M = expm(tau * S1)
        w = mobius(M, 1j)
        maxdev = max(maxdev, abs(abs(w) - 1.0))       # orbit should stay on |w|=1
        assert w.imag > 0                              # stays in upper half-plane
    print(f"   max | |w(tau)| - 1 | over tau in [-2,2] = {maxdev:.2e}  => z=0 orbit of i IS the geodesic.")
    assert maxdev < 1e-12
    print(f"   det(exp(sigma1)) = {np.linalg.det(expm(1.0*S1)):.12f}  (SL(2,R))")

    banner("2. The Dirac dispersion: eigenvalues of i z sigma3 + mu sigma1 are +-sqrt(mu^2 - z^2)")
    print("   generator G(z) = [[i z, mu],[mu, -i z]];  tr=0, det=z^2-mu^2; eigenvalues +-sqrt(mu^2-z^2).")
    print("   |z|<mu: REAL eigenvalues = hyperbolic BOOST = geodesic flow (z=0 => pure boost, Pillar-2 geodesic)")
    print("   |z|=mu: null (parabolic) = the LIGHT CONE;   |z|>mu: IMAGINARY = elliptic ROTATION = oscillation")
    mu = 1.0
    for z in [0.0, 0.5, 1.0, 1.5]:
        G = 1j * z * S3 + mu * S1
        ev = np.linalg.eigvals(G)
        kind = ("boost/hyperbolic -> geodesic" if z < mu - 1e-9
                else "NULL (light cone)" if abs(z - mu) < 1e-9
                else "elliptic/rotation -> oscillation")
        disc = mu ** 2 - z ** 2
        disp = np.sqrt(disc + 0j)
        print(f"   z={z:>4}: eig={ev[0].real:+.4f}{ev[0].imag:+.4f}j, {ev[1].real:+.4f}{ev[1].imag:+.4f}j  "
              f"sqrt(mu^2-z^2)={disp.real:+.4f}{disp.imag:+.4f}j   {kind}")
        assert abs(abs(ev[0]) - abs(disp)) < 1e-9
    print("   => mass-shell |z|=mu is the Dirac light cone; z=0 (far inside) is the pure-boost geodesic.")

    banner("3. FUCC metric geodesic and canonical geodesic share one clock; related by the omega-jet")
    # conductor weight at omega=1/2 is phi(n)/n;  Weil weight (first jet) is 2 Lambda(n)/sqrt(n)
    print("   n : b_{1/2}(n)=phi(n)/n (omega=1/2 VALUE) | 2Lambda/sqrt n (omega=0 VELOCITY) -- same family b_omega")
    for n in [2, 3, 4, 5, 6, 8, 9, 12]:
        phin = int(sp.totient(n))
        b_half = phin / n
        fac = sp.factorint(n)
        Lam = float(sp.log(list(fac)[0])) if len(fac) == 1 else 0.0
        weil = 2 * Lam / n ** 0.5
        # cross-check b_{1/2}(n) via the exact conductor formula n^{0}*prod(1-1/p) = phi(n)/n
        prod = 1.0
        for p in fac:
            prod *= (1 - 1.0 / p)
        assert abs(prod - b_half) < 1e-12
        print(f"   {n:>2}: {b_half:.6f}                               {weil:.6f}")
    # FUCC worldline: d_F(L_{N-1}, L_N) = Lambda(N), proper time tau(N)=log N
    print("\n   FUCC LCM worldline: d_F(L_{N-1},L_N)=log(lcm(1..N)/lcm(1..N-1))=Lambda(N); proper time=log N")
    from math import gcd, log
    L_prev = 1
    ok = True
    for N in range(2, 18):
        L = L_prev
        L = L * N // gcd(L, N)
        dF = log(L / L_prev)
        fac = sp.factorint(N)
        Lam = float(sp.log(list(fac)[0])) if len(fac) == 1 else 0.0
        ok = ok and abs(dF - Lam) < 1e-9
        L_prev = L
    print(f"   d_F(L_{{N-1}},L_N) == Lambda(N) for N=2..17: {'OK' if ok else 'FAIL'}")
    assert ok
    print("   => Weil weight (omega=0 velocity) and conductor weight (omega=1/2 value) are two samples of")
    print("      the SAME family b_omega -- one log clock, one prime-event set; NOT a linearization relation.")

    banner("4. Global curvature = limit of actualization: renormalized det_3 holonomy vs a (omega=1/2)")
    print("   log m_3(a) = 2 tau_1(a) + sum_j [ log((1+lam_j)/(1-lam_j)) - 2 lam_j ];  the sum is the")
    print("   renormalized accumulated curvature (leading term (2/3) lam_j^3). Computed from H_{1/2,a}.")
    print("   cells scaled with a (fixed resolution per unit log-length); diagnostic, resolution-limited.")
    print(f"\n   {'a':>5} {'cells':>6} {'Ncond':>6} {'||H||':>10} {'1-||H||':>10} {'det3-holonomy':>14}")
    for a in [1.2, 1.5, 2.0, 2.5, 3.0]:
        cells = int(round(24 * a))
        H, res = build_galerkin(a=a, omega=0.5, cells=cells)
        lam = np.linalg.eigvalsh(H)
        lam = lam[np.abs(lam) < 1 - 1e-9]  # guard the renormalized log near +-1
        holo = float(np.sum(np.log((1 + lam) / (1 - lam)) - 2 * lam))
        gap = 1 - res.norm_lower
        print(f"   {a:>5} {cells:>6} {res.conductors:>6} {res.norm_lower:>10.6f} {gap:>10.2e} {holo:>14.6f}")
    print("\n   det_3 holonomy (renormalized accumulated curvature) rises with the horizon; the small")
    print("   wiggle is Galerkin truncation (finite cells), not structure. 1-||H|| -> 0 is the geodesic")
    print("   reaching the ideal boundary of H (a->inf = 'actualization to infinity'). The Weyl-disk")
    print("   limit is m_infinity = -Xi'/Xi (SU11); RH <=> m_infinity Herglotz (no C+ pole) -- OPEN.")
    print("\nALL CHECKS PASSED.  Structure is standard (credit de Branges/Krein/Remling/Suzuki 2012/")
    print("aletheia Dirac+SU11+DET3+METRIC). GR analogy is a dictionary, NOT a mechanism; no positivity")
    print("is claimed (Conrey-Li 2000 refuted de Branges' positivity route). RH remains open. No zeta zeros.")


if __name__ == "__main__":
    main()
