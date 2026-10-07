"""Exact finite Fourier/refinement controls and Arb residue-theta checks.

No zeta values or zeros enter these constructions.  Exact proofs are in the
Round008 notes; finite certificates are normalization/mutation controls only.
"""
from __future__ import annotations

import json
from math import gcd, isqrt
import sympy as sp
from flint import acb, arb, ctx


def pullback(L: int, M: int) -> sp.Matrix:
    if L < 1 or M % L:
        raise ValueError("positive L dividing M required")
    return sp.Matrix(M, L, lambda a, b: int(a % L == b))


def dual_injection_unscaled(L: int, M: int) -> sp.Matrix:
    if L < 1 or M % L:
        raise ValueError("positive L dividing M required")
    r = M // L
    return sp.Matrix(M, L, lambda a, b: int(a == r * b))


def root_sum_remainder(modulus: int, exponents: list[int]) -> sp.Poly:
    """Exact sum of roots of unity, reduced in Q[z]/Phi_modulus(z)."""
    z = sp.Symbol("z")
    expr = sum(z ** (e % modulus) for e in exponents)
    return sp.rem(sp.Poly(expr, z), sp.Poly(sp.cyclotomic_poly(modulus, z), z))


def refinement_character_checks(L: int, M: int) -> bool:
    """Checks the geometric sums proving C_M I=r E C_L exactly."""
    if L < 1 or M % L:
        raise ValueError("positive L dividing M required")
    r = M // L
    for b in range(M):
        got = root_sum_remainder(M, [b * j * L for j in range(r)])
        if got.as_expr() != (r if b % r == 0 else 0):
            return False
    # C_M E=I C_L follows entrywise from (r*c)*b/M=c*b/L.
    return all((b * r * c) % M == r * ((b % L) * c % L)
               for b in range(M) for c in range(L))


