#!/usr/bin/env python3
"""
Diagnostics for the trivial-zero / inverse-SUCC / completed-causal-history coupling.

No RH assumption. Zero locations are not used to build any operator or transfer
function. Optional diagnostic evaluations near known/trivial zeros merely verify
classical residue cancellation.

Requires: mpmath, sympy
"""

from __future__ import annotations

import mpmath as mp
import sympy as sp

mp.mp.dps = 50


def xi(s):
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def minus_xi_log_derivative(s):
    return (
        -1 / s
        - 1 / (s - 1)
        + mp.mpf("0.5") * mp.log(mp.pi)
        - mp.mpf("0.5") * mp.digamma(s / 2)
        - mp.diff(mp.zeta, s) / mp.zeta(s)
    )


def det_hinf_plus(s):
    """zeta-regularized det(H_inf+s), H_inf spectrum 0,2,4,..."""
    return mp.power(2, 1 - s / 2) * mp.sqrt(mp.pi) / mp.gamma(s / 2)


def chi(s):
    """Functional-equation factor zeta(s)=chi(s) zeta(1-s)."""
    return (
        mp.power(mp.pi, s - mp.mpf("0.5"))
        * mp.gamma((1 - s) / 2)
        / mp.gamma(s / 2)
    )


def prime_power_dirichlet(s, cutoff=500_000):
    """Truncated -zeta'/zeta Dirichlet series over p^k <= cutoff."""
    total = mp.mpf("0")
    for p in sp.primerange(2, cutoff + 1):
        lp = mp.log(p)
        pk = p
        while pk <= cutoff:
            total += lp * mp.power(pk, -s)
            pk *= p
    return total


def causal_continuous_diff(s, s0):
    """
    Integral of (e^-st-e^-s0t)[Tr exp(-tH_inf)-1-e^t] dt.
    The basepoint subtraction removes the t=0 regularization singularity.
    """
    def integrand(t):
        density = 1 / (1 - mp.e ** (-2 * t)) - 1 - mp.e**t
        return (mp.e ** (-s * t) - mp.e ** (-s0 * t)) * density

    return mp.quad(integrand, [0, mp.mpf("0.1"), 1, mp.inf])


def check_determinant_formula():
    print("=== zeta-regularized determinant / Gamma ===")
    for s in [mp.mpf("0.7"), mp.mpf("2.3"), mp.mpf("3.1")]:
        lhs = det_hinf_plus(s)
        rhs = mp.power(2, 1 - s / 2) * mp.sqrt(mp.pi) / mp.gamma(s / 2)
        print(f"s={s}: |lhs-rhs|={mp.nstr(abs(lhs-rhs), 6)}")


def check_scattering():
    print("\n=== Archimedean scattering determinant ratio ===")
    for t in [mp.mpf("0.3"), mp.mpf("2"), mp.mpf("10")]:
        lhs = chi(mp.mpf("0.5") + 1j * t)
        rhs = (
            mp.power(2 * mp.pi, 1j * t)
            * det_hinf_plus(mp.mpf("0.5") + 1j * t)
            / det_hinf_plus(mp.mpf("0.5") - 1j * t)
        )
        print(
            f"t={t}: |chi-ratio|={mp.nstr(abs(lhs-rhs), 6)}, "
            f"|chi|={mp.nstr(abs(lhs), 10)}"
        )


def check_trivial_residue_cancellation():
    print("\n=== trivial-zero residue cancellation ===")
    eps = mp.mpf("1e-8")
    for m in [1, 2, 3, 5]:
        s = -2 * m + eps
        zeta_piece = eps * (mp.diff(mp.zeta, s) / mp.zeta(s))
        gamma_piece = eps * (mp.mpf("0.5") * mp.digamma(s / 2))
        print(
            f"m={m}: eps*zeta'/zeta={mp.nstr(zeta_piece, 14)}, "
            f"eps*(1/2 psi)={mp.nstr(gamma_piece, 14)}, "
            f"sum={mp.nstr(zeta_piece+gamma_piece, 8)}"
        )


def check_completed_causal_transfer():
    print("\n=== completed causal-history transfer ===")
    s0 = mp.mpf("3")
    cutoff = 500_000

    for s in [mp.mpf("2"), mp.mpf("2.5")]:
        prime_diff = (
            prime_power_dirichlet(s, cutoff)
            - prime_power_dirichlet(s0, cutoff)
        )
        continuous_diff = causal_continuous_diff(s, s0)
        approx = prime_diff + continuous_diff
        exact = minus_xi_log_derivative(s) - minus_xi_log_derivative(s0)
        print(
            f"s={s}: truncated causal={mp.nstr(approx, 16)}, "
            f"exact={mp.nstr(exact, 16)}, "
            f"error={mp.nstr(approx-exact, 8)}"
        )


def check_trivial_locations_in_t_plane():
    print("\n=== critical-centered trivial ladder ===")
    for m in range(5):
        t = 1j * (2 * m + mp.mpf("0.5"))
        s = mp.mpf("0.5") + 1j * t
        print(f"m={m}: t={t}, s={s}")


def main():
    check_determinant_formula()
    check_scattering()
    check_trivial_residue_cancellation()
    check_completed_causal_transfer()
    check_trivial_locations_in_t_plane()


if __name__ == "__main__":
    main()
