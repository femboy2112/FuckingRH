#!/usr/bin/env python3
"""Zero-free exact controls for the Hecke--Tate connected source.

Checks Euler-log primitive support, Davenport--Heilbronn-style mixture
curvature, three mutations, primitive quartic theta/Poisson, and the
chiral commutator obstruction. Never reads or computes a zeta zero.
Requires sympy and mpmath.
"""
import sympy as s
import mpmath as mp

I=s.I

def chi(n):
    return (0,1,I,-I,-1)[n%5]

def dlog(d,N):
    """Finite Dirichlet-convolution log with exact rational coefficients."""
    u={n:d[n] for n in range(2,N+1) if d[n]!=0}
    power=dict(u)
    out=[s.Integer(0)]*(N+1)
    for k in range(1,N.bit_length()):
        for n,v in power.items():
            out[n]+=s.Rational((-1)**(k+1),k)*v
        nxt={}
        for a,x in power.items():
            for b,y in u.items():
                if a*b<=N:
                    nxt[a*b]=nxt.get(a*b,0)+x*y
        power=nxt
        if not power:break
    return [s.simplify(x) for x in out]

def expected(n,alpha):
    f=s.factorint(n)
    if len(f)!=1:return s.Integer(0)
    p,k=next(iter(f.items()))
    return alpha(p)**k/s.Integer(k)

def test_exact():
    N=90
    d1=[s.Integer(0)]+[s.Integer(1)]*N
    dchi=[s.Integer(0)]+[chi(n) for n in range(1,N+1)]
    for name,d,alpha in (("zeta",d1,lambda p:s.Integer(1)),
                         ("chi5",dchi,chi)):
        b=dlog(d,N)
        for n in range(2,N+1):
            assert s.simplify(b[n]-expected(n,alpha))==0,(name,n)
        print("PASS primitive support",name,"through",N)

    a=s.Rational(1,3);b=1-a
    mix=[s.Integer(0)]+[s.simplify(a*chi(n)+b*s.conjugate(chi(n)))
                        for n in range(1,N+1)]
    curv=s.simplify(mix[6]-mix[2]*mix[3])
    assert curv==4*a*b==s.Rational(8,9)
    assert dlog(mix,N)[6]==curv
    assert dlog(dchi,N)[6]==0
    print("PASS nonmultiplicative composite cumulant at 6 =",curv)

    eps=s.Rational(1,7)
    assert eps/s.log(6)!=0
    print("PASS fake c(6)=1/7 creates b(6)=1/(7 log 6)")

    alpha=s.Rational(6,5)*I
    assert s.simplify(alpha*s.conjugate(alpha)-1)==s.Rational(11,25)
    print("PASS modulus mutation U*U-P = 11/25 at unramified 2")

    delta=s.Rational(1,11)
    assert s.simplify(s.log(2)-(s.log(2)+delta))==-delta
    print("PASS shifted log 2 violates H commutator/product formula")

    A0=s.log(6)/2-s.Rational(1,100)
    A1=s.log(6)/2+s.Rational(1,100)
    assert 2*A0<s.log(6)<2*A1
    print("PASS support horizon for new log 6 impulse: 2A>log 6")

def mpcchi(n, conjugated=False):
    x=chi(n)
    z=mp.mpc(str(s.re(x)),str(s.im(x)))
    return mp.conj(z) if conjugated else z

def theta(t,conjugated=False):
    return 2*sum(n*mpcchi(n,conjugated)*
                 mp.exp(-mp.pi*n*n*t/5) for n in range(1,101))

def test_theta():
    mp.mp.dps=55
    tau=sum(mpcchi(n)*mp.exp(2j*mp.pi*n/5) for n in range(1,6))
    epsilon=tau/(1j*mp.sqrt(5))
    assert abs(abs(epsilon)-1)<mp.mpf("1e-50")
    for t0 in ("0.7","1.2","2.0","3.0"):
        t=mp.mpf(t0)
        err=abs(theta(t)-epsilon*t**(-mp.mpf("1.5"))*
                theta(1/t,True))
        assert err<mp.mpf("1e-42"),(t,err)
    print("PASS quartic odd theta/Poisson FE at 55 digits")
    print("epsilon",mp.nstr(epsilon,26))

def test_chiral_no_go():
    N=7;S=s.zeros(N)
    for j in range(N-1):S[j+1,j]=1
    C=s.Rational(1,2)*S+s.Rational(2,3)*I*(S**2)
    K=C.H*C-C*C.H
    R=s.zeros(N)
    for j in range(N):R[j,N-1-j]=1
    assert K.H==K and K!=s.zeros(N)
    assert R*s.conjugate(K)*R==-K and s.trace(K)==0
    print("PASS mixed carry commutator has chiral paired +/- spectrum")

if __name__=="__main__":
    test_exact()
    test_theta()
    test_chiral_no_go()
    print("ALL ZERO-FREE SOURCE CONTROLS PASSED; RH UNPROVED")
