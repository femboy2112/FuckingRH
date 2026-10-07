# SUCC/FUCC analogy discriminator and proof-obligation ledger

**Status:** Research design, not theorem claims. Complements [user-prompt provenance](USER_PROMPT_PROVENANCE_2026-10-07.md), [typed concept atlas](SUCC_FUCC_CONCEPT_ATLAS_2026-10-07.md), `CLAIM_LEDGER.md` and the Round007/008 theorem DAGs. The existing mathematical claim ledger takes precedence when there is any conflict.

**Rule:** A metaphor is permitted as a hypothesis generator. It enters the proof dependency graph only after an independently specified operator/form and a decisive comparison with the completed arithmetic target. A "pass" below generally establishes the **stated local criterion**, never RH by itself.

## I. Current obstruction map, scoped correctly

The genuinely explicit nonnegative arithmetic event square

\[
E_N(f)=E_\Gamma(f)+\sum_{n\le N}
\frac{\Lambda(n)}{\sqrt n}\|(\tau_{\log n}-I)f\|_2^2
\]

differs from the completed Weil form by

\[
\mathcal W(f)-E_N(f)
=(c_0-2S_N)\|f\|_2^2
+2\Re(\ell_+(f)\overline{\ell_-(f)}).
\]

This identity is a **proved-in-repo scoped result** (Round007) and the correct baseline for a new positive-square architecture. The large negative identity cannot be repaired by an orthogonal positive direct sum or a fixed finite-rank boundary term. Round008 adds no-gos for a **particular normalized coordinate boundary** class and a **particular shared-origin heat-coupling** class; it does *not* rule out every nonlocal interaction.

A new construction must therefore beat the actual discrepancy and reproduce the exact prime/Gamma/pole pairing, not merely "realize Euler" or match zeros numerically.

Useful immediate audits:
- a new cross-term cannot introduce nonzero extra `log(3/2)` translation atoms in a target requiring only prime-power integer shifts;
- a boundary correction with norm vanishing in the limit cannot remove a bulk term whose necessary magnitude diverges;
- preserving conductor labels under an isometry is not synonymous with creating conductor interactions;
- Gamma/digamma "passivity," shifted-ratio positivity and negative-index assertions inherited from Round006 must be checked against Round007 `PARENT_AUDIT.md`.

## II. Hypothesis register and discriminating probes

### H1 — A nonreducing continuum interaction is the missing FUCC/SUCC metric

**Prompt parents:** U09, U12, U20, U33. **Status:** UNVERIFIED; structurally motivated by the obstructions, not established.

**Candidate:** Work on a declared inductive clock-plus-continuum test space. Construct a source or observation operator `A_N` that does *not* preserve all conductor subspaces, is compatible with refinement maps, and has a computable polarized quadratic pairing. Its coefficients must be derived from SUCC, prime rays, Haar/CRT and the Gamma/pole completion — not reverse-engineered from a precomputed `\mathcal W` or zero ordinates.

**Decisive local probe:** Calculate the complete distributional translation kernel `K_{A,N}(x,y)`, including all cross terms, then compare with the finite-horizon completed Weil kernel.

- **Pass (local only):** The coefficients of the `log(3/2)` shift and every other forbidden rational-prime-ratio shift vanish *by a structural identity*, and the bulk `I` coefficient is corrected with the required sign/magnitude, all before fitting any data.
- **Fail:** An isolated forbidden atom survives; or the correction norm tends to zero while the needed identity coefficient diverges; or the only interaction is a basis change.
- **Ambiguous:** A fixed finite test grid matches, but the polarized distributional identity or limiting bounds are unavailable.

**Controls:** delete prime 3; mutate `log p→1`; replace `p^{-k/2}`; remove Gamma; replace the actual clock with synthetic modular periods. A construction insensitive to all mutations is probably RH-inert.

