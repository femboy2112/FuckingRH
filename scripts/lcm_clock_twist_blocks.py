#!/usr/bin/env python3
"""
Exact/numerical checks for:
- LCM prime-power refinement as rank-one boundary twists;
- Ramanujan exact-conductor projectors;
- cyclotomic determinant blocks;
- telescoping local Euler factors.

No zeta zeros used.
"""

from __future__ import annotations
import math
import cmath
import numpy as np
import sympy as sp


def cyclic_shift(n: int) -> np.ndarray:
    U = np.zeros((n, n), dtype=complex)
    for j in range(n):
        U[(j + 1) % n, j] = 1.0
    return U


def dft(n: int) -> np.ndarray:
    w = cmath.exp(2j * math.pi / n)
    return np.array([[w ** (a * b) / math.sqrt(n) for b in range(n)] for a in range(n)], dtype=complex)


def boundary_twist(L: int, omega: complex) -> np.ndarray:
    U = cyclic_shift(L)
    U[0, L - 1] = omega
    return U


def check_global_refinement(L: int, p: int) -> None:
    U_big = cyclic_shift(p * L)

    # D maps n=a+bL to (a,b).
    # Matrix in tensor basis |a>⊗|b>, flattened as a*p+b.
    D = np.zeros((p * L, p * L), dtype=complex)
    for n in range(p * L):
        a = n % L
        b = n // L
        D[a * p + b, n] = 1.0

    U_tens = D @ U_big @ D.conj().T

    C_L = cyclic_shift(L)
    C_p = cyclic_shift(p)
    e = np.zeros((L, L), dtype=complex)
    e[0, L - 1] = 1.0
    rhs = np.kron(C_L, np.eye(p)) + np.kron(e, C_p - np.eye(p))

    print(f"refinement L={L}, p={p}: ||exact-rhs||={np.linalg.norm(U_tens-rhs):.3e}")

    # Fourier-transform new p digit only.
    Fp = dft(p)
    UF = np.kron(np.eye(L), Fp) @ U_tens @ np.kron(np.eye(L), Fp.conj().T)

    # F convention may give omega^{-r}; compare as an unordered family via spectra/block norms.
    off_block = 0.0
    for a in range(p):
        for b in range(p):
            if a != b:
                block = UF[a::p, b::p]
                off_block = max(off_block, np.linalg.norm(block))
    print(f"  max off-sector block norm={off_block:.3e}")

    det_err = 0.0
    z = 1.37 + 0.22j
    lhs = np.linalg.det(z * np.eye(p * L) - U_big)
    rhsdet = z ** (p * L) - 1
    det_err = abs(lhs - rhsdet)
    print(f"  det global error={det_err:.3e}")


def ramanujan_sum(q: int, n: int) -> complex:
    return sum(
        cmath.exp(2j * math.pi * a * n / q)
        for a in range(q)
        if math.gcd(a, q) == 1
    )


def check_ramanujan_projector(p: int, k: int) -> None:
    q = p ** k
    P = np.zeros((q, q), dtype=complex)
    for m in range(q):
        for n in range(q):
            P[m, n] = ramanujan_sum(q, m - n) / q

    phi = int(sp.totient(q))
    print(
        f"Ramanujan p={p}, k={k}: "
        f"||P^2-P||={np.linalg.norm(P@P-P):.3e}, "
        f"trace={P.trace().real:.8f}, phi={phi}"
    )

    U = cyclic_shift(q)
    # Restriction eigenvalues are primitive roots; compare their product polynomial numerically.
    primitive_eigs = [
        cmath.exp(2j * math.pi * a / q)
        for a in range(q)
        if math.gcd(a, q) == 1
    ]
    x = 0.31
    det_detail = np.prod([1 - x * lam for lam in primitive_eigs])
    cyclo = complex(sp.N(sp.cyclotomic_poly(q, sp.Symbol("x")).subs({"x": x}), 30))
    print(f"  |detail det - Phi_q(x)|={abs(det_detail-cyclo):.3e}")


def check_euler_telescope(p: int, s: float, K: int) -> None:
    x = p ** (-s)
    prod = 1.0
    for k in range(1, K + 1):
        q = p ** k
        poly = sp.cyclotomic_poly(q, sp.Symbol("x"))
        prod *= float(sp.N(poly.subs({"x": x}), 30))

    finite = (1 - x ** (p ** K)) / (1 - x)
    euler = 1 / (1 - x)
    print(
        f"Euler p={p}, s={s}, K={K}: "
        f"|prod-finite|={abs(prod-finite):.3e}, "
        f"|prod-Lp|={abs(prod-euler):.3e}"
    )


def main() -> None:
    print("=== rank-one global LCM twist recursion ===")
    for L, p in [(1, 2), (2, 3), (6, 2), (12, 5)]:
        check_global_refinement(L, p)

    print("\n=== Ramanujan innovation projectors ===")
    for p, k in [(2, 1), (2, 3), (3, 2), (5, 1)]:
        check_ramanujan_projector(p, k)

    print("\n=== cyclotomic refinements telescope to Euler factors ===")
    for p in [2, 3, 5, 7]:
        check_euler_telescope(p, 1.7, 4)


if __name__ == "__main__":
    main()
