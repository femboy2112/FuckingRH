#!/usr/bin/env python3
"""Finite checks for the source-wired prime-ray identities."""

import math
from sympy import primerange, factorint
from mpmath import mp, zeta, diff, log

mp.dps = 40

def mangoldt(n):
    f=factorint(n)
    if len(f)==1:
        p=list(f)[0]
        return math.log(p)
    return 0.0

def prime_power_incidence(n, p, k):
    return 1 if n == p**k else 0

# 1. Incidence formula for Lambda and critical event weights.
for n in range(2,300):
    rhs=0.0
    rhscrit=0.0
    for p in primerange(2,n+1):
        pk=p
        k=1
        while pk<=n:
            if n==pk:
                rhs += math.log(p)
                rhscrit += math.log(p) * p**(-0.5*k)
            pk*=p
            k+=1
    lam=mangoldt(n)
    assert abs(rhs-lam)<1e-12
    assert abs(rhscrit - (lam/math.sqrt(n) if lam else 0.0)) < 1e-12

print("Prime-ray incidence reproduces Lambda(n) and Lambda(n)/sqrt(n) for n<300.")

# 2. Finite source correlation converges to -zeta'/zeta in Re(s)>1.
def truncated_source(sigma, t, Pmax=20000):
    total=0j
    for p in primerange(2,Pmax+1):
        p=float(p)
        # exact infinite depth on this prime ray
        z=p**complex(-sigma, t)  # p^{-sigma+it}
        total += math.log(p) * z/(1-z)
    return total

def minus_log_derivative(s):
    s=mp.mpc(s)
    return -diff(lambda z: log(zeta(z)), s)

for sigma,t in [(2.0,0.0),(2.0,1.0),(1.5,2.0)]:
    got=truncated_source(sigma,t,20000)
    target=complex(minus_log_derivative(mp.mpc(sigma,-t))) # -zeta'/zeta(sigma-it)
    print(f"sigma={sigma:.1f}, t={t:.1f}: truncated={got:.10g}, target={target:.10g}, err={abs(got-target):.3e}")

print("Identity checked: source correlation = -zeta'/zeta(sigma-it), up to prime cutoff tail.")

# 3. Source ray response per prime.
for p in [2,3,5,11]:
    s=2.0+0.7j
    direct=sum(math.log(p)*p**(-k*s) for k in range(1,100))
    closed=math.log(p)/(p**s-1)
    assert abs(direct-closed)<1e-12
print("Per-prime source admittance m_p(s)=log(p)/(p^s-1) verified.")

print("RH remains open: these identities factor the event/source layer, not the completed Weil positivity.")
