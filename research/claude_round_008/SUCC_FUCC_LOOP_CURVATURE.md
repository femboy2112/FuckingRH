# Arithmetic interaction curvature: SUCC/FUCC loops, prime-ray flatness, and the counterterm

**Round 008. Branch `claude/arithmetic-curvature-loops-008` (from the Suzuki finite-conductor
frontier `aletheia/finite-hankel-contraction-frontier-2026-10-07`, head `0840c39`).**
**RH IS OPEN.** **Reproduce:** `scripts/r008_loop_curvature.py` (all checks pass; no zeta zeros).

This note takes an externally-supplied geometric intuition — *"a category of arithmetic/algebraic
phase changes whose graph closes into complete cycles; can the loops carry weight/energy; is that
the arithmetic interaction curvature?"* — and pins it, exactly, onto the live wall of the
finite-conductor arc. The result is a **location theorem**: the entire difficulty of the Suzuki
localized-Weil positivity is concentrated in one place, the SUCC↔FUCC non-commutator, and the
prime arithmetic itself is *flat*. This reproduces, from the loop side, the frontier's own verdict
(`DISCRETE_CONDUCTOR_SUZUKI_FACTORIZATION.md §13`: *"the remaining wall is Archimedean boundary
realization, not arithmetic bookkeeping"*). It is RH-inert — it relocates the wall, it does not
breach it.

---

## 0. The objects

- **SUCC** `T: x ↦ x+1` (the additive/Archimedean generator) and its inverse.
- **FUCC** `D_p: x ↦ p·x` for each prime `p` (the multiplicative generators) and inverses.
- The **succ-form graph** `G`: vertices `ℚ_{>0}` (or a finite window of `ℕ`), directed edges the
  elementary moves above and their rational affine composites `x ↦ (ax+b)/c`. Each edge is an
  element of the affine group `ax+b` over `ℚ`, i.e. a matrix `[[a, b],[0,1]] ∈ GL₂(ℚ)` acting by
  `x ↦ ax+b`.
- A **succ loop** is a closed walk: a word `w` in the generators that returns its basepoint to
  itself.

---

## 1. A loop is a relation (closed word = identity)

**Observation.** The user's Collatz-side loop

\[
3 \;\xrightarrow{\,4x+1\,}\; 13 \;\xrightarrow{\,(3x+1)/8\,}\; 5 \;\xrightarrow{\,(2x-1)/3\,}\; 3
\]

composes to the **identity affine map** `x ↦ x`, not merely to a map fixing the point `3`
(verified symbolically). So a closed succ loop is a **relation in the affine groupoid**: a
nontrivial word equal to the identity element.

Its content is the *word*, not the endpoint. Two balances hold simultaneously:

- **Multiplicative balance.** The product of the linear parts is `4 · (3/8) · (2/3) = 1`: the
  numerator mass `4·3·2 = 2³·3` cancels the denominator mass `8·3 = 2³·3`. The primes `{2,3}`
  balance exactly — a *coherent syzygy* (the user's "`2a − 3b` with `a,b` coherent", here the
  balanced multiset `{2³,3}` up and down).
- **Additive balance.** The `+1,+1,−1` offsets cancel through the braid (below) to close the loop.

This is the general shape: **a succ loop is a simultaneous multiplicative and additive balance
condition** — a word in SUCC and FUCC whose group element is `1`.

---

## 2. The curvature is `[SUCC, FUCC]` — and nothing else

The multiplicative group `⟨D_p⟩_p` is **abelian** (`D_pD_q = D_qD_p`, i.e. `pq = qp`). The additive
group `⟨T⟩` is a single `ℤ`. The only non-commuting pair is successor-against-dilation, the repo's
affine braid:

\[
D_p T D_p^{-1} = T_p,\qquad\text{equivalently}\qquad
D_pT - TD_p \;=\; (p-1)\quad(\neq 0).
\]

(Verified: `(D_p∘T)(x)=p(x+1)=px+p` vs `(T∘D_p)(x)=px+1`, defect `p-1`.)

> **Definition (arithmetic interaction curvature).** The curvature of the succ-form graph is the
> non-abelian holonomy of its loops, and its *only* generator is the braid defect `[T, D_p]=p-1`.
> SUCC is flat; FUCC is flat; the curvature is entirely in their coupling.

---

## 3. FUCC is flat (the clean theorem)

**Theorem 1 (prime-ray flatness).**
In log-coordinates `u = log x`, each `D_p` is the translation `τ_{\log p}: u ↦ u + \log p`. The
pure-FUCC subgraph is the Cayley graph of the free abelian group `⨁_p ℤ` with generators
`{\log p}`. Then:

1. **Every pure-FUCC loop carries zero net log-displacement.** A closed FUCC word is a signed
   multiset `∑ m_p · \log p` with net value `0`; by unique factorisation (UFD), `∏ p^{m_p} = 1`
   forces every `m_p = 0`. Equivalently, `{\log p : p\ \text{prime}}` is **ℤ-linearly independent**
   (verified: `\min_{0<|{\bf m}|≤8}|m_2\log2+m_3\log3+m_5\log5| ≈ 4.7\times10^{-3} > 0`).
2. **Every pure-FUCC loop is a consequence of commutativity** `[D_p, D_q]=0` (the 4-cycles
   `x\xrightarrow{p}px\xrightarrow{q}pqx\xrightarrow{1/p}qx\xrightarrow{1/q}x`). Holonomy is trivial.
3. **Consequence.** The prime-ray translation energy is a function of net displacement only; it is
   **curl-free** — a pure gradient (potential) energy with no loop (circulation) content.

So UFD = the *fundamental theorem of arithmetic* is, verbatim, the statement **"the prime-ray graph
closes no loop of nonzero displacement"**: the multiplicative world is flat, a tree-of-abelian-grids
with no holonomy.

This is exactly why the frontier's prime-ray Dirichlet energy

\[
\mathcal{E}_{\mathrm{prime},a}(v)=\sum_{p^k\le e^{2a}}\frac{\log p}{p^{k/2}}\,
\|v-\tau_{k\log p}v\|^2
\]

(WEIL_PRIME_RAY_DIRICHLET_FORM.md) is manifestly a *positive gradient energy* and never the source
of a sign problem: a flat (curl-free) field has no obstruction of its own.

---

## 4. The counterterm is the graph degree — so the coupling is mandatory

Write the prime part of Suzuki's global counterterm:

\[
\mathcal{V}_a^{\mathrm{prime}} \;=\; 2\sum_{p^k\le e^{2a}}\frac{\log p}{p^{k/2}}
\;=\; 2\cdot(\text{total edge weight of the prime-ray graph})\;=\;2\deg.
\]

(Verified: `a=1.0 → 5.852`, `a=1.5 → 13.016`, `a=2.0 → 24.383`, matching
`𝒱_a = 2A+1 + 2∑ \log p/p^{k/2}` once the Archimedean `2A+1` is added.)

In graph-Laplacian language `⟨Lv,v⟩ = ∑_e w_e\|v-\tau_e v\|^2`, the number `2\deg` is the *diagonal
mass*: what the energy would be if every shift had disjoint support (`\|v-\tau v\|^2 = 2\|v\|^2`).
The localized-Weil positivity `Q_W^a(v)≥0` is, in these coordinates,

\[
\underbrace{\mathcal{L}_a(v)}_{\text{Archimedean (}\sim|\xi|\text{)}}
\;+\;
\underbrace{\mathcal{E}_{\mathrm{prime},a}(v)}_{\text{prime-ray, flat}}
\;\ge\;
\mathcal{V}_a\|v\|^2+\langle R_av,v\rangle .
\]

**Theorem 2 (the coupling is structurally necessary).**
The prime-ray Laplacian annihilates constants: `𝓔_{prime,a}(\mathbf 1)=0`, while
`𝒱_a\|\mathbf 1\|^2>0`. Hence **no flat (prime-ray-only) bound can dominate the counterterm.** The
low-frequency / constant direction must be controlled by the Archimedean channel `𝓛_a` (symbol
`∼|\xi|`, vanishing only at `\xi=0`, where the `H^1_0(-a,a)` boundary condition and the
`-\tfrac12\log(a^2-x^2)` potential take over). The sign battle is therefore *never* inside the
prime arithmetic; it is the **coupling** between the flat prime-ray field and the Archimedean
successor field — i.e. the curvature `[T,D_p]`.

---

## 5. What this says about the wall (honest)

The frontier wall (CONDUCTOR_FIRST_JET §9, WEIL_PRIME_RAY §6) is:
*"why does the global Archimedean/diagonal counterterm never overwhelm the combined continuous +
prime-ray difference energy?"* Theorems 1–2 re-express it precisely:

> **Relocation.** The prime side is flat (Theorem 1), and the counterterm is its degree (Theorem 2),
> so the counterterm is paid *only* by circulation that crosses between the prime-ray field and the
> Archimedean field. **RH, in this coordinate system, is a nonnegativity of arithmetic interaction
> curvature**: the braid coupling `[T,D_p]` must deposit exactly enough cross-energy to cover the
> degree, never less.

This matches, and sharpens, the frontier's own `DISCRETE_CONDUCTOR §13` ("Archimedean boundary
realization, not arithmetic bookkeeping") and its proven negative (`CAUSAL_TOEPLITZ §5–6`:
`g(a)=1-\|H_{1/2,a}\|\to0`, so no horizon-uniform gap can exist). A curvature/holonomy proof must
therefore be of the **marginal/critical** type — it cannot leave a fixed buffer — and must live in
the cross term, exactly where Theorem 2 forces it. The user's instinct ("loops carry weight = the
interaction curvature") is correct and now *located*; it does not, by itself, supply that bound.

---

## 6. Ledger

- **C105 (RH-inert, structural).** *Loop/curvature location.* Closed SUCC/FUCC succ-loops are
  relations (identity words) subject to simultaneous multiplicative (UFD) and additive balance. The
  pure-FUCC subgraph is flat: every loop has zero net log-displacement and trivial holonomy (UFD =
  {log p} ℤ-independent), so the prime-ray Dirichlet energy `𝓔_prime` is curl-free. The only
  curvature generator is the braid `[T,D_p]=p-1`. Suzuki's prime counterterm equals twice the
  prime-ray graph degree, and the prime-ray Laplacian annihilates constants, so the counterterm
  cannot be dominated by `𝓔_prime` alone — the Archimedean coupling is mandatory. Hence Suzuki
  positivity `Q_W^a≥0` is a nonnegativity statement about the **cross (curvature) energy**, not the
  (flat) prime arithmetic. Locates the frontier wall; no RH progress. `scripts/r008_loop_curvature.py`.

RH remains open.
