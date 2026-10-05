# Finite–Archimedean Fourier–Mellin transport: construction, obstruction, and RH boundary

**Date:** 2026-10-05  
**Status:** Exact transport and counterexample results; **not a proof or disproof of RH**.  
**Scope:** Radial Schwartz–Bruhat functions, Gaussian dilation spans, rational arithmetic periodization, and the centered Weil form. No priority claim is made for the constructions derived here.

## Executive result

The proposed correspondence can be made into an explicit linear map:

\[
T_p\mathbf1_{p^m\mathbb Z_p}(x)=e^{-\pi p^{2m}x^2}.
\]

For one prime this map preserves pointwise positivity, additive integral, Fourier transform, and normalized local Mellin transforms. It is an $L^2$ contraction, not an isometry or a convolution-algebra homomorphism.

The simultaneous extension that sends every finite-adelic ball $r\widehat{\mathbb Z}$ to the Gaussian $e^{-\pi r^2x^2}$ is **not** positivity preserving. The first obstruction already occurs at the primes $2,3$:

\[
\mathbf1_{\widehat{\mathbb Z}}-\mathbf1_{2\widehat{\mathbb Z}}
-\mathbf1_{3\widehat{\mathbb Z}}+\mathbf1_{6\widehat{\mathbb Z}}\ge0,
\]

whereas its prescribed image is

\[
e^{-\pi x^2}-e^{-4\pi x^2}-e^{-9\pi x^2}+e^{-36\pi x^2}
=-24\pi x^2+O(x^4)<0
\]

for sufficiently small nonzero $x$.

Arithmetic periodization repairs this particular positivity defect exactly: replacing a Gaussian by its integer-periodized theta sum makes the same inclusion–exclusion expression a sum over integers coprime to $6$.

That pointwise positivity is still not Weil positivity. Independently, a positive, normalized, Fourier-self-dual Gaussian mixture yields a completed Mellin transform with explicit zeros at real parts $1/4$ and $3/4$. Thus positivity of local test functions, self-duality, and the global functional equation do not suffice for RH.

## 1. Conventions and the exact RH target

Use additive Haar measure on $\mathbb Q_p$ with $\operatorname{vol}(\mathbb Z_p)=1$. The additive character has conductor exactly $\mathbb Z_p$: it is trivial on $\mathbb Z_p$ and nontrivial on $p^{-1}\mathbb Z_p$. This fixes the self-dual Fourier normalization.

On $\mathbb R$,

\[
\mathcal F_\infty f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi ix\xi}\,dx,
\qquad g(x)=e^{-\pi x^2},\qquad \widehat g=g.
\]

For local zeta integrals, use multiplicative Haar measure normalized by $\operatorname{vol}^{\times}(\mathbb Z_p^\times)=1$, and $d^\times x=dx/|x|$ on $\mathbb R^\times$. These are **not** the additive measures used in Fourier transforms.

\[
L_p(s)=\frac1{1-p^{-s}},\qquad
\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2).
\]

Write

\[
\mathcal Z(s)=\Gamma_{\mathbb R}(s)\zeta(s),\qquad
\xi(s)=\tfrac12s(s-1)\mathcal Z(s).
\]

The letter $\Lambda(n)$ below denotes the von Mangoldt function, not completed zeta.

For a nontrivial zero $\rho=\beta+i\gamma$, put

\[
z_\rho=\frac{\rho-1/2}{i}=\gamma-i(\beta-1/2).
\]

RH is precisely that every $z_\rho$ is real. In the logarithmic scale coordinate $u$, the centered zero mode is

\[
e^{(\rho-1/2)u}=e^{(\beta-1/2)u}e^{i\gamma u}.
\]

Thus RH says that these centered modes are purely oscillatory, without exponential growth or decay. This is a reformulation, not an independently constructed spectral realization.

## 2. A genuine one-prime transport

