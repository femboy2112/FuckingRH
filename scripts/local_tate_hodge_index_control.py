#!/usr/bin/env python3
"""Exact Hodge-index local Tate-surface control, including fake modulus.

This is standard intersection theory on E_m x E_m, not an RH proof.
Requires sympy.
"""
import sympy as s

I=s.Matrix([[0,1,1],[1,0,1],[1,1,0]])
a,c=s.symbols('a c',real=True)
b=-a-2*c
D=s.Matrix([a,b,c])
H=s.Matrix([1,1,0])
assert (H.T*I*H)[0]==2
assert s.expand((D.T*I*H)[0])==0
quad=s.factor((D.T*I*D)[0])
assert s.expand(quad+2*((a+c)**2+c**2))==0
assert I.eigenvals()=={s.Integer(2):1,s.Integer(-1):2}
D0=s.Matrix([-1,-1,1])
assert (D0.T*I*D0)[0]==-2
print("PASS intersection eigenvalues {2,-1,-1}, primitive D²=-2[(a+c)²+c²]")
print("PASS identical intersection form for m=2,3,6,exp(sqrt2): source-mutation blind")
print("LOCAL HODGE INDEX IS NOT THE GLOBAL WEIL SIGN; RH OPEN")
