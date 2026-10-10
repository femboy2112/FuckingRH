"""Exact finite SUCC continuation and source-faithful Gamma/theta seam controls.

No zero locations, fitted ordinates, or Weil positivity assumptions are used.
All negative-integer values are exact Fractions.  mpmath evaluations of
eta and xi are independent numerical calibration, not finite certificates.
"""
import math
import unittest
from fractions import Fraction as Q

import mpmath as mp

from actualization.hasse_theta_seam import (
    SeamError, SUCCDifferenceSource, finite_mutation_parity_error,
    raw_completed_finite_mutation, theta_xi_partial, theta_xi_tail_bound,
)
from actualization import Engine, Limits, Scalar, source_at


class FiniteSUCCHasseTests(unittest.TestCase):
    def test_two_SUCC_differences_recover_negative_one_exactly(self):
        a=SUCCDifferenceSource.zeta(64)
        row=a.negative_difference_rows(1,terms=12)
        self.assertEqual(row["eta"][:2],(Q(1,2),-Q(1,4)))
        self.assertTrue(all(x==0 for x in row["eta"][2:]))
        self.assertEqual(row["hasse_numerator"][:3],(Q(1),-Q(3,2),Q(2,3)))
        self.assertTrue(all(x==0 for x in row["hasse_numerator"][3:]))
        value=a.zeta_negative_certified(1)
        self.assertEqual(value["eta"],Q(1,4))
        self.assertEqual(value["zeta"],-Q(1,12))
        self.assertEqual(value["hasse"],-Q(1,12))
        self.assertTrue(value["status"].startswith("exact"))

    def test_trivial_zeros_from_finite_integer_data_without_gamma(self):
        a=SUCCDifferenceSource.zeta(64)
        expected={
            0:-Q(1,2),1:-Q(1,12),2:Q(0),3:Q(1,120),4:Q(0),
            5:-Q(1,252),6:Q(0),7:Q(1,240),8:Q(0),
            9:-Q(1,132),10:Q(0)
        }
        with mp.workdps(75):
            for m,truth in expected.items():
                value=a.zeta_negative_certified(m)
                self.assertEqual(value["zeta"],truth,(m,value))
                self.assertEqual(value["hasse"],truth)
                self.assertLess(
                    abs(mp.mpf(truth.numerator)/truth.denominator-mp.zeta(-m)),
                    mp.mpf("1e-69")
                )
                eta_row=a.negative_difference_rows(m,terms=min(m+7,63))
                self.assertTrue(all(q==0 for q in eta_row["eta"][m+1:]))
                self.assertTrue(all(q==0 for q in eta_row["hasse_numerator"][m+2:]))

    def test_full_prefix_not_future_or_predicted(self):
        e=Engine(arithmetic=True,limits=Limits(max_target=24))
        for n in range(1,6):
            e.advance(source_at(n),context="zeta",probe="coefficient")
        old=SUCCDifferenceSource.from_engine(e)
        self.assertEqual(old.horizon,5)
        self.assertEqual(old.trace_head,e.head)
        e.predict(6,Scalar(2),"not actualized yet")
        e.step(Scalar(2),context="mutant",probe="coefficient")
        unchanged=SUCCDifferenceSource.from_engine(e)
        self.assertEqual(unchanged.horizon,5)
        self.assertTrue(old.source_prefix_compatible(unchanged))
        with self.assertRaises(SeamError):
            SUCCDifferenceSource.from_engine(e,horizon=6)
        e.propagate()
        actualized=SUCCDifferenceSource.from_engine(e)
        self.assertEqual(actualized.horizon,6)
        self.assertFalse(actualized.genuine_zeta_prefix)
        self.assertEqual(actualized.parity_source_defects(primitive_only=True),{3:Q(1)})
        with self.assertRaises(SeamError):
            actualized.zeta_negative_certified(1)
        self.assertTrue(old.source_prefix_compatible(actualized))

    def test_fake_six_breaks_parity_coupling_and_has_Hasse_divergence(self):
        true=SUCCDifferenceSource.zeta(64)
        fake={n:1 for n in range(1,65)}
        fake[6]=2
        mutant=SUCCDifferenceSource.from_prefix(fake,64)
        self.assertEqual(true.parity_source_defects(),{})
        self.assertEqual(mutant.parity_source_defects(primitive_only=True),{3:Q(1)})
        self.assertEqual(mutant.parity_source_defects(),{3:Q(1),6:-Q(1)})
        self.assertEqual(true.hasse_pole_negative(1,terms=60),-Q(1,12))
        for n in (5,8,16,32,60):
            extra=18*sum((Q(math.comb(j,5),j+1)
                          for j in range(5,n+1)),Q())
            self.assertEqual(
                mutant.hasse_pole_negative(1,terms=n)-true.hasse_pole_negative(1,terms=n),
                extra)
        self.assertGreater(
            mutant.hasse_pole_negative(1,terms=60),
            mutant.hasse_pole_negative(1,terms=32))
        self.assertNotEqual(
            mutant.euler_eta_negative(1,terms=60),Q(1,4))
        self.assertFalse(mutant.genuine_zeta_prefix)

    def test_real_nonunit_prime_mutation_is_not_generic_composite_defect(self):
        def nonunit(n):
            x=Q(1)
            while n%2==0:
                x*=Q(3,2);n//=2
            return x
        changed=SUCCDifferenceSource.from_prefix(
            {n:nonunit(n) for n in range(1,65)},64)
        self.assertFalse(changed.genuine_zeta_prefix)
        self.assertEqual(changed.parity_source_defects(),{})
        with self.assertRaises(SeamError):
            changed.zeta_negative_certified(1)

    def test_eta_acceleration_reconstructs_nonspecial_complex_strip(self):
        a=SUCCDifferenceSource.zeta(256)
        with mp.workdps(115):
            samples=[
                mp.mpc("0.5","2.3"), mp.mpc("0.7","6.2"),
                mp.mpc("0.25","8"), mp.mpc("0.8","1"),
                mp.mpc("-1.4","1.1"),mp.mpc("2","0")
            ]
            for s in samples:
                z=a.zeta_from_eta_analytic(s,terms=112,dps=115)
                self.assertLess(abs(z-mp.zeta(s)),mp.mpf("1e-31"),s)

    def test_eta_also_has_extra_prime_two_factor_zeros(self):
        a=SUCCDifferenceSource.zeta(256)
        with mp.workdps(115):
            s=mp.mpc(1,2*mp.pi/mp.log(2))
            self.assertLess(abs(1-mp.power(2,1-s)),mp.mpf("1e-110"))
            eta=a.eta_euler_analytic(s,terms=128,dps=115)
            self.assertLess(abs(eta),mp.mpf("1e-29"))
            self.assertGreater(abs(mp.zeta(s)),mp.mpf("0.01"))
            with self.assertRaisesRegex(SeamError,"ill-conditioned"):
                a.zeta_from_eta_analytic(s,terms=128,dps=115)

    def test_exact_local_prime_two_defect_identity_for_full_fake_model(self):
        with mp.workdps(90):
            for s in (mp.mpc(2),mp.mpc("0.3","2.4"),mp.mpc(-1)):
                d=mp.power(6,-s)
                lhs= -d-(1-mp.power(2,1-s))*d
                rhs=finite_mutation_parity_error(s,n=6,delta=1,dps=90)
                self.assertLess(abs(lhs-rhs),mp.mpf("1e-82"))
                self.assertGreater(abs(rhs),0)

    def test_insufficient_prefix_and_wrong_source_refused(self):
        src=SUCCDifferenceSource.zeta(6)
        with self.assertRaises(SeamError):
            src.zeta_negative_certified(6)
        with self.assertRaises(SeamError):
            src.euler_eta_negative(-1)
        with self.assertRaises(SeamError):
            src.zeta_from_eta_analytic(2,terms=6)
        with self.assertRaises(SeamError):
            SUCCDifferenceSource.from_prefix({1:1,2:1},3)
        with self.assertRaises(SeamError):
            SUCCDifferenceSource.from_prefix({1:2,2:1},2)
        with self.assertRaises(SeamError):
            SUCCDifferenceSource.from_prefix({1:1,2:1.1},2)
        with self.assertRaises(SeamError):
            src.source_prefix_compatible(SUCCDifferenceSource.zeta(4))


