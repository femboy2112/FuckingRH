# Stratified SUCC/FUCC and the generator-level diagonal (seam refinement)

**Date:** 2026-10-06. **Status:** CONJECTURED / program (UNVERIFIED). **RH open.**
**Grounding:** affine braid + product-formula first-jet nullity verified exactly (inline check).

A conceptual refinement of the seam (C110/C111), from the observation that the *original* prime-clock
wiring — SUCC activating on each prime jet, the wavefront activating the `t`-action — is not a competitor
to the current source/place-character picture but the **missing gluing** between them.

## 1. The structure: SUCC is attached to every prime ray (exact)

SUCC does not merely underlie `N` while prime rays sit separately prewired. SUCC is **stratified onto
each prime family**, and the exact statement of "attach the successor-form onto the `p`-ray" is the
**affine braid**

    V_p S = S^p V_p        (verified: ||V_p S - S^p V_p|| = 0 on the safe block, p=2,3,5).

On the `p`-ray the successor acts as the `p`-fold successor: each prime family carries a *rescaled* copy
of the SUCC-`N`-backbone. The whole object is the ax+b / Bost–Connes affine monoid `N ⋊ N^×`
(repo: `SUCC_FUCC_AFFINE_KMS_THEOREM`, C97). The common unit `Ω=|1⟩` is the shared basepoint of every
stratified copy (`V_p^0 Ω = Ω`), and the Ψ-wavefront (`t`-action = log-energy `H`) threads **diagonally**
through SUCC-proper (the Archimedean place) and through each stratified prime copy at once.

## 2. The right diagonal: on the generating basis, NOT the shadow in N

This is the load-bearing distinction.

- **Shadow-in-N diagonal** = the profinite/CRT diagonal `Z ↪ ∏_p Z_p` (residues mod `p` independent
  across `p`). Round 005 (C97) proved this **factorizes → RH-inert**. Dead.
- **Generator-level diagonal** = the diagonal embedding of the *generators/places* themselves,
  `Q ↪ A_Q = R × ∏'_p Q_p`, balanced by the **product formula** `∏_v |x|_v = 1`, i.e.
  `Σ_v log|x|_v = 0` (verified exactly for several rationals). This is the live one, and it is exactly the
  unit-basepoint place-character diagonal of C110.

The stratified affine braid is the *mechanism* that realizes this diagonal: threading the single additive
worldline through every prime place simultaneously **is** the diagonal `Q ↪ A`.

## 3. What this buys: the diagonal is a SYMMETRY to project onto

The divergence that blocks us (`Σ_p M_p = ∞`, the `P^{1-σ}` near-line fluctuation of C106) is a
**first-jet** quantity, and the first jet is **product-formula-null** (`Σ_v log|x|_v = 0`, §1 check). So:

> **Organizing conjecture (UNVERIFIED).** Treat the generator diagonal (product formula / the stratified
> affine action fixing `Ω`) as a **symmetry**. Build the place-character Gram and **project onto the
> diagonal-invariant sector**. The divergent first-jet corrections live in the diagonal-*null* sector and
> are projected out *exactly* (not subtracted asymptotically); the surviving diagonal-invariant
> **second-jet** cross-place form `Σ_{v<w} log|x|_v log|x|_w` is the candidate positive Gram with kernel
> `K_Ψ`.

This is the symmetry-reduction the UBRPCT (C111) needed: positivity formed in the invariant sector, with
the exact cancellation happening *because* the divergence is symmetry-odd, not by hand.

## 4. Honest placement: this is Connes' adelic frame, re-derived — and its wall

The wavefront-intersecting-each-place picture, with the diagonal `Q^×` / product formula and positivity
of the resulting Weil distribution, is **Connes' adelic trace-formula approach** (Connes 1999, *Trace
formula in noncommutative geometry and the zeros of the Riemann zeta function*; Bost–Connes). That it was
re-derived here from the SUCC/FUCC primitives is strong triangulation — the instinct is the serious one —
but it is also the known hard frontier: Connes' framework reduces RH to exactly the positivity of the
Weil distribution (our second-jet Gram positivity), which no one has proved. So this refinement:

- **does not bypass** Weil positivity (nothing short of a proof could); it lands *on* it, in adelic form;
- **does add** two things our seam lacked: (i) the explicit finite **gluing** (the affine braid as
  stratified SUCC) that constructs the generator diagonal, and (ii) a concrete **organizing principle**
  (project the second-jet Gram onto the diagonal-invariant sector) that makes the first-jet cancellation
  *structural* and is **finite-testable**.

## 5. The finite experiment this proposes (next step)

Non-circular, mutation-sensitive, no zeta zeros:
1. Build the finite stratified affine system on `{1..N}`: `S`, `{V_p}`, shared unit `Ω`.
2. Form the second-jet place-character form from `χ^{(1/2)}_{v,z}=|x|_v^{1/2+z}` at `z=0` (first jets
   `|x|_v^{1/2}\log|x|_v`, second jets the cross-place products).
3. Define the diagonal-invariant projector `Π_diag` (product-formula / affine-fixed-`Ω` sector).
4. **Test:** (a) does `Π_diag` annihilate the first-jet divergence (the `Σ_p M_p` linear part)? (b) is the
   projected second-jet form `Π_diag G Π_diag ⪰ 0` with compression to `K_{Ψ,L}`? (c) hostile controls:
   fake prime / wrong half-density / remove Archimedean must break it.
   - If (a)+(b) hold and (c) breaks it → the first genuinely new positive object (would be a real crack).
   - If the projected form is still indefinite with growing index → the symmetry does not isolate
     positivity, and the wall is confirmed one level deeper (a sharper no-go than C106/C108).

## Ledger

New row **C112**: the stratified SUCC (affine braid `V_pS=S^pV_p`, exact) realizes the generator-level
diagonal `Q↪A` (product formula, first-jet null — verified), as opposed to the RH-inert N-shadow diagonal
(C97). Organizing conjecture: project the second-jet place-character Gram onto the diagonal-invariant
sector so the divergent first jets cancel by symmetry and the invariant second-jet form is the candidate
positive `K_Ψ`. Identified as Connes' adelic/Weil frame re-derived from SUCC/FUCC; adds the explicit
affine-braid gluing + a finite, mutation-sensitive symmetry-projection test. UNVERIFIED.
