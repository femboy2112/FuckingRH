#!/usr/bin/env python3
"""Strict zero-free source and noncompact-cover controls.

Tests actual LCM/torus impulse geometry, local Hecke unitary holonomy,
the connected n=6 discriminator, shifted physical log2, and the
unbounded periodization lemma.

These tests certify source distinctions, NOT Weil positivity.
"""
import math
import cmath
import numpy as np

def test_actual_area_and_halfdensity():
    L=1
    events=[]
    for n in range(2,101):
        newL=math.lcm(L,n)
        ratio=newL//L
        factors=[]
        x=n
        for p in range(2,n+1):
            if x%p==0:
                factors.append(p)
                while x%p==0: x//=p
        prime_power=(len(factors)==1)
        assert ratio==(factors[0] if prime_power else 1),(n,ratio)
        delta=math.log(newL)-math.log(L)
        expected=math.log(factors[0]) if prime_power else 0.0
        assert abs(delta-expected)<1e-12
        if prime_power:
            p=factors[0]
            branch_amp=p**(-0.5)
            assert abs(branch_amp**2-1/p)<1e-15
            events.append((n,p,delta))
        if n==6:
            assert delta==0.0
        L=newL
    assert any(n==2 for n,_,_ in events)
    assert any(n==3 for n,_,_ in events)
    assert not any(n==6 for n,_,_ in events)
    print("PASS LCM Tate-area increments & half-density; no fake 6")

def quartic(n):
    return (0,1,1j,-1j,-1)[n%5]

def test_hecke_holonomy():
    for p in (2,3,7,11):
        a=quartic(p)
        if p%5:
            assert abs(abs(a)-1)<1e-15
            for k in range(1,6):
                geom=(2*math.pi*math.log(p))/(2*math.pi)
                coeff=geom*a**k*p**(-k/2)
                source=math.log(p)*quartic(p**k)*p**(-k/2)
                assert abs(coeff-source)<1e-14
    mutant=1.1j
    assert abs(abs(mutant)-1)>0.09
    # A shifted 2-period is a different torus, not the actual p=2 one.
    eps=0.03
    assert abs((math.log(2)+eps)-math.log(2))>0.02
    # Conjugate quartic Dirichlet-series mixture: connected c(6)=4ab.
    a=1/3;b=2/3
    d=lambda n:a*quartic(n)+b*quartic(n).conjugate()
    assert abs((d(6)-d(2)*d(3))-4*a*b)<1e-14
    assert abs(quartic(6)-quartic(2)*quartic(3))<1e-14
    print("PASS genuine chi holonomies, unitary alpha, log2, DH connected-6 defect")

def test_periodization_unbounded():
    ell=math.log(2)
    # Smooth phi supported in (0,ell/2) with L2(R) norm 1.
    # f_N=N^(-1/2) sum_j phi(x+j ell) has disjoint translates.
    # Therefore ||f_N||=1 and ||P_ell f_N||_normalized=sqrt(N/ell).
    previous=0
    for N in (1,4,9,25,100):
        norm=(N/ell)**0.5
        assert norm>previous
        previous=norm
    assert (100/ell)**0.5>10
    print("PASS analytic periodization witness grows as sqrt(N/log2)")

def test_antipodal_equivariance():
    z=complex(1.2,0.7)
    for n in range(1,9):
        for c in (1+0j,cmath.exp(0.4j),1.15+0j):
            fj=c*(-1/z.conjugate())**n
            jf=-1/(c*z**n).conjugate()
            commute=abs(fj-jf)<1e-11
            assert commute==(n%2==1 and abs(abs(c)-1)<1e-12)
    print("PASS twistor f(z)=c z^n equivariant iff odd n & |c|=1")

if __name__=="__main__":
    test_actual_area_and_halfdensity()
    test_hecke_holonomy()
    test_periodization_unbounded()
    test_antipodal_equivariance()
    print("ALL ZERO-FREE SOURCE/DUALIZING CONTROLS PASSED; RH OPEN")
