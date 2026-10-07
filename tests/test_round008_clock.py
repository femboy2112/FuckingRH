"""Exact finite checks for the Haar/carry/CRT clock theorem."""

import unittest

import sympy as sp

from scripts.round008_clock import (
    Z,
    clock,
    conductor_projector,
    crt_labels,
    difference_basis,
    innovation_conductors,
    innovation_restriction,
    mutation_controls,
    ramanujan,
    root_sum,
    verify_clock,
)


class ClockTests(unittest.TestCase):
    def test_exact_joint_identities_on_primary_fixtures(self):
        for p, L in [(2, 1), (2, 3), (2, 6), (3, 4)]:
            with self.subTest(p=p, L=L):
                verify_clock(p, L)

    def test_holdouts_include_ramification_and_unit_clock(self):
        for p, L in [(3, 1), (3, 6), (5, 2), (2, 4)]:
            with self.subTest(p=p, L=L):
                verify_clock(p, L)

    def test_ramanujan_matches_primitive_root_sum(self):
        for q in range(1, 13):
            for d in range(q):
                exact = root_sum(q, tuple(a * d for a in range(q) if sp.gcd(a, q) == 1))
                self.assertEqual(exact, ramanujan(q, d))

    def test_full_conductor_resolution_of_identity(self):
        for n in [1, 6, 12, 18]:
            projectors = [conductor_projector(n, q) for q in sp.divisors(n)]
            self.assertEqual(sum(projectors, sp.zeros(n)), sp.eye(n))
            for i, P in enumerate(projectors):
                self.assertEqual(P * P, P)
                for Q in projectors[:i]:
                    self.assertEqual(P * Q, sp.zeros(n))

    def test_mixed_conductor_fixture_is_not_only_new_prime(self):
        self.assertEqual(innovation_conductors(2, 6), (4, 12))
        self.assertEqual(innovation_conductors(3, 4), (3, 6, 12))
        self.assertEqual({row[2] for row in crt_labels(2, 6)}, {1, 3, 5, 7, 9, 11})

    def test_restriction_is_not_assumed_euclidean_unitary(self):
        D = difference_basis(3, 2)
        R = innovation_restriction(3, 2)
        self.assertEqual(clock(6) * D, D * R)
        self.assertNotEqual(R.T * R, sp.eye(4))
        self.assertEqual(R.T * (D.T * D) * R, D.T * D)
        self.assertEqual(R.charpoly(Z).as_expr(), Z**4 + Z**2 + 1)

    def test_hostile_mutations(self):
        data = mutation_controls()
        self.assertEqual(data["pure_prime_only_missing_dimension"], 6)
        self.assertTrue(data["phase_mutation_preserves_charpoly"])
        self.assertFalse(data["phase_mutation_preserves_old_subspace"])

    def test_invalid_parameters_fail_explicitly(self):
        with self.assertRaises(ValueError):
            verify_clock(4, 3)
        with self.assertRaises(ValueError):
            verify_clock(2, 0)
        with self.assertRaises(ValueError):
            conductor_projector(6, 4)


if __name__ == "__main__":
    unittest.main()