**Repo:** PR #6 `WEIL_PUSHFORWARD.md`; `REFINEMENT_CARRY_OSCILLATOR.md`; `CURRENT_WALL.md`.

### H2 — The growing clock has a small sufficient nonlinear boundary state

**Prompt parents:** U19–U20. **Status:** PARTIALLY CORROBORATED as a *finite-state recurrence observation*, UNVERIFIED as an RH bridge.

A growing `L_N`-dimensional clock can have low-dimensional formulas for selected scalar transfer observables. But a scalar rational/Möbius recursion and an exact polarized Weil test-space kernel are different data. Round008 established a scalar nonlinear closure for one class while rejecting an overbroad finite-LTI impossibility inference.

**Probe:** Construct two arithmetic histories with the same candidate compressed state. Apply the same next refinement and compare their complete continuum pairing and charge determinant.

- **Pass:** The compressed state is a genuine congruence for the specified complete observable, with exact refinement update.
- **Fail:** Same compressed state, different subsequent required pairing (minimal counterexample).
- **Ambiguous:** Exact agreement only for one scalar determinant, with cross-prime continuum correlations unmeasured.

**Controls:** reverse 2-then-3 and 3-then-2 charge order; compare full innovation determinants, not hand-inserted local Euler factors.

**Repo:** PR #6 `BOUNDARY_TRANSFER_STATE.md` and `MIXED_CONDUCTOR_HOLONOMY.md`.

### H3 — The modulus/carry twists are merely alternative encodings

**Prompt parent:** U22. **Status:** EXACT for declared unitary conjugacies; FALSE if "same support" is taken as enough.

Take two explicitly different clock descriptions and an intertwining unitary `U_N`. Check, on common domains,

\[
S'_N=U_NS_NU_N^*,\quad
H'_N=U_NH_NU_N^*,\quad
A'_N=U_NA_NU_N^*.
\]

**Probe:** Compare not only spectra and support but also weighted charge assignments, normalized Haar pairings, polarized test kernels and refinement compatibility.

- **Pass:** Every required observable is intertwined (same theory, different coordinates).
- **Fail:** A support-preserving or CRT-relabeling map changes the birth-charge functional or boundary pairing.
- **Ambiguous:** It preserves the prime list and eigenvalues but not the test-space kernel.

**Controls:** pure CRT permutation; random basis change conjugating **all** operators; random permutation of one operator's labels only. Conjugating the entire system should preserve all invariant results. Modifying only the charge assignment should generally not.

### H4 — The cube's coherent limit is spherical/local-flat, with a special critical-line tangent

**Prompt parents:** U28–U30. **Status:** CONJECTURED metaphor, no defined limit object.

A finite prime-exponent box is exact bookkeeping. A high-dimensional cube does not automatically converge to a sphere; high-dimensional concentration statements do not assert a geometric limit with RH content.

**Constructible lamp:** Choose `X_d` (metric space of finite prime supports), normalized metric `d_d`, embeddings/truncations `\pi_{d+1,d}`, and convergence notion (metric-measure, Gromov–Hausdorff, measured spectral, or a well-specified local tangent limit). Define the allegedly preserved arithmetic observable.

- **Pass (geometry only):** Rigorous limit in the declared topology; compatible quotient or pullback; same observable under coherent truncation.
- **Fail:** Different legal truncations have different limits, or the proposed sphere is not the limit in the declared metric.
- **Ambiguous:** Pictures of cubes and spheres have matching local tangent *appearance* but no transport of the arithmetic pairing.

**Adversary:** Construct two metric families with the same finite factor-support cubes but inequivalent limits; prevents claiming "prime support determines spherical geometry." RH needs a further Weil-identity/positivity theorem even after a geometrical limit.

### H5 — Gamma implements a rotation required by arithmetic dimensional orthogonality

**Prompt parent:** U04, U31–U32. **Status:** UNVERIFIED literal rotation claim; Gamma functional identities are exact.

