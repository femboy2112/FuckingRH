# The rightmost zeta zero as a Weyl passivity abscissa

**Date:** 2026-10-06  
**Status:** exact spectral reformulation. **RH remains open.**

The vertical position of the Weyl evaluation line can be treated as a continuous parameter.

This turns the rightmost zero real part into a critical passivity threshold.

---

## 1. Define the shifted completed response

For real \(\sigma\), define

\[
\boxed{
F_\sigma(z)
=
\xi(\sigma-iz)
}
\]

and

\[
\boxed{
m_\sigma(z)
=
-\frac{F_\sigma'(z)}{F_\sigma(z)}
=
i\frac{\xi'}{\xi}(\sigma-iz).
}
\]

Let

\[
\boxed{
\beta_*
=
\sup_{\rho}
\Re\rho
}
\]

over nontrivial zeros.

Classically,

\[
\frac12\le\beta_*\le1.
\]

RH is equivalent to

\[
\beta_*=\frac12.
\]

---

## 2. Where the zeros move in Weyl coordinates

Let

\[
\rho=\beta+i\gamma.
\]

The corresponding zero of \(F_\sigma\) satisfies

\[
\sigma-iz=\rho.
\]

Hence

\[
\boxed{
\lambda_{\rho,\sigma}
=
-\gamma+i(\beta-\sigma).
}
\]

Therefore:

- if \(\beta<\sigma\), the pole lies in the lower half-plane;
- if \(\beta=\sigma\), it lies on the real axis;
- if \(\beta>\sigma\), it lies in the upper half-plane.

---

## 3. Paired Hadamard logarithmic derivative

Using the standard symmetrically paired Hadamard product for \(\xi\), the logarithmic derivative can be written as the symmetrically convergent sum over zeros.

In \(z\)-coordinates this gives

\[
\boxed{
m_\sigma(z)
=
\sum_{\rho}^{*}
\frac1{
\lambda_{\rho,\sigma}-z
}.
}
\]

The star indicates the standard symmetric pairing/regularization.

If

\[
\sigma\ge\beta_*,
\]

all \(\lambda_{\rho,\sigma}\) lie in the closed lower half-plane.

For \(z\in\mathbb C_+\),

\[
\Im
\frac1{\lambda-z}
>0
\]

when \(\Im\lambda\le0\), with the real-pole case understood as the usual Herglotz boundary spectrum.

Therefore

\[
\boxed{
\Im m_\sigma(z)>0
\qquad(z\in\mathbb C_+)
}
\]

and \(m_\sigma\) is a meromorphic Herglotz/Nevanlinna function.

---

## 4. Converse

If

\[
\sigma<\beta_*,
\]

some zero has

\[
\beta>\sigma.
\]

Then

\[
\lambda_{\rho,\sigma}\in\mathbb C_+.
\]

Hence \(m_\sigma\) has a pole inside the upper half-plane.

A Herglotz function is analytic there.

Therefore \(m_\sigma\) cannot be Herglotz.

---

## 5. Exact threshold theorem

Combining the two directions:

\[
\boxed{
m_\sigma\text{ is Herglotz}
\iff
\sigma\ge\beta_*.
}
\]

Equivalently,

\[
\boxed{
\beta_*
=
\inf
\{
\sigma:
m_\sigma
\text{ is Weyl/Herglotz}
\}.
}
\]

So the rightmost zeta-zero real part is exactly the **passivity abscissa** of the completed logarithmic-derivative system.

---

## 6. RH as critical passivity threshold

Functional symmetry forces

\[
\beta_*\ge\frac12.
\]

Therefore

\[
\boxed{
RH
\iff
\beta_*=\frac12
}
\]

becomes

\[
\boxed{
RH
\iff
m_{1/2}
\text{ is Herglotz}.
}
\]

This recovers the earlier \(m_\Xi\) criterion, now embedded in a continuous one-parameter phase transition.

---

## 7. Local prime channels have threshold \(0\), not \(1/2\)

For each prime define

\[
\boxed{
q_{p,\sigma}(z)
=
p^{-\sigma+iz}.
}
\]

If

\[
\sigma>0
\]

and

\[
\Im z>0,
\]

then

\[
|q_{p,\sigma}(z)|
=
p^{-\sigma-\Im z}
<1.
\]

So every local Euler/prime channel remains Schur for **every positive \(\sigma\)**.

Its local passivity threshold is \(0\).

Yet the completed global system has threshold

\[
\beta_*\ge1/2.
\]

Therefore the nontrivial critical threshold is not local.

It is created by the infinite global assembly/completion.

This is a sharp theorem-level local/global distinction.

---

## 8. Thermodynamic phase-transition language

For large \(\sigma\), all prime channels are strongly contractive and the global Euler description converges comfortably.

As \(\sigma\) decreases, every individual prime remains contractive.

The only possible breakdown is collective.

The critical global value is

\[
\sigma=\beta_*.
\]

Thus:

\[
\boxed{
\text{rightmost zero}
=
\text{collective passivity breakdown threshold}.
}
\]

RH asserts that this threshold is pushed all the way down to the self-dual half-density point.

---

## 9. Why this is useful experimentally

Instead of testing only \(\sigma=1/2\), construct finite causal approximants for a range

\[
1>\sigma>\frac12.
\]

Measure:

- Schur norm;
- Pick-matrix smallest eigenvalue;
- Weyl-disk radius;
- transfer-matrix conditioning;
- Schur-complement innovation.

Then study whether the finite systems exhibit a uniform stability margin as \(\sigma\downarrow1/2\).

A proof would establish uniform passivity at the endpoint.

A numerical failure at some \(\sigma>1/2\) would immediately falsify the proposed finite realization, not RH.

---

## 10. House slogan

\[
\boxed{
\text{Every prime stays passive.}
}
\]

\[
\boxed{
\text{Only the infinite completed network can lose passivity.}
}
\]

\[
\boxed{
\text{The first }\sigma\text{ where global passivity becomes possible is the rightmost zero real part.}
}
\]

\[
\boxed{
RH=\text{collective passivity survives exactly to }\sigma=1/2.
}
\]
