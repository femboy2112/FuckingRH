"""Arb one-level certificates and critical-scale finite calibration.

No LP/SDP oracle and no zero data. Universal statements are analytic proofs.
"""
import argparse
import json
from pathlib import Path
from flint import arb, ctx
from .primitive_projection import midpoint_distances, factors


def normalized_defect(p, d, k):
    if not (p > d > 0 and k > 0):
        raise ValueError('positive level and 0<d<p required')
    return ((arb(p)/(p-d)).sqrt()**k+(arb(p)/(p+d)).sqrt()**k)/2-1


def run(limit=101):
    records=[]
    for p in range(2,limit+1):
        if factors(p)!={p:1}:continue
        ds=midpoint_distances(p)
        if not ds:
            records.append({'p':p,'feasible_level1':False,'reason':'no old cell'})
            continue
        lo=normalized_defect(p,min(ds),1)
        hi=normalized_defect(p,max(ds),1)
        if hi<1:
            feasible=False;weight=None
        elif lo<1 and hi>1:
            feasible=True;weight=(1-lo)/(hi-lo)
            assert weight>0 and weight<1
            assert (weight*hi+(1-weight)*lo).contains(1)
        else:raise ArithmeticError('ambiguous level1 feasibility')
        full=sum((normalized_defect(p,d,1) for d in range(1,p)),arb(0))/(p-1)
        kept=sum((normalized_defect(p,d,1) for d in ds),arb(0))/len(ds)
        records.append({'p':p,'radii':ds,'feasible_level1':feasible,
            'min_m1':str(lo),'max_m1':str(hi),
            'weight_on_max_radius':None if weight is None else str(weight),
            'sqrt_p_times_full_average_H1':str(full),
            'sqrt_p_times_retained_average_H1':str(kept)})
    return {'precision_bits':ctx.prec,'scope':f'prime p <= {limit}',
            'universal_sign_inferred':False,'records':records}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--limit',type=int,default=101)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    with ctx.workprec(180):result=run(args.limit)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
