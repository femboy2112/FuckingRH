"""Exact carrier-relative information-flow controls for observational SUCC.

Two independent mechanisms, rigorously distinguished:
1. For every bounded time window a nonnegative screw-form kernel has a
   delayed source-ramp counterpart with identical observations but negative
   global Gram diagonal. This is for a broad CONTINUOUS FUNCTION CLASS,
   not an Euler/Gamma-admissible arithmetic source.
2. A binary finite-observation channel with Bernoulli(1/3) vs Bernoulli(2/3)
   hidden models has strictly ambiguous finite evidence yet infinite
   almost-sure distinguishability (by the strong law).

No RH conclusion, no thermodynamic entropy-production result and no
actual infinite computation is claimed.
"""
from __future__ import annotations

from fractions import Fraction
from typing import Iterable


class CarrierImpedanceError(ValueError):
    """Outside the declared finite carrier / exact-data domain."""


def _int(value: int, name: str, min_value: int = 0, max_value: int = 2048) -> int:
    if type(value) is not int or not min_value <= value <= max_value:
        raise CarrierImpedanceError(
            f"{name} must be an exact integer in [{min_value},{max_value}]"
        )
    return value


def quadratic_psi(t: int) -> int:
    """Reference even source psi(t)=t^2, with globally PSD kernel 2tu."""
    _int(t, "time", -1_000_000, 1_000_000)
    return t * t


def delayed_psi(t: int, threshold: int, amplitude: int) -> int:
    """Fake late kink: NOT an authenticated von Mangoldt/Euler source."""
    _int(t, "time", -1_000_000, 1_000_000)
    _int(threshold, "threshold", 1, 100_000)
    _int(amplitude, "amplitude", 1, 10**15)
    return t * t - amplitude * max(0, abs(t) - threshold)


def quadratic_kernel(t: int, u: int) -> int:
    """Direct closed form of psi(t)+psi(u)-psi(t-u) for quadratic psi."""
    _int(t, "time", -1_000_000, 1_000_000)
    _int(u, "time", -1_000_000, 1_000_000)
    return 2 * t * u


def delayed_kernel(t: int, u: int, threshold: int, amplitude: int) -> int:
    """Kernel reads only the permitted specified time evaluations."""
    _int(t, "time", -100_000, 100_000)
    _int(u, "time", -100_000, 100_000)
    return (delayed_psi(t, threshold, amplitude)
            + delayed_psi(u, threshold, amplitude)
            - delayed_psi(t-u, threshold, amplitude))


def late_witness(bound: int) -> dict[str, int | bool]:
    """Certificate that each bounded observation window admits a late defect.

    This certificate is accompanied by an elementary all-real-time proof:
        abs(t), abs(u)<=B implies abs(t-u)<=2B< threshold.
    Hence the entire real observation square agrees, not just integer points.
    """
    _int(bound, "bound", 0, 1000)
    threshold = 2 * bound + 1
    future_time = threshold + 1
    amplitude = future_time * future_time + 1
    return {
        "bound": bound,
        "threshold": threshold,
        "future_time": future_time,
        "amplitude": amplitude,
        "same_all_real_carrier_probes_by_support": True,
        "global_reference_kernel_PSD_by_rank_one": True,
        "late_negative_diagonal":
            delayed_kernel(future_time, future_time, threshold, amplitude),
        "Euler_source_mutation_admissible": False,
        "RH_sign_proved": False,
    }


def finite_all_zero_prefix(observed: Iterable[int]) -> dict[str, int | str | bool | None]:
    """A prefix may refute 'every bit is zero' but cannot verify it."""
    bits = tuple(observed)
    _int(len(bits), "number of observed bits", 0, 2048)
    for i, bit in enumerate(bits):
        if type(bit) is not int or bit not in (0, 1):
            raise CarrierImpedanceError("observations must be exact 0 or 1")
        if bit == 1:
            return {
                "observed_length": len(bits), "verdict": "refuted",
                "first_witness_index": i + 1, "positive_certificate": False,
            }
    return {
        "observed_length": len(bits), "verdict": "unresolved",
        "first_witness_index": None, "positive_certificate": False,
    }


def bernoulli_posterior_plus(observed: Iterable[int]) -> Fraction:
    """Exact P(p=2/3 | finite bits) with equal prior vs p=1/3.

    Likelihood ratio = 2^(2*ones-n). No finite record returns 0 or 1.
    """
    bits = tuple(observed)
    _int(len(bits), "number of observed bits", 0, 2048)
    for bit in bits:
        if type(bit) is not int or bit not in (0, 1):
            raise CarrierImpedanceError("binary channel requires exact 0 or 1")
    shift = 2 * sum(bits) - len(bits)
    ratio = (Fraction(2**shift, 1) if shift >= 0
             else Fraction(1, 2**(-shift)))
    return ratio / (1 + ratio)


def best_possible_posterior_error(n: int) -> Fraction:
    """Minimum residual uncertainty over n-bit histories (equal prior)."""
    _int(n, "n", 0, 2048)
    return Fraction(1, 1 + 2**n)


if __name__ == "__main__":
    import json

    example = late_witness(6)
    example["no_infinite_execution"] = True
    example["posterior_after_6_ones"] = str(bernoulli_posterior_plus([1] * 6))
    example["finite_observer_all_zero_verdict"] = finite_all_zero_prefix([0] * 6)["verdict"]
    print(json.dumps(example, indent=2, sort_keys=True))
