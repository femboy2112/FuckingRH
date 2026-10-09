#!/usr/bin/env python3
"""Optional numerical calibration of the authentic archimedean digamma high-frequency obstruction.
Requires numpy and scipy; not part of mandatory CI. No zeros are read.
"""
import numpy as np
try:
    from scipy.special import digamma
except ImportError as exc:
    raise SystemExit('Install scipy to run this optional UV control') from exc


def run():
    length=16.0
    n=32768
    u=np.linspace(-length,length,n,endpoint=False)
    du=u[1]-u[0]
    phi=np.zeros_like(u)
    m=np.abs(u)<1
    phi[m]=np.exp(-1/(1-u[m]**2))
    norm2=np.sum(abs(phi)**2)*du
    omega=2*np.pi*np.fft.fftshift(np.fft.fftfreq(n,d=du))
    A=np.real(digamma(.25+.5j*omega))-np.log(np.pi)
    dt=omega[1]-omega[0]
    print('Authentic A_inf(t)=Re psi(1/4+it/2)-log pi; compact smooth modulated test; no zeros')
    for T in (20,50,100,200,400):
        f=phi*np.exp(1j*T*u)
        F=du*np.fft.fftshift(np.fft.fft(np.fft.ifftshift(f)))
        energy=np.sum(A*abs(F)**2)*dt/(2*np.pi)/norm2
        expected=np.log(T/(2*np.pi))
        print(f'T={T:3d} Gamma energy/norm2={energy:.9f} predicted={expected:.9f} residual={energy-expected:+.6e}')
    print('OBSERVATION ONLY: gamma multiplier is unbounded above; proof in research note')


if __name__=='__main__':run()