### Theorem 1: radial Fourier–Mellin intertwiner

Let $B_m=\mathbf1_{p^m\mathbb Z_p}$ for $m\in\mathbb Z$. Radial Schwartz–Bruhat functions are finite linear combinations of these nested-ball indicators. Define

\[
T_pB_m=g(p^m x).
\]

Then the following identities hold on their finite linear span:

\[
T_p\mathcal F_p=\mathcal F_\infty T_p,
\]

\[
\frac{Z_\infty(T_pf,s)}{\Gamma_{\mathbb R}(s)}
=\frac{Z_p(f,s)}{L_p(s)},\qquad \Re s>0.
\]

Also $T_pf(0)=f(0)$ and

\[
\int_{\mathbb R}T_pf(x)\,dx=\int_{\mathbb Q_p}f(x)\,dx_p.
\]

**Proof.** Character orthogonality gives

\[
\mathcal F_pB_m=p^{-m}B_{-m}.
\]

Real Gaussian scaling gives

\[
\mathcal F_\infty[g(p^m\cdot)]=p^{-m}g(p^{-m}\cdot).
\]

These are the same transformation rule. For the Mellin identities, the $p$-adic shell of valuation $k$ has multiplicative measure one, so

\[
Z_p(B_m,s)=\sum_{k\ge m}p^{-ks}=p^{-ms}L_p(s).
\]

A change of real variable yields

\[
Z_\infty(g(p^m\cdot),s)
=2\int_0^\infty e^{-\pi p^{2m}x^2}x^{s-1}\,dx
=p^{-ms}\Gamma_{\mathbb R}(s).
\]

The additive integrals of $B_m$ and $g(p^m\cdot)$ are both $p^{-m}$, and both functions take value one at zero. Extend linearly. $\square$

This is a map of test-function spaces. It is not a field map $\mathbb Q_p\to\mathbb R$, and it does not derive the Gaussian from $p$ alone: the real Fourier-normalized Gaussian is a specified target vector.

### Theorem 2: positivity and a positive norm defect

Let $f_m$ be the value of radial $f$ on the shell $v_p(x)=m$. For $x\ne0$, set

\[
K_m(x)=g(p^m x)-g(p^{m+1}x).
\]

Then $K_m(x)>0$ and $\sum_{m\in\mathbb Z}K_m(x)=1$. Moreover,

\[
(T_pf)(x)=\sum_m K_m(x)f_m.
\]

Consequently $f\ge0$ implies $T_pf\ge0$, and

\[
\|T_pf\|_{L^2(\mathbb R)}\le\|f\|_{L^2(\mathbb Q_p)}.
\]

More precisely,

\[
\boxed{
\|f\|_2^2-\|T_pf\|_2^2
=\frac12\int_{\mathbb R}\sum_{m,n}K_m(x)K_n(x)|f_m-f_n|^2\,dx.
}
\]

**Proof.** Telescoping gives the kernel formula on $B_n$, since $\sum_{m\ge n}K_m=g(p^nx)$. The kernel integrates to

\[
\int_{\mathbb R}K_m(x)\,dx=p^{-m}-p^{-m-1},
\]

which is exactly the additive measure of the $p$-adic shell. Apply the variance identity for a probability distribution $(K_m(x))_m$, integrate, and use Tonelli on the nonnegative terms. $\square$

This is an actual positive quadratic form, but it is a local smoothing defect, **not** the Weil form. It cannot be substituted for the RH-bearing form without proving an additional equality or inequality.

### Metric and convolution boundaries

The transport is not an isometry:

\[
\|B_0\|_2^2=1,\qquad \|g\|_2^2=1/\sqrt2.
\]

Even after normalizing each basis vector to unit norm, overlaps differ. For $m,n\in\mathbb Z$,

\[
\langle p^{m/2}B_m,p^{n/2}B_n\rangle=p^{-|m-n|/2},
\]

whereas the normalized real Gaussian dilation overlaps are

