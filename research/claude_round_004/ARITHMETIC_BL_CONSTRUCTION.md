# Exact local operator squares and the precise global residual

**Date:** 2026-10-06
**Status:** exact closed-form LOCAL factorization (DISCLOSED, verified `scripts/local_spectral_square.py`)
+ precise statement of the global obstruction. RH remains open. Executes FUCC_IS_PASCAL §3–4.

## 1. The repaired prime tower has an exact, manifestly positive spectral measure

For a prime $p$, $r=p^{-1/2}$, the repaired tower $D_p(t)=M_p|t|-h_p(t)$ with
$h_p(t)=\log p\sum_{k\ge1}r^k(|t|-k\log p)_+$ is CND, and its screw kernel is the Gram of
\[
\boxed{\ B_p(t)(\xi)=\frac{e^{i\xi t}-1}{\xi}\sqrt{\sigma_p(\xi)},\qquad
K_{D_p}(t,u)=\langle B_p(t),B_p(u)\rangle=\int_0^\infty\frac{(1-\cos\xi t)+\cdots}{\xi^2}\,d\sigma_p\ }
\]
with the **exact closed-form positive density** (derived from $D_p''=2M_p\delta_0-\sum_k r^k\log p\,(\delta_{k\log p}+\delta_{-k\log p})$ and inverse cosine transform):
\[
\boxed{\ \sigma_p(\xi)=\frac{2\log p}{\pi}\Big[\frac{r}{1-r}-\sum_{k\ge1}r^k\cos(k\log p\,\xi)\Big]
=\frac{2\log p}{\pi}\,\frac{r(1+r)}{1-r}\,\frac{1-\cos(\log p\,\xi)}{\,|1-re^{i\log p\,\xi}|^2\,}\ \ge 0.\ }
\]
This is **(high-pass $1-\cos(\log p\,\xi)$) $\times$ (local Euler/Poisson whitening $P_r$)** — exactly the
FUCC_IS_PASCAL §4 architecture and the LOCAL_L_FACTOR_WHITENING Poisson kernel (C06), now assembled
into a single positive density. Verified $\sigma_p\ge0$ (min $\sim5\times10^{-12}$, touching $0$ only at
$\xi=0$) and $\int\frac{1-\cos\xi t}{\xi^2}\sigma_p\,d\xi=D_p(t)$ for $p=2,3,5$.

**$M_p$ is forced.** $\max_\xi\log p\sum_k r^k\cos(k\log p\,\xi)=\log p\sum_k r^k=\frac{r\log p}{1-r}$ at
$\xi=0$, so $\sigma_p\ge0$ iff $M_p\ge\frac{r\log p}{1-r}$, and equality (the critical, tight value) gives
$M_p=\frac{r\log p}{1-r}$ with $\sigma_p(0)=0$. The repaired-tower slope is the *minimal* one keeping the
local block CND — a local knife-edge, consistent with the global one (C84).

## 2. This is a genuine non-circular local factor

$B_p$ is built from the shift ($e^{i\xi t}$), the prime log-step ($\log p$), and the half-density
weight $r=p^{-1/2}$ — **not** from $K_\Psi$, its square root, or any zero. It is the explicit local
piece of the arithmetic $B_L$ the program wants (FUCC_IS_PASCAL §9), and it is manifestly $\succeq0$.
The Archimedean block $D_\infty$ is likewise CND (ARCHIMEDEAN_REPAIRED_BLOCK), giving $\sigma_\infty\ge0$.

## 3. The precise global residual (same wall, sharpened)

By the explicit formula the completed screw measure is
\[
\boxed{\ \sigma_{\rm total}=\sum_p\sigma_p+\sigma_\infty-\sigma_{\rm pole}
=\sum_\gamma\frac{1}{\gamma^2}\big(\delta_\gamma+\delta_{-\gamma}\big),\ }
\]
and $\mathrm{RH}\iff\sigma_{\rm total}\ge0$ on the real axis. Two exact facts now sharpen the obstruction:

- **Each $\sigma_p\ge0$ and $\sigma_\infty\ge0$ (manifest).** The pole contributes
  $E_{\rm pole}(t)=8(\cosh\tfrac t2-1)=-8(1-\cos\xi t)|_{\xi=i/2}$ — a positive atom at the **imaginary**
  frequency $\xi=\pm i/2$ (mass 2), i.e. an anti-CND piece *off* the real axis.
- **$\sum_p\sigma_p(\xi)$ diverges pointwise** at every real $\xi$: for large $p$,
  $\sigma_p(\xi)\sim\frac{2\log p}{\pi}p^{-1/2}(1-\cos(\log p\,\xi))$ and
  $\sum_p\frac{\log p}{\sqrt p}=\infty$ (PNT, $\sim2\sqrt X$ to cutoff $X=e^L$).

So the obstruction is **not** a missing cross term and **not** local positivity (both the prime and
Archimedean local densities are explicitly $\ge0$). It is a *pointwise-divergent* real-axis prime
density renormalized by the imaginary-frequency pole atom, the two balancing (the explicit formula's
$4e^{L/2}$ cancellation) to the finite positive zero-measure. RH is the statement that this
renormalized real-axis measure stays $\ge0$.

> **Net:** the local Route-B factors are solved in closed form and manifestly positive; the global
> problem is a single *renormalization-positivity* statement — keep $\sum_{p\le e^L}\sigma_p$ positive
> after the pole subtraction, uniformly in $L$ — which is RH (C75/C84). This is the cleanest spectral
> localization the program has, and it is consistent with the Round-004 meta-finding: the hard content
> is the real-axis renormalization against the pole, not any multiplicative cross-coupling.
