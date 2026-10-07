# Round 010 — attack on `Ψ≥0` (curvature reserve) + the factorization tensor skeleton

**Branch `claude/arithmetic-curvature-loops-008` (continuing on the Suzuki finite-conductor frontier).**
**RH IS OPEN.** **Outcome (2):** an **exact reduction** of Suzuki's RH-equivalent `Ψ≥0` to a single
curvature-balance inequality, with a **genuinely unconditional (PNT)** total `O(√X)` cancellation as the
sharp new fact — and the user's composite-factorization pattern formalized as the exact Euler/Möbius
tensor skeleton that it rides on. No RH progress; the wall is located with maximum precision and passed
through a hostile audit (AUDIT_010.md) that caught and removed real overclaims.

## Part A — the attack on `Ψ≥0`

Suzuki (JLMS 2023, Thm 1.7): `RH ⟺ Ψ(t)≥0`. Exact one-block decomposition `Ψ=A−P`:
- `A` = smooth **Archimedean reserve**; `P(t)=\sum_{n\le e^t}(\Lambda(n)/\sqrt n)(t-\log n)` = **prime
  ramp** (monotone, convex, piecewise-linear). Verified `A−P=Ψ` to `~10^{-15}`.
- Curvature form `Ψ=\int_0^t(t-s)[A''(s)-\sum_n(\Lambda(n)/\sqrt n)\delta(s-\log n)]ds`. `A''` changes
  sign at `s≈0.281` (`<0` on the prime-free `(0,0.281)`, `>0` for all `s≥\log 2`, where every impulse
  lives) — so, in the bulk, RH `⟺` the positive Archimedean curvature dominates the prime impulse train.

**The sharp fact (unconditional, PNT):** `A(t)` and `P(t)` both grow like `4e^{t/2}=4\sqrt X`, and the
**entire** `O(\sqrt X)` reserve cancels the **entire** `O(\sqrt X)` ramp (ratios → 1, `t=4..12`; `A,P≈1578`
at `t=12`). The remainder `Ψ=A−P` is `o(\sqrt X)` — small (`~0.03–0.06`) in the computed range.
**Honest boundary:** the leading cancellation is PNT (unconditional); the remainder's *boundedness and
positivity for all `t`* are each **RH-equivalent, not shown** (an off-line zero `β>½` makes `Ψ\sim
e^{(β-½)t}`, sign-indefinite). This reduces RH to: *"a single oscillation `A−P`, whose `O(\sqrt X)` bulk
is already cancelled unconditionally, must stay bounded and `≥0`"* — the smallest the target has been. The
block must never be split (`|.|`-estimating `P` is vacuous), and Conrey–Li 2000 refuted the de Branges
positivity route to exactly this remainder.

## Part B — the factorization pattern (the user's idea)

Writing each factor as `N=pa+b` and multiplying expands multilinearly, `\prod(p_ia_i+b_i)=\sum_S(\prod_S
p_ia_i)(\prod_{\bar S}b_i)`, graded by `|S|` = #prime-parts chosen. This is **exactly** the conductor
coefficient `b_ω(n)=n^{ω-1/2}\prod_{p|n}(1-p^{-2ω})=n^{ω-1/2}\sum_{d|\mathrm{rad}\,n}\mu(d)d^{-2ω}`
(verified), with subset size `|S|` = ω-jet order = `ν(n)` and leading `(2ω)^ν\prod\log p = b_0^{(ν)}`.

**Honest scope (post-audit):** for a *fixed* `n` this is a finite tensor over the primes `p|n`, exact
Möbius inclusion–exclusion — RH-inert per-`n` bookkeeping. But the **unrestricted** Euler product
`\prod_{\text{all }p}(1-p^{-2ω})=1/\zeta(2ω)` carries **every** zero, so "flat" is a per-`n` statement,
**not** a claim that the prime side of RH is analytically trivial. Its real use: it factors each conductor
coefficient into an independent prime tensor, and confirms the prime ramp `P(t)` (a monotone nonnegative
sum — *not itself a tensor*) has no internal sign cancellation. So the `Ψ=A−P` positivity obstruction
cannot come from re-organizing the primes; it lives in the `A−P` balance.

## The honest answer to "is there an exploitable arithmetic pattern in how composites factor?"

**Yes — as exact, finite bookkeeping** (the Euler/Möbius tensor skeleton; standard). It beautifully
organizes the ω-jet and the conductor coupling. **But it is RH-inert:** the pattern is the *flat*
multiplicative side, and summing it over all `n` just reconstructs `ζ` — the analytic content you need
reappears there, not in the combinatorics. The attack makes this precise: the prime side contributes a
total `4√X` that cancels unconditionally, and **everything that decides RH is in the Archimedean
continuation of the `A−P` remainder**, provably not in the factorization combinatorics.

## Honest status and next

Round 010 pushed the target to its sharpest form and verified the one genuinely unconditional gain (the
total PNT cancellation). It did **not** move RH, and the hostile audit removed every overclaim (the
"bounded" RH-leak, a false `A''>0`, and a tensor/flatness misattribution). The wall is exactly the one
every round reaches: the positivity (equivalently boundedness) of the `o(√X)` Archimedean-continuation
remainder = Weil positivity = `m_∞=−Ξ'/Ξ` Herglotz, refuted-as-naive-de-Branges by Conrey–Li 2000.

The only directions that are not provably flat/inert are the ones that act on that remainder directly:
the **Archimedean `Γ`-factor / functional-equation** object (construct it non-circularly), or the
**function-field analogue** where the corresponding positivity is a theorem. Both live on the dual side,
as every round since 006 has concluded.

## Ledger

- **C114 (round close).** Round 010 = Part A (attack: `Ψ=A−P`, exact; curvature form with `A''` sign-change
  at `s≈0.281`, `A''>0` for `s≥\log2`; **unconditional PNT total `O(√X)` cancellation** leaving an
  `o(√X)` remainder whose boundedness/positivity are RH-equivalent; reduces RH to the `A−P` balance) +
  Part B (the user's `N=pa+b` factorization = the Euler/Möbius subset-over-primes tensor skeleton =
  conductor coefficient `b_ω(n)`, exact finite per-`n` bookkeeping, RH-inert, scope-caveated by
  `\prod_{\text{all}p}=1/\zeta(2ω)`). Answer to "exploitable factorization pattern?": yes as bookkeeping,
  no for RH (flat side). Hostile audit (AUDIT_010.md) removed an RH-leak ("Ψ bounded"), a false `A''>0`,
  and a tensor misattribution. Wall unmoved (Archimedean continuation / Weil positivity; Conrey–Li 2000).
  Scripts r010_reserve_curvature, r010_factorization_tensor (both pass, no zeta zeros as input).

RH remains open.
