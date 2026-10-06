"""Exact/Arb controls for the Round006 scope audit; no RH construction.

Run ``python -m scripts.round007_parent_audit``.  Arb balls certify the
displayed scalar signs.  Rational matrices check the distinct notions of
Cayley pole count and negative-square index.
"""

from __future__ import annotations

import json

from flint import acb, acb_series, arb, ctx
import sympy as sp


def xi(s: acb) -> acb:
    """Completed xi away from its removable presentation points 0 and 1."""
    s = acb(s)
    return s * (s - 1) / 2 * acb.pi() ** (-s / 2) * (s / 2).gamma() * s.zeta()


def archimedean_port(s: acb) -> acb:
    s = acb(s)
    return 1 / s + 1 / (s - 1) - arb.pi().log() / 2 + (s / 2).digamma() / 2


def xi_log_derivative(s: acb) -> acb:
    """Arb Taylor coefficient, not a finite difference or zero expansion."""
    s = acb(s)
    old_cap = ctx.cap
    try:
        ctx.cap = 2
        z = acb_series([s, 1]).zeta()
        return archimedean_port(s) + z[1] / z[0]
    finally:
        ctx.cap = old_cap


def von_mangoldt_terms(horizon: int):
    if horizon < 2:
        return []
    terms = []
    for p in sp.primerange(2, horizon + 1):
        p = int(p)
        n = p
        while n <= horizon:
            terms.append((n, p))
            n *= p
    return sorted(terms)


def finite_completion(s: acb, horizon: int) -> acb:
    """The particular Euler--Maclaurin boundary used in Round006."""
    if horizon < 2:
        raise ValueError("horizon must be at least 2")
    s = acb(s)
    log_n = arb(horizon).log()
    regularized_pole = log_n if s == 1 else (1 - ((1 - s) * log_n).exp()) / (s - 1)
    prime_sum = sum(
        (arb(p).log() * (-s * arb(n).log()).exp() for n, p in von_mangoldt_terms(horizon)),
        acb(0),
    )
    return 1 / s - arb.pi().log() / 2 + (s / 2).digamma() / 2 + regularized_pole - prime_sum


def pole_positive_real_kernel(points):
    """K_F for F(s)=1/(s-1), domain Re(s)>1/2, exact real points."""
    points = list(map(sp.Rational, points))
    if any(s <= 1 for s in points) or len(set(points)) != len(points):
        raise ValueError("use distinct real points greater than 1")
    return sp.Matrix([
        [(1 / (s - 1) + 1 / (u - 1)) / (s + u - 1) for u in points]
        for s in points
    ])


def pole_kernel_decomposition(points):
    points = list(map(sp.Rational, points))
    d = sp.diag(*(1 / (s - 1) for s in points))
    c = sp.Matrix([[1 / (s + u - 1) for u in points] for s in points])
    return d * (sp.ones(len(points)) - c) * d


def exact_ldl_inertia(matrix):
    """For these nonsingular real symmetric controls, no pivot is zero."""
    _, diagonal = matrix.LDLdecomposition(hermitian=False)
    vals = [diagonal[i, i] for i in range(matrix.rows)]
    return tuple(sum(bool(v > 0) if sign > 0 else bool(v < 0) for v in vals) for sign in (1, -1))


def audit_certificates(dps=70):
    with ctx.workdps(dps):
        s = acb(1, 282)
        ratio = (xi(s) / xi(s + 1)).real
        log_derivative = xi_log_derivative(s).real
        gamma_at_two = acb(1).digamma().real / 2
        sample = finite_completion(acb(arb(51) / 100), 200).real
        boundary = finite_completion(acb(arb(1) / 2), 200).real
        assert ratio < 0 and log_derivative > 0 and gamma_at_two < 0 and sample < 0 and boundary < 0
        return {
            "precision_decimal_digits": dps,
            "method": "python-flint Arb interval arithmetic; no zero ordinates",
            "xi_ratio_at_1_plus_282i_real": str(ratio),
            "xi_log_derivative_at_1_plus_282i_real": str(log_derivative),
            "half_digamma_at_s_2": str(gamma_at_two),
            "specific_finite_completion_P_200_s_51_over_100": str(sample),
            "specific_finite_completion_P_200_boundary_s_1_over_2": str(boundary),
            "pole_kernel_inertias_positive_negative": {
                str(n): exact_ldl_inertia(pole_positive_real_kernel(range(2, n + 2)))
                for n in range(1, 7)
            },
            "scope": "Scalar counterexamples and exact finite inertia controls; universal statements are proved in PARENT_AUDIT.md.",
        }


if __name__ == "__main__":
    print(json.dumps(audit_certificates(), indent=2))
