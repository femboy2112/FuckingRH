# Finite completion + Schur complement: the Laplace-source completion is not passive (ckpt8)

**Date:** 2026-10-06. **Status:** DISCLOSED (measured no-go + unconditional mechanism). **RH open.**
**Reproduce:** `scripts/finite_completion_test.py`, `scripts/finite_completion_index.py`.

This is the crack-or-die experiment of §§8, 12, 16. Result: **die**, cleanly, for the natural
(Laplace/source-response) finite-completion class — and with a precise, RH-independent reason.

## The Schur complement of an independent-ray star is just the sum of rays

The Feshbach/Schur object `M_X(z) = A_X(z) - C_X^* D_X(z)^{-1} C_X` for the source star (one center `Ω`,
arms = prime rays, internal dynamics the depth shift) eliminates the internal rays and returns
`A_X - Σ_p (arm response)`. With arithmetically-forced couplings the arm response on ray `p` is exactly
`m_p(s) = log p/(p^s-1)` (the depth-shift resolvent at `ζ=p^{-s}`), so

    M_X(s) = A_{inf}(s) - Σ_{p≤P} m_p(s).

An **independent-arm** star gives precisely the **sum** — no cross terms — so by C103 it is RH-inert for
positivity. Cross-coupling can only come from an operator that does not respect unique factorization, i.e.
the additive `SUCC` (which maps `|p^k> → |p^k+1>`, jumping between rays) — the Round004/005 irregular
braid. The star alone adds nothing beyond §5.

## The explicit pole-cancelling finite boundary (§16 done)

The naive `M_X` has the `κ=1` pole at `s=1` (C105). Cancel it with the Euler–Maclaurin counterterm

    reg_P(s) := ∫_1^P x^{-s} dx = (1 - P^{1-s})/(s-1)   →  1/(s-1) on Re s>1,  = log P at s=1 (entire),

giving the completed finite object

    A_{inf,P}(s) := 1/s - ½log π + ½ψ(s/2) + reg_P(s),
    F_P(s) := A_{inf,P}(s) - Σ_{p^k≤P} Λ(p^k)(p^k)^{-s}.

Verified: `F_P` is **holomorphic on `H_{1/2}`** (finite at `s=1`), and `F_P → xi'/xi` locally uniformly
on `Re s>1` (`err ~ 1e-6` at `P=2000`, `s=2+i`). So `F_P` meets hypothesis (E) and the holomorphy half of
(P). Its "prime part" `reg_P - Σ_{n≤P}Λ(n)n^{-s} = -∫_1^P x^{-s} d(ψ(x)-x)` is literally the
explicit-formula fluctuation.

## The positivity test (the point)

`min Re F_P` over grids in `H_{1/2}` (`finite_completion_test.py`):

| `P` | min Re F_P on strip (½,1) | locus | min Re F_P on Re s>1 |
|---|---|---|---|
| 200 | **−2.02** | `0.52 + 48.9 i` | −0.011 (boundary artifact) |
| 2000 | **−1.88** | `0.52 + 72.6 i` | +0.022 |
| 20000 | **−2.44** | `0.52 + 77.6 i` | +0.023 |

`F_P` is **not positive-real on `H_{1/2}`**: strongly negative near the critical line (`σ→½⁺`), and it does
**not** improve as `P` grows. On `Re s>1` it is `≥0` (consistent with the unconditional Lagarias (1.4)).

## Why it fails — unconditional, RH-independent (`finite_completion_index.py`)

Near `σ=½`, `F_P` is dominated by the finite von Mangoldt fluctuation
`Σ_{n≤P}Λ(n)n^{-σ}e^{-it log n}`, whose max-over-`t` amplitude grows like `P^{1-σ}/(1-σ)`, dwarfing the
`~log t` Archimedean. Measured on `σ=0.51, t∈[0,300]`:

| `P` | max\|Re F_P\| | min Re F_P | # excursions `Re F_P < -a` (a=1) |
|---|---|---|---|
| 200 | 6.83 | −3.31 | 108 |
| 2000 | 9.29 | −3.64 | 205 |
| 20000 | 11.21 | −4.72 | 291 |
| 200000 | 13.20 | −5.08 | 362 |

Two consequences, **both independent of RH**:

1. **(P) fails for the Laplace-source class, unconditionally.** `max|Re F_P| → ∞` near the line, so `F_P`
   is not positive-real for any large finite `P`. The source response *is* the Laplace transform of the
   von Mangoldt measure (ckpt4–5), and Laplace completions expose the raw `P^{1-σ}` fluctuation; no choice
   of the (pole-cancelling) Archimedean boundary removes it.
2. **The finite-`κ` Krein/Pontryagin escape (§19) is closed for this construction.** The negative index
   `κ_P` = #{poles of `Cayley_a[F_P]` in `H_{1/2}`} = #{`Re F_P < -a` excursions} **grows with `P`**
   (108 → 362 on a fixed window). So there is no fixed-finite-negative-index parent for the completed
   source response built this way; the index diverges.

## Verdict and the one surviving door

The RH content **cannot** be reached by completing the source *impedance* `F_P` and hoping it is passive —
it provably is not, and its Pontryagin index diverges. The only way (P) can still hold is to enforce
contractivity **structurally**: a finite **unitary/passive colligation** whose transfer function
`Θ_X` satisfies `|Θ_X| ≤ 1` on `H_{1/2}` *by the unitarity of the colligation*, regardless of how wild the
associated impedance is. That requires a **positive-definite** state-space metric and a dissipative
generator supplied by the arithmetic. ckpt8 shows the impedance-based metric is **indefinite with
diverging index**; whether a different, genuinely coupled (SUCC-braided) colligation supplies a positive
metric is ckpt9 — and it is exactly where Conrey–Li/Sarnak predict failure. 

## Ledger

New row **C106**: the Euler–Maclaurin pole-cancelling boundary `reg_P=(1-P^{1-s})/(s-1)` makes the finite
completion `F_P = 1/s-½log π+½ψ(s/2)+reg_P - Σ_{p^k≤P}Λ n^{-s}` holomorphic on `H_{1/2}` and `→xi'/xi` on
`Re s>1` (hyp E ✓). But `F_P` is NOT positive-real on `H_{1/2}`: `max|Re F_P| ~ P^{1-σ} → ∞` near the
line (measured; unconditional), and the Pontryagin index `κ_P` (excursion count) grows with `P`
(108→362). Kills the Laplace/source-response finite-completion class for Schur-Vitali (P), and closes the
finite-`κ` Krein escape. Passivity, if attainable, must be structural (unitary colligation), not from
completing the impedance.
