# Attack: `Ψ≥0` as the Archimedean curvature-reserve dominating the prime ramp

**Round 010 / Part A. Branch `claude/arithmetic-curvature-loops-008`.** **RH IS OPEN.**
**Reproduce:** `scripts/r010_reserve_curvature.py` (all checks pass; no zeta zeros used as input).

This is the attack both the Round-008 (curvature) and Round-009 (GR) pictures agreed was the real fight:
Suzuki's RH-equivalent `Ψ(t)≥0` (JLMS 2023, Thm 1.7), read as a **curvature-domination / integrate-and-
fire reserve** statement, kept in **one block**. Outcome: an **exact reduction** plus a sharp, striking,
verified fact — and an honest wall. No RH progress.

## 1. The one-block decomposition (verified)

`Ψ` is even, `Ψ(0)=0`, and splits exactly as `Ψ(t)=A(t)−P(t)`:

$$A(t)=4\big(e^{t/2}+e^{-t/2}-2\big)+\tfrac{t}{2}\big(\psi(\tfrac14)-\log\pi\big)+\tfrac14\big(C-e^{-t/2}\,\Phi(e^{-2t},2,\tfrac14)\big),\quad C=\pi^2+8G,$$
$$P(t)=\sum_{n\le e^{t}}\frac{\Lambda(n)}{\sqrt n}\,(t-\log n)\quad(\text{convex, piecewise-linear}).$$

`A` = the smooth **Archimedean reserve**; `P` = the **prime ramp**. Verified `A−P=Ψ` to `~10^{-15}`
(`t=1,2,3,5`) against a **separate evaluator** `suzuki_psi.py` — which uses the *same* Suzuki closed form
by a different code path, so this is a transcription cross-check of the `A/P` split, **not** an
independent validation of the formula.

## 2. The curvature form

Away from `t=0`, `Ψ(t)=\int_0^t (t-s)\,Ψ''(s)\,ds` with `Ψ(0)=0`, and

$$Ψ''(s)=\underbrace{A''(s)}_{\text{Archimedean}}\;-\;\underbrace{\sum_n\frac{\Lambda(n)}{\sqrt n}\,\delta(s-\log n)}_{\text{prime impulse train}}.$$

The Archimedean curvature is **not** globally positive: `A''(s)` **changes sign at `s≈0.2812`** — it is
**negative on `(0,0.281)`** and **positive for all `s≥0.281`** (verified analytically: `A''=−8.25,−3.25,
−0.73` at `s=0.05,0.1,0.2`, then `+0.11,+0.83,+1.18,…` at `s=0.3,0.5,\log 2,…`). Crucially the sign-change
is *before the first prime impulse* at `\log 2≈0.693`, so **`A''>0` throughout `s≥\log 2`, the entire
region where prime impulses live.** (On `(0,\log 2)` there are no primes, `Ψ=A`, and `A` has a `t\log t`
corner near 0 — a prime-free Archimedean regime, positive but not of this curvature-competition form.)
So, in the bulk, **RH `⟺` the (positive) Archimedean curvature dominates the prime impulses, time-weighted
by `(t-s)`** — the user's "first domino sets the slope, the reservoir bends it, the next prime fires."

## 3. The attack payoff: a total `O(√X)` cancellation (PNT) to an `o(√X)` remainder

The striking fact — the leading part **unconditional** (Prime Number Theorem). Both the Archimedean
reserve and the prime ramp grow like the *same* leading term `4e^{t/2}=4\sqrt X` (`X=e^t`; `A` from its
closed form, `P` from `\sum_{n\le X}\Lambda(n)/\sqrt n\sim 2\sqrt X`), and the **entire** `O(\sqrt X)`
reserve cancels the **entire** `O(\sqrt X)` ramp, leaving a remainder `Ψ=A−P` that is `o(\sqrt X)` and, in
the computed range, small:

| `t` | `X=e^t` | `A(t)` | `P(t)` | `A/4e^{t/2}` | `P/4e^{t/2}` | `Ψ=A−P` |
|----:|----:|----:|----:|----:|----:|----:|
| 4 | 55 | 15.11 | 15.08 | 0.511 | 0.510 | 0.035 |
| 6 | 403 | 60.53 | 60.48 | 0.753 | 0.753 | 0.048 |
| 8 | 2981 | 193.20 | 193.17 | 0.885 | 0.885 | 0.031 |
| 10 | 22026 | 563.09 | 563.03 | 0.949 | 0.948 | 0.062 |
| 12 | 162755 | 1577.78 | 1577.75 | 0.978 | 0.978 | 0.029 |

