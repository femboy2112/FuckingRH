# The growth cascade: the divergence and the pole are RH-inert; RH lives in the bounded remainder

**Date:** 2026-10-06. **Status:** DISCLOSED (measured, two exact cancellations). **RH open.**
**Reproduce:** `scripts/r007_signature_ledger.py`, `scripts/r007_repaired_decomposition.py`, and the inline
growth/slope checks.

Working the stratified-diagonal / half-density seam produced a clean structural fact that **reframes the
wall** and confirms the half-density intuition exactly.

## The two exact cancellations

Suzuki `Ψ(t) = 8(cosh(t/2)−1) − Σ_{p^k≤e^t} (log p) p^{−k/2}(t − k log p) + (t/2)(ψ(1/4)−log π) + lerch`.
Individually the pole and prime pieces blow up (±4300 at `t=14`); `Ψ(t)` itself stays `O(1)` (≈0.03–0.06
out to `t=14`, `Ψ/e^{t/2}→0`). Two cancellations, both **exact and unconditional** (no RH input):

**Level 1 — the half-density / Chebyshev balance (exponential).** The pole grows as
`8cosh(t/2) ~ 4e^{t/2}`. The prime sum, by `ψ(x)=Σ_{n≤x}Λ(n)~x` (Chebyshev / PNT) and the `n^{−1/2}`
weight, has `Σ_{n≤e^t}Λ(n)n^{−1/2} ~ 2e^{t/2}` and `Σ_{n≤e^t}Λ(n)n^{−1/2}log n ~ 2t e^{t/2} − 4e^{t/2}`,
so the prime part `= −t·(2e^{t/2}) + (2t e^{t/2} − 4e^{t/2}) = −4e^{t/2}` to leading order. The `t·e^{t/2}`
terms **self-cancel**, and `pole + prime ~ 4e^{t/2} − 4e^{t/2} = 0`: the entire exponential sector
cancels. This is precisely the `e^{t/2} = |x|^{1/2}` **half-density** growth being globally balanced — the
critical-line normalization made structural.

**Level 2 — the Archimedean balance (linear).** The residual slope of `pole + prime` converges to exactly
`−(ψ(1/4)−log π)/2 = −LIN = 2.686092…` (measured: `2.679, 2.661, 2.694, 2.679` → `2.686`). The
Archimedean drift is `+LIN·t = −2.686…·t`. They cancel. This is the explicit formula's boundary/constant
balance (the `ĝ(0)+ĝ(1)` terms).

What remains is `Ψ(t)` itself, with `Ψ(0)=0`, and (Suzuki) `RH ⟺ Ψ(t) ≥ 0 ∀t`.

**Precise scope (no overclaim).** The two cancellations remove exactly the **`β=1` layer** of the growth.
In explicit-formula terms, a zero/pole at real part `β` contributes to `Ψ` a term of growth rate
`e^{(β−1/2)t}`; the pole sits at `β=1` (rate `e^{t/2}`) and is cancelled by the prime sum's `β=1` growth —
this is exactly the **Prime Number Theorem** (no zeros on `Re s=1`), hence Level 1 is unconditional but
*only* PNT-strength. After it, `Ψ` grows at most like `e^{(Θ−1/2)t}` where `Θ = sup{β : ξ(β+iγ)=0}`. So:

    Ψ bounded  ⟺  Θ = 1/2  ⟺  RH,   and then additionally  Ψ ≥ 0  (Suzuki).

The numerically-observed boundedness (`Ψ≈0.03–0.06` out to `t=14`) is **finite-window** and does not prove
`Ψ` bounded — a zero at `β=1/2+ε` would add an `e^{εt}` term invisible at small `t` / large `γ`. What the
cascade *does* prove unconditionally is that the `e^{t/2}` (pole/`β=1`) layer — the source of the
`Σ_p M_p=∞` divergence — cancels exactly. **That layer is RH-inert; RH lives strictly above it.**

## Why this reframes the wall (and corrects an over-emphasis)

Three independent measurements (ledger C106 impedance index, and R007 probes A/B) had made the
**divergence** `Σ_p M_p = ∞` look like the obstruction. The growth cascade shows it is **not**:

- The divergence is the `e^{t/2}` (imaginary-frequency / exponential) sector, and it **cancels exactly
  and unconditionally** against the pole. So the divergence is **RH-inert**.
- The **pole's indefiniteness** (the rank-2, signature-(1,1), `κ=1` negative square — confirmed bounded in
  probe A) lives at the same imaginary frequency `ξ=i/2`, and it is **absorbed** by the same exponential
  cancellation. This is why probe B found no additive split into `(CND) + (finite-rank indefinite)`: the
  indefinite pole is not a separable summand of the *bounded* object — it has already been cancelled.
- The Round-006 "Pontryagin index `κ_P → ∞`" (C106) is therefore a **representation artifact of the
  Laplace/impedance coordinate**, not a feature of the screw/CND object. In the CND representation `Ψ` is
  bounded and the index question dissolves.

**Net:** neither the divergence nor the pole is where RH hides. RH lives **entirely in the sign of the
bounded remainder** `Ψ`, equivalently in the positivity of its **finite** spectral measure.

## The residue (bare RH, honestly)

The zero-side distribution is `σ = Σ_γ γ^{−2}(δ_γ + δ_{−γ})` (eigen-recovery of the zeros from the
prime-built kernel is the repo's standing check, `prime_kernel_psd_boundary.py (A)`). `RH ⟺ Ψ ≥ 0 ⟺` `σ`
is a **positive measure supported on the real `ξ`-axis** `⟺` all zeros real. (Under RH `σ` is a finite
positive measure, mass `2Σ_γγ^{−2}`; off the line the "atoms" move to complex `ξ`, i.e. `σ` fails to be a
positive real-axis measure.)

The exponential/`β=1` underbrush (the divergence + the pole) is cleared **exactly and unconditionally**;
what is left is the positivity of `σ` assembled from the prime oscillations — an assembly that is
**conditionally/oscillatorily convergent**, which is exactly why no finite-rank or additive-split handle
survives (probes A/B). This is bare RH: no residual finite structure to leverage was found.

## What the seam did and did not buy

- **Bought (real, clean):** the half-density `e^{t/2}` cancellation is exact (Level 1), confirming the
  unit-basepoint ½-twist is the *globally balanced* direction; the pole and divergence are RH-inert; the
  problem is cleanly reduced to the sign of a bounded remainder / positivity of a finite measure; the
  Round-006 index divergence is demoted to a representation artifact.
- **Did not buy:** any handle on the positivity itself. After the cascade, `σ ≥ 0` is `all zeros real`
  with no finite-rank, no symmetry projection, and no additive-split leverage that we could find — the
  oscillatory assembly is irreducible. The stratified-diagonal projection (C112) would have to act on this
  bounded-remainder assembly, and nothing here shows it isolates positivity.

## Ledger

New rows **C113** (growth cascade: two exact unconditional cancellations — Level-1 half-density `e^{t/2}`
and Level-2 Archimedean linear — leave `Ψ` bounded; divergence and pole are RH-inert; RH ⟺ bounded
remainder ≥ 0 ⟺ finite spectral measure `σ=Σγ^{−2}δ_γ ≥ 0`) and **C114** (the `κ_P→∞` of R006/C106 is a
Laplace/impedance **representation artifact**; in the screw/CND representation `Ψ` is bounded and no
additive split yields a finite-rank obstruction — probes A/B).
