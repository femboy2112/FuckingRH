# Riemann Band Lab
## A self-contained research setup for multiplicative-band communications

**Version:** 0.1.0  
**Prepared:** September 11, 2026, America/New_York (September 12 UTC)  
**Deliverable type:** research charter, mathematical specification, experimental protocol, and local coding handoff  
**Status:** finite calibration implemented; communications advantage and hardware applicability **UNVERIFIED**.

> Investigate the band, not just the carrier: can dilation-aware representations and arithmetic structure improve a realistically constrained broadband transceiver—and do Riemann-zeta zeros contribute anything that a good generic design cannot?

This document stands alone. No conversation, private repository, previous assistant response, or unstated theoretical framework is required. The accompanying starter is useful but not essential: the definitions, proofs, tests, and implementation requirements needed to reconstruct it are included here.

“Riemann antenna” is the motivating code name. The immediate object is a **digital broadband waveform-and-receiver research program**, not a demonstrated antenna, a proof of the Riemann hypothesis, or a claim of additional physical channel capacity.

---

# 1. Mission and acceptance criteria

Explore communication with geometrically related carrier centers or waveform scales, particularly the dyadic family

\[
 f_n=f_{\mathrm{ref}}2^n.
\]

The central intuition is that a complete frequency band may have useful multiplicative structure. Taking logarithms makes multiplication into translation. Mellin analysis then supplies a natural transform; integer dilations introduce Dirichlet convolution, prime factorization, Euler products, and Möbius inversion. A further, genuinely speculative step asks whether the particular geometry of zeta zeros improves pulse shaping, coding, estimation, or numerical conditioning.

**Keep three questions separate.**

1. Does an appropriate scale-domain method help on a specified physical channel?
2. Does arithmetic factorization help when the channel really has integer-scale structure?
3. Do actual zeta zeros improve anything beyond matched, optimized non-zeta controls?

A positive answer to the first does not establish the second or third. A positive arithmetic toy experiment does not establish a physical channel model. Failure of a zero-based candidate does not invalidate Mellin communication.

## Deliverable that counts as success

Produce a reproducible local repository with correct transforms, declared physical and synthetic channel models, strong baselines, falsifiable hypotheses, tests, immutable experiment receipts, and a clear verdict. A negative finding, a cheaper exact factorization, or a sharply delimited useful regime is a successful research outcome. A pretty spectrum without a competitive experiment is not.

A claim of a **zeta-specific communications benefit** requires a frozen design to improve a preregistered metric against the strongest applicable non-zeta baseline under matched resources, then survive fresh data, channel mismatch, discretization checks, and implementation/provenance scrutiny. It cannot be inferred from a low Gram-matrix coherence alone.

## Local execution constraints

Start with ordinary Python and the standard library; use exact `fractions.Fraction` for finite arithmetic identities. The included calibration needs no installed packages. NumPy is appropriate when implementing sampled waveforms and linear algebra. `mpmath` is optional for zero generation and analytic-number-theory controls. Avoid mandatory GPUs, cloud services, SageMath, large ML stacks, or electromagnetic solvers in the first vertical slice.

Work locally. Do not create or publish a remote repository, push a branch, purchase equipment, change account settings, or transmit RF without explicit authorization. Do not use this exploratory name to imply novelty has been established.

---

# 2. Corrections that must survive every implementation

The following are load-bearing boundaries, not optional caveats.

| Tempting statement | Correct research statement |
|---|---|
| Prime-valued carrier frequencies intrinsically avoid interference. | Frequency planning depends on waveform overlaps, observation time, channel response, and nonlinear products. Being prime in a chosen unit is not an invariant physical property. Integer ratios relative to a reference can be meaningful. |
| Harmonics are linear copies of the input at integer scales. | A **constructed linear scale-copy channel** has that form. A nonlinear amplifier generally creates signal-dependent harmonics and cross-stream intermodulation. These are different models. |
| A log-frequency transform automatically preserves energy and white noise. | Use the correct Jacobian, discrete quadrature, and transformed noise covariance. Interpolating a spectrum is not automatically an isometry. |
| The \(1/2\) Mellin line explains or proves RH. | It follows from the chosen \(L^2(dq)\) normalization. A different measure changes the normalization. It says nothing by itself about the zero locations of zeta. |
| A finite prime-coordinate lift creates extra independent physical dimensions. | An exact coefficient relabeling can expose sparsity or factorization. It cannot create observations or recover information already lost by the measurement map. |
| The Euler product can simply be evaluated as a convergent physical filter on \(\Re s=1/2\). | Ordinary absolute convergence is available for \(\Re s>1\). A finite sum, an analytic continuation, and a centered Müntz operator are different objects. [S1–S3] |
| Every spectral zero annihilates a nonzero finite-energy mode. | A discrete matrix can have an exact null. Isolated zeros of a continuous multiplier need not give a nontrivial \(L^2\) kernel; they can nevertheless destroy a stable inverse. |
| Shuffling the zero ordinates is a meaningful Gram-matrix control. | Merely permuting matrix rows leaves \(R^*R\) unchanged. Shuffle **gaps and reconstruct new ordinates**, or use genuinely different point processes, for a discriminating test. |
| A common zero-derived phase mask improves interscale orthogonality. | A common unit-modulus Mellin phase leaves the dilation Gram matrix unchanged. It may still affect localization or performance through a noncommuting physical channel. |
| Any \(\Xi\)-shaped or warped filter is physically realizable. | Positivity, finite energy, reconstruction, conditioning, physical time duration, and implementation must be checked. A nonlinear warp does not automatically preserve positive definiteness. |
| Infinitely many ideal scale states imply infinite capacity in a fixed band. | The mathematical family spans an unbounded scale axis. Finite RF bandwidth, duration, sampling, power, and receiver observations constrain an actual device. |

The source behind the physical nonlinear distinction is standard RF device modeling; the quadratic counterexample below also establishes it directly. [S6]

---

# 3. Fix the physical meaning of “without bleed”

The default target is **powers-of-two scaling**. An additive carrier lattice, such as \(f_n=f_0+2n\Delta f\), is a different target and should be retained as a conventional control.

On an ideal linear time-invariant wire or RF channel,

\[
Y(f)=H_{\mathrm{RF}}(f)X(f).
\]

There is no frequency conversion in this model. Finite observation windows, overlapping modulation spectra, timing/frequency errors, channel variation, and nonlinearities are separate mechanisms that can impair recovery.

For a rectangular symbol interval of duration \(T\), equally spaced complex tones satisfy the elementary identity

\[
\frac1T\int_0^T e^{2\pi i(n-m)t/T}\,dt=\delta_{mn}.
\]

