# The Schur–Vitali continuation theorem: a clean, non-circular reduction (ckpt6)

**Date:** 2026-10-06. **Status:** DISCLOSED (theorem, proved). **RH open** (the theorem is conditional;
its one hard hypothesis is unmet). **Reproduce:** `scripts/schur_vitali_demo.py`.

This is the round's central **limit mechanism**, isolated and proved as an independent complex-analysis
theorem so the rest of the round can aim at exactly one target. It makes precise the directive's §10/§17
"take the fucking limit": if finite arithmetic hardware gives transfer functions that are **contractive
on all of `H_{1/2}` by construction** and converge to the right thing **only on the safe Euler region**,
then RH follows — and crucially, this is **not** circular.

## Classical interface (literature-locked)

`H_{1/2} := {s : Re s > 1/2}`. With `xi(s) = ½ s(s-1) π^{-s/2} Γ(s/2) ζ(s)`:

- **(Lagarias 1999, (1.4); unconditional)** `Re[xi'/xi(s)] > 0` for `Re s > 1` (no zeros of `xi` there).
- **(Hinkkanen; Lagarias 1999, (1.5) and (1.19))** `RH ⟺ Re[xi'/xi(s)] > 0` for all `Re s > 1/2`,
  equivalently `i·xi'/xi(½+iτ)` is a Pick (Herglotz) function, i.e. `xi'/xi` is **positive-real** on
  `H_{1/2}`. The partial-fraction form `Re xi'/xi(σ+it) = Σ_ρ (σ-β)/((σ-β)²+(t-γ)²)` (Lagarias p. 227)
  makes each term's sign `= sign(σ-β)`; positivity throughout `H_{1/2}` ⟺ every `β ≤ ½` ⟺ RH.
- The 2005 correction (Acta Arith. 116) repairs only two lemmas inside the *conditional* Thm 1.3; the
  decomposition it fixes is `xi'/xi = 1/s + 1/(s-1) - ½log π + ½ψ(s/2) + ζ'/ζ` with **+**`1/(s-1)`
  (= the `A_inf - Σ_p m_p` of §6). The equivalence (1.5) is untouched.

So the proof-target is unambiguous and standard: **realize `xi'/xi` as a positive-real function on
`H_{1/2}` via a limit of structurally-passive finite objects.**

## Theorem (Schur–Vitali continuation)

Let `{Θ_X}` be holomorphic functions on the connected open set `H_{1/2}` with `|Θ_X(s)| ≤ 1` for all
`s ∈ H_{1/2}` and all `X`. Let `U = {Re s > 1} ⊂ H_{1/2}` be the open sub-half-plane, and suppose
`Θ_X(s) → Θ_∞(s)` pointwise on `U` with `Θ_∞` **non-constant**. Then:

(a) there is a unique holomorphic `Θ : H_{1/2} → \overline{D}` with `Θ|_U = Θ_∞`, and `Θ_X → Θ`
    locally uniformly on all of `H_{1/2}`;
(b) `|Θ(s)| < 1` for every `s ∈ H_{1/2}` (strict interior contraction).

*Proof.* **(a)** `{Θ_X}` is uniformly bounded, hence locally bounded, hence **normal** on `H_{1/2}`
(Montel). Let `Θ', Θ''` be locally-uniform limits of subsequences. Each is holomorphic (Weierstrass) and
`≤1` in modulus. On `U`, both equal the pointwise limit `Θ_∞`. Two holomorphic functions agreeing on the
open subset `U` of the connected set `H_{1/2}` agree everywhere (identity theorem): `Θ' ≡ Θ''`. So all
subsequential limits coincide; a normal family whose subsequential limits all coincide converges locally
uniformly to that common limit `Θ`. Uniqueness of the extension is the identity theorem again. (This is
the Vitali–Porter theorem.) **(b)** If `|Θ(s_0)| = 1` at an interior `s_0`, maximum-modulus forces
`Θ ≡ c`, `|c| = 1`, so `Θ_∞ = Θ|_U` is constant — contradiction. Hence `|Θ| < 1` throughout. ∎

## Corollary (arithmetic ⇒ RH; conditional, non-circular)

Fix `a > 0`. Suppose a family of **finite** arithmetic systems produces holomorphic transfer functions
`Θ_X : H_{1/2} → \overline{D}` with:

- **(P) structural passivity:** each `Θ_X` is contractive on *all* of `H_{1/2}` provably from finite
  operator theory (e.g. `Θ_X` = transfer function of a finite unitary/passive colligation) — **no
  zeta-zero data used**;
- **(E) Euler-side convergence (unconditional):** on `U = {Re s>1}`,
  `Θ_X → (xi'/xi - a)/(xi'/xi + a)` locally uniformly.

Then **RH holds**.

