# An arithmetic connection with Poisson completion

**Date:** 2026-10-09. **Parent:** `265bf38dfd6af7d5820396f7e80244122a4aa235` (Round 059).

**Result:** a zero-input arithmetic compatibility system, an exact discriminator at
the composite 6, a convergent finite theta completion with a proved error bound,
and a closed arithmetic lift with its completed logarithmic connection.
**Not obtained:** a positive realization of the completed Weil form. RH remains open.

Here “zero-input” means that no zero locations, zero-defined matrices, spectral
boundary conditions, or scattering phases are supplied to the construction. The
finite Gauss phase below is computed from a character and an additive Fourier
transform. It is not inferred from a zero spectrum.

## 1. The hole contract

| Item | Contract |
|---|---|
| Proposed statement | The integer incidence connection, a marked character line in the additive residue module, and the integer-lattice Poisson lift jointly recover the actual degree-one arithmetic source and admit an explicit convergent finite completion. |
| Quantifiers | Every finite incidence cutoff N; every normalized arithmetic sequence a for the incidence identity; primitive Dirichlet characters for the character/Poisson identity; the stated Schwartz seed and every integer N for the cutoff theorem. |
| Truth state | Proved by the elementary identities and estimates below; numerical implementations cross-check the formulas. |
| Weakest useful form | Exact source identification plus one nontrivial, quantitatively convergent global Poisson seed. This is sufficient for the present construction, not sufficient for RH. |
| Edges closed | Coefficients to actual Lambda impulses; character to admissible local amplitudes; integer dilation to log n and half-density; finite theta sums to an actual L2 completion; moment-retaining lattice and logarithmic maps to closed operators on stated domains. |
| Edge still open | A trace/pairing identity that turns this completion into the full Weil form with an independently proved sign. |
| Novelty tax | Dirichlet convolution, Gauss sums, Poisson/Müntz summation and Euler summation are classical. The integration, exact cutoff witness, and mutation audit are contributions to this program; no literature-level novelty or new RH theorem is claimed. |
| Known failures avoided | A per-prime square replacing the Weil form; a hidden zero-built state; a divergent hard-cutoff Gram; treating symmetry as positivity; promoting coefficient admissibility to RH. |
| Falsifiers | A nonzero connection residual on arbitrary coefficients; DH satisfying the marked character equation; incorrect clock/amplitude satisfying the fixed covariance; the proved cutoff estimate failing. |
| Fresh probe region | Theta parameters 0.37, 1.3, 3.7 and cutoffs 37, 101, 257, with a larger raw-norm check at N=1024; declared in the script before its first run. |
| Computational boundary | Exact symbolic finite identities; ordinary high-precision arithmetic and floating-point quadrature elsewhere, not interval certification or an infinite numerical proof. |

The primary obstruction is a **pathway gap** between the completed arithmetic
source and an independently positive Weil pairing. The missing historical
`dh/` scripts are a separate reproducibility gap: the Round 049/051/058 values
are repository-reported observations, not measurements rerun in this checkpoint.

## 2. The integer incidence connection

Let a be an arithmetic function with a(1)=1. Dirichlet convolution is

$$ (a*c)(n)=\sum_{d\mid n}a(d)c(n/d). $$

On the coordinates 1,...,N define

$$
C_N(a)_{m,n}=\begin{cases}
a(m/n)(m/n)^{-1/2},&n\mid m,\\
0,&\text{otherwise},
\end{cases}
\qquad H_N=\mathrm{diag}(\log1,\ldots,\log N).
$$

### Proposition 1: exact source extraction

For every N,

$$ C_N(a)C_N(c)=C_N(a*c),\qquad [H_N,C_N(a)]=C_N(a\log). $$

Thus, with the inverse taken in the normalized Dirichlet convolution algebra,

$$
\boxed{[H_N,C_N(a)]C_N(a)^{-1}=C_N(b_a),\qquad
b_a=(a\log)*a^{-1}.}
$$

**Proof.** The matrix product sums over the intermediate divisors n|j|m.
The two half-density factors multiply to (m/n)^(-1/2). The commutator multiplies
each nonzero entry by log m-log n=log(m/n). C_N(a) is triangular with unit
diagonal, so its inverse exists and represents the convolution inverse. No
infinite limit is involved. ∎

The source can be computed without ever inserting prime support:

$$
b_a(n)=a(n)\log n-
\sum_{\substack{d\mid n\\1<d<n}}b_a(d)a(n/d),\quad n>1,
\qquad b_a(1)=0.
$$

For a character chi, complete multiplicativity and the divisor identity
sum_{d|n} Lambda(d)=log n give

$$\boxed{b_\chi(n)=\chi(n)\Lambda(n).}$$

