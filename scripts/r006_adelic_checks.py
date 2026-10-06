#!/usr/bin/env python3
"""Round006: local Haar half-density and the adelic product formula -- where p^{-k/2} comes from,
and why it is the Tate/Connes self-dual normalization (NOT a new mechanism). No zeta zeros.
"""
import numpy as np
from sympy import factorint, primerange
import mpmath as mp
mp.mp.dps = 30

def val_p(q_num, q_den, p):
    return factorint(q_num).get(p, 0) - factorint(q_den).get(p, 0)

print("="*88)
print("PRODUCT FORMULA  prod_v |q|_v = 1  for q in Q^x   (|q|_p = p^{-v_p(q)}, |q|_inf = |q|)")
print("="*88)
for (num, den) in [(12, 1), (50, 7), (360, 49), (2*3*5*7, 11*13)]:
    q = mp.mpf(num)/den
    primes = set(factorint(num)) | set(factorint(den))
    prod = abs(q)                                   # the real place |q|_inf
    for p in primes:
        prod *= mp.mpf(p)**(-val_p(num, den, p))     # |q|_p = p^{-v_p}
    print(f"  q={num}/{den}:  prod_v |q|_v = {mp.nstr(prod,12)}   (=1 ? {mp.almosteq(prod,1)})")

print("\n"+"="*88)
print("LOCAL HALF-DENSITY ORIENTATION for a = p^k")
print("="*88)
for (p, k) in [(2,3),(3,2),(5,1)]:
    mod_p = mp.mpf(p)**(-k)        # |p^k|_p
    mod_inf = mp.mpf(p)**(k)       # |p^k|_inf
    print(f"  a=p^k={p}^{k}:  |a|_p={mp.nstr(mod_p,6)} -> half-density |a|_p^{{1/2}}={mp.nstr(mp.sqrt(mod_p),6)} = p^{{-k/2}}")
    print(f"               |a|_inf={mp.nstr(mod_inf,6)} -> |a|_inf^{{1/2}}={mp.nstr(mp.sqrt(mod_inf),6)} = p^{{+k/2}}  (reciprocal)")
print("  => the CRITICAL weight p^{-k/2} is the square-root of the local modulus (Tate self-dual).")

print("\n"+"="*88)
print("UNITARY DILATION on L^2(R, dx) requires EXACTLY the 1/2 power:  (U_a f)(x)=|a|^{-1/2}f(x/a)")
print("  with exponent 1/2+eps, ||U_a f||/||f|| = |a|^{-eps} != 1 unless eps=0.")
print("="*88)
xs = np.linspace(-20, 20, 40001); dx = xs[1]-xs[0]
f = np.exp(-xs**2/2)
nf = np.sqrt(np.sum(f**2)*dx)
a = 3.0
for eps in [0.0, 0.05, -0.1]:
    # (U_a f)(x) = |a|^{-(1/2+eps)} f(x/a)
    Uf = abs(a)**(-(0.5+eps)) * np.interp(xs/a, xs, f, left=0, right=0)
    nUf = np.sqrt(np.sum(Uf**2)*dx)
    print(f"  eps={eps:+.2f}: ||U_a f||/||f|| = {nUf/nf:.6f}   (predicted |a|^{{-eps}} = {abs(a)**(-eps):.6f})")
print("  => local unitarity SELECTS 1/2 exactly; any other weight is a non-isometry (control H).")
print("\nDONE. The half-density apparatus = Tate/Connes self-dual Haar normalization (LITERATURE_INTERFACE).")
