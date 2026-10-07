#!/usr/bin/env python3
"""Reproduction gates for inherited RH critiques and source normalization.

Provenance: research/audits/2026-10-07/CUBE_ATOM_CRITICAL_AUDIT_IMPORTED.md
and research/audits/2026-10-07/RH_CLAIM_PROVENANCE_LEDGER.md.

Standard library only. These are finite exact or calibrated counterexamples,
NOT numerical evidence for RH. Run: python scripts/rh_critical_provenance_controls.py
"""
from fractions import Fraction
from math import cos, cosh, gamma, gcd, isclose, log, pi, sqrt


def test_nonprojective_conductor_weights():
    l2 = {1: Fraction(1, 2), 2: Fraction(1, 2)}
    l4 = {1: Fraction(1, 4), 2: Fraction(1, 4), 4: Fraction(1, 2)}
    pushed = {1: Fraction(0), 2: Fraction(0)}
    for d, weight in l4.items():
        pushed[gcd(d, 2)] += weight
    assert pushed != l2, (l2, pushed)
    assert pushed == {1: Fraction(1, 4), 2: Fraction(3, 4)}


def test_coherent_rotation_is_not_markov():
    c = s = 1 / sqrt(2)
    R = ((c, -s), (s, c))
    R2 = tuple(
        tuple(sum(R[i][k] * R[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )
    assert isclose(R2[1][0]**2, 1, abs_tol=1e-14)
    # Independent fresh-ancilla Markov births require probability 1/2,
    # not a deterministic 90-degree coherent second rotation.
    assert not isclose(R2[1][0]**2, 1/2, abs_tol=1e-14)


def test_mellin_multiplier_is_modified():
    # g(x)=e^{-x}; M[g](s)=Gamma(s), M[(1-x)g](s)=Gamma(s)-Gamma(s+1)
    s = 1.5
    assert isclose(gamma(s) - gamma(s + 1), -gamma(s)/2, rel_tol=1e-13)
    assert not isclose(gamma(s), gamma(s) - gamma(s + 1), rel_tol=1e-13)


def test_unimodularity_does_not_imply_hardy_innerness():
    # Inverse Blaschke function has |B(t)|=1 on R and a pole at z=i*a.
    a = 1.2
    for t in (-10, -1, 0, 1, 10):
        value = (t + 1j*a)/(t - 1j*a)
        assert isclose(abs(value), 1., abs_tol=1e-13)
    near_pole = 1j*a*(1+1e-6)
    assert abs((near_pole+1j*a)/(near_pole-1j*a)) > 1e5


def test_fake_zero_pair_beats_scalar_hodge_norm():
    # Xi_fake has quartet +/-1/4 +/- 2*pi*i.
    # Its two-point Weil tangent is [[4,4cosh(1/4)],[4cosh(1/4),4]]
    negative_eigenvalue = 4 * (1 - cosh(1/4))
    q6_hodge = log(6)**2 + log(2)**2 + log(3)**2
    assert negative_eigenvalue < 0 < q6_hodge


def test_true_first_jet_support():
    # b_omega(n)=n^(omega-1/2) prod_{p|n}(1-p^(-2 omega)).
    # Its half-derivative at zero is Lambda(n)/sqrt(n).
    eps = 1e-6
    for n, primes, target in [
        (8, [2], log(2)/sqrt(8)),
        (6, [2, 3], 0.),
        (12, [2, 3], 0.),
    ]:
        b = n**(eps-0.5)
        for p in primes:
            b *= 1-p**(-2*eps)
        assert abs(b/(2*eps)-target) < 1e-5


def main():
    tests = [
        test_nonprojective_conductor_weights,
        test_coherent_rotation_is_not_markov,
        test_mellin_multiplier_is_modified,
        test_unimodularity_does_not_imply_hardy_innerness,
        test_fake_zero_pair_beats_scalar_hodge_norm,
        test_true_first_jet_support,
    ]
    for fn in tests:
        fn()
        print("PASS",fn.__name__)
    print("All 6 finite provenance controls passed. RH remains OPEN.")


if __name__ == "__main__":
    main()
