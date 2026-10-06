# Passive colligation / Krein–Pontryagin: the positive-metric route and why it is closed (ckpt9)

**Date:** 2026-10-06. **Status:** DISCLOSED (obstruction, measured + literature-anchored). **RH open.**
**Reproduce:** `scripts/colligation_obstruction.py` (+ `finite_completion_index.py` from ckpt8).

ckpt8 showed the *impedance* route (complete the source response, hope it is passive) is dead:
`F_P` is not positive-real and its Pontryagin index diverges. The directive's remaining hope (§9, §19) is
the **colligation** route: build a finite unitary/passive system whose **transfer function** `Θ_X` is
`≤1` by the unitarity of the system — contractive *by construction*, regardless of how wild the impedance
is. This checkpoint pins exactly what that requires and why the natural realizations are closed.

## What a passive colligation needs

A finite colligation `U = [[A,B],[C,D]]` on `(state) ⊕ (port)` has transfer function
`Θ(λ) = D + C(λ - A)^{-1}B`. `Θ` is a **Schur** function (|Θ|≤1) on the relevant half-plane **iff** the
colligation is contractive in its state-space metric, i.e. iff that **metric is positive-definite** and
the generator is dissipative. So:

> Hypothesis (P) of Schur–Vitali is available **iff** the arithmetic supplies a **positive-definite**
> state-space metric with a dissipative generator whose transfer limit is `Cayley_a[xi'/xi]`.

## The natural metric is indefinite, and not finitely correctable

1. **Impedance realization (ckpt8):** the Laplace-source metric is indefinite and its negative index
   `κ_P → ∞` (excursion count `108→362`). No **fixed finite** Pontryagin index `κ<∞` parent exists for
   this construction, so the §19 Krein escape (finite negative index, then a positive Schur complement)
   is **closed** here.
2. **de Branges realization (Conrey–Li):** the canonical colligation state space for `xi'/xi` is the
   de Branges space `H(E)`, `E(z)=ξ(1-iz)`, whose structural positivity `Re⟨F, F(·+i)⟩ ≥ 0` would make
   the colligation passive and **imply RH**. Conrey–Li (IMRN 2000) prove this positivity **fails** for
   ζ: explicit negative values at the 34th zero and at `w=-282`. So the natural colligation metric is
   **indefinite**.

## The obstruction is a property of the FUNCTION ξ, not of the chosen parent

This is the decisive point (it also closes the history-space escape, HISTORY_SPACE_SOURCE_PORT.md). The
quantity that must be nonnegative — `Re xi'/xi` on `H_{1/2}`, equivalently the positivity of the
Sarnak/Conrey–Li ratio `Re{ξ(s)/ξ(s+1)}` — is a property of the **function** ξ. No Hilbert-space
construction, coupling order, or history lift can change whether a fixed function is positive-real.
Confirmed numerically (`colligation_obstruction.py`):

- **`Re{ξ(s)/ξ(s+1)} = -0.161 < 0` at `s = 0.55 + 110.3 i`** (strip, `Re s>½`). Sarnak's mechanism
  (`Im log(ξ(s)/ξ(s+1)) = Im log ζ + O(1)`, `log ζ` dense on `½<Re s<2`) made manifest.
- **`Re{ξ(1+iτ)/ξ(2+iτ)} = -0.000132 < 0` at `τ = 282`** — reproduces Conrey–Li's published value
  `-0.000131957` to all shown digits (primary-source cross-check).

## The precise obstruction (feeds the obstruction theorem, PROOF_ATTEMPT_006)

> **(P) ⟺ RH.** A finite family `{Θ_X}` with (P) [contractive on all of `H_{1/2}`] and (E) [→
> `Cayley_a[xi'/xi]` on `Re s>1`] exists **iff** RH holds (⇐: take `Θ_X=Cayley_a[xi'/xi]`, Schur iff RH;
> ⇒: Schur–Vitali, C104). Therefore no **unconditional** construction of such a family can exist, from any
> parent. The colligation route does not evade this; it only relocates (P) to "positive-definite
> arithmetic state metric," which — for every natural realization (Laplace-source: divergent index;
> de Branges `H(E)`: Conrey–Li indefinite) — is **false**, and falsified by a **function-level** fact
> (the `ξ(s)/ξ(s+1)` phase) that no parent choice can repair.

**What is NOT excluded (the honest residue).** A structure function or chain of spaces *not* governed by
the single-space de Branges positivity, whose passivity is forced by the arithmetic for a reason
orthogonal to `Re{ξ(s)/ξ(s+1)}≥0`, is not logically excluded by this checkpoint — but constructing one is
equivalent to proving RH, and nothing in the source/ray/SUCC/Archimedean toolkit so far supplies it.

## Ledger

New row **C107**: the passive-colligation route needs a positive-definite arithmetic state metric; every
natural realization is indefinite — the Laplace-source metric has divergent Pontryagin index (ckpt8,
closes the finite-`κ` Krein escape §19), and the de Branges `H(E)`, `E=ξ(1-iz)` metric fails positivity
(Conrey–Li, verified `Re{ξ(1+282i)/ξ(2+282i)}=-0.000132`). The obstruction is function-level
(`Re{ξ(s)/ξ(s+1)}<0` in the strip, confirmed), hence parent-independent; `(P)⟺RH`.
