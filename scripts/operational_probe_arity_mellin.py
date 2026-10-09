#!/usr/bin/env python3
"""Operational wavefront / Mellin bridge controls. Zero-input, finite algebra.

Assumptions: squarefree probe sets, standard zeta/Dirichlet characters,
standard Haar counting measure. Output is evidence for the linked proofs,
not an RH or GRH verification.
"""
from fractions import Fraction
from itertools import combinations
from math import prod, log
import cmath
import json
import mpmath as mp

mp.mp.dps = 75
PRIMES = [(2, 3), (2, 3, 5), (2, 3, 5, 7)]

def h_fraction(n, ps):
    z = Fraction(1)
    for p in ps:
        z *= Fraction(int(n % p == 0), 1) - Fraction(1, p)
    return z

def divisibility_observations(ps):
    d = prod(ps)
    h = [h_fraction(n, ps) for n in range(d)]
    norm = sum((x*x for x in h), Fraction())/d
    predicted = prod((Fraction(p-1, p*p) for p in ps), start=Fraction(1))
    assert norm == predicted
    tested = 0
    for r in range(len(ps)):
        for chosen in combinations(ps, r):
            m = prod(chosen)
            for a in range(m):
                group = [h[n] for n in range(d) if n % m == a]
                assert sum(group) == 0
                tested += 1
    plus = [Fraction(1, d)*(1+x) for x in h]
    minus = [Fraction(1, d)*(1-x) for x in h]
    assert min(plus+minus)>0
    for r in range(len(ps)):
        for chosen in combinations(ps,r):
            m = prod(chosen)
            assert [sum(plus[n] for n in range(d) if n%m==a)
                    for a in range(m)] == [sum(minus[n] for n in range(d) if n%m==a)
                                        for a in range(m)]
    assert sum(plus[n]*h[n] for n in range(d)) == norm
    assert sum(minus[n]*h[n] for n in range(d)) == -norm
    return {"primes":list(ps),"d":d,"birth":max(ps),"direct_event":d,
            "arity":len(ps),"norm_squared":str(norm),"conditional_checks":tested,
            "rival_joint_expectations":[str(-norm),str(norm)]}

def mellin_s(s,ps):
    return mp.zeta(s)*prod((mp.power(p,-s)-mp.mpf(1)/p for p in ps))

def hurwitz_independent(s,ps):
    d=prod(ps)
    return mp.power(d,-s)*sum(mp.mpf(h_fraction(r,ps).numerator)/h_fraction(r,ps).denominator
                                   *mp.zeta(s,mp.mpf(r)/d) for r in range(1,d+1))

def complex_pair(z): return [mp.nstr(mp.re(z),22),mp.nstr(mp.im(z),22)]

def analytic_checks():
    rows=[]
    for ps in PRIMES:
        s=mp.mpf('2.37')+mp.mpf('0.41')*mp.j
        lhs=mellin_s(s,ps)
        rhs=hurwitz_independent(s,ps)
        assert abs(lhs-rhs)<mp.mpf('1e-60')
        r=len(ps)
        expected=(-1)**r*prod((mp.log(p)/p for p in ps))
        eps=mp.mpf('1e-24')
        observed=mellin_s(1+eps,ps)/eps**(r-1)
        assert abs(observed-expected)<mp.mpf('1e-19')
        rows.append({"S":list(ps),"order_at_s_1":r-1,
                     "leading_coefficient":mp.nstr(expected,24),
                     "numeric_jet_lead":mp.nstr(observed,24),
                     "hurwitz_residual":mp.nstr(abs(lhs-rhs),5)})
    # Hostile exact-conductor-6 Fourier probe: same one-prime nulls,
    # but its Mellin value at s=1 is NOT zero (polylog(1,e^(i pi/3))).
    w=mp.exp(mp.pi*mp.j/3)
    addval=-mp.log(1-w)
    via_hurwitz=mp.power(6,-1)*sum(w**r*mp.zeta(mp.mpf(1)+mp.mpf('1e-20'),mp.mpf(r)/6)
                     for r in range(1,7))
    assert abs(addval-mp.j*mp.pi/3)<mp.mpf('1e-70')
    assert abs(via_hurwitz-addval)<mp.mpf('1e-15')
    return rows,complex_pair(addval)

