"""Exact controls for the RH equator atlas. Synthetic zeros only; no zeta-zero input.

The symbolic adversary is a generic entire-function non-uniqueness test, NOT an
arithmetic L-function or a counterexample to RH.
"""
from fractions import Fraction
import json
from itertools import combinations
import sympy as sp

S = sp.symbols("s")
T = sp.symbols("t")
HALF = sp.Rational(1, 2)


def cayley(z):
    """Möbius s -> (s-1)/s, including the critical-line equator."""
    return sp.cancel((z - 1) / z)


def reflection_control(z):
    """The FE+conjugation reflection, not the antipodal twistor map."""
    w = cayley(z)
    return sp.simplify(cayley(1 - sp.conjugate(z)) - 1 / sp.conjugate(w))


def finite_jet_adversary(samples, order=3, rho=sp.Rational(1, 4) + sp.I):
    """Real, s<->1-s symmetric polynomial B, B=1 to order at samples,
    B(rho)=0 at a prescribed off-critical nonreal rho.

    No Euler-product constraints are retained. This proves only a finite-jet
    obstruction in the broad class of real symmetric entire functions.
    """
    u = (S - HALF) ** 2
    ur = sp.expand((rho - HALF) ** 2)
    assert sp.im(ur) != 0
    q = sp.Integer(1)
    for z in samples:
        uz = sp.expand((z - HALF) ** 2)
        q *= ((T - uz) * (T - sp.conjugate(uz))) ** order
    q = sp.factor(q)
    qr = sp.simplify(q.subs(T, ur))
    assert qr != 0, "prescribed off-line zero conflicts with samples"
    target = sp.simplify(-1 / qr)
    b = sp.simplify(sp.im(target) / sp.im(ur))
    a = sp.simplify(sp.re(target) - b * sp.re(ur))
    assert sp.im(a) == 0 and sp.im(b) == 0
    factor = 1 + q.subs(T, u) * (a + b * u)
    return factor


def gaussian_multiply(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gaussian_real_power(z, n):
    out = (Fraction(1), Fraction(0))
    for _ in range(n):
        out = gaussian_multiply(out, z)
    return out[0]


def cayley_fraction(x, y):
    den = x * x + y * y
    return (Fraction(1) - x / den, y / den)


def li_for_symmetric_quartet(a, n, t=Fraction(1)):
    """Exact finite zero-multiset Li expression for 1/2+-a+-it.

    It is NOT a zeta Li coefficient and makes no L-function claim.
    """
    right = cayley_fraction(Fraction(1, 2) + a, t)
    left = cayley_fraction(Fraction(1, 2) - a, t)
    return Fraction(4) - 2 * (gaussian_real_power(right, n) + gaussian_real_power(left, n))


def li_cnd_gram(a, dimension, t=Fraction(1)):
    """Schoenberg kernel lambda_i+lambda_j-lambda_|i-j|, exact."""
    L = [li_for_symmetric_quartet(a, n, t) for n in range(dimension + 1)]
    return sp.Matrix([[sp.Rational(L[i] + L[j] - L[abs(i - j)])
                       for j in range(1, dimension + 1)]
                      for i in range(1, dimension + 1)])


def all_principal_minors_nonnegative(M):
    for k in range(1, M.rows + 1):
        for inds in combinations(range(M.rows), k):
            if M.extract(inds, inds).det() < 0:
                return False
    return True


def check_controls():
    # Analytic involutions: critical-line reflection fixes equator; antipodal doesn't.
    rho = sp.Rational(1, 4) + sp.I
    assert reflection_control(rho) == 0
    on = HALF + sp.I
    assert sp.simplify(cayley(on) * sp.conjugate(cayley(on)) - 1) == 0
    w = cayley(on)
    assert sp.simplify(w + 1 / sp.conjugate(w)) != 0
    assert sp.simplify(cayley(1 - on) - 1 / cayley(on)) == 0

    # Li: finite-horizon pass does not certify all-n positivity.
    off = Fraction(1, 4)
    assert all(li_for_symmetric_quartet(off, n) > 0 for n in range(1, 6))
    assert li_for_symmetric_quartet(off, 6) < 0
    near = Fraction(1, 4096)
    horizon = 40
    assert all(li_for_symmetric_quartet(near, n) > 0 for n in range(1, horizon + 1))

    # Correlation is more discriminating than scalar Li positivity on this
    # synthetic quartet: an exact 3x3 CND Gram minor is negative already.
    K_on = li_cnd_gram(Fraction(0), 3)
    K_far = li_cnd_gram(off, 3)
    K_near = li_cnd_gram(near, 3)
    assert all_principal_minors_nonnegative(K_on)
    assert K_far.det() < 0 and K_near.det() < 0

    # A finite collection of arbitrary complex jets cannot distinguish a
    # fully on-equator symmetric baseline from a symmetric off-equator model.
    samples = [sp.Integer(0), sp.Integer(1), HALF + sp.I / 3]
    order = 3
    B = finite_jet_adversary(samples, order, rho)
    E = (S - HALF) ** 2 + 1  # calibrated on-equator zero pair only
    F = E * B
    assert sp.simplify(B.subs(S, rho)) == 0
    assert sp.simplify(B.subs(S, 1 - rho)) == 0
    assert sp.simplify(B.subs(S, sp.conjugate(rho))) == 0
    assert sp.simplify(B.subs(S, 1 - sp.conjugate(rho))) == 0
    assert sp.simplify(B.subs(S, 1 - S) - B) == 0
    assert sp.simplify(sp.conjugate(B).subs(sp.conjugate(S), S) - B) == 0
    for z in samples:
        for j in range(order):
            assert sp.simplify(sp.diff(F - E, S, j).subs(S, z)) == 0
    assert sp.simplify(E.subs(S, rho)) != 0

    # Arithmetic language: mixed composites are zero, prime powers are not.
    from sympy import primefactors
    assert len(primefactors(4)) == 1 and len(primefactors(6)) == 2
    return {
        "scope": "exact rational/symbolic synthetic controls; RH remains open",
        "equator": "|w|=1 iff Re(s)=1/2",
        "off_line_quartet_a_1_4": {
            "li_1_to_5": "positive",
            "li_6": str(li_for_symmetric_quartet(off, 6)),
        },
        "off_line_quartet_a_1_4096": {
            "first_40_li": "strictly positive (exact Fractions)",
            "horizon": horizon,
        },
        "li_cnd_3x3": {
            "on_line_quartet": "positive semidefinite (all principal minors exact)",
            "off_line_a_1_4_determinant": "negative",
            "off_line_a_1_4096_determinant": "negative",
            "note": "a stronger finite diagnostic here, not a proof for xi",
        },
        "finite_jet_adversary": {
            "samples": list(map(str, samples)),
            "matched_jet_orders": list(range(order)),
            "new_off_critical_quartet": list(map(str, [rho, 1 - rho, sp.conjugate(rho), 1 - sp.conjugate(rho)])),
        },
        "antipodal_equals_RH_reflection": False,
    }


if __name__ == "__main__":
    print(json.dumps(check_controls(), indent=2))
