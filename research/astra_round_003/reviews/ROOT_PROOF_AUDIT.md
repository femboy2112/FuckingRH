# Second triangulation: hostile audit of the root proofs

**Findings first:** no blocking mathematical error found in the four scoped
proofs audited. The common positive moment reconstruction is genuinely
excluded; the support theorem does not claim to exclude non-grading maps;
the finite/free-groupoid distinction and signed-cocycle restrictions are
correct. The successor costs are consistent with the declared immutable
unary machine. One explanatory sentence should be tightened: the
addition-chain lower bound follows because **each addition can at most
double the current maximum**, not from the existence of a doubling chain.
No claim here supplies RH positivity.

Scope: read-only audit of `PRIME_TOWER_MOMENT_CONE.md`,
`COMPOSITE_TO_PRIMITIVE_PROJECTION.md`,
`SUCCESSOR_OPERATIONAL_GEOMETRY.md`, and
`COMPUTATION_GROUPOID_CONTROL.md`; the associated implementations and
moment adversary proof were inspected where they bear on these claims.
No new literature lookup or full-suite run was performed. This is a
same-model independent derivation/check, not an independent external
mathematical authority.

## 1. Moment separation: quantifiers and signs survive

For the pure inverse-power constructor, the scalar function
`z^r-1-r(z-1)` is nonnegative for `r>1` and vanishes only at `z=1`.
Integrating with `Z=(p/N)^(k/2)` therefore proves the stated strict
separator. The barycenter ensures positive individual pure-power
defects, although the separating inequality itself needs only the
nontrivial positive law. Finite conic sums and limits of finite moment
vectors remain in the closed half-space; `(1,1)` is strictly outside.
Thus no hidden normalization assumption was used.

For the log-weighted variant, expanding both sides independently gives

`E[a Z^r]-r E[a Z]+r-1`

for the claimed difference, exactly as required. The remainder has two
nonnegative parts; strictness comes from `E log N < log p` under the
barycenter condition. `N>=1` is essential for `a>=0` and is explicitly
retained. All required expectations exist with `E N=p`. The proof does
not incorrectly assume convexity of `log(N)N^(-k/2)`.

The three-level direct theorem is a separate claim with different
hypotheses. Positive logarithmic masses normalized by the first moment
produce a probability law; the next two equations force variance zero.
The invisible unit causes no problem: it cannot provide positive target
mass. Countable supports are justified by the supplied finite moments.
No barycenter is smuggled into that proof.

Independent rational control: endpoint masses proportional to `2/9` at
`2` and `8/9` at `4` give moments `1/3,1/9,1/24` at levels `2,4,6`.
The first two match the prime `3` target; the third misses, and the
Hankel determinant is exactly `1/648`. This confirms that the three-level
statement is not silently overstating a two-level non-barycentric no-go.

The midpoint coefficient-ratio argument is valid: successive even
binomial coefficient ratios increase strictly, giving both the sharp
small-radius coefficient and monotone cone slopes. Caratheodory counts
are consistent with the number of constrained coordinates. The
constructive decomposition through deviation-mass couplings reproduces
both endpoint probabilities and total mass.

The all-level normalized-law obstruction also survives: on integers
excluding `p`, the chord through `p-1,p+1` lies below a convex function at
every allowed integer. Its inverse-power value diverges with the level.
The document correctly does not extend this conclusion to independent
unnormalized rescalings or automatically to the logarithmic observable.

## 2. Primitive projection and exact support

At any fixed integer `n`, every term of a formal Dirichlet logarithm
uses a finite factorization into factors at least `2`; the coefficient
series terminates. Products of old-monoid factors remain old-generated.
This proves the support theorem with no convergence or positivity
assumption. Formal inverse and coefficientwise-limit extensions have
the same reasoning.

The accelerant counterpart is also valid: the logarithms of positive
integer old states form a locally finite closed set. A test supported
near the missing `k log p` annihilates every approximant and therefore
its distributional limit. The origin-only atom from `|t|` does not enter
that neighborhood. Signed coefficients do not evade this argument.

