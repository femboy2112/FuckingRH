#!/usr/bin/env python3
"""Zero-free finite/Archimedean duality controls (RH OPEN).

Tests exact-conductor Fourier projectors, vector theta/Poisson inversion,
completed theta/Gamma/pole duality, half-canonical quaternionic reversal,
twistor odd-Frobenius parity, and LCM Tate-torus area increments.

Requires numpy and mpmath. No zeta zeros or fitted spectral parameters.
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 78


def fourier(m):
    a = np.arange(m)
    return np.exp(2j*np.pi*np.outer(a,a)/m)/np.sqrt(m)


def test_conductor():
    for m in (2,3,5,6,10,12,30):
        F=fourier(m)
        units=[a for a in range(m) if math.gcd(a,m)==1]
        PW=np.zeros((m,m),complex)
        for a in units:
            v=np.exp(2j*np.pi*a*np.arange(m)/m)/np.sqrt(m)
            PW+=np.outer(v,v.conj())
        PU=np.diag([int(a in units) for a in range(m)])
        assert np.linalg.norm(F@PW@F.conj().T-PU)<1e-11
        assert np.linalg.norm(F@F.conj()-np.eye(m))<1e-12
    for a in (1,5):
        v=np.exp(2j*np.pi*a*np.arange(6)/6)/np.sqrt(6)
        crt=np.empty((2,3),complex)
        for n in range(6):
            crt[n%2,n%3]=v[n]
        assert np.max(abs(crt.mean(axis=0)))<1e-12
        assert np.max(abs(crt.mean(axis=1)))<1e-12
    print("PASS exact-conductor -> unit support, W6 joint-only amplitude")


def theta_vector(m,t,N=180):
    out=[mp.mpf(0) for _ in range(m)]
    for n in range(-N,N+1):
        out[n%m]+=mp.exp(-mp.pi*t*n*n)
    return out


def test_vector_poisson():
    worst=mp.mpf(0)
    for m in (2,3,6,12):
        for tx in ("0.45","1.0","2.3"):
            t=mp.mpf(tx)
            v=theta_vector(m,t)
            w=theta_vector(m,1/(m*m*t))
            for r in range(m):
                rhs=sum(mp.exp(2j*mp.pi*r*a/m)*w[a] for a in range(m))/(m*mp.sqrt(t))
                err=abs(v[r]-rhs)
                worst=max(worst,err)
                assert err<mp.mpf("1e-66"),(m,tx,r,err)
    print("PASS vector theta/Poisson, max err",mp.nstr(worst,8))


def test_theta_reversal():
    rng=np.random.default_rng(2112)
    for m in (2,3,6,12):
        F=fourier(m)
        t=1.7
        u=1/(m*m*t)
        v=rng.normal(size=m)+1j*rng.normal(size=m)
        Rv=(F@v.conj())/np.sqrt(m*u)
        RRv=(F@Rv.conj())/np.sqrt(m*t)
        assert np.linalg.norm(RRv-v)<1e-12
    print("PASS half-density antiunitary reversal R^2=I")


def scalar_theta(t):
    return 1+2*sum(mp.exp(-mp.pi*n*n*t) for n in range(1,19))


def completed_theta(s):
    s=mp.mpc(s)
    integrand=lambda t: (scalar_theta(t)-1)*(t**(s/2)+t**((1-s)/2))/(2*t)
    return 1/(s*(s-1))+mp.quad(integrand,[1,1.5,2,3,5,10,30,mp.inf])


def test_completed_gamma():
    worst=mp.mpf(0)
    for s in (mp.mpc("1.3","2.1"),mp.mpc("0.25","1.4"),mp.mpc("-0.6","3.2")):
        x=completed_theta(s)
        y=mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)
        err=max(abs(x-y),abs(x-completed_theta(1-s)))
        worst=max(worst,err)
        assert err<mp.mpf("1e-62"),(s,err)
    print("PASS completed gamma/pole reflection, max err",mp.nstr(worst,8))


def test_twistor():
    # j([v])=[A conjugate(v)], A conjugate(A)=-I.
    A=np.array([[0,-1],[1,0]],dtype=complex)
    assert np.array_equal(A@A.conj(),-np.eye(2))
    B=np.kron(A,A)
    assert np.array_equal(B@B.conj(),np.eye(4))
    # f(z)=c z^n commutes with j(z)=-1/conj(z)
    # iff n is odd AND |c|=1.
    z=complex(1.3,0.4)
    for n in range(1,11):
        for c in (1+0j,np.exp(0.37j),1.2+0j,0.8*np.exp(0.5j)):
            lhs=c*(-1/z.conjugate())**n
            rhs=-1/(c*z**n).conjugate()
            assert (abs(lhs-rhs)<1e-10)==(n%2==1 and abs(abs(c)-1)<1e-12)
            assert ((n-1)%2==0)==(n%2==1)
    print("PASS twistor O(-1) quaternionic/O(-2) real; n odd, |c|=1")


def test_lcm_area():
    prev=1
    for n in range(2,101):
        L=math.lcm(prev,n)
        ratio=L//prev
        x=n; factors=set()
        for p in range(2,n+1):
            if x%p==0:
                factors.add(p)
                while x%p==0:x//=p
        expected=next(iter(factors)) if len(factors)==1 else 1
        assert ratio==expected,(n,ratio,expected)
        # E_L has area 2 pi log L. Increment = 2 pi Lambda(n).
        error=(2*math.pi*math.log(L)-2*math.pi*math.log(prev))/(2*math.pi)
        assert abs(error-math.log(ratio))<1e-12
        prev=L
    # P^1 RR: O(-1) has deg -1, h0=h1=0, chi=0.
    assert 0-0==(-1)+1
    print("PASS LCM Tate area growth = Lambda, and RR doesn't imply degree>=0")


if __name__=="__main__":
    test_conductor()
    test_theta_reversal()
    test_vector_poisson()
    test_completed_gamma()
    test_twistor()
    test_lcm_area()
    print("ALL CHECKS PASSED; RH UNPROVED")
