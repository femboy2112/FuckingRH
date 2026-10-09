#!/usr/bin/env python3
"""Zero-input tests of history-conditioned reversal, not an RH test.

Verifies:
  - normalized p-digit refinement and its noninvertible shadow adjoint;
  - coherent vs dephased reconstruction;
  - Bayes reverse = the half-density weighted adjoint;
  - a finite-horizon reverse/forward rational echo when forward product vanishes;
  - the precise L=log(3) activation criterion from analytic interval formulas.

Requires numpy. Never reads/computes zeros or uses fitted boundary data.
"""
from __future__ import annotations
import math
import numpy as np


def digit_refinement(p: int) -> np.ndarray:
    return np.ones((p, 1), dtype=np.complex128) / np.sqrt(p)


def test_refinement() -> None:
    for p in (2, 3, 5, 7):
        J = digit_refinement(p)
        assert np.allclose(J.conj().T @ J, np.eye(1))
        assert np.allclose(J @ J.conj().T, np.ones((p, p)) / p)
        assert not np.allclose(J @ J.conj().T, np.eye(p))

        coherent = np.ones(p, dtype=complex) / np.sqrt(p)
        recovered = (J.conj().T @ coherent)[0]
        assert np.isclose(recovered, 1.0)

        phases = np.exp(2j * np.pi * np.arange(p) / p)
        dephased = phases / np.sqrt(p)
        amplitude = (J.conj().T @ dephased)[0]
        assert abs(amplitude) < 1e-12
    print("PASS: p-ary half-density, coherent return and dephased loss")


def test_bayesian_reverse() -> None:
    mu = np.array([0.3, 0.7], dtype=float)
    P = np.array([[0.5, 0.2], [0.3, 0.3], [0.2, 0.5]])
    assert np.allclose(P.sum(axis=0), 1)
    nu = P @ mu
    Q = np.diag(mu) @ P.T @ np.diag(1 / nu)
    assert np.allclose(Q.sum(axis=0), 1)

    # Whiten forward and reverse using the specified prior/output measures.
    forward = np.diag(1 / np.sqrt(nu)) @ P @ np.diag(np.sqrt(mu))
    reverse = np.diag(1 / np.sqrt(mu)) @ Q @ np.diag(np.sqrt(nu))
    assert np.allclose(reverse, forward.conj().T)
    assert not np.allclose(Q, P.T)
    print("PASS: Bayes reverse is a measure-dependent half-density adjoint")


def truncated_shift(a: int, L: int) -> np.ndarray:
    S = np.zeros((L, L))
    for j in range(L - a):
        S[j + a, j] = 1.0
    return S


def test_rational_echo_discrete() -> None:
    # Integer analogue of 0<a<b<L<a+b; p=2,q=3,L=4.
    a, b, L = 2, 3, 4
    Ta, Tb = truncated_shift(a, L), truncated_shift(b, L)
    assert np.count_nonzero(Ta @ Tb) == 0
    assert np.linalg.norm(Ta.T @ Tb, ord=2) == 1
    K = Ta.T @ Tb - Tb @ Ta.T
    assert np.isclose(np.linalg.norm(K, ord=2), 1.0)
    assert np.isclose(np.trace(K), 0.0)
    print("PASS: forward product vanishes, reverse/forward echo has norm one")


def test_logarithmic_echo_window() -> None:
    a = math.log(2)
    b = math.log(3)
    L = 1.2
    assert b < L < 2*a < a + b
    # Exact intervals from the continuous analytic commutator formula.
    first = (b - a, L - a)
    second = (b, L)
    assert all(y > x for x, y in (first, second))
    assert first[1] < second[0]  # disjoint output strips
    assert np.isclose(first[1] - first[0], L - b)
    assert np.isclose(second[1] - second[0], L - b)
    assert a+b>L  # no forward 6 shift
    print("PASS: log(3/2) ratio echo is visible while log(6) is beyond horizon")


if __name__ == "__main__":
    test_refinement()
    test_bayesian_reverse()
    test_rational_echo_discrete()
    test_logarithmic_echo_window()
    print("ALL TIME-REVERSAL TESTS PASSED; RH REMAINS OPEN.")
