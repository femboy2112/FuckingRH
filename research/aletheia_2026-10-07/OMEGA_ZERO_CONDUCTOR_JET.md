# The omega-zero conductor jet: von Mangoldt is the first derivative of exact-conductor multiplicity

**Date:** 2026-10-07  
**Status:** exact arithmetic theorem. No RH assumption.  
**Main result:** the first \(\omega\)-jet of Suzuki's exact-conductor event weights is precisely the half-density von Mangoldt measure. More generally, the jet order at which an integer first appears is its number of distinct prime factors.

This gives a direct arithmetic explanation of why the \(\omega\downarrow0\) tangent of the Suzuki finite-Hankel family is the Weil explicit-formula geometry.

---

# 1. Suzuki conductor weight

The causal/discrete conductor coefficient is

\[
\boxed{
b_\omega(n)
=
\frac{c_\omega(n)}{\sqrt n}
=
n^{\omega-\frac12}
\prod_{p\mid n}
(1-p^{-2\omega}).
}
\]

For

\[
n=1,
\]

\[
b_\omega(1)=1.
\]

For every

\[
n>1,
\]

at least one factor

\[
1-p^{-2\omega}
\]

vanishes at

\[
\omega=0.
\]

Therefore

\[
\boxed{
b_0(n)=0
\qquad(n>1).
}
\]

At the true RH endpoint, the arithmetic event train has collapsed to the unit conductor.

---

# 2. First derivative selects prime powers

For one prime,

\[
1-p^{-2\omega}
=
2\omega\log p
+
O(\omega^2).
\]

Let

\[
\nu(n)
=
\#\{p:p\mid n\}
\]

be the number of distinct prime divisors.

Then

\[
\prod_{p\mid n}
(1-p^{-2\omega})
=
(2\omega)^{\nu(n)}
\prod_{p\mid n}\log p
+
O(\omega^{\nu(n)+1}).
\]

Also

\[
n^\omega
=
1+O(\omega).
\]

Hence

\[
\boxed{
b_\omega(n)
=
\frac{
(2\omega)^{\nu(n)}
}{
\sqrt n
}
\prod_{p\mid n}\log p
+
O(\omega^{\nu(n)+1}).
}
\]

If \(n\) contains at least two distinct primes, the first derivative vanishes.

If

\[
n=p^k,
\]

then

\[
\nu(n)=1
\]

and

\[
\boxed{
b_\omega(p^k)
=
\frac{
2\omega\log p
}{
\sqrt{p^k}
}
+
O(\omega^2).
}
\]

Since

\[
\Lambda(p^k)=\log p,
\]

we obtain the exact first-jet identity

\[
\boxed{
b_0'(n)
=
\frac{
2\Lambda(n)
}{
\sqrt n
}.
}
\]

This holds for every integer \(n\ge1\), taking \(\Lambda(1)=0\).

---

# 3. Higher jets are stratified by prime-support cardinality

The previous expansion gives more.

If

\[
r=\nu(n),
\]

then

\[
\boxed{
b_0^{(j)}(n)=0
\qquad
(0\le j<r),
}
\]

while

\[
\boxed{
b_0^{(r)}(n)
=
r!\,2^r
\frac{
\prod_{p\mid n}\log p
}{
\sqrt n
}.
}
\]

Therefore the Taylor hierarchy is filtered by exact prime-support complexity:

\[
\boxed{
\begin{array}{ccl}
\text{1st jet}
&:&
p^k,\\[2mm]
\text{2nd jet}
&:&
p^kq^\ell,\\[2mm]
\text{3rd jet}
&:&
p^kq^\ell r^m,\\
&\vdots&
\end{array}
}
\]

where the primes displayed in each row are distinct.

The exponents \(k,\ell,m,\ldots\) do not affect the jet order. They live along the already-open prime ray.

The jet order counts how many independent prime rays must be coupled before the conductor state can exist.

This is exactly compatible with the SUCC/FUCC interpretation.

---

# 4. Dirichlet-series triangulation

The same theorem drops out independently from the Euler product.

For the conductor event measure,

\[
A_\omega(s)
=
\sum_{n\ge1}
\frac{
b_\omega(n)
}{
n^s
}.
\]

A local Euler-factor calculation gives

\[
\boxed{
A_\omega(s)
=
\frac{
\zeta(s+\frac12-\omega)
}{
\zeta(s+\frac12+\omega)
}.
}
\]

At

\[
\omega=0,
\]

\[
A_0(s)=1.
\]

Differentiate:

