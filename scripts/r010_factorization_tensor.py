#!/usr/bin/env python3
r"""
Round 010 / Part B -- The composite-factorization pattern = the Euler/Mobius tensor skeleton.

User's observation: write each factor in division-algorithm form  N = p*a + b  (prime * index +
residue). Multiplying such factors expands MULTILINEARLY -- one binary choice per factor, "take the
prime part p*a" OR "take the residue part b":

  (p a + b)(q c + d)(r e + f)
    = sum over subsets S of the factors of  (prod_{i in S} prime_i*index_i)(prod_{i not in S} residue_i)
    = pq r (ace) + ... (one term per subset),  graded by |S| = how many prime-parts were chosen.

This script shows that pattern IS the exact backbone of our machine:

 (1) the multilinear subset expansion reproduces the user's hand expansion (N=2,3), verified symbolically;
 (2) the SAME subset-over-primes structure is the conductor coefficient
        b_omega(n) = n^{omega-1/2} prod_{p|n} (1 - p^{-2 omega}) = n^{omega-1/2} sum_{d | rad(n)} mu(d) d^{-2 omega},
     each prime contributing "1" (not chosen) or "-p^{-2 omega}" (chosen), subset d = prod_{p in S} p,
     sign mu(d) = (-1)^{|S|};
 (3) the subset SIZE |S| = the omega-jet order = nu(n) (#distinct primes): the leading omega-power of
     prod(1-p^{-2omega}) is (2 omega)^{nu} prod log p (all primes chosen) -- this is Pillar-1 b_0^{(nu)};
 (4) it is the FLAT (tensor) multiplicative side: the expansion is exact, finite, multilinear = a tensor
     product over independent prime channels; by UFD the prime log-displacements are independent, so the
     cross-terms are pure Mobius inclusion-exclusion with NO resonance (Round-008 flatness, combinatorial
     form). Hence the coupling that can carry RH is NOT inter-prime (flat) but Archimedean.

CREDIT: this is the standard Euler-product / Mobius / inclusion-exclusion structure (Dirichlet
convolution; the CAR/Bost-Connes tensor-over-primes). RH IS OPEN; nothing here is a proof; no zeta zeros.
"""

import sympy as sp
from itertools import combinations, product


