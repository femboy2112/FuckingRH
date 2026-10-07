"""Round008 exact Gamma/affine controls. No zeros are input.

The universal statements are proved in GAMMA_DRIFT.md and
AFFINE_CONTINUUM.md. Finite matrices calibrate those proofs; Arb supplies
rigorous enclosures for the stated special-function identities and tails.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from flint import acb, acb_series, arb, ctx
import sympy as sp


def ladder_determinant(s):
    """det_zeta(diag(0,2,4,...)+s), entire continuation via reciprocal Gamma."""
    s = acb(s)
    return ((1-s/2)*arb(2).log()).exp()*arb.pi().sqrt()*(s/2).rgamma()


def hurwitz_ladder_determinant(s):
    """Independent Arb Hurwitz-zeta Taylor differentiation at w=0."""
    old_cap = ctx.cap
    try:
        ctx.cap = 2
        w = acb_series([0, 1])
        z = (-w*arb(2).log()).exp()*w.zeta(acb(s)/2)
        return (-z[1]).exp()
    finally:
        ctx.cap = old_cap


def relative_det2(s, base):
    """Hilbert--Schmidt relative determinant; distinct from the zeta ratio."""
    s, base = acb(s), acb(base)
    return (base/2).gamma()*(s/2).rgamma()*(((s-base)/2)*(base/2).digamma()).exp()


def gamma_multiplier(v):
    v = arb(v)
    return acb(arb(1)/4, v/2).digamma().real - (arb(1)/4).digamma()


def gamma_multiplier_cutoff(v, modes):
    if modes < 0:
        raise ValueError('modes must be nonnegative')
    v = arb(v)
    return sum((2*v*v/(lam*(lam*lam+v*v))
                for lam in (arb(2*m)+arb(1)/2 for m in range(modes))), arb(0))


def gamma_multiplier_tail_bound(v, modes):
    """Uniform pointwise bound by an integral-test tail, valid even for M=0."""
    if modes < 0:
        raise ValueError('modes must be nonnegative')
    v = arb(v)
    lam = arb(2*modes)+arb(1)/2
    return 2*v*v*(1/(lam**3)+1/(4*lam**2))


def heat_hankel(points, modes=None):
    """Exact heat Gram, points x_i=e^(-2t_i) in (0,1).

    Unshifted ladder; multiplying by exp(-(t_i+t_j)/2) is a positive
    diagonal congruence and does not change the rank/inertia theorem.
    """
    points = [sp.Rational(x) for x in points]
    if any(not 0 < x < 1 for x in points):
        raise ValueError('points must be rational numbers in (0,1)')
    if modes is None:
        return sp.Matrix([[1/(1-x*y) for y in points] for x in points])
    if modes < 0:
        raise ValueError('modes must be nonnegative')
    V = sp.Matrix([[x**m for m in range(modes)] for x in points])
    return V*V.T


def carry_step(clock_size, residue, quotient):
    """Integer Euclidean-division carry; extends by translation of a real fiber."""
    if clock_size < 1 or not 0 <= residue < clock_size:
        raise ValueError('invalid residue clock')
    return ((residue+1) % clock_size,
            quotient + int(residue == clock_size-1))


def carry_power(clock_size, residue, quotient, steps):
    if clock_size < 1 or not 0 <= residue < clock_size:
        raise ValueError('invalid residue clock')
    wraps, new_residue = divmod(residue+steps, clock_size)
    return new_residue, quotient+wraps


def helical_heat_trace(clock_size, power, heat_time):
    """Exact formula Tr[(I tensor exp(-t Hosc)) U_L^k]."""
    if clock_size < 1:
        raise ValueError('clock must be positive')
    t = arb(heat_time)
    if not t > 0:
        raise ValueError('heat time must be certified positive')
    if power % clock_size:
        return arb(0)
    a = arb(power//clock_size)
    return clock_size/(1-(-2*t).exp())*(-a*a/(4*t.tanh())).exp()


def evidence():
    with ctx.workdps(65):
        determinant_records = []
        for s in (acb(arb(1)/2), acb(2), acb(arb(7)/3, 2), acb(1, 9)):
            direct = ladder_determinant(s)
            hurwitz = hurwitz_ladder_determinant(s)
            discrepancy = direct-hurwitz
            recurrence = s*ladder_determinant(s+2)-direct
            assert discrepancy.contains(0) and recurrence.contains(0)
            determinant_records.append({'s': str(s), 'determinant': str(direct),
                'hurwitz_discrepancy': str(discrepancy),
                'recurrence_discrepancy': str(recurrence)})
        tail_records = []
        for v, modes in ((1, 2), (3, 8), (17, 32), (100, 128)):
            finite = gamma_multiplier_cutoff(v, modes)
            tail = gamma_multiplier(v)-finite
            upper = gamma_multiplier_tail_bound(v, modes)
            assert tail > 0 and upper-tail > 0
            tail_records.append({'frequency': v, 'modes': modes,
                'finite_positive_multiplier': str(finite),
                'actual_tail': str(tail), 'analytic_upper_bound': str(upper)})
        ranks = []
        for n in range(1, 8):
            points = [sp.Rational(1, 2**j) for j in range(1, n+1)]
            infinite = heat_hankel(points)
            finite = heat_hankel(points, n)
            assert infinite.det() > 0 and finite.det() > 0
            ranks.append({'size': n, 'infinite_kernel_det': str(infinite.det()),
                'first_n_modes_det': str(finite.det()),
                'first_n_minus_one_modes_rank': heat_hankel(points, n-1).rank()})
        return {'status': 'finite exact/Arb controls; no RH conclusion',
            'precision_decimal_digits': 65, 'determinants': determinant_records,
            'positive_cutoff_tail_certificates': tail_records,
            'heat_hankel_controls': ranks,
            'nontrivial_helical_trace': str(helical_heat_trace(6, 12, arb(3)/5)),
            'off_cycle_trace': str(helical_heat_trace(6, 5, arb(3)/5))}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = json.dumps(evidence(), indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result+'\n')
    else:
        print(result)
