# Independent moment-cone adversarial audit

Scope: a positive combination of *additive-barycentric inverse-power
Jensen defects*. This is an amplitude test, not an identification of a
Suzuki ramp, knot measure, Gram map, or primitive extraction. No claim of
literature priority is made. RH is not proved or reduced by this audit.

## 1. State the proposed marginal exactly

For a prime p, let a cell be a probability law ν on positive old-generated
integers, with ∫n dν=p. Define

\[
 H^{(k)}_p(\nu)=\int n^{-k/2}\,d\nu-p^{-k/2},\qquad
 m_k(\nu)=p^{k/2}H^{(k)}_p(\nu).
\]

For a symmetric cell at p±d, put u=d/p and

\[
 g_k(u)=\tfrac12[(1-u)^{-k/2}+(1+u)^{-k/2}]-1;
 \qquad m_k=g_k(u).
\]

A proposed **common conic weighting** λ_c≥0 of cells must satisfy

\[
 \sum_c\lambda_c m_k(\nu_c)=1
\]

at every requested tower level k. A convex weighting additionally has
Σλ_c=1. The common factor log p in the tower weights cancels. All
statements below concern these exact equations; inserting a log n jet
or a signed primitive map defines a different problem and needs its own
proof.

## 2. A separator for arbitrary barycentric cells

**Theorem.** If 0<k<l and ν is a nontrivial barycentric cell, then

\[
 m_k>0,\qquad m_l>\frac lk m_k.
 \tag{1}
\]

Allow +∞ on the left where an inverse moment fails to exist. For integer
endpoints all inverse moments are bounded, so there is no such issue.

**Proof.** Write X=n/p, Z=X^{-k/2}, and r=l/k>1. Strict convexity of
x↦x^{-k/2}, with EX=1, gives EZ>1. Pointwise,

\[
 Z^r-1-r(Z-1)\ge0,
\]

with equality exactly at Z=1. Integration proves (1), strictly for every
nontrivial cell. This proof allows three, four, or arbitrarily many
endpoints, unbounded endpoint sets, and nonsymmetric barycentric laws.

Consequently the closed half-space

\[
 v_l-(l/k)v_k\ge0
\]

contains the entire positive cone and its finite-moment limits, whereas
its value at the desired target (1,1) is 1−l/k<0. **No common positive
weighting, normalized or unnormalized, matches even two distinct tower
levels.** This is a finite-dimensional separating certificate, not a
numerical LP conclusion.

The coefficient l/k is sharp if arbitrary positive real endpoints are
allowed without an upper bound. Use a two-point barycentric law on
(a,b), 0<a<1<b. First let b→∞ and then a↑1. The ratio tends to
(a^{-l/2}−1)/(a^{-k/2}−1) and then to l/k. This sharpness statement does
not assert that every fixed-prime integer endpoint set attains that
infimum.

A useful exact k=1,l=2 identity is

\[
 m_2-2m_1=E(X^{-1/2}-1)^2>0.
\]

For k=2,l=4 the analogous identity is
m_4−2m_2=E(X^{-1}−1)^2>0; this gives a fully rational hostile probe on
integer endpoints.

## 3. Sharper separators exploit midpoint or bounded support geometry

### 3.1 Symmetric midpoint cells

For 0<u<1, the absolutely convergent binomial expansion gives

\[
 g_k(u)=\sum_{j\ge1}\frac{(k/2)_{2j}}{(2j)!}u^{2j}.
\]

For l>k>0 the ratio of the l-coefficient to the k-coefficient is strictly
increasing in j. Its first value is

\[
 c_{k,l}=\frac{l(l+2)}{k(k+2)}.
\]

Termwise comparison, with strictness already in the fourth-order term,
therefore proves

\[
 \boxed{g_l(u)>c_{k,l}g_k(u)\quad(0<u<1).}
 \tag{2}
\]

The coefficient is sharp as u↓0. In particular, g_2>(8/3)g_1 and
g_4>3g_2. Thus the proposed tower target does not merely miss the cone by
a small normalization error; its ratios point to the wrong side of an
exact positive functional.

