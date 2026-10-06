"""Small exact/Arb mutation battery for the Round007 lifted geometry.

No mutated kernel is claimed PSD.  Separate identity sensitivity from the
negative residual witness that survives arbitrary nonnegative event weights.
"""
from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path
from random import Random

import sympy as sp
from flint import arb, ctx

from .round007_geometry import shift
from .round007_factor_cone import factor_lift, swap_matrix
from .round007_squares import event_weights, positive_gamma, scalar_parts
from .event_dynamics import gamma_linear
from .suzuki_psi import prime_power_events_up_to, primes_up_to

SEED = 20261007


def random_coprime_generators(seed=SEED):
    primes = [2, 3, 5, 7, 11, 13]
    Random(seed).shuffle(primes)
    return [primes[j] * primes[j + 1] for j in range(0, len(primes), 2)]


def generator_events(generators, horizon):
    out = {}
    for g in generators:
        n = g
        while n <= horizon:
            out[n] = out.get(n, arb(0)) + arb(g).log() / arb(n).sqrt()
            n *= g
    return out


def bulk_rayleigh(weights, linear=None):
    """Cancel the positive rank-one pole direction analytically.

    This evaluates the residual formula for arbitrary nonnegative weights;
    the document proof, not finite sampling, supplies its universal scope.
    """
    c = gamma_linear() if linear is None else arb(linear)
    d = sum(weights.values(), arb(0)) - c
    times = [arb(2).log(), arb(3).log()]
    v = [(times[1] / 2).sinh(), -(times[0] / 2).sinh()]
    matrix = [[8 * ((t / 2).sinh() * (u / 2).sinh()
                   - ((t / 2).cosh() - 1) * ((u / 2).cosh() - 1))
               - 2 * d * min(t, u) for u in times] for t in times]
    return sum((v[i] * matrix[i][j] * v[j]
                for i in range(2) for j in range(2)), arb(0))


def fake_monoid_map():
    """Generators 2 and 4: exponent vectors (0,1) and (2,0) collide."""
    return sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1]])


def broken_factor_swap(horizon=8):
    pairs, canonical = factor_lift(horizon, normalized=True)
    swap = swap_matrix(pairs)
    asymmetric = sp.diag(*(2 if a < b else 1 for a, b in pairs)) * canonical
    return canonical, asymmetric, swap


def permuted_carrier(size=8):
    order = list(range(1, size + 1))
    order[1], order[3] = order[3], order[1]
    permutation = sp.zeros(size)
    for j, n in enumerate(order):
        permutation[n - 1, j] = 1
    return order, permutation * shift(size) * permutation.T


def label_mutation(horizon=32, seed=SEED):
    primes = primes_up_to(horizon)
    labels = primes.copy()
    Random(seed).shuffle(labels)
    permutation = dict(zip(primes, labels))
    weights = {event.n: arb(permutation[event.prime]).log() / arb(event.n).sqrt()
               for event in prime_power_events_up_to(horizon)}
    return permutation, weights


