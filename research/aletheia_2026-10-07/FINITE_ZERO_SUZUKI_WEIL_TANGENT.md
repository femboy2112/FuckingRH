# Finite-zero theorem: Weil's Gram form is the exact tangent of Suzuki passivity

**Date:** 2026-10-07  
**Status:** exact finite-dimensional/rational theorem. The passage to the full xi zero set is a separate distributional form-limit theorem and is not silently assumed here.  
**RH remains open.**

This note supplies a calibrated model for the proposed \(\omega\downarrow0\) Suzuki-to-Weil bridge.

The result is exact for **every finite symmetry-closed zero multiset**:

\[
\boxed{
\text{Weil Gram operator}
=
\left.
\frac{d}{d(2\omega)}
\bigl(I-C_{\omega,T}^{*}C_{\omega,T}\bigr)
\right|_{\omega=0}.
}
\]

This fixes the normalization and shows that the relation is structural, not an analogy.

---

# 1. Finite xi model

Let

\[
\Lambda
\]

be a finite multiset of complex numbers closed under

\[
\lambda\mapsto-\lambda,
\qquad
\lambda\mapsto\overline{\lambda}.
\]

Think of

\[
\lambda=\rho-\frac12
\]

for a finite symmetry-closed selection of nontrivial zeta zeros.

Define the finite even polynomial

\[
\boxed{
\Xi_\Lambda(s)
=
\prod_{\lambda\in\Lambda}(s-\lambda).
}
\]

Because \(\Lambda=-\Lambda\), its degree is even and

\[
\Xi_\Lambda(-s)=\Xi_\Lambda(s).
\]

Because \(\Lambda=\overline\Lambda\), it has real coefficients.

Define the finite Suzuki scattering ratio

\[
\boxed{
B_{\omega,\Lambda}(s)
=
\frac{
\Xi_\Lambda(s-\omega)
}{
\Xi_\Lambda(s+\omega)
}.
}
\]

Then

\[
\boxed{
B_{\omega,\Lambda}(s)
B_{\omega,\Lambda}(-s)
=
1.
}
\]

So the finite model has the same meromorphic all-pass symmetry as the genuine Suzuki transfer.

---

# 2. First variation

Let