The ratio g_l(u)/g_k(u) is itself strictly increasing in u. One proof:
write it as the mean of the increasing coefficient ratios under weights
proportional to a_j u^{2j}. Its logarithmic derivative is twice the
strictly positive covariance of j and that coefficient ratio. The
series are absolutely convergent for u<1, so the differentiation is
justified. On a finite allowed radius set D, the exact extreme slopes
are attained at min D and max D.

### 3.2 Any barycentric law with endpoints below 2p

For k=1,l=2 one can improve the universal coefficient 2 without assuming
symmetry. Let y=√X and subtract the affine tangent at X=1:

\[
 R_1(X)=X^{-1/2}-1+\tfrac12(X-1)
       =\frac{(y-1)^2(y+2)}{2y},
\]
\[
 R_2(X)=X^{-1}-1+(X-1)
       =\frac{(y-1)^2(y+1)^2}{y^2}.
\]

Their ratio away from X=1 is

\[
 \frac{R_2(X)}{R_1(X)}
 =2+\frac{2}{\sqrt X(\sqrt X+2)}.
\]

It decreases strictly in X. For 0<X<2, it is strictly greater than
1+√2. Barycentricity annihilates the affine tangents. Hence

\[
 \boxed{m_2>(1+\sqrt2)m_1.}
 \tag{3}
\]

More generally, if X≤B with B>1, replace 1+√2 by
2+2/[√B(√B+2)]. This is sharp over real barycentric laws with that upper
bound: use two-point laws at 1−ε and B and let ε↓0. Again integer
arithmetic can only narrow this class further.

## 4. Exact convex-hull and one-level feasibility criteria

### 4.1 Three or more endpoints supply no hidden escape

For a finite endpoint set E, the probability laws satisfying ∫n=p form
a polytope. Its extreme points are the two-point laws supported on
some a<p<b in E (and δ_p if p were allowed). Their masses are

\[
 \nu_{a,b}=\frac{b-p}{b-a}\delta_a+\frac{p-a}{b-a}\delta_b.
\]

For completeness, there is a constructive decomposition. The lower
and upper endpoint deviation measures have equal mass

\[
 D=\sum_{a<p}\nu(a)(p-a)=\sum_{b>p}\nu(b)(b-p).
\]

Choose any coupling β_ab of those deviation measures. Then

\[
 \theta_{ab}=\frac{\beta_{ab}(b-a)}{(p-a)(b-p)}
\]

are nonnegative, sum to 1, and give ν=Σθ_ab ν_ab. Thus the complete
moment-vector region is exactly the convex hull of these two-point
vectors. A three-endpoint cell is already in that hull, not a new
kind of moment direction. The construction also extends to integrable
countable laws; apply Tonelli to the nonnegative coefficients.

For a finite family of symmetric cells, the exact two-level conic
criterion for a positive target (t_k,t_l) is

\[
 \min_{d\in D}\frac{g_l(d/p)}{g_k(d/p)}
 \le\frac{t_l}{t_k}\le
 \max_{d\in D}\frac{g_l(d/p)}{g_k(d/p)}.
\]

Every intermediate slope is obtained by two nonnegative generators.
The convex, normalized criterion is target membership in the convex
hull of the vectors, not just the slope interval. In any number of
levels it is exactly the corresponding finite convex-hull/cone
membership problem; the separator above decides the proposed target
without solving it numerically.

### 4.2 One-level symmetric matching is sometimes feasible

Let D_p={1≤d<p: p+d is composite}, for an odd prime p. The old-monoid
condition on p−d is automatic. The set is nonempty, its minimum is 1,
and its maximum is

\[
 d_{\max}=
 \begin{cases}p-1,&2p-1\text{ composite},\\p-2,&2p-1\text{ prime}.
 \end{cases}
\]

The second case follows because 2p−2 is an old-generated composite.
There is no barycentric old-generated cell at p=2: the old monoid is
only {1}.

Since g_k is strictly increasing in u, a normalized weighting matches
one level exactly iff

