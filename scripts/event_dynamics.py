"""Certified finite event probes. Universal claims are proved in EVENT_DYNAMICS.md.

No zero ordinates are used. Arb balls enclose rounding and exponential-series
tails. Integer event indices fix which prime powers are active; no exp/log
round-trip is used to decide event inclusion.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from flint import arb, ctx

try:
    from .suzuki_psi import prime_power_events_up_to
except ImportError:
    from suzuki_psi import prime_power_events_up_to


def gamma_linear():
    return -(arb.const_euler() + arb.pi()/2 + 3*arb(2).log() + arb.pi().log())/2


def arch(t, terms=None):
    """Enclose A(t) for a strictly positive real ball t.

    Tail after N terms of 4 sum exp(-(4k+1)t/2)/(4k+1)^2 is <=
    4 exp(-(4N+1)t/2)/((4N+1)^2 (1-exp(-2t))).
    """
    t = arb(t)
    if t.is_zero():
        return arb(0)
    if not t > 0:
        raise ValueError('arch requires t>0 or exact t=0')
    z = (-t/2).exp()
    ratio = (-2*t).exp()
    target = arb(2)**(-ctx.prec+16)
    total = arb(0)
    term_exp = z
    k = 0
    while True:
        tail = 4*term_exp/((4*k+1)**2*(1-ratio))
        if (terms is None and tail < target) or (terms is not None and k >= terms):
            break
        total += 4*term_exp/(4*k+1)**2
        term_exp *= ratio
        k += 1
        if k > 100000:
            raise ArithmeticError('series budget exhausted; no certificate')
    # Symmetric enclosure is wider than necessary but always includes [0,tail].
    remainder = arb(0, tail.upper())
    c4 = arb.pi()**2/4 + 2*arb.const_catalan()
    return 4*((t/2).exp()+z-2) + gamma_linear()*t + c4-total-remainder


def arch_prime(t):
    t = arb(t)
    if not t > 0:
        raise ValueError('derivative requires t>0')
    y = (t/2).exp()
    z = 1/y
    return 2*(y-z)+gamma_linear()+z.atanh()+z.atan()


def curvature(t):
    t = arb(t)
    if not t > 0:
        raise ValueError('curvature requires t>0')
    x = t.exp()
    return (x**3-x-1)/(x.sqrt()*(x**2-1))


def prefix(events):
    s = arb(0)
    h = arb(0)
    for e in events:
        w = arb(e.prime).log()/arb(e.n).sqrt()
        s += w
        h += w*arb(e.n).log()
    return s, h


def frozen_value(t, s, h):
    return arch(t)-s*t+h


def minimum(s, h, left, right, bits=90):
    """Convex constrained min on [left,right], after the plastic transition.

    Every classification is a certified comparison. Ambiguity raises instead
    of manufacturing a sign. Returns (minimizer enclosure, value enclosure,
    endpoint/interior classification).
    """
    left, right = arb(left), arb(right)
    if not (left > 0 and curvature(left) > 0 and right > left):
        raise ValueError('minimum requires an ordered interval of positive curvature')
    dl, dr = arch_prime(left)-s, arch_prime(right)-s
    if dl >= 0:
        return left, frozen_value(left, s, h), 'left'
    if dr <= 0:
        return right, frozen_value(right, s, h), 'right'
    if not (dl < 0 and dr > 0):
        raise ArithmeticError('ambiguous endpoint derivative; increase precision')
    lo, hi = left.lower(), right.upper()
    tolerance = arb(2)**(-bits)
    for _ in range(bits+50):
        mid = ((lo+hi)/2).mid()
        d = arch_prime(mid)-s
        if d < 0:
            lo = mid
        elif d > 0:
            hi = mid
        else:
            break
        if hi-lo < tolerance:
            break
    box = lo.union(hi)
    return box, frozen_value(box, s, h), 'interior'


def initial_certificate():
    """Finite certificates plus analytic curvature argument cover [0,log2]."""
    theta = arb('1.3247179572').union(arb('1.3247179573'))
    assert arb('1.3247179572')**3-arb('1.3247179572')-1 < 0
    assert arb('1.3247179573')**3-arb('1.3247179573')-1 > 0
    t0 = theta.log()
    at_transition = arch(t0)
    assert at_transition > 0
    assert arch_prime(arb('0.46400')) < 0
    assert arch_prime(arb('0.46401')) > 0
    critical_box = arb('0.46400').union(arb('0.46401'))
    at_minimum = arch(critical_box)
    assert at_minimum > 0
    return {'transition':str(t0), 'A_transition':str(at_transition),
            'initial_minimum_bracket':str(critical_box),
            'A_initial_minimum':str(at_minimum)}


def run_certificate(last_event=101):
    events = prime_power_events_up_to(last_event)
    if not events or events[-1].n != last_event:
        raise ValueError('last_event must be a prime power >= 2')
    records = []
    s = h = arb(0)
    for j, e in enumerate(events[:-1]):
        w = arb(e.prime).log()/arb(e.n).sqrt()
        a = arb(e.n).log()
        s += w
        h += w*a
        b = arb(events[j+1].n).log()
        point, value, kind = minimum(s,h,a,b)
        if not value > 0:
            raise ArithmeticError(f'positivity not certified after q={e.n}: {value}')
        records.append({'q':e.n,'next_q':events[j+1].n,'kind':kind,
                        'minimum_time':str(point),'minimum_value':str(value)})
    return {'precision_bits':ctx.prec,'scope':f'0 < t <= log({last_event})',
            'initial':initial_certificate(),'intervals':records,
            'universal_claim':False}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--last-event',type=int,default=101)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    with ctx.workprec(200):
        result=run_certificate(args.last_event)
        output=json.dumps(result,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(output)
    print(output if not args.output else f'Certified {len(result["intervals"])} intervals; {result["scope"]}')


if __name__=='__main__':
    main()
