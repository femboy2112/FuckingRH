# Affine chiral pairs, their bottom boundary, and factor orientation

Status: exact bounded-operator classification on \(\ell^2(\mathbb N_{>0})\).
The binary pair is the smallest nondegenerate carry pair, not the only one.

## Complete affine classification

For integers \(m\ge1\), \(r\ge0\), define
\[
A_+=S^rV_m,\qquad A_-=(S^*)^rV_m,\qquad C_{m,r}=A_+-A_-.
\]
Thus \(A_+\delta_n=\delta_{mn+r}\), whereas
\(A_-\delta_n=\delta_{mn-r}\) for \(mn>r\), zero otherwise. Put
\(E_h=\sum_{n=1}^h|n\rangle\langle n|\), \(h=\lfloor r/m\rfloor\).
The boundary identities are
\[
A_+^*A_+=I,\qquad A_-^*A_-=I-E_h.
\]
The minus branch is an isometry only when \(r<m\). For all parameters,
\[
A_-^*A_+=V_m^*S^{2r}V_m
=\begin{cases}S^{2r/m},&m\mid2r,\\0,&m\nmid2r.\end{cases}
\]
Indeed the output \(mn+2r\) is divisible by \(m\) exactly when \(m\mid2r\),
independently of \(n\). The opposite cross term is the adjoint. Therefore
\[
\boxed{C_{m,r}^*C_{m,r}
=2I-E_{\lfloor r/m\rfloor}
-1_{m\mid2r}\bigl(S^{2r/m}+(S^*)^{2r/m}\bigr).}
\]
For \(r=0\), the cross power is zero and the right side is zero, as required.
No high-end truncation or discarded boundary is used in this formula.

The exact one-step carry cross term occurs iff \(2r=m\). Thus all even
\(m\) with \(r=m/2\) give
\(C_{m,m/2}^*C_{m,m/2}=2I-S-S^*\).
Among nonzero nearest offsets \(r=1\), the unique such radix is \(m=2\).
More generally an exact \(k\)-step cross term occurs iff \(2r=mk\).
For \(k\ge2\), the bottom defect is \(E_{\lfloor k/2\rfloor}\) and cannot
be dropped. For example \((m,r)=(3,3)\) gives
\(2I-E_1-S^2-(S^*)^2\), not the uncorrected two-step Laplacian.
If \(m\nmid2r\), the two branches have disjoint range residues and the
square is simply \(2I-E_h\); no carrier cross energy survives.

This gives a sharp local obstruction: disjoint affine residue channels cannot
manufacture a SUCC cross term. Wider offsets escape it exactly under the
divisibility condition above, with the stated boundary cost.

## Graded first-order operator

On the doubled Hilbert space define
\[
\mathscr D_{m,r}=\begin{pmatrix}0&C_{m,r}^*\\C_{m,r}&0\end{pmatrix},
\qquad \Gamma=\begin{pmatrix}I&0\\0&-I\end{pmatrix}.
\]
This is a bounded self-adjoint operator on the whole doubled space,
\(\{\Gamma,\mathscr D_{m,r}\}=0\), and
\[
\mathscr D_{m,r}^2=\operatorname{diag}(C_{m,r}^*C_{m,r},C_{m,r}C_{m,r}^*).
\]
Its off-diagonal differential is forced by the difference of two specified
affine embeddings; the block notation alone carries no RH content.
For the binary pair, the lower square can also be written explicitly. Let
\(P_o\) project onto positive odd integers. Since \(A_-\) maps onto all
odds and \(A_+\) onto odds at least 3,
\[
C_{2,1}C_{2,1}^*
=2P_o-|1\rangle\langle1|-S^2P_o-P_o(S^*)^2.
\]
It vanishes on the even subspace. In particular the two blocks are not the
same concrete operator even though their nonzero singular spectra agree.

Keeping the branches until coupling is essential: the separate squares sum
to \(2I-E_h\) and lose the entire carrier cross term. The subtraction in
the completed square is internal and exact, but so far produces only the
carry Laplacian; no prime or Gamma identification has been paid for.

## Factor swap is a distinct involution

On ordered positive-integer factor pairs, let
\(J_f\delta_{a,b}=\delta_{b,a}\). Then \(J_f^2=I\). On the finite divisor
fiber \(\mathcal F_n=\operatorname{span}\{\delta_{a,b}:ab=n\}\), the
product-summing map \(M_n\delta_{a,b}=\delta_n\) kills every antisymmetric
vector because \(M_nJ_f=M_n\). Globally this unnormalized product map is
unbounded: \(\|M_n\|=\sqrt{d(n)}\) is unbounded. The normalized fiber
coisometry \(\widetilde M\delta_{a,b}=d(ab)^{-1/2}\delta_{ab}\) is bounded
and still kills the antisymmetric sector. Choosing that normalization
changes amplitudes; it is not harmless when comparing to a trace formula.

In log coordinates \(c=(\log a+\log b)/2\),
\(r_f=(\log a-\log b)/2\), factor swap fixes \(c\) and sends
\(r_f\mapsto-r_f\). Its basis fixed points are \(a=b\), hence perfect-square
products. The full invariant vector subspace is much larger: symmetric
superpositions of distinct factors are also invariant. Confusing basis
fixed points with all invariant vectors would create false square support.

Affine branch exchange and factor swap are not yet the same symmetry. The
former relates two embeddings with a computed overlap; the latter permutes
a factor fiber. There is no supplied canonical intertwiner that turns one
into the other or makes either supply the critical half-density. The equal
appearance of a factor \(1/2\) is therefore not counted as an identification.

Exact controls retain every affine output row before forming the Gram
matrix, so no high-end truncation contaminates the infinite-space identity.
They test all \(1\le m\le7\), \(0\le r\le10\), including the missing
bottom-boundary regime, and separately test grading and cross terms.