\[
 g_k(1/p)\le1\le g_k(d_{\max}/p).
 \tag{4}
\]

When strict on each side, two radii suffice, with interpolation weight
(1−g_min)/(g_max−g_min) on the maximal radius. An unnormalized positive
weighting can always match a single level whenever a cell exists: use
one cell and coefficient 1/g_k.

For k=1, the exact threshold g_1(u)≥1 is

\[
 u^2\ge\frac{111-\sqrt{33}}{128}.
\]

The first feasible prime is 11. Among primes below 23, exactly 11,13,17
are feasible; p=19 fails even though p=17 succeeds. Every prime p≥23
is feasible, because d_max/p≥1−2/p and the inequality is already
strict at p=23. Thus one-level feasibility is not monotone in the
small-prime range.

For k=2 the threshold is u²≥1/2; for k=4 it is
u²≥(5−√17)/4. In both cases the first feasible prime is 5 and every
prime p≥5 is feasible. For larger k, do not omit the left inequality
in (4): the minimum defect can itself exceed 1.

For arbitrary finite old endpoint sets, the exact one-level minimum
is the chord value from the nearest endpoint below p and the nearest
one above p; the maximum is the chord from the extreme endpoints.
This follows by convexity of n↦n^{-k/2}, or from the two-point hull.
For the whole unbounded old monoid at p≥3, the minimum comes from
p−1,p+1, and the supremum of m_k is p^{k/2}−1, approached by laws on
1 and arbitrarily large powers of 2. The supremum is not attained.
Hence unrestricted-endpoint one-level normalized matching is feasible
iff g_k(1/p)≤1<p^{k/2}−1. This differs from the symmetric-radius test.

### 4.3 Level-dependent alternatives

Allowing a different λ^(k) at every level defeats the common-cone
obstruction: unnormalized one-level amplitudes can be matched
independently. Normalized weights can do so exactly when each separate
hull test (4) holds (or its arbitrary-endpoint counterpart).

There is a stronger all-level obstruction even after allowing a different
normalized law at every level and arbitrarily many unbounded old
endpoints. For p≥3, the old monoid omits p and contains p−1 and p+1.
For convex f, the affine line through (p−1,f(p−1)), (p+1,f(p+1)) lies
below f at every admissible integer outside that open interval. Hence
barycentricity gives

\[
 E f(N)\ge\tfrac12[f(p-1)+f(p+1)].
\]

For f(n)=n^(−k/2), every admissible m_k is therefore at least
g_k(1/p), which tends to infinity as k→∞. For example, the lower bound
\(g_k(1/p)\ge\tfrac12[p/(p-1)]^{k/2}-1\) is already greater than 1
when \(k>2\log4/\log[p/(p-1)]\). No sequence of normalized,
level-dependent old-monoid barycentric laws matches the entire tower.
This conclusion does not apply to independent conic rescalings.

Scalar feasibility is
not yet a single positive operator, functor, martingale dilation, or
Gram representation. Its compatibility with multiplication, the
logarithmic derivative, and physical knots k log p is unpaid.

In particular amplitude matching alone cannot move an endpoint knot
log n to log p. A proposed exact representation of D_p or h_p must
also match its distributional second derivative and its sign. The
Round002 tower Gram and divergent linear compensation are unchanged.

## 5. Weighted deletion of forbidden radii: retain the singular endpoint

Write C=√2−1 and

\[
 F_p=\sum_{1\le d<p}H^{(1)}_{p,d},\quad
 N_p=\pi(2p)-\pi(p),\quad
 B_p=\sum_{p<q<2p}H^{(1)}_{p,q-p}.
\]

Elementary decreasing-sum bounds give F_p=C√p+O(1). The exact retained
sum is F_p−B_p and its number of radii is p−1−N_p.

### 5.1 What the qualitative PNT alone pays for

The endpoint singularity is (2p−q)^(-1/2), not q^(-1/2). If the omitted
integers m=2p−q form any set of N_p distinct positive integers, then

\[
 \sum_{q}(2p-q)^{-1/2}
 \le\sum_{m=1}^{N_p}m^{-1/2}\le2\sqrt{N_p}.
\]

