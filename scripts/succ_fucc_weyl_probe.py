#!/usr/bin/env python3
"""
SUCC/FUCC -> Weyl diagnostic suite.

Checks exact/local structures without using nontrivial zero locations:
  * p-adic depth Toeplitz Gram positivity;
  * local scalar/matrix Caratheodory positivity;
  * SU(1,1) transfer preservation under irregular phase sequences;
  * direct xi-log-derivative Pick matrices (diagnostic only);
  * Gamma trivial-ladder Blaschke divergence.

RH is not assumed or proved by this script.
"""

from __future__ import annotations

import cmath
import math

import mpmath as mp
import numpy as np


mp.mp.dps = 60


def prime_depth_gram(p: int, n: int) -> np.ndarray:
    r = p ** -0.5
    return np.array(
        [[r ** abs(j - k) for k in range(n)] for j in range(n)],
        dtype=float,
    )


def scalar_caratheodory(r: float, z: complex) -> complex:
    return (1 + r * z) / (1 - r * z)


def exact_conductor_phases(p: int, k: int) -> np.ndarray:
    q = p**k
    return np.array(
        [
            cmath.exp(2j * math.pi * a / q)
            for a in range(q)
            if math.gcd(a, p) == 1
        ],
        dtype=complex,
    )


def matrix_caratheodory(p: int, k: int, z: complex) -> np.ndarray:
    r = p ** -0.5
    phases = exact_conductor_phases(p, k)
    A = np.diag(r * phases)
    I = np.eye(len(phases), dtype=complex)
    return (I + z * A) @ np.linalg.inv(I - z * A)


def su11_matrix(alpha: complex) -> np.ndarray:
    rho = math.sqrt(1 - abs(alpha) ** 2)
    return np.array(
        [[1, alpha], [alpha.conjugate(), 1]],
        dtype=complex,
    ) / rho


def xi_log_derivative(s: complex) -> complex:
    """
    xi'/xi using the completed logarithmic-derivative formula.

    Avoid exact elementary pole/cancellation points such as s=0,1.
    """
    s = mp.mpc(s)
    return (
        1 / s
        + 1 / (s - 1)
        - mp.log(mp.pi) / 2
        + mp.digamma(s / 2) / 2
        + mp.diff(mp.zeta, s) / mp.zeta(s)
    )


def m_xi(z: complex) -> complex:
    """
    m_Xi(z) = -Xi'(z)/Xi(z), with Xi(z)=xi(1/2+i z).

    This direct formula uses xi'/xi, not a list of zeros.
    """
    z = mp.mpc(z)
    s = mp.mpf("0.5") + 1j * z
    return -1j * xi_log_derivative(s)


def pick_matrix(points: list[complex]) -> np.ndarray:
    n = len(points)
    K = np.empty((n, n), dtype=complex)
    vals = [m_xi(z) for z in points]
    for i, z in enumerate(points):
        for j, w in enumerate(points):
            num = vals[i] - mp.conj(vals[j])
            den = z - complex(w).conjugate()
            K[i, j] = complex(num / den)
    return (K + K.conj().T) / 2


def gamma_blaschke_partial(M: int) -> float:
    """
    Partial upper-half-plane Blaschke sum for z_m=i(2m+1/2).
    Diverges logarithmically.
    """
    total = 0.0
    for m in range(M):
        y = 2 * m + 0.5
        total += y / (1 + y * y)
    return total


def main() -> None:
    print("=== p-adic depth Gram positivity ===")
    for p in [2, 3, 5, 7, 11]:
        G = prime_depth_gram(p, 16)
        ev = np.linalg.eigvalsh(G)
        print(
            f"p={p:2d}  min_eig={ev.min():.12g}  "
            f"max_eig={ev.max():.12g}"
        )

    print("\n=== scalar Caratheodory positivity ===")
    test_z = [0.2 + 0.1j, -0.5 + 0.3j, 0.75j]
    for p in [2, 3, 5]:
        r = p ** -0.5
        vals = [scalar_caratheodory(r, z).real for z in test_z]
        print(f"p={p}: Re F = {vals}")

    print("\n=== matrix-valued conductor Weyl blocks ===")
    for p, k in [(2, 3), (3, 2), (5, 1)]:
        F = matrix_caratheodory(p, k, 0.31 + 0.22j)
        ReF = (F + F.conj().T) / 2
        ev = np.linalg.eigvalsh(ReF)
        print(
            f"p={p}, k={k}: dim={len(ev)}, "
            f"min eig Re F={ev.min():.12g}"
        )

    print("\n=== SU(1,1) irregular phase cocycle ===")
    J = np.diag([1.0, -1.0]).astype(complex)
    phases = [
        0.13,
        2.7,
        -1.2,
        math.pi / 7,
        4.1,
        -2.2,
    ]
    primes = [2, 3, 5, 7, 11, 13]
    U = np.eye(2, dtype=complex)
    for p, phi in zip(primes, phases):
        alpha = p ** -0.5 * cmath.exp(1j * phi)
        U = su11_matrix(alpha) @ U
    jerr = np.linalg.norm(U.conj().T @ J @ U - J)
    derr = abs(np.linalg.det(U) - 1)
    print(f"J-unitarity error={jerr:.3e}")
    print(f"determinant error={derr:.3e}")

    print("\n=== direct Xi-side Herglotz/Pick diagnostic ===")
    pts = [
        5 + 0.2j,
        10 + 0.5j,
        14 + 0.3j,
        20 + 0.7j,
        30 + 1.0j,
    ]
    for z in pts:
        mz = m_xi(z)
        print(
            f"z={z!s:>10}: "
            f"m={mp.nstr(mz, 15)}, "
            f"Im m={mp.nstr(mp.im(mz), 12)}"
        )
    K = pick_matrix(pts)
    ev = np.linalg.eigvalsh(K)
    print("Pick eigenvalues:", ev)
    print(
        "NOTE: finite positive samples are diagnostics only; "
        "they do not establish RH."
    )

    print("\n=== Gamma Blaschke obstruction ===")
    for M in [10, 100, 1000, 10000]:
        B = gamma_blaschke_partial(M)
        print(
            f"M={M:5d}: partial sum={B:.12f}, "
            f"ratio / log(M+1)={B/math.log(M+1):.12f}"
        )


if __name__ == "__main__":
    main()
