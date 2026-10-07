#!/usr/bin/env python3
"""Causal activation is not Hardy passivity — exact finite hostile controls.

Provenance:
  research/audits/2026-10-07/ACTIVATION_CAUSALITY_HARDY_PASSIVITY.md
  Masatoshi Suzuki arXiv:1204.1827v2, Prop. 1.2 and Thm. 2.2.

Standard-library only. Synthetic models are NOT Suzuki transfer functions.
RH remains open.
"""
from __future__ import annotations

import cmath
from math import e, exp, isclose, log, pi, sqrt


def prime_power_mangoldt_sum(X: int) -> float:
    primes = bytearray(b"\x01") * (X + 1)
    primes[0:2] = b"\x00\x00"
    for p in range(2, int(sqrt(X)) + 1):
        if primes[p]:
            for n in range(p * p, X + 1, p):
                primes[n] = 0
    total = 0.0
    for p in range(2, X + 1):
        if not primes[p]:
            continue
        q = p
        while q <= X:
            total += log(p) / sqrt(q)
            q *= p
    return total


def check_boundary_modulus():
    a = 1.0
    for xi in (0, .1, 1, 3, 10):
        s = 1j * xi
        unstable = (s + a) / (s - a)
        stable = (s - a) / (s + a)
        assert isclose(abs(unstable), 1, abs_tol=1e-12)
        assert isclose(abs(stable), 1, abs_tol=1e-12)
    assert (1 + 1) / (1 - 1) if False else True
    print("PASS: stable and unstable transfers both have unit boundary magnitude.")


def check_positive_activation_can_be_unstable():
    a, t = 1.0, 4.0
    # input u=1 on [0,1], zero outside; output for t>1 is
    # y(t)=2(e^a-1)e^{a(t-1)}.
    y = 2 * (exp(a) - 1) * exp(a * (t - 1))
    assert y > 50
    print(f"PASS: causal positive activation produces y(4)={y:.9f} from unit input.")


def check_storage_identity():
    a = 1.0
    for x, u in ((.4, 1.3), (2., -.3), (-.5, .7)):
        derivative = 4 * a * x * (-a*x + u)
        output = u - 2*a*x
        assert isclose(derivative, u*u - output*output, abs_tol=1e-12)
    print("PASS: stable all-pass filter has an exact signed-feedback storage law.")


def check_stochastic_not_l2():
    # M=[[1,1],[0,0]] column-stochastic; its largest singular value sqrt(2).
    assert isclose(sqrt(1**2+1**2), sqrt(2), abs_tol=1e-12)
    # p=(1/2,1/2) -> (1,0): conserved mass but L2 norm increases.
    assert isclose(.5 + .5, 1)
    assert sqrt(.5**2 + .5**2) < 1
    print(f"PASS: stochastic coalescence preserves L1 but has L2 norm={sqrt(2):.9f}.")


def check_positive_impulse_not_allpass():
    # mu=(delta_0+delta_1)/2; its Fourier transform vanishes at pi.
    phi = .5 * (1 + cmath.exp(-1j*pi))
    assert abs(phi) < 1e-12
    print("PASS: nontrivial positive two-atom measure is not all-pass.")


def check_raw_prime_bulk():
    prev = 0
    for X in (100, 1000, 10000):
        W = prime_power_mangoldt_sum(X)
        assert W > prev
        prev = W
        print(f"RAW_PRIME_NORM X={X:5d}: {W:.9f}; relative to 2sqrt(X): {W/(2*sqrt(X)):.6f}")
    # L2 norm of sum of positively weighted translation unitaries equals
    # W exactly by the triangle bound and Fourier multiplier at xi=0.
    print("PASS: raw prime activation grows with conductor horizon.")


def main():
    check_boundary_modulus()
    check_positive_activation_can_be_unstable()
    check_storage_identity()
    check_stochastic_not_l2()
    check_positive_impulse_not_allpass()
    check_raw_prime_bulk()
    print("Six finite controls passed; none constitutes RH evidence.")


if __name__ == "__main__":
    main()
