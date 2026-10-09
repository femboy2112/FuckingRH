# 7. Methodology & discipline

*This page documents how the program keeps itself honest. The methodology is the reason the rest
of the wiki can be trusted: every claim is graded, every construction is stress-tested against
fake arithmetic, and every numerical instrument is calibrated on known answers before its novel
readings count.*

---

## 7.1 The crucifixion method

Each round of work follows one loop, recorded in `CRUCIFIXION_LEDGER.md`:

1. **Steelman** the current idea — state it in its strongest, most coherent form, naming the real
   mathematical landmark it is circling.
2. **Crucify** it adversarially against reality — compute the thing it predicts, hunt the
   counterexample, feed it fake arithmetic, find the exact point where it breaks.
3. **Log** the outcome to the ledger with an epistemic label and the boundary of what was actually
   shown. Pre-register a falsifiable prior *before* each experiment and score it on contact.
4. **Refine** from the wreckage and repeat.

The stance is **cartographer, not advocate**: the job is to map the geometry of the problem —
where the positivity is free, where it is RH-equivalent, where a route is a relocated wall — not
to manufacture a verdict. Errors (citation slips, over-claims, mis-named mechanisms) are eaten
publicly in the ledger. Three from recent rounds, kept visible as tombstones:

- a Connes–Consani mislabel ("Theorem 7.1 / archimedean place" → actually **Theorem 1 /
  prime-free window $(\tfrac12,2)$**), caught and corrected against the paper;
- a literature author error in the repo (an arXiv preprint credited to the wrong name), verified
  against the arXiv page and fixed;
- a mis-named mechanism (the symbol's well-compensation called "the functional equation" — it is
  the **positivity of the low-passed zero comb**; the conclusion survived, the mechanism was
  corrected — [§4.3](04-the-symbol-and-the-wells.md)).

## 7.2 Epistemic labels

Every claim in the repo carries exactly one status. They never silently upgrade.

| Label | Meaning |
|---|---|
| **Verified** | Re-derived independently here (second method / independent implementation). |
| **Demonstrated** | Proved, with the proof checked step by step. |
| **Observed** | Measured on a calibrated instrument or read off a sweep; *not* an independent re-derivation, and *not* a proof. |
| **[derived]** | A structural identity worked out here from proved inputs, labeled pending an independent re-derivation. |
| **Conjectured** | Induced from evidence, stated falsifiably, not proved. |
| **UNVERIFIED** | A proposed construction whose load-bearing step has not been checked. Said loudly. |
| **Refuted** | Shown false, with the counterexample kept visible (a tombstone, not a deletion). |

A numerical agreement — even to hundreds of digits — is **Observed**, never **Demonstrated**.
Accumulation does not promote a label.

## 7.3 Hostile controls (the mutation-sensitivity gate)

A construction only has RH content if it **depends on the real arithmetic**. So every candidate is
run against deliberately corrupted inputs:

- delete or insert a prime;
- use the wrong charge $\log p$ (or a random period in its place);
- use the wrong half-density $p^{-1/2}$;
- remove or perturb the archimedean boundary term;
- replace the primes with a fake, non-multiplicative set.

> **If a construction still "works" on fake arithmetic, it is RH-inert** — it was measuring the
> stage, not the shadow-succ content ([§1.6](01-the-successor-frame.md)). The coupled-form
> mutation controls (B5) and the two-sided separator (the non-multiplicative Davenport–Heilbronn
> control plus the matched multiplicative partner, C1–C3 on [page 6](06-state-of-the-program.md))
> are exactly this gate applied to the current frontier.

Known attractive dead ends that failed these controls are preserved, not hidden
(`docs/NEGATIVE_CONTROLS.md`, and §4 of `CONSOLIDATED_RH_STATE.md`).

## 7.4 The no-zero-input rule

**Zeta-zero ordinates are never used as construction input** — only as after-the-fact
diagnostics. A construction that reads the zeros to build its positivity has proved nothing (it has
assumed the answer). This is why, in the calibrated instrument, the zero side is used *only* to
confirm the explicit formula balances ($M_{\mathrm{full}} \equiv M_{\mathrm{zeros}}$, B1); the
arithmetic side — primes plus archimedean, no zeros — is the object under study. The symbol face of
[page 4](04-the-symbol-and-the-wells.md) is this rule taken to its limit: the symbol $\Psi_L$ is
built with no zeros at all, and the content of [§4.3](04-the-symbol-and-the-wells.md) is precisely
the proof that it *nonetheless* equals the (zero-defined) low-passed comb.

## 7.5 Calibrated instruments (the Instrument rule)

Code that measures mathematics is a scientific instrument, and an instrument is believed only after
it recovers a **known** answer:

- A summation / quadrature routine must reproduce a known value (e.g. $\zeta(2) = \pi^2/6$, or a
  known explicit-formula balance) before its novel outputs are trusted.
- Load-bearing values are recomputed by a **second independent implementation** (different library,
  algorithm, or precision).
- One variable changes at a time; seeds, working precision, and exact outputs are quoted, not
  rounded away.
- Boundaries are stated: what resolution/support/basis was tested, and what was *not*.

In this repo the instrument work is delegated to a dedicated experimentalist agent that holds this
rule strictly. Two gates worth naming as examples:

- The coupled-form results (group B, [page 6](06-state-of-the-program.md)) passed because the
  explicit formula balances to 60 digits — which is what licenses reading the eigenvalues as
  evidence about the *form* (while never making the zero-side check a test of RH itself).
- The matched-partner and symbol work (groups C, D) is gated on the exposed object reproducing the
  already-calibrated $M_{\mathrm{full}}$ eigenvalue before any new reading counts — and the
  diggability model is calibrated on a *known* off-line zero (Davenport–Heilbronn's $85.699$) before
  it is pointed at $\zeta$. An instrument is calibrated on the known answer first, always.

## 7.6 Reproduction

Scripts under `scripts/` reproduce the exact identities and the measured no-gos (`numpy`, `mpmath`,
`sympy`, `scipy`; see `requirements.txt`). The claim spine is `CLAIM_LEDGER.md` (rows with status +
reproduction pointer); the live narrative map is `CRUCIFIXION_LEDGER.md`; the cross-repo
consolidation is `CONSOLIDATED_RH_STATE.md`.

---

**Back to:** [Wiki index](README.md) · [1 Successor frame](01-the-successor-frame.md) ·
[2 RH-equivalent target](02-the-rh-equivalent-target.md) · [3 Diophantine & semigroup
frame](03-the-diophantine-semigroup-frame.md) · [4 The symbol & the
wells](04-the-symbol-and-the-wells.md) · [5 What ζ is, from every side](05-what-is-zeta-here.md) ·
[6 State of the program](06-state-of-the-program.md)
