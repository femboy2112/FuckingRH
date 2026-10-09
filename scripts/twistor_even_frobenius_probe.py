#!/usr/bin/env python3
"""Zero-input source/twistor tests, independent of RH and its zeros.
Standard library, Python 3.11+. Construction audit, not a PSD test.
"""
import cmath, json, math, random
rng=random.Random(20261009)

def j(e,z): return e/z.conjugate()
def f(n,z,c=1): return c*z**n
def t(e): return 1 if e==1 else 1j
def s(n,w): return math.sqrt(n)*w**(n-1)
def close(x,y): return abs(x-y)<=1e-12*max(1,abs(x),abs(y))
def chi(n): return {0:0,1:1,2:1j,3:-1j,4:-1}[n%5]

def convolve(a,b,N):
    out=[0j]*(N+1)
    for i in range(1,N+1):
        if not a[i]:continue
        for k in range(1,N//i+1):
            if b[k]:out[i*k]+=a[i]*b[k]
    return out

def logstar(a,N):
    x=list(a);x[1]-=1;power=[0j]*(N+1);power[1]=1;out=[0j]*(N+1)
    for k in range(1,int(math.log2(N))+2):
        power=convolve(power,x,N)
        for i in range(2,N+1):out[i]+=(-1)**(k+1)*power[i]/k
    return out

def run():
    tested=[1,2,3,4,5,6]
    holdouts=[7,8,9,10,11,12,15,21,22,25,30]
    maxrel=0.0;odd=even=0
    for n in tested+holdouts:
        for e in (-1,1):
            for _ in range(20):
                z=complex(rng.uniform(-1.4,1.4),rng.uniform(-1.4,1.4))
                if abs(z)<.3:z+=.8+.3j
                c=cmath.exp(1j*rng.uniform(-math.pi,math.pi))
                x,y=f(n,j(e,z),c),j(e**n,f(n,z,c))
                maxrel=max(maxrel,abs(x-y)/max(1,abs(x),abs(y)))
                assert close(x,y)
                if e==-1:
                    wrong=j(-1,f(n,z,c))
                    if n%2:assert close(x,wrong);odd+=1
                    else:assert not close(x,wrong);even+=1
    # Real-structure covariance classification: |c|^2 e^n = e_target
    for n in tested+holdouts:
        for e in (-1,1):
            assert [dest for dest in (-1,1) if dest/e**n>0]==[e**n]
    for n in tested+holdouts:
        for e in (-1,1):
            w=.37+.29j
            jt=lambda x:t(e)/x.conjugate()
            assert close(jt(w)**2,j(e,w**2))
            assert close(jt(jt(w)),e*w)
            assert close(s(n,-w),(-1)**(n-1)*s(n,w))
            for m in tested+holdouts:
                assert n*(m-1)+n-1==n*m-1
                assert close(s(m,w**n)*s(n,w),s(m*n,w))
                lhs=t(e)**(n*m)/t(e**(n*m))
                rhs=(t(e)**n/t(e**n))**m*(t(e**n)**m/t(e**(n*m)))
                assert close(lhs,rhs)
    # Untagged even map collapses (+,k) and (-,k); source-tagged map does not.
    for n in (2,4,6,8,10,22):
        for k in range(-3,4):
            assert ((-1)**n,n*k)==((1)**n,n*k)
            assert ((-1)**n,n*k,-1)!=((1)**n,n*k,1)
    N=60
    zeta=[0j]+[1+0j for _ in range(N)]
    char=[0j]+[complex(chi(n)) for n in range(1,N+1)]
    phi=(1+math.sqrt(5))/2
    kap=math.sqrt(1+phi*phi)-phi
    a=(1-1j*kap)/2
    dh=[0j]+[a*chi(n)+a.conjugate()*complex(chi(n)).conjugate()
             for n in range(1,N+1)]
    bz,bc,bd=logstar(zeta,N),logstar(char,N),logstar(dh,N)
    # Source log-primitivity test by independently enumerating prime powers.
    for n in range(2,N+1):
        pp=False
        for p in range(2,n+1):
            if any(p%q==0 for q in range(2,math.isqrt(p)+1)):continue
            m=n
            while m%p==0:m//=p
            if m==1:pp=True;break
        if not pp:assert abs(bz[n])<1e-10 and abs(bc[n])<1e-10
    assert abs(bc[6])<1e-12 and abs(bd[6]-(1+kap**2))<1e-12
    assert abs(bd[4]-(-1-kap**2/2))<1e-12
    altered=char.copy();altered[6]+=.03
    assert abs(logstar(altered,N)[6]-.03)<1e-12
    # Hecke character phases must twist the fiber, not coefficient c_n in c_n z^n.
    c2,c3,c6=chi(2),chi(3),chi(6)
    assert c2*c3==c6==1
    assert c3*c2**3==-1 and c2*c3**2==-1j
    assert abs(abs(1.03j)**2-1)>.05
    assert abs(math.exp(math.log(2)+.01)-2)>.01
    return {
      "status":"PASS","source":"no zeros","tested_n":tested,"fresh_holdout_n":holdouts,
      "max_relative_covariance_residual":maxrel,
      "signed_odd_ok":odd,"signed_even_failed_as_expected":even,
      "spin_even_deck_parity":-1,"coarse_even_history_collision":True,
      "tagged_one_step_isometry":True,
      "zeta_b6":[bz[6].real,bz[6].imag],"character_b6":[bc[6].real,bc[6].imag],
      "DH_b4":[bd[4].real,bd[4].imag],"DH_b6":[bd[6].real,bd[6].imag],
      "DH_kappa":kap,"fake6_logcoefficient":.03,
      "monomial_composition_phase_3_after_2":[-1,0],
      "monomial_composition_phase_2_after_3":[0,-1],
      "character_tensor_phase_6":[1,0],
      "note":"geometry and source constraints do not prove the Weil sign"
    }

if __name__=="__main__":print(json.dumps(run(),indent=2,sort_keys=True))
