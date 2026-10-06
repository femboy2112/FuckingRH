# Round 006 — SOURCE PORT / PASSIVITY / TAKE THE FUCKING LIMIT

**Branch:** `claude/source-port-passivity-006` (forked from Round005 head `3222f97`).
**Status:** IN PROGRESS. **RH IS OPEN.**

## The thesis of the round

SUCC boots the system: `|0> --S--> |1> = Omega` is the multiplicative source. Every prime ray
`Omega -> |p> -> |p^2> -> ...` is **prewired**. The SUCC worldline `S^n|0>=|n>` intersects the rays
exactly at prime powers; the weighted incidence is von Mangoldt `Lambda`. The log-energy generator `H`
drives the `t`-action; the common-source correlation is `-zeta'/zeta`; the Archimedean boundary
completes it to `xi'/xi`. Classically (Lagarias 1999):

    RH  <=>  Re[xi'/xi(s)] > 0  for Re(s) > 1/2   (xi'/xi is positive-real on the right half-plane).

**Target:** build FINITE arithmetic source circuits that are **passive by construction** (Schur transfer
functions contractive on `Re s > 1/2`), converge to `Cayley[xi'/xi]` only where **Euler is safe**
(`Re s > 1`), and let **normal-family / Vitali compactness take the limit**. If achieved without zero
ordinates and without assuming strip convergence, RH follows.

## CURRENT WALL  (live — updated every checkpoint)

> **[after ckpt 5]** The wall has MOVED to a precise location. It is no longer "the per-ray object is not
> passive" (that is now a *settled no-go*, C103, rigorous): the one-port/direct-sum class is dead because
> `s |-> p^s` is exponential/periodic and cannot transport the arithmetic's Cauchy-Herglotz-in-`w`
> positivity to the `s`-half-plane. **The live wall is now:** *does a GENUINE coupling across rays +
> the Archimedean completion (the only pieces not a function of any single `p^s`) produce a finite
> object that is structurally passive on `Re s>1/2`?* The Archimedean port is the suspect load-bearing
> piece, and the Schur/Vitali limit lemma is the mechanism that would close the deal IF such a family
> exists.
>
> **[after ckpt 7]** The wall is now SHARP and split in two. The Archimedean port (C105) is realizable:
> a genuinely passive Γ-channel (resolvent of `D_Γ=2N`, poles at the trivial zeros outside `H_{1/2}`)
> plus a pole part whose only `H_{1/2}` singularity is the SINGLE pole at `s=1` (one negative square,
> `κ=1`). So the finite-completion problem reduces to **(1)** cancel the `s=1` pole at finite `P` with a
> cutoff-dependent boundary `A_{inf,P}` [solvable — Euler–Maclaurin counterterm, ckpt8], and **(2)** make
> the pole-cancelled finite `F_P` positive-real on `H_{1/2}` [the real wall]. (2) is where Conrey–Li/
> Sarnak bite: the `ξ(s)/ξ(s+1)` phase (dense `log ζ`) forces `Re<0` in the strip unless the coupling
> dodges it. Next: build the finite coupled Schur-complement with explicit `A_{inf,P}` (ckpt8) and test
> (2) directly.

## Checkpoint log

1. **[done]** Integrate the two Aletheia side branches (source-wired prime rays + FUCC/SUCC
   composition-carry). Scripts re-verified: incidence reproduces `Lambda` and `Lambda/sqrt n` (n<300);
   `J_sigma^* e^{itH} J_sigma = -zeta'/zeta(sigma-it)|Omega><Omega|` to prime-tail accuracy;
   `m_p(s)=log p/(p^s-1)`; `2^{n-1}` compositions = causal FUCC histories, Pascal-counted, carry law
   `n - s_m(N) = (m-1) sum c_j`, radix-3 carry-free = Fibonacci.
2. **[done]** Scope corrections (SCOPE_CORRECTIONS.md, ledger C100/C101/C102): C98 refutes only the
   shared-DC mechanism (not all algebraic renorm); C99 carré gives the *weighted/repaired* local energy
   (not raw Λ); birth-order kernel-invariance does *not* kill history-space factorizations.
