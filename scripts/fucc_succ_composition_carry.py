#!/usr/bin/env python3
"""Exact checks for FUCC/SUCC composition-polynomial carry identities."""

from itertools import combinations

def compositions(n):
    # cuts among the n-1 gaps
    for mask in range(1 << (n-1)):
        out=[]
        last=0
        for i in range(1,n):
            if mask & (1 << (i-1)):
                out.append(i-last)
                last=i
        out.append(n-last)
        yield tuple(out)

def poly_eval(alpha,m):
    v=0
    for a in alpha:
        v=m*v+a
    return v

def digits_and_carries(alpha,m):
    # ascending raw coefficients are reversed alpha
    raw=list(reversed(alpha))
    d=[]
    carries=[]
    cprev=0
    j=0
    while j < len(raw) or cprev:
        b=raw[j] if j < len(raw) else 0
        t=b+cprev
        dj=t % m
        cj=t // m
        d.append(dj)
        carries.append(cj)
        cprev=cj
        j+=1
    return d,carries

def digit_sum(n,m):
    s=0
    while n:
        s += n % m
        n//=m
    return s

def cut_positions(alpha):
    s=0
    out=[]
    for a in alpha[:-1]:
        s += a
        out.append(s)
    return out

def q_coeffs(alpha):
    # Q=(P-P(1))/(x-1), descending coefficients are prefix cut positions
    return cut_positions(alpha)

def carry_free_count(n,m):
    return sum(all(a < m for a in alpha) for alpha in compositions(n))

def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a

for n in range(1,9):
    cs=list(compositions(n))
    assert len(cs)==2**(n-1)
    byk={}
    for a in cs:
        byk[len(a)-1]=byk.get(len(a)-1,0)+1
    import math
    assert all(byk[k]==math.comb(n-1,k) for k in byk)

    for alpha in cs:
        assert sum(alpha)==n
        for m in range(2,7):
            N=poly_eval(alpha,m)
            d,c=digits_and_carries(alpha,m)
            assert N==sum(x*(m**j) for j,x in enumerate(d))
            assert n-sum(d)==(m-1)*sum(c)
            assert n-digit_sum(N,m)==(m-1)*sum(c)

for n in range(0,12):
    # radix 3 carry-free histories = compositions using 1,2 = F_{n+1}, with n=0 empty history
    got=1 if n==0 else carry_free_count(n,3)
    assert got==fib(n+1), (n,got,fib(n+1))

a=(1,2,2)
assert poly_eval(a,1)==5
assert poly_eval(a,2)==10
assert q_coeffs(a)==[1,3]
d,c=digits_and_carries(a,2)
assert d==[0,1,0,1]
assert sum(c)==3

print("All FUCC/SUCC composition, Pascal, carry, and Fibonacci checks passed.")
print("Example alpha=(1,2,2): P(1)=5, P(2)=10, cuts=[1,3], binary carries=3.")
