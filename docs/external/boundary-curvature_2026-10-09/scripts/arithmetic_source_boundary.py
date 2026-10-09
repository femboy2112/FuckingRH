"""Zero-free arithmetic-source and mixed finite-window boundary diagnostics.

This module constructs a source-faithful *candidate architecture*, NOT an RH proof.
No zero ordinates, scattering phases, or zero-side matrices are used.

Conventions:
  F(s)=sum_n a[n] n**(-s), a[1]=1;
  -F'/F=sum_n b[n] n**(-s);
  T_h f(x)=1_I(x)1_I(x-h) f(x-h), I=[-L,L]; T_h*=T_-h.
"""
from __future__ import annotations

from math import isqrt, log
from typing import Callable, Sequence


def factorization(n: int) -> tuple[tuple[int, int], ...]:
    """Trial division; only used for small finite control instruments."""
    if n < 1:
        raise ValueError('positive integers only')
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            exponent = 0
            while n % d == 0:
                n //= d
                exponent += 1
            factors.append((d, exponent))
        d += 1
    if n > 1:
        factors.append((n, 1))
    return tuple(factors)


def prime_power(n: int) -> tuple[int, int] | None:
    factors = factorization(n)
    return factors[0] if len(factors) == 1 else None


def coefficients_from_local_parameters(
    alpha: dict[int, complex], limit: int
) -> list[complex]:
    """Degree-one Euler coefficients (unitarity is checked separately)."""
    a = [0j] * (limit + 1)
    for n in range(1, limit + 1):
        z = 1 + 0j
        for p, k in factorization(n):
            z *= alpha[p] ** k
        a[n] = z
    return a


