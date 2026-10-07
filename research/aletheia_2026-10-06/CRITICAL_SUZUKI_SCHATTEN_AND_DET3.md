# The critical Suzuki seam: bounded compact operator, fractional singularity, and a det_3 continuation candidate

**Date:** 2026-10-06  
**Status:** boundedness/compactness are proved directly. The Schatten-\(p\) classification uses standard fractional-integral singular-value theory. The renormalized determinant ratio is a concrete research candidate, **not yet proved to generate Suzuki's canonical system at \(\omega=\tfrac12\)**. RH remains open.

---

## 1. What actually breaks at \(\omega=1/2\)

Suzuki proves that

\[
h_\omega\in L^1_{\mathrm{loc}}
\qquad(\omega>0)
\]

and

\[
h_\omega\in L^2_{\mathrm{loc}}
\qquad(\omega>1/2).
\]

At an integer seam,

\[
g_\omega(x)
\sim
\frac{(2\pi)^\omega}{\Gamma(\omega)}
(1-x)^{\omega-1}.
\]

Thus at

\[
\omega=\frac12,
\]

\[
\boxed{
g_{1/2}(x)
\sim
\sqrt2\,(1-x)^{-1/2}.
}
\]

The finite Hankel kernel is therefore not square-integrable across the hyperbolas

\[
xy=n.
\]

But this does **not** imply that the finite operator ceases to exist or becomes unbounded.

---

# 2. Direct Schur-test boundedness for every \(\omega>0\)

Fix \(a>0\).

Let

\[
K_{\omega,a}(x,y)=h_\omega(xy),
\qquad
0<x,y<a.
\]

For fixed \(x\),

\[
\int_0^a
|K_{\omega,a}(x,y)|\,dy
=
\frac1x
\int_0^{ax}
|h_\omega(u)|\,du.
\]

If

\[
ax<1,
\]

this is zero because \(h_\omega\) is supported on \([1,\infty)\).

Otherwise

\[
x\ge\frac1a,
\]

hence

\[
\frac1x\le a.
\]

Therefore

\[
\boxed{
\sup_{0<x<a}
\int_0^a
|h_\omega(xy)|\,dy
\le
a
\int_1^{a^2}
|h_\omega(u)|\,du
<\infty.
}
\]

By symmetry, the same bound holds for the column integral.

The Schur test gives

\[
\boxed{
\|H_{\omega,a}\|
\le
a
\int_1^{a^2}
|h_\omega(u)|\,du.
}
\]

Thus:

\[
\boxed{
H_{\omega,a}
\text{ is bounded on }L^2(0,a)
\text{ for every }\omega>0.
}
\]

No RH assumption is used.

---

# 3. Compactness for every finite horizon and every \(\omega>0\)

Because

\[
h_\omega\in L^1([1,a^2]),
\]

choose bounded functions \(h_j\) such that

\[
\|h_j-h_\omega\|_{L^1([1,a^2])}\to0.
\]

Let

\[
K_j(x,y)=h_j(xy).
\]

Since \(h_j\) is bounded and the square \((0,a)^2\) has finite measure,

\[
K_j\in L^2((0,a)^2),
\]

so the corresponding operators \(H_j\) are Hilbert--Schmidt, hence compact.

The same Schur estimate gives

\[
\boxed{
\|H_j-H_{\omega,a}\|
\le
a
\|h_j-h_\omega\|_{L^1([1,a^2])}
\to0.
}
\]

Therefore:

\[
\boxed{
H_{\omega,a}
\text{ is compact for every }\omega>0
\text{ and finite }a.
}
\]

Since the kernel is real and symmetric,

\[
\boxed{
H_{\omega,a}
\text{ is compact self-adjoint}.
}
\]

This remains true at and below the \(L^2\) threshold.

---

# 4. What fails at the critical point is Hilbert--Schmidt regularity

For \(a>1\), the seam \(xy=1\) lies inside the square.

At \(\omega=1/2\),

\[
h_{1/2}(u)
\sim
\sqrt2\,(u-1)^{-1/2}
\qquad
(u\to1^+)
\]

up to the smooth Jacobian normalization.

Hence

\[
|h_{1/2}(xy)|^2
\asymp
|xy-1|^{-1}
\]

near the seam.

The two-dimensional integral of this quantity diverges logarithmically.

