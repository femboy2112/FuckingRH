#!/usr/bin/env python3
"""Closed prime-ray Fourier symbol for Suzuki's positive finite Weil parent.

No zeros as inputs. Exact symbolic/geometric identity, with finite numerical
cross-checks; low-frequency minima are exploration, NOT proof of RH.
"""
from __future__ import annotations
import cmath
from math import cos, exp, floor, log, pi, sqrt

try:
    import mpmath as mp
except ImportError:
    raise SystemExit("Requires mpmath, already used in the RH repository.")


def primes_up_to(N):
    flags=bytearray(b"\x01")*(N+1)
    flags[0:2]=b"\x00\x00"
    for p in range(2,int(sqrt(N))+1):
        if flags[p]:
            for q in range(p*p,N+1,p):
                flags[q]=0
    return [p for p in range(2,N+1) if flags[p]]


def ray_symbol(p:int,a:float,xi:float)->float:
    h=log(p)
    r=p**-.5
    K=floor(2*a/h)
    if K<=0:return 0.
    z=r*cmath.exp(1j*xi*h)
    return 2*h*(r*(1-r**K)/(1-r)-(z*(1-z**K)/(1-z)).real)


def ray_symbol_brute(p:int,a:float,xi:float)->float:
    h=log(p);r=p**-.5
    return 2*h*sum(r**k*(1-cos(k*h*xi)) for k in range(1,floor(2*a/h)+1))


def log_symbol(a:float,xi:float)->float:
    if xi==0:return 0.
    z=2*a*abs(xi)
    return float(mp.euler+mp.log(z)-mp.ci(z))


def positive_weil_symbol(a:float,xi:float,primes=None)->float:
    if primes is None:primes=primes_up_to(int(exp(2*a)))
    return log_symbol(a,xi)+sum(ray_symbol(p,a,xi) for p in primes)


def main():
    for p in [2,3,5,11]:
        for a in [1.,2.,3.,4.]:
            for xi in [0.,0.3,1.2,3.7,15.1]:
                u=ray_symbol(p,a,xi)
                v=ray_symbol_brute(p,a,xi)
                assert abs(u-v)<1e-11
                assert u>-1e-10
    a=3.
    ps=primes_up_to(int(exp(2*a)))
    print(f"Positive full symbol at horizon a={a}, active primes={len(ps)}")
    for xi in [0.,.1,.25,.5,1.,2.,4.,8.,16.]:
        print(f"  xi={xi:5g}  F_a={positive_weil_symbol(a,xi,ps):.10g}")
    print("PASS: finite Euler ray geometric formula matches exact prime-power sum.")
    print("This is not the signed completed Weil symbol; RH remains open.")


if __name__=="__main__":
    main()