Also Σ_q q^(-1/2)≤N_p/√p. Positivity of each defect gives

\[
 0\le B_p\le\sqrt{N_p}+\frac{N_p}{2\sqrt p}.
\]

The qualitative PNT supplies N_p=O(p/log p). Therefore

\[
 B_p=O\!\left(\sqrt{p/\log p}\right),\qquad
 \frac{F_p-B_p}{p-1-N_p}
 =\frac{C+O((\log p)^{-1/2})}{\sqrt p}.
 \tag{5}
\]

This already proves the claimed leading critical-scale asymptotic for
the actual old-generated midpoint average. It needs no short-interval
prime theorem, RH, or hidden tail estimate.

A formal invocation of only π(x)∼x/log x does not give the sharper
relative O(1/log p) deletion rate. For example, a hypothetical
prime-like set may add clusters of length p_j/(log p_j)^a near 2p_j,
where 1<a<2 and p_j grow sufficiently rapidly. These are o(p_j/log p_j)
perturbations of its counting function, so preserve its PNT, but their
endpoint weighted contribution is of size √p_j/(log p_j)^(a/2), larger
than √p_j/log p_j. The clusters may be restricted to odd integers and
still have this effect. This is a logical countermodel to that
*inference*, not a statement that actual primes have these clusters.

### 5.2 The sharper bound is valid with an explicit extra theorem

A standard unconditional short-interval sieve bound is sufficient:

\[
 \pi(x+y)-\pi(x)\le C_0\frac y{\log y}\quad(y>1)
 \tag{BT}
\]

with an absolute constant. The classical Montgomery–Vaughan result
allows C_0=2. A directly accessible primary source gives a stronger
version: Tomohiro Yamada, *Explicit improvements of the Brun–Titchmarsh
theorem for arbitrary intervals*, arXiv:2312.16090v1, Theorem 2, pp. 3,
https://arxiv.org/pdf/2312.16090. Taking modulus 1 gives denominator
log y+0.8601. Only the weaker bound (BT) is used here; no finite
computational constant is needed for the argument.

Let A_p(y)=#{q prime: 2p−y≤q<2p}. Endpoint conventions change this by
at most one and have no effect on the estimates. For y≥√p, (BT) gives
A_p(y)≪y/log p. For y≤√p use the all-integer bound. Partial summation
therefore yields

\[
 \sum_q(2p-q)^{-1/2}
 \ll p^{1/4}+
 \frac{\sqrt p}{\log p}
 +\frac1{\log p}\int_{\sqrt p}^p y^{-1/2}\,dy
 \ll\frac{\sqrt p}{\log p}.
\]

Thus B_p=O(√p/log p), proving the sharper omitted-contribution claim
with its actual dependency exposed.

One can sharpen the result further without an RH-strength estimate.
The qualitative PNT controls every fixed truncated interval
q/p∈[1,2−ε]. On it, ordinary partial summation gives the limiting
weighted integral. The preceding sieve bound gives a uniform tail
bound O(√ε √p/log p)+O(p^(1/4)), after first taking p large. Letting
ε↓0 proves

\[
 B_p\sim C\frac{\sqrt p}{\log p}.
 \tag{6}
\]

Indeed the limiting integral is

\[
 \int_1^2\left\{\tfrac12[(2-v)^{-1/2}+v^{-1/2}]-1\right\}dv
 =\sqrt2-1=C.
\]

Combining N_p∼p/log p, (6), and F_p=C√p+O(1), the first-order deletion
and denominator effects cancel:

\[
 \frac{F_p-B_p}{p-1-N_p}
 =\frac C{\sqrt p}+o\!\left(\frac1{\sqrt p\log p}\right).
\]

This stronger asymptotic is still only a size statement. It does not
repair the two-level moment-cone obstruction in sections 2–3.

## 6. Verdict and adversarial boundary

- **PROVED IN THIS AUDIT:** common positive barycentric defect weights
  cannot reproduce any two distinct inverse-power tower amplitudes;
  symmetric and bounded-support geometry give stronger exact dual
  separators.