def logarithmic_derivative_coefficients(a: Sequence[complex]) -> list[complex]:
    """Dirichlet-convolution recurrence for coefficients of -F'/F."""
    if not a or abs(a[1] - 1) > 1e-12:
        raise ValueError('a[1] must equal 1')
    limit = len(a) - 1
    b = [0j] * (limit + 1)
    for n in range(2, limit + 1):
        value = a[n] * log(n)
        for d in range(2, n):
            if n % d == 0:
                value -= b[d] * a[n // d]
        b[n] = value
    return b


def logarithmic_source_defect(
    a: Sequence[complex], alpha: dict[int, complex]
) -> float:
    """Max defect from b[p^k]=alpha[p]^k log p and all other b[n]=0."""
    b = logarithmic_derivative_coefficients(a)
    return max(
        (
            abs(b[n] - (alpha[pk[0]] ** pk[1] * log(pk[0]) if pk else 0j))
            for n in range(2, len(a))
            for pk in (prime_power(n),)
        ),
        default=0.0,
    )


def local_unitarity_defect(alpha: dict[int, complex]) -> float:
    """Omit ramified primes (alpha[p]=0); reject |alpha[p]| != 1 elsewhere."""
    return max((abs(abs(z) - 1.0) for z in alpha.values() if z != 0), default=0.0)


def character_compatibility_defect(alpha: dict[int, complex], character) -> float:
    """Check local parameters against one specified global Dirichlet character.

    Unitarity alone is NOT enough: an arbitrary assignment of unit phases
    need not come from a genuine Dirichlet character.
    """
    return max((abs(z-character(p)) for p,z in alpha.items()), default=0.0)


def clock_defect(p: int, imposed_step: float) -> float:
    """||([log N,V_p] - imposed_step*V_p)e_n||, any basis vector e_n."""
    return abs(log(p) - imposed_step)


def chi_mod_5(n: int) -> complex:
    """Primitive odd character mod 5 with chi(2)=i."""
    return (0j, 1 + 0j, 1j, -1j, -1 + 0j)[n % 5]


def inside(x: float, L: float) -> bool:
    return -L <= x <= L


def compressed_shift(f: Callable[[float], complex], x: float, a: float, L: float) -> complex:
    """(T_a f)(x), zero-extended beyond [-L,L]."""
    return f(x - a) if inside(x, L) and inside(x - a, L) else 0j


def mixed_commutator_nested(f: Callable[[float], complex], x: float, a: float, b: float, L: float) -> complex:
    """([T_a^*,T_b]f)(x), using literal nested compressions."""
    left = compressed_shift(
        lambda y: compressed_shift(f, y, b, L), x, -a, L
    )
    right = compressed_shift(
        lambda y: compressed_shift(f, y, -a, L), x, b, L
    )
    return left - right


def mixed_commutator_boundary(f: Callable[[float], complex], x: float, a: float, b: float, L: float) -> complex:
    """Exact boundary-geometry formula for [T_a^*,T_b] on the interval."""
    if not inside(x, L) or not inside(x + a - b, L):
        return 0j
    return (int(inside(x + a, L)) - int(inside(x - b, L))) * f(x + a - b)


def prime_half_density_weight(p: int, k: int) -> float:
    """The Weil source weight (log p) p^(-k/2), NOT a positive theorem."""
    return log(p) * p ** (-k / 2)


# Finite arithmetic-coordinate realization of the canonical Euler logarithm.
# This is an INDEPENDENT lattice algebra check, not a discretization of log R.
def truncated_multiplication_shift(m: int, limit: int):
    """V_m e_n=e_(m*n), discarded if m*n>limit, on C^limit."""
    import numpy as np
    out = np.zeros((limit, limit), dtype=complex)
    for n in range(1, limit // m + 1):
        out[m * n - 1, n - 1] = 1
    return out


def finite_dirichlet_operator(a: Sequence[complex]):
    """F_a=sum_{n<=N}a(n)/sqrt(n) V_n. No zero input."""
    import numpy as np
    from math import sqrt
    limit = len(a) - 1
    out = np.zeros((limit, limit), dtype=complex)
    for n in range(1, limit + 1):
        if a[n] != 0:
            out += (a[n] / sqrt(n)) * truncated_multiplication_shift(n, limit)
    return out


def finite_euler_inverse(alpha: dict[int, complex], limit: int):
    """E=prod_{p<=N}(I-alpha_p p^-1/2 V_p), including zeros at ramified primes."""
    import numpy as np
    from math import sqrt
    I = np.eye(limit, dtype=complex)
    euler = I.copy()
    for p in range(2, limit + 1):
        if prime_power(p) == (p, 1):
            euler = euler @ (I - alpha[p] / sqrt(p) * truncated_multiplication_shift(p, limit))
    return euler


def finite_nilpotent_log(unipotent):
    """Canonical finite polynomial log(I+Y), where Y raises index >= x2.

    For Y=sum_{n>=2} c_n V_n on e_m, Y^(floor(log2 N)+1)=0.
    We DO NOT use an amplitude threshold to decide when to stop.
    """
    import numpy as np
    dim = unipotent.shape[0]
    I = np.eye(dim, dtype=complex)
    Y = unipotent - I
    power = I.copy()
    result = np.zeros_like(unipotent)
    for k in range(1, dim.bit_length()):
        power = power @ Y
        result += (-1) ** (k + 1) * power / k
    if np.max(np.abs(power @ Y)) > 1e-10:
        raise ValueError('Input not a truncated unipotent Dirichlet-convolution operator')
    return result


def finite_clock_commutator(V):
    """[X,V] where X=diag(log n); its source amplitudes are b(n)/sqrt n."""
    import numpy as np
    dim = V.shape[0]
    X = np.diag([log(n) for n in range(1, dim+1)])
    return X @ V - V @ X


def finite_source_operator(b: Sequence[complex]):
    """sum_{n<=N}b(n)/sqrt(n) V_n; compare with [X,log F]."""
    return finite_dirichlet_operator(b)


if __name__ == '__main__':
    alpha = {p: chi_mod_5(p) for p in (2, 3, 5, 7, 11, 13)}
    a = coefficients_from_local_parameters(alpha, 13)
    print('chi_5 source max residual:', logarithmic_source_defect(a, alpha))
    print('chi_5 local unitarity residual:', local_unitarity_defect(alpha))
    f = lambda x: 1+0j
    print('mixed [T_log2*,T_log3] at x=-0.2, L=1:',
          mixed_commutator_boundary(f, -0.2, log(2), log(3), 1.0))