The zeta functional-equation factor is a unit-modulus scalar **on** the critical line, but that does not establish zero confinement. The inverse-Gamma spectral determinant recovers a ladder of nonpositive even zeros in one normalization. These are separate statements.

**Constructible lamp:** Specify a family of Hilbert spaces `H_d`, a prime-direction vector `v_d`, a Gamma-derived linear operator `G_d(t)`, the inner product and a common-basis transport. Require `G_d^*G_d=I` if "rotation" means unitary; otherwise use a different, honestly named operation.

- **Pass (local only):** Exact orthogonality/phase identity under declared normalization that *detects arithmetic mutations* and survives change of basis.
- **Fail:** Gamma is only a scalar factor/phase with no action on prime directions, or changes norms/angles contrary to the claim.
- **Ambiguous:** An angle can be chosen after the fact to match a known critical-line spectral phase.

**Controls:** replace Gamma by an artificial functional-equation factor with similar unit-modulus symmetry; the discriminant must rely on arithmetic, not just reflection symmetry.

### H6 — Correlated collapses yield exact prime-source cross terms

**Prompt parents:** U32–U34. **Status:** EXACT as atomic/ramp arithmetic distribution; UNVERIFIED for extra `2ω log p` mixed-field mechanism.

The guaranteed distributional identity is

\[
\left(\sum_{p,k}\frac{\log p}{p^{k/2}}
(t-k\log p)_+\right)''
=\sum_{p,k}\frac{\log p}{p^{k/2}}\delta_{k\log p}.
\]

A coherent amplitude square `\|a+b\|^2=\|a\|^2+\|b\|^2+2\Re\langle a,b\rangle` **does** generate cross terms. Their coefficients are fixed by the actual operators; they cannot be asserted to be `2\omega\log p` without such an operator.

**Probe:** Declare the carrier and event amplitude maps and compute their Gram for two distinct prime powers, with no orthogonalization before the square. Compare complete off-diagonal distribution and pole channel with Weil.

- **Pass:** A required mixed coefficient is derived exactly, with correct sign and support.
- **Fail:** Cross terms vanish under the proposed history, have the wrong sign or extra rational-ratio shifts.
- **Ambiguous:** A scalar frequency fit agrees but no polarized kernel matches.

**Controls:** one-prime-only and two-prime controls; correct/incorrect half-density; artificial event permutations. A literal quantum measurement model requires separate empirical/operational evidence.

### H7 — A nontrivial curvature lives on weighted SUCC-form loops

**Prompt parents:** U25–U27. **Status:** UNVERIFIED; finite algebraic loops can be exact.

For example, the *sequence of different maps*

\[
3\xrightarrow{4n+1}13
\xrightarrow{(3n+1)/8}5
\xrightarrow{(2n-1)/3}3
\]

closes arithmetically. It is **not** automatically one autonomous dynamical system, a connection, or a nonzero holonomy.

**Probe:** Define a directed graph of arithmetic maps, edge transport `U_e` in a fixed coefficient space and a declared path-composition convention. Evaluate the ordered product around the loop and compare with a contractible control loop and basis conjugacy.

- **Pass (local only):** A nontrivial conjugacy-invariant holonomy derived from the arithmetic transport, stable under redundant path refinements.
- **Fail:** Every loop product is identity (flat), or nontriviality is inserted by arbitrary edge phases.
- **Ambiguous:** Numeric loop weight depends on coordinate choices with no gauge invariant.

**Controls:** reverse loop orientation, subdivide edges, permute labels, replace integers by fake arithmetic with same path length. Relate curvature to completed Weil only by an additional exact trace/pairing identity.

### H8 — "Self-sieving" clock activations reconstruct the prime weights without circular input

**Prompt parents:** U11–U14. **Status:** DISCLOSED for LCM log-increments, not an RH theorem.

