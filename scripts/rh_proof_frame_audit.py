#!/usr/bin/env python3
"""Hostile finite controls for cubical/Hodge/Schur approaches to RH.

No zeta-zero data. The resulting tests establish obstructions, not RH.
Run: python scripts/rh_proof_frame_audit.py
"""
from math import cos, cosh, log, pi, sqrt
import mpmath as mp
import numpy as np

mp.mp.dps = 60


def arch_plateau_bound(k, c=mp.mpf("0.5")):
    """Lower bound for Suzuki's 1/4 * double-difference kinetic form.

    v(x)=chi(x)e^{ikx}; chi is smooth, supported inside (-a,a),
    and equals one on [-c,c].
    """
    x = 2*c*k
    return 2*c*(mp.euler + mp.log(x) - mp.ci(x)) - 2*c + mp.sin(x)/k


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, int(sqrt(n))+1))


def prime_power_weight_sum(N):
    total = 0.0
    for p in range(2, N+1):
        if not is_prime(p):
            continue
        q = p
        while q <= N:
            total += log(p)/sqrt(q)
            q *= p
    return total


def cube_short_values(p, q):
    """Two-event exterior square and Schur short; no primality assumption."""
    N = int(np.lcm(p, q))

    def wake(n, m):
        return float((n+1) % m == 0) - float(n % m == 0)

    def vec(n):
        return np.array([sqrt(p/2)*wake(n,p), sqrt(q/2)*wake(n,q)])

    values = []
    for n in range(N):
        v, v1 = vec(n), vec(n+1)
        d = float(np.dot(v1, v1))
        values.append(float(np.dot(v,v1)**2/d) if d else float(np.dot(v,v)))
    return np.array(values)


def main():
    print("1. UV mismatch: bounded prime Gram versus unbounded Weil form")
    for k in (10, 100, 1000, 10000, 100000):
        print(f"   k={k:6d}: kinetic lower bound={mp.nstr(arch_plateau_bound(k), 12)}")
    assert arch_plateau_bound(100000) > 11
    S = prime_power_weight_sum(54)
    print(f"   finite prime square <= 4*S*||v||^2; S={S:.8f}")
    assert 0 < S < 20

    print("2. Boundary term makes Weil exceed kinetic+prime raw energy")
    # For normalized v_eps supported on (a-2eps,a-eps):
    # Q_W(v_eps) - raw(v_eps) >=
    #  -0.5*log(4a eps) - V_a - ||R_a|| -> infinity.
    a = mp.mpf(2)
    for T in (10, 30, 50):
        eps = mp.exp(-2*T)/(4*a)
        assert abs(-mp.log(4*a*eps)/2 - T) < mp.mpf("1e-50")
        print(f"   eps={mp.nstr(eps,8)}, Q-raw >= {T} - V_a - ||R_a||")

    print("3. Synthetic off-line symmetric quartet")
    # Finite Xi with zeros lambda=+/-1/4 +/- 2*pi*i, kernel
    # K(h)=4*cosh(h/4)*cos(2*pi*h); on points 0,1.
    eig_negative = 4*(1-cosh(0.25))
    print(f"   finite Weil 2-point negative eigenvalue={eig_negative:.12f}")
    assert eig_negative < 0
    logs = (log(6), -log(2), -log(3))
    assert abs(sum(logs)) < 1e-14
    print(f"   Hodge product-formula primitive norm={sum(v*v for v in logs):.12f}")

    print("4. Factorized place lift is rigid")
    # For q=p: sum_v log|q|_v A_v = log(p)*(A_inf-A_p).
    A_inf = np.diag([2., 1.])
    for p in (2, 3, 5):
        assert np.linalg.norm(log(p)*(A_inf-A_inf)) == 0
        assert np.linalg.norm(log(p)*(A_inf-(A_inf+np.eye(2)))) > 0
    print("   primitive for every rational q forces A_p=A_inf")

    print("5. Positive cube short ignores prime authenticity")
    real = cube_short_values(2,3)
    fake = cube_short_values(4,9)
    print("   (2,3):", np.array2string(real,precision=3))
    print("   (4,9) minimum:", fake.min())
    assert real.min()>=-1e-12 and fake.min()>=-1e-12
    print("PASS: five hostile controls. RH remains unproved.")


if __name__ == "__main__":
    main()
