# Cubical Hodge index: the product formula puts arithmetic log-vectors in the primitive hyperplane

**Date:** 2026-10-07  
**Status:** exact finite algebraic/Hodge theorem for the toric cube \((\mathbf P^1)^m\). This produces a canonical positive primitive metric, but it is not yet identified with the Weil form.  
**RH remains open.**

The support cube has a standard compact toric realization:

\[
I^m
\longleftrightarrow
(\mathbf P^1)^m.
\]

The corresponding cohomology/Chow ring has an elementary Hodge--Riemann relation.

When the Archimedean place is added, the rational product formula puts every arithmetic local-log vector exactly into the primitive Hodge hyperplane.

This gives a rigorous finite version of:

> the infinity direction completes/rotates the prime vector into the orthogonal physical subspace.

---

# 1. Cohomology ring of the cubical compactification

Let

\[
X_m=(\mathbf P^1)^m.
\]

Write

\[
x_i
\]

for the pullback of the hyperplane class from the \(i\)-th factor.

Then

\[
\boxed{
A^\bullet(X_m)
=
\mathbb R[x_1,\ldots,x_m]/(x_1^2,\ldots,x_m^2).
}
\]

Normalize the degree map by

\[
\boxed{
\deg(x_1\cdots x_m)=1.
}
\]

Choose positive weights

\[
a_i>0
\]

and define the ample class

\[
\boxed{
L=\sum_{i=1}^m a_ix_i.
}
\]

---

# 2. Degree-one primitive condition

Let

\[
u=\sum_{i=1}^m c_ix_i.
\]

The primitive condition in degree one is

\[
\boxed{
L^{m-1}u=0.
}
\]

Because \(x_i^2=0\),

\[
L^{m-1}
=
(m-1)!
\sum_{i=1}^m
\left(
\prod_{j\ne i}a_j
\right)
\prod_{j\ne i}x_j.
\]

Therefore

\[
\deg(L^{m-1}u)
=
(m-1)!
\left(
\prod_ja_j
\right)
\sum_i\frac{c_i}{a_i}.
\]

Hence:

\[
\boxed{
u\text{ primitive}
\iff
\sum_i\frac{c_i}{a_i}=0.
}
\]

This is exact.

---

# 3. Explicit Hodge--Riemann form

The degree-one Hodge form is

\[
\boxed{
Q_L(u)
=
-\deg(u^2L^{m-2}).
}
\]

Compute

\[
u^2
=
2\sum_{i<j}c_ic_jx_ix_j.
\]

Therefore

\[
\deg(u^2L^{m-2})
=
2(m-2)!
\sum_{i<j}
c_ic_j
\prod_{k\ne i,j}a_k.
\]

Factor out

\[
\prod_ka_k
\]

and put

\[
y_i=\frac{c_i}{a_i}.
\]

Then

\[
\deg(u^2L^{m-2})
=
(m-2)!
\left(
\prod_ka_k
\right)
\left[
\left(\sum_i y_i\right)^2
-
\sum_iy_i^2
\right].
\]

On the primitive hyperplane

\[
\sum_i y_i=0.
\]

Thus

\[
\boxed{
Q_L(u)
=
(m-2)!
\left(
\prod_ka_k
\right)
\sum_i
\left(
\frac{c_i}{a_i}
\right)^2
>0
}
\]

for every nonzero primitive \(u\).

This is the elementary Hodge--Riemann theorem for the cubical toric variety.

---

# 4. Add the Archimedean place

Let \(S\) be any finite set of finite primes containing the support of a rational number

\[
q\in\mathbb Q^\times.
\]

Take one coordinate for each

\[
v\in S\cup\{\infty\}.
\]

The local logarithms are

\[
\lambda_v(q)=\log|q|_v.
\]

For finite \(p\),

\[
\lambda_p(q)
=
-v_p(q)\log p.
\]

At infinity,

\[
\lambda_\infty(q)
=
\log|q|.
\]

The rational product formula is

\[
\boxed{
\lambda_\infty(q)
+
\sum_{p\in S}
\lambda_p(q)
=
0.
}
\]

Now define the degree-one class

\[
\boxed{
u_q
=
\sum_{v}
a_v\lambda_v(q)x_v.
}
\]

Its coefficients are

\[
c_v=a_v\lambda_v(q).
\]

Therefore

