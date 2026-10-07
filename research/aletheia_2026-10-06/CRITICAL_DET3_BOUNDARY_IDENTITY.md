# Critical det_3 = combined boundary trace: endpoint determinant identification

**Date:** 2026-10-06  
**Status:** endpoint determinant-variation identity derived by trace powers away from conductor-entry seams, with integrable extension across the seam set. This identifies the positive det_3 ratio with Suzuki's critical combined boundary coefficient. **RH remains open.**

This note resolves one of the main endpoint identification problems left by the previous work.

Let

\[
T_a=H_{1/2,a}.
\]

We already have

\[
T_a=T_a^*,
\qquad
\|T_a\|<1,
\qquad
T_a\in S_3.
\]

Define

\[
\tau_1(a)
=
\int_0^a h_{1/2}(x^2)\,dx
\]

and

\[
\boxed{
m_3(a)
=
e^{2\tau_1(a)}
\frac{
\det_3(I+T_a)
}{
\det_3(I-T_a)
}.
}
\]

The critical boundary solutions satisfy

\[
\phi_a^\pm
=
(I\pm T_a)^{-1}h_a,
\qquad
h_a(x)=h_{1/2}(ax).
\]

The result is

\[
\boxed{
\frac{d}{da}\log m_3(a)
=
\phi_a^+(a)+\phi_a^-(a)
}
\]

for \(a^2\notin\mathbb N\), with the right side understood as the combined trace constructed in the previous note.

Equivalently,

\[
\boxed{
a\frac{d}{da}\log m_3(a)
=
\mu_{1/2}(a).
}
\]

---

## 1. Spectral expansion of the regularized determinant ratio

For a self-adjoint \(S_3\) contraction \(T\),

\[
\log
\frac{
\det_3(I+T)
}{
\det_3(I-T)
}
=
\sum_j
\left[
\log\frac{1+\lambda_j}{1-\lambda_j}
-2\lambda_j
\right].
\]

Since

\[
\log\frac{1+\lambda}{1-\lambda}
-2\lambda
=
2\sum_{m\ge1}
\frac{\lambda^{2m+1}}{2m+1},
\]

we obtain

\[
\boxed{
\log
\frac{
\det_3(I+T)
}{
\det_3(I-T)
}
=
2\sum_{m\ge1}
\frac{
\operatorname{Tr}T^{2m+1}
}{
2m+1
}.
}
\]

The series converges absolutely because

\[
T\in S_3
\]

and

\[
\|T\|<1.
\]

Therefore

\[
\boxed{
\log m_3(a)
=
2\tau_1(a)
+
2\sum_{m\ge1}
\frac{
\operatorname{Tr}T_a^{2m+1}
}{
2m+1
}.
}
\]

---

# 2. Domain-variation identity for trace powers

Let \(K(x,y)=h_{1/2}(xy)\) be the fixed symmetric kernel.

For an integer \(n\ge3\),

\[
\operatorname{Tr}T_a^n
=
\int_{(0,a)^n}
K(x_1,x_2)
K(x_2,x_3)
\cdots
K(x_n,x_1)
\,dx_1\cdots dx_n.
\]

For \(n\ge3\), this trace is absolutely meaningful because

\[
T_a^n\in S_1.
\]

Away from values \(a^2\in\mathbb N\), differentiating the moving-domain integral gives one boundary contribution from each of the \(n\) variables.

By cyclic symmetry all \(n\) boundary contributions are equal.

Therefore

\[
\boxed{
\frac d{da}
\operatorname{Tr}T_a^n
=
n\,[T_a^n](a,a)
}
\]

for

\[
a^2\notin\mathbb N.
\]

Here \([T_a^n](a,a)\) denotes the continuous/Hölder diagonal representative produced after enough kernel compositions.

The weak square-root singularities are integrable, so the same identity can be recovered by cutoff approximation if desired.

---

## 3. Differentiate the det_3 ratio

Using the trace-power expansion,

\[
\begin{aligned}
\frac d{da}
\log m_3(a)
&=
2\tau_1'(a)
+
2\sum_{m\ge1}
[T_a^{2m+1}](a,a).
\end{aligned}
\]

Away from seams,

\[
\boxed{
\tau_1'(a)
=
h_{1/2}(a^2)
=
K(a,a).
}
\]

Thus

\[
\boxed{
\frac d{da}
\log m_3(a)
=
2K(a,a)
+
2\sum_{m\ge1}
[T_a^{2m+1}](a,a).
}
\]

---

# 4. Expand the combined critical boundary solution

The exact resolvent identity gives

\[
\boxed{
\psi_a
:=
\phi_a^++\phi_a^-
=
2(I-T_a^2)^{-1}h_a.
}
\]

Since

\[
\|T_a\|<1,
\]

