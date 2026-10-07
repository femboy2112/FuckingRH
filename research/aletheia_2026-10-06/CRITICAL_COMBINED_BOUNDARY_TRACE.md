# Critical combined boundary trace: odd singularities cancel and Suzuki's canonical coefficient survives

**Date:** 2026-10-06  
**Status:** endpoint boundary-trace mechanism derived from the \(L^q\) solutions and fractional smoothing. A full publication-grade proof of uniform parameter dependence remains to be written. **RH remains open.**

The individual critical solutions \(\phi_a^\pm\) are too singular for naive pointwise boundary evaluation. However Suzuki's canonical coefficient uses only their sum, and this sum has a much better structure.

The key exact algebraic cancellation is

\[
\boxed{
\phi_a^+ + \phi_a^-
=
2(I-H_a^2)^{-1}h_a.
}
\]

At the critical half-integral seam, \(H_a^2\) gains one full order of regularity. This makes the combined boundary trace well defined away from conductor-entry points and shows that its seam singularities are integrable.

---

## 1. Critical endpoint equations

Write

\[
T_a:=H_{1/2,a},
\qquad
h_a(x):=h_{1/2}(ax).
\]

For any fixed

\[
1<q<2,
\]

the preceding \(L^q\) endpoint theorem gives unique solutions

\[
\boxed{
\phi_a^+
=
(I+T_a)^{-1}h_a,
}
\]

\[
\boxed{
\phi_a^-
=
(I-T_a)^{-1}h_a.
}
\]

They lie in \(L^q(0,a)\).

---

## 2. Exact even/odd resolvent decomposition

Use

\[
(I+T)^{-1}
=
(I-T)(I-T^2)^{-1},
\]

\[
(I-T)^{-1}
=
(I+T)(I-T^2)^{-1}.
\]

Adding,

\[
\boxed{
(I+T)^{-1}
+
(I-T)^{-1}
=
2(I-T^2)^{-1}.
}
\]

Therefore

\[
\boxed{
\psi_a
:=
\phi_a^+ + \phi_a^-
=
2(I-T_a^2)^{-1}h_a.
}
\]

Subtracting,

\[
\boxed{
\phi_a^--\phi_a^+
=
2T_a(I-T_a^2)^{-1}h_a.
}
\]

Thus the individual odd-\(T\) contribution, which carries the worst boundary self-interaction, cancels completely from the sum used in Suzuki's canonical coefficient.

---

# 3. Why the individual boundary traces are problematic

At criticality, near one active seam

\[
x_0=\frac n a,
\]

the forcing behaves as

\[
h_a(x)
\sim
C_{n,a}
(x-x_0)_+^{-1/2}.
\]

At the outer boundary \(x=a\), the kernel \(h_{1/2}(ay)\) has the same singularity at

\[
y=x_0.
\]

Therefore the first odd iterate

\[
(T_ah_a)(a)
=
\int_0^a
h_{1/2}(ay)h_{1/2}(ay)\,dy
\]

contains locally

\[
\int
\frac{dy}{y-x_0},
\]

a logarithmic divergence.

This explains why neither

\[
\phi_a^+(a)
\quad\text{nor}\quad
\phi_a^-(a)
\]

should be expected to exist naively at the critical endpoint.

But the divergent \(T_ah_a\) term appears with opposite signs in \(\phi_a^\pm\) and cancels in their sum.

---

## 4. Two half-integrations give one full smoothing order

The principal singularity of \(T_a\) is locally a reflected Riemann--Liouville half-integral.

For

\[
1<q<2,
\]

\[
T_a:
L^q
\longrightarrow
L^r,
\qquad
\frac1r=\frac1q-\frac12.
\]

Then

\[
r>2.
\]

A second application of the half-integral maps \(L^r\) into a Hölder/continuous class, since

\[
\frac12-\frac1r
=
1-\frac1q
>0.
\]

Thus, after localization over the finitely many seams,

\[
\boxed{
T_a^2:
L^q(0,a)
\longrightarrow
C^{\,1-1/q}_{\rm loc}
}
\]

up to the harmless smooth pieces and boundary restrictions.

Because

\[
\|T_a\|_{L^2}<1
\]

and \(I-T_a^2\) is invertible on the relevant Banach scale, the resolvent expansion

\[
(I-T_a^2)^{-1}
=
I+T_a^2+T_a^4+\cdots
\]

shows that

\[
\boxed{
\psi_a-2h_a
=
2T_a^2(I-T_a^2)^{-1}h_a
}
\]

has a continuous/Hölder representative.

This is the endpoint regularization mechanism.

---

# 5. Critical canonical coefficient away from entry seams

If

\[
a^2\notin\mathbb N,
\]

the boundary point \(x=a\) is not itself a singular point of

\[
h_a(x)=h_{1/2}(ax).
\]

Hence \(h_a(a)=h_{1/2}(a^2)\) is finite.

The correction

\[
\psi_a-2h_a
\]

has a continuous representative at \(x=a\).

Therefore the combined trace

\[
\boxed{
\psi_a(a)
}
\]

is well defined for

\[
a^2\notin\mathbb N.
\]

Define

\[
\boxed{
\mu_{1/2}(a)
=
a\,\psi_a(a)
=
a[\phi_a^+(a)+\phi_a^-(a)]
}
\]