\[
\sum_v\frac{c_v}{a_v}
=
\sum_v\lambda_v(q)
=
0.
\]

So:

\[
\boxed{
u_q
\text{ is automatically Hodge primitive.}
}
\]

The infinity coordinate is exactly what closes the finite-prime log vector into the primitive hyperplane.

---

# 5. The primitive norm is a sum over places

Apply the explicit Hodge form:

\[
\boxed{
Q_L(u_q)
=
C_L
\sum_v
\lambda_v(q)^2,
}
\]

where

\[
C_L
=
(m-2)!
\prod_va_v
>0.
\]

Thus:

\[
\boxed{
Q_L(u_q)
=
C_L
\left[
(\log|q|)^2
+
\sum_p
v_p(q)^2(\log p)^2
\right].
}
\]

This is unconditionally positive for \(q\ne1\).

It is a genuine place-globalized Hodge index inequality.

---

# 6. Finite primes alone are not primitive

Delete the infinity coordinate.

For a positive integer

\[
n>1,
\]

the finite-place sum is

\[
\sum_p\log|n|_p
=
-\log n
\ne0.
\]

So the finite-prime vector misses the primitive hyperplane by exactly

\[
\boxed{
\log n.
}
\]

Adding infinity contributes

\[
+\log n
\]

and closes it.

Therefore the Archimedean direction is not optional in the Hodge geometry.

It is the exact normal component required by the product formula.

This is a rigorous form of:

\[
\boxed{
\text{finite prime vector}
+
\text{infinity}
\to
\text{orthogonal/primitive completed vector}.
}
\]

---

# 7. Relation to the arithmetic cube

The finite divisor/support box uses valuation coordinates

\[
(v_p(n)).
\]

The canonical height covector is

\[
(\log p)_p.
\]

The local logarithms are precisely the signed coordinate contributions

\[
-v_p(n)\log p.
\]

So the product formula says that the Archimedean coordinate is the negative total contraction against the prime-log height covector:

\[
\boxed{
\lambda_\infty(n)
=
-\sum_p\lambda_p(n)
=
\sum_pv_p(n)\log p.
}
\]

Thus infinity supplies the normal closure of the arithmetic height direction.

---

# 8. Hilbert-valued extension

The algebraic calculation remains valid if each scalar coefficient is replaced by a vector in a real Hilbert space \(\mathcal H\).

Let

\[
u=\sum_i a_i h_i x_i,
\qquad
h_i\in\mathcal H,
\]

and impose the vector primitive condition

\[
\boxed{
\sum_i h_i=0.
}
\]

Polarizing the previous identity gives

\[
\boxed{
Q_L(u)
=
C_L
\sum_i\|h_i\|_{\mathcal H}^2.
}
\]

So Hodge positivity survives when the place coefficients are continuum test-function responses rather than scalars.

This is the relevant version for an eventual Weil/Suzuki coupling.

---

# 9. What this does not yet prove

The Weil form is not simply

\[
\sum_v\|\lambda_v f\|^2.
\]

Its prime terms involve translations by

\[
\log p^k,
\]

and its Archimedean sector contains the Gamma difference kernel and pole boundary form.

Therefore the product-formula Hodge metric is a **canonical parent geometry**, not yet the desired pushforward.

The missing theorem is to derive the correct place-valued response vectors

\[
h_v(f)
\]

from:

- the prime-support/carry cube;
- the Mellin/Dirac Gamma measure;
- the pole/boundary states;

such that:

\[
\boxed{
\sum_vh_v(f)=0
}
\]

is the completed/product-formula primitive condition and

\[
\boxed{
Q_L(u_f)
=
Q_W(f).
}
\]

If that identity holds on every finite support interval, RH follows immediately from Hodge--Riemann positivity.

---

# 10. Why this is a sharper target than “find a positive metric”

The metric and its signature are no longer arbitrary.

They come from ordinary Hodge theory of the cubical toric compactification.

The ample weights

\[
a_v
\]

remain to be derived from the physical half-density/Gamma normalization, but **for every positive choice** the primitive Hodge form is positive.

So the proof problem is reduced to an exact arithmetic identification:

\[
\boxed{
\text{Weil response}
=
\text{primitive place-response class in the cubical Hodge ring}.
}
\]

This is structurally the same kind of missing bridge that appears in geometric proofs of RH over function fields, now with an explicit finite cube and an exact Archimedean primitive-completion law.
