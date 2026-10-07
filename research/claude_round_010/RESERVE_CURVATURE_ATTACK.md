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

`A` = the smooth **Archimedean reserve**; `P` = the **prime ramp**. Verified `A−P=Ψ` against the
independent evaluator `suzuki_psi.py` to `<10^{-4}` (`t=1,2,3,5`), with `A,P` computed separately.

## 2. The curvature form

Since `Ψ(0)=Ψ'(0)=0`, `Ψ(t)=\int_0^t (t-s)\,Ψ''(s)\,ds`, and

$$Ψ''(s)=\underbrace{A''(s)}_{\text{smooth, }>0}\;-\;\underbrace{\sum_n\frac{\Lambda(n)}{\sqrt n}\,\delta(s-\log n)}_{\text{prime impulse train}}.$$

The Archimedean curvature is **strictly positive** (verified `A''>0`: `0.83,1.55,2.71,7.39,20.1` at
`s=0.5,1,2,4,6`). So **RH `⟺` the accumulated Archimedean curvature dominates the accumulated prime
impulses, time-weighted by `(t-s)`** — the user's "first domino sets the slope, the reservoir bends it,
the next prime fires; the reserve never goes below zero."

## 3. The attack payoff: a total `O(√X)` cancellation to a bounded remainder

The striking, exact, verified fact. Both the Archimedean reserve and the prime ramp grow like the *same*
leading term `4e^{t/2}=4\sqrt X` (`X=e^t`), and the **entire** `O(\sqrt X)` reserve cancels the **entire**
`O(\sqrt X)` ramp, leaving `Ψ` **bounded** (`O(1)`):

| `t` | `X=e^t` | `A(t)` | `P(t)` | `A/4e^{t/2}` | `P/4e^{t/2}` | `Ψ=A−P` |
|----:|----:|----:|----:|----:|----:|----:|
| 4 | 55 | 15.11 | 15.08 | 0.511 | 0.510 | 0.035 |
| 6 | 403 | 60.53 | 60.48 | 0.753 | 0.753 | 0.048 |
| 8 | 2981 | 193.20 | 193.17 | 0.885 | 0.885 | 0.031 |
| 10 | 22026 | 563.09 | 563.03 | 0.949 | 0.948 | 0.062 |
| 12 | 162755 | 1577.78 | 1577.75 | 0.978 | 0.978 | 0.029 |

Both ratios climb to `1`; `A` and `P` reach `~1578` at `t=12` while `Ψ=A−P` stays `~0.03`. **The whole
square-root-of-`X` growth cancels; RH is the positivity of the tiny bounded remainder.** The leading
cancellation is the Prime Number Theorem — i.e. the **flat multiplicative side** (Part B: `P` is a flat
tensor over primes). The bounded remainder is the Archimedean/continuation content.

## 4. The exact reduction, and why the block cannot be split

- **Prime side (computed, no zeros):** `Ψ(t)=A(t)−P(t)`.
- **Zero side (equivalence, stated — zeros *not* used as input):** `Ψ(t)=\sum_\gamma(1-\cos\gamma t)/\gamma^2`,
  which is `≥0` iff every `\gamma` is real `= RH`.

So the attack reduces RH to: **the bounded remainder `A−P` never goes negative.** Two hard constraints,
both honest:

1. **Never split the block.** Estimating `P` by absolute value discards the `4\sqrt X` cancellation and
   the bound goes vacuous (`4\sqrt X \gg 0.03`). The Archimedean `A` and prime `P` must stay paired — the
   repo's recurring "complete first, test positivity second" (frontier `WEIL_PRIME_RAY §7`).
2. **The prime side is flat (Part B).** `P` is a tensor over independent prime channels (UFD); its
   combinatorics carry no sign structure. The sign of the bounded remainder is therefore **not**
   inter-prime — it is the **Archimedean analytic continuation**, i.e. the Round-006 `C103` / Weil wall.

## 5. Honest wall

This is an **exact reduction plus a sharp leading-cancellation fact**, not a proof. `A−P≥0` *is* Suzuki
Thm 1.7 `=` RH. What the attack genuinely establishes:

- the `O(\sqrt X)` reserve/ramp cancellation is total and is PNT (flat side) — so RH lives entirely in
  the **bounded `O(1)` remainder**;
- that remainder's positivity is the **Archimedean continuation** content, provably untouched by the
  (flat) prime combinatorics — the same wall every round reaches;
- **Conrey–Li (2000)** refuted the naive de Branges positivity route to exactly this kind of remainder
  positivity, so no cheap positivity argument applies.

The attack sharpens the target to the smallest it has been — *"a single bounded oscillation `A−P`, whose
`O(\sqrt X)` bulk is already cancelled, must stay `≥0`"* — and shows precisely why the arithmetic
(factorization/curvature) structure cannot supply that last step. RH remains open.

## 6. Ledger

- **C113 (RH-inert reduction + exact fact).** Suzuki `Ψ(t)=A(t)−P(t)`, `A`=smooth Archimedean reserve,
  `P=\sum_{n\le e^t}(\Lambda(n)/\sqrt n)(t-\log n)` prime ramp (verified `A−P=Ψ` vs suzuki_psi, `<1e-4`).
  Curvature form `Ψ=\int(t-s)[A''-\sum(\Lambda/\sqrt n)\delta_{\log n}]`, `A''>0` verified. **Exact fact:**
  `A(t),P(t)\sim 4e^{t/2}` (ratios→1, verified `t=4..12`), the full `O(\sqrt X)` cancels to a **bounded**
  `Ψ\sim0.03–0.06`; RH = positivity of that bounded remainder. Leading cancellation = PNT (flat side,
  C112); remainder = Archimedean continuation (C103/Weil wall). Must not split the block
  (`|.|`-estimating `P` is vacuous). Zero-side `Ψ=\sum_\gamma(1-\cos\gamma t)/\gamma^2\ge0\iff` RH
  (stated, zeros not used). Conrey–Li 2000 refuted the de Branges positivity route. Credit Suzuki 2023,
  Weil 1952, Bombieri 2000; frontier route 3. `scripts/r010_reserve_curvature.py`. No RH progress.

RH remains open.
