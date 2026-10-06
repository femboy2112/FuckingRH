"""Certified finite Brownian lift probes; no inference beyond the sampled grid.

NumPy proposes an eigenvector/shift. Arb LDL and rational Rayleigh quotients
certify the two endpoints. Event activation is exact integer arithmetic.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
from pathlib import Path
import random
import numpy as np
from flint import arb, ctx
from .event_dynamics import arch
from .suzuki_psi import prime_power_events_up_to, primes_up_to

@dataclass(frozen=True)
class Event:
    location: int
    prime: int
    weight_denominator: int
    multiplier: int = 1

    def weight(self):
        return self.multiplier*arb(self.prime).log()/arb(self.weight_denominator).sqrt()


def events_for(N, model='actual', seed=20261006):
    ev=[Event(e.n,e.prime,e.n) for e in prime_power_events_up_to(N)]
    if model=='actual': return ev
    if model=='increase_first': return [Event(2,2,2,20)]+ev[1:]
    if model=='delete_first': return ev[1:]
    if model=='relocate_first': return [Event(3,2,2)]+ev[1:]
    rng=random.Random(seed)
    if model=='shuffled':
        locations=[e.location for e in ev]; rng.shuffle(locations)
        return [Event(a,e.prime,e.weight_denominator) for a,e in zip(locations,ev)]
    if model=='random_sparse': return [e for e in ev if rng.randrange(2)]
    if model=='composite_only':
        primes=set(primes_up_to(N))
        return [Event(n,n,n) for n in range(4,N+1) if n not in primes]
    raise ValueError('unknown event model')


def psi_uniform_values(N,m,events=None):
    """Enclose Psi(k log(N)/m), k=0..m, using exact event predicates."""
    if N<2 or m<1: raise ValueError('N>=2, m>=1 required')
    events=events_for(N) if events is None else list(events)
    step=arb(N).log()/m
    weighted=[(e,e.weight(),arb(e.location).log(),e.location**m) for e in events]
    values=[arb(0)]
    for k in range(1,m+1):
        t=k*step
        value=arch(t)
        cutoff=N**k
        for e,w,a,power in weighted:
            if power<cutoff: value-=w*(t-a)
            # Equality contributes exactly zero, so no rounded subtraction.
        values.append(value)
    return values,step


def uniform_kernel(N,m,events=None):
    values,step=psi_uniform_values(N,m,events)
    K=[[values[i]+values[j]-values[abs(i-j)] for j in range(1,m+1)] for i in range(1,m+1)]
    B=[[2*min(i,j)*step for j in range(1,m+1)] for i in range(1,m+1)]
    return K,B


def canonical_times(times):
    """Exact rational inputs: zero rows removed and duplicates quotiented."""
    ts=[Fraction(t) for t in times]
    if any(t<0 for t in ts): raise ValueError('nonnegative times required')
    unique=sorted(set(ts)-{Fraction(0)})
    index={t:i for i,t in enumerate(unique)}
    return unique,[None if t==0 else index[t] for t in ts]


def ldlt_positive(matrix):
    """Return certified positive pivots, or None; ambiguity is not negativity."""
    n=len(matrix)
    L=[[arb(0) for _ in range(n)] for _ in range(n)]
    d=[]
    for i in range(n):
        pivot=matrix[i][i]-sum((L[i][k]**2*d[k] for k in range(i)),arb(0))
        if not pivot>0: return None
        d.append(pivot); L[i][i]=arb(1)
        for j in range(i+1,n):
            L[j][i]=(matrix[j][i]-sum((L[j][k]*L[i][k]*d[k] for k in range(i)),arb(0)))/pivot
    return d


def quadratic(matrix,vector):
    return sum((arb(str(vector[i].numerator))/vector[i].denominator*matrix[i][j]*arb(str(vector[j].numerator))/vector[j].denominator for i in range(len(vector)) for j in range(len(vector))),arb(0))


def exact_endpoint(value):
    mantissa,exponent=value.man_exp()
    return Fraction(int(mantissa))*Fraction(2)**int(exponent)


def finite_lift_certificate(K,B):
    """Bracket inf{c>=0: K+cB PSD}, for positive definite B."""
    if ldlt_positive(B) is None: raise ValueError('B not certified positive definite')
    km=np.array([[float(v.mid()) for v in row] for row in K]); bm=np.array([[float(v.mid()) for v in row] for row in B])
    chol=np.linalg.cholesky(bm)
    inverse=np.linalg.inv(chol)
    eigenvalues,eigenvectors=np.linalg.eigh(inverse@km@inverse.T)
    estimate=max(0.,-float(eigenvalues[0]))
    pivots=ldlt_positive(K)
    if pivots is not None:
        return {'status':'certified_zero_lift','lower':'0','upper':'0','lower_exact':'0','upper_exact':'0','numpy_candidate':estimate,'minimum_ldl_pivot':str(min(pivots,key=lambda z:float(z.mid()))),'finite_grid_only':True}
    vector=np.linalg.solve(chol.T,eigenvectors[:,0]); vector/=np.max(np.abs(vector))
    rational=[Fraction(float(x)).limit_denominator(10**8) for x in vector]
    denominator=quadratic(B,rational)
    if not denominator>0: raise ArithmeticError('Rayleigh denominator not positive')
    rayleigh=-quadratic(K,rational)/denominator
    upper=Fraction(str(max(estimate*(1+1e-7),estimate+1e-9)))
    for _ in range(30):
        ball=arb(upper.numerator)/upper.denominator
        shifted=[[K[i][j]+ball*B[i][j] for j in range(len(K))] for i in range(len(K))]
        pivots=ldlt_positive(shifted)
        if pivots is not None: break
        upper=upper*2+Fraction(1,10**9)
    else: raise ArithmeticError('could not certify lift upper bound')
    return {'status':'certified_positive_lift' if rayleigh>0 else 'bracket_includes_zero','lower':str(rayleigh.lower()) if rayleigh>0 else '0','upper':str(ball),'lower_exact':str(exact_endpoint(rayleigh.lower())) if rayleigh>0 else '0','upper_exact':str(upper),'rayleigh_enclosure':str(rayleigh),'rational_witness':[str(v) for v in rational],'numpy_candidate':estimate,'minimum_shifted_ldl_pivot':str(min(pivots,key=lambda z:float(z.mid()))),'finite_grid_only':True}


def exact_null_reduction(K,B):
    """Rational semidefinite-B feasibility, returning a reduced SPD-B pencil.

    A negative null quadratic or coupling into a null direction of the
    null-block makes every finite Brownian lift impossible. Positive null
    pivots are removed by an exact Schur complement.
    """
    K=[[Fraction(v) for v in row] for row in K]; B=[[Fraction(v) for v in row] for row in B]
    n=len(K)
    if len(B)!=n or any(len(row)!=n for row in K+B): raise ValueError('square matrices required')
    if any(K[i][j]!=K[j][i] or B[i][j]!=B[j][i] for i in range(n) for j in range(n)): raise ValueError('symmetric matrices required')
    def swap(M,i,j):
        M[i],M[j]=M[j],M[i]
        for row in M: row[i],row[j]=row[j],row[i]
    def shear(M,p,j,f):
        oldrow=M[p][:]; oldjj=M[j][j]; oldpj=M[p][j]
        for i in range(n):
            if i!=j: M[i][j]=M[j][i]=M[i][j]-f*oldrow[i]
        M[j][j]=oldjj-2*f*oldpj+f*f*oldrow[p]
    r=0
    while r<n:
        if any(B[i][i]<0 for i in range(r,n)): raise ValueError('B is not PSD')
        p=next((i for i in range(r,n) if B[i][i]>0),None)
        if p is None:
            if any(B[i][j] for i in range(r,n) for j in range(r,n)): raise ValueError('B is not PSD')
            break
        swap(K,r,p); swap(B,r,p)
        for j in range(r+1,n):
            f=B[r][j]/B[r][r]
            shear(K,r,j,f); shear(B,r,j,f)
        r+=1
    null=list(range(r,n))
    while null:
        if any(K[i][i]<0 for i in null): return {'feasible':False,'reason':'negative null-block quadratic'}
        p=next((i for i in null if K[i][i]>0),None)
        if p is None:
            if any(K[i][j] for i in null for j in null): return {'feasible':False,'reason':'indefinite null block'}
            if any(K[i][j] for i in null for j in range(r)): return {'feasible':False,'reason':'incompatible null-to-range coupling'}
            break
        for j in list(range(r))+[i for i in null if i!=p]:
            shear(K,p,j,K[p][j]/K[p][p])
        null.remove(p)
    return {'feasible':True,'rank_B':r,'K_reduced':[[K[i][j] for j in range(r)] for i in range(r)],'B_reduced':[[B[i][j] for j in range(r)] for i in range(r)]}


def finite_lift_rational(K,B):
    """Exact rational null reduction followed by certified finite lift bracket."""
    reduced=exact_null_reduction(K,B)
    if not reduced['feasible']:
        return {'status':'no_finite_lift','reason':reduced['reason']}
    if reduced['rank_B']==0:
        return {'status':'certified_zero_lift','lower_exact':'0','upper_exact':'0'}
    def convert(M):
        return [[arb(v.numerator)/v.denominator for v in row] for row in M]
    return finite_lift_certificate(convert(reduced['K_reduced']),convert(reduced['B_reduced']))


def run():
    records=[]
    for N in (16,64,256,1024):
        for m in (8,16,32):
            K,B=uniform_kernel(N,m)
            records.append({'N':N,'m':m,'model':'actual',**finite_lift_certificate(K,B)})
    for model in ('increase_first','delete_first','relocate_first','shuffled','random_sparse','composite_only'):
        K,B=uniform_kernel(64,16,events_for(64,model))
        records.append({'N':64,'m':16,'model':model,**finite_lift_certificate(K,B)})
    K,B=uniform_kernel(4096,32)
    records.append({'N':4096,'m':32,'model':'actual_holdout',**finite_lift_certificate(K,B)})
    # An event strictly beyond the largest sampled time is invisible here.
    base=events_for(64); planted=base+[Event(65,2,2,10**8)]
    x,step=psi_uniform_values(64,16,base); y,_=psi_uniform_values(64,16,planted)
    assert all(a.overlaps(b) for a,b in zip(x,y))
    future,_=psi_uniform_values(128,1,planted)
    assert future[-1]<0
    return {'precision_bits':ctx.prec,'numpy_version':np.__version__,'random_seed':20261006,'normalization':'K_ij=Psi(t_i)+Psi(t_j)-Psi(t_i-t_j), B_ij=2 min(t_i,t_j)','grid':'t_i=i log(N)/m, i=1..m; zero removed','certificates':records,'planted_tail':{'event_location':65,'sample_N':64,'new_event_multiplier':10**8,'unchanged_on_grid_by_exact_support':True,'Psi_log128':str(future[-1])},'universal_claim':False}

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--output',type=Path,required=True); args=parser.parse_args()
    with ctx.workprec(180): result=run()
    args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Wrote {len(result["certificates"])} finite-grid certificates to {args.output}')
