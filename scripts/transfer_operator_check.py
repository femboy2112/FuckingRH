import numpy as np
# The directive's "non-diagonal" transfer operator A(s) = sum_p p^{-s} T_{log p} on a periodic
# log-time grid (T_a = shift by a). Is it genuinely noncommutative, or still RH-inert?
N=4096; L=40.0; dx=L/N            # log-time grid, periodic
xs=np.arange(N)*dx
def primes_upto(X):
    s=np.ones(X+1,bool); s[:2]=False
    for i in range(2,int(X**0.5)+1):
        if s[i]: s[i*i::i]=False
    return list(np.nonzero(s)[0])
P=primes_upto(20000)
s=0.8
# A as a convolution kernel: shift by log p (nearest grid), weight p^{-s}
ker=np.zeros(N)
for p in P:
    j=int(round(np.log(p)/dx))%N
    ker[j]+=p**(-s)
# A commutes with its adjoint? convolution operators all commute (circulant) -> Fourier diagonal.
Ahat=np.fft.fft(ker)              # eigenvalues of the circulant A
# symbol should be P(s - i xi) = sum_p p^{-s+i xi}; check at a few frequencies
xis=2*np.pi*np.fft.fftfreq(N,d=dx)
def primezeta_symbol(xi): return np.sum(np.array(P,float)**(-s+1j*xi))
print("=== directive transfer operator A=sum_p p^{-s} T_{log p} ===")
print(" A is a CIRCULANT/convolution => normal => Fourier-diagonal => COMMUTATIVE.")
print(" Check eigenvalues == prime-zeta symbol P(s-i xi):")
for k in [10,50,200,1000]:
    print("   xi=%.3f : A_hat=%.4f%+.4fj   P(s-i xi)=%.4f%+.4fj"%(
        xis[k],Ahat[k].real,Ahat[k].imag, primezeta_symbol(xis[k]).real, primezeta_symbol(xis[k]).imag))
# commutator with a RANDOM circulant ~ 0; with SUCC (irregular log-steps) != 0
# SUCC in log-time: n -> n+1 maps log n -> log(n+1); irregular. Build succ on integer states instead.
print("\n commutator norm [A, A^*] (should be ~0, A normal):", end=" ")
# circulant => [A,A^*]=0 exactly
print("0 exactly (circulant).")
print("\n=> the 'non-diagonal' transfer operator is STILL commutative (convolution). RH-inert.")
print("   Genuine noncommutativity requires SUCC's IRREGULAR log-steps log(n+1)-log n,")
print("   i.e. the additive-multiplicative incompatibility (the braid V_m S=S^m V_m).")
# demonstrate succ irregularity breaks convolution structure:
ns=np.arange(1,30); steps=np.log(ns+1)-np.log(ns)
print("   succ log-steps log(n+1)-log n for n=1..8:", np.round(steps[:8],4), " (nonuniform => not a convolution)")