The actual matrix coefficient is therefore chi(n)Lambda(n)/sqrt(n). This
includes the exact prime-power weight log p, rather than log(p^k).

### Proposition 2: converses and the composite defect

The following statements are exact:

1. b_a is supported on prime powers if and only if a is multiplicative in the
   ordinary coprime sense.
2. For a fixed character chi, b_a=chi Lambda if and only if a=chi.
3. For distinct primes p and q,

$$\boxed{b_a(pq)=\log(pq)[a(pq)-a(p)a(q)].}$$

**Proof of 1.** The locally finite convolution logarithm

$$\log_*a=\sum_{j\ge1}\frac{(-1)^{j+1}}{j}(a-\delta_1)^{*j}$$

has only finitely many nonzero terms at any particular integer. Since a -> a log
is a derivation of convolution,

$$b_a(n)=\log n\,(\log_*a)(n).$$

The convolution logarithm of an Euler product is a sum of its individual
prime-power parts. Conversely, exponentiating a sum supported on prime powers
gives an Euler product and hence a multiplicative sequence. This characterizes
ordinary multiplicativity; a degree-one tower law is an additional requirement.

**Proof of 2.** The forward identity has already been shown. Conversely, the
triangular recurrence a log=(chi Lambda)*a determines a(n) inductively. After
the preceding a(n/d) have been identified with chi(n/d), it gives
a(n)log n=chi(n)sum_{d|n}Lambda(d)=chi(n)log n. ∎

**Proof of 3.** Only d=p and d=q occur in the proper-divisor sum. Collect
log p+log q=log(pq). ∎

This is a source identity, not a positivity theorem. The finite connection is
strictly triangular; its finite spectrum cannot be interpreted as zeta zeros.

## 3. A shared additive residue module

On C[Z/qZ], use the additive translation, multiplicative pullback, and additive
Fourier transform

$$
(Sv)(r)=v(r-1),\quad (M_mv)(r)=v(mr),\quad
(\mathcal F_qv)(a)=q^{-1/2}\sum_{r\bmod q}e^{2\pi iar/q}v(r).
$$

M_m is unitary whenever gcd(m,q)=1. With this pullback convention its inverse
obeys M_m^(-1)S=S^m M_m^(-1). For the character vector v_chi(r)=chi(r),

$$M_mv_\chi=\chi(m)v_\chi.$$

Consequently a nonzero marked eigenline requires |chi(m)|=1 at unramified
primes. The ramified case is separate: chi(p)=0 for p|q.

For a primitive character the finite Gauss identity is

$$
\mathcal F_qv_\chi=\frac{\tau(\chi)}{\sqrt q}v_{\bar\chi},\qquad
\tau(\chi)=\sum_{r\bmod q}\chi(r)e^{2\pi ir/q},\qquad
|\tau(\chi)|=\sqrt q.
$$

The marked eigenline and its Fourier partner belong to the **same additive
module**. An arbitrary superposition can preserve the Fourier symmetry while
losing the multiplicative eigenline.

### The exact Dirichlet/Davenport–Heilbronn discriminator

Take chi modulo 5 with chi(2)=i. In residue order 0,1,2,3,4,

$$v_\chi=(0,1,i,-i,-1).$$

Define

$$
\kappa=\frac{\sqrt{10-2\sqrt5}-2}{\sqrt5-1}
=0.284079043840412296028291832393\ldots,
$$

and v_D=(0,1,kappa,-kappa,-1), periodically extended to the integers. It is
the normalized Davenport–Heilbronn combination. Directly,

$$\mathcal F_5v_D=i v_D,$$

but

$$
M_2v_D-\kappa v_D=(0,0,-1-\kappa^2,1+\kappa^2,0),
\qquad
\|M_2v_D-\kappa v_D\|^2=2(1+\kappa^2)^2>0.
$$

Its source at 6 is

$$
\boxed{b_D(6)=(1+\kappa^2)\log6,\qquad
\frac{b_D(6)}{\sqrt6}=0.790514058009852033\ldots.}
$$

For chi, b_chi(6)=0. Both use exactly the same integer logarithms. Thus rational
independence of prime logarithms cannot itself be their separator.

## 4. The actual clock and half-density

On L2(R,dx), let

$$ (R_af)(x)=a^{-1/2}f(x/a),\qquad (T_bf)(x)=f(x-b). $$

The exponent 1/2 is forced by unitarity for a positive real dilation amplitude:
if R_a used a^(-gamma), its squared norm would be multiplied by a^(1-2gamma).
An additional unit-modulus phase is distinct character data, not a change of
the real half-density.

The exact affine relation is

$$R_aT_1=T_aR_a.$$

Therefore the integer dilation labelled 2 must satisfy