This gives the basic non-zeta orthogonality control. Do not benchmark a sophisticated scale receiver only against an incorrectly synchronized or deliberately underpowered conventional receiver.

Define each claimed form of “bleed” operationally:

- **Basis overlap:** nonzero off-diagonal entries of the weighted synthesis Gram matrix.
- **Channel-induced mixing:** off-diagonal entries of the effective channel after a specified analysis/synthesis pair.
- **Recovery error:** EVM, NMSE, uncoded BER, or coded block error rate under a specified noise and estimation model.

Zero basis overlap is not the same as zero recovery error in noise. Orthogonality before the channel need not survive the channel. Perfect equalization with oracle coefficients does not establish performance with estimated coefficients.

For dyadic carrier centers in a fixed positive band, the number of available centers is at most

\[
1+\left\lfloor\log_2(f_{\max}/f_{\min})\right\rfloor,
\]

before accounting for each waveform's occupied bandwidth and guards. The scale transform does not remove this elementary geometric constraint.

---

# 4. Mathematical conventions: coordinates, energy, and transforms

## 4.1 Dimensionless frequency

Let \(f>0\) be physical frequency in Hz and choose a recorded reference \(f_{\mathrm{ref}}>0\). Define

\[
q=f/f_{\mathrm{ref}},\qquad u=\log q.
\]

Never take the logarithm of a dimensional frequency without specifying the reference.

For a positive-frequency spectrum \(X(f)\), use

\[
g(q)=\sqrt{f_{\mathrm{ref}}}\,X(f_{\mathrm{ref}}q),
\]

so that

\[
\int_0^\infty |g(q)|^2\,dq
=
\int_0^\infty |X(f)|^2\,df.
\]

For a real RF waveform the negative-frequency conjugate is also required; record whether energy is one-sided analytic-signal energy or full real-signal energy. Do not silently lose the corresponding factor.

## 4.2 Unitary change of coordinates

Define

\[
(Ug)(u)=h(u)=e^{u/2}g(e^u).
\]

Then, by \(dq=e^u du\),

\[
\int_{\mathbb R}|h(u)|^2du
=
\int_0^\infty|g(q)|^2dq.
\]

This is the normalization to implement. On a grid, use weighted samples or an explicitly weighted matrix inner product, not unweighted Euclidean norms of differently sampled arrays.

## 4.3 Fourier and Mellin signs

Use the following Fourier convention throughout the code:

\[
G(\tau)=\int_{\mathbb R}h(u)e^{-i\tau u}du,
\qquad
h(u)=\frac1{2\pi}\int_{\mathbb R}G(\tau)e^{i\tau u}d\tau.
\]

With the classical Mellin transform

\[
(\mathcal M g)(s)=\int_0^\infty g(q)q^{s-1}dq,
\]

we have

\[
G(\tau)=(\mathcal M g)(1/2-i\tau).
\]

The plus-sign convention \(1/2+i\tau\) is equally valid after reversing \(\tau\). Do not mix them silently. Here \(\tau\) is a dimensionless angular frequency conjugate to log-scale; it is **not an RF frequency in Hz**.

Plancherel gives

\[
\|g\|_{L^2(dq)}^2
=\|h\|_{L^2(du)}^2
=\frac1{2\pi}\int|G(\tau)|^2d\tau.
\]

The \(1/2\) arises from using \(dq\). With Haar measure \(dq/q\) and a different normalization, a line with real part zero is natural. The coincidence with the zeta critical line is a useful representational alignment, not a proof of RH.

## 4.4 Dilation becomes translation

Define the energy-preserving upward-frequency dilation

\[
(D_a g)(q)=a^{-1/2}g(q/a),\qquad a>0.
\]

Then

\[
UD_a g(u)=h(u-\log a),
\qquad
\mathcal FUD_a g(\tau)=e^{-i\tau\log a}G(\tau).
\]

These identities follow directly by substitution and should be recovered numerically before any zeta experiment. Mellin-based wideband modulation has existing engineering precedent; this project is not claiming that scale modulation itself is new. [S4]

---

# 5. The exact multiplicative Nyquist problem

Let \(L=\log2\), and synthesize a family

\[
g_n=D_{2^n}g,\qquad n\in\mathbb Z.
\]

For the inner product \(\langle a,b\rangle=\int\overline a b\), write

\[
W(\tau)=|G(\tau)|^2.
\]

The scale correlation is

\[
R[k]=\langle g_0,g_k\rangle
=\frac1{2\pi}\int_{\mathbb R}W(\tau)e^{-ikL\tau}d\tau.
\]

Thus ideal unit-energy, zero-interscale-overlap signaling requires

\[
R[k]=\delta_{k0}.
\]

This is a Nyquist condition in log-scale, rather than in ordinary time. It is a mathematically meaningful starting point, but says nothing yet about a finite transmitted symbol block.

## 5.1 A complete non-zeta solution

Let

\[
\Omega=2\pi/L,
\qquad
P_W(\tau)=\sum_{j\in\mathbb Z}W(\tau+j\Omega).
\]

For nonnegative integrable \(W\), the orthonormality condition is equivalent to

\[
\boxed{P_W(\tau)=L\quad\text{almost everywhere}.}
\]

**Derivation.** Decompose the correlation integral into intervals of length \(\Omega\). Since \(e^{-ikL j\Omega}=1\),

\[
R[k]=\frac1{2\pi}\int_I P_W(\tau)e^{-ikL\tau}d\tau.
\]

These are the Fourier coefficients of the periodized power spectrum, with the displayed normalization. The constant \(L\) gives \(R[0]=L\Omega/(2\pi)=1\) and all other coefficients zero. Conversely, uniqueness of Fourier coefficients in \(L^1\) gives the constant periodization.

A rectangular solution is

\[
W(\tau)=L\,\mathbf 1_{[-\pi/L,\pi/L]}(\tau).
\]

Choosing \(G=\sqrt W\),

\[
h(u)=L^{-1/2}\operatorname{sinc}(u/L),
\quad
\operatorname{sinc}(x)=\frac{\sin(\pi x)}{\pi x},
\]

and

\[
g(q)=q^{-1/2}h(\log q).
\]

This ideal function has tails over the full positive-frequency axis. Truncation to a physical band changes its Gram matrix. It is an exact mathematical control, not a ready-made finite-band antenna waveform.

## 5.2 A general normalization that preserves selected zeros

Choose a nonnegative integrable seed \(V\) whose periodization

\[
P_V(\tau)=\sum_j V(\tau+j\Omega)
\]

is finite and strictly positive almost everywhere. Define

\[
\boxed{W(\tau)=\frac{L V(\tau)}{P_V(\tau)}.}
\]

