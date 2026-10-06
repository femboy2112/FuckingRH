import numpy as np
from sympy import primerange

# ===== Section 5: residue-branch isometries R_{m,r}, Cuntz relations, affine braid =====
# R_{m,r}|q> = |m q + r>.  On truncated l2(0..Nn-1).
def Rmat(m,r,Nn):
    R=np.zeros((Nn,Nn))
    for q in range(Nn):
        n=m*q+r
        if n<Nn: R[n,q]=1.0
    return R
def Smat(Nn):
    S=np.zeros((Nn,Nn))
    for n in range(Nn-1): S[n+1,n]=1.0
    return S
Nn=60; m=3
S=Smat(Nn); Rs=[Rmat(m,r,Nn) for r in range(m)]
# S R_{m,r} = R_{m,r+1} (r<m-1);  S R_{m,m-1} = R_{m,0} S ; V_m=R_{m,0}; V_m S=S^m V_m
print("=== Section 5: refinement branches = affine braid (Cuntz structure) ===")
ok1=all(np.allclose((S@Rs[r])[:40,:40],(Rs[r+1])[:40,:40]) for r in range(m-1))
ok2=np.allclose((S@Rs[m-1])[:30,:30],(Rs[0]@S)[:30,:30])
Vm=Rs[0]
ok3=np.allclose((Vm@S)[:20,:20],(np.linalg.matrix_power(S,m)@Vm)[:20,:20])
# Cuntz: sum_r R_r R_r^* = I ; R_r^* R_r = I
cuntz_sum=sum(Rs[r]@Rs[r].T for r in range(m))
iso=all(np.allclose((Rs[r].T@Rs[r])[:40,:40],np.eye(Nn)[:40,:40]) for r in range(m))
print("  S R_{m,r}=R_{m,r+1} (r<m-1):",ok1," ; S R_{m,m-1}=R_{m,0}S:",ok2," ; V_m S=S^m V_m:",ok3)
print("  R_r isometries (R_r^*R_r=I):",iso," ; sum_r R_r R_r^* = I (Cuntz O_m):",np.allclose(cuntz_sum[:40,:40],np.eye(Nn)[:40,:40]))
print("  => {S,R_{m,r}} = refinement+carry generates the Cuntz/ax+b braid. 'affine noncommutativity = carry curvature.'")

# ===== Section 8 hostile check: SUCC on Z/L_N is a cyclic shift = circulant = RH-inert =====
print("\n=== Section 8 hostile: quotient filtration SUCC on Z/L_N is convolution (RH-inert) ===")
def lcm_upto(N):
    from math import gcd
    L=1
    for k in range(2,N+1): L=L*k//gcd(L,k)
    return L
for N in [6,8]:
    L=lcm_upto(N)
    # succ mod L = cyclic shift on Z/L
    Scyc=np.zeros((L,L))
    for x in range(L): Scyc[(x+1)%L,x]=1.0
    comm=np.linalg.norm(Scyc@Scyc.T-Scyc.T@Scyc)  # circulant => normal => [S,S^*]=0
    # Fourier-diagonal check: eigenvalues are roots of unity
    ev=np.linalg.eigvals(Scyc)
    print("  N=%d (L_N=%d): SUCC mod L is circulant: [S,S^*]=%.1e ; |eigenvalues|=1 (Fourier-diagonal): %s"%(
        N,L,comm,np.allclose(np.abs(ev),1.0)))
print("  => the pure quotient filtration is COMMUTATIVE (cyclic shift = convolution) = RH-inert (C94).")
print("     The carry/wrap (distinguishing Z from Z/L_N) is LOST in the quotient; it survives ONLY in the")
print("     branch sections R_{m,r} (the irregular lift back to Z). Carry info lives in sections, not quotients.")
