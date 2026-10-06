# Finite-grid Brownian lift: certified diagnostic

Status: **finite certificates and hostile controls only**. This probe neither
constructs a global Brownian compensation nor reduces the infinite sign theorem.
The grid locations, formula evaluator, and event definitions use no zero ordinates.

## Object and exact finite theorem

For distinct positive times `t_1 < ... < t_n`, put

\[
K_{ij}=\Psi(t_i)+\Psi(t_j)-\Psi(t_i-t_j),\qquad
B_{ij}=2\min(t_i,t_j).
\]

The finite lift cost is

\[
c_* = \inf\{c\ge0:K+cB\succeq0\}.
\]

Let `C` be the lower triangular matrix whose entries on and below its diagonal
are one, and let `d_i=t_i-t_{i-1}`, with `t_0=0`. Direct summation gives

\[
B=2C\operatorname{diag}(d_i)C^T,
\quad \det B=2^n\prod_i d_i>0,
\quad \operatorname{rank}B=n.
\]

Thus a single scalar coefficient multiplying the function `|t|` is **not** a
rank-one Hilbert-space correction: its Brownian Gram matrix has full rank on
every such grid. The finite cost is exactly

\[
c_* =\max\left(0,-\lambda_{\min}(B^{-1/2}KB^{-1/2})\right)
=\max\left(0,\sup_{v\ne0}\frac{-v^TKv}{v^TBv}\right).
\]

Congruence by a Cholesky factor may replace the symmetric square root. NumPy
estimates the eigenpair solely to propose a rational witness and an upper shift.
It certifies no sign. Every accepted upper endpoint has an Arb LDL factorization
with strictly positive pivots. Every positive lower endpoint is bounded by the
Rayleigh quotient of the stored **rational** vector, evaluated using Arb. The
machine-readable `lower_exact` and `upper_exact` fields are rational bounds;
rounded display strings are not the authoritative endpoint representation.
When the unshifted matrix has certified positive pivots, `c_*=0` follows exactly
from the definition's constraint `c>=0`.

The code removes time zero and duplicate times by exact rational equality in
`canonical_times`. A zero time contributes a zero row because `Psi(0)=0`;
duplicates contribute identical rows. Quotienting them preserves positivity and
the lift cost. The uniform-grid runs directly use only distinct positive times.

### Arbitrary positive semidefinite B: null directions cannot be dropped

An exact rational simultaneous congruence first transforms `B` to a positive
diagonal block and a zero block. Write the corresponding `K` as

\[
K=\begin{pmatrix}K_R&E\\E^T&N\end{pmatrix},\qquad
B=\begin{pmatrix}B_R&0\\0&0\end{pmatrix},\quad B_R\succ0.
\]

A finite lift exists if and only if

\[
N\succeq0,\qquad \ker N\subseteq\ker E.
\]

Necessity follows by restricting the quadratic form to the null block; a vector
in `ker N` coupled nontrivially to the range block makes the full quadratic
indefinite for every finite `c`. Under these two conditions the Schur complement
is `K_R-E N^\dagger E^T+cB_R`, which admits a sufficiently large shift. Exact
positive pivots of `N` implement this reduction without computing a pseudoinverse.
A remaining nonzero null coupling is rejected. The implementation tests negative
null blocks, indefinite null blocks with zero diagonal, nonzero null coupling,
positive null-block Schur complements, singular congruent `B`, and `B=0`.

This theorem is finite-dimensional linear algebra, not a new RH theorem.

## Certified arithmetic evaluation

The physical-time grids are

\[
t_i=i\log N/m,\qquad i=1,\ldots,m.
\]

For an event located at `log n`, its ramp is active precisely when

\[
n^m<N^i.
\]

