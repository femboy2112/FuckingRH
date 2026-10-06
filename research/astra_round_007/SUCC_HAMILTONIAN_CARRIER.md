# The SUCC carrier, its jumps, and its log-height commutator

Status: exact elementary geometry; no new RH estimate.

Unique factorization makes \(\nu(1),\nu(2),\ldots\) a one-way enumeration
of every finitely supported nonnegative prime valuation vector exactly once.
It is a Hamiltonian ray in the graph whose edges include these carrier edges.
It is **not** a Hamiltonian ray in the coordinate nearest-neighbor FUCC graph:
most successive integers are not coordinate neighbors. This distinction
prevents a false locality premise.

## Exact jump length and orientation

In the undirected coordinate graph, distance is the \(\ell^1\) distance of
valuation vectors. Since \(\gcd(n,n+1)=1\), their nonzero supports are
disjoint. Therefore
\[
d(\nu(n),\nu(n+1))
=\|\nu(n+1)-\nu(n)\|_1
=\Omega(n)+\Omega(n+1).
\]
In particular a shortest path removes all prime factors of \(n\) and adds
all prime factors of \(n+1\), in any order. Every removed coordinate has a
negative jump, and every added coordinate a positive jump. The directed FUCC
graph (only increasing coordinates) cannot follow the carrier except
\(1\to2\): for \(n>1\), \(n\nmid n+1\).

The jumps are unbounded: at \(n=2^k\) the distance is at least \(k\).
The total-factor-number commutator is also unbounded. If
\(N_\Omega\delta_{\nu(n)}=\Omega(n)\delta_{\nu(n)}\), then its commutator
with \(\Sigma\) has coefficient \(\Omega(n+1)-\Omega(n)\). At \(n=2^k\),
all factors of \(2^k+1\) are at least 3, so
\[
\Omega(2^k+1)-k\le\frac{\log(2^k+1)}{\log3}-k\longrightarrow-\infty.
\]
Consequently FUCC locality and carrier locality are genuinely different
notions in this basis. A finite-range bound in one does not transfer to the
other by relabeling.

## Log height is different: a compact carrier commutator

Both \(\Sigma\) and its adjoint preserve the height domain stated in
`VALUATION_LATTICE_GEOMETRY.md`. On that domain,
\[
[H,\Sigma]\delta_{\nu(n)}
=\log\!\left(\frac{n+1}{n}\right)\delta_{\nu(n+1)}.
\]
Thus this commutator extends to a compact weighted shift, with norm
\(\log2\) and singular values \(w_n=\log(1+1/n)\). The estimates
\(1/(n+1)\le w_n\le1/n\) prove
\[
[H,\Sigma]\in\mathcal S_q\iff q>1\quad(q>0).
\]
It is not trace class: \(\sum_{n=1}^M w_n=\log(M+1)\).
In contrast the coordinate commutator is the constant increment
\([H,UV_pU^*]=(\log p)UV_pU^*\). This difference is the precise distinction
between compressed carrier log time and a prime jet's equally spaced log
clock. It is not a spectral statement about zeta zeros.

## Carries and histories

Radix carries describe a different coordinate encoding of the same successor
map. The vector change above does not equal a radix carry vector; the two
descriptions are related only through their common integer value unless an
explicit history lift is supplied. A composition-history polynomial evaluates
to that integer, so pulling back \(\nu\), \(H\), or a stratum indicator
along evaluation gives a canonical **observable** on histories. If a fixed
grammar supplies finite nonempty fibers \(\mathcal F_n\), their counting
measure also gives a canonical uniform isometry
\[
J_{\rm hist}\delta_n=|\mathcal F_n|^{-1/2}\sum_{h\in\mathcal F_n}\delta_h.
\]
This does not by itself give an intrinsic successor operation on histories.
One can always define \(J_{\rm hist}SJ_{\rm hist}^*\), but that merely embeds
the original carrier and acts as zero on the orthogonal complement. To make
history information do new work, an independently specified history dynamics
and its compatibility with this lift remain necessary. Infinite fibers
require a different normalization/measure. These are missing constructions,
not an obstruction to every possible history theory.

Exact controls use an independently factored valuation table and
breadth-first nearest-neighbor searches; they do not merely compare two
copies of the jump formula. The proof, rather than any finite sample, gives
the universal statements.
