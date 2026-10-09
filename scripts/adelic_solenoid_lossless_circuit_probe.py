#!/usr/bin/env python3
"""Zero-free finite checks for arithmetic-solenoid causal refinement (NOT RH)."""
from math import lcm, log
from fractions import Fraction
import numpy as np

def prime_power_factor(n):
    x=n
    factors=[]
    for p in range(2,n+1):
        if x % p == 0:
            factors.append(p)
            while x % p == 0: x //= p
    return factors[0] if len(factors)==1 else 1

def lcm_refinement_test():
    old=1
    for n in range(2,101):
        new=lcm(old,n)
        ratio=new//old
        assert ratio == prime_power_factor(n)
        if ratio>1:
            assert abs(log(new)-log(old)-log(ratio))<1e-11
        old=new
    print("PASS: all prime-power event ratios through N=100")

def p_sheet_test(L,p):
    J=np.zeros((p*L,L),float)
    for a in range(L):
        for b in range(p):
            J[a+b*L,a]=1/(p**0.5)
    assert np.allclose(J.T@J,np.eye(L))
    assert np.linalg.norm(J@J.T-np.eye(p*L))>0.1
    for a in range(L):
        g=np.zeros(p*L,complex)
        for b in range(p):
            g[a+b*L]=np.exp(2j*np.pi*b/p)/(p**0.5)
        assert np.linalg.norm(J.T@g)<1e-12
    print(f"PASS: {L} -> {p*L} half-density lift/conditional-adjoint")

def fine_history_reverse():
    roots=[Fraction(1+2*k,3) for k in range(3)]
    assert len(set(roots))==3
    assert all((3*x-1)%2==0 for x in roots)
    y6=5
    recovered=Fraction(y6,3)%2
    assert recovered==Fraction(5,3) and recovered in roots
    print("PASS: y mod2=1 has three inverse roots; y mod6=5 selects 5/3")

def product_formula():
    assert Fraction(3,2)*Fraction(2,1)*Fraction(1,3)==1
    print("PASS: q=3/2 adelic product/half-density conservation")

if __name__=="__main__":
    lcm_refinement_test()
    p_sheet_test(2,3)
    p_sheet_test(6,2)
    fine_history_reverse()
    product_formula()
    print("RH OPEN; all checks are kinematic.")