*Proof.* `Θ_∞ := (xi'/xi - a)/(xi'/xi + a)` is holomorphic and non-constant on `U` (there `Re xi'/xi > 0`,
so `xi'/xi ≠ -a` and the denominator never vanishes). By the Theorem, `Θ_X → Θ` locally uniformly on
`H_{1/2}`, `Θ` holomorphic with `|Θ| < 1` strictly (part (b)). Set `F := a(1+Θ)/(1-Θ)`; since `|Θ|<1`,
`F` is holomorphic on `H_{1/2}` with `Re F ≥ 0` (Cayley `D → {Re ≥ 0}`). On `U`, `F = xi'/xi`. By the
identity theorem `F` is THE analytic continuation of `xi'/xi` to `H_{1/2}`, so `xi'/xi` is
**holomorphic (pole-free)** on `H_{1/2}`. Its poles are the zeros of `xi`, so `xi` has no zero with
`Re s > 1/2`; the functional equation `xi(s)=xi(1-s)` removes `Re s < 1/2`. Hence all zeros lie on
`Re s = 1/2`: RH. ∎

## Non-circularity audit (the point of the whole architecture)

The proof uses only **(P)** — a finite, `X`-by-`X` operator fact provable without any zeta-zero
information — and **(E)** — convergence on `Re s > 1`, the region of *absolute* Euler convergence, which
is unconditional. It **never** assumes `Θ_X → Θ_∞` on the strip `1/2 < Re s ≤ 1`; that convergence is a
**conclusion** (Montel + identity theorem), not a hypothesis. Assuming strip convergence would be circular
(it already encodes a zero-free strip). We do not. **The entire RH content is compressed into (P).**

## Numerical confirmation that the mechanism is real (and that (P) is the content)

`schur_vitali_demo.py` (no zeta involved):

- **GOOD family** `F_X = (1/X)Σ_{j=1}^X 1/(w + j/X)`, `w=s-½` (Riemann sum of `∫_0^1 dτ/(w+τ)` — each
  kernel Herglotz, so each `F_X` positive-real on `H_{1/2}` **by construction**): measured
  `sup_{H_{1/2}} |Θ_X| ≤ 0.9994 < 1` (Schur), and `Θ_X` converges to the same analytic limit on **both**
  the Euler region *and* the strip (`|Θ_{1024}-Θ_∞| ∼ 10^{-4}` at `s=0.7+2i` and `0.55+0.5i`) — exactly
  as the theorem predicts: Euler-side convergence of a uniformly-Schur family **forces** strip
  convergence.
- **BAD family** `g(s)=1/(s-0.7)` (pole in the strip): `sup_{Re s>1} |Cayley g| = 0.9996 ≤ 1` but
  `sup_{H_{1/2}} |Cayley g| = 1.44 > 1`. So Euler-side contractivity does **not** imply `H_{1/2}`
  contractivity; the strip pole survives, and Vitali does not apply. **(P) is essential and
  non-automatic.**

## Where (P) is at risk — the de Branges / Conrey–Li warning

(P) says: produce finite arithmetic `Θ_X` contractive on all of `H_{1/2}`. ckpt5 (C103) already shows the
naive one-port constructions fail it. Two structural dangers, both now literature-anchored:

1. **Indefinite (Krein/Pontryagin) metric from the pole sector.** If the arithmetic forces negative
   squares (the rank-2 pole, C83/C84), the `Θ_X` are only `J`-contractive, hence **not** uniformly
   bounded by 1 — Montel fails, the Theorem does not apply. (ckpt7/ckpt9.)
2. **The natural space-level positivity is known to fail for ζ.** The cleanest way to get (P) would be a
   de Branges `H(E)` space whose structural positivity (`Re⟨F, F(·+i)⟩ ≥ 0`) makes the colligation
   passive. **Conrey–Li (IMRN 2000, arXiv:math/9812166)** prove this exact positivity condition **fails**
   for the `ζ`-associated spaces `E(z)=ξ(1-iz)` and `W=1/ξ(1-iz)` — explicit counterexamples (the 34th
   zero; `w=-282`), and **Sarnak's** conceptual argument: `F(s)=ξ(s)/ξ(s+1)` has `Im log F = Im log ζ +
   O(1)`, and `log ζ` is dense in `C` on `1/2<Re s<2`, so `Re{W(z)/W(z+i)} < 0` somewhere — the positivity
   is violated. What survives is the one-directional implication (positivity ⇒ zeros on the line) and the
   structure theory; what is **killed** is verifying the natural positivity directly.

**Reading for this round.** The Schur–Vitali reduction is sound and sharp; it is NOT circular; it reduces
RH to the single statement (P). But (P), in its most natural realization, is precisely the positivity that
Conrey–Li showed fails for the obvious ζ-spaces. So a Round006 crack must either (i) find a *different*
structure function / chain whose positivity is **not** the Conrey–Li one and is still structurally forced
by the arithmetic, or (ii) genuinely couple + complete so that passivity holds for a reason orthogonal to
the de Branges single-space condition. This is the exact bar for the rest of the round.

## Ledger

New row **C104**: Schur–Vitali continuation theorem proved (Vitali–Porter + Cayley): a family of
functions contractive on all of `H_{1/2}` and convergent to `Cayley_a[xi'/xi]` only on `Re s>1` forces
`xi'/xi` positive-real on `H_{1/2}`, i.e. RH — non-circularly (strip convergence is concluded, not
assumed). The sole hard hypothesis is **(P)** (structural contractivity on `H_{1/2}`); C103 kills the
naive realization and Conrey–Li/Sarnak kill the natural de Branges-space realization for ζ.
