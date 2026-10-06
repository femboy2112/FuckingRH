# Prime midpoint pairs as discrete martingale / second-difference probes

**Date:** 2026-10-05  
**Status:** exact algebraic insight / speculative proof probe. RH is not proved here.

## 1. Midpoint algebra

Let \(p\) be prime and suppose there are primes

\[
q=p-a,\qquad r=p+a,
\]

so

\[
q+r=2p.
\]

This is a **non-diagonal** Goldbach representation of \(2p\). Ordinary Goldbach applied to \(2p\) is vacuous for prime \(p\), because \(2p=p+p\) is always the diagonal representation. The useful condition is \(q\ne r\).

Recenter at \(p\). The two displacements are

\[
-a,\quad +a.
\]

Their first moment vanishes:

\[
\frac{-a+a}{2}=0,
\]

while their second moment is positive:

\[
\frac{a^2+a^2}{2}=a^2
=
\left(\frac{r-q}{2}\right)^2.
\]

Thus a symmetric prime pair kills first-order drift while retaining quadratic energy.

## 2. Hilbert midpoint identity

For Hilbert vectors \(x,y\) and midpoint \(m=(x+y)/2\),

\[
\boxed{
\frac{\|x-m\|^2+\|y-m\|^2}{2}
=
\frac14\|x-y\|^2.
}
\]

Therefore a centered two-point split is the elementary atom of "remove the mean, retain variance."

This is exactly the geometry of a two-point martingale split.

More generally, if \(y_-<x<y_+\), choose

\[
\lambda=\frac{y_+-x}{y_+-y_-},
\qquad
1-\lambda=\frac{x-y_-}{y_+-y_-}.
\]

Then

\[
x=\lambda y_-+(1-\lambda)y_+.
\]

The first displacement moment vanishes, while every strictly convex test detects a positive dispersion cost.

## 3. The signed midpoint operator is a discrete Laplacian

Define

\[
\Delta_{p,a}^{(2)}
=
\delta_{p-a}+\delta_{p+a}-2\delta_p.
\]

Then

\[
\int1\,d\Delta_{p,a}^{(2)}=0,
\qquad
\int x\,d\Delta_{p,a}^{(2)}=0.
\]

Thus it annihilates constants and linear functions.

For convex \(F\),

\[
F(p-a)+F(p+a)-2F(p)\ge0.
\]

For concave \(F\), the sign reverses.

This is a genuine positive curvature detector after quotienting affine modes.

## 4. Goldbach symmetry is not symmetry in the RH spectral coordinate

RH prime events live at

\[
\ell_p=\log p,
\]

not at \(p\).

For \(q=p-a,\ r=p+a\),

\[
\frac{\log q+\log r}{2}
=
\frac12\log(p^2-a^2)
=
\log p+\frac12\log\left(1-\frac{a^2}{p^2}\right).
\]

Hence

\[
\boxed{
J_p(a)
:=
\log p-\frac{\log q+\log r}{2}
=
-\frac12\log\left(1-\frac{a^2}{p^2}\right)
>0.
}
\]

The expansion is

\[
J_p(a)
=
\frac{a^2}{2p^2}
+\frac{a^4}{4p^4}
+\frac{a^6}{6p^6}
+\cdots.
\]

Thus additive midpoint symmetry cancels the **first-order** displacement, while the logarithm converts the spread into a positive **second-order Jensen/curvature defect**.

At tower level \(k\),

\[
k\log p-
\frac{k\log q+k\log r}{2}
=
kJ_p(a)>0.
\]

So the two side towers arrive earlier in log-time, by an exactly quantified curvature gap.

## 5. Critical half-density also converts spread into positive curvature

The function

\[
x\mapsto x^{-1/2}
\]

is strictly convex. Therefore

\[
\boxed{
\frac{q^{-1/2}+r^{-1/2}}2
>
p^{-1/2}
}
\]

for a nontrivial symmetric pair.

For small \(a/p\),

\[
\frac{(p-a)^{-1/2}+(p+a)^{-1/2}}2-p^{-1/2}
=
\frac{3a^2}{8p^{5/2}}
+O\left(\frac{a^4}{p^{9/2}}\right).
\]

Again the first-order term cancels and the surviving defect is quadratic.

## 6. Full critical tower weights

At level \(k\), the Suzuki weight as a function of the prime base is

\[
w_k(x)=\log x\,x^{-k/2}.
\]

A direct differentiation gives

\[
\boxed{
w_k''(x)
=
x^{-k/2-2}
\left[
\frac{k(k+2)}4\log x-(k+1)
\right].
}
\]

Hence \(w_k\) is convex once

\[
\log x>
\frac{4(k+1)}{k(k+2)}.
\]

Examples:

- \(k=1\): convex for \(x>e^{8/3}\), hence for primes \(p\ge17\);
- \(k=2\): convex for \(x>e^{3/2}\), hence for primes \(p\ge5\);
- \(k\ge3\): the threshold is already very small.

In those ranges, a symmetric prime split obeys

\[
\frac{w_k(q)+w_k(r)}2\ge w_k(p).
\]

This gives a positive weight-surplus simultaneously with the positive log-time Jensen gap.

## 7. Why this resembles the desired quotient operation

The global RH problem repeatedly asks us to:

1. remove a common/first-order mode;
2. retain second/higher-order dispersion;
3. turn that residual into a positive Gram quantity.

The midpoint operator does exactly this algebraically:

\[
\delta_{p-a}+\delta_{p+a}-2\delta_p.
\]

It annihilates affine modes but detects curvature.

This is the finite-dimensional analogue of:

- quotienting the principal/degree direction;
- martingale centering;
- passing from first jets to second jets;
- replacing drift by variance.

## 8. Why ordinary Goldbach does not solve the problem

There are three independent obstructions.

1. For prime \(p\), the diagonal representation
   \[
   2p=p+p
   \]
   is always available but gives zero dispersion. We need a non-diagonal representation.

2. Additive midpoint symmetry in \(p\) is not midpoint symmetry in the actual spectral coordinates
   \[
   \log p
   \quad\text{or}\quad
   \sigma_p=A'(\log p).
   \]
   The resulting mismatch is precisely the Jensen gap above.

3. Even if suitable pairs exist, their induced weights must reproduce the **exact** Suzuki prime-tower measure. Arbitrary midpoint pairing can change the arithmetic marginal. Round 002 shows that changing the coupling without respecting the exact marginal does not pay the RH reserve.

Therefore midpoint/Goldbach geometry is currently a **probe for a positive second-difference decomposition**, not a proof.

## 9. The theorem-shaped question

Seek a positive decomposition of the exact prime-tower/service measure into centered two-point or finite martingale cells

\[
x=\sum_j\lambda_j y_j,
\qquad
\sum_j\lambda_j=1,
\qquad
\sum_j\lambda_j(y_j-x)=0,
\]

such that:

- the cells use actual prime/prime-power spectral nodes;
- the exact Suzuki masses are preserved globally;
- the first/common mode cancels cellwise;
- the second/higher-order Jensen defects sum to the positive prime-tower Gram blocks \(D_p\), or to a quantity that pays the Brownian debt.

A successful construction would be a discrete "Goldbach Laplacian" realization of the same primitive/quotient mechanism sought adelically.

This is unproved.
