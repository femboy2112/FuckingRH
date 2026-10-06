from fractions import Fraction
from math import isqrt
import unittest

import sympy as sp

from scripts.round007_factor_cone import (
    active, cone, current, current_decomposition, divisors, factor_count,
    factor_pairs, factor_lift, swap_matrix, compressed_coordinate_energy,
    factor_graph_offdiagonal, same_factor_lift, same_factor_hop, hyperbola_sum,
)


class FactorConeTests(unittest.TestCase):
    def test_fiber_normalization_and_swap(self):
        pairs, U = factor_lift(20)
        _, J = factor_lift(20, normalized=True)
        R = swap_matrix(pairs)
        self.assertEqual(U.T * U, sp.diag(*(len(divisors(n)) for n in range(1, 21))))
        self.assertEqual(J.T * J, sp.eye(20))
        self.assertEqual(R * R, sp.eye(len(pairs)))
        self.assertEqual(R * U, U)
        self.assertEqual(U.T * (sp.eye(len(pairs)) - R), sp.zeros(20, len(pairs)))

    def test_factor_chiral_square_before_projection(self):
        pairs, U = factor_lift(20)
        R = swap_matrix(pairs)
        T = sp.diag(*(int(a <= b) for a, b in pairs))
        C = (sp.eye(len(pairs)) - R) * T * U
        expected = sp.diag(*(len(divisors(n)) - int(isqrt(n) ** 2 == n)
                             for n in range(1, 21)))
        self.assertEqual(C.T * C, expected)
        self.assertEqual(U.T * C, sp.zeros(20))
        self.assertNotEqual(C.T * C, sp.zeros(20))

    def test_square_and_bulk_current_exact(self):
        for n in range(1, 300):
            for a in range(1, 25):
                self.assertEqual(cone(n + 1, a) - cone(n, a), int(n + 1 == a * a))
                b, v = current_decomposition(n, a)
                self.assertEqual(current(n, a), b + v)
                if a > 1:
                    self.assertEqual(current(n, a) ** 2, active(n + 1, a) + active(n, a))
        self.assertEqual(current_decomposition(5, 2), (0, 1))
        self.assertEqual(current_decomposition(6, 2), (0, -1))

    def test_arbitrary_cone_mutation(self):
        for c in [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)]:
            for n in range(1, 40):
                for a in range(1, 10):
                    v = cone(n + 1, a, c) - cone(n, a, c)
                    self.assertEqual(v, int(n ** c.numerator < a ** c.denominator <= (n + 1) ** c.numerator))
        self.assertEqual(cone(8, 2, Fraction(1, 3)), 1)
        self.assertEqual(cone(4, 2, Fraction(1, 3)), 0)
        self.assertNotEqual(cone(3, 2, Fraction(2, 3)), cone(3, 2, Fraction(1, 2)))

    def test_same_factor_successor_obstruction(self):
        _, L, S = same_factor_lift(24)
        self.assertEqual(L.T * S * L, sp.zeros(24))
        self.assertEqual(L.T * (2 * sp.eye(S.rows) - S - S.T) * L,
                         sp.diag(*(2 * factor_count(n) for n in range(1, 25))))
        for h in [2, 3, 5]:
            K = L.T * S ** h * L
            for n in range(1, 25 - h):
                self.assertEqual(K[n + h - 1, n - 1], len(same_factor_hop(n, h)))
        _, L1, S1 = same_factor_lift(12, unit=True)
        self.assertEqual((L1.T * S1 * L1)[1, 0], 1)

    def test_coordinate_graph_compression(self):
        for units in [False, True]:
            K = compressed_coordinate_energy(24, remove_units=units)
            for n in range(1, 25):
                for m in range(n + 1, 25):
                    self.assertEqual(K[n - 1, m - 1], factor_graph_offdiagonal(n, m, units))
            if units:
                for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
                    self.assertEqual(K[:, p - 1], sp.zeros(24, 1))

    def test_factor_count_and_prime_towers(self):
        for n in range(1, 200):
            self.assertEqual(factor_count(n), (len(divisors(n)) + int(isqrt(n) ** 2 == n)) // 2 - 1)
        for p in [2, 3, 5]:
            for k in range(1, 6):
                self.assertEqual(factor_count(p ** k), k // 2)
        self.assertEqual(factor_count(18), factor_count(32))

    def test_hyperbola_and_finite_dimension(self):
        for N in range(1, 70):
            r = isqrt(N)
            self.assertEqual(len(factor_pairs(N)), 2 * sum(N // a for a in range(1, r + 1)) - r * r)
            for f, g in [(lambda a: 1, lambda b: 1),
                         (lambda a: (-1) ** a * a, lambda b: b * b + 1)]:
                direct = sum(f(a) * g(b) for a, b in factor_pairs(N))
                self.assertEqual(hyperbola_sum(N, f, g), direct)

    def test_half_density_not_forced_by_cone_and_swap(self):
        pairs, J = factor_lift(16, normalized=True)
        R = swap_matrix(pairs)
        for beta in [sp.Rational(0), sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(1)]:
            W = sp.diag(*(sp.Integer(n) ** (-beta) for n in range(1, 17)))
            L = J * W
            self.assertEqual(R * L, L)
            self.assertEqual(L.T * L, W * W)
            self.assertEqual({(i, j) for i in range(L.rows) for j in range(L.cols) if L[i, j] != 0},
                             {(i, j) for i in range(J.rows) for j in range(J.cols) if J[i, j] != 0})
        q, gamma = sp.symbols("q gamma", real=True)
        self.assertEqual(sp.solve(q - 2 * gamma, gamma), [q / 2])


if __name__ == "__main__":
    unittest.main()
