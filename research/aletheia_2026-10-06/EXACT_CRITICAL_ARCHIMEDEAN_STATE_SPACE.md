# Exact critical Archimedean state-space: the square-root seam is the inverse-SUCC Gamma ladder

**Date:** 2026-10-06  
**Status:** exact algebraic/state-space decomposition at \(\omega=\tfrac12\). **RH remains open.**

This note replaces the crude statement

> "the critical Suzuki seam behaves like a fractional half-integral"

by an exact realization.

The universal critical Archimedean impulse response is a countable sum of stable exponential modes with decay rates

\[
2,4,6,\ldots,
\]

i.e. the same even inverse-SUCC ladder that generates the Gamma/trivial-zero sector, plus one distinguished zero-frequency negative boundary mode.

---

## 1. Exact simplification of Suzuki's \(g_\omega\) at \(\omega=1/2\)

Suzuki's profile is

\[
g_\omega(x)
=
\frac{2\pi^\omega}{\Gamma(\omega)}
\left[
x^{2-\omega}(1-x^2)^{\omega-1}
-
\omega x^{\omega-1}
\int_{x^2}^1
t^{1/2-\omega}(1-t)^{\omega-1}\,dt
\right]
\]

for \(0<x<1\).

At

\[
\omega=\frac12,
\]

\[
\frac{2\pi^{1/2}}{\Gamma(1/2)}=2,
\]

and

\[
\int_{x^2}^1
(1-t)^{-1/2}\,dt
=
2\sqrt{1-x^2}.
\]

Therefore

\[
\boxed{
g_{1/2}(x)
=
2
\left[
\frac{x^{3/2}}{\sqrt{1-x^2}}
-
x^{-1/2}\sqrt{1-x^2}
\right].
}
\]

Combining terms,

\[
\boxed{
g_{1/2}(x)
=
2x^{-1/2}
\frac{2x^2-1}{\sqrt{1-x^2}}.
}
\]

This identity is exact.

---

## 2. Exact causal log-time kernel

Recall

\[
K_\omega(r)
=
e^{-r/2}g_\omega(e^{-r})\,1_{r>0}.
\]

At criticality,

\[
\boxed{
K_{1/2}(r)
=
2
\frac{2e^{-2r}-1}
{\sqrt{1-e^{-2r}}}
\,1_{r>0}.
}
\]

Near the birth seam,

\[
1-e^{-2r}\sim2r,
\]

so

\[
\boxed{
K_{1/2}(r)
\sim
\sqrt2\,r^{-1/2}.
}
\]

But the exact formula contains much more structure than this asymptotic.

---

## 3. Binomial expansion

Use

\[
\boxed{
(1-y)^{-1/2}
=
\sum_{m=0}^\infty
C_m y^m,
\qquad
C_m=
\frac{\binom{2m}{m}}{4^m}.
}
\]

Set

\[
y=e^{-2r}.
\]

Then

\[
\frac{2y-1}{\sqrt{1-y}}
=
(2y-1)
\sum_{m\ge0}C_my^m.
\]

The constant coefficient is

\[
-C_0=-1.
\]

For \(m\ge1\), the coefficient of \(y^m\) is

\[
\boxed{
a_m
=
2C_{m-1}-C_m.
}
\]

Since

\[
\frac{C_m}{C_{m-1}}
=
\frac{2m-1}{2m},
\]

\[
\boxed{
a_m
=
\frac{2m+1}{2m}C_{m-1}
=
\frac{2m+1}{2m-1}C_m
>0.
}
\]

Therefore

\[
\boxed{
K_{1/2}(r)
=
-2
+
2\sum_{m=1}^\infty
a_m e^{-2mr},
\qquad
r>0.
}
\]

The series converges absolutely for every \(r>0\).

---

# 4. The decay rates are exactly the inverse-SUCC Gamma ladder

The modal exponents are

\[
\boxed{
2m,
\qquad
m=1,2,3,\ldots
}
\]

which are precisely the eigenvalues of the even SUCC operator

\[
H_\infty|m\rangle=2m|m\rangle.
\]

Earlier work derived the Gamma factor as the zeta-regularized determinant of this same ladder and the trivial zeros as its reflected pole/zero locations.

Now the **critical Suzuki boundary response itself** decomposes into the semigroup modes

\[
e^{-rH_\infty}.
\]

This is a second, independent appearance of the same operator.

---

## 5. Exact state-space realization

For each \(m\ge1\), define a scalar state

\[
x_m(r)
\]

obeying

\[
\boxed{
\dot x_m(r)
=
-2m\,x_m(r)+u(r).
}
\]

Its impulse response is

\[
e^{-2mr}.
\]

Define the zero-frequency state

\[
x_0'(r)=u(r),
\]

whose impulse response is the constant function \(1\).

Then the output

\[
\boxed{
y(r)
=
-2x_0(r)
+
2\sum_{m\ge1}a_mx_m(r)
}
\]

has impulse response exactly

\[
\boxed{
K_{1/2}(r).
}
\]

Thus the critical Archimedean seam has a countable first-order realization with diagonal generator

\[
\boxed{
A_\infty
=
\operatorname{diag}
(0,-2,-4,-6,\ldots).
}
\]

The state generator is nothing but zero plus the negative even inverse-SUCC ladder.

---

## 6. Transfer function

For \(\Re s>0\),

\[
\boxed{
\widehat K_{1/2}(s)
=
-\frac2s
+
2\sum_{m=1}^\infty
\frac{a_m}{s+2m}.
}
\]

The series converges after the same cancellation encoded by the exact closed form.

This is a regularized resolvent expansion over the inverse-SUCC ladder.

Compare with the earlier digamma/Gamma resolvent structure:

