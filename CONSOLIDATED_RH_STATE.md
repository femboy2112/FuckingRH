# CONSOLIDATED RH STATE — cross-repo, 2026-10-07

**What this is.** A read-only consolidation of *every* RH-relevant fact across all math repos on this
machine, graded by epistemic status, deduped by provenance. It answers one question: **what do we
actually HAVE toward a proof of the Riemann Hypothesis, and what is missing?** It supersedes
`CURRENT_STATE.md` for that question only (that file is Round-006-stale; see §6). Produced by a
read-only four-bearing sweep (FuckingRH guts, IPromiseImNotCrazy, SmartAlgebra, adjacent repos).

**Bottom line.** RH is OPEN. There is **no (B)-gold brick** — no proved, unconditional, non-RH-equivalent
result that bridges to Weil positivity — in any repo. What exists is a complete classical toolkit (A), a
handful of genuine but *local* lemmas (B-local), and a well-mapped graveyard of dead routes (D). The one
missing object is a **new theorem**, not a recombination of what's here (§5).

---

## 0. Provenance — it is ONE corpus, not independent witnesses

The three "RH repos" are a single program, same author, same agent/napkin pipeline, same literature,
same wall. They must **not** be counted as independent triangulation.

- `FuckingRH` (origin on github, from 2026-10-05) — the live program; 40+ branches, Rounds 001–010.
- `SmartAlgebra` — separate repo, but `FuckingRH/upstream/SmartAlgebra/*` are **byte-identical imports**
  of it (`H009_…RESULT.md` diffed SAME). The function-field/Hodge source. `Verified`.
- `IPromiseImNotCrazy` — the **older ancestor lab-notebook** (2026-08-24…28, no remote). 0 files
  md5-identical to FuckingRH, but FuckingRH's archive cites its `SCHRODINGER_ARCHIMEDEAN_DOSSIER` as
  source `[I1]`. Upstream INPUT, not a copy. `Verified`.
- `fine-man` (GR/QM physics — "Riemann" = curvature tensors), `collatz-src` (Collatz; self-declares *no*
  RH relevance), `ProjectEULER` (agent plugin): **adjacent-irrelevant, zero transferable RH content.**
  `Verified`.

---

## 1. The invariant wall (every repo, every round, converges here)

> **Independent, non-circular positivity of the Weil form `W(g⋆g̃) ≥ 0` at the prime–archimedean
> interface** — equivalently, a verified "square host" for `Spec ℤ` carrying an intersection/Gram
> identity with Hodge-index positivity.

Everything positive in the corpus flows *through the zeros* or *through Weil purity as an input*. **No
object anywhere establishes positivity without already standing on the completed Weil form / zero data.**

---

## 2. (A) The toolkit we have — classical, the giants' shoulders

Strong and essentially complete as *equivalences and tools*:

- Weil positivity ⟺ RH (the proof gate). Explicit formula. Tate local/Archimedean dictionary.
- Suzuki `Ψ(t) ≥ 0 ∀t ⟺ RH`; Schur–Vitali reduction (C104: contractivity on all `H_{1/2}` + Euler-region
  convergence ⟹ RH). Nakamura–Suzuki `e^{-Ψ}` infinite-divisibility ⟺ RH.
- de Bruijn–Newman: RH ⟺ `Λ = 0` (Rodgers–Tao `Λ ≥ 0`). Li criterion. Jensen–Pólya/Turán
  (Griffin–Ono–Rolen–Zagier).
- Connes–Consani **Theorem 1** (unconditional positivity *only* for test functions with
  `supp(g⋆g*) ⊂ (1/2,2)` — the **prime-free window**, via the Sonin space / Toeplitz Thm 6.11, Yoshida;
  **NOT** "positivity at the archimedean place" — that was a mislabel, corrected 2026-10-08 R37 against the
  paper, arXiv:2006.13771); CCM prolate operator;
  Connes–van Suijlekom **conditional** ground-state theorem. Rudnick–Sarnak support budget.
