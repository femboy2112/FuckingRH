#!/usr/bin/env python3
"""Reversal/memory/polarization controls; no zeta zeros or RH assumption.

Exact integer/rational controls are separated from floating-point diagnostics.
Run: python scripts/reversal_memory_polarization_probe.py --output PATH
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.special import digamma


def determinant(a):
    n = len(a)
    out = 0
    for perm in itertools.permutations(range(n)):
        inv = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = math.prod(int(a[i][perm[i]]) for i in range(n))
        out += (-1 if inv % 2 else 1) * term
    return out


def principal_minors(a):
    n = len(a)
    return {','.join(map(str, s)): determinant([[a[i][j] for j in s] for i in s])
            for k in range(1, n + 1) for s in itertools.combinations(range(n), k)}


def memory_control():
    cases = []
    for phase in (1, -1):
        u = np.array([[0, 0, phase], [1, 0, 0], [0, 1, 0]], dtype=np.int64)
        assert np.array_equal(u.T @ u, np.eye(3, dtype=np.int64))
        a, b, c, d = u[:1, :1], u[:1, 1:], u[1:, :1], u[1:, 1:]
        kernels = [int((b @ np.linalg.matrix_power(d, m) @ c)[0, 0]) for m in range(7)]
        history = [1]
        for n in range(8):
            history.append(int(a[0, 0]) * history[n] +
                           sum(kernels[n - 1 - j] * history[j] for j in range(n)))
        direct = [int(np.linalg.matrix_power(u, n)[0, 0]) for n in range(9)]
        assert history == direct
        seed = np.array([1, 0, 0], dtype=np.int64)
        final = np.linalg.matrix_power(u, 2) @ seed
        assert np.array_equal(np.linalg.matrix_power(u.T, 2) @ final, seed)
        erased = np.array([final[0], 0, 0], dtype=np.int64)
        assert np.array_equal(np.linalg.matrix_power(u.T, 2) @ erased, np.zeros(3, dtype=np.int64))
        assert history[3] == phase and a[0, 0] == 0
        cases.append({'return_phase': phase, 'memory_B_Dm_C': kernels,
                      'full_observed_history': history, 'iterated_shadow_after_time0': [0] * 8,
                      'exact_inverse_recovers': True, 'environment_erasure_recovers': False})
    return {'status': 'VERIFIED_FINITE_EXACT', 'cases': cases}


def duality_control():
    b = np.array([[0, 1], [-1, 0]], dtype=np.int64)
    j = -b
    r = np.array([[0, 1], [1, 0]], dtype=np.int64)
    identity = np.eye(2, dtype=np.int64)
    bad4 = np.diag([3, 1])  # D = diag(3/4,1/4), within the critical strip.
    good4 = np.array([[2, -12], [12, 2]], dtype=np.int64)
    for d4 in (bad4, good4):
        assert np.array_equal(d4.T @ b + b @ d4, 4 * b)
        l4 = d4 - 2 * identity
        assert np.array_equal(r @ l4 @ r, -l4)
    assert np.array_equal(b @ j, identity)
    assert not np.array_equal(bad4 @ j, j @ bad4)
    assert np.array_equal(good4 @ j, j @ good4)
    assert np.array_equal(good4.T + good4, 4 * identity)
    # The positive metric equation on e1 would read (3/2)G11=G11.
    obstruction = 2 * Fraction(3, 4) - 1
    assert obstruction > 0
    return {'status': 'VERIFIED_FINITE_EXACT', 'B': b.tolist(), 'J': j.tolist(),
            'reversal_R': r.tolist(), 'bad_D_times4': bad4.tolist(),
            'good_D_times4': good4.tolist(), 'bad_eigenvalues': ['3/4', '1/4'],
            'good_eigenvalues': ['1/2+3i', '1/2-3i'],
            'duality_and_reversal_hold_in_both': True,
            'bad_positive_metric_obstruction_coefficient': str(obstruction)}


def primitive_filter_control():
    rp, rq = 1 / math.sqrt(2), 1 / math.sqrt(3)
    erased = np.array([[1, rp, rq, 0], [rp, 1, 0, rq],
                       [rq, 0, 1, rp], [0, rq, rp, 1]])
    retained = erased.copy()
    for i, k in ((0, 3), (1, 2), (2, 1), (3, 0)):
        retained[i, k] = rp * rq
    witness = np.array([1, -1, -1, 1])
    erased_q = float(witness @ erased @ witness)
    assert erased_q < 0 and np.linalg.eigvalsh(retained)[0] > 0
    assert Fraction(7, 10) ** 2 < Fraction(1, 2)
    assert Fraction(57, 100) ** 2 < Fraction(1, 3)
    bound = 4 * (1 - Fraction(7, 10) - Fraction(57, 100))
    assert bound == Fraction(-27, 25)
    # A separable Fourier kernel keeps mixed paths. Its log generating series
    # has connected xy coefficient zero. Changing the composite coefficient
    # from1 to2 produces connected xy coefficient1.
    connected = {'Euler_product_xy': str(Fraction(1) - Fraction(1) * Fraction(1)),
                 'fake_composite_xy': str(Fraction(2) - Fraction(1) * Fraction(1))}
    assert connected == {'Euler_product_xy': '0', 'fake_composite_xy': '1'}
    axes = []
    for primes in ([2], [2, 3], [2, 3, 5]):
        radii = [1 / math.sqrt(p) for p in primes]
        minimum = 1 - sum(2 * radius / (1 + radius) for radius in radii)
        axes.append({'primes': primes, 'axis_only_Poisson_density_minimum': minimum})
    assert axes[0]['axis_only_Poisson_density_minimum'] > 0
    assert axes[1]['axis_only_Poisson_density_minimum'] < 0
    return {'status': 'EXACT_SIGN_PROOFS_WITH_FLOAT_DIAGNOSTICS',
            'points': ['1', '2', '3', '6'], 'mixed_erasure_matrix': erased.tolist(),
            'retained_product_matrix': retained.tolist(), 'witness': witness.tolist(),
            'erasure_quadratic_value': erased_q,
            'rigorous_quadratic_upper_bound_strict': str(bound),
            'erasure_eigenvalues': np.linalg.eigvalsh(erased).tolist(),
            'retained_eigenvalues': np.linalg.eigvalsh(retained).tolist(),
            'connected_xy_coefficients': connected, 'axis_masks': axes}


def fp2_count(p):
    nonresidue = next(d for d in range(2, p) if pow(d, (p - 1) // 2, p) == p - 1)
    def mul(x, y):
        return ((x[0] * y[0] + nonresidue * x[1] * y[1]) % p,
                (x[0] * y[1] + x[1] * y[0]) % p)
    def power(x, n):
        out = (1, 0)
        while n:
            if n & 1:
                out = mul(out, x)
            x = mul(x, x)
            n //= 2
        return out
    field = list(itertools.product(range(p), repeat=2))
    squares = {}
    for y in field:
        y2 = mul(y, y)
        squares[y2] = squares.get(y2, 0) + 1
    count_dictionary, count_character = 1, 1  # point at infinity
    for x in field:
        x3 = mul(mul(x, x), x)
        rhs = ((x3[0] - 4) % p, x3[1])
        count_dictionary += squares.get(rhs, 0)
        roots = 1 if rhs == (0, 0) else (2 if power(rhs, (p * p - 1) // 2) == (1, 0) else 0)
        count_character += roots
    assert count_dictionary == count_character
    return count_dictionary, nonresidue


def frobenius_gram(q, a0, a1, a2):
    powers = [a0, a1, a2]
    return [[q ** min(i, j) * powers[abs(i - j)] for j in range(3)] for i in range(3)]


def common_history_control():
    curves = []
    for p in (5, 7, 11, 13, 17, 19, 23, 29, 31):
        brute = 1 + sum((y * y - x * x * x + 4) % p == 0
                        for x in range(p) for y in range(p))
        character = 1
        for x in range(p):
            rhs = (x ** 3 - 4) % p
            character += 1 if rhs == 0 else (2 if pow(rhs, (p - 1) // 2, p) == 1 else 0)
        assert brute == character
        n2, nonresidue = fp2_count(p)
        a1, a2 = p + 1 - brute, p * p + 1 - n2
        assert a2 == a1 * a1 - 2 * p
        gram = frobenius_gram(p, 2, a1, a2)
        minors = principal_minors(gram)
        assert all(m >= 0 for m in minors.values()) and determinant(gram) == 0
        curves.append({'p': p, 'Fp2_nonresidue': nonresidue, 'N1': brute, 'N2': n2,
                       'a1': a1, 'a2': a2, 'gram': gram, 'principal_minors': minors})
    # Stronger forged control: even a reciprocal genus-two-shaped polynomial,
    # integral nonnegative closed-point counts through degree2, and all pairwise
    # Gram checks do not guarantee a positive common history.
    q, g, a1, a2 = 5, 2, -6, -18
    charpoly = [1, 6, 27, 30, 25]  # descending coefficients
    assert [charpoly[i] * q ** (4 - i) for i in range(5)][::-1] == [q * q * x for x in charpoly]
    assert a1 == -charpoly[1] and a2 == a1 * a1 - 2 * charpoly[2]
    n1, n2 = q + 1 - a1, q * q + 1 - a2
    assert a1 * a1 <= (2 * g) ** 2 * q
    assert a2 * a2 <= (2 * g) ** 2 * q * q
    assert n1 >= 0 and n2 >= n1 and (n2 - n1) % 2 == 0
    gram = frobenius_gram(q, 2 * g, a1, a2)
    minors = principal_minors(gram)
    assert all(value > 0 for key, value in minors.items() if len(key.split(',')) <= 2)
    v = [4, 1, 1]
    value = sum(v[i] * gram[i][j] * v[j] for i in range(3) for j in range(3))
    assert value == -68 and determinant(gram) == -12160
    return {'status': 'VERIFIED_FINITE_EXACT', 'curve': 'y^2=x^3-4', 'actual_curves': curves,
            'forged_reciprocal_control': {'q': q, 'g': g, 'characteristic_polynomial': charpoly,
                'N1': n1, 'N2': n2, 'degree2_closed_point_count': (n2 - n1) // 2,
                'passes_individual_Hasse_bounds': True, 'passes_all_pairwise_Gram_checks': True,
                'gram': gram, 'principal_minors': minors, 'witness': v, 'quadratic_value': value,
                'is_actual_curve': False}}


def prime_power_weights(cutoff):
    weights = {}
    for p in range(2, cutoff + 1):
        if any(p % d == 0 for d in range(2, math.isqrt(p) + 1)):
            continue
        n = p
        while n <= cutoff:
            weights[n] = math.log(p) / math.sqrt(n)
            n *= p
    return weights


def clock_control():
    frequencies = np.array([0., 1., 4., 16., 256., 65536.])
    gamma = np.real(digamma(0.25 + 0.5j * frequencies)) - digamma(0.25)
    weights = prime_power_weights(16)
    energy = gamma.copy()
    for n, weight in weights.items():
        energy += 2 * weight * (1 - np.cos(frequencies * math.log(n)))
    assert np.all(energy >= 0)
    results = []
    for omega in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6):
        t = np.exp(-omega * energy)
        r = np.sqrt(-np.expm1(-2 * omega * energy))
        assert np.max(np.abs(t * t + r * r - 1)) < 5e-15
        tangent = r * r / (2 * omega)
        tau = math.sqrt(2 * omega)
        group_tangent = np.sin(tau * np.sqrt(energy)) ** 2 / (2 * omega)
        wrong_clock = np.sin(omega * np.sqrt(energy)) ** 2 / (2 * omega)
        results.append({'omega': omega, 'heat_dilation_tangent': tangent.tolist(),
                        'rotation_group_tangent': group_tangent.tolist(),
                        'unrescaled_smooth_clock_tangent': wrong_clock.tolist(),
                        'heat_error_max': float(np.max(np.abs(tangent - energy))),
                        'rotation_error_max': float(np.max(np.abs(group_tangent - energy)))})
    assert results[-1]['heat_error_max'] < results[0]['heat_error_max'] / 1000
    assert max(results[-1]['unrescaled_smooth_clock_tangent']) < 1e-3
    return {'status': 'FLOATING_POINT_DIAGNOSTIC', 'frequencies': frequencies.tolist(),
            'Gamma_symbol': gamma.tolist(), 'positive_Gamma_prime_energy': energy.tolist(),
            'prime_cutoff': 16, 'includes_Weil_scalar_and_polar_deficit': False, 'samples': results}


def connes_consani_crosswalk():
    # Smooth compact bumps; outer/inner quadrature is a diagnostic, not an enclosure.
    radius = 1.25
    nodes, w = np.polynomial.legendre.leggauss(256)
    def bump(t, primitive):
        t = np.asarray(t)
        out = np.zeros_like(t, dtype=float)
        mask = np.abs(t) < radius
        x = t[mask]
        z = 1 - (x / radius) ** 2
        base = np.exp(-1 / z)
        if primitive:
            hp = -2 * x / radius ** 2 / z ** 2
            hpp = -2 / radius ** 2 / z ** 2 - 8 * x ** 2 / radius ** 4 / z ** 3
            out[mask] = base * (hp * hp + hpp - 0.25)
        else:
            out[mask] = (1 + 0.4 * x) * base
        return out
    samples = []
    weights = prime_power_weights(math.floor(math.exp(2 * radius)))
    for primitive in (False, True):
        norm = math.sqrt(float(radius * np.dot(w, bump(radius * nodes, primitive) ** 2)))
        def v(t):
            return bump(t, primitive) / norm
        def corr(h):
            left, right = max(-radius, -radius + h), min(radius, radius + h)
            if left >= right:
                return 0.0
            t = (left + right) / 2 + (right - left) / 2 * nodes
            return float((right - left) / 2 * np.dot(w, v(t) * v(t - h)))
        n = corr(0.0)
        c = float(radius * np.dot(w, v(radius * nodes) * np.cosh(radius * nodes / 2)))
        s = float(radius * np.dot(w, v(radius * nodes) * np.sinh(radius * nodes / 2)))
        polar = 2 * (c * c - s * s)
        def cc_integrand(h):
            return (math.exp(-h / 2) * corr(h) - math.exp(-2 * h) * n) / (-math.expm1(-2 * h))
        def weil_integrand(h):
            return (math.exp(-h / 2) * corr(h) - math.exp(-h) * n) / (-math.expm1(-2 * h))
        cc_int, cc_err = quad(cc_integrand, 0, 2 * radius, epsabs=2e-10, epsrel=2e-10, limit=160)
        cc_int += n / 2 * math.log1p(-math.exp(-4 * radius))
        w_int, w_err = quad(weil_integrand, 0, 2 * radius, epsabs=2e-10, epsrel=2e-10, limit=160)
        w_int -= n * math.atanh(math.exp(-2 * radius))
        prime = sum(a * corr(math.log(k)) for k, a in weights.items())
        cc_origin = 0.5 * (math.log(math.pi) + float(np.euler_gamma))
        cc_self = prime + cc_int + cc_origin * n
        q_weil = polar - 2 * prime - (math.log(4 * math.pi) + float(np.euler_gamma)) * n - 2 * w_int
        mapped = polar - 2 * cc_self
        residual = abs(q_weil - mapped)
        assert residual < 1e-8
        if primitive:
            assert abs(c) + abs(s) < 1e-10
        else:
            assert abs(polar) > 0.1
        missing_origin_residual = abs(q_weil - (polar - 2 * (cc_self - cc_origin * n)))
        assert missing_origin_residual > 1
        samples.append({'primitive': primitive, 'C': c, 'S': s, 'norm2': n, 'polar': polar,
                        's_CC': cc_self, 'Q_Weil': q_weil, 'polar_minus_2s_CC': mapped,
                        'crosswalk_residual': residual, 'missing_CC_origin_residual': missing_origin_residual,
                        'reported_outer_quad_error': max(cc_err, w_err)})
    return {'status': 'FLOATING_POINT_DIAGNOSTIC', 'radius': radius, 'Gauss_nodes': 256,
            'no_zero_input': True, 'samples': samples}


def retarded_advanced_control():
    radius = 1.25
    def source(t, kind):
        if abs(t) >= radius:
            return 0.0
        z = 1 - (t / radius) ** 2
        g = math.exp(-1 / z)
        hp = -2 * t / radius ** 2 / z ** 2
        hpp = -2 / radius ** 2 / z ** 2 - 8 * t * t / radius ** 4 / z ** 3
        if kind == 'primitive':
            return g * (hp * hp + hpp - 0.25)
        if kind == 'ordinary_zero_mean_only':
            return g * hp
        return g
    def integral(f, left, right):
        if left >= right:
            return 0.0
        return quad(f, left, right, epsabs=1e-11, epsrel=1e-11, limit=160)[0]
    cases = []
    for kind in ('primitive', 'ordinary_zero_mean_only', 'nonprimitive'):
        minus = integral(lambda u: math.exp(-u / 2) * source(u, kind), -radius, radius)
        plus = integral(lambda u: math.exp(u / 2) * source(u, kind), -radius, radius)
        mass = integral(lambda u: source(u, kind), -radius, radius)
        samples = []
        for t in (-2., -1., -0.25, 0., 0.25, 1., 2.):
            retarded = integral(lambda u: 2 * math.sinh((t - u) / 2) * source(u, kind),
                                -radius, min(t, radius))
            advanced = integral(lambda u: -2 * math.sinh((t - u) / 2) * source(u, kind),
                                max(t, -radius), radius)
            decaying = integral(lambda u: -math.exp(-abs(t - u) / 2) * source(u, kind),
                                -radius, min(t, radius))
            decaying += integral(lambda u: -math.exp(-abs(t - u) / 2) * source(u, kind),
                                 max(t, -radius), radius)
            predicted = math.exp(t / 2) * minus - math.exp(-t / 2) * plus
            assert abs(retarded - advanced - predicted) < 1e-9
            if kind == 'primitive':
                expected = 0. if abs(t) >= radius else math.exp(-1 / (1 - (t / radius) ** 2))
                assert max(abs(retarded - expected), abs(advanced - expected), abs(decaying - expected)) < 1e-9
            samples.append({'t': t, 'retarded': retarded, 'advanced': advanced,
                            'decaying': decaying, 'predicted_retarded_minus_advanced': predicted})
        if kind == 'primitive':
            assert abs(minus) + abs(plus) < 1e-9
        elif kind == 'ordinary_zero_mean_only':
            assert abs(mass) < 1e-10 and abs(minus) > 0.01 and abs(plus) > 0.01
            assert abs(samples[-1]['retarded']) > 0.01
        cases.append({'kind': kind, 'ordinary_mass': mass, 'exponential_moment_minus': minus,
                      'exponential_moment_plus': plus, 'samples': samples})
    return {'status': 'FLOATING_POINT_DIAGNOSTIC_OF_EXACT_DOMAIN_THEOREM',
            'operator': 'd^2/dt^2-1/4', 'radius': radius, 'cases': cases}


def prepared_history_dilation_control():
    # A concrete gradient, rather than a factorization fitted to the Weil form.
    gradient = np.array([[1., -1., 0.], [0., 1., -1.], [1., 0., 0.]])
    energy = gradient.T @ gradient
    eigenvalues, basis = np.linalg.eigh(energy)
    assert eigenvalues[0] > 0
    def exp_energy(s):
        return (basis * np.exp(s * eigenvalues)) @ basis.T
    seed = np.array([1., 2., -1.]) / math.sqrt(6)
    samples = []
    for t in (0.1, 0.7, 1.3):
        target = exp_energy(-t)
        compressed = np.zeros((3, 3))
        for i in range(3):
            for j in range(3):
                compressed[i, j] = quad(
                    lambda s: float((2 * exp_energy(s) @ energy @ exp_energy(s - t))[i, j]),
                    -np.inf, 0., epsabs=2e-11, epsrel=2e-11)[0]
        loss = float(seed @ seed - np.linalg.norm(target @ seed) ** 2)
        outgoing = quad(lambda s: float(2 * np.linalg.norm(gradient @ exp_energy(s - t) @ seed) ** 2),
                        0., t, epsabs=2e-11, epsrel=2e-11)[0]
        error = float(np.max(np.abs(compressed - target)))
        assert error < 1e-9 and abs(loss - outgoing) < 1e-9 and outgoing > 0
        samples.append({'t': t, 'compression_matrix_error': error,
                        'observable_norm_loss': loss, 'outgoing_history_norm2': outgoing})
    return {'status': 'FLOATING_POINT_DIAGNOSTIC_OF_EXACT_DILATION',
            'gradient': gradient.tolist(), 'energy': energy.tolist(),
            'seed': seed.tolist(), 'prepared_history_jump_norm2': float(2 * np.linalg.norm(gradient @ seed) ** 2),
            'includes_Weil_deficit': False, 'samples': samples}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    results = {
        'schema': 'reversal-memory-polarization-v1',
        'claim_boundary': 'Exact controls and new theorem checks; no RH proof or global positivity certification.',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'environment': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
        'memory': memory_control(),
        'duality': duality_control(),
        'primitive_filter': primitive_filter_control(),
        'common_history': common_history_control(),
        'singular_clock': clock_control(),
        'CC_crosswalk': connes_consani_crosswalk(),
        'retarded_advanced': retarded_advanced_control(),
        'prepared_history_dilation': prepared_history_dilation_control(),
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(results, indent=2, allow_nan=False) + '\n')
    print('PASS: exact memory recurrence, coherent return, erasure/phase controls')
    print('PASS: duality+reversal countermodel and positive-polarization control')
    print('PASS: prime2/3 mixed-erasure negative witness and product-kernel positive control')
    print('PASS: nine independently counted finite-field histories and reciprocal forged negative control')
    print('PASS: singular-clock energy diagnostic; full Weil deficit explicitly excluded')
    print('PASS: full Connes-Consani/Weil sign-factor-origin crosswalk diagnostic')
    print('PASS: compact retarded/advanced reconstruction and ordinary-zero-mean mutation')
    print('PASS: unitary history-shift dilation, compression and outgoing-environment energy')
    print('RH REMAINS OPEN; numerical diagnostics are not certified enclosures.')


if __name__ == '__main__':
    main()
