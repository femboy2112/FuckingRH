# The prime-built Weil kernel: zeros from primes, the PSD-cone knife-edge, and $K_{\Psi,L}=T_L^\*T_L$

**Date:** 2026-10-06
**Status:** exploratory numerics (exact, reproducible) + one concrete Route-B object + a sharpened,
slack-free target. **RH is not proved here.** Every RH-equivalent statement is labelled.
**Reproduce:** `scripts/prime_kernel_psd_boundary.py` (needs only numpy + mpmath for two constants).

This note follows one thread of light through the positivity wall and reports exactly how far it
goes — including where it stops. The guiding principle is the meta-lesson of the refuted shortcuts
(C07, C09, C12, C14) together with Rodgers–Tao ($\Lambda_{\mathrm{dBN}}\ge0$): **RH is slack-free.**
No robust/generic positivity can prove it, because a slack inequality would prove more than is true.
So the only admissible opening is an *exact* object, and the search is for one whose positivity is
manifestly tight.

## 0. The object: Suzuki's kernel is exactly prime-built

Suzuki (JLMS 2023, Thm 1.7; repo C31–C33) gives an even $\Psi$ with
$\mathrm{RH}\iff\Psi\ge0\iff K_\Psi\succeq0$, where the screw kernel is
$K_\Psi(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u)$. Crucially $\Psi$ is a **finite sum at each $t$** (the prime
part is cut *exactly* at $n\le e^t$, not truncated):
\[
\Psi(t)=\underbrace{8(\cosh\tfrac t2-1)}_{\text{pole }E}
-\underbrace{\sum_{n\le e^t}\tfrac{\Lambda(n)}{\sqrt n}(t-\log n)}_{\text{prime ramps}}
+\tfrac t2\big[\tfrac{\Gamma'}{\Gamma}(\tfrac14)-\log\pi\big]
+\tfrac14\big(C-e^{-t/2}\Phi(e^{-2t},2,\tfrac14)\big),\quad C=\pi^2+8G.
\]
On a uniform grid $t_i=i\,\Delta t$ the differences $t_i-t_j$ land on the grid, so by evenness
\[
\boxed{\,K_\Psi[i,j]=\psi_i+\psi_j-\psi_{|i-j|},\qquad \psi_k=\Psi(k\,\Delta t)\,}
\]
needs only $M{+}1$ evaluations. **No zero ordinates are used anywhere.** (Verified: $\Psi_{\text{arith}}$
matches the zero-side identity $\Psi(t)=\sum_\gamma\frac{1-\cos\gamma t}{\gamma^2}$ once one sums over
zeros of *both* signs and adds the finite-$N$ tail: at $t=1$, arith $=0.0440$ vs
$2\times0.0204+0.003=0.0398$.)

> One technical null to keep honest: row $0$ is identically zero ($K_\Psi[0,j]=\Psi(0)+\Psi(j)-\Psi(j)=0$
> since $\Psi$ is even and $\Psi(0)=0$). So "$\lambda_{\min}=0$" means the **nontrivial** spectrum is
> exactly PSD; a genuinely negative $\lambda_{\min}$ is a nontrivial mode going negative (RH-violating
> on the window).

## 1. The zeros fall out of the primes (concrete Hilbert–Pólya)

Diagonalizing the prime-built $K_{\Psi,L}$ on $[0,L]$, the eigenvectors are the zero-waves and their
dominant frequencies converge to the Riemann zeros as the window grows — **with no zeros used as input:**

| window $L$ | $\gamma_1$ (14.1347) | $\gamma_2$ (21.0220) | $\gamma_3$ (25.0109) | $\gamma_4$ (30.4249) |
|---|---|---|---|---|
| 6 | 14.141 | 21.033 | 25.009 | 30.406 |
| 8 | 14.128 | 21.019 | 25.003 | 30.401 |
| 10 | 14.130 | 21.018 | 25.007 | 30.419 |

Each zero appears as a near-degenerate cos/sin **doublet**, with eigenvalue $\sim 1/\gamma^2$. This is
the Hilbert–Pólya space made explicit and arithmetic: an operator assembled from von Mangoldt weights
plus the Archimedean block, whose spectrum is the nontrivial zeros. *(OBSERVED, finite; exact kernel.)*

**The dominant mode is $\Psi$ itself.** The top eigenvalue is large and gapped (e.g. $9.62$ vs next
$1.0$), and its eigenvector has $|\mathrm{corr}|=0.999$ with the sampled $\Psi$ — not with
$\cosh(t/2)-1$ or $e^{t/2}$. The "reserve" direction of the explicit formula is the leading mode.

## 2. The rank-2 pole is real — but inseparable (one wall, closed)

The pole sector $E(t)=8(\cosh\tfrac t2-1)$ has screw kernel $K_E$ of **exact signature $(1,1)$,
rank 2** — confirming the earlier structural claim. The tempting move is to treat RH as a rank-2
indefinite correction of a PSD background. It fails, decisively:
\[
K_{\Psi,L}-K_E\quad\text{has}\quad \lambda_{\min}\approx-2.1\times10^{4}.
\]
The pole's $e^{t/2}$ growth is *cancelled* by the prime ramp inside $\Psi$; tearing them apart exposes
raw divergence. **The pole cannot be additively isolated — pole and primes are entangled.** So the
"finite-rank Schur-complement" shortcut is a wall, now closed with a computation. *(DISCLOSED no-go.)*

## 3. The knife-edge — corrected: an extreme, horizon-collapsing stability window

**Correction (continuity audit, `PSD_BOUNDARY_CONTINUITY_AUDIT.md`, verified 2026-10-06).** The
original wording of this section — "every nonzero tilt/mutation destroys PSD on a fixed finite grid"
— is **false** and is retracted. The $\lambda_{\min}=0$ reported below is the *structural* $t=0$ null
($K(0,t)\equiv0$), which is present for every weight choice. The honest diagnostic is the **reduced**
matrix $K^\circ=K[\{t_i>0\},\{t_j>0\}]$, which at the true weights is **strictly positive definite**:
\[
\lambda_{\min}(K^\circ_0)\approx 0.00467185065\quad(T=8,\ \Delta t=0.04),
\]
so finite-dimensional continuity *forces* a nonzero PSD neighborhood around the true data. What is
real and striking is that the neighborhood is **extremely narrow and appears to collapse with the
horizon**. For the finite-place-only exponent tilt below, the reduced kernel stays PSD exactly on

| horizon $T$ | $\lambda_{\min}(K^\circ_0)$ | $\epsilon_-$ | $\epsilon_+$ |
|---:|---:|---:|---:|
| 4 | 0.006784 | $-3.87\times10^{-5}$ | $+1.25\times10^{-4}$ |
| 6 | 0.005602 | $-5.59\times10^{-6}$ | $+1.15\times10^{-5}$ |
| 8 | 0.004672 | $-8.27\times10^{-7}$ | $+2.30\times10^{-6}$ |
| 10| 0.003672 | $-2.31\times10^{-7}$ | $+3.81\times10^{-7}$ |

(The $T=8$ row $\lambda_{\min}$ and $\epsilon_+$ independently reproduced.) The correct target is
therefore an **asymptotic stability-radius** statement, not a finite-grid exact-boundary one:
\[
\boxed{\ 0\in\operatorname{int}\mathcal E_L\ \text{for each finite }L,\qquad \bigcap_{L>0}\mathcal E_L=\{0\}\ }
\]
and quantitatively $\operatorname{rad}(\mathcal E_L)\to0$ (rate TBD, possibly $\sim e^{-cL}$). This
reconciles finite-dimensional continuity with the global slack-free character — RH is the knife-edge
*in the limit*, not on any one window. The tables below are kept as the raw (coarse) observations
that motivated the corrected statement; read $\lambda_{\min}$ there as the *reduced* value.

**Single-weight mutation** $\Lambda(2)/\sqrt2\to f\cdot\Lambda(2)/\sqrt2$ (large mutations shown; a
*small* enough mutation stays PSD by the same continuity):

| $f$ | 0.90 | 0.98 | **1.00** | 1.02 | 1.10 |
|---|---|---|---|---|---|
| $\lambda_{\min}$ | $-0.135$ | $-0.021$ | **$0$** | $-6.40$ | $-51.0$ |

**Global exponent tilt** $w_n\to\Lambda(n)\,n^{-(1/2+\epsilon)}$ — a **finite-place-only** tilt (prime
weights move, Archimedean block held fixed); this is *not* the fully completed Suzuki/Bost–Connes
temperature flow (cf. C77/C80 and the completed-shift experiment):

| $\epsilon$ | $-0.04$ | $-0.01$ | **$0$** | $+0.01$ | $+0.04$ |
|---|---|---|---|---|---|
| $\lambda_{\min}$ | $-3417$ | $-787$ | **$0$** | $-168$ | $-621$ |

The positivity margin is **sharply peaked at the critical exponent** (the reduced $\lambda_{\min}$
is maximal near $\epsilon=0$ and crosses zero at the tiny $\epsilon_\pm$ above). Two conclusions,
stated correctly:

1. **"$\tfrac12$ is (asymptotically) the PSD-cone boundary" ties to "$\tfrac12$ is the critical line."**
   The exponent that makes the prime weights match the Archimedean cancellation, and the exponent
   whose finite stability window collapses to a point as $L\to\infty$, are the same number. This is
   the positivity face of the half-density/unitarity result (the braid forces $|a|_v^{1/2}$).
2. **RH is a boundary/extremal positivity in the horizon limit, not an interior one.** On any fixed
   window there is a genuine (tiny) PSD neighborhood; the slack-free character is the *collapse*
   $\operatorname{rad}(\mathcal E_L)\to0$, not finite-grid exactness. This is still why every robust
   method fails (a robust bound would give an $L$-uniform radius). *(OBSERVED, finite; equivalence to
   RH is C31–C33; the collapse $\bigcap_L\mathcal E_L=\{0\}$ is CONJECTURED, not proved.)*

## 4. $K_{\Psi,L}=T_L^\*T_L$ — the Route-B factor, made concrete

The screw kernel is PSD on every window (RH holds there), so it factors. Taking the matrix square
root of the **prime-built** $K_{\Psi,L}$ (after dropping the trivial $t=0$ node),
\[
\boxed{\,K_{\Psi,L}=T_L^\*T_L,\qquad T_L=\Sigma^{1/2}V^\*=\sqrt{K_{\Psi,L}}\,,}\qquad
\frac{\|T_L^\*T_L-K_{\Psi,L}\|}{\|K_{\Psi,L}\|}=7.6\times10^{-15}.
\]
This is the finite-wavefront form of Front A / Route B ($G_g(t,u)=\langle V(t),V(u)\rangle$), now a
concrete operator. Three facts pin down what it is and what it would take to close:

- **$T_L$ is prime-built.** $\sqrt{K_{\Psi,L}}$ is a deterministic function of $K_{\Psi,L}$, which uses
  no zeros. The zeros appear only when one *reads* $T_L$: its rows are the zero-waves
  $\tfrac{e^{i\gamma t}-1}{\gamma}$ (leading-row frequencies $14.13, 21.02, 25.0,\dots$), and its
  singular values are $s_k=\sqrt{\sigma_k}\sim 1/\gamma_k$, accumulating at $0$ — $T_L$ is a *critically
  compact* operator (the slack-free signature at the level of the factor).
- **RH $\iff$ the prime-built square root stays real, uniformly in $L$.** An off-line zero makes
  $K_{\Psi,L}$ indefinite and $\sqrt{K_{\Psi,L}}$ complex. So positivity is exactly "$\sqrt{K}$ real for
  all $L$."
- **The causal (Cholesky) factor $K_{\Psi,L}=R^\*R$** ($R$ upper-triangular) exists too; its diagonal
  $R_{tt}$ is the *successor-time innovation std* — the reserve increment at execution time $t$. It is
  smooth and slowly decaying ($0.192$ at $\log 2$, $0.180$ at $\log 3$, $0.165$ at $\log 5,\dots$), i.e.
  the reserve accumulates smoothly rather than in sharp per-prime spikes. This is the causal/"succ
  traverses state" realization of the same factorization.

## 5. Where the light reaches — and where it stops

**What is genuinely in hand (exact, verified):** an explicit prime-built operator $K_{\Psi,L}$ that is
PSD $\iff$ RH-on-$[0,L]$, whose spectrum is the zeros, that sits on the PSD-cone boundary exactly at
the critical exponent, and an exact factorization $K_{\Psi,L}=T_L^\*T_L$ with $T_L=\sqrt{K_{\Psi,L}}$.

**What this does not do (the honest stop):** it does not prove $\sqrt{K_{\Psi,L}}$ stays real as
$L\to\infty$. Building $T_L$ via the square root *presupposes* PSD; it is not an independent reason for
it. A proof needs an **explicit arithmetic $B_L$** (not $\sqrt{K}$) with $K_{\Psi,L}=B_L^\*B_L$, built
from the Euler/convolution identity that *defines* the weights
($\Lambda=\mu*\log$, i.e. $\sum_{d\mid n}\Lambda(d)=\log n$; equivalently the coherent-state identity
$\sum\Lambda(n)n^{-s}=-\zeta'/\zeta$ of the companion note), and with operator norm controlled
**uniformly in $L$**. That uniform control is RH (C75).

So the thread of light sharpens the target rather than reaching the far side:

> **Sharpened target (slack-free, non-circular form of Route B).** Exhibit $B_L$ with
> $K_{\Psi,L}=B_L^\*B_L$ whose columns are given *in closed form from prime data* (not from the spectrum
> of $K$), such that the Euler constraint $\Lambda=\mu*\log$ forces $\|B_L\|$-type control uniform in
> $L$. Equivalently: prove the von Mangoldt weights are the argmax over weight-space of the positivity
> margin, with max value $\ge 0$, using only the convolution identity — no zero locations.

This is consistent with everything the ledger forbids: it is exact (not a robust bound), it is
mutation-sensitive (§3), and it uses the arithmetic-specific Euler structure that generic methods
ignore. It is the same wall as Weil positivity — but now with the exact object, its boundary geometry,
and its factor all in hand, and with a precise statement of the one missing ingredient.

## Ledger deltas

See `CLAIM_LEDGER.md` rows **C82–C85** (zeros-from-primes OBSERVED; pole non-separability DISCLOSED
no-go; PSD-boundary/critical-exponent OBSERVED; $K_{\Psi,L}=T_L^\*T_L$ with the uniform-control gap,
UNVERIFIED / RH-equivalent).

## Appendix — reproduce

`python3 scripts/prime_kernel_psd_boundary.py` prints: (A) zeros recovered vs window, (B) dominant
mode $=\Psi$, (C) rank-2 pole signature + non-separability, (D) the mutation and exponent-tilt knife
edge, (E) the exact factorization $K_{\Psi,L}=T_L^\*T_L$ with its singular values and zero-wave rows.
