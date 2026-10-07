#!/usr/bin/env python3
"""
Round 008 -- Arithmetic interaction curvature: SUCC/FUCC loops and prime-ray flatness.

Thesis (all RH-inert; this script proves NO RH progress):

  * A "succ loop" is a closed word in the affine generators {SUCC: x->x+1, its inverse,
    FUCC_p: x->p*x, its inverse}.  A loop that returns to its start is a RELATION:
    the composite affine map is the identity.  (The user's Collatz loop 3->13->5->3 is one.)

  * PURE-FUCC loops are FLAT: the multiplicative group is abelian, so every pure-FUCC
    loop is a consequence of commutativity [xp, xq] = 0; it carries ZERO net log-displacement
    and ZERO holonomy.  Equivalently (UFD / unique factorisation): {log p} is Z-independent,
    so the prime-ray translation graph closes NO loop of nonzero displacement.  The prime-ray
    Dirichlet energy therefore depends only on net displacement -- it is a curl-free gradient
    energy.

  * ALL curvature of the SUCC-FUCC system lives in the commutator [SUCC, FUCC]
    (the affine braid, defect = p-1).  This is the "arithmetic interaction curvature."

  * Consequence for the Suzuki finite-conductor wall: the prime-ray edge-weight mass
    2 * sum_{p^k <= e^{2a}} (log p)/p^{k/2} is exactly the prime part of Suzuki's global
    counterterm V_a.  It equals twice the total degree of the prime-ray translation graph.
    Because that graph is flat (Laplacian kernel = constants, E_prime(const)=0), the
    counterterm cannot be dominated by the prime-ray energy alone: the Archimedean/successor
    channel is structurally mandatory.  The wall = a curvature statement, not an arithmetic one.

No zeta zeros are used anywhere.
"""

import math
import itertools
import sympy as sp

x = sp.symbols('x')


def affine_compose(maps):
    """Compose a list of affine maps (sympy exprs in x), applying maps[0] first."""
    e = x
    for m in maps:
        e = m.subs(x, e)
    return sp.simplify(e)


def banner(s):
    print("\n" + "=" * 72 + "\n" + s + "\n" + "=" * 72)


