import numpy as np
np.set_printoptions(precision=3,suppress=True,linewidth=140)

# ===== Section 2: radix-m carry decomposition  S~_m = I(x)C_m + (S-I)(x)|0><m-1| =====
# Work on l2(0..Nq-1) (x) C^m, representing n = m*q + r, 0<=q<Nq, 0<=r<m.
def build(m, Nq):
    dq=Nq; d=dq*m
    # index (q,r) -> q*m + r  (so basis of l2(N_0) truncated, n = q*m+r)
    def ix(q,r): return q*m+r
    # successor on n-space (truncated): S|n>=|n+1>, drop top
    Nn=dq*m
    S=np.zeros((Nn,Nn))
    for n in range(Nn-1): S[n+1,n]=1.0
    # D_m is identity on the n<->(q,r) relabeling (n=q*m+r already), so S~_m = S in (q,r) order,
    # but we must express it in the tensor basis |q>(x)|r> with flat index q*m+r (same). Good.
    Stil=S
    # RHS: I(x)C_m + (S_q - I)(x)|0><m-1|, where S_q is successor on the quotient (q->q+1)
    I_q=np.eye(dq); Cm=np.zeros((m,m))
    for r in range(m): Cm[(r+1)%m, r]=1.0
    Sq=np.zeros((dq,dq))
    for q in range(dq-1): Sq[q+1,q]=1.0
    E=np.zeros((m,m)); E[0,m-1]=1.0   # |0><m-1|
    RHS=np.kron(I_q,Cm)+np.kron(Sq-np.eye(dq),E)
    return Stil,RHS,Cm,Sq,E

for m in [2,3,5]:
    Nq=12
    Stil,RHS,Cm,Sq,E=build(m,Nq)
    # compare on interior (avoid the single truncation-boundary column at the very top)
    diff=Stil-RHS
    # the only mismatch should be at the top boundary n=Nq*m-1 (carry to out-of-range); zero it
    diff[:, -1]=0  # top column is boundary artifact
    print("m=%d: ||S~_m - [I(x)C_m + (S-I)(x)|0><m-1|]|| (interior) = %.2e"%(m,np.linalg.norm(diff)))

# ===== Fourier-decompose the carry (Section 4): C_m diagonal, carry becomes rank-1 across harmonics =====
m=5
Fm=np.array([[np.exp(2j*np.pi*a*r/m) for r in range(m)] for a in range(m)])/np.sqrt(m)  # rows=characters
Cm=np.zeros((m,m));
for r in range(m): Cm[(r+1)%m,r]=1.0
E=np.zeros((m,m)); E[0,m-1]=1.0
Cm_F=Fm@Cm@Fm.conj().T
E_F=Fm@E@Fm.conj().T
print("\nSection 4 (m=%d): F C_m F* diagonal? off-diag norm=%.2e ; diag (characters e^{-2pi i a/m}):"%(m,np.linalg.norm(Cm_F-np.diag(np.diag(Cm_F)))))
print("  ",np.round(np.diag(Cm_F),3))
print("  carry F|0><m-1|F* rank =",np.linalg.matrix_rank(E_F,tol=1e-9)," (rank-1 coupling across all %d harmonic channels)"%m)
u,sv,vh=np.linalg.svd(E_F); print("  singular values:",np.round(sv,3)," (one nonzero => rank 1)")

# ===== Section 3: binary (m=2) full adder: bit'=bit XOR carry_in, carry_out=bit AND carry_in =====
# The carry term for m=2: (S-I)(x)|0><1|.  Acting: residue(low bit) r=1 with carry -> r=0, q++ (carry out).
# Verify the increment on (q,bit): n=2q+bit, n+1: if bit=0 -> bit=1,q same (no carry); if bit=1 -> bit=0,q+1 (carry).
print("\nSection 3 binary incrementer n->n+1 as (q,bit): carry_out = bit AND 1 (incrementing):")
for q in range(3):
    for bit in range(2):
        n=2*q+bit; n1=n+1; q1,b1=divmod(n1,2)
        print("  (q=%d,bit=%d) n=%d -> n+1=%d = (q=%d,bit=%d)  [bit'=bit XOR 1=%d, carry=bit AND 1=%d]"%(
            q,bit,n,n1,q1,b1, bit^1, bit&1))
