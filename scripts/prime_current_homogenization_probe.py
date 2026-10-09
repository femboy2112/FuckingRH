#!/usr/bin/env python3
"""Prime-current homogenization and counterexample controls.

No zeros are calculated/read. Uses numpy>=2.3, mpmath>=1.3.
Outputs numerical observations, NOT infinite proofs or rigorous intervals.
"""
import json
import math
import numpy as np
import mpmath as mp

def arithmetic_current(limit=2_000_000):
    # Sieve actual prime-power von Mangoldt weights.
    is_prime=np.ones(limit+1,dtype=bool)
    is_prime[:2]=False
    for p in range(2, math.isqrt(limit)+1):
        if is_prime[p]:is_prime[p*p::p]=False
    lamb=np.zeros(limit+1, dtype=float)
    for p in np.flatnonzero(is_prime):
        n=int(p)
        while n<=limit:
            lamb[n]=math.log(p)
            n*=int(p)
    assert lamb[6]==0 and abs(lamb[4]-math.log(2))<1e-14
    ns=np.maximum(np.arange(limit+1),1)
    w=lamb/np.sqrt(ns)
    j=np.cumsum(w)
    energy=np.cumsum(w*w)
    fake_all=1/np.sqrt(ns)
    fake_all[0]=0
    fake_all_cumulative=np.cumsum(fake_all)
    rows=[]
    for x in [100,1000,10000,100000,1000000,2000000]:
        t=math.log(x)
        bulk=2*(math.sqrt(x)-1)
        rows.append({
            "x":x,
            "J":float(j[x]),
            "continuum_integral":bulk,
            "discrepancy":float(j[x]-bulk),
            "J_over_sqrt_x":float(j[x]/math.sqrt(x)),
            "Bohr_energy":float(energy[x]),
            "Bohr_rms_over_log_x":float(math.sqrt(energy[x])/t),
            "fake_all_integer_discrepancy":float(fake_all_cumulative[x]-bulk),
            "fake_impulse_6_delta03_discrepancy":float(j[x]-bulk+.03/math.sqrt(6))
        })
    windows=[]
    for x in [1000,10000,100000,500000]:
        for ratio in [1.25,1.5,2.0]:
            hi=int(x*ratio)
            if hi>limit:continue
            seen=float((j[hi]-j[x])/math.sqrt(x))
            model=2*(math.sqrt(ratio)-1)
            windows.append({"x":x,"ratio":ratio,"observed":seen,"PNT_prediction":model,"error":seen-model})
    return {"limit":limit,"rows":rows,"windows":windows,"source_controls":{
        "Lambda_6":float(lamb[6]),"Lambda_4":float(lamb[4]),"Lambda_8":float(lamb[8]),
        "Lambda_9":float(lamb[9]),"primes_through_limit":int(is_prime.sum())}}

def completion_probe():
    mp.mp.dps=45
    q=mp.mpf(1)/4
    b=(mp.digamma(q)-mp.log(mp.pi))/2
    C=mp.zeta(2,q)
    def G(t):
        t=mp.mpf(t)
        return (C-mp.exp(-t/2)*mp.lerchphi(mp.exp(-2*t),2,q))/4
    def A(t):
        t=mp.mpf(t)
        return 4*(mp.exp(t/2)+mp.exp(-t/2)-2)+b*t+G(t)
    def smooth(t):
        t=mp.mpf(t)
        return A(t)-4*(mp.exp(t/2)-1)+2*t
    # Independent prime-power list, separate from numerical sieve above.
    def lam(n):
        fac=[]
        r=n
        for p in range(2,math.isqrt(n)+1):
            if r%p==0:
                while r%p==0:
                    r//=p
                    fac.append(p)
        if r>1:fac.append(r)
        return mp.log(fac[0]) if fac and len(set(fac))==1 else mp.mpf(0)
    def exact_psi(t):
        t=mp.mpf(t)
        return A(t)-sum(lam(n)/mp.sqrt(n)*(t-mp.log(n))
                         for n in range(2,int(mp.exp(t))+1) if lam(n)>0)
    rows=[]
    for t in [".2",".5","1","2","3","4","6","8"]:
        true=exact_psi(t)
        continuum=smooth(t)
        rows.append({"t":float(t),"genuine_psi":float(true),
                     "homogenized_psi":float(continuum),"difference":float(true-continuum)})
    # Analytic upper bound for t>=3:
    # G(t) <= C/4; c=b+2<0; 4(exp(-t/2)-1)+ct+C/4 decreases.
    bound3=4*(mp.exp(-mp.mpf(3)/2)-1)+3*(b+2)+C/4
    assert bound3<0 and b+2<0
    return {"b":float(b),"linear_drift_b_plus_2":float(b+2),
            "G_infty_upper_C_over_4":float(C/4),
            "upper_bound_at_3_for_all_t_ge_3":float(bound3),"rows":rows,
            "status":"homogenized completion is provably negative for t>=3"}

if __name__=="__main__":
    print(json.dumps({"arithmetic":arithmetic_current(),
                      "completion":completion_probe(),
                      "claim":"finite tests only; analytic sign failure proved in research note"},
                     indent=2,sort_keys=True))
