#!/usr/bin/env python3
"""Calibrated boundary-elimination/centering probe; no RH positivity claim.

The Fraction controls certify exact finite identities and a false sign rule.
The Gamma/prime step-cell checks are floating-point diagnostics of the stated
closed-form matrices. They do not certify continuum or all-horizon positivity.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from scipy.special import digamma, polygamma


def schur(matrix: np.ndarray, boundary_size: int = 1) -> np.ndarray:
    a = matrix[:boundary_size, :boundary_size]
    b = matrix[:boundary_size, boundary_size:]
    c = matrix[boundary_size:, boundary_size:]
    return a - b @ np.linalg.solve(c, b.conj().T)


def exact_colligation_control() -> dict:
    r, s = F(3, 5), F(4, 5)
    assert r * r + s * s == 1

    def transfer(z):
        return r - z * s * s / (1 - r * z)

    points = [F(0), F(1, 3), F(-1, 2), F(2, 5)]
    for w in points:
        for z in points:
            lhs = 1 - transfer(w) * transfer(z)
            rhs = (1 - w * z) * s * s / ((1 - r * w) * (1 - r * z))
            assert lhs == rhs
    z = F(1, 2)
    truncated_transfer = r - z * s * s
    missing_return = transfer(z) - truncated_transfer
    assert missing_return == F(-24, 175)
    # A zero-state transfer does not include a nonzero initial history.
    initial_history_coefficient = s / (1 - r * z)
    assert initial_history_coefficient == F(8, 7)
    return {
        "status": "EXACT_FRACTION_PASS",
        "cross_kernel_pairs": len(points) ** 2,
        "omitting_internal_returns_mutation_rejected": True,
        "missing_return_at_z_half": str(missing_return),
        "initial_history_boundary_coefficient": str(initial_history_coefficient),
    }


def exact_centering_controls() -> dict:
    rows = []
    for n in (0, 1, 10, 100):
        a, b, c, kappa = F(n) + F(7, 4), F(-1), F(n + 2), F(n + 1)
        assert a > 0 and a * c - b * b > 0
        naive = a - b * b / c - kappa
        correct = a - kappa - b * b / (c - kappa)
        correction = kappa * b * b / (c * (c - kappa))
        assert naive - correction == correct == F(-1, 4)
        assert naive > 0
        # At boundary value 1, the true minimizing hidden value is 1.
        witness = a + 2 * b + c - 2 * kappa
        assert witness == F(-1, 4)
        rows.append({
            "cutoff": n,
            "passive_determinant": str(a * c - b * b),
            "wrong_reduce_then_center": str(naive),
            "correct_center_then_reduce": str(correct),
            "omitted_correction": str(correction),
            "negative_witness": [1, 1],
            "negative_witness_energy": str(witness),
        })
    # Positive control: same coupling and hidden block, larger boundary energy.
    positive_control = F(5, 4) - F(1)
    assert positive_control == F(1, 4)
    # Degenerate control: no coupling, hence no order error.
    assert F(1) * F(0) ** 2 / (F(2) * F(1)) == 0
    # Weil-shaped scalar plus rank-one subtraction. Even when P has no
    # boundary/interior coupling, the pole rank-one term creates one.
    # P=2I, D=(1/2)I+[[1,1],[1,1]], Q=[[1/2,-1],[-1,1/2]].
    pole_naive = F(2) - (F(1, 2) + 1)
    pole_correct = F(1, 2) - 1 / F(1, 2)
    assert pole_naive == F(1, 2) and pole_correct == F(-3, 2)
    resonance_rows = []
    for epsilon in (F(1, 10), F(1, 1000)):
        naive = 1 - 1 / (1 + epsilon)
        correct = 1 - 1 / epsilon
        correction = 1 / (epsilon * (1 + epsilon))
        assert naive > 0 > correct
        assert naive - correction == correct
        resonance_rows.append({
            "hidden_centered_gap": str(epsilon),
            "wrong_boundary": str(naive),
            "correct_boundary": str(correct),
            "omitted_correction": str(correction),
        })
    return {
        "status": "EXACT_FRACTION_PASS",
        "cutoff_family": rows,
        "positive_control_boundary": str(positive_control),
        "decoupled_control_order_error": "0",
        "pole_block_control": {
            "positive_storage": [[2, 0], [0, 2]],
            "scalar_deficit": "1/2",
            "rank_one_deficit": [[1, 1], [1, 1]],
            "wrong_boundary_only_rank_subtraction": str(pole_naive),
            "correct_full_block_subtraction": str(pole_correct),
            "negative_witness": [1, 2],
        },
        "closing_hidden_gap_controls": resonance_rows,
        "reduce_then_center_positivity_rule_rejected": True,
    }


def gamma_step_matrix(cell_width: float, cells: int, terms: int = 512):
    """Exact series formula, with rapidly convergent exponentials truncated.

    The non-exponential tail sum 1/b_j^2 is included through trigamma. Thus
    terms=512 truncates only exponentially decaying series, not a 1/j tail.
    The stated remainder bound excludes special-function/roundoff error.
    """
    b = 2 * np.arange(terms, dtype=float) + 0.5
    total_inverse_square = float(polygamma(1, 0.25)) / 4

    def exponential_sum(k):
        if k == 0:
            return total_inverse_square
        return float(np.sum(np.exp(-b * (k * cell_width)) / (b * b)))

    values = [2 * (exponential_sum(0) - exponential_sum(1)) / cell_width]
    for distance in range(1, cells):
        values.append(-(
            exponential_sum(distance - 1)
            - 2 * exponential_sum(distance)
            + exponential_sum(distance + 1)
        ) / cell_width)
    matrix = np.array([[values[abs(j - k)] for k in range(cells)] for j in range(cells)])
    first_omitted = 2 * terms + 0.5
    exp_tail = math.exp(-first_omitted * cell_width) / (
        first_omitted ** 2 * (1 - math.exp(-2 * cell_width))
    )
    return matrix, 4 * exp_tail / cell_width


def primes_through(limit: int):
    prime = np.ones(limit + 1, dtype=bool)
    prime[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if prime[p]:
            prime[p * p::p] = False
    return [int(p) for p in np.flatnonzero(prime)]


def prime_power_weights(limit: int):
    weights = {}
    for p in primes_through(limit):
        n = p
        while n <= limit:
            weights[n] = math.log(int(p)) / math.sqrt(n)
            n *= int(p)
    return weights


def step_source_matrix(horizon: float, cells: int, prime_cutoff: int,
                       full_prime_axes: bool = False):
    edges = np.linspace(-horizon, horizon, cells + 1)
    width = float(edges[1] - edges[0])
    gamma, tail_bound = gamma_step_matrix(width, cells)
    prime_energy = np.zeros((cells, cells))
    mass = 0.0
    if full_prime_axes:
        # A finite all-pass prime cascade includes EVERY power of each prime.
        # Powers beyond the support contribute an exact diagonal tail.
        weights = {}
        full_mass = 0.0
        for p in primes_through(prime_cutoff):
            full_mass += math.log(p) / (math.sqrt(p) - 1)
            n = p
            while math.log(n) <= 2 * horizon:
                weights[n] = math.log(p) / math.sqrt(n)
                n *= p
    else:
        weights = prime_power_weights(prime_cutoff)
    for n, weight in weights.items():
        h = math.log(n)
        overlap = np.maximum(
            0,
            np.minimum(edges[1:, None], edges[None, 1:] + h)
            - np.maximum(edges[:-1, None], edges[None, :-1] + h),
        ) / width
        prime_energy += weight * (2 * np.eye(cells) - overlap - overlap.T)
        mass += weight
    if full_prime_axes:
        prime_energy += 2 * (full_mass - mass) * np.eye(cells)
        mass = full_mass
    cosine = 2 * (np.sinh(edges[1:] / 2) - np.sinh(edges[:-1] / 2)) / math.sqrt(width)
    sine = 2 * (np.cosh(edges[1:] / 2) - np.cosh(edges[:-1] / 2)) / math.sqrt(width)
    scalar = math.log(math.pi) - float(digamma(0.25)) + 2 * mass
    positive = gamma + prime_energy + 2 * np.outer(cosine, cosine)
    deficit = scalar * np.eye(cells) + 2 * np.outer(sine, sine)
    return positive, deficit, scalar, tail_bound, mass


def source_centering_controls() -> dict:
    rows = []
    for horizon in (0.5, 1.0, 2.0):
        cells = 16
        cutoff = math.floor(math.exp(2 * horizon))
        p, d, kappa, tail, mass = step_source_matrix(horizon, cells, cutoff)
        even = np.zeros((cells, cells // 2))
        for j in range(cells // 2):
            even[j, j] = even[cells - 1 - j, j] = 1 / math.sqrt(2)
        pe = even.T @ p @ even
        de = even.T @ d @ even
        qe = pe - de
        assert np.linalg.norm(de - kappa * np.eye(cells // 2), ord=2) < 1e-11
        gap = float(np.linalg.eigvalsh(qe[1:, 1:])[0])
        assert gap > 0, "Selected finite control must have a positive hidden block."
        naive = schur(pe) - kappa
        correct = schur(qe)
        b, c = pe[:1, 1:], pe[1:, 1:]
        correction = kappa * b @ np.linalg.solve(
            c - kappa * np.eye(c.shape[0]), np.linalg.solve(c, b.T)
        )
        identity_error = float(np.linalg.norm(naive - correct - correction))
        assert identity_error < 2e-10
        assert float(correction[0, 0]) > 1e-4
        # The full-space prime form is needed: compressing the shift first
        # and then taking its square omits escaped mass at the boundary.
        box = np.ones(cells) / math.sqrt(cells)
        h = math.log(2)
        edges = np.linspace(-horizon, horizon, cells + 1)
        width = edges[1] - edges[0]
        overlap = np.maximum(
            0,
            np.minimum(edges[1:, None], edges[None, 1:] + h)
            - np.maximum(edges[:-1, None], edges[None, :-1] + h),
        ) / width
        true_square = float(box @ (2 * np.eye(cells) - overlap - overlap.T) @ box)
        compressed_square = float(np.linalg.norm(box - overlap @ box) ** 2)
        assert true_square > compressed_square + 1e-4
        # Add actual prime terms entirely beyond the fixed support horizon.
        p2, d2, _, _, mass2 = step_source_matrix(horizon, cells, max(1000, cutoff + 1))
        increment = 2 * (mass2 - mass)
        cutoff_identity_error = max(
            float(np.linalg.norm((p2 - p) - increment * np.eye(cells), 2)),
            float(np.linalg.norm((d2 - d) - increment * np.eye(cells), 2)),
            float(np.linalg.norm((p2 - d2) - (p - d), 2)),
        )
        assert cutoff_identity_error < 2e-10
        p_axes, d_axes, _, _, axis_mass = step_source_matrix(
            horizon, cells, 1000, full_prime_axes=True
        )
        axis_increment = 2 * (axis_mass - mass)
        axis_identity_error = max(
            float(np.linalg.norm((p_axes - p) - axis_increment * np.eye(cells), 2)),
            float(np.linalg.norm((d_axes - d) - axis_increment * np.eye(cells), 2)),
            float(np.linalg.norm((p_axes - d_axes) - (p - d), 2)),
        )
        assert axis_identity_error < 2e-10
        rows.append({
            "horizon": horizon,
            "cells": cells,
            "even_dimension": cells // 2,
            "base_prime_cutoff": cutoff,
            "scalar_deficit": kappa,
            "centered_hidden_gap": gap,
            "wrong_reduce_then_center": float(naive[0, 0]),
            "correct_center_then_reduce": float(correct[0, 0]),
            "required_hidden_correction": float(correction[0, 0]),
            "boundary_identity_residual": identity_error,
            "gamma_exponential_tail_entry_bound_excludes_roundoff": tail,
            "box_true_shift_square": true_square,
            "box_compressed_shift_square_mutation": compressed_square,
            "higher_prime_cutoff_identity_residual": cutoff_identity_error,
            "all_powers_of_primes_through_1000_mass": axis_mass,
            "all_prime_axes_identity_residual": axis_identity_error,
        })
    return {
        "status": "FLOATING_POINT_DIAGNOSTIC_OF_PROVED_IDENTITIES",
        "continuum_positivity_certified": False,
        "all_horizon_positivity_certified": False,
        "rows": rows,
    }


def passive_limit_controls() -> dict:
    rows = []
    for offset in (-1.0, 1.0):
        for t in (10.0, 100.0, 1000.0):
            # Both unshifted positive storages are positive, and the same
            # fixed deficit D_0=2 gives the opposite centered signs.
            fixed_deficit = 2.0
            p = t + fixed_deficit + offset
            assert p > 0
            cayley = (p - 1) / (p + 1)
            recovered = t - t * t / (p + 1) - 1 - fixed_deficit
            exact_error = -(fixed_deficit + offset + 1) ** 2 / (
                t + fixed_deficit + offset + 1
            )
            assert abs(recovered - offset - exact_error) < 1e-11
            rows.append({
                "centered_energy": offset,
                "divergent_positive_mass": t,
                "fixed_deficit": fixed_deficit,
                "passive_cayley": cayley,
                "rescaled_resolvent_recovery": recovered,
            })
    return {
        "status": "FLOATING_POINT_DIAGNOSTIC_OF_EXACT_SCALAR_FORMULAS",
        "same_passive_limit_opposite_centered_signs": True,
        "rows": rows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = {
        "claim_status": "PROVED_FINITE_IDENTITIES_AND_CALIBRATED_DIAGNOSTICS",
        "rh_claim": False,
        "colligation": exact_colligation_control(),
        "rational_centering": exact_centering_controls(),
        "actual_source_matrices": source_centering_controls(),
        "passive_limit": passive_limit_controls(),
    }
    path = args.output
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("PASS: exact colligation, scalar/pole centering, actual Gamma/prime matrices, passive-limit controls")
    print(json.dumps({"maximum_boundary_residual": max(row["boundary_identity_residual"] for row in report["actual_source_matrices"]["rows"])}))


if __name__ == "__main__":
    main()
