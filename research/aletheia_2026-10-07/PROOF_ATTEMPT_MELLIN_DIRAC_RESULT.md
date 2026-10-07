# Mellin-Dirac RH proof attempt — result

**Date:** 2026-10-07  
**Branch:** \`proof/mellin-dirac-completion-2026-10-07\`  
**Outcome:** no RH proof. Two natural proof routes were refuted. A new exact source-balance / quantile-geodesic formulation survived and sharply identifies the remaining theorem.

## What was proved

### Completed source identity

For \(t>0\),

\[
\boxed{
\Psi''
=
(e^{t/2}+e^{-t/2})dt
-
\operatorname{Tr}(e^{-tD_{1/2}})dt
-
\sum_q\frac{\Lambda(q)}{\sqrt q}\delta_{\log q},
}
\]

with

\[
D_{1/2}
=
\operatorname{diag}
\left(
\frac12,\frac52,\frac92,\ldots
\right).
\]

Thus Suzuki curvature is exactly pole/vacuum supply minus Gamma heat source minus prime Dirac source.

### Weighted-PNT identity

In \(x=e^t\) coordinates,

\[
dM_{\rm prime}
=
x^{-1/2}d\psi(x),
\qquad
dM_{\rm vac}
=
x^{-1/2}dx.
\]

Therefore the leading source discrepancy is

\[
x^{-1/2}d(\psi(x)-x).
\]

### Quantile-geodesic reserve identity

Let

\[
S_j=\sum_{i\le j}\frac{\Lambda(q_i)}{\sqrt{q_i}},
\]

and define

\[
Q_{\rm ar}(v)=\log q_j
\quad
(S_{j-1}<v\le S_j).
\]

Let

\[
\tau(v)=(A^*)'(v)
\]

be the smooth Archimedean convex-gradient quantile.

Then

\[
\boxed{
M_j
=
A(\log2)
+
\int_0^{S_j}
\bigl(Q_{\rm ar}(v)-\tau(v)\bigr)dv.
}
\]

Since the initial interval is already certified,

\[
\boxed{
RH
\iff
M_j\ge0
\quad\forall j.
}
\]

Therefore RH is exactly the assertion that the accumulated signed transport area between the discrete prime-power actualization path and the smooth Archimedean curvature path never exhausts the initial reserve.

## What was refuted

### Local curvature-payment induction

The inequality

\[
A'(\log q_{j+1})-A'(\log q_j)
\ge
\frac{\Lambda(q_{j+1})}{\sqrt{q_{j+1}}}
\]

fails for actual prime powers. Hence the next domino is not necessarily paid by curvature accumulated only since the previous domino.

The process is globally reserve-coupled.

### Naive finite-positive limit

Finite prime/Gamma characteristic functions are positive definite, but their critical prime exponent diverges with the prime cutoff. They do not converge directly to the finite Suzuki screw exponent.

Thus:

\[
\boxed{
\text{finite positivity is too cheap; critical completion is the theorem}.
}
\]

## The single remaining proof seam

The signed scalar completion must arise as the boundary shadow of a larger positive/self-adjoint system.

A proof-bearing finite construction would need a canonical positive block system whose boundary Schur complement is the exact finite Suzuki/Weil kernel, with all cross couplings derived from prime/Gamma/carry data and no zero input.

Then one must prove a positivity-preserving completed limit.

Generic Schur-complement existence is equivalent to the target positivity and therefore circular.

The new Mellin-Dirac work helps only by making the Archimedean block explicit and canonical.

## Claim status

**DISCLOSED:** source identity, weighted-PNT source relation, quantile-geodesic reserve identity, two no-gos.

**UNVERIFIED:** canonical positive dilation with exact Suzuki boundary response.

**REFUTED:** local one-domino payment; naive finite-positive critical limit.

**RH:** open.
