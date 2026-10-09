#!/usr/bin/env python3
"""Probe completeness versus archimedean logarithmic energy.
Numerical illustrations of an analytical theorem; NO zeros used and NO RH test.
"""
import json
import math
import numpy as np
from scipy.special import digamma

def ghat(x):
    x=np.asarray(x,dtype=float)
    y=np.zeros_like(x)
    ok=(abs(x)>1e-7)&(abs(abs(x)-math.pi)>1e-6)
    y[ok]=math.pi**2*np.sin(x[ok])/(x[ok]*(math.pi**2-x[ok]**2))
    y[abs(x)<=1e-7]=1.0
    y[abs(abs(x)-math.pi)<=1e-6]=0.5
    return y

eta=np.linspace(-150,150,60001)
sq=ghat(eta)**2
norm_numerical=float(np.trapezoid(sq,eta)/(2*math.pi))
assert abs(norm_numerical-.75)<1e-6,(norm_numerical,abs(norm_numerical-.75))
rows=[]
for T in [10,20,40,80,160,320,640]:
    Omega=np.real(digamma(.25+0.5j*(eta+T)))-math.log(math.pi)
    energy=float(np.trapezoid(sq*Omega,eta)/(2*math.pi))
    readings=np.abs(ghat(np.array([T-j for j in range(4)])))
    rows.append({"T":T,"gamma_energy":energy,"gamma_minus_threequarters_logT":energy-.75*math.log(T),
                 "max_first_four_linear_probe_amplitudes":float(max(readings))})
assert rows[-1]["max_first_four_linear_probe_amplitudes"]<1e-6
assert rows[-1]["gamma_energy"]>rows[0]["gamma_energy"]+2
print(json.dumps({"status":"PASS", "source_zeros_read":False,
    "g":"(1+cos(pi*x))/2 on |x|<=1; C1 and piecewise smooth, ghat~|xi|^-3",
    "norm_squared_exact":"3/4", "norm_squared_numerical":norm_numerical,
    "fourier_tail_cutoff":150,"mesh_points":60001,
    "asymptotic_theorem":"for smooth compact g, gamma_energy = norm² log T + O(1)",
    "rows":rows,"scope":"illustration, NOT interval certification or universal sign test"},indent=2))
