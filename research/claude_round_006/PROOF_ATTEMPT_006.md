# Proof attempt 006 — source port / passivity / take the fucking limit

**Date:** 2026-10-06. **Verdict:** RH remains open. **Outcome (2):** the central new route (finite passive
source completion) is killed by a precise, unconditional obstruction for its natural class, and the two
escape hatches (Krein finite-index; colligation / history-before-quotient) are closed by a
function-level obstruction; the surviving class is strictly smaller and named. One clean positive theorem
landed (the Schur–Vitali reduction), plus the exact Archimedean port structure.

## The target

Realize `xi'/xi` as a **positive-real** function on `H_{1/2}={Re s>1/2}` (⟺ RH, Lagarias(1999)(1.5)/
(1.19), equivalence due to Hinkkanen) as a **limit of structurally-passive finite arithmetic objects**,
converging only where Euler is safe (`Re s>1`), letting normal-family compactness take the limit — all
without zero ordinates and without assuming strip convergence.

## What landed

### Positive theorem (DISCLOSED): the Schur–Vitali reduction (C104)
`SCHUR_VITALI_LIMIT.md`. If finite `Θ_X` are holomorphic and **contractive on all of `H_{1/2}`** (P) and
converge to `Cayley_a[xi'/xi]` locally uniformly **only on `Re s>1`** (E), then `xi'/xi` continues
positive-real to `H_{1/2}`, hence **RH** — and this is **non-circular** (strip convergence is a
*conclusion* via Montel + identity theorem, never a hypothesis). Proved (Vitali–Porter + Cayley),
demo-confirmed, edge cases handled. This compresses all RH content into the single hypothesis (P).

### Exact structure (DISCLOSED)
- **Source layer (C-source, ckpt3–4):** `E^*E=I_ray`; `Lambda(n)=Σ_{p,k}log p⟨n|V_p^kΩ⟩`;
  `W_β=EQe^{-βH}E^*` diagonal with `W_β|n>=Λ(n)n^{-β}|n>`; `B_β^*B_β=W_β` exact (non-circular factor of
  the **diagonal** weight, not `K_Ψ`); `J_σ^* e^{itH} J_σ=-ζ'/ζ(σ-it)|Ω><Ω|`.
- **Archimedean port (C105, ckpt7):** `A_inf =` passive Γ-channel `½ψ(s/2)=` regularized resolvent of
  `D_Γ=2N` (poles at trivial zeros, `Re≤0`, outside `H_{1/2}`) `+` pole part whose only `H_{1/2}`
  singularity is the single pole at `s=1` (one negative square `κ=1`). `xi'/xi(1)=-B=0.023096`.

## No-gos (DISCLOSED)

- **C103 (ckpt5):** `m_p(s)=log p/(p^s-1)` is not positive-real on any right half-plane (periodicity-in-
  `s`); nor is `-ζ'/ζ` on `Re s>1`. The arithmetic carries only Cauchy-Herglotz in `w=p^s` and real-axis
  complete monotonicity, neither transporting to `s`-positivity. **Kills the one-port/direct-sum class.**
- **C106 (ckpt8):** the Euler–Maclaurin boundary `reg_P=(1-P^{1-s})/(s-1)` makes the finite completion
  `F_P` holomorphic on `H_{1/2}` and `→xi'/xi` on `Re s>1` (E ✓), but `F_P` is **not positive-real**:
  `max|Re F_P|~P^{1-σ}→∞` near the line, Pontryagin index `κ_P→∞` (108→362). **Kills the Laplace/
  source-response completion class for (P); closes the finite-`κ` Krein escape (§19).**
- **C107 (ckpt9):** a passive colligation needs a positive-definite arithmetic state metric; every natural
  realization is indefinite (Laplace-source: divergent index; de Branges `H(E)`, `E=ξ(1-iz)`: Conrey–Li
  positivity failure, verified `Re{ξ(1+282i)/ξ(2+282i)}=-0.000132`).
- **C108 (ckpt10):** **parent-independence lemma** — the RH-equivalent positivity is a property of the
  function `ξ` (`Re{ξ(s)/ξ(s+1)}=-0.161<0` at `0.55+110i`; Sarnak), so history-before-quotient and all
  coupling orders are **not unconditional escapes**: `(P)+(E)⟺RH` from any parent.

## The obstruction theorem (§18, precise, unconditional)

