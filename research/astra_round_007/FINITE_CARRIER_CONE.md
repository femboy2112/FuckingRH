# Canonical finite carrier cone and its incidence-square compression

Date: 2026-10-06. Exact finite formulas and scoped no-go; no RH conclusion. Companion: `FACTOR_CONE_AND_SQRT_WINDOW.md`.

## 1. One finite volume, not independently completed towers

At integer horizon \(N\ge1\), take
\[
\mathscr F_{\le N}=\{(a,b)\in\mathbb N_{>0}^2:ab\le N\},\qquad
\mathscr H_{F,N}=\ell^2(\mathscr F_{\le N}).
\]
This is exactly the valuation splitting condition \(\alpha+\beta=\nu(n)\) with \(n\le N\). Its product fibers are complete, its swap is an involution, and its embeddings as \(N\) increases are canonical. Both \(J_F\) and \(M^*\) restrict to these fibers without discarding half a prime tower.

If \(r=\lfloor\sqrt N\rfloor\), then
\[
\dim\mathscr H_{F,N}=\sum_{n\le N}d(n)
=2\sum_{a\le r}\left\lfloor\frac Na\right\rfloor-r^2.
\]
Proof: every pair with \(ab\le N\) has \(a\le r\) or \(b\le r\); pairs satisfying both inequalities form the full \(r\times r\) square and were counted twice. This is Dirichlet's hyperbola method, not a new asymptotic principle.

More generally, for arbitrary complex sequences and their finite sums \(F(x)=\sum_{a\le x}f(a)\), \(G(x)=\sum_{b\le x}g(b)\),
\[
\sum_{ab\le N}f(a)g(b)
=\sum_{a\le r}f(a)G(N/a)
+\sum_{b\le r}g(b)F(N/b)-F(r)G(r).
\]
This identity is exact even with signed or complex weights. It is independent of prime-distribution estimates. The familiar Dirichlet-series product \(\sum(f*g)(n)n^{-s}=(\sum f(a)a^{-s})(\sum g(b)b^{-s})\) follows by absolute rearrangement wherever both absolute series converge; neither it nor a Mellin/Perron representation supplies a positivity-preserving completion across that region.

The ambient square-window space \(\{(n,a):n\le N,a\le\sqrt N\}\) is different: it contains nondivisibility states. One cannot replace it by the actual factor cone while keeping the same carrier-only successor. For \(a>1\), \((n,a)\) with \(a\mid n\) shifts outside divisor incidence at \(n+1\). This is the mechanism proved in the companion note.

## 2. A genuinely geometric first-order candidate

Put a nearest-coordinate graph on \(\mathscr F_{\le N}\): include the oriented edges
\[
(a,b)\longrightarrow(a+1,b),\qquad
(a,b)\longrightarrow(a,b+1)
\]
whenever both endpoints remain in the cone. Orientation merely fixes the incidence convention. Let
\[
(E_Nx)(v\to w)=x(w)-x(v).
\]
This is a first-order graph incidence map with forced unit coefficients. On vertex plus edge space the operator
\[
\mathcal D_N=\begin{pmatrix}0&E_N^*\\E_N&0\end{pmatrix}
\]
is self-adjoint and odd for the vertex/edge grading. Its square is the vertex graph Laplacian plus the edge counterpart. Swap acts on vertices and the corresponding exchanged edges, so the construction is swap-equivariant.

This is a derived graph Dirac, rather than a block name attached to a desired matrix. Its finite eigenvalues are real because the displayed operator is self-adjoint. That elementary fact is not a statement about zeta zeros.

Let \(U_N=M_N^*\) be the unnormalized constant-fiber lift. Define
\[
K_N=U_N^*E_N^*E_NU_N\succeq0.
\]
For distinct carrier indices \(1\le n<m\le N\), writing \(h=m-n\), there is a precise compression formula:
\[
\boxed{(K_N)_{n,m}=-2\,1_{h\mid n}.}
\]
Indeed, a horizontal graph edge from product \(n=ab\) to product \(m=(a+1)b\) must have \(b=h\), and exists exactly when \(h\mid n\). There is one such edge and one transposed vertical edge. Each contributes \(-1\) to the Laplacian cross entry. The diagonal is
\[
(K_N)_{n,n}=\sum_{ab=n}\deg_N(a,b),
\]
where
\[
\deg_N(a,b)=1_{a>1}+1_{b>1}+1_{(a+1)b\le N}+1_{a(b+1)\le N}.
\]
Thus \(K_N\) is a weighted carrier graph Laplacian with an edge of weight two when one integer is the product of the other edge's difference and a positive integer. Its row sums vanish because \(U_N\mathbf1\) is constant on all vertices. These identities give its structure, not just a matrix norm.

