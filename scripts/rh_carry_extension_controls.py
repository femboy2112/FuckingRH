#!/usr/bin/env python3
"""Classical cyclic carry-extension and gauge-sensitive local p-adic-digit tests.

Provenance: research/audits/2026-10-07/INTRINSIC_CARRY_EXTENSION_CLASS.md
Not RH, not a CI run. Requires numpy.
"""
import itertools
import math
import numpy as np


def v_p(L,p):
    a=0
    while L%p==0:
        a+=1
        L//=p
    return a


def carry(L,a,b):
    return (a+b)//L


def verify_carry_cocycle(L,p):
    for a,b,c in itertools.product(range(L),repeat=3):
        lhs=carry(L,a,b)+carry(L,(a+b)%L,c)
        rhs=carry(L,b,c)+carry(L,a,(b+c)%L)
        assert (lhs-rhs)%p==0
    if math.gcd(L,p)==1:
        inv=pow(L,-1,p)
        for a,b in itertools.product(range(L),repeat=2):
            coboundary=(inv*a+inv*b-inv*((a+b)%L))%p
            assert coboundary==carry(L,a,b)%p
    else:
        assert all(not (x%L==1 and x%p==0) for x in range(p*L))


def verify_local_padic_refinement(L,p,omega=0.5):
    power=p**v_p(L,p)
    J=np.zeros((L*p,L),dtype=complex)
    V=np.zeros_like(J)
    zeta=np.exp(2j*np.pi/p)
    for r in range(p*L):
        J[r,r%L]=1
        digit=(r%(p*power))//power
        V[r,r%L]=zeta**digit
    I=np.eye(L)
    assert np.allclose(J.conj().T@J/p,I)
    assert np.allclose(V.conj().T@V/p,I)
    assert np.allclose(J.conj().T@V/p,0,atol=1e-13)
    b=math.sqrt(1-p**(-2*omega))
    W=p**(-omega)*J+b*V
    assert np.allclose(W.conj().T@W/p,I)
    Sold=np.roll(np.eye(L),1,axis=0)
    Snew=np.roll(np.eye(p*L),1,axis=0)
    C=Snew@W-W@Sold
    expected=np.zeros_like(C)
    for r in range(p*L):
        if r%power==0:
            digit=(r%(p*power))//power
            expected[r,(r-1)%L]=b*zeta**digit*(zeta**-1-1)
    assert np.allclose(C,expected,atol=1e-12)
    s=np.linalg.svd(C,compute_uv=False)
    rank=int(np.count_nonzero(s>1e-10))
    assert rank==L//power
    assert abs(s[0]/math.sqrt(p)-2*math.sin(math.pi/p)*b)<1e-11
    return rank,float(s[0]/math.sqrt(p))



def local_isometry(L,p,omega):
    a=v_p(L,p)
    power=p**a
    zeta=np.exp(2j*np.pi/p)
    W=np.zeros((p*L,L),dtype=complex)
    for r in range(p*L):
        digit=(r%(p*power))//power
        W[r,r%L]=p**(-omega)+math.sqrt(1-p**(-2*omega))*zeta**digit
    return W


def verify_distinct_prime_flatness(L,p,q,omega):
    assert p!=q
    lhs=local_isometry(p*L,q,omega)@local_isometry(L,p,omega)
    rhs=local_isometry(q*L,p,omega)@local_isometry(L,q,omega)
    assert np.allclose(lhs,rhs,atol=2e-13)

def main():
    for L,p in [(2,3),(3,2),(4,3),(6,5),(2,2),(4,2),(6,2),(6,3),(12,2),(18,3)]:
        verify_carry_cocycle(L,p)
        rank,norm=verify_local_padic_refinement(L,p)
        print(f'L={L:2d}, p={p}: split={p and L%p!=0}, '
              f'local p-adic carry rank={rank}, norm={norm:.8f}')
    for L,p,q in [(1,2,3),(2,2,3),(3,2,3),(6,2,3),(4,2,5),(6,3,5),(12,2,3)]:
        for omega in (0.1,0.5,1.):
            verify_distinct_prime_flatness(L,p,q,omega)
        print(f'flat: L={L}, p={p}, q={q}')
    print('PASS: split iff p∤L, local p-adic isometric carry and seven exactly flat distinct-prime squares.')


if __name__=='__main__':
    main()
