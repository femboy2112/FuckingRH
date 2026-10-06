"""Exact/interval controls for the fixed carrier-observation obstruction."""
import json
from pathlib import Path
import sympy as sp
from flint import arb,ctx
from .event_dynamics import gamma_linear


def scalar_certificate():
    ctx.prec=180
    h=arb(1)/65536
    lower=2*gamma_linear()+(-arb(1)/2).exp()*(1/h).log()-2*h*(h/2).exp()
    assert lower>0 and arb(2).log()<1 and arb(3).log()>1+h and h<arb(2).log()
    return {'h':'1/65536','positive_weil_lower_coefficient':str(lower),
            'interval_inside_log2_log3':True,'precision_bits':ctx.prec,
            'scope':'For every nonzero smooth f supported in (1,1+h); proof uses disjoint translates.'}


def exact_zero_average_fixture():
    x=sp.Symbol('x');h=sp.Rational(1,65536)
    b=(x-1)**3*(1+h-x)**3
    f=sp.diff(b,x)
    return {'average':sp.integrate(f,(x,1,1+h)),
            'norm_square':sp.integrate(f*f,(x,1,1+h)),
            'endpoint_values':(f.subs(x,1),f.subs(x,1+h)),
            'endpoint_derivatives':(sp.diff(f,x).subs(x,1),sp.diff(f,x).subs(x,1+h))}

if __name__=='__main__':
    c=scalar_certificate();e=exact_zero_average_fixture()
    assert e['average']==0 and e['norm_square']>0
    c['polynomial_control']={k:str(v) for k,v in e.items()}
    p=Path('research/astra_round_007/evidence/observation_no_go.json')
    p.write_text(json.dumps(c,indent=2)+'\n');print('Certified positive invisible-test region:',c['positive_weil_lower_coefficient'])