$$R_{e^{\ell_2}}T_1=T_2R_{e^{\ell_2}}
\quad\Longrightarrow\quad e^{\ell_2}=2
\quad\Longrightarrow\quad\ell_2=\log2.$$

The implication uses faithfulness of the real translation representation.
Assigning arbitrary lengths to a free monoid would miss this constraint.

On the positive half-line, set U_n=R_n^*, so

$$U_nf(x)=\sqrt n f(nx),\qquad Xf(x)=-(\log x)f(x).$$

Then [X,U_n]=(log n)U_n. The continuous counterpart of the incidence system is

$$
\Theta_af(x)=\sum_{n\ge1}a(n)n^{-1/2}U_nf(x)
=\sum_{n\ge1}a(n)f(nx).
$$

For bounded character coefficients and a rapidly decreasing input, the sums
below converge absolutely at each fixed x>0:

$$
\boxed{[X,\Theta_\chi]f=B_\chi\Theta_\chi f,\qquad
B_\chi=\sum_{d\ge1}\frac{\chi(d)\Lambda(d)}{\sqrt d}U_d.}
$$

Indeed, collecting dm=n on the right gives the divisor identity of section 2.
This is a pointwise/distributional identity. It does **not** assert boundedness
of B_chi on L2, convergence of a critical-line Euler series in operator norm,
or existence of the requested Weil adjoint.

## 5. Poisson supplies the Gamma and pole completion

Use the real Fourier convention hat f(xi)=integral f(x)exp(-2 pi i x xi)dx.
Let g(x)=exp(-pi x^2), D=x d/dx, and define the explicit seed

$$
\boxed{\phi(x)=\frac{D(D+1)g(x)}{4\pi^2}
=\left(x^4-\frac{3x^2}{2\pi}\right)e^{-\pi x^2}.}
$$

Fourier transformation sends D to -D-1, so D(D+1) commutes with Fourier
transformation. Thus hat phi=phi. Direct evaluation also gives phi(0)=0 and
integral_R phi=0. These are outputs of the explicit differential polynomial;
no spectral boundary condition is chosen.

Poisson summation now gives, for x>0,

$$\boxed{\Theta\phi(x)=x^{-1}\Theta\phi(1/x).}$$

The large-x side decays as a Gaussian; the reciprocal identity controls the
small-x side. In particular Theta phi is in L2(R+,dx).

Initially for Re s>1, termwise Mellin transformation gives

$$
\mathcal M(\Theta\phi)(s)
=\zeta(s)\mathcal M\phi(s)
=\frac{s(s-1)}{8\pi^2}\pi^{-s/2}\Gamma(s/2)\zeta(s)
=\boxed{\frac{\xi(s)}{4\pi^2}}.
$$

The left side is entire by its decay at both ends, supplying continuation.
The displayed equality identifies the output; xi or its zeros are not inputs.

For primitive nontrivial chi of conductor q and parity epsilon in {0,1}, use
phi_epsilon(x)=x^epsilon exp(-pi x^2/q). The analogous formulas are

$$
\mathcal M(\Theta_\chi\phi_\epsilon)(s)
=\frac12\left(\frac q\pi\right)^{(s+\epsilon)/2}
\Gamma\left(\frac{s+\epsilon}{2}\right)L(s,\chi),
$$

$$
\Theta_\chi\phi_\epsilon(x)
=\omega_\chi x^{-1}\Theta_{\bar\chi}\phi_\epsilon(1/x),\qquad
\omega_\chi=\frac{\tau(\chi)}{i^\epsilon\sqrt q}.
$$

For the mod-5 character, omega_chi=0.85065080835...+0.52573111212...i.
Writing c=(1-i kappa)/2 gives c omega_chi=bar c, so the combination
a_D=c chi+bar c bar chi has the corresponding self-dual theta identity too.
The probe verifies both identities. Poisson symmetry alone therefore cannot
replace the multiplicative eigenline condition.

The classical lineage is Poisson/Müntz summation; see Burnol [S1, S2]. The
degree-one character/Gamma data and related converse theorem are in [S3].

## 6. There really are mixed-prime terms

For the seed above, direct Gaussian integration gives

$$
K(m,n)=\int_0^\infty\phi(mx)\phi(nx)\,dx
=\frac{3m^2n^2[35m^2n^2-6(m^2+n^2)^2]}
{32\pi^4(m^2+n^2)^{9/2}}.
$$

In particular K(2,3)>0 and K(2,5)<0. They are nonzero overlaps in the common
additive space, rather than independent orthogonal ray norms. Every finite
matrix K is nevertheless a Gram matrix and hence PSD. Signed entries do not
make a Gram indefinite, and its PSD does not identify it with the Weil form.