The denominator is periodic. Therefore

\[
\sum_jW(\tau+j\Omega)=L,
\]

and the family is orthonormal in the ideal model. Zeros of \(V\) are preserved wherever the denominator is nonzero. For numerical or physical robustness, impose and report an appropriate denominator floor on the implemented domain rather than hiding singular divisions.

This is important: **many seeds, including seeds with no arithmetic content, can be normalized to satisfy exactly the same ideal orthogonality condition.** Zeta cannot earn its place merely by producing zero off-diagonal correlations after this construction.

A meaningful comparison asks which seeds yield better finite-band retention, physical time localization, noise behavior, PAPR, or implementation cost after the identical normalization and constraints.

## 5.3 What a Xi-seeded construction actually means

Define

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad
\Xi(\tau)=\xi(1/2+i\tau).
\]

The critical-line real zeros of \(\Xi\) supply optional notch locations. This definition does not assume every nontrivial zero lies on the critical line. [S7]

A candidate seed is

\[
V(\tau)=r(\tau)|\Xi(\tau)|^2,
\]

with a specified nonnegative envelope \(r\), followed by the periodization normalization above. If valid, one may choose

\[
G(\tau)=\Xi(\tau)\sqrt{\frac{Lr(\tau)}{P_V(\tau)}}.
\]

Do not silently replace this with a Gaussian carrying a few zero-centered notches and call them the same object. The starter implements the latter as a **generic zero-location control**, not \(\Xi\) evaluation.

The completed function's gamma factor strongly changes amplitude and numerical dynamic range. Compare raw completed-function designs, explicitly de-enveloped designs, and location-only notch designs as different families. A warp \(\Xi(\alpha\tau+\beta)\) has tuning parameters and must consume the same optimization budget as matched non-zeta warps.

## 5.4 Phase invariance: a required null test

Replacing \(G\) by \(e^{i\theta(\tau)}G\), with real \(\theta\), leaves \(W\) unchanged. Hence it leaves every ideal dilation Gram entry unchanged.

This rules out a claimed **ideal orthogonality** improvement from a common phase-only mask. It does not rule out improvements to other properties, or effects after a noncommuting channel or a finite projection. Keep those claims separate.

---

# 6. Linear scale-copy channels and arithmetic equalization

## 6.1 Start with an explicitly synthetic linear model

On \(L^2(\mathbb R,du)\), define

\[
(S_nh)(u)=h(u-\log n).
\]

Then \(S_mS_n=S_{mn}\) and \(\|S_n\|=1\). For real \(\sigma>1\), set

\[
\mathcal C_\sigma=\sum_{n\ge1}n^{-\sigma}S_n.
\]

Absolute convergence of \(\sum n^{-\sigma}\) gives convergence in operator norm. Its log-Fourier multiplier is

\[
H_\sigma(\tau)=\sum_{n\ge1}n^{-\sigma}e^{-i\tau\log n}
=\zeta(\sigma+i\tau).
\]

The Dirichlet series/Euler product identities used here are in their ordinary absolutely convergent domain. [S1]

The corresponding physical-frequency operation is a weighted sum of **normalized spectral dilations** \(D_n\). It would need deliberate signal processing or a justified physical channel. It is not the transfer function of an ordinary passive linear time-invariant antenna, because it mixes physical frequencies.

## 6.2 Dyadic geometric mixing: an exact control

For \(|a|<1\),

\[
\mathcal C_{2,a}=\sum_{j\ge0}a^jS_2^j=(I-aS_2)^{-1}.
\]

Therefore

\[
\boxed{\mathcal E_{2,a}=I-aS_2}
\]

is its inverse. On a discrete scale index with zero initial state,

\[
y_j=x_j+a y_{j-1},\qquad x_j=y_j-a y_{j-1}.
\]

This is an exact two-tap cancellation theorem **for the stated linear geometric channel**. The infinite-series convergence condition is unnecessary for a finite triangular recurrence, but remains necessary for the stated infinite operator argument.

For a truncation after \(J\),

\[
(I-aS_2)\sum_{j=0}^{J}a^jS_2^j
=I-a^{J+1}S_2^{J+1}.
\]

Retain this boundary residual in tests. Unknown out-of-band inputs cannot be removed merely by setting them to zero inside the simulator.

If white independent scale-index noise of variance \(v\) is added after the channel, two-tap inversion gives interior variance \(v(1+|a|^2)\), not \(v\). Exact noiseless cancellation is not free noise cancellation.

## 6.3 General integer mixing: Möbius inversion

The Möbius function is defined by \(\mu(1)=1\), \(\mu(n)=0\) when a prime square divides \(n\), and \(\mu(n)=(-1)^r\) when \(n\) is the product of \(r\) distinct primes.

Use the divisor identity

\[
\sum_{d\mid k}\mu(d)=\delta_{k1}.
\]

For \(\sigma>1\), define

\[
\mathcal E_\sigma=\sum_{n\ge1}\mu(n)n^{-\sigma}S_n.
\]

Both operator series converge absolutely. The coefficient of \(S_k\) in their product is

\[
\sum_{d\mid k}\mu(d)d^{-\sigma}(k/d)^{-\sigma}
=k^{-\sigma}\sum_{d\mid k}\mu(d),
\]

so

\[
\boxed{\mathcal E_\sigma\mathcal C_\sigma=I.}
\]

The standard Dirichlet convolution and inversion identities support this calculation. [S2]

Equivalently, prime by prime,

\[
\mathcal C_\sigma=\prod_p(I-p^{-\sigma}S_p)^{-1},
\quad
\mathcal E_\sigma=\prod_p(I-p^{-\sigma}S_p).
\]

This is a promising **structured implementation**, not yet an advantage over a competent generic solver on the same problem.

## 6.4 The best first finite implementation

Use one-indexed coefficient arrays \(x[1],\ldots,x[N]\), and define

\[
y[k]=\sum_{d\mid k}w[d]x[k/d].
\]

The exact control takes \(w[n]=1/n^2\). Its inverse is

\[
x[k]=\sum_{d\mid k}\frac{\mu(d)}{d^2}y[k/d].
\]

Define a finite shift \(T_p x[k]=x[k/p]\) when \(p\mid k\), and zero otherwise. Then cascading \(I-p^{-2}T_p\), for primes through \(N\), gives the same inverse on indices through \(N\).

This finite triangular model retains the needed lower indices and has diagonal coefficient one. It is invertible without assuming anything about zeta zeros. It is an algebra calibration, not an RF measurement model.

The starter checks three calculation routes: divisor-sum inversion, a generic recursive inverse, and the prime cascade. A separate product-index loop checks the convolution implementation. These are different decompositions written in the same session, not fully independent external witnesses.

