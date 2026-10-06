import numpy as np
np.set_printoptions(precision=3,suppress=True,linewidth=140)

# Weighted Koszul/Hodge complex on the prime-exponent lattice for primes P, exponents 0..K.
# Per-prime weighted difference  nabla_p = I - r_p E_p^{-1},  r_p = p^{-1/2}  (critical half-density).
# nabla_p^* nabla_p = local Euler/whitening (AR(1) precision).  D = sum_p nabla_p (x) a_p^* (Koszul).
# D^2=0 ; Hodge Laplacians Delta_d = D^*D+DD^* are >=0 ; cross terms live in Delta_1 off-diagonal.

P=[2,3]; K=5
R=len(P); shape=[K+1]*R; dim=(K+1)**R
# build per-prime backward-shift S_p (lower exponent of prime p by 1) as dim x dim
def lattice_index(v): 
    idx=0
    for x in v: idx=idx*(K+1)+x
    return idx
def all_v():
    import itertools
    return list(itertools.product(range(K+1),repeat=R))
V=all_v(); pos={v:i for i,v in enumerate(V)}
def Sdown(pi):  # E_p^{-1}: |..v_p..> -> |..v_p-1..>
    M=np.zeros((dim,dim))
    for v in V:
        if v[pi]>=1:
            w=list(v); w[pi]-=1; M[pos[tuple(w)],pos[v]]=1.0
    return M
r=[p**-0.5 for p in P]
nabla=[np.eye(dim)-r[pi]*Sdown(pi) for pi in range(R)]

# degree-0 Laplacian = sum_p nabla_p^* nabla_p  (diagonal/factorized local whitening, no cross)
Delta0=sum(nabla[pi].T@nabla[pi] for pi in range(R))
# degree-1 space = R copies of the lattice (1-forms f_p dx_p). 
# D0: deg0->deg1 : (D f)_p = nabla_p f.   D1: deg1->deg2: (D w)_{pq}=nabla_p w_q - nabla_q w_p.
# Delta_1 = D0 D0^* + D1^* D1  acting on deg1 (block RxR of dim-blocks)
D0=np.vstack([nabla[pi] for pi in range(R)])          # (R*dim) x dim
# D1 for R=2: maps (w_0,w_1) -> nabla_0 w_1 - nabla_1 w_0  (single 2-form component, dim)
if R==2:
    D1=np.hstack([-nabla[1], nabla[0]])               # dim x (2*dim): [ -nabla_1 | nabla_0 ]
Delta1 = D0@D0.T + D1.T@D1                            # (R*dim)x(R*dim)
# positivity + D^2=0 checks
D2=D1@D0
print("checks: D^2=0 ?", np.allclose(D2,0), " ; Delta0>=0 ?", np.linalg.eigvalsh(Delta0).min()>-1e-9,
      " ; Delta1>=0 ?", np.linalg.eigvalsh(Delta1).min()>-1e-9)

# Inspect Delta1 block structure: diagonal blocks vs off-diagonal (cross-prime)
B=Delta1.reshape(R,dim,R,dim)
diag00=B[0,:,0,:]; diag11=B[1,:,1,:]; off01=B[0,:,1,:]
print("\nDelta1 diagonal block (prime 2) nonzero pattern == local whitening + I ? sample 4x4 top-left:")
print(diag00[:4,:4])
print("off-diagonal (cross 2<->3) block, 4x4 top-left (THE cross-prime term):")
print(off01[:4,:4])
print("off-diagonal Frobenius norm = %.4f  (nonzero => genuine cross coupling)"%np.linalg.norm(off01))

# Is the off-diagonal cross block exactly  -nabla_0 nabla_1^*  (the Hecke/prime-swap analog)?
cross_pred = -nabla[0]@nabla[1].T
print("off-diag block == -nabla_2 nabla_3^* ?", np.allclose(off01,cross_pred))

# Compare the cross block's action to the C79 prime-swap: does it move 2^a3^b <-> 2^{a-1}3^{b+1} ?
# nabla_0 nabla_1^* = (I-r2 E2^-1)(I-r3 E3^-1)^* = (I-r2 E2^-1)(I-r3 E3^+1)
print("\ncross block matrix elements <w| -nabla_2 nabla_3^* |v> for sample lattice moves:")
for (v,w,desc) in [((1,0),(0,1),"2^1 -> 3^1  (swap 2->3)"),
                   ((1,1),(0,2),"2.3 -> 3^2  (swap 2->3)"),
                   ((2,0),(1,1),"2^2 -> 2.3  (swap 2->3)"),
                   ((0,1),(1,0),"3 -> 2      (swap 3->2)")]:
    val=cross_pred[pos[w],pos[v]]
    print("   <%s| . |%s>  (%s) = %+.4f"%(w,v,desc,val))