**Probe:** Derive `log L_N-log L_{N-1}=\Lambda(N)` from independent LCM construction and compare the complete source `\sum\Lambda(n)n^{-s}` to the Euler-region logarithmic derivative. Then test a *global* determinant built from full conductor innovations versus a product of local prime resolvents.

- **Pass:** Exact `Λ` and `-\zeta'/\zeta` Euler-region identities; correct full mixed-conductor multiplicities.
- **Fail:** A purported full-innovation determinant is instead silently replaced by local Euler factors; the two are known to differ.
- **Ambiguous:** Numeric agreement at one `s` while determinant normalizations differ.

**Repo:** PR #6 `GLOBAL_INNOVATION_THEOREM.md`; this class of **uncoupled** determinant is already refuted as zeta, so do not rerun without changing the hypothesis.

### H9 — A clock matrix is equivalent to Suzuki's finite Hankel matrix

**Prompt parents:** U19, U23–U24, U36. **Status:** UNVERIFIED; automatic identification is false.

Suzuki moments are defined from the **completed** `Ψ`, and the Hankel criteria require both determinant families at every order. LCM clock spaces are finite Fourier/residue spaces with different measures, dimensions and indexed observables.

**Probe:** Give explicit maps `A_{N,m}` from the clock/continuum source to moments `μ_0,\ldots,\mu_{2m+1}`. Prove exact equality for every finite `m` **with residuals and Gamma/pole channels derived**, and then quantify uniformity as `m,N→∞`.

- **Pass (finite):** Exact first `2m+1` moments with correct normalization, and no fitting the target moments as source input.
- **Fail:** Missing Gamma or pole terms, or moment matching relies on replacing true clock dynamics by preloaded `Ψ`.
- **Ambiguous:** A finite Hankel matrix is positive but the all-order limit has no established sign control.

**Hostile control:** insert a synthetic measure whose first `k` moments agree but whose later Hankel minor is negative; this demonstrates why finite matches cannot certify a universal criterion. The synthetic control must be constructed explicitly before claiming it separates a particular method.

### H10 — Unit-basepoint character jets cancel the divergent first-order prime debit before squaring

**Prompt parents:** U09, U21 and historical U02/U05; **agent-origin name:** UBRPCT. **Status:** UNVERIFIED.

The rational product formula gives `\sum_v\log|x|_v=0`, but an identity on diagonal rationals is not yet a trace/correlation identity for the complete test-space kernel.

**Probe:** Specify finite places and the real place in the *same* operator/measure, write a renormalized second derivative or polarized jet *before* separate local squaring, and prove convergence to the actual Weil distribution. Check the entire correction, not merely the scalar first-jet cancellation.

- **Pass (local only):** Exact place-by-place and cross-place identity for a rich test class with arithmetic normalization.
- **Fail:** Cancellation only on a rational scalar diagonal or the resulting Gram has indefinite/non-vanishing residual.
- **Ambiguous:** A formal product-formula square with no positive trace, domain or limit.

**Control:** compare with a function-field positive Gram (valid external positive control), and with a synthetic self-dual factor carrying off-line zeros (negative control); self-duality alone is insufficient.

### H11 — Trivial zeros are a causal precursor of the nontrivial zero modes

**Prompt parents:** U04, U17, U31–U32. **Status:** CONJECTURED geometry; exact Gamma/trivial-zero identities exist.

`1/\Gamma(s/2)` has zeros at `s=0,-2,-4,\ldots`. Zeta's trivial zeros occur at `-2,-4,\ldots`; the completed xi function cancels them with Gamma poles and prefactors. That is a meromorphic identity, not a dynamical derivation of the nontrivial zero heights.

**Probe:** A zero-independent operator built from the proposed inverse-SUCC and Gamma channels must recover **both** the true completion and a positive/self-adjoint structure. Test deformations preserving the Gamma ladder but altering the Euler source.

