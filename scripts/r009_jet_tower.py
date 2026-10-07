#!/usr/bin/env python3
r"""
Round 009 / Pillar 1 -- The omega-jet tower = the user's "chain of 1st/2nd/3rd-order derivatives".

The externally-supplied intuition: "how strongly the first actualization affects the state ... feels
like polynomial approximation and chains of first/second/third order derivatives." This is EXACTLY the
omega-jet of Suzuki's inner family, already proven in aletheia OMEGA_ZERO_CONDUCTOR_JET.md; here we
re-verify it and give the differential-geometric reading: the jet is the Taylor expansion of the inner
curve B_omega off the flat base point B_0 = 1, the FIRST jet is the velocity = the Weil generator
-2(xi'/xi)(s+1/2), and the stratification by nu(n) = #distinct primes IS the Taylor order.

CREDIT (standard / prior art, NOT invented here): Suzuki 2012 (RIMS B34) builds the canonical system
for Theta_omega; the jet stratification is aletheia OMEGA_ZERO_CONDUCTOR_JET.md; the Weil generator
-2(xi'/xi) is the Lagarias/Weil object. RH IS OPEN; nothing here is a proof. No zeta zeros are used as
input (xi, xi'/xi are evaluated as meromorphic functions, not fed zero ordinates).
"""

import math
import sympy as sp
import mpmath as mp

mp.mp.dps = 40


def xi(s):
    s = mp.mpf(s) if not isinstance(s, mp.mpc) else s
    return mp.mpf('0.5') * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def xi_log_deriv(s, h=mp.mpf('1e-12')):
    return (mp.log(xi(s + h)) - mp.log(xi(s - h))) / (2 * h)


def banner(t):
    print("\n" + "=" * 74 + "\n" + t + "\n" + "=" * 74)


