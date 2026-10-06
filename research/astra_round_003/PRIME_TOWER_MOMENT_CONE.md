# Prime-tower moment cones: exact feasible pieces and separating theorems

**Result:** the proposed common positive old-state curvature mechanism is
refuted already by two tower levels. Three equally spaced levels refute
even positive direct reconstruction without a barycentric constraint.
The logarithmic weight does not rescue the barycentric construction.
These are scoped moment-cone theorems, not a proof or strict reduction of RH.

## 1. Exact target and normalization

Fix prime p and k>0. A cell nu is a probability law on positive old-generated
integers N with E N=p. The original midpoint simplex is a subset of these
cells. Define

\[
 m_k(\nu)=p^{k/2}(E N^{-k/2}-p^{-k/2}).
\]

To reproduce the tower weight `w_k(p)=log(p)p^(-k/2)` using the indicated
inverse-power curvature observables and common nonnegative coefficients
lambda_c, one must solve `sum_c lambda_c m_k(nu_c)=1` at every chosen
level. The cone allows any finite total coefficient, not just sum lambda=1.
The logarithmic factor log p cancels from this necessary amplitude system.
It is necessary only for this declared curvature implementation; no claim
that all possible Gram constructions must solve it is made.

## 2. A dual functional excludes two levels

For 0<k<l put r=l/k and Z=(p/N)^(k/2). Convexity and E N=p give E Z>1
for a nontrivial cell. The scalar tangent inequality `z^r>=1+r(z-1)` gives

\[
 \boxed{m_l-rm_k=E[Z^r-1-r(Z-1)]>0.}
\]

Strictness follows because old support excludes N=p. Thus the whole positive
cone, including its finite-moment limits, lies in `v_l-rv_k>=0`.
The target (1,1) gives `1-r<0`. No common positive conic or convex weights
can match it. Three or more endpoints, relocation within old support,
and extra midpoint radii cannot evade this theorem.

For symmetric cells with u=d/p, the normalized moments are

`g_k(u)=((1-u)^(-k/2)+(1+u)^(-k/2))/2-1`.

The even binomial coefficient expansion proves the sharper sharp bound

\[
 g_l(u)>\frac{l(l+2)}{k(k+2)}g_k(u),\qquad 0<u<1.
\]

Coefficient ratios strictly increase with series index; the first ratio is
the displayed constant and equality is approached only as u tends to zero.
In particular `g_2>(8/3)g_1` and `g_4>3g_2`. For arbitrary barycentric
endpoints below 2p, a separate tangent-remainder comparison gives
`m_2>(1+sqrt(2))m_1`. Proofs and exact algebra are independently reconstructed
in `reviews/MOMENT_ADVERSARY.md`, §§2–3. No numerical optimization is used.

## 3. Including the actual log N factor still fails

A possible escape is to use the full observable
`w_k(N)=log(N)N^(-k/2)` rather than freezing log p. Define its normalized
Jensen difference

`mtilde_k=E[(log N/log p)(p/N)^(k/2)]-1`.

Put a=log N/log p>=0. Strict concavity of log and E N=p imply E a<1.
For r=l/k and the same Z,

\[
\boxed{\widetilde m_l-r\widetilde m_k
=E[a(Z^r-1-r(Z-1))]+(r-1)(1-Ea)>0.}
\]

All integrals exist: log N<=N, and log N times a negative power of N is
bounded for N>=1. This proof does not require individual mtilde_k positive;
indeed they need not be. The same separating half-space rejects target
(1,1) for any common positive conic weighting. It also rejects direct
barycentric reconstruction at two levels, which would require the vector
(0,0) for a nontrivial probability law. The independent audit includes an
exact negative-defect control at p=3, endpoints 2 and 4.

## 4. Three moments force the missing prime, without barycentricity

There is a distinct direct-reconstruction theorem. Suppose c_n>=0 is a
countable old-support family and, for three equally spaced positive levels
k,k+h,k+2h, h>0,

\[
 \sum_n c_n(\log n)n^{-j/2}=(\log p)p^{-j/2}.
\]

Let z_n=n^(-1/2), r=p^(-1/2), and normalize the positive masses
`c_n(log n) z_n^k` by `(log p)r^k`. They form a probability law; the next
two equalities give `E z_n^h=r^h` and `E z_n^(2h)=r^(2h)`. Its variance
is zero, so every active n equals p. This contradicts old support. The unit
n=1 has zero logarithmic mass and is invisible. First-level finiteness and
the two supplied moments justify the countable argument directly.

Equivalently, the target Hankel matrix has rank one:
`a_k a_(k+2h)-a_(k+h)^2=0`. Equality in positive moment log-convexity forces
a single endpoint. This kills positive direct old-weight reconstruction
with common coefficients even if barycentricity is dropped. It does not
apply to signed cross terms or independent coefficients at each level.

