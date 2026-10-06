# First-order candidates: what their squares actually contain

RH OPEN. These are forced incidence/difference operators, not sqrt(K).
Every candidate is accompanied by its actual compression or an obstruction.

## 1. Carrier chirality, jet charge, stratum current, cone current

On finite input {1,...,N}, keep outgoing carrier states through 2N+1 for
`A_+e_n=e_(2n+1)` and `A_-e_n=e_(2n-1)`. Put `C=A_+-A_-`.
This rectangular realization preserves
`C*C=2I-S_N-S_N*`. Truncating the output to N first changes the square by
an upper-boundary term; it is not the same operator.

Embed the visible `B_jet e_n=sqrt(w_n)e_n` in that same carrier output.
Then a genuine coherently coupled trial is
\[
A_N=C-B_{\rm jet},\qquad
A_N^*A_N=C^*C+B_{\rm jet}^*B_{\rm jet}
-C^*B_{\rm jet}-B_{\rm jet}^*C.
\]
Here
\[
(C^*B_{\rm jet})_{ij}
=\sqrt{w_j}(1_{j=2i+1}-1_{j=2i-1}).
\]
The cross terms are nonzero and arithmetically specified. Squaring channels
separately deletes them. The relative sign selects the two-channel difference;
geometry alone has not proved that this choice is the Weil map.

The other forced maps are `F_N=[S,P_1]` and the cone boundary incidence
`Q_N e_(a²-1)=e_a`, with all other columns zero. Their direct sum with C
and B_jet gives a positive first-order incidence energy with all three kinds
of event, and its doubled block is a self-adjoint graded Dirac. But this
orthogonal sum has no cross-channel cancellation. Adding F_N and Q_N to
A_N as separate output sectors remains a construction, not an identity to
Weil. The exact scripts retain these terms separately to expose what is lost.

`F_N*F_N` detects only entering/leaving the one-support stratum. For example
2->3 is inside the stratum, so it contributes zero current even though both
endpoints have nonzero Lambda. A current square alone cannot equal the jet
charge. These are different observables with closed arithmetic formulas.

## 2. Factor-chiral and factor-coordinate candidates

The swap-odd operator `(I-R)Pi_triangle M*` has square
`diag(d(n)-1_(n square))` and is annihilated by multiplication projection.
It is nonzero before projection, but its energy is a divisor statistic.

The nearest-coordinate factor graph on `ab<=N` supplies a separate incidence
Dirac. Its compressed off-diagonals are exactly
`-2*1_((m-n)|n)` for n<m (normalized by sqrt(d(n)d(m)) for the isometric lift).
These divisor-difference cross terms are a stable bulk, not an upper-boundary
error. Deleting unit factors kills every prime column and all nearest SUCC
cross terms. Proofs and tests are in `FINITE_CARRIER_CONE.md`.

The more general same-factor locality theorem rules out changing weights to
repair that defect: `L*S_XL=0` for every lift preserving a nonunit divisor.
Escaping requires factor-label mixing or unbounded propagation, not just a
larger matrix or extra positive diagonal weights.

## 3. Why a simple SUCC/FUCC bicomplex does not close

If exterior directions are attached to `S-I` and `V_p-I`, then the cross
coefficient of d² is their commutator. On e_n,
\[
[S,V_p]e_n=e_{pn+1}-e_{p(n+1)}\ne0.
\]
The affine braid is `V_p S=S^p V_p`, not commutation. Hence the naive Koszul
bicomplex is not a complex. One can add 2-cells for the braid word, but their
boundary has p carrier edges on one side and one on the other; no canonical
metric identity to Weil follows from declaring those cells. This avoids
silently returning to the factorized C88 construction.

## 4. The compression problem is decisive

A finite carrier matrix acts on coefficient sequences. It does not yet act
on the continuum Weil test class. Sampling f(log n), sampling any finite jets
there, or taking a single fixed log-cell average leaves a common invisible
space for every horizon. `CARRIER_OBSERVATION_NO_GO.md` proves that Weil is
strictly positive on some such invisible tests, so **no** D_N after those
maps can have the required exact identity or all-test convergence. This
applies to every candidate above regardless of coherent internal cross terms.

Keeping a continuum test register escapes this sampling obstruction. The
natural Mellin translation-difference square then does reproduce the prime
cross terms, but `WEIL_SQUARE_ATTEMPT.md` computes its infinite-rank negative
bulk residual. Thus the next construction must evade both obstructions.

The evidence is not a theorem that every conceivable stratified Dirac fails.
It eliminates the specified observation maps, factor-local stencils and
finite-rank repairs. An exact continuum, nonlocal, label-mixing coupling with
its full completed pairing has not been constructed.
