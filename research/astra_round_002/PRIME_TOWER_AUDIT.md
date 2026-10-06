# Prime towers: a positive arithmetic Gram block and its exact cost

**Result:** grouping each full tower `p,p^2,p^3,...` yields an explicit,
noncircular positive Gram construction after a sharp linear correction.
The uncorrected tower is indefinite. Summing the corrected towers with
positive weights creates a divergent correction; its normalized limit is
`|t|`, and the arithmetic residual disappears. Full towers also acquire
infinite first moments in the service coordinate. These statements leave
coupled, explicitly renormalized constructions open. RH is not proved.

“Tower” here means all powers `p^k`, `k>=1`. Literal iterated exponentials
`p,p^p,p^(p^p),...` omit almost all Euler-factor events and do not give an
exact regrouping. The usual Euler product and its prime-power expansion
can be checked against [DLMF 27.4](https://dlmf.nist.gov/27.4) and the
Euler-factor discussion in [Nakamura–Suzuki, section 1](https://arxiv.org/html/2306.08317v1).
The identities below are derived directly; no zero ordinates enter them.

## 1. Exact block, moments, and geometric remainder

Fix a prime `p`; write `ell=log p`, `r=p^(-1/2) in(0,1)`. Its physical
event measure and even ramp are

\[
 \mu_p=\ell\sum_{k\ge1}r^k\delta_{k\ell},\qquad
 h_p(t)=\ell\sum_{k\ge1}r^k(|t|-k\ell)_+.
\]

Every value of `h_p` uses finitely many active powers. Its total mass and
first physical moment are finite:

\[
 M_p=\frac{\ell r}{1-r},\qquad
 H_p=\frac{\ell^2r}{(1-r)^2}.
\]

For `K=floor(|t|/ell)`, endpoint equality being harmless, put

\[
 M_{p,K}=\ell\frac{r(1-r^K)}{1-r},\qquad
 H_{p,K}=\ell^2\frac{r[1-(K+1)r^K+Kr^{K+1}]}{(1-r)^2}.
\]

Then `h_p(t)=|t| M_(p,K)-H_(p,K)`. The exact positive remainder in its
large-time affine asymptotic is

\[
 h_p(t)=M_p|t|-H_p+R_p(t),
\]
\[
 R_p(t)=\ell r^{K+1}
 \left[\frac{(K+1)\ell-|t|}{1-r}
       +\frac{\ell r}{(1-r)^2}\right]\ge0.
\]

This gives exact tower sums and geometric error control without estimates
for prime counting or RH. Regrouping a finite event prefix into its
truncated towers leaves `P`, `S`, `H`, the reserve, and every transport
cost unchanged. Existing actual-prime counterexamples therefore survive
that regrouping.

## 2. A genuine positive arithmetic Gram construction

Define the repaired block

\[
 \boxed{D_p(t)=M_p|t|-h_p(t)
       =\ell\sum_{k\ge1}r^k\min(|t|,k\ell).}
\]

For `a>0`, let `I_(t,a)=1_[t,t+a]` in `L^2(R)`. Interval-overlap
geometry gives

\[
 \frac12\|I_{t,a}-I_{0,a}\|_2^2=\min(|t|,a).
\]

In the independently positive Hilbert space `direct_sum_(k>=1)L^2(R)`,
set

\[
 V_p(t)_k=\sqrt{\ell r^k}\,(I_{t,k\ell}-I_{0,k\ell}).
\]

The squared norm sum converges, bounded by `2M_p|t|`. Translation of
intervals is unitary, so

\[
 D_p(t)=\tfrac12\|V_p(t)\|^2,\qquad
 \|V_p(t)-V_p(u)\|^2=2D_p(t-u),
\]
\[
 \boxed{\langle V_p(t),V_p(u)\rangle
 =D_p(t)+D_p(u)-D_p(t-u).}
\]

Thus `D_p` is CND, proved directly from prime arithmetic and interval
geometry. No kernel was factorized after assuming its positivity.

**Sharpness of the linear correction.** For real `c`,

\[
 c|t|-h_p(t)\text{ is CND}\quad\Longleftrightarrow\quad c\ge M_p.
\]

Sufficiency follows from the Gram construction and CND of `|t|`.
If `c<M_p`, the exact asymptotic in section 1 makes the function tend
to minus infinity, contradicting CND nonnegativity. The correction
cannot be made cheaper within this linear-repair class.

## 3. Tower Fourier sum and positive Lévy measure

Use `hat f(x)=integral exp(-itx)f(t)dt`. Since
`h_p''=ell sum_(k>=1)r^k(delta_(k ell)+delta_(-k ell))`,

\[
 \frac1{2\pi}\widehat{h_p''}(x)
 =\frac\ell\pi\sum_{k\ge1}r^k\cos(k\ell x)
 =\frac\ell\pi\frac{r\cos\theta-r^2}{1-2r\cos\theta+r^2},
 \qquad\theta=\ell x.
\]

Absolute uniform convergence justifies the geometric sum. The density
is positive at `theta=0` and negative at `theta=pi`. Thus it is not
a positive spectral measure. There is also an immediate finite witness:
at `t=3ell/4`, `u=-3ell/4`, the anchored kernel of `h_p` is

\[
 \begin{pmatrix}0&-\ell^2r/2\\-\ell^2r/2&0\end{pmatrix}.
\]

Only the first tower event is active in the off-diagonal entry. Both
signs of this matrix are indefinite, so neither `h_p` nor `-h_p` is CND.
Completing infinitely many events in one tower does not fix that defect.

The repaired block has the explicit positive, finite Lévy measure

\[
 \boxed{\nu_p(dx)=\frac\ell{\pi x^2}
 \frac{r(1+r)(1-\cos(\ell x))}
 {(1-r)(1-2r\cos(\ell x)+r^2)}\,dx,}
\]

with the removable density value at zero interpreted by continuity.
Indeed this is
`sum_(k>=1) ell r^k (1-cos(k ell x))/(pi x^2) dx`, and

\[
 D_p(t)=\int(1-\cos(tx))\nu_p(dx),\qquad
 \nu_p(\mathbb R)=\ell\sum_{k\ge1}r^k(k\ell)=H_p<\infty.
\]

The integral identity follows from
`integral (1-cos(ax))/(pi x^2) dx=|a|`, or from the interval Gram
calculation. Thus each repaired tower is a zero-free arithmetic
**compound Poisson exponent**, not just an abstract positive kernel.

For completeness, the opposite sign also has a sharp linear repair:

\[
 h_p(t)+c|t|\text{ is CND}
 \quad\Longleftrightarrow\quad c\ge\frac{\ell r}{1+r}.
\]

The cosine sum has minimum `-r/(1+r)`. At equality its repaired
spectral density is proportional to
`r(1-r)(1+cos theta)/[(1+r)(1-2r cos theta+r^2)]`, which is
nonnegative. A smaller correction leaves negative density on an open
set. This is a spectral control; the actual prime term in `Psi` has
the `-h_p` sign and requires the larger correction `M_p`.

## 4. Positive aggregation has a Cauchy limit and loses the residual

For primes `p<=X`, let

\[
 M_X=\sum_{p\le X}M_p,\qquad D_X=\sum_{p\le X}D_p.
\]

Each `D_X` is manifestly CND. But `M_X→infinity`: for every prime,
`M_p=log p/(sqrt p-1)>1/p`, and `sum_p 1/p` diverges. One elementary
proof of the latter is that convergence would bound
`product_(p<=X)(1-1/p)^(-1)`, whereas its positive expansion contains
`sum_(n<=X)1/n`, which is unbounded.

For every fixed `T`, once `X>=exp(T)`, all prime events visible in
`[-T,T]` belong to the included towers. Therefore, exactly on that window,

\[
 D_X(t)=M_X|t|-P(|t|),\qquad
 \sup_{|t|\le T}\left|\frac{D_X(t)}{M_X}-|t|\right|
 \le\frac{P(T)}{M_X}\longrightarrow0.
\]

Thus the manifestly positive normalized closure is `|t|`, whose
characteristic function is the symmetric Cauchy function `exp(-|t|)`.
As a variogram the same `|t|` is Brownian; those are two different uses
of the argument coordinate. The exact arithmetic correction
`P(t)/M_X` vanishes in this limit.

Keeping the complete arithmetic residual instead requires

\[
 \Psi(t)=A(t)-M_X|t|+D_X(t)\quad(|t|\le\log X).
\]

The negative linear renormalization diverges. Positive-CND closure does
not survive subtraction of that term. At every nonzero fixed `t`, the
positive sum `sum_p D_p(t)` itself diverges: for `p>exp(|t|)` one has
`D_p(t)=M_p|t|`. Hence an unrenormalized Hilbert direct sum over all
primes cannot be the desired finite norm for `Psi`.

For a finite set of complete towers, their ramp grows only linearly at
infinity, while `A(t)~4exp(t/2)`. Retaining exact `A` with finitely many
towers still violates the at-most-quadratic growth of a CND function.
The full-tower grouping therefore does not bypass the round001
finite-place cutoff obstruction.

## 5. Full towers have infinite first service moments

Let `alpha=-gamma_linear>0`, so the exact Archimedean derivative is

\[
 A'(t)=2e^{t/2}-\alpha+eta(t),\qquad
 \eta(t)=2\sum_{m\ge1}\frac{e^{-(4m+1)t/2}}{4m+1}>0.
\]

For the tower service nodes `sigma_k=A'(k ell)` and weights
`w_k=ell r^k`,

\[
 w_k\sigma_k=2\ell-\alpha\ell r^k+\ell r^k\eta(k\ell)
 \longrightarrow2\ell.
\]

Thus the physical first moment `H_p` is finite, but

\[
 \boxed{\sum_{k\ge1}w_k\sigma_k=+\infty.}
\]

The service-node law has finite mass and infinite first moment. Standard
finite-first-moment Strassen/Kellerer martingale and barycentric-moment
arguments cannot be applied to this whole block as if it were an
integrable probability measure.

There is exact renormalized bookkeeping, but it is signed compensation:

\[
 \sum_{k=1}^K w_k\sigma_k-2\ell K
 =-\alpha M_{p,K}+E_{p,K},
\]

where `E_(p,K)=sum_(k<=K) ell r^k eta(k ell)` converges and obeys

\[
 0<E_{p,K}\le
 \frac{2\ell}{5(1-r^4)}\frac{r^6(1-r^{6K})}{1-r^6}.
\]

The bound follows termwise from
`eta(k ell)<=2r^(5k)/[5(1-r^(4k))]`.
Removing `2ell` per tower level is not a positive-probability operation;
any use of this finite part must retain its exact debit.

## 6. Scope and the next missing step

The tower suggestion supplies a real positive arithmetic building block:
`D_p` has an explicit interval Gram map and a positive finite Lévy measure.
It also exposes precisely what positivity costs: the sharp linear term
`M_p|t|`. Independent positive aggregation either diverges or, after its
natural normalization, yields only the universal `|t|` limit.

A surviving route must couple towers and the Archimedean contribution
so that the divergent linear/service corrections cancel while a separate
positive structure remains. Nothing here proves that such a coupled
construction exists, or that every conceivable one is impossible.
The scalar reserve and its compensated transport obligation remain open.

Verification uses exact rational geometric identities and certified Arb
inequalities in `tests/test_prime_towers.py`, backed by
`scripts/prime_towers.py`. These tests cover full-block formulas and
finite calibration; the all-`t` statements and convergence are proved
above rather than inferred from samples.
