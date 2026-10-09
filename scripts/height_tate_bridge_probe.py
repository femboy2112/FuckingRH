#!/usr/bin/env python3
"""Source-only probes for the sharp arithmetic-height/Tate bridge.
No zeta zero inputs; finite checks are not RH positivity tests.
Dependencies: numpy, mpmath (both already in the repository requirements).
"""
from fractions import Fraction
from math import cos, exp, gcd, log, pi, sin, sqrt
import mpmath as mp
import numpy as np


def height(r):
    r = Fraction(r)
    return log(max(r.numerator, r.denominator))


def totient(n):
    return sum(gcd(k, n) == 1 for k in range(1, n+1))


def rational_states(M):
    return [Fraction(a,b) for a in range(1,M+1) for b in range(1,M+1) if gcd(a,b)==1]


def finite_height_mass(M, tau):
    return sum(exp(-2*tau*height(r)) for r in rational_states(M))


def totient_height_mass(M, tau):
    return 1 + 2*sum(totient(n)*n**(-2*tau) for n in range(2,M+1))


def exact_mass(tau):
    if tau<=1: raise ValueError('Unbounded regime: exact HS mass diverges')
    return 2*mp.zeta(2*tau-1)/mp.zeta(2*tau)-1


def tate_overlap(r, s):
    return sqrt(2*float(r)*float(s)/(float(r)**2+float(s)**2))


def tate_direct_overlap(r, s):
    r, s = mp.mpf(r.numerator)/r.denominator, mp.mpf(s.numerator)/s.denominator
    a,b=mp.log(r),mp.log(s)
    c=mp.power(2,mp.mpf('0.75'))
    return c*c*mp.exp(-(a+b)/2)*mp.quad(lambda x: mp.exp(-mp.pi*x*x*(mp.exp(-2*a)+mp.exp(-2*b))), [0,1,mp.inf])


def tate_fourier_gamma(t):
    t=mp.mpf(t)
    return mp.power(2,-mp.mpf('0.25'))*mp.power(mp.pi,-mp.mpf('0.25')+1j*t/2)*mp.gamma(mp.mpf('0.25')-1j*t/2)


def tate_fourier_grid(t):
    # Independent trapezoidal integration in log coordinate; truncation at -120 and 3.
    u=np.linspace(-120,3,180001)
    g=2**.75*np.exp(u/2-np.pi*np.exp(2*u))
    return np.trapezoid(g*np.exp(-1j*t*u),u)


def near_unit_bessel(M,tau,profile='box',eps=.2):
    total=0.
    for b in range(2,M+1):
        for k in range(1,int(eps*b)+1):
            if gcd(k,b)!=1: continue
            r=Fraction(b+k,b)
            shift=log(float(r))
            overlap=max(0.,1-abs(shift)) if profile=='box' else exp(-shift*shift/4)
            total+=exp(-2*tau*height(r))*overlap**2
    return total


def cocycle(tau,q,r):
    return exp(tau*(height(q*r)-height(r)))


def character_mixture_atom_six(a,b):
    # Primitive quartic chi mod 5 has chi(2)=i, chi(3)=-i, chi(6)=1.
    assert abs(a+b-1)<1e-12
    a2=1j*(a-b);a3=-1j*(a-b);a6=1
    return (a6-a2*a3)*log(6)


def clock_shift_defect(eta):
    # Norm of difference of two normalized log-Gaussian shifts.
    d=eta*log(2)
    return sqrt(2*(1-exp(-d*d/4)))


def run():
    mp.mp.dps=55
    print('SOURCE-ONLY HEIGHT/TATE BRIDGE — no spectral-zero input')
    for M in (4,8,16):
        n=len(rational_states(M))
        expected=1+2*sum(totient(k) for k in range(2,M+1))
        mass=finite_height_mass(M,1.25)
        independent=totient_height_mass(M,1.25)
        assert n==expected and abs(mass-independent)<1e-10
        print(f'COUNT M={M} states={n} mass={mass:.12f} independent={independent:.12f}')
    print(f'INFINITE HS^2 tau=1.25 {float(exact_mass(1.25)):.12f}')
    for r,s in [(Fraction(1),Fraction(2)),(Fraction(2,3),Fraction(5,4)),(Fraction(17,16),Fraction(33,32))]:
        direct=float(tate_direct_overlap(r,s)); closed=tate_overlap(r,s)
        assert abs(direct-closed)<2e-14
        print(f'TATE r={r},s={s}: direct={direct:.12f}, closed={closed:.12f}')
    for t in [0,2.5,14.25]:
        direct=tate_fourier_grid(t); gamma=complex(tate_fourier_gamma(t));res=abs(direct-gamma)
        assert res<1e-9
        print(f'GAMMA Fourier t={t}: residual={res:.3g}')
    for M in (32,64,128,256):
        v05=near_unit_bessel(M,.5,profile='box')
        v1=near_unit_bessel(M,1.,profile='box')
        v125=near_unit_bessel(M,1.25,profile='box')
        print(f'BOX HOLDOUT M={M}: tau=.5 {v05:.6f}, tau=1 {v1:.6f}, tau=1.25 {v125:.6f}')
    for q in [Fraction(2),Fraction(3),Fraction(6),Fraction(2,3)]:
        for r in [Fraction(1),Fraction(2,3),Fraction(5,4)]:
            w=lambda x:exp(-1.25*height(x))
            assert abs(cocycle(1.25,q,r)*w(q*r)-w(r))<5e-15
    print('COVARIANCE: 12 exact rational tests PASS')
    for a,b in [(1.,0.),(.6,.4)]:
        got=character_mixture_atom_six(a,b)
        assert abs(got-4*a*b*log(6))<1e-13
        print(f'SOURCE mix a={a} b={b} b6={got.real:.12f}')
    for eta in (0,.01,.1):
        print(f'CLOCK shift log2 eta={eta}: norm defect={clock_shift_defect(eta):.12f}')
    for tau in (1.1,1.01,1.001):
        mass=float((tau-1)*exact_mass(tau))
        fixed=sqrt(tau-1)
        print(f'CRITICAL limit tau={tau}: normalized mass²={mass:.9f} fixed label norm={fixed:.9f}')
    print('ALL CHECKS PASSED (FINITE / DIRECT QUADRATURE; NOT AN RH CLAIM)')

if __name__=='__main__': run()