- **PROVED IN THIS AUDIT:** exact finite hull characterization,
  one-level feasibility criteria, and the p=19 normalized midpoint
  failure after the p=17 success.
- **PROVED FROM QUALITATIVE PNT:** deletion preserves the leading
  critical-half-density constant, with the elementary rate (5).
- **PROVED USING AN ADDITIONAL PRIMARY-SOURCE SIEVE THEOREM:** the
  sharper deletion estimate and (6). The singular endpoint must not
  be dismissed by a smooth-weight PNT slogan.
- **NOT ESTABLISHED:** compatibility of level-dependent amplitudes,
  signed primitive extraction, tensor/composite Gram constructions,
  exact Suzuki knot matching, or positivity of the Suzuki reserve.

The separator survives endpoint duplication, deletion, relocation,
old-monoid permutation, and extra endpoints whenever the individual
cells remain positive and barycentric. That robustness marks its
scope: it rejects a whole proposed generic positive moment mechanism,
not an arithmetic RH statement. Allowing negative coefficients or
changing the observable leaves this theorem's hypotheses; it does
not refute the theorem.

Verification: `python -m unittest tests.test_r3_moment_adversary` checks
exact rational identities, exact symbolic remainder factorizations,
and Arb-certified finite threshold signs. The universal inequalities
and asymptotics are proved above, not inferred from those samples.

## 7. Second bearing: the full logarithmic weight does not evade the separator

This section audits a stronger statement separately from the pure
inverse-power theorem. Define the exact weight function

\[
 w_k(n)=(\log n)n^{-k/2},
\]

and, for the same barycentric probability law ν on old-generated
positive integers N with EN=p>1, define

\[
 \widetilde m_k
 =\frac{E w_k(N)-w_k(p)}{w_k(p)}
 =E\!\left[\frac{\log N}{\log p}(p/N)^{k/2}\right]-1.
\]

Unlike the pure inverse-power defect, an individual logarithmic-weight
defect can be negative. No assertion that w_k is globally convex is
needed or valid here.

**Theorem.** For every 0<k<l and every such law,

\[
 \boxed{\widetilde m_l>\frac lk\widetilde m_k.}
 \tag{7}
\]

**Proof.** Put a=(log N)/(log p), Z=(p/N)^(k/2), and r=l/k>1.
Because N≥1, a≥0. The positive-integer lower bound is a load-bearing
hypothesis: allowing arbitrary N<1 would permit negative a and would
invalidate this proof. Barycentricity and strict logarithmic Jensen
give 0≤Ea<1. Strictness holds because an old-monoid law cannot be δ_p;
indeed p is not an old-generated integer. All expectations exist:
log N≤N and EN=p, while (log N)N^(−s) is bounded on [1,∞) for every
s>0. In particular, unbounded old-generated support is permitted.

An exact algebraic identity is

\[
 \widetilde m_l-r\widetilde m_k
 =E\{a[Z^r-1-r(Z-1)]\}+(r-1)(1-Ea).
 \tag{8}
\]

The first term is nonnegative by the scalar power tangent inequality;
the second is strictly positive. This proves (7), regardless of the
individual signs of the two defects.

Consequently the same linear functional v_l−(l/k)v_k is nonnegative
on every finite positive conic mixture of these *full logarithmic*
defect vectors, and on its closure. At the target (1,1), required by
matching the new tower amplitudes with common positive defect weights,
it equals 1−l/k<0. **Including the log n jet does not rescue the common
positive barycentric defect constructor.** No absolute-convergence
loophole exists for proposed finite-vector limits: every finite partial
cone sum lies in a closed half-space excluding the target.

Here is an exact old-support witness exercising the negative-defect
regime. At p=3 take ν=(δ_2+δ_4)/2, and put a_0=log2/log3. For levels
k=2 and l=4,

\[
 \widetilde m_2=\tfrac32a_0-1<0,\qquad
 \widetilde m_4=\tfrac{27}{16}a_0-1,
\]
\[
 \widetilde m_4-2\widetilde m_2
 =1-\tfrac{21}{16}a_0>\tfrac18>0.
\]

