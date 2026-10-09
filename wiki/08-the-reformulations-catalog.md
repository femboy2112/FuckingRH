# 8. The reformulations catalog — RH through every lens we tried

*This page is a map of the program's **branches**: ~47 experimental branches across four agent
lineages, combed read-only and distilled here. Each branch looks at RH through some lens and
produces a faithful restatement. The purpose of cataloguing them is **honesty, not advertisement**:
every entry is either an **exact RH-equivalent reformulation** (a real theorem, but it only moves
the target) or a **stage-reconstruction** (it re-derives known structure and is RH-inert). **None is
a proof, and none is a non-circular step toward one.** We keep the walls visible so no one re-walks
a path thinking it is new.*

*Read each entry as: **RH looks like this if you consider X → here is what you get → here is the
wall.** Classes: `REFORMULATION→WALL` (exact restatement, RH-equivalent), `STAGE-RECONSTRUCTION`
(re-derives known math, RH-inert), `NO-GO` (a proved obstruction — negative content).*

---

## 8.0 Read this first: two facts that govern the whole catalog

**(1) Common-mode provenance.** The branches are **one stacked lineage**, not independent
witnesses: `rh-consolidation ⊂ profinite-successor ⊂ …`, same author, same pipeline, same Suzuki-Ψ
target, and the internal audits are same-model. So the fact that *every* branch "converges on the
same wall" is **common-mode** — it is one bearing seen from many angles, and it should be counted as
*one*, not as dozens of confirmations. (The repo says this itself:
`docs/RH_LINEAGE_SOURCE_INDEPENDENCE`.)

**(2) The factorization meta-theorem.** A construction that is **commutative-multiplicative**
collapses to a **factorized** (per-prime, tensor) object, and a factorized positivity is
**RH-inert** — it holds whether or not the arithmetic is real (proved four ways in the Round-004
notes: uniform Pascal / binomial Fock isometry / Koszul–Hodge / GCD kernel). This is *why* almost
every "I found a positive object" below is inert: the positivity is per-prime, and RH lives in the
*cross-prime, global, Archimedean-coupled* part that none of these constructions build.