\[
\frac1{\sqrt{\cosh((m-n)\log p)}}.
\]

Thus no isometry can simultaneously send all these normalized basis vectors to their prescribed normalized Gaussian counterparts. This does not exclude other unitary maps with different vector assignments.

There is also a simple convolution obstruction. With additive convolution,

\[
B_0*B_0=B_0,
\]

but

\[
(g*g)(x)=2^{-1/2}e^{-\pi x^2/2}\ne g(x).
\]

Therefore no convolution-algebra homomorphism can send $B_0$ to $g$. The map in Theorem 1 deliberately does not preserve that operation.

## 3. The mixed-prime obstruction

Let $\widehat{\mathbb Z}=\prod_p\mathbb Z_p$ inside the finite adeles. For positive rational $r$, define

\[
\beta_r=\mathbf1_{r\widehat{\mathbb Z}}.
\]

The natural simultaneous extension is

\[
T\beta_r=g(rx).
\]

Finite linear combinations of the $\beta_r$ have unique coefficient representations: restrict to the finitely many involved primes and apply finite differences to the corresponding valuation-threshold functions. Thus this is a well-defined linear map on that span.

The product formula gives $\operatorname{vol}(r\widehat{\mathbb Z})=1/r$, and Fourier transform gives

\[
\mathcal F_{\rm fin}\beta_r=r^{-1}\beta_{1/r}.
\]

The same rule holds on the real Gaussian side. Fourier intertwining and integral normalization therefore survive the simultaneous extension.

### Theorem 3: the simultaneous map is not positive

For distinct primes $p,q$, the function

\[
f_{p,q}=\beta_1-\beta_p-\beta_q+\beta_{pq}
\]

is nonnegative: it is the indicator of the elements of $\widehat{\mathbb Z}$ that are units at both $p$ and $q$. The intersection identity $p\widehat{\mathbb Z}\cap q\widehat{\mathbb Z}=pq\widehat{\mathbb Z}$ is load-bearing here; the primes must be distinct.

Yet

\[
Tf_{p,q}(x)=g(x)-g(px)-g(qx)+g(pqx)
\]

has the expansion

\[
Tf_{p,q}(x)=-\pi(p^2-1)(q^2-1)x^2+O(x^4).
\]

Its quadratic coefficient is strictly negative. Thus $Tf_{p,q}(x)<0$ throughout a sufficiently small punctured neighborhood of zero. $\square$

For $p=2,q=3,x=0.1$, direct evaluation gives approximately $-0.343833180682784$.

**What this proves:** there is no positive linear map on this full finite-adelic span with all the assignments $\beta_r\mapsto g(rx)$.

**What this does not prove:** it does not exclude a different transport, a higher-dimensional target, a different target profile, or a map containing additional arithmetic summation. It says nothing against RH itself.

The same Taylor argument applies to any even $C^2$ profile $h$ with $h''(0)<0$, replacing $g$: the leading coefficient becomes $\tfrac12h''(0)(p^2-1)(q^2-1)$.

## 4. Exact repair by arithmetic periodization

Define, for $x>0$,

\[
\mathcal A f(x)=\sum_{r\in\mathbb Q} f(r_{\rm fin})g(xr).
\]

For the finite-adelic test functions under discussion, the diagonal support has a bounded denominator and the Gaussian ensures absolute convergence. This map is positive by construction.

Since

\[
\mathbb Q\cap\widehat{\mathbb Z}=\mathbb Z,
\]

we have

\[
\mathcal A\beta_a(x)=\sum_{n\in\mathbb Z}g(anx)=\theta(a^2x^2),
\qquad \theta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t}.
\]

The intersection identity follows directly from rational factorization: a reduced rational integral at every finite prime has denominator one.

For the obstruction in Theorem 3, periodization gives

