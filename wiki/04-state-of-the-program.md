# 4. State of the program

*This page is the honest current picture. The numerical results are **Observed** on a
**calibrated** instrument (see [page 5](05-methodology-and-discipline.md) for what that word
buys); nothing here is a proof of anything, and the headline result is a confirmed
**null**: the target is exactly RH-equivalent, and no unconditional brick was found.*

---

## 4.1 The target, named precisely

All the reformulations of [page 2](02-the-rh-equivalent-target.md) and the semigroup of
[page 3](03-the-diophantine-semigroup-frame.md) converge on one object. On the finite-window
test space (support `L`), the completed Weil form splits as

```
Q  =  P  −  K
```

where `P` is the **archimedean + pole** part (`pole + arch + (−log π)·I`) and `K` is the
**prime semigroup** `K = Σ_n c_n (T_{log n} + T_{log n}†)/2` of [§3.4](03-the-diophantine-semigroup-frame.md).

> **The missing theorem, as a coercivity.** `Q = P − K ⪰ 0` for all admissible finite-window
> test functions.

This is not a new equivalence — it is RH wearing operator clothes. Its value is that each
piece is now something we can *measure*, and we did.

## 4.2 What the calibrated instrument measured

A completed Weil form was built on finite-window trial spaces and **calibrated** by checking
that its arithmetic side reproduces its zero side (`M_full ≡ M_zeros`) to 60 digits — i.e.
the explicit formula balances at the matrix level, which is what makes any reading
meaningful. The results (all **Observed[instrument]**, scratch-only, within the stated
boundaries of [page 5](05-methodology-and-discipline.md)):

1. **The "arch dominates primes" brick is dead — measured.** The archimedean-plus-pole part
   `P`, *with no primes in it at all*, is **not positive semidefinite** at any support tested:
   `λ_min(P)` runs `−0.08, −0.92, −1.77, −3.0, −4.9, −8.0, −16.1` for support `L_t = 0.4 … 3.0`.
   There is **no positive archimedean floor** for the primes to erode. The clean inequality
   `arch + pole ≥ ‖K‖` that would have been an unconditional proof fails, and fails wide.
   Positivity here is a *cancellation*, never a floor.

2. **The nonalignment bound holds and over-delivers.** The prime term's actual collective
   operator norm satisfies `λ_max(K) ≤ C_L < A_L` — in fact `λ_max(K) ≈ ⅓` of the worst-case
   pointwise comb mass `A_L` (ratios `0.30–0.42`), even smaller than the `C_L` bound of
   [§3.4](03-the-diophantine-semigroup-frame.md). The band-limit genuinely suppresses the
   prime term. This buy-back is real and unconditional.

3. **The full form is positive — and razor-thin.** `λ_min(Q)` is positive but **collapses
   toward zero** as resolution grows (`≈ 1e-11 → 1e-22` from support `0.8` to `1.6` at
   increasing basis size), and the band of prime-weight scale `s` for which `P − sK ⪰ 0`
   pinches to a knife around the true weight `s = 1`: `[1 − 1.8e-13, 1 + 1.8e-15]`. This is
   not a coercivity margin; it is the RH-equivalent near-cancellation, seen directly.

4. **Multiplicativity holds the knife-edge — measured.** Every mutation of the arithmetic
   drives `λ_min(Q)` **clearly negative**, roughly linearly in the perturbation: injecting a
   fake impulse at `n = 6` (where `Λ(6) = 0`), detuning `|α_2| ≠ 1`, scaling all prime
   weights, or nudging `log 2`. The form is positive **only** at the arithmetically-correct
   point and nowhere near it. So multiplicativity *is* load-bearing for the sign — but it
   balances the form **at zero**, it does not lift it to a margin, and a knife-edge poised at
   zero **is** RH-equivalence.

5. **The crossover: the off-line zero is the negative direction.** On a non-multiplicative
   control (Davenport–Heilbronn — functional equation, no Euler product), the form is positive
   at small support just like `ζ`, then first goes indefinite at support `L* ≈ 4`. The entire
   negative eigenvalue is supplied by its **single off-line zero** (height `85.699`): moving
   only that zero onto the line restores a positive form; the other off-line zeros contribute
   `≤ 1.6e-6`; a band containing no off-line zero stays positive. In the instrument,
   **positivity's sign tracks zero-location exactly** — which is Weil's criterion, made
   visible.

   The **matched-partner positive control** completes this experiment. Take `L(s, χ)` for the
   character `χ mod 5` with `χ(2) = i` — the *same* conductor 5, the *same* archimedean factor
   `Γ((s+1)/2)`, the *same* functional-equation shape as Davenport–Heilbronn, differing in
   **one** thing only: it carries an Euler product. Under the identical calibrated instrument
   it stays **PSD across the whole tested range** (`L = 0.4 … 9`), collapsing-but-positive just
   like `ζ`, at every setting where its non-multiplicative twin goes indefinite. One variable
   toggled, opposite outcome: **multiplicativity is the operative separator** between a positive
   form and an indefinite one, measured, with everything else held fixed. The caveat is exact
   and was pre-registered: `L(s, χ)` staying PSD is *itself* equivalent to GRH for that
   `L`-function — so this measures the **separator**, not a mechanism, and not a brick. Together
   with item 4's mutation controls (destroy `ζ`'s multiplicativity locally and the form cracks),
   multiplicativity is now pinned as load-bearing for the sign from **both** sides.