## 6.5 General weights require a general inverse

For Dirichlet convolution \((w *_D b)[n]=\sum_{d\mid n}w[d]b[n/d]\), an inverse exists when \(w[1]\ne0\). It obeys

\[
b[1]=1/w[1],
\qquad
b[n]= -\frac1{w[1]}\sum_{\substack{d\mid n\\d>1}}w[d]b[n/d].
\]

The shortcut \(b[n]=\mu(n)w[n]\) requires the appropriate **complete multiplicativity**, including \(w[p^r]=w[p]^r\). Ordinary multiplicativity only for coprime arguments does not suffice for two-tap prime factors.

Mutation control: alter \(w[4]\) while leaving \(w[2]\) unchanged. The naive Möbius-weight shortcut should fail; the generic recurrence should still invert the finite model. The starter includes this test.

## 6.6 Truncation is a separate operator

If both infinite filters are cut off at \(N\), their product is the identity in coefficients through \(N\), but generally has residual coefficients between \(N+1\) and \(N^2\). For example,

\[
(1+\tfrac14 S_2)(1-\tfrac14 S_2)=1-\tfrac1{16}S_4.
\]

Likewise, projecting a waveform onto a finite measured band can break identities that hold on the full scale axis. A finite cyclic FFT shift, a zero-padded shift, and an actual physical band crop are different boundary conditions.

---

# 7. What prime coordinates expose—and what they cannot create

Unique factorization gives

\[
n=\prod_p p^{v_p(n)},\qquad \log n=\sum_p v_p(n)\log p.
\]

A formal Dirichlet series can be represented by a multivariate power series via

\[
n^{-s}\longleftrightarrow\prod_p z_p^{v_p(n)},\qquad z_p=p^{-s}.
\]

This is the relevant Bohr-transform structure; ordinary Dirichlet-series theory has a rigorous connection to Fourier analysis on an infinite-dimensional torus. [S5]

For a finite coefficient dictionary, the prime-exponent description is an exact relabeling and can make a convolution or a prior easier to represent. Do not infer independently measurable prime channels from that relabeling. At a fixed spectral parameter, all \(z_p=p^{-s}\) are tied to that same parameter. A finite physical observation of a mixture is not an arbitrary observation of the full torus.

For an invertible coordinate change, transform the noise covariance and regularization consistently. A unitary change preserves singular values. A nonunitary change may alter the Euclidean condition number, but that does not establish an improved noise-aware inverse problem.

**Meaningful opportunities:** reduced memory, sparse operations, better parameter sharing when the model is correct, improved estimation with a justified prior, or a more efficient solver.

**Not a valid opportunity:** recovering an unobservable component solely by renaming its coordinates.

A fair arithmetic experiment must include a generic triangular/Dirichlet solver, not only a dense cubic-cost matrix inversion, as a cost baseline.

---

# 8. The nonlinearity boundary: an explicit hostile probe

Take a real passband input with two tones,

\[
x(t)=\cos(2\pi f_1t)+\cos(2\pi f_2t),
\]

and a quadratic device

\[
F(x)=x+\alpha x^2.
\]

The cross term in \(x^2\) is

\[
2\cos(2\pi f_1t)\cos(2\pi f_2t)
=\cos(2\pi(f_1-f_2)t)+\cos(2\pi(f_1+f_2)t).
\]

These sum/difference products are not generally integer-scaled copies of either input tone. A cubic polynomial adds further mixed products. This is the standard intermodulation mechanism. [S6]

Moreover,

\[
F(x+y)-F(x)-F(y)=2\alpha xy,
\]

so superposition fails. Harmonic amplitude and phase depend on the data symbols themselves. A second harmonic of a modulated carrier carries a transformed symbol, not necessarily the original symbol linearly copied.

The starter uses coherent bins \(f_1=5\), \(f_2=9\), \(\alpha=0.1\) on a 256-sample periodic record. It observes sum/difference bins 14 and 4 with cosine amplitudes 0.1. This is a counterexample to the universal linear-harmonic-copy assumption, not a measurement of an actual amplifier.

## Separate physical models to implement later

**P0: linear time-invariant propagation.** Frequency response and additive noise; no synthetic harmonic generation.

**P1: wideband delay–scale propagation.** For example,

\[
y(t)=\sum_{\ell=1}^{K}c_\ell\sqrt{a_\ell}\,x(a_\ell(t-d_\ell))+\eta(t),\qquad a_\ell>0.
\]

This is a linear time-varying model. Record scale and delay conventions explicitly. Delay and dilation do not commute; a scalar Mellin multiplier does not automatically diagonalize the full model. ODSS is relevant prior work, not a synonym for every log-FFT receiver. [S4]

**P2: nonlinear real-passband model.** Start with \(a_1x+a_2x^2+a_3x^3\), then consider memory or clipping only after controls pass. Sample sufficiently fast to prevent the modeled harmonics/intermodulation from aliasing, or use a documented oversampling/filtering chain. A complex-baseband cubic model such as \(z+\alpha z|z|^2\) is useful for in-band distortion, but it is not by itself a model of real-passband second-harmonic generation.

**A0: synthetic arithmetic scale-copy model.** The linear operator in Section 6, clearly labeled synthetic.

**A1: synthetic arithmetic model with broken weights/boundaries.** Perturb complete multiplicativity, crop observations, and add unknown lower-band inputs.

Do not calibrate only A0 and then announce success on P2.

---

# 9. Where the Riemann connection is exact

## 9.1 Müntz's centered operator

For a sufficiently regular function \(f\), define

\[
(Pf)(q)=\sum_{n\ge1}f(nq)-\frac1q\int_0^\infty f(v)dv.
\]

A safe sufficient starting class is \(f\in C_c^\infty(0,\infty)\). The classical identity is

\[
\mathcal M(Pf)(s)=\zeta(s)\mathcal M f(s),\qquad 0<\Re s<1.
\]

Báez-Duarte's paper gives the operator, Müntz formula, and a carefully qualified dilation-closure connection to RH. The theorem's hypotheses matter. It is not a claim that every dilation family provides an RH criterion. [S3]

The centered operator is not the raw absolutely convergent channel of Section 6 transported unchanged into the strip. Its cancellation term, domain, scale direction, and implementation all need explicit treatment.

A concrete optional analytic control uses \(f(q)=e^{-q}\):

\[
(Pf)(q)=\frac1{e^q-1}-\frac1q,
\qquad
\mathcal M(Pf)(s)=\Gamma(s)\zeta(s)
\quad(0<\Re s<1).
\]

Evaluate the small-\(q\) difference stably, for example using its local expansion

