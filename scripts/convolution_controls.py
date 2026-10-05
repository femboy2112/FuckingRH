"""Exact/interval controls for the convolution-residual no-go theorem.

These routines do not calculate zeta zeros or certify RH. All sign-sensitive
numerics return mpmath interval enclosures. The accompanying note contains
the universal proofs; finite examples test the implementation and controls.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import factorial, isqrt
import mpmath as mp


def primes_up_to(n: int) -> list[int]:
    """Small independent trial-division enumerator, not the Suzuki sieve."""
    return [p for p in range(2, n + 1)
            if all(p % d for d in range(2, isqrt(p) + 1))]


def uniform_sum_cdf(widths: list[Fraction], x: Fraction) -> Fraction:
    """Exact CDF of the sum of Uniform[-a,a] variables, a in widths."""
    widths = list(map(Fraction, widths))
    x = Fraction(x)
    if not widths or any(a <= 0 for a in widths):
        raise ValueError("At least one positive half-width is required")
    n = len(widths)
    shifted = x + sum(widths)
    numerator = Fraction(0)
    for size in range(n + 1):
        for subset in combinations(range(n), size):
            positive_part = max(Fraction(0), shifted - 2 * sum(widths[j] for j in subset))
            numerator += (-1) ** size * positive_part ** n
    denominator = Fraction(factorial(n))
    for a in widths:
        denominator *= 2 * a
    return numerator / denominator


def borwein_plateau_ratio(boundary: Fraction, widths: list[Fraction]) -> Fraction:
    """Return (2*a0/pi)*integral_0^infinity product_j sinc(a_j*x) dx."""
    boundary = Fraction(boundary)
    if boundary <= 0:
        raise ValueError("The boundary must be positive")
    return uniform_sum_cdf(widths, boundary) - uniform_sum_cdf(widths, -boundary)


def log_residual_modulus_interval(primes: list[int], t, dps: int = 50):
    """Enclose log|exp(V*t^2/2)*E exp(it(S-E S))| without series truncation."""
    mp.iv.dps = dps
    iv = mp.iv
    t = iv.mpf(t)
    result = iv.mpf(0)
    for p in primes:
        if p < 2:
            raise ValueError("Prime bases must be at least two")
        r = 1 / iv.sqrt(p)
        ell = iv.log(p)
        variance = ell ** 2 * r / (1 - r) ** 2
        modulus_squared_denominator = 1 + r ** 2 - 2 * r * iv.cos(t * ell)
        result += (variance * t ** 2 / 2 + iv.log(1 - r)
                   - iv.log(modulus_squared_denominator) / 2)
    return result


def residual_pd_minor_interval(primes: list[int], t, dps: int = 50):
    """Two-point characteristic-function PSD determinant: 1-|R(t)|^2."""
    log_modulus = log_residual_modulus_interval(primes, t, dps=dps)
    return 1 - mp.iv.exp(2 * log_modulus)


def two_prime_gaussian_image_interval(p: int, q: int, x, dps: int = 50):
    mp.iv.dps = dps
    iv = mp.iv
    x = iv.mpf(x)
    g = lambda a: iv.exp(-iv.pi * (a * x) ** 2)
    return g(1) - g(p) - g(q) + g(p * q)


def gaussian_mixture_multiplier(y: Fraction) -> Fraction:
    """P(s), with y=16^s, evaluated algebraically away from y=0."""
    y = Fraction(y)
    return (y * y + 10 * y + 16) / (27 * y)


def synthetic_quartet_at_period_interval(a, b, dps: int = 50):
    """Psi from z=+/-a+/-ib at t=2*pi/a, using its exact simplification."""
    mp.iv.dps = dps
    iv = mp.iv
    a, b = iv.mpf(a), iv.mpf(b)
    t = 2 * iv.pi / a
    bt = b * t
    cosh_bt = (iv.exp(bt) + iv.exp(-bt)) / 2
    return 4 * (1 - cosh_bt) * (a ** 2 - b ** 2) / (a ** 2 + b ** 2) ** 2


def planted_tail(t: Fraction, horizon: Fraction) -> Fraction:
    """Even exact toy: t^2 on [-T,T], negative at 2T; T must be positive."""
    t, horizon = Fraction(t), Fraction(horizon)
    if horizon <= 0:
        raise ValueError("horizon must be positive")
    return t * t - 5 * horizon * max(Fraction(0), abs(t) - horizon)


def geometric_cumulants_exact(r: Fraction, jump: Fraction = Fraction(1)):
    """First three cumulants for P(K=k)=(1-r)r^k, with signed jump."""
    r, jump = Fraction(r), Fraction(jump)
    if not 0 < r < 1:
        raise ValueError("r must be in (0,1)")
    return (jump * r / (1 - r),
            jump ** 2 * r / (1 - r) ** 2,
            jump ** 3 * r * (1 + r) / (1 - r) ** 3)


if __name__ == "__main__":
    print("Borwein plateau:", borwein_plateau_ratio(Fraction(1), [Fraction(1, 3), Fraction(1, 5)]))
    print("Borwein post-contact:", borwein_plateau_ratio(Fraction(1), [Fraction(1), Fraction(1, 3)]))
    print("One-prime log residual modulus:", log_residual_modulus_interval([2], "1"))
    print("One-prime PD determinant:", residual_pd_minor_interval([2], "1"))
    print("Two-prime Gaussian image:", two_prime_gaussian_image_interval(2, 3, "0.1"))
    print("Synthetic off-line quartet:", synthetic_quartet_at_period_interval("1", "0.25"))
    print("Planted tail at 2T for T=10:", planted_tail(Fraction(20), Fraction(10)))
