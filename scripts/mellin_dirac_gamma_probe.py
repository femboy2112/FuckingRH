#!/usr/bin/env python3
"""Mellin/Dirac/Gamma finiteization probes for the RH program.

No zeta-zero data. Nothing here proves RH.

Verifies:
  * the critical Archimedean Gamma ratio is a characteristic function;
  * its phase quotient is exactly the critical-line Archimedean scattering factor;
  * its higher cumulants are spectral traces of the inverse-SUCC Gamma ladder;
  * the shifted Weierstrass/det_2 truncation converges and stays nonzero on R;
  * generalized Gauss-Laguerre gives a positive finite Dirac-comb Mellin model
    matching ordinary Gamma moments through degree 2N-1 exactly;
  * a log-Gamma Gaussian quadrature matches spectral/Taylor jets through
    degree 2N-1 exactly on finite order.
"""
from __future__ import annotations

import mpmath as mp

mp.mp.dps = 80

A = mp.mpf(1) / 4
LOG_PI = mp.log(mp.pi)
DRIFT = (mp.digamma(A) - LOG_PI) / 2


def lam(m: int) -> mp.mpf:
    """Critical inverse-SUCC Gamma ladder: 1/2, 5/2, 9/2, ..."""
    return 2 * m + mp.mpf("0.5")


def phi_exact(t):
    """Normalized critical Archimedean carrier characteristic function."""
    t = mp.mpf(t)
    return mp.power(mp.pi, -0.5j * t) * mp.gamma(A + 0.5j * t) / mp.gamma(A)


def chi_exact(t):
    """Critical-line Archimedean scattering factor chi(1/2+it)."""
    t = mp.mpf(t)
    return mp.power(mp.pi, 1j * t) * mp.gamma(A - 0.5j * t) / mp.gamma(A + 0.5j * t)


def phi_modes(t, M: int):
    """M-mode centered-exponential / det_2 truncation."""
    z = 1j * mp.mpf(t)
    out = mp.e ** (DRIFT * z)
    for m in range(M):
        l = lam(m)
        out *= mp.e ** (z / l) / (1 + z / l)
    return out


def chi_modes(t, M: int):
    p = phi_modes(t, M)
    return mp.conj(p) / p


def cumulant_exact(n: int):
    if n == 1:
        return DRIFT
    return mp.polygamma(n - 1, A) / (2 ** n)


def cumulant_modes(n: int, M: int):
    if n == 1:
        return DRIFT
    return ((-1) ** n) * mp.factorial(n - 1) * mp.fsum(
        [lam(m) ** (-n) for m in range(M)]
    )


def cumulant_tail_bound(n: int, M: int):
    """Integral-test bound for n>=2."""
    if n < 2:
        raise ValueError("n must be >=2")
    # sum_{m>=M} (2m+1/2)^-n <= first term + integral_M^inf
    first = lam(M) ** (-n)
    integ = lam(M) ** (1 - n) / (2 * (n - 1))
    return mp.factorial(n - 1) * (first + integ)


def verify_phase_identity():
    for t in [mp.mpf("0.1"), 1, 3, 10, 25]:
        p = phi_exact(t)
        assert abs(mp.conj(p) / p - chi_exact(t)) < mp.mpf("1e-60")
        assert abs(abs(chi_exact(t)) - 1) < mp.mpf("1e-60")


def verify_cumulant_trace_identity():
    for n in range(2, 9):
        spectral = ((-1) ** n) * mp.factorial(n - 1) * mp.nsum(
            lambda k: lam(k) ** (-n), [0, mp.inf]
        )
        assert abs(spectral - cumulant_exact(n)) < mp.mpf("1e-60")

        for M in [2, 4, 8, 16]:
            err = abs(cumulant_exact(n) - cumulant_modes(n, M))
            assert err <= cumulant_tail_bound(n, M)


