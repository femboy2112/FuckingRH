# Shared-DC telescoping: refuted. The divergence is bulk + analytic, not DC duplication.

**Date:** 2026-10-06. **Status:** DISCLOSED no-go, verified `scripts/shared_dc_test.py`. RH open.
Tests the central Round-005 hypothesis (§10, major-crack-B): that the divergent $\sum_p M_p$ is a
duplicated coarse/DC channel that telescopes in a shared-coarse multiresolution.

## The test and the verdict

The local density is $\sigma_p(\xi)=c_p^2\,|1-z|^2/|1-rz|^2$, $z=e^{i\log p\,\xi}$, $r=p^{-1/2}$.

1. **No duplicated DC channel.** $\sigma_p(0)=0$ **exactly** for every prime (verified $5\times10^{-14}$,
   because $M_p=\frac{\log p\,r}{1-r}$ is exactly the value making the DC cancel, C90). A duplicated
   coarse/DC channel would be a *nonzero shared* DC value; there is none to merge.
2. **The divergence is bulk, not coarse.** $\sum_{p\le X}\sigma_p(\xi)$ is identically $0$ at $\xi=0$ but
   diverges for every $\xi\ne0$ (e.g. $\xi=0.5$: $14.6\to66.9\to199\to333$ as $X:10^2\to10^5$).
3. **The divergent quantity is the prime-side $e^{L/2}$.** $\sum_{p\le X}M_p\sim2\sqrt X$ (ratio $\to1.00$),
   i.e. the $e^{L/2}$ prime growth that the explicit formula cancels against the **pole**.

## Why no multiresolution fixes it

The cancellation that tames the divergence is the pole term $E_{\rm pole}$, which sits at the **imaginary**
frequency $\xi=i/2$ and whose real-axis screw kernel is **rank-2 indefinite** (C83). So:
- the coarse mode that would absorb the divergence is the pole — **indefinite**, not a positive
  coarse channel, so it cannot be the $V_0$ of a positive multiresolution;
- a finite-rank indefinite operator cannot reduce a *divergent* positive bulk density to a *finite*
  positive one — only finitely many eigenvalues change. The reduction must instead be the **analytic
  continuation** that moves the imaginary-frequency pole into the real-axis measure.

> **No-go.** The divergence is bulk ($\xi\ne0$) and its renormalization is **analytic** (continuation of
> an imaginary-frequency pole), not **algebraic** (subtraction of a shared coarse mode). No
> shared-DC / wavelet multiresolution — an algebraic Hilbert structure — can perform it. The carry
> machine's algebraic coarse/detail decomposition therefore hits exactly the Round-004 analytic wall:
> the real-axis renormalization-positivity against the (imaginary, indefinite) pole, uniformly in $L$ = RH.

The $\sigma_p(0)=0$ fact is itself a *positive* local result (each prime's coarse mode is already
perfectly balanced); it just means the obstruction lives entirely in the bulk/analytic sector, which is
where Round-004 already placed it (C91). Shared-DC does not shrink that wall.
