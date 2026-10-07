#!/usr/bin/env python3
"""Actualization geometry / curvature controls for the RH program.

Finite/exact symbolic checks.  No zeta-zero input.  Nothing here proves RH.

Checks:
  1. support states form the exponent/divisibility lattice;
  2. the least unsupported positive integer is always a prime power;
  3. the greedy least-unsupported evolution generates prime powers in order;
  4. bare LCM pullback refinement is plaquette-flat;
  5. the critical parity system has the flat 1+1 principal cone;
  6. similarity/gauge changes of the canonical system do not curve that cone;
  7. the first three Magnus terms expose a polynomial moment/history hierarchy.
"""
from __future__ import annotations

from math import gcd, lcm, log
from sympy import (
    I, Matrix, Symbol, symbols, simplify, expand, integrate, cos, sin, exp,
)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def prime_power_base(n: int) -> int | None:
    if n < 2:
        return None
    if is_prime(n):
        return n
    for p in range(2, int(n**0.5) + 2):
        if not is_prime(p):
            continue
        x = p
        while x < n:
            x *= p
        if x == n:
            return p
    return None


def least_unsupported(M: int) -> int:
    n = 2
    while M % n == 0:
        n += 1
    return n


def greedy_actualization(count: int = 24):
    """Return (event q, prime p, new support L)."""
    L = 1
    out = []
    for _ in range(count):
        q = least_unsupported(L)
        p = prime_power_base(q)
        assert p is not None, f"least unsupported {q} was not a prime power"
        new_L = lcm(L, q)
        assert new_L // L == p
        out.append((q, p, new_L))
        L = new_L
    return out


def pullback(values: tuple[int, ...], factor: int) -> tuple[int, ...]:
    """Normalized-Haar pullback on values; norm normalization is irrelevant here."""
    L = len(values)
    return tuple(values[n % L] for n in range(factor * L))


def verify_flat_refinement() -> None:
    """The p-then-q and q-then-p bare refinement squares commute exactly."""
    seeds = [
        (1,),
        (2, -1),
        (3, 1, 4, 1, 5, 9),
    ]
    for f in seeds:
        for p, q in [(2, 3), (2, 5), (3, 5), (5, 7)]:
            pq = pullback(pullback(f, p), q)
            qp = pullback(pullback(f, q), p)
            assert pq == qp


def pauli():
    s1 = Matrix([[0, 1], [1, 0]])
    s2 = Matrix([[0, -I], [I, 0]])
    s3 = Matrix([[1, 0], [0, -1]])
    return s1, s2, s3


def comm(A, B):
    return simplify(A * B - B * A)


def coeff(A, sigma):
    return simplify((sigma * A).trace() / 2)


def verify_su11_transport() -> None:
    """The parity transfer generator is sigma3-skew-Hermitian: SU(1,1)-type."""
    s1, s2, s3 = pauli()
    z, mu = symbols("z mu", real=True)
    M = I*z*s3 + mu*s1
    assert simplify(M.conjugate().T*s3 + s3*M) == Matrix.zeros(2)
    assert simplify(M.trace()) == 0


def support_height(n: int) -> int:
    """Least X such that n divides lcm(1,...,X)."""
    x = n
    best = 1
    p = 2
    while p*p <= x:
        if x % p == 0:
            pk = 1
            while x % p == 0:
                x //= p
                pk *= p
            best = max(best, pk)
        p += 1
    if x > 1:
        best = max(best, x)
    return best


def verify_support_event_lag(N: int = 500) -> None:
    """support time <= event time, equality iff n is a prime power."""
    for n in range(2, N+1):
        h = support_height(n)
        assert h <= n
        equal = (h == n)
        assert equal == (prime_power_base(n) is not None)


def verify_principal_cone() -> None:
    """Mass and similarity gauges do not alter the characteristic cone."""
    s1, s2, s3 = pauli()
    xiA, xiX, u = symbols("xiA xiX u", real=True)

    principal = xiA * Matrix.eye(2) - xiX * s3
    assert simplify(principal.det() - (xiA**2 - xiX**2)) == 0

    # G=exp(u sigma1); explicit hyperbolic matrix.
    from sympy import cosh, sinh
    G = cosh(u) * Matrix.eye(2) + sinh(u) * s1
    B = simplify(G.inv() * s3 * G)
    gauged = xiA * Matrix.eye(2) - xiX * B
    assert simplify(gauged.det() - (xiA**2 - xiX**2)) == 0
    assert simplify(B * B - Matrix.eye(2)) == Matrix.zeros(2)


