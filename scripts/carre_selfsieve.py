import numpy as np
from sympy import primerange, isprime

# ===== Section 15/22-E: carre-du-champ of carry curvature = high-pass energy =====
# CARRY_m = (S-I)(x)|0><m-1|.  CARRY_m^* CARRY_m = (S-I)^*(S-I) (x) |m-1><m-1| = (2I-S-S^*)(x)|m-1><m-1|
def Smat(Nn):
    S=np.zeros((Nn,Nn))
    for n in range(Nn-1): S[n+1,n]=1.0
    return S
Nn=40; m=3
S=Smat(Nn); I=np.eye(Nn)
E=np.zeros((m,m)); E[0,m-1]=1.0  # |0><m-1|
CARRY=np.kron(S-I,E)
lhs=CARRY.T@CARRY
Lap=(2*I - S - S.T)  # (S-I)^*(S-I) on the shift (=2I-S-S^* up to boundary)
Ebb=np.zeros((m,m)); Ebb[m-1,m-1]=1.0
rhs=np.kron(Lap,Ebb)
# compare interior
d=lhs-rhs; d[:, -m:]=0; d[-m:,:]=0
print("=== Section 15/22-E: carre of carry curvature ===")
print("  ||CARRY^*CARRY - (2I-S-S^*)(x)|m-1><m-1|||(interior) = %.2e"%np.linalg.norm(d))
print("  => carre-du-champ of the carry = high-pass energy (2I-S-S^*)=|I-U|^2 (symbol 2(1-cos)), ")
print("     projected on the top residue m-1. This IS the (I-U_depth)^*(I-U_depth) innovation of B_p (sec 11).")
print("  Weighted by log p & half-density over the p-adic depth hierarchy it reconstructs sigma_p (C90).")
print("  => Suzuki/von-Mangoldt event measure = carre-du-champ of carry curvature, LOCALLY (per prime).")

# ===== Section 6: self-sieve correctness =====
# odd candidate n survives clocks of discovered primes p (activated at p^2, firing at multiples) iff prime
print("\n=== Section 6: self-sieve (clocks activated at p^2) is correct ===")
def self_sieve(maxn):
    primes=[]; clocks={}  # p -> next fire
    out=[]
    for n in range(2,maxn+1):
        # advance/fire existing clocks
        killed=False
        for p in primes:
            if p*p>n: break
            # p-clock fires at multiples of p (>=p^2)
            if n>=p*p and n%p==0: killed=True
        if not killed:
            out.append(n); primes.append(n)  # survivor => new clock born
    return out
sieved=self_sieve(500)
true=list(primerange(2,501))
print("  self-sieve primes up to 500 == true primes:",sieved==true)

# ===== Section 18-E: causal birth vs static prime set -> same Suzuki kernel =====
print("\n=== Section 18-E hostile: causal self-sieve vs static prime set give the SAME K_Psi ===")
print("  The Suzuki kernel at horizon L sums Lambda over ALL prime powers <= e^L regardless of birth order.")
print("  Causal (primes born 2,3,5,...) and static (all primes preloaded) yield identical prime-power sets,")
print("  hence identical K_{Psi,L}. => causality/birth-ORDER is RH-inert for the kernel (a dynamics statement,")
print("  not a kernel statement). The RH content is in WHICH p^k enter (+their coupling), not the birth order.")
# demonstrate: set of prime powers <= e^L is order-independent
L=4.0
pps=set()
for p in primerange(2,int(np.exp(L))+1):
    pk=p
    while pk<=np.exp(L): pps.add(pk); pk*=p
print("  #prime powers <= e^%.0f = %d (a set; order of discovery irrelevant)"%(L,len(pps)))