\[
-\frac12+\frac q{12}-\frac{q^3}{720}+\frac{q^5}{30240}+\cdots,
\]

and compare quadrature with \(\Gamma(s)\zeta(s)\), increasing precision and integration range. This analytic control is **specified but not run** in the bundled starter. A numerical agreement would be an implementation check, not a new proof of the source theorem.

## 9.2 Zeros are not automatically extra usable channels

In the absolutely convergent Euler-product regime, there are no zeta zeros. Thus the stable arithmetic inverse constructed there does not exploit nontrivial zeros. [S1, S7]

On a critical-line multiplier model, a zero of \(m(\tau)=\zeta(1/2+i\tau)\) makes \(1/m\) singular. The precise consequence depends on the observation space:

- In a finite diagonal matrix, an exactly sampled zero can produce an exact null and rank loss.
- On \(L^2\) with Lebesgue measure, isolated zeros do not provide nonzero functions supported only on those points. Multiplication can remain injective on its natural domain.
- Nevertheless, norm-one wave packets concentrated near a continuous zero have output norm tending to zero. Therefore there is no uniformly bounded inverse across that region.

For the last statement, choose normalized spectral packets supported on \((\gamma-\epsilon,\gamma+\epsilon)\). Their output norm is bounded above by

\[
\sup_{|\tau-\gamma|<\epsilon}|m(\tau)|,
\]

which tends to zero. No assumption of simple zeros is needed.

This is an inverse-problem conditioning issue, not automatically a useful guard channel. Notches may be useful when placed in an interference path or a designed pulse, but notching the desired signal's only measurement does not create capacity.

## 9.3 RH is not a prerequisite

Use finite, explicitly supplied numerical critical-line zero ordinates. Do not assume completeness of an unverified zero table or assume all nontrivial zeros lie on the line. The experiments do not require a proof of RH, and their success would not prove RH.

---

# 10. The exploratory zero–prime frame

This is an optional side track, not the default physical architecture. For \(M\) zero ordinates \(\gamma_k\) and \(N\) primes \(p_n\), define

\[
R_{kn}=M^{-1/2}e^{-i\gamma_k\log p_n}.
\]

The Gram matrix is

\[
(R^*R)_{mn}=\frac1M\sum_k e^{i\gamma_k\log(p_m/p_n)}.
\]

Measure mutual coherence, singular values, rank, and noise-aware recovery conditioning. Do not conflate column normalization with orthogonality.

## Mandatory comparisons

Use a partial DFT with the same \(M\ge N\), random phase frames, generic orthonormal frames, and point-process/coordinate controls. A partial DFT already has exact orthonormal columns in ideal arithmetic, so no candidate can beat zero coherence there. Search for a constrained robustness or cost advantage instead.

A row permutation \(P\) gives

\[
(PR)^*(PR)=R^*R.
\]

The same holds for any common unitary left multiplication. Row permutation is a **null/invariance control**. It becomes operationally meaningful only if a separately specified row-dependent channel or ordering constraint is held fixed—and then the test concerns that interaction, not the bare frame Gram matrix.

For a real surrogate, permute spacings and cumulatively reconstruct a different point set, or generate a matched-span/density point process. Record that a raw-gap surrogate and an unfolded-density surrogate answer different questions. Endpoint matching, affine rescaling, and truncation are transformations of the candidate and must be disclosed.

For a complete two-factor test, compare all four cells:

| | Prime-log columns | Matched generic columns |
|---|---|---|
| Actual zero rows | candidate | zero-only control |
| Surrogate rows | prime-only control | neither structure |

Use identical dimensions, spans, tuning budgets, and precision. Without all four cells, do not claim a mixed zero–prime effect.

For full-rank \(R\), replacing it by \(R(R^*R)^{-1/2}\) makes its columns orthonormal. That is a generic whitening operation, not evidence of a zeta-specific property. Compare the raw and whitened versions and charge their computation/conditioning costs.

---

# 11. Fair physical observations, noise, and resource accounting

Every physical simulation must declare:

**Signal resources:** sample rate, positive/negative-frequency convention, occupied physical band, block duration, number of independent payload symbols, guard intervals, pilots, coding rate, and total transmitted energy.

**Channel resources:** coefficient knowledge, estimation budget, synchronization accuracy, channel stationarity assumptions, observation bandwidth, and front-end effects.

**Computational resources:** transform sizes, interpolation method, training steps, matrix factorizations, arithmetic counts, peak memory, and inference latency on a recorded environment.

These are matched constraints, not optional metadata.

If a physical sample vector \(y\) has noise covariance \(C_\eta\), and the receiver computes \(z=Sy\), then

\[
C_z=SC_\eta S^*.
\]

An arbitrary log-grid interpolation matrix \(S\) does not preserve white noise. If it oversamples, its outputs can be correlated or linearly dependent. Never count them as newly independent measurements.

For a linear effective synthesis/channel matrix \(A\), include:

- a matched-filter receiver;
- a stable dense least-squares/SVD or QR reference;
- a correctly noise-weighted linear MMSE receiver;
- the structure-exploiting receiver with the same information and regularization rights.

For iid symbols with variance \(E_s\), the linear MMSE expression is

\[
\widehat d=(A^*C_\eta^{-1}A+E_s^{-1}I)^{-1}A^*C_\eta^{-1}y.
\]

Implement a solve/factorization rather than an explicit inverse. Handle singular covariance by restricting to the supported observation subspace or a documented regularization—not by silently inserting convenient iid noise after interpolation.

For nonlinear channels, a global linear oracle is not the correct ultimate comparator. Include a justified nonlinear estimator or predistortion/equalization baseline once that phase is reached.

---

# 12. Experimental program and gates

## E0 — Calibration and mutation controls: implemented

Run the bundled exact arithmetic tests, frame invariances, periodization checks, and two-tone nonlinear counterexample. Validate the data manifest. Reproduce the baseline before changing implementation.

**Pass:** exact identities hold in the declared finite model; numerical errors remain below tolerances; negative/mutation controls fail the intended false assumption.

**Fail:** an identity test fails, a null control spuriously improves the metric, or a deliberately broken assumption goes undetected. Repair the harness before performance claims.

## E1 — Sampled physical waveform baseline

Implement a uniform physical-frequency grid and a clear map between coefficients, spectra, and time-domain samples. Construct dilated spectral pulses from the dimensionless definitions. Initially keep at most 16 streams and 4096 samples per block; expose these as configuration parameters, not fixed scientific limits.

Measure the weighted Gram matrix before and after physical band cropping and finite time-windowing. Validate Parseval normalization and reconstruction. Establish linear-channel QPSK recovery using a generic dense decoder. Add delay, scaling, and frequency offset one at a time.