- Alpöge–Furman (arXiv:2608.13637): ≥2/3 of zeros simple and on the line. (Lives only in
  `archive/legacy/RH_MASTER_DOSSIER_10_TRIANGULATIONS.md:1784`; absent from docs/README — surface it.)
- Function field: Weil RH for curves, Hodge index on `C×C`, Bombieri criterion, Castelnuovo–Severi/Rosati.

---

## 3. (B) Genuine unconditional results we OWN — all LOCAL, none bridges to Weil

Two items previously over-credited as the "bricks" are **demoted** after the adversarial dig:

- ~~Round-010 `O(√X)` cancellation of `A` vs `P`~~ → **(A), PNT-strength.** It is partial summation of
  `ψ(x) ~ x`; `A,P ≈ 4e^{t/2}`. The remainder `Ψ = A−P` (0.035, 0.048, 0.031, 0.062, 0.029 at
  `t=4,6,8,10,12`) being bounded/`≥0` is **RH-equivalent, not shown**. `Observed[dig]`.
- ~~Finite cubical Hodge–Riemann positivity~~ → **(A)/trivial.** `Q_L = C_L·Σ_v λ_v(q)²` is a positively-
  weighted sum of squares on a hyperplane; the doc's own §9 admits the Weil form is **not** `Σ‖λ_v f‖²`.
  `Observed[dig]`.

Genuinely proved, unconditional, non-equivalent — but each is *local* and does not cross the interface:

- **`C57`** (`astra_round_002/PRIME_TOWER_AUDIT.md §2`): `D_p(t)=ℓΣ r^k·min(|t|,kℓ)` is CND with an explicit
  interval Gram; the linear repair is sharp (`c|t|−h_p` CND iff `c ≥ M_p`).
- **`C90`**: closed-form `σ_p ≥ 0`. Proved lemmas `C51, C53, C59, C62, C63, C67, C87`.
- **`CRITICAL_SUZUKI_STRICT_CONTRACTION.md`** (unmerged; on cubical/mellin/succ-loop branches): the only
  real functional analysis — `‖H_{1/2,a}‖ < 1` for `a > 1`, resting on Suzuki Lemma 4.1 + a support
  lemma. **Partial** contraction; the gap to C104 is all of `H_{1/2}` (the `a → 1` / full-space edge).
  `Observed[dig], not re-derived`.
- `A''` sign-change at `s ≈ 0.2812` (`A'' > 0` iff `e^{3t}−e^{t} > 1`) — correct, trivial. `Verified[dig]`.

---

## 4. (D) The no-go graveyard — the real asset (do NOT re-walk these)

Consolidated across all bearings:

- Global pointwise Gaussian transport (two-prime image goes negative). Positive Fourier self-duality ⟹ RH.
  Canonical Gaussian quotient → `e^{-Ψ}` (C38). Impedance/Laplace completion (killed: `inf Re F_P → −∞`).
- Fixed-index Krein escape; colligation / history-before-quotient escapes (closed by parent-independence,
  Conrey–Li/Sarnak). de Branges positivity → the `Ψ` remainder (Conrey–Li 2000).
- Barycentric tower-moment matching (R003); martingale coupling of transport marginals (R002, impossible).
- Higher-moment inertia lever; sign-of-`κ₄` route; SOS square-completion (the "U/2 tax" certified);
  Lee–Yang; operator sieve / parity decoy; directed-sign (grid artifact); banded commutant / prolate
  symmetry (generic); Baker seam; "Euler-into-strip = Mertens = RH"; "finite `e0 > 0` extrapolates"
  (artifact **retracted**); resolvent-blindness `(−1)ⁿ R_Ξ⁽ⁿ⁾ > 0` for `n ≤ 21` (RH-independent).

---

## 5. What is NOT anywhere — the missing brick, precisely shaped

