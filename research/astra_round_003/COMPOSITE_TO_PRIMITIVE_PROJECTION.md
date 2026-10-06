# Composite states and the primitive projection: an exact support barrier

**NEW LEMMA PROVED THIS ROUND (repository claim, no priority claim):**
formal Dirichlet logarithms and their logarithmic derivatives cannot create
a new prime coordinate from data supported on the monoid of older primes.
Generic positivity also does not survive that projection. These are two
separate obstructions.

## 1. Tensor states and exact connected expansion

For `n=product r^v_r`, the critical observable factors exactly:

`n^(-k/2) log n = (product r^(-k v_r/2)) (sum v_r log r)`.

For a finite set S of primes, use independent formal variables z_r and

`Z_S(z)=product_(r in S)(1-z_r)^(-1)=sum_(v>=0) product z_r^v_r`.

The logarithm is exactly `sum_r sum_(k>=1) z_r^k/k`. Therefore mixed
monomials cancel: full composite/tensor states are present in Z, while its
log contains only single-prime towers. The operator
`sum_r (log r) z_r d/dz_r` removes the 1/k and yields
`sum_(r,k) (log r) z_r^k`. This is the precise connected/primitive analogy.
It works because the partition series factors into independent geometric
factors, not because every positive partition function has positive cumulants.

Substitute `z_r=r^(-s)`. For the infinite Euler product this step is justified
by absolute convergence only for Re(s)>1. There it gives the usual three
identities for zeta, log zeta and -zeta'/zeta (DLMF §27.4,
https://dlmf.nist.gov/27.4). At s=1/2, coefficientwise formal identities
remain valid, but an infinite positive Hilbert/measure limit has not been
justified by that substitution. Analytic continuation is not such a limit.

## 2. Monoid-support theorem

Let M be any multiplicative submonoid of positive integers, including 1.
Let `a_1=1` and `a_n=0` outside M. In the formal Dirichlet algebra write

`log_* a = sum_(j>=1) (-1)^(j+1) (a-epsilon)^{*j}/j`.

At a fixed n this sum is finite: a product of j integers >=2 exceeds n
when j>log_2 n. Every factorization contributing to a coefficient in a
convolution power uses factors in M, so its product lies in M. Therefore

`supp(log_* a) subset M`.

Coefficient multiplication by log n, finite sums/products, formal inverses
of normalized series, and coefficientwise limits preserve the same support.
No sign assumption was needed. Taking `M=M_<p` excludes every p^k. Thus even
a signed formal primitive projection of old-state data cannot create the
new tower if it preserves this multiplicative grading.

This also holds in the multivariate formulation: a series independent of
z_p remains independent of z_p after logarithm and differentiation in the
existing variables. Adding a missing independent variable is new arithmetic
input, not a consequence of quotienting the old partition function.

## 3. Positive moments do not bypass support

The positive barycentric identity `p=E[N]` with old-generated N uses addition
of endpoint values. Evaluation at that mean is not a homomorphism of the
Dirichlet convolution algebra. In particular, it cannot be inserted as an
unmentioned commuting arrow between old-state tensor data and the missing
primitive coordinate. Taking a Jensen difference explicitly adds the signed
center term `-delta_p`; the new p input is already in that definition.

There is a matching event-location obstruction. Any ramp mixture located
at logarithms of old-generated integers has second-derivative distribution
supported there. The integer p^k is not in that monoid. In a compact positive
time interval those integer-log locations are locally finite; a small open
neighborhood of k log p excludes all of them. A distributional/vague limit
of measures supported on this fixed closed set still vanishes on tests in
that neighborhood. It cannot equal a tower atom there. The only origin
atom from a |t| repair is at zero and cannot repair this missing positive-time
support. Signed coefficients do not change this local test-function argument.

Hence matching one nonlinear scalar moment cannot establish equality of
the tower ramp, accelerant, or screw kernel. Exact locations and weights
must both be reconstructed by a specified map.

## 4. Positivity failure, independently of support

Take the positive finite partition series `Z=1+z_2`. Then

`log Z=z_2-z_2^2/2+z_2^3/3-...`.

Its second connected coefficient is negative; applying the logarithmic
derivative produces a negative coefficient at 4. The same failure appears
in probability as a Bernoulli law whose logarithm is not a compound-Poisson
exponent. No probability terminology is needed for the exact coefficient
counterexample. More generally a positive correlated tensor polynomial can
have signed mixed connected coefficients. For example a_2=2, a_3=1, a_6=1
gives `(log_* a)_6=1-2=-1`.

Conversely the true finite Euler partition does recover the positive tower
coefficients exactly. This positive control isolates what is load-bearing:
the multiplicative/geometric factorization. It does not generate a new
factor from earlier factors. `tests/test_primitive_projection.py` reconstructs
all coefficients through 256 using rational arithmetic and checks both
positive controls and mutations.

## 5. Surviving boundary

This kills the class “positive old-state tensor data followed only by the
usual grading-preserving primitive/logarithmic projection creates p's
Suzuki tower.” It does not exclude an explicitly non-grading-preserving
operator coupling addition, finite places and infinity. Such an operator
must supply the new spectral locations, preserve the relevant positive
pairing, and pay the common-mode cost. None has been constructed this round.