The obstruction even separates the **closed** moment cone. Let
`z0=p^(-h/2)` and `delta=z0-(p+1)^(-h/2)>0`. Monotonicity and convexity
of x^(-h/2) imply `|n^(-h/2)-z0|>=delta` at every integer n!=p.
For moments M_j of any positive old-support coefficients,

`M_(k+2h)-2z0 M_(k+h)+(z0^2-delta^2) M_k>=0`.

The target geometric moments give a strictly negative value
`-delta^2(log p)p^(-k/2)`. Thus approximate fitting cannot converge to all
three target moments while retaining that support and positivity. For an
exact sharpness control, old endpoints 2 and 4 at p=3 with logarithmic
masses proportional to 2/9 and 8/9 match levels 2 and 4; level 6 is 1/24
instead of 1/27 before the common log(3) factor. The third level matters.

## 5. Exact moment regions and extremal measures

For a finite radius set D, the normalized attainable m-vector at m requested
levels is exactly `conv{(g_k(d/p))_k:d in D}`; the unnormalized attainable
set is its nonnegative cone. This is an equality, by the definitions of a
positive mixture, not an approximate LP fit. The two-level cone has precisely
the slopes between the smallest and largest generator slope. Those slopes
occur at the smallest and largest radius: the coefficient-ratio expansion
shows `g_l(u)/g_k(u)` strictly increasing in u.

Caratheodory bounds here have elementary proofs: if more than m+1 positive
weights occur in a convex representation in R^m, affine dependence lets
one vary them preserving the vector and sum until a weight becomes zero.
Repeat. For a conic representation, linear dependence gives at most m
generators. No cone separation algorithm needs to be trusted.

For arbitrary finite old endpoint sets, every barycentric law is a convex
mixture of two-point cells at a<p<b. To prove it, couple the equal deviation
masses `nu(a)(p-a)` and `nu(b)(b-p)` by beta_ab, and assign cell coefficient
`beta_ab(b-a)/[(p-a)(b-p)]`. These coefficients reconstruct nu and sum to one.
Thus no unexamined 3+endpoint escape remains. Direct endpoint representations
matching m moments plus mass and barycenter need at most m+2 endpoints, by
the same linear-dependence elimination. With unrestricted old integer support,
the inequalities above remain valid even when finite polytope compactness is
unavailable.

## 6. One-level successes and level-dependent failure boundaries

For an odd prime, min D_p=1 and max D_p is p-1 if 2p-1 is composite,
otherwise p-2. Since g_k increases with u, normalized one-level matching is
possible exactly when

`g_k(1/p)<=1<=g_k(max D_p/p)`.

If both inequalities are strict, the explicit weight on the largest radius
is `(1-g_min)/(g_max-g_min)`, with the remaining mass on radius 1. This is
a genuine positive scalar amplitude construction. It is not yet an exact
portion of D_p as a function of time, because the endpoints have different
event locations.

For k=1 the threshold is
`u^2>=(111-sqrt(33))/128`. The first success is p=11; below 23 exactly
11,13,17 succeed, and p=19 fails. Every prime p>=23 succeeds because
u_max>=1-2/p and the threshold already holds at 23. The latter is an
analytic monotonic bound, not extrapolation from checked primes.

Allowing a different normalized law at each level still cannot match the
entire **pure inverse-power** tower. For any convex f on positive integers
omitting p, its chord through p-1,p+1 lies below f on every allowed integer.
For p>=3 both neighbors are old-generated, so

`E f(N)>= [f(p-1)+f(p+1)]/2`.

Consequently every m_k>=g_k(1/p), which tends to infinity. Already
`k>2 log(4)/log(p/(p-1))` makes its elementary lower bound exceed 1.
At p=2 no barycentric old-state law exists at all. This all-level conclusion
does not extend automatically to the log-weighted observable, whose unit
has zero mass, and is not asserted for it.

With independently chosen **unnormalized** positive coefficients at each
level, any single positive inverse-power defect can be rescaled to the
target. This is scalar feasibility with no shared marginal or bounded cost;
it is not an RH proof and does not contradict the common-cone no-go.

## 7. Connection and limit of the result

The old-state average has the correct first-level asymptotic scale; its
moment ratios do not have the exact tower shape. The first unpaid edge
for every surviving alternative is a specified positive operator/primitive
map that reconstructs **locations as well as amplitudes** and keeps the
Brownian lift uniformly bounded. The ordinary Dirichlet primitive map is
separately refuted by its support theorem. The results therefore eliminate
concrete constructions, while leaving nonlocal signed/compressed couplings
open under their own positivity obligation.

Tests use exact rational even-level identities, symbolic factorizations,
Arb one-level thresholds, log-jet counter-regimes, and moment-preserving
endpoint mutations. Raw finite certificates: `evidence/moment_cone.json`.
