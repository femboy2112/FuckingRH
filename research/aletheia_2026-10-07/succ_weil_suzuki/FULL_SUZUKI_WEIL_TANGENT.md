# The full Suzuki–Weil tangent on a compact smooth core

**Session date:** 2026-10-07.  
**Scope:** an unconditional identity between a first variation of finite Suzuki Hankel forms and the completed Weil form.  
**RH status:** no positivity theorem or proof of RH is claimed.

| Claim ID | Statement established here | Boundary |
| --- | --- | --- |
| SWS-002 | The derivative at zero of the finite Hankel norm defect is exactly twice the Weil form. | Every fixed finite active interval and every fixed compactly supported smooth test function; distributional kernel differentiation and differentiation of vectors/forms. |
| SWS-003 | The family cannot converge to its zero-parameter reflection in operator norm. | The complete infinite-dimensional $L^2$ space of a fixed nonempty active interval. |

The concrete result is

\[
\boxed{
\lim_{\omega\downarrow0}
\frac{\|v\|_2^2-\|H_{\omega,A}v\|_2^2}{2\omega}
=Q_W(v),
\qquad A>0,\quad v\in C_c^\infty(-A,A).
}
\tag{T}
\]

This completes the analytic matching left open in the earlier arithmetic first-jet notes. It includes the Gamma factor, both polynomial factors in the completed xi function, the origin distribution, and the prime-power events. It does not infer the sign of either side.

## 1. Provenance and relation to the earlier work

Leah's successor/carry, Gamma, and Dirac-event ideas motivated the question addressed here: how to turn the project's conductor arithmetic into a rigorously defined family whose first variation is the actual Weil form. The derivation in this note was developed by the GPT-6 assistant and checked through a bounded audit by another agent of the same model. That is an additional check within a shared provenance family, not independent peer review. No priority or novelty claim is made.

Two earlier repository notes at the fixed commit `0840c3905f27b96f8d6011d85523130ffbab48aa` supply the arithmetic starting point:

