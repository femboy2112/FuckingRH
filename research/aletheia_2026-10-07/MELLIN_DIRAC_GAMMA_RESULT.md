# Mellin-Dirac Gamma round result

**Date:** 2026-10-07  
**Branch:** \`aletheia/mellin-dirac-gamma-2026-10-07\`  
**Verdict:** strong structural advance; no RH proof. The local/global Gamma intuition is exact and yields canonical finite Archimedean models. The proof wall moves to the completed infinite prime/Gamma limit.

## Strongest exact results

### 1. Local Mellin atom

With multiplicative Haar measure,

\[
\mathcal M[\delta_a^\times](s)=a^s.
\]

A Dirac atom is one localized multiplicative scale.

### 2. Gamma is global scale superposition

\[
\Gamma(s)=\int_0^\infty e^{-a}a^s\,d^\times a.
\]

So Gamma is the continuous Archimedean superposition of local Mellin atoms.

### 3. Critical Gamma carrier is a characteristic function

\[
\Phi_\infty(t)
=
\pi^{-it/2}
\frac{\Gamma(1/4+it/2)}{\Gamma(1/4)}
=
\mathbb E[e^{itY}],
\]

where

\[
Y=\frac{\log X-\log\pi}{2},
\qquad
X\sim\Gamma(1/4,1).
\]

### 4. Exact phase quotient

\[
\chi(\tfrac12+it)
=
\frac{\overline{\Phi_\infty(t)}}{\Phi_\infty(t)}.
\]

The repository's critical Archimedean scattering phase is exactly the phase quotient of the log-Gamma characteristic function.

### 5. Log-Gamma Lévy measure

\[
\log\Phi_\infty(t)
=
itb+
\int_0^\infty
(e^{-itr}-1+itr)
\frac{e^{-r/2}}{r(1-e^{-2r})}\,dr.
\]

### 6. Exact inverse-SUCC mode decomposition

\[
\frac{e^{-r/2}}{r(1-e^{-2r})}
=
\frac1r
\sum_{m\ge0}e^{-(2m+1/2)r}.
\]

So the log-Gamma Lévy rates are exactly

\[
2m+\frac12.
\]

### 7. Exact random series

\[
Y
\overset d=
b+\sum_{m\ge0}
\left(
\frac1{2m+1/2}
-
E_m
\right),
\]

with independent

\[
E_m\sim\operatorname{Exp}(2m+1/2).
\]

### 8. Exact det2 realization

\[
\pi^{-w/2}
\frac{\Gamma((1/2+w)/2)}{\Gamma(1/4)}
=
e^{bw}
\det_2(I+wD^{-1})^{-1},
\]

\[
D=\operatorname{diag}(1/2,5/2,9/2,\ldots).
\]

### 9. Finite mode truncation preserves trivial zeros

The reciprocal \(M\)-mode product has exact zeros at

\[
s=0,-2,-4,\ldots,-2(M-1).
\]

Thus spectral-product truncation is the canonical finite inverse-Gamma model if zero structure matters.

### 10. Cumulants are spectral traces

For \(n\ge2\),

\[
\kappa_n
=
(-1)^n(n-1)!
\operatorname{Tr}(D^{-n}).
\]

The whole higher derivative chain of Gamma is a spectral trace hierarchy.

### 11. Canonical finite Dirac comb

Generalized Gauss-Laguerre with \(\alpha=-3/4\) gives positive nodes and weights reproducing

\[
\Gamma(k+1/4)
\]

for

\[
k=0,\ldots,2N-1.
\]

### 12. Jacobi operator realization

The same Gauss-Laguerre atoms are the spectral measure of the positive self-adjoint tridiagonal Jacobi matrix

\[
(J_N)_{nn}=2n+\frac14,
\]

\[
(J_N)_{n,n+1}
=
\sqrt{(n+1)(n+\tfrac14)}.
\]

It satisfies

\[
\langle e_0,J_N^k e_0\rangle
=
(1/4)_k
\]

through degree \(2N-1\).

### 13. Sum/product duality

In the infinite model,

\[
\frac{\Gamma(a+z)}{\Gamma(a)}
=
\langle e_0,J_a^z e_0\rangle
=
e^{z\psi(a)}
\det_2(I+zD_a^{-1})^{-1}.
\]

Gamma therefore has independent moment/spectral-measure and cumulant/determinant operator realizations.

### 14. Common prime-Gamma source kernel

Prime:

\[
-\partial_\sigma
\log\frac{\zeta(\sigma+it)}{\zeta(\sigma)}
=
\int(e^{-itr}-1)\,dM_{\mathrm{prime},\sigma}(r),
\]

\[
dM_{\mathrm{prime},\sigma}
=
\sum_{p,k}
(\log p)p^{-k\sigma}
\delta_{k\log p}.
\]

Gamma:

\[
-\partial_\sigma\log G_\sigma(t)
=
\int(e^{-itr}-1)\,dM_{\infty,\sigma}(r),
\]

\[
dM_{\infty,\sigma}
=
\frac{e^{-\sigma r}}{1-e^{-2r}}\,dr.
\]

At \(\sigma=1/2\), these are exactly the repository's critical prime source and shifted Gamma ladder.

### 15. Gamma source is a heat trace

\[
\frac{e^{-\sigma r}}{1-e^{-2r}}
=
\operatorname{Tr}e^{-rD_\sigma},
\]

\[
D_\sigma
=
\operatorname{diag}
(\sigma,\sigma+2,\sigma+4,\ldots).
\]

### 16. Bernoulli UV expansion

\[
\operatorname{Tr}e^{-rD_\sigma}
=
\frac1{2r}
\sum_{n\ge0}
B_n(1-\sigma/2)
\frac{(2r)^n}{n!}.
\]

This is the same Bernoulli generating mechanism appearing independently in the actualization-jet program.

## Finite positivity theorem

For finite \(P,M\) and every \(\sigma>0\),

\[
C_{P,M,\sigma}(t)
=
e^{itb_\sigma}
\prod_{m<M}
\frac{e^{it/(\sigma+2m)}}{1+it/(\sigma+2m)}
\prod_{p\le P}
\frac{1-p^{-\sigma}}{1-p^{-\sigma-it}}
\]

is an honest characteristic function.

Thus all finite hybrid systems are positive definite.

This is RH-inert by itself.

## Critical obstruction

At \(\sigma=1/2\), as \(P\to\infty\),

\[
\sum_{p\le P}
\frac{\log p}{\sqrt p-1}
\sim2\sqrt P
\]

and

\[
\sum_{p\le P}
(\log p)^2
\frac{p^{-1/2}}{(1-p^{-1/2})^2}
\sim2\sqrt P\log P.
\]

The Gamma cumulants stay finite.

Therefore the positive Gamma probability sector does not cancel the prime bulk. The signed Archimedean/pole completion remains load-bearing.

## Verdict-changing next probe

Construct a finite completed operator in **both** Gamma bases:

1. Jacobi/Dirac spectral measure;
2. diagonal det2 Gamma ladder.

Couple each independently to the same finite conductor/carry arithmetic system.

Then ask whether they produce the same completed **scalar/boundary transfer observable** under an explicitly declared comparison map. Do not require a unitary intertwiner between the Gamma Jacobi operator and the diagonal mode ladder: their infinite spectral types differ (continuous versus pure point), so direct operator equivalence is not the target.

Pass criteria:

- exact or controlled agreement of the two induced boundary/transfer observables after coupling;
- mutation sensitivity to real prime data;
- correct signed pole/boundary sector;
- stable two-parameter \((X,M)\) limit independent of cofinal path;
- convergence to the Suzuki/Weil object in a positivity-preserving topology.

That is the shortest current route to turn the Mellin-Dirac insight into proof-bearing RH machinery.
