# Arithmetic Gram and Lévy attempts: finite-event rigidity

Status: **RH NOT PROVED**. The lemmas below are proved in this round.
“New” here means newly established in this repository; no literature
priority or research novelty is claimed. Zero spectral data enter only the conditional
spectral control in Theorem 4, not an attempted positive construction.

## 1. A single event is an indefinite kernel update

Put `h_a(t)=(|t|-a)_+`, where `a>0`. Its anchored kernel is

\[
 K_{h_a}(t,u)=h_a(t)+h_a(u)-h_a(t-u).
\]

**Lemma 1 (exact event witness).** Neither `h_a` nor `-h_a` is CND.
At `t_1=3a/4`, `t_2=-3a/4`, the kernel matrix is

\[
 \begin{pmatrix}0&-a/2\\-a/2&0\end{pmatrix},
\]

whose eigenvalues are `a/2` and `-a/2`. Changing its sign leaves it
indefinite. Alternatively, coefficients `(1,1,-2)` at
`(3a/4,-3a/4,0)` have zero sum and CND quadratic form `a>0` for `h_a`.
For `-h_a`, coefficients `(1,-1)` at `(0,2a)` give `2a>0`.

At an arithmetic event `a=log q`, the actual contribution to `Psi` is
`-w_q h_a`, `w_q=Lambda(q)/sqrt(q)>0`. Its kernel is therefore not a
positive independent covariance increment or a PSD rank-one update.
Summing orthogonal prime-event Hilbert components cannot reproduce the
exact eventwise decomposition. Cross-event/Archimedean coupling would
have to do real work.

This does **not** say that the full kernel is indefinite. Indefinite
summands may cancel. A Schur complement is likewise not a positivity
proof unless its coupling estimate is proved independently.

## 2. Global CND growth and the finite-cutoff obstruction

**Lemma 2 (growth).** A continuous even CND function `f` with `f(0)=0`
satisfies `0<=f(t)<=C(1+t^2)`.

Proof. PSD of the anchored kernel first gives `f>=0`. Its matrix at
`t,2t` is

\[
 \begin{pmatrix}2f(t)&f(2t)\\ f(2t)&2f(2t)\end{pmatrix}.
\]

The nonnegative determinant gives `f(2t)<=4f(t)` when `f(2t)>0`,
and the same inequality is trivial otherwise. Let `M=max_{[1,2]} f`.
For `t>=1`, write `t=2^k u`, `1<=u<2`; then
`f(t)<=4^k M<=Mt^2`. Continuity covers the compact initial range and
evenness covers negative `t`. QED.

Let `F` be any finite set of prime-power labels `q>1` and let

\[
 \Psi_F(t)=A_\infty(|t|)-\sum_{q\in F}w_qh_{\log q}(t),
\]

with every Gamma/pole/Lerch term retained exactly in `A_infty`.
Set `L=(digamma(1/4)-log pi)/2`, `B=C/4-8`. Expanding only the
absolutely convergent Lerch series at large positive `t` gives the exact
identity

\[
 A_\infty(t)=4e^{t/2}+Lt+B
 -4\sum_{n\ge1}\frac{e^{-(4n+1)t/2}}{(4n+1)^2}.
\]

The `n=0` Lerch term cancels the pole's `4e^{-t/2}` term. Hence

\[
 \Psi_F(t)=4e^{t/2}
 +(L-\sum_{q\in F}w_q)t
 +B+\sum_{q\in F}w_q\log q+O(e^{-5t/2}).
\]

**Theorem 3 (finite cutoff no-go).** No such `Psi_F` is globally CND;
adding or subtracting any fixed Gaussian correction `b t^2` cannot make
it globally CND.

Proof. The exponential asymptotic contradicts Lemma 2. More explicitly,
`(Psi_F(2t)+4bt^2)/(Psi_F(t)+bt^2)` tends to infinity, so the displayed
two-point kernel determinant eventually becomes negative. QED.

For `F={q<=X}`, these functions nevertheless equal the full `Psi` on
`|t|<=log X`, and converge pointwise to it as `X→infinity`. Their
convergence is exact on growing windows, but **none** is a global
positive Lévy approximant. A scheme which changes the tail nonlocally
may escape this theorem; that change needs its own exact convergence and
positivity proof.

## 3. Polynomial growth already forces RH

**Lemma 3.** For Suzuki's exact `Psi`, a bound
`Psi(t)=O(1+t^2)` on `t>=0` implies RH.

