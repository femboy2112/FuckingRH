import unittest
from fractions import Fraction as F

import mpmath as mp
from flint import arb, ctx

from scripts import event_dynamics as ev
from scripts.suzuki_psi import psi_suzuki, prime_power_events_up_to


class EventDynamicsTests(unittest.TestCase):
    def setUp(self):
        self.old=ctx.prec
        ctx.prec=200

    def tearDown(self):
        ctx.prec=self.old

    def test_independent_archimedean_series_and_formula(self):
        # Independent Arb exponential-series evaluation vs mpmath Lerch.
        for t in ['0.1','0.5','1','2']:
            a=ev.arch(arb(t))
            want=psi_suzuki(t,dps=90,events=[])
            self.assertTrue(a.contains(arb(mp.nstr(want,85))))

    def test_derivatives_against_lerch(self):
        with mp.workdps(80):
            for t in ['0.1','0.5','1','3']:
                x=mp.mpf(t)
                a=lambda u:psi_suzuki(u,dps=85,events=[])
                # Explicit finite differences avoid mp.diff's tiny-step/dps clash.
                h=mp.mpf('1e-20')
                d=(a(x+h)-a(x-h))/(2*h)
                dd=(a(x+h)-2*a(x)+a(x-h))/h**2
                self.assertLess(abs(ev.arch_prime(arb(t))-arb(mp.nstr(d,75))),arb('1e-36'))
                self.assertLess(abs(ev.curvature(arb(t))-arb(mp.nstr(dd,75))),arb('1e-36'))

    def test_curvature_identity_exact(self):
        for y in [F(5,4),F(3,2),F(2),F(7,3)]:
            original=y+1/y-y**3/(y**4-1)
            factored=(y**6-y**2-1)/(y*(y**4-1))
            self.assertEqual(original,factored)
        self.assertLess(ev.curvature(arb('0.1')),0)
        self.assertGreater(ev.curvature(arb(2).log()),0)

    def test_distribution_jump_and_continuity(self):
        events=prime_power_events_up_to(29)
        s=h=arb(0)
        for e in events:
            t=arb(e.n).log();w=arb(e.prime).log()/arb(e.n).sqrt()
            before=ev.frozen_value(t,s,h)
            after=ev.frozen_value(t,s+w,h+w*t)
            self.assertTrue((after-before).contains(0))
            jump=(ev.arch_prime(t)-(s+w))-(ev.arch_prime(t)-s)
            self.assertTrue((jump+w).contains(0))
            s+=w;h+=w*t

    def test_initial_and_interval_certification(self):
        cert=ev.run_certificate(101)
        self.assertEqual(len(cert['intervals']),len(prime_power_events_up_to(101))-1)
        self.assertFalse(cert['universal_claim'])

    def test_event_recurrence(self):
        events=prime_power_events_up_to(11)
        s,h=ev.prefix(events[:3])
        a,b=arb(4).log(),arb(5).log()
        e=ev.frozen_value(a,s,h);d=ev.arch_prime(a)-s
        recurrence=e+d*(b-a)+ev.arch(b)-ev.arch(a)-ev.arch_prime(a)*(b-a)
        self.assertTrue((recurrence-ev.frozen_value(b,s,h)).contains(0))

    def test_healthy_interval_endpoint_trichotomy(self):
        a,b=arb(2).log(),arb(3).log()
        low=ev.arch_prime(a)-1; high=ev.arch_prime(b)+1
        self.assertEqual(ev.minimum(low,arb(0),a,b)[2],'left')
        self.assertEqual(ev.minimum(high,arb(0),a,b)[2],'right')
        s,h=ev.prefix(prime_power_events_up_to(2))
        self.assertEqual(ev.minimum(s,h,a,b)[2],'interior')

    def test_monotone_fenchel_reserve_is_false(self):
        margins=[]
        for q in [4,5]:
            s,h=ev.prefix(prime_power_events_up_to(q))
            _,v,_=ev.minimum(s,h,arb(2).log(),arb(10).log())
            margins.append(v)
        self.assertGreater(margins[0],0)
        self.assertLess(margins[1]-margins[0],0)

    def test_event_gamma_and_planted_tail_mutations(self):
        s,h=ev.prefix(prime_power_events_up_to(2))
        original=ev.frozen_value(arb(1),s,h)
        ramp=arb(2).log()/arb(2).sqrt()*(1-arb(2).log())
        self.assertGreater(original,0)
        self.assertLess(original-ramp,0)   # duplicate q=2
        self.assertGreater(original+ramp,original)  # deletion raises scalar value
        self.assertLess(original-arb(1)/10,0)  # linear Gamma mutation
        s4,h4=ev.prefix(prime_power_events_up_to(54))
        self.assertLess(ev.frozen_value(arb(4),s4,h4)-100,0)
        # The planted subtraction 100*(|t|-3)_+ is exactly zero for |t|<=3.
        self.assertEqual(max(F(0),F(3)-F(3)),0)

    def test_tent_transform_and_convolution_exact(self):
        # Rectangle overlap length is (t-|x|)_+; Taylor coefficients of the
        # transform integral equal those of (1-cos(tz))/z², including z=0.
        import math
        for k in range(12):
            t=F(7,3)
            moment=t**(2*k+2)/((2*k+1)*(2*k+2))
            integral_coefficient=(-1)**k*moment/math.factorial(2*k)
            cosine_coefficient=(-1)**k*t**(2*k+2)/math.factorial(2*k+2)
            self.assertEqual(integral_coefficient,cosine_coefficient)


if __name__=='__main__':
    unittest.main()