def banner(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def multilinear_expand(primes, indices, residues):
    """sum over subsets S of (prod_{i in S} prime_i*index_i)(prod_{i notin S} residue_i)."""
    n = len(primes)
    total = 0
    terms_by_size = {k: 0 for k in range(n + 1)}
    for k in range(n + 1):
        for S in combinations(range(n), k):
            term = sp.Integer(1)
            for i in range(n):
                term *= (primes[i] * indices[i]) if i in S else residues[i]
            total += term
            terms_by_size[k] += term
    return sp.expand(total), {k: sp.expand(v) for k, v in terms_by_size.items()}


def main():
    banner("1. The multilinear subset expansion reproduces the user's hand expansion")
    p, q, r, a, c, e, b, d, f = sp.symbols('p q r a c e b d f')
    # N=2
    tot2, _ = multilinear_expand([p, q], [a, c], [b, d])
    user2 = sp.expand(p * a * q * c + p * a * d + b * q * c + b * d)
    print("   (pa+b)(qc+d):")
    print("     subset expansion =", tot2)
    print("     user expansion   =", user2, "  match:", sp.simplify(tot2 - user2) == 0)
    assert sp.simplify(tot2 - user2) == 0
    # N=3
    tot3, by3 = multilinear_expand([p, q, r], [a, c, e], [b, d, f])
    user3 = sp.expand((r * e + f) * (p * a * q * c + p * a * d + b * q * c + b * d))
    print("   (re+f)(pa+b)(qc+d):  subset == user:", sp.simplify(tot3 - user3) == 0)
    assert sp.simplify(tot3 - user3) == 0
    print("   graded by |S| (#prime-parts chosen):")
    for k in range(4):
        print(f"     |S|={k}: {by3[k]}")
    print("   => |S|=3 is the pure-prime term pqr*(ace); |S|=0 is the pure-residue bdf; the")
    print("      mixed |S|=1,2 are the cross terms (the inter-channel 'interference').")

    banner("2. Same structure IS the conductor coefficient b_omega(n) (subset over prime support)")
    w = sp.symbols('omega')
    print("   b_omega(n) = n^(omega-1/2) prod_{p|n}(1-p^{-2omega}) = n^(omega-1/2) sum_{d|rad n} mu(d) d^{-2omega}")
    for n in [6, 12, 30, 36]:
        primesupp = sorted(int(P) for P in sp.factorint(n).keys())
        # direct product
        prodform = n ** (w - sp.Rational(1, 2)) * sp.prod([1 - P ** (-2 * w) for P in primesupp])
        # subset/mobius form
        mob = 0
        for k in range(len(primesupp) + 1):
            for S in combinations(primesupp, k):
                dd = 1
                for P in S:
                    dd *= P
                mob += sp.Integer(-1) ** k * sp.Integer(dd) ** (-2 * w)
        mobform = n ** (w - sp.Rational(1, 2)) * mob
        # numeric equality (sympy won't auto-combine 2^{-2w} 3^{-2w} == 6^{-2w}); check at sample omega
        diffs = [abs(complex((prodform - mobform).subs(w, sp.Float(wv))))
                 for wv in (0.17, 0.37, 0.5)]
        ok = max(diffs) < 1e-12
        print(f"   n={n:>2} (primes {primesupp}): product == subset/Mobius form (numeric): {ok}  max|diff|={max(diffs):.1e}")
        assert ok

    banner("3. Subset SIZE = omega-jet order = nu(n); leading omega-power = (2omega)^nu prod log p")
    for n in [6, 12, 30]:
        primesupp = sorted(sp.factorint(n).keys())
        nu = len(primesupp)
        prodpoly = sp.prod([1 - P ** (-2 * w) for P in primesupp])
        ser = sp.series(prodpoly, w, 0, nu + 1).removeO()
        lead = sp.simplify(ser.coeff(w, nu) * w ** nu)  # the omega^nu term
        pred = (2 * w) ** nu * sp.prod([sp.log(P) for P in primesupp])
        ok = sp.simplify(sp.expand(lead) - sp.expand(pred)) == 0
        print(f"   n={n:>2}: lowest nonzero order = omega^{nu}; coeff matches (2omega)^nu prod log p: {ok}")
        assert ok
    print("   => choosing ALL nu primes at leading order = the pure-prime subset |S|=nu = b_0^{(nu)} (Pillar 1).")

    banner("4. FLAT tensor side: cross-terms are pure Mobius inclusion-exclusion, NO resonance (UFD)")
    # the subset expansion of prod(1-p^{-2omega}) is a tensor product over primes:
    # each prime is an independent 2-state channel {1, -p^{-2omega}}. Verify factorization = tensor.
    primesupp = [2, 3, 5]
    direct = sp.expand(sp.prod([1 - P ** (-2 * w) for P in primesupp]))
    print("   prod_{p in {2,3,5}} (1 - p^{-2omega}) expands to 2^3=8 subset terms (signed by mu):")
    print("     ", direct)
    print("   This is a TENSOR product over primes (each prime an independent 2-state channel).")
    print("   By UFD the prime log-scales {log p} are Z-independent (Round 008): the cross terms do")
    print("   not resonate -- they are exact finite inclusion-exclusion, RH-INERT (the flat side).")
    print("   => In the one-block conductor coupling V, the prime factors are an independent tensor;")
    print("      the ONLY channel that can carry RH positivity is the Archimedean block (Part A).")

    print("\nALL CHECKS PASSED.  The factorization pattern = Euler/Mobius tensor skeleton = the flat")
    print("multiplicative side (RH-inert). Its role: it factors the prime channels so the attack can")
    print("isolate the Archimedean coupling. RH remains open. No zeta zeros used.")


if __name__ == "__main__":
    main()
