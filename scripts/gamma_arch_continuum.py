#!/usr/bin/env python3
"""Zero-free archimedean Gamma as a compensated continuous-shift Dirichlet form.
Only mpmath required. No zeta zeros, no fitted spectral boundary.
"""
from math import exp, log
import mpmath as mp


def arch_symbol(t):
    t=mp.mpf(t)
    return mp.re(mp.digamma(mp.mpf('0.25')+1j*t/2))-mp.log(mp.pi)


def levy_density(u):
    return mp.exp(-u/2)/(-mp.expm1(-2*u))


def compensated_symbol(t):
    t=mp.mpf(t)
    def f(u):
        if u==0:return mp.mpf('0')
        return 4*levy_density(u)*mp.sin(t*u/2)**2
    return mp.quad(f,[0,mp.mpf('.001'),mp.mpf('.1'),1,10,90])


def log_gaussian_overlap_shift(a):
    return mp.exp(-mp.mpf(a)**2/4)


def fake_source_control(delta):
    a=mp.log(6)
    return -2*delta*log_gaussian_overlap_shift(a), delta*2*(1-log_gaussian_overlap_shift(a))-2*delta


def run():
    mp.mp.dps=40
    print('ARCHIMEDEAN GAMMA: compensated continuous-shift energy, no zero input')
    a0=arch_symbol(0)
    print('A_inf(0)=',mp.nstr(a0,18))
    for t in [0,mp.mpf('.25'),1,3,10]:
        integral=compensated_symbol(t)
        exact=arch_symbol(t)-a0
        err=abs(integral-exact)
        print(f't={mp.nstr(t,6)} integral={mp.nstr(integral,16)} Gamma diff={mp.nstr(exact,16)} err={mp.nstr(err,4)}')
        assert err<mp.mpf('1e-16')
    for delta in [mp.mpf('0'),mp.mpf('.02')]:
        direct,sos=fake_source_control(delta)
        assert abs(direct-sos)<mp.mpf('1e-35')
        print(f'fake n=6 delta={delta} source change={mp.nstr(direct,16)} SOS-minus-debit={mp.nstr(sos,16)}')
    print('ALL FINITE CHECKS PASSED; no positivity inference toward RH')


if __name__=='__main__':run()