The old universal commutativity-to-factorization claim is separately false.
For commuting V_m e_n=e_(mn), take B=V_2+V_3. Then

$$B^*B=2I+V_2^*V_3+V_3^*V_2.$$

On e_1,e_2,e_3,e_6 its compression is

$$\begin{pmatrix}2&0&0&0\\0&2&1&0\\0&1&2&0\\0&0&0&2\end{pmatrix},$$

with eigenvalues 1,2,2,3. It is not a tensor product across the two prime
coordinates. Even commuting normal unitaries give the nonseparable positive
function |z_2+z_3|^2 on the two-torus. The valid Round-004 Koszul calculation
does not imply a universal prohibition on these constructions.

## 7. Why the raw finite Gram fails

Put

$$\Theta_N(x)=\sum_{n=1}^N\phi(nx),\qquad
F(y)=\int_0^y\phi(u)\,du=-\frac{y^3}{2\pi}e^{-\pi y^2}.$$

### Theorem 3: an exact cutoff divergence

$$
\boxed{\lim_{N\to\infty}\frac{\|\Theta_N\|_2^2}{N}
=\int_0^\infty\left|\frac{F(y)}y\right|^2dy
=C_\phi:=\frac{3}{128\sqrt2\pi^4}>0.}
$$

**Proof.** At the shrinking spatial scale x=y/N,

$$h_N(y):=N^{-1}\Theta_N(y/N)\longrightarrow
\int_0^1\phi(ty)dt=F(y)/y.$$

This is an ordinary Riemann sum. To justify the norm limit, use
|phi(x)|<=C min(x^2,x^(-2)). For y<=1 this bounds h_N by C' y^2.
For y>=1, write h=y/N. Splitting the integer sum at nh=1 proves
h sum_{n>=1}|phi(nh)|<=C'' uniformly over h>0, so |h_N(y)|<=C''/y.
Thus |h_N|^2 has an integrable majorant proportional to min(y^4,y^(-2)).
Finally ||Theta_N||^2/N=integral |h_N|^2dy. Dominated convergence and a
Gaussian fourth moment finish the proof. ∎

The full Theta phi is in L2, while its bare partial sums have norm squared
growing linearly. Pointwise convergence did not justify exchanging the
infinite sum with the Hilbert-space norm. The missing mass concentrates at
x of order 1/N; in logarithmic coordinates it travels towards the origin end.

## 8. An explicit finite completion and its error bound

### Theorem 4: subtract the integral from the same lattice

Define

$$
\boxed{\widetilde\Theta_N(x)=\Theta_N(x)-\frac{F(Nx)}x
=\Theta_N(x)+\frac{N^3x^2}{2\pi}e^{-\pi N^2x^2}.}
$$

Then

