import collections
import itertools
import unittest

import sympy as sp

from scripts.round007_geometry import (
    affine_branches, carrier_jump, doubled_dirac, graph_projection,
    jet_charge, omega, predicted_affine_square, return_time, shift,
    stratum_current, support_size, valuation,
)


class Round007GeometryTests(unittest.TestCase):
    def test_valuation_against_independent_factorizer(self):
        for n in range(1, 500):
            self.assertEqual(valuation(n), sp.factorint(n))

    def test_jump_distance_by_breadth_first_search(self):
        # Independent nearest-neighbor paths in the smallest coordinate box.
        for n in range(1, 30):
            a, b = valuation(n), valuation(n + 1)
            primes = sorted(a.keys() | b.keys())
            start = tuple(a.get(p, 0) for p in primes)
            end = tuple(b.get(p, 0) for p in primes)
            limits = tuple(max(x, y) for x, y in zip(start, end))
            queue, seen = collections.deque([(start, 0)]), {start}
            while queue:
                point, distance = queue.popleft()
                if point == end:
                    break
                for j in range(len(primes)):
                    for delta in (-1, 1):
                        nxt = list(point)
                        nxt[j] += delta
                        nxt = tuple(nxt)
                        if 0 <= nxt[j] <= limits[j] and nxt not in seen:
                            seen.add(nxt)
                            queue.append((nxt, distance + 1))
            self.assertEqual(distance, omega(n) + omega(n + 1))
            self.assertTrue(set(a).isdisjoint(b))

    def test_stratum_current_by_matrix_commutator(self):
        size = 40
        s = shift(size)
        for r in range(4):
            projection = sp.diag(*(int(support_size(n) == r)
                                   for n in range(1, size + 1)))
            current = s * projection - projection * s
            expected = sp.zeros(size)
            for n in range(1, size):
                expected[n, n - 1] = stratum_current(n, r)
            self.assertEqual(current, expected)
            self.assertEqual(current.T * current,
                             sp.diag(*(stratum_current(n, r) ** 2
                                       for n in range(1, size)), 0))
        # Sign orientation: 1->2 enters; 5->6 leaves.
        self.assertEqual(stratum_current(1, 1), -1)
        self.assertEqual(stratum_current(5, 1), 1)

    def test_jet_charge_against_independent_prime_power_enumeration(self):
        expected = {}
        for p in sp.primerange(2, 300):
            n = int(p)
            while n < 300:
                expected[n] = sp.log(p)
                n *= int(p)
        for n in range(1, 300):
            self.assertEqual(jet_charge(n), expected.get(n, 0))

    def test_first_return_minimality_and_cocycle(self):
        for p in (2, 3, 5, 7):
            for k in range(4):
                n = p ** k
                hits = {p ** ell for ell in range(k + 3)}
                first = next(value for value in range(n + 1, p ** (k + 1) + 1)
                             if value in hits)
                self.assertEqual(first - n, return_time(p, k))
                for a, b in itertools.product(range(4), repeat=2):
                    self.assertEqual(return_time(p, k, a + b),
                                     return_time(p, k, a) + return_time(p, k + a, b))

    def test_affine_identity_all_boundary_regimes(self):
        for m in range(1, 8):
            for r in range(11):
                ap, am = affine_branches(m, r, 7)
                c = ap - am
                self.assertEqual(c.T * c, predicted_affine_square(m, r, 7))
                cross = shift(7, 2 * r // m) if 2 * r % m == 0 else sp.zeros(7)
                self.assertEqual(am.T * ap, cross)
                # Check against independently composed ambient S and V_m.
                ambient = m * 7 + r + 1
                s = shift(ambient)
                vm = sp.zeros(ambient, 7)
                for j in range(7):
                    vm[m * (j + 1) - 1, j] = 1
                direct = s ** r * vm - (s.T) ** r * vm
                self.assertEqual(direct.T * direct, c.T * c)

    def test_unpaid_boundary_is_detectable(self):
        ap, am = affine_branches(3, 3, 5)
        naive = 2 * sp.eye(5) - shift(5, 2) - shift(5, 2).T
        self.assertEqual(naive - (ap - am).T * (ap - am), sp.diag(1, 0, 0, 0, 0))

    def test_doubled_dirac_grading_and_square(self):
        ap, am = affine_branches(2, 1, 6)
        c = ap - am
        d, gamma = doubled_dirac(c)
        self.assertEqual(d, d.T)
        self.assertEqual(gamma * d + d * gamma, sp.zeros(d.rows))
        self.assertEqual(d * d, sp.diag(c.T * c, c * c.T))

    def test_binary_lower_square_on_independent_output_window(self):
        ap, am = affine_branches(2, 1, 9)
        c = ap - am
        size = 12  # Below the last input's two affine outputs.
        odd = sp.diag(*(int(n % 2 == 1) for n in range(1, size + 1)))
        s2 = shift(size, 2)
        expected = 2 * odd - sp.diag(1, *([0] * (size - 1))) - s2 * odd - odd * s2.T
        self.assertEqual((c * c.T)[:size, :size], expected)

    def test_height_commutators_on_full_output_core(self):
        size = 8
        sin = shift(size)
        height = sp.diag(*(sp.log(n) for n in range(1, size + 1)))
        comm = height * sin - sin * height
        expected = sp.zeros(size)
        for n in range(1, size):
            expected[n, n - 1] = sp.log(sp.Rational(n + 1, n))
        self.assertTrue(all(sp.expand_log(x, force=True) == 0 for x in comm - expected))
        for p in (2, 3, 5):
            vm = sp.zeros(p * size, size)
            for j in range(size):
                vm[p * (j + 1) - 1, j] = 1
            hout = sp.diag(*(sp.log(n) for n in range(1, p * size + 1)))
            residual = hout * vm - vm * height - sp.log(p) * vm
            self.assertTrue(all(sp.simplify(sp.logcombine(x, force=True)) == 0
                                for x in residual))

    def test_factor_swap_forgets_orientation_with_explicit_normalization(self):
        n = 12
        pairs = [(a, n // a) for a in sp.divisors(n)]
        swap = sp.zeros(len(pairs))
        for j, (a, b) in enumerate(pairs):
            swap[pairs.index((b, a)), j] = 1
        product = sp.ones(1, len(pairs))
        self.assertEqual(swap * swap, sp.eye(len(pairs)))
        self.assertEqual(product * (sp.eye(len(pairs)) - swap), sp.zeros(1, len(pairs)))
        self.assertEqual(product * product.T, sp.Matrix([[len(pairs)]]))
        normalized = product / sp.sqrt(len(pairs))
        self.assertEqual(normalized * normalized.T, sp.ones(1, 1))

    def test_graph_projection_reduces_synchronized_carrier(self):
        size = 5
        p = graph_projection(size)
        joint = sp.kronecker_product(shift(size), shift(size))
        self.assertEqual(p * p, p)
        self.assertEqual(p * joint, joint * p)
        # Compression of a tensor product is entrywise (Hadamard) product.
        embedding = sp.zeros(size * size, size)
        for j in range(size):
            embedding[j * size + j, j] = 1
        a = shift(size) + 2 * sp.eye(size)
        b = shift(size).T + 3 * sp.eye(size)
        self.assertEqual(embedding.T * sp.kronecker_product(a, b) * embedding,
                         a.multiply_elementwise(b))
        # It is not a homomorphism: separate shifts compress to zero;
        # their synchronized product compresses to S.
        x = sp.kronecker_product(shift(size), sp.eye(size))
        y = sp.kronecker_product(sp.eye(size), shift(size))
        self.assertEqual(embedding.T * x * embedding, sp.zeros(size))
        self.assertEqual(embedding.T * y * embedding, sp.zeros(size))
        self.assertEqual(embedding.T * x * y * embedding, shift(size))

    def test_height_gap_and_telescoping_singular_values(self):
        for size in range(2, 12):
            # Exact rational comparison before applying increasing log.
            ratios = [sp.Rational(n, m) for n in range(1, size + 1)
                      for m in range(1, n)]
            self.assertEqual(min(ratios), sp.Rational(size, size - 1))
            product = sp.prod(sp.Rational(n + 1, n) for n in range(1, size + 1))
            self.assertEqual(product, size + 1)


if __name__ == "__main__":
    unittest.main()
