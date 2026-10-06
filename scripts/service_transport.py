"""Round002 certified service-clock/order probes; no zero data.

Universal statements are proved in research/astra_round_002/. Arb bounds
certify the finite counterexamples; undecidable ball comparisons raise.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from flint import arb, ctx
try:
    from .event_dynamics import arch, arch_prime, curvature
    from .suzuki_psi import prime_power_events_up_to
except ImportError:
    from event_dynamics import arch, arch_prime, curvature
    from suzuki_psi import prime_power_events_up_to


def constants():
    a = arb(2).log()
    sigma, c, A = arch_prime(a), curvature(a), arch(a)
    return a, sigma, c, A, A-sigma*sigma/(2*c)


def choose_max(x, y):
    if x >= y: return x
    if y >= x: return y
    return x.max(y)


def positive(x):
    return choose_max(arb(0), x)


def inverse(s, bits=110):
    """Restricted inverse tau(s), rigorous for non-boundary input balls."""
    s = arb(s)
    a, sigma, *_ = constants()
    if s <= sigma: return a
    if not s > sigma: raise ArithmeticError('ambiguous inverse branch')
    lo, hi = a.lower(), arb(2)
    while not arch_prime(hi) > s: hi *= 2
    for _ in range(bits+60):
        mid = ((lo+hi)/2).mid()
        d = arch_prime(mid)-s
        if d < 0: lo = mid
        elif d > 0: hi = mid
        else: break
        if hi-lo < arb(2)**(-bits): break
    return lo.union(hi)


def primitive(s):
    """Integral_0^s tau(b) db = restricted A*(s)+A(a0)."""
    s = arb(s)
    a, sig, c, A, K = constants()
    if s <= sig: return a*s
    t = inverse(s)
    return s*t-arch(t)+A


def bar_primitive(s):
    s = arb(s)
    a,sig,c,A,K = constants()
    if s <= sig: return a*s+(s*s/2-sig*s)/c
    if not s > sig: raise ArithmeticError('ambiguous extension branch')
    return primitive(s)-sig*sig/(2*c)


def bar_inverse(s):
    s = arb(s)
    a,sig,c,*_ = constants()
    if s <= sig: return a+(s-sig)/c
    return inverse(s)


def states(limit):
    out=[]
    s=h=m=arb(0)
    for e in prime_power_events_up_to(limit):
        a=arb(e.n).log(); w=arb(e.prime).log()/arb(e.n).sqrt()
        sig=arch_prime(a)
        s+=w; h+=w*a; m+=w*sig
        out.append(dict(q=e.n,a=a,w=w,sigma=sig,S=s,H=h,N=m))
    return out


def call_uniform(k, S):
    # Unnormalized mass S on [0,S].
    if k is S: return arb(0)
    if k <= 0: return S*S/2-S*k
    if k >= S: return arb(0)
    if not (k > 0 and k < S): raise ArithmeticError('ambiguous call branch')
    return (S-k)**2/2


def call_prime(k, records):
    return sum((r['w']*positive(r['sigma']-k) for r in records),arb(0))


def call_difference_extrema(records):
    """D(k)=int(z-k)+ d(prime-flat). Candidates exhaust all real k.

    Between nodes D is concave quadratic on [0,S], affine outside.
    Critical points occur at k=mass of atoms <=k. Include all such mass
    values; extra candidate evaluations cannot alter global extrema.
    """
    S=records[-1]['S']
    ks=[arb(0),S]+[r['sigma'] for r in records]+[r['S'] for r in records]
    vals=[(k,call_prime(k,records)-call_uniform(k,S)) for k in ks]
    lo=hi=vals[0][1]
    for _,v in vals[1:]: lo=lo.min(v); hi=hi.max(v)
    return lo,hi,vals


def defects(records, shifted=False):
    """Independent OT costs; formulas proved in companion document."""
    a,sig,c,A,K=constants()
    D=arb(0); credit=arb(0); prev=arb(0); eps=arb(0)
    for r in records:
        S,z,loc=r['S'],r['sigma'],r['a']
        # Integral on [prev,S] of (tau(b)-T(z))_+.
        if S <= z: debit=arb(0)
        else:
            if prev >= z:
                lower=prev; prim_lower=primitive(prev)
            elif z > prev:
                lower=z; prim_lower=z*loc-arch(loc)+A
            else:
                raise ArithmeticError('ambiguous cost split')
            debit=primitive(S)-prim_lower-loc*(S-lower)
        D+=debit
        # Signed increment determines opposite one-sided cost.
        signed=r['w']*loc-(primitive(S)-primitive(prev))
        credit+=signed+debit
        eps=choose_max(eps,S/2-r['N']/S)
        prev=S
    result={'one_sided_cost':D,'credit':credit,'winfty_icv_defect':eps,
            'lipschitz_repair_cost':prev*eps/c,
            'reserve':A+credit-D,'A0':A,'K0':K}
    if shifted:
        result['exact_shift_cost']=sum((r['w']*(inverse(r['sigma']+eps)-r['a']) for r in records),arb(0))
    return result


def run(limit=101, shifted=False):
    rows=[]; all_states=states(limit)
    for j,r in enumerate(all_states):
        block=all_states[:j+1]
        low,high,_=call_difference_extrema(block)
        # PutY-PutX = CallY-CallX - (N-S^2/2).
        dm=r['N']-r['S']**2/2
        data={**r,**defects(block,shifted=shifted), 'call_min':low,'call_max':high,
              'put_min':low-dm,'put_max':high-dm,'mean_mass_defect':dm}
        rows.append({k:(v if k=='q' else str(v)) for k,v in data.items()})
    return {'precision_bits':ctx.prec,'scope':f'actual prefixes q <= {limit}',
            'infinite_claim':False,'records':rows}


def main():
    p=argparse.ArgumentParser();p.add_argument('--limit',type=int,default=101)
    p.add_argument('--shifted',action='store_true');p.add_argument('--output',type=Path)
    args=p.parse_args()
    with ctx.workprec(200): data=run(args.limit,args.shifted)
    text=json.dumps(data,indent=2)+'\n'
    if args.output: args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(text)
    else: print(text)

if __name__=='__main__': main()