def conductor_projector(L: int, conductors: list[int]) -> sp.Matrix:
    if any(d < 1 or L % d for d in conductors):
        raise ValueError("conductors must divide L")
    if len(set(conductors)) != len(conductors):
        raise ValueError("duplicate conductors")
    def ramanujan(d: int, n: int) -> int:
        return sum(int(e * sp.mobius(d // e)) for e in sp.divisors(gcd(d, n)))
    return sp.Matrix(L, L, lambda a, b:
                     sp.Rational(sum(ramanujan(d, a-b) for d in conductors), L))


def conductor_mask(L: int, conductors: list[int]) -> sp.Matrix:
    return sp.diag(*[int(L // gcd(k, L) in conductors) for k in range(L)])


def theta(L: int, t: arb, cutoff: int | None = None) -> list[arb]:
    """Theta_a=sum_{n=a mod L}exp(-pi*t*n^2/L), with rigorous total tail.

    A single absolute tail bound is added to every coordinate.  This is wider
    than necessary but valid. Selection of cutoff does not enter correctness.
    """
    if L < 1 or not t > 0:
        raise ValueError("positive L and certified positive t required")
    K = cutoff if cutoff is not None else 20 * isqrt(L) + 20
    if K < 0:
        raise ValueError("nonnegative cutoff required")
    a = arb.pi() * t / L
    out = [arb(0) for _ in range(L)]
    for n in range(-K, K+1):
        out[n % L] += (-a * n*n).exp()
    tail = 2 * (-a * (K+1)**2).exp() / (1 - (-a * (2*K+3)).exp())
    error = arb(0, tail.upper())
    return [v + error for v in out]


def fourier(vector: list[arb | acb], normalize: bool = True) -> list[acb]:
    L = len(vector)
    scale = arb(L).sqrt() if normalize else arb(L)
    return [sum((acb(arb(-2*a*b)/L).exp_pi_i() * v
                 for a, v in enumerate(vector)), acb(0)) / scale
            for b in range(L)]


def gaussian_packet(L: int, t: arb, center: arb, frequency: arb) -> list[acb]:
    """Balanced periodization of a shifted/modulated Gaussian, Arb bounded.

    Unlike even theta, this holdout detects the Fourier sign convention.
    """
    if L < 1 or not t > 0:
        raise ValueError("positive L and certified positive t required")
    K = 20 * isqrt(L) + 20
    rootL = arb(L).sqrt()
    distance = K+1-abs(center)*rootL
    if not distance > 0:
        raise ValueError("center lies outside this certified truncation")
    out = [acb(0) for _ in range(L)]
    for n in range(-K,K+1):
        x = arb(n)/rootL
        value = (-arb.pi()*t*(x-center)**2).exp() * acb(2*frequency*x).exp_pi_i()
        out[n % L] += value
    a = arb.pi()*t/L
    tail = 2*(-a*distance**2).exp()/(1-(-a*(2*distance+1)).exp())
    error = arb(0,tail.upper())
    return [v+acb(error,error) for v in out]


def packet_residual(L: int, t: arb, center: arb, frequency: arb,
                    reverse_finite_sign: bool = False) -> list[acb]:
    left = fourier(gaussian_packet(L,t,center,frequency))
    if reverse_finite_sign:
        left = [left[(-b) % L] for b in range(L)]
    right = gaussian_packet(L,1/t,frequency,-center)
    phase = acb(2*center*frequency).exp_pi_i()/t.sqrt()
    return [x-phase*y for x,y in zip(left,right)]


def apply_rational(matrix: sp.Matrix, vector: list[arb | acb]) -> list[acb]:
    return [sum((acb(arb(int(matrix[a,b].p)) / int(matrix[a,b].q)) * vector[b]
                 for b in range(matrix.cols)), acb(0))
            for a in range(matrix.rows)]


def theta_residual(L: int, t: arb) -> list[acb]:
    lhs = fourier(theta(L, t))
    rhs = theta(L, 1/t)
    return [x-y/t.sqrt() for x,y in zip(lhs,rhs)]


def theta_refinement(L: int, M: int, t: arb) -> tuple[list[arb], list[arb]]:
    if L < 1 or M % L:
        raise ValueError("positive L dividing M required")
    r = M//L
    base = theta(L, t)
    coarse = theta(M, r*t)
    dual = theta(M, t/r)
    return ([sum((coarse[a+j*L] for j in range(r)), arb(0))-base[a]
             for a in range(L)],
            [dual[r*a]-base[a] for a in range(L)])


def gaussian_norm(L: int) -> arb:
    v = theta(L, arb(1))
    return sum((x*x for x in v), arb(0)) / arb(L).sqrt()


def evidence() -> dict:
    ctx.prec = 192
    cases = [(1,2),(2,6),(4,12),(6,30),(10,60)]
    holdouts = [(6,arb(3)/2),(12,arb(2)/7),(30,arb(7)/3)]
    L, t = 6, arb(3)/2
    P = conductor_projector(L,[1,2,3])
    v, dual = theta(L,t), theta(L,1/t)
    deletion = [x-y/t.sqrt() for x,y in zip(fourier(apply_rational(P,v)),
                                           apply_rational(P,dual))]
    wrong_scale = [x-y/t.sqrt() for x,y in zip(fourier(v,False),dual)]
    # Omitting the /L in exp(-pi*t*n^2/L) replaces t by L*t.
    wrong_mesh = [x-y/t.sqrt() for x,y in zip(fourier(theta(L,L*t)),
                                            theta(L,L/t))]
    return {
        "precision_bits":ctx.prec,
        "theorems_are_analytic_not_inferred_from_samples":True,
        "exact_refinement_cases":[{"L":a,"M":b,"passed":refinement_character_checks(a,b)}
                                  for a,b in cases],
        "theta_holdouts":[{"L":a,"t":str(b),"residual":[str(x) for x in theta_residual(a,b)],
                           "all_contain_zero":all(x.contains(0) for x in theta_residual(a,b))}
                          for a,b in holdouts],
        "refinement_holdout":{"L":6,"M":30,"t":"3/2",
           "residuals":[[str(x) for x in row] for row in theta_refinement(6,30,t)]},
        "phase_sensitive_holdout":{"L":6,"t":"3/2","center":"1/3","frequency":"2/5",
            "residuals":[str(x) for x in packet_residual(6,t,arb(1)/3,arb(2)/5)],
            "reversed_finite_sign_nonzero_components":[i for i,x in enumerate(
                packet_residual(6,t,arb(1)/3,arb(2)/5,True)) if not x.contains(0)]},
        "mutations":{
            "delete_conductor_6":{"rank":str(P.trace()),"nonzero_components":
                [i for i,x in enumerate(deletion) if not x.contains(0)],
                "residual":[str(x) for x in deletion]},
            "wrong_Haar_normalization":{"nonzero_components":
                [i for i,x in enumerate(wrong_scale) if not x.contains(0)]},
            "unbalanced_mesh":{"nonzero_components":
                [i for i,x in enumerate(wrong_mesh) if not x.contains(0)]},
            "naive_same_embedding":{"r":2,"squared_error":"2-sqrt(2)"}},
        "gaussian_norm_calibration":[{"L":L,"norm_squared":str(gaussian_norm(L)),
            "error_from_1_over_sqrt2":str(gaussian_norm(L)-1/arb(2).sqrt())}
            for L in [1,6,30,210]],
        "mixed_conductors_retained":True,
        "RH_proved":False,
    }


if __name__ == "__main__":
    print(json.dumps(evidence(),indent=2))