For the isometric lift \(J_{F,N}=U_Nd(X)^{-1/2}\), the corresponding compression is
\[
\widehat K_N=d(X)^{-1/2}K_Nd(X)^{-1/2};\qquad
(\widehat K_N)_{n,m}=\frac{-2\,1_{m-n\mid n}}{\sqrt{d(n)d(m)}}.
\]
The kernel vector becomes \(\sqrt{d(n)}\), as it must under this change of normalization.

## 3. Unit removal isolates the obstruction

Repeat the construction on \(\mathscr F_{\le N}^{\circ}=\{(a,b):a,b\ge2,ab\le N\}\), retaining only edges with both endpoints in this interior. Its unnormalized compressed energy satisfies
\[
(K_N^{\circ})_{n,m}
=-2\,1_{h\mid n}\,1_{h\ge2}\,1_{n/h\ge2},\quad n<m.
\]
Therefore
\[
\boxed{(K_N^{\circ})_{n,n+1}=0,\qquad
K_N^{\circ}e_p=0\text{ for every prime }p\le N.}
\]
Every nearest-carrier cross term in the full graph comes from the two unit axes. Removing the units, as the positive primality-defect square does, removes those cross terms and annihilates every prime input. This is exact for every horizon and cannot be repaired by taking \(N\to\infty\) within this same candidate.

The diagonal weights, the two coordinate edge families, and the cone boundary are all retained before squaring in this calculation. The failure is not caused by dropping an edge orientation or doing floating-point arithmetic. A nonzero exact Suzuki pushforward needs a different coupling and an independently specified time/test transform; this candidate itself does not supply it.

## 4. Boundary versus bulk under the carrier limit

For fixed \(n,m\), the off-diagonal compression above stabilizes once \(N\ge\max(n,m)\). The interior divisor cross entries are not confined to \(ab=N\) and do not tend to zero. At fixed \(n\), the diagonal eventually stabilizes to
\[
\sum_{ab=n}(2+1_{a>1}+1_{b>1}).
\]
Thus an exact target comparison must retain this stable divisor-dependent bulk. One cannot call it an upper-horizon error.

There is a separate finite-truncation issue with a carrier shift \(S_Ne_N=0\):
\[
(I-S_N)^*(I-S_N)=2I-S_N-S_N^*-|N\rangle\langle N|.
\]
If the intended finite energy includes the outgoing edge, instead use the difference map from \(\{1,\ldots,N\}\) into \(\{1,\ldots,N+1\}\), sending \(e_n\) to \(e_{n+1}-e_n\). Its square is \(2I-S_N-S_N^*\). Neither choice removes the exact interior obstruction.

## 5. Hostile checks and the next hypothesis to break

The exact tests verify fiber normalization, swap, oriented energy before/after projection, all divisor-current terms, arbitrary rational cone mutations, coordinate incidence compression, removal of units, longer carrier hops, weighted hyperbola identities, and a continuum of geometry-preserving amplitude exponents. Raw finite examples are in `evidence/factor_cone.json`.

Changing the cone from \(1/2\) to \(1/3\) or \(2/3\) changes its threshold fires, as required, but does not remove the arithmetic fact \(\gcd(n,n+1)=1\). Product-only reweighting preserves all cone and swap identities while changing square amplitudes; half-density is not determined. Deleting the swap partner destroys the relation \(MR=M\), yet a graph square remains positive: generic positivity alone cannot certify that the right arithmetic has survived.

The next operator must break **same-factor local propagation** in a controlled way and retain its new cross terms through the Weil/test-function pushforward. Mixing labels arbitrarily is insufficient: \(J_FSJ_F^*\) only reconstructs a previously specified carrier shift. The theorem to prove is an exact completed energy identity, including the infinite-place contribution, for an arithmetically forced label-mixing operator. That theorem is unpaid; this dossier does not assert it is impossible.

## Sources and reproducibility boundary

The classical counting/convolution source is Tao, [254A Notes 1](https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/), (35), (44), (54)–(56), Remark 41. All finite operator formulas above are derived directly. Imported Round004 C87/C88 contribute their stated isometry/factorization obstructions, not a universal claim that every commutative representation is mathematically incapable of addressing RH. No finite spectrum or PSD certificate is promoted to an infinite theorem.
