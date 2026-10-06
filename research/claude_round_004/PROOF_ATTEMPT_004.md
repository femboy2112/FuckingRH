# Proof attempt 004 — Pascal / binomial / Möbius-Hodge / affine attack on an arithmetic B_L

**Date:** 2026-10-06
**Verdict:** RH remains open. The round did not produce a global non-circular $B_L$. It produced one
structural meta-theorem, two exact constructive positives, four clean no-gos, and a sharpened wall.

## The target

\[
K_{\Psi,L}=B_L^\*B_L,\quad B_L\ \text{from arithmetic (SUCC/FUCC/Euler/affine/Archimedean) only —}
\]
no diagonalizing $K_\Psi$, no assuming $K_\Psi\succeq0$, no zero ordinates, no functional calculus of
$K_\Psi$. Equivalently a global operator $B$ with $B_L=\mathrm{compr}_L(B)$.

## What landed

### Meta-theorem (DISCLOSED, proved 4 ways): commutative-multiplicative ⇒ factorized ⇒ RH-inert
Every factor built from the **commuting** prime dilations (and functions of them), without the additive
successor or the Archimedean place, yields a factorized Gram that carries no zero information:
1. **Uniform-time Pascal innovation Gram** $G_L=\Pi^{-1}K_{\Psi,L}\Pi^{-T}$ equals the **zero-moment
   matrix** $\sum_\gamma\bar z_\gamma^k z_\gamma^\ell/\gamma^2$, $z_\gamma=e^{i\gamma h}-1$ — it
   *re-encodes the zeros*, circular (PASCAL_INNOVATION_GRAM).
2. **Multiplicative binomial Fock** $J_B$ is an **isometry** ($J_B^\*J_B=I$) — trivial Gram
   (MULTIPLICATIVE_BINOMIAL_FOCK).
3. **Koszul/Hodge Laplacian** on the prime-exponent lattice **factorizes**: the degree-1 cross block is
   the commutator $[\tilde\nabla_p,\tilde\nabla_q^\*]=0$ (MOBIUS_FERMIONIC_COMPLEX).
4. All three coincide with the **GCD kernel** $\gcd/\sqrt{ab}$ already known RH-inert (C81).
The RH-bearing cross terms exist only as **products** $V_p^\*V_q$ (nonzero), never as commutators;
they require the **noncommutative affine braid** $V_mS=S^mV_m$ or the Archimedean place.

### Constructive positives (DISCLOSED)
- **Exact local operator squares.** The repaired tower $D_p$ has the closed-form positive spectral
  density $\sigma_p=(1-\cos\log p\,\xi)\times$(Euler/Poisson whitening)$\ge0$, giving
  $B_p(t)(\xi)=\frac{e^{i\xi t}-1}{\xi}\sqrt{\sigma_p}$; $M_p=\frac{r\log p}{1-r}$ is *forced* by
  $\sigma_p\ge0$ (ARITHMETIC_BL_CONSTRUCTION). Non-circular, manifestly positive, local.
- **Euler identity = discrete exactness.** $\Lambda=\mu*\log=(\prod_{p\mid n}\nabla_p)\log$ vanishes on
  $\omega(n)\ge2$ because a mixed difference of an additive function is $0$ (MOBIUS_FERMIONIC_COMPLEX §1).
- **Binomial-Fock contraction = prime-swap.** $J_B^\*(|q\rangle\langle p|\otimes I)J_B$ gives exactly the
  C79 coupling $[pm=qn]$, binomial-dressed (MULTIPLICATIVE_BINOMIAL_FOCK §2).

### No-gos (DISCLOSED)
- Uniform Pascal factor is circular (zero-moment).
- Rank-2 pole is **inseparable** from the primes ($K_\Psi-K_E$ min eig $\sim-2\times10^4$) — earlier round.
- Koszul/Hodge Laplacian factorizes — no cross coupling.
- **Schematic affine KMS CRT Gram is not PSD at $\beta=1/2$** (min eig $-1.10$): the naive residue-
  projection values fail state-consistency $\sum_r\phi(e_{r,a})=a^{1-\beta}\ne1$; the critical KMS state
  is not a measure, so "affine cross terms = free positivity" is false without the exact Laca–Raeburn
  state. (AFFINE_CROSS_TERM_GRAM caution.)

### Corrections / refinements (OBSERVED)
- **C84 corrected** (continuity audit): reduced $K^\circ$ is strictly PD at the true weights
  ($\lambda_{\min}\approx0.00467$ at $T=8$); the knife-edge is an *asymptotic* shrinking window
  $\mathcal E_L\downarrow\{0\}$, not a finite-grid exact boundary.
- **Finite-only tilt vs completed shift are different**: the completed shift breaks positivity for any
  $\omega\ne0$ (exponential $\cosh\omega t$, set $=\{0\}$); the finite-only tilt has radius
  $\epsilon_+\sim e^{-0.85\,T}$ (OBSERVED), collapsing to $0$ (COMPLETED_SHIFT_STABILITY).

## The sharpened wall (current)

Local Route-B factors are solved in closed form and manifestly $\ge0$. Globally,
\[
\sigma_{\rm total}=\sum_{p}\sigma_p+\sigma_\infty-\sigma_{\rm pole}=\sum_\gamma\gamma^{-2}(\delta_\gamma+\delta_{-\gamma}),
\]
with each $\sigma_p\ge0$, $\sigma_\infty\ge0$, the pole a positive atom at **imaginary** $\xi=i/2$, and
$\sum_p\sigma_p(\xi)$ **divergent** on the real axis ($\sim2\sqrt{e^L}$). RH $=$ the renormalized
real-axis measure stays $\ge0$ after the pole subtraction, uniformly in $L$ — slack-free. This is the
same Weil/renormalization wall, now with explicit positive local factors and the obstruction localized
to the real-axis renormalization against the pole (not to any multiplicative cross-coupling).

## Where to hit next (for a future round)
1. The **noncommutative affine Dirac/BC spectral triple** (the one Hodge variant whose Laplacian need
   not factorize because $[V_p,S]\ne0$) — build it concretely and test compression to $K_\Psi$.
2. The **exact Laca–Raeburn KMS$_{1/2}$ state** for the affine CRT Gram (the schematic one failed).
3. A rigorous **collapse-rate theorem** $\operatorname{rad}(\mathcal E_L)\le Ce^{-cL}$ from Euler sums
   (would be real quantitative progress toward the slack-free statement).
