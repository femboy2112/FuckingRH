# Bernstein operators on the actual prime service nodes

**Result:** a positive barycentric Bernstein-type operator can be constructed
on the nonuniform prime service grid. Its prescribed arithmetic marginal
and the required reserve sign do not follow. The unmodified uniform-to-prime
martingale prescription is impossible, and its concave Jensen inequality
has the wrong orientation. These are scoped obstructions, not a prohibition
on compensated transport.

Base inspected: `77ba6793be220c2fb5c2f0a6c250c54774acb9ea`.
Branch: `astra/prime-transport-martingale-002`.

## 1. Objects and the obligations an operator must satisfy

For the first `j` actual prime-power events, define

\[
 a_i=\log q_i,\quad w_i=\frac{\Lambda(q_i)}{\sqrt{q_i}},\quad
 S=\sum_{i=1}^j w_i,\quad \sigma_i=A'(a_i),
\]
\[
 \lambda=db\big|_{[0,S]},\qquad
 \nu=\sum_{i=1}^j w_i\delta_{\sigma_i}.
\]

Both measures have mass `S`; probabilities are obtained by dividing both
by `S`. All `sigma_i` are strictly increasing because `A''>0` on
`[log 2,infinity)`. On their hull the inverse `T=(A')^{-1}` is strictly
increasing and strictly concave:

