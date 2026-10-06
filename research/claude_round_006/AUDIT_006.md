# Adversarial audit of Round 006 — outcome and fixes applied

**RH IS OPEN.** An independent hostile audit re-ran all five scripts, hand-re-derived the load-bearing
identities, and ran independent checks. **Verdict: no blocking issues; no file claims RH progress; RH stated
open everywhere; honest characterization/rediscovery with sharp new no-gos.** Two should-fix defects and
three phrasing nits were found and have been **fixed** (this commit). Recorded here for provenance.

## Confirmed by the audit (independently re-derived)

- All exact identities correct, correctly adjointed, honestly scoped RH-inert, truncation separated from
  genuine defects: `E_S=I−SS*=[S*,S]=|1><1|`; `Λ_op=diag Λ`; `H_log=diag(log n)`; `Π_{p,k}S̃=S^{p^k}Π_{p,k}`;
  `v_p`=survival; the affine braid; and the **exclude-0 Nica defect `S*V_p−S^{p-1}V_pS*=|p−1><1|`**. Scripts
  verify Λ/off-diagonals at exactly `0.00e+00`, `H_log` at `9e-16`, Nica `<1e-12` — genuinely tight.
- The honesty reframing of the von-Mangoldt note is thorough and correct ("novel framing of a trivial
  Bost–Connes fact, RH-inert, not progress").
- C101/C102 correctly drawn; the audit independently reproduced the intersect tables and the common-mode
  mechanism, and confirmed the strengthened C101 (prime-specificity necessary but insufficient; the sign
  structure is load-bearing).
- Literature placement correct and not overstated (`H_log` = BC Hamiltonian exactly; BC has no successor;
  Cuntz `Q_ℕ` match correctly scoped "close"; "no framework breaks the wall" defensible for the cited
  circle).

## Fixes applied

- **S1 (should-fix, RH-inert).** The local carry filter `B_p` was written with the **unit successor `S`**;
  its symbol `σ_p` lives on the **prime clock** `e^{i(log p)ξ}`, whose shift is the **prime-depth shift
  `U_p` (= `V_p` on the `p`-tower)**, not `S`. The abstract Toeplitz identity is shift-agnostic, so the
  §8a check (on `S`) did not pin the shift. **Fixed:** `B_p=(I−U_p)(I−p^{-1/2}U_p)^{-1}`; script §8
  rewritten to check the prime-depth tower (§8b) and that the two memories genuinely differ (§8c,
  `‖·‖=0.75`); the unit-successor augmentation `(I−S)*(I−S)=2I−S−S*` relabeled §8d (its own, integer-clock,
  von-Mangoldt route). Corrected in `BILATERAL_SUCC_TOEPLITZ.md`, `ROUND_RESULT.md`,
  `THEOREM_DEPENDENCY_DAG.md`, `PROOF_ATTEMPT_006.md`, and the C100 ledger row. No conclusion changes
  (local ⇒ RH-inert either way).
- **S2 (should-fix, concrete bug).** `r006_intersect_before_squaring.py` printed a stale READING (claiming
  the stratified boundary "cures the common mode / diverges only linearly") that contradicted its own table.
  **Fixed:** the READING now matches the data (stratified still grows `~π(N)/2`, total still quadratic).
- **N1.** `FRACTIONAL_SUCC_GAMMA_INTERTWINER.md §D/G` "this is **why** … the decisive conceptual result"
  softened to "the structural reading / central conceptual reading — a heuristic argument, not a theorem"
  (the sound part is the *negative* claim that the algebra reproduces `ζ` only in `Re s>1`).
- **N2.** `INTERSECT_BEFORE_SQUARING.md` "the dichotomy is complete / done correctly *is* the Weil
  distribution" scoped to the two boundary families tested and marked a conjecture/heuristic.
- **N4.** `FRACTIONAL …§F` "verified vs mpmath" corrected to "classically exact for `Re s>1`; finite
  prime-cutoff sum matches to `|diff|~6e-3` (σ=1.5) — truncation-limited."
- **N3** (direct-sum `~π(N)` vs `~2π(N)` constant looseness) left as-is: order-level and not wrong.

## Net

Round 006 stands as pushed: an honest characterization/rediscovery (Bost–Connes + Cuntz `Q_ℕ` + Connes/Tate
in exact coordinates) with three sharp new no-gos (C101/C102/C103), RH untouched. The audit changed no
conclusion; it tightened the shift labeling of `B_p`, corrected one stale script printout, and hedged three
over-confident lines.
