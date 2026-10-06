import numpy as np
from scipy.integrate import quad
# Exact local repaired tower D_p(t) = M_p|t| - h_p(t),  h_p = log p sum_r r^k (|t|-k log p)_+, r=p^{-1/2}
# Claim: D_p(t) = int_0^inf (1-cos(xi t))/xi^2 * sigma_p(xi) dxi  with sigma_p>=0 closed form.
def test_prime(p, tmax=6.0):
    r=p**-0.5; lp=np.log(p); Mp=lp*r/(1-r)
    def h(t):
        t=abs(t); s=0.0; k=1
        while k*lp<=t+1e-12 and k<10000:
            s+=r**k*(t-k*lp); k+=1
        return lp*s
    def Dp(t): return Mp*abs(t)-h(t)
    # closed-form spectral density (two equivalent forms); use the rational closed form
    def sigma(xi):
        th=lp*xi
        return (2*lp/np.pi)*(r*(1+r)/(1-r))*(1-np.cos(th))/(1-2*r*np.cos(th)+r*r)
    # (a) sigma>=0 ?
    xis=np.linspace(1e-6,200,20000); svals=sigma(xis)
    print("p=%d: r=%.4f  M_p=%.5f  min sigma_p=%.3e (>=0 ?) "%(p,r,Mp,svals.min()), svals.min()>=-1e-12)
    # (b) reconstruct D_p(t) = int (1-cos xi t)/xi^2 sigma(xi) dxi, compare to direct
    print("   t     D_p direct     D_p from sigma     |diff|")
    for t in [0.5,1.0,2.0,3.5]:
        val,_=quad(lambda xi:(1-np.cos(xi*t))/xi**2*sigma(xi),1e-9,np.inf,limit=400)
        d=Dp(t)
        print("   %.1f   %+.6f      %+.6f       %.2e"%(t,d,val,abs(d-val)))
for p in [2,3,5]:
    test_prime(p); print()
print("sigma_p(xi) = (2 log p/pi) (1-cos(log p xi)) P_r(log p xi)/(1-r^2) * (r(1+r^2)/...)  => (1-cos) * Poisson kernel")
print("i.e. local square B_p(t)(xi)=(e^{i xi t}-1)/xi * sqrt(sigma_p(xi)); high-pass (1-cos) x Euler-whitening P_r.")
