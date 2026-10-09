"""Synthetic, exact boundary tests. No Riemann-zero data are supplied."""
from fractions import Fraction
import sympy as sp
from scripts.riemann_sphere_atlas_probe import (
    HALF, S, cayley, check_controls, finite_jet_adversary,
    li_for_symmetric_quartet, li_cnd_gram, all_principal_minors_nonnegative,
    radial_defect, trivial_norm_diagonal, reflection_control,
)


def test_equator_and_reflection_are_exact():
    rho = sp.Rational(1, 4) + sp.I
    w = cayley(rho)
    assert reflection_control(rho) == 0
    assert sp.simplify(cayley(1-rho)-1/w) == 0
    assert sp.simplify(cayley(HALF+sp.I)*sp.conjugate(cayley(HALF+sp.I))-1) == 0
    assert sp.simplify(w + 1/sp.conjugate(w)) != 0  # antipodal != reflection


def test_li_finite_horizon_counterexample_exact():
    a = Fraction(1,4)
    assert all(li_for_symmetric_quartet(a, n) > 0 for n in range(1,6))
    assert li_for_symmetric_quartet(a, 6) == Fraction(-309804177801344, 5892961181640625)
    a = Fraction(1,4096)
    assert all(li_for_symmetric_quartet(a, n) > 0 for n in range(1,41))


def test_cnd_kernel_finite_diagnostic_exact():
    assert all_principal_minors_nonnegative(li_cnd_gram(Fraction(0), 3))
    assert li_cnd_gram(Fraction(1,4), 3).det() < 0
    assert li_cnd_gram(Fraction(1,4096), 3).det() < 0


def test_radial_defect_is_precisely_the_missing_norm_identity():
    assert radial_defect(Fraction(0), 1) == 0
    for a in (Fraction(1, 4), Fraction(1, 4096)):
        for n in (1, 3, 6):
            assert radial_defect(a, n) > 0
            assert (trivial_norm_diagonal(a, n)
                    - 2 * li_for_symmetric_quartet(a, n)) == radial_defect(a, n)


def test_finite_jet_adversary_exact():
    rho = sp.Rational(1,4)+sp.I
    samples = [sp.Integer(0), sp.Integer(1), HALF+sp.I/3]
    B = finite_jet_adversary(samples, 3, rho)
    E = (S-HALF)**2+1
    assert sp.simplify(B.subs(S,rho)) == 0
    assert sp.simplify(B.subs(S,1-sp.conjugate(rho))) == 0
    assert sp.simplify(B.subs(S,1-S)-B) == 0
    for z in samples:
        for d in range(3):
            assert sp.simplify(sp.diff(E*(B-1), S, d).subs(S,z)) == 0


def test_integrated_probe():
    report = check_controls()
    assert report["antipodal_equals_RH_reflection"] is False
    assert report["off_line_quartet_a_1_4096"]["horizon"] == 40