\[
\begin{aligned}
\mathcal A f_{p,q}(x)
&=\theta(x^2)-\theta(p^2x^2)-\theta(q^2x^2)+\theta(p^2q^2x^2)\\
&=\sum_{\substack{n\in\mathbb Z\\p\nmid n,\ q\nmid n}}e^{-\pi n^2x^2}\ge0.
\end{aligned}
\]

For $p=2,q=3,x=0.1$, this is approximately $3.333874018467492$. The sign repair is exact inclusion–exclusion, not a numerical coincidence.

Poisson summation gives

\[
\theta(t)=t^{-1/2}\theta(1/t).
\]

The Gaussian Mellin integral and absolute convergence for $\Re s>1$ give

\[
\int_0^\infty\big(\theta(x^2)-1\big)x^{s-1}\,dx
=\Gamma_{\mathbb R}(s)\zeta(s).
\]

Thus the successful assembly is

\[
\text{all finite integrality constraints}
\longrightarrow\text{rational diagonal/integer lattice}
\longrightarrow\text{Gaussian theta sum}
\longrightarrow\text{completed zeta}.
\]

This recovers a classical theta/Tate mechanism. It does not prove that its analytically continued zeros lie on the critical line.

## 5. A decisive self-duality mutation

A Gaussian is not the unique positive normalized Fourier-self-dual Schwartz function.

### Theorem 4: explicit off-line zeros with positive self-dual local data

Define

\[
\phi(x)=\frac{10g(x)+16g(16x)+g(x/16)}{27}.
\]

Then $\phi$ is positive, even, Schwartz, and

\[
\phi(0)=\int_{\mathbb R}\phi(x)\,dx=1,
\qquad \widehat\phi=\phi.
\]

Its Mellin integral is

\[
Z_\infty(\phi,s)=\Gamma_{\mathbb R}(s)P(s),\quad \Re s>0,
\]

where

\[
\boxed{P(s)=\frac{10+16^{1-s}+16^s}{27}
=\frac{(16^s+2)(16^s+8)}{27\,16^s}.}
\]

In particular $P(1-s)=P(s)$ and $P(0)=P(1)=1$. Nevertheless it has zeros

\[
s=\frac14+\frac{(2k+1)\pi i}{\log16},\qquad
s=\frac34+\frac{(2k+1)\pi i}{\log16},\qquad k\in\mathbb Z.
\]

**Proof.** Fourier scaling exchanges $16g(16x)$ with $g(x/16)$, and fixes $10g(x)$. The values and integrals follow by scaling. The Mellin transform of $g(ax)$ is $a^{-s}\Gamma_{\mathbb R}(s)$. Factor the resulting quadratic in $16^s$. $\square$

Keep all finite local test functions equal to $\mathbf1_{\mathbb Z_p}$. The modified entire completion is

\[
\widetilde\xi(s)=P(s)\xi(s).
\]

It satisfies $\widetilde\xi(s)=\widetilde\xi(1-s)$ and inherits the original normalization at $0,1$. It has the explicit off-line zeros above, irrespective of RH for the original $\xi$.

This is **not a counterexample to RH**. It is a counterexample to the proposed inference from positive self-dual local kernels and their global functional equation to critical-line zeros. The Archimedean factor has been changed by $P$; pretending it remained the standard gamma factor would invalidate the control.

The same multiplier can be inserted at the prime $2$ instead, using

\[
\phi_2=\frac{10\mathbf1_{\mathbb Z_2}+16\mathbf1_{16\mathbb Z_2}+\mathbf1_{(1/16)\mathbb Z_2}}{27}.
\]

Its additive Fourier transform fixes it, its value at zero and additive integral are one, and its local zeta integral is $L_2(s)P(s)$. In this version the real Gaussian stays fixed but the finite local factor changes. Neither variant changes the actual Riemann zeta function into a counterexample to RH.

### General off-line placement

Let $b>1$ and $0<c<1/2$. The positive self-dual mixture