\[
\boxed{
L_\Lambda(s)
=
\frac{\Xi_\Lambda'(s)}
     {\Xi_\Lambda(s)}
=
\sum_{\lambda\in\Lambda}
\frac1{s-\lambda}.
}
\]

Taylor expansion at \(\omega=0\) gives

\[
\boxed{
B_{\omega,\Lambda}(s)
=
1-2\omega L_\Lambda(s)+O(\omega^2).
}
\]

Because the model is rational, this expansion is ordinary finite-dimensional algebra away from the finite pole set.

For \(\Re s>\max_{\lambda\in\Lambda}\Re\lambda\),

\[
\mathcal L^{-1}
\left[
\frac1{s-\lambda}
\right](t)
=
e^{\lambda t}1_{t\ge0}.
\]

Therefore the causal first-variation kernel is

\[
\boxed{
\ell_\Lambda(t)
=
\sum_{\lambda\in\Lambda}
e^{\lambda t},
\qquad
t\ge0.
}
\]

---

# 3. Finite-time causal operator

On

\[
L^2(0,T),
\]

define

\[
\boxed{
(\mathcal L_{\Lambda,T}f)(t)
=
\int_0^t
\ell_\Lambda(t-u)f(u)\,du.
}
\]

Let

\[
C_{\omega,\Lambda,T}
\]

be the finite causal convolution operator whose transfer is \(B_{\omega,\Lambda}\), including the identity impulse at \(\omega=0\).

Then, in operator norm for this finite rational model,

\[
\boxed{
C_{\omega,\Lambda,T}
=
I
-
2\omega\mathcal L_{\Lambda,T}
+
O(\omega^2).
}
\]

Consequently,

\[
\begin{aligned}
I-C_{\omega,\Lambda,T}^{*}C_{\omega,\Lambda,T}
&=
2\omega
\left(
\mathcal L_{\Lambda,T}
+
\mathcal L_{\Lambda,T}^{*}
\right)
+
O(\omega^2).
\end{aligned}
\]

Define

\[
\boxed{
A_{\Lambda,T}
=
\mathcal L_{\Lambda,T}
+
\mathcal L_{\Lambda,T}^{*}.
}
\]

Then

\[
\boxed{
\frac{
I-C_{\omega,\Lambda,T}^{*}C_{\omega,\Lambda,T}
}{
2\omega
}
\longrightarrow
A_{\Lambda,T}
}
\]

in operator norm as \(\omega\to0\).

---

# 4. The symmetric operator has the finite Weil kernel

Because the zero multiset is closed under \(\lambda\mapsto-\lambda\),

\[
\ell_\Lambda(-r)
=
\ell_\Lambda(r).
\]

Because it is closed under conjugation,

\[
\ell_\Lambda(r)\in\mathbb R
\qquad(r\in\mathbb R).
\]

For \(t>u\), the kernel of \(\mathcal L_{\Lambda,T}\) is

\[
\ell_\Lambda(t-u).
\]

For \(t<u\), the kernel of its adjoint is

\[
\ell_\Lambda(u-t)
=
\ell_\Lambda(t-u).
\]

Therefore, off the measure-zero diagonal,

\[
\boxed{
A_{\Lambda,T}(t,u)
=
\sum_{\lambda\in\Lambda}
e^{\lambda(t-u)}.
}
\]

Translate the interval \([0,T]\) to

\[
[-T/2,T/2].
\]

If

\[
\lambda=i\gamma,
\]

then by the symmetry of the complete multiset,

\[
\sum_{\lambda\in\Lambda}
e^{\lambda(t-u)}
=
\sum_{\gamma\in\Gamma_\Lambda}
e^{-i\gamma(t-u)}.
\]

This is exactly the finite version of the formal difference kernel used for the Weil operator.

---

# 5. Finite Weil Gram form

For \(f\in L^2(0,T)\),

\[
\begin{aligned}
\langle A_{\Lambda,T}f,f\rangle
&=
\sum_{\lambda\in\Lambda}
\int_0^T\int_0^T
e^{\lambda(t-u)}
f(u)\overline{f(t)}
\,du\,dt.
\end{aligned}
\]

Writing

\[
\lambda=i\gamma
\]

and using the Fourier convention

\[
\widehat f(z)
=
\int f(t)e^{izt}\,dt,
\]

this is the finite spectral Weil expression

\[
\boxed{
Q_\Lambda(f)
=
\sum_{\gamma\in\Gamma_\Lambda}
\widehat f(\gamma)
\overline{\widehat f(\overline\gamma)}.
}
\]

Hence

\[
\boxed{
\langle A_{\Lambda,T}f,f\rangle
=
Q_\Lambda(f).
}
\]

Combining with the first variation:

\[
\boxed{
\lim_{\omega\to0}
\frac{
\|f\|_2^2
-
\|C_{\omega,\Lambda,T}f\|_2^2
}{
2\omega
}
=
Q_\Lambda(f).
}
\]

This is the finite-zero Suzuki--Weil tangent theorem.

---

# 6. On-line zeros give positive rank-two blocks

Suppose

\[
\lambda=\pm i\gamma,
\qquad
\gamma\in\mathbb R.
\]

The corresponding kernel is

\[
e^{i\gamma(t-u)}
+
e^{-i\gamma(t-u)}
=
2\cos(\gamma(t-u)).
\]

And

\[
2\cos(\gamma(t-u))
=
2[
\cos(\gamma t)\cos(\gamma u)
+
\sin(\gamma t)\sin(\gamma u)
].
\]

Therefore each on-line conjugate pair contributes a positive-semidefinite operator of rank at most two.

This is the finite Gram manifestation of Weil positivity under RH.

---

# 7. Off-line quartets are intrinsically indefinite

Let

\[
\lambda
=
r+i\gamma,
\qquad
r\ne0,
\]

and include the full quartet

\[
\{\lambda,\overline\lambda,-\lambda,-\overline\lambda\}.
\]

Its kernel contribution is

\[
\boxed{
4\cosh(r(t-u))\cos(\gamma(t-u)).
}
\]

Unlike the \(r=0\) kernel, this is not a positive Gram kernel in general.

Thus an off-line quartet changes the infinitesimal passivity defect from a sum of positive rank-two blocks into an indefinite Hermitian form.

This provides a mutation-sensitive negative control:

\[
\boxed{
\text{move a zero pair off the critical line}
\Longrightarrow
\text{create a negative direction in the finite Weil tangent}
}
\]

for suitable finite horizons/test states.

The exact horizon at which a chosen fake quartet exposes a negative eigenvalue depends on \(r\) and \(\gamma\); the companion numerical probe checks this behavior.

---

# 8. Passage to the genuine xi function

Put

\[
\Xi(s)
=
\xi\!\left(\frac12+s\right).
\]

Then

\[
\Xi(-s)=\Xi(s).
\]

Because the zero offsets occur in \(\pm\) pairs and

\[
\sum_\rho
|\rho-\tfrac12|^{-2}
<\infty,
\]

the even Hadamard product can be organized as

\[
\boxed{
\Xi(s)
=
\Xi(0)
\prod_{\lambda\in\Lambda_+}
\left(
1-\frac{s^2}{\lambda^2}
\right)
}
\]

with locally uniform convergence.

Formally differentiating gives

\[
\boxed{
\frac{\Xi'(s)}{\Xi(s)}
=
\sum_{\lambda\in\Lambda_+}
\left(
\frac1{s-\lambda}
+
\frac1{s+\lambda}
\right).
}
\]

For every fixed finite zero truncation this is exactly the object of Sections 1--7.

The full inverse Laplace transform is no longer an ordinary function: the zero sum has an ultraviolet/distributional singularity at \(t=0\).

This is not an accident. Suzuki's 2026 localized Weil operator is precisely a self-adjoint realization of the distributional difference kernel

\[
\boxed{
k(t-u)
=
\sum_{\rho}
e^{-i\gamma(t-u)},
\qquad
\rho=\frac12+i\gamma.
}
\]

Equivalently, Suzuki writes the Weil form using the screw function \(g\) with distributional kernel

\[
-g''(t-u).
\]

Thus the finite-zero tangent converges toward the already established Weil operator architecture.

---

# 9. The one remaining analytic theorem

The finite theorem fixes the expected infinite result and its normalization:

## Suzuki--Weil tangent theorem target

For

\[
f\in C_c^\infty(0,T),
\]

prove

\[
\boxed{
\lim_{\omega\downarrow0}
\frac{
\|f\|_2^2
-
\|C_{\omega,T}f\|_2^2
}{
2\omega
}
=
Q_W(f_T),
}
\]

where \(f_T\) denotes the translation of \(f\) from \([0,T]\) to

\[
[-T/2,T/2].
\]

Equivalently, in quadratic-form language,

\[
\boxed{
\frac{
I-C_{\omega,T}^{*}C_{\omega,T}
}{
2\omega
}
\longrightarrow
A_{T/2},
}
\]

after the translation unitary, on a common smooth form core.

This statement is **UNVERIFIED** for the full infinite zero set.

The remaining debt is now narrow and analytic:

1. establish the distributional derivative
   \[
   \partial_\omega k_\omega|_{\omega=0}
   =
   -2\,\mathcal L^{-1}
   \left[
   \Xi'/\Xi
   \right];
   \]

2. show the resulting causal first-variation operator has symmetric part equal to Suzuki's localized Weil distribution;

3. justify passage from distributional convergence to the quadratic-form limit on \(C_c^\infty\);

4. close the form and identify the Friedrichs extension with Suzuki's \(A_{T/2}\).

No arithmetic conjecture is required for those four steps.

---

# 10. Why this matters for the proof program

We now have two finite-horizon RH interfaces:

### Nonlinear Suzuki passivity

\[
\|C_{\omega,T}\|\le1
\quad
\forall\omega>0,\ T>0.
\]

### Linearized Weil positivity

\[
Q_W^a(f)\ge0
\quad
\forall a>0,\ f.
\]

The finite-zero theorem proves that the second is the exact tangent of the first at the true endpoint \(\omega=0\).

So these are not competing reformulations.

They are the same geometry at different resolution:

\[
\boxed{
\text{Suzuki finite passivity}
\ \xrightarrow{\ \omega\downarrow0\ }\ 
\text{Weil finite positivity}.
}
\]

If the infinite tangent theorem closes, the repo should treat this as the permanent bridge between the 2012 finite Hankel program and Suzuki's 2026 finite-interval Weil program.

The RH-bearing problem then becomes:

\[
\boxed{
\text{make the finite Weil/passivity form positive from the discrete conductor/carry architecture.}
}
\]

That is the same fixed dragon, now seen both nonlinearly and infinitesimally.
