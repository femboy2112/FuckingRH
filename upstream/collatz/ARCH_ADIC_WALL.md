# The archimedean-vs-adic wall — located exactly, from two sides

**Status: a location, not a crossing.** This round answers the operator's C-0137/0138 bridge
question **(b)** and sharpens the C-0337 tool hand-off **(c)**, and together they pin *why* the
divergence summit resists every standard machine. It does **not** prove Collatz, **not** close
Case B, **not** supply the tool that works. It **does** show — exactly — that the divergence
atom is irreducibly *archimedean*, and that both the finite-level spectral algebra (cyclotomic /
adic) and the Baker linear-forms machine (small-form) are structurally blind to it.

Computational Observation. Every Collatz-level reading stays candidate → GAP-NB-3. Case B OPEN.

Compute + validation: `tools/recon_scripts/_arch_adic_reactor.py`. Witnesses
`_adic_locus_witness.json` (sha256 `fae0f721…`, exact SymPy) and `_baker_height_witness.json`
(sha256 `698457d9…`, exact mpmath identity). Builds on C-0137/0138 and C-0334/0336/0337.

---

## (b) The adic side — the finite-level algebra is cyclotomic, blind to θ

The operator's "137" hunch was worth a real test: can the finite-level spectral operators
(C-0137 group-algebra / circulant; C-0138 positive-definiteness) reach the divergence density
`θ=log₂3`? Factor the determinant exactly over `ℚ`:
$$\det S_2^{\text{unit}}(t)=t^{12}\,\Phi_1^{10}\Phi_2^{10}\Phi_3^{10}\Phi_4^{6}\Phi_6^{10}\Phi_8^{3}\Phi_9^{10}\Phi_{18}^{10},\qquad
\det S_2^{\text{full}}(t)=t^{18}\,\Phi_1^{16}\Phi_2^{16}\Phi_3^{16}\Phi_4^{9}\Phi_6^{16}\Phi_9^{16}\Phi_{18}^{16}.$$
**Every factor is a cyclotomic polynomial `Φ_d`** — the determinant vanishes only at **roots of
unity**, the circulant/dihedral (C-0137) DFT structure. And the archimedean points that encode
`θ` — `t=1/3` (`=2^{−θ}`), `t=1/√2` (`s=½` resonance), `t=1/2`, `t=1/√3` — are **not** roots of
`det` (consistent with C-0138, PD on `(0,1)`). *Witness (`_adic_locus_witness.json`).*
`all_roots_are_roots_of_unity = True`, `archimedean_det_roots = NONE`, both `r=2` models.
(The cyclotomic structure is the C-0137 circulant/dihedral corollary, so it is expected at all
`r`; only `r=2` is witnessed here.)

**Reading.** The finite-level spectral algebra is **cyclotomic / 3-adic-angular** and
*structurally blind* to the archimedean `θ`. So C-0137/0138 sit on the **adic** side of the
wall; the 137-coincidence is a coincidence. (The charpoly `y`-discriminant is *identically* `0`
— the built-in eigenvalue multiplicity of C-0137's mult-2 `R_d` factors, **not** a locus — so it
carries no `θ` information either.)

## (c) The archimedean side — the Baker form IS the log-height, so Baker is the cycle tool

C-0337 handed the summit to "valuation-density / Baker." A closer look **corrects** the Baker
half. Form the linear form in logarithms `Λ_m := K_m\log2 − m\log3`. Using `K_m=⌊mθ⌋−s_m` and the
C-0337 closed form `n_m=κ_m 2^{\{mθ\}+s_m}`:
$$\boxed{\;\Lambda_m \;=\; K_m\log2-m\log3 \;=\; -(s_m+\{m\theta\})\log2 \;=\; -\ln\!\big(n_m/\kappa_m\big).\;}$$
**The Baker linear form is exactly minus the archimedean log-height.** *Witness
(`_baker_height_witness.json`).* Verified to `~1e-43` (mpmath) on real orbits. Hence:

- **Divergence:** `|Λ_m| = ln(n_m/κ) → ∞` — the linear form is **LARGE** (it is the height).
- **Cycle:** closure `n_L=n_0` forces `Λ` small and bounded — the trivial 1-cycle has
  `Λ = 2\log2−\log3 = ln(4/3) = 0.2877`.