\[
f_{b,c}(x)=g(x)+c\big(b^{1/2}g(bx)+b^{-1/2}g(x/b)\big)
\]

has Mellin multiplier

\[
1+2c\cosh((s-1/2)\log b).
\]

Given $0<\delta<1/2$ and $\gamma>0$, choose

\[
b=e^{\pi/\gamma},\qquad c=\frac1{2\cosh(\delta\pi/\gamma)}.
\]

Then the multiplier vanishes at $s=1/2\pm\delta+i\gamma$. Divide by $f_{b,c}(0)$ for the same point/integral normalization. This shows that the counterexample is not tied to the numerical choices $16,2,8$.

For fixed $\delta$ and $\gamma\to\infty$, these normalized profiles converge to $g$ in the Schwartz topology while their added off-line zeros escape to large height. Finite-profile agreement cannot, by itself, certify a universal statement about zero locations.

## 6. Testing the tempting positive-norm repair

A natural centered, pole-subtracted theta function is

\[
E(x)=x^{1/2}\big(\theta(x^2)-1-x^{-1}\big),\qquad x>0.
\]

Poisson summation gives $E(x)=E(1/x)$. It decays like $-x^{-1/2}$ at infinity and like $-x^{1/2}$ at zero, so $K(u)=E(e^u)$ is integrable and square-integrable on $\mathbb R$.

For $0<\Re s<1$, splitting at $x=1$ and using theta inversion proves

\[
\int_0^\infty(\theta(x^2)-1-x^{-1})x^{s-1}\,dx
=\mathcal Z(s).
\]

Consequently, under the convention $\widehat K(t)=\int K(u)e^{itu}\,du$,

\[
\widehat K(t)=\mathcal Z(1/2+it).
\]

One might now try to prove RH by using the obviously nonnegative norm $\|K*f\|_2^2$. But Plancherel computes it exactly:

\[
\|K*f\|_2^2=\frac1{2\pi}\int_{\mathbb R}
|\mathcal Z(1/2+it)|^2|\widehat f(t)|^2\,dt.
\]

This is a continuous spectral weight, not the zero-evaluation form required by the explicit formula. Indeed the weight vanishes at critical-line zeta zeros rather than assigning them the spectral contributions of the Weil form.

There is also an unconditional distribution-level obstruction to equality: $K$ is Schwartz, so its autocorrelation is smooth, whereas the scale-space Weil distribution has nonzero Dirac masses at $\pm\log p^k$, with smooth Archimedean and pole terms away from the origin. A smooth convolution kernel cannot equal that distribution.

Thus this concrete positive-norm construction does **not** prove RH. It produces a different quadratic form.

## 7. The actual inequality that remains

Let $f\in C_c^\infty(\mathbb R)$, $\widetilde f(u)=\overline{f(-u)}$, and

\[
C_f=f*\widetilde f,\quad F(z)=\int_{\mathbb R}f(u)e^{izu}\,du,
\quad H(z)=F(z)\overline{F(\bar z)}.
\]

For real $t$, $H(t)=|F(t)|^2$. This identity is not an ordinary modulus square at a nonreal argument.

With these conventions, the centered explicit formula gives

\[
\begin{aligned}
\mathcal W(f)={}&H(i/2)+H(-i/2)\\
&+\frac1{2\pi}\int_{\mathbb R}|F(t)|^2
\left[\Re\psi\left(\frac14+\frac{it}{2}\right)-\log\pi\right]dt\\
&-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\Re C_f(\log n)\\
={}&\sum_\rho H(z_\rho).
\end{aligned}
\]

Zeros are counted with multiplicity. The prime sum is finite for compactly supported $f$; no divergent Euler product is substituted into this identity.

Weil's criterion is

\[
\boxed{\mathrm{RH}\iff\mathcal W(f)\ge0\text{ for every }f\in C_c^\infty(\mathbb R).}
\]

