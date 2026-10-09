#!/usr/bin/env python3
"""Exact linear-algebra audit of the even-Frobenius spinorial obstruction.
Requires SymPy; this is a model of CP^1 complex-point spinors, NOT an absolute sheaf.
"""
import json
import sympy as s
I=s.I
Jminus=s.Matrix([[0,-1],[1,0]]) # antiunitary Jminus(v)=matrix*conj(v)
Jplus=s.Matrix([[0,1],[1,0]])
assert Jminus*s.conjugate(Jminus)==-s.eye(2)
assert Jplus*s.conjugate(Jplus)==s.eye(2)
variables=s.symbols("x0:8",real=True)
T=s.Matrix(2,2,lambda i,j:variables[2*(2*i+j)]+I*variables[2*(2*i+j)+1])
equations=T*Jminus-Jplus*s.conjugate(T)
real_equations=[]
for item in equations:
    real_equations += [s.re(s.expand_complex(item)),s.im(s.expand_complex(item))]
M,rhs=s.linear_eq_to_matrix(real_equations,variables)
assert M.rank()==8 and M.nullspace()==[]
for n in [2,3,4,5,6,8,9,11,15,22,30]:
    assert (n-1)%2 == (n%2==0)
print(json.dumps({
    "status":"PASS",
    "real_unknowns":8,
    "linear_system_rank":M.rank(),
    "kernel_dimension":0,
    "negative_spin_reversal_square":"-I",
    "positive_spin_reversal_square":"+I",
    "theorem":"no nonzero strict complex-linear spinor intertwiner from - to + sectors",
    "boundary":"a base real-structure morphism still exists; a graded/twisted target is needed"
},indent=2,sort_keys=True))
