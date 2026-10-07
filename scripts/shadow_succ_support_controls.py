#!/usr/bin/env python3
"""
Exact controls for shadow-SUCC loop support geometry.

No zeta zeros are used.
"""

from fractions import Fraction
from math import gcd, lcm, log, sqrt
from dataclasses import dataclass


def gcd_many(vals):
    xs=[abs(int(x)) for x in vals if x]
    if not xs:
        return 1
    g=xs[0]
    for x in xs[1:]:
        g=gcd(g,x)
    return g


@dataclass(frozen=True)
class Affine:
    a:int
    b:int
    c:int
    def __post_init__(self):
        if self.a <= 0 or self.c <= 0:
            raise ValueError
        if gcd_many((self.a,self.b,self.c)) != 1:
            raise ValueError("not primitive")
    def matrix(self):
        return ((self.a,self.b),(0,self.c))
    def __call__(self,x):
        return Fraction(self.a*x+self.b,self.c)


def mm(A,B):
    return (
        (A[0][0]*B[0][0]+A[0][1]*B[1][0],
         A[0][0]*B[0][1]+A[0][1]*B[1][1]),
        (A[1][0]*B[0][0]+A[1][1]*B[1][0],
         A[1][0]*B[0][1]+A[1][1]*B[1][1]),
    )


def primitive(A):
    k=gcd_many((A[0][0],A[0][1],A[1][0],A[1][1]))
    P=tuple(tuple(v//k for v in row) for row in A)
    return k,P


def compose(f,g):
    k,P=primitive(mm(f.matrix(),g.matrix()))
    return Affine(P[0][0],P[0][1],P[1][1]),k


def product(forms):
    P=((1,0),(0,1))
    for f in forms:
        P=mm(f.matrix(),P)
    return P


def factor(n):
    x=n; out={}; p=2
    while p*p<=x:
        while x%p==0:
            out[p]=out.get(p,0)+1; x//=p
        p=3 if p==2 else p+2
    if x>1: out[x]=out.get(x,0)+1
    return out


def beta(n):
    if n==1:return 1
    return max(p**k for p,k in factor(n).items())


def L(N):
    z=1
    for n in range(1,N+1): z=lcm(z,n)
    return z


def vm(n):
    fs=factor(n)
    return log(next(iter(fs))) if len(fs)==1 else 0.0


def jet_coeff(n):
    """coefficient of omega^r in first nonzero term of b_omega(n)"""
    if n==1:return 1.0
    fs=factor(n)
    z=1.0
    for p in fs:z*=log(p)
    return (2**len(fs))*z/sqrt(n)


def check_user_loop():
    fs=[Affine(4,1,1),Affine(3,1,8),Affine(2,-1,3)]
    P=product(fs)
    assert P==((24,0),(0,24))
    for x in range(1,30,2):
        y=Fraction(x)
        for f in fs:y=f(y)
        assert y==x
    print("user loop: primitive central holonomy=24, integer-prefix support=odd class")
    print("holonomy beta(24)=",beta(24),"support-rank=",len(factor(24)),
          "top jet coeff=",jet_coeff(24))


def check_n_loops():
    for n in range(1,101):
        up=Affine(n,1,1); down=Affine(1,-1,n)
        assert product([up,down])==((n,0),(0,n))
    print("canonical loops: D_n U_n=nI for n<=100")


def check_cocycle():
    F=[Affine(2,1,3),Affine(3,-2,5),Affine(5,1,2),Affine(7,-3,4)]
    cnt=0
    for f in F:
        for g in F:
            for h in F:
                fg,k1=compose(f,g)
                left,k2=compose(fg,h)
                gh,k3=compose(g,h)
                right,k4=compose(f,gh)
                assert left==right
                assert k1*k2==k3*k4
                cnt+=1
    print("content cocycle:",cnt,"triples exact")


def check_lcm():
    last=1
    for n in range(1,121):
        cur=L(n)
        lhs=log(cur/last)
        rhs=vm(n)
        assert abs(lhs-rhs)<1e-12
        last=cur
        assert n % 1 == 0
        assert L(beta(n)) % n == 0
        if beta(n)>1:
            assert L(beta(n)-1) % n != 0
    print("LCM derivative=Lambda and beta minimality exact through 120")


def check_factorial_lcm_primorial(N=12):
    fact=1
    for n in range(1,N+1):fact*=n
    prim=1
    for p in factor(L(N)): prim*=p
    print(f"N={N}: factorial={fact}, LCM={L(N)}, radical(LCM)={prim}")


def main():
    check_user_loop()
    check_n_loops()
    check_cocycle()
    check_lcm()
    check_factorial_lcm_primorial()


if __name__=="__main__":
    main()