\[
\begin{aligned}
A_0'(s)
&=
-2
\frac{\zeta'}{\zeta}
\left(s+\frac12\right)\\
&=
2\sum_{n\ge1}
\frac{
\Lambda(n)
}{
n^{s+1/2}}
\end{aligned}
\]

in the initial convergence half-plane.

But coefficientwise,

\[
A_0'(s)
=
\sum_{n\ge1}
\frac{
b_0'(n)
}{
n^s}.
\]

Therefore again

\[
\boxed{
b_0'(n)
=
\frac{
2\Lambda(n)
}{
\sqrt n
}.
}
\]

The coefficient derivation and the Euler-product derivation are independent checks of the same identity.

---

# 5. Time-domain event train

The arithmetic event measure is

\[
d\nu_\omega(t)
=
\sum_{n\ge1}
b_\omega(n)
\delta_{\log n}(dt).
\]

At \(\omega=0\),

\[
\boxed{
d\nu_0
=
\delta_0.
}
\]

Its first variation is

\[
\boxed{
\left.
\frac{\partial}{\partial\omega}
d\nu_\omega
\right|_{\omega=0}
=
2
\sum_{n\ge1}
\frac{
\Lambda(n)
}{
\sqrt n
}
\delta_{\log n}.
}
\]

Thus the familiar prime-power event train does not have to be inserted into Suzuki's family.

It is the derivative of the exact-conductor event train at the point where all nontrivial conductor channels have just closed.

---

# 6. Why the sign in Weil's explicit formula is correct

The completed Suzuki transfer near \(\omega=0\) is

\[
B_\omega(s)
=
1
-
2\omega
\frac{\xi'}{\xi}
\left(s+\frac12\right)
+
O(\omega^2).
\]

Write

\[
L(s)
=
\frac{\xi'}{\xi}
\left(s+\frac12\right).
\]

The zeta part is

\[
\frac{\zeta'}{\zeta}
\left(s+\frac12\right)
=
-
\sum_n
\frac{\Lambda(n)}{n^{s+1/2}}.
\]

Therefore the causal kernel of \(L\) has prime atoms

\[
\boxed{
-
\frac{\Lambda(n)}{\sqrt n}
\delta_{\log n}.
}
\]

The passivity tangent is the symmetric part

\[
L_T+L_T^*.
\]

It therefore contains the reflected pair

\[
\boxed{
-
\frac{\Lambda(n)}{\sqrt n}
\left[
\delta_{+\log n}
+
\delta_{-\log n}
\right],
}
\]

which is exactly the sign and half-density normalization of the prime contribution in Weil's explicit formula.

So the prime part of the proposed Suzuki--Weil tangent is already proved coefficientwise, without invoking any zero locations.

---

# 7. Archimedean first jet

Write the completed transfer as

\[
B_\omega(s)
=
A_\omega(s)G_\omega(s),
\]

where

\[
A_\omega(s)
=
\frac{
\zeta(s+\frac12-\omega)
}{
\zeta(s+\frac12+\omega)
}.
\]

The Archimedean factor is

\[
G_\omega(s)
=
\pi^\omega
\frac{
(s+\frac12-\omega)(s-\frac12-\omega)
}{
(s+\frac12+\omega)(s-\frac12+\omega)
}
\frac{
\Gamma((s+\frac12-\omega)/2)
}{
\Gamma((s+\frac12+\omega)/2)
}.
\]

At

\[
\omega=0,
\]

\[
G_0(s)=1.
\]

Its logarithmic derivative is

\[
\boxed{
\left.
\partial_\omega\log G_\omega(s)
\right|_{\omega=0}
=
\log\pi
-
\frac{2}{s+\frac12}
-
\frac{2}{s-\frac12}
-
\psi\!\left(
\frac{s+\frac12}{2}
\right).
}
\]

This is exactly

\[
\boxed{
-2
\frac{d}{ds}
\log
\left[
\frac12
(s+\tfrac12)(s-\tfrac12)
\pi^{-(s+1/2)/2}
\Gamma((s+1/2)/2)
\right].
}
\]

So the first Suzuki jet separates exactly into:

\[
\boxed{
\text{von Mangoldt prime-power distribution}
+
\text{Archimedean Gamma/polynomial distribution}.
}
\]

Their sum is

\[
\boxed{
-2
\frac{\xi'}{\xi}
\left(s+\frac12\right).
}
\]

That is precisely the logarithmic-derivative object whose symmetric distribution is the Weil kernel.

---

# 8. Structural interpretation

At \(\omega=0\), all conductor channels other than \(n=1\) are closed.

Increasing \(\omega\) opens them in layers.

A prime-power conductor requires one independent prime ray, so it opens linearly.

A conductor supported on two primes requires two independent prime rays, so it opens quadratically.

In general:

\[
\boxed{
\text{prime-support cardinality}
=
\text{order of first appearance in the Suzuki deformation}.
}
\]

This supplies a precise mathematical version of the project's old intuition that prime rays are the elementary channels and mixed conductors are higher-order interactions.

---

# 9. Consequence for the fixed RH program

The nonlinear finite-Hankel passivity family contains an intrinsic perturbative filtration:

\[
\boxed{
\begin{array}{rcl}
O(\omega)
&=&
\text{Weil / von Mangoldt layer},\\
O(\omega^2)
&=&
\text{two-prime conductor interactions},\\
O(\omega^3)
&=&
\text{three-prime conductor interactions},\\
&\vdots&
\end{array}
}
\]

Therefore the localized Weil quadratic form is not an external criterion pasted onto the Suzuki machinery.

It is the **first arithmetic jet of that machinery**.

This makes the next proof task sharper:

\[
\boxed{
\text{derive positivity of the first jet from the exact-conductor geometry,}
}
\]

while retaining the higher jets as nonlinear consistency constraints and possible square-completion resources.

If a proof exists in this architecture, the higher conductor layers may explain why the prime-power first jet must organize positively rather than serving as independent new goalposts.