def character_checks():
    chi={0:mp.mpf(0),1:mp.mpf(1),2:mp.j,3:-mp.j,4:-mp.mpf(1)}
    def L(s,conjugate=False):
        if s == 1:
            return -sum((mp.conj(chi[r]) if conjugate else chi[r])
                        *mp.digamma(mp.mpf(r)/5) for r in range(1,5))/5
        return sum((mp.conj(chi[r]) if conjugate else chi[r])
                   *mp.zeta(s,mp.mpf(r)/5) for r in range(1,5))*mp.power(5,-s)
    s=mp.mpf(1)
    L1=L(s)
    assert abs(L1)>mp.mpf('1e-5')
    # Same centered Haar probes for zeta do not cancel the true
    # non-real Hecke character at s=1.
    haar=L1*prod((chi[p]*mp.power(p,-s)-mp.mpf(1)/p for p in (2,3)))
    assert abs(haar-L1/3)<mp.mpf('1e-65')
    # Hecke-centered probes differ from Haar probes; center at chi(p)/p.
    def char_lift(ss):
        return L(ss)*prod((chi[p]*mp.power(p,-ss)-chi[p]/p for p in (2,3)))
    eps=mp.mpf('1e-24')
    expected_lead=L1*chi[2]*chi[3]*mp.log(2)*mp.log(3)/6
    observed=char_lift(1+eps)/eps**2
    assert abs(observed-expected_lead)<mp.mpf('1e-19')
    phi=(1+mp.sqrt(5))/2
    kap=mp.sqrt(1+phi**2)-phi
    a=(1-mp.j*kap)/2
    b=mp.conj(a)
    def dh_lift(ss):
        prodchi=prod((chi[p]*mp.power(p,-ss)-chi[p]/p for p in (2,3)))
        prodbar=prod((mp.conj(chi[p])*mp.power(p,-ss)-chi[p]/p for p in (2,3)))
        return a*L(ss)*prodchi+b*L(ss,True)*prodbar
    s2=mp.mpf('2.37')+mp.mpf('0.41')*mp.j
    def periodic_lift(weights):
        return mp.power(30,-s2)*sum(weights(n)*mp.zeta(s2,mp.mpf(n)/30)
                                       for n in range(1,31))
    def hc(n):
        return prod((mp.mpf(int(n%p==0))-chi[p]/p for p in (2,3)))
    def dcoeff(n):
        return a*chi[n%5]+b*mp.conj(chi[n%5])
    assert abs(periodic_lift(lambda n:chi[n%5]*hc(n))-char_lift(s2))<mp.mpf('1e-62')
    assert abs(periodic_lift(lambda n:dcoeff(n)*hc(n))-dh_lift(s2))<mp.mpf('1e-62')
    DH1=dh_lift(s)
    expected_DH=b*mp.mpf(2)/3*L(s,True)
    assert abs(DH1-expected_DH)<mp.mpf('1e-65')
    assert abs(DH1)>mp.mpf('1e-4')
    return {"Lchi_at_1":complex_pair(L1),"haar_probe_at_1":complex_pair(haar),
            "hecke_centered_order":2,
            "hecke_centered_jet_lead":complex_pair(expected_lead),
            "hecke_centered_observed":complex_pair(observed),
            "davenport_heilbronn_adapted_probe_at_1":complex_pair(DH1),
            "DH_nonzero":True}

def source_mutations():
    # at 2, either local weight alpha^v2 or displaced log-degree 2
    def b2(b):return ((b/2-mp.mpf(1)/2)*(1-mp.mpf(1)/2)/(1-b/2))
    def value(b):return -mp.log(3)/3*b2(b)
    fake=mp.mpf(1)/7
    # h_23(6)=h_23(30)=1/3. Two separate composite innovations
    # cancel the zeroth Mellin value but NOT the coefficientwise log_*.
    assert h_fraction(6,(2,3))==h_fraction(30,(2,3))==Fraction(1,3)
    assert fake*mp.mpf(1)/18 +(-5*fake)*mp.mpf(1)/90 == 0
    assert fake !=0
    eps=mp.mpf('0.01')
    alpha=mp.mpf('1.03')
    return {"fake6_delta_a6":mp.nstr(fake,20),
            "fake6_F_at_1":mp.nstr(fake/18,24),
            "alpha2_1_03_F_at_1":mp.nstr(value(alpha),24),
            "shift_log2_delta_0_01_F_at_1":mp.nstr(value(mp.exp(-eps)),24),
            "balanced_composite_mutations":{"a6_delta":mp.nstr(fake,22),
              "a30_delta":mp.nstr(-5*fake,22),"F_at_1":"0",
              "connected_log_star_at_6":mp.nstr(fake,22)}}

def finite_jet_spoof():
    # m specified analytic jets at s=1, spoofed by m+1 composites.
    candidates=[6,30,42,66,78,102,114]
    rows=[]
    for m in range(1,5):
        ns=candidates[:m+1]
        ts=[mp.log(n) for n in ns]
        c=[1/prod((ts[j]-ts[k] for k in range(m+1) if k!=j))
           for j in range(m+1)]
        raw=[3*n*c[j] for j,n in enumerate(ns)] # h_23(n)=1/3 for 6|n
        scale=mp.mpf('.001')/max(map(abs,raw))
        delta=[scale*x for x in raw]
        derivs=[sum(delta[j]/(3*ns[j])*(-ts[j])**k
                    for j in range(m+1)) for k in range(m)]
        assert max(abs(z) for z in derivs)<mp.mpf('1e-60')
        assert abs(delta[0])>0
        rows.append({"jet_count":m,"mutated_composites":ns,
                     "largest_abs_coeff_mutation":mp.nstr(max(map(abs,delta)),5),
                     "first_connected_innovation":mp.nstr(delta[0],20),
                     "max_jet_residual":mp.nstr(max(map(abs,derivs)),5)})
    return rows

if __name__=='__main__':
    finite=[divisibility_observations(ps) for ps in PRIMES]
    analytic, add=analytic_checks()
    print(json.dumps({"status":"PASS","no_zeta_zeros_used":True,
      "finite_probes":finite,"mellin_factorization":analytic,
      "additive_exact_conductor_6_jet0":add,
      "hecke_and_DH":character_checks(),"mutations":source_mutations(),
      "finite_jet_spoof":finite_jet_spoof(),
      "not_proven":"Weil sign, arithmetic self-product, global positive polarization"},indent=2))