Store the raw dilation family and any numerically orthogonalized control separately. Orthogonalizing a cropped family changes the transmitted waveforms; it does not show the original finite-band dilation family was orthogonal.

**Pass:** a correctly modeled reference receiver recovers noiseless payloads within declared tolerance and all energy/resource accounting closes. If rank is insufficient, report it instead of forcing a solve.

## E2 — Arithmetic structure, estimation, and model mismatch

Compare direct Möbius inversion, the prime cascade, a generic sparse triangular/Dirichlet solver, and a dense oracle on the same finite arithmetic channel. The exact known-coefficient versions should agree, not produce mysterious BER differences.

Next perturb weights, especially prime powers; introduce phase errors, out-of-band inputs, missing bins, coefficient-estimation error, and finite-band crops. Measure when factor sharing helps estimation and when misspecified arithmetic priors hurt.

**Discriminator:** a structure-exploiting method may reduce computation or estimation variance on truly structured channels. It should not retain a claimed universal advantage after its assumed structure is deliberately broken.

Use a complete two-factor contrast: structured versus broken channel, and arithmetic-aware versus generic decoder. Freeze the primary metric and compute any interaction only after all four cells exist.

## E3 — Zero–prime frame screen

Expand the small starter screen over bounded \((M,N)\) grids and separate zero-index ranges. Compare against DFT and genuinely different surrogate ensembles. Record both raw and any span-normalized views.

**Pass for continuation:** a specified constrained property survives matched surrogates, multiplicity correction/holdouts, and whitening/coordinate controls. Lower coherence than one random draw is not sufficient.

**Fail for that claim:** an alleged effect is exactly row-order invariant, disappears after a fair comparator is introduced, or depends on a tuning advantage.

## E4 — Riemann-seeded multiplicative Nyquist bands

Implement the generic periodization construction first. Then test location-only zeta notches, actual \(\Xi\)-derived seeds, and matched generic notches/envelopes.

At equal physical resources, evaluate physical-band energy retention, duration/leakage tradeoffs, off-grid scale errors, PAPR in the reconstructed physical time waveform, and receiver noise amplification. Compute final Gram matrices after all projections, not only on the convenient Mellin grid.

Every candidate receives the same parameter count and optimization budget. Freeze the candidate and generic optimizer before holdout comparison. A common phase-only change is tested against the invariance theorem and may be evaluated only for metrics it can actually change.

**Pass for a zeta-specific hypothesis:** an advantage remains over a comparably optimized generic design and survives the physical projections.

## E5 — Actual nonlinear communication

Test P2 with new symbols and several drive levels, including a linear-limit control. Preserve cross-stream intermodulation. Match physical bandwidth, mean energy, peak constraints, and noise placement across methods.

Include a model-appropriate non-zeta nonlinear receiver. A method tuned to the synthetic arithmetic channel is expected to need modification; failure on P2 diagnoses its scope, not a failure of an unrelated identity.

**Pass for a physical claim:** benefits persist against the relevant nonlinear comparator on fresh regimes, not merely against a linear receiver whose model is knowingly wrong.

## E6 — Hardware relevance, only after simulation evidence

An antenna's broadband geometry is a separate engineering layer. No antenna purchase or build is needed for E0–E5. A later measured front-end response can be inserted as \(H_{\mathrm{RF}}(f)\), together with measured nonlinear behavior and noise.

A later self-similar or log-periodic front end may be compatible with the bandwidth requirements, but it does not implement a Mellin decoder or Möbius inverse by itself. Electromagnetic simulation, calibration, legal transmission conditions, and safety are distinct future tasks, not implied permissions.

---

# 13. Metrics, statistical discipline, and verdicts

## Core metrics

Record separately:

\[
\mu_{\mathrm{frame}}=\max_{m\ne n}|\langle\tilde g_m,\tilde g_n\rangle|,
\quad
\kappa_2(A)=\sigma_{\max}(A)/\sigma_{\min}(A),
\]

alongside numerical rank, EVM, NMSE, BER/block error counts, physical occupied bandwidth, transmitted energy per useful bit, pilot/guard overhead, physical-time PAPR, memory, and runtime.

Use \(\mu_{\mathrm{Mobius}}\) or an explicit name in code when referring to the number-theory function; do not confuse it with frame coherence or probe-availability notation.

A small coherence does not alone certify good conditioning. For normalized columns, the crude bound \(\|R^*R-I\|_2\le(N-1)\mu_{\mathrm{frame}}\) already shows why dimension matters. Inspect singular values in the numerical implementation.

## Predeclare the performance gate

Before a substantial sweep, choose one primary outcome and a minimum practically interesting effect. One possible gate is a 0.5 dB reduction in **transmitted** \(E_b/N_0\) at BER \(10^{-3}\), without increased physical bandwidth/block duration or more than a predefined overhead allowance. These values are a proposed protocol, not an established optimal threshold.

A computation-focused alternative may target at least a twofold runtime or memory reduction at indistinguishable error performance. Choose the gate before looking at holdouts. Do not retrospectively exchange a failed BER objective for an unregistered PAPR success and call it the same claim.

Report a Pareto comparison when there are tradeoffs; do not hide worse latency or lower net payload rate inside one composite “truth” or “quality” score.

## Holdouts and uncertainty

The included seed `20260911` is a **calibration seed**, not a fresh holdout. Freeze code/configuration hashes before a separate evaluator generates or reveals holdout seeds and channel cases. A deterministic seed does not by itself provide blinding.

Use paired input/noise/channel realizations across receivers, with enough independent blocks to support uncertainty estimates. Estimate intervals at the block level when errors are correlated. Zero observed errors means zero out of a stated sample count, not a zero true BER. Do not extrapolate a target-BER SNR crossing that the simulated range never brackets.

Archive all attempted candidate families and tuning budgets, including failures. Training examples, calibration controls, and chosen examples cannot also serve as fresh validation.

## Outcome vocabulary

**PASS / supported within scope:** a preregistered criterion is met with the stated uncertainty and controls.

**FAIL / refuted within scope:** a discriminator contradicts the claim or a necessary acceptance criterion fails.

**AMBIGUOUS:** numerical resolution, error-count uncertainty, or an unmodeled effect prevents a decision.

**UNVERIFIED:** the suitable experiment has not run.

A simulated positive result is not a universal theorem or a hardware demonstration. A finite arithmetic identity may be proved for its declared model even while its physical applicability remains unverified.

---

# 14. Initial claim ledger and research risks

