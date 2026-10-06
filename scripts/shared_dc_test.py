import numpy as np
from sympy import primerange

def sigma_p(xi,p):
    r=p**-0.5; lp=np.log(p); th=lp*xi
    return (2*lp/np.pi)*(r*(1+r)/(1-r))*(1-np.cos(th))/np.abs(1-r*np.exp(1j*th))**2

# ===== TEST 1: is there a duplicated DC/coarse channel? sigma_p(0) =====
print("=== Shared-DC hypothesis test ===")
print("sigma_p(0) per prime (duplicate DC channel would be nonzero & shared):")
for p in [2,3,5,7,11,101]:
    print("   p=%3d: sigma_p(0+)=%.3e"%(p, sigma_p(1e-7,p)))
print("  => sigma_p(0)=0 EXACTLY per prime (DC cancels: M_p = log p r/(1-r) exactly).")
print("     There is NO duplicated DC/coarse channel to merge. Refutes the specific shared-DC mechanism.")

# ===== TEST 2: where does the divergence live? sum_p sigma_p(xi) at xi=0 vs xi!=0 =====
print("\nsum_{p<=X} sigma_p(xi):  xi=0 stays 0 (finite); xi!=0 diverges (bulk):")
for xi in [0.0, 0.5, 1.0, 2.0]:
    vals=[]
    for X in [100,1000,10000,100000]:
        s=sum(sigma_p(xi if xi>0 else 1e-9,p) for p in primerange(2,X))
        vals.append(s)
    print("   xi=%.1f : sum over p<X=[1e2..1e5] = %s"%(xi,["%.3f"%v for v in vals]))

# ===== TEST 3: M_p sum divergence rate + is it a |t| (linear/DC) or bulk effect? =====
print("\nsum_{p<=X} M_p (M_p=log p/(sqrt p -1)) vs 2 sqrt(X):")
for X in [100,1000,10000,100000,1000000]:
    Msum=sum(np.log(p)/(np.sqrt(p)-1) for p in primerange(2,X))
    print("   X=%7d: sum M_p=%.3f   2 sqrt X=%.3f   ratio=%.3f"%(X,Msum,2*np.sqrt(X),Msum/(2*np.sqrt(X))))
print("\n  => the divergence is BULK (xi!=0), not a DC/coarse duplication; sigma_p(0)=0 kills the DC-merge idea.")
print("     M_p ~ log p/sqrt p sums like 2 sqrt X = the prime-side e^{L/2} that the POLE (indefinite) cancels.")