The corpus has, for `Spec ℤ`, **no** verified square host: the `RH_BRIDGE.md §3` rungs read Gram identity
**"not supplied"**, Hodge-index positivity **"Open"**, finite decision **"breaks"** (infinite zero set, no
`n = 2g`). The margin is *collapsing*: the numerical semi-local positivity margin `e0` shrinks
`4.94e-7 → 3.05e-7` as primes are added, and the CvS ground-state isolation gap collapses
super-exponentially (`Observed[IPromiseImNotCrazy S114–S115]`). So **no asymptotic/approximate method can
reach it** — it needs an exact identity or a structural positivity theorem.

**Why consolidation cannot produce the proof (meta-theorem).** Every non-local object in the corpus is
either (A) classical, (C) an RH-*equivalence*, or (D) a no-go. A bound on any RH-equivalent remainder
*is* RH (the remainder's worst excursion scales like `e^{(Θ−½)t}`, `Θ = sup Re ρ`; any sub-exponential
collar forces `Θ = ½`). Equivalences and local lemmas are **closed under recombination** — they cannot
manufacture the one thing absent: an *external* positivity not routed through the zeros. The missing
input is a **new theorem**, not a merge.

---

## 6. Corrections the live blast MUST apply (main carries refuted / mislabeled claims)

The ledger is stale and partly wrong — treat these as blocking before building further:

1. **`C108` FALSE as stated** (`CURRENT_STATE.md:12-13`): "RH ⟺ `Re{ξ(s)/ξ(s+1)} ≥ 0` on `Re s>½`" is
   **refuted** — `Re[ξ/ξ(·+1)] = −0.000131957` at `s=1+282i` (`Verified`, independent mpmath; also the
   repo's own `astra_round_007/PARENT_AUDIT.md`). (Nag: magnitude at `0.55+110i` reads `−0.0418`, vs
   `−0.161` quoted in C108 — same sign, different magnitude; the ledger number is itself off.)
