# The target global factor: the architecture, and exactly where it stalls

**Round 006. RH IS OPEN.** This note states the strongest architecture the inverse-affine completion
suggests, and locates — precisely — the one step that does not close. See `PROOF_ATTEMPT_006.md`.

## The desired architecture (directive §17)

    invertible rational/adelic affine parent  Q ⋊ Q^×  on  l²(Q) / L²(A_Q)
        → universal bilateral SUCC/FUCC geometry        [RATIONAL_AFFINE_PARENT]
        → stratified prime sheets, identical SUCC form   [PRIME_JET_STRATIFICATION]
        → history/carry boundary operator  I−S           [BILATERAL_SUCC_TOEPLITZ]
        → INTERSECT BEFORE SQUARING                       [INTERSECT_BEFORE_SQUARING]
        → compression to the positive integer corner      [INTEGER_CORNER_DEFECTS]
        → completed Archimedean coupling (Γ / half-density)[ADELIC_HALF_DENSITY]
        → arithmetic B
        → K_Ψ = B^* B                                     (RH ⟺ K_Ψ ⪰ 0)

The **non-circular** requirement: build `B` independently of zeta zeros, `√K_Ψ`, Cholesky,
eigendecomposition of `K_Ψ`, or assuming RH — then prove `K_Ψ = B^*B`.

## What this round delivered toward it (all exact, all RH-inert)

- The parent, the compression, and the generators are realized exactly, and identified as the
  **Bost–Connes + Cuntz `Q_ℕ`** system (`LITERATURE_INTERFACE`).
- The universal boundary is pinned: `I−S = T_{1−z}`, with `E_S = I−SS* = [S*,S] = |1><1|` the rank-one
  compression defect; `Λ_op`, `H_log` realized diagonally; `B_p` realized as an exact analytic-Toeplitz
  local factor. Every ingredient of the architecture up to "arithmetic `B`" is in hand, in closed form,
  zero-free.

## Where it stalls — three precise markers on the wall

The architecture stalls at the single arrow **`intersect before squaring → B`**, and this round pins why,
three ways:

1. **Assembly amplifies, not cancels (C101).** With the *universal* boundary `(I−S)` the sheets share a
   common mode; assembling before squaring diverges **quadratically** (`~π(N)²`), strictly worse than the
   direct sum's `π(N)`. A working `B` needs a **prime-specific, sign-structured** wiring whose cross terms
   cancel the bulk. The only such object in the program is the **Weil explicit formula** (signed prime ×
   prime and prime × Archimedean terms). So "intersect before squaring, done correctly" *is* the Weil
   distribution — and its positivity is RH.

2. **The balance is algebraic, the cancellation is analytic (C102).** The adelic product formula
   `∏_v|q|_v=1` is a *modulus* identity; it does not subtract the additive bulk `Σ_p M_p`. The cancellation
   that produces a finite completed object is the functional equation's `Γ`-factor/pole — an **analytic
   continuation**, not an algebraic assembly.

3. **Group completion ≠ analytic continuation (C103).** The affine completion reproduces the arithmetic
   only in `Re s > 1` (where the semigroup presentation is literal); the step into the critical strip is an
   **extra analytic datum** (the functional equation = Archimedean `Γ` + product formula), which — as the
   Bohr–Mollerup control for `Γ` shows in miniature — a group/measure completion structurally cannot
   supply. RH is a statement about the *continued* object; it is invisible to the algebra that this round
   makes exact.

## Status of the target

Not achieved, and now understood as **not achievable by this family of moves**: every route from the
invertible parent to a global positive `B` either (i) stays in the commutative multiplicative algebra
(factorized/GCD, RH-inert, C89), (ii) uses a common-mode boundary (quadratic divergence, C101), or (iii)
needs the analytic continuation the completion cannot produce (C102/C103). The missing object is identified
exactly — the **signed Weil cross terms / the analytic positivity of the Weil distribution** — which is the
Connes gap (`LITERATURE_INTERFACE §3`) = Weil positivity = RH. The inverse-affine parent gives the cleanest
coordinates yet for the *prime side* and the *boundary*, and a sharp proof that the *completion* is where RH
hides. It does not give `B`.