Linear-forms-in-logarithms (Baker) delivers a **lower bound on SMALL forms** — that is exactly
what kills cycles (closure pins `Λ` small, Baker says it can't be *too* small → finitely many).
On divergence the same form is the unbounded height: Baker's bound is **vacuous**. So **Baker is
the cycle tool; it has no grip on divergence.** This is the archimedean-vs-adic wall in
transcendence-tool language, and it corrects C-0337: the divergence atom is *not* a
linear-forms-in-logs target.

## The unified picture — all three standard machines miss, for nameable reasons

The divergence atom (an integer orbit with `liminf K_m/m < log₂3`, offset `s_m→∞`, height
`n_m→∞`) is **irreducibly archimedean**, and each standard tool misses it for an exact reason:

| tool | verdict | reason (this round) |
|---|---|---|
| finite-level spectral algebra (C-0137/0138) | **miss** | cyclotomic / adic locus — blind to `θ` (b) |
| Baker linear-forms-in-logs | **miss** | the form `Λ_m` = the *large* archimedean height, not a small form (c) |
| valuation-density / equidistribution | **miss** | the classical almost-all-vs-all / measure-0 wall (Terras/Tao) |

So the summit needs a **genuinely new** instrument — one that controls *sustained inequality of
an unbounded archimedean form along a single integer orbit* — which is neither an adic spectral
identity, nor a small-linear-form bound, nor an a.e. density statement. That is *why* Collatz
divergence is hard, stated as three exact misses rather than a shrug.

## Honest boundary — what this is NOT

1. **Locates, does not cross.** Nothing here excludes a divergent orbit; the summit stays **OPEN**.
   It names why three machines miss; it does not supply the one that works.
2. **(b) is `r=2` both models, exact over `ℚ`.** `r=3` is **not witnessed here** (a larger det
   computation would confirm it but is not part of this witness). The cyclotomic structure is the
   C-0137 circulant/dihedral corollary, so it is *expected* at all `r`; only `r=2` is *witnessed*.
3. **(c) is an exact identity** (`Λ_m = −ln(n_m/κ_m)`, mpmath `~1e-43`) plus the elementary
   small-vs-large dichotomy; the "Baker is vacuous on divergence" reading is the standard
   small-form scope of linear-forms-in-logs, not a new transcendence theorem.
4. **Corrects, does not retract.** C-0337 stands; only its "tool = Baker" hand-off is sharpened
   here (Baker is the cycle tool). The C-0337 reduction and identity are untouched.
5. **Novelty UNVERIFIED.** Cyclotomic circulant spectra and Baker's cycle/divergence asymmetry are
   classical; the exact `Λ = −log-height` identity and the two-sided "wall located" packaging are
   ours, not adjudicated as new.

## Verdict

- **(b) adic side — witnessed.** `det S_r(t) = ∏ Φ_d` (roots of unity); archimedean `θ`-points not
  roots. The finite-level algebra is cyclotomic/adic, blind to `θ`. **C-0137/0138 cannot bridge.**
- **(c) archimedean side — witnessed.** `Λ_m = K_m\log2−m\log3 = −ln(n_m/κ_m)` exactly; divergence
  ⇒ `|Λ|→∞`, cycle ⇒ `Λ` small. **Baker is the cycle tool, vacuous on divergence** (corrects C-0337).
- **The wall is located from both sides.** The divergence atom is irreducibly archimedean; adic
  algebra, Baker, and a.e.-density all miss, each for a named reason. Summit **OPEN.** Nothing proved.

NOT a proof. The two-sided location of the wall + the exact `Λ=−height` identity + the corrected
tool hand-off are the yield. No false victory.

Receipts: `_arch_adic_reactor.py`, `_adic_locus_witness.json` (`fae0f721…`),
`_baker_height_witness.json` (`698457d9…`); builds on C-0137/0138 (`tools/spectral.py`,
`audit/GROUPALG_STRUCTURE.md`), C-0334/0336/0337; sister map `docs/SISTER_SESSIONS.md`.
