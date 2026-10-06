import numpy as np
from math import comb, isqrt
from fractions import Fraction

def factor(n):
    f={}; d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
def Omega(n): return sum(factor(n).values())
def divisors(n):
    ds=[1]
    for p,e in factor(n).items():
        ds=[d*p**k for d in ds for k in range(e+1)]
    return sorted(ds)
def Binom(n,d):   # multiplicative binomial prod_p C(v_p(n), v_p(d))
    assert n%d==0
    fn=factor(n); fd=factor(d); r=1
    for p,e in fn.items(): r*=comb(e, fd.get(p,0))
    return r

X=64
nums=list(range(1,X+1)); idx={n:i for i,n in enumerate(nums)}

# ---- (1) isometry: ||J_B|n>||^2 = 2^{-Omega} sum_{d|n} Binom(n,d) = 1 ----
print("(1) J_B isometry check: 2^{-Omega(n)} sum_{d|n} Binom(n,d) == 1 for all n<=%d"%X)
ok=all( Fraction(sum(Binom(n,d) for d in divisors(n)), 2**Omega(n))==1 for n in nums if n>1)
print("    holds:", ok, " (and <J_B m|J_B n>=0 for m!=n since the split (d,n/d) determines n)")

# ---- (2) contraction with A=|q><p| gives the prime-swap [pm=qn] ----
# <m|J_B^*(|q><p| (x) I)J_B|n> = 2^{-(Om(m)+Om(n))/2} sqrt(Binom(m,g)Binom(n,g)) [pm=qn], g=m/q=n/p
def contraction_direct(m,n,p,q):
    # brute force from the definition of J_B
    tot=0.0
    cm=2**(-0.5*Omega(m)); cn=2**(-0.5*Omega(n))
    for e in divisors(m):
        for d in divisors(n):
            # J_B|m> has term amp_m(e)|e> x |m/e>;  A=|q><p| maps |e>-> [e==p]|q>
            # <q,m/e | ... | contributes when first leg e==p (bra side) ... careful with adjoint:
            # <m|J_B^* (|q><p| x I) J_B|n> = sum_{e|m,d|n} amp_m(e)amp_n(d) <e|q><p|d> <m/e|n/d>
            if e==q and d==p and (m//e)==(n//d):
                amp_m=cm*np.sqrt(Binom(m,e)); amp_n=cn*np.sqrt(Binom(n,d))
                tot+=amp_m*amp_n
    return tot
def contraction_formula(m,n,p,q):
    if p*m!=q*n: return 0.0
    if m%q!=0 or n%p!=0: return 0.0
    g=m//q
    if n//p!=g: return 0.0
    return 2**(-0.5*(Omega(m)+Omega(n)))*np.sqrt(Binom(m,g)*Binom(n,g))

print("\n(2) contraction J_B^*(|q><p| x I)J_B gives prime-swap [pm=qn]:")
print("   (m,n,p,q) : direct      formula    match")
tests=[(2,3,3,2),(12,18,3,2),(30,45,2,3),(6,10,5,3),(4,9,3,2),(20,50,5,2),(12,8,2,3),(6,6,2,2)]
allok=True
for (m,n,p,q) in tests:
    a=contraction_direct(m,n,p,q); b=contraction_formula(m,n,p,q)
    mt=abs(a-b)<1e-9; allok&=mt
    print("   (%2d,%2d,%d,%d): %.5f     %.5f     %s   [pm=qn? %s]"%(m,n,p,q,a,b,mt,p*m==q*n))
print("   all match:",allok)

# ---- (3) does summing these contractions with critical weights give anything K_Psi-like? ----
# Build the operator C = sum_{p,q} sqrt(log p log q) (pq)^{-1/4} J_B^*(|q><p| x I)J_B  on n<=X
# and look at its structure (diagonal vs off-diagonal prime-swap graph), compare to C79.
primes=[2,3,5,7,11,13,17,19,23,29,31]
import math
def amp(p): return math.sqrt(math.log(p))*p**-0.25
M=np.zeros((X,X))
for m in nums:
    for n in nums:
        s=0.0
        for p in primes:
            for q in primes:
                if p*m==q*n and n%p==0 and m%q==0:
                    s+=amp(p)*amp(q)*contraction_formula(m,n,p,q)
        M[idx[m],idx[n]]=s
print("\n(3) weighted swap operator built from J_B: symmetric=%s, diag range [%.3f,%.3f]"%(
      np.allclose(M,M.T), M.diagonal().min(), M.diagonal().max()))
print("    (this is the binomial-dressed version of the C79 prime-swap graph F*F)")
