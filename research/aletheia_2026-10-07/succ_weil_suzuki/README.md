# From succ/fucc to the completed Weil form and Suzuki

**Date:** 2026-10-07. **Research branch:** `research/succ-weil-suzuki-rigorous-bridge-2026-10-07`.  
**Frozen parent:** `987a67d891879e966c9e0c7fb533a5dc74f805fd`, the current provenance-audit line.  
**Status:** a derivation, several unconditional operator estimates, reproducible finite controls, and an explicit remaining theorem. **RH is open.**

Leah's request is the organizing question: carry the succ/fucc, finite-clock, divisibility, Gaussian, and wavefront intuition through an actual mathematical argument to Weil/Suzuki. The purpose of this note is to make every transition explicit. An analogy selects a construction; it does not discharge the hypotheses of the next theorem.

This bundle contains:

| File | Purpose |
|---|---|
| This note | The entire mathematical path, including definitions and the point at which new analytic input is needed |
| [FULL_SUZUKI_WEIL_TANGENT.md](FULL_SUZUKI_WEIL_TANGENT.md) | The full, normalized derivative of Suzuki's local contraction defect, including the Gamma and elementary factors |
| [GAMMA_ENERGY_COMPACT_SIGN_OPERATOR.md](GAMMA_ENERGY_COMPACT_SIGN_OPERATOR.md) | Exact positive-energy decomposition, closed forms, compact sign operator, quantitative tail, and horizon obstruction |
| [LOCAL_POSITIVITY_CERTIFICATE.md](LOCAL_POSITIVITY_CERTIFICATE.md) | An explicit unconditional short-interval inequality for the completed form |
| [FINITE_CERTIFICATE_INTERFACE.md](FINITE_CERTIFICATE_INTERFACE.md) | A precise spectral truncation and tail criterion that would make finite work certify a whole interval |
| [PROVENANCE_AND_CLAIMS.md](PROVENANCE_AND_CLAIMS.md) | Sources, claim IDs, authorship, dependencies, execution status, and the unpaid theorem |
| [ROUND_RESULT.md](ROUND_RESULT.md) | What this round actually established and what the computations found |

## 1. Fix the spaces and conventions first

There are several useful representations. They must not be identified without a map and a proof.

1. The unilateral arithmetic representation is on \(\ell^2(\mathbb N_{\ge1})\).
2. The finite-clock representation is on normalized-Haar spaces \(L^2(\mathbb Z/L\mathbb Z)\), with specified refinement maps.
3. The explicit formula acts on compactly supported functions on the logarithmic line \(\mathbb R\).
4. Suzuki's local Hankel operator acts on the active interval \(I_A=(-A,A)\).

On the logarithmic line use

\[
\widehat v(z)=\int_{\mathbb R}v(t)e^{izt}\,dt,
\qquad \widetilde v(t)=\overline{v(-t)},
\qquad (\tau_hv)(t)=v(t-h).
\]

Plancherel has the factor \(1/(2\pi)\). A function on \(I_A\) is extended by zero before taking translation norms. The initial proof core is \(C_c^\infty(I_A)\). Inner products and all polarizations use a consistent complex convention; statements written as quadratic forms are convention independent.

Write

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad a_n=\frac{\Lambda(n)}{\sqrt n},\quad h_n=\log n.
\]

