# Valuation lattice and the exact graph diagonal

Status: elementary identities proved here, with exact finite controls. No RH
positivity conclusion follows from this change of coordinates.

## Hilbert spaces, operators, and domains

Let \(\mathcal A=\mathbb N_0^{(\mathcal P)}\) be the countable set of finitely
supported prime valuation vectors. Unique factorization gives the bijection
\(\nu:\mathbb N_{>0}\to\mathcal A\), hence the unitary
\(U\delta_n=\delta_{\nu(n)}\) from \(\ell^2(\mathbb N_{>0})\) to
\(\ell^2(\mathcal A)\). Thus this lift retains all integer-state information;
it does not by itself add degrees of freedom. A tensor/history extension can
add degrees of freedom, which must subsequently be accounted for.

The isometries \(S\delta_n=\delta_{n+1}\) and
\(V_m\delta_n=\delta_{mn}\) are bounded everywhere. Their adjoints are
\(S^*\delta_1=0\), \(S^*\delta_n=\delta_{n-1}\) for \(n>1\), and
\(V_m^*\delta_n=\delta_{n/m}\) when \(m\mid n\), zero otherwise.
For prime \(p\), \(UV_pU^*\delta_\alpha=\delta_{\alpha+e_p}\).
The different coordinate shifts commute. Set \(\Sigma=USU^*\).

The log height is the nonnegative self-adjoint multiplication operator
\[
H\delta_\alpha=h(\alpha)\delta_\alpha,
\quad h(\alpha)=\sum_p\alpha_p\log p,
\quad \mathcal D(H)=\{f:\sum_\alpha h(\alpha)^2|f_\alpha|^2<\infty\}.
\]
Finite-support vectors form a core. All unbounded identities in this note
hold on that core and on the stated maximal domains. In particular,
\([H,UV_pU^*]=(\log p)UV_pU^*\) extends boundedly; the coordinate shift and
its adjoint preserve \(\mathcal D(H)\). No finite-prime truncation is needed
to define any of these operators.

## The graph diagonal

In \(\mathcal H_c\otimes\mathcal H_m\), define the **closed** graph subspace
\[
\mathcal D=\overline{\operatorname{span}}
\{\delta_n\otimes\delta_{\nu(n)}:n\ge1\}.
\]
The closure matters: the algebraic span alone is not a Hilbert subspace.
Its canonical isometry and orthogonal projection are
\[
J\delta_n=\delta_n\otimes\delta_{\nu(n)},\qquad
P_{\mathcal D}=JJ^*
=\sum_{n\ge1}|n,\nu(n)\rangle\langle n,\nu(n)|,
\]
where the sum converges strongly. The subspace is reducing, not merely
forward invariant, for \(S\otimes\Sigma\) and for every synchronized
\(V_p\otimes UV_pU^*\). Consequently,
\[
J^*(S\otimes\Sigma)J=S,
\qquad J^*(V_p\otimes UV_pU^*)J=V_p.
\]
One proof identifies the second tensor basis with another integer \(m\):
the simultaneous moves \((n,m)\mapsto(n+1,m+1)\) and
\((n,m)\mapsto(pn,pm)\) preserve equality, as do their partial inverses.

The source-inclusive prime-jet incidence subspace is exactly
\[
\mathcal D_p=\overline{\operatorname{span}}
\{|p^k\rangle\otimes|ke_p\rangle:k\ge0\}
=\mathcal D\cap(\mathcal H_c\otimes\ell^2(J_p)).
\]
Its projection is the corresponding strong sum of rank-one projections.
Distinct \(\mathcal D_p\) share precisely the source vector
\(|1\rangle\otimes|0\rangle\); removing that source makes their positive-depth
parts orthogonal. \(\mathcal D_p\) is not invariant under the one-step joint
carrier, but its induced return map is multiplication by \(p\).

