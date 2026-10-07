#!/usr/bin/env python3
"""Independent finite controls for the RH logarithmic bathtub and boundary layer.

Only standard Python library. No zeros used. Finite tests are calibration,
not proofs of the infinite operator convergence or RH-scale rate.
"""
from __future__ import annotations

from bisect import bisect_left, bisect_right
from math import ceil, cos, e, exp, gamma, log, pi, sin, sqrt

try:
    from mpmath import ci, euler
except ImportError:
    raise SystemExit("Requires mpmath, already used throughout this RH repo.")


def von_mangoldt_sieve(nmax: int) -> list[float]:
    """True von Mangoldt weights; unlike a naive prime-power sieve, composites stay zero."""
    primes = bytearray(b"\x01") * (nmax + 1)
    primes[0:2] = b"\x00\x00"
    for p in range(2, int(sqrt(nmax)) + 1):
        if primes[p]:
            for m in range(p * p, nmax + 1, p):
                primes[m] = 0
    ans = [0.0] * (nmax + 1)
    for p in range(2, nmax + 1):
        if not primes[p]:
            continue
        q = p
        while q <= nmax:
            ans[q] = log(p)
            q *= p
    return ans


def bathtub_bound(n: int) -> float:
    z = pi * n
    return float(euler + log(z) - ci(z) - 1)


def legacy_bound(n: int) -> float:
    z = pi * n / 2
    return float((euler + log(z) - ci(z)) / 2)


def sharp_shift_overlap(width: float, h: float) -> float:
    return cos(pi / (ceil(width / h) + 1))


def finite_chain_largest_eigen(n: int) -> float:
    """Exact sine eigenvalue of path-Jacobi adjacency with offdiag 1/2."""
    return cos(pi / (n + 1))


def arithmetic_shift_floor(A: float, lam: list[float]) -> tuple[float, float]:
    X = min(len(lam) - 1, int(exp(2 * A)))
    s = 0.
    floor = 0.
    for q in range(2, X + 1):
        if lam[q] == 0:
            continue
        w = lam[q] / sqrt(q)
        N = ceil(2*A / log(q))
        floor += 2*w*(1-cos(pi / (N + 1)))
        s += w
    return floor, s


def prime_boundary_measure(A: float, ell: float, lam: list[float]):
    """Normalized source on w=2A-log q in [0,2ell]."""
    X = int(exp(2*A))
    lo = X*exp(-2*ell)
    atoms = []
    for q in range(max(2, ceil(lo)), X+1):
        if lam[q]:
            w = 2*A-log(q)
            if 0 <= w <= 2*ell:
                atoms.append((w, exp(-A)*lam[q]/sqrt(q)))
    atoms.sort()
    return atoms


def boundary_probe(X: int, ell: float, lam: list[float]):
    A = .5*log(X)
    atoms = prime_boundary_measure(A, ell, lam)
    ws=[w for w,c in atoms]
    cum=[0.]
    hcum=[0.]
    for w,c in atoms:
        cum.append(cum[-1]+c)
        hcum.append(hcum[-1]+c*exp(-w/2))

    def interval_weighted(lo, hi):
        return hcum[bisect_right(ws,hi)]-hcum[bisect_left(ws,lo)]

    # Exact source CDF supremum up to rounding: compare both sides of each jump.
    eta=0.
    for j,(w,c) in enumerate(atoms):
        target=2*(1-exp(-w/2))
        eta=max(eta,abs(cum[j]-target),abs(cum[j+1]-target))
    eta=max(eta,abs(cum[-1]-2*(1-exp(-ell))))

    # Input f(v)=exp(-v/2) on [0,ell].
    us=[ell*j/300 for j in range(301)]
    values=[]
    targets=[]
    for u in us:
        hu=exp(u/2)*interval_weighted(u,u+ell)
        pu=exp(-u/2)*(1-exp(-ell))
        values.append((hu-pu)**2)
        targets.append(pu**2)
    def trap(vals):
        return ell/300*(sum(vals)-.5*(vals[0]+vals[-1]))
    strong_relative_err = sqrt(trap(values)/trap(targets))
    return len(atoms),cum[-1],eta,strong_relative_err


def main():
    print("Bathtub bound compared with old half-slope bound")
    for n in [1,2,3,5,10,100,1000]:
        new,old=bathtub_bound(n),legacy_bound(n)
        assert new>old
        print(f"n={n:4d} new={new:.9f} old={old:.9f}")

    print("Sharp one-shift chain constants")
    for width,h in [(2.,1.2),(2.,.5),(2.,2.),(2.,.3)]:
        N=ceil(width/h)
        gap=2*(1-sharp_shift_overlap(width,h))
        assert abs(sharp_shift_overlap(width,h)-finite_chain_largest_eigen(N))<1e-14
        print(f"width={width:g} h={h:g} N={N} minimal gap={gap:.9f}")

    nmax=250000
    lam=von_mangoldt_sieve(nmax)
    print("Arithmetic shift floor, exact genuine-prime-power source")
    for A in [1.,2.,3.,4.,5.,6.]:
        G,S=arithmetic_shift_floor(A,lam)
        assert G>0 and G<=2*S
        print(f"A={A:g} G={G:.9f} S={S:.9f} G/S={G/S:.6f}")

    ell=1.4
    print(f"Prime -> rank-one pole strong boundary convergence (ell={ell})")
    for X in [2500,25000,250000]:
        count,mass,eta,err=boundary_probe(X,ell,lam)
        print(f"X={X:6d} events={count:5d} mass={mass:.9f} "
              f"CDF_err={eta:.6g} strong_L2_relative_err={err:.7g}")
    assert boundary_probe(250000,ell,lam)[-1] < boundary_probe(2500,ell,lam)[-1]

    print("PASS: zero-input exact-constant and finite PNT/shift calibrations.")
    print("The all-horizon RH rate remains UNPROVED.")


if __name__ == "__main__":
    main()
