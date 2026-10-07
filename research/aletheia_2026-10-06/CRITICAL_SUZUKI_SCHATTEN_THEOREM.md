# Critical Suzuki Schatten theorem: \(H_{1/2,a}\in S_p\) for every \(p>2\), but not \(S_2\)

**Date:** 2026-10-06  
**Status:** theorem reduction to standard Riemann--Liouville singular-value asymptotics. **RH remains open.**

This note upgrades the earlier Schatten claim from a heuristic to a clean reduction to classical fractional-integral theory.

---

## 1. Finite-horizon log-coordinate operator

Fix \(a>1\) and write

\[
A=\log a.
\]

After the unitary logarithmic transform

\[
(Uf)(u)=e^{u/2}f(e^u),
\]

Suzuki's critical truncation is unitarily equivalent to an additive Hankel operator on a finite interval with kernel

\[
\mathfrak h_{1/2}(u+v).
\]

Only integers

\[
n<a^2
\]

occur, hence there are only finitely many seam lines

\[
\boxed{
u+v=\tau_n,
\qquad
\tau_n=\log n.
}
\]

---

## 2. Principal singularity of one seam

The exact critical Archimedean response is

\[
K(r)
=
2\frac{2e^{-2r}-1}{\sqrt{1-e^{-2r}}},
\qquad r>0.
\]

As

\[
r\downarrow0,
\]

Taylor expansion gives

\[
\boxed{
K(r)
=
\sqrt2\,r^{-1/2}
+
O(r^{1/2})
}
\]

after absorbing the bounded/less singular terms into the remainder.

More generally, the \(n\)-th causal seam contributes

\[
\boxed{
\frac{\varphi(n)}n
K(u+v-\tau_n)
1_{u+v>\tau_n}.
}
\]

Therefore its principal singular kernel is

\[
\boxed{
\sqrt2\,
\frac{\varphi(n)}n
(u+v-\tau_n)_+^{-1/2}.
}
\]

---

## 3. Reflection gives the Riemann--Liouville half-integral

Fix \(n\) and set

\[
r=\tau_n-v.
\]

Reflection/translation in the second variable is unitary on the appropriate finite interval.

Then

\[
u+v-\tau_n
=
u-r.
\]

Hence the principal seam operator is unitarily equivalent, up to restriction to finite intervals and multiplication by a scalar, to

\[
\boxed{
(I^{1/2}f)(u)
=
\frac1{\sqrt\pi}
\int_{r<u}
(u-r)^{-1/2}f(r)\,dr.
}
\]

This is the classical Riemann--Liouville fractional integral of order

\[
\alpha=\frac12.
\]

---

## 4. Classical singular-value asymptotics

For the Riemann--Liouville fractional integral \(I^\alpha\) on a bounded interval, classical results of Hille/Tamarkin and later sharp results of Dostanić, Vũ--Gorenflo, Faber--Wing, and Burman give

\[
\boxed{
s_j(I^\alpha)
\asymp
j^{-\alpha}.
}
\]

At

\[
\alpha=\frac12,
\]

\[
\boxed{
s_j(I^{1/2})
\asymp
j^{-1/2}.
}
\]

Therefore

\[
\sum_j
s_j(I^{1/2})^p
<\infty
\]

iff

\[
p>2.
\]

So:

\[
\boxed{
I^{1/2}\in S_p
\quad\forall p>2,
}
\]

but

\[
\boxed{
I^{1/2}\notin S_2.
}
\]

---

## 5. The exact seam differs by a Hilbert--Schmidt operator

Define

\[
R(r)
=
K(r)-\sqrt2\,r^{-1/2}
\]

for small positive \(r\), with a smooth cutoff localizing near \(r=0\).

The exact closed formula for \(K\) gives

\[
R(r)=O(1)
\]

(and in fact a stronger half-power expansion) as \(r\downarrow0\).

On a bounded two-dimensional rectangle, a bounded kernel is square-integrable.

Therefore the localized remainder operator belongs to

\[
\boxed{S_2.}
\]

Away from the seam, the kernel is smooth/bounded on the finite rectangle, hence also Hilbert--Schmidt.

Thus each exact seam operator is

\[
\boxed{
\text{scalar}\times I^{1/2}
+
S_2.
}
\]

Because

\[
S_2\subset S_p
\qquad(p>2),
\]

each seam belongs to every \(S_p,\ p>2\).

---

## 6. Finite number of seams

At finite horizon \(a\), only

\[
n<a^2
\]

occur.

Therefore \(H_{1/2,a}\) is a finite sum of seam operators plus a globally Hilbert--Schmidt remainder.

Hence

\[
\boxed{
H_{1/2,a}\in S_p
\qquad
\forall p>2.
}
\]

In particular,

\[
\boxed{
H_{1/2,a}\in S_3.
}
\]

---

## 7. Failure of Hilbert--Schmidt regularity

If \(a>1\), the seam \(n=1\) occurs inside the integration square.

Its principal kernel has squared magnitude

\[
\asymp
(u+v)_+^{-1}.
\]

The local two-dimensional integral diverges logarithmically transverse to the seam.

Equivalently, the principal Riemann--Liouville operator is not in \(S_2\).

The positive coefficient of the \(n=1\) seam is nonzero, so no cancellation removes this local singularity.

Therefore

\[
\boxed{
H_{1/2,a}\notin S_2
\qquad(a>1).
}
\]

---

## 8. Exact endpoint classification

For every finite \(a>1\),

\[
\boxed{
H_{1/2,a}
\in
\bigcap_{p>2}S_p
\setminus
S_2.
}
\]

This is the precise operator-ideal meaning of the critical half-density threshold.

It is not merely "weakly singular."

It sits exactly at the half-integral Schatten boundary.

---

## 9. Consequence for regularized determinants

Since

\[
H_{1/2,a}\in S_3,
\]

the Hilbert-space regularized determinant

\[
\boxed{
\det_3(I\pm H_{1/2,a})
}
\]

is well-defined.

Together with the independent strict-contraction result

\[
\|H_{1/2,a}\|<1,
\]

neither determinant has a zero arising from an eigenvalue \(\mp1\).

This rigorously validates the use of a third-order regularized determinant as a candidate endpoint technology.

It does **not** yet prove that this particular determinant is identical to the p-summing determinant technology suggested by Suzuki/König in the more singular regime.

---

## 10. Broader \(\omega\)-prediction

At a general seam,

\[
K_\omega(r)\sim C_\omega r^{\omega-1}.
\]

After reflection, this is a fractional integral of order

\[
\alpha=\omega.
\]

The same singular-value theory suggests

\[
\boxed{
H_{\omega,a}\in S_p
\quad\text{for }p>1/\omega,
}
\]

modulo the same finite-seam localization argument.

At \(\omega=1/2\), this becomes exactly \(p>2\).

This offers a natural hierarchy of regularized determinant orders as \(\omega\downarrow0\).

---

## 11. House result

\[
\boxed{
\omega=\frac12
\text{ is exactly the transition }
S_2\longrightarrow S_{2+}.
}
\]

\[
\boxed{
\text{The finite critical operator remains compact, strictly contractive, and }S_3.
}
\]

So the endpoint wall is now narrowed to **renormalized determinant/canonical variation**, not existence, compactness, or invertibility.
