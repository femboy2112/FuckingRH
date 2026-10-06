#!/usr/bin/env python3
"""Exact finite checks for factor-square / moving sqrt-window geometry."""

from math import isqrt

def primes_upto(n):
    out=[]
    for x in range(2,n+1):
        ok=True
        for d in range(2,isqrt(x)+1):
            if x%d==0:
                ok=False
                break
        if ok:
            out.append(x)
    return out

PRIMES=set(primes_upto(500))

def factor_defect(x):
    return [(a,x//a) for a in range(2,isqrt(x)+1) if x%a==0]

def prime_clock_defect(x):
    return [(p,x//p) for p in PRIMES if p*p<=x and x%p==0]

# 1. Prime iff no interior factor pair in triangular half.
for x in range(2,500):
    isprime=(x in PRIMES)
    assert (len(factor_defect(x))==0) == isprime
    assert (len(prime_clock_defect(x))==0) == isprime
print("Prime iff triangular interior factor defect vanishes: verified x<500.")

# 2. sqrt window is exactly a<=b on ab=x.
for x in range(1,500):
    for a in range(1,x+1):
        if x%a:
            continue
        b=x//a
        assert (a<=b) == (a*a<=x)
print("a<=b iff a^2<=x on every factor fiber: verified x<500.")

# 3. Prime-clock moving window changes only at prime squares.
prev=set()
events=[]
for x in range(1,500):
    active={p for p in PRIMES if p*p<=x}
    added=active-prev
    if added:
        events.append((x,sorted(added)))
        assert all(x==p*p for p in added)
    prev=active
print("Prime-clock activation events:",events[:10])
print("Active prime window changes only when SUCC crosses p^2.")

# 4. Cone/SUCC commutator support: gate(a,x)=1[a^2<=x].
boundary=[]
for x in range(1,200):
    for a in range(1,30):
        delta=int(a*a<=x+1)-int(a*a<=x)
        if delta:
            boundary.append((x+1,a))
            assert x+1==a*a
print("Cone gate discrete derivative supported exactly on square boundary:",boundary[:12])

# 5. Log-free exact centered geometry: on ab=x, comparing a and b is equivalent
# to choosing one sign of relative coordinate; diagonal iff perfect square.
for x in range(1,500):
    diag=[a for a in range(1,isqrt(x)+1) if a*a==x]
    assert bool(diag) == (isqrt(x)**2==x)
print("Diagonal fixed locus projects exactly to perfect squares.")

print("All factor-square / moving-window checks passed.")
print("RH remains open: this is a lifted positive geometry, not yet a completed Weil identity.")
