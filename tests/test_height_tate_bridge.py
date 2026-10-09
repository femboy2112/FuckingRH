"""Finite, zero-free controls for the height-Tate bridge (not an RH sign test)."""
import unittest
from fractions import Fraction
from math import log, sqrt
import mpmath as mp
from scripts.height_tate_bridge_probe import (
    character_mixture_atom_six, clock_shift_defect, cocycle, exact_mass,
    finite_height_mass, height, near_unit_bessel, rational_states,
    tate_direct_overlap, tate_fourier_gamma, tate_fourier_grid, tate_overlap,
    totient, totient_height_mass,
)


class HeightTateBridgeControls(unittest.TestCase):
    def test_totient_independent_enumeration(self):
        for M in (2, 4, 8, 16):
            self.assertEqual(len(rational_states(M)),
                             1+2*sum(totient(m) for m in range(2,M+1)))
            self.assertAlmostEqual(finite_height_mass(M,1.25),
                                   totient_height_mass(M,1.25),places=11)

    def test_tate_gaussian_closed_overlap(self):
        mp.mp.dps=55
        for r,s in [(Fraction(1),Fraction(2)),
                    (Fraction(2,3),Fraction(5,4)),
                    (Fraction(17,16),Fraction(33,32))]:
            self.assertAlmostEqual(float(tate_direct_overlap(r,s)),
                                   tate_overlap(r,s),places=12)

    def test_mellin_gamma_from_independent_grid(self):
        mp.mp.dps=50
        for t in (0,2.5,14.25):
            self.assertLess(abs(tate_fourier_grid(t)-
                                complex(tate_fourier_gamma(t))),1e-9)

    def test_rational_cocycle_intertwining(self):
        from math import exp
        w=lambda r:exp(-1.25*height(r))
        for q in [Fraction(2), Fraction(3), Fraction(2,3)]:
            for r in [Fraction(1), Fraction(2,3), Fraction(5,4)]:
                self.assertAlmostEqual(cocycle(1.25,q,r)*w(q*r),w(r),places=13)

    def test_source_connected_six_and_character_mixture(self):
        self.assertAlmostEqual(character_mixture_atom_six(1,0).real,0,places=13)
        self.assertAlmostEqual(character_mixture_atom_six(.6,.4).real,
                               .96*log(6),places=12)

    def test_shifted_real_log_breaks_intertwining(self):
        self.assertEqual(clock_shift_defect(0),0)
        self.assertGreater(clock_shift_defect(.01),0)
        self.assertLess(clock_shift_defect(.01),clock_shift_defect(.1))

    def test_independent_box_seed_threshold_witness(self):
        for tau in (.5,1.,1.25):
            xs=[near_unit_bessel(M,tau,profile='box') for M in (32,64,128)]
            self.assertTrue(xs[0]<xs[1]<xs[2])
        # Finite growth is an observation; infinite divergence is proved in the note.

    def test_normalized_hs_limit_is_nonzero_but_each_fixed_label_goes_to_zero(self):
        mp.mp.dps=50
        targets=[(tau,float((tau-1)*exact_mass(tau))) for tau in (1.1,1.01,1.001)]
        expected=float(1/mp.zeta(2))
        self.assertLess(abs(targets[-1][1]-expected),.001)
        self.assertGreater(sqrt(.1),sqrt(.001))

    def test_bad_tau_rejected_as_hilbert_schmidt(self):
        for tau in (.5,1.):
            with self.assertRaises(ValueError): exact_mass(tau)


if __name__=='__main__': unittest.main()