def main():
    banner("1. SUCC loops are RELATIONS (closed word = identity affine map)")

    # User's Collatz loop:  3 -> 4n+1 -> (3n+1)/8 -> (2n-1)/3 -> 3
    collatz = [4 * x + 1, (3 * x + 1) / 8, (2 * x - 1) / 3]
    vals = [3]
    for m in collatz:
        vals.append(int(m.subs(x, vals[-1])))
    print(f"   Collatz loop path: {vals}   (returns to start)")
    H = affine_compose(collatz)
    print(f"   composite word  = {H}   => IDENTITY: the loop is a relation in ax+b.")
    assert H == x, "Collatz loop must compose to identity"

    # multiplicative content: numerator primes vs denominator primes must balance
    lin = sp.Integer(4) * sp.Rational(3, 8) * sp.Rational(2, 3)
    print(f"   product of linear parts = {lin}  (=1 => primes balance exactly)")
    print(f"     up mass   4*3*2 = 24 = {sp.factorint(24)}")
    print(f"     down mass 8*3   = 24 = {sp.factorint(24)}   -> {{2,3}} balanced ('coherent' syzygy)")
    assert lin == 1

    # a second, structurally different loop to show generality
    # 1 -> x2 -> 2 -> x3 -> 6 -> /2 -> 3 -> /3 -> 1   (pure-FUCC 4-cycle)
    fucc = [2 * x, 3 * x, x / 2, x / 3]
    v = 1
    path = [1]
    for m in fucc:
        v = int(m.subs(x, v))
        path.append(v)
    Hf = affine_compose(fucc)
    print(f"\n   Pure-FUCC loop path: {path}")
    print(f"   composite word  = {Hf}   => IDENTITY (commutativity relation [x2,x3]=0)")
    assert Hf == x

    banner("2. ARITHMETIC INTERACTION CURVATURE = [SUCC, FUCC]  (affine braid)")
    p = sp.symbols('p', positive=True)
    T = x + 1        # SUCC
    D = p * x        # FUCC_p
    TD = T.subs(x, D)      # SUCC after FUCC:  p*x + 1
    DT = D.subs(x, T)      # FUCC after SUCC:  p*(x+1) = p*x + p
    defect = sp.simplify(DT - TD)
    print(f"   (SUCC o FUCC)(x) = {TD}")
    print(f"   (FUCC o SUCC)(x) = {sp.expand(DT)}")
    print(f"   curvature defect  FUCC.SUCC - SUCC.FUCC = {defect}  (= p-1 != 0)")
    print("   This is the ONLY source of non-abelian holonomy in the system.")
    assert sp.simplify(defect - (p - 1)) == 0

    banner("3. FUCC IS FLAT: every pure-FUCC loop has ZERO net log-displacement")
    # a pure-FUCC word is sum of signed log p; it closes iff the multiset of primes balances
    disp = math.log(2) + math.log(3) - math.log(2) - math.log(3)
    print(f"   net log-displacement of the 4-cycle above = {disp:+.1e}  (=0)")
    # UFD: {log p} is Z-independent -> no nonzero-displacement loop exists
    best = None
    for a, b, c in itertools.product(range(-8, 9), repeat=3):
        if (a, b, c) == (0, 0, 0):
            continue
        val = abs(a * math.log(2) + b * math.log(3) + c * math.log(5))
        if best is None or val < best[0]:
            best = (val, (a, b, c))
    print(f"   min |a*log2+b*log3+c*log5| over 0<|coeffs|<=8 : {best[0]:.6f} at {best[1]}")
    print("   bounded away from 0 => prod p^k = 1 forces k=0 (UFD) => NO nonzero-displacement loop.")
    print("   => prime-ray energy depends only on net displacement: curl-free / gradient / FLAT.")
    assert best[0] > 1e-3

    banner("4. The counterterm IS the prime-ray graph degree (flat => coupling is mandatory)")
    # Suzuki prime counterterm mass (prime part of V_a) = 2 * sum_{p^k<=e^{2a}} log p / p^{k/2}
    # = 2 * (total edge weight of the prime-ray translation graph) = 2 * degree.
    def prime_powers_up_to(bound):
        out = []
        n = 2
        # sieve primes up to bound
        sieve = [True] * (int(bound) + 1)
        for q in range(2, int(bound) + 1):
            if sieve[q]:
                for mlt in range(q * q, int(bound) + 1, q):
                    sieve[mlt] = False
        primes = [q for q in range(2, int(bound) + 1) if sieve[q]]
        for q in primes:
            pk = q
            k = 1
            while pk <= bound:
                out.append((q, k, pk))
                k += 1
                pk *= q
        return out

    for a in (1.0, 1.5, 2.0):
        bound = math.exp(2 * a)
        pks = prime_powers_up_to(bound)
        degree = sum(math.log(q) / pk ** 0.5 for (q, k, pk) in pks)
        counterterm_prime = 2 * degree
        print(f"   a={a}: horizon e^(2a)={bound:8.1f}, #prime-power edges={len(pks):4d}, "
              f"degree(sum w)={degree:.5f}, prime counterterm 2*degree={counterterm_prime:.5f}")
    print("   The prime-ray graph Laplacian kills constants (E_prime(const)=0),")
    print("   so E_prime ALONE cannot dominate V_a*||v||^2.  The Archimedean/|xi| channel")
    print("   must supply the low-frequency control.  => the wall is the COUPLING = curvature.")

    print("\nALL CHECKS PASSED.  (RH-inert structural facts; proves no RH progress.)")


if __name__ == "__main__":
    main()
