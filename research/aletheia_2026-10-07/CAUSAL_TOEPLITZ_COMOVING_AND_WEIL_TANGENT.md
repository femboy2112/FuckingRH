# Causal Toeplitz reduction, co-moving subcritical frame, and the Weil tangent

**Date:** 2026-10-07  
**Branch:** \`aletheia/finite-hankel-contraction-frontier-2026-10-07\`  
**Status:** Sections 1--9 are exact algebra/operator reductions from Suzuki's kernel. Section 10 is a theorem target: the first-variation/Weil identification is strongly motivated but **UNVERIFIED** until the distributional form limit and normalization are proved.  
**RH remains open.**

The finite-conductor passivity theorem is now the fixed target:

\[
\|H_{\omega,a}\|_{2\to2}\le1
\qquad(\omega>0,\ a>0).
\]

This note changes the attack without changing the goal. It puts every finite Suzuki Hankel operator into a causal Toeplitz coordinate system, proves the horizon monotonicity that any proof must respect, closes one tempting but globally impossible perturbation strategy, and finds a co-moving frame in which the subcritical arithmetic deformation has a fixed inverse-FUCC/Möbius filter.

---

# 1. Exact logarithmic reduction

Let

\[
A=\log a
\]

and use the unitary logarithmic map

\[
(Uf)(u)=e^{u/2}f(e^u).
\]

Suzuki's finite operator is

\[
(H_{\omega,a}f)(x)
=
\int_0^a h_\omega(xy)f(y)\,dy.
\]

Put

\[
x=e^u,\qquad y=e^v.
\]

Then

\[
e^{u/2}(H_{\omega,a}f)(e^u)
=
\int_{-\infty}^{A}
e^{(u+v)/2}h_\omega(e^{u+v})(Uf)(v)\,dv.
\]

Define the causal log kernel

\[
\boxed{
k_\omega(t)
=
e^{t/2}h_\omega(e^t).
}
\]

Since Suzuki proved

\[
h_\omega(x)=0\qquad(0<x<1),
\]

we have

\[
\boxed{
k_\omega(t)=0\qquad(t<0).
}
\]

Hence

\[
(UH_{\omega,a}U^{-1}F)(u)
=
\int_{-\infty}^{A}k_\omega(u+v)F(v)\,dv.
\]

If \(u<-A\), then \(u+v<0\) for every \(v\le A\), so the output vanishes. Thus the whole nonzero finite operator lives on

\[
[-A,A].
\]

---

# 2. Reflection turns Hankel into causal Toeplitz

Let

\[
(RF)(v)=F(-v).
\]

On \(L^2(-A,A)\), \(R\) is unitary. Set \(G=RF\). Then

\[
(UH_{\omega,a}U^{-1}R^{-1}G)(u)
=
\int_{-A}^{A}k_\omega(u-v)G(v)\,dv.
\]

Because \(k_\omega(t)=0\) for \(t<0\),

\[
\boxed{
(UH_{\omega,a}U^{-1}R^{-1}G)(u)
=
\int_{-A}^{u}k_\omega(u-v)G(v)\,dv.
}
\]

Translate

\[
t=u+A,\qquad s=v+A,
\]

so the interval becomes

\[
[0,T],
\qquad
\boxed{T=2A=2\log a.}
\]

Define

\[
\boxed{
(C_{\omega,T}g)(t)
=
\int_0^t
k_\omega(t-s)g(s)\,ds.
}
\]

All changes of variables are unitary, therefore

\[
\boxed{
\|H_{\omega,a}\|
=
\|C_{\omega,\,2\log a}\|.
}
\]

This is exact.

So the finite-conductor RH problem is equivalently a family of finite-time causal convolution inequalities.

---

# 3. The transfer function is exactly Suzuki's scattering ratio

Suzuki's Mellin identity gives, in its initial convergence half-plane,

\[
\int_0^\infty
h_\omega(x)x^{1/2+iz}\frac{dx}{x}
=
\Theta_\omega(z).
\]

With \(x=e^t\),

\[
\Theta_\omega(z)
=
\int_0^\infty
k_\omega(t)e^{izt}\,dt.
\]

Set

\[
z=is.
\]

Then

\[
\boxed{
\mathcal L k_\omega(s)
=
\Theta_\omega(is).
}
\]

Write

\[
\delta=\frac12-\omega.
\]

Then

\[
\boxed{
B_\delta(s)
:=
\mathcal L k_\omega(s)
=
\frac{\xi(s+\delta)}
     {\xi(s+1-\delta)}.
}
\]

By the functional equation of \(\xi\),

\[
\boxed{
B_\delta(s)B_\delta(-s)=1
}
\]

as a meromorphic identity.

Thus the completed Suzuki transfer is algebraically all-pass. The unknown content is not the boundary modulus; it is whether the causal transfer is stable/Schur in the right half-plane.

---

# 4. Finite contraction criterion in the causal picture

The branch companion note proves

\[
\Theta_\omega\text{ inner}
\iff
\|H_{\omega,a}\|\le1\quad\forall a>0.
\]

The log reduction makes this

\[
\boxed{
B_\delta\text{ is a Schur/all-pass transfer}
\iff
\|C_{\omega,T}\|\le1\quad\forall T>0.
}
\]

This also gives a direct Hardy-space proof.

If every finite \(C_{\omega,T}\) is contractive, then for every compactly supported \(f\in L^2(0,\infty)\),

\[
\|P_TC_\omega f\|_2\le\|f\|_2
\]

for all sufficiently large \(T\). Monotone convergence produces a global causal \(L^2\) contraction.

The Laplace transform maps \(L^2(0,\infty)\) to \(H^2(\Re s>0)\), and causal convolution becomes multiplication by \(B_\delta\). Hence \(B_\delta\in H^\infty\) with norm at most one. Together with the all-pass boundary identity, this is innerness.

This is the same content as Suzuki's Theorem 2.2 viewed through the Hankel-to-Toeplitz conjugacy.

---

# 5. Horizon monotonicity

For

\[
0<T_1<T_2,
\]

the operator \(C_{\omega,T_1}\) is the compression of \(C_{\omega,T_2}\) to \(L^2(0,T_1)\).

Therefore

\[
\boxed{
\|C_{\omega,T_1}\|
\le
\|C_{\omega,T_2}\|.
}
\]

Equivalently,

\[
\boxed{
a\longmapsto \|H_{\omega,a}\|
\text{ is nondecreasing.}
}
\]

This is unconditional.

If \(B_\delta\) is inner, the global causal operator is an isometry. Since finite projections converge strongly to the identity,

\[
P_TC_\omega P_T\to C_\omega
\]

strongly. For any nonzero compactly supported \(f\),

\[
\|C_\omega f\|=\|f\|.
\]

Hence

\[
\liminf_{T\to\infty}\|C_{\omega,T}\|\ge1.
\]

The finite contractions give the opposite inequality, so

\[
\boxed{
\|C_{\omega,T}\|\uparrow1
\qquad(T\to\infty)
}
\]

whenever \(B_\delta\) is inner.

In particular, unconditionally at the critical endpoint,

\[
\boxed{
1-\|H_{1/2,a}\|
\downarrow0
\qquad(a\to\infty).
}
\]

---

# 6. Negative result: the fixed critical-margin perturbation route cannot prove RH

We previously defined

\[
g(a)=1-\|H_{1/2,a}\|>0
\]

and the subcritical tilt cost

\[
L_\delta(a)
=
\|H_{1/2-\delta,a}-H_{1/2,a}\|.
\]

For each fixed finite \(a\),

\[
L_\delta(a)<g(a)
\]

is a valid sufficient condition for subcritical contractivity.

But Section 5 proves

\[
\boxed{
g(a)\to0.
}
\]

Therefore no strategy requiring a positive horizon-uniform lower bound

\[
g(a)\ge g_0>0
\]

can work.

This closes an important false route:

\[
\boxed{
\text{RH cannot come from preserving a fixed critical norm gap as }a\to\infty.
}
\]

The critical endpoint is still the correct local launch surface, but the global proof must use exact completion/cancellation rather than a uniform perturbative buffer.

---

# 7. Finite passivity failure is a genuine phase transition

Fix \(\omega>0\).

Since the finite operators are compact and depend continuously on the finite horizon locally, their extreme eigenvalues vary continuously under horizon variation.

If \(\Theta_\omega\) is not inner, the finite-contraction criterion implies that there exists a finite horizon \(a\) with

\[
\|H_{\omega,a}\|>1.
\]

By horizon monotonicity, once the norm exceeds one it never returns below one.

Therefore there is a first loss-of-passivity horizon

\[
\boxed{
a_*(\omega)
=
\inf\{a:\|H_{\omega,a}\|>1\},
}
\]

with the crossing occurring through

\[
\boxed{
\lambda_{\max}=1
\quad\text{or}\quad
\lambda_{\min}=-1.
}
\]

Thus an off-line zero, if one exists, forces a finite causal/conductor machine through a literal unit-gain spectral transition.

This is a finite observable.

---

# 8. Co-moving subcritical frame

For

\[
0<\omega<\frac12,
\qquad
\delta=\frac12-\omega>0,
\]

the bare Archimedean subsystem has one known unstable mode of rate \(+\delta\).

Remove that deterministic rate from the time coordinate by defining

\[
\boxed{
\widetilde{k}_\delta(t)
=
e^{-\delta t}k_\delta(t).
}
\]

Let

\[
(M_\delta f)(t)=e^{\delta t}f(t).
\]

Then on every finite interval,

\[
\boxed{
\widetilde C_{\delta,T}
=
M_{-\delta}C_{\delta,T}M_\delta.
}
\]

Thus unweighted contractivity of the original operator is equivalent to contractivity of \(\widetilde C_{\delta,T}\) in the weighted Hilbert norm

\[
\boxed{
\|f\|_{\delta,T}^{2}
=
\int_0^T e^{2\delta t}|f(t)|^2\,dt.
}
\]

The transfer function becomes

\[
\boxed{
\widetilde B_\delta(s)
=
B_\delta(s+\delta)
=
\frac{\xi(s+2\delta)}
     {\xi(s+1)}.
}
\]

This is the key simplification:

\[
\boxed{
\text{the denominator is now independent of }\delta.
}
\]

The entire subcritical family is transported onto a common spectral denominator.

---

# 9. Fixed inverse-FUCC filter theorem

Before the Archimedean factor, the original conductor transfer is

\[
A_\delta(s)
=
\frac{\zeta(s+\delta)}
     {\zeta(s+1-\delta)}.
\]

After the same co-moving shift,

\[
\boxed{
\widetilde A_\delta(s)
=
A_\delta(s+\delta)
=
\frac{\zeta(s+2\delta)}
     {\zeta(s+1)}.
}
\]

Its event coefficients are therefore

\[
\boxed{
\widetilde b_\delta(n)
=
b_\delta(n)n^{-\delta}
=
n^{-2\delta}
\prod_{p\mid n}(1-p^{-1+2\delta}).
}
\]

Expand the Euler factor:

\[
\widetilde b_\delta(n)
=
n^{-2\delta}
\sum_{d\mid n}\mu(d)d^{-1+2\delta}.
\]

Write \(n=dm\). Then

\[
\boxed{
\widetilde b_\delta(n)
=
\sum_{dm=n}
\frac{\mu(d)}{d}\,m^{-2\delta}.
}
\]

Equivalently,

\[
\boxed{
\widetilde b_\delta
=
\left(\frac{\mu}{\mathrm{id}}\right)
*
\left(n\mapsto n^{-2\delta}\right).
}
\]

This is an exact structural theorem.

The signed inverse-divisibility filter

\[
\boxed{
d\longmapsto\frac{\mu(d)}d
}
\]

is **independent of \(\delta\)**.

All subcritical deformation sits in the positive monotone carrier

\[
\boxed{
m^{-2\delta}.
}
\]

In transfer language,

\[
\boxed{
\frac1{\zeta(s+1)}
}
\]

is the fixed inverse-FUCC filter, while

\[
\boxed{
\zeta(s+2\delta)
}
\]

is the transported carrier.

This is substantially cleaner than the unshifted formula, where both pieces appeared to deform.

---

## 9.1 Arithmetic event amplitudes decrease below half-density

For \(n>1\),

\[
b_\delta(n)
=
n^{-\delta}
\prod_{p\mid n}(1-p^{-1+2\delta}).
\]

Differentiate:

\[
\boxed{
\frac{\partial}{\partial\delta}\log b_\delta(n)
=
-\log n
-
2\sum_{p\mid n}
\frac{(\log p)p^{-1+2\delta}}
     {1-p^{-1+2\delta}}
<0.
}
\]

Therefore

\[
\boxed{
\delta\mapsto b_\delta(n)
\text{ is strictly decreasing for every }n>1.
}
\]

The same is true for the transported weights \(\widetilde b_\delta(n)\).

So subcritical passivity cannot fail because the individual finite conductor events get larger. They get smaller.

What becomes dangerous is the changed temporal metric / Archimedean organization and the collective resonance structure.

---

# 10. Transported carry formula

Define the transported summatory conductor signal

\[
\boxed{
S_\delta(X)
=
\sum_{n\le X}\widetilde b_\delta(n).
}
\]

Using the fixed-filter convolution,

\[
\boxed{
S_\delta(X)
=
\sum_{d\le X}
\frac{\mu(d)}d
H_{2\delta}(X/d),
}
\]

where

\[
H_{2\delta}(y)
=
\sum_{m\le y}m^{-2\delta}.
\]

For

\[
0\le\delta<\frac12,
\]

define

\[
\mathscr C_{2\delta}(y)
=
H_{2\delta}(y)
-
\frac{y^{1-2\delta}}{1-2\delta}.
\]

The main coefficient is

\[
\boxed{
C_\delta^{\rm mov}
=
\frac1{(1-2\delta)\zeta(2-2\delta)}.
}
\]

Hence the centered transported discrepancy

\[
F_\delta(X)
=
S_\delta(X)
-
C_\delta^{\rm mov}X^{1-2\delta}
\]

satisfies the exact identity

\[
\boxed{
F_\delta(X)
=
\sum_{d\le X}
\frac{\mu(d)}d
\mathscr C_{2\delta}(X/d)
-
\frac{X^{1-2\delta}}{1-2\delta}
\sum_{d>X}\frac{\mu(d)}{d^{2-2\delta}}.
}
\]

At \(\delta=0\),

\[
\mathscr C_0(y)=-\{y\},
\]

so

\[
\boxed{
F_0(X)
=
-\sum_{d\le X}\frac{\mu(d)}d\{X/d\}
-
X\sum_{d>X}\frac{\mu(d)}{d^2}.
}
\]

The important improvement is conceptual:

\[
\boxed{
\text{all }\delta\text{-dependence is in the carry/carrier vector;}
}
\]

\[
\boxed{
\text{the inverse-FUCC Möbius row }\mu(d)/d\text{ is fixed.}
}
\]

This is now the preferred arithmetic coordinate system for the subcritical proof.

---

# 11. The shifted Archimedean channel is critical-shaped for every \(\delta\)

The unshifted Archimedean transfer is

\[
G_\delta(s)
=
\pi^{1/2-\delta}
\frac{(s+\delta)(s+\delta-1)}
     {(s+1-\delta)(s-\delta)}
\frac{\Gamma((s+\delta)/2)}
     {\Gamma((s+1-\delta)/2)}.
\]

Shift \(s\mapsto s+\delta\):

\[
\boxed{
\widetilde G_\delta(s)
=
\pi^{1/2-\delta}
\frac{(s+2\delta)(s+2\delta-1)}
     {(s+1)s}
\frac{\Gamma((s+2\delta)/2)}
     {\Gamma((s+1)/2)}.
}
\]

The formerly unstable pole at \(s=\delta\) has moved to

\[
\boxed{s=0.}
\]

The remaining Archimedean poles lie at

\[
\boxed{
s=-2\delta-2m,\qquad m\ge1,
}
\]

strictly in the stable half-plane.

Meanwhile

\[
\widetilde A_\delta(s)
=
\frac{\zeta(s+2\delta)}{\zeta(s+1)}
\]

has the matching zero at \(s=0\) from \(1/\zeta(1)\).

Therefore every subcritical system, after the co-moving transport, has the same qualitative completion geometry as the critical endpoint:

\[
\boxed{
\text{one marginal Archimedean mode at }0
+
\text{stable tower}
+
\text{arithmetic zero at }0.
}
\]

The completed product is

\[
\boxed{
\widetilde A_\delta(s)\widetilde G_\delta(s)
=
\frac{\xi(s+2\delta)}
     {\xi(s+1)}.
}
\]

Again the denominator is fixed.

---

# 12. Spectral interpretation of the co-moving frame

The poles introduced by the fixed completed denominator are

\[
s=\rho-1
\]

where

\[
\xi(\rho)=0.
\]

Their locations no longer move with \(\delta\).

The deformation parameter instead changes the exponential weight in the Hilbert norm:

\[
e^{2\delta t}.
\]

So the subcritical family may be rephrased as:

> How much exponential weight can the single fixed completed causal system tolerate while remaining contractive?

If a zero has real part \(\beta\), its transported resonance has real part

\[
\boxed{
\beta-1.
}
\]

RH says

\[
\beta=\frac12
\]

for all nontrivial zeros, hence every transported resonance lies on

\[
\boxed{
\Re s=-\frac12.
}
\]

This makes the geometric meaning of the full range

\[
0<\delta<\frac12
\]

transparent: RH asserts that the system has exactly a half-unit exponential stability margin against the co-moving weight.

This is a characterization, not yet a proof.

---

# 13. The real endpoint is \(\omega\downarrow0\), not \(\omega=1/2\)

The critical point \(\omega=1/2\) is the last unconditional inner point and is useful for local construction.

But RH itself is reached by

\[
\omega\downarrow0.
\]

Write directly

\[
\boxed{
B_\omega(s)
=
\frac{\xi(s+\frac12-\omega)}
     {\xi(s+\frac12+\omega)}.
}
\]

For fixed \(s\) away from zeros,

\[
\log B_\omega(s)
=
-2\omega
\frac{\xi'}{\xi}(s+\tfrac12)
+
O(\omega^3).
\]

Hence

\[
\boxed{
B_\omega(s)
=
1
-
2\omega
\frac{\xi'}{\xi}(s+\tfrac12)
+
O(\omega^2).
}
\]

At \(\omega=0\), the transfer is the identity:

\[
B_0(s)=1.
\]

Thus the whole Suzuki inner family is a nonlinear all-pass deformation whose infinitesimal generator is

\[
\boxed{
-\frac{\xi'}{\xi}(s+\tfrac12).
}
\]

Lagarias' positivity theorem identifies the positive-realness of \(\xi'/\xi\) on the shifted right half-plane with RH.

This strongly suggests that the \(\omega\downarrow0\) first variation of finite Hankel passivity is not a new object: it should be the localized Weil positivity form.

---

# 14. Weil tangent theorem target — finite model proved, infinite form limit open

The companion note

\[
\texttt{FINITE\_ZERO\_SUZUKI\_WEIL\_TANGENT.md}
\]

proves the following **exactly** for every finite symmetry-closed zero multiset.

Let \(C_{\omega,\Lambda,T}\) be the rational finite-zero Suzuki convolution and let \(Q_\Lambda\) be the corresponding finite Weil Gram form. Then

\[
\boxed{
\lim_{\omega\to0}
\frac{
\|f\|^2-\|C_{\omega,\Lambda,T}f\|^2
}{
2\omega
}
=
Q_\Lambda(f).
}
\]

Equivalently,

\[
\boxed{
\frac{
I-C_{\omega,\Lambda,T}^{*}C_{\omega,\Lambda,T}
}{
2\omega
}
\longrightarrow
A_{\Lambda,T},
}
\]

where \(A_{\Lambda,T}\) has the finite difference kernel

\[
\sum_{\rho\in\Lambda}
e^{-i\gamma(t-u)},
\qquad
\rho=\frac12+i\gamma.
\]

This fixes the normalization: the denominator is \(2\omega\), not \(4\omega\).

For the genuine xi function, write

\[
C_{\omega,T}
=
I-2\omega\mathcal L_T+o(\omega)
\]

on a smooth form core, where the causal distribution \(\mathcal L_T\) has transfer

\[
\frac{\xi'}{\xi}(s+\tfrac12).
\]

The finite-zero theorem shows that the symmetric part should satisfy

\[
\boxed{
\mathcal L_T+\mathcal L_T^*
=
A_{T/2}
}
\]

after translating \([0,T]\) to \([-T/2,T/2]\), where \(A_{T/2}\) is Suzuki's 2026 localized Weil operator in quadratic-form sense.

Therefore the infinite theorem target is

\[
\boxed{
\frac{
I-C_{\omega,T}^{*}C_{\omega,T}
}{
2\omega
}
\longrightarrow
A_{T/2}
}
\]

on \(C_c^\infty\), followed by form closure.

This is **not yet proved** for the full zero set. The remaining debt is specifically the distributional/form-limit passage:

- \(\xi'/\xi\) has the ultraviolet logarithmic growth that becomes the singular Weil kernel;
- the inverse transform is a distribution, not an \(L^1\) kernel;
- \(C_{\omega,T}\to I\) through a singular approximate identity;
- the correct convergence mode is quadratic-form convergence on a common core.

Suzuki's 2026 construction independently identifies \(A_a\) as the self-adjoint realization of the localized Weil form and describes its formal difference kernel as the zero distribution. This is exactly the object generated by the finite-zero derivative.

If the infinite form-limit theorem closes, it will establish:

\[
\boxed{
\text{localized Weil positivity is the infinitesimal }\omega\downarrow0
\text{ shadow of finite Suzuki passivity.}
}
\]

# 15. What is now fixed, what is open

## Proved / exact in this note

1. Hankel-to-causal-Toeplitz unitary equivalence:
   \[
   \|H_{\omega,a}\|
   =
   \|C_{\omega,2\log a}\|.
   \]

2. Exact causal transfer:
   \[
   \mathcal L k_\omega(s)
   =
   \xi(s+\delta)/\xi(s+1-\delta).
   \]

3. Horizon monotonicity.

4. Under innerness:
   \[
   \|H_{\omega,a}\|\uparrow1.
   \]

5. Hence the critical norm gap tends to zero; a uniform-gap perturbation proof is impossible.

6. Exact co-moving transform:
   \[
   \widetilde B_\delta(s)
   =
   \xi(s+2\delta)/\xi(s+1).
   \]

7. Fixed inverse-FUCC factor:
   \[
   \widetilde b_\delta
   =
   (\mu/\mathrm{id})*(n^{-2\delta}).
   \]

8. Exact transported carry formula.

9. Individual conductor weights decrease as one moves subcritically.

## Corroborated externally

Suzuki 2012:
- Proposition 1.2: zero-free half-plane \(\Leftrightarrow\) innerness of the \(\Theta_\omega\) family.
- Proposition 2.1: Mellin transform of \(h_\omega\).
- Theorem 2.2: \(L^2\) convolution/support characterization of innerness.
- Lemma 4.1: innerness gives the global isometric Hankel operator.

Suzuki 2026:
- localized Weil quadratic forms are represented by self-adjoint operators \(A_a\);
- RH fails iff the lowest finite-interval eigenvalue becomes negative somewhere;
- the lowest eigenvalue is continuous in the interval length.

## UNVERIFIED / next theorem

\[
\boxed{
\text{first variation of finite Suzuki passivity}
=
\text{localized Weil quadratic form}.
}
\]

This is now the highest-value bridge to derive.

---

# 16. Research direction from here

The fixed proof goal remains finite conductor passivity.

The preferred route is no longer “borrow a nonvanishing gap from \(\omega=1/2\).”

Instead:

1. use the co-moving frame so the inverse-FUCC filter is fixed;
2. understand the weighted finite-time contractivity of the common completed system;
3. derive the \(\omega\downarrow0\) quadratic-form tangent exactly;
4. identify that tangent with localized Weil positivity;
5. use the discrete conductor/carry realization to prove that form is nonnegative, rather than taking Weil positivity as an assumption.

The dragon has become more sharply localized:

\[
\boxed{
\text{prove positivity of the fixed Möbius/carry completion under every admissible exponential weight.}
}
\]

Or, infinitesimally at the true RH endpoint,

\[
\boxed{
\text{prove the localized Weil form from the conductor/carry factorization.}
}
\]

No new characterization will replace this target unless one of these steps is decisively refuted.
