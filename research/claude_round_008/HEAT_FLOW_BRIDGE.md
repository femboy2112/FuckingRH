# The de Bruijn–Newman heat flow: one shared coordinate, and an honest reassessment

**Date:** 2026-10-06. **Status:** DISCLOSED (rigorous identification + demonstrated unification) + honest
no-leverage verdict. **RH open.** **Reproduce:** `scripts/r008_dbn_backbone.py` (H_t from the arithmetic
kernel Φ, verified `H_0=½Ξ`), `scripts/r008_margin_flow.py`, and the forced-complex-pair demo.
**Literature:** Rodgers–Tao, *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi 8 (2020) e6,
arXiv:1801.05914; Polymath15, arXiv:1904.12438; Csordas–Smith–Varga (1994); Tao's heat-flow blog.

## Setup (literature-locked)

`Φ(u) = Σ_{n≥1}(2π²n⁴e^{9u} − 3πn²e^{5u})exp(−πn²e^{4u})` (even), `H_t(x)=∫_0^∞ e^{tu²}Φ(u)cos(xu)du`,
`H_0(x)=⅛ξ(½+ix/2)=⅛Ξ(x/2)`; backward heat `∂_t H = −∂_{xx}H`. (Our scripts use the `u/2`-substituted
variant `H_0=½Ξ(x)`, zeros at `x=γ_n`; verified against mpmath `Ξ` to ratio `0.50000` down to `|Ξ|~1e-11`.
Convention-independent facts below hold in either.) `Λ` = de Bruijn–Newman constant: `H_t` all-real-zeros
`⟺ t≥Λ`; `RH ⟺ Λ≤0`; **Rodgers–Tao: `Λ≥0`** (so `Λ=0 ⟺ RH`, "RH barely true"). Zero flow (RT eq.56):
`∂_t x_k = 2 Σ'_{j≠k} 1/(x_k−x_j)` (repulsive; gradient ascent of `S=Σ_{j<k}log|x_j−x_k|`).

## The rigorous payoff: one coordinate `b`, three frameworks

A zeta zero `ρ=β+iγ` corresponds to a zero of `H_0` at `x = γ − i(β−½)` (from `½+ix=ρ`). Hence

    b := β − ½  =  −Im(dBN x-zero)  =  distance of ρ from the critical line.

This single `b` is simultaneously:
1. **the dBN zero's imaginary part** — what the heat flow pushes to zero (`Λ` = how much `t` is needed);
2. **our growth-cascade exponent** (Round 007): a zero contributes `e^{(β−½)t}=e^{bt}` to Ψ's growth;
3. **the screw-kernel's negativity driver** (demonstrated): displacing one zero to `b>0` sends the screw
   kernel's smallest eigenvalue **negative** — measured `b=0.02→−6e−9, 0.05→−2e−5, 0.10→−7e−4, 0.20→−2e−2`
   (`∝ b²` for small `b`); `b=0 ⟺ K_Ψ⪰0 ⟺` CND `⟺` Ψ bounded.

So `RH ⟺ b=0 for all zeros ⟺ Λ≤0 ⟺ K_Ψ⪰0 ⟺ Ψ bounded` — the dBN flow, our growth cascade, and the
screw/CND positivity are **the same statement read on the same coordinate `b`**, and the heat flow is the
canonical (Coulomb-gas, gradient) dynamics on `b`. That identification is exact and convention-free.

## Honest reassessment (correcting my earlier oversell)

I had flagged the heat flow as "the one direction with live, non-obstructed machinery." Working it
carefully, that was too optimistic. The honest situation:

1. **The frameworks are the same RH, not complementary leverage.** The unification above is, at bottom, a
   tautology: all four statements *are* RH, now seen to share the coordinate `b`. Reading RH through the
   flow does not add proving power — it relabels the same wall.
2. **The one hard theorem points the wrong way.** Rodgers–Tao proved `Λ≥0` — a **lower** bound. RH needs
   `Λ≤0`. Their mechanism (contradiction: `Λ<0` would force the `t=0` zeros into near-equispaced
   *equilibrium*, which Montgomery pair-correlation refutes) is powered by the zeros' *fluctuations* and
   can only bound `Λ` from below. It gives no handle on `Λ≤0`.
3. **The natural energy-bridge is backwards.** I had guessed "`Λ≤0` ⟺ the zero gas is already at
   equilibrium energy at `t=0`." That is inverted: equilibrium-at-`t=0` is exactly what `Λ<0` would
   require, and it is *disproved*. `Λ=0` (RH) is the borderline "critical at `t=0`, any earlier and a pair
   splits off." There is **no published theorem** expressing `Λ≤0` as an energy/equilibrium positivity
   criterion (primary-source check), and **no established bridge** from the dBN flow to Weil positivity or
   to the Lévy/CND structure of `log|ξ|`. I did not establish one either (beyond the `b`-identification).

**Net:** the heat flow is a beautiful, rigorous, *separate* RH-equivalent circle that unifies cleanly with
our objects through the coordinate `b` — but it supplies **no new leverage** toward RH, and its proven
content (`Λ≥0`) is the lower bound, away from RH.

## The one genuine resonance (observation, not theorem)

Rodgers–Tao's `Λ≥0` says RH, *if true, is true by the narrowest margin*. Our Round-004 finding C84 —
measured — was that the prime-built screw kernel sits on the **PSD-cone boundary** with a positivity margin
that shrinks (the "slack-free / knife-edge" observation, `λ_min→0` on a shrinking window). These are two
independent routes to the **same qualitative picture**: the positivity holds with vanishing slack. The
`b`-identification makes the link concrete (the screw margin `∝ −b²` near a zero, and `Λ` is the flow time
to reach `b=0`), but a *theorem* equating the C84 margin with `Λ` is not established — present it as a
resonance, not a result.

## Ledger

New rows **C115** (the shared coordinate: `b=β−½ = −Im(dBN zero) = growth-cascade exponent =
screw-kernel negativity driver`, measured `margin ∝ −b²`; dBN flow is the canonical Coulomb/gradient
dynamics on `b`; `H_t` built and verified from the arithmetic Φ, `H_0=½Ξ`) and **C116** (honest
no-leverage verdict: dBN is a *separate* RH-equivalent circle unifying with our objects only
tautologically; `Λ≥0` (Rodgers–Tao) is a lower bound, the wrong direction for RH; the energy/equilibrium
bridge is backwards and no dBN↔Weil/CND bridge is established — corrects the earlier oversell. The C84
knife-edge ↔ `Λ≥0` "RH barely true" is a resonance, not a theorem).
