"""Independent exact event count; this certifies enumeration, not positivity."""
import argparse
import json
from pathlib import Path
from sympy import integer_nthroot, primepi


def count_events(limit):
    if limit < 2:
        return {'limit':limit,'count':0,'terms':[]}
    terms=[]
    for k in range(1,limit.bit_length()):
        root=int(integer_nthroot(limit,k)[0])
        assert root**k <= limit < (root+1)**k
        terms.append({'exponent':k,'floor_root':root,'prime_count':int(primepi(root))})
    return {'limit':limit,'count':sum(t['prime_count'] for t in terms),'terms':terms,
            'scope':'Exact prime-power enumeration only; no reserve signs computed.'}


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--limit',type=int,default=10**10)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    result=json.dumps(count_events(args.limit),indent=2)+'\n'
    if args.output:
        args.output.write_text(result)
    print(result)