class ThetaGammaSeamTests(unittest.TestCase):
    def test_reflection_is_manifest_and_completed_identity_matches_zeta(self):
        with mp.workdps(100):
            cases=[
                mp.mpc("0.5","4"),mp.mpc("0.4","9"),
                mp.mpc("0.83","2.2"),mp.mpc("0.2","0"),
                mp.mpc(2),mp.mpc("-1.4","0.7")
            ]
            for s in cases:
                t=theta_xi_partial(s,max_integer=7,dps=100)
                r=theta_xi_partial(1-s,max_integer=7,dps=100)
                self.assertLess(abs(t-r),mp.mpf("1e-91"))
                exact=(s*(s-1)/2*mp.power(mp.pi,-s/2)
                       *mp.gamma(s/2)*mp.zeta(s))
                self.assertLess(abs(t-exact),mp.mpf("1e-56"),s)

    def test_critical_strip_truncation_has_theoretical_uniform_bound(self):
        with mp.workdps(100):
            for s in (mp.mpc("0.5","1.3"),mp.mpc("0.7","12"),
                      mp.mpc("0.04","3"),mp.mpc("0.99","0.5")):
                exact=s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)/2
                for m in (1,2,3,4):
                    got=theta_xi_partial(s,max_integer=m,dps=100)
                    bound=theta_xi_tail_bound(s,max_integer=m,dps=100)
                    self.assertLess(abs(got-exact),bound+mp.mpf("1e-88"),(s,m))
                    self.assertLess(theta_xi_tail_bound(s,max_integer=m+1,dps=100),bound)

    def test_trivial_zero_ladder_is_cancelled_in_entire_xi(self):
        with mp.workdps(95):
            for s in (-2,-4,-6):
                left=theta_xi_partial(s,max_integer=5,dps=95)
                right=theta_xi_partial(1-s,max_integer=5,dps=95)
                self.assertLess(abs(left-right),mp.mpf("1e-87"))
                self.assertGreater(abs(left),mp.mpf("0.3"))

    def test_fake_arithmetic_cannot_be_repaired_by_forcing_symmetry(self):
        # Countermodel defined FOR ALL future indices: a(6)=2, all others 1.
        # Its true completed Dirichlet function differs O(1) at s=2.
        # Artificially symmetrized Gaussian-weight theta differs ~exp(-36π).
        with mp.workdps(105):
            s=mp.mpc(2)
            genuine=theta_xi_partial(s,max_integer=6,dps=105)
            fake_symmetric=theta_xi_partial(s,max_integer=6,dps=105,
                                             mutations={6:Q(2)})
            fake_reflected=theta_xi_partial(1-s,max_integer=6,dps=105,
                                             mutations={6:Q(2)})
            fake_actual=raw_completed_finite_mutation(s,n=6,delta=1,dps=105)
            actual_genuine=(s*(s-1)/2*mp.power(mp.pi,-s/2)
                            *mp.gamma(s/2)*mp.zeta(s))
            self.assertLess(abs(fake_symmetric-fake_reflected),mp.mpf("1e-93"))
            self.assertLess(abs(fake_symmetric-genuine),mp.mpf("1e-45"))
            self.assertLess(abs(fake_actual-actual_genuine-1/(36*mp.pi)),mp.mpf("1e-93"))
            self.assertGreater(abs(fake_actual-fake_symmetric),mp.mpf("0.008"))
            # Both continuations are entire in this completion chart;
            # reflection symmetry ALONE did not enforce source identity.

    def test_theta_numeric_charts_and_bounds_refuse_overclaim(self):
        with self.assertRaises(SeamError):
            theta_xi_tail_bound(2,max_integer=4)
        with self.assertRaises(SeamError):
            theta_xi_partial(1,max_integer=41)
        with self.assertRaises(SeamError):
            theta_xi_partial(1,max_integer=4,mutations={6:2})
        with self.assertRaises(SeamError):
            theta_xi_partial(1,max_integer=4,mutations={1:2.2})
        with self.assertRaises(SeamError):
            raw_completed_finite_mutation(2,n=1)
        with self.assertRaises(SeamError):
            raw_completed_finite_mutation(0,n=6)


if __name__=="__main__":
    unittest.main()
