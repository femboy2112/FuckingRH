#!/usr/bin/env python3
"""Archimedean Weil-symbol range-no-go calibration; no zeros or fitted boundary data."""
import mpmath as mp


def arch_symbol(t):
    return mp.re(mp.digamma(mp.mpf('0.25')+mp.j*t/2))-mp.log(mp.pi)


def run():
    mp.mp.dps=70
    print('ARCHIMEDEAN RANGE OBSTRUCTION: a(t) cannot be Fourier transform of finite measure')
    for T in (0,10,50,100,1000,10000,1000000):
        got=arch_symbol(T)
        if T:
            predicted=mp.log(mp.mpf(T)/(2*mp.pi))
            print(f'T={T:7d} a(t)={float(got):13.9f} log(t/2pi)={float(predicted):13.9f} residual={float(got-predicted):+.3e}')
        else:
            print(f'T={T:7d} a(t)={float(got):13.9f}')
    assert arch_symbol(10**6)>arch_symbol(1000)>arch_symbol(100)>0
    print('PASS: finite spot test only; unboundedness is proved by digamma asymptotics')


if __name__=='__main__':run()
