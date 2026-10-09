# Provenance — "The shattered teacup: reversing SUCC is not reversing time" (external)

**Origin:** supplied by the user 2026-10-09 as a single pasted **ChatGPT** text (`ARTIFACT.md`), under
the prompt "go full blast on any threads this could pull loose." **No code was shipped** (the artifact
reports its own numerics as "I verified this" / "I checked this algebraically"; nothing executable
accompanied it). This is a **different provenance** from the aletheia sibling-lineage zips of R60–62
(`../dlewc_2026-10-09/`, `../boundary-curvature_2026-10-09/`, `../arithmetic-poisson_2026-10-09/`) and is
deliberately **not** folded into this repo's "sibling-lineage triangulation" bearing count
(Aletheia: factor shared provenance before counting independent bearings — and a distinct source is a
distinct bearing only if it is not re-deriving the same object, which here it is).

**Status in this repo:** archived for provenance only. Scored in `CRUCIFIXION_LEDGER.md` **Round 63**.

**Independent verification:** every load-bearing claim re-derived on my own instrument,
`/tmp/.../scratchpad/independent_verify4.py` (my own log-coordinate grid operators + mpmath Mellin
quadrature — a second blind path, not a re-run of anything). Instrument calibrated first (R²=I,
norm-preservation, conjugate-linearity, translation unitarity, T†=T₋ₘ — all `0.00e+00`). **No bugs this
round.**

**Independent verdict (what reproduced):**
- **No zeros read:** confirmed. No code shipped; the text uses no zero ordinates — every "reverse" is an
  operator reversal, not a zero table.
- **Exact identities (all verified on my instrument):** `R²=I`; `R U_n R = U_n⁻¹` (`0.00e+00`);
  `R X R = −X` (`0.00e+00`); `M(Rf)(½+it)=conj(Mf(½+it))` (`2e-31`, mpmath, calibrated on
  `Mf=Γ(s+α)`); `R Θ_a R = Θ_a†` for genuine `χ` **and** Davenport–Heilbronn alike (`0.00e+00`, with
  `‖Θ−Θ†‖=0.71, 0.50 ≠0`); the shadow-return defect `Ω_P=PAQBP=PABP−(PAP)(PBP)` on random `A,B,P`
  (`2.7e-15`). The boundary-leakage `A†A+E†E=I` and the compressed-shift / chirality / Möbius-vs-adjoint
  facts are exact and elementary.
- **KEY STRUCTURAL FACT (derived + verified):** in log coordinates `x=e^u`, `h(u)=e^{u/2}f(e^u)` (a
  unitary map to `L²(ℝ,du)`), `R h(u)=conj(h(−u))` — i.e. `R` is **literally parity∘conjugation**, the
  R62 antiunitary `𝒥`, and on `Re(s)=½` it is the **functional-equation reflection** `s↔1−s`. So the
  artifact's "canonical Mellin reversal" is the R62 boundary-curvature tombstone re-derived from
  time-reversal — **common-mode**, not a new bearing.
- **Its own falsifier, confirmed:** `R Θ_a R=Θ_a†` holds identically regardless of coefficients ⟹
  reversal symmetry is **sign-blind** (DH, with off-line zeros, satisfies it) ⟹ "time reversal ⇏ Weil
  positivity." The artifact states this; I verified it.

**The unification (what this artifact actually contributes):** its three distinctions map onto three
walls this repo already owns, now seen as one from a reversibility angle —
(1) "full dynamical time reversal" = Hilbert–Pólya unitarity / self-adjoint realization of the completed
generator (R59; `wiki/08` xp-lens);
(2) the Mellin reversal `R` = the R62 FE-reflection tombstone (`wiki/06` F2);
(3) the "shadow-return defect" `Ω_P` = Feshbach/Schur-complement off-diagonal = "no archimedean floor"
(`wiki/06` F4).
**RH ⟺ the completed arithmetic evolution is reversible (unitary); the prime-window irreversibility is
only apparent — an artifact of premature projection.** The leakage norm `‖Ef‖²` would give `Q⪰0` iff the
completed evolution is unitary = RH. A clean reformulation of the positivity as a reversibility
statement; **no new content**, and the sign still has to come from the arithmetic source through the
completion = the **fourth gate**, not from `R`.

**Inert / not new:** the bare `Ω_P` is a universal algebraic identity (holds for arbitrary `A,B,P`),
hence RH-inert. The one cheap falsifier it earns: the cross-atom cancellation at `log(p/q)`, `log(pq)` is
a necessary condition checkable for any proposed coupling without knowing the right one — a sharpened
mutation control, not a path to the sign.

**Not attempted (no false proofs):** the proposed "first discriminating probe" (derive the candidate
pairing by choosing the oriented coupling and compare to the Weil formula) = fabricating the fourth-gate
operator = the open theorem itself. Refused, as in R59/R62.

**Bottom line:** not a brick and not a new route — a vivid thermodynamic re-derivation that **unifies
three walls as one reversibility wall**, with the R62 tombstone shown to be the **functional equation
itself** and reversal symmetry verified **sign-blind**. **RH/GRH open.**