for such \(a\).

This is the exact same algebraic quantity Suzuki uses in the smooth regime, now interpreted through the combined endpoint trace.

---

## 6. Singular coefficient of \(h_{1/2}\) at an integer

At

\[
x\to n^+,
\]

only the \(n\)-th term of the arithmetic sum creates the new singularity.

Using

\[
c_{1/2}(n)
=
\frac{\varphi(n)}{\sqrt n}
\]

and

\[
g_{1/2}(n/x)
\sim
\sqrt2
\left(1-\frac n x\right)^{-1/2},
\]

we obtain

\[
\boxed{
h_{1/2}(x)
\sim
\frac{
\sqrt2\,\varphi(n)
}{
n
}
(x-n)^{-1/2}.
}
\]

This coefficient is exact at leading order.

---

# 7. The canonical coefficient has explicit square-root event spikes

Let

\[
a\downarrow\sqrt n
\]

from above.

Then

\[
a^2-n
\sim
2\sqrt n\,(a-\sqrt n).
\]

The direct forcing term in

\[
\psi_a(a)
=
2h_{1/2}(a^2)
+
\text{continuous correction}
\]

therefore contributes

\[
2h_{1/2}(a^2)
\sim
\frac{
2\sqrt2\,\varphi(n)
}{
n
}
(a^2-n)^{-1/2}.
\]

Multiplying by \(a\sim\sqrt n\),

\[
\mu_{1/2}(a)
\sim
\frac{
2\sqrt2\,\varphi(n)
}{
\sqrt n
}
(a^2-n)^{-1/2}.
\]

Using the local conversion above,

\[
\boxed{
\mu_{1/2}(a)
\sim
\frac{
2\varphi(n)
}{
n^{3/4}
}
(a-\sqrt n)^{-1/2}
}
\]

from the right, provided the continuous resolvent correction remains locally bounded in the parameter \(a\).

The latter boundedness is the remaining technical point to formalize uniformly across seam entry.

The leading coefficient itself is forced by the exact local singularity.

---

## 8. The spikes are integrable

Since

\[
(a-\sqrt n)^{-1/2}
\]

is locally integrable,

\[
\boxed{
\mu_{1/2}\in L^1_{\rm loc}
}
\]

is compatible with these conductor-entry singularities.

Therefore the natural canonical evolution is not a jump process with delta masses.

It is a **piecewise regular evolution with integrable square-root impulse densities** at

\[
a=\sqrt n.
\]

This corrects the earlier crude "jump at every conductor entry" picture.

---

# 9. Critical canonical evolution as an absolutely-continuous/Stieltjes limit

The natural candidate is

\[
\boxed{
m(a)
=
\exp
\left(
\int_1^a
\mu_{1/2}(b)\frac{db}{b}
\right).
}
\]

Because the event spikes are integrable, \(m(a)\) should remain continuous across

\[
a=\sqrt n
\]

even though its logarithmic derivative diverges integrably from the right.

This is a much closer endpoint analogue of Suzuki's smooth formula than a literal multiplicative jump.

---

## 10. Relation to the det_3 variation

The determinant candidate gives

\[
\frac{d}{da}\log m_3(a)
=
2\tau_1'(a)
+
2\operatorname{Tr}
\left[
((I-T_a^2)^{-1}-I)T_a'
\right]
\]

where differentiable.

The combined solution gives

\[
\mu_{1/2}(a)
=
2a
\left[
h_a(a)
+
(T_a^2(I-T_a^2)^{-1}h_a)(a)
\right].
\]

These expressions have the same structural decomposition:

### direct / first-order counterterm

\[
h_a(a)
\quad\leftrightarrow\quad
\tau_1'(a),
\]

### even resolvent correction

\[
T_a^2(I-T_a^2)^{-1}
\quad\leftrightarrow\quad
((I-T_a^2)^{-1}-I).
\]

Therefore the exact next theorem is:

\[
\boxed{
\frac{d}{da}\log m_3(a)
=
\frac{\mu_{1/2}(a)}a
}
\]

away from conductor-entry seams, followed by extension across the integrable spikes.

This would identify the positive \(\det_3\) Hamiltonian with the critical Suzuki boundary-solution Hamiltonian.

---

## 11. Why this is a serious narrowing of the wall

We no longer need individual critical traces

\[
\phi_a^\pm(a).
\]

We need only their sum, and the exact resolvent algebra removes the first singular odd iterate automatically.

So the endpoint problem has reduced to:

1. formalize \(T_a^2:L^q\to C^\alpha\);
2. prove local uniformity in \(a\);
3. prove the det_3/boundary-trace variation identity;
4. transport Suzuki's remaining canonical-system proof using \(\psi_a\).

The worst endpoint singularity has already canceled algebraically.

---

## 12. House result

\[
\boxed{
\text{The individual critical boundary states are singular.}
}
\]

\[
\boxed{
\text{The physical/canonical combination is their even resolvent and is much smoother.}
}
\]

\[
\boxed{
\text{One half-integral is singular; two half-integrals restore a boundary trace.}
}
\]

\[
\boxed{
\text{The conductor clock appears as integrable }(a-\sqrt n)^{-1/2}\text{ pulses with amplitude }2\varphi(n)n^{-3/4}.
}
\]

This is the strongest current endpoint boundary mechanism.