def verify_mode_convergence():
    ts = [mp.mpf("0.1"), mp.mpf("0.5"), 1, 2, 5]
    previous = None
    for M in [2, 4, 8, 16, 32, 64]:
        err = max(abs(phi_modes(t, M) - phi_exact(t)) for t in ts)
        if previous is not None:
            assert err < previous
        previous = err

        # finite product has no real-axis zeros and phase quotient is unitary
        for t in ts:
            assert abs(phi_modes(t, M)) > 0
            assert abs(abs(chi_modes(t, M)) - 1) < mp.mpf("1e-60")


def verify_gauss_laguerre_atoms(N: int = 6):
    """Positive Dirac comb for x^{-3/4} e^{-x} dx.

    Matches Gamma(k+1/4) for k=0,...,2N-1 exactly (up to precision).
    """
    X, W = mp.gauss_quadrature(N, "glaguerre", alpha=A - 1)
    for k in range(2 * N):
        approx = mp.fsum([W[j] * X[j] ** k for j in range(N)])
        exact = mp.gamma(A + k)
        assert abs(approx - exact) < mp.mpf("1e-65")
    assert all(w > 0 for w in W)
    assert abs(mp.fsum(W) - mp.gamma(A)) < mp.mpf("1e-65")
    return X, W


def loggamma_cumulants(maxn: int):
    ks = [mp.mpf("0")] * (maxn + 1)
    ks[1] = DRIFT
    for n in range(2, maxn + 1):
        ks[n] = cumulant_exact(n)
    return ks


def moments_from_cumulants(ks, maxn: int):
    moments = [mp.mpf("0")] * (maxn + 1)
    moments[0] = mp.mpf(1)
    for n in range(1, maxn + 1):
        moments[n] = mp.fsum(
            [
                mp.binomial(n - 1, k - 1) * ks[k] * moments[n - k]
                for k in range(1, n + 1)
            ]
        )
    return moments


def loggamma_jet_quadrature(N: int = 5):
    """N-atom quadrature for Y=(log X-log pi)/2, X~Gamma(1/4,1).

    The nodes/weights are reconstructed from the Hankel moment problem.
    It exactly matches Y^k moments through k=2N-1.
    """
    moments = moments_from_cumulants(loggamma_cumulants(2 * N), 2 * N)

    H0 = mp.matrix(N)
    H1 = mp.matrix(N)
    for i in range(N):
        for j in range(N):
            H0[i, j] = moments[i + j]
            H1[i, j] = moments[i + j + 1]

    L = mp.cholesky(H0)
    Linv = L ** -1
    J = Linv * H1 * Linv.T
    evals, _ = mp.eigsy(J)
    nodes = [evals[i] for i in range(N)]

    V = mp.matrix(N)
    rhs = mp.matrix(N, 1)
    for k in range(N):
        rhs[k] = moments[k]
        for j in range(N):
            V[k, j] = nodes[j] ** k
    weights_vec = mp.lu_solve(V, rhs)
    weights = [weights_vec[j] for j in range(N)]

    assert all(w > 0 for w in weights)
    assert abs(mp.fsum(weights) - 1) < mp.mpf("1e-60")

    for k in range(2 * N):
        approx = mp.fsum([weights[j] * nodes[j] ** k for j in range(N)])
        assert abs(approx - moments[k]) < mp.mpf("1e-55")

    return nodes, weights



def gamma_source_integral(sigma, t):
    """Continuous Archimedean source in common log-scale coordinates."""
    sigma = mp.mpf(sigma)
    t = mp.mpf(t)

    def integrand(r):
        return (
            mp.expm1(-1j * t * r)
            * mp.e ** (-sigma * r)
            / (-mp.expm1(-2 * r))
        )

    return mp.quad(integrand, [0, 1, mp.inf])


def gamma_source_exact(sigma, t):
    a = mp.mpf(sigma) / 2
    return -mp.mpf("0.5") * (mp.digamma(a + 0.5j * t) - mp.digamma(a))


