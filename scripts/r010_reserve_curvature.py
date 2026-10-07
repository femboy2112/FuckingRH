#!/usr/bin/env python3
r"""
Round 010 / Part A -- ATTACK: Psi(t) >= 0 as "Archimedean curvature reserve dominates the prime ramp".

Suzuki (JLMS 2023, Thm 1.7): RH <=> Psi(t) >= 0 for all real t, where (even, Psi(0)=0)

  Psi(t) = A(t) - P(t),
  A(t) = 4(e^{t/2}+e^{-t/2}-2)  +  (t/2)(psi(1/4)-log pi)  +  (1/4)(C - e^{-t/2} LerchPhi(e^{-2t},2,1/4)),
         C = pi^2 + 8*Catalan                                         [smooth Archimedean reserve]
  P(t) = sum_{n<=e^t} (Lambda(n)/sqrt n) (t - log n)                   [prime ramp, convex p.w.-linear]

This is the frontier's "route 3" / the Round-008-009 curvature statement, kept in ONE BLOCK (never
estimate P by absolute value -- that destroys the cancellation; cf frontier WEIL_PRIME_RAY).

Curvature form: Psi(0)=Psi'(0)=0 (even), so  Psi(t) = int_0^t (t-s) Psi''(s) ds  with
  Psi''(s) = A''(s)  -  sum_n (Lambda(n)/sqrt n) delta(s - log n)
           = [smooth positive Archimedean curvature]  -  [prime impulse train].
So RH <=> the accumulated Archimedean curvature dominates the accumulated prime impulses, time-weighted.

THE EXACT RESULT of this attack (verified below, no zeta zeros used as input):
  A(t) and P(t) BOTH grow like 4 e^{t/2} = 4 sqrt(X), X=e^t, and UNCONDITIONALLY (by the Prime Number
  Theorem: sum_{n<=X} Lambda(n)/sqrt n ~ 2 sqrt X) the ENTIRE O(sqrt X) leading reserve cancels the
  ENTIRE O(sqrt X) prime ramp, leaving a remainder that is o(sqrt X). In the computed range (t<=12) that
  remainder Psi=A-P is small (~0.03-0.06). CAVEAT (RH-equivalent, NOT a theorem): the remainder being
  BOUNDED and POSITIVE for ALL t is itself equivalent to RH -- an off-line zero rho=beta+i gamma, beta>1/2,
  makes Psi grow like e^{(beta-1/2) t} and go negative. The leading O(sqrt X) cancellation is PNT; the
  remainder is the Archimedean continuation content (the Weil wall). The prime ramp P is a monotone
  nonnegative sum (Part B factors each conductor coefficient b_omega(n), NOT P, into a prime tensor).

Zero-side equivalence (STATED, not used as input): Psi(t) = sum_gamma (1 - cos(gamma t))/gamma^2, which
is >= 0 iff every gamma is real (= RH). We compute Psi ONLY from the prime side.

CREDIT: Suzuki 2023 (Thm 1.7); the screw/Weil form (Weil 1952, Bombieri 2000); frontier route 3. RH IS OPEN.
"""

import os
import sys
import math
import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from suzuki_psi import psi_suzuki, prime_power_events_up_to, active_horizon  # noqa: E402

mp.mp.dps = 30
PSI_D, LOGPI, CATALAN = float(mp.digamma(mp.mpf(1) / 4)), float(mp.log(mp.pi)), float(mp.catalan)
C_CONST = float(mp.pi ** 2) + 8 * CATALAN
GAMMA_LINEAR = 0.5 * (PSI_D - LOGPI)


def archimedean(t):
    """A(t): the smooth Archimedean reserve (no primes)."""
    tt = abs(t)
    pole = 4 * (math.exp(tt / 2) + math.exp(-tt / 2) - 2)
    glin = tt * GAMMA_LINEAR
    lerch = 0.25 * (C_CONST - math.exp(-tt / 2) * float(mp.lerchphi(math.exp(-2 * tt), 2, mp.mpf(1) / 4)))
    return pole + glin + lerch


