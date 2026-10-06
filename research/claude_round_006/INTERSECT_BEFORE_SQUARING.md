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

## Why — and the sharpened requirement it exposes

The mechanism is exact. The universal boundary makes `(I−S)v` a **common mode**: for every prime,

    C_p v = (I − S)(I − p^{-1/2}V_p)^{-1} v = (I − S)v + p^{-1/2}(I − S)V_p v + …

so the leading term `(I−S)v` is *identical across all sheets*. Assembling before squaring adds these
π(N) copies **coherently**: `⟨C_p v, C_q v⟩ ≈ ‖(I−S)v‖²` for every pair, hence
`CROSS ≈ π(N)(π(N)−1)·‖(I−S)v‖²`. For `v=|1>`, `(I−S)|1> = |1>−|2>`, `‖·‖²=2`, matching `2π(N)²` to the digit.

> **No-go (C101).** A *common-mode* (prime-independent) boundary cannot renormalize the bulk by assembly:
> the shared boundary adds coherently across the π(N) prime sheets and **amplifies** the divergence from
> `π(N)` to `π(N)²`. Neither assembly order escapes — the dead sum diverges linearly, the dressed
> intersect-first diverges quadratically.

This *sharpens*, rather than contradicts, the earlier controls. C89 (any commuting-`V_p` object is
RH-inert) and the Aletheia note §7 (the universal composition/augmentation boundary is RH-inert by itself)
said the uniform boundary carries no RH content. The experiment shows the stronger fact: it is actively
*anti-helpful* when assembled, because it is coherent. The Aletheia note §8 anticipated the fix in words —
*"the self-sieving carry network determines how the different history variables `X_p` are wired rather than
independently summed"* — and this experiment turns that into a concrete, measurable **requirement**:

> **The RH-bearing boundary wiring must be prime-SPECIFIC and sign-structured, producing cross terms whose
> signs cancel the bulk — not a universal boundary that adds in phase.** The only object in this program
> with exactly that signed-cross-term structure is the Weil explicit formula: its prime×prime and
> prime×Archimedean cross terms carry the signs. So "intersect before squaring" done *correctly* is the
> Weil distribution, and its positivity is RH (C91). The uniform-boundary assembly is the naive version,
> and it fails loudly.

## Status

A decisive, quantitative **no-go** with a constructive lesson: it rules out the uniform-boundary
intersect-first assembly (the natural reading of the §7/§14 hope), and it names precisely what a working
assembly would need (prime-specific signed wiring = the Weil cross terms). The wall is unchanged (C91), now
flanked by a sharper boundary marker.
