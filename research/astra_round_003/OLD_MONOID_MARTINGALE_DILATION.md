# Old-monoid midpoint dilation: abundance proved, spectral identification unpaid

## 1. Exact saturation, including the first prime

Let p be prime, let M_<p be the multiplicative monoid of primes strictly
below p including its unit, and let D_p consist of radii 1<=d<p whose
two endpoints p-d,p+d belong to M_<p. The left endpoint is automatically
old-generated. The right endpoint is less than 2p. If composite, none of
its prime factors can be >=p: a proper cofactor would make it >=2p.
If prime, it is not old-generated. Consequently

\[
 |D_p|=(p-1)-[\pi(2p-1)-\pi(p)].
\]

For p=2, M_<p={1} and D_p is empty. For every odd prime p, radius 1
works: p-1 and p+1 are even, with all prime factors below p. The ordinary
PNT implies the bad count is `(1+o(1))p/log p`, so `|D_p|/(p-1)->1`.
This uses no RH-strength prime error term. No claim that every sufficiently
large prime has a growing local gap is needed or made.

## 2. Exact positive cells, and their coordinate cost

For d in D_p, `nu_d=(delta_(p-d)+delta_(p+d))/2` has total mass one and
mean p. Jensen gives `delta_p <=cx nu_d`. Every positive normalized
mixture remains barycentric and old-generated. For a finite collection
of arbitrary old endpoints a<p<b the two-point mean-preserving cell has
weights `(b-p)/(b-a)` and `(p-a)/(b-a)`. All finite barycentric laws on
the endpoint set are convex mixtures of these two-point cells; the explicit
deviation-mass coupling proof is in `PRIME_TOWER_MOMENT_CONE.md` and its
independent review. Thus allowing 3+ endpoints is audited, not ignored.

The additive martingale does not remain a martingale under nonlinear
coordinates. The exact midpoint log deficit is

\[
 J_{p,d}=-\tfrac12\log(1-d^2/p^2)>0.
\]

The inverse-power surplus is

\[
 H^{(k)}_{p,d}=\tfrac12[(p-d)^{-k/2}+(p+d)^{-k/2}]-p^{-k/2}>0.
\]

These are strict Jensen effects, not automatically the Suzuki event mass
or a payment of its Brownian debt. Moreover “old-generated” does not mean
smaller numerical endpoint (the right endpoint is larger), shorter program,
or lower integer-complexity defect. Those additional comparisons need their
own metric and are not assumed by the monoid theorem.

## 3. Reconstruct the critical-scale law and delete bad radii rigorously

Write C=sqrt(2)-1 and `F_p=sum_(1<=d<p) H^(1)_(p,d)`. Decreasing-sum
integral bounds give

`sum_(m=1)^(p-1) m^(-1/2)=2 sqrt(p)+O(1)`,

`sum_(n=p+1)^(2p-1) n^(-1/2)=2(sqrt(2)-1)sqrt(p)+O(p^(-1/2))`.

Subtracting `(p-1)/sqrt(p)` proves `F_p=C sqrt(p)+O(1)` and hence

\[
 \frac{1}{p-1}\sum_d H^{(1)}_{p,d}
 =\frac{C}{\sqrt p}+O(p^{-1}).
\]

Bad radii have p+d=q prime in (p,2p). Their singular contribution is
`(2p-q)^(-1/2)`; treating that weight as smooth at the upper endpoint
would be an error. Let N be the number of such primes and B their total
H contribution. Because the integers `2p-q` are distinct,

\[
0\le B\le\sqrt N+\frac{N}{2\sqrt p}.
\]

Indeed the largest sum over N distinct positive integers of m^(-1/2)
is at m=1,...,N and is at most 2sqrt(N). PNT gives N=O(p/log p), so

\[
 \boxed{\frac1{|D_p|}\sum_{d\in D_p}H^{(1)}_{p,d}
 =\frac{\sqrt2-1+O((\log p)^{-1/2})}{\sqrt p}.}
\]

This suffices for the proposed leading critical scale. Multiplication by
log p produces exactly its stated leading scale, not the coefficient one
or the remaining levels of the prime tower.

For completeness, the stronger omitted-weight rate `B=O(sqrt(p)/log p)`
requires an explicit singular-tail estimate in addition to the qualitative
PNT slogan. The classical Brun–Titchmarsh bound on arbitrary intervals
provides it: split endpoint distances at sqrt(p), use the all-integer bound
below, and `#{q in [2p-y,2p)}=O(y/log p)` above. Partial summation then
bounds the tail. PNT on fixed truncated scaled intervals plus this uniform
tail control even gives `B~C sqrt(p)/log p`; cancellation with the deleted
denominator count gives the retained mean
`C/sqrt(p)+o(1/(sqrt(p)log p))`. Full derivation and quantifiers are in
`reviews/MOMENT_ADVERSARY.md`, §5.

Primary short-interval statement inspected: Yamada,
https://arxiv.org/pdf/2312.16090v1, Theorem 2, PDF p.3, specializing its
modulus to 1. Only the weaker classical O(y/log y) consequence is needed;
none of its improved numerical constants enters our calculation. This is
a source theorem, not an independently rerun proof of the sieve theorem.

## 4. Outcome

The supply of old-state midpoint cells and their critical-scale mean are
proved. The two-level moment-cone theorem shows why that abundance is
insufficient: their nonlinear moment ratios cannot be the required tower
ratios under a common positive weighting. No amount of extra midpoint
radii alters that separating inequality. One-level scalar successes are
retained, with exact interval weights in `evidence/moment_cone.json`;
their event-location/Gram bridge remains unpaid.
