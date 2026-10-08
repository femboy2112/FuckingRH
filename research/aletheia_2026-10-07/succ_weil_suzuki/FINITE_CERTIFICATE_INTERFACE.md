# What a finite computation must prove to certify a whole interval

**Claim ID:** SWS-009. **Date:** 2026-10-07.  
**Status:** an exact conditional certificate and proof, using a classical rank-one reduction. No finite data in this round satisfy or purport to satisfy the complete certificate at a general horizon.  
**Origin:** GPT-6 derivation in the user-requested succ–Weil–Suzuki research round, following the compact operator of SWS-005. No new-priority or external peer-review claim.

The role of this note is to replace “the matrix looked positive” with a mathematically sufficient finite interface. Its hypotheses specify exact spectral information or rigorous enclosures. The floating-point step-cell scan in this bundle is not such an enclosure.

## 1. Fixed target and domain

Fix \(A>0\), let \(H=L^2(-A,A)\), and use the form domain \(V_A\) and the strictly positive compact-resolvent operator \(P=P_A\) constructed in [GAMMA_ENERGY_COMPACT_SIGN_OPERATOR.md](GAMMA_ENERGY_COMPACT_SIGN_OPERATOR.md). Write

\[
d=d_A,\qquad s=s_A=\sinh(x/2),\qquad
q[v]=\|P^{1/2}v\|^2-d\|v\|^2-2|\langle v,s\rangle|^2.
\tag{1.1}
\]

Let \(p_j\) be the eigenvalues of \(P\) in increasing order, with multiplicity, and let \(e_j\) be an orthonormal eigenbasis. Put \(s_j=\langle s,e_j\rangle\). The inner product is linear in the first argument; only \(|s_j|\) enters.

## 2. Exact scalar criterion, including the equality case

**Proposition.** If \(p_1>d\), then

\[
\boxed{q\ge0\text{ on }V_A
\quad\Longleftrightarrow\quad
2\sum_{j\ge1}\frac{|s_j|^2}{p_j-d}\le1.}
\tag{2.1}
\]

If \(p_1<d\), then \(q\) has a negative direction. If \(p_1=d\), positivity requires \(s\perp\ker(P-dI)\), and (2.1) then applies to the sum over the strictly positive spectrum of \(P-dI\).

**Proof.** When \(p_1>d\), set \(T=P-dI>0\) and \(u=T^{1/2}v\). The map from the form domain to \(H\) is bijective. Therefore

\[
q[v]=\|u\|^2-2|\langle u,T^{-1/2}s\rangle|^2.
\]

Cauchy–Schwarz proves sufficiency of \(2\|T^{-1/2}s\|^2\le1\). Testing \(u=T^{-1/2}s\) proves necessity, with the zero-vector case immediate. Spectral expansion gives (2.1), whose series converges since its denominators are bounded below by \(p_1-d>0\).

If \(p_1<d\), an eigenvector for \(p_1\) has negative value in (1.1). If \(p_1=d\), every kernel vector has value \(-2|\langle v,s\rangle|^2\); hence \(s\) must be orthogonal to that kernel. Compact resolvent implies a strictly positive gap above the finite-dimensional kernel, so the preceding argument applies on its orthogonal complement. The kernel then contributes zero and no mixed term. \(\square\)

This is the standard rank-one perturbation test, explicitly proved here in the exact form domain. It does not establish its baseline spectral hypothesis for an arbitrary \(A\).

## 3. A finite sufficient certificate with an explicit tail

Let \(\Pi_N\) be the spectral projection onto the first \(N\) basis vectors. Suppose rigorously established numbers satisfy

\[
\underline p_j\le p_j\quad(1\le j\le N),
\qquad\underline p_j>d,
\]

\[
|s_j|^2\le U_j,\qquad
\|(I-\Pi_N)s\|^2\le R_N^2,
\qquad p_{N+1}\ge L_N>d.
\tag{3.1}
\]

Then the finite inequality

\[
\boxed{
2\sum_{j=1}^N\frac{U_j}{\underline p_j-d}
+\frac{2R_N^2}{L_N-d}\le1
}
\tag{3.2}
\]

certifies \(q[v]\ge0\) for every \(v\in V_A\).

Indeed the first part bounds the first \(N\) terms of (2.1), while

\[
\sum_{j>N}\frac{|s_j|^2}{p_j-d}
\le\frac{\|(I-\Pi_N)s\|^2}{p_{N+1}-d}
\le\frac{R_N^2}{L_N-d}.
\]

The available unconditional inputs include

\[
\|s\|^2=\sinh A-A,
\qquad
p_{N+1}\ge
\beta\!\left(\frac{\pi(N+1)}{2A}\right),
\quad
\beta(R)=\frac1R\int_0^R\alpha(u)\,du.
\tag{3.3}
\]