- [OMEGA_ZERO_CONDUCTOR_JET.md](https://github.com/femboy2112/FuckingRH/blob/0840c3905f27b96f8d6011d85523130ffbab48aa/research/aletheia_2026-10-07/OMEGA_ZERO_CONDUCTOR_JET.md): the coefficient identity $b'_0(n)=2\Lambda(n)/\sqrt n$.
- [CONDUCTOR_FIRST_JET_WEIL_OPERATOR.md](https://github.com/femboy2112/FuckingRH/blob/0840c3905f27b96f8d6011d85523130ffbab48aa/research/aletheia_2026-10-07/CONDUCTOR_FIRST_JET_WEIL_OPERATOR.md): shifted reflections produce the reflected prime translations; its final Archimedean matching step was explicitly left open.

The classical anchors are Suzuki's shifted-xi Hankel construction [S12], his screw-function normalization and Weil identity [S23], and standard beta/digamma integrals [B, P]. The explicit Weil normalization is also displayed in the later paper [S26]. All source links are listed in Section 10.

The present note supplies the missing distributional and topological argument. Earlier references to an operator expansion at zero should be read in the precise smooth-core sense proved below. An operator-norm expansion is false by SWS-003.

## 2. Conventions and the target form

Use the completed function

\[
\xi(q)=\gamma(q)\zeta(q),
\qquad
\gamma(q)=\frac12q(q-1)\pi^{-q/2}\Gamma(q/2).
\]

The Laplace variable is $s$, and throughout

\[
q=s+\frac12,
\qquad
\mathcal L f(s)=\int_0^\infty f(t)e^{-st}\,dt.
\]

For distributions supported in $[0,\infty)$, the Laplace transform is taken in a right half-plane where the exponentially weighted distribution is tempered. Its derivative rule is the distributional rule

\[
\mathcal L(DT)(s)=s\,\mathcal LT(s).
\]

This convention already includes distributions at the origin. It does not require ordinary initial derivative values.

On complex $L^2$, the inner product is linear in the first entry:

\[
\langle f,h\rangle=\int f(t)\overline{h(t)}\,dt.
\]

Set

\[
\widehat f(z)=\int_{\mathbb R}f(t)e^{izt}\,dt,
\qquad
\widetilde f(t)=\overline{f(-t)}.
\]

Let $\gamma_E$ denote Euler's constant, and define the completed Weil distribution on $f\in C_c^\infty(\mathbb R)$ by

\[
\begin{aligned}
W(f)={}&
\int_{\mathbb R}(e^{t/2}+e^{-t/2})f(t)\,dt\\
&-\sum_{n\ge1}\frac{\Lambda(n)}{\sqrt n}
\bigl(f(\log n)+f(-\log n)\bigr)
-(\log(4\pi)+\gamma_E)f(0)\\
&-\int_0^\infty
\frac{e^{-t/2}}{1-e^{-2t}}
\bigl(f(t)+f(-t)-2e^{-t/2}f(0)\bigr)\,dt.
\end{aligned}
\tag{2.1}
\]

The apparent origin singularity in the last integral is canceled by its displayed subtraction. The sum is finite on the support of $f$. This is a real, even distribution, and

\[
Q_W(v,w)=W(v*\widetilde w),
\qquad Q_W(v)=Q_W(v,v).
\tag{2.2}
\]

Weil's positivity criterion is the classical statement that $Q_W(v)\ge0$ for every $v\in C_c^\infty(\mathbb R)$ is equivalent to RH; see [S23, Section 3.2]. This criterion identifies the eventual inequality target. Its validity does not supply that inequality.

## 3. Constructing the causal source without a boundary multiplier

For real $\omega>0$, define

\[
\begin{aligned}
J_\omega(t)
&=\frac{2\pi^\omega}{\Gamma(\omega)}
e^{(\omega-1/2)t}
(1-e^{-2t})^{\omega-1}\mathbf1_{t>0},\\
R_{\omega,\pm}
&=\delta_0-2\omega
e^{-(\omega\pm1/2)t}\mathbf1_{t>0},\\
K_\omega&=J_\omega*R_{\omega,+}*R_{\omega,-}.
\end{aligned}
\tag{3.1}
\]

All convolutions here are causal convolutions. They are well-defined because the supports are bounded below. Near zero, $J_\omega(t)$ is a constant times $t^{\omega-1}$; thus $K_\omega\in L^1_{\mathrm{loc}}$ for every positive $\omega$.

With $u=e^{-2t}$, the beta integral [B] gives

\[
\begin{aligned}
\mathcal LJ_\omega(s)
&=\frac{\pi^\omega}{\Gamma(\omega)}
\int_0^1u^{(q-\omega)/2-1}(1-u)^{\omega-1}\,du\\
&=\pi^\omega
\frac{\Gamma((q-\omega)/2)}{\Gamma((q+\omega)/2)}.
\end{aligned}
\tag{3.2}
\]

Also

\[
\mathcal LR_{\omega,\pm}(s)
=1-\frac{2\omega}{s+\omega\pm1/2}
=\frac{s-\omega\pm1/2}{s+\omega\pm1/2}.
\tag{3.3}
\]

The individual Archimedean transforms converge together, for example, in $\Re s>|\omega-1/2|$. Their product is

\[
\boxed{
\mathcal LK_\omega(s)
=G_\omega(s):=\frac{\gamma(q-\omega)}{\gamma(q+\omega)}.
}
\tag{3.4}
\]

The arithmetic event distribution and its coefficients are

\[
\nu_\omega=\sum_{n\ge1}b_\omega(n)\delta_{\log n},
\qquad
b_\omega(n)=n^{\omega-1/2}
\prod_{p\mid n}(1-p^{-2\omega}).
\tag{3.5}
\]

The empty product makes $b_\omega(1)=1$. Define the full source

\[
\boxed{
k_\omega=\nu_\omega*K_\omega
=\sum_{n\ge1}b_\omega(n)K_\omega(t-\log n).
}
\tag{3.6}
\]

The sum in (3.6) is locally finite. In the common absolute-convergence half-plane

\[
\Re s>\frac12+\omega,
\tag{3.7}
\]

the Euler product gives

\[
\mathcal L\nu_\omega(s)
=\frac{\zeta(q-\omega)}{\zeta(q+\omega)}.
\]

Therefore

\[
\boxed{
\mathcal Lk_\omega(s)
=B_\omega(s)
:=\frac{\xi(q-\omega)}{\xi(q+\omega)}.
}
\tag{3.8}
\]

This construction uses only explicit causal functions, distributions, and convergent transforms in (3.7). It does not identify a real-boundary unitary multiplier with a causal convolution operator.

For comparison with [S12], if $h_\omega$ and $g_\omega$ have Suzuki's multiplicative-coordinate meanings, transform uniqueness gives

\[
K_\omega(t)=e^{-t/2}g_\omega(e^{-t}),
\qquad
k_\omega(t)=e^{t/2}h_\omega(e^t).
\tag{3.9}
\]

Indeed Suzuki's coefficient $c_\omega(n)$ is $\sqrt n\,b_\omega(n)$, so his formula for $h_\omega$ transforms term by term into (3.6).

## 4. The active finite interval

Fix $A>0$, put $I_A=(-A,A)$, and extend its functions by zero to the line. Let

\[
(Rv)(u)=v(-u),
\qquad
(H_{\omega,A}v)(u)
=\int_{-A}^{A}k_\omega(u+y)v(y)\,dy
=(k_\omega*Rv)(u),\quad u\in I_A.
\tag{4.1}
\]

For $\omega>0$, Young's inequality gives

\[
\|H_{\omega,A}\|
\le\|k_\omega\|_{L^1(0,2A)}<\infty.
\tag{4.2}
\]

The kernel is real and symmetric in (u,y), so this bounded operator is self-adjoint. Only events with $\log n\le2A$ can act. The endpoint event makes no difference to the action on the compact smooth core.

The interval is the active part of Suzuki's multiplicative operator. For $a=e^A>1$, the latter acts on $L^2(0,a)$ with kernel $h_\omega(xy)$. Since $h_\omega(x)=0$ for (x<1), its summand $L^2(0,1/a)$ is inactive. The unitary map

\[
(Uf)(u)=e^{u/2}f(e^u)
\]

identifies $L^2(1/a,a;dx)$ with $L^2(I_A;du)$ and gives (4.1). Thus $H_{0,A}=R$ below is a statement on this active interval. Using the full identity on $L^2(0,a)$ would also leave a constant identity defect on its inactive summand.

## 5. Analytic continuation of the source through zero

### 5.1. Normalized power distributions: the subtraction argument

Initially for $\Re\omega>0$, let

\[
T_\omega=\frac{t_+^{\omega-1}}{\Gamma(\omega)}.
\]

For $\phi\in C_c^\infty(\mathbb R)$, subtract its value at zero on $(0,1)$:

\[
\begin{aligned}
\langle T_\omega,\phi\rangle
={}&\frac{\phi(0)}{\Gamma(1+\omega)}\\
&+\frac1{\Gamma(\omega)}
\left[
\int_0^1t^{\omega-1}(\phi(t)-\phi(0))\,dt
+\int_1^\infty t^{\omega-1}\phi(t)\,dt
\right].
\end{aligned}
\tag{5.1}
\]

The bracket is holomorphic for $\Re\omega>-1$. Its derivatives are controlled by fixed test-function seminorms on each compact parameter neighborhood of zero. Formula (5.1) therefore defines an analytic distribution family there, and

\[
T_0=\delta_0.
\tag{5.2}
\]

In particular, the first derivative is fixed without an arbitrary origin constant:

\[
\langle T'_0,\phi\rangle
=\gamma_E\phi(0)
+\int_0^1\frac{\phi(t)-\phi(0)}{t}\,dt
+\int_1^\infty\frac{\phi(t)}{t}\,dt.
\tag{5.3}
\]

Subtracting further Taylor coefficients extends this normalized power family farther if needed; the neighborhood established by (5.1) is sufficient here.

### 5.2. Apply the argument to the full source

Let

\[
a(t)=\frac{1-e^{-2t}}{2t},\qquad a(0)=1.
\]

This is smooth and positive for real $t$, with its removable value at zero understood. Rewrite (3.1) as

\[
J_\omega
=(2\pi)^\omega e^{(\omega-1/2)t}
a(t)^{\omega-1}T_\omega.
\tag{5.4}
\]

The multiplier is smooth in $t$ and analytic in $\omega$, using the real logarithm of (a(t)>0). At $\omega=0,t=0$ its value is one. Hence $J_0=\delta_0$ and $J_\omega$ is locally analytic in distributions through zero.

The two $R_{\omega,\pm}$ are analytic causal distribution families with $R_{0,\pm}=\delta_0$. On each compact interval, causal convolution only uses compact portions of their supports. It consequently preserves this analytic dependence. The coefficients $b_\omega(n)$ are analytic, and only finitely many of them contribute on a compact time interval. Therefore

\[
k_\omega\text{ is locally analytic in }\mathcal D'(\mathbb R)
\text{ near }0,
\qquad k_0=\delta_0.
\tag{5.5}
\]

This also verifies $H_{0,A}=R$ directly in the source construction.

Differentiating (3.8) in a sufficiently far right common half-plane gives

\[
\left.\partial_\omega B_\omega(s)\right|_0
=-2\frac{\xi'}{\xi}\left(s+\frac12\right).
\tag{5.6}
\]

Here transform differentiation is justified from the explicit factors: exponential damping controls the tails, the subtraction in (5.1) controls the origin, and the arithmetic series and its parameter derivatives converge uniformly after moving the vertical line sufficiently far right. For example, for $0\le\omega\le\varepsilon$, the first two derivatives of $b_\omega(n)$ are bounded by constants times $n^{\varepsilon-1/2}(1+\log n)^2$. Laplace uniqueness then identifies the locally defined distribution derivative.

## 6. Identify the origin term and the complete Weil distribution

### 6.1. The causal logarithmic derivative

Let $L$ be the causal distribution with transform

\[
\mathcal LL(s)=\frac{\xi'}{\xi}\left(s+\frac12\right),
\qquad\Re s>\frac12.
\tag{6.1}
\]

One can define it directly, including its origin subtraction. The digamma integral [P]

\[
\psi(z)+\gamma_E
=\int_0^\infty\frac{e^{-u}-e^{-zu}}{1-e^{-u}}\,du,
\qquad\Re z>0,
\]

combined with the logarithmic derivative of $\gamma(q)\zeta(q)$, gives

\[
\begin{aligned}
\langle L,\phi\rangle={}&
\int_0^\infty(e^{t/2}+e^{-t/2})\phi(t)\,dt
-\sum_{n\ge1}\frac{\Lambda(n)}{\sqrt n}\phi(\log n)\\
&-\frac{\log\pi+\gamma_E}{2}\phi(0)
+\int_0^\infty
\frac{e^{-2t}\phi(0)-e^{-t/2}\phi(t)}{1-e^{-2t}}\,dt.
\end{aligned}
\tag{6.2}
\]

The numerator in the final integral vanishes to first order at zero. At infinity its noncompact term decays exponentially. Thus (6.2) defines a causal distribution on all compact smooth tests and has precisely transform (6.1).

Equations (5.6) and (6.1) now give the unconditional source identity

\[
\boxed{k'_0=-2L.}
\tag{6.3}
\]

For a distribution (T), write $T^\vee(t)=T(-t)$, defined by reflection of test functions. Symmetrizing (6.2), and using

\[
2\int_0^\infty
\frac{e^{-2t}-e^{-t}}{1-e^{-2t}}\,dt
=-2\log2=-\log4,
\tag{6.4}
\]

gives exactly (2.1). The integral in (6.4) follows from $x=e^{-t}$, which reduces the unmultiplied integral to $-\int_0^1(1+x)^{-1}\,dx$. Consequently

\[
\boxed{L+L^\vee=W.}
\tag{6.5}
\]

In particular, the scalar contact term is $-\log(4\pi)-\gamma_E$, not a freely chosen renormalization. The identity (6.4) is the conversion between the causal and symmetric subtraction conventions.

### 6.2. Match Suzuki's continuous primitive

For $t\ge0$, define Suzuki's function with its full arithmetic formula [S23]:

\[
\begin{aligned}
\Psi(t)={}&4(e^{t/2}+e^{-t/2}-2)
-\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n)\\
&+\frac t2\bigl(\psi(1/4)-\log\pi\bigr)\\
&+\frac14\left[
\Phi(1,2,1/4)-e^{-t/2}\Phi(e^{-2t},2,1/4)
\right].
\end{aligned}
\tag{6.6}
\]

Here $\Phi(z,2,a)=\sum_{m\ge0}z^m/(m+a)^2$. Extend $\Psi$ evenly to the line. It is continuous and $\Psi(0)=0$. Suzuki's unilateral transform, with $z=is$, is

\[
\int_0^\infty\Psi(t)e^{-st}\,dt
=\frac1{s^2}\frac{\xi'}{\xi}\left(s+\frac12\right),
\qquad\Re s>\frac12.
\tag{6.7}
\]

Let $\Psi_+=\mathbf1_{t>0}\Psi(t)$, as a locally integrable distribution. The causal distributional derivative rule and (6.7) imply

\[
\boxed{
L=D^2\Psi_+,
\qquad
k'_0=-2D^2\Psi_+,
\qquad
W=D^2\Psi.
}
\tag{6.8}
\]

There is no assumption that $\Psi'(0+)$ is finite. In fact [S26, Section 2.2] gives

\[
\Psi(t)=-\frac12|t|\log|t|
-\frac12\bigl(\log(2\pi)+\gamma_E-1\bigr)|t|
+O(t^2).
\tag{6.9}
\]

The logarithmic origin singularity is retained by (6.2), (6.6), and the distributional differentiation in (6.8).

## 7. SWS-002: the form tangent theorem

**Theorem.** For $A>0$ and $v,w\in C_c^\infty(I_A)$, define

\[
\mathfrak D_{\omega,A}(v,w)
=\langle v,w\rangle
-\langle H_{\omega,A}v,H_{\omega,A}w\rangle.
\tag{7.1}
\]

Then

\[
\boxed{
\left.\frac d{d\omega}\mathfrak D_{\omega,A}(v,w)\right|_{0+}
=2Q_W(v,w).
}
\tag{7.2}
\]

Equivalently,

\[
\boxed{
\lim_{\omega\downarrow0}
\frac{\mathfrak D_{\omega,A}(v,w)}{2\omega}
=Q_W(v,w).
}
\tag{7.3}
\]

All zero extensions and inner products in this statement use the fixed interval $I_A$. For $\omega>0$, self-adjointness permits writing the diagonal defect as $\langle(I-H_{\omega,A}^2)v,v\rangle$; this notation does not assert operator-norm differentiability.

**Proof.** Choose $\chi\in C_c^\infty(\mathbb R)$ equal to one on a neighborhood of ([0,2A]). Causality and the support of $Rv$ imply

\[
H_{\omega,A}v=((\chi k_\omega)*Rv)|_{I_A}.
\]

The compactly supported distribution family $\chi k_\omega$ is analytic near zero by Section 5. Convolution against the fixed compact smooth function $Rv$ is analytic in $C^\infty(\overline I_A)$: derivatives in the spatial argument fall on $Rv$, and the required test-function seminorms are uniform for that argument in the compact interval. In particular it is analytic in $L^2(I_A)$, with

\[
H_{\omega,A}v
=Rv-2\omega(L*Rv)|_{I_A}+O_{A,v}(\omega^2)
\quad\text{in }L^2(I_A).
\tag{7.4}
\]

This is a statement for a fixed test vector; its remainder is not an operator-norm estimate.

Differentiate the squared norm in (7.1). The diagonal derivative is

\[
\left.\frac d{d\omega}\mathfrak D_{\omega,A}(v,v)\right|_0
=4\Re\langle L*Rv,Rv\rangle.
\tag{7.5}
\]

For a compact smooth $f$, the reality of $L$ gives the adjoint-kernel identity

\[
2\Re\langle L*f,f\rangle
=\langle(L+L^\vee)*f,f\rangle
=\langle W*f,f\rangle.
\tag{7.6}
\]

The final pairing equals $W(f*\widetilde f)$: the direct convolution pairing first produces the reflected autocorrelation, and reflection has no effect because $W$ is even. Thus (7.5) equals $2Q_W(Rv)$. Again by evenness of $W$,

\[
Q_W(Rv)=Q_W(v)
\]

for complex as well as real $v$. This proves (7.2) on the diagonal.

Both sides are Hermitian sesquilinear forms, linear in their first entry. Applying the polarization identity

\[
F(v,w)=\frac14\sum_{j=0}^3i^jF(v+i^jw,v+i^jw)
\tag{7.7}
\]

proves (7.2) for complex $v,w$. Finally $H_{0,A}=R$ is unitary, so $\mathfrak D_{0,A}=0$. This yields (7.3). \(\square\)

### A direct connection with the screw kernel

Define the anchored continuous kernel

\[
\mathcal K_\Psi(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u).
\]

Since compactly supported derivatives have integral zero, (6.8) and two integrations by parts give the established screw/Weil identity

\[
Q_W(v,w)
=\int_{\mathbb R^2}\mathcal K_\Psi(t,u)
v'(u)\overline{w'(t)}\,du\,dt.
\tag{7.8}
\]

This is [S23, Proposition 3.1] in the present conventions. Combining (7.3) and (7.8) identifies the finite Hankel norm tangent with the continuous screw-kernel form, including all Archimedean terms.

## 8. SWS-003: why the topology restriction is necessary

**Proposition.** For every fixed $A>0$ and $\omega>0$, $H_{\omega,A}$ is compact on $L^2(I_A)$, but

\[
\boxed{
\|H_{\omega,A}-R\|\ge1,
\qquad
\|I-H_{\omega,A}^2\|\ge1.
}
\tag{8.1}
\]

Thus the family is not operator-norm continuous at $\omega=0$, and the normalized defect in (7.3) has no bounded-operator norm limit.

**Proof.** Approximate $k_\omega$ on $(0,2A)$ in $L^1$ by bounded smooth kernels. Each resulting finite Hankel operator has a bounded kernel on $I_A\times I_A$ and is Hilbert–Schmidt, hence compact. Young's inequality bounds the operator-norm approximation error by the $L^1$ error of the kernels. Therefore $H_{\omega,A}$ is compact for every positive $\omega$, including $0<\omega\le1/2$, where the original kernel need not be Hilbert–Schmidt.

Let $(e_m)$ be any orthonormal sequence in $L^2(I_A)$. It converges weakly to zero, so compactness gives $H_{\omega,A}e_m\to0$ in norm. Since $R$ is unitary,

\[
\|(H_{\omega,A}-R)e_m\|\longrightarrow1.
\]

This proves the first inequality. The same argument applied to the compact operator $H_{\omega,A}^2$ proves the second. In particular

\[
\left\|\frac{I-H_{\omega,A}^2}{2\omega}\right\|
\ge\frac1{2\omega}\longrightarrow\infty.
\tag{8.2}
\]

The convergence on fixed compact smooth vectors in Theorem SWS-002 is compatible with these operator-norm obstructions. \(\square\)

## 9. The remaining inequality and its exact quantifiers

Theorem SWS-002 proves a bridge, not a sign. It yields the following conditional route directly, without an additional pole-cancellation argument.

Suppose that, for every $A>0$ and every $v\in C_c^\infty(I_A)$, there is a positive sequence $\omega_j\to0$ along which

\[
\|H_{\omega_j,A}v\|_2\le\|v\|_2.
\tag{9.1}
\]

Then (7.3) implies $Q_W(v)\ge0$ for every compact smooth test, and Weil's criterion implies RH. The sequence may depend on $A,v$. An all-vector operator contraction bound on every finite interval along a common sequence of shrinking parameters is a stronger sufficient hypothesis.

No statement in this note establishes (9.1). The coefficient identities, positive conductor weights, existence of the causal source, and distributional analyticity by themselves do not imply contractivity. A finite numerical sample would likewise establish neither the quantified contraction nor Weil positivity.

The work completed here is precise: the arithmetic first jet and the full Archimedean first jet now meet in one verified quadratic-form identity, with the factor, origin subtraction, reflection, active interval, and differentiation topology fixed.

## 10. Sources

- **[S12]** Masatoshi Suzuki, *A canonical system of differential equations arising from the Riemann zeta-function*, arXiv:1204.1827v2. See Proposition 2.1, formulas (2.1)–(2.4), Theorem 2.2, and the finite Hankel construction in Section 4. [Versioned PDF](https://arxiv.org/pdf/1204.1827v2).
- **[S23]** Masatoshi Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, arXiv:2206.03682v4, 2023. See formulas (1.1)–(1.3), Theorem 1.1, Section 3.2, and Proposition 3.1. [Versioned PDF](https://arxiv.org/pdf/2206.03682v4).
- **[S26]** Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3, 2026. Used for the displayed completed Weil normalization and origin expansion in Section 2.2. [Versioned PDF](https://arxiv.org/pdf/2606.09096v3).
- **[B]** NIST Digital Library of Mathematical Functions, Euler's beta integral, equation 5.12.1. [Formula](https://dlmf.nist.gov/5.12.E1).
- **[P]** NIST Digital Library of Mathematical Functions, digamma integral, equation 5.9.16. [Formula](https://dlmf.nist.gov/5.9.E16).

The mathematical derivation is recorded here; numerical control results, if produced separately, must be reported with their actual execution scope. The same-model audit and primary-source checks are not a claim of independent peer review.
