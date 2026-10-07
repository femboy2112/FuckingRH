# Critical determinant variation: renormalized trace and SUCC seam evolution

**Date:** 2026-10-06  
**Status:** exact \(\det_3\) variation identity under \(S_3\)-differentiability, plus a structural warning that the horizon evolution is not expected to be classically smooth at conductor-entry points. **RH remains open.**

---

## 1. Critical determinant candidate

At \(\omega=1/2\), let

\[
T(a)=H_{1/2,a}.
\]

The finite-horizon strict-contraction theorem gives

\[
\|T(a)\|<1.
\]

Assuming/using the Schatten result

\[
T(a)\in S_3,
\]

define

\[
\boxed{
m_3(a)
=
\exp(2\tau_1(a))
\frac{
\det_3(I+T(a))
}{
\det_3(I-T(a))
},
}
\]

where

\[
\boxed{
\tau_1(a)
=
\int_0^a
h_{1/2}(x^2)\,dx
}
\]

is the finite diagonal kernel counterterm.

---

## 2. General \(S_3\) derivative formula

For an \(S_3\)-differentiable family \(T(a)\), the third regularized determinant is

\[
\det_3(I+T)
=
\det\left[
(I+T)
e^{-T+T^2/2}
\right]
\]

in the standard regularized sense.

Its logarithmic derivative is

\[
\boxed{
\frac{d}{da}
\log\det_3(I+T)
=
\operatorname{Tr}
\left[
\left(
(I+T)^{-1}-I+T
\right)T'
\right].
}
\]

Similarly,

\[
\boxed{
\frac{d}{da}
\log\det_3(I-T)
=
\operatorname{Tr}
\left[
\left(
-(I-T)^{-1}+I+T
\right)T'
\right].
}
\]

Subtracting,

\[
\boxed{
\frac{d}{da}
\log
\frac{
\det_3(I+T)
}{
\det_3(I-T)
}
=
\operatorname{Tr}
\left[
\left(
(I+T)^{-1}
+
(I-T)^{-1}
-
2I
\right)T'
\right].
}
\]

Since

\[
(I+T)^{-1}
+
(I-T)^{-1}
=
2(I-T^2)^{-1},
\]

\[
\boxed{
\frac{d}{da}
\log
\frac{
\det_3(I+T)
}{
\det_3(I-T)
}
=
2
\operatorname{Tr}
\left[
\left(
(I-T^2)^{-1}-I
\right)T'
\right].
}
\]

---

## 3. Why the trace is genuinely regularized

For \(T\in S_3\),

\[
T^2\in S_{3/2}.
\]

Also

\[
(I-T^2)^{-1}-I
=
T^2(I-T^2)^{-1}
\in S_{3/2}.
\]

If

\[
T'\in S_3,
\]

then Schatten Hölder gives

\[
S_{3/2}S_3\subset S_1
\]

because

\[
\frac{2}{3}+\frac13=1.
\]

Therefore

\[
\boxed{
\left[
(I-T^2)^{-1}-I
\right]T'
\in S_1,
}
\]

and the trace is legitimate.

The subtraction by \(I\) is not cosmetic. It removes the non-trace-class first-order term.

---

## 4. Critical renormalized variation law

Differentiating \(m_3\) gives

\[
\boxed{
\frac{d}{da}\log m_3(a)
=
2\tau_1'(a)
+
2
\operatorname{Tr}
\left[
\left(
(I-T(a)^2)^{-1}-I
\right)
T'(a)
\right].
}
\]

Define the renormalized resolvent trace

\[
\boxed{
\mathfrak T_{\rm ren}(a)
=
\tau_1'(a)
+
\operatorname{Tr}
\left[
\left(
(I-T(a)^2)^{-1}-I
\right)
T'(a)
\right].
}
\]

Then

\[
\boxed{
\frac{d}{da}\log m_3(a)
=
2\mathfrak T_{\rm ren}(a).
}
\]

This is the natural critical replacement for Suzuki's classical determinant variation coefficient.

---

# 5. Consistency with the ordinary determinant in an overlap regime

Suppose temporarily that \(T\) is trace class and smooth enough that

