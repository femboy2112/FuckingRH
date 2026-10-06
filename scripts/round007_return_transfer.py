"""Exact discriminators for genuine forward jet returns versus inserted loops.

Run ``python -m scripts.round007_return_transfer`` to reproduce the evidence.
No zeros, numerical PSD decisions, or completed independent prime towers occur.
The determinant conclusions at infinite volume are proved in the companion note.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def jet_states(horizon: int, bases=None):
    """Decorated states (base, depth, integer), truncated by base**depth <= N.

    For actual primes these are distinct integer states. Explicit other bases
    are permitted only for mutation controls; collisions remain decorated.
    The shared state 1 is excluded so that it is not duplicated over primes.
    """
    if horizon < 1:
        raise ValueError("horizon must be positive")
    if bases is None:
        bases = list(sp.primerange(2, horizon + 1))
    bases = tuple(int(b) for b in bases)
    if len(set(bases)) != len(bases) or any(b < 2 for b in bases):
        raise ValueError("bases must be distinct integers >= 2")
    states = []
    for b in bases:
        k, n = 1, b
        while n <= horizon:
            states.append((b, k, n))
            k, n = k + 1, n * b
    return sorted(states, key=lambda x: (x[2], x[0]))


def return_data(base: int, depth: int, returns: int = 1):
    """Exact SUCC count and log-time cocycle, including the common source k=0."""
    if base < 2 or depth < 0 or returns < 0:
        raise ValueError("base >= 2 and nonnegative depths are required")
    start = base**depth
    end = base**(depth + returns)
    return {"start": start, "end": end, "succ_steps": end - start,
            "log_roof": returns * sp.log(base)}


def return_transfer(horizon: int, bases=None, exponent=2, mode="roof"):
    """Pushforward on counting l2: e_(p,k) -> weight * e_(p,k+1).

    ``roof`` uses p**(-exponent), the actual constant log-return roof.
    ``height`` uses (p**k)**(-exponent), extra absolute-height damping.
    Missing targets outside the carrier horizon are killed, never wrapped.
    """
    if mode not in {"roof", "height", "unit"}:
        raise ValueError("mode must be roof, height, or unit")
    states = jet_states(horizon, bases)
    positions = {(p, k): j for j, (p, k, _) in enumerate(states)}
    result = sp.zeros(len(states))
    for j, (p, k, n) in enumerate(states):
        target = positions.get((p, k + 1))
        if target is not None:
            weight = sp.Integer(1)
            if mode != "unit":
                weight = sp.Integer(p if mode == "roof" else n)**(-sp.sympify(exponent))
            result[target, j] = weight
    return states, result


def collapsed_euler_operator(bases, exponent=2):
    """Changed dynamics: one weighted self-loop per supplied base."""
    return sp.diag(*(sp.Integer(b)**(-sp.sympify(exponent)) for b in bases))


def path_determinant(depth: int, edge_weight, z):
    """det(I-z*a*(R+R*)) for a real edge weight; exact continuant."""
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    a = sp.sympify(edge_weight)
    previous, current = sp.Integer(1), sp.Integer(1)
    for _ in range(2, depth + 1):
        previous, current = current, sp.expand(current - z*z*a*a*previous)
    return current


def matrix_record(horizon: int, bases=None, mode="roof"):
    states, matrix = return_transfer(horizon, bases, mode=mode)
    z = sp.Symbol("z")
    powers = []
    term = sp.eye(len(states))
    for _ in range(1, min(8, len(states)) + 1):
        term = term * matrix
        powers.append(str(sp.trace(term)))
    return {"horizon": horizon, "mode": mode,
            "states": [list(s) for s in states],
            "edges": [[states[j][2], states[i][2], str(matrix[i, j])]
                      for i in range(len(states)) for j in range(len(states))
                      if matrix[i, j] != 0],
            "det_I_minus_z_transfer": str((sp.eye(len(states)) - z*matrix).det()),
            "traces_of_powers": powers}


def evidence():
    z = sp.Symbol("z")
    actual = [matrix_record(n, mode=mode)
              for n in [2, 4, 9, 16, 32, 64] for mode in ["roof", "height"]]
    mutations = {
        "delete_prime_3": matrix_record(32, bases=[2, 5, 7, 11, 13]),
        "insert_composite_6": matrix_record(64, bases=[2, 3, 5, 6, 7]),
        "coprime_composite_generators": matrix_record(64, bases=[4, 9, 25]),
        "mutate_roof_to_unit": matrix_record(32, mode="unit"),
    }
    bases = [2, 3, 5]
    collapsed = collapsed_euler_operator(bases)
    one_jet, shift = return_transfer(64, bases=[2])
    jacobi = shift + shift.T
    diagonal = sp.diag(*(sp.Rational(1, n*n) for _, _, n in one_jet))
    return {
        "status": "exact finite discriminators; infinite theorem is in DYNAMICAL_ZETA_AUDIT.md",
        "actual_carrier_horizons": actual,
        "forward_mutations_all_have_determinant_one": mutations,
        "inserted_loops": {
            "bases": bases,
            "determinant": str(sp.factor((sp.eye(3)-z*collapsed).det())),
            "at_z_one": str((sp.eye(3)-collapsed).det()),
            "changed_dynamics": True,
        },
        "backward_orientation_added": {
            "base": 2, "states": len(one_jet),
            "determinant": str(sp.factor((sp.eye(len(one_jet))-z*jacobi).det())),
            "trace_square": str(sp.trace(jacobi*jacobi)),
            "continuant_matches": sp.expand((sp.eye(len(one_jet))-z*jacobi).det()
                                               - path_determinant(len(one_jet), sp.Rational(1, 4), z)) == 0,
        },
        "forward_current_invisible_to_triangular_determinant": {
            "det_diagonal_plus_shift": str(sp.factor((sp.eye(len(one_jet))-z*(diagonal+shift)).det())),
            "equals_diagonal_determinant": sp.expand((sp.eye(len(one_jet))-z*(diagonal+shift)).det()
                                                       -(sp.eye(len(one_jet))-z*diagonal).det()) == 0,
        },
    }


if __name__ == "__main__":
    path = Path(__file__).resolve().parents[1] / "research/astra_round_007/evidence/return_transfer.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(evidence(), indent=2) + "\n")
    print(path)