def primes_up_to(N):
    out = []
    for n in range(2, N + 1):
        ok = True
        d = 2
        while d * d <= n:
            if n % d == 0:
                ok = False
                break
            d += 1
        if ok:
            out.append(n)
    return out


def prime_source_finite(P, sigma, t):
    """Finite-prime Dirac source: sum_{p<=P,k>=1} log p p^-ksigma (e^-it klogp-1)."""
    sigma = mp.mpf(sigma)
    t = mp.mpf(t)
    total = 0j
    for p in primes_up_to(P):
        lp = mp.log(p)
        rs = mp.power(p, -sigma)
        rt = mp.power(p, -(sigma + 1j * t))
        total += lp * (rt / (1 - rt) - rs / (1 - rs))
    return total


def finite_euler_ratio(P, sigma, t):
    sigma = mp.mpf(sigma)
    t = mp.mpf(t)
    z = 1 + 0j
    for p in primes_up_to(P):
        z *= (1 - mp.power(p, -sigma)) / (1 - mp.power(p, -(sigma + 1j * t)))
    return z


def verify_common_source_kernel():
    # Gamma source identity, including the critical sigma=1/2 line.
    for sigma in [mp.mpf("0.5"), mp.mpf("1.25"), 2]:
        for t in [mp.mpf("0.2"), 1, 2]:
            lhs = gamma_source_integral(sigma, t)
            rhs = gamma_source_exact(sigma, t)
            assert abs(lhs - rhs) < mp.mpf("1e-35")

    # Finite Euler product: analytic derivative equals the discrete Dirac-source sum.
    for P in [7, 19, 43]:
        for sigma in [mp.mpf("1.25"), 2]:
            for t in [mp.mpf("0.3"), 1]:
                h = mp.mpf("1e-20")
                deriv = -(
                    mp.log(finite_euler_ratio(P, sigma + h, t))
                    - mp.log(finite_euler_ratio(P, sigma - h, t))
                ) / (2 * h)
                source = prime_source_finite(P, sigma, t)
                assert abs(deriv - source) < mp.mpf("1e-25")

def report():
    print("Critical Archimedean carrier:")
    print("  phi(t)=pi^{-it/2} Gamma(1/4+it/2)/Gamma(1/4)")
    print(f"  exact mean/drift = {mp.nstr(DRIFT, 18)}")
    print()

    print("First cumulants (spectral traces of lambda_m=2m+1/2):")
    for n in range(1, 7):
        print(f"  kappa_{n} = {mp.nstr(cumulant_exact(n), 18)}")
    print()

    print("Mode-truncation errors max over t={0.1,0.5,1,2,5}:")
    ts = [mp.mpf("0.1"), mp.mpf("0.5"), 1, 2, 5]
    for M in [2, 4, 8, 16, 32, 64]:
        err = max(abs(phi_modes(t, M) - phi_exact(t)) for t in ts)
        print(f"  M={M:2d}: {mp.nstr(err, 10)}")
    print()

    X, W = verify_gauss_laguerre_atoms(6)
    print("6-node generalized Gauss-Laguerre Dirac comb:")
    for x, w in zip(X, W):
        print(f"  x={mp.nstr(x, 12)}  w={mp.nstr(w, 12)}")
    print("  Matches Gamma(k+1/4), k=0..11.")
    print()

    nodes, weights = loggamma_jet_quadrature(5)
    print("5-node log-Gamma jet-matched Dirac comb:")
    for x, w in zip(nodes, weights):
        print(f"  y={mp.nstr(x, 12)}  weight={mp.nstr(w, 12)}")
    print("  Matches spectral derivatives/moments through order 9.")


def main():
    verify_phase_identity()
    verify_cumulant_trace_identity()
    verify_mode_convergence()
    verify_gauss_laguerre_atoms()
    loggamma_jet_quadrature()
    verify_common_source_kernel()
    report()
    print()
    print("Verified common probe kernel for continuous Gamma and discrete prime sources.")\n    print("All Mellin/Dirac/Gamma controls passed.")


if __name__ == "__main__":
    main()
