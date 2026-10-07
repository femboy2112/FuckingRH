"""Exact boundary-state algebra and certified grouped clock determinants.

No standard Fredholm determinant is asserted for the noncompact infinite
clock direct sum. Universal claims are proved in the Round008 notes.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp
from flint import arb, ctx
from scripts.round008_clock import clock


def events(horizon):
    if not isinstance(horizon, int) or horizon < 1:
        raise ValueError('positive integer horizon required')
    out = []
    for p in sp.primerange(2, horizon+1):
        p = int(p)
        q, k = p, 1
        while q <= horizon:
            out.append((q, p, k))
            q, k = q*p, k+1
    return sorted(out)


def refinement_data(horizon):
    length = 1
    out = []
    for q, p, k in events(horizon):
        out.append((q, p, k, length, (p-1)*length))
        length *= p
    return length, out


def green(z, length):
    return 1/(z**length-1)


def refine_green(g, ratio):
    if ratio < 2:
        raise ValueError('proper integer refinement required')
    return g**ratio/((g+1)**ratio-g**ratio)


def twist_green(g, omega):
    return g/(1-(omega-1)*g)


def full_factor(x, prime, old_length):
    return sum(x**(b*old_length) for b in range(prime))


def local_factor(x, prime, depth):
    return full_factor(x, prime, prime**(depth-1))


def mixed_product(horizon, sigma):
    """Real positive grouped product, Arb enclosure at finite horizon."""
    sigma = arb(sigma)
    if not sigma > 0:
        raise ValueError('positive real sigma required')
    length, data = refinement_data(horizon)
    value = arb(1)
    for q, p, k, old, dim in data:
        y = (-sigma*old*arb(p).log()).exp()
        value *= (1-y**p)/(1-y)
    # Every future old length is at least length * 2**r.  Since 2**r>=r+1,
    # sum y/(1-y) <= z/(1-z)**2 for z=2**(-sigma*length).
    z = (-sigma*length*arb(2).log()).exp()
    log_tail_bound = z/(1-z)**2
    return value, log_tail_bound


def exact_boundary_checks():
    z, g, omega = sp.symbols('z g omega')
    checked = []
    for length in [1, 2, 3, 5]:
        C = clock(length)
        R = (z*sp.eye(length)-C).inv()
        assert sp.cancel(R[length-1, 0]-green(z, length)) == 0
        boundary = sp.zeros(length)
        boundary[0, length-1] = 1
        twisted = C+(omega-1)*boundary
        Rw = (z*sp.eye(length)-twisted).inv()
        rhs = R+(omega-1)/(1-(omega-1)*green(z, length))*R*boundary*R
        assert (Rw-rhs).applyfunc(sp.cancel) == sp.zeros(length)
        assert sp.cancel(Rw[length-1, 0]-twist_green(green(z, length), omega)) == 0
        for ratio in [2, 3, 4, 5]:
            assert sp.cancel(refine_green(green(z, length), ratio)-green(z, ratio*length)) == 0
        assert sp.cancel(sp.diff(green(z, length), z)+(length/z)*green(z, length)*(green(z, length)+1)) == 0
        checked.append(length)
    degrees = {}
    for ratio in [2, 3, 4, 5, 7]:
        n, d = sp.fraction(sp.cancel(refine_green(g, ratio)))
        assert sp.gcd(n, d) == 1
        degrees[ratio] = int(max(sp.degree(n, g), sp.degree(d, g)))
        assert degrees[ratio] == ratio
    return {'lengths': checked, 'refinement_rational_degrees': degrees}


def controls():
    x, z = sp.symbols('x z')
    assert full_factor(x, 3, 2)-local_factor(x, 3, 1) == x**4-x
    # General nested composite refinements retain the clock identity: it is
    # harmonic algebra, not a test that singles out the prime schedule.
    length, product = 1, sp.Integer(1)
    for ratio in [4, 3, 6]:
        product *= full_factor(x, ratio, length)
        length *= ratio
    assert sp.cancel(product-(1-x**length)/(1-x)) == 0
    # Order-sensitive birth charges: two genuinely different global products.
    order23 = (1+sp.Rational(1, 2)**2)*(1+sp.Rational(1, 3)**4+sp.Rational(1, 3)**8)
    order32 = (1+sp.Rational(1, 3)**2+sp.Rational(1, 3)**4)*(1+sp.Rational(1, 2)**6)
    assert order23 != order32
    # Acyclic forward shift stays nilpotent, so cannot replace clock loops.
    F = sp.zeros(5)
    for i in range(4):
        F[i+1, i] = 1
    assert (sp.eye(5)-z*F).det() == 1
    return {'q3_full_minus_local': str(x**4-x), 'composite_refinements': [4,3,6],
            'order23_at_s2': str(order23), 'order32_at_s2': str(order32),
            'forward_determinant': '1'}


def evidence():
    with ctx.workprec(160):
        value, tail = mixed_product(7, 2)
        upper = value*tail.exp()
        zeta2 = arb.pi()**2/6
        assert upper < zeta2
        return {'method': 'exact rational identities and Arb enclosure with analytic infinite tail',
                'boundary': exact_boundary_checks(), 'mutations': controls(),
                'global_at_s2': {'prefix_N7': str(value), 'log_tail_upper': str(tail),
                                 'infinite_product_upper': str(upper), 'zeta2': str(zeta2),
                                 'certified_strictly_less': True},
                'scope': 'product mismatch is certified for the infinite grouped product; not an RH sign test'}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path)
    args = p.parse_args()
    content = json.dumps(evidence(), indent=2)+'\n'
    if args.output:
        args.output.write_text(content)
    else:
        print(content, end='')
