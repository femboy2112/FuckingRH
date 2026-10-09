# 2. The RH-equivalent target

*This page states the classical object the program aims at. Everything here is standard,
proved mathematics, cited to its authors. The frame of [page 1](01-the-successor-frame.md)
is a way of thinking about it; this is the thing itself.*

---

## 2.1 The completed zeta function

The Riemann zeta function `ζ(s) = Σ n^{-s}` (for `Re s > 1`, continued elsewhere) has an
Euler product `ζ(s) = ∏_p (1 - p^{-s})^{-1}` that encodes unique factorization. Its
**completion** folds in the archimedean factor of [§1.5](01-the-successor-frame.md):

```
ξ(s) = ½ s(s-1) π^{-s/2} Γ(s/2) ζ(s)
```

`ξ` is entire, and satisfies the functional equation `ξ(s) = ξ(1-s)` — the reflection across
the critical line `Re s = ½`. Its zeros are exactly the **nontrivial** zeros of `ζ` (the
Γ-factor's poles cancel the trivial zeros at `s = -2, -4, …`).

> **The Riemann Hypothesis.** Every zero of `ξ` lies on the line `Re s = ½`.

A crucial negative lesson the frame keeps front of mind: **the functional equation alone does
not imply RH.** The Davenport–Heilbronn function has a functional equation of the same shape
and a Dirichlet series, yet has zeros *off* the line. What `ξ` has and Davenport–Heilbronn
lacks is the **Euler product** (multiplicativity). Any route to RH must use multiplicativity
somewhere; symmetry is not enough. (This is made quantitative on
[page 4, §4.5](04-the-symbol-and-the-wells.md): a matched pair — Davenport–Heilbronn and a
genuine `L(s, χ)` sharing conductor, Γ-factor and functional equation, differing *only* by the
Euler product — measurably separates into an indefinite form and a positive one.)

## 2.2 Weil's explicit formula: zeros ↔ primes

The explicit formula pairs a test function `f` against the zeros and against the primes
simultaneously. Schematically, for a nice even `f` with transform `f̂`:

```
Σ_ρ f̂(γ_ρ)   =   [archimedean term in f]   +   [pole terms]   −   Σ_{p,k} (log p) p^{-k/2} [f at k·log p]
 └─ zeros ─┘       └────────── the "arithmetic side": Γ-factor digamma + the prime powers ──────────┘
```

The left side is a sum over the zeros `ρ = ½ + iγ_ρ`; the right side is built only from the
archimedean Γ-data and the von Mangoldt prime powers of [§1.3](01-the-successor-frame.md).
The two sides are *equal* — this is a theorem (Guinand–Weil). It is the exact bridge between
the dynamics (primes) and the spectrum (zeros).

## 2.3 Weil positivity ⟺ RH

Apply the explicit formula to a self-correlation `f = g ⋆ g̃`. Define the **Weil functional**

```
W(g) = Σ_ρ |ĝ(γ_ρ)|²      (the zero side of f = g ⋆ g̃)
```

Then:

> **Weil's criterion.** `W(g) ≥ 0` for all admissible `g`  ⟺  RH.

The direction that matters: if all zeros are on the line, every `γ_ρ` is real and the sum of
`|ĝ(γ_ρ)|²` is manifestly `≥ 0`; conversely a single off-line zero produces an admissible `g`
making `W(g) < 0`. So **RH is exactly a positivity statement** — and because the zero side
equals the arithmetic side (prime + archimedean), proving RH means proving that the
*arithmetic* side is non-negative *without ever looking at the zeros*.

This is the whole game. The program's target is: **an independent, non-circular reason the
prime-plus-archimedean form is positive.**

## 2.4 Equivalent reformulations used in this repo

Several exact restatements are used interchangeably; each repackages the same positivity.

- **Suzuki (JLMS 2023).** There is an explicit even function `Ψ(t)`, built from prime powers
  plus the archimedean completion, with

  ```
  RH  ⟺  Ψ(t) ≥ 0 for all t  ⟺  the Kreĭn screw kernel K_Ψ(t,u) = Ψ(t)+Ψ(u)−Ψ(t−u) ⪰ 0,
  ```

  and (Nakamura–Suzuki) `⟺ e^{-Ψ}` is an infinitely divisible characteristic function.

- **`ξ′/ξ` positive-real (Lagarias 1999; Hinkkanen).**

  ```
  RH  ⟺  ξ′/ξ is positive-real (Pick/Herglotz) on H_{1/2} = {Re s > ½}.
  ```

- **Passivity coordinates (this repo, Round 006).**

  ```
  RH  ⟺  Re{ ξ(s) / ξ(s+1) } ≥ 0 on H_{1/2}.
  ```

- **de Branges spaces (Lagarias; Suzuki).** Under RH the Weil-form Hilbert space is a de Branges
  space, and `E_h(z) = ξ(½ + h − iz)` is a de Branges structure function for every `h ≠ 0` iff
  RH. This is the natural "canonical system / string" home for the positivity — but the single-
  space version of the de Branges route is **known to fail** for `ζ` and for `L(s, χ₋₄)`
  (Conrey–Li), which is exactly why this program's live operator seam is a *second-jet, cross-
  place* coupling rather than a single-space contraction ([§5.4](05-what-is-zeta-here.md),
  [§6.4](06-state-of-the-program.md)).

These are **exact reformulations, not progress.** Moving between them reshapes the target; it
never reaches it. The variational form of the same object (Bombieri's Problems A/B — minimize
`Q(v)/‖v‖²` over a test space) is in the same boat: a minimizer exists, but bounding it below zero
*is* RH.

## 2.5 The free half, and the prime-free window

Two unconditional facts fix exactly how much is "for free" and how much is RH.

- **Above `Re s = 1` it is free.** The Euler product converges, `log ζ = Σ_{p,k} p^{-ks}/k`
  has non-negative coefficients, and positivity (`Re ξ′/ξ > 0` on `Re s > 1`; no zeros on
  `Re s = 1` by the classical `3 + 4cosθ + cos 2θ = 2(1+cosθ)² ≥ 0` argument) follows directly
  from multiplicativity. **All RH content is pushing positivity from `Re s > 1` down to
  `Re s > ½`.**

- **The prime-free window (Connes–Consani, *Theorem 1*, arXiv:2006.13771).** Unconditional
  positivity of the Weil form is known for test functions whose self-correlation is supported
  in `(½, 2)` — the window in which *no prime power log appears* — via the Sonin space /
  Toeplitz (Thm 6.11) route (Yoshida). This is the refereed, classical frontier of what
  positivity is unconditionally available.

  > *Historical note / correction.* Earlier internal notes mislabeled this as "Theorem 7.1,
  > positivity at the archimedean place." That was wrong on both counts and was corrected on
  > 2026-10-08 against the paper: it is **Theorem 1**, and it is the **prime-free support
  > window `(½,2)`**, not an "archimedean place" statement. The error and its correction are
  > logged (this is the kind of citation slip the methodology is built to catch — see
  > [page 7](07-methodology-and-discipline.md)).

The gap between "free above `Re s > 1`" and "known on `(½, 2)`" and "RH" is where every
construction in this repo lives and dies.

---

**Next:** [The Diophantine & semigroup frame →](03-the-diophantine-semigroup-frame.md) — why
the obstruction is really about the prime *frequencies*, and the finite-window operator model
that gives it a rigorous home.