Therefore

\[
\boxed{
H_{1/2,a}\notin S_2
\qquad(a>1).
}
\]

So the critical obstruction is specific:

\[
\boxed{
\text{bounded compact}
\quad\text{but not Hilbert--Schmidt}.
}
\]

---

# 5. Log coordinates isolate a universal fractional-integral singularity

Use the unitary logarithmic map

\[
(Uf)(u)=e^{u/2}f(e^u).
\]

At finite horizon \(a=e^A\), the effective support of the transformed operator lies in

\[
-A\le u,v\le A.
\]

Its kernel is

\[
\mathfrak h_\omega(u+v).
\]

The \(n\)-th seam is

\[
u+v=\log n.
\]

At \(\omega=1/2\),

\[
\boxed{
\mathfrak h_{1/2}(t)
=
\sqrt2
\sum_{\log n\le t}
\frac{\varphi(n)}n
(t-\log n)^{-1/2}
+
R_A(t)
}
\]

on every fixed finite interval, where the remainder \(R_A\) is locally \(L^2\).

More precisely, the equality here means decomposition into the displayed principal singular parts plus an \(L^2\) remainder; only finitely many \(n\) occur on a finite interval.

---

## 6. Reflection converts each seam into a Riemann--Liouville half-integral

Fix

\[
\tau=\log n.
\]

The model seam operator has kernel

\[
(u+v-\tau)_+^{-1/2}.
\]

Reflect the second coordinate:

\[
r=\tau-v.
\]

Then

\[
u+v-\tau=u-r.
\]

So, up to restrictions to finite intervals and unitary reflection, the seam operator is the Riemann--Liouville fractional integral

\[
\boxed{
(I^{1/2}f)(u)
=
\frac1{\sqrt\pi}
\int^u
(u-r)^{-1/2}
f(r)\,dr.
}
\]

Thus the critical Suzuki singularity is a finite sum of translated/reflected order-\(1/2\) fractional integrals plus a Hilbert--Schmidt remainder.

---

# 7. Schatten class expected/obtained from standard fractional-integral theory

Classical singular-value results for the Riemann--Liouville fractional integral of order \(\alpha\) give

\[
s_j(I^\alpha)
\asymp
j^{-\alpha}.
\]

At

\[
\alpha=\frac12,
\]

\[
s_j
\asymp
j^{-1/2}.
\]

Hence the model seam belongs to

\[
S_p
\quad\Longleftrightarrow\quad
p>2,
\]

and not to \(S_2\).

Since a finite Suzuki horizon contains only finitely many seams and the remainder is Hilbert--Schmidt,

\[
\boxed{
H_{1/2,a}\in S_p
\qquad
\text{for every }p>2.
}
\]

In particular,

\[
\boxed{
H_{1/2,a}\in S_3.
}
\]

This conclusion uses standard fractional-integral singular-value theory (Dostanić; Vũ--Gorenflo; later sharp estimates).

A fully self-contained verification of all localization hypotheses for the exact Suzuki remainder should be included before promoting this to a publication-grade theorem.

---

# 8. The diagonal integral remains finite

Although \(H_{1/2,a}\) is not trace class merely from the above information, the kernel diagonal has only integrable square-root singularities.

Define

\[
\boxed{
\tau_1(a)
=
\int_0^a
h_{1/2}(x^2)\,dx.
}
\]

Near

\[
x=\sqrt n,
\]

\[
h_{1/2}(x^2)
=
O(|x-\sqrt n|^{-1/2}),
\]

which is integrable.

Therefore

\[
\boxed{
\tau_1(a)
\text{ is finite for every finite }a.
}
\]

This is the natural first-order kernel trace counterterm.

---

# 9. A canonical det_3 continuation candidate

Since

\[
H_{1/2,a}\in S_3,
\]

the third regularized Fredholm determinant

\[
\det_3(I\pm H_{1/2,a})
\]

is defined.

Define, whenever \(I\pm H_{1/2,a}\) are invertible,

\[
\boxed{
m^{[3]}_{1/2}(a)
=
\exp(2\tau_1(a))
\frac{
\det_3(I+H_{1/2,a})
}{
\det_3(I-H_{1/2,a})
}.
}
\]

This is a concrete candidate for the critical continuation of Suzuki's determinant ratio.

---

## 10. Why this normalization is not arbitrary

