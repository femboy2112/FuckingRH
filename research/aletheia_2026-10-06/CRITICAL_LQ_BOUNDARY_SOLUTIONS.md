# Critical endpoint integral equations in \(L^q\): extending Suzuki's boundary solutions beyond \(L^2\)

**Date:** 2026-10-06  
**Status:** endpoint Banach-space extension based on standard weak-singular/fractional-integral mapping theory plus the critical \(L^2\) strict-contraction theorem. **RH remains open.**

Suzuki's regular \(L^2\) integral equation uses

\[
h_\omega(a\,\cdot)\in L^2(0,a),
\]

which fails at \(\omega=\tfrac12\).

The correct endpoint space is not \(L^2\), but the scale

\[
1<q<2.
\]

On this scale the critical forcing is integrable, the weakly singular operator is compact, and \(\pm1\) remain outside the spectrum.

---

## 1. Critical forcing belongs to every \(L^q,\ q<2\)

Fix \(a>1\).

The function

\[
x\mapsto h_{1/2}(ax)
\]

has finitely many singularities in \((0,a]\), at

\[
\boxed{
x=\frac n a,
\qquad
1\le n\le a^2.
}
\]

Each singularity has local form

\[
\boxed{
C_n|x-n/a|^{-1/2}
+
O(1).
}
\]

Therefore

\[
|h_{1/2}(ax)|^q
\]

is locally integrable iff

\[
q/2<1,
\]

that is,

\[
\boxed{
h_{1/2}(a\,\cdot)\in L^q(0,a)
\qquad
1\le q<2.
}
\]

It is not in \(L^2\) when a seam is present.

---

## 2. Boundedness of \(H_{1/2,a}\) on \(L^q\)

The kernel

\[
K_a(x,y)=h_{1/2}(xy)
\]

has finitely many weak square-root singularities along

\[
xy=n.
\]

Uniform row and column \(L^1\) bounds follow from

\[
h_{1/2}\in L^1_{\mathrm{loc}}.
\]

Thus \(H_{1/2,a}\) is bounded on:

\[
L^1(0,a)
\]

and

\[
L^\infty(0,a).
\]

Interpolation yields

\[
\boxed{
H_{1/2,a}:L^q(0,a)\to L^q(0,a)
\text{ bounded}
}
\]

for every

\[
1\le q\le\infty.
\]

---

## 3. Compactness on \(L^q,\ 1<q<\infty\)

For \(\varepsilon>0\), cut off \(\varepsilon\)-neighborhoods of every seam

\[
xy=n.
\]

The remaining kernel is bounded on the compact square and can be approximated by finite-rank kernels.

The removed singular neighborhoods have row and column \(L^1\) masses of order

\[
O(\sqrt\varepsilon)
\]

because

\[
\int_0^\varepsilon r^{-1/2}\,dr
=
2\sqrt\varepsilon.
\]

Therefore the corresponding error operators tend to zero in both \(L^1\) and \(L^\infty\) operator norms, and hence in every intermediate \(L^q\) norm by interpolation.

Consequently:

\[
\boxed{
H_{1/2,a}
\text{ is compact on }L^q(0,a)
}
\]

for every

\[
1<q<\infty.
\]

---

# 4. Fractional smoothing

Near one seam, logarithmic reflection reduces the principal operator to a Riemann--Liouville half-integral:

\[
(I^{1/2}f)(u)
=
\frac1{\sqrt\pi}
\int_{r<u}
(u-r)^{-1/2}f(r)\,dr.
\]

The one-dimensional Hardy--Littlewood--Sobolev/fractional-integration estimate gives, for

\[
1<q<2,
\]

\[
\boxed{
I^{1/2}:L^q\to L^r,
\qquad
\frac1r
=
\frac1q-\frac12.
}
\]

Equivalently,

\[
\boxed{
r=\frac{2q}{2-q}>2.
}
\]

The smooth parts of the finite kernel map at least as well.

A finite partition of unity over the finitely many seams therefore gives

\[
\boxed{
H_{1/2,a}:L^q(0,a)\to L^r(0,a),
\qquad
r=\frac{2q}{2-q},
}
\]

for every

\[
1<q<2.
\]

---

# 5. No endpoint eigenvalue \(\pm1\) on \(L^q\)

Suppose

\[
f\in L^q(0,a),
\qquad
f\ne0,
\]

satisfies

\[
H_{1/2,a}f
=
\pm f.
\]

The fractional smoothing gives

\[
f
=
\pm H_{1/2,a}f
\in L^r(0,a),
\qquad
r>2.
\]

Since the interval has finite measure,

