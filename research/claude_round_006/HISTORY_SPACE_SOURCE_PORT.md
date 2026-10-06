# History-space source port: the escape hatch is not unconditional (ckpt10)

**Date:** 2026-10-06. **Status:** DISCLOSED (parent-independence lemma; escape hatch closed as an
*unconditional* route). **RH open.** **Companion:** `scripts/colligation_obstruction.py`,
`scripts/fucc_succ_composition_carry.py`.

The directive (§14) flags history-before-quotient as "probably the main orthogonal escape hatch": the
full causal FUCC/SUCC history space `H_hist` (the `2^{n-1}` ordered compositions `α ⊨ n`, Pascal-counted)
is strictly larger than the quotient integer/ray space, and Round005 showed conditional
expectation/quotienting can kill carry curvature (C97). So one hopes the coherent history parent retains
cross-phases that make a **passive** completed source response, lost after quotienting.

## What the history space genuinely is (verified)

`fucc_succ_composition_carry.py` confirms: `#{α ⊨ n} = 2^{n-1}`, `k`-cut histories counted by
`binom(n-1,k)` (Pascal), the execution map `P_α(m)` with carry law `n - s_m(P_α(m)) = (m-1)Σ c_j`, and
the augmentation quotient `Q_α(x)=(P_α(x)-n)/(x-1)` storing the exact cut positions. So `H_hist` is a
real, strictly larger, phase-coherent parent, and `E_hist : H_hist → H_integer` (execute to the integer)
is a genuine quotient with nontrivial fibers. C102 (this round) already corrected the Round005
overstatement: endpoint kernel equality under reordering does **not** make `H_hist` irrelevant to a
factorization. So the hatch is a priori open.

## Why it is nonetheless not an unconditional escape — the parent-independence lemma

**Lemma (parent-independence).** The property that must hold for RH — `xi'/xi` positive-real on
`H_{1/2}`, equivalently `Re{ξ(s)/ξ(s+1)} ≥ 0` on `Re s>½` — is a property of the **function** `ξ`. No
Hilbert-space parent, coupling order, or history lift changes the value of a fixed function. Concretely
(ckpt9): `Re{ξ(s)/ξ(s+1)} = -0.161 < 0` at `s=0.55+110.3i`, and `Re{ξ(1+282i)/ξ(2+282i)}=-0.000132<0`.
These negativities are facts about `ξ`; a coherent history parent cannot delete them.

What the history space *can* change is the family of finite **transfer functions** `Θ_X` (different
parent ⇒ different finite approximants). But the Schur–Vitali reduction (C104) forces:

- **(P)+(E) ⟺ RH**, from any parent. A history-space family that is contractive on `H_{1/2}` (P) and
  converges to `Cayley_a[xi'/xi]` on `Re s>1` (E) exists **iff** RH. So history-before-quotient is subject
  to exactly the same equivalence; it is not an unconditional escape.

**Reading of the hatch.** The hope "cross-phases in `H_hist` → passive response, lost after quotient" is
half right and half wrong:
- *Right:* the quotient does lose structure (C97/C102); couple-before-quotient is a genuinely different,
  richer parent.
- *Wrong:* the **passivity we need** is not a feature of the parent that the quotient could destroy — it
  is positive-realness of the **endpoint function** `xi'/xi`, which is quotient-invariant. The quotient
  cannot turn a positive-real endpoint into a non-positive-real one or vice versa. So there is no way for
  "passive before quotient, non-passive after" to hold for the RH-bearing object: both before and after,
  the endpoint is the same `xi'/xi`, with the same (RH-equivalent) positive-realness.

The only residue is the same as in PASSIVE_COLLIGATION: a history-space family could meet (P) *if RH is
true*, giving a proof — but verifying (P) requires beating the function-level `ξ(s)/ξ(s+1)` obstruction,
which the history structure does not touch. So the hatch does not lower the bar; it relocates it.

## Ledger

New row **C108**: parent-independence lemma. The RH-equivalent positivity (`Re{ξ(s)/ξ(s+1)}≥0` on
`H_{1/2}`) is a property of the function `ξ`, confirmed violated in the strip (`-0.161` at `0.55+110i`;
`-0.000132` at `1+282i`). Hence the history-before-quotient escape (§14) is NOT an unconditional route:
`(P)+(E) ⟺ RH` from any parent, and the quotient cannot change positive-realness of the endpoint. The
history space gives different finite approximants `Θ_X`, not a lower bar; verifying (P) still requires
beating a function-level obstruction the parent choice does not touch.