Both ratios climb to `1`; `A` and `P` reach `~1578` at `t=12` while `Ψ=A−P` stays `~0.03`. **The whole
square-root-of-`X` growth cancels unconditionally (PNT).** The remainder `Ψ=A−P` is `o(\sqrt X)` and is
small in this range — **but its boundedness and positivity for *all* `t` are each RH-equivalent, not
established here:** an off-line zero `ρ=β+iγ` with `β>½` makes `Ψ` grow like `e^{(β-½)t}` and go negative.
The leading `O(\sqrt X)` cancellation is PNT (the per-`n` flat multiplicative bookkeeping, Part B); the
remainder is the Archimedean/continuation content.

## 4. The exact reduction, and why the block cannot be split

- **Prime side (computed, no zeros):** `Ψ(t)=A(t)−P(t)`.
- **Zero side (equivalence, stated — zeros *not* used as input):** `Ψ(t)=\sum_\gamma(1-\cos\gamma t)/\gamma^2`,
  which is `≥0` iff every `\gamma` is real `= RH`.

So the attack reduces RH to: **the remainder `A−P` stays bounded-and-`≥0` for all `t`** (both are RH).
Two hard constraints, both honest:

1. **Never split the block.** Estimating `P` by absolute value discards the `4\sqrt X` cancellation and
   the bound goes vacuous (`4\sqrt X \gg 0.03`). The Archimedean `A` and prime `P` must stay paired — the
   repo's recurring "complete first, test positivity second" (frontier `WEIL_PRIME_RAY §7`).
2. **The prime ramp has no internal sign cancellation.** `P(t)=\sum\Lambda(n)/\sqrt n\,(t-\log n)` is a
   **monotone sum of nonnegative terms** — it is **not** a tensor (that is the per-`n` conductor
   coefficient `b_ω(n)`, Part B; Part B explicitly disclaims "the prime side of RH is flat"). So the
   positivity obstruction cannot come from re-organizing the primes; it lives in the **`A−P` balance** —
   the **Archimedean analytic continuation**, i.e. the Round-006 `C103` / Weil wall.

## 5. Honest wall

This is an **exact reduction plus a sharp *unconditional* leading-cancellation fact (PNT)**, not a proof.
`A−P` bounded-and-`≥0` for all `t` *is* Suzuki Thm 1.7 `=` RH. What the attack genuinely establishes:

- the `O(\sqrt X)` reserve/ramp cancellation is total and **unconditional** (PNT) — so RH lives entirely
  in the `o(\sqrt X)` remainder `A−P`, whose boundedness and positivity are *themselves* RH;
- that remainder's behaviour is the **Archimedean continuation** content, not supplied by the per-`n` flat
  prime combinatorics (Part B) — the same wall every round reaches;
- **Conrey–Li (2000)** refuted the naive de Branges positivity route to exactly this kind of remainder
  positivity, so no cheap positivity argument applies.

The attack sharpens the target to the smallest it has been — *"a single oscillation `A−P`, whose
`O(\sqrt X)` bulk is already cancelled unconditionally, must stay bounded and `≥0`"* — and shows precisely
why the arithmetic (factorization/curvature) structure cannot supply that last step. RH remains open.

## 6. Ledger

- **C113 (RH-inert reduction + unconditional leading-cancellation fact).** Suzuki `Ψ(t)=A(t)−P(t)`,
  `A`=smooth Archimedean reserve, `P=\sum_{n\le e^t}(\Lambda(n)/\sqrt n)(t-\log n)` prime ramp (verified
  `A−P=Ψ` to `~1e-15` vs a separate evaluator = same closed form, different code path — a transcription
  cross-check, not independent formula validation). Curvature form
  `Ψ=\int(t-s)[A''-\sum(\Lambda/\sqrt n)\delta_{\log n}]`; `A''` **changes sign at `s≈0.2812`** (`<0` on
  `(0,0.281)`, the prime-free region before the first impulse at `\log2≈0.693`; `>0` for all `s≥\log2`,
  where the impulses live — verified analytically). **Fact (unconditional, PNT):** `A(t),P(t)\sim 4e^{t/2}`
  (ratios→1, `t=4..12`), the full `O(\sqrt X)` cancels, leaving `Ψ=A−P` `o(\sqrt X)` (`~0.03–0.06` in
  range). **Boundedness AND positivity of the remainder for all `t` are each RH-equivalent, NOT shown**
  (off-line zero `β>½` ⟹ `Ψ\sim e^{(β-½)t}`, sign-indefinite). Leading cancellation = PNT (per-`n` flat
  bookkeeping, C112); remainder = Archimedean continuation (C103/Weil wall). `P` is a monotone nonnegative
  sum, **not** a tensor (Part B factors `b_ω(n)`, not `P`); must not split the block
  (`|.|`-estimating `P` is vacuous). Zero-side `Ψ=\sum_\gamma(1-\cos\gamma t)/\gamma^2\ge0\iff` RH
  (stated, zeros not used). Conrey–Li 2000 refuted the de Branges positivity route. Credit Suzuki 2023,
  Weil 1952, Bombieri 2000; frontier route 3. `scripts/r010_reserve_curvature.py`. No RH progress.

RH remains open.
