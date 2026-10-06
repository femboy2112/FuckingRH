# Intersect before squaring: a sharp (and worse-than-expected) no-go

**Round 006. RH IS OPEN. Reproduce:** `scripts/r006_intersect_before_squaring.py`.

## The hypothesis

Round004/005 killed the **dead order** `B = ⊕_p B_p` (direct sum of local squares): the energy
`Σ_p ‖B_p v‖²` diverges in bulk `~ π(N)` (C91/C98), renormalized only *analytically* by the indefinite
Archimedean pole, never by an algebraic Hilbert-space subtraction. The Round006 hope (§7/§14) was to dress
each sheet with the **universal successor boundary** `(I−S)` — the one non-commuting, non-multiplicative
generator, hence the only possible carrier of RH content (C89/C94) — and assemble **before** squaring:

    C_p := (I − S)(I − p^{-1/2} V_p)^{-1},      B_int := Σ_{p≤P} C_p,
    ‖B_int v‖² = DIAG + CROSS,   DIAG = Σ_p ‖C_p v‖²  (dead sum),  CROSS = Σ_{p≠q} ⟨C_p v, C_q v⟩.

If `CROSS ≈ −DIAG`, the cross terms renormalize the bulk and we have a crack.

## The result: quadratic divergence (the common-mode trap)

Measured for the source `|1>` and random unit vectors, horizon `N = 60…960`:

| N | #primes | DIAG | CROSS | TOTAL | CROSS/DIAG | DIAG/π(N) |
|---:|---:|---:|---:|---:|---:|---:|
| 60 | 17 | 37.3 | 518.8 | 556.2 | 13.9 | 2.20 |
| 120 | 30 | 63.7 | 1696 | 1760 | 26.6 | 2.12 |
| 240 | 52 | 108 | 5229 | 5337 | 48.4 | 2.08 |
| 480 | 92 | 188 | 16613 | 16801 | 88.2 | 2.05 |
| 960 | 162 | 328 | 51934 | 52262 | 158 | 2.03 |

- `DIAG ~ 2·π(N)` — the bulk divergence returns, exactly as in the direct sum (C98).
- `CROSS ~ +2·π(N)²` and **positive** — `CROSS/DIAG` grows linearly in the prime count, never → −1.

So "intersect before squaring" with a **uniform** boundary is **strictly worse** than the dead sum: the
total diverges *quadratically* (`~π(N)²`) instead of linearly.

## Is it just the uniform boundary? No — the prime-specific (stratified) boundary too

The natural fix is a **prime-specific** boundary: by the stratified identity `Π_{p,1}S̃ = S^p Π_{p,1}`, the
sheet's unit step shadows to `(I − S^p)`, which differs per prime. Re-running with
`C_p = (I − S^p)(I − p^{-1/2}V_p)^{-1}`:

| N | #primes | DIAG | CROSS | CROSS/DIAG (uniform → stratified) |
|---:|---:|---:|---:|---|
| 60 | 17 | 37.9 | 277 | 13.9 → **7.3** |
| 120 | 30 | 64.3 | 875 | 26.6 → **13.6** |
| 240 | 52 | 109 | 2658 | 48.4 → **24.5** |
| 480 | 92 | 189 | 8379 | 88.2 → **44.4** |
| 960 | 162 | 329 | 26090 | 158 → **79.3** |

Stratification only **halves** the coefficient; `CROSS/DIAG` still **grows ~π(N)** and the total still
diverges quadratically. So prime-specificity alone is *not* the fix.

## Why — the common mode is the identity, and it is unavoidable for any `(I−S^{shift})`

The mechanism is exact and robust. Any boundary of the form `(I − S^{shift})` contains the **identity**
`I`, and the identity is shared by every sheet:

    C_p v = (I − S^{shift_p})(I − p^{-1/2}V_p)^{-1} v = v − S^{shift_p}v + (higher V_p terms),

so every `C_p v` carries the same leading `v`. Assembling before squaring adds these coherently:
`⟨C_p v, C_q v⟩ ⊇ ‖v‖²` for every pair, hence `CROSS ⊇ π(N)(π(N)−1)·‖v‖²`. (Uniform `(I−S)` shares *both*
`v` and `Sv` → coefficient ≈ 2; stratified `(I−S^p)` shares only `v` → coefficient ≈ 1, the observed
halving.) For `v=|1>` the shared component is the source `|1>` itself (the `k=0` term of every resolvent).

> **No-go (C101, strengthened).** The quadratic amplification is **not** an artifact of the uniform
> boundary; it is intrinsic to *coherent* assembly of any boundaries that share a common component — and
> every `(I − S^{shift})` boundary shares the identity `I` (equivalently, every sheet's range contains the
> source `|1>`). The dichotomy is complete:
> - assemble with **overlap** (shared `I`) → coherent common mode → **quadratic** divergence `~π(N)²`;
> - assemble **orthogonally** (direct sum, no cross terms) → the dead order → **linear** bulk divergence
>   `~π(N)` (C98).
>
> Both diverge. The **only** escape is cross terms that interfere **destructively** — `CROSS ≈ −DIAG` with
> `DIAG` itself tamed — i.e. boundaries whose shared components carry **opposite signs**. No positive,
> coherent, algebraic assembly produces that.

The object with exactly that signed structure is the **Weil explicit formula**: the prime terms enter with
one sign, the Archimedean pole/`Γ`-term with the other, and their destructive interference is the bounded
`Σ_γ`-side. So "intersect before squaring, done correctly" *is* the Weil distribution — and its positivity
is RH (C91). This also matches `FRACTIONAL_SUCC_GAMMA_INTERTWINER.md §G`: the cancelling sign is the
*analytic* `Γ`-sector, not anything the algebraic assembly can supply. The Aletheia note §8's intuition
("wired, not independently summed") is correct but insufficient: the wiring must be **signed**, not merely
prime-specific.

## Status

A decisive, quantitative **no-go** with a constructive lesson: it rules out the uniform-boundary
intersect-first assembly (the natural reading of the §7/§14 hope), and it names precisely what a working
assembly would need (prime-specific signed wiring = the Weil cross terms). The wall is unchanged (C91), now
flanked by a sharper boundary marker.
