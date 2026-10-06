# Round006 ckpt2 — scope corrections to two Round005 overstatements

**Date:** 2026-10-06. **Status:** DISCLOSED (meta). **RH open.** These narrow the *readings* of C98/C99
before Round006 builds on them. No prior finding is retracted; three universal-sounding corollaries are
downgraded to their actual (narrower) content. Ledger rows C100, C101, C102.

## 1. C98 is about ONE mechanism, not all algebraic renormalization  (→ C100)

**What C98 actually proved.** On the real frequency axis `sigma_p(0)=0` exactly for every prime (to
`5e-14`). Therefore there is **no duplicated coarse/DC channel** across primes to telescope, and the
specific *shared-nonzero-DC positive multiresolution* mechanism that Round005 hoped would renormalize
`sum_p M_p ~ 2 sqrt(e^L)` **cannot exist**. The divergence is bulk (`xi != 0`), and its only renormalizer
is the indefinite imaginary-frequency pole (C83) acting by analytic continuation.

**The overstatement.** The old "Next" cell read: *"algebraic Hilbert structures cannot do it."* That is
too strong. C98 refutes a **single** algebraic mechanism (a shared low-pass/DC band common to all primes,
subtracted by a wavelet/MRA projector). It says nothing about a **coupled** renormalization in which the
prime rays are wired to a common source and the global response is formed by **elimination**
(Schur complement / Weyl function) rather than by **summation of pre-squared local pieces**. A
Schur-complement renormalization is not a telescoping of a shared band; it is a different operation, and
C98's `sigma_p(0)=0` argument does not touch it.

**Corrected reading (C100).** *The specific shared-nonzero-DC telescoping mechanism is dead. Whether a
coupled source-port algebraic renormalization can reproduce the completed response with manifest
positivity is open — and is the Round006 target.*

## 2. The carry carré-du-champ gives the REPAIRED, WEIGHTED local energy — not raw Λ  (→ C101)

**What C99 actually established.** `CARRY_m^* CARRY_m = (2I - S - S^*) (x) |m-1><m-1|` is the high-pass
innovation energy of the carry channel. To recover the local spectral density `sigma_p` (C90) one must
then apply:
- the **charge** weight `log p` (per prime);
- the **half-density / depth** weights `p^{-k/2}` along the tower (the Haar-cylinder metric, C96);
- the **Green/repair** step that turns the bare high-pass difference into the repaired tower resolvent.

Only after all three does `carré -> sigma_p`. The script `carre_selfsieve.py` carries these weights
explicitly; they are **load-bearing**.

**The overstatement.** Casually writing "carré-du-champ of carry = von Mangoldt event measure" invites
reading `Lambda`-measure `= CARRY^* CARRY` with no dressing. False: the raw carré is a flat
nearest-neighbour Dirichlet form on the depth chain; `Lambda` and its critical weight `Lambda(n)/sqrt n`
appear only through the `(log p, p^{-k/2})` dressing + Green repair.

**Corrected reading (C101).** *The carré generates the LOCAL repaired prime-tower Dirichlet/high-pass
energy; `sigma_p` is reconstructed after half-density/depth weighting and the Green/repair step. "Carré =
Λ" always carries the silent qualifier "repaired and weighted."*

## 3. Birth-order kernel-invariance ≠ history spaces are irrelevant to a factorization  (→ C102)

**What C99 actually established.** Discovering the primes in any order (causal self-sieve vs a static
prime set) yields the **same** endpoint kernel `K_Psi`. So for the KERNEL, birth-order is RH-inert.

**The overstatement.** This was read as "causal/history spaces don't matter." But a **factorization**
`K = B^* B` lives upstream of the kernel: equality of endpoint Grams does **not** imply equality of the
parent Hilbert spaces that produce them. A quotient/conditional-expectation map can collapse an
orthogonal, phase-coherent **history** parent onto exactly the same Gram as a smaller commutative parent
(Round005 itself showed conditional expectation killing carry curvature — C97 — which is the same
phenomenon: the quotient loses structure the parent had). So two different parents, one of which carries
cross-phases the other lacks, can share the kernel.

**Corrected reading (C102).** *Endpoint kernel equality under reordering does not make the causal history
space `H_hist` irrelevant to the search for a non-circular factor `B`. The history-before-quotient
construction (Round006 §14) is a live, genuinely distinct factorization channel: couple-before-quotient
and quotient-before-couple are different parents that may differ exactly in the positivity-bearing
cross-terms, even when they project to the same `K_Psi`.*

## Consequence for Round006

All three corrections **open** space the Round005 wrap-up had prematurely closed:
1. coupled (Schur/colligation) renormalization is not excluded by C98;
2. the local carré is a genuine positive object but only after weighting — so a GLOBAL positive object,
   if it exists, needs the weights wired in at the coupling, not bolted on after;
3. the history parent is a legitimate place to look for the missing cross-phase positivity.

These are the three doors Round006 walks through. RH remains open.
