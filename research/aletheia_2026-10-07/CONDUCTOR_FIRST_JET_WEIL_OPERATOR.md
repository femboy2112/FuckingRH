# Conductor first jet gives the prime-shift Weil operator

**Date:** 2026-10-07  
**Status:** exact first-order operator algebra for the arithmetic/conductor sector in finite log-Hankel coordinates. The Archimedean distributional first jet is treated separately. No RH assumption.  
**RH remains open.**

This note upgrades the coefficient identity

\[
b_0'(n)=2\Lambda(n)n^{-1/2}
\]

to an operator identity.

At \(\omega=0\), the finite Suzuki Hankel machine is the basic reflection in log coordinates. Opening one prime-power conductor channel at first order composes that reflection with a shifted reflection. Their product is translation. Symmetrizing the passivity defect produces exactly the prime-shift term in Suzuki's localized Weil operator.

Thus the arithmetic part of the Weil operator is not merely coefficientwise compatible with the conductor model: it is the first derivative of the finite conductor **operator geometry**.

---

# 1. Log-Hankel coordinates

Let

\[
A=\log a,
\]

and work on

\[
L^2(-A,A).
\]

After the unitary logarithmic map

\[
(Uf)(u)=e^{u/2}f(e^u),
\]

Suzuki's finite Hankel operator has kernel

\[
k_\omega(u+v),
\qquad
k_\omega(t)=e^{t/2}h_\omega(e^t).
\]

The arithmetic event decomposition is

\[
\boxed{
k_\omega(t)
=
\sum_{n\ge1}
b_\omega(n)\,
K_\omega(t-\log n),
}
\]

where \(K_\omega\) is the universal Archimedean log kernel and only the finitely many events \(n<e^{2A}=a^2\) act on the finite interval.

The conductor coefficient is

\[
b_\omega(n)
=
n^{\omega-\frac12}
\prod_{p\mid n}(1-p^{-2\omega}).
\]

---

# 2. The omega-zero base operator is reflection

At the true endpoint,

\[
b_0(1)=1,
\qquad
b_0(n)=0\quad(n>1).
\]

The completed transfer satisfies

\[
B_0(s)=1.
\]

Therefore the causal Toeplitz representation at \(\omega=0\) is the identity.

Before the reflection that turns Hankel into Toeplitz, the corresponding log-Hankel operator is the reflection

\[
\boxed{
(R_0f)(u)=f(-u).
}
\]

Thus

\[
\boxed{
H_{0,A}=R_0,
\qquad
R_0^2=I.
}
\]

The unit conductor is the base reflection state.

---

# 3. A conductor event is a shifted reflection

Fix a conductor event

\[
n,
\qquad
h=\log n.
\]

At first order, the singular event kernel is concentrated on

\[
u+v=h.
\]

Define the shifted reflection

\[
\boxed{
(R_hf)(u)=f(h-u),
}
\]

with the understanding that \(f\) is zero-extended outside \([-A,A]\).

Then the arithmetic first-order contribution from conductor \(n\) is

\[
\boxed{
b_0'(n)R_h.
}
\]

The omega-zero conductor-jet theorem gives

\[
b_0'(n)
=
\frac{2\Lambda(n)}{\sqrt n}.
\]

Hence only prime powers appear at first order.

---

# 4. Reflection composition is translation

Let

\[
(\tau_hf)(u)=f(u-h)
\]

on the zero-extended line.

A direct computation gives

\[
\boxed{
R_hR_0=\tau_h,
}
\]

because

\[
(R_hR_0f)(u)
=
R_0f(h-u)
=
f(u-h).
\]

Likewise,

\[
\boxed{
R_0R_h=\tau_{-h}.
}
\]

Therefore

\[
\boxed{
R_hR_0+R_0R_h
=
\tau_h+\tau_{-h}.
}
\]

This is the exact algebraic source of the reflected prime shifts in Weil's explicit formula.

---

# 5. Differentiate the passivity defect

Let

\[
H_{\omega,A}
=
R_0+\omega H_A^{(1)}+O(\omega^2)
\]

in the formal/finite arithmetic first-jet sense.

Because the operator is self-adjoint,

\[
H_{\omega,A}^*H_{\omega,A}
=
H_{\omega,A}^2.
\]

Differentiate:

\[
\left.
\frac d{d\omega}
H_{\omega,A}^2
\right|_{\omega=0}
=
H_A^{(1)}R_0
+
R_0H_A^{(1)}.
\]

Therefore the infinitesimal passivity defect is

\[
\boxed{
\left.
\frac d{d\omega}
\left(
I-H_{\omega,A}^2
\right)
\right|_{\omega=0}
=
-
\left(
H_A^{(1)}R_0
+
R_0H_A^{(1)}
\right).
}
\]

Now isolate the arithmetic first jet:

\[
H_{A,\mathrm{prime}}^{(1)}
=
\sum_{n\le e^{2A}}
\frac{2\Lambda(n)}{\sqrt n}R_{\log n}.
\]

Substitute:

\[
\begin{aligned}
-\frac12
\left[
H_{A,\mathrm{prime}}^{(1)}R_0
+
R_0H_{A,\mathrm{prime}}^{(1)}
\right]
&=
-\sum_{n\le e^{2A}}
\frac{\Lambda(n)}{\sqrt n}
\left(
R_{\log n}R_0
+
R_0R_{\log n}
\right)
\\
&=
\boxed{
-\sum_{n\le e^{2A}}
\frac{\Lambda(n)}{\sqrt n}
\left(
\tau_{\log n}
+
\tau_{-\log n}
\right).
}
\end{aligned}
\]

This is exactly the prime-power translation operator in Suzuki's localized Weil kernel.

---

# 6. Quadratic-form identity

For \(v\) zero-extended outside the finite interval,

\[
\left\langle
(\tau_h+\tau_{-h})v,
v
\right\rangle
=
2\Re\langle\tau_hv,v\rangle.
\]

Thus the arithmetic first-jet passivity form is

\[
\boxed{
-2
\sum_{n\le e^{2A}}
\frac{\Lambda(n)}{\sqrt n}
\Re\langle\tau_{\log n}v,v\rangle.
}
\]

This is precisely the prime term in Suzuki's explicit finite-interval formula.

Using

\[
-2\Re\langle\tau_hv,v\rangle
=
\|v-\tau_hv\|^2
-
2\|v\|^2,
\]

it becomes

\[
\boxed{
\sum_{p^k\le e^{2A}}
\frac{\log p}{p^{k/2}}
\|v-\tau_{k\log p}v\|^2
-
2
\left(
\sum_{p^k\le e^{2A}}
\frac{\log p}{p^{k/2}}
\right)
\|v\|^2.
}
\]

Therefore the nonlocal prime-ray first jet is a positive Dirichlet energy, and only its diagonal completion carries the negative mass.

---

# 7. Why this derivation is independent of the zero-side derivation

There are now two routes to the same operator.

## Route A: zero/scattering side

Differentiate

\[
B_\omega(s)
=
\frac{\xi(s+\frac12-\omega)}
{\xi(s+\frac12+\omega)}
\]

at \(\omega=0\):

\[
B_\omega(s)
=
1
-
2\omega
\frac{\xi'}{\xi}(s+\tfrac12)
+
O(\omega^2).
\]

Use the explicit formula / zero distribution to identify the symmetric first variation with the Weil kernel.

## Route B: conductor/event side

Differentiate the exact conductor coefficients:

\[
b_0'(n)=2\Lambda(n)n^{-1/2}.
\]

Each conductor event is a shifted reflection \(R_{\log n}\).

Compose with the base unit-conductor reflection \(R_0\):

\[
R_{\log n}R_0=\tau_{\log n}.
\]

Symmetrize the passivity defect.

This produces the prime translation operator directly.

The two routes agree exactly.

Their shared provenance is only the Suzuki family itself; the local derivations use different decompositions.

---

# 8. The Archimedean remainder

The arithmetic derivation above recovers exactly

\[
-\sum_n
\frac{\Lambda(n)}{\sqrt n}
(\tau_{\log n}+\tau_{-\log n}).
\]

The full localized Weil operator additionally contains the Archimedean/distributional terms:

- the finite-part \(1/|t|\) kernel;
- the scalar delta term;
- the smooth remainder \(r''\).

Those must arise from the \(\omega\)-derivative of the universal Archimedean block together with the unit-conductor channel.

Coefficientwise, the companion omega-zero conductor-jet note already proves

\[
\left.
\partial_\omega\log G_\omega(s)
\right|_0
=
\log\pi
-
\frac2{s+\frac12}
-
\frac2{s-\frac12}
-
\psi\!\left(\frac{s+\frac12}{2}\right),
\]

which is exactly the completed Archimedean logarithmic derivative.

The remaining analytic task is to take its inverse transform in the same distributional normalization as Suzuki's \(g''\) and verify equality of the finite-interval quadratic forms.

No arithmetic unknown remains in this Archimedean matching step.

---

# 9. The fixed first-jet wall

After the arithmetic operator has been derived directly from conductor geometry, the RH-bearing inequality is

\[
\boxed{
Q_W^A(v)\ge0
\qquad
\forall A>0,\ v.
}
\]

In square-completed coordinates:

\[
\boxed{
\mathcal L_A(v)
+
\sum_{p^k\le e^{2A}}
\frac{\log p}{p^{k/2}}
\|v-\tau_{k\log p}v\|^2
\ge
\mathcal V_A\|v\|^2
+
\langle R_Av,v\rangle.
}
\]

This note proves that the prime-ray translation part on the left is the first derivative of the exact finite-conductor machine.

So the remaining question is no longer:

> Why should the von Mangoldt weights appear?

or:

> Why do prime translations occur?

Both are now explained structurally.

The remaining question is:

\[
\boxed{
\textbf{Why does the exact global Archimedean/diagonal completion never overwhelm the positive continuous + prime-ray difference energy?}
}
\]

That is the present RH wall.
