"""Exact finite Dirichlet-algebra controls for composite-to-primitive maps."""
from fractions import Fraction


def convolution(a, b, limit):
    out = {}
    for n, x in a.items():
        for m, y in b.items():
            if n*m <= limit:
                out[n*m] = out.get(n*m, Fraction(0))+x*y
    return {n: v for n, v in out.items() if v}


def dirichlet_log(a, limit):
    """Formal log_* a with a[1]=1, exact rational coefficients n<=limit."""
    if a.get(1) != 1 or any(n < 1 for n in a):
        raise ValueError('normalized positive integer grading required')
    b = {n: Fraction(v) for n, v in a.items() if 1 < n <= limit and v}
    power, out = b, {}
    for j in range(1, limit.bit_length()):
        if not power:
            break
        for n, c in power.items():
            out[n] = out.get(n, Fraction(0))+Fraction((-1)**(j+1), j)*c
        power = convolution(power, b, limit)
    return {n: v for n, v in out.items() if v}


def factors(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0)+1
    return out


def old_monoid(n, p):
    return n >= 1 and all(r < p for r in factors(n))


def midpoint_distances(p):
    if p < 2 or factors(p) != {p: 1}:
        raise ValueError('p must be prime')
    return [d for d in range(1, p)
            if old_monoid(p-d, p) and old_monoid(p+d, p)]


def even_level_surplus(p, d, k):
    """Normalized m_k=p^(k/2) H^(k), rational for positive even k."""
    if not (0 < d < p and k > 0 and k % 2 == 0):
        raise ValueError('positive even level and valid radius required')
    exponent = k//2
    return (Fraction(p, p-d)**exponent+Fraction(p, p+d)**exponent)/2-1
