#!/usr/bin/env python3
"""Finite normalized-Haar prime-digit actualization and SUCC carry tests.

Provenance: research/audits/2026-10-07/FRESH_DIGIT_ISOMETRIC_ACTUALIZATION.md
No RH proof, no zero data, and no CI attestation. Requires numpy.
"""
import numpy as np
import math


def matrices(L, p, omega):
    J=np.zeros((p*L,L),dtype=complex)
    V=np.zeros_like(J)
    zeta=np.exp(2j*np.pi/p)
    for k in range(p):
        for r0 in range(L):
            J[r0+k*L,r0]=1
            V[r0+k*L,r0]=zeta**k
    a=p**(-omega)
    b=math.sqrt(1-p**(-2*omega))
    W=a*J+b*V
    So=np.zeros((L,L),dtype=complex)
    Sn=np.zeros((p*L,p*L),dtype=complex)
    for r in range(L): So[r,(r-1)%L]=1
    for r in range(p*L): Sn[r,(r-1)%(p*L)]=1
    return J,V,W,So,Sn


def verify(L,p,omega):
    J,V,W,So,Sn=matrices(L,p,omega)
    # Haar weighted adjoint: domain metric I/L, codomain metric I/(pL).
    adj=lambda A:A.conj().T/p
    eye=np.eye(L)
    assert np.allclose(adj(J)@J,eye,atol=1e-13)
    assert np.allclose(adj(V)@V,eye,atol=1e-13)
    assert np.allclose(adj(J)@V,0,atol=1e-13)
    assert np.allclose(adj(W)@W,eye,atol=1e-13)
    assert np.allclose(Sn@J,J@So,atol=1e-13)
    C=Sn@W-W@So
    wanted=np.zeros_like(C)
    zeta=np.exp(2j*np.pi/p)
    for k in range(p):
        wanted[k*L,L-1]=math.sqrt(1-p**(-2*omega))*zeta**k*(zeta**-1-1)
    assert np.allclose(C,wanted,atol=1e-12)
    singular=np.linalg.svd(C,compute_uv=False)
    norm=float(singular[0]/math.sqrt(p))
    expected=2*math.sin(math.pi/p)*math.sqrt(1-p**(-2*omega))
    assert abs(norm-expected)<1e-12
    if omega>0:
        assert np.count_nonzero(singular>1e-11)==1
    return norm


def main():
    for L,p in [(2,2),(4,2),(6,2),(3,3),(4,3),(6,3),(3,5),(6,5)]:
        assert verify(L,p,0)==0
        for omega in [0.1,0.5,1.0]:
            norm=verify(L,p,omega)
        print(f'L={L:2d}, p={p}: isometry, orthogonal innovation and rank-one SUCC carry; omega=1 norm={norm:.9f}')
    print('PASS: all finite fresh-digit causal isometries and exact carry identities; RH OPEN.')


if __name__=='__main__':
    main()
