import unittest

import sympy as sp

from scripts.round007_return_transfer import (
    collapsed_euler_operator, jet_states, path_determinant,
    return_data, return_transfer,
)


class ReturnTransferTests(unittest.TestCase):
    def test_exact_first_return_and_cocycle(self):
        for base in [2, 3, 5, 6, 11]:
            for k in range(4):
                first = return_data(base, k)
                self.assertEqual(first["succ_steps"], (base-1)*base**k)
                self.assertTrue(all(n != base**j for n in range(first["start"]+1, first["end"])
                                    for j in range(k+1)))
                for r in range(4):
                    combined = return_data(base, k, r+1)
                    self.assertEqual(combined["succ_steps"], first["succ_steps"]
                                     + return_data(base, k+1, r)["succ_steps"])
                    self.assertEqual(combined["log_roof"], (r+1)*sp.log(base))

    def test_carrier_horizon_has_no_completed_tower_or_duplicated_origin(self):
        states = jet_states(20)
        values = [n for _, _, n in states]
        self.assertEqual(values, [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19])
        self.assertEqual(len(values), len(set(values)))
        self.assertNotIn(1, values)
        self.assertNotIn(25, values)

    def test_return_is_not_one_step_compression(self):
        # S never sends a nontrivial p-power to the next power for p>=2.
        for p in [2, 3, 5, 11]:
            self.assertTrue(all(p**k+1 != p**(k+1) for k in range(1, 7)))
        states, matrix = return_transfer(8, bases=[2], mode="unit")
        self.assertEqual(states, [(2, 1, 2), (2, 2, 4), (2, 3, 8)])
        self.assertEqual(matrix, sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]]))

    def test_forward_class_has_no_closed_paths(self):
        z = sp.Symbol("z")
        for mode in ["roof", "height", "unit"]:
            for bases in [[2, 3, 5], [2, 6, 7], [4, 9, 25]]:
                states, matrix = return_transfer(64, bases=bases, mode=mode)
                self.assertEqual((sp.eye(len(states))-z*matrix).det(), 1)
                self.assertEqual(matrix**len(states), sp.zeros(len(states)))
                for k in range(1, 7):
                    self.assertEqual(sp.trace(matrix**k), 0)

    def test_height_damping_singular_values_are_inserted_weights(self):
        states, matrix = return_transfer(81, bases=[2, 3], mode="height")
        gram = matrix.T*matrix
        for j, (p, k, n) in enumerate(states):
            self.assertEqual(gram[j, j], sp.Rational(1, n**4) if n*p <= 81 else 0)
        self.assertEqual(gram, sp.diag(*gram.diagonal()))

    def test_inserting_loops_changes_determinant(self):
        z = sp.Symbol("z")
        loop = collapsed_euler_operator([2, 3, 5])
        self.assertEqual(sp.expand((sp.eye(3)-z*loop).det()
                                   -(4-z)*(9-z)*(25-z)/900), 0)
        self.assertEqual((sp.eye(3)-loop).det(), sp.Rational(16, 25))
        # Fake composite creates an extra Euler factor, not arithmetic recovery.
        fake = collapsed_euler_operator([2, 3, 5, 6])
        self.assertEqual((sp.eye(4)-fake).det(), sp.Rational(16, 25)*sp.Rational(35, 36))

    def test_backward_orientation_cost_is_continuant_not_euler(self):
        z = sp.Symbol("z")
        for depth in range(1, 7):
            states, matrix = return_transfer(2**depth, bases=[2])
            jacobi = matrix + matrix.T
            det = (sp.eye(depth)-z*jacobi).det()
            self.assertEqual(sp.expand(det-path_determinant(depth, sp.Rational(1, 4), z)), 0)
            self.assertEqual(det.subs(z, -z), det)
            self.assertEqual(sp.trace(jacobi*jacobi), sp.Rational(depth-1, 8))

    def test_diagonal_plus_forward_current_has_no_determinant_interaction(self):
        z, a, b, c, u, v, w = sp.symbols("z a b c u v w")
        matrix = sp.Matrix([[a, 0, 0], [u, b, 0], [v, w, c]])
        self.assertEqual(sp.expand((sp.eye(3)-z*matrix).det()
                                   -(1-z*a)*(1-z*b)*(1-z*c)), 0)
        for k in range(1, 5):
            self.assertEqual(sp.expand(sp.trace(matrix**k)-a**k-b**k-c**k), 0)

    def test_invalid_input_is_rejected(self):
        for bases in [[1], [2, 2], [-3]]:
            with self.assertRaises(ValueError):
                jet_states(10, bases)
        with self.assertRaises(ValueError):
            return_transfer(10, mode="wrap")


if __name__ == "__main__":
    unittest.main()
