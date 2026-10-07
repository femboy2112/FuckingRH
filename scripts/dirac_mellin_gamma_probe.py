#!/usr/bin/env python3
"""
Controls for DIRAC_MELLIN_GAMMA_LOCALIZATION.md.

Checks:
  1. multiplicative Dirac comb -> Euler factor;
  2. Gaussian Mellin measure -> Gamma_R(s);
  3. normalized critical Gamma_R -> characteristic function of log-scale law;
  4. incomplete-Gamma log-cutoff derivative -> one local Mellin character;
  5. digamma resolvent comb truncation convergence.

No zeta-zero data are used.
"""

import mpmath as mp
mp.mp.dps = 60


def gamma_R(s):
    return mp.power(mp.pi, -s/2) * mp.gamma(s/2)


def check_euler_comb():
    print("=== Euler factor from multiplicative Dirac comb ===")
    p = 3
    s = mp.mpc("1.7", "0.4")
    exact = 1/(1-mp.power(p, -s))
    for K in [4, 12, 40]:
        approx = mp.fsum(mp.power(p, -k*s) for k in range(K+1))
        if K == 40:
            print("p=3 K=40 error:", mp.nstr(abs(approx-exact), 10))
            assert abs(approx-exact) < mp.mpf("1e-18")


def check_gamma_mellin():
    print("\n=== Gamma_R from continuous scale measure ===")
    s = mp.mpc("0.7", "1.2")
    integ = 2 * mp.quad(lambda t: mp.e**(-mp.pi*t*t) * mp.power(t, s) / t,
                        [0, 1, mp.inf])
    exact = gamma_R(s)
    err = abs(integ-exact)
    print("error:", mp.nstr(err, 10))
    assert err < mp.mpf("1e-40")


def critical_density(x):
    norm = gamma_R(mp.mpf("0.5"))
    return 2 * mp.e**(x/2) * mp.e**(-mp.pi * mp.e**(2*x)) / norm


def check_characteristic_function():
    print("\n=== critical Gamma_R as log-scale characteristic function ===")
    for t in [mp.mpf("0.5"), mp.mpf("3.0"), mp.mpf("10.0")]:
        phi = mp.quad(lambda x: mp.e**(1j*t*x)*critical_density(x),
                      [-mp.inf, 0, mp.inf])
        exact = gamma_R(mp.mpf("0.5")+1j*t)/gamma_R(mp.mpf("0.5"))
        err = abs(phi-exact)
        print("t=", t, "error=", mp.nstr(err, 10))
        assert err < mp.mpf("1e-35")


def gamma_R_lower(s, X):
    upper = mp.pi * mp.e**(2*X)
    return mp.power(mp.pi, -s/2) * mp.gammainc(s/2, 0, upper)


def check_incomplete_derivative():
    print("\n=== incomplete-Gamma cutoff derivative ===")
    s = mp.mpc("0.8", "1.1")
    for X in [mp.mpf("-0.7"), mp.mpf("0.0"), mp.mpf("0.8")]:
        deriv = mp.diff(lambda xx: gamma_R_lower(s, xx), X)
        local = 2 * mp.e**(-mp.pi * mp.e**(2*X)) * mp.e**(s*X)
        err = abs(deriv-local)
        print("X=", X, "error=", mp.nstr(err, 10))
        assert err < mp.mpf("1e-40")


def check_digamma_resolvent():
    print("\n=== digamma as regularized spectral delta comb ===")
    z = mp.mpc("0.7", "0.8")
    exact = mp.digamma(z)
    for M in [100, 1000, 10000]:
        approx = -mp.euler + mp.fsum(
            (1/mp.mpf(m+1) - 1/(m+z)) for m in range(M+1)
        )
        # tail is O(1/M), so just report/check at final cutoff.
        if M == 10000:
            err = abs(approx-exact)
            print("M=10000 error:", mp.nstr(err, 10))
            assert err < mp.mpf("0.0002")


def main():
    check_euler_comb()
    check_gamma_mellin()
    check_characteristic_function()
    check_incomplete_derivative()
    check_digamma_resolvent()
    print("\nALL DIRAC/MELLIN/GAMMA CONTROLS PASSED.")


if __name__ == "__main__":
    main()