The harmless factor \(1/2\) in \(\xi\) cancels in logarithmic derivatives and ratios. Distributions below live in \(\mathcal D'(\mathbb R)\). Global temperedness is not assumed: it would require an additional argument, and the local derivation does not need it.

## 2. The exact arithmetic content of succ/fucc

Define

\[
Se_n=e_{n+1},\qquad V_me_n=e_{mn}.
\]

These are isometries and satisfy the exact braid relation

\[
V_mS=S^mV_m,\qquad V_mV_n=V_{mn}.
\]

Thus the intuitive operation of replacing one successor step by \(m\) steps has an honest operator realization. Its unilateral boundary is

\[
E=I-SS^*=|e_1\rangle\langle e_1|.
\]

Let \(D_m=V_mV_m^*\), the projection onto integers divisible by \(m\). Then

\[
D_mD_n=D_{\operatorname{lcm}(m,n)}.
\]

On finitely supported vectors, unique factorization gives two distinct operator identities:

\[
\boxed{H_{\log}:=\operatorname{diag}(\log n)
       =\sum_{p}\sum_{k\ge1}(\log p)D_{p^k},}
\]

\[
\boxed{\Lambda_{\rm op}:=\operatorname{diag}(\Lambda(n))
       =\sum_p\sum_{k\ge1}(\log p)V_{p^k}EV_{p^k}^*.}
\]

For the first identity, the diagonal entry at \(n\) counts each prime dividing \(n\) with its valuation. For the second, \(V_{p^k}EV_{p^k}^*\) is the projection onto the single basis vector \(e_{p^k}\). Every relevant sum on a fixed basis vector is finite.

This is the precise part of the “successor boundary sees prime powers” framing. The primes and the weights \(\log p\) are arithmetic input to the displayed sum. The identity does not derive them from an arbitrary abstract isometry. A bilateral successor has \(I-SS^*=0\), so the same boundary formula cannot be transported unchanged to a cyclic or profinite model.

### 2.1 LCM clocks give exactly the von Mangoldt events

Set \(L_N=\operatorname{lcm}(1,\ldots,N)\). Unique factorization gives

\[
\log L_N-\log L_{N-1}=\Lambda(N).
\]

Consequently the right-continuous function

\[
C(t)=\log L_{\lfloor e^t\rfloor}\quad(t\ge0)
\]

has distributional derivative

\[
dC=\sum_{n\ge2}\Lambda(n)\delta_{\log n}.
\]

After the half-density normalization, the event measure required by the explicit formula is

\[
\boxed{d\mu_P(t)=e^{-t/2}dC(t)=\sum_{n\ge2}a_n\delta_{h_n}.}
\]

Integrating twice on the positive half-line produces the prime ramp

\[
P(T)=\sum_{h_n\le T}a_n(T-h_n).
\]

The half-density is a choice of analytic representation. For example,

\[
(Uf)(t)=e^{t/2}f(e^t)
\]

is unitary from \(L^2(\mathbb R_+,dx)\) to \(L^2(\mathbb R,dt)\). The factor \(e^{-t/2}\) in the event measure is compatible with this change of coordinates and the critical-line centering. It is not forced by the bare relation \(V_mS=S^mV_m\).

## 3. What the Gaussian contributes

The arithmetic events determine the Euler-product portion. Completion supplies a second, indispensable input:

\[
\int_0^\infty e^{-\pi x^2}x^{s-1}\,dx
 =\tfrac12\pi^{-s/2}\Gamma(s/2),\qquad \Re s>0.
\]

Poisson summation for the theta function supplies the reflection \(s\leftrightarrow1-s\); the factors \(s(s-1)\) remove the two elementary poles. These are classical Mellin/theta facts, not consequences of the successor braid. The connection to a Gaussian is therefore a specific Mellin identity and a functional equation, with exact normalization. See NIST DLMF [25.4](https://dlmf.nist.gov/25.4) and [25.5](https://dlmf.nist.gov/25.5).

For \(\Re s>1\), logarithmic differentiation gives

\[
\boxed{\frac{\xi'}{\xi}(s)
 =\frac1s+\frac1{s-1}-\frac12\log\pi
  +\frac12\psi(s/2)
  -\sum_{n\ge2}\Lambda(n)n^{-s}.}
\]

This is the first point at which the prime events, Gaussian completion, and elementary terms are all present in one exact expression.

## 4. The completed Weil distribution

For \(F\in C_c^\infty(\mathbb R)\), the completed explicit formula is

\[
\begin{aligned}
W(F)={}&\widehat F(i/2)+\widehat F(-i/2)
 -\sum_{n\ge2}a_n\bigl(F(h_n)+F(-h_n)\bigr)\\
&+\frac1{2\pi}\int_{\mathbb R}\widehat F(u)
 \left[\Re\psi\!\left(\tfrac14+\tfrac{iu}2\right)-\log\pi\right]du.
\end{aligned}
\tag{4.1}
\]

The prime sum is finite for a fixed compact support. Formula (4.1), or its origin-renormalized version below, defines the arithmetic side without placing the zeros on the critical line.

The source normalization is Suzuki, arXiv:2206.03682v4, equation (5.15) and Section 3.2; the [versioned primary paper](https://arxiv.org/pdf/2206.03682v4) uses this same centered explicit formula.

For comparison with the zero side set \(\gamma_\rho=(\rho-1/2)/i\). Then

\[
W(F)=\sum_\rho\widehat F(\gamma_\rho)
\]

with the usual zero multiplicities. For compact smooth tests the rapid decay in horizontal strips and the zero-counting estimate justify the sum. The \(\gamma_\rho\) are not assumed real.

This coordinate reverses the sign of Suzuki's convention \(\rho=1/2-i\gamma\). The functional equation makes the zero multiset invariant under this reversal, so the displayed full sums and the even Weil distribution are unchanged.

The Weil quadratic form is

\[
\boxed{Q(v)=W(v*\widetilde v).}
\]

Off the critical line its spectral expression is

\[
Q(v)=\sum_\rho
\widehat v(\gamma_\rho)
\overline{\widehat v(\overline{\gamma_\rho})}.
\tag{4.2}
\]

Replacing each summand by \(|\widehat v(\gamma_\rho)|^2\) would assume the central issue. Weil's criterion states that \(Q(v)\ge0\) for every compact smooth \(v\) is equivalent to RH. Suzuki's [2026 paper, v3](https://arxiv.org/html/2606.09096v3) records the normalization and the associated interval forms in (2.3)–(2.7).

### 4.1 The origin term must be fixed

Put

\[
w_\Gamma(h)=\frac{e^{-h/2}}{1-e^{-2h}},\qquad h>0.
\]

An equivalent formula, whose singularity has been explicitly subtracted, is

\[
\begin{aligned}
W(F)={}&\int_{\mathbb R}2\cosh(t/2)F(t)\,dt
-\sum_{n\ge2}a_n\bigl(F(h_n)+F(-h_n)\bigr)\\
&-(\log(4\pi)+\gamma_E)F(0)\\
&-\int_0^\infty
 \bigl[F(h)+F(-h)-2e^{-h/2}F(0)\bigr]w_\Gamma(h)\,dh.
\end{aligned}
\tag{4.3}
\]

The bracket vanishes to first order at the origin, so this integral converges. Dropping its subtraction or changing the scalar at \(F(0)\) changes the target form. The full tangent note independently obtains the same scalar from the digamma integral, rather than fitting it to numerical positivity.

## 5. Suzuki's function is the twice-integrated completed distribution

Define the triangle

\[
\Delta_T(t)=\frac{(T-|t|)_+}{2}
=R_T*\widetilde R_T(t),\qquad
R_T=2^{-1/2}1_{[-T/2,T/2]}.
\]

The convolution identity fixes the factor \(1/2\). Substituting it into (4.3) gives, for \(T\ge0\),

\[
\boxed{\begin{aligned}
\Psi(T)={}&W(\Delta_T)\\
={}&8\bigl(\cosh(T/2)-1\bigr)-P(T)
 +\frac T2\bigl(\psi(1/4)-\log\pi\bigr)\\
&+\sum_{m\ge0}\frac{1-e^{-(2m+1/2)T}}{(2m+1/2)^2}.
\end{aligned}}
\tag{5.1}
\]

Extend \(\Psi\) evenly. The series is absolutely convergent. The triangular test can be obtained by mollification; its transform has quadratic decay in horizontal strips, enough for the zero sum. This extension does not require an unconditional temperedness assertion.

Away from the origin, differentiating (5.1) in distributions gives

\[
\Psi''|_{(0,\infty)}
=\bigl(2\cosh(t/2)-w_\Gamma(t)\bigr)dt
 -\sum_{n\ge2}a_n\delta_{h_n}.
\tag{5.2}
\]

On the whole line the correct statement is \(\Psi''=W\), using (4.3) at the origin. In particular,

\[
\Psi(t)=-\tfrac12|t|\log|t|
 -\tfrac12\bigl(\log(2\pi)+\gamma_E-1\bigr)|t|+O(t^2).
\]

Thus \(\Psi'(0+)\) is infinite. Imposing \(\Psi'(0+)=0\) would be an error. Adding \(c|t|\) changes \(W\) by \(2c\delta_0\), and changes \(Q(v)\) by \(2c\|v\|_2^2\).

### 5.1 The screw kernel and the exact positivity statement

Define

\[
K_\Psi(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u).
\]

Two integrations by parts give

\[
\boxed{Q(v)=\iint_{\mathbb R^2}
K_\Psi(t,u)v'(t)\overline{v'(u)}\,dt\,du.}
\tag{5.3}
\]

The separate \(\Psi(t)\) and \(\Psi(u)\) terms vanish because \(\int v'=0\). There is no restriction \(\int v=0\). Imposing that restriction on the original Weil test would silently shrink the claimed criterion.

Conversely, let

\[
\eta=\sum_jc_j(\delta_{t_j}-\delta_0).
\]

Mollify this zero-mass distribution and take a compactly supported antiderivative. Applying \(Q\ge0\) and passing to the limit yields

\[
\sum_{j,k}c_j\overline{c_k}K_\Psi(t_j,t_k)\ge0.
\]

Consequently the positivity assertions on all compact smooth tests and on every finite kernel matrix are equivalent. Under RH the zero-side formula (4.2) is a sum of squares, proving one direction. The reverse direction can also be seen directly: kernel positivity realizes \(K_\Psi\) as a Gram kernel, so the associated vectors satisfy

\[
\|b_t-b_u\|^2=2\Psi(t-u).
\]

The triangle inequality makes \(\sqrt{\Psi}\) subadditive and hence \(\Psi(t)=O((1+|t|)^2)\). Therefore its Laplace transform is holomorphic for \(\Re s>0\). Direct termwise integration of (5.1), initially for \(\Re s>1/2\), gives

\[
\boxed{s^2\int_0^\infty\Psi(t)e^{-st}\,dt
       =\frac{\xi'}{\xi}(s+1/2).}
\tag{5.4}
\]

The analytic continuation supplied by the left side rules out zeros to the right of the critical line, and the functional equation rules out zeros to the left. This explains why the particular completed kernel is an RH criterion. Pointwise nonnegativity of a generic even function does not imply kernel positivity. For this specific \(\Psi\), Suzuki proves the stronger pointwise criterion in [arXiv:2206.03682v4, Theorem 1.7](https://arxiv.org/pdf/2206.03682); that is a separate source theorem.

## 6. The finite-clock construction and its exact limitation

On \(H_L=L^2(\mathbb Z/L\mathbb Z)\) with normalized Haar measure, let

\[
U_Lf(x)=f(x-1),\qquad
(D_{m,L}f)(x)=\sqrt m\,1_{m\mid x}f(x/m),
\quad D_{m,L}:H_L\longrightarrow H_{mL}.
\]

Then \(D_{m,L}\) is an isometry and

\[
D_{m,L}U_L=U_{mL}^mD_{m,L}.
\]

For \(L\mid L'\), pullback by reduction modulo \(L\) defines an isometric refinement \(J_{L,L'}\). These refinements commute with the displayed dilations. This supplies an exact clock model of the braid. Multiplication modulo one fixed modulus can have collisions and is not a substitute for this map between different spaces.

The exact-conductor sector \(W_n\) is spanned by characters

\[
x\mapsto e^{2\pi irx/n},\quad (r,n)=1,
\]

and has dimension \(\varphi(n)\). At ambient modulus \(L\), \(n\mid L\), its projection matrix in the normalized point basis has entries \(c_n(x-y)/L\), where \(c_n\) is the Ramanujan sum. The factor is \(1/L\); it becomes \(1/n\) only when \(L=n\).

If \(\mathcal C\) acts by the order of a character on the countable character space, then

\[
\operatorname{Tr}\mathcal C^{-u}
=\sum_{n\ge1}\frac{\varphi(n)}{n^u}
=\frac{\zeta(u-1)}{\zeta(u)},\qquad\Re u>2.
\]

This explains a genuine bridge to Euler ratios. It does not identify normalized finite-Haar spaces, \(\ell^2(\mathbb N)\), and a KMS representation as one Hilbert space.

### 6.1 The conductor deformation has the correct first derivative

Suzuki's arithmetic coefficients in logarithmic coordinates are

\[
b_\omega(n)=n^{\omega-1/2}\prod_{p\mid n}(1-p^{-2\omega}).
\tag{6.1}
\]

At \(\omega=1/2\), these are \(\varphi(n)/n\). General \(\omega\) supplies a Jordan-type deformation; unweighted sector dimensions alone do not derive this entire real-parameter family.

At zero,

\[
b_0(n)=1_{n=1},\qquad
\boxed{b_0'(n)=\frac{2\Lambda(n)}{\sqrt n}.}
\tag{6.2}
\]

Proof: if \(n\) has \(r\) distinct prime divisors, the product in (6.1) vanishes to order \(r\). A first derivative can therefore survive only on prime powers. For \(n=p^k\), differentiating the sole factor gives \(2\log p/\sqrt n\). The \(n=1\) coefficient is constant.

Higher derivatives contain new sectors and corrections to older sectors. For example,

\[
b_0''(p^k)=4(k-1)(\log p)^2p^{-k/2}.
\]

It would be false to say that derivative order \(r\) contains only integers with exactly \(r\) distinct prime divisors. Since only finitely many events meet a compact logarithmic interval, (6.2) also holds for the event measure in the local distribution topology.

For \((R_hv)(u)=v(h-u)\), one has

\[
R_hR_0=\tau_h,\qquad R_0R_h=\tau_{-h}.
\]

Thus the prime derivative \(2\sum_na_nR_{h_n}\), after the symmetric defect operation, yields exactly

\[
-\sum_na_n(\tau_{h_n}+\tau_{-h_n}).
\]

The prime part of Weil's form is now derived from the conductor family. The archimedean and elementary pieces are still required.

## 7. Complete the bridge: the full Suzuki tangent

Put \(q=s+1/2\) and define

\[
B_\omega(s)=\frac{\xi(q-\omega)}{\xi(q+\omega)}.
\]

Its causal inverse Laplace kernel \(k_\omega\) factors into the arithmetic measure with weights (6.1), an explicit beta/Gamma kernel, and two elementary kernels. All factors, their domains, and the proof of differentiation on compact smooth tests are in [FULL_SUZUKI_WEIL_TANGENT.md](FULL_SUZUKI_WEIL_TANGENT.md).

On \(I_A\), set

\[
H_{\omega,A}v=(k_\omega*R_0v)|_{I_A}.
\]

At \(\omega=0\), \(k_0=\delta_0\), so \(H_{0,A}=R_0\). The completed theorem is

\[
\boxed{
\lim_{\omega\downarrow0}
\frac{\|v\|_2^2-\|H_{\omega,A}v\|_2^2}{2\omega}
=Q(v),\qquad v\in C_c^\infty(I_A).
}
\tag{7.1}
\]

The limit is proved on each fixed test, with polarization. It uses the full \(\xi\)-ratio, not just its Euler factor. In particular, it includes the scalar at the origin in (4.3).

There is an essential topology boundary: for every \(\omega>0\), the local operator is compact, whereas \(H_{0,A}=R_0\) is not compact. Hence \(H_{\omega,A}\) cannot converge to \(R_0\) in operator norm. An estimate uniform over the unit ball cannot be inferred from (7.1). The full finite multiplicative space \(L^2(0,a)\), \(a=e^A\), also contains the inactive summand \(L^2(0,1/a)\); (7.1) is explicitly on its active logarithmic interval.

## 8. Work on the fixed completed form

For zero-extended \(v\) supported in \(I_A\), define

\[
\begin{aligned}
E_\Gamma(v)&=\int_0^\infty w_\Gamma(h)\|v-\tau_hv\|_2^2\,dh,\\
E_{P,A}(v)&=\sum_{h_n\le2A}a_n\|v-\tau_{h_n}v\|_2^2,\\
M_A&=\sum_{h_n\le2A}a_n,\qquad
d_A=\log\pi-\psi(1/4)+2M_A,\\
C(v)&=\int\cosh(t/2)v(t)\,dt,\qquad
S(v)=\int\sinh(t/2)v(t)\,dt.
\end{aligned}
\]

Expanding the translation squares and using (4.1) yields

\[
\boxed{
Q(v)=E_\Gamma(v)+E_{P,A}(v)
+2|C(v)|^2-2|S(v)|^2-d_A\|v\|_2^2.
}
\tag{8.1}
\]

Every coefficient and term in (8.1) is fixed before asking for positivity.

The Gamma/prime energy and scalar deficit in this identity were already obtained in [Round007's WEIL_SQUARE_ATTEMPT.md](https://github.com/femboy2112/FuckingRH/blob/8da6cf92d276961356497486048163f0aff08233/research/astra_round_007/WEIL_SQUARE_ATTEMPT.md). We retain that result and its bulk-deficit obstruction. The split below separates the two polar directions and supports the further domain, compact-operator, and horizon estimates. Define

\[
\mathsf P_A(v)=E_\Gamma(v)+E_{P,A}(v)+2|C(v)|^2,
\quad
\mathsf D_A(v)=d_A\|v\|_2^2+2|S(v)|^2.
\]

The RH inequality is precisely \(\mathsf D_A\le\mathsf P_A\) for every \(A\). Calling the first form positive does not prove it dominates the second.

### 8.1 An unconditional operator theorem

The Gamma energy has Fourier multiplier

\[
\alpha(u)=\Re\psi(1/4+iu/2)-\psi(1/4)
=2\sum_{m\ge0}\frac{u^2}{a_m(a_m^2+u^2)},
\quad a_m=2m+1/2.
\]

It is increasing in \(|u|\), strictly positive away from zero, and grows like \(\log|u|\). The full energy form is closed after completion of the core and has a compact embedding into \(L^2(I_A)\). Its associated operator \(\mathsf P_A\) is strictly positive with compact resolvent. Therefore

\[
\boxed{\mathsf B_A=\mathsf P_A^{-1/2}\mathsf D_A\mathsf P_A^{-1/2}}
\]

is a well-defined positive compact operator and

\[
Q\ge0\text{ on }I_A
\quad\Longleftrightarrow\quad
\|\mathsf B_A\|\le1.
\tag{8.2}
\]

This is a classical compact-operator reduction applied to the exact completed form. It is an equivalent target, not a positivity proof. A Bessel/bathtub bound gives

\[
\lambda_n(\mathsf P_A)\ge
\beta\!\left(\frac{\pi n}{2A}\right),\qquad
\beta(R)=\frac1R\int_0^R\alpha(u)\,du
=\log R+O(1).
\]

Since \(\mathsf D_A=d_AI+2|s_A\rangle\langle s_A|\), \(s_A=\sinh(t/2)1_{I_A}\), rank-one interlacing yields

\[
\lambda_{n+1}(\mathsf B_A)
\le\frac{d_A}{\beta(\pi n/(2A))}.
\]

Here the eigenvalues of \(\mathsf P_A\) are ordered increasingly, while those of the compact operator \(\mathsf B_A\) are ordered decreasingly, both with multiplicity.

The exact-domain proof and boundary conditions are supplied in the Gamma note. The underlying Bessel/bathtub method was already developed on the parent branch; this application is not a new-priority claim for that method.

### 8.2 A quantitative obstruction to a tempting proof strategy

Fix \(0\ne v\) supported in \(I_R\). For \(A\ge R\), newly included translations have disjoint support from \(v\), so

\[
\begin{aligned}
\mathsf P_A(v)&=\mathsf P_R(v)+2(M_A-M_R)\|v\|_2^2,\\
\mathsf D_A(v)&=\mathsf D_R(v)+2(M_A-M_R)\|v\|_2^2.
\end{aligned}
\]

Thus

\[
\boxed{\frac{\mathsf D_A(v)}{\mathsf P_A(v)}
=1-\frac{Q(v)}{\mathsf P_A(v)}\longrightarrow1.}
\tag{8.3}
\]

An elementary central-binomial estimate proves \(M_A\ge(\log2)e^A-o(e^A)\); PNT is not used. If \(Q(v)<0\), the ratio approaches one from above with excess \(O(e^{-A})\). Therefore a uniform strict bound \(\|\mathsf B_A\|\le1-\varepsilon\) is impossible, even under RH, and numerical ratios approaching one do not discriminate the sign.

### 8.3 A genuine short-interval inequality

The [explicit local certificate](LOCAL_POSITIVITY_CERTIFICATE.md) proves

\[
\boxed{Q(v)\ge\frac3{100}\|v\|_2^2
\quad\text{for }v\in V_A,\quad0<A\le\frac1{128}.}
\tag{8.4}
\]

Here \(V_A=\{v\in L^2(-A,A):E_\Gamma(v)<\infty\}\), using zero extension, is the closed form domain; in particular the estimate applies to every compact smooth test on the interval.

This follows from an explicit Fourier concentration estimate, a lower bound for \(\alpha\), and the exact scalar and odd rank correction. It is an unconditional, all-vectors statement on those intervals. Its deliberately conservative support size is a calibration, not an optimized theorem and not an all-horizon result.

## 9. Finite computation: a discriminator with a declared scope

The durable probe [rh_succ_weil_suzuki_probe.py](../../../scripts/rh_succ_weil_suzuki_probe.py) uses step cells on \([-A,A]\), exact translated-cell overlaps, Gamma quadrature, an independent exponential-series Gamma matrix, and the origin-renormalized explicit formula. Step functions lie in the logarithmic form domain and can be approximated there by compact smooth tests.

It records:

- agreement of the full square identity with the independent explicit formula;
- agreement of the box test with \(\Psi(2A)/A\) and of an odd Haar test with its Gamma series;
- the prime first derivative and exact finite-clock relations;
- mutations that omit the origin scalar, lose the triangle factor, or measure a translation difference only on the compressed interval;
- finite Ritz values for \(Q\), generalized Ritz values for \(\mathsf D_A/\mathsf P_A\), and fixed-test horizon cancellation.

All scanned eigenvalues are floating-point observations. A positive finite compression cannot certify all vectors on that interval. In particular, a finite maximum of \(\mathsf D_A/\mathsf P_A\) is a **lower** bound on the true compact-operator norm. The [finite certificate interface](FINITE_CERTIFICATE_INTERFACE.md) identifies the missing eigenvalue, projection, and tail bounds required to change that status.

## 10. The exact unpaid theorem and next proof process

The arithmetic-to-analytic bridge is now a chain of equations with assigned domains:

\[
\text{successor/divisibility}
\longrightarrow d\mu_P
\longrightarrow \xi'/\xi
\longrightarrow W=\Psi''
\longrightarrow Q
\longleftrightarrow K_\Psi
\longleftrightarrow\text{the full Suzuki tangent}.
\]

The arrows that introduce half-densities, completion, or a deformed conductor family explicitly state that input. The final sign is a separate theorem:

> **Unpaid all-horizon domination.** For every \(A>0\) and every \(v\) in the completed form domain on \((-A,A)\), prove
> \[
> d_A\|v\|_2^2+2|S(v)|^2
> \le E_\Gamma(v)+E_{P,A}(v)+2|C(v)|^2.
> \]

This statement is RH-equivalent. Neither a new name for it nor a positive factorization of only its right side advances the sign proof.

The next useful work has a concrete contract:

1. Keep (8.1), its scalar, and its domain fixed. Any modified target must be separately labelled and compared with the original.
2. Work first on an explicit containing interval. Produce either an analytic lower bound with a real margin, a rigorously enclosed negative witness, or a certified finite reduction with controlled complement and mixed block.
3. If using \(\mathsf B_A\), retain the cancelled \(Q\) and absolute error alongside normalized ratios. Equation (8.3) forbids a uniform strict-margin route.
4. To pass from individual intervals to all horizons, prove an actual stability or induction theorem that preserves the completed inequality. The prime jumps cancel in the decomposition and do not by themselves supply positive slack.
5. Stop and record a failed bound when an endpoint box, an odd mode, a high-frequency packet, a new prime-power event, or the true Gamma tail defeats it. A finite fit must not be promoted to a universal inequality.

The finite certificate note turns item 2 into an explicit spectral-tail inequality. The local theorem settles an initial support range. The unsolved step is how to extend positivity with a quantitatively adequate treatment of the completed boundary and prime correlations.

## Sources and attribution

The [claim ledger](PROVENANCE_AND_CLAIMS.md) contains the detailed source and first-appearance map. Main external sources are Masatoshi Suzuki, *Aspects of the screw function corresponding to the Riemann zeta function*, arXiv:2206.03682v4 (2023), *Weil's quadratic form via the screw function*, arXiv:2606.09096v3 (2026), and *A canonical system of differential equations arising from the Riemann zeta-function*, arXiv:1204.1827v2 (2016), together with classical Mellin, digamma, quadratic-form, and compact-operator results. Exact source titles and theorem references are recorded in that ledger after checking the primary texts.

The user supplied the organizing mathematical framing and requested this research/write-up. GPT-6 generated the synthesis, proofs, code, and same-model adversarial checks in this round. The connected GitHub account's commit attribution does not imply sole mathematical authorship by that account, and same-model checks are not external peer review.
