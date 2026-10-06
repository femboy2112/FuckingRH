import numpy as np
from mpmath import mp, mpf, digamma, catalan, pi, log as mlog
mp.dps=25
LIN=float((digamma(mpf(1)/4)-mlog(pi))/2); Cc=float(pi**2+8*catalan)
def mangoldt(X):
    X=int(X); s=np.ones(X+1,bool); s[:2]=False
    for i in range(2,int(X**0.5)+1):
        if s[i]: s[i*i::i]=False
    ns=[];lp=[]
    for p in np.nonzero(s)[0]:
        pk=int(p);L=np.log(p)
        while pk<=X: ns.append(pk);lp.append(L);pk*=int(p)
    return np.array(ns,float),np.array(lp)
def lblock(t):
    z=np.exp(-2*t);s=1/0.25**2;k=1;term=1
    while term>1e-18 and k<20000: term=z**k/(k+0.25)**2;s+=term;k+=1
    return (Cc-np.exp(-t/2)*s)/4
def reduced_mineig(T,dt,eps):
    ns,lp=mangoldt(int(np.exp(T))+2);ln=np.log(ns);w=lp/np.sqrt(ns)*ns**(-eps)
    M=int(round(T/dt));psi=np.empty(M+1)
    for k in range(M+1):
        a=k*dt
        if a==0: psi[k]=0.0;continue
        m=ln<=a+1e-12; psi[k]=8*(np.cosh(a/2)-1)-np.sum(w[m]*(a-ln[m]))+LIN*a+lblock(a)
    i=np.arange(M+1);D=np.abs(i[:,None]-i[None,:]);K=psi[:,None]+psi[None,:]-psi[D]
    return np.linalg.eigvalsh(K[1:,1:]).min()

print("reduced lambda_min at eps=0 (expect ~0.00467185 at T=8):")
for T in [4,6,8,10]:
    print("  T=%2d: %.11f"%(T,reduced_mineig(T,0.04,0.0)))

# bisect crossings at T=8
def bisect(T,dt,lo,hi):
    # find eps in [lo,hi] where mineig crosses 0; assume mineig(lo or hi)<0
    for _ in range(60):
        mid=(lo+hi)/2
        if reduced_mineig(T,dt,mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2
print("\nT=8 crossings (expect ~ -8.27e-7, +2.30e-6):")
print("  eps- =", bisect(8,0.04,-1e-4,0.0))
print("  eps+ =", bisect(8,0.04,0.0,1e-4))