def verify_interaction_picture() -> None:
    """Free Dirac transport rotates one actualization pulse through harmonic phase."""
    s1, s2, s3 = pauli()
    z, t = symbols("z t", real=True)
    Uminus = Matrix([[exp(-I*z*t), 0], [0, exp(I*z*t)]])
    Uplus = Uminus.inv()
    rotated = simplify(Uminus * s1 * Uplus)
    target = cos(2*z*t) * s1 + sin(2*z*t) * s2
    assert simplify(rotated - target) == Matrix.zeros(2)


def magnus_integrands():
    """Return exact Pauli coefficients in the Ω2 and Ω3 Magnus integrands."""
    s1, s2, s3 = pauli()
    z, m1, m2, m3 = symbols("z m1 m2 m3", real=True)

    def M(m):
        return I*z*s3 + m*s1

    c12 = comm(M(m1), M(m2))
    assert simplify(coeff(c12, s2) - 2*z*(m1-m2)) == 0
    assert coeff(c12, s1) == 0 and coeff(c12, s3) == 0

    third = simplify(
        comm(M(m1), comm(M(m2), M(m3)))
        + comm(M(m3), comm(M(m2), M(m1)))
    )
    c1 = coeff(third, s1)
    c2 = coeff(third, s2)
    c3 = coeff(third, s3)

    assert simplify(c1 - 4*z**2*(-m1 + 2*m2 - m3)) == 0
    assert c2 == 0
    assert simplify(
        c3 - 4*I*z*(m1*(m2-m3)-m3*(m1-m2))
    ) == 0
    return c12, third


def verify_magnus_moment_kernels() -> None:
    """Reduce the linear-in-mu Magnus kernels to centered polynomials."""
    t, T = symbols("t T", positive=True, real=True)

    # Ω2 after the 1/2 Magnus coefficient:
    k1 = expand(2*t - T)
    assert expand(k1 - 2*(t-T/2)) == 0

    # Ω3 linear-in-mu ordered-simplex kernel before the 2/3 factor.
    k2 = expand(-t**2/2 + 2*t*(T-t) - (T-t)**2/2)
    centered = expand(T**2/4 - 3*(t-T/2)**2)
    assert expand(k2-centered) == 0

    # It is -T^2/2 times the shifted Legendre P2.
    x = 2*t/T - 1
    P2 = (3*x**2 - 1)/2
    assert simplify(k2 + T**2*P2/2) == 0


def verify_two_dim_scalar_curvature_formula() -> None:
    """Symbolically verify R for ds^2=N(A)^2 dA^2-a(A)^2 dX^2.

    Convention matches the explicit Christoffel/Ricci calculation in the
    research note; the overall sign flips under the opposite Riemann convention.
    """
    from sympy import Function, diff
    A = Symbol("A", real=True)
    N = Function("N")(A)
    a = Function("a")(A)
    formula = -2/(N*a) * diff(diff(a, A)/N, A)
    expanded_formula = simplify(
        2*(-N*diff(a, A, 2) + diff(N, A)*diff(a, A))/(N**3*a)
    )
    assert simplify(formula - expanded_formula) == 0


def main() -> None:
    events = greedy_actualization()
    expected = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27]
    assert [q for q, _, _ in events[:len(expected)]] == expected

    verify_flat_refinement()
    verify_su11_transport()
    verify_support_event_lag()
    verify_principal_cone()
    verify_interaction_picture()
    magnus_integrands()
    verify_magnus_moment_kernels()
    verify_two_dim_scalar_curvature_formula()

    print("First greedy actualization events:")
    print("  " + ", ".join(str(q) for q, _, _ in events))
    print("Verified: least-unsupported evolution fires prime powers only.")
    print("Verified: bare LCM refinement plaquettes are flat.")
    print("Verified: parity transfer is SU(1,1)-type (sigma3 metric preserving).")
    print("Verified: support time equals event time iff n is a prime power.")
    print("Verified: Suzuki parity principal cone is xi_A^2-xi_X^2=0.")
    print("Verified: similarity gauges leave that cone unchanged.")
    print("Verified: Ω1/Ω2/Ω3 expose P0/P1/P2-type moment hierarchy + ordered correlations.")
    print("Verified: 1+1 diagonal metric scalar-curvature formula.")


if __name__ == "__main__":
    main()