$$
\boxed{\|\widetilde\Theta_N-\Theta\phi\|_2^2
\le\frac1N\int_0^\infty
\left(\int_y^\infty|\phi'(u)|du\right)^2dy.}
$$

The constant is finite, so this proves L2 convergence with norm error
O(N^(-1/2)). No infinite numerical extrapolation is used.

**Proof.** Compare each tail term phi(nx), n>N, with the integral of phi(tx)
over t in [n-1,n]. The fundamental theorem of calculus gives

$$\left|\sum_{n>N}\phi(nx)-\int_N^\infty\phi(tx)dt\right|
\le\int_{Nx}^\infty|\phi'(u)|du.$$

Since integral_0^infinity phi=0, the continuous tail equals -F(Nx)/x.
The expression on the left is Theta phi-tilde Theta_N. Square, integrate,
and substitute y=Nx. ∎

An optional endpoint correction improves the rate:

$$\widetilde\Theta_N^{\rm trap}(x)=
\Theta_N(x)-F(Nx)/x-\tfrac12\phi(Nx).$$

The composite trapezoid remainder has kernel bounded by 1/8 on each unit
interval. Applied to t -> phi(tx), it gives

$$
\boxed{\|\widetilde\Theta_N^{\rm trap}-\Theta\phi\|_2^2
\le\frac1{64N^3}\int_0^\infty y^2
\left(\int_y^\infty|\phi''(u)|du\right)^2dy.}
$$

Hence its norm error is O(N^(-3/2)). This is an approximation theorem for the
theta completion, not a positivity estimate for the Weil form.

There are also two exact calibration facts. First, the trapezoid estimate
shows that at x=y/N the leading error of tilde Theta_N is phi(y)/2.
Dominated convergence using the first-derivative bound yields

$$\lim_{N\to\infty}N\|\widetilde\Theta_N-\Theta\phi\|_2^2
=\tfrac14\|\phi\|_2^2=\frac{33}{2048\sqrt2\pi^4}.$$

Second, for every fixed complex scalar lambda,

$$
\lim_{N\to\infty}\frac{\|\Theta_N-\lambda F(Nx)/x\|_2^2}{N}
=|1-\lambda|^2C_\phi.
$$

This follows from the same rescaled Riemann sum and majorant as Theorem 3.
The coefficient 1 is forced if this leading divergence is to disappear.

For nonprincipal periodic coefficients with mean zero, including chi_5 and
DH, partial sums are bounded. Abel summation controls the raw tail by a
constant times |phi(Nx)|+integral_(Nx)^infinity |phi'|. It already converges
in L2 at O(N^(-1/2)). This convergence property accepts DH and is not the
multiplicativity discriminator.

## 9. The bare moment obstruction and its closed completion

Success for phi does not make X=-log x preserve the completed space. In fact,

$$\int_0^\infty X\phi(x)dx=-(\mathcal M\phi)'(1)=-\frac1{8\pi^2}\ne0.$$

Riemann summation consequently gives

$$\Theta(X\phi)(x)\sim-\frac1{8\pi^2x}\quad(x\downarrow0),$$

which is not L2. The displayed continuous source connection cannot therefore
be promoted silently to an identity of closed operators on the theta L2
space. Its moment and pole terms must also be completed.

Nor can one repair this by demanding all log moments vanish while keeping a
nonzero Schwartz input. A function smooth at 0 and rapidly decreasing at
infinity has a Mellin transform holomorphic for Re s>0. If
integral X^k f=0 for every nonnegative integer k, every derivative of its
Mellin transform at s=1 vanishes. The identity theorem and Mellin uniqueness
force f=0. A useful logarithmic domain completion must retain the moment
data or another explicit compensating term.

The analytic Mellin hypothesis matters. Merely assuming that every logarithmic
moment exists does not justify an analytic Taylor expansion. The obstruction
just proved applies to the stated smooth, rapidly decreasing core (and more
generally to inputs with an open strip of absolute Mellin convergence).

### 9.1 Retain the moment: the closed lattice lift

The preceding failure has an explicit repair. Start with the dense core
$\mathcal D=C_c^\infty(0,\infty)$ in $H=L^2(\mathbb R_+,dx)$ and define

$$
I(f)=\int_0^\infty f(u)du,\qquad
\boxed{\mathcal A_0f(x)=\sum_{n\ge1}f(nx)-\frac{I(f)}x.}
$$

For fixed x the sum is finite. The subtraction uses the integral of the
same input; nonzero moments are retained. The sum/integral estimate gives

$$|\mathcal A_0f(x)|\le\int_0^\infty|f'(u)|du.$$

Beyond the support of f, A_0 f=-I(f)/x. Thus A_0 f and X A_0 f are in L2.

**Theorem 5 (closed moment-retaining lift).** A_0 is closable. Its graph
closure is a closed normal operator, identified by Mellin transformation
with maximal multiplication by zeta(1/2+it).

**Mellin identity.** For 0<Re s<1, integrate over x>=epsilon and change
variables inside the finite dilation sums. Euler summation gives

$$\sum_{n\le Y}n^{-s}=\frac{Y^{1-s}}{1-s}+\zeta(s)+O_s(Y^{-\operatorname{Re}s}).$$

With Y=u/epsilon, the first term integrates to
epsilon^(s-1) I(f)/(1-s), exactly the integral being subtracted. The error
is O_f,s(epsilon^(Re s)), since the support is bounded away from zero. Hence

$$\boxed{\mathcal M(\mathcal A_0f)(s)=\zeta(s)\mathcal Mf(s),\quad0<\operatorname{Re}s<1.}$$

This is the classical Müntz identity [S1, p. 69, formula (5)]. The lattice
sum/integral defect was the definition; zeta is the identified output.

**Joint graph-core proof.** Mellin Plancherel is unitary from H to
L2(dt/(2 pi)). The identity first places A_0 inside a closed multiplication
operator, proving closability. Euler's fractional-part formula gives

$$\zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{u\}u^{-s-1}du,$$

and, on Re s=1/2,

$$|\zeta(s)|\le1+2|s|,\qquad|\zeta'(s)|\le6+4|s|.$$

The unitary log-coordinate map U f(v)=exp(v/2)f(exp v) sends the core onto
C_c^infinity(R); Mellin becomes Fourier. Smooth compact frequency functions
are dense in the joint weighted space with weight
1+|zeta|^2+|zeta'|^2. Their inverse Fourier transforms are Schwartz.
Smooth cutoff in v converges in H1 and therefore in both graph norms.
This proves that the physical core is a joint graph core for the two
maximal multipliers zeta and -zeta'. In particular the asserted closure
of A_0 is maximal. ∎

Its maximal domain is an output characterization:

$$\operatorname{Dom}\mathcal A
=\{f\in H:\zeta(1/2+it)\mathcal Mf(1/2+it)\in L^2(dt)\},
\qquad\mathcal A=\overline{\mathcal A_0}.$$

No zero locations or spectral boundary data were selected. Normality does
not assert a self-adjoint operator having zeta zeros as eigenvalues.

### 9.2 The logarithmic insertion is also completed

Write J(f)=integral_0^infinity (log u)f(u)du and define on the same core

$$
\boxed{\mathcal C_0f(x)=\sum_{n\ge1}(\log n)f(nx)
-\int_0^\infty(\log t)f(tx)dt.}
$$

Changing variables in the integral gives the genuine core commutator

$$
\mathcal C_0f=[X,\mathcal A_0]f
=\sum_{n\ge1}(\log n)f(nx)+\frac{I(f)\log x-J(f)}x.
$$

Differentiating the Müntz identity gives

$$\mathcal M(\mathcal C_0f)(s)=-\zeta'(s)\mathcal Mf(s).$$

By the joint graph-core argument, C_0 is closable and its closure C is the
maximal multiplier -zeta'. The commutator equality is proved on the stated
core; maximal commutator domains have not been equated.

The seed phi and each fixed X^k phi also satisfy these formulas. Their
behavior O(x^2(1+|log x|^k)) at zero and rapid decay at infinity give the
required integrability and log-coordinate cutoff approximation. In particular,

$$\mathcal C\phi(x)=\sum_{n\ge1}(\log n)\phi(nx)-\frac1{8\pi^2x}\in L^2.$$

This repairs the bare-domain failure by retaining the logarithmic moment.

### 9.3 Finite approximation of both completed operators

For f in the core, put

$$
\mathcal A_Nf(x)=\sum_{n=1}^Nf(nx)-\frac1x\int_0^{Nx}f(u)du,\qquad
\mathcal A_N^{\rm trap}f=\mathcal A_Nf-\tfrac12f(Nx).
$$

With $H_j^f(y)=\int_y^\infty|f^{(j)}(u)|du$, section 8's proofs give

$$
\|\mathcal A_Nf-\mathcal A f\|_2^2\le N^{-1}\|H_1^f\|_2^2,\qquad
\|\mathcal A_N^{\rm trap}f-\mathcal A f\|_2^2
\le\frac{\|yH_2^f(y)\|_2^2}{64N^3}.
$$

The first estimate also holds for C1 inputs with its displayed constant
finite. The second requires a locally absolutely continuous first
derivative and the displayed second-derivative integral. Both hold for
every fixed X^k phi; no vanishing-moment requirement is imposed.

Finite logarithmic approximants are

$$
\mathcal C_Nf=[X,\mathcal A_N]f
=\sum_{n=1}^N(\log n)f(nx)-\int_0^N(\log t)f(tx)dt,\qquad
\mathcal C_N^{\rm trap}f=\mathcal C_Nf-\tfrac12(\log N)f(Nx).
$$

Their norm errors on the core are O_f((1+log N)N^(-1/2)) and
O_f((1+log N)N^(-3/2)). Indeed, if r_N=A_N-A, then
C_N-C=X r_N f-r_N(Xf). Apply the preceding pointwise derivative-tail
bounds and put y=Nx. In particular,

$$
\|\mathcal C_N^{\rm trap}f-\mathcal C f\|_2
\le\frac{(\log N)\|yH_2^f\|_2+
\|y(\log y)H_2^f\|_2+\|yH_2^{Xf}\|_2}{8N^{3/2}}.
$$

Every displayed constant is finite on the core. The approximants use
integer sums and ordinary integrals only.

### 9.4 A closed connected source and its precise boundary

Define the connection on the arithmetic image of the core:

$$\boxed{\nabla_0(\mathcal A_0f)=\mathcal C_0f,\qquad f\in\mathcal D.}$$

A_0 is injective: its Mellin multiplier is nonzero almost everywhere,
because it is a nonzero analytic function, without needing the locations
of its zeros. Its core image is dense by the graph-core result and the
dense range of the maximal multiplier.

**Proposition 6.** nabla_0 is closable; its closure is the maximal
Mellin multiplier -zeta'/zeta, defined almost everywhere.

**Proof.** Write a(t)=zeta(1/2+it), c(t)=-zeta'(1/2+it). The arithmetic
graph consists of pairs (a F,c F) for F in the Mellin image of the core.
It lies in the closed graph of multiplication by c/a. Conversely, for
h in that maximal graph domain, restrict h to |t|<=k and |a(t)|>=1/k.
Then f_k=h_k/a belongs to the joint domain of multiplication by a and c.
Joint graph-core approximation gives physical core vectors whose image
pairs tend to (h_k,(c/a)h_k). Let k tend to infinity to recover the full
pair (h,(c/a)h). ∎

These proof truncations identify the already defined lattice graph
closure. They are not supplied zero data or a chosen spectral boundary.
The primary construction is the arithmetic graph, not an imported
logarithmic-derivative or scattering phase. The maximal closure can have
a larger domain than the literal composition C A^(-1), because h/a need
not be in L2.

**Renormalization remains essential.** If I(f) is nonzero, then for large
d one has A_0f(dx)=-I(f)/(dx); the raw prime sum
sum_d Lambda(d)A_0f(dx) diverges. If I(f)=0, it instead equals
sum_n (log n)f(nx), but the subtraction -J(f)/x is still required.
Thus nabla is the closed completed source, not a convergence assertion
for the unrenormalized critical prime series. Its Euler-region source
is the actual Lambda, as extracted in section 2.

For primitive nonprincipal chi, use A_chi,0 f=sum chi(n)f(nx), without
the trivial-character integral term, and C_chi,0=[X,A_chi,0]. Bounded
character partial sums give the analogous Mellin identities and
polynomial growth/core proof with L(s,chi), -L'(s,chi). The connected
source is chi Lambda. Mean-zero periodic DH data also admit closed
lifts, but fail the common character line and have the extra composite
source. Closedness alone is not the discriminator.

The closed lift and connected operator, including their ordinary Hilbert
adjoints, now exist unconditionally. Their full Weil pairing and its
independent sign remain the open theorem.

## 10. What the original mutations actually say

| Mutation | Identity that fails | What may still survive |
|---|---|---|
| Fake b(6) | b_chi=chi Lambda, and the fixed completion | All original zeros can remain unchanged |
| Nonunit alpha_2 at an unramified prime | Unitary character eigenline; fixed degree-one completion | Complete multiplicativity and an Euler product |
| Whole 2-tower at the wrong log length | Actual integer affine covariance; fixed completion | An abstract multiplicative semigroup |
| Wrong real half-density | L2(dx) dilation isometry | A formal convolution identity |
| DH | Common multiplicative eigenline and prime-power source support | Additive Fourier symmetry and its functional equation |

### Proposition 7: one-prime completion rigidity

Let p be unramified, a=chi(p), |a|=1, and

$$F_b(s)=L(s,\chi)R(s),\qquad R(s)=\frac{1-ap^{-s}}{1-bp^{-s}}.$$

If F_b has the same conductor and Gamma factor as L(s,chi), with
coefficient-conjugate reflected functional equation and any constant nonzero
root factor, then b=a and the root factor is unchanged.

**Proof.** Dividing the meromorphic functional equations gives
R(s)=c R^#(1-s), where R^#(s)=overline{R(bar s)}. Put x=p^(-s), clear
denominators, and compare coefficients:

$$ (1-ax)(px-\bar b)=c(1-bx)(px-\bar a). $$

Constant and quadratic terms give bar b=c bar a and a=cb; in particular
|b|=1 and c=a bar b. Linear terms then give p+c=cp+1, so c=1 and b=a. ∎

For a coherently shifted tower with real ell>0, replace the denominator by
1-a exp(-ell s). Along real s tending to positive infinity, R(s) tends to 1,
while R^#(1-s) is asymptotic to exp((log p-ell)(s-1)). A constant reflected
functional equation forces ell=log p.

Most importantly, a fake source impulse does not require changing zeros.
If in the Euler region

$$-F'/F=-L'/L+\eta6^{-s},\qquad F/L\longrightarrow1,$$

then exactly

$$\boxed{F(s)=L(s,\chi)\exp\left(\frac\eta{\log6}6^{-s}\right).}$$

The exponential is entire and never zero, so all zeros are preserved. A
fixed completion would require R(s)=c R^#(1-s). Logarithmic differentiation
would require -eta 6^(-s)=bar eta 6^(s-1), which forces eta=0. Thus the
nonzero fake impulse violates the old completion. A negative mutated
arithmetic form cannot automatically be interpreted as newly off-line zeros:
it no longer has the original explicit-formula package.

## 11. The precise map into the Weil form

For g in C_c^infinity([-L,L]), use

$$F_g(z)=\int_\mathbb Rg(u)e^{izu}du,\qquad
R_g(u)=(g*\tilde g)(u),\quad\tilde g(u)=\overline{g(-u)}.$$

For primitive chi of conductor q and parity epsilon, the arithmetic form is

$$
Q_\chi(g)=P_\chi(g)+\frac1{2\pi}\int_\mathbb R|F_g(t)|^2
\left[\log(q/\pi)+\mathrm{Re}\,\psi\left(\frac{1/2+\epsilon+it}{2}\right)\right]dt
-2\mathrm{Re}\sum_{2\le n\le e^{2L}}
\frac{b_\chi(n)}{\sqrt n}R_g(\log n).
$$

For primitive nontrivial chi, P_chi=0. For zeta,

$$P_\zeta(g)=2\mathrm{Re}[F_g(i/2)\overline{F_g(-i/2)}].$$

The connection supplies b_chi=chi Lambda. The Poisson lift supplies q,
epsilon, Gamma and the pole normalization. Every input on this arithmetic
side is now explicit. The finite sum does not invoke convergence of the
infinite prime comb on the critical line.

As a normalization check, for the box g=1_[-T/2,T/2] the probe independently
integrates the origin-renormalized Gamma difference kernel and obtains
Q_zeta(g)=2 Psi(T), matching the existing Suzuki evaluator at T=0.3,1.1,2.3,4.1
to better than 3e-45 in the run. Box tests are a finite-energy extension of
the smooth test convention, not a claim that four values establish positivity.

The unconditional zero-side analytic pairing, used here only to identify the
classical criterion, is

$$\sum_\rho F_g(\gamma_\rho)\overline{F_g(\bar\gamma_\rho)},
\qquad\gamma_\rho=(\rho-1/2)/i.$$

It becomes a sum of modulus squares when the ordinates are real. Using
|F_g(gamma_rho)|^2 for complex ordinates would already insert the desired sign.
See Lagarias [S4], section 3 and Appendix A, for the reflected pairing.

### The fourth gate

On a domain where the full theta lift belongs to L2(dx) and its Mellin identity
holds, Mellin Plancherel identifies its positive norm with an integral of
|L(s,chi) M f(s)|^2 on Re s=1/2. The explicit completed seed is in that domain.
A finite raw theta Gram instead uses the finite Dirichlet polynomial in place
of L(s,chi). The Weil form contains
the connected logarithmic source and its signed completion. They are distinct
pairings. The construction above has not proved an identity

$$Q_\chi(g)=\|\mathcal B_\chi g\|^2$$

for an independently constructed operator B_chi, or an inequality implying
Q_chi(g)>=0 for every admissible g.

That is the **fourth gate**: exact identification with the full Weil form
together with a valid sign mechanism and domain/limit control. Passing the
three arithmetic gates alone is not a proof of RH. The distinction also
appears in the semilocal operator strategy of Connes–Consani–Moscovici [S5],
whose introduction leaves comparison of the positive trace with the Weil
functional as the task to be supplied.

## 12. Next discriminating work

The finite theta completion and the closed logarithmic connection are usable.
The next concrete test is to construct a source-compatible trace or pairing
for these operators, compute it on two independent compact test families,
and compare it with Q_chi above. A successful comparison must cover the
whole form, not just its prime term or its box restriction. It must preserve
the reflected conjugation and handle both parity sectors.

A candidate is rejected immediately if it gives the theta norm in place of
Q, produces spurious log(pq) or log(p/q) atoms in the final source, discards
the pole/moment counterterms, or relies on a finite sign to infer all-support
positivity. A proof of a weaker domain/trace lemma can still be useful, but
must be graded by that exact scope.

## Sources and provenance

- **[S1]** J.-F. Burnol, *Two complete and minimal systems associated with the
  zeros of the Riemann zeta function*, section 1 (Poisson/Müntz and Mellin
  conventions): https://jtnb.centre-mersenne.org/item/10.5802/jtnb.434.pdf
- **[S2]** J.-F. Burnol, *Entrelacement de co-Poisson*:
  https://arxiv.org/abs/math/0407443
- **[S3]** J. Kaczorowski, G. Molteni, A. Perelli, *A converse theorem for
  Dirichlet L-functions*, Comment. Math. Helv. 85 (2010), 463–483,
  introduction and Theorem 1. Its hypotheses include analytic continuation,
  growth and the logarithmic Euler condition; it is not a GRH theorem:
  https://sites.unimi.it/molteni/research/papers-pdf/23-molteni-A_converse_theorem_for_Dirichlet_L-functions.pdf
- **[S4]** J. C. Lagarias, *Li coefficients for automorphic L-functions*,
  Ann. Inst. Fourier 57 (2007), 1689–1740, section 3 and Appendix A:
  https://www.numdam.org/item/10.5802/aif.2311.pdf
- **[S5]** A. Connes, C. Consani, H. Moscovici, *Zeta zeros and prolate wave
  operators: Semilocal adelic operators*, introduction, pp. 2–3:
  https://arxiv.org/pdf/2310.18423

The finite incidence identities, mixed-prime Gram, cutoff estimates and mutation
rigidity are proved directly above. These citations establish the classical
lineage and normalize the remaining problem. They are not evidence that the
missing positivity theorem has been supplied.
