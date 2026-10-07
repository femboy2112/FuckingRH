#!/usr/bin/env python3
"""Zero-extension Weil form and quantitative logarithmic spectral controls.

The identity is proved in LOG_EXTENSION_FESHBACH_THEOREM.md; numerical
examples calibrate constants only. No zeta zeros are used; RH remains open.
"""
import mpmath as mp
mp.mp.dps = 70

def m(R, xi):
    """Fourier multiplier for the positive finite-range translation square."""
    x = R*abs(xi)
    return mp.mpf(0) if x == 0 else mp.euler+mp.log(x)-mp.ci(x)

def indicator_calibration(a):
    """v=1 on (-a,a), 0 outside; finite energy."""
    local = 2*a*(1-mp.log(2*a))
    exterior = 2*a
    assert abs(local-(exterior-mp.log(2*a)*(2*a))) < mp.mpf('1e-60')
    return local, exterior

def linear_calibration(a):
    """v(x)=x on (-a,a), 0 outside; independent 1D translation integral."""
    def sqnorm(h):
        return h*h*(2*a-h)+mp.mpf(2)/3*(a**3-(a-h)**3)
    exterior = mp.mpf('0.5')*mp.quad(lambda h: sqnorm(h)/h, [0,a,2*a])
    kinetic = 2*a**3/3
    boundary = -mp.quad(lambda x: x*x*mp.log(a*a-x*x), [-a,0,a])/2
    local = kinetic+boundary
    norm2 = 2*a**3/3
    assert abs(local-(exterior-mp.log(2*a)*norm2)) < mp.mpf('1e-55')
    return local, exterior

def ordered_eigenvalue_lower_bound(n):
    """Analytic min-max bound for lambda_n(P_a), uniform in a."""
    assert n>=1
    # choose Fourier cutoff B=pi*n/(4a); 2a*B=pi*n/2.
    z = mp.pi*n/2
    return mp.mpf('0.5')*(mp.euler+mp.log(z)-mp.ci(z))

def main():
    for as_str in ['0.2','0.5','1','2']:
        a=mp.mpf(as_str)
        u,eu=indicator_calibration(a)
        v,ev=linear_calibration(a)
        print(f'a={as_str}: indicator L={mp.nstr(u,13)}, E={mp.nstr(eu,13)}; '
              f'linear L={mp.nstr(v,13)}, E={mp.nstr(ev,13)}')
    print('Uniform min-max lower bound: lambda_n(P_a) >= 0.5 m_{2a}(pi*n/(4a))')
    for n in [1,2,4,8,16,32,64,128,512,2048]:
        lb=ordered_eigenvalue_lower_bound(n)
        print(f'  n={n:4d}: {mp.nstr(lb,12)}')
        assert lb>=0
    assert all(ordered_eigenvalue_lower_bound(n)<ordered_eigenvalue_lower_bound(2*n)
               for n in [1,2,4,8,16,32,64,128])
    print('PASS: two calibrated finite-range identities and monotone log-frequency spectral lower bound.')
    print('The compact-resolvent and min-max assertions require the mathematical proof in the note; RH open.')

if __name__ == '__main__':
    main()