def lambda_sieve(X):
    """von Mangoldt Lambda(n) for n<=X via smallest-prime-factor sieve."""
    X = int(X)
    spf = list(range(X + 1))
    i = 2
    while i * i <= X:
        if spf[i] == i:
            for j in range(i * i, X + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    Lam = [0.0] * (X + 1)
    for n in range(2, X + 1):
        p = spf[n]
        m = n
        while m % p == 0:
            m //= p
        if m == 1:
            Lam[n] = math.log(p)      # n is a prime power
    return Lam


def prime_ramp(t, Lam):
    X = int(math.exp(t))
    s = 0.0
    for n in range(2, X + 1):
        if Lam[n]:
            s += (Lam[n] / math.sqrt(n)) * (t - math.log(n))
    return s


def banner(x):
    print("\n" + "=" * 80 + "\n" + x + "\n" + "=" * 80)


def main():
    banner("1. Decomposition Psi = A - P (A, P computed separately; cross-check vs suzuki_psi)")
    print("   (suzuki_psi returns the same Suzuki closed form; this is a transcription cross-check of the")
    print("    A/P split, NOT an independent validation of the formula.)")
    Lam = lambda_sieve(math.exp(5.2))
    for t in [1.0, 2.0, 3.0, 5.0]:
        A = archimedean(t)
        P = prime_ramp(t, Lam)
        evs = prime_power_events_up_to(active_horizon(mp.mpf(t)))
        psi = float(psi_suzuki(mp.mpf(t), dps=30, events=evs))
        print(f"   t={t:>4}: A={A:>12.6f}  P={P:>12.6f}  A-P={A-P:>10.6f}  Psi(suzuki)={psi:>10.6f}  diff={abs((A-P)-psi):.1e}")
        assert abs((A - P) - psi) < 1e-4

    banner("2. Curvature form: A''(s)>0 for s>=log2 (where primes live); A''<0 on (0,0.281)")
    print("   Psi(t) = int_0^t (t-s)[A''(s) - sum_n (Lambda/sqrt n) delta(s-log n)] ds.")
    print("   A'' changes sign at s~0.2812 (A''<0 on (0,0.281), the PRIME-FREE region before the first")
    print("   impulse at log2~0.693); A''>0 for ALL s>=log2, so the curvature-vs-impulse competition")
    print("   lives in the bulk s>=log2 where A''>0. (Near 0, prime-free, A has a t*log t corner.)")
    def A_mp(t):  # mpmath Archimedean reserve (for the analytic 2nd derivative)
        t = mp.mpf(t)
        return (4 * (mp.e ** (t / 2) + mp.e ** (-t / 2) - 2) + t * mp.mpf(GAMMA_LINEAR)
                + mp.mpf(1) / 4 * (mp.mpf(C_CONST) - mp.e ** (-t / 2) * mp.lerchphi(mp.e ** (-2 * t), 2, mp.mpf(1) / 4)))
    for s in [0.05, 0.1, 0.2, 0.2812, 0.3, 0.5, math.log(2), 1.0, 2.0, 4.0]:
        App = float(mp.diff(A_mp, mp.mpf(s), 2))  # analytic 2nd derivative (mpmath)
        tag = "(<0: prime-free region)" if App < 0 else "(>0)"
        print(f"   A''({s:.4f}) = {App:>12.6f}  {tag}")
        if s >= math.log(2):
            assert App > 0            # A''>0 throughout the region where prime impulses occur

    banner("3. THE ATTACK PAYOFF: A ~ 4 e^{t/2} and P ~ 4 e^{t/2} cancel; remainder Psi is o(sqrt X)")
    print(f"   {'t':>4} {'X=e^t':>10} {'A(t)':>12} {'P(t)':>12} {'A/(4e^{t/2})':>13} {'P/(4e^{t/2})':>13} {'Psi=A-P':>10}")
    for t in [4.0, 6.0, 8.0, 10.0, 12.0]:
        Lt = lambda_sieve(math.exp(t) + 1)
        A = archimedean(t)
        P = prime_ramp(t, Lt)
        lead = 4 * math.exp(t / 2)
        print(f"   {t:>4} {math.exp(t):>10.0f} {A:>12.3f} {P:>12.3f} {A/lead:>13.5f} {P/lead:>13.5f} {A-P:>10.5f}")
    print("\n   => BOTH A and P -> 4 e^{t/2} (ratios -> 1): UNCONDITIONALLY (PNT) the entire O(sqrt X)")
    print("      leading reserve cancels the entire O(sqrt X) prime ramp. The remainder Psi=A-P is")
    print("      o(sqrt X); in this range (t<=12) it is ~0.03-0.06. Its BOUNDEDNESS and POSITIVITY for")
    print("      ALL t are each RH-equivalent (NOT shown here): an off-line zero beta>1/2 makes Psi grow")
    print("      like e^{(beta-1/2)t} and go negative. The O(sqrt X) cancellation is PNT (Part B flat side).")

    banner("4. The exact reduction + the zero-side equivalence (zeros NOT used as input)")
    print("   Prime-side (computed above, no zeros):  Psi(t) = A(t) - P(t).")
    print("   Zero-side (equivalence, stated only):   Psi(t) = sum_gamma (1 - cos(gamma t))/gamma^2,")
    print("                                           >= 0  <=>  every gamma real  <=>  RH.")
    print("   So the attack REDUCES RH to: the remainder A-P stays bounded-and->=0 for all t.")
    print("   The prime ramp P is a MONOTONE NONNEGATIVE sum (NOT a tensor; Part B factors each conductor")
    print("   coefficient b_omega(n), not P) -- it has no internal sign cancellation, so the obstruction")
    print("   is in the A-P BALANCE (the Archimedean continuation, C103/Weil wall), not re-organizing")
    print("   primes. The one-block A-P must NOT be split (|.|-estimating P loses the 4 sqrt(X)")
    print("   cancellation and the bound becomes vacuous).")

    banner("5. HONEST WALL")
    print("   This attack is an EXACT reduction + the sharp UNCONDITIONAL leading-cancellation fact (PNT),")
    print("   NOT a proof. A-P bounded-and->=0 for all t is Suzuki Thm 1.7 = RH. The O(sqrt X) cancellation")
    print("   is PNT; the remainder's boundedness/positivity is the analytic-continuation / Weil-positivity")
    print("   content, not supplied by the (per-n flat) prime combinatorics. Conrey-Li 2000 refuted the de")
    print("   Branges positivity route.")
    print("\nALL CHECKS PASSED.  Exact reduction; no RH progress; RH remains open. No zeta zeros used as input.")


if __name__ == "__main__":
    main()