\[
 T'(b)=\frac1{A''(T(b))}>0,\qquad
 T''(b)=-\frac{A'''(T(b))}{A''(T(b))^3}<0.
\]

An extension of `T` below `sigma_1` must be supplied before using a
global concavity statement on `[0,S]`. The restricted inverse clamped
constant there is not globally concave: its derivative jumps upward from
zero to a positive number. An affine tangent extension avoids that
particular defect, but does not fix the separate marginal obstructions.
The exact initial/compensation term belongs in the transport identity;
it must not be discarded when interpreting the inequalities below.

A kernel into the grid has coefficients `k_i(b)` and operator

\[
 Bf(b)=\sum_i k_i(b)f(\sigma_i).
\]

There are **four different conditions**:

1. `k_i(b)>=0` (positivity);
2. `sum_i k_i(b)=1` (constant reproduction);
3. `sum_i sigma_i k_i(b)=b` (barycentric reproduction);
4. `integral k_i(b)lambda(db)=w_i` (the exact arithmetic output marginal).

Putting `w_i` somewhere in a coefficient formula does not establish item 4.

## 2. Primary literature: what transfers

- [Aldaz–Render, *Generalized Bernstein operators on the classical
  polynomial spaces*, arXiv:1803.01673v2](https://arxiv.org/pdf/1803.01673),
  Definition 2.2, equations (5)–(6), and Theorem 3.2: fixing two functions
  constrains the nodes and weights through their basis coefficients.
  Arbitrary prescribed nodes and marginals are not automatic.
- [Aldaz–Render, *Generalized Bernstein operators defined by increasing
  nodes*, arXiv:1803.05343](https://arxiv.org/pdf/1803.05343) studies
  existence under ordered-node and shape-preservation constraints.
- [Jourdain–Pagès, *Quantization and martingale couplings*, ALEA 19
  (2022)](https://alea.impa.br/articles/v19/19-01.pdf) develops convex-order
  preserving quantization and its martingale interpretation. Its premise
  includes the required convex ordering; that premise cannot be supplied
  by renaming a prime-weighted discretization.
- [Jourdain–Margheriti, *A new family of one dimensional martingale
  couplings*, arXiv:1808.01390v2](https://arxiv.org/html/1808.01390v2)
  constructs couplings from convex-order hypotheses, and treats
  super/submartingale variants with their corresponding orders.

The following constructions and obstructions are proved explicitly here.
No novelty claim is made for the general approximation/transport facts.

## 3. Exact Bernstein construction, including the actual weights

Reindex the `j>=2` nodes as `z_0<...<z_n`, `n=j-1`, and let
`v_i=w_{i+1}>0`. Define the weighted binomial probabilities

\[
 p_i(u)=\frac{v_i\binom ni u^i(1-u)^{n-i}}
                 {\sum_{r=0}^n v_r\binom nr u^r(1-u)^{n-r}},
 \qquad 0<u<1,
\]
\[
 m(u)=\sum_i z_i p_i(u).
\]

Put `theta=log(u/(1-u))`. Differentiating this finite exponential family,

\[
 \frac{dm}{d\theta}
 =\operatorname{Cov}_{p(u)}(z_I,I)
 =\frac12\sum_{i,r}p_i(u)p_r(u)(z_i-z_r)(i-r)>0.
\]

Moreover `m(0+)=z_0` and `m(1-)=z_n`. Thus `m` has a unique inverse
`u(b)` on `(z_0,z_n)`. Set

\[
 k_i(b)=p_i(u(b)),\qquad
 Bf(b)=\sum_i k_i(b)f(z_i).
\]

At endpoints take the limiting point masses. This explicitly proves
positivity, constant reproduction, and `B(id)=id` on the node hull.
It uses the exact `w_i` in its definition and no zero ordinates.

It also has a genuine order-two total-positivity property. For `i<r`,

\[
 \frac{k_r(b)}{k_i(b)}
 =\frac{v_r\binom nr}{v_i\binom ni}
       \left(\frac{u(b)}{1-u(b)}\right)^{r-i}
\]

is strictly increasing, so all ordered `2x2` minors are positive in the
interior. This is an actual Pascal/binomial construction, rather than
an unsupported claim that some average ought to preserve signs. No
higher-order variation-diminishing claim is needed here.

**What it does not prove:** the induced masses
`tilde w_i=integral k_i(b)lambda(db)` need not equal `w_i`.
Indeed for just two nodes, barycentric reproduction uniquely forces

\[
 k_0(b)=\frac{z_1-b}{z_1-z_0},\qquad
 k_1(b)=\frac{b-z_0}{z_1-z_0},
\]

regardless of the weights initially inserted in the binomial formula.
Uniform input on the node hull assigns equal output masses. The actual
weights at `q=2,3` are unequal. Thus even after replacing the source
interval by the node hull, inserting prime weights is not a marginal proof.

For comparison, using the *unreparameterized* ordinary Bernstein basis
on `[l,r]` and requiring both constants and `id` to be fixed forces
`z_i=l+i(r-l)/n`, by uniqueness of coefficients in that basis. The actual
first three service nodes are not equally spaced. Nonuniformity kills
that narrow classical prescription, but not the construction above.

## 4. Sharp grid lemma: prescribed marginals require more than positivity

Let `z_0<...<z_n` be any finite grid, and let a finite source measure
`eta` be supported on its hull. For `b in[z_i,z_{i+1}]`, define the
adjacent-node kernel

\[
 L(b,\cdot)=\frac{z_{i+1}-b}{z_{i+1}-z_i}\delta_{z_i}
          +\frac{b-z_i}{z_{i+1}-z_i}\delta_{z_{i+1}}.
\]

**Lemma.** `L` is the unique barycentric kernel restricted to those
two adjacent nodes. Among *all* grid-valued laws of mean `b`, it minimizes
every convex cost. Consequently its output measure `eta_*=eta L` is
minimal in convex order among output marginals of barycentric grid kernels.

Proof. For a convex function `f`, the linear interpolation `I_f` of its
values on the grid is convex. For any grid-valued `Y` with `E[Y]=b`,
`E f(Y)=E I_f(Y)>=I_f(b)`, while the adjacent-node law attains `I_f(b)`.
Integrate this inequality against `eta`. QED.

It follows that a prescribed grid measure `rho` can be the output of
a barycentric kernel from `eta` **iff** it has the same mass and mean
and `eta_*<=_cx rho`. Necessity is the lemma. Sufficiency follows by
composing `L` with a finite martingale coupling from `eta_*` to `rho`
(the finite form of the martingale convex-order theorem).

This condition has a finite, sharp test:

\[
 \int(y-z_k)_+\rho(dy)
 \ \ge\ \int(b-z_k)_+\eta(db),\qquad k=1,\ldots,n-1,
\]

together with mass and mean equality. Every convex function on the
grid is an affine function plus a nonnegative sum of these hinges;
hinges at grid nodes are reproduced exactly by adjacent interpolation.
Thus the call tests are sufficient as well as necessary.

For Lebesgue input on the node hull, the adjacent kernel's masses are

\[
 m_0=\frac{z_1-z_0}2,\quad
 m_n=\frac{z_n-z_{n-1}}2,\quad
 m_i=\frac{z_{i+1}-z_{i-1}}2\ (0<i<n).
\]

They depend on grid spacings, not on von-Mangoldt weights. Any source
rescaling multiplies all these masses by the same scalar; it does not
give individual freedom to set them to the prime weights.

## 5. Two exact obstructions for the actual uniform source

### 5.1 Convex-hull obstruction, with a sharp quantitative cost

Write `l=sigma_1`, `r=sigma_j`. Every positive constant-reproducing
kernel supported on these nodes has mean `m_K(b) in[l,r]`. Since
`l>0`, it cannot reproduce `b` on the positive-measure interval `(0,l)`.
At active endpoints with `S>r`, the interval `(r,S)` also fails.

More sharply, because `S>l` for every nonempty actual prefix,

\[
 \int_0^S|m_K(b)-b|\,db
 \ge \frac{l^2}2+\frac{(S-r)_+^2}2>0.
\]

Proof: pointwise the distance is at least the distance from `b` to
`[l,r]`; integrate. Without a prescribed output marginal this bound is
sharp: clamp to the endpoints outside the hull and use `L` inside.
With a prescribed marginal further error may be necessary.
Thus any approximate barycentric scheme has a strictly positive,
explicit boundary debit. “Small” is not “zero.”

### 5.2 First-moment obstruction survives reversing the kernel

Any exact martingale coupling in **either** direction between `lambda`
and `nu` requires

\[
 D_j:=\sum_{i\le j}w_i\sigma_i-\frac{S_j^2}2=0.
\]

This necessary equality fails already for actual primes, with rigorously
enclosed signs from the unmutated Archimedean formula:

| Last prime-power event | Certified interval for `D_j` |
|---|---:|
| 2 | `(-0.009847,-0.009846)` |
| 7 | `(0.008874,0.008875)` |
| 8 | `(-0.009696,-0.009695)` |
| 11 | `(0.011625,0.011626)` |

The signs are not constant. These are finite counterexamples to an
all-prefix exact-martingale prescription, not evidence about an infinite
tail. Arb tests also certify `sigma_1 in(0.224975,0.224976)` and
`S_1>sigma_1`. A single constant shift of every service node cannot
center both the prefixes ending at 2 and 7: it would need opposite signs,
since the required shift is `-D_j/S_j`.

For a supermartingale from `nu` to `lambda`, which would have the useful
increasing-concave direction, one needs `D_j>=0`; the prefix at 2 already
fails. A submartingale would require the reverse first-moment inequality,
but does not supply the desired increasing-concave Jensen conclusion.
Compensated measures must be assessed on their own exact mass, mean,
support, and call inequalities.

## 6. Jensen points the wrong way for the forward operator

For any concave `T` on the common domain, a barycentric kernel into the
prime nodes satisfies

\[
 BT(b)\le T(b).
\]

If its prescribed output marginal were `nu`, integration would give

\[
 \sum_i w_i T(\sigma_i)\le\int_0^S T(b)\,db.
\]

The left side is `H_j=sum_i w_i a_i`. The reserve argument seeks the
opposite difference, plus its exact initial/compensation term. Therefore
ordinary forward Bernstein Jensen does not pay the arithmetic reserve;
it supplies a debit. The reverse martingale from discrete nodes to the
continuous reference would give the useful direction, but it must meet
the moment and convex-order conditions just identified.

The debit can be quantitatively unavoidable even after repairing support.
On a node hull where `-T''>=kappa>0`, every grid-valued barycentric law
of mean `b in[z_i,z_{i+1}]` has

\[
 \operatorname{Var}(Y)\ge(b-z_i)(z_{i+1}-b),
\]

by the minimal-convex-cost lemma applied to `y^2`. Strong concavity gives

\[
 T(b)-E[T(Y)]\ge\frac\kappa2(b-z_i)(z_{i+1}-b).
\]

With Lebesgue input on the hull, integration yields the sharp variance
lower bound and the associated concavity bound

\[
 \int(T-BT)\,db\ge\frac\kappa{12}\sum_i(z_{i+1}-z_i)^3.
\]

Equality in the variance minimum uses the adjacent kernel. The final
concavity bound is attained for a quadratic of curvature `-kappa`.
Thus an exact initial credit must cover a nonzero Jensen loss; it cannot
be removed by total positivity or finer prose.

## 7. Moment-preserving hostile control on the actual grid

Take any four distinct service nodes `z_0<z_1<z_2<z_3` and set

\[
 v_i=\frac1{\prod_{r\ne i}(z_i-z_r)}.
\]

Lagrange interpolation of `1,x,x^2` proves
`sum_i v_i z_i^k=0` for `k=0,1,2`, by taking the coefficient of `x^3`.
The signs of `v_i` are `(-,+,-,+)`. A sufficiently small nonzero
perturbation `w_i→w_i+epsilon v_i` keeps all masses positive and
preserves total mass and the first two moments **exactly**.

Nevertheless the change in call value at the second node is

\[
 \sum_i v_i(z_i-z_1)_+=v_0(z_1-z_0)<0,
\]

while at the third node it is `v_3(z_3-z_2)>0`.
Hence the original and perturbed grid measures are incomparable in
convex order, despite matching their first two moments. This applies to
the actual first four service nodes as well as to an equally spaced grid.
Neither first-two-moment fitting nor positivity of coefficients certifies
the missing order inequalities.

The ordinary Bernstein construction above survives deletion, duplication,
weight increase, or relocation whenever it still has an ordered positive
grid. That robustness exposes its limitation: its elementary identities
alone cannot imply the mutation-sensitive RH reserve. Any complete
argument needs an additional premise involving the exact arithmetic
weights and completion which fails under those mutations.

## 8. Disposition and precise surviving obligation

- **Constructed:** weighted, reparameterized binomial kernel on the actual
  node hull, with positivity, constants, barycenters, and TP2 proved.
- **Refuted:** the simultaneous unmodified uniform-source / exact-prime-
  marginal / exact-barycenter prescription; also the use of forward
  concave Bernstein Jensen as the desired reserve sign.
- **Proved:** sharp nearest-grid convex-order criterion, unavoidable
  boundary bias, and a quantitative Jensen debit.
- **Still open:** a compensated source/target pair whose exact accounting
  yields the reserve and whose required one-sided or projected order can
  be proved arithmetically. The compensation must be retained in both
  the marginal equations and the final inequality.

No statement here excludes all positive compensated, signed-residual,
or non-martingale constructions. No numerical LP fit is promoted to an
all-prefix theorem, and RH remains unproved.

Validation: `tests/test_bernstein_prime_operator.py` checks exact
binomial/TP2 identities, the two-node marginal failure, neighboring-grid
variance, moment-preserving call crossings, and the actual-prime
first-moment counterexamples with Arb interval arithmetic.
