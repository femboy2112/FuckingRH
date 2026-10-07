# Gamma is not an inner Weyl channel: a Blaschke obstruction

**Date:** 2026-10-06  
**Status:** exact no-go preventing a circular/incorrect Weyl construction. **RH remains open.**

The Archimedean functional-equation factor has unit modulus on the real critical-line coordinate, but this does **not** make it an inner/Schur function in the upper half-plane.

This distinction is load-bearing.

---

## 1. Centered Gamma scattering factor

Define

\[
\Theta_\infty(z)
=
\chi\!\left(\frac12+iz\right)
=
\pi^{iz}
\frac{
\Gamma(\frac14-\frac{iz}{2})
}{
\Gamma(\frac14+\frac{iz}{2})
}.
\]

For real \(t\),

\[
\boxed{
|\Theta_\infty(t)|=1.
}
\]

Moreover,

\[
\Theta_\infty(t)
=
e^{-2i\vartheta(t)}.
\]

So it is a perfect all-pass phase on the physical real axis.

---

## 2. Its upper-half-plane zeros are the trivial-zero ladder

The denominator Gamma function has poles when

\[
\frac14+\frac{iz}{2}
=
-m,
\qquad m\in\mathbb N_0.
\]

Therefore \(\Theta_\infty\) has zeros at

\[
\boxed{
z_m
=
i\left(2m+\frac12\right).
}
\]

These are exactly the trivial-zero locations after the critical-line coordinate change

\[
s=\frac12+iz.
\]

The numerator Gamma poles lie in the lower half-plane, so \(\Theta_\infty\) is analytic at these upper-half-plane zeros.

---

## 3. Blaschke condition fails

A nonzero bounded analytic function on the upper half-plane must have zeros satisfying the Blaschke condition

\[
\sum_m
\frac{
\Im z_m
}{
1+|z_m|^2
}
<\infty.
\]

Here

\[
\frac{
\Im z_m
}{
1+|z_m|^2
}
=
\frac{
2m+\frac12
}{
1+(2m+\frac12)^2
}
\sim
\frac1{2m}.
\]

Hence

\[
\boxed{
\sum_m
\frac{
\Im z_m
}{
1+|z_m|^2
}
=
\infty.
}
\]

Therefore

\[
\boxed{
\Theta_\infty
\notin H^\infty(\mathbb C_+).
}
\]

In particular it is **not** an inner/Schur function on \(\mathbb C_+\).

So the inference

\[
|\Theta_\infty(t)|=1\text{ on }\mathbb R
\Longrightarrow
\Theta_\infty\text{ inner}
\]

is false.

---

## 4. Disk version of the same obstruction

Under the Cayley map

\[
w=\frac{z-i}{z+i},
\]

the zeros

\[
z_m=i y_m,
\qquad
y_m=2m+\frac12,
\]

map to

\[
w_m
=
\frac{y_m-1}{y_m+1}
\to1.
\]

The disk Blaschke condition would require

\[
\sum_m
(1-|w_m|)
<\infty.
\]

But

\[
1-w_m
=
\frac2{y_m+1}
\sim
\frac1m,
\]

so again the sum diverges.

---

## 5. Why zeta-regularized determinant language did not contradict this

Previous work derived

\[
\Theta_\infty(z)
=
(2\pi)^{iz}
\frac{
\det_\zeta(H_0+iz)
}{
\det_\zeta(H_0-iz)
},
\]

with

\[
H_0|m\rangle
=
\left(2m+\frac12\right)|m\rangle.
\]

This is a **zeta-regularized** determinant ratio.

It is not the ordinary convergent Blaschke/Fredholm determinant of a trace-class perturbation.

The regularization precisely permits the non-Blaschke zero density.

Therefore no bounded-inner conclusion follows from the determinant ratio alone.

---

## 6. Completion removes the obstruction locally

The same upper-half-plane points

\[
z_m=i\left(2m+\frac12\right)
\]

correspond to

\[
s=-2m,
\]

the trivial zeta zeros.

In the completed logarithmic derivative,

\[
\frac12\psi(s/2)
+
\frac{\zeta'}{\zeta}(s),
\]

the Gamma pole and trivial-zero pole cancel with opposite residues.

Thus the non-Blaschke Archimedean ladder is removed from the completed residual spectrum.

This gives a new structural interpretation of the exact trivial-zero cancellation:

\[
\boxed{
\text{completion removes the local non-Blaschke obstruction before the global Weyl test.}
}
\]

---

## 7. No orientation trick fixes Gamma alone

Taking

\[
\Theta_\infty^{-1}
\]

does not help.

It replaces the upper-half-plane zeros by upper-half-plane poles, so it is not analytic there.

Therefore neither orientation of the bare Gamma scattering factor gives the desired Schur channel.

The arithmetic trivial-zero sector is essential.

---

## 8. Correct Weyl target comes only after completion

The legitimate completed candidate is

\[
m_\Xi(z)
=
-\frac{\Xi'(z)}{\Xi(z)}.
\]

Its poles are only the nontrivial zero modes because the trivial/Gamma ladder has already canceled.

The exact criterion is

\[
\boxed{
RH
\iff
m_\Xi\text{ is Herglotz}.
}
\]

So the ordering of the construction must be:

\[
\boxed{
\text{prime arithmetic}
+
\text{Gamma/trivial sector}
\to
\text{exact cancellation/completion}
\to
\text{Weyl/Herglotz test}.
}
\]

It is invalid to demand ordinary Weyl positivity of the Gamma channel in isolation.

---

## 9. Consequence for the causal-network program

The finite prime subsystems can be individually Schur/passive.

The bare Gamma subsystem is only a real-axis all-pass/regularized scattering factor, not a bounded Schur component.

Therefore a global passive-network construction must incorporate the trivial arithmetic modes and Gamma sector as a **paired renormalized block**, rather than cascade a positive prime network with an independent Gamma inner factor.

This is a concrete architectural constraint.

---

## 10. House slogan

\[
\boxed{
\text{Boundary unitarity is weaker than Weyl positivity.}
}
\]

\[
\boxed{
\text{Gamma's trivial ladder is too dense to be Blaschke.}
}
\]

\[
\boxed{
\text{The trivial zeros cancel precisely the obstruction that prevents Gamma from being a standalone inner channel.}
}
\]

That cancellation must occur before any proof-bearing Herglotz argument.
