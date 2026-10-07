# Suzuki kernel as a causal log-time convolution of SUCC conductor events

**Date:** 2026-10-06  
**Status:** exact change-of-variables identity connecting Suzuki's Hankel kernel to the project's causal event-history language. **RH remains open.**

This note turns the arithmetic/Archimedean decomposition of Suzuki's kernel into an exact causal convolution in logarithmic SUCC time.

---

## 1. Start from Suzuki's kernel

For \(x>1\),

\[
h_\omega(x)
=
\frac1x
\sum_{n\le x}
c_\omega(n)
g_\omega(n/x),
\]

with

\[
c_\omega(n)
=
n^\omega
\prod_{p\mid n}
(1-p^{-2\omega}).
\]

Set

\[
x=e^t,
\qquad
\tau_n=\log n.
\]

Use the unitary-log-coordinate normalization natural for \(L^2(dx)\):

\[
\boxed{
\mathfrak h_\omega(t)
=
e^{t/2}
h_\omega(e^t).
}
\]

Then

\[
\mathfrak h_\omega(t)
=
e^{-t/2}
\sum_{\tau_n\le t}
c_\omega(n)
g_\omega(e^{-(t-\tau_n)}).
\]

---

## 2. Exact causal event weights

Define

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

Define the universal Archimedean response

\[
\boxed{
K_\omega(r)
=
e^{-r/2}
g_\omega(e^{-r})
\,1_{r\ge0}.
}
\]

Since

\[
t=\tau_n+r,
\]

\[
e^{-t/2}c_\omega(n)
=
\frac{c_\omega(n)}{\sqrt n}
e^{-r/2}.
\]

Therefore

\[
\boxed{
\mathfrak h_\omega(t)
=
\sum_{\tau_n\le t}
b_\omega(n)
K_\omega(t-\tau_n).
}
\]

This is an exact causal convolution.

---

## 3. Event-measure formulation

Define the discrete arithmetic measure

\[
\boxed{
d\nu_\omega(\tau)
=
\sum_{n\ge1}
b_\omega(n)
\delta_{\log n}(d\tau).
}
\]

Then

\[
\boxed{
\mathfrak h_\omega
=
K_\omega * d\nu_\omega
}
\]

on the additive log-time half-line.

Thus Suzuki's global scattering kernel consists of:

1. arithmetic events at causal times
   \[
   \tau_n=\log n;
   \]

2. event amplitudes
   \[
   b_\omega(n);
   \]

3. one translation-invariant Archimedean impulse response
   \[
   K_\omega.
   \]

This is precisely the event-history architecture sought in the SUCC/FUCC program.

---

## 4. Critical half-density point

At

\[
\omega=\frac12,
\]

\[
c_{1/2}(n)
=
\frac{\varphi(n)}{\sqrt n}.
\]

Therefore

\[
\boxed{
b_{1/2}(n)
=
\frac{\varphi(n)}{n}.
}
\]

For the exact-conductor space

\[
W_n\subset L^2(\mathbb Z/n\mathbb Z),
\]

\[
\dim W_n=\varphi(n),
\qquad
\dim L^2(\mathbb Z/n\mathbb Z)=n.
\]

Hence

\[
\boxed{
b_{1/2}(n)
=
\frac{\dim W_n}
{\dim H_n}.
}
\]

So the critical event amplitude is exactly the **fraction of the finite \(n\)-clock occupied by primitive conductor modes**.

This is a purely finite SUCC interpretation of the arithmetic coefficient.

---

## 5. Critical causal kernel

At \(\omega=1/2\),

\[
\boxed{
\mathfrak h_{1/2}(t)
=
\sum_{\log n\le t}
\frac{\varphi(n)}{n}
K_{1/2}(t-\log n).
}
\]

This is perhaps the cleanest formula currently connecting the finite clock geometry to an established zeta canonical-system kernel.

Every integer contributes when the log-time front reaches \(\log n\).

No future integer contributes.

---

## 6. Boundary singularity = universal event impulse

Suzuki's Archimedean profile satisfies

\[
g_\omega(x)
\sim
\frac{(2\pi)^\omega}{\Gamma(\omega)}
(1-x)^{\omega-1}
\qquad
(x\to1^-).
\]

For

\[
r\to0^+,
\]

\[
1-e^{-r}\sim r.
\]

Therefore

\[
\boxed{
K_\omega(r)
\sim
\frac{(2\pi)^\omega}{\Gamma(\omega)}
r^{\omega-1}.
}
\]

At the half-density point,

\[
\boxed{
K_{1/2}(r)
\sim
C\,r^{-1/2}.
}
\]

Thus each newly activated integer/conductor event produces the same universal square-root boundary singularity, scaled only by

\[
\varphi(n)/n.
\]

---

## 7. The \(L^2\) transition becomes a causal-memory threshold

The impulse tail near its birth time is

\[
r^{\omega-1}.
\]

Its square is locally integrable iff