Thus \(R_N^2=\sinh A-A\) is always a valid, possibly very poor tail bound. The positive arctangent series and explicit remainder for \(\beta\) in SWS-005 give a route to a rigorous lower enclosure for the second quantity. Approximate eigenvectors by themselves do not give \(\Pi_N\), a lower eigenvalue bound, or a projection remainder bound. Degenerate eigenvalues should be handled as certified spectral subspaces; the corresponding coefficient sums are basis independent within the subspace.

If a certificate gives strict slack, it is quantitatively stable under errors smaller than that slack after every error is propagated in the unfavorable direction. If equality is approached, point estimates and printed digits are insufficient.

## 4. A block alternative when the scalar baseline is unavailable

For the positive compact operator

\[
B=P^{-1/2}(dI+2|s\rangle\langle s|)P^{-1/2},
\]

let \(\Pi\) be any orthogonal projection. Suppose certified bounds give

\[
\|\Pi B\Pi\|\le a,\qquad
\|(I-\Pi)B(I-\Pi)\|\le c,\qquad
\|\Pi B(I-\Pi)\|\le b,
\tag{4.1}
\]

where \(a,c,b\ge0\). Decomposing a unit vector into the two orthogonal blocks gives

\[
\boxed{
\|B\|\le
\frac{a+c+\sqrt{(a-c)^2+4b^2}}2.
}
\tag{4.2}
\]

To prove it, bound the quadratic form by
\(a x^2+2bxy+c y^2\), where \(x,y\ge0\) and \(x^2+y^2=1\). The maximum is the larger eigenvalue of the displayed real two-by-two matrix. Because \(B\ge0\), its norm is the supremum of its quadratic form. In particular,

\[
a\le1,\quad c\le1,\quad b^2\le(1-a)(1-c)
\tag{4.3}
\]

is sufficient for \(B\le I\). A small omitted diagonal block alone does not suffice: the mixed block consumes the available margin.

For \(\Pi=\Pi_N\), the first \(N\) spectral modes of \(P\), the mixed block comes only from the rank-one correction. With \(z=P^{-1/2}s\),

\[
\|\Pi_N B(I-\Pi_N)\|
=2\|\Pi_Nz\|\,\|(I-\Pi_N)z\|,
\]

\[
\|(I-\Pi_N)B(I-\Pi_N)\|
\le\frac{d+2\|s\|^2}{p_{N+1}}.
\tag{4.4}
\]

These are structural estimates, not a statement that the step-cell basis diagonalizes \(P\).

## 5. Why the current scan is useful, and why it stops short

The executable probe computes exact cell-overlap formulas with floating-point integration/eigensolvers. It compares the completed form with an independent explicit-formula evaluation, so it can detect sign, factor, boundary, and contact-term mistakes. It also produces candidate low-energy vectors.

It supplies none of the lower spectral enclosures or true spectral-projector errors in (3.1). A finite Ritz minimum is an upper bound on the unrestricted infimum; a finite generalized maximum is a lower bound on \(\|B\|\). Passing those observations through (3.2) as if they were certified inputs would reverse the required inequalities.

Two concrete difficulties remain even after the identities are correct. The available tail grows only logarithmically in frequency, while \(d_A\) contains a large prime mass. Also SWS-006 proves that relative positivity margins close at least as fast as a fixed-test \(O(e^{-A})\) upper bound under all-horizon positivity. Therefore an all-horizon proof needs estimates that retain the cancellation and actual prime correlations. Enlarging a matrix or reporting a ratio close to one does not supply them.

## 6. Next falsifiable task

At one specified interval beyond a rigorously settled range, construct certified spectral enclosures and an explicit tail bound that satisfy either (3.2) or (4.3), or prove that the proposed enclosure method cannot close the gap at that interval. The output must include the actual interval, bound directions, numerical error enclosures if used, and the margin remaining after the tail and mixed block.

Success would certify that interval. Extending those certificates to every interval still requires an independent all-horizon argument. This note makes that distinction an explicit mathematical condition.

## Provenance and dependencies

SWS-009 depends on the exact completed identity SWS-004 and the domain/compactness result SWS-005. Its proof uses only the spectral theorem, Cauchy–Schwarz, orthogonal projections, and elementary two-by-two matrix algebra. It introduces no RH, PNT, zero data, Hardy invariance, or unproved positivity assumption except where those appear as expressly stated hypotheses of a conditional certificate. It is an in-repository application of classical rank-one and Schur-complement reasoning, not a new external theorem.

The first derivation commit and actual execution history are tracked in [PROVENANCE_AND_CLAIMS.md](PROVENANCE_AND_CLAIMS.md). The finite probe does not execute a certified spectral enclosure and is not claimed to verify (3.1).
