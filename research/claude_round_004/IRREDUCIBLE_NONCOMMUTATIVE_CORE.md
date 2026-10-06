# The irreducible non-commutative core: SUCC's irregular log-steps

**Date:** 2026-10-06
**Status:** DISCLOSED sharpening of the Round-004 meta-theorem. RH open.
Reproduce: `scripts/transfer_operator_check.py`.

## Statement

Round 004 showed, route by route, that commutative structures are RH-inert. This note closes the last
apparent escape — the "non-diagonal transfer operator" — and isolates the irreducible core.

**The directive's transfer operator is still commutative.** $A(s)=\sum_p p^{-s}T_{\log p}$ (weighted
sum of log-time translations) is a **convolution/circulant** operator: $[A,A^\*]=0$ exactly, it is
Fourier-diagonal, and its eigenvalues are the prime-zeta symbol $P(s-i\xi)=\sum_p p^{-s+i\xi}$ on a
horizontal line (verified numerically). No Riemann zeros appear without analytic continuation. So the
non-diagonal transfer operator is **RH-inert**, like the diagonal prime operator (C93), the uniform
Pascal (C86), the binomial Fock (C87), and the Hodge Laplacian (C88).

**Two commutative families, both inert.**
- *Prime-diagonal* $\mathrm{diag}(p^{-s})$ and all its $S_r$/Schur sectors → symmetric functions of
  $\{p^{-s}\}$ (C93).
- *Log-time convolution* $\sum_p p^{-s}T_{\log p}$ and anything translation-invariant → Fourier-diagonal
  (this note).

## The core

What breaks commutativity is **SUCC**: $n\mapsto n+1$ acts in multiplicative proper time by the
**irregular** step $\log(n+1)-\log n$ ($=0.693,0.405,0.288,0.223,\dots$), which is *not* a fixed
translation and *not* a convolution. This is precisely the braid
\[
\boxed{\ V_mS=S^mV_m\ }
\]
— the step size changes under dilation — i.e. the additive–multiplicative incompatibility of the
integers. Every RH-bearing object (the zeros, $K_\Psi$'s non-factorized content, the Weil form) requires
this irregularity; every object that is translation-invariant in $\log n$ **or** diagonal in the primes
discards it and becomes RH-inert.

> **Round-004 sharpened meta-theorem.** RH-inertness is broken *only* by SUCC's irregular log-stepping
> (the braid). Consequently any non-circular arithmetic $B_L$ with $K_{\Psi,L}=B_L^\*B_L$ must be built
> from the crossed-product/affine braid (succ ⋊ fucc), whose positive trace is the Weil functional —
> i.e. the Connes/Berry–Keating object. All of Round 004's routes funnel here, which is strong evidence
> that this wall is intrinsic to RH, not an artifact of any one construction.

This is the cleanest localization the program has produced of *where the entire difficulty lives*: not
in positivity of local blocks (solved, C90), not in cross-prime multiplicative coupling (RH-inert,
C81/C89), not in statistics (C93), but in the single fact that **succ and fucc do not commute**, and the
Weil-positivity of their crossed-product trace.
