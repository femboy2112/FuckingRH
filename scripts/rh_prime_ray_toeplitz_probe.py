#!/usr/bin/env python3
"""Exact finite prime-power-ray Toeplitz/AR(1) controls.

No zeta zero ordinates. Only finite matrices; the theorem is proved in
research/aletheia_2026-10-07/PRIME_POWER_RAY_TOEPLITZ.md.
"""
from __future__ import annotations

from math import ceil, cos, floor, log, pi, sqrt
import numpy as np


def ray_matrix(p: int, a: float):
    h=log(p)
    r=p**-0.5
    W=2*a
    K=floor(W/h)
    N=ceil(W/h)
    if N<1:
        N=1
    S=h*sum(r**k for k in range(1,K+1))
    J=np.zeros((N,N))
    for j in range(N-1):
        J[j+1,j]=1
    direct=2*S*np.eye(N)
    for k in range(1,K+1):
        power=np.linalg.matrix_power(J,k)
        direct-=h*r**k*(power+power.T)
    C=np.fromfunction(lambda i,j:r**np.abs(i-j),(N,N))
    compact=(2*S+h)*np.eye(N)-h*C
    assert np.allclose(direct,compact,atol=1e-12,rtol=0)
    if N>=2:
        T=np.diag([1]+[1+r*r]*(N-2)+[1])
        T+=np.diag([-r]*(N-1),1)+np.diag([-r]*(N-1),-1)
        assert np.allclose(C@T,(1-r*r)*np.eye(N),atol=1e-12,rtol=0)
    return direct,C,S,K,N


def independent_gap(p: int,a: float) -> float:
    h=log(p)
    return sum(
        2*h*p**(-k/2)*
        (1-cos(pi/(ceil((2*a)/(k*h))+1)))
        for k in range(1,floor(2*a/h)+1)
    )


def upper_sine_bound(p:int,a:float,N:int)->float:
    h=log(p); r=p**-.5
    return 2*h*(1-cos(pi/(N+1)))*r*(1+r)/(1-r)**3


def main():
    print("Prime ray p | horizon a | N | gap | independent-shift gap | gain")
    for p,a in [(2,.8),(2,2),(2,3),(3,2),(5,3),(11,3)]:
        G,C,S,K,N=ray_matrix(p,a)
        eig=np.linalg.eigvalsh(G)
        gap=float(eig[0])
        independent=independent_gap(p,a)
        assert gap>=independent-1e-10
        assert gap>0
        assert gap<=upper_sine_bound(p,a,N)+1e-10
        print(f"p={p:2d} a={a:3g} N={N:2d} gap={gap:.9f} independent={independent:.9f} gain={gap-independent:.9f}")
    print("Large-N prime-ray gap decays at quadratic chain scale")
    p=3
    for N in [20,40,80,160]:
        h=log(p)
        # Noninteger W/h=N-.5 guarantees maximal chain N.
        a=h*(N-.5)/2
        G,_,_,_,actualN=ray_matrix(p,a)
        assert actualN==N
        gap=float(np.linalg.eigvalsh(G)[0])
        assert gap<=upper_sine_bound(p,a,N)+1e-9
        print(f"N={N:3d} gap={gap:.9g} N^2 gap={N*N*gap:.6f}")
    print("PASS: exact KMS compression, tridiagonal inverse, ray gap, and quadratic upper bound.")


if __name__ == "__main__":
    main()