Proof. Such a bound makes

\[
 H(z)=\int_0^\infty\Psi(t)e^{izt}\,dt
\]

holomorphic for `Im z>0`, by domination on compact sub-half-planes,
also after any number of `z` derivatives. Suzuki's unconditional
transform identity, obtained from the explicit arithmetic formula, is

\[
 H(z)=-z^{-2}\frac{\xi'}{\xi}(1/2-iz),\qquad \Im z>1/2.
\]

The identity theorem for meromorphic functions extends this equality
through the connected upper half-plane. Any zero of `xi(1/2-iz)` there
would give a nonremovable logarithmic-derivative pole; the nonzero factor
`z^{-2}` cannot remove it. This contradicts holomorphy of `H`. Thus `xi`
has no zeros with real part greater than `1/2`; its functional equation
excludes the other half. QED.

No zero ordinates were used in this argument. It is a direct consequence
of the arithmetic transform, not an estimate supplied by RH.

## 4. Finite-event rigidity, including Gaussian repairs

**Theorem 4 (finite-event rigidity).** Let `a_1,...,a_N>0` be distinct,
and `c_1,...,c_N,b` be real. Define

\[
 F(t)=\Psi(t)+\sum_{j=1}^N c_j h_{a_j}(t)+bt^2.
\]

Then

\[
 F\text{ is CND}
 \quad\Longleftrightarrow\quad
 \mathrm{RH},\quad c_1=\cdots=c_N=0,\quad b\ge0.
\]

In particular no nonzero finite alteration of prime-power weights,
including a deletion, duplication, or signed mutation, can yield a CND
function with the original Archimedean normalization. A Gaussian term
cannot repair it. Event times need not be prime logarithms for the theorem.

**Proof.** Suppose `F` is CND. Lemma 2 bounds `F` quadratically; the
finite ramp sum is `O(1+|t|)`. Subtracting it and `bt^2` bounds `Psi`
quadratically. Lemma 3 therefore gives RH.

At this point—and only as a conditional verification device—the
Nakamura–Suzuki theorem identifies the Lévy measure of `Psi` as a finite
purely atomic symmetric measure

\[
 \nu_\zeta=\sum_\gamma m_\gamma\gamma^{-2}\delta_\gamma,
\]

where `gamma` ranges over distinct real nonzero ordinates. Its Gaussian
coefficient is zero. The atoms are locally finite.

Use the Fourier convention
`hat f(x)=integral exp(-itx)f(t)dt`, extended to tempered distributions.
For any symmetric CND function

\[
 f(t)=\frac a2t^2+\int(1-\cos(tx))\nu(dx),
\]

distributional differentiation and Fourier transformation give the
positive tempered measure

\[
 \frac1{2\pi}\widehat{f''}=a\delta_0+x^2\nu(dx).
\]

These operations are legitimate even without finite second moments:
`x^2 nu` has polynomial growth since `nu` has finite mass outside
`[-1,1]`, and is finite on compact neighborhoods of zero by the Lévy
condition. The identity follows by pairing with Schwartz test functions.

Since `h_a''=delta_a+delta_{-a}`, applying it to our identity for `F`
gives

\[
 \frac1{2\pi}\widehat{F''}
 =2b\delta_0+\sum_\gamma m_\gamma\delta_\gamma
   +\frac1\pi\left(\sum_{j=1}^N c_j\cos(a_jx)\right)dx.
\]

This must be a positive measure. Its absolutely continuous part must
therefore be nonnegative: the other terms are singular and cannot pay
for negative density on a set of positive Lebesgue measure. By
continuity the trigonometric polynomial

\[
 T(x)=\sum_j c_j\cos(a_jx)
\]

must satisfy `T(x)>=0` everywhere. Its symmetric Cesàro mean is zero,
whereas its squared mean is

\[
 \lim_{R\to\infty}\frac1{2R}\int_{-R}^R T(x)^2\,dx
 =\frac12\sum_j c_j^2.
\]

These identities follow by integrating each cosine; distinct positive
frequencies have no constant cross term, irrespective of rational
relations. If `T>=0`, then `0<=T^2<=||T||_infty T`; averaging forces
the squared mean to vanish. Thus every `c_j=0`.

Finally `F=Psi+bt^2`; under RH `Psi` is bounded, so `b<0` would make
`F` negative eventually, contradicting CND. Hence `b>=0`. Conversely,
under RH the function `Psi` is CND and `bt^2` is CND for `b>=0`, so
their sum is CND. QED.

**Signed Lévy form of one event.** The same Fourier computation gives
the convergent identity

\[
 h_a(t)=\int_{\mathbb R}(1-\cos(tx))
             \frac{\cos(ax)}{\pi x^2}\,dx.
\]

It also follows by expanding the product and using
`integral (1-cos(tx))/(pi x^2)dx=|t|`. Near zero the factor
`1-cos(tx)` makes the integral finite; at infinity `x^{-2}` does so.
The density is **signed**, not a Lévy measure. This is the precise
failure of “positive event mass becomes positive Fourier-dual mass.”

**Control interpretation.** Deleting a prime event adds a nonnegative
ramp to `Psi`. If RH holds, scalar positivity survives that deletion.
Yet Theorem 4 says CND does not. Thus the special Suzuki implication
`Psi>=0 ⇒ Psi CND` must never be applied to a mutated formula. Negative
atoms of `Psi''` in event time are not themselves a refutation either:
CND requires its Fourier transform to be a positive measure, not that
`Psi''` itself be a positive measure in event time.

## 5. The origin forces heavy spectral moments

For `0<t<log 2` the prime sum is empty. Write `a=1/4` and

\[
 S_a(t)=\sum_{n\ge0}\frac{e^{-2(n+a)t}}{n+a}.
\]

Its derivative is `-2e^{-2at}/(1-e^{-2t})=-1/t+O(1)`. Comparison with
`S_1(t)=-log(1-e^{-2t})`, using the convergent digamma difference
series, gives

\[
 S_a(t)=-\log(2t)-\gamma_E-\operatorname{digamma}(a)+O(t).
\]

To justify the comparison limit, integrate the derivative in `a` between
`1` and `a`: the `1/(n+a)^2` part is dominated by a summable series,
and the extra `2t/(n+a)` part is `O(t log(1/t))` and tends to zero.
The derivative formula then improves the residual to `O(t)`.
Differentiating the exact Archimedean formula on this prime-free interval
and integrating from zero gives

\[
 \Psi(t)=\frac t2\log\frac1t
 +\frac{1-\gamma_E-\log(2\pi)}2t+O(t^2).
\]

In particular `Psi(t)/t→infinity`, independently of RH.

**Lemma 5 (moment obstruction).** Suppose symmetric positive Lévy
approximants

\[
 \psi_n(t)=\frac{a_n}2t^2+\int(1-\cos(tx))\nu_n(dx)
\]

with `a_n>=0` converge pointwise to `Psi`. Then their first absolute Lévy moments
cannot be uniformly bounded.

Proof. Since both terms are nonnegative, convergence at `t=1` bounds
`a_n`. If `integral |x|nu_n(dx)<=M` uniformly, the elementary bound
`1-cos y<=2|y|` gives
`psi_n(t)<=Ct^2+2M|t|`. Pass to the limit and divide by positive `t`;
this contradicts the displayed cusp. QED.

This allows finite positive measures with increasingly heavy tails.
It forbids arguments based on uniform first-moment control, and hence
uniformly bounded mass together with uniformly bounded second moments.
It does not rule out every arithmetic Lévy construction.

## 6. What survives and what remains unpaid

Refuted construction classes:

- independent PSD additions of the literal prime-event ramps;
- globally CND finite event truncations with exact Archimedean terms;
- Gaussian repairs of those truncations or of finite weight mutations;
- treating a Gaussian-divided residual as automatically characteristic;
- Lévy closure with uniformly bounded first absolute Lévy moments.

The desired arithmetic Gram representation remains unconstructed.
Finite-place, adelic, prolate, or Schur-complement machinery would have
to provide **nonlocal cancellation across the exact full arithmetic
configuration**, not just change signs of the displayed summands.
Theorem 4 gives an exact hostile test for such machinery: it must fail
after every nonzero finite event-weight mutation, even though deletion
can preserve scalar positivity.

The first unpaid lemma is still a positive full arithmetic spectral
measure or independently positive Gram construction reproducing the
complete `Psi`. No statement here reduces that remaining lemma to
an already-proved estimate. The useful result is a decisive elimination
of local positive-update and finite-cutoff closures, not an RH proof.

Tests in `tests/test_gram_levy_obstructions.py` check the exact finite
kernel/CND witnesses and Fourier coefficient algebra. The universal
statements are established by the proofs above, not by those tests.
