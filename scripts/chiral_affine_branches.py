#!/usr/bin/env python3
"""Finite checks for the chiral affine branch identities."""
import numpy as np

def shift(N):
    S=np.zeros((N,N))
    for n in range(N-1):
        S[n+1,n]=1.0
    return S

def V(N,m):
    # basis index j=0 represents integer n=j+1
    M=np.zeros((N,N))
    for j in range(N):
        n=j+1
        mn=m*n
        if 1 <= mn <= N:
            M[mn-1,j]=1.0
    return M

N=200
S=shift(N)
V2=V(N,2)
Aplus=S@V2
Aminus=S.T@V2

# Ignore high-end truncation boundary.
K=60
sl=slice(0,K)

cross1=Aminus.T@Aplus
cross2=Aplus.T@Aminus
lap=(Aplus-Aminus).T@(Aplus-Aminus)
target=2*np.eye(N)-S-S.T

print("||A_-^* A_+ - S|| interior =",np.linalg.norm((cross1-S)[sl,sl]))
print("||A_+^* A_- - S^*|| interior =",np.linalg.norm((cross2-S.T)[sl,sl]))
print("||(A_+-A_-)^*(A_+-A_-) - (2I-S-S^*)|| interior =",np.linalg.norm((lap-target)[sl,sl]))

# General m nearest ±1 cross term.
for m in [2,3,4,5,6]:
    Vm=V(N,m)
    Ap=S@Vm
    Am=S.T@Vm
    cr=Am.T@Ap
    print(f"m={m}: interior ||A_-^*A_+||={np.linalg.norm(cr[sl,sl]):.6g}, ||-S||={np.linalg.norm((cr-S)[sl,sl]):.6g}")

# Wider symmetric pair S^{±r}V_m when 2r=m.
for m in [2,4,6,8]:
    r=m//2
    Sp=np.linalg.matrix_power(S,r)
    Sm=np.linalg.matrix_power(S.T,r)
    Vm=V(N,m)
    Ap=Sp@Vm
    Am=Sm@Vm
    cr=Am.T@Ap
    print(f"m={m}, r={r}: ||A_-^*A_+ - S|| interior={np.linalg.norm((cr-S)[sl,sl]):.6g}")

print("Finite truncation checks complete; all theorem statements are infinite-space identities.")
