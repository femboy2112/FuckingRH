#!/usr/bin/env python3
"""Proof-attempt probes for Mellin/Dirac completed source balance.

No zero ordinates are used. RH remains open.

Checks:
  * exact Archimedean curvature = pole vacuum - Gamma heat trace;
  * finite prime source in log coordinates;
  * local one-event curvature payment fails for true arithmetic;
  * cumulative prime/vacuum balance is the weighted PNT error;
  * finite positive Euler characteristic exponents do not approach Suzuki Psi.
"""
from __future__ import annotations
import math
import mpmath as mp

mp.mp.dps = 60


def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d=3
    while d*d <= n:
        if n%d == 0: return False
        d += 2
    return True


def prime_powers(N):
    out={}
    for p in range(2,N+1):
        if not is_prime(p): continue
        q=p
        while q<=N:
            out[q]=p
            q*=p
    return sorted(out.items())


def gamma_heat(t):
    t=mp.mpf(t)
    return mp.e**(-t/2)/(1-mp.e**(-2*t))


def A2(t):
    t=mp.mpf(t)
    return mp.e**(t/2)+mp.e**(-t/2)-gamma_heat(t)


def Aprime(t):
    t=mp.mpf(t)
    B=(mp.digamma(mp.mpf("0.25"))-mp.log(mp.pi))/2
    z=mp.e**(-t/2)
    return 2*(mp.e**(t/2)-z)+B+mp.atanh(z)+mp.atan(z)


def verify_arch_source():
    for t in [mp.mpf("0.3"), mp.log(2), 1, 3, 7]:
        x=mp.e**t
        closed=(x**3-x-1)/(mp.sqrt(x)*(x**2-1))
        assert abs(A2(t)-closed)<mp.mpf("1e-50")


def event_weight(q,p):
    return mp.log(p)/mp.sqrt(q)


def local_payment_stats(N=10000):
    ev=prime_powers(N)
    ratios=[]
    for (q,p),(qq,pp) in zip(ev,ev[1:]):
        supply=Aprime(mp.log(qq))-Aprime(mp.log(q))
        debit=event_weight(qq,pp)
        ratios.append((supply/debit,q,qq))
    return ratios


def verify_local_payment_no_go():
    ratios=local_payment_stats()
    # Counterexample to "each next event is paid by preceding curvature".
    r,q,qq=min(ratios,key=lambda z:z[0])
    assert r<mp.mpf("0.2")
    # Certified simple early witness used in the note.
    witness=[x for x in ratios if x[1]==16 and x[2]==17][0]
    assert witness[0] < mp.mpf("0.37")
    return witness, (r,q,qq)


def mangoldt(n):
    # elementary prime-power detector for finite probes
    for p in range(2,int(math.sqrt(n))+2):
        if not is_prime(p): continue
        q=p
        while q<n: q*=p
        if q==n: return mp.log(p)
    if is_prime(n): return mp.log(n)
    return mp.mpf(0)


def S_half(X):
    return mp.fsum([mangoldt(n)/mp.sqrt(n) for n in range(2,X+1)])


def psi(X):
    return mp.fsum([mangoldt(n) for n in range(2,X+1)])


def verify_weighted_error_identity(X=1000):
    # Abel/partial summation in its finite step-function integral form:
    # sum Lambda(n)/sqrt(n)
    # = psi(X)/sqrt(X) + 1/2 integral_1^X psi(u)u^-3/2 du,
    # where the integral over each [n,n+1) uses constant psi(n).
    rhs=psi(X)/mp.sqrt(X)
    for n in range(1,X):
        rhs += psi(n)*(1/mp.sqrt(n)-1/mp.sqrt(n+1))
    assert abs(rhs-S_half(X))<mp.mpf("1e-45")


def finite_prime_energy(P,t,sigma=mp.mpf("0.5")):
    total=mp.mpf(0)
    for p in range(2,P+1):
        if not is_prime(p): continue
        r=mp.power(p,-sigma)
        theta=t*mp.log(p)
        # -log modulus of normalized geometric characteristic factor
        total += mp.mpf("0.5")*mp.log(
            (1-2*r*mp.cos(theta)+r*r)/(1-r)**2
        )
    return total


def verify_finite_positive_limit_no_go():
    # Fixed nonzero frequency: the naive positive critical prime exponent
    # grows strongly with cutoff instead of approaching a finite Suzuki object.
    vals=[finite_prime_energy(P,1) for P in [100,1000,10000]]
    assert vals[0] < vals[1] < vals[2]
    assert vals[-1] > 10*vals[0]
    return vals


def report():
    witness,worst=verify_local_payment_no_go()
    vals=verify_finite_positive_limit_no_go()
    print("Exact source identity: A'' = exp(t/2)+exp(-t/2)-GammaHeat(t)")
    print("Local curvature-payment counterexample:")
    print(f"  {witness[1]} -> {witness[2]} supply/debit = {mp.nstr(witness[0],10)}")
    print("Worst ratio through 10000:")
    print(f"  {worst[1]} -> {worst[2]} ratio = {mp.nstr(worst[0],10)}")
    print("Naive positive critical prime exponent at t=1:")
    for P,v in zip([100,1000,10000],vals):
        print(f"  P={P:5d}: {mp.nstr(v,12)}")
    print("Weighted Abel identity checked.")
    print("All proof-attempt controls passed; no RH proof obtained.")


def main():
    verify_arch_source()
    verify_weighted_error_identity()
    report()


if __name__=="__main__":
    main()