\[
2\omega-2>-1,
\]

i.e.

\[
\boxed{
\omega>\frac12.
}
\]

So:

- \(\omega>1/2\): every event response has finite local \(L^2\) energy;
- \(\omega=1/2\): universal square-root borderline;
- \(0<\omega<1/2\): each event response is \(L^1\) but not \(L^2\) at birth.

This gives a dynamical interpretation of Suzuki's operator threshold.

---

## 8. Dirichlet/Laplace transform of the event measure

Because

\[
b_\omega(n)
=
c_\omega(n)n^{-1/2},
\]

\[
\int_0^\infty
e^{-s\tau}
d\nu_\omega(\tau)
=
\sum_{n\ge1}
\frac{
c_\omega(n)
}{
n^{s+1/2}
}.
\]

Using Suzuki's Dirichlet identity,

\[
\boxed{
\sum_{n\ge1}
\frac{
c_\omega(n)
}{
n^u
}
=
\frac{
\zeta(u-\omega)
}{
\zeta(u+\omega)
}
}
\]

in the absolute-convergence region.

Hence

\[
\boxed{
\mathcal L\nu_\omega(s)
=
\frac{
\zeta(s+\frac12-\omega)
}{
\zeta(s+\frac12+\omega)
}.
}
\]

So the arithmetic event measure itself has the zeta-ratio scattering transform.

The Archimedean response \(K_\omega\) contributes the Gamma ratio.

Their product is exactly the completed scattering function \(\Theta_\omega\).

---

## 9. Log-coordinate form of the Hankel operator

Suzuki's operator is

\[
(H_\omega f)(x)
=
\int_0^\infty
h_\omega(xy)f(y)\,dy.
\]

Apply the unitary logarithmic transform

\[
(Uf)(u)
=
e^{u/2}f(e^u).
\]

Then

\[
\boxed{
(UH_\omega U^{-1}F)(u)
=
\int_{-\infty}^{\infty}
\mathfrak h_\omega(u+v)
F(v)\,dv.
}
\]

Thus it becomes an **additive Hankel operator** whose kernel depends only on the sum \(u+v\).

Substituting the event expansion,

\[
\boxed{
\mathfrak h_\omega(u+v)
=
\sum_n
b_\omega(n)
K_\omega(u+v-\log n)
1_{u+v\ge\log n}.
}
\]

Therefore every conductor \(n\) contributes across the causal boundary line

\[
\boxed{
u+v=\log n.
}
\]

This gives an exact geometric realization of the "boundary interaction history."

---

## 10. Finite horizon activates only finitely many arithmetic systems

Suzuki truncates to

\[
0<x,y<a.
\]

Therefore

\[
xy<a^2.
\]

Since the \(n\)-th arithmetic contribution requires

\[
xy\ge n,
\]

only

\[
\boxed{
n<a^2
}
\]

can contribute to \(H_{\omega,a}\).

Thus at every finite canonical-system horizon \(a\), the arithmetic part consists of only finitely many conductor events.

A new integer block enters exactly when

\[
\boxed{
a=\sqrt n.
}
\]

This is the precise growing-dimension phenomenon sought in the original matrix intuition.

---

## 11. A finite conductor state space at horizon \(a\)

Define

\[
\boxed{
\mathcal K_a
=
\bigoplus_{n\le a^2}W_n.
}
\]

Then

\[
\dim\mathcal K_a
=
\sum_{n\le a^2}\varphi(n).
\]

At \(\omega=1/2\), each block enters with normalized trace weight

\[
\varphi(n)/n.
\]

The continuous Archimedean kernel determines how that block couples to the \(u+v\) boundary after activation.

Thus a natural hybrid realization has:

- a finite arithmetic conductor space \(\mathcal K_a\);
- a continuous boundary coordinate;
- universal Archimedean response \(K_\omega\);
- new blocks activated causally at \(a=\sqrt n\).

---

## 12. The exact remaining problem

The scalar convolution identity is established.

The missing theorem is an **operator factorization** showing that the finite conductor/carry blocks can replace the singular continuum arithmetic kernel in such a way that:

1. the resulting finite-horizon operator has the same boundary/Fredholm response as Suzuki's \(H_{\omega,a}\);
2. its passivity/self-adjoint structure is manifest;
3. it remains well controlled through the non-\(L^2\) regime \(0<\omega\le1/2\).

This is now an explicit engineering/mathematical problem rather than a vague analogy.

---

## 13. House slogan

\[
\boxed{
\text{Integers are event times in log space.}
}
\]

\[
\boxed{
\text{Exact conductor fraction is the critical event amplitude.}
}
\]

\[
\boxed{
\text{Gamma supplies one universal causal impulse response.}
}
\]

\[
\boxed{
\text{Suzuki's Hankel operator is the sum-history of those boundary events.}
}
\]

\[
\boxed{
\text{At finite horizon, only finitely many arithmetic blocks exist.}
}
\]