| ID | Claim | Initial status and scope |
|---|---|---|
| C01 | The normalized log map preserves \(L^2\) energy and diagonalizes pure dilation. | **Disclosed:** substitution proof in Section 4. Discrete implementation still requires tests. |
| C02 | Constant periodization of Mellin power gives orthonormal dyadic translates. | **Disclosed:** Section 5, under stated integrability assumptions. |
| C03 | Zeta is necessary for ideal dyadic orthogonality. | **Refuted:** the rectangular/generic periodized construction is a counterexample. |
| C04 | Geometric dyadic linear mixing has a two-tap inverse. | **Disclosed:** Section 6; finite exact test also observed. |
| C05 | Completely multiplicative integer-scale mixing admits the stated Möbius inverse. | **Disclosed:** divisor calculation; finite exact tests observed. |
| C06 | An arbitrary harmonic-generating amplifier is this linear channel. | **Refuted as a universal statement:** quadratic two-tone counterexample. Applicability to a special engineered channel remains a separate question. |
| C07 | Prime-coordinate factorization can reduce computational or estimation cost. | **Conjectured for a useful communications regime:** algebra is established, comparative advantage unverified. |
| C08 | Row permutation or a common unitary row phase improves the bare frame Gram matrix. | **Refuted:** invariance proof and observed numerical controls. |
| C09 | Critical-line zeros automatically supply nonzero finite-energy null channels. | **Refuted as a general claim:** continuous and discrete observation spaces differ. |
| C10 | Zero-based coding or shaping beats optimized generic controls. | **UNVERIFIED.** |
| C11 | The proposed system improves a realistic nonlinear RF link. | **UNVERIFIED.** |
| C12 | The research proves RH or increases information by coordinate relabeling. | **Not a supported objective or inference.** |

## Diagnostic separation

Keep the following as separate fields rather than one score:

- **Contact / κ:** what physical or computational system was actually observed?
- **Pathway state / φ:** is there a constructible route to the claimed outcome with available tools? Lack of a route is not a disproof.
- **Source-map adequacy / σ_source:** are formulas, domains, citations, models, and conversions actually the right ones for the claim?
- **Commitment coupling / ρ:** could preference for the name or a successful-looking visualization bias candidate selection?
- **Probe availability / μ_probe:** is there a runnable discriminator, and what is missing?
- **Tool closure, independence, coherence, and discrimination:** record these separately, including shared software and derivation provenance.

An exact arithmetic success may resolve a mathematical pathway while leaving the physical source map unresolved. A code test and a symbolic argument written by the same model are not blind witnesses. The optional zero generation and residual calculation both use mpmath and must be labeled as shared-library checks.

## Obstruction classification

Use **pathway gap** for a missing candidate/algorithm, **probe gap** for a missing distinguishing test, **access gap** for unavailable measurements or tools, and **boundary** only for an actually established logical, physical, permission, or safety constraint.

The first major source-map risk is the leap from nonlinear RF to linear integer-scale mixing. The first major numerical risk is silently changing energy/noise normalization during log resampling. The first major experimental risk is declaring a zeta win over a weak comparator.

---

# 15. What has actually run in this package

The included starter is a calibration harness, not the planned transceiver.

**Observed environment:** Python 3.13.5. No third-party package is needed to run tests or the audit. The optional zero-data generation used mpmath 1.3.0 at 40 decimal digits, with residual evaluation at 55 digits using the same library. The zero file is numerical, not a rigorously certified or independently verified zero table. [S8]

**Observed test result:** 25 unit tests passed. The aggregate audit passed 13 calibration checks. Exact inversion used rational arithmetic on a finite coefficient model with cutoff \(N=96\); the dyadic gain was \(2/3\). The complete-multiplicativity mutation produced the expected nonzero residual \(1/17\) at index 4.

The exploratory frame used the first 32 supplied critical-line zero ordinates and primes

\[
2,3,5,7,11,13,17,19.
\]

| Frame / control | Maximum off-diagonal Gram magnitude |
|---|---:|
| Zero-ordinate × prime-log frame | 0.16146736413948087 |
| Partial DFT, same 32 × 8 shape | 5.368569792575578 × 10⁻¹⁶ |
| One raw-gap-permuted surrogate | 0.19434899413409853 |
| One matched-span uniform surrogate | 0.33016647485933237 |

The actual zero frame is not orthogonal. Its lower coherence than those two particular surrogate draws is **not** an ensemble result, an optimized comparison, or a communications advantage. The DFT control already achieves numerical orthogonality.

Row permutation changed the Gram matrix by at most \(1.11\times10^{-16}\); a common unit-modulus row phase changed it by at most \(6.84\times10^{-17}\), consistent with the exact invariances.

The finite-grid periodization probe used 8 tiles of 64 bins each. The maximum correlation over lags 1 through 8 was approximately \(2.87\times10^{-15}\) for a generic Gaussian seed and \(2.92\times10^{-15}\) for a Gaussian with zero-location notches. Both pass the same discrete normalization identity. This does **not** certify a continuous pulse, finite physical-band orthogonality, or \(\Xi\)-specific behavior.

The quadratic two-tone control detected the intended sum/difference products. No BER sweep, physical waveform reconstruction, ODSS reproduction, nonlinear decoder comparison, hardware test, or speedup benchmark has run.

**Raw evidence:** `results/reference_tests.txt`, `results/reference_audit.json`, and `data/critical_line_zeros_32.json`. The audit includes input values, source hashes, Gram matrices, surrogate point sets, sampled seeds/weights, and the two-tone records. Re-run rather than trusting this paragraph.

---

# 16. Repository map and first actions for the local model

The companion directory contains:

```text
riemann_band_lab/
  README.md
  RESEARCH_HANDOFF.md             # this self-contained specification
  START_HERE.txt                  # pasteable local-model / Codex instruction
  AGENTS.md                      # durable operating boundaries
  pyproject.toml
  Makefile
  sources.json
  MANIFEST.sha256
  rband/
    __init__.py
    __main__.py
    algebra.py                   # exact finite arithmetic operators
    spectral.py                  # small dependency-free spectral controls
    probes.py                    # aggregate reproducible audit
  tests/
    test_algebra.py
    test_spectral.py
  tools/
    check_sources.py
    generate_zeros.py             # optional; requires mpmath
  data/
    critical_line_zeros_32.json
  research/
    claims.jsonl
    experiments.jsonl
  results/
    reference_tests.txt
    reference_audit.json
    reference_checks.txt
```

From the project root:

```sh
python -m unittest discover -s tests -v
python tools/check_sources.py
python -m rband audit --json results/local_audit_001.json
```

The audit refuses to overwrite an existing result. Choose a new receipt name for every run. `make test`, `make lint`, and `make check` are convenience commands; the Python commands work without Make. Here `lint` is a small syntax/whitespace/JSON check, not a claim of full static type verification.

