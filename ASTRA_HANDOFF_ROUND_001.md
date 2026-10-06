# Astra Work handoff — Round 001: normalize the actual RH proof target

Repository: \`femboy2112/FuckingRH\`  
Base branch: \`aletheia/rh-consolidation-2026-10-05\`

## Mission

Do not write another survey. Do not assume RH. Do not declare victory because the framework is elegant.

Your task is to **attempt the actual proof** using the sharpest normalized target now present in the repository, and to leave the repo in a state where every surviving proof obligation is explicit, minimal, and independently checkable.

The current shortest target is Masatoshi Suzuki's explicit function \(\Psi(t)\):

\[
\mathrm{RH}
\iff
\Psi(t)\ge0\quad\forall t\in\mathbb R.
\]

The same object also satisfies:

\[
\Psi(t)=W(R_t*\widetilde R_t),
\]

where \(R_t\) is a rectangular window and the Fourier side is sinc-squared;

\[
g(t)=-\Psi(t),\qquad
G_g(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u),
\]

with RH equivalent to global positive semidefiniteness of the screw kernel; and Nakamura–Suzuki prove

\[
\mathrm{RH}
\iff
e^{-\Psi(t)}
\]

is an infinitely divisible characteristic function.

The repository's current hypothesis is that the useful finite-to-Archimedean carrier is **aggregate prime-place convolution on logarithmic scale**, not an independent pointwise \(p\mapsto\infty\) smoothing. The Gaussian is the universal second-cumulant bulk; the proof-bearing data is the exact residual/closure.

## Mandatory first actions

1. Verify the remote repository, base branch, and exact head commit before editing.
2. Create a new branch from the consolidation branch, e.g.
   \`astra/psi-wavefront-proof-001\`.
3. Read, in this order:
   - \`README.md\`
   - \`CURRENT_STATE.md\`
   - \`docs/SCREW_SINC_LEVY_UNIFICATION.md\`
   - \`CLAIM_LEDGER.md\`
   - \`docs/NEGATIVE_CONTROLS.md\`
   - \`PROVENANCE_MAP.md\`
   - \`docs/LITERATURE_CURRENT_2026-10-05.md\`
   - \`research/2026-10-05/FOURIER_MELLIN_TRANSPORT_PROBE.md\`
   - \`upstream/SmartAlgebra/RH_BRIDGE_2026-10-02.md\`
4. Run the baseline:
   - install \`requirements.txt\`;
   - run \`tests/test_suzuki_psi.py\`;
   - inspect and independently verify \`scripts/suzuki_psi.py\` against Suzuki's published Eq. (1.1).
5. Treat archive material as evidence/history, not current truth. Read old dossiers only when a live lemma or dead end needs provenance.

## Primary-source audit

Before using any theorem, independently read the primary source and pin theorem/equation locators.

At minimum:
- Masatoshi Suzuki, JLMS 108 (2023), DOI 10.1112/jlms.12785:
  - Eq. (1.1), Theorems 1.2, 1.7;
  - Section 3.4, especially the triangular/rectangular convolution identity.
- Nakamura–Suzuki, arXiv:2306.08317:
  - Theorems 1.1–1.2;
  - the exact relationship \(g_\zeta=-\Psi\);
  - the Lévy–Khintchine normalization.
- Current 2026 compact-window / spectral literature in the repo bibliography if used.
- Recent Mittermeier checkpoint/tail preprints are **leads only**. Reconstruct every needed lemma independently before promotion.

If a repository summary disagrees with a primary source, fix the summary and record the correction.

## Preserve one principal causal state

Keep one principal reasoning thread carrying the theorem dependencies, conventions, failed routes, and residuals. If Work supports forks/subagents, fork narrowly from that state instead of spawning broad independent rereads.

Useful narrow forks:
1. **Source auditor** — Suzuki/Nakamura-Suzuki/Mittermeier theorem and sign audit.
2. **Event-dynamics analyst** — exact derivative/jump/convexity/checkpoint algebra.
3. **Lévy/CND analyst** — Schoenberg/Kreĭn/infinite-divisibility factorization route.
4. **Adversarial auditor** — circularity, hidden RH-equivalent estimates, hostile controls.

The principal agent must re-derive and integrate their results; helper reports are leads, not truth.

# The exact object to normalize

For \(t\ge0\), work from Suzuki's prime/Archimedean formula

\[
\begin{aligned}
\Psi(t)
={}&4(e^{t/2}+e^{-t/2}-2)
-\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n)\\
&+\frac t2\left[\frac{\Gamma'}{\Gamma}\!\left(\frac14\right)-\log\pi\right]
+\frac14\left(C-e^{-t/2}\Phi(e^{-2t},2,1/4)\right),
\end{aligned}
\]

with \(C=\Phi(1,2,1/4)=\pi^2+8G\), extended evenly.

Define the prime-power measure

\[
\mu
=
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}\,
\delta_{\log n}
\]

and the ramp

\[
r(t)=t_+.
\]

Then the prime contribution is the one-sided convolution

\[
P(t)
=
\int (t-u)_+\,d\mu(u)
=
\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n).
\]

Write

\[
\Psi(t)=A_\infty(t)-P(t)
\]

with all pole/Gamma/Lerch terms in \(A_\infty\).

Derive this decomposition independently and keep the exact signs fixed for the entire round.

## Immediate exact identities to derive

Do not assume these from prose; prove/check each:

1. Prime event times are exactly \(t=\log p^k\).
2. \(\Psi\) is continuous at every event.
3. The derivative has a downward jump
   \[
   \Delta\Psi'(\log q)=-\frac{\Lambda(q)}{\sqrt q}.
   \]
4. Distributionally,
   \[
   P''=\mu.
   \]
5. Between events, \(P\) is affine; all ordinary curvature is Archimedean.
6. For
   \[
   R_t(x)=2^{-1/2}\mathbf1_{[-t/2,t/2]}(x),
   \]
   show
   \[
   R_t*\widetilde R_t=\frac12(t-|x|)_+,
   \qquad
   \widehat{R_t*\widetilde R_t}(z)=\frac{1-\cos(zt)}{z^2}.
   \]
7. Verify
   \[
   \Psi(t)=W(R_t*\widetilde R_t)
   \]
   in the repo's fixed Weil convention.
8. With \(g=-\Psi\),
   \[
   G_g(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u).
   \]
9. State precisely the conditional-negative-definite / Schoenberg / infinitely-divisible equivalence with the correct signs and hypotheses.
10. Map this exact kernel to the Nakamura–Suzuki exponent, not a merely analogous Lévy process.

# Main proof attack

The goal is to prove, from arithmetic data,

\[
\boxed{\Psi(t)\ge0\quad\forall t\ge0.}
\]

Attack the following candidate mechanisms in order. Kill a mechanism decisively if it fails; do not keep weak routes alive for aesthetics.

## A. Exact arithmetic Gram / covariance factorization

Search for an arithmetic-only Hilbert map \(V(t)\) such that

\[
G_g(t,u)=\langle V(t),V(u)\rangle
\]

without using the unknown zero locations.

Equivalent useful targets include:

\[
\Psi(t)=\frac12\|V(t)-V(0)\|^2
\]

or an exact positive integral/sum representation of \(\Psi\).

This would be decisive.

Try:
- finite prime-place convolution spaces;
- adelic/Tate test-function spaces;
- periodization over the rational diagonal;
- Schur complements;
- rank-one/rank-two updates at prime-power event times;
- a direct covariance construction from independent local increments;
- an exact Hodge/Gram-style construction suggested by the function-field control.

Do **not** manufacture \(V\) by diagonalizing a matrix whose positivity is the thing being proved.

## B. Lévy / conditional-negative-definite closure

Since RH is equivalent to \(e^{-\Psi}\) being infinitely divisible, attempt to construct finite manifestly positive Lévy measures \(\nu_X\) and exponents

\[
g_X(t)
=
-\frac12a_Xt^2
+\int
\left(
e^{itx}-1-\frac{itx}{1+x^2}
\right)\nu_X(dx)
\]

such that

\[
g_X\to -\Psi
\]

in a topology known to preserve infinite divisibility / conditional negative definiteness.

Requirements:
- \(\nu_X\ge0\) by construction;
- no use of zeta zero locations;
- identify exactly how the Archimedean contribution enters;
- retain the non-Gaussian residual—ordinary CLT is insufficient;
- prove convergence, not numerical resemblance.

Try to derive the finite approximants from truncated Euler/local factors or from the aggregate prime-power convolution process already identified in the repo.

## C. Prime-wavefront reserve invariant

Treat \(\Psi\) as a deterministic reserve process:

- smooth Archimedean curvature accumulates between events;
- event \(q=p^k\) causes a slope drop \(\Lambda(q)/\sqrt q\);
- the active finite data at time \(t\) is exactly \(n\le e^t\).

Derive the exact minimum in each event interval.

Audit the 2026 checkpoint papers independently:
- verify or refute the claimed strict convexity regime;
- verify the plastic-constant curvature calculation if relevant;
- reproduce the one-minimum-per-interval reduction;
- locate the exact infinite-tail inequality;
- determine whether that tail inequality is genuinely weaker than RH or merely RH in disguise.

Then search for a **global inductive invariant** that pays each event cost from accumulated Archimedean reserve.

Good candidate shapes:
- a telescoping potential;
- a Bregman divergence;
- a renewal/storage inequality;
- a majorization relation;
- a completely monotone kernel comparison;
- a convolution-support inequality analogous to the Borwein plateau mechanism.

Finite interval verification is calibration only. The theorem is the infinite tail.

## D. Borwein/sinc support geometry

Exploit the exact fact that the RH-equivalent Weil test is generated by rectangular windows and sinc-squared Fourier weights.

Investigate whether Borwein-style convolution support thresholds give a useful monotone/threshold structure for the arithmetic explicit formula.

Be precise:
- identify the support object;
- identify the boundary;
- identify what is exactly constant/positive before contact;
- identify what changes at prime-power activation;
- do not transfer a finite-support plateau theorem by analogy alone.

The desired result is an inequality or factorization for \(\Psi\), not a metaphor.

## E. Aggregate finite-place Gaussianization — residual, not bulk

Re-derive the finite-prime convolution CLT in \`CURRENT_STATE.md\`, but use it only as a decomposition tool:

\[
\text{finite-place law}
=
\text{universal Gaussian bulk}
\times
\text{arithmetic residual}.
\]

Try mod-Gaussian or operator-valued refinements that remain uniform at the moving wavefront.

The question is whether the residual is exactly the object in the screw/Weil kernel.

If not, record the mismatch and stop using CLT as a proof route.

# Adversarial controls

Every promising lemma must be run against hostile models.

At minimum:
- synthetic off-line zero configurations satisfying functional symmetry;
- mutate one prime-power weight;
- omit/duplicate a prime power;
- phase-randomized prime models preserving one-point density;
- mutate the Gamma/Archimedean term;
- the two-prime Gaussian positivity obstruction in the repo;
- the positive Fourier-self-dual Gaussian-mixture false friend;
- finite-window models with a planted negative tail;
- check whether any "PNT error" or "Chebyshev error" bound used is already known equivalent to RH.

For an actual proof, conclusions inherit the weakest premise.

# Proof normalization requirements

Create \`research/astra_round_001/\` with at least:

### \`NORMALIZED_PROOF_TARGET.md\`
A self-contained theorem statement:
- definitions;
- exact equivalence to RH;
- no historical narrative;
- one fixed normalization.

### \`THEOREM_DEPENDENCY_DAG.md\`
Every arrow required for a complete proof. Mark each:
- PROVED-IN-REPO,
- PRIMARY-SOURCE THEOREM,
- NEW LEMMA PROVED THIS ROUND,
- UNVERIFIED,
- REFUTED.

There must be no invisible arrow from "finite checks" to "all \(t\)."

### \`EVENT_DYNAMICS.md\`
Exact prime-power event equations, derivatives, jumps, curvature, interval minima, and any checkpoint recurrence.

### \`LEVY_CND_BRIDGE.md\`
Exact sign conventions and equivalence among:
- screw-kernel PSD,
- conditional negative definiteness of \(\Psi\),
- Schoenberg positive definiteness of \(e^{-r\Psi}\),
- Nakamura–Suzuki infinite divisibility.

### \`CHECKPOINT_TAIL_AUDIT.md\`
Independent audit of the 2026 checkpoint/tail preprints. State exactly what is proved, what is reproduced, and where the tail remains.

### \`PROOF_ATTEMPT_001.md\`
The strongest actual proof chain you can obtain. If it stops, stop at the first unpaid lemma and explain why that lemma is not RH restated tautologically.

### \`ROUND_RESULT.md\`
Short final verdict:
- what became a theorem;
- what was refuted;
- what remains;
- whether RH is proved (almost certainly "no" unless every arrow is discharged);
- the single next verdict-changing probe.

Also:
- add reproducible scripts/tests for every nontrivial symbolic or numerical claim;
- use interval/exact arithmetic where sign claims depend on numerics;
- update \`CLAIM_LEDGER.md\`;
- update \`CURRENT_STATE.md\` only for results that survive audit.

# Git discipline

- Work only on your new branch.
- Make small, meaningful commits.
- Never rewrite the imported \`archive/\` history except to correct a clearly documented import corruption.
- Preserve raw experimental outputs where useful.
- Do not merge to \`main\`.
- At the end, open a draft PR back to \`aletheia/rh-consolidation-2026-10-05\` with a precise proof-status summary.

# Success criterion

A successful round is **not** "we found more RH-shaped structure."

A successful round does one of these:

1. proves \(\Psi(t)\ge0\) for all \(t\), with every dependency discharged, thereby proving RH through Suzuki's theorem; or
2. proves a new nontrivial lemma that strictly reduces the infinite-tail/CND/closure obstruction; or
3. decisively kills a plausible route and leaves a smaller, sharper obstruction.

Prefer exact identities, positive factorizations, monotone invariants, and structural comparison theorems over asymptotic fits.

The central question is now brutally simple:

\[
\boxed{
\text{Why can the explicit prime-wavefront reserve }\Psi(t)\text{ never cross below zero?}
}
\]

Go answer that—not rhetorically, but mathematically.
