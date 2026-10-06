#!/usr/bin/env python3
"""Round008 centerpiece: the screw-kernel positivity margin AS A FUNCTION of dBN flow time tau.

DIAGNOSTIC (uses the first N zeros gamma_n as input to study the CORRESPONDENCE between our screw-kernel
positivity and the de Bruijn-Newman flow -- NOT a non-circular proof construction).

Zero-side CND representation of Suzuki's object:  Psi(t) = 2 sum_n (1 - cos(gamma_n t))/gamma_n^2,
screw kernel K[i,j]=Psi(t_i)+Psi(t_j)-Psi(|t_i-t_j|);  K >= 0  <=>  all gamma_n real.

dBN flow (canonical, repulsive / gradient ascent of S=sum log|x_j-x_k|), in the gamma variable:
  d gamma_k/dtau = (1/2) sum'_{j != k, over the symmetric set +-gamma} 1/(gamma_k - gamma_j).
Increasing tau relaxes the gas (zeros spread); decreasing tau (backward) lets pairs collide and go complex.

Claim tested: the margin lambda_min(tau) (smallest eigenvalue of the nontrivial block of K at flowed zeros)
is monotone increasing in tau, and crosses 0 exactly when a pair collides = the (truncated) dBN constant.
So "dBN flow time" and "our positivity margin" are the same coordinate; RH <=> Lambda<=0 <=> margin(0)>=0.
"""
import numpy as np
from scipy.integrate import solve_ivp
from mpmath import mp, zetazero
mp.dps = 20

N = 30
print(f"loading first {N} zeros (diagnostic input)...")
G0 = np.array([float(zetazero(n).imag) for n in range(1, N+1)])

def flow_rhs(tau, g):
    # symmetric set {+g, -g}; d g_k/dtau = (1/2)[ sum_{j!=k} 1/(g_k-g_j) + sum_j 1/(g_k+g_j) ]
    out = np.zeros_like(g)
    for k in range(len(g)):
        s = 0.0
        for j in range(len(g)):
            if j != k:
                s += 1.0/(g[k]-g[j])
            s += 1.0/(g[k]+g[j])       # interaction with the mirror -g_j
        out[k] = 0.5*s
    return out

def psi_screw_margin(g, T=8.0, dt=0.1):
    tg = np.arange(0, T+dt, dt)
    # Psi(t) = 2 sum (1-cos(g_n t))/g_n^2
    Psi = 2.0*np.sum((1-np.cos(np.outer(tg, g)))/g**2, axis=1)
    M = len(tg)-1; i = np.arange(M+1); D = np.abs(i[:,None]-i[None,:])
    K = Psi[:,None]+Psi[None,:]-Psi[D]
    Kb = K[1:,1:]                       # drop trivial t=0 null node
    return float(np.linalg.eigvalsh(Kb).min())

if __name__ == "__main__":
    print("margin lambda_min(tau) of the screw kernel at dBN-flowed zeros:\n")
    print(f"   {'tau':>7} {'lambda_min':>14}   note")
    taus = [+0.6, +0.4, +0.2, +0.1, 0.0, -0.1, -0.2, -0.4, -0.6]
    base = None
    results = []
    for tau in taus:
        if tau == 0:
            g = G0.copy()
        else:
            sol = solve_ivp(flow_rhs, [0, tau], G0, rtol=1e-8, atol=1e-10, max_step=abs(tau)/50 or 0.01)
            g = sol.y[:, -1]
        m = psi_screw_margin(g)
        results.append((tau, m))
        print(f"   {tau:+7.2f} {m:14.6e}")
    # monotonicity check
    ms = [m for _, m in sorted(results)]
    mono = all(ms[i] <= ms[i+1]+1e-9 for i in range(len(ms)-1))
    print(f"\n   margin increasing in tau? {mono}")
    print("""
Reading: if lambda_min(tau) increases with tau and would cross 0 at some tau=Lambda_trunc (negative, since
the first 30 zeros are well separated), then the dBN flow time is exactly our positivity-margin coordinate:
margin(tau)=0 <=> tau=Lambda. RH <=> Lambda<=0 <=> margin at tau=0 is >=0. This is the explicit bridge the
literature does not record (dBN <-> screw-kernel/CND positivity), built here as a diagnostic. The true
Lambda (=0 under RH) needs the tight high-zero Lehmer pairs, not the first 30. RH remains open.""")