For an operator \(T\) in a region where both the classical kernel Fredholm determinant and the Hilbert--Schmidt regularization are valid,

\[
D(I+T)
=
e^{\tau_1(T)}
\det_2(I+T),
\]

with the diagonal kernel integral as first counterterm.

Moreover, for \(T\in S_2\),

\[
\det_3(I+T)
=
\det_2(I+T)
\exp\!\left(\frac12\operatorname{Tr}T^2\right),
\]

and

\[
\det_3(I-T)
=
\det_2(I-T)
\exp\!\left(\frac12\operatorname{Tr}T^2\right).
\]

The quadratic counterterm cancels in the ratio.

Hence

\[
\boxed{
\frac{
D(I+T)
}{
D(I-T)
}
=
e^{2\tau_1(T)}
\frac{
\det_3(I+T)
}{
\det_3(I-T)
}
}
\]

whenever the classical quantities are simultaneously available.

So the proposed \(m^{[3]}_{1/2}\) is the unique obvious \(S_3\)-regularized expression that agrees with Suzuki's old ratio in the overlap region.

---

# 11. What this would buy us if it works

Suzuki's Hamiltonian in the regular regime has the form

\[
\operatorname{diag}
\left(
m(a)^{-2},
m(a)^2
\right).
\]

If one can prove that

\[
m^{[3]}_{1/2}(a)
\]

satisfies the same integral/differential identities as the original determinant ratio, then one gets a canonical candidate

\[
\boxed{
H_{1/2}^{\rm can}(a)
=
\begin{pmatrix}
(m^{[3]}_{1/2}(a))^{-2}&0\\
0&(m^{[3]}_{1/2}(a))^2
\end{pmatrix}.
}
\]

This would carry the explicit canonical-system construction through the precise place where Hilbert--Schmidt theory fails.

That would be serious progress.

---

# 12. The remaining hard conditions

The formula above is **not yet a proof-bearing extension**.

We still need:

### A. Exact Schatten proof

Verify rigorously that the exact finite Suzuki operator belongs to \(S_3\) at \(\omega=1/2\), including all seam localizations.

### B. Invertibility

Prove

\[
\boxed{
\pm1\notin\operatorname{Spec}(H_{1/2,a})
}
\]

for all finite \(a\).

This is already close to the innerness/passivity wall and may contain RH-level difficulty.

### C. Variation formula

Prove the \(a\)-derivative of

\[
\log m^{[3]}_{1/2}(a)
\]

matches the boundary solution coefficient required by the canonical system.

### D. Terminal function

Prove that the resulting canonical solution has the required \(\xi\)-scattering terminal data.

Until these are established, \(m^{[3]}\) is a research candidate, not a solution.

---

# 13. A better description of the wall

The \(\omega=1/2\) problem is not:

\[
\text{"the operator blows up."}
\]

It is:

\[
\boxed{
\text{the operator drops from }S_2
\text{ into the fractional class }S_{2+},
}
\]

while remaining bounded, compact, and self-adjoint.

So the natural move is not to discard the operator.

It is to change determinant/realization technology.

---

# 14. Research direction below \(1/2\)

For general

\[
0<\omega<1,
\]

the seam is of fractional order \(\omega\), with expected

\[
s_j\asymp j^{-\omega}.
\]

Thus one expects finite truncations to lie in

\[
\boxed{
S_p
\quad\text{for }p>1/\omega.
}
\]

As \(\omega\downarrow0\), increasingly high regularized determinants are needed.

This suggests a hierarchy:

\[
\boxed{
\omega
\longleftrightarrow
\text{minimal determinant renormalization order}.
}
\]

The critical RH point \(\omega=1/2\) is the first non-Hilbert--Schmidt case and naturally asks for order \(3\) regularization.

---

# 15. House summary

\[
\boxed{
\text{Critical Suzuki is still a compact self-adjoint system.}
}
\]

\[
\boxed{
\text{Its seam is a half-integral, not a pathology.}
}
\]

\[
\boxed{
H_{1/2,a}\in S_{2+}\text{ rather than }S_2.
}
\]

\[
\boxed{
\det_3+\text{the finite diagonal counterterm is the natural next determinant technology.}
}
\]

The highest-value immediate question is whether this renormalized determinant ratio obeys Suzuki's canonical-system variation law.