This predicate uses exact integer powers. At equality the contribution is
exactly zero and is omitted. No rounded `exp(log n)` determines event inclusion.
The complete smooth Suzuki contribution is enclosed by `event_dynamics.arch`,
including its rigorous exponential-series tail. Weights for actual events are
`log p/sqrt(p^k)`, with all powers supplied by the exact integer sieve. The
symmetry formula generates each kernel entry from `Psi(t_i)` and
`Psi(|t_i-t_j|)`. All certificates use 180-bit Arb arithmetic.

The hostile models preserve this exact event activation. Their weights and
locations are explicit in `events_for`, with random seed `20261006`:

- `increase_first`: multiply the event at 2 by 20.
- `delete_first`: remove the event at 2.
- `relocate_first`: move its unchanged weight to `log 3`.
- `shuffled`: permute all event locations, preserving the weight multiset and
  total mass.
- `random_sparse`: retain a seeded random subset of the actual events.
- `composite_only`: place weight `log n/sqrt n` at every composite `n<=N`.

These are different arithmetic models, not synthetic claims about actual primes.
In particular, deleting an event can increase the pointwise reserve while
breaking the stronger Gram positivity: pointwise positivity and CND are distinct
properties for arbitrary mutations.

## Raw results

The complete reproducible records are
[`evidence/grid_lift_certificates.json`](evidence/grid_lift_certificates.json).
All twelve actual-prime grids below have `c_*=0`, proved on those matrices:

| Horizon N | Grid sizes m | Certified lift cost |
|---:|---|---|
| 16 | 8, 16, 32 | 0 |
| 64 | 8, 16, 32 | 0 |
| 256 | 8, 16, 32 | 0 |
| 1024 | 8, 16, 32 | 0 |
| 4096, larger-horizon holdout | 32 | 0 |

On the single hostile grid `N=64,m=16`, the following deliberately widened
decimal intervals contain the certified lift cost:

| Mutation | Certified enclosure of c_* |
|---|---:|
| Increase first weight | [8.34766, 8.34767] |
| Delete first event | [0.3071302, 0.3071303] |
| Relocate first event | [0.4816571, 0.4816572] |
| Shuffle event locations | [0.3633585, 0.3633587] |
| Random sparse events | [2.1868627, 2.1868630] |
| Composite-only events | [3.7331309, 3.7331314] |

Each positive lower endpoint has a stored rational separating vector. Thus the
probe distinguishes all six mutations from the actual grids. It does not show
that either the list of mutations or the selected grids exhaust a rival class.

### Planted negative tail

Append an event of weight `10^8 log(2)/sqrt(2)` at `log 65` to the finite actual
measure through 64. This event contributes identically zero for every
`|t|<=log 64`, so every entry of the tested `N=64` matrix is unchanged **exactly**.
At `t=log 128`, the same model has

\[
\Psi(t)\in[-33213250.966645601,-33213250.966645599]<0.
\]

This is an explicit support obstruction: all observations on a fixed compact
time interval can miss a subsequently planted negative tail. The artificial
model is not the zeta function, and this control does not refute actual RH.
It refutes inference from these finite certificates to a global lift bound.

## Scope and next use

The sampled actual grids require no Brownian lift at all. There is consequently
no positive fitted trend to extrapolate, and the finite results supply no bound
on lift costs for denser grids, larger horizons, or arbitrary test functions.
The larger horizon is a holdout against these selected finite probes only.

A genuine future theorem would have to control all finite Gram matrices
uniformly, or establish CND by another independent construction. Replacing that
obligation with an unchecked infinite collection of numerical matrices changes
neither its logical strength nor its proof status.

Reproduce with:

```sh
python -m scripts.finite_grid_lift --output research/astra_round_003/evidence/grid_lift_certificates.json
python -m unittest tests.test_finite_grid_lift -v
```

NumPy proposes eigendirections; `python-flint` certifies signs. NumPy version
2.3.5 was used. There are ten focused tests. No source theorem about zeta zeros,
no zero ordinate, and no numerical eigensolver sign enters a certificate.