- **Pass (local only):** Correct cancellation and target determinant without using nontrivial zero ordinates as input.
- **Fail:** A construction produces only Gamma's trivial spectral ladder or needs planted nontrivial zeros.
- **Ambiguous:** Functional equation is recovered, but self-adjoint positivity is not.

### H12 — The locally exact construction extends through infinite closure

**Prompt parents:** U19–U20,U35–U36. **Status:** the central UNVERIFIED arrow.

**Probe contract:** Fix complete test class `C_c^\infty(R)`, cutoff/refinement net, exact target `\mathcal W`, operator topologies and normalizations, then prove:
1. finite objects arise independently of the desired sign;
2. complete (not sampled) polarized test pairing converges to Weil;
3. positivity passes to the limit in a topology controlling every admissible test;
4. Archimedean and prime compensations are justified uniformly;
5. the construction is sensitive to arithmetic mutations and does not collapse to a tautological `\mathcal W^{1/2}`.

- **Pass:** A bona fide independent positive family satisfying all four analytical dependencies and the target identity would prove RH, subject to hostile proof audit.
- **Fail:** Any limiting step removes an infinite negative residual, assumes target positivity, or fails at a fixed compact test.
- **Ambiguous:** Millions of successful finite tests and no tail estimates. Finite evidence is finite.

**Class constraints already known:** Round007 sampling no-go, factor-local lift no-go and difference-square bulk deficit; Round008 localized-boundary/vanishing-capacity theorem and reducing-oscillator example.

## III. Highest-information next probe

**Target:** H1 informed by H3 and H6, not another fit to zero ordinates.

Use the complete, already constructed Round008 clock/continuum setup. Introduce **one independently motivated nonreducing observable** and compute its entire polarized kernel. Before any positivity claim, impose:

1. **Finite exact support test:** coefficient at `log(3/2)` vanishes; no forbidden rational-ratio atoms.
2. **Bulk identity test:** comparison with `c_0-2S_N` produces the required cancellation through an actual interaction, without a divergent unaccounted metric.
3. **Infinite-place test:** Gamma difference, pole cross product and arithmetic source have exactly the Weil normalization.
4. **Uniformity test:** prove a limit on compact smooth tests, preserving positivity if the finite forms are positive.
5. **Hostile controls:** mutate prime weights, half-density and Gamma; fake primes cannot pass for the same structural reason.

A **failure** is scientifically useful if it yields a small counterexample or a scoped theorem (which hypotheses it excludes), and the lineage is recorded under the user's original U-ID. A **pass** through 1–3 is not yet RH; the uniform all-test positivity step remains.

## IV. Archival rules

- Do not silently change the user prompt to make a theorem look more natural.
- Preserve the distinction between `phi`-pathway success (a formalization exists) and `sigma`-source adequacy (the arithmetic Weil target is still represented correctly).
- Same-model review is not independent provenance.
- A finite matrix with positive eigenvalues may be an intrinsically different object from the required Hankel/Weil matrix.
- Equivalence under change of basis requires transporting **every** source, measure, operator and observable, not only integer support.
- Register failed analogies as failed in their **specific formalization class**, not as globally refuted human intuitions.
- Never promote "the cube is a sphere," "Gamma rotates by 90°," "wave collapse," "flat modulus twist," or "small matrix holds the universe" to theorem without the listed decisive tests.

**Latest lineage read for this file:** `main` @ `b836656f9b284a35ef7e412b2af24b879ea80ed9` (Round006 consolidation); PR #5 @ `8da6cf92d276961356497486048163f0aff08233` (Round007); PR #6 @ `90f93e655ee7e57260d6a45c168ce8dcff321601` (Round008). Open PR heads are not merged into this provenance branch; source paths there are cited as external-branch research, not claimed to exist on main.

**Provenance verdict:** exact local identities and several negative theorems are available; a nonreducing, completed Weil interaction remains UNVERIFIED. RH OPEN.