def braid_matrices(p, inputs=7):
    size = p * (inputs + 1) + 1
    s, v = shift(size), sp.zeros(size)
    for n in range(1, size // p + 1):
        v[p * n - 1, n - 1] = 1
    return ((s * v)[:, :inputs], (v * s)[:, :inputs],
            ((s ** p) * v)[:, :inputs])


def evidence():
    ctx.prec = 180
    horizon = 32
    base = event_weights(horizon)
    generators = random_coprime_generators()
    assert all(gcd(generators[i], generators[j]) == 1
               for i in range(len(generators)) for j in range(i))
    generic = generator_events(generators, 256)
    ones = {e.n: 1 / arb(e.n).sqrt() for e in prime_power_events_up_to(horizon)}
    tilt = {e.n: arb(e.prime).log() * (-arb(e.n).log() / 3).exp()
            for e in prime_power_events_up_to(horizon)}
    permutation, relabeled = label_mutation(horizon)
    changed_label = next(p for p in permutation if permutation[p] != p)
    weight_delta = relabeled[changed_label] - base[changed_label]
    assert not weight_delta.contains(0)
    assert ones[2] - base[2] > 0 and tilt[2] - base[2] > 0
    assert all(w > 0 for model in (base, generic, ones, tilt, relabeled)
               for w in model.values())

    rays = {"actual": bulk_rayleigh(base), "coprime_composites": bulk_rayleigh(generic),
            "unit_log_charge": bulk_rayleigh(ones), "one_third_density": bulk_rayleigh(tilt),
            "permuted_charge_labels": bulk_rayleigh(relabeled)}
    assert all(value < 0 for value in rays.values())
    fake = fake_monoid_map()
    kernel = sp.Matrix([0, 0, 1, -1])
    assert fake * kernel == sp.zeros(3, 1)
    canonical, asymmetric, swap = broken_factor_swap()
    assert swap * canonical == canonical and swap * asymmetric != asymmetric
    canonical_energy, mutated_energy = canonical.T * canonical, asymmetric.T * asymmetric
    assert canonical_energy == sp.eye(8) and mutated_energy != canonical_energy
    asym_current = asymmetric - swap * asymmetric
    order, _ = permuted_carrier()
    p2_hits = [n for n in order if n in (1, 2, 4, 8)]
    complete_mass = sum((arb(p).log() / (arb(p).sqrt() - 1)
                         for p in primes_up_to(horizon)), arb(0))
    extra_mass = complete_mass - sum(base.values(), arb(0))
    assert extra_mass > 0
    t = arb(2).log() * arb(3) / 2
    gamma_contribution = gamma_linear() * t + positive_gamma(t)
    assert gamma_contribution < 0
    no_gamma_ray = bulk_rayleigh(base, linear=0)
    assert no_gamma_ray < 0
    E, residual, target = scalar_parts(t, base)
    finite_extended = generator_events(primes_up_to(horizon), horizon ** 2)
    ext_E, ext_residual, ext_target = scalar_parts(t, finite_extended)
    ext_mass = sum(finite_extended.values(), arb(0)) - sum(base.values(), arb(0))
    assert ext_mass > 0 and (ext_target - target).contains(0)
    assert (ext_E - E - ext_mass * t).contains(0)
    assert (ext_residual - residual + ext_mass * t).contains(0)
    # Completed infinite towers change local repair mass, not ramps before L.
    assert ((E + extra_mass * t) + (residual - extra_mass * t) - target).contains(0)
    for p in (2, 3, 5):
        sv, vs, spv = braid_matrices(p)
        assert sv != vs and vs == spv

    return {
        "seed": SEED, "bits": ctx.prec,
        "scope": "exact identity sensitivity and finite Arb residual witnesses; no mutated PSD claim",
        "coprime_generators": {
            "generators": generators, "horizon": 256, "events": sorted(generic),
            "all_composite": all(not sp.isprime(g) for g in generators),
            "first_return_geometry_survives": True,
            "zeta_prime_event_identity_fails": 2 not in generic,
        },
        "unit_log_charge": {"at_2_mutant_minus_actual": str(ones[2] - base[2]),
                            "event_support_unchanged": sorted(ones) == sorted(base)},
        "half_density_tilt": {"theta": "1/3", "at_2_mutant_minus_actual": str(tilt[2] - base[2]),
                              "event_support_unchanged": sorted(tilt) == sorted(base)},
        "fake_monoid": {"generators": [2, 4], "collision": [[0, 1], [2, 0]],
                        "collision_value": 4, "map": fake.tolist(),
                        "kernel_vector": list(kernel), "rank": fake.rank()},
        "destroyed_factor_swap": {
            "horizon": 8, "mutation": "multiply normalized factor-lift rows a<b by 2; other rows by 1",
            "canonical_swap_invariance": True, "mutated_swap_invariance": False,
            "canonical_compressed_energy_diagonal": [str(x) for x in canonical_energy.diagonal()],
            "mutated_compressed_energy_diagonal": [str(x) for x in mutated_energy.diagonal()],
            "mutated_swap_current_energy_diagonal": [str(x) for x in (asym_current.T * asym_current).diagonal()],
            "classification": "identity sensitivity only; no Weil or mutated PSD inference"},
        "destroyed_carrier_order": {"order": order, "prime_2_section_hits": p2_hits,
                                    "negative_log_step": "log(3/4)",
                                    "valuation_bijection_unchanged": True},
        "randomized_jet_charge_labels": {
            "permutation": permutation, "first_changed_prime": changed_label,
            "mutant_minus_actual_at_first_change": str(weight_delta),
            "held_fixed": "SUCC, integer heights, event locations; only log charge labels permuted",
            "caveat": "A fully transported coordinate relabeling is unitary and is not this mutation."},
        "independently_completed_towers": {
            "horizon": horizon, "same_prime_heads": primes_up_to(horizon),
            "infinite_tower_mass_minus_carrier_mass": str(extra_mass),
            "first_extra_2_tower_event": 64,
            "independent_finite_tower_recheck_horizon": horizon ** 2,
            "local_repair_energy_change": "extra_mass * abs(t)",
            "local_residual_change": "-extra_mass * abs(t)",
            "local_target_unchanged_below_log_N": True},
        "removed_gamma": {
            "removed": "gamma_linear*abs(t) + positive_gamma(t); pole and prime terms retained",
            "test_time": "3*log(2)/2", "actual_minus_mutant": str(gamma_contribution),
            "no_gamma_bulk_rayleigh": str(no_gamma_ray)},
        "negative_residual_witnesses": {k: str(v) for k, v in rays.items()},
        "braid": {"primes_checked": [2, 3, 5], "inputs": 7,
                  "noncommutation": "S V_p != V_p S", "identity": "V_p S = S^p V_p"},
        "interpretation": "Arithmetic identities are mutation-sensitive. The canonical edge-square bulk mismatch survives these positive event mutations and Gamma removal; that is a class obstruction, not evidence that the mutants satisfy RH positivity.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=Path("research/astra_round_007/evidence/hostile_controls.json"))
    args = parser.parse_args()
    result = evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, default=int) + "\n")
    print(args.output)


if __name__ == "__main__":
    main()
