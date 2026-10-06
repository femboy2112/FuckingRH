import numpy as np
from sympy import isprime, primerange, factorint, n_order
def chi4(p): return 1 if p%4==1 else -1
def chi3(q): return 1 if q%3==1 else -1

# ---- A: q=(p+chi4(p))/2 ; F(q)=2q-chi3(q) is the unique possible prime child ----
print("=== A/B: routing F(q)=2q-chi3(q); character invariance chi3(F(q))=chi3(q) ===")
bad=0
for q in primerange(5,2000):
    s=chi3(q); F=2*q-s
    # the other branch 2q+s should be composite (div by 3)
    other=2*q+s
    assert other%3==0 or other<=3, (q,other)
    assert chi3(F)==s   # routing character invariant
    # F(q)-s = 2(q-s)
    assert F-s==2*(q-s)
print("  verified for primes 5..2000: F(q)-s=2(q-s), chi3(F(q))=chi3(q), other branch div by 3.")

# ---- C: wheel-6 (s,a)->(s,2a); F^n(q)=s+6*2^n a ----
print("\n=== C: wheel-6 form q=s+6a => F(q)=s+12a => F^n(q)=s+6*2^n a ===")
ok=True
for q in primerange(5,500):
    s=chi3(q); a=(q-s)//6; assert q==s+6*a
    for n in range(1,6):
        Fn=s+6*(2**n)*a
        # iterate F directly
        x=q
        for _ in range(n): x=2*x-chi3(x)  # note chi3 invariant so = 2x-s
        if x!=Fn: ok=False
print("  F^n(q)=s+6*2^n a holds:",ok)

# ---- D: character transport chi4(p)=chi3(q) for prime edge p<-q (p=2q-s prime) ----
print("\n=== D: character transport chi4(p)=chi3(q) when p=2q-chi3(q) is prime ===")
cnt=0; bad=0
for q in primerange(5,5000):
    s=chi3(q); p=2*q-s
    if isprime(p):
        cnt+=1
        if chi4(p)!=s: bad+=1
print("  checked %d prime edges; violations of chi4(p)=chi3(q): %d"%(cnt,bad))

# ---- E: each sieve prime ell fires at ONE residue class mod ord_ell(2) along q_n=s+2^n(q0-s) ----
print("\n=== E: order-clock structure: ell | q_n at one n-class mod ord_ell(2) ===")
q0=5; s=chi3(q0); y0=q0-s
for ell in [3,5,7,11,13,17]:
    if y0%ell==0: 
        print("  ell=%d divides y0, always fires"%ell); continue
    if ell==2: continue
    ordl=n_order(2,ell)
    # n with 2^n (y0) = -s mod ell  => 2^n = -s*y0^{-1} mod ell
    target=(-s*pow(y0,-1,ell))%ell
    hits=[n for n in range(0,2*ordl) if pow(2,n,ell)==target%ell]
    # check hits form one class mod ord
    cls=set(h%ordl for h in hits) if hits else set()
    inseq=any(pow(2,n,ell)==target for n in range(ordl))
    print("  ell=%2d: ord_ell(2)=%2d, target=%d in <2>? %s, n-hits mod ord = %s"%(ell,ordl,target,inseq,cls if cls else "{} (never)"))

# ---- G: semiprime control: (p^2-1)/8 is a semiprime iff p in {7,11,13} ----
print("\n=== G: (p^2-1)/8 semiprime (2 prime factors w/ multiplicity) iff p in {7,11,13} ===")
sp=[]
for p in primerange(3,200):
    N=(p*p-1)//8
    if sum(factorint(N).values())==2: sp.append(p)
print("  primes p<200 with (p^2-1)/8 semiprime:",sp)