Compression \(\Phi(X)=J^*XJ\) is unital completely positive, but is **not an
algebra homomorphism**. In particular,
\[
\Phi(A\otimes UBU^*)_{nm}=A_{nm}B_{nm}.
\]
For \(X=S\otimes I\) and \(Y=I\otimes\Sigma\),
\(\Phi(X)=\Phi(Y)=0\) while \(\Phi(XY)=S\). This is an exact reason that
coupling before projection can retain information lost by separate projection.
The block map \(E(X)=P_{\mathcal D}XP_{\mathcal D}+
(I-P_{\mathcal D})X(I-P_{\mathcal D})\) is the natural normal conditional
expectation onto the block-diagonal algebra. The corner compression itself
should not be mislabeled as an expectation onto all original operators.

## A natural incidence operator, with a sharp gap obstruction

Let \(H_c\delta_n=\log n\,\delta_n\). The diagonal self-adjoint operator
\[
K=H_c\otimes I-I\otimes H,
\quad K|n,\nu(m)\rangle=\log(n/m)|n,\nu(m)\rangle
\]
has domain given by square summability after multiplication by
\(\log(n/m)\). Then \(\ker K=\mathcal D\) exactly and
\(P_{\mathcal D}=1_{\{0\}}(K)\). However there is **no spectral gap off the
graph diagonal**:
\[
\|K|n,\nu(n+1)\rangle\|=\log(1+1/n)\longrightarrow0.
\]
On the finite box \(n,m\le N\), the smallest nonzero absolute eigenvalue is
\(\log(N/(N-1))\), whose reciprocal grows like \(N\); the inverse
coercivity constant for \(K^2\) grows like \(N^2\). The spectrum of the
full operator is \(\mathbb R\), since positive rational numbers are dense
and its eigenvalues are all logarithms of positive rationals.

Thus the natural height-mismatch square \(K^2\) detects the graph but does
not provide a uniform coercive estimate on its complement. Replacing its
spectral projection by an inverse or a fixed-gap estimate incurs a real,
explicitly diverging cost. This refutes that particular projection mechanism;
it does not rule out nonlocal incidence operators or a different metric.

## Prime-power charge

Let \(P_r\) project onto \(|\operatorname{supp}\alpha|=r\). On \(P_1\),
define \(Q_1\delta_{ke_p}=(\log p)\delta_{ke_p}\), \(k\ge1\), and set it
to zero elsewhere. This nonnegative diagonal operator has its maximal
weighted \(\ell^2\) domain. The bounded extension of
\[
E_{\rm jet}=Q_1e^{-H/2},\qquad
B_{\rm jet}=Q_1^{1/2}e^{-H/4}
\]
satisfies \(B_{\rm jet}^*B_{\rm jet}=E_{\rm jet}\) and
\[
E_{\rm jet}\delta_{\nu(n)}=\frac{\Lambda(n)}{\sqrt n}\delta_{\nu(n)}.
\]
Here the common source \(1\) belongs to \(P_0\), not \(P_1\), and has zero
charge. Since \(\Lambda(n)\le\log n\), the event eigenvalues tend to zero
and are at most \(2/e\). Hence \(E_{\rm jet}\) is compact and bounded.

There is nevertheless no unregularized finite trace. More precisely,
\[
E_{\rm jet}\in\mathcal S_q\iff q>2,
\qquad B_{\rm jet}\in\mathcal S_q\iff q>4 \quad(q>0).
\]
For the first assertion, the Schatten sum is
\(\sum_{p,k}(\log p)^q p^{-kq/2}\). It converges for \(q>2\) by comparison
with \(\sum_{n\ge2}(\log n)^q n^{-q/2}\); for \(q\le2\) its prime terms
eventually dominate \(1/p\). The elementary Euler divergence of
\(\sum_p1/p\) follows because a finite product
\(\prod_{p\le X}(1-1/p)^{-1}\) dominates \(\sum_{n\le X}1/n\).
The square-root assertion follows by replacing \(q\) with \(q/2\).

These are upstream positive operators. None identifies their energy with the
completed Suzuki form. The signs and the infinite-place completion remain
separate proof obligations.

Reproduction: `python -m unittest tests.test_round007_geometry -v` and
`python -m scripts.round007_geometry`.