\[
(I-T_a^2)^{-1}
=
\sum_{m\ge0}T_a^{2m}
\]

in operator norm on \(L^2\), and compatibly on the endpoint \(L^q\) scale after regularization.

Therefore

\[
\psi_a
=
2\sum_{m\ge0}
T_a^{2m}h_a.
\]

But

\[
h_a(x)
=
K(x,a)
\]

is the boundary column of \(T_a\).

Hence

\[
\boxed{
(T_a^{2m}h_a)(a)
=
[T_a^{2m+1}](a,a).
}
\]

For \(m=0\),

\[
[T_a](a,a)
=
K(a,a)
=
h_{1/2}(a^2).
\]

Thus

\[
\boxed{
\psi_a(a)
=
2K(a,a)
+
2\sum_{m\ge1}
[T_a^{2m+1}](a,a).
}
\]

Comparing with the determinant derivative:

\[
\boxed{
\frac d{da}
\log m_3(a)
=
\psi_a(a)
=
\phi_a^+(a)+\phi_a^-(a).
}
\]

---

## 5. Suzuki's canonical coefficient survives exactly

Define

\[
\boxed{
\mu_{1/2}(a)
=
a\psi_a(a).
}
\]

Then

\[
\boxed{
a\frac d{da}\log m_3(a)
=
\mu_{1/2}(a)
}
\]

for every

\[
a>1,\qquad a^2\notin\mathbb N.
\]

This is exactly Suzuki's relation

\[
\mu(a)
=
a\frac{d}{da}\log m(a)
\]

from the regular regime.

So the \(\det_3\) ratio is not merely a positive candidate. It has the **correct infinitesimal canonical coefficient** at the critical endpoint.

---

# 6. Integrable conductor-entry singularities

The previous combined-trace analysis gives

\[
\mu_{1/2}(a)
\sim
\frac{
2\varphi(n)
}{
n^{3/4}
}
(a-\sqrt n)^{-1/2}
\]

as

\[
a\downarrow\sqrt n^+
\]

at leading order, subject to the already stated local-uniformity detail for the smoother resolvent correction.

This singularity is locally integrable.

Therefore

\[
\log m_3(a)
\]

is locally absolutely continuous across conductor-entry points, even though its derivative has square-root spikes.

In particular the natural integral identity is

\[
\boxed{
m_3(a)
=
\exp
\left(
\int_1^a
\mu_{1/2}(b)\frac{db}{b}
\right),
}
\]

with the integral interpreted across the integrable seam singularities.

For

\[
0<a\le1,
\]

the truncated Hankel operator is zero, so

\[
m_3(a)=1.
\]

---

## 7. Why the individual trace divergences are harmless

The first odd resolvent term

\[
T_ah_a
\]

is logarithmically singular at the boundary.

It appears with opposite signs in

\[
\phi_a^+
\quad\text{and}\quad
\phi_a^-.
\]

The determinant ratio also contains only **odd trace powers**, but after the regularized first term:

\[
T,\quad T^3,\quad T^5,\ldots.
\]

At criticality the problematic boundary self-interaction corresponds to the even spectral counterterm that is absent/canceled in the ratio.

Thus both sides perform the same parity cancellation.

This explains structurally why the combined boundary trace and regularized determinant are the correct physical objects.

---

# 8. Agreement with the regular regime

Whenever \(T_a\) is Hilbert--Schmidt and Suzuki's old Fredholm determinant exists,

\[
\frac{
\det_3(I+T_a)
}{
\det_3(I-T_a)
}
=
\frac{
\det_2(I+T_a)
}{
\det_2(I-T_a)
},
\]

because the quadratic regularization factors cancel in the ratio.

Restoring the first diagonal counterterm gives exactly the classical kernel Fredholm ratio.

Therefore the endpoint formula is a genuine continuation of Suzuki's determinant coefficient, not a new unrelated normalization.

---

## 9. What remains before claiming an endpoint canonical system theorem

The determinant coefficient is now identified.

Still required:

1. make the \(a\)-dependence and boundary regularity statements fully uniform at the seam points;
2. extend Suzuki's differential/distributional derivation of \(\widetilde A_a,\widetilde B_a\) using the critical \(L^q\) solutions;
3. prove the canonical equations hold with the positive Hamiltonian
   \[
   \operatorname{diag}(m_3^{-2},m_3^2);
   \]
4. verify the initial matching at \(a=1\) and the de Branges/scattering identities.

These are serious but now much narrower analytic tasks.

---

## 10. House result

\[
\boxed{
\text{The critical det}_3\text{ ratio has exactly Suzuki's canonical logarithmic derivative.}
}
\]

\[
\boxed{
\text{The same even-resolvent cancellation regularizes both the boundary trace and the determinant.}
}
\]

So the finite positive endpoint Hamiltonian candidate has passed the first nontrivial identification test.