3. **[done]** Source-ray incidence + event-weight factorization (SOURCE_RAY_INCIDENCE.md, ckpt3).
   Operator-level (not just scalar): `E^*E=I_ray` exact; `W_beta|n>=Lambda(n)n^{-beta}|n>`;
   `B_beta^*B_beta=W_beta` exact (`<1e-15`). Non-circular factorization of the DIAGONAL event weight —
   not of `K_Psi`.
4. **[done]** Source correlation = log-derivative (SOURCE_CORRELATION_LOG_DERIVATIVE.md, ckpt4).
   `J_sigma^* e^{itH} J_sigma = -zeta'/zeta(sigma-it)|Omega><Omega|` exact for Re s>1. KEY CATEGORY
   FINDING: this is a rank-1 AUTOCORRELATION, positive-DEFINITE in `t` (Bochner), which is NOT
   positive-REAL in `s` — numerics show `Re(-zeta'/zeta)<0` at (2,1.3),(1.5,2),(3,5). The two
   positivities are different theorems; bridging them is the round.

5. **[done]** Branch-transfer passivity classification (BRANCH_TRANSFER_CLASSIFICATION.md, ckpt5,
   ledger C103). Rigorous no-go: `m_p` not positive-real on any right half-plane (periodicity-in-`s`);
   `-zeta'/zeta` not positive-real on Re s>1; the arithmetic carries only Cauchy-Herglotz-in-`w` and
   real-axis complete monotonicity, neither transporting to `s`-positivity; raw Cauchy transform diverges
   (`psi(x)~x`). Kills the one-port/direct-sum class; forces coupling + Archimedean completion.

6. **[done]** Schur–Vitali continuation theorem (SCHUR_VITALI_LIMIT.md + LITERATURE_INTERFACE.md,
   ckpt6, ledger C104). PROVED: contractive-on-all-of-`H_{1/2}` (P) + Euler-region convergence (E) ⇒
   `xi'/xi` positive-real on `H_{1/2}` ⇒ RH, **non-circularly** (strip convergence concluded, not
   assumed). Demo confirms the mechanism and that (P) is the essential, non-automatic hypothesis.
   Literature locked (Lagarias/Hinkkanen criterion; 2005 correction; de Branges positivity; Conrey–Li +
   Sarnak show the natural de Branges-space positivity FAILS for ζ — a direct obstruction to the obvious
   realization of (P)).
7. **[done]** Archimedean source port (ARCHIMEDEAN_SOURCE_PORT.md, ckpt7, ledger C105). `A_inf` =
   passive Γ-channel (regularized resolvent of `D_Γ=2N`, poles at trivial zeros, outside `H_{1/2}`) +
   pole part whose only `H_{1/2}` pole is the single one at `s=1` (one negative square, κ=1). Finite
   `F_P` has an `s=1` pole for every finite `P` (emergent only as `P→∞`) ⇒ finite completion needs a
   cutoff-dependent boundary `A_{inf,P}`. Reduces to (1) pole cancellation [solvable] + (2) positive-
   realness of the pole-cancelled finite object [the wall].

## Net ledger additions this round

- C100/C101/C102: scope corrections (meta).
- C103: one-port/direct-sum class is RH-inert for positivity (rigorous no-go).
- C104: Schur–Vitali continuation theorem (the round's central reduction; conditional on (P)).
- C105: Archimedean port = passive Γ-channel + single κ=1 pole at s=1; finite completion needs A_{inf,P}.

## What would count as a crack (from the directive §24)

A. explicit finite passive colligations `Theta_X` contractive on `Re s>1/2`;
B. exact Archimedean port coupling to finite prime rays → completed source response;
C. the Schur/Vitali limit theorem + an arithmetic family meeting its hypotheses;
D. a source-star Schur complement with manifest finite-volume positivity and `xi'/xi` Euler limit;
E. history-before-quotient construction passive where the quotient is not;
F. a rigorous obstruction theorem killing a precise natural class.

Not a crack: another rewrite of `xi'/xi`; another numerical positivity plot; another `sqrt(K)`; another
direct sum of local `B_p`; assuming convergence on `Re s>1/2`; inserting zeros; "it's Weil" with no
named failed operator property.
