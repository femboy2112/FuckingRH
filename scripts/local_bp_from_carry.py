import numpy as np
from sympy import primerange, factorint

# ===== Section 7: carry-depth records = von Mangoldt =====
# R_p(N)=v_p(lcm(1..N))=floor(log_p N); R_p(N)-R_p(N-1)=1 iff N=p^k; sum_p log p * [record step]=Lambda(N)
def vmax(p,N): 
    k=0; pk=p
    while pk<=N: k+=1; pk*=p
    return k
def Lambda(N):
    f=factorint(N)
    return np.log(list(f.keys())[0]) if len(f)==1 else 0.0
print("=== Section 7: carry-depth record update = von Mangoldt ===")
bad=0
for N in range(2,300):
    s=0.0
    for p in primerange(2,N+1):
        s+=np.log(p)*(vmax(p,N)-vmax(p,N-1))
    if abs(s-Lambda(N))>1e-9: bad+=1
print("  sum_p log p [R_p(N)-R_p(N-1)] == Lambda(N) for N=2..299, violations:",bad)

# ===== Section 12: half-density p^{-1/2} forced by Haar cylinder; AR(1) depth covariance =====
# phi_{p,k}=p^{k/2} 1_{p^k Z_p}; <phi_k,phi_l>=p^{-|k-l|/2}. r=p^{-1/2} = cylinder amplitude ratio.
print("\n=== Section 12: Haar cylinder forces r=p^{-1/2}; <phi_k,phi_l>=p^{-|k-l|/2} ===")
for p in [2,3,5]:
    K=8; cov=np.array([[p**(-0.5*abs(k-l)) for l in range(K)] for k in range(K)])
    # built from Haar: <1_{p^k},1_{p^l}>=p^{-max(k,l)}; normalized p^{k/2}p^{l/2}p^{-max}=p^{-|k-l|/2}
    haar=np.array([[p**(0.5*k)*p**(0.5*l)*p**(-max(k,l)) for l in range(K)] for k in range(K)])
    print("  p=%d: r=p^{-1/2}=%.4f ; ||cov - Haar-built||=%.1e (AR(1)/depth chain)"%(p,p**-0.5,np.linalg.norm(cov-haar)))

# ===== Section 11: local B_p as carry-response filter  B_p = c_p (I-U)(I-r U)^{-1} =====
# On the depth chain, U = depth-shift (one p-adic level = one carry wrap). Symbol z=e^{i theta}.
# |H_p(z)|^2 = |1-z|^2/|1-r z|^2 = 2(1-cos th)/(1-2r cos th + r^2).  Compare to C90 sigma_p.
print("\n=== Section 11: B_p=(I-U)(I-r U)^{-1} reproduces C90 sigma_p (carry-response filter) ===")
for p in [2,3,5,7]:
    r=p**-0.5; lp=np.log(p)
    th=np.linspace(1e-4,np.pi,400)
    H2=np.abs(1-np.exp(1j*th))**2/np.abs(1-r*np.exp(1j*th))**2        # |carry-filter|^2
    # C90 closed form: sigma_p = (2 log p/pi) r(1+r)/(1-r) (1-cos th)/|1-r e^{i th}|^2
    sigma=(2*lp/np.pi)*(r*(1+r)/(1-r))*(1-np.cos(th))/np.abs(1-r*np.exp(1j*th))**2
    # ratio sigma/H2 should be constant = (2 log p/pi) r(1+r)/(1-r) / 2
    ratio=sigma/H2
    const_pred=(2*lp/np.pi)*(r*(1+r)/(1-r))/2
    print("  p=%d: sigma_p/|H_p|^2 const? mean=%.5f std=%.1e  pred c_p^2=%.5f"%(p,ratio.mean(),ratio.std(),const_pred))
print("  => sigma_p = c_p^2 |H_p|^2, c_p^2=(log p/pi) r(1+r)/(1-r).  B_p=c_p(I-U_depth)(I-p^{-1/2}U_depth)^{-1}:")
print("     (I-U_depth)=carry/wrap innovation, (I-p^{-1/2}U_depth)^{-1}=geometric depth memory (Euler whitening).")
