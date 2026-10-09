#!/usr/bin/env python3
"""Two-character operator law versus nonmultiplicative scalar realization.
Exact SymPy algebra + numerical pure-state controls; no L-function zeros.
"""
import json
import sympy as s

t=s.symbols('t',real=True)
k=s.symbols('k',positive=True,real=True)
I=s.I
U2=s.diag(I,-I)
U3=s.diag(-I,I)
U6=U2*U3
assert U6==s.eye(2)

def value(M,weight):
    return s.simplify(weight*M[0,0]+(1-weight)*M[1,1])

d2=value(U2,t);d3=value(U3,t);d6=value(U6,t)
cov=s.factor(d6-d2*d3)
assert s.simplify(cov-4*t*(1-t))==0
assert s.simplify(cov.subs(t,(1-I*k)/2)-(1+k*k))==0
assert s.solve(cov,t)==[0,1]
# A full Hilbert-space pure superposition can have a *non-pure restriction*
# to the diagonal arithmetic observable algebra.
psi=s.Matrix([s.sqrt(t),s.sqrt(1-t)])
rho=psi*psi.T
assert s.simplify(rho*rho-rho)==s.zeros(2)
assert s.simplify(s.trace(rho))==1
assert s.simplify(s.trace(rho*U2)-d2)==0
assert s.simplify(s.trace(rho*U3)-d3)==0
# DH's coefficients cannot come from a positive diagonal character-mixture:
# expectation of U2 under positive state lies on imaginary segment [-i,i],
# but DH d2=kappa>0 is real.
phi=(1+s.sqrt(5))/2
kap=s.sqrt(1+phi**2)-phi
assert kap.is_positive is True
assert s.simplify(value(U2,(1-I*kap)/2)-kap)==0
assert s.simplify(value(U3,(1-I*kap)/2)+kap)==0
rows=[]
for q in [s.Rational(0),s.Rational(1,4),s.Rational(1,2),s.Rational(3,4),s.Rational(1)]:
    rows.append({'sector_weight':str(q), 'observed_a2':str(d2.subs(t,q)),
                 'observed_a3':str(d3.subs(t,q)),
                 'observed_a6':str(d6.subs(t,q)),
                 'connected_b6':str(cov.subs(t,q))})
print(json.dumps({'status':'PASS','operator_U2_U3_equals_U6':True,
    'a2_formula':str(d2),'a3_formula':str(d3),
    'scalar_connected_defect':str(cov),
    'zero_defect_exact_iff':'t in {0,1} for nonnegative diagonal-mixture weights',
    'pure_full_vector_mixed_observable_restriction':True,
    'DH_weight':'(1-i*kappa)/2',
    'DH_connected_defect_formula':'1+kappa**2',
    'DH_kappa_numerical':str(s.N(kap,18)),
    'DH_b6_numerical':str(s.N(1+kap**2,18)),
    'finite_controls':rows,
    'interpretation':'source multiplicativity needs an algebra-character state, not generic positive state'},indent=2))