\[
\frac12\psi(s/2)
\sim
-\sum_m\frac1{s+2m}
+\text{counterterm}.
\]

The critical Suzuki kernel therefore packages the same Archimedean spectral ladder with a different positive modal weighting.

---

# 7. Modal weights and the square-root singularity

The central-binomial coefficients satisfy

\[
C_m
\sim
\frac1{\sqrt{\pi m}}.
\]

Hence

\[
\boxed{
a_m
\sim
\frac1{\sqrt{\pi m}}.
}
\]

Therefore the modal weights are not summable:

\[
\sum_ma_m=\infty.
\]

This divergence is exactly what produces the short-time singularity

\[
K_{1/2}(r)\sim\sqrt2\,r^{-1/2}.
\]

So the failure of Hilbert--Schmidt regularity has a concrete state-space cause:

\[
\boxed{
\text{infinitely many stable inverse-SUCC modes have weights }m^{-1/2}.
}
\]

Nothing locally unstable occurs.

The singularity is a collective ultraviolet accumulation of stable modes.

---

## 8. The sign structure is isolated to one mode

All \(m\ge1\) coefficients satisfy

\[
a_m>0.
\]

The only negative coefficient is the distinguished \(m=0\) contribution

\[
\boxed{-2.}
\]

So the critical Archimedean response has the form

\[
\boxed{
\text{negative zero-frequency boundary mode}
+
\text{positive stable inverse-SUCC tower}.
}
\]

This strongly echoes the earlier prime/Gamma decomposition:

- positive local prime/conductor sectors;
- one signed Archimedean/boundary direction;
- global completion requiring cancellation rather than a naive positive direct sum.

The indefinite signature is now explicit in the critical state-space realization.

---

# 9. Exact finite-modal approximants

Define

\[
\boxed{
K^{(M)}_{1/2}(r)
=
-2
+
2\sum_{m=1}^M
a_me^{-2mr}.
}
\]

Every \(M\) gives a finite-dimensional state-space realization of dimension

\[
M+1.
\]

For every fixed

\[
r_0>0,
\]

\[
K^{(M)}_{1/2}\to K_{1/2}
\]

uniformly on

\[
[r_0,\infty).
\]

Thus the critical Archimedean channel admits causal finite matrix approximants.

The singular boundary is recovered only as

\[
M\to\infty.
\]

This is exactly the kind of finite-to-infinite architecture sought in the SUCC/FUCC program.

---

# 10. Combine with the finite conductor channels

The critical arithmetic event train is

\[
\boxed{
d\nu_{1/2}
=
\sum_n
\frac{\varphi(n)}n
\delta_{\log n}.
}
\]

Equivalently, each primitive conductor mode at \(n\) has coupling amplitude

\[
n^{-1/2}.
\]

The global critical Suzuki causal kernel is

\[
\mathfrak h_{1/2}
=
K_{1/2}*d\nu_{1/2}.
\]

Substituting the modal expansion,

\[
\boxed{
\mathfrak h_{1/2}(t)
=
-2
\sum_{\log n\le t}
\frac{\varphi(n)}n
+
2
\sum_{m\ge1}a_m
\sum_{\log n\le t}
\frac{\varphi(n)}n
e^{-2m(t-\log n)}.
}
\]

Therefore the full critical kernel is generated by the interaction of:

1. discrete conductor events \(n\);
2. the even inverse-SUCC modes \(2m\);
3. one zero-frequency signed boundary channel.

This is an explicit two-index arithmetic/Archimedean network.

---

## 11. Double-sum arithmetic form

Since

\[
e^{-2m(t-\log n)}
=
e^{-2mt}n^{2m},
\]

for fixed finite \(t\) only \(n\le e^t\) occurs, so

\[
\boxed{
\mathfrak h_{1/2}(t)
=
-2A_0(e^t)
+
2\sum_{m\ge1}
a_me^{-2mt}
A_{2m}(e^t),
}
\]

where

\[
\boxed{
A_j(X)
=
\sum_{n\le X}
\varphi(n)n^{j-1}.
}
\]

This expresses the critical global boundary history as a tower of finite weighted conductor moments.

It may be useful for exact finite computations and asymptotics.

---

# 12. Why this is better than the fractional-integral approximation

The local singular model

\[
r^{-1/2}
\]

was useful for Schatten-class intuition.

But the exact exponential expansion reveals:

- the actual state variables;
- the exact generator spectrum;
- positivity of every nonzero mode weight;
- the distinguished negative boundary mode;
- finite modal approximants;
- direct compatibility with the earlier Gamma inverse-SUCC operator.

So the preferred critical realization should use this exact ladder, not a generic fractional continuum.

---

# 13. New proof-bearing question

Can the combined conductor/Gamma state-space be organized as a finite-signature passive or \(J\)-passive colligation such that:

1. the negative \(m=0\) boundary mode is paired by the finite arithmetic boundary term;
2. every finite \((n,m)\) truncation is \(J\)-contractive;
3. the resulting transfer/Fredholm response agrees with Suzuki's \(H_{1/2,a}\);
4. the \(M\to\infty\) modal limit preserves the critical strict-contraction bound?

If yes, the critical singularity becomes a transparent thermodynamic limit of ordinary finite-dimensional systems.

---

## 14. House result

\[
\boxed{
\text{The critical square-root seam is not an alien singularity.}
}
\]

\[
\boxed{
\text{It is the inverse-SUCC Gamma ladder seen in the time domain.}
}
\]

\[
\boxed{
\text{All nonzero ladder modes are stable and positively weighted.}
}
\]

\[
\boxed{
\text{The only explicit negative direction is the zero-frequency boundary mode.}
}
\]

This is the strongest current state-space description of the critical Archimedean wall.
