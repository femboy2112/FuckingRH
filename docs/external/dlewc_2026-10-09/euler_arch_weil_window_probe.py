#!/usr/bin/env python3
"""Small zero-free finite-window Weil-form evaluator for degree-one sources.

Compact C1 polynomial windows (a numerical form-core calibration, not full Cc∞).
No calls to zeta-zero functions, no M_zeros, no fitted scattering data.
Quadrature results are exploratory, not rigorous interval bounds or RH evidence.
Requires numpy/scipy and euler_arch_rigidity_probe.py in the same directory.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import spherical_jn, digamma
from numpy.polynomial.legendre import leggauss
from euler_arch_rigidity_probe import (chi5, dh5, zeta_coeff,
    logarithmic_derivative_coeff)

XG, WG = leggauss(128)

def shape(y):
    """Fourier of (1-u^2)^2 1_{|u|<1}, with e^{+iyu}."""
    y=complex(y)
    if abs(y) < 1e-3:
        return 16/15 - 8*y*y/105 + 2*y**4/945
    return 16*spherical_jn(2,y)/(y*y)

def ft(L, freq, z):
    return L*shape(L*(complex(z)+freq))

def phi(L, fi, fj, shift):
    """Cross autocorrelation of two polynomial bump modes with e^(+i freq x)."""
    u=float(shift)
    left=max(-L,-L-u)
    right=min(L,L-u)
    if right <= left:
        return 0j
    xs=(right+left)/2+(right-left)/2*XG
    y=xs+u
    bx=(1-(xs/L)**2)**2
    by=(1-(y/L)**2)**2
    vals=by*bx*np.exp(1j*(fi*y-fj*xs))
    return complex((right-left)/2*np.dot(WG,vals))

def inner(L,fi,fj):
    return phi(L,fi,fj,0)

def gamma_symbol(t,q,parity):
    return (math.log(q/math.pi)+np.real(digamma((1+2*parity)/4+0.5j*t)))

def arch_form(L,fi,fj,q,parity,polar):
    def integrand(t):
        return ft(L,fi,t)*ft(L,fj,t).conjugate()*gamma_symbol(t,q,parity)/(2*math.pi)
    # The frequency modes are modest in this calibration. Compact basis decays O(t^-3).
    re=quad(lambda t:integrand(t).real,-700,700,epsabs=3e-9,limit=300)[0]
    im=quad(lambda t:integrand(t).imag,-700,700,epsabs=3e-9,limit=300)[0]
    out=complex(re,im)
    if polar:
        z=0.5j
        out+=ft(L,fi,z)*ft(L,fj,-z).conjugate()
        out+=ft(L,fi,-z)*ft(L,fj,z).conjugate()
    return out

def matrix(L, freqs, a, q, parity, polar=False, with_edges=True):
    dim=len(freqs)
    c=logarithmic_derivative_coeff(a,math.floor(math.exp(2*L)))
    A=np.zeros((dim,dim),complex)
    K=np.zeros_like(A)
    Edge=np.zeros_like(A)
    M=np.zeros_like(A)
    weightsum=0
    primitive=[]
    for n in range(2,len(c)):
        if abs(c[n]) < 1e-10:continue
        w=c[n]/math.sqrt(n)
        primitive.append((n,w))
    # Edges are only legitimate for degree-one unitary characters, using 
    # the exact positive weight log(p)/sqrt(p^k), not complex log-derivative c.
    for i,fi in enumerate(freqs):
        for j,fj in enumerate(freqs):
            A[i,j]=arch_form(L,fi,fj,q,parity,polar)
            M[i,j]=inner(L,fi,fj)
            K[i,j]=sum(w*phi(L,fi,fj,math.log(n))+
                     w.conjugate()*phi(L,fi,fj,-math.log(n)) for n,w in primitive)
            if with_edges:
                e=0j
                for n,w in primitive:
                    if n==0:continue
                    p=next((p for p in range(2,n+1) if n%p==0),None)
                    if p is None:continue
                    r=n
                    while r%p==0:r//=p
                    if r!=1:raise ValueError('non-prime-power source cannot be an edge Gram')
                    alpha=a(n)
                    if abs(alpha)!=0 and abs(abs(alpha)-1)>1e-10:
                        raise ValueError('nonunit character cannot use 2S edge formula')
                    if not alpha: continue
                    positive_weight=math.log(p)/math.sqrt(n)
                    e+=positive_weight*(2*M[i,j]-alpha*phi(L,fi,fj,math.log(n))-
                        alpha.conjugate()*phi(L,fi,fj,-math.log(n)))
                Edge[i,j]=e
    if with_edges:
        weightsum=sum(math.log(next(p for p in range(2,n+1) if n%p==0))/math.sqrt(n)
                      for n,_ in primitive)
    return A,K,M,Edge,weightsum

def main():
    L=1.22
    modes=[0,2.3]
    for label,a,q,parity,polar,edges in [
        ('zeta',zeta_coeff,1,0,True,True),
        ('chi5',chi5,5,1,False,True),
        ('Davenport-Heilbronn',dh5,5,1,False,False)]:
        A,K,M,E,S=matrix(L,modes,a,q,parity,polar,edges)
        Q=A-K
        herm=np.linalg.norm(Q-Q.conj().T)
        eig=np.linalg.eigvalsh((Q+Q.conj().T)/2)
        print(f'{label}: full Q hermitian residual={herm:.2e}; sample basis eigenvalues={eig}')
        assert herm < 1e-7
        if edges:
            residual=np.linalg.norm(Q-(A-2*S*M+E))
            print(f'  corrected prime-edge+arch minus 2S residual={residual:.2e}')
            assert residual<1e-9
    print('PASS: finite-window full source form assembled, no zeros read; no all-horizon sign theorem.')

if __name__ == '__main__':main()
