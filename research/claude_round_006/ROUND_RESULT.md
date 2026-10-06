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

> **[after ckpt 2]** Wall inherited from Round004/005 = real-axis
> renormalization positivity of the coupled prime+pole trace (= Weil). Round006 reframes it as:
> *is the completed finite source response positive-real / passive on `Re s > 1/2`?*
> First concrete datum already in hand: `-zeta'/zeta` is **NOT** positive-real even on `Re s > 1`
> (`Re(-zeta'/zeta)(1.5 - 2i) = -0.262 < 0`), so per-ray one-ports are **not** passive — passivity, if
> it exists, must be a property of the COMPLETED, COUPLED system. This is the seed of the §5 no-go and
> the whole-round question.

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

## Net ledger additions this round

- C100/C101/C102: scope corrections (meta).
- (pending C103+: source layer, correlation category, passivity classification.)

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