\[
L^r(0,a)\subset L^2(0,a).
\]

Thus \(f\) would be an \(L^2\) eigenvector of \(H_{1/2,a}\) with eigenvalue \(\pm1\).

But the endpoint strict-contraction theorem gives

\[
\boxed{
\|H_{1/2,a}\|_{L^2\to L^2}<1.
}
\]

Contradiction.

Therefore:

\[
\boxed{
\pm1
\text{ are not eigenvalues of }
H_{1/2,a}:L^q\to L^q.
}
\]

---

## 6. Fredholm invertibility on \(L^q\)

Because \(H_{1/2,a}\) is compact on \(L^q\),

\[
I\pm H_{1/2,a}
\]

are Fredholm operators of index zero.

The previous injectivity result therefore implies surjectivity.

Hence:

\[
\boxed{
I\pm H_{1/2,a}
:
L^q(0,a)\to L^q(0,a)
\text{ are boundedly invertible}
}
\]

for every

\[
\boxed{
1<q<2.
}
\]

---

# 7. Critical Suzuki boundary solutions exist uniquely

Define

\[
h_a(x)=h_{1/2}(ax).
\]

For any fixed

\[
1<q<2,
\]

\[
h_a\in L^q(0,a).
\]

Therefore the equations

\[
\boxed{
\phi_a^+
+
H_{1/2,a}\phi_a^+
=
h_a
}
\]

and

\[
\boxed{
\phi_a^-
-
H_{1/2,a}\phi_a^-
=
h_a
}
\]

have unique solutions

\[
\boxed{
\phi_a^\pm\in L^q(0,a).
}
\]

This extends the static content of Suzuki's Lemma 4.5 to the critical endpoint in the natural Banach scale.

---

## 8. Support property survives

For

\[
0<x<1/a,
\]

and

\[
0<y<a,
\]

we have

\[
xy<1.
\]

Since

\[
h_{1/2}(u)=0
\qquad(0<u<1),
\]

\[
(H_{1/2,a}\phi)(x)=0.
\]

Also

\[
h_{1/2}(ax)=0.
\]

Therefore the integral equation gives

\[
\boxed{
\phi_a^\pm(x)=0
\quad
\text{for a.e. }0<x<1/a.
}
\]

So every endpoint solution has compact support contained in

\[
[1/a,a].
\]

---

## 9. Entire Mellin transforms still exist

Because

\[
\phi_a^\pm\in L^q(0,a),
\qquad
q>1,
\]

and their support lies in the finite annulus

\[
[1/a,a],
\]

they also belong to \(L^1\).

Therefore their logarithmic Fourier/Mellin transforms are entire functions of exponential type.

So the loss of \(L^2\) does **not** destroy the analytic-transform side of Suzuki's construction.

This is important: a substantial portion of the later Paley--Wiener/meromorphic-continuation machinery can potentially be rebuilt at the endpoint.

---

# 10. What is still missing

The endpoint solutions are generally not continuous at the conductor seams.

Suzuki's smooth canonical-system derivation for \(\omega>1\) uses boundary values such as

\[
\phi_a^\pm(a)
\]

and differentiability in \(a\).

These cannot simply be imported into the critical \(L^q\) setting.

The correct next tasks are:

1. define renormalized/non-tangential boundary traces of \(\phi_a^\pm\);
2. prove their piecewise variation between
   \[
   a=\sqrt n;
   \]
3. calculate the jump/singular contribution when a new conductor seam enters;
4. compare the resulting Stieltjes coefficient with the \(\det_3\) variation measure.

So the endpoint boundary solutions now exist; the remaining issue is how to read the canonical coefficient from them.

---

## 11. Why this is a genuine endpoint extension

At \(\omega=1/2\):

- the \(L^2\) forcing fails;
- but the operator remains compact/strictly contractive in \(L^2\);
- fractional smoothing allows \(L^q\) eigenvectors to bootstrap into \(L^2\);
- this excludes the critical Fredholm obstruction on every \(1<q<2\);
- hence the singular integral equations remain solvable.

The obstruction is therefore **not existence of critical boundary solutions**.

It is the extraction of a canonical evolution law from their singular traces.

---

## 12. House result

\[
\boxed{
\text{The half-density endpoint does not destroy Suzuki's boundary states.}
}
\]

\[
\boxed{
\text{It moves them from }L^2\text{ into }L^{2-}.
}
\]

\[
\boxed{
\text{Fractional smoothing then ties their solvability back to the }L^2\text{ strict contraction.}
}
\]

This narrows the endpoint wall further to boundary traces / Stieltjes canonical evolution.