\[
\tau_1'(a)=\operatorname{Tr}T'(a).
\]

Then

\[
\begin{aligned}
\mathfrak T_{\rm ren}
&=
\operatorname{Tr}T'
+
\operatorname{Tr}
\left[
((I-T^2)^{-1}-I)T'
\right]\\
&=
\operatorname{Tr}
\left[
(I-T^2)^{-1}T'
\right].
\end{aligned}
\]

Therefore

\[
\boxed{
\frac{d}{da}\log m_3(a)
=
2
\operatorname{Tr}
\left[
(I-T^2)^{-1}T'
\right],
}
\]

which is exactly the formal variation of

\[
\log\frac{\det(I+T)}{\det(I-T)}.
\]

So the renormalized formula matches the old one when the latter exists.

---

# 6. The horizon family is not expected to be globally \(S_3\)-smooth

This is crucial.

Move all operators to a fixed space \(L^2(0,1)\) by dilation:

\[
(D_af)(u)
=
a^{1/2}f(au).
\]

Then the transformed kernel is

\[
\boxed{
\widetilde K_a(u,v)
=
a\,h_{1/2}(a^2uv).
}
\]

The \(n\)-th conductor seam lies at

\[
\boxed{
uv=\frac{n}{a^2}.
}
\]

As \(a\) varies, this singular curve moves.

At the activation value

\[
\boxed{
a=\sqrt n,
}
\]

a new seam first enters the unit square.

Therefore ordinary differentiability in \(a\) cannot simply be assumed globally.

The critical evolution has a natural discrete event set

\[
\{\sqrt n:n\in\mathbb N\}.
\]

This is precisely the SUCC conductor-entry schedule found independently in the discrete realization.

---

## 7. Canonical evolution should be treated as a Stieltjes/product-integral evolution

Rather than insist on

\[
\frac{d}{da}Y(a,z)
=
A(a,z)Y(a,z)
\]

with a smooth coefficient everywhere, the natural critical form is

\[
\boxed{
dY
=
\mathcal A_{\rm cont}(a,z)Y\,da
+
\sum_n
\mathcal J_n(z)Y\,
\delta_{\sqrt n}(da),
}
\]

or an equivalent measure-valued canonical/product-integral formulation.

Between conductor-entry events, the \(\det_3\) variation formula applies in the ordinary way if the required differentiability is established.

At an event

\[
a=\sqrt n,
\]

the exact finite conductor block \(W_n\) supplies the jump/boundary update.

This is not an artificial patch: it directly reflects the arithmetic growth of the finite system.

---

## 8. Relation to Suzuki's smoother \(\omega>1\) construction

For \(\omega>1\), the kernel is continuous and differentiable enough for Suzuki's classical Fredholm-minor derivation of

\[
\mu(a)
=
a\phi_a^+(a)+a\phi_a^-(a)
\]

and

\[
m(a)
=
\exp\left(
\int_1^a\mu(b)\frac{db}{b}
\right)
\]

to proceed as an ordinary differential canonical system.

At criticality, the arithmetic event locations are no longer smoothed away by enough regularity.

The SUCC/FUCC interpretation suggests this is meaningful rather than pathological:

\[
\boxed{
\text{the canonical clock becomes visibly event-driven at the half-density endpoint}.
}
\]

---

## 9. Exact research target

A publication-grade critical extension now requires:

1. prove piecewise \(S_3\)-differentiability or an appropriate weaker variation theorem away from \(a=\sqrt n\);
2. calculate the singular/jump contribution at each conductor-entry seam using \(W_n\);
3. show the total logarithmic variation measure equals the boundary coefficient required by Suzuki's canonical system;
4. prove the resulting product integral has the same terminal \(\Theta_{1/2}\) scattering data.

The finite-horizon invertibility needed for all resolvents is already available.

---

## 10. House statement

\[
\boxed{
\text{At criticality, determinant renormalization is smooth between integers and arithmetic at the seams.}
}
\]

\[
\boxed{
\text{The subtraction in }\det_3\text{ removes the divergent bulk trace.}
}
\]

\[
\boxed{
\text{The remaining nonsmoothness is exactly where SUCC says a new conductor block is born.}
}
\]