> **The verdict, stated once.** Across every framing below, **zero** carry genuine non-circular
> content toward RH. The one entry with a genuinely new conservation law (the fresh-digit isometry,
> [§8.5](#85-dynamical-lens)) conserves norm *inside the finite source* and is mutation-insensitive
> — real mathematics, RH-inert. Every route to *positivity* lands on the same object: the completed
> Weil form's global coupling, which is [the missing theorem](06-state-of-the-program.md).

---

## 8.1 Spectral / Weil lens

- **Suzuki-Ψ screw / sinc / Lévy.** *RH as* `Ψ(t) ≥ 0 ∀t`, equivalently the screw kernel
  `K_Ψ ⪰ 0`, equivalently `e^{-Ψ}` infinitely divisible. *You get* the clean zero-side identity
  `Ψ = Σ_γ (1−cos γt)/γ²` and the tent test family. *The wall:* this is Suzuki's theorem; positivity
  of the zero comb **is** RH. `REFORMULATION→WALL`. *(astra psi-wavefront, rh-consolidation,
  mellin-dirac-completion.)*
- **The completed edge-square.** *RH as* a positive first-order square `W(f⋆f̃) = ‖D_N f‖²`. *You
  get* the exact identity `W(f) = ‖D_N f‖² + (c_0 − 2S_N)‖f‖² + 2\,Re(ℓ_+f·\overline{ℓ_-f})` with
  `c_0 = ψ(¼) − log π < 0` and `S_N = Σ_{n≤N} Λ(n)/√n`: the negative prime correlations are honest
  cross-terms costing `2S_N‖f‖²`. *The wall:* the residual is negative on an infinite-dimensional
  subspace; closing it needs a continuum, nonlocal, factor-mixing coupling equal to the completed
  Weil form — naming it is "RH-shaped restatement." Several **NO-GO**s fall out (fixed integer-log
  samples share an invisible subspace with `W ≥ 1.3544‖f‖²`; forward trace-class returns have
  Fredholm det `= 1`, so no Euler determinant). *(astra stratified-succ-fucc-square,
  chiral-krein-completed-square.)*
- **Finite Weil operator `Q_W^a = P_a − D_a`** (Feshbach / log-bathtub). *RH as* `Q_W^a ⪰ 0` for every
  finite interval `a`. *You get* genuine **unconditional** spectral theorems — a zero-extension
  identity, compact resolvent, eigenvalue lower bounds `λ_n(P_a) ≥ ½[γ + log(πn/2) − Ci(πn/2)]`, and
  a finite negative-index bound. *The wall:* `P_a ⪰ D_a` for all `a` is RH-equivalent; and the
  "`RH ⟺ η_A(ℓ) = O(e^{-A}(1+A)^K)`" criterion is very likely von Koch's `ψ(x)−x = O(√x\,log²x)` in
  boundary-strip dress. `REFORMULATION→WALL` (with real unconditional operator content that does not
  touch the sign). *(audit rh-proof-bearing-frontier, research rh-log-bathtub-prime-shift.)*
- **Suzuki → Weil tangent.** *RH as* the first variation (in the conductor parameter `ω`) of Suzuki
  passivity. *You get* `d/dω\, b_ω(n)|_{0} = 2Λ(n)/√n` (verified), so the prime term of the localized
  Weil form is the prime-ray Dirichlet energy minus `2(Σω)‖v‖²` — unconditionally positive. *The
  wall:* the global diagonal/Archimedean counterterm (the old "local squares vs global completion").
  The infinite-zero form-limit is explicitly **UNVERIFIED**; the finite-zero version takes zeros as
  *input* and is circular as a positivity route. `REFORMULATION→WALL`. *(finite-hankel-contraction,
  succ-weil-suzuki-rigorous-bridge SWS-002.)*
- **Euler product as Fock / whitening (the ζ-Gram).** *RH as* positivity at the edge of a Fock space:
  `⟨ζ_u|ζ_s⟩ = ζ(s+\bar u)`, `‖ζ_σ‖² = ζ(2σ) < ∞ ⟺ σ > ½`, so the critical line is exactly where the
  creation vectors leave the space. *The wall:* positivity holds precisely where the vectors exist
  (`σ > ½`); RH is the continuation to the line, which the Gram does not deliver. `STAGE-RECONSTRUCTION`.
  *(profinite-successor, pascal-fucc.)*
- **Prime-built Weil kernel / PSD knife-edge.** *RH as* `K_{Ψ,L} = T_L^*T_L` with `T_L = √{K_{Ψ,L}}`
  real for all `L`. *You get* a "Hilbert–Pólya from primes" observation (eigenmodes converge to the
  zeros `14.13, 21.02, …` as `1/γ²` doublets) and a measured stability radius of the finite-place tilt
  `∼ e^{-0.85L}` shrinking to `{0}`. *The wall:* forming `√K` presupposes `K ⪰ 0`; "the zeros fall out
  of the primes" is the explicit formula, not a discovery. `REFORMULATION→WALL`. *(pascal-fucc;
  the knife-edge is the measured razor-thin balance of [page 6](06-state-of-the-program.md).)*

## 8.2 Operator / passivity lens

- **Schur–Vitali passive-limit.** *RH as* the existence of finite arithmetic transfer functions `Θ_X`
  that are **contractive on all of** `H_{1/2}` *by construction* and converge to `Cayley[ξ'/ξ]` only on
  the safe Euler region `Re s > 1`; Montel/Vitali then forces positive-realness down to the line. *You
  get* a valid conditional theorem (Vitali–Porter + Cayley) and the honest reduction that *strip
  convergence is concluded, not assumed*. *The wall:* the hypothesis "(P): such a passive family
  exists" **is** RH (taking `Θ_X = Cayley[ξ'/ξ]` is Schur iff RH). `REFORMULATION→WALL`.
  *(source-port-passivity-006, source-wired-prime-rays, and an independent Aletheia derivation.)*
- **Impedance / Laplace one-port.** *RH as* a passive source-response port
  `F_P = A_{\infty,P} − Σ_{p^k≤P} Λ\,n^{-s}`. *You get* the measured fact that it is **not**
  positive-real: `min Re F_P ≈ −2` and the excursion count diverges with `P`. *The wall + the
  mechanism:* a truncated primewise (hence factorized) Dirichlet sum **cannot** be passive — by the
  meta-theorem, and concretely by Bohr–Kronecker phase alignment (`Re Σ Λ n^{-σ-it} ≈ P^{1-σ}/(1-σ)`).
  `NO-GO` (kills the one-port / direct-sum class). *(source-port-006.)*
- **Finite-horizon Hankel contraction.** *RH as* `‖H_{ω,a}‖ ≤ 1` for all `ω > 0` and all `a > 0`
  (Suzuki's multiplicative Hankel), equivalently a family of causal-Toeplitz convergence inequalities.
  *You get* an exact finite-horizon interface, horizon-monotone norms, and an exact discrete-conductor
  factorization `H = V^*GV` with blocks `W_n` of dimension `φ(n)` and critical weights `φ(n)/√n`. *The
  wall:* under innerness `‖H‖ → 1`, so the critical gap `g(a) → 0` — no uniform gap can come from any
  finite computation; the real endpoint is `ω ↓ 0`, not the PNT-known `ω = ½`. `REFORMULATION→WALL`.
  *(finite-hankel-contraction, discrete-conductor-suzuki, causal-filtration tangent.)*
- **Hardy innerness / activation-vs-passivity.** *RH as* `Θ_ω(z) = ξ(½−ω−iz)/ξ(½+ω−iz)` meromorphic
  **inner** for every `ω > 0`. *You get* unconditional causality and `|Θ_ω| = 1` on `ℝ`, a clean KYP
  storage picture, and an explicit stable/unstable counterexample pair showing a positive causal
  boundary-modulus-1 system can still have an unstable pole. *The wall:* the global `L²` mapping of
  `h_ω ⋆ f` (Suzuki Thm 2.2), i.e. a source-derived all-`ω` contractive transfer on the Euler-safe
  half-plane with `P ⪰ 0`. This **is** the user's "activation vs passivity" intuition, and it is
  correct at source-support level only. `REFORMULATION→WALL`. *(rh-activation-causality-passivity.)*
- **Weyl / Herglotz passivity abscissa.** *RH as* `β_* = ½`, where `β_* = \inf\{σ : m_σ\ \text{Herglotz}\}
  = \sup Re ρ`; each prime is a Schur channel `F_p = (1+rz)/(1-rz)`, `r = p^{-1/2}`, and
  `-ζ'/ζ(½-iz) = ½Σ(\log p)[F_p − 1]`. *The wall:* existence of passive finite approximants
  (the same object as Schur–Vitali); local primes all survive the half-shift, so the failure is the
  infinite centering + Γ renormalization. `NO-GO`s: Γ is not an inner channel (Blaschke fails); direct
  sums of positive prime blocks diverge. `REFORMULATION→WALL`. *(succ-fucc-weyl.)*
- **Refuted coordinate (tombstone).** `Re\{ξ(s)/ξ(s+1)\} ≥ 0` on `H_{1/2}` is **not** RH-equivalent —
  a de Branges / Conrey–Li *sufficient* condition that is itself false in the strip
  (`Re = −0.000132` at `s = 1+282i`; verified). Kept only as a correction; see
  [§2.4](02-the-rh-equivalent-target.md). `NO-GO`.

## 8.3 Adelic / Tate lens

- **Unit-basepoint place-character jets (UBRPCT).** *RH as* an object built at the trivial valuation
  with the `½`-twist `|x|_v^{1/2+z}`: the half-density `p^{-k/2}` is the first jet, the first jet is
  product-formula-null (`Σ_v \log|x|_v = 0`), and the cross-prime coupling lives in the **second
  jets** (`0 = (Σ_v \log|x|_v)² = Σ_v(\log|x|_v)² + 2Σ_{v<w}\log|x|_v\log|x|_w`). *The wall:* the
  product formula is a *modulus identity* and does not cancel the additive bulk `ΣM_p` (measured:
  intersect-before-squaring diverges `∼ π(N)²`); cancellation needs the signed Weil cross-terms, i.e.
  Connes' adelic positivity. `REFORMULATION→WALL` — Connes–Tate re-derived. This is **open seam #2**
  on [page 6](06-state-of-the-program.md). *(unit-place-transport, stratified-diagonal, cross-pollination.)*
- **Affine `ax+b` / Bost–Connes.** *RH as* the arithmetic of the `ℕ⋊ℕ^×` monoid with
  `V_aS = S^aV_a` (this is exactly Cuntz's `Q_ℕ`: `s_n v = v^n s_n`, with a **unique KMS state at
  `β = 1`** in the standard normalization — the branch's half-density-shifted convention relabels it
  `3/2`/`β=½`, which should not be quoted as standard); the KMS state restricts to Bost–Connes; `Λ(q)/√q` and
  `P(t)` are its expectations, with a gcd/lcm CND metric. *The wall:* only the **finite-place half** is
  represented; the missing object is a vector `η_t` with `‖Proj_{pp}η_t‖² = P(t)` and `‖η_t‖² = A_∞(t)`
  (Bessel would then give `Ψ ≥ 0`) — not constructed. `STAGE-RECONSTRUCTION` (= BC + Cuntz + Connes/Tate;
  the branch says so). *(pascal-fucc, profinite-successor.)*
- **Bilateral affine `Aff(ℚ) → Aff(ℝ)`.** *RH as* the closure under inverse SUCC/FUCC forcing fractional
  steps, unitarity forcing `a^{-1/2}`, and the product formula `\log|q|_∞ + Σ\log|q|_p = 0`. *The wall:*
  group completion ≠ analytic continuation; the θ/Poisson symmetry must be inserted from outside, and no
  trace theorem is supplied. `STAGE-RECONSTRUCTION`. *(bilateral-affine-completion.)*
- **Cubical Hodge-index via the product formula.** *RH as* a Hodge-index inequality on `(ℙ¹)^m`: the
  product formula places `u_q = Σ_v a_v λ_v x_v` in the primitive hyperplane, and
  `Q_L(u_q) = C_L[(\log|q|)² + Σ_p v_p(q)²(\log p)²] > 0` **unconditionally**. *The wall, loud:* this is
  positive because it is a *weighted Euclidean norm on a hyperplane* — trivially positive for any
  positive weights. It is **not** the Weil form (no `log p^k` translations, no Γ-difference kernel, no
  pole form); the identification `Q_L(u_f) = Q_W(f)` is unbuilt. It is the function-field geometric-proof
  *shape* without the function-field *input*. `STAGE-RECONSTRUCTION` (+ unbuilt target).
  *(cubical-gamma-rh-proof-attempt.)*
- **Profinite successor lightcone.** *RH as* the Koopman dynamics on `ℝ × \hat{ℤ}`, prime-power events as
  first entrances into `p^kℤ_p`, half-density `‖1_{p^kℤ_p}‖_{L²} = p^{-k/2}`. *The wall:* the CRT/profinite
  diagonal factorizes and is RH-inert (meta-theorem); the "Profinite Successor Gram" theorem is
  UNVERIFIED. `STAGE-RECONSTRUCTION` + `REFORMULATION→WALL`. *(profinite-successor.)*

## 8.4 Diophantine lens

- **ℚ-independence / FUCC = Pascal.** *RH as* the geometry of the step-set `{\log p}` (independent over
  `ℚ`); multiplication by `m` is translation by `\log m`, giving the generalized Pascal matrix
  `P(a)P(b) = P(a+b)`, and `K_{Ψ,L} = Π G_L Π^T`. *The wall:* congruence preserves inertia, so
  `G_L ⪰ 0 ⟺ K ⪰ 0`, and `G_L` is the zero-moment matrix — recovering it from the arithmetic *is* the
  explicit formula again. `REFORMULATION→WALL`, RH-inert as a construction. *(pascal-fucc,
  composition-augmentation.)*
- **Subcritical conductor discrepancy (Mertens / Nyman–Beurling).** *RH as* `E_d(X) = X^{o(1)}` for all
  `d ∈ (0,½)`, where `E_d` is the summatory error of the conductor weights, Dirichlet series
  `ζ(s+d)/ζ(s+1-d)` — a tilted Mertens/Landau object; an off-line zero is a power-law gain mode, and at
  `d → 0` the discrepancy collapses to the sawtooth `-\{X/d\}`, the classical Landau/Nyman–Beurling
  identity `Σ μ(d)/d\{X/d\}`. *The wall:* a cancellation theorem for `μ(d) ×` carry-phase; the
  Nyman–Beurling → Suzuki operator map is not built. `REFORMULATION→WALL`. *(discrete-conductor-suzuki.)*
- **Forbidden-ratio / forbidden-composite-atom filter.** *RH as* a *constraint* on any physical Weil
  pushforward: it may carry delta atoms **only** at `±\log p^k`. Mixed-composite atoms `\log(pq)`
  (`Λ(pq) = 0`) and ratio atoms `\log(p^j/q^k)` (distinct primes) are forbidden; a naive cubical shorting
  for `\{2,3\}` illegally produces a `\log 6` atom. *The wall:* this is a **falsifier filter**, not a
  positivity theorem — a necessary condition a construction must pass, together with reproducing the exact
  Γ/pole/boundary scalar and all-`ω` Hardy causality. `REFORMULATION→WALL` (a sharp no-go test).
  *(rh-log-bathtub-prime-shift, cube-atom audit; it is the mechanism that walked back the cubical
  proof-attempt, [§8.6](#86-genuinely-new-sub-lenses).)*

## 8.5 Dynamical lens

- **SUCC-lightcone / von Koch distortion.** *RH as* `-\log δ_N = N + O(√N\,\log²N)` for
  `δ_N = \mathrm{lcm}(1..N)^{-1} = e^{-ψ(N)}` — exactly the classical von Koch equivalence
  `ψ(x) = x + O(√x\,\log²x)`, with the critical amplitude `p^{-1/2}` as normalized branching. *The wall:*
  it is a geometric dress for a standard RH-equivalent estimate. `REFORMULATION→WALL` (classical).
  *(prime-index-succ, lightcone-stability.)*
- **Lightcone gain cocycle.** *RH as* a zero Lyapunov exponent: `2\log G_N = ψ(N) − N`, PNT iff the gain
  cocycle is flat, RH iff `\log G_N = O(√N\,\log²N)`; under the explicit formula an off-line zero is a
  hyperbolic gain mode `e^{(β-½)t}`. *The wall:* causality/isometry give no bound — any integer branching
  schedule has the same isometries with arbitrary relative gain. "Recovers Suzuki, no new criterion"
  (the branch). `REFORMULATION→WALL`. *(lightcone-stability.)*
- **Self-sieving carry curvature.** *RH as* the global assembly of a causal carry machine: SUCC =
  carrier + boundary carry, Euler factor = carry-response filter, and the von Mangoldt measure is the
  **carré-du-champ of carry curvature** — but *locally*. *The wall:* the curvature positivity is of the
  form `A^*A`, per-prime, so RH-inert by the meta-theorem; the global assembly diverges (`Σ_p M_p ∼ 2√{e^L}`)
  and needs the indefinite pole renormalization. `STAGE-RECONSTRUCTION`. *(self-sieving-carry.)*
- **Prime-transport martingale (stochastic order).** *RH as* an ordered-transport cost inequality
  `(R2): ∫T\,dλ − ∫T\,dα ≤ E` per recovered episode (`= J_q ≤ C_q`, RH-equivalent). *You get*
  unconditionally: a stochastic order `α ≤_{st} λ` (an ordered positive coupling exists), **no** martingale
  coupling (means differ), and the optimal `W_1` cost `= ∫Y\,dt`. *The wall:* the transport positivity
  *exists but pays nothing* — the cost is the unpaid debit; and the pinned-tail constructor was **refuted**
  at a certified witness beyond `10^{10}`. `REFORMULATION→WALL`, new sub-lens (peacocks).
  *(prime-transport-martingale.)*
- **Causal filtration / fresh-digit isometry — the one genuine conservation law.** *RH as* an
  increasing-filtration actualization ("only encountered events affect the next"). *You get* a real,
  non-circular isometry `W_{p,ω} = p^{-ω}J + √{1-p^{-2ω}}\,V`, `W^*W = I`, with the fresh-innovation
  probability equal to the exact local factor `1 - p^{-2ω}`, plus a carry 2-cocycle that is nontrivial
  exactly at repeated prime-power depths. *The wall:* it conserves norm **inside the finite source** and
  is **mutation-insensitive** — replace the rates `2\log p` by arbitrary `λ_p > 0` and the isometry
  survives; only the exact ζ-coupling disappears. So it is genuine mathematics and **RH-inert**.
  `STAGE-RECONSTRUCTION` (with real content). *This is the closest thing in the whole repo to
  "genuine non-circular content," and it still does not touch the completed sign.*
  *(causal-filtration-energy.)*
- **de Bruijn–Newman heat flow.** *RH as* `Λ ≤ 0` (the dBN constant), with a zeta zero `β+iγ ↔` a dBN zero
  at `γ - i(β-½)`, so `b = β - ½` is the one shared coordinate and the zero flow is a Coulomb-gas gradient
  dynamics. *The wall:* Rodgers–Tao proved `Λ ≥ 0` (the wrong direction); no theorem expresses `Λ ≤ 0` as
  an energy/positivity criterion; the identification is tautological, and the branch retracts its earlier
  oversell. `REFORMULATION→WALL` (tautological). *(heat-flow.)*

## 8.6 Genuinely new sub-lenses (outside the six)

These are lenses the frame generated that are *not* variants of the six. All are still RH-equivalent or
RH-inert; they are listed because they are genuinely different *pictures*.

- **Arithmetic Hodge-index / Arakelov.** The cubical `(ℙ¹)^m` Hodge-Riemann picture ([§8.3](#83-adelic--tate-lens));
  the Dirac superconnection `𝒟 = ∇ + ∇^*` with `𝒟² ⪰ 0` and Schur-shorting of hidden faces. Walked back
  by the forbidden-composite-atom selection rule (`\log 6`, `\log(2/3)` atoms Γ cannot cancel). The
  function-field model (where this *is* a theorem, via Hodge index on `C×C`) is the stated analogy — but
  Spec ℤ has no verified square host. `STAGE` + unbuilt target.
- **Curvature / holonomy (GR-shaped).** The divisibility lattice as a causal set, support-time lag
  `ΔA(n) = ½\log(n/h(n)) ≥ 0` (equality iff prime power), and a conjectured identity "plaquette holonomy
  curvature = Levi-Civita curvature of the det₃ Hessian." UNVERIFIED; the branch states it may be
  "mathematically real but RH-inert." *(actualization-curvature.)*
- **Coulomb gas.** The dBN zero flow as `∂_t x_k = 2Σ' 1/(x_k - x_j)` ([§8.5](#85-dynamical-lens)).
- **Stochastic order / peacocks.** Prime-transport as a convex-order (peacock) problem
  ([§8.5](#85-dynamical-lens)).
- **Complexity / addition-chain crests.** Primes as martingale midpoints of old-generated numbers;
  integer-complexity strata. **Refuted** (Astra R003: moment-cone and primitive-support no-gos; the signal
  is weight-mutation-blind, hence cannot carry the sign). `NO-GO`.
- **Prime-index / Wold-defect.** A second successor axis `𝒫|n⟩ = |p_n⟩`, superprimes as nested ranges.
  RH-inert: superprimes do not carry the prime-zeta singularity, and the critical-half-density bulk still
  diverges. *(prime-index-succ, prime-index-lift.)*

## 8.7 The graveyard (proved or measured dead — do not re-dig)

Collected from the branches' own hostile controls and audits, so no one re-walks them:

- The product formula cancelling `ΣM_p` (it is a modulus identity; measured quadratic divergence).
- Any commutative-multiplicative / factorized / direct-sum positivity (meta-theorem; also the convolution
  transfer `Σ p^{-s} T_{\log p}`).
- Impedance/Laplace one-port and fixed-`κ` Krein escape (`inf\,Re\,F_P → −∞`).
- Single-space de Branges `H(E)` positivity (Conrey–Li, for ζ and `L(s,χ_{-4})`).
- Superprimes in place of primes (bulk still diverges).
- Midpoint-martingale / barycentric tower matching (Astra R003).
- Edge-square with independent endpoint channels or finite boundary completions (infinite negative index).
- Fixed integer-log observation maps (invisible positive subspace, `W ≥ 1.3544‖f‖²`).
- Naive cubical shorting (`\log 6` / `\log(2/3)` atoms).
- `Re\{ξ(s)/ξ(s+1)\} ≥ 0` as an equivalence (false; [§8.2](#82-operator--passivity-lens)).
- Heat flow as a proof route (`Λ ≥ 0` is the wrong direction).
- Pinned-tail transport constructor (refuted past `10^{10}`).

## 8.8 The convergent lesson

Strip the catalogue down and one sentence survives, said by five lineages in six vocabularies: **every
positive object anyone can build from the primes alone is per-prime and therefore RH-inert; the sign of
RH lives in the global, Archimedean-coupled, cross-prime completion — the Weil positivity — and nobody
has built it.** The catalogue's value is not a route; it is a *fence*. It marks, precisely and with
proofs, where the walls are, so the search can spend itself on the one object that is actually open
([the joint coercivity](06-state-of-the-program.md)) instead of re-deriving Bost–Connes for the
twentieth time.

## 8.9 Postscript: the QM / path-integral reading (the canonical illustration of §8.8)

A natural and genuinely beautiful lens, and the cleanest demonstration of §8.8's lesson: read the
sum over arithmetic paths `1 → n` as a Feynman path integral, with `●`-log-length as the action and
`succ`-count as the time. It unifies the dynamical and operator lenses, and every piece has a name —
but a targeted literature map (read-only) found it is RH-equivalent or inert at every turn, and it
corrected two hopeful guesses.

- **The landmarks.** The weighted path sum is the dynamical zeta `−ζ'/ζ` (Berry–Keating); primes =
  periodic orbits, `log p` = action, the explicit formula = the Gutzwiller/Selberg **trace formula**;
  the zeros = the spectrum; RH ⟺ the path integral is unitary / the Hamiltonian self-adjoint
  (**Hilbert–Pólya**, a *program*, not a theorem). `ζ`-as-gas = the **primon/Riemann gas** (Julia;
  Bost–Connes QSM) with its phase transition at `β = 1` — **the pole, not the zeros**. `C×C` where RH
  *is* proved = Weil's function-field surface (positivity from the Hodge index — and it needs **no**
  instanton; the classical path simply realizes). `ℕ` = Spec ℤ with no such surface = Connes–Consani.
- **Crisp inertness (quotable).** The primon Hamiltonian `H = log n` **is** self-adjoint, real
  spectrum — the framing's wish granted for free — yet the zeros live in the **analytic
  continuation** of the partition function, *not* in the spectrum of `H`. So "RH ⟺ `H` self-adjoint"
  misidentifies where the zeros are. The operator whose spectrum *would* be the zeros is
  Berry–Keating's `H = xp`, and it has **no self-adjoint realization** on the natural space
  ("closing the phase space is the central unsolved problem," in the authors' own words). That
  unsolved self-adjoint **extension**, closed by the archimedean place, is the wall in its most
  canonical operator form — the same object as the missing archimedean partner of the affine lens
  ([§8.3](#83-adelic--tate-lens)).
- **The braid is kinematics, not an interaction.** `V_m S = S^m V_m` is realized exactly as Cuntz's
  `Q_ℕ`, but it is the `ax+b` covariance (the discrete skeleton of `xp`), the dynamics
  `λ_t(s_n) = n^{it}s_n` acts freely, and the state is the unique KMS one — RH-inert. No source treats
  it as the non-free "interaction vertex" a tunneling event would need. `NO-GO` for "the braid is where
  the instanton hides," as stated.
- **Resurgence (the one checked crack): real, but inert, and the sign is backwards.** There *are*
  resurgent structures near `ζ` — Berry's Riemann–Siegel resummation, Voros's exponential asymptotics
  of the Li/Keiper coefficients, the Stirling/Bernoulli series. But (i) the one published "instanton"
  (Berry–Keating's `e^{-\pi t}`, period `iπ`) is the **archimedean Γ-factor's** Stirling singularity,
  known exactly — not a new zero mechanism; (ii) in Voros's rigorous saddle picture the
  non-perturbative sector is the **off-line** zeros, i.e. RH being *false* — so a tunneling event is
  the **counterexample**, not the proof (RH = that sector is **empty**); and (iii) the hoped-for
  "the divergent prime sum `Σ Λ(n)/√n ~ 2√X` is the Borel fingerprint of the zeros" is a **category
  error** — that is a power-law (pole) divergence, renormalized by subtraction, whereas a
  Borel/instanton fingerprint is *factorial* (Gevrey-1). A power divergence has no Borel plane. The
  only Gevrey-1 series near `ζ` encode the archimedean place + the functional equation.
- **Verdict.** `REFORMULATION→WALL`. The QM reading is the most canonical *statement* of the wall
  (self-adjoint extension of the `xp`/braided generator, closed by the archimedean place) and hands
  over a different toolbox (non-perturbative QFT) aimed at the known Connes–Consani wall — but it adds
  no crack, and it clarifies that the non-perturbative sector is the *obstruction*, not the mechanism.

---

**Back to:** [Wiki index](README.md) · [5 What ζ is, from every side](05-what-is-zeta-here.md) ·
[6 State of the program](06-state-of-the-program.md) · [7 Methodology](07-methodology-and-discipline.md)
