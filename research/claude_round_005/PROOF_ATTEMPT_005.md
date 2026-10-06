# Proof attempt 005 — the self-sieving profinite carry machine

**Date:** 2026-10-06. **Verdict:** RH remains open. The carry machine is an exact reframing that
**solves the local layer cleanly** and **confirms the Round-004 wall is intrinsic**; the central new
hope (shared-DC telescoping) is **refuted**.

## Thesis tested
That the missing global B is the linear-response operator of a causally self-sieving carry machine,
whose shared coarse channel telescopes the divergent sum_p M_p into a positive global object.

## What the machine gave (exact positives)
1. **Carry decomposition (C95):** $\tilde S_m=I\otimes C_m+(S-I)\otimes|0\rangle\langle m-1|$ — SUCC =
   harmonic carrier + boundary carry; Fourier → diag characters + rank-1 carry coupling; m=2 = full adder.
2. **Local $B_p$ = carry filter (C96):** $B_p=c_p(I-U_{\rm depth})(I-p^{-1/2}U_{\rm depth})^{-1}$ reproduces
   C90's $\sigma_p$ exactly; carry-depth records $=\Lambda$; half-density $p^{-1/2}$ forced by Haar cylinder.
3. **Carry = Cuntz/affine braid (C97):** $\{S,R_{m,r}\}$ satisfy $V_mS=S^mV_m$, $\sum_rR_rR_r^\*=I$ (Cuntz
   $O_m$). "Affine noncommutativity = carry curvature," nonabelian exactly at the carry step.
4. **Carré-du-champ (C99):** $\mathrm{CARRY}_m^\*\mathrm{CARRY}_m=(2I-S-S^\*)\otimes|m-1\rangle\langle m-1|$ =
   high-pass innovation energy. The von-Mangoldt event measure is the carré-du-champ of carry curvature,
   **locally**. (§22-E holds per prime.)
5. **Dyadic clock graph:** prime ancestry conjugates to binary doubling + order-clocks (period
   $\operatorname{ord}_\ell(2)$). Elegant; tangential (orders of 2, not zeta).

## What the machine killed (no-gos)
- **Shared-DC telescoping REFUTED (C98):** $\sigma_p(0)=0$ exactly per prime — there is **no duplicated
  DC/coarse channel** to merge. The divergence $\sum_pM_p\sim2\sqrt{e^L}$ is **bulk** ($\xi\ne0$); its
  renormalizer is the **indefinite imaginary-frequency pole** (C83), not a positive coarse mode, and the
  renormalization is **analytic** (continuation), not algebraic (shared-coarse subtraction). No
  multiresolution performs it.
- **Quotient filtration RH-inert (C97):** SUCC on $\mathbb Z/L_N$ is a circulant (convolution) → RH-inert
  (C94); carry survives only in the irregular branch sections. (Hostile control D confirmed.)
- **Causality RH-inert for the kernel (C99):** causal self-sieve and static prime set give identical
  $K_{\Psi,L}$; birth order does not change the kernel.

## Net
The carry machine is the **same object** as the Round-004 affine braid, now with a beautiful operational
skin: SUCC = carrier + carry, $B_p$ = carry-response filter, $\Lambda$ = carré-du-champ of carry. Every
*global/causal/filtration* escape it suggested is RH-inert or analytic-walled. The wall is exactly C91:
real-axis renormalization-positivity of the bulk prime density against the indefinite pole, uniformly in
$L$ — the Weil positivity of the Cuntz/braid carry trace. Round 005 shrank no wall; it **re-expressed the
whole program in carry language and closed its own new hopes with exact no-gos**, strengthening the case
that the wall is intrinsic.

## Where a future round could still pry
The carré-du-champ picture (C99) is the sharpest positive structure. A real target: realize the
**completed** screw kernel (incl. the indefinite pole + Archimedean) as the carré-du-champ / Dirac
$[D,a]^\*[D,a]$ of a single carry-Dirac on the Cuntz/braid groupoid, with the pole as a boundary/cokernel
term — i.e. Connes' trace formula in explicit carry coordinates. Expect it to reproduce Weil positivity.
