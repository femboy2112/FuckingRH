#!/usr/bin/env python3
"""
Zero-free/special-value diagnostics for NEGATIVE_SUCC_JET_DUALITY.md.

Verifies:
- negative-even slope formula for positive odd zeta values;
- negative-odd Bernoulli/value channel;
- Euler-Mascheroni constant in the Hadamard linear factor B;
- free Gamma-clock nonlinear SUCC spacing asymptotic.

No RH assumption.
"""

from __future__ import annotations
import mpmath as mp

mp.mp.dps = 60


def xi(s):
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def theta(t):
    # mpmath's siegeltheta uses the standard continuous Riemann-Siegel theta.
    return mp.siegeltheta(t)


def theta_succ(t):
    target = theta(t) + mp.pi
    # asymptotic step as initial guess
    step0 = 2 * mp.pi / mp.log(t / (2 * mp.pi))
    return mp.findroot(lambda u: theta(u) - target, (t + step0 * mp.mpf("0.8"), t + step0 * mp.mpf("1.2")))


def main():
    print("=== negative-even first-jet formula ===")
    for m in range(1, 7):
        lhs = mp.diff(mp.zeta, -2 * m)
        rhs = ((-1) ** m) * mp.factorial(2 * m) * mp.zeta(2 * m + 1) / (
            2 * mp.power(2 * mp.pi, 2 * m)
        )
        print(
            f"m={m}: zeta'(-{2*m})={mp.nstr(lhs, 18)}  "
            f"formula error={mp.nstr(lhs-rhs, 5)}"
        )

    print("\n=== negative-odd value/Bernoulli channel ===")
    for m in range(1, 7):
        s = 1 - 2 * m
        lhs = mp.zeta(s)
        # Bernoulli number via mpmath.bernoulli
        rhs = -mp.bernoulli(2 * m) / (2 * m)
        print(
            f"s={s:3d}: zeta(s)={mp.nstr(lhs, 18)}  "
            f"Bernoulli error={mp.nstr(lhs-rhs, 5)}"
        )

    print("\n=== Euler-Mascheroni in the residual Hadamard normalization ===")
    B_num = mp.diff(lambda x: mp.log(xi(x)), 0)
    B_formula = mp.log(2) + mp.log(mp.pi) / 2 - 1 - mp.euler / 2
    print("xi'(0)/xi(0) =", mp.nstr(B_num, 30))
    print("formula        =", mp.nstr(B_formula, 30))
    print("error          =", mp.nstr(B_num - B_formula, 8))

    print("\n=== free Gamma-clock SUCC ===")
    for t in [100, 1000, 10000]:
        t = mp.mpf(t)
        u = theta_succ(t)
        delta = u - t
        asym = 2 * mp.pi / mp.log(t / (2 * mp.pi))
        print(
            f"t={mp.nstr(t,8)}: exact clock step={mp.nstr(delta,14)}, "
            f"2pi/log(t/2pi)={mp.nstr(asym,14)}, ratio={mp.nstr(delta/asym,10)}"
        )


if __name__ == "__main__":
    main()