## 4.3 What all five say together

Every feature the frame predicted is **true and measured**: positive at small support,
primes drive toward negative, `λ_min` never crosses (it sits at the positive floor),
multiplicativity holds the sign, the off-line zero is the break. And every one of them lands
on the **same wall**: the positivity *is* RH (`M_full ≡ M_zeros`; the collapsing window; the
mutation-fragility). The frame is now mapped to the micron. It has not been crossed.

The one durable gain is a sharper target: not "find a positivity that is not there" (the
arch floor does not exist) but **prove the joint coercivity `P − K ⪰ 0` between two named,
measured, indefinite pieces.** That is still RH-hard — but it is now made of operator
estimates (well width/density versus band-limit, boundary flux, the semigroup's SOS energy)
rather than of a floor that was never real.

## 4.4 How we got here (research arc)

The program ran as several independent agent lineages that converged on one obstruction.

- **astra** — the CND / infinite-divisibility / transport attack. Finite-event rigidity; the
  geometric-prime Gaussian residual is not a characteristic function; prime-transport
  martingale and complexity-crest controls. (`research/astra_round_001..003/`.)
- **aletheia** — the adelic / affine / place-character structure. The SUCC/FUCC affine-braid
  and KMS structure, the repaired prime tower and adelic radical, `FUCC = Pascal` translation,
  the finite reduced kernel's strict positive-definiteness (the knife-edge as an asymptotic
  shrinking window), and the **unit-basepoint place-character seam** (§4.5).
  (`research/aletheia_2026-10-05/`, `_2026-10-06/`.)
- **claude** — the operator-algebra / passivity attack. The meta-theorem
  (commutative-multiplicative ⇒ factorized ⇒ RH-inert); exact local operator squares; the
  self-sieving carry machine (`B_p` as a literal carry filter, von Mangoldt as the
  carré-du-champ of carry curvature); and Round 006's clean positive theorem, the
  **Schur–Vitali limit** (`C104`): a non-circular reduction of RH to one hypothesis — a finite
  family contractive on all of `H_{1/2}` and converging to `Cayley[ξ′/ξ]` only on the safe
  Euler region `Re s > 1` forces RH. (`research/claude_round_004..006/`.)

The current session (Rounds 029–051, `CRUCIFIXION_LEDGER.md`) added the ground-up successor
frame, the archimedean Γ-from-succ construction, the Diophantine reframe, the finite-window
semigroup of [page 3](03-the-diophantine-semigroup-frame.md), the calibrated coupled-form
measurements of §4.2, and the matched-partner positive control that isolates multiplicativity
as the crossover's separator.

## 4.5 The open seams

Two concrete, still-unproven candidate architectures for the one missing theorem. Neither is
known to work; both are RH-hard and are kept precisely because they are *not* obviously
circular.

- **The joint coercivity (§4.1).** Prove `P − K ⪰ 0` unconditionally, using the semigroup's
  positive SOS energy and a boundary-flux bound against the measured-indefinite `P`. The matched
  multiplicative partner `L(s, χ)` (§4.2, item 5) has now been run and isolates multiplicativity
  as the operative separator — but that only *names* the open lever; it does not supply an
  unconditional coercivity margin, because `L(s, χ)`'s own positivity is GRH-equivalent. The
  theorem still owed is a reason `P − K ⪰ 0` that reads multiplicativity and does **not** read
  the zeros.

- **The unit-basepoint place-coupling (UBRPCT, Round 006).** The critical half-density weight
  `p^{-k/2} log p` is the *first jet* at `z = 0` of the ½-twisted adelic character
  `χ^{(1/2)}_{v,z}(x) = |x|_v^{1/2+z}`; the product formula `∏_v |x|_v^{1/2} = 1` makes the
  half-density globally balanced (the adelic "why ½"); the cross-prime coupling that
  primewise-independent constructions discard lives in the *second jets*. The seam is to build
  the global object at the unit basepoint so the divergent first-jet corrections cancel **by
  the product-formula identity before** positivity is formed, yielding a second-jet Gram with
  kernel `K_Ψ`. **Proposed architecture, UNVERIFIED**; orthogonal to the single-space de
  Branges positivity that Conrey–Li/Sarnak proved fails for `ζ`. Full statement and honest gap:
  `research/aletheia_2026-10-05/CURRENT_MISSING_THEOREM.md`, `PLACE_CHARACTER_UNIT_BASEPOINT.md`,
  `CND_PROOF_SEAM.md`, `research/claude_round_006/PROOF_ATTEMPT_006.md`.

## 4.6 The discriminator (what would count as progress)

> A result is real RH progress **iff** it *proves* a statement that was previously only
> conjectured, that statement does **not** reduce to an RH-equivalent, and its proof does
> **not** assume zero locations or Weil positivity. Any result with a load-bearing "if … then
> RH" is a relocated wall.

**Score to date: zero constructions pass.** The honest state is a precisely-shaped target
and a well-mapped graveyard — not a theorem.

---

**Next:** [Methodology & discipline →](05-methodology-and-discipline.md) — how claims are
graded, how constructions are stress-tested, and what "calibrated instrument" means.