Under RH every summand is $|F(\gamma)|^2$. Off the line, a reflected pair $z,\bar z$ contributes

\[
F(z)\overline{F(\bar z)}+F(\bar z)\overline{F(z)}
=2\Re(a\bar b),
\]

which has signature $(1,1)$ in the two evaluation coordinates. The converse direction of the criterion requires admissible test-function localization; a negative contribution from one pair alone is not a proof that an arbitrary full zero sum is negative.

A successful Hilbert-space route would have to produce an independently defined positive pairing whose value is **this entire form**, with the exact prime-power coefficients, gamma term, and pole contributions. Positivity of a substitute form does not meet that criterion.

In unitary language: if every zero could be represented by a nonzero vector $v_\rho$ satisfying

\[
U_uv_\rho=e^{(\rho-1/2)u}v_\rho
\]

inside an independently constructed unitary representation, equality of norms would force $\Re\rho=1/2$. Neither local Fourier unitarity nor the positive theta norm constructed above establishes this spectral realization.

## 8. Computation and calibration

The companion scripts were actually run. They preserve their raw JSON outputs and logs.

### `verify.py`

Environment: Python 3.13.5, SymPy 1.14.0, mpmath 1.3.0, NumPy 2.3.5. Analytic-function computations used 70 decimal digits of working precision.

Exact symbolic checks covered the mixed-prime Taylor coefficient, Gaussian-mixture Fourier coefficient permutation, multiplier factorization and reflection, and endpoint normalization.

Numerical checks covered direct Fourier and Mellin integrals of the mixture, the explicit off-line zeros, finite one-prime Gram contraction matrices, the obstruction for four distinct-prime pairs, arithmetic theta inclusion–exclusion, Gaussian convolution, and the centered theta Mellin identity.

All implemented checks passed. Direct Fourier errors on the four evaluated frequencies were at most about $3.6\times10^{-59}$; the numerical Mellin residuals on the three evaluated points were below $6\times10^{-71}$. These are numerical diagnostics, not interval certificates.

### `weil_control.py`

The actual Guinand–Weil formula was evaluated for

\[
C_f(u)=e^{-u^2/(4a)},\qquad H(z)=\sqrt{4\pi a}e^{-az^2},
\]

with $a=0.02,0.05,0.1$, using prime powers up to $5000$ and 65-digit working precision. This admissible Gaussian calibration is not a compact-support universal proof.

| $a$ | Arithmetic Weil value | After increasing only the $n=2$ coefficient by 1% |
|---:|---:|---:|
| 0.02 | 0.018590450440763 | 0.018566289474473 |
| 0.05 | 0.000072732367540 | -0.000814525777947 |
| 0.10 | 0.000000004718954 | -0.002949134176507 |

The arithmetic values matched the finite calibration sum over 30 computed critical-line zeros to better than $3\times10^{-66}$. No completeness claim is made for that root sample. The prime-tail bound was evaluated analytically; the quadratures and zero-side tail were not interval-certified.

The coefficient mutation is a sensitivity control on the formula, not the construction of a valid new Euler product. It demonstrates why exact gluing coefficients matter, without implying anything new about universal Weil positivity.

## 9. Corrections to earlier heuristics

1. A normalized measure escaping to an added point of a one-point compactification does not identify that point with the Archimedean absolute value. For fixed nonzero rational $x$, one has $|x|_p=1$ for all but finitely many $p$. Thus $|x|_p\to1$ as the primes leave every finite set: the pointwise limit is the trivial absolute value, not $|x|_\infty$.
2. Raising $|\cdot|_p$ to an exponent approaching zero approaches the trivial norm; it does not change $\mathbb Q_p$ into $\mathbb R$. A continuum limit of radial shell spacing is only a statement about that radial coordinate and its measures.
3. Fourier self-duality, positivity, Schwartz decay, and point/integral normalization do not uniquely determine the Gaussian. The explicit mixture above satisfies all four.
4. The sign in the finite logarithmic derivative is
   \[
   -\frac d{ds}\log(1-p^{-s})^{-1}=\frac{\log p}{p^s-1}.
   \]
   Summing over primes gives $-\zeta'/\zeta$ only where the prime-power series converges absolutely, $\Re s>1$.
