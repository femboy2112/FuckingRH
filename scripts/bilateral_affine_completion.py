#!/usr/bin/env python3
"""Exact algebra checks for bilateral affine completion and centered edge factorization."""

from fractions import Fraction
import cmath
import math

# affine map represented by (a,b): x -> a*x+b
def compose(g,h):
    a,b=g; c,d=h
    return (a*c, a*d+b)

def inv(g):
    a,b=g
    return (1/a, -b/a)

I=(Fraction(1),Fraction(0))
T1=(Fraction(1),Fraction(1))
Tm1=inv(T1)

def D(p):
    return (Fraction(p),Fraction(0))

# inverse SUCC
x=Fraction(0)
assert compose(Tm1,I)[0] == 1
def act(g,x):
    a,b=g
    return a*x+b

assert act(Tm1,Fraction(0)) == -1
assert act(compose(Tm1,Tm1),Fraction(0)) == -2

# affine conjugacy D_p T_b D_p^-1 = T_{p b}
for p in [2,3,5,7]:
    Dp=D(p); Dpi=inv(Dp)
    lhs=compose(compose(Dp,T1),Dpi)
    rhs=(Fraction(1),Fraction(p))
    assert lhs==rhs
    lhs2=compose(compose(Dpi,T1),Dp)
    rhs2=(Fraction(1),Fraction(1,p))
    assert lhs2==rhs2

print("Affine conjugacy and forced fractional SUCC verified exactly.")

# closed affine relation loop D_p T_1 D_p^-1 T_-p = I
for p in [2,3,5,7]:
    loop=compose(compose(compose(D(p),T1),inv(D(p))),(Fraction(1),Fraction(-p)))
    assert loop==I
print("Closed affine braid loops verified.")

# centered translation identity on Fourier symbols:
# C_a^*C_a = 2 - e^{iva} - e^{-iva}
# E_a^*E_a = 2 + e^{iva} + e^{-iva}
for a in [math.log(2),math.log(3),1.7]:
    for v in [0.0,0.3,1.1,2.7]:
        cp=cmath.exp(1j*v*a/2)-cmath.exp(-1j*v*a/2)
        ep=cmath.exp(1j*v*a/2)+cmath.exp(-1j*v*a/2)
        adj=cmath.exp(1j*v*a)+cmath.exp(-1j*v*a)
        assert abs(abs(cp)**2 - (2-adj).real) < 1e-12
        assert abs(abs(ep)**2 - (2+adj).real) < 1e-12
        assert abs(0.5*(abs(cp)**2-abs(ep)**2) + adj.real) < 1e-12

print("Centered chiral/symmetric edge identities verified.")

# weighted graph Laplacian-degree cancellation on symbols
weights=[(math.log(2)/math.sqrt(2),math.log(2)),
         (math.log(3)/math.sqrt(3),math.log(3)),
         (math.log(4)/2 if False else math.log(2)/2,math.log(4))]
# use Lambda(4)=log 2
S=sum(w for w,a in weights)
for v in [0,0.4,1.3]:
    lap=sum(w*(2-2*math.cos(a*v)) for w,a in weights)
    adjacency=sum(2*w*math.cos(a*v) for w,a in weights)
    assert abs((lap-2*S)+adjacency)<1e-12

print("Degree subtraction converts prime edge Laplacian to minus adjacency.")
print("RH remains open: these identities expose a new reversible constructor class only.")