## Required opening behavior

Inspect the actual directory and instructions. If it is inside an existing Git repository, record repository root, branch, HEAD, and worktree status before modifying files. Do not discard unrelated changes. If no repository exists, work in this folder; do not invent repository history. A local research branch is appropriate only under the user's applicable authorization. No remote publish is authorized by this handoff.

Run E0 unchanged and record a fresh receipt. Check manifest hashes. Read the discrepancies and boundary notes before expanding the code. Do not simply continue a prior assistant's confident prose.

## First implementation task after E0

Build the smallest E1 physical waveform slice: explicit uniform frequency samples, energy-preserving spectrum/time conversion, a finite dyadic pulse family, its cropped weighted Gram matrix, and a correct dense recovery baseline. Add a test that intentionally drops the Jacobian and is caught. Add a resampling covariance check. Use at most a small matrix and one symbol block until these controls pass.

Keep the arithmetic channel separate. Do not start by adding zeta to a large simulator whose normalization and observation model are not yet validated.

---

# 17. Required experiment receipt and persistence rules

Every new experiment should append one machine-readable receipt with at least:

```json
{
  "schema_version": "1.0",
  "experiment_id": "E1_example_001",
  "claim_ids": ["C01", "C10"],
  "status": "UNVERIFIED",
  "physical_or_synthetic": "physical_sampled_model",
  "channel_model_id": "P0",
  "hypothesis": "Specify the discriminating claim before running",
  "acceptance_criteria": {},
  "config": {},
  "input_seed_manifest": [],
  "code_state": {"commit": null, "worktree_dirty": null, "file_hashes": {}},
  "normalization": {},
  "noise_model_and_covariance": {},
  "resource_budget": {},
  "baselines": [],
  "ablations_and_controls": [],
  "raw_artifacts": [],
  "metrics_with_uncertainty": {},
  "source_families": [],
  "shared_dependencies": [],
  "holdout_policy": {},
  "limitations": [],
  "next_verdict_changing_probe": ""
}
```

`null` means unknown or not applicable, never an invented clean worktree or a fabricated commit. The bundled calibration receipt has a smaller existing schema; preserve it and version any extension rather than pretending it already contains every future field.

For model criticism, retain raw and normalized/transported views. Declare the common basis, Fourier sign, ordering, and any phase operation before interpreting interference. A visual resemblance to a zeta plot is not a phase measurement.
Save durable mathematics, negative results, receipts, and open obligations in the repository. Re-entry should require only the files, not a model's remembered conversation. Finish each coding session with commands actually run, their outcomes, the current claim ledger, and one next verdict-changing probe.

---

# 18. Sources, provenance, and the scope of what they establish

The references below were checked for this setup. Formulas derived explicitly above are checkable derivations, not claims that the cited papers propose this transceiver. No novelty or exhaustive prior-art search has been completed.

**[S1] NIST Digital Library of Mathematical Functions, §27.4, “Euler Products and Dirichlet Series,” especially Eq. 27.4.3.**  
<https://dlmf.nist.gov/27.4>  
Supports the ordinary Dirichlet-series/Euler-product identity in \(\Re s>1\). Does not license raw convergence on the critical line.

**[S2] NIST DLMF, §27.5, “Inversion Formulas,” especially Eqs. 27.5.1–27.5.3.**  
<https://dlmf.nist.gov/27.5>  
Supports Dirichlet convolution and the Möbius divisor identity. The finite channel algebra and its boundary analysis are supplied explicitly in this handoff.

**[S3] Luis Báez-Duarte, “A general strong Nyman–Beurling criterion for the Riemann Hypothesis,” arXiv:math/0505453v1 (2005), §2.4 and the qualified theorems in §1.**  
<https://arxiv.org/abs/math/0505453>  
<https://arxiv.org/html/math/0505453v1>  
Supports the centered Müntz operator and Mellin multiplier identity, with hypotheses. It is not an RF realization or an antenna proposal.

**[S4] Arunkumar K. P. and Chandra R. Murthy, “Orthogonal Delay Scale Space Modulation: A New Technique for Wideband Time-Varying Channels,” arXiv:2111.10765v3 (2022), accepted in IEEE Transactions on Signal Processing.**  
<https://arxiv.org/abs/2111.10765>  
<https://arxiv.org/html/2111.10765v3>  
Prior work for delay–scale communication and Mellin transformations. Its particular performance results are not reproduced here. The paper also discusses limitations of exact robust biorthogonality with finite-duration pulses; do not assume all ideal conditions transfer to finite waveforms.

**[S5] Andreas Defant and Ingo Schoolmann, “\(\mathcal H_p\)-theory of general Dirichlet series,” arXiv:1811.09182v3 (2019), introduction and Bohr-transform setup.**  
<https://arxiv.org/abs/1811.09182>  
<https://arxiv.org/html/1811.09182>  
Supports the Dirichlet-series/torus connection. Does not supply independently accessible physical prime dimensions.

**[S6] Analog Devices, “IP3 and Intermodulation Guide” (2012).**  
<https://www.analog.com/en/resources/technical-articles/ip3-and-intermodulation-guide.html>  
Manufacturer technical reference for polynomial nonlinearity and intermodulation. The explicit quadratic counterexample is also derived and tested here.

**[S7] NIST DLMF, §§25.4 and 25.10, “Reflection Formulas” and “Zeros.”**  
<https://dlmf.nist.gov/25.4>  
<https://dlmf.nist.gov/25.10>  
Supports the completed zeta definition and the distinction between known critical-line zeros and the RH statement. No assumption of RH is needed for this project.

**[S8] mpmath documentation, “Zeta functions, L-series and polylogarithms,” including `zetazero` and `zeta`.**  
<https://mpmath.org/doc/current/functions/zeta.html>  
Supports the optional numerical API. Runtime version and precision are recorded in the generated data file. Library documentation is not an independent certification of that file's outputs.

Access dates and source families are machine-readable in `sources.json`. Several DLMF pages share the same reference family; multiple citations to them are not independent corroboration. HTML was used for the cited papers; no unseen figure analysis is claimed.

---

# 19. Final instruction to the research session

Preserve the creative objective: discover whether multiplicative-band structure is useful rather than prematurely reducing everything to a conventional carrier-allocation problem.

Pay for that freedom with discriminating tests. Maintain exact mathematical identities, physical model boundaries, noise and energy accounting, strong non-zeta baselines, complete controls, and durable negative results.

**Build the generic scale system correctly. Establish when arithmetic structure is actually present. Then make the Riemann zeros earn their place.**