> **Theorem (source-response completion is not passive).** Let the *source-response completion class* be
> `{F_P}` where `F_P(s)=A_{inf,P}(s)-Σ_{p^k≤P}Λ(p^k)(p^k)^{-s}`, the prime part the genuine finite von
> Mangoldt Dirichlet polynomial and `A_{inf,P}` any holomorphic boundary making `F_P` holomorphic on
> `H_{1/2}` with `A_{inf,P}→A_inf` locally uniformly on `Re s>1`. Then
> `inf_{s∈H_{1/2}} Re F_P(s) → -∞` as `P→∞`. Consequently no `F_P` is positive-real on `H_{1/2}` for
> large `P`, and the Pontryagin index of `Cayley_a[F_P]` diverges — so the class cannot satisfy
> Schur–Vitali hypothesis (P). This is **independent of RH**.

*Proof sketch.* By Dirichlet's simultaneous-approximation theorem, for each `σ_0>½` and `ε>0` there is a
(large) `t` with `|n^{-it}-1|<ε` for all `n≤P`; then
`Re Σ_{n≤P}Λ(n)n^{-(σ_0+it)} ≥ (1-ε')Σ_{n≤P}Λ(n)n^{-σ_0} = (1-ε')·P^{1-σ_0}/(1-σ_0)·(1+o(1))` by partial
summation and `ψ(x)~x` (PNT). At such `t` the boundary is negligible (`½ψ(s/2)~½log t`; `reg_P→0`), so
`Re F_P ≤ -c·P^{1-σ_0}`. Letting `σ_0↓½` along `P` gives `inf Re F_P ≤ -c√P → -∞`. ∎ (modulo standard
Dirichlet-polynomial estimates; the numerics in `finite_completion_index.py` confirm the growth of both
`max|Re F_P|` and the excursion count on bounded windows.)

*Index nuance (verified).* For fixed `P`, `Re F_P<-a` holds on a **positive-density** `t`-set (measured
density `≈0.65` on `σ=0.51`, stable across `T=300,1000,3000`), but only within an **active window**
`t ≲ exp(2·amplitude)`: as `t→∞` the Archimedean `½ψ(s/2)~½log(t/2)→+∞` eventually dominates the bounded
prime fluctuation and `Re F_P>0` thereafter. So `κ_P` (number of strip poles of `Cayley_a[F_P]`) is
**finite for each `P` but unbounded as `P→∞`** (the active window grows with the `√P`-type amplitude).
This is what closes the *fixed-finite-`κ`* Krein escape (§19); it is not a claim of literally infinite
index.

**Which hypothesis must break to escape:** the finite member must **not** be the source-response impedance
`F_P` itself, but a colligation transfer function `Θ_X` bounded `≤1` *by construction* (positive metric).
That relocates (P) to "positive-definite arithmetic state metric," which C107/C108 show is false for every
natural realization and blocked by a **function-level** obstruction (Conrey–Li/Sarnak) no parent dodges.

## The sharpened wall (current)

RH `=` hypothesis (P) `=` the existence of a **positive-definite arithmetic state metric** whose transfer
limit is `Cayley_a[xi'/xi]`. Equivalently (parent-free): `Re{ξ(s)/ξ(s+1)}≥0` on `H_{1/2}`. This is RH
restated in passivity language, now with: (i) the limit mechanism fully proved and non-circular (C104);
(ii) the Archimedean port realized, obstruction localized to one `κ=1` pole + the prime fluctuation;
(iii) the impedance/Laplace-completion and finite-`κ` Krein routes killed unconditionally (obstruction
theorem); (iv) the colligation/history routes shown non-unconditional and blocked function-level. The wall
is the **positivity of the completed von Mangoldt fluctuation against the line, uniformly in the cutoff** —
the same Weil/renormalization wall as Round004 C91, now named as "no positive-definite finite arithmetic
state metric," with the Conrey–Li/Sarnak phase density as the concrete mechanism of failure.

## Where to hit next (future round)

1. The only logically-open door: a structure function / chain of de Branges spaces whose positivity is
   **not** the single-space `Re⟨F,F(·+i)⟩≥0` condition and is still arithmetically forced — i.e. a
   positivity orthogonal to the `ξ(s)/ξ(s+1)` phase. This is the actual open problem; nothing in the
   source/ray/SUCC/Archimedean toolkit supplies it.
2. Quantify the index growth: prove `κ_P ≍ (prime count)` or a sharp rate, turning the "diverges" into a
   rate law (as C84's collapse-rate did for the tilt).
3. A genuine SUCC-braided (cross-ray) colligation: does the irregular-log-step coupling (Round004 core)
   change the *sign* of the metric's smallest eigenvalue at finite cutoff, or only its magnitude? (Expect:
   magnitude only — same wall — but this is the one untested finite experiment.)