The certified bound a_0<2/3 follows exactly from 2^3<3^2, so the
strict signs do not depend on floating-point evidence. Identity (8)
has first term 3a_0/16 and second term 1−3a_0/2 here.

Keep the targets distinct. The defect-cone task is Σλ_c m_c=(1,1).
Direct normalized reconstruction E w_k(N)=w_k(p) instead asks for
m=(0,0). For an individual nontrivial barycentric probability law,
(7) already excludes direct reconstruction at two levels. Positive
reconstruction without a barycenter constraint is a different moment
problem; the present argument does not claim its finite-level
impossibility. Neither assertion identifies the Suzuki physical
knots, proves primitive-extraction positivity, nor removes the exact
linear compensation in the Round002 tower Gram.


## 8. Third bearing: three levels already obstruct positive reconstruction

This strengthens the separate whole-tower support obstruction to a finite
certificate. It concerns **direct weight reconstruction**, not the defect
cone in sections 2 and 7.

**Theorem.** Let p be a prime, k>0, h>0, and let c_n≥0 be coefficients on positive
integers. If

\[
 \sum_n c_n(\log n)n^{-j/2}=(\log p)p^{-j/2}
 \quad\text{at }j=k,k+h,k+2h,
 \tag{9}
\]

then every active n≥2 equals p. In particular, (9) is impossible on the
old-prime monoid. Finite and countable supports are both covered; the
finite first sum in (9) supplies the required normalization. No
barycenter condition on the n's is needed.

**Proof.** Put a_n=c_n log n≥0, z_n=n^(-1/2), r=p^(-1/2), and
C=log p. The n=1 term is invisible. The positive weights

\[
 \rho_n=\frac{a_n z_n^k}{C r^k}
\]

sum to 1 by the first equation. The next two equations give

\[
 E_\rho(z^h)=r^h,\qquad E_\rho(z^{2h})=r^{2h}.
\]

Thus Var_ρ(z^h)=0. Every active z_n^h equals r^h, hence n=p, since
h>0. If p is allowed, its coefficient is necessarily c_p=1; the
coefficient of n=1 remains unobservable. If p is prohibited by old
support, there is a contradiction.

Equivalently the 2×2 Hankel matrix of these three equally spaced
moments has determinant zero. A positive mixture of distinct active
nodes has strictly positive determinant. There is no analytic
continuation, limiting tower, fitted matrix factorization, or assumed
kernel positivity in this argument.

The support gap also separates the *closed* positive moment cone. Put

\[
 \delta=p^{-h/2}-(p+1)^{-h/2}>0.
\]

For integers n≠p, monotonicity and convexity of n↦n^(-h/2) imply
|n^(-h/2)−p^(-h/2)|≥δ. (For n≤p−1 the one-step difference is larger
than the corresponding difference above p.) Thus, writing M_j=Σa_n
z_n^j, every old-support moment vector satisfies

\[
 M_{k+2h}-2r^hM_{k+h}+(r^{2h}-\delta^2)M_k\ge0.
 \tag{10}
\]

At the target in (9), the same functional equals −δ² C r^k<0. This
excludes arbitrary limits of positive old-support moment vectors, not
only exact finite combinations.

Two levels alone do not give this obstruction without barycentricity.
An exact rational control is p=3 with old endpoints 2 and 4. Remove
the common factor C=log3 and choose coefficients a_2/C=2/9,
a_4/C=8/9. At even levels 2,4,6 their normalized moments are

\[
 M_2/C=\tfrac13,\qquad M_4/C=\tfrac19,\qquad
 M_6/C=\tfrac1{24}>\tfrac1{27}.
\]

The first two match the target exactly; the third cannot. The tilted
law has masses 1/3,2/3 at x=1/2,1/4, respectively. Its variance is
1/72, and the corresponding Hankel determinant is 1/648. The
underlying c_n=a_n/log n are positive, so this is a legitimate direct
weight reconstruction control. It is not required to be additive
barycentric, and in fact no such condition was used.
