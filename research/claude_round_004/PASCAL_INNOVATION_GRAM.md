# Pascal innovation Gram: the uniform-time Pascal re-encodes the zeros (partial no-go)

**Date:** 2026-10-06
**Status:** OBSERVED-FINITE + exact mechanism. Kills the *literal uniform-time* Pascal factor ansatz
as a non-circular construction; preserves the FUCC=Pascal identities. RH remains open.
**Reproduce:** `scripts/pascal_innovation_gram.py`.

## Setup

FUCC_IS_PASCAL §5 gives the tautology $K_{\Psi,L}=\Pi\,G_L\,\Pi^T$ on a uniform successor-time grid
$t_j=jh$, with $\Pi_{nk}=\binom nk$ and the **innovation Gram** $G_L=\Pi^{-1}K_{\Psi,L}\Pi^{-T}$. Since
congruence preserves inertia, $G_L\succeq0\iff K_{\Psi,L}\succeq0$, and the proposed arithmetic factor
is $B_L=C_L\Pi_L^T$ with $G_L=C_L^\*C_L$. So *all* RH-bearing content is in $G_L$. We computed it.

## Stable evaluation (no Pascal inversion)

For $k,\ell\ge1$ the pure $\Psi(s)$ and $\Psi(u)$ terms of $K(s,u)=\Psi(s)+\Psi(u)-\Psi(s-u)$ are
annihilated by the mixed difference (because $\sum_j(-1)^{\ell-j}\binom\ell j=(1-1)^\ell=0$), leaving
the exact finite-difference formula
\[
\boxed{\,G_{k\ell}=-\sum_{i=0}^{k}\sum_{j=0}^{\ell}(-1)^{k-i}\binom ki(-1)^{\ell-j}\binom\ell j\,\Psi(|i-j|h)\,}
\]
(and $G_{0\ell}=G_{k0}=0$ from $K(0,t)=0$). Computed at `mpmath` dps=80, $N=16$, $h=0.1$.

## Result: $G_L$ is PSD, dense, exponentially growing — and it is the zero-moment matrix

- **Inertia check.** $G_L\succeq0$ (no negative eigenvalues), as required.
- **Not sparse, not banded.** Entries grow to $\sim10^7$ at the $N{=}16$ corner; the matrix is full.
  Antidiagonals are symmetric and middle-peaked $\approx\binom{k+\ell}{k}$.
- **Exact mechanism.** FUCC_IS_PASCAL §6: the zero-wave feature $\phi_\gamma(n)=\frac{e^{i\gamma nh}-1}{\gamma}$
  has innovation vector $z_\gamma^k/\gamma$ with $z_\gamma=e^{i\gamma h}-1$. Hence
  \[
  \boxed{\,G_{k\ell}=\sum_{\gamma}\frac{\overline{z_\gamma}^{\,k}z_\gamma^{\,\ell}}{\gamma^2}
  =\sum_{\gamma>0}\frac{2\,\mathrm{Re}(\overline{z_\gamma}^{\,k}z_\gamma^{\,\ell})}{\gamma^2}\,,\qquad z_\gamma=e^{i\gamma h}-1.\,}
  \]
  Verified against the (prime-built) $G_L$: the ratio computed/predicted is a **constant** $1.063$–$1.066$
  across all entries over 8 decades of magnitude — exactly the $\gamma>\gamma_{300}$ tail
  ($G_{11}$'s tail $\approx\sum_{\gamma>541}4/\gamma^2\approx6\%$), not a structural deviation. With all
  zeros the identity is exact.

So $G_L$ is the **complex moment matrix** of the measure $\mu=\sum_\gamma\gamma^{-2}\delta_{z_\gamma}$
supported on the circle $|z+1|=1$. The exponential growth is $|z_\gamma|^{k+\ell}$ with
$|z_\gamma|=2|\sin(\gamma h/2)|$, maximal ($=2$) near $\gamma=\pi/h$.

## Verdict (partial no-go, with a preserved positive)

> **The literal uniform-time Pascal factorization is RH-inert as a construction.** Passing to the
> innovation basis exactly re-expresses the Riemann zeros as moments of $z_\gamma$ on $|z+1|=1$; it
> does not expose any prime/arithmetic structure, and recovering $\mu$ (equivalently $C_L$) from
> arithmetic is the explicit formula again — circular.

What survives: FUCC_IS_PASCAL §6 is confirmed exactly (zero-waves *are* Pascal expansions), and the
*additive* Pascal $\Pi$ is correctly identified as the **universal causal propagation** (RH-inert).
The arithmetic must therefore enter through a *different* operator composed with $\Pi$ — the
**multiplicative** binomial/divisor-multiset incidence (FUCC_IS_PASCAL §7–8) and the Möbius/affine
structure — not the additive time-Pascal. That is the pivot for the rest of Round 004.

*(Status: OBSERVED-FINITE for the numerics; the moment-matrix identity is DISCLOSED given
FUCC_IS_PASCAL §6 + the Suzuki zero-side identity C31; the no-go is a construction-level statement,
not an RH statement.)*
