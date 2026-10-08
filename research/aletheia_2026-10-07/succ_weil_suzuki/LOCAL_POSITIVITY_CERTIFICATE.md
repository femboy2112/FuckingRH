# SWS-007: an explicit short-interval Weil positivity certificate

Session date: 2026-10-07.

**Claim ID: SWS-007. Status: proved within the stated support and form domain.**

For every \(0<A\le 1/128\), the convention-consistent Weil form in this bundle satisfies

\[
\boxed{Q_W(v)\ge \frac{3}{100}\,\|v\|_2^2
\qquad (v\in C_c^\infty(-A,A)).}
\tag{1}
\]

The inequality also holds on its closed form domain \(V_A\), defined below. It has no zero-mean or parity restriction. The proof actually gives the stronger strict bound

\[
Q_W(v)>\frac{39199}{1000000}\,\|v\|_2^2
\qquad(v\ne0,\ v\in V_A).
\tag{2}
\]

The advertised constant \(3/100\) leaves a deliberate margin. Every decimal-looking constant used below is a rational bound justified in Appendix A; none is a floating-point estimate of an eigenvalue.

**Position in the research program.** This is an explicit quantitative application of known short-interval positivity, not a priority claim or a gain on the all-horizon RH problem. Suzuki's *Weil's quadratic form via the screw function*, Theorem 1.4, states positivity of the lowest eigenvalue for sufficiently small intervals and discusses the earlier work of Yoshida in Section 1.1; see [the primary paper, version 3](https://arxiv.org/html/2606.09096v3). The present note proves its own conservative interval and constant directly in this bundle's normalization.

The originating identities, domain, and smooth core are in [GAMMA_ENERGY_COMPACT_SIGN_OPERATOR.md](GAMMA_ENERGY_COMPACT_SIGN_OPERATOR.md), claims SWS-004 and SWS-005. The connection to the first variation of Suzuki's Hankel family is in [FULL_SUZUKI_WEIL_TANGENT.md](FULL_SUZUKI_WEIL_TANGENT.md), claim SWS-002. See [README.md](README.md) for the full successor-to-Weil/Suzuki proof chain.

## 1. Conventions, zero extension, and the form being bounded

Work on \(H_A=L^2(-A,A)\), with complex inner product linear in its first argument. Every function is extended by zero to the entire real line. Use the bundle's Fourier convention

\[
\widehat v(u)=\int_{\mathbb R}v(x)e^{iux}\,dx,
\qquad
\|v\|_2^2=\frac1{2\pi}\int_{\mathbb R}|\widehat v(u)|^2\,du.
\tag{3}
\]

For \(h>0\), let \((\tau_hv)(x)=v(x-h)\). The translation difference norm below is always the full \(L^2(\mathbb R)\) norm, including the part of the translated function outside \((-A,A)\).

Set

\[
w_\Gamma(h)=\frac{e^{-h/2}}{1-e^{-2h}},
\qquad
E_\Gamma(v)=\int_0^\infty
w_\Gamma(h)\|v-\tau_hv\|_2^2\,dh,
\tag{4}
\]

\[
\begin{aligned}
C_v&=\int_{-A}^A v(x)\cosh(x/2)\,dx,\\
S_v&=\int_{-A}^A v(x)\sinh(x/2)\,dx,\\
M_A&=\sum_{2\le n\le e^{2A}}\frac{\Lambda(n)}{\sqrt n},\\
d_0&=\log\pi-\psi(1/4),\qquad d_A=d_0+2M_A.
\end{aligned}
\tag{5}
\]

Here \(\psi=\Gamma'/\Gamma\), and the two displayed integrals are the inner products with the real functions \(\cosh(x/2)\) and \(\sinh(x/2)\).

The exact square identity SWS-004 is

\[
\begin{aligned}
Q_W(v)={}&E_\Gamma(v)
+\sum_{2\le n\le e^{2A}}
\frac{\Lambda(n)}{\sqrt n}\|v-\tau_{\log n}v\|_2^2\\
&+2|C_v|^2-2|S_v|^2-d_A\|v\|_2^2.
\end{aligned}
\tag{6}
\]

Initially this is an identity on \(C_c^\infty(-A,A)\). The Gamma integral is finite there because its integrand is \(O(h)\) near zero and decays exponentially at infinity.

For completeness, the closed form domain from SWS-005 is

\[
V_A=\{v\in H_A:E_\Gamma(v)<\infty\},
\qquad
\|v\|_{V_A}^2=\|v\|_2^2+E_\Gamma(v).
\tag{7}
\]

SWS-005 proves that this form is closed and that \(C_c^\infty(-A,A)\) is a form core. The finite prime sum and the two rank-one terms in (6) are bounded on \(H_A\), so (6) defines the closed extension of \(Q_W\) to \(V_A\). The estimates below also apply directly to every \(v\in V_A\).

## 2. No prime event is active in the certified interval

Appendix A proves

\[
\log2>\frac{277}{400}>\frac1{64}.
\]

If \(A\le1/128\), then \(2A\le1/64<\log2\), hence \(e^{2A}<2\). The prime sum and \(M_A\) in (6) are therefore both zero. Thus

\[
Q_W(v)=E_\Gamma(v)+2|C_v|^2-2|S_v|^2-d_0\|v\|_2^2.
\tag{8}
\]

The task is to bound the Gamma energy from below, retain the exact scalar subtraction, and control the one negative rank term. Discarding the nonnegative \(2|C_v|^2\) is valid for complex as well as real \(v\).

## 3. A support bound forces most Fourier mass outside a finite band

Every \(v\in H_A\) is integrable, and Cauchy--Schwarz gives, for every real \(u\),

\[
|\widehat v(u)|
\le\int_{-A}^A|v(x)|\,dx
\le\sqrt{2A}\,\|v\|_2.
\tag{9}
\]

Choose

\[
R=\frac{\pi}{10A}.
\tag{10}
\]

Integrating (9) over \([-R,R]\), with the Plancherel normalization in (3), yields

\[
\frac1{2\pi}\int_{-R}^R|\widehat v(u)|^2\,du
\le\frac{2AR}{\pi}\|v\|_2^2
=\frac15\|v\|_2^2.
\tag{11}
\]

Consequently at least four fifths of the Fourier mass lies outside this band:

\[
\frac1{2\pi}\int_{|u|>R}|\widehat v(u)|^2\,du
\ge\frac45\|v\|_2^2.
\tag{12}
\]

This is a direct support/Cauchy--Schwarz estimate. It requires no information about zeta zeros.

## 4. An elementary lower bound for the exact Gamma multiplier

Put \(b_j=2j+1/2\). Plancherel, the positive geometric series
\(w_\Gamma(h)=\sum_{j\ge0}e^{-b_jh}\), and Tonelli's theorem give

\[
E_\Gamma(v)=\frac1{2\pi}\int_{\mathbb R}
\alpha(u)|\widehat v(u)|^2\,du,
\qquad
\alpha(u)=2\sum_{j\ge0}
\frac{u^2}{b_j(b_j^2+u^2)}.
\tag{13}
\]

Both sides are allowed to be infinite before restricting to \(V_A\). This is the multiplier proved in SWS-004; equivalently,
\(\alpha(u)=\operatorname{Re}\psi(1/4+iu/2)-\psi(1/4)\).

Every summand in (13) is nonnegative and increasing in \(|u|\). Therefore (12) gives

\[
E_\Gamma(v)\ge\frac45\alpha(R)\|v\|_2^2.
\tag{14}
\]

To estimate \(\alpha(R)\), define

\[
f_R(b)=\frac{2R^2}{b(b^2+R^2)}\quad(b>0).
\]

This is strictly decreasing in \(b\): its positive denominator has derivative \(3b^2+R^2>0\). For every \(j\ge1\),

\[
f_R(b_j)\ge\frac12\int_{b_j}^{b_j+2}f_R(b)\,db.
\]

The integration intervals partition \([5/2,\infty)\). Keeping the \(j=0\) term separately gives

\[
\begin{aligned}
\alpha(R)
&\ge\frac{4R^2}{R^2+1/4}
+\frac12\int_{5/2}^\infty
\frac{2R^2}{b(b^2+R^2)}\,db\\
&=\frac{4R^2}{R^2+1/4}
+\frac12\log\left(1+\frac{R^2}{(5/2)^2}\right).
\end{aligned}
\tag{15}
\]

The last equality follows by integrating
\(2/b-2b/(b^2+R^2)\). No asymptotic approximation of the digamma function is used.

Appendix A proves \(\pi>25/8\). Thus, for \(A\le1/128\),

\[
R\ge\frac{128\pi}{10}>40.
\tag{16}
\]

The first term in (15) consequently satisfies

\[
\frac{4R^2}{R^2+1/4}
>\frac{25600}{6401}>\frac{3999}{1000}.
\tag{17}
\]

For the second term, use \(R>40\) and the logarithm bound from Appendix A:

\[
\begin{aligned}
\frac12\log\left(1+\frac{R^2}{(5/2)^2}\right)
&>\frac12\log257\\
&>\frac12\log256
=4\log2
>\frac{277}{100}.
\end{aligned}
\tag{18}
\]

Combining (15)--(18),

\[
\boxed{\alpha(R)>\frac{6769}{1000}.}
\tag{19}
\]

Hence (14) gives, for every nonzero \(v\in V_A\),

\[
\boxed{E_\Gamma(v)>\frac45\frac{6769}{1000}\|v\|_2^2.}
\tag{20}
\]

## 5. Scalar and odd-rank bounds; completion of the proof

The digamma reflection and duplication identities give

\[
\psi(1/4)=-\gamma_E-\frac\pi2-3\log2,
\]

so

\[
d_0=\log\pi+\gamma_E+\frac\pi2+3\log2.
\tag{21}
\]

For reference, this identity follows by applying duplication first at \(z=1/2\), then at \(z=1/4\), and reflection at \(z=1/4\), starting with \(\psi(1)=-\gamma_E\). The official formulas are [DLMF 5.5.8](https://dlmf.nist.gov/5.5.E8), [DLMF 5.5.4](https://dlmf.nist.gov/5.5.E4), and [DLMF 5.4.11](https://dlmf.nist.gov/5.4.E11), together with \(\Gamma(1)=1\).

The rational bounds proved in Appendix A imply

\[
\begin{aligned}
d_0
&<\frac{229}{200}+\frac{289}{500}
+\frac{1571}{1000}+\frac{1041}{500}\\
&=\frac{672}{125}.
\end{aligned}
\tag{22}
\]

For the negative rank term, Cauchy--Schwarz and a direct integration give

\[
2|S_v|^2
\le2\|v\|_2^2\int_{-A}^A\sinh^2(x/2)\,dx
=2(\sinh A-A)\|v\|_2^2.
\tag{23}
\]

For \(0<A<1\), the positive power series of \(\sinh\) implies

\[
2(\sinh A-A)
=2\sum_{k\ge1}\frac{A^{2k+1}}{(2k+1)!}
\le\frac{A^3}{3(1-A^2)}.
\tag{24}
\]

At \(A\le1/128\), this is bounded by

\[
\frac{1}{3\cdot128\cdot(128^2-1)}
=\frac1{6291072}<\frac1{1000000}.
\tag{25}
\]

Apply (20), (22), and (23)--(25) to (8), and discard the nonnegative even-rank term. For every nonzero \(v\in V_A\),

\[
\begin{aligned}
Q_W(v)
&>\left(
\frac45\frac{6769}{1000}
-\frac{672}{125}
-\frac1{1000000}
\right)\|v\|_2^2\\
&=\frac{39199}{1000000}\|v\|_2^2
>\frac3{100}\|v\|_2^2.
\end{aligned}
\tag{26}
\]

The zero vector satisfies (1) with equality. This proves (1) and (2). The calculation applies directly on \(V_A\); alternatively, one may prove it on the smooth core and pass to its form-norm closure using SWS-005. \(\square\)

## 6. What the certificate settles

The estimate is for every vector in the stated infinite-dimensional form domain, not merely for a finite family of trial functions or a finite matrix. It proves

\[
\inf_{0\ne v\in V_A}\frac{Q_W(v)}{\|v\|_2^2}\ge\frac3{100}
\quad\text{for every }0<A\le1/128.
\]

Together with SWS-002, it bounds the normalized limit of the Suzuki norm defect divided by \(2\omega\) below by \((3/100)\|v\|_2^2\); the unnormalized derivative is therefore at least \((3/50)\|v\|_2^2\) on the smooth core. This does not give a uniform operator-norm expansion in \(\omega\), a uniform range of \(\omega\) for all test vectors, or the all-horizon positivity required by RH.

The interval contains no prime-shift event. Its role is to certify the small-support baseline and the normalization of the exact Gamma/scalar/rank decomposition. Extending positivity into the interacting prime regime remains a separate theorem obligation. No claim that the chosen interval or constant is optimal is made.

## Appendix A. Explicit elementary enclosures for all constants

The following enclosures suffice:

\[
\frac{25}{8}<\pi<\frac{1571}{500},\qquad
\frac{277}{400}<\log2<\frac{347}{500},
\qquad
\gamma_E<\frac{289}{500},\qquad
\log\pi<\frac{229}{200}.
\tag{A.1}
\]

### A.1. Bounds for \(\pi\)

For \(0<x<1\), the alternating arctangent series gives

\[
x-\frac{x^3}{3}<\arctan x
<x-\frac{x^3}{3}+\frac{x^5}{5},
\qquad \arctan x<x.
\tag{A.2}
\]

The Machin identity

\[
\pi=16\arctan(1/5)-4\arctan(1/239)
\tag{A.3}
\]

can be checked without decimal constants: if \(\theta=\arctan(1/5)\), then \(\tan(2\theta)=5/12\) and \(\tan(4\theta)=120/119\); subtracting \(\arctan(1/239)\) gives tangent one and an angle in \((0,\pi/2)\).

Use the lower bound in (A.2) for the positive term and the upper bound \(\arctan x<x\) for the subtracted term to obtain

\[
\pi>
16\left(\frac15-\frac1{3\cdot5^3}\right)-\frac4{239}
>\frac{25}{8}.
\tag{A.4}
\]

Reversing the choices gives

\[
\pi<
16\left(\frac15-\frac1{3\cdot5^3}+\frac1{5\cdot5^5}\right)
-4\left(\frac1{239}-\frac1{3\cdot239^3}\right)
<\frac{1571}{500}.
\tag{A.5}
\]

The final comparisons in (A.4)--(A.5) are inequalities between explicit rational numbers.

### A.2. Bounds for \(\log2\)

Integrating the geometric series for \(1/(1-t^2)\) on \([0,1/3]\) gives the positive series

\[
\log2=2\sum_{j\ge0}\frac1{(2j+1)3^{2j+1}}.
\tag{A.6}
\]

Let

\[
L_J=2\sum_{j=0}^{J-1}\frac1{(2j+1)3^{2j+1}}.
\]

Its tail has the elementary geometric bound

\[
0<\log2-L_J
\le\frac{2}{(2J+1)3^{2J+1}(1-1/9)}.
\tag{A.7}
\]

At \(J=3\),

\[
L_3=\frac{842}{1215}>\frac{277}{400},
\qquad
L_3+\frac{2}{7\cdot3^7(1-1/9)}<\frac{347}{500}.
\tag{A.8}
\]

This proves both bounds for \(\log2\) in (A.1).

### A.3. An elementary upper bound for Euler's constant

Let \(H_n=\sum_{k=1}^n1/k\), so \(\gamma_E=\lim_{n\to\infty}(H_n-\log n)\). Telescoping the decreasing sequence \(H_n-\log n\) gives

\[
H_n-\log n-\gamma_E
=\sum_{k=n}^\infty
\left(\log(1+1/k)-\frac1{k+1}\right).
\tag{A.9}
\]

Each summand has the integral representation and lower bound

\[
\begin{aligned}
\log(1+1/k)-\frac1{k+1}
&=\int_k^{k+1}\frac{k+1-x}{x(k+1)}\,dx\\
&>\frac1{2(k+1)^2}.
\end{aligned}
\tag{A.10}
\]

The decreasing-function integral comparison then yields

\[
H_n-\log n-\gamma_E
>\frac12\sum_{j=n+1}^\infty\frac1{j^2}
>\frac1{2(n+1)}.
\tag{A.11}
\]

Take \(n=32\), use \(\log32=5\log2>5L_4\), and retain the notation from A.2. All remaining terms are rational:

\[
\begin{aligned}
\gamma_E
&<H_{32}-5L_4-\frac1{66}\\
&=\frac{6756824388151759}{11696687784381600}
<\frac{289}{500}.
\end{aligned}
\tag{A.12}
\]

No tabulated decimal value of \(\gamma_E\) is required.

### A.4. An upper bound for \(\log\pi\)

The exponential series has positive terms, so

\[
e^{229/200}
>\sum_{k=0}^8\frac{(229/200)^k}{k!}
>\frac{1571}{500}>\pi.
\tag{A.13}
\]

The middle comparison is an explicit rational inequality. Monotonicity of the logarithm proves \(\log\pi<229/200\), completing (A.1).

### A.5. Exact arithmetic verification record

The finite rational comparisons in (A.4), (A.5), (A.8), (A.12), (A.13), (17), (25), and (26) were evaluated with Python's standard-library `fractions.Fraction` and integer factorials: nine comparisons, all passed. They are reproducible through `local_rational_controls()` in [the durable probe](../../../scripts/rh_succ_weil_suzuki_probe.py), and the actual output is [recorded here](evidence/finite_probe_results.json). This checks arithmetic transcription. The inequalities, series remainder bounds, Fourier estimate, and form-domain passage are justified in the proof above; the arithmetic run is not a substitute for those arguments or external independent review.

## Claim ledger

| Claim | Truth state and exact scope | What is not asserted |
|---|---|---|
| SWS-007 | Disclosed: \(Q_W(v)\ge(3/100)\|v\|_2^2\) for every \(0<A\le1/128\) and every \(v\in V_A\), with the stated zero-extension and Fourier conventions | Optimal constants, new priority for short-interval positivity, positivity in the prime-interacting regime, or RH |

