"""Zero-input-free algebraic calibration and hostile mutations for source/boundary object."""
from math import log
import unittest

from scripts.arithmetic_source_boundary import (
    chi_mod_5, clock_defect, coefficients_from_local_parameters,
    character_compatibility_defect,
    compressed_shift, factorization, local_unitarity_defect,
    logarithmic_derivative_coefficients, logarithmic_source_defect,
    mixed_commutator_boundary, mixed_commutator_nested,
    prime_half_density_weight, prime_power,
    truncated_multiplication_shift, finite_dirichlet_operator,
    finite_euler_inverse, finite_nilpotent_log, finite_clock_commutator,
    finite_source_operator,
)


class ArithmeticSourceBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.limit = 64
        self.alpha = {p: chi_mod_5(p) for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61)}

    def test_factorization_and_prime_power_fixtures(self):
        self.assertEqual(factorization(1), ())
        self.assertEqual(factorization(72), ((2, 3), (3, 2)))
        self.assertIsNone(prime_power(6))
        self.assertEqual(prime_power(32), (2, 5))
        self.assertEqual(prime_power(37), (37, 1))

    def test_chi5_true_source_has_no_mixed_composite_atoms(self):
        a = coefficients_from_local_parameters(self.alpha, self.limit)
        b = logarithmic_derivative_coefficients(a)
        self.assertLess(logarithmic_source_defect(a, self.alpha), 1e-12)
        self.assertLess(abs(b[6]), 1e-12)
        self.assertLess(abs(b[10]), 1e-12)
        self.assertAlmostEqual(b[8].imag, -log(2), places=12)
        self.assertEqual(b[25], 0j)  # ramified p=5

    def test_faked_composite_six_is_detected_exactly(self):
        a = coefficients_from_local_parameters(self.alpha, self.limit)
        a[6] += 0.01
        b = logarithmic_derivative_coefficients(a)
        self.assertAlmostEqual(b[6].real, 0.01 * log(6), places=12)
        self.assertGreater(logarithmic_source_defect(a, self.alpha), 0.01)

    def test_davenport_heilbronn_six_defect_without_zeros(self):
        kappa = 0.7
        a = [0j] * 7
        a[1], a[2], a[3], a[6] = 1, kappa, -kappa, 1
        b = logarithmic_derivative_coefficients(a)
        self.assertAlmostEqual(b[6].real, (1+kappa*kappa)*log(6), places=12)

    def test_unity_of_actual_dirichlet_local_character(self):
        self.assertEqual(local_unitarity_defect(self.alpha), 0.0)
        altered = dict(self.alpha)
        altered[2] *= 1.01
        self.assertAlmostEqual(local_unitarity_defect(altered), 0.01, places=12)
        # A nonunit local parameter STILL defines an Euler product: support alone misses it.
        a = coefficients_from_local_parameters(altered, self.limit)
        self.assertLess(logarithmic_source_defect(a, altered), 1e-12)

    def test_character_mod_five_group_law_and_unit_phase_not_sufficient(self):
        from cmath import exp
        for n in range(1, 15):
            for m in range(1, 15):
                self.assertAlmostEqual(abs(chi_mod_5(m*n)-chi_mod_5(m)*chi_mod_5(n)),0)
        self.assertLess(character_compatibility_defect(self.alpha,chi_mod_5),1e-12)
        phase_mutant = dict(self.alpha)
        phase_mutant[2] *= exp(0.03j)
        self.assertLess(local_unitarity_defect(phase_mutant),1e-12)
        self.assertGreater(character_compatibility_defect(phase_mutant,chi_mod_5),0.02)

    def test_dilating_clock_is_log_n_not_a_free_frequency(self):
        self.assertEqual(clock_defect(2, log(2)), 0)
        self.assertAlmostEqual(clock_defect(2, 1.0001 * log(2)), 0.0001*log(2))

    def test_half_density_is_exact_source_weight(self):
        self.assertAlmostEqual(prime_half_density_weight(2, 3), log(2)/(2**1.5))
        self.assertNotAlmostEqual(prime_half_density_weight(2, 3), log(2)/(2**1.8))

    def test_compressed_shifts_conspire_at_common_boundary(self):
        L = 1.0
        a, b = log(2), log(3)
        f = lambda x: complex(1 + x/10, x*x/7)
        for x in (-0.999, -0.6, -0.2, 0.0, 0.2, 0.307, 0.6, 0.999):
            lhs = mixed_commutator_nested(f, x, a, b, L)
            rhs = mixed_commutator_boundary(f, x, a, b, L)
            self.assertAlmostEqual(abs(lhs - rhs), 0.0, places=12)
        one = lambda x: 1+0j
        self.assertEqual(mixed_commutator_boundary(one, -0.2, a, b, L), 1)
        self.assertEqual(mixed_commutator_boundary(one, 0.6, a, b, L), -1)

    def test_no_cross_commutator_without_compression(self):
        # On R: all translations, including adjoints, commute. Boundary is load-bearing.
        f = lambda x: complex(x*x, x)
        a, b, x = log(2), log(3), 0.4
        self.assertAlmostEqual(abs(f(x+a-b)-f(x-b+a)), 0.0)

    def test_exact_sos_and_mixed_curvature_is_not_positive(self):
        # Lattice shifts are an independent algebraic control, NOT replacements
        # for the true irrational prime logarithms used in the continuum.
        import numpy as np
        d = 9
        T1 = np.diag(np.ones(d - 1), -1).astype(complex)
        T2 = T1 @ T1
        U = -1j * T1  # chi(2)=i, U=conj(chi(2))T_1
        I = np.eye(d)
        lhs = 2 * I - U - U.conj().T
        rhs = (I-U).conj().T @ (I-U) + (I-U.conj().T@U)
        np.testing.assert_allclose(lhs, rhs, atol=1e-14)
        self.assertGreaterEqual(np.linalg.eigvalsh(lhs).min(), -1e-12)
        # Compress-first is genuinely different from whole-line translations:
        # the common-boundary mixed commutator has both signs.
        B = T1 + T2
        curvature = B.conj().T @ B - B @ B.conj().T
        eigs = np.linalg.eigvalsh(curvature)
        self.assertLess(eigs[0], -1e-6)
        self.assertGreater(eigs[-1], 1e-6)
        self.assertAlmostEqual(float(np.trace(curvature).real), 0.0)

    def test_canonical_euler_log_commutator_realizes_source(self):
        import numpy as np
        a = coefficients_from_local_parameters(self.alpha, 40)
        direct = finite_dirichlet_operator([z.conjugate() for z in a])
        E = finite_euler_inverse({p: z.conjugate() for p, z in self.alpha.items() if p <= 40}, 40)
        I = np.eye(40, dtype=complex)
        np.testing.assert_allclose(E @ direct, I, atol=1e-13)
        V = finite_nilpotent_log(direct)
        got = finite_clock_commutator(V)
        b = logarithmic_derivative_coefficients([z.conjugate() for z in a])
        expected = finite_source_operator(b)
        np.testing.assert_allclose(got, expected, atol=1e-13)
        self.assertLess(abs(got[5,0]), 1e-13)  # no forbidden composite-6 impulse
        self.assertAlmostEqual(got[3,0].real, -log(2)/2, places=12)  # chi(4)=-1

    def test_canonical_operator_detects_fake_six_and_dh(self):
        from math import sqrt
        a = coefficients_from_local_parameters(self.alpha, 30)
        changed = list(a)
        changed[6] += 0.01
        direct = finite_dirichlet_operator([z.conjugate() for z in changed])
        got = finite_clock_commutator(finite_nilpotent_log(direct))
        self.assertAlmostEqual(got[5,0].real, 0.01*log(6)/sqrt(6), places=12)
        kappa = 0.7
        dh = [0j] * 31
        dh[1],dh[2],dh[3],dh[6] = 1,kappa,-kappa,1
        dh_operator = finite_clock_commutator(finite_nilpotent_log(finite_dirichlet_operator(dh)))
        self.assertAlmostEqual(dh_operator[5,0].real,(1+kappa*kappa)*log(6)/sqrt(6),places=12)

    def test_canonical_boundary_mixed_curvature_has_both_signs(self):
        import numpy as np
        a = coefficients_from_local_parameters(self.alpha, 40)
        D = finite_clock_commutator(finite_nilpotent_log(
            finite_dirichlet_operator([z.conjugate() for z in a])))
        curvature = D.conj().T @ D - D @ D.conj().T
        eigen = np.linalg.eigvalsh(curvature)
        self.assertLess(eigen[0],-0.01)
        self.assertGreater(eigen[-1],0.01)
        self.assertAlmostEqual(np.trace(curvature).real,0,places=11)
        # Contrast with infinite, full-line translates: cross adjoint commutator = 0.
        V2 = truncated_multiplication_shift(2, 40)
        V3 = truncated_multiplication_shift(3, 40)
        C23 = V2.conj().T @ V3 - V3 @ V2.conj().T
        self.assertGreater(float(np.linalg.norm(C23)),0.1)

    def test_clock_covariance_in_matrix_representation(self):
        import numpy as np
        V2 = truncated_multiplication_shift(2, 30)
        measured = finite_clock_commutator(V2)
        np.testing.assert_allclose(measured,log(2)*V2,atol=1e-14)
        distorted = (1+1e-4)*log(2)*V2
        self.assertGreater(np.linalg.norm(measured-distorted),1e-5)

    def test_nilpotent_log_does_not_truncate_small_source_amplitudes(self):
        import numpy as np
        v6 = truncated_multiplication_shift(6,30)
        I = np.eye(30)
        small = I + 1e-16*v6
        out = finite_nilpotent_log(small)
        # Float64 cannot represent 1+1e-16 for off-diagonal? It CAN: offdiag adds to 0.
        self.assertAlmostEqual(abs(out[5,0]-(1e-16)),0,places=25)

    def test_sharp_boundary_pulse_indefiniteness_lemma(self):
        import numpy as np
        d = 11
        V1 = np.diag(np.ones(d-1),-1)
        V3 = V1 @ V1 @ V1
        B = (1+2j)*V1+(0.5-1j)*V3
        curv = B.conj().T @ B-B @ B.conj().T
        mass = abs(1+2j)**2+abs(0.5-1j)**2
        self.assertAlmostEqual(curv[0,0].real,mass, places=12)
        self.assertAlmostEqual(curv[-1,-1].real,-mass, places=12)


if __name__ == '__main__':
    unittest.main()
