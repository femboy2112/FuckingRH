#!/usr/bin/env python3
"""Finite proof controls for causal arithmetic SUCC information filtrations.

Source/provenance: research/audits/2026-10-07/CAUSAL_FILTRATION_INFORMATION_ENERGY.md.
Uses true prime powers, not zeta zero ordinates. Requires numpy.
"""
from __future__ import annotations
import math
import numpy as np


def prime_power_weights(X: int) -> dict[int, float]:
    flags=[True]*(X+1)
    flags[:2]=[False,False]
    for p in range(2,math.isqrt(X)+1):
        if flags[p]:
            for n in range(p*p,X+1,p): flags[n]=False
    result={}
    for p in range(2,X+1):
        if flags[p]:
            q=p
            while q<=X:
                result[q]=math.log(p)/math.sqrt(q)
                q*=p
    return result


def check_lcm_event_weights():
    L=1
    true=prime_power_weights(250)
    for n in range(2,251):
        Lnext=math.lcm(L,n)
        delta=math.log(Lnext//L)/math.sqrt(n)
        target=true.get(n,0.)
        assert math.isclose(delta,target,rel_tol=2e-14,abs_tol=2e-14),(n,delta,target)
        L=Lnext
    print('PASS: lcm increment is von Mangoldt using only past L and current n (n<=250)')


def check_haar_information():
    f2=np.array([2.,0.]);g4=np.array([3.,0.,1.,0.])
    J=np.array([[1.,0.],[0.,1.],[1.,0.],[0.,1.]])
    Jstar=J.T/2.;Q=J@Jstar
    assert np.array_equal(Jstar@J,np.eye(2))
    assert np.array_equal(Jstar@g4,f2)
    new=float(g4@g4/4)
    old=float(f2@f2/2)
    innovation=float(((np.eye(4)-Q)@g4)@((np.eye(4)-Q)@g4)/4)
    assert math.isclose(new,old+innovation,abs_tol=1e-14)
    S4=np.roll(np.eye(4),1,axis=0)
    assert np.array_equal(S4@Q,Q@S4)
    print(f'PASS: Haar energy old={old}, innovation={innovation}, new={new}; cyclic SUCC projection flat')


def check_prefix_births():
    N=40
    S=np.zeros((N,N))
    for k in range(N-1): S[k+1,k]=1
    for q in (2,3,4,5,7,8,9,11,13,16,17,19,23,25):
        P=np.diag([1.]*(q-1)+[0.]*(N-q+1))
        comm=S@P-P@S
        expected=np.zeros_like(S)
        expected[q-1,q-2]=1.
        assert np.array_equal(comm,expected)
    print('PASS: 14 encountered-event commutators equal the rank-one next-state birth')


def check_bounded_source_and_unbounded_readout():
    for X in (16,100,1000,10000):
        w=prime_power_weights(X)
        norm2=max(w.values());total=sum(w.values())
        assert norm2<=2/math.e+1e-14
        if X<=100:
            D=np.zeros((X+2,X+2))
            for q,wq in w.items():D[q-1,q-2]=math.sqrt(wq)
            assert math.isclose(np.linalg.norm(D,2)**2,norm2,abs_tol=1e-12)
            assert np.allclose(D@D.T,np.diag(np.diag(D@D.T)),atol=1e-12)
        print(f'X={X:5d}: bounded_source_norm²={norm2:.8f}, coherent_readout_at_zero={total:.8f}')
    print('PASS: event injection bounded independently of event horizon; coherent readout not')


def check_adaptation_not_contraction():
    state=1.
    for _ in range(12):state*=2
    assert state==4096.
    print('PASS: no-future-data adapted doubling still amplifies to 4096 in 12 steps')


def main():
    check_lcm_event_weights()
    check_haar_information()
    check_prefix_births()
    check_bounded_source_and_unbounded_readout()
    check_adaptation_not_contraction()
    print('ALL 5 CAUSAL-FILTRATION CONTROLS PASS. RH OPEN.')

if __name__=='__main__':main()