5. $\zeta(-1)$ is an analytic-continuation value, not an ordinarily convergent sum of positive integers. No step in this note equates those two.
6. No ordinal or Lambert-$W$ claim supplies the missing global positivity in this attempt. Those prior encodings are not premises of the proofs here.

## 10. Claim ledger and outcome

**Proved within the stated domains:** the radial transport, Fourier and normalized Mellin identities, local positive kernel and contraction defect, mixed-prime positivity obstruction, periodized inclusion–exclusion repair, and explicit off-line-zero mutation.

**Recovered established theory:** theta inversion, the completed-zeta Mellin representation, and the precise Weil positivity target.

**Observed, finite computational scope:** the integral checks, Gram diagnostics, and three arithmetic Weil calibrations recorded in the logs.

**Refuted:** the specified simultaneous Gaussian assignment is positive; positive normalized Fourier-self-dual local data automatically imply critical-line zeros; the naive theta convolution norm equals the Weil form.

**Not established:** universal positivity of $\mathcal W$, an independently positive global pairing reproducing it, or a proof/disproof of RH.

The result is not that the finite–Archimedean bridge is empty. A concrete bridge exists. The result is that its preservation properties must be stated exactly, and that local positivity cannot be silently promoted to the global arithmetic positivity needed for RH.

## Sources and provenance

External sources were checked during this investigation. Formulas developed in Theorems 1–4 were derived in this note and tested by the accompanying scripts; no novelty claim is made.

- NIST DLMF, **§1.14 Integral Transforms**, https://dlmf.nist.gov/1.14 — Fourier/Mellin and Plancherel conventions; constants above are derived explicitly for the $e^{-2\pi ix\xi}$ Fourier normalization.
- NIST DLMF, **§20.7(viii)**, especially equation 20.7.32, https://dlmf.nist.gov/20.7 — theta inversion.
- NIST DLMF, **§25.4**, https://dlmf.nist.gov/25.4 — completed xi and reflection.
- NIST DLMF, **§25.5**, especially 25.5.13–14, https://dlmf.nist.gov/25.5 — theta integral representations of zeta.
- NIST DLMF, **§27.4**, https://dlmf.nist.gov/27.4 — Euler products and Dirichlet-series identities.
- A. Connes and C. Consani, **Weil positivity and Trace formula, the archimedean place**, arXiv:2006.13771, https://arxiv.org/abs/2006.13771 — introduction and pp. 1–3 inspected, including rendered pages. Supports the Weil criterion and the distinction between a positive operator trace and the full Weil distribution. No claim that the paper proves full RH is made.
- Clay Mathematics Institute, **Riemann Hypothesis**, https://www.claymath.org/millennium/Riemann-Hypothesis/ — official statement.
- User Library: **RH_WEIL_FORM_MASTER_DOSSIER.md**, file `file_00000000f9e8822f814c88842d7fad8e`, version 1 — retrieved sections on the centered spectral coordinate, explicit formula, and positivity criterion. Other historical numerical, bibliographic, or priority claims in that dossier were not adopted as premises.

An attempted fetch of the original Tate thesis PDF at the IMJ mirror exceeded the web tool's content limit. No unseen passage of that PDF was used as evidence.

## Reproduction

```sh
python verify.py
python weil_control.py
```

The scripts overwrite only their corresponding JSON output files in this directory. The original run logs are included. NumPy eigenvalues are floating-point diagnostics; mpmath is high-precision floating-point arithmetic, not a rigorous interval package. The universal statements rest on the explicit mathematical proofs above, not on finite test counts.