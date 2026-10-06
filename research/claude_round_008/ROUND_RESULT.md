# Round 008 — de Bruijn–Newman heat flow ("full blast")

**Branch:** `claude/heat-flow-008` (from `main`). **RH IS OPEN.**

## CURRENT WALL (live)

> **[after ckpt1]** The dBN heat flow is a rigorous, *separate* RH-equivalent framework that unifies with
> our program through one shared coordinate `b = β−½` (= `−Im(dBN zero)` = Round-007 growth exponent =
> the driver that sends the screw-kernel margin negative, measured `∝ −b²`). The flow is the canonical
> Coulomb-gas gradient dynamics on `b`; `RH ⟺ Λ≤0 ⟺ K_Ψ⪰0 ⟺ Ψ bounded ⟺ b≡0`. **But the heat flow
> supplies no new leverage:** the unification is tautological (all are RH), the one hard theorem
> (Rodgers–Tao `Λ≥0`) is a *lower* bound (wrong way for RH), the natural energy/equilibrium bridge is
> *backwards*, and no dBN↔Weil/CND bridge is established. `Λ≤0` (RH) is as walled as ever. The C84
> knife-edge ↔ `Λ≥0` "RH barely true" is a genuine resonance but not a theorem.

## Checkpoint log

1. **[done]** Heat-flow bridge (HEAT_FLOW_BRIDGE.md, C115/C116). Built + verified the arithmetic dBN
   backbone `H_t` from Φ (`H_0=½Ξ`, ratio 0.5000 to `1e-11`); the zero ODE and gradient/Lyapunov structure
   (lit-locked); the rigorous `b`-identification unifying dBN / growth cascade / screw-kernel; demonstrated
   `b>0 ⟺ screw margin <0`; honest no-leverage verdict + correction of the earlier oversell.

## Net ledger additions

- C115: the shared coordinate `b`; dBN flow = Coulomb/gradient dynamics on `b`; arithmetic `H_t` verified.
- C116: honest no-leverage verdict (separate RH-circle; `Λ≥0` is the lower bound; energy bridge backwards;
  no dBN↔Weil/CND bridge; C84↔`Λ≥0` is a resonance).

## Honest status

"Full blast at the heat flow" produced a clean, rigorous **unification** (three frameworks, one coordinate
`b`) and an important **honesty correction** (the heat flow is not the shortcut I'd suggested). It did
**not** produce a proof step toward RH. The proven direction (`Λ≥0`) is the lower bound; the RH direction
(`Λ≤0`) has no new handle, and the literature does not bridge dBN to the positivity machinery (Weil/CND)
our program is built on. The most useful residue is the confirmed picture that RH, if true, is true with
vanishing margin (Rodgers–Tao `Λ≥0` ⟷ our C84 knife-edge) — which constrains *how* a proof must look
(no slack to exploit) more than it opens a route.
