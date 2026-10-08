# Exact Gamma energy, a compact sign operator, and the horizon gap

Date: 2026-10-07.

Claim IDs: **SWS-004** (exact square identity), **SWS-005** (closed compact sign operator and quantitative spectral control), **SWS-006** (horizon cancellation and impossibility of a uniform contraction margin).

**Status.** The statements below are proved within their stated domains. They apply standard Fourier analysis, closed-form theory, the min-max principle, Bessel's inequality, elementary rearrangement, and a rank-one Birman--Schwinger argument to an exact decomposition of the Weil form. They are not an RH proof and carry no priority claim. The remaining RH-equivalent assertion is explicitly isolated in (5.4).

This positive operator is built from the **exact Gamma translation energy**, the exact finite prime translation energies, and the even polar term. It is a different decomposition from one using a logarithmic principal symbol plus a remainder. Bounds proved for a previously named positive operator must not be transferred to this one without a comparison proof.

The underlying exact Gamma/prime energy and scalar deficit were already derived in [Round007, WEIL_SQUARE_ATTEMPT.md, Sections 1–4](https://github.com/femboy2112/FuckingRH/blob/8da6cf92d276961356497486048163f0aff08233/research/astra_round_007/WEIL_SQUARE_ATTEMPT.md). SWS-004 is a normalization-preserving rederivation of that identity, with the polar cross product separated into its even and odd rank-one parts. This note adds the detailed closed core, the compact sign-operator application and quantitative tail, and the exact horizon-quotient obstruction; it does not claim first discovery of the energy identity.

## 1. Conventions and the object to be controlled

Fix a finite \(A>0\). Work on \(H_A=L^2(-A,A)\), identify its elements with their zero extensions to \(\mathbb R\), and use the inner product linear in its first argument. Define

\[
\widehat f(u)=\int_{\mathbb R}f(x)e^{iux}\,dx,
\qquad
\widetilde f(x)=\overline{f(-x)},
\qquad
(\tau_hf)(x)=f(x-h).
\]

Initially \(f\in C_c^\infty(-A,A)\). Put

\[
N_f=\|f\|_2^2,\qquad F=f*\widetilde f,
\qquad a_n=\frac{\Lambda(n)}{\sqrt n},
\qquad M_A=\sum_{2\le n\le e^{2A}}a_n.
\]

All sums over \(n\le e^{2A}\) mean integer \(n\) in that range. Define

\[
c_A(x)=\cosh(x/2),\quad s_A(x)=\sinh(x/2),
\quad C_f=\langle f,c_A\rangle,\quad S_f=\langle f,s_A\rangle,
\]

and

\[
d_A=\log\pi-\psi(1/4)+2M_A>0.
\tag{1.1}
\]

Here \(\psi=\Gamma'/\Gamma\). The inequality follows, for example, from
\(\psi(1/4)=-\gamma_E-\pi/2-3\log2\).

The convention-consistent Weil form is

\[
\begin{aligned}
Q_W(f)={}&2\operatorname{Re}\!\left[
 \widehat f(i/2)\overline{\widehat f(-i/2)}\right]\\
&+\frac1{2\pi}\int_{\mathbb R}
 \left[\operatorname{Re}\psi(1/4+iu/2)-\log\pi\right]
 |\widehat f(u)|^2\,du\\
&-2\operatorname{Re}\sum_{n\le e^{2A}}a_nF(\log n).
\end{aligned}
\tag{1.2}
\]

This normalization agrees with Suzuki's explicit formula [R1, equation (5.15)]. The prime cutoff follows from \(\operatorname{supp}F\subset[-2A,2A]\); an endpoint term vanishes. No assumption about the location of zeta zeros is used in (1.2).

## 2. SWS-004: an exact identity in positive translation energies

Set

\[
w_\Gamma(h)=\frac{e^{-h/2}}{1-e^{-2h}}\quad(h>0),
\]

\[
E_\Gamma(f)=\int_0^\infty
 w_\Gamma(h)\|f-\tau_h f\|_2^2\,dh,
\qquad
E_{\rm prime,A}(f)=\sum_{n\le e^{2A}}
 a_n\|f-\tau_{\log n}f\|_2^2.
\tag{2.1}
\]

Both are nonnegative. For smooth compactly supported \(f\), the Gamma integral is finite: near zero the squared difference is \(O(h^2)\) and \(w_\Gamma(h)=O(h^{-1})\); at infinity the weight decays exponentially.

### Proposition 2.1: exact Gamma multiplier

For every \(f\in L^2(\mathbb R)\), allowing either side to be \(+\infty\),

\[
E_\Gamma(f)=\frac1{2\pi}\int_{\mathbb R}
 \alpha(u)|\widehat f(u)|^2\,du,
\quad
\alpha(u)=\operatorname{Re}\psi(1/4+iu/2)-\psi(1/4).
\tag{2.2}
\]

**Proof.** Plancherel and Tonelli give

\[
\alpha(u)=2\int_0^\infty
 \frac{e^{-h/2}(1-\cos uh)}{1-e^{-2h}}\,dh.
\]

Writing \(b_m=2m+1/2\), expand the denominator into a positive geometric series and integrate:

\[
\boxed{\alpha(u)=2\sum_{m\ge0}
 \frac{u^2}{b_m(b_m^2+u^2)}.}
\tag{2.3}
\]

The partial-fraction expansion of the digamma function [R3] identifies this series with (2.2). In particular, \(\alpha\) is even, nonnegative, continuous, zero only at zero, and strictly increasing as a function of \(|u|>0\). This also proves

\[
\alpha(cu)\le c^2\alpha(u)\qquad(c\ge1).
\tag{2.4}
\]

The digamma asymptotic [R4] yields

\[
\alpha(u)=\log|u|-\log2-\psi(1/4)+O(|u|^{-2})
\quad(|u|\longrightarrow\infty).
\tag{2.5}
\]

This asymptotic is not used as a finite numerical enclosure. \(\square\)

### Proposition 2.2: exact square completion

For all \(f\in C_c^\infty(-A,A)\),

\[
\boxed{
Q_W(f)=E_\Gamma(f)+E_{\rm prime,A}(f)
 +2|C_f|^2-2|S_f|^2-d_A\|f\|_2^2.}
\tag{2.6}
\]

**Proof.** The archimedean term of (1.2), by (2.2), is

\[
E_\Gamma(f)-[\log\pi-\psi(1/4)]\|f\|_2^2.
\]

For every real \(h\),

\[
\|f-\tau_hf\|_2^2
 =2\|f\|_2^2-2\operatorname{Re}F(h).
\]

Thus the prime term is \(E_{\rm prime,A}(f)-2M_A\|f\|_2^2\). Finally,

\[
\widehat f(i/2)=C_f-S_f,
\quad\widehat f(-i/2)=C_f+S_f,
\]

so the polar term is \(2|C_f|^2-2|S_f|^2\). Combining these equalities proves (2.6). \(\square\)

There is no zero-mean requirement on \(f\). If the form is instead written using Suzuki's continuous kernel and \(u=f'\), then \(u\) has zero mean. Those are different variables and different statements.

## 3. SWS-005: closed domain and a genuine smooth core

Define

\[
V_A=\left\{f\in H_A:
 \frac1{2\pi}\int_{\mathbb R}\alpha(u)|\widehat f(u)|^2\,du<\infty
\right\},
\qquad
\|f\|_{V_A}^2=\|f\|_2^2+E_\Gamma(f).
\tag{3.1}
\]

### Proposition 3.1: closedness and core

\(E_\Gamma\) is a densely defined closed nonnegative form on \(H_A\), with domain \(V_A\), and \(C_c^\infty(-A,A)\) is a form core.

**Proof.** On the real line, the Fourier representation identifies the form norm with a weighted \(L^2\) norm of weight \(1+\alpha\), hence gives completeness. The requirement that a function vanish outside \([-A,A]\) is closed under \(L^2\) convergence and therefore under form-norm convergence. This proves closedness on \(H_A\).

For the core assertion, let \(f\in V_A\) and, for \(0<r<1\), set

\[
f_r(x)=r^{-1/2}f(x/r).
\]

Then \(f_r\) has support in \([-rA,rA]\) and

\[
\widehat f_r(u)=r^{1/2}\widehat f(ru),
\quad
\|f_r\|_{V_A}^2
 =\frac1{2\pi}\int_{\mathbb R}
 [1+\alpha(v/r)]|\widehat f(v)|^2\,dv.
\]

By (2.4), these dilation operators are uniformly bounded in the global weighted Fourier norm for \(r\) near one. Their convergence to the identity is immediate on functions with smooth compactly supported Fourier transforms, which are dense in that weighted space. Hence \(f_r\to f\) in form norm as \(r\uparrow1\).

For fixed \(r<1\), convolve \(f_r\) with a nonnegative smooth unit-mass mollifier supported in \([-\varepsilon,\varepsilon]\), where \(\varepsilon<(1-r)A\). The resulting function belongs to \(C_c^\infty(-A,A)\). Its Fourier transform is \(\widehat f_r(u)\widehat\eta(\varepsilon u)\), where \(|\widehat\eta|\le1\) and \(\widehat\eta(\varepsilon u)\to1\). Dominated convergence in the weight \(1+\alpha\) proves convergence to \(f_r\) in form norm. A diagonal choice proves the core assertion. \(\square\)

Define the positive form

\[
p_A[f]=E_\Gamma(f)+E_{\rm prime,A}(f)+2|C_f|^2
\quad(f\in V_A).
\tag{3.2}
\]

The added forms are bounded, since

\[
0\le E_{\rm prime,A}(f)\le4M_A\|f\|_2^2,
\quad
\|c_A\|_2^2=\sinh A+A,
\quad
\|s_A\|_2^2=\sinh A-A.
\tag{3.3}
\]

Consequently \(p_A\) is closed on \(V_A\), with the same smooth core. Let \(P_A\) be its associated nonnegative self-adjoint operator. Also define the bounded positive operator

\[
D_A=d_AI+2|s_A\rangle\langle s_A|,
\quad
\|D_A\|=d_A+2(\sinh A-A).
\tag{3.4}
\]

Here \(|v\rangle\langle v|f=\langle f,v\rangle v\). By bounded form perturbation,

\[
q_A[f]=p_A[f]-\langle D_Af,f\rangle
\tag{3.5}
\]

is closed and bounded below, has domain \(V_A\), and is exactly the closure of the Weil form (1.2). Its self-adjoint operator is

\[
\mathcal W_A=P_A-D_A,
\qquad\operatorname{Dom}(\mathcal W_A)=\operatorname{Dom}(P_A).
\tag{3.6}
\]

All of this is local to a finite interval. No unconditional global temperedness of Suzuki's function is assumed.

## 4. Compactness and a quantitative Bessel--bathtub bound

### Proposition 4.1: compact embedding and compact resolvent

The embedding \(V_A\hookrightarrow H_A\) is compact. Both \(P_A\) and \(\mathcal W_A\) have compact resolvent.

**Proof.** On a set bounded in form norm,

\[
\frac1{2\pi}\int_{|u|>R}|\widehat f(u)|^2\,du
 \le\frac{E_\Gamma(f)}{\alpha(R)}\longrightarrow0
\tag{4.1}
\]

uniformly as \(R\to\infty\). Splitting the Fourier formula for
\(\|\tau_hf-f\|_2^2\) at \(R\) gives uniform translation continuity: the low-frequency contribution tends to zero with \(h\), and the high-frequency contribution is bounded by four times the tail in (4.1). All functions have support in one fixed compact interval. The Kolmogorov--Riesz compactness criterion proves compact embedding. The standard compact-form embedding criterion then gives compact resolvent for \(P_A\), and the bounded perturbation \(D_A\) preserves it. \(\square\)

For \(R>0\), define the explicit increasing function

\[
\beta(R)=\frac1R\int_0^R\alpha(u)\,du.
\tag{4.2}
\]

It is strictly positive. A positive convergent series for it is

\[
\boxed{\beta(R)=2\sum_{m\ge0}
 \left[\frac1{b_m}-\frac1R\arctan\!\left(\frac R{b_m}\right)\right].}
\tag{4.3}
\]

If \(\beta_J\) denotes the sum over \(0\le m<J\), then

\[
0\le\beta(R)-\beta_J(R)
\le\frac{2R^2}{3}
\left[\frac1{b_J^3}+\frac1{4b_J^2}\right].
\tag{4.4}
\]

Indeed \(0\le x-\arctan x\le x^3/3\), and the remaining decreasing series is bounded by its first term plus its integral. Thus finite lower bounds and explicit remainders are available without treating an asymptotic formula as a certificate.

There is also an exact Gamma-phase expression:

\[
\beta(R)=\frac2R\operatorname{Im}
 \operatorname{Log}\Gamma(1/4+iR/2)-\psi(1/4).
\tag{4.5}
\]

Here \(\operatorname{Log}\Gamma\) is the holomorphic logarithm on the right half-plane chosen real on the positive real axis. It is an unwrapped phase, not the principal argument of the complex number \(\Gamma(1/4+iR/2)\). Formula (4.5) follows by differentiating this declared logarithm. Finally,

\[
\beta(R)=\log R-1-\log2-\psi(1/4)+O(R^{-1}).
\tag{4.6}
\]

### Proposition 4.2: spectral lower bound

Let \(\lambda_n(P_A)\), \(n\ge1\), be the eigenvalues of \(P_A\), ordered increasingly with multiplicity. Then

\[
\boxed{
\lambda_n(P_A)\ge
L_A(n):=\beta\!\left(\frac{\pi n}{2A}\right)>0.
}
\tag{4.7}
\]

In particular \(P_A\ge L_A(1)I>0\).

**Proof.** Take normalized eigenvectors \(f_1,\ldots,f_n\) for the first \(n\) eigenvalues and put

\[
\rho_n(u)=\frac1{2\pi}\sum_{j=1}^n|\widehat f_j(u)|^2.
\]

Bessel's inequality, applied in \(L^2(-A,A)\) to \(e^{-iux}\), gives

\[
0\le\rho_n(u)\le\frac A\pi,
\qquad\int_{\mathbb R}\rho_n(u)\,du=n.
\tag{4.8}
\]

Because \(\alpha\) is even and increasing in \(|u|\), these constraints minimize
\(\int\alpha\rho_n\) by filling the interval \([-R_n,R_n]\) to height \(A/\pi\), where \(R_n=\pi n/(2A)\). Explicitly,

\[
\int_{\mathbb R}
[\alpha(u)-\alpha(R_n)]
\left[\rho_n(u)-\frac A\pi\mathbf1_{[-R_n,R_n]}(u)\right]du\ge0,
\]

since the two factors have the same sign both inside and outside the interval. The mass constraint removes the term involving \(\alpha(R_n)\). Therefore

\[
\begin{aligned}
n\lambda_n(P_A)
&\ge\sum_{j=1}^n\lambda_j(P_A)\\
&\ge\sum_{j=1}^nE_\Gamma(f_j)
 =\int_{\mathbb R}\alpha(u)\rho_n(u)\,du\\
&\ge\frac{2A}{\pi}\int_0^{R_n}\alpha(u)\,du
 =n\beta(R_n).
\end{aligned}
\]

This proves (4.7). The same estimate follows for the Gamma operator alone. \(\square\)

The weaker half-mass bound
\(P_A\ge\tfrac12\alpha(\pi/(4A))I\) is valid, but (4.7) gives the full logarithmic leading coefficient rather than half of it.

## 5. The positive compact sign operator

Since \(P_A\ge L_A(1)I>0\), its inverse square root is bounded and compact. Define

\[
\boxed{
B_A=P_A^{-1/2}D_AP_A^{-1/2}
=d_AP_A^{-1}
 +2|v_A\rangle\langle v_A|,
\qquad v_A=P_A^{-1/2}s_A.
}
\tag{5.1}
\]

This \(B_A\) is a positive compact operator on \(H_A\). In particular,

\[
\|B_A\|\le
\frac{d_A+2(\sinh A-A)}{L_A(1)}.
\tag{5.2}
\]

### Proposition 5.1: exact sign criterion

For \(u=P_A^{1/2}f\),

\[
q_A[f]=\langle(I-B_A)u,u\rangle.
\tag{5.3}
\]

The map \(P_A^{1/2}:V_A\to H_A\) is bijective, with inverse \(P_A^{-1/2}\). Therefore

\[
\boxed{
Q_W(f)\ge0\text{ for every }f\in C_c^\infty(-A,A)
\iff B_A\le I
\iff\|B_A\|\le1.
}
\tag{5.4}
\]

The smooth-core assertion is essential in the first equivalence. The global missing inequality is

\[
\boxed{\text{For every finite }A>0,\qquad\|B_A\|\le1.}
\tag{5.5}
\]

By Weil positivity, this all-horizon statement is equivalent to RH. This note does not prove it.

### Proposition 5.2: quantitative eigenvalue tails and inertia

Write \(b_1(A)\ge b_2(A)\ge\cdots\ge0\) for the eigenvalues of \(B_A\), with multiplicity. Positive rank-one interlacing applied to (5.1) gives, for every \(n\ge1\),

\[
\boxed{
b_n(A)\ge\frac{d_A}{\lambda_n(P_A)},
\qquad
b_{n+1}(A)\le\frac{d_A}{\lambda_n(P_A)}
\le\frac{d_A}{L_A(n)}.
}
\tag{5.6}
\]

Thus for fixed \(A\), \(b_{n+1}(A)=O_A(1/\log n)\) as an upper bound. Equation (4.3), rather than the asymptotic (4.6), can be used to certify a particular finite tail bound.

If \(\Pi_N\) projects onto the first \(N\) eigenvectors of \(P_A\), a direct bound for the omitted compression is

\[
\|(I-\Pi_N)B_A(I-\Pi_N)\|
\le\frac{d_A+2\|s_A\|_2^2}{\lambda_{N+1}(P_A)}
\le\frac{d_A+2(\sinh A-A)}{L_A(N+1)}.
\tag{5.7}
\]

The off-diagonal coupling is entirely due to the rank-one term, and has norm

\[
\|\Pi_NB_A(I-\Pi_N)\|
=2\|\Pi_Nv_A\|\,\|(I-\Pi_N)v_A\|.
\tag{5.8}
\]

It must be retained in a finite-section certificate; a small omitted diagonal block by itself does not bound the full operator norm.

The number of negative directions of \(q_A\) is exactly the number of eigenvalues \(b_j(A)>1\), counted with multiplicity. The congruence (5.3) proves this assertion directly. In particular, if \(L_A(N)>d_A\), then \(b_{N+1}(A)<1\), and any negative index is at most \(N\). Compactness does not show that this finite index is zero.

There is a scalar rank-one test whenever \(\lambda_1(P_A)>d_A\):

\[
q_A\ge0
\iff
2\langle(P_A-d_AI)^{-1}s_A,s_A\rangle\le1.
\tag{5.9}
\]

If \(\lambda_1(P_A)<d_A\), positivity is already impossible. If \(\lambda_1(P_A)=d_A\), positivity requires \(s_A\perp\ker(P_A-d_AI)\), followed by (5.9) with the inverse on the orthogonal complement. The next positive eigenvalue is separated from zero by compact resolvent, so this restricted inverse is bounded. This is a standard rank-one reduction, not an estimate of its unresolved scalar.

### Parity refinement

Reflection \(f(x)\mapsto f(-x)\) commutes with \(P_A\) and \(D_A\). The Gamma and prime energies preserve parity, \(c_A\) is even, and \(s_A\) is odd. Consequently

\[
B_A^{\rm even}=d_A(P_A^{\rm even})^{-1},
\qquad
B_A^{\rm odd}=d_A(P_A^{\rm odd})^{-1}
 +2|v_A\rangle\langle v_A|.
\tag{5.10}
\]

The odd polar correction can contribute at most one additional negative direction beyond those already caused by eigenvalues of \(P_A\) below \(d_A\). This gives a concrete separation for further estimates and calibration.

### What the estimates do and do not certify

The bound \(L_A(n)=\log n+O_A(1)\) proves spectral control. It can nevertheless demand a very large \(n\) when compared with \(d_A\), which contains the large finite mass \(2M_A\). It is not, by itself, a practical all-horizon truncation strategy. The terms \(2M_AI\) in the completed prime energy and in \(D_A\) cancel exactly; separate crude estimates lose that dependence.

As a useful unconditional check, (5.2) proves \(q_A\ge0\) whenever

\[
L_A(1)\ge d_A+2(\sinh A-A).
\tag{5.11}
\]

This holds for all sufficiently small \(A>0\): before the first prime threshold \(M_A=0\), whereas \(L_A(1)\to\infty\) as \(A\downarrow0\). This recovers a small-support positivity regime. It does not extend (5.11) to every \(A\).

## 6. SWS-006: increasing the horizon and the unavoidable gap collapse

To keep the operator \(B_A\) distinct from a horizon parameter, write \(0<A<T\), and let \(J_{A,T}:H_A\to H_T\) be zero extension. Set

\[
\Delta M=M_T-M_A\ge0.
\]

### Proposition 6.1: exact cancellation on old support

For every \(f\in V_A\),

\[
\boxed{
p_T[J_{A,T}f]-p_A[f]
=\langle D_TJ_{A,T}f,J_{A,T}f\rangle-\langle D_Af,f\rangle
=2\Delta M\|f\|_2^2.
}
\tag{6.1}
\]

In particular,

\[
q_T[J_{A,T}f]=q_A[f].
\tag{6.2}
\]

**Proof.** The Gamma energy and the two polar functionals do not change under zero extension. Every new prime term has \(\log n>2A\). For such a shift, the zero-extended \(f\) and \(\tau_{\log n}f\) have disjoint supports up to a null set, so their squared difference has norm \(2\|f\|_2^2\). Summing gives the first equality. The scalar \(d_T-d_A\) is \(2\Delta M\), while \(S_f\) is unchanged, giving the second. \(\square\)

The statement about \(P_T\) is a **form compression identity**. It does not assert that the old-support subspace is invariant under \(P_T\), or that compressing \(P_T^{-1/2}\) gives a function of \(P_A\). No such unjustified inverse or square-root compression is needed below.

### Proposition 6.2: fixed-test generalized quotient

Fix a nonzero \(f\in V_A\). Its generalized quotient at horizon \(T\ge A\) is

\[
\begin{aligned}
r_T(f)
&:=\frac{\langle D_TJ_{A,T}f,J_{A,T}f\rangle}{p_T[J_{A,T}f]}\\
&=1-\frac{q_A[f]}{p_A[f]+2(M_T-M_A)\|f\|_2^2}.
\end{aligned}
\tag{6.3}
\]

Also

\[
\|B_T\|
=\sup_{0\ne g\in V_T}\frac{\langle D_Tg,g\rangle}{p_T[g]}
\ge r_T(f).
\tag{6.4}
\]

If \(q_A[f]>0\), the fixed-test quotient increases toward one as the added mass increases. If \(q_A[f]<0\), it remains greater than one and decreases toward one. If \(q_A[f]=0\), it equals one identically. These are exact algebraic statements, not numerical observations.

### An elementary quantitative lower bound for the mass

For every even integer \(N\le e^{2T}\),

\[
\boxed{
M_T\ge\frac{N\log2-\log(N+1)}{\sqrt N}.
}
\tag{6.5}
\]

**Proof.** Let \(N=2m\). The factorial identity

\[
\log\binom{2m}{m}
=\sum_{k\le2m}\Lambda(k)
\left(\left\lfloor\frac{2m}{k}\right\rfloor
 -2\left\lfloor\frac m{k}\right\rfloor\right)
\]

has bracketed coefficients in \(\{0,1\}\), so it is at most
\(\sum_{k\le N}\Lambda(k)\). The central binomial coefficient is the largest of the \(N+1\) coefficients whose sum is \(2^N\), giving

\[
\sum_{k\le N}\Lambda(k)
\ge\log\binom{N}{N/2}
\ge N\log2-\log(N+1).
\]

Finally \(k^{-1/2}\ge N^{-1/2}\) for \(k\le N\). \(\square\)

Taking \(N=2\lfloor e^{2T}/2\rfloor\) shows \(M_T\to\infty\) and, more quantitatively,

\[
\liminf_{T\to\infty}e^{-T}M_T\ge\log2.
\tag{6.6}
\]

This elementary bound suffices here; no prime number theorem or RH is invoked.

### Corollary 6.3: no uniform fixed contraction margin

Unconditionally,

\[
\boxed{\liminf_{T\to\infty}\|B_T\|\ge1.}
\tag{6.7}
\]

Indeed choose any fixed nonzero core test \(f\), apply (6.3)--(6.4), and use \(M_T\to\infty\). Consequently there is **no** \(\varepsilon>0\) such that

\[
\|B_T\|\le1-\varepsilon\qquad\text{for every sufficiently large }T.
\tag{6.8}
\]

This is a sharp obstruction to a proof strategy requiring a uniform relative coercivity
\(q_T\ge\varepsilon p_T\). It does not obstruct the needed inequality \(\|B_T\|\le1\).

If Weil positivity holds at every horizon, then \(\|B_T\|\le1\), and (6.7) sharpens to

\[
\|B_T\|\longrightarrow1.
\tag{6.9}
\]

Under that assumption the norms are also nondecreasing in the horizon: for each old test \(q_A[f]\ge0\), so \(r_T(f)\ge r_A(f)\), and one can take suprema. Moreover, for any fixed nonzero \(f\in V_A\),

\[
0\le1-\|B_T\|
\le\frac{q_A[f]}{p_A[f]+2(M_T-M_A)\|f\|_2^2}
=O_f(e^{-T}).
\tag{6.10}
\]

The big-O follows from the elementary bound (6.5). If the fixed numerator is zero, the gap is identically zero for all larger horizons.

The closing gap is forced by the normalization: both positive sides acquire the same growing scalar on old support while the original Weil form stays fixed. A computed norm close to one is therefore not, by itself, evidence for RH, an off-line zero, or a newly discovered near-null Weil direction. An actual negative old test would still give \(r_T(f)>1\) at every later horizon, but its relative excess would shrink at the same fixed-test scale.

## 7. Proof obligations left visible

The chain established here is

\[
\text{exact arithmetic Weil form}
\longrightarrow P_A-D_A
\longrightarrow I-B_A,
\]

with an exact smooth core, a compact positive \(B_A\), and explicit spectral tails. The unproved arithmetic inequality remains \(B_A\le I\) for **every** finite \(A>0\).

For a finite computational certificate, one must control both a chosen finite compression and its coupling to the omitted space, using bounds such as (5.7)--(5.8), sharper structural estimates, or the rank-one criterion (5.9) where its baseline hypothesis has been proved. Finite positivity with a numerical tolerance is not the all-horizon theorem. Because of (6.8), a successful uniform argument must permit its relative margin to tend to zero.

No implementation, floating-point experiment, or eigenvalue computation is claimed in this note. The quantitative estimates are mathematical inequalities, with explicit finite-series enclosures where indicated.

## 8. Claim ledger and sources

| Claim | Status and precise scope | Remaining obligation |
|---|---|---|
| SWS-004 | Disclosed: exact square identity (2.6) on every \(C_c^\infty(-A,A)\), with all constants and signs proved | None for the identity; it does not assert a sign |
| SWS-005 | Disclosed: closed core, compact resolvent, Bessel--bathtub bounds, positive compact \(B_A\), and exact sign equivalence for every fixed finite \(A\) | Prove \(\|B_A\|\le1\) for all \(A\); current estimates do not do so |
| SWS-006 | Disclosed: horizon form cancellation, elementary mass growth, and impossibility of a uniform fixed contraction margin | Does not rule out the required non-strict all-horizon inequality |

These are standard analytic and spectral tools applied to this normalization. No novelty or priority assertion is made.

- **[R1]** Masatoshi Suzuki, *Aspects of the screw function corresponding to the Riemann zeta function*, arXiv:2206.03682v4. Equations (1.1)--(1.3) fix the arithmetic/spectral screw-function normalization; equation (5.15) supplies the explicit formula. [Primary paper](https://arxiv.org/pdf/2206.03682v4).
- **[R2]** Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3, version of September 23, 2026. The finite-interval Weil form and operator treatment are prior context, particularly Sections 1.2 and 2.3--2.5. [Primary paper](https://arxiv.org/html/2606.09096v3). The particular exact positive/negative split and all core, compactness, and horizon claims used here have been proved explicitly above.
- **[R3]** NIST Digital Library of Mathematical Functions, equation 5.7.6, digamma partial-fraction expansion. [Official formula](https://dlmf.nist.gov/5.7.E6).
- **[R4]** NIST Digital Library of Mathematical Functions, equation 5.11.2, digamma asymptotic expansion. [Official formula](https://dlmf.nist.gov/5.11.E2).

