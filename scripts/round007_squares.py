"""Round007 first-order candidates and exact Weil edge-square residual.

No zeros or fitted Gram factors. Arb enclosures certify only stated finite
identities/signs; universal claims have proofs in the accompanying notes.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sympy as sp
from flint import arb, ctx
from .suzuki_psi import prime_power_events_up_to
from .event_dynamics import arch, gamma_linear


def carrier_channels(N, weights=None):
    """Rectangular outgoing halo retains the exact upper chiral boundary.

    Input integers 1..N, output integers 1..2N+1. Optional weights are exact
    event-square weights. Defaults retain symbolic square roots of log p/n^.5.
    """
    if N < 1:
        raise ValueError('N must be positive')
    rows = 2*N+1
    plus, minus, jet = [sp.zeros(rows, N) for _ in range(3)]
    events = {e.n: sp.log(e.prime)/sp.sqrt(e.n) for e in prime_power_events_up_to(N)}
    if weights is not None:
        events = dict(weights)
    for n in range(1, N+1):
        plus[2*n, n-1] = 1
        minus[2*n-2, n-1] = 1
        if n in events:
            jet[n-1, n-1] = sp.sqrt(events[n])
    pp = {e.n for e in prime_power_events_up_to(N+1)}
    flux = sp.zeros(N+1, N)
    for n in range(1, N+1):
        flux[n, n-1] = int(n in pp)-int(n+1 in pp)
    labels = [a for a in range(2, sp.integer_nthroot(N+1, 2)[0]+1)]
    cone = sp.zeros(len(labels), N)
    for i,a in enumerate(labels):
        cone[i, a*a-2] = 1
    return {'plus':plus, 'minus':minus, 'chiral':plus-minus,
            'jet':jet, 'flux':flux, 'cone':cone}


def block_dirac(A):
    return sp.BlockMatrix([[sp.zeros(A.cols), A.T.conjugate()],
                           [A, sp.zeros(A.rows)]]).as_explicit()


def event_weights(N, overrides=None):
    w = {e.n: arb(e.prime).log()/arb(e.n).sqrt() for e in prime_power_events_up_to(N)}
    if overrides:
        for n,v in overrides.items():
            if v is None:
                w.pop(n, None)
            else:
                w[n] = arb(v)
    return w


def positive_gamma(t):
    t=abs(arb(t))
    if t.is_zero(): return arb(0)
    pole=8*((t/2).cosh()-1)
    return arch(t)-pole-gamma_linear()*t


def scalar_parts(t, weights):
    t=abs(arb(t))
    W=sum(weights.values(),arb(0))
    P=arb(0)
    for n,w in weights.items():
        d=t-arb(n).log()
        if d>0: P += w*d
        elif d<0 or d.contains(0):
            # Exact equality can be an interval around zero. Enclose max(d,0)
            # rather than decide inclusion through a rounded logarithm.
            if d.contains(0): P += w*arb(0,max(abs(d.lower()),abs(d.upper())))
        else: raise ArithmeticError('unclassified ramp')
    E=positive_gamma(t)+W*t-P
    pole=8*((t/2).cosh()-1)
    residual=pole+(gamma_linear()-W)*t
    target=arch(t)-P if not t.is_zero() else arb(0)
    return E,residual,target


def kernel_parts(t,u,weights):
    # The same argument has exactly zero difference. Ball subtraction forgets
    # this dependency; overlap of two unrelated balls is NOT treated as equality.
    delta=arb(0) if t is u else t-u
    a,b,c=scalar_parts(t,weights),scalar_parts(u,weights),scalar_parts(delta,weights)
    return tuple(a[j]+b[j]-c[j] for j in range(3))


def residual_matrix(times,weights):
    d=sum(weights.values(),arb(0))-gamma_linear()
    return [[8*((t/2).sinh()*(u/2).sinh()-((t/2).cosh()-1)*((u/2).cosh()-1))-2*d*min(t,u)
             for u in times] for t in times]


def evidence():
    ctx.prec=180
    records=[]
    for N in (4,16,64,256):
        weights=event_weights(N); L=arb(N).log()
        times=[L*arb(i)/5 for i in range(1,6)]
        R=residual_matrix(times,weights)
        # Exact algebraic cancellation of the positive rank-one pole direction.
        v=[(times[1]/2).sinh(),-(times[0]/2).sinh()]+[arb(0)]*3
        ray=sum((v[i]*R[i][j]*v[j] for i in range(5) for j in range(5)),arb(0))
        assert ray<0
        for t in times:
            for u in times:
                E,r,K=kernel_parts(t,u,weights)
                assert (K-E-r).contains(0)
        records.append({'N':N,'events':len(weights),'negative_bulk_coefficient':str(2*gamma_linear()-2*sum(weights.values(),arb(0))),
                        'negative_rayleigh':str(ray),'all_25_kernel_identities_enclosed':True})
    C=carrier_channels(12, {2:sp.Rational(1,2),3:sp.Rational(2,3),4:sp.Rational(1,3),5:sp.Rational(3,5)})
    A,B=C['chiral'],C['jet']
    cross=-(A.T*B+B.T*A)
    assert cross!=sp.zeros(12)
    return {'bits':ctx.prec,'exact_carrier_dimension':12,'coherent_cross_nonzero_entries':sum(x!=0 for x in cross),
            'residual_certificates':records,
            'scope':'finite enclosure of exact analytic residual; no RH or target-PSD assertion'}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default='research/astra_round_007/evidence/square_residual.json')
    a=p.parse_args();result=evidence();Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
    print('Certified carrier-square identities and four negative residual witnesses:',a.output)
