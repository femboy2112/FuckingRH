"""Exact carrier/valuation and affine-current controls for Round 007.

These finite checks falsify operator identities; they do not certify any
infinite Weil positivity assertion.  No zeta-zero data are used.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def valuation(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError("carrier states are positive integers")
    result: dict[int, int] = {}
    divisor = 2
    remainder = n
    while divisor * divisor <= remainder:
        while remainder % divisor == 0:
            result[divisor] = result.get(divisor, 0) + 1
            remainder //= divisor
        divisor += 1
    if remainder > 1:
        result[remainder] = result.get(remainder, 0) + 1
    return result


def support_size(n: int) -> int:
    return len(valuation(n))


def omega(n: int) -> int:
    """Total number of prime factors, counted with multiplicity."""
    return sum(valuation(n).values())


def carrier_jump(n: int) -> dict[int, int]:
    before, after = valuation(n), valuation(n + 1)
    return {p: after.get(p, 0) - before.get(p, 0)
            for p in sorted(before.keys() | after.keys())}


def stratum_current(n: int, r: int) -> int:
    """Coefficient of |n+1> in [Sigma,P_r]|n>; exit minus entry."""
    if r < 0:
        raise ValueError("support strata have nonnegative index")
    return int(support_size(n) == r) - int(support_size(n + 1) == r)


def jet_charge(n: int):
    factors = valuation(n)
    return sp.log(next(iter(factors))) if len(factors) == 1 else sp.Integer(0)


def return_time(p: int, k: int, steps: int = 1) -> int:
    """Elapsed SUCC time along a geometric jet (prime status not needed)."""
    if p < 2 or k < 0 or steps < 0:
        raise ValueError("require p>=2 and k,steps>=0")
    return p ** k * (p ** steps - 1)


def shift(size: int, power: int = 1) -> sp.Matrix:
    if size < 1 or power < 0:
        raise ValueError("require positive size, nonnegative power")
    return sp.Matrix(size, size, lambda i, j: int(i == j + power))


def affine_branches(m: int, r: int, inputs: int) -> tuple[sp.Matrix, sp.Matrix]:
    """All output rows are retained, so there is no upper-cutoff defect."""
    if m < 1 or r < 0 or inputs < 1:
        raise ValueError("require m,inputs>=1 and r>=0")
    rows = m * inputs + r
    plus, minus = sp.zeros(rows, inputs), sp.zeros(rows, inputs)
    for j in range(inputs):
        value = m * (j + 1)
        plus[value + r - 1, j] = 1
        if value > r:
            minus[value - r - 1, j] = 1
    return plus, minus


def predicted_affine_square(m: int, r: int, inputs: int) -> sp.Matrix:
    result = 2 * sp.eye(inputs)
    for j in range(min(r // m, inputs)):
        result[j, j] -= 1
    if (2 * r) % m == 0:
        cross = shift(inputs, (2 * r) // m)
        result -= cross + cross.T
    return result


def doubled_dirac(c: sp.Matrix) -> tuple[sp.Matrix, sp.Matrix]:
    rows, columns = c.shape
    d = sp.zeros(columns + rows)
    d[:columns, columns:] = c.T
    d[columns:, :columns] = c
    gamma = sp.diag(*([1] * columns + [-1] * rows))
    return d, gamma


def graph_projection(size: int) -> sp.Matrix:
    """Valuation basis is relabeled by its unique integer for this control."""
    return sp.diag(*(int(n == m)
                     for n in range(1, size + 1)
                     for m in range(1, size + 1)))


def evidence() -> dict:
    examples = []
    for n in range(1, 33):
        examples.append({
            "n": n, "valuation": valuation(n), "jump": carrier_jump(n),
            "jump_distance": sum(abs(a) for a in carrier_jump(n).values()),
            "omega_sum": omega(n) + omega(n + 1),
            "strata": [support_size(n), support_size(n + 1)],
            "P1_current": stratum_current(n, 1),
        })
    pairs = []
    for m, r in [(2, 1), (3, 1), (4, 2), (3, 3), (2, 5), (1, 1), (2, 0)]:
        ap, am = affine_branches(m, r, 6)
        c = ap - am
        actual = c.T * c
        expected = predicted_affine_square(m, r, 6)
        assert actual == expected
        pairs.append({"m": m, "r": r, "lower_boundary_rank": r // m,
                      "cross_step": 2 * r // m if 2 * r % m == 0 else None,
                      "square": actual.tolist()})
    return {"status": "exact finite controls; no RH inference",
            "carrier_examples": examples, "affine_examples": pairs,
            "height_commutator_partial_trace": "log(M+1)",
            "graph_gap_in_horizon_N": "log(N/(N-1)), N>=2",
            "first_return_examples": [
                {"p": p, "k": k, "tau": return_time(p, k)}
                for p in (2, 3, 5, 7) for k in range(4)]}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=Path("research/astra_round_007/evidence/geometry.json"))
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence(), indent=2, default=int) + "\n")
    print(args.output)


if __name__ == "__main__":
    main()