2. **`C106` mislabel** (`scripts/finite_completion_index.py`): claimed "unconditional `max|Re F_P| ~
   P^{1−σ}`"; measured `6.83, 9.29, 11.21, 13.20` is `~ log P`, **not** a power; the "Pontryagin index" is
   an excursion count on one line (`σ=0.51, t≤300`) and its stated scope is equivalent to **not-RH**.
   `Observed[dig]`.
3. **`C105` over-claim**: `½ψ(s/2)` called "passive" but equals `−γ/2 < 0` at `s=2`; C107's "every natural
   realization indefinite" is over-extended. `Observed[dig]`.
4. **LIVE RH-leak** on `claude/stratified-diagonal-007`: ledger `C114` asserts "`Ψ` is bounded" while its
   own `C113` says bounded ⟺ RH. `AUDIT_010` fixed this leak **only** on the `…-008` branch. Unfixed here.
5. **Stale/colliding ledger**: main says "all lineages merged / no loose threads" (`04ca37c`) but carries
   **0** files from `astra_round_007/008` or `claude_round_007–010` and only 6 from `aletheia_2026-10-06/07`;
   live branches are 15–97 commits ahead; **ledger IDs `C104–C133` denote different claims on different
   branches.** The ID space has collided — any cross-branch citation by number is unsafe.
6. **`H-009` is not a bridge**: `upstream/SmartAlgebra` H-009 is function-field plumbing (its own doc:
   "carries NO number-field RH implication"); `CURRENT_STATE §17` slightly over-reads it.
7. **Script hygiene**: `completed_shift_diagnostic.py:2` loads an uncommitted `/tmp/.../zeros300.npy`;
   `pascal_innovation_gram.py:66` uses `zetazero` (honestly a circular no-go, C86); 9 tests need
   `python-flint` (not installed), 52 others pass.

---

## 7. The discriminator — what would actually count as progress

> A branch is real RH progress **iff** it *proves* a statement that was previously only Conjectured, AND
> that statement does **not** reduce to an RH-equivalent, AND its proof does **not** assume zero locations
> or Weil positivity. Any result doc containing a load-bearing "if … then RH" is a **relocated wall**.

Score across Rounds 001–010 + all live branches: **zero** branches pass. The only non-inert directions
are both open and both on the dual side: construct the Archimedean `Γ`-factor / functional-equation
positivity non-circularly, or supply the `Spec ℤ` square host (Gram + Hodge-index) that SmartAlgebra
documents as nonexistent.

---

## 8. This session — the 2026-10-08 live blast (Rounds 001–049, `CRUCIFIXION_LEDGER.md`)

The live blast extended the frame through archimedean/finite-place geometry (`Γ_ℝ` built from succ/● with no
zeta, R29), the shadow-succ / Zeno "never-cross-0" picture, the Diophantine reframe (prime frequencies
`{log p}` ℚ-independent ⟹ Kronecker phase-alignment), and a **finite-window multiplicative semigroup**
(`T_a` = log-shift, `T_{log m}T_{log n}=T_{log mn}`, SOS identity, nonalignment theorem). Net result is
**fully consistent with §1 and §5**: every piece measured, all RH-equivalent, **no brick**, discriminator
§7 **still unmet** (zero branches pass). No theorem-debt moved.

The one genuine sharpening — the missing object of §5 now has a crisp operator name and its pieces are
**measured** (daniel's calibrated completed-Weil instrument, scratch-only; `M_full ≡ M_zeros` to 60 digits
⟹ the form's positivity *is* RH):

- **Target = joint coercivity `P − K ⪰ 0`** on the finite-window (support-`L`) test space.
- `P` (pole + arch + `−log π`) is **INDEFINITE** at every `L` tested (`λ_min(P) = −0.08 … −16.1` for
  `L_t=0.4…3.0`). ⟹ the "positive archimedean floor that primes erode" **does not exist as a floor**; the
  "arch dominates primes" brick (`arch+pole ≥ ‖K‖`) is **dead, measured**. `Observed[daniel §3]`.
- `K` (prime semigroup) is norm-bounded `λ_max(K) ≤ C_L < A_L` (≈ ⅓ of the worst-case pointwise comb mass)
  — the **nonalignment theorem** (band-limit can't concentrate on the Kronecker phase-alignments),
  confirmed and over-delivering. `Observed[daniel §3]`.
- The balance is **razor-thin** (`λ_min(P−K)` positive but collapsing `1e-11 → 1e-22` with resolution;
  PSD-window of prime-weight pinches to `[1−1.8e-13, 1+1.8e-15]`) and **held exactly by multiplicativity**:
  every mutation (fake impulse at `n=6`, `|α_2|≠1`, scaled weights, shifted `log 2`) drives `λ_min` clearly
  negative, ≈linear in the perturbation. `Observed[daniel §3–4]`.
- Crossover control: a non-multiplicative `L`-function (Davenport–Heilbronn) first goes indefinite at
  `L*≈4`, and the negative direction is **entirely** its single off-line zero (height 85.699) — moving only
  that zero on-line restores positivity. ⟹ in-instrument, positivity's sign **tracks zero-location
  exactly**. `Observed[daniel §2]`. (Matched multiplicative partner `L(s,χ)` not yet built — the clean
  open control.)

Reading (⟹ §5 unchanged): multiplicativity is **load-bearing for the sign** (measured), but it balances the
form *at zero*, it does not lift it to a margin; a knife-edge poised at zero **is** RH-equivalence. The live
lever is the **Diophantine well structure of `{t·log p}` × band-limit**, "of the same nature as the zeros."
`[Inf]`, RH-equivalent, not a theorem.

---

*Labels: `Verified` = re-derived independently here; `Observed[dig]`/`Observed[daniel]` = measured (sweep or
the calibrated scratch instrument), not a test of RH itself; `[Inf]` = interpretation; classical results
cited to their authors. §8 reflects the session state committed to `main` on 2026-10-08; this file changes
no source logic.*
