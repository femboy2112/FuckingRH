#!/usr/bin/env python3
"""Checks for continuum affine, half-density, Gamma-log transform, and phasor identities."""
import math, cmath
from mpmath import mp

mp.dps=50

# 1. Unitary affine half-density on a Gaussian via numerical quadrature.
def f(x): return mp.e**(-x*x)
def U(a,b,x): return a**(-mp.mpf("0.5"))*f((x-b)/a)

norm = mp.quad(lambda x: abs(f(x))**2, [-mp.inf, mp.inf])
for a,b in [(2,0),(3,1),(mp.mpf("0.5"),-2)]:
    n2=mp.quad(lambda x: abs(U(a,b,x))**2, [-mp.inf, mp.inf])
    assert abs(n2-norm) < mp.mpf("1e-30")
print("Affine a^(-1/2) normalization preserves L2 norm.")

# 2. Gamma as bilateral log-Laplace transform.
for s in [mp.mpf("0.7"), mp.mpf("1.3"), mp.mpf("2.5")]:
    lhs=mp.gamma(s)
    rhs=mp.quad(lambda u: mp.e**(s*u-mp.e**u), [-mp.inf, mp.inf])
    assert abs(lhs-rhs) < mp.mpf("1e-30")
print("Gamma(s)=∫ exp(su-e^u) du verified.")

# 3. Arithmetic half-density.
for p in [2,3,5,7]:
    for k in [1,2,3]:
        a=mp.mpf(p)**k
        assert abs(a**(-mp.mpf("0.5")) - mp.mpf(p)**(-mp.mpf(k)/2)) < mp.mpf("1e-45")
print("Affine half-density at a=p^k equals p^(-k/2).")

# 4. Euler-side zeta as log-frequency phasor sum, finite truncation check.
sigma=mp.mpf("2")
t=mp.mpf("3")
for N in [100,1000,10000]:
    s=sum(mp.power(n,-sigma)*mp.e**(-1j*t*mp.log(n)) for n in range(1,N+1))
    target=mp.zeta(sigma+1j*t)
    print("N",N,"zeta phasor error",abs(s-target))

print("Continuum affine checks passed. RH remains open.")
