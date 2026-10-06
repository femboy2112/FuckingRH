# Completed shift vs finite-place-only tilt: two different deformations

**Date:** 2026-10-06
**Status:** theory + partial diagnostic (zeros used only for after-the-fact analysis). RH open.
Answers the open question in `PSD_BOUNDARY_CONTINUITY_AUDIT.md` §5.

## Two deformations, two behaviours

**A. Finite-place-only tilt** ($\Lambda(n)n^{-1/2}\to\Lambda(n)n^{-1/2-\epsilon}$, Archimedean fixed).
Continuity audit: for each finite horizon $L$ the reduced kernel keeps a *nonzero* stability interval
$\mathcal E_L\ni0$, with $\operatorname{rad}(\mathcal E_L)\to0$ as $L\to\infty$ (shrinking window;
$\bigcap_L\mathcal E_L=\{0\}$ conjectured). This is an inconsistent (mismatched) deformation — primes
and infinity no longer share an exponent — and its positivity fails only *gradually* with horizon.

**B. Completed shift** (center Suzuki at $\mathrm{Re}=1/2+\omega$; primes **and** Archimedean move
coherently, $\xi'/\xi(1/2+\omega-iz)$). The frequencies become complex, $\gamma\to\gamma+i\omega$, so
\[
\Psi_\omega(t)=\mathrm{Re}\sum_\gamma\frac{1-\cos((\gamma+i\omega)t)}{(\gamma+i\omega)^2}
\]
carries a $\cosh(\omega t)$ envelope. For **any** $\omega\ne0$ this grows without bound and oscillates in
sign, so $\Psi_\omega\ge0$ fails at large $t$ — **no shrinking-window reprieve**; the positivity set is
$\{0\}$ outright (in the full-zero limit).

## Diagnostic (300 zeros)

$\min_t\Psi_\omega$ on $t\in[0,40]$: positive for $\omega=0$; the first negative excursion appears at
$t\approx25$ for $\omega=0.05$. Small $\omega\le0.01$ shows no negativity in $[0,40]$ **only because the
300-zero truncation cuts off the high-frequency $\cosh(\omega t)$ growth** (which needs $t\gtrsim1/\omega$);
it is a truncation artifact, not stability. The theoretical envelope argument is the operative statement.

## Takeaway

The earlier "knife-edge" intuition is **correct for the completed family** (exact $\{0\}$) and only
*approximately/asymptotically* correct for the finite-place-only tilt (shrinking window). The honest
RH-equivalent statement uses the completed family; the finite-only sweep is a coarser proxy whose
collapse rate $\operatorname{rad}(\mathcal E_L)$ is itself an interesting (unproved) quantitative target.
