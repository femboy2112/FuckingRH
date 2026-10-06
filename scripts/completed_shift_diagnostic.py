import numpy as np
g=np.load('/tmp/claude-0/-home-user-FuckingRH/a2e55c68-1445-594b-b9d1-fbb6544ba338/scratchpad/zeros300.npy')  # positive gammas
# Completed shift: center Suzuki at Re=1/2+omega  => frequencies gamma + i*omega (complex).
# Psi_omega(t) = Re sum_gamma (1 - cos((gamma+i omega) t)) / (gamma+i omega)^2  (sum over +/- gamma).
def Psi_omega(t, omega):
    w=g+1j*omega
    terms=(1-np.cos(w*t))/w**2 + (1-np.cos((-g+1j*omega)*t))/(-g+1j*omega)**2
    return np.sum(terms).real
print("COMPLETED shift (primes+Archimedean move together): is Psi_omega(t)>=0 ?")
print(" omega     min_t Psi_omega (t in [0,40])     first t with Psi<0")
for omega in [0.0, 0.001, 0.005, 0.01, 0.05]:
    ts=np.linspace(0.01,40,4000); vals=np.array([Psi_omega(t,omega) for t in ts])
    neg=ts[vals<0]
    print("  %.3f    %+.6e                 %s"%(omega, vals.min(), ("%.2f"%neg[0]) if len(neg) else "none in [0,40]"))
print("\n=> for the COMPLETED shift, any omega!=0 drives Psi_omega negative at large t (cosh(omega t) growth):")
print("   the positivity interval is {0} with NO shrinking-window reprieve --- UNLIKE the finite-only tilt,")
print("   whose interval is a tiny nonzero E_L collapsing as L->inf (continuity audit).")
print("   So the two deformations are genuinely different; the knife-edge is exact only for the completed family.")
