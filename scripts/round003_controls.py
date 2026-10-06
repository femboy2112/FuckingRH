"""Retain extra hostile certificates and verify frozen Round002 evidence."""
import json
import hashlib
from pathlib import Path
from fractions import Fraction as Q
from flint import arb, ctx
from .finite_grid_lift import Event, events_for, uniform_kernel, finite_lift_certificate


def run():
    events=events_for(64)
    tower=[Event(e.location,e.prime,e.weight_denominator,20 if e.prime==3 else e.multiplier)
           for e in events]
    result={}
    for name,es in [('whole_tower_3_times20',tower),('duplicate_first',events+[events[0]])]:
        K,B=uniform_kernel(64,16,es)
        result[name]=finite_lift_certificate(K,B)
        assert Q(result[name]['lower_exact'])>0
    K,B=uniform_kernel(64,16); h=arb(64).log()/16
    mutated=[[K[i][j]-20*(i+1)*(j+1)*h*h for j in range(16)] for i in range(16)]
    result['A_minus_10t_squared']=finite_lift_certificate(mutated,B)
    assert Q(result['A_minus_10t_squared']['lower_exact'])>0
    path=Path(__file__).resolve().parents[1]/'research/astra_round_002/evidence'
    gzip_hash=hashlib.sha256((path/'pinned_tail_recovery_moments_8192.csv.gz').read_bytes()).hexdigest()
    assert gzip_hash=='f1d0f70dacd3dce8b9b2145fc06dd9258fb1499e67c900470cce75c10872ccac'
    old=json.loads((path/'pinned_tail_recovery_certificate_8192.json').read_text())
    assert arb(old['slack'])<0 and arb(old['terminal_value'])>0
    result['frozen_round002']={'q':old['q'],'slack':old['slack'],
        'positive_actual_reserve':old['terminal_value'],'gzip_sha256':gzip_hash,
        'large_sieve_rerun':False}
    return {'precision_bits':ctx.prec,'finite_controls_only':True,'controls':result}


if __name__=='__main__':
    with ctx.workprec(180):data=run()
    path=Path(__file__).resolve().parents[1]/'research/astra_round_003/evidence/hostile_certificates.json'
    path.write_text(json.dumps(data,indent=2)+'\n')
    print(f'Wrote {path}')