def main():
    w = sp.symbols('omega')

    banner("1. The conductor coefficient b_omega(n) and its omega-jet (chain of derivatives)")
    print("b_omega(n) = n^(omega-1/2) * prod_{p|n} (1 - p^(-2 omega)); b_0(n)=0 for n>1, b_0(1)=1.")
    print("Taylor in omega at 0 -- first NONZERO order = nu(n) = # distinct primes:\n")
    print(f"   {'n':>3} {'nu':>3} {'first nonzero jet order':>24}   check b_0^(nu) = nu! 2^nu prod(log p)/sqrt(n)")
    for n in [1, 2, 3, 4, 6, 8, 12, 30]:
        fac = sp.factorint(n)
        nu = len(fac)
        # symbolic b_omega(n)
        b = n ** (w - sp.Rational(1, 2)) * sp.prod([(1 - sp.Integer(p) ** (-2 * w)) for p in fac]) if nu else n ** (w - sp.Rational(1, 2))
        ser = sp.series(b, w, 0, (nu + 2) if nu else 2).removeO()
        # first nonzero derivative order
        order = None
        for j in range(0, nu + 2):
            cj = sp.diff(b, w, j).subs(w, 0)
            cj = sp.simplify(cj)
            if cj != 0:
                order = j
                break
        # predicted b_0^(nu)
        if nu == 0:
            pred = sp.nsimplify(0)
            got = sp.diff(b, w, 0).subs(w, 0)  # = 1 for n=1
            ok = (n == 1 and sp.simplify(got - 1) == 0)
            print(f"   {n:>3} {nu:>3} {order!s:>24}   b_0(1)={got} (flat base point) [{'OK' if ok else 'FAIL'}]")
        else:
            cnu = sp.simplify(sp.diff(b, w, nu).subs(w, 0))
            pred = sp.factorial(nu) * 2 ** nu * sp.prod([sp.log(p) for p in fac]) / sp.sqrt(n)
            ok = sp.simplify(cnu - pred) == 0 and order == nu
            print(f"   {n:>3} {nu:>3} {order!s:>24}   match={'OK' if ok else 'FAIL'}")
            assert ok, (n, cnu, pred, order)

    banner("2. First jet = von Mangoldt = the Weil layer:  b_0'(n) = 2 Lambda(n)/sqrt(n)")
    for n in [2, 3, 4, 5, 6, 7, 8, 9, 12]:
        fac = sp.factorint(n)
        b = n ** (w - sp.Rational(1, 2)) * sp.prod([(1 - sp.Integer(p) ** (-2 * w)) for p in fac])
        b1 = sp.simplify(sp.diff(b, w, 1).subs(w, 0))
        Lam = sp.log(list(fac)[0]) if len(fac) == 1 else sp.Integer(0)  # Lambda(n)=log p iff prime power
        pred = 2 * Lam / sp.sqrt(n)
        ok = sp.simplify(b1 - pred) == 0
        print(f"   n={n:>2}: b_0'(n)={sp.nsimplify(b1)!s:>22}  2Lambda/sqrt n={sp.nsimplify(pred)!s:>16}  [{'OK' if ok else 'FAIL'}]")
        assert ok

    banner("3. The inner curve B_omega(s) off the flat base B_0=1; VELOCITY = -2 (xi'/xi)(s+1/2)")
    print("B_omega(s) = xi(s+1/2-omega)/xi(s+1/2+omega),  B_0=1.  dB/domega|_0 should be -2(xi'/xi)(s+1/2).")
    for s in [mp.mpf('1.5'), mp.mpc(2, 1), mp.mpc('1.2', '0.8')]:
        def B(om):
            return xi(s + mp.mpf('0.5') - om) / xi(s + mp.mpf('0.5') + om)
        h = mp.mpf('1e-6')
        vel_num = (B(h) - B(-h)) / (2 * h)              # d/domega at 0 (B_0=1)
        vel_pred = -2 * xi_log_deriv(s + mp.mpf('0.5'))  # -2 (xi'/xi)(s+1/2)
        err = abs(vel_num - vel_pred)
        print(f"   s={str(s):>14}: velocity={mp.nstr(vel_num,8):>22}  -2 xi'/xi={mp.nstr(vel_pred,8):>22}  |diff|={mp.nstr(err,2)}")
        assert err < mp.mpf('1e-4')

    banner("4. Dirichlet side: A_omega(s)=zeta(s+1/2-omega)/zeta(s+1/2+omega); A_0'(s)=2 sum Lambda(n)/n^{s+1/2}")
    s = mp.mpf('2.0')

    def A(om):
        return mp.zeta(s + mp.mpf('0.5') - om) / mp.zeta(s + mp.mpf('0.5') + om)
    h = mp.mpf('1e-6')
    A0p = (A(h) - A(-h)) / (2 * h)
    # truncated 2 sum Lambda(n) n^{-(s+1/2)}
    def Lambda(n):
        f = sp.factorint(n)
        return float(sp.log(list(f)[0])) if len(f) == 1 else 0.0
    trunc = 2 * mp.fsum([Lambda(n) * mp.mpf(n) ** (-(s + mp.mpf('0.5'))) for n in range(2, 4000)])
    print(f"   A_0'(2)      = {mp.nstr(A0p,10)}")
    print(f"   2 sum Lambda = {mp.nstr(trunc,10)}  (truncated n<4000)  |diff|={mp.nstr(abs(A0p-trunc),2)}")
    assert abs(A0p - trunc) < mp.mpf('1e-3')

    banner("5. The 'chain of derivatives / polynomial approximation' = the nu(n) filtration")
    print("Taylor order j in omega first populates integers with exactly j distinct primes:")
    for j in range(0, 4):
        members = [n for n in range(1, 61) if len(sp.factorint(n)) == j][:12]
        label = {0: "n=1 (flat base)", 1: "prime powers (Weil/von Mangoldt layer)",
                 2: "two-prime conductors", 3: "three-prime conductors"}[j]
        print(f"   O(omega^{j}):  {label}\n              members<=60: {members}")
    print("\nGR reading: B_omega is a curve off the flat base B_0=1; the first jet is the VELOCITY")
    print("(= Weil generator -2(xi'/xi)(s+1/2)); higher jets (nu>=2) are the acceleration/curvature.")
    print("\nALL CHECKS PASSED.  RH-inert (standard jet of Suzuki's family; credit Suzuki 2012, OMEGA_ZERO).")
    print("RH remains open.  No zeta zeros used as input.")


if __name__ == "__main__":
    main()
