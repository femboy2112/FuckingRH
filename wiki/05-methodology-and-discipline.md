# 5. Methodology & discipline

*This page documents how the program keeps itself honest. The methodology is the reason the
rest of the wiki can be trusted: every claim is graded, every construction is stress-tested
against fake arithmetic, and every numerical instrument is calibrated on known answers before
its novel readings count.*

---

## 5.1 The crucifixion method

Each round of work follows one loop, recorded in `CRUCIFIXION_LEDGER.md`:

1. **Steelman** the current idea — state it in its strongest, most coherent form, naming the
   real mathematical landmark it is circling.
2. **Crucify** it adversarially against reality — compute the thing it predicts, hunt the
   counterexample, feed it fake arithmetic, find the exact point where it breaks.
3. **Log** the outcome to the ledger with an epistemic label and the boundary of what was
   actually shown.
4. **Refine** from the wreckage and repeat.

The stance is **cartographer, not advocate**: the job is to map the geometry of the problem —
where the positivity is free, where it is RH-equivalent, where a route is a relocated wall —
not to manufacture a verdict. Errors (including citation slips and over-claims) are eaten
publicly in the ledger; see the Connes–Consani correction logged for 2026-10-08 (a "Theorem
7.1 / archimedean place" mislabel caught and fixed against the paper).

## 5.2 Epistemic labels

Every claim in the repo carries exactly one status. They never silently upgrade.

| Label | Meaning |
|---|---|
| **Verified** | Re-derived independently here (second method / independent implementation). |
| **Demonstrated** | Proved, with the proof checked step by step. |
| **Observed** | Measured on a calibrated instrument or read off a sweep; *not* an independent re-derivation, and *not* a proof. |
| **Conjectured** | Induced from evidence, stated falsifiably, not proved. |
| **UNVERIFIED** | A proposed construction or claim whose load-bearing step has not been checked. Said loudly. |
| **Refuted** | Shown false, with the counterexample kept visible (a tombstone, not a deletion). |

A numerical agreement — even to hundreds of digits — is **Observed**, never **Demonstrated**.
Accumulation does not promote a label.

## 5.3 Hostile controls (the mutation-sensitivity gate)

A construction only has RH content if it **depends on the real arithmetic**. So every
candidate is run against deliberately corrupted inputs:

- delete or insert a prime;
- use the wrong charge `log p` (or a random period in its place);
- use the wrong half-density `p^{-1/2}`;
- remove or perturb the archimedean boundary term;
- replace the primes with a fake, non-multiplicative set.

> **If a construction still "works" on fake arithmetic, it is RH-inert** — it was measuring
> the stage, not the shadow-succ content ([§1.6](01-the-successor-frame.md)). The
> coupled-form mutation controls on [page 4](04-state-of-the-program.md) are exactly this gate
> applied to the current frontier: the form's positivity breaks under every arithmetic
> mutation, which is what certifies it is tracking real multiplicativity and not an artifact.

Known attractive dead ends that failed these controls are preserved, not hidden
(`docs/NEGATIVE_CONTROLS.md`, and §4 of `CONSOLIDATED_RH_STATE.md`).

## 5.4 The no-zero-input rule

**Zeta-zero ordinates are never used as construction input** — only as after-the-fact
diagnostics. A construction that reads the zeros to build its positivity has proved nothing
(it has assumed the answer). This is why, in the calibrated instrument, the zero side is used
*only* to confirm the explicit formula balances (`M_full ≡ M_zeros`); the arithmetic side —
primes plus archimedean, no zeros — is the object under study.

## 5.5 Calibrated instruments (the Instrument rule)

Code that measures mathematics is a scientific instrument, and an instrument is believed only
after it recovers a **known** answer:

- A summation / quadrature routine must reproduce a known value (e.g. `ζ(2) = π²/6`, or a
  known explicit-formula balance) before its novel outputs are trusted.
- Load-bearing values are recomputed by a **second independent implementation** (different
  library, algorithm, or precision).
- One variable changes at a time; seeds, working precision, and exact outputs are quoted, not
  rounded away.
- Boundaries are stated: what resolution/support/basis was tested, and what was *not*.

In this repo the instrument work is delegated to a dedicated experimentalist agent that holds
this rule strictly (calibration gate first, second-implementation cross-checks, explicit
boundaries). The coupled-form results on [page 4](04-state-of-the-program.md) passed the gate
— the explicit formula balances to 60 digits — which is precisely what licenses reading the
eigenvalues as evidence about the *form* (while never making the zero-side check a test of RH
itself).

## 5.6 Reproduction

Scripts under `scripts/` reproduce the exact identities and the measured no-gos (`numpy`,
`mpmath`, `sympy`, `scipy`; see `requirements.txt`). The claim spine is
`CLAIM_LEDGER.md` (rows with status + reproduction pointer); the live narrative map is
`CRUCIFIXION_LEDGER.md`; the cross-repo consolidation is `CONSOLIDATED_RH_STATE.md`.

---

**Back to:** [Wiki index](README.md) · [The successor frame](01-the-successor-frame.md) ·
[The RH-equivalent target](02-the-rh-equivalent-target.md) · [The Diophantine & semigroup
frame](03-the-diophantine-semigroup-frame.md) · [State of the program](04-state-of-the-program.md)