The proof correctly stops at grading-preserving operations. Addition or
an explicitly relocated event can leave this class. The barycentric
identity for endpoint values is not a missing algebra homomorphism.
The positive-partition counterexamples have the stated coefficients:
`log(1+z)` has second coefficient `-1/2`, and the two-order factorization
at `6` produces `1-2=-1` in the correlated control.

## 3. Successor model and input accounting

The loops consume existing input tails as control steps and allocate a
successor only when a new output numeral node is created. Existing-input
addition therefore costs `m` successor operations and `m+1` tests.
Multiplication makes `m` additions of length `n`, together with `m+1`
outer tests, hence `nm` successors and `nm+2m+1` tests. Expression-level
recurrences correctly add both child costs and one syntax dispatch.

As an independent small unrolling, `(n,m)=(2,3)` gives `6` successors and
`13` tests, while `(3,2)` gives `6` and `11`. The distinction in control
cost is deliberate operand orientation, not a numerical discrepancy.
For `S(S(S(1)))` multiplied by itself, two tree copies cost `8` initial
successors and the output costs `16`, giving `W=24` and `D=9` as stated.
This is formula-tree evaluation, not a shared DAG with free input reuse.

The bound `W>=n` is valid for construction from zero with this immutable
unary representation: the output contains `n` allocated successor nodes.
It is not asserted for pre-supplied `n`, cyclic/compressed unary storage,
or hardware integers. The zero-excess trap is therefore correctly scoped.
The Pareto recurrence omits only dominated identity products; every
remaining child value is smaller. Coordinatewise-monotone recurrences
justify pruning dominated children, and sorting before pruning is safe.

**Wording improvement only:** replace “Doubling at every step gives the
lower bound” by the maximum-growth argument identified above. Powers of
two witness sharpness, rather than proving the lower bound by themselves.

## 4. Computation groupoid and comparison square

The free groupoid of a finite graph is generally infinite; the document
states this explicitly. Assigning negative costs to formal inverses makes
the additive signed cocycle well defined, while the text does not treat
those negatives as executable work. A nonnegative real cocycle on every
arrow must vanish because inverses negate it. In a genuinely finite
groupoid every isotropy element has finite order, so real loop cocycles
vanish; remaining cocycles are endpoint-potential differences. These are
correct universal claims.

The residue construction `Pair({0,...,N}) x (Z/mZ)^3` is genuinely finite.
The functor from histories may have only a subgroupoid as its image; the
proof does not require surjectivity onto all displayed residues. It retains
residues, not ordered costs. The implementation verifies path composability
and declared endpoints before constructing the finite arrow.

The adelic comparison remains properly limited. On nonzero adeles a
rational multiplier is determined by its source and target, so many
computation histories become the same rational-action arrow. Valuation
vectors encode the multiplier, not a program computing it.

Separately, the Mellin/trace square in
`ADELIC_COMPUTATION_GROUPOID_COMPARISON.md` is valid for smooth compact
additive tests, norm-dependent multiplicative tests, normalized compact
Haar factor, and the trivial compact-character cohomology sector:
`J(phi)(u)=u^(-1/2)phi(log u)` intertwines convolutions by direct
substitution. Its half-density involution agrees with the additive
conjugate-reflection involution. The trace identity is a normalized
explicit-formula identification, **not** a positive Hilbert-space
isometry. Nonsmooth tents require the previously established Weil/tent
extension, which the report explicitly cites. No new map from computation
histories to that primitive trace pairing has been established.

## 5. Limits of this audit

No proof in this set shows that every conceivable positive operator must
solve the declared inverse-power moment equations. No result equates
correct scalar amplitude scale with exact event locations. No finite
atlas or certificate proves an infinite tail. These restrictions are
present in the audited text and should be preserved in synthesis and PR
language. The first unpaid proof-bearing object remains an explicit
arithmetic map into the exact Suzuki pairing with controlled common-mode
cost.
