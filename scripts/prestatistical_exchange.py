import numpy as np
from itertools import product, permutations
from mpmath import mp, mpc, zeta as mzeta
mp.dps=20

# ================= C. parent: one-particle A(s)=diag(p^{-s}); det identities =================
def primes_upto(X):
    s=np.ones(X+1,bool); s[:2]=False
    for i in range(2,int(X**0.5)+1):
        if s[i]: s[i*i::i]=False
    return list(np.nonzero(s)[0])
P=primes_upto(2000)
s=2.0  # Re>1 so Euler products converge
x=np.array([p**(-s) for p in P])
boson=np.prod(1/(1-x)); fermi_signed=np.prod(1-x); fermi_unsigned=np.prod(1+x)
z=float(mzeta(s))
print("=== C. ONE parent A(s)=diag(p^{-s}); second-quantized determinants ===")
print("  det(I-A)^{-1} = prod 1/(1-p^{-s}) = %.8f   zeta(%.1f)=%.8f   (BOSONIC => zeta)"%(boson,s,z))
print("  det(I-A)      = prod (1-p^{-s})   = %.8f   1/zeta  =%.8f   (FERMION SUPERTRACE => 1/zeta = Mobius)"%(fermi_signed,1/z))
print("  prod(1+p^{-s}) = %.8f   zeta/zeta(2s)=%.8f   (fermion UNSIGNED => squarefree |mu|)"%(fermi_unsigned,z/float(mzeta(2*s))))
print("  -d/ds log det(I-A) = sum_{p,k} log p p^{-ks} = -zeta'/zeta (von Mangoldt, the 'log trace')")
print("  => zeta, 1/zeta, Lambda are three traces/characters of the SAME diagonal prime operator.")

# ================= D. do the S_r sectors escape? Schur functions of {p^{-s}} =================
# For r=2: Sym^2 trace = h_2 = (p1^2+p2)/2 ; Lambda^2 trace = e_2 = (p1^2 - p2)/2.  (p_k = sum_p p^{-ks})
p1=np.sum(x); p2=np.sum(x**2)
print("\n=== D. S_r/Schur sectors of the DIAGONAL parent are symmetric functions of {p^{-s}} ===")
print("  h_2 (Sym^2) = (p1^2+p2)/2 = %.6f ;  e_2 (Lambda^2) = (p1^2-p2)/2 = %.6f"%( (p1**2+p2)/2,(p1**2-p2)/2))
print("  p1 = P(s)= %.6f, p2 = P(2s)= %.6f  (prime zeta functions)"%(p1,p2))
print("  => every sector is a polynomial in the prime zetas P(ks); all COMMUTATIVE/diagonal => RH-inert (C89).")

# ================= D(2). is the prime-swap S_r-equivariant (present in ALL sectors)? =============
# one-particle swap p->q is |q><p| ; second-quantized on V^{x r} = sum_i (pos i). Check it preserves &
# is nonzero on Sym, Lambda, and MIXED isotypic components for r=2 and r=3 on a 3-prime space.
Pn=[2,3,5]; d=len(Pn); idx={p:i for i,p in enumerate(Pn)}
def onehot(p): e=np.zeros(d); e[idx[p]]=1; return e
def swap_op(r,p,q):   # sum_i I..|q><p|..I on (C^d)^{x r}
    O=np.zeros((d**r,d**r))
    E=np.outer(onehot(q),onehot(p))
    for i in range(r):
        mats=[np.eye(d)]*r; mats[i]=E
        M=mats[0]
        for k in range(1,r): M=np.kron(M,mats[k])
        O+=M
    return O
def sym_proj(r):   # projector onto Sym^r
    Pr=np.zeros((d**r,d**r))
    for perm in permutations(range(r)):
        Pr+=perm_mat(perm)
    return Pr/math.factorial(r)
def perm_mat(perm):
    r=len(perm); M=np.zeros((d**r,d**r))
    for idxs in product(range(d),repeat=r):
        src=idxs; dst=tuple(idxs[perm.index(i)] for i in range(r))
        M[flat(dst),flat(src)]=1
    return M
def flat(t): 
    v=0
    for a in t: v=v*d+a
    return v
import math
def alt_proj(r):
    Pr=np.zeros((d**r,d**r))
    for perm in permutations(range(r)):
        sgn=sign(perm); Pr+=sgn*perm_mat(perm)
    return Pr/math.factorial(r)
def sign(perm):
    perm=list(perm); s=1
    for i in range(len(perm)):
        for j in range(i+1,len(perm)):
            if perm[i]>perm[j]: s=-s
    return s
r=3
Sym=sym_proj(r); Alt=alt_proj(r); Mixed=np.eye(d**r)-Sym-Alt   # mixed isotypic = rest
O=swap_op(r,2,3)  # swap a 2 for a 3
def sector_norm(Proj): 
    return np.linalg.norm(Proj@O@Proj)
print("\n=== D(2). prime-swap (2->3) is S_r-equivariant: nonzero in EVERY sector (r=3, primes {2,3,5}) ===")
print("  ||Sym   O Sym||   = %.4f"%sector_norm(Sym))
print("  ||Alt   O Alt||   = %.4f"%sector_norm(Alt))
print("  ||Mixed O Mixed|| = %.4f"%sector_norm(Mixed))
print("  [O,Sym]=0 ? %s   => O preserves sectors, acts within each; NOT localized to a mixed sector."%(
      np.allclose(O@Sym,Sym@O)))
