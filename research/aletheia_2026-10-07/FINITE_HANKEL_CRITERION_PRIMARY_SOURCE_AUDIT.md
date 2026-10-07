# Primary-source audit of the finite-Hankel contraction criterion

**Date:** 2026-10-07  
**Status:** audit against Masatoshi Suzuki, *A canonical system of differential equations arising from the Riemann zeta-function* (RIMS Kôkyûroku Bessatsu B34, 2012).  
**Verdict:** the criterion is not stated verbatim by Suzuki, but the reverse implication is supported by his Proposition 2.1 and Theorem 2.2 and can also be proved directly through Hardy multipliers after the exact log-Toeplitz conjugacy. No RH assumption enters the bridge itself.

---

## 1. Published inputs

Suzuki defines

\[
\Theta_\omega(z)
=
\frac{\xi(\frac12-\omega-iz)}
     {\xi(\frac12+\omega-iz)}.
\]

His Proposition 1.2 states, for \(\omega_0\ge0\),

\[
\zeta(s)\ne0
\quad
(\Re s>\tfrac12+\omega_0)
\]

if and only if

\[
\Theta_\omega
\]

is meromorphic inner in the upper half-plane for every

\[
\omega>\omega_0.
\]

This is the externally fixed RH criterion used by the present branch.

Suzuki's Proposition 2.1 proves

\[
\boxed{
\int_0^\infty
h_\omega(x)x^{1/2+iz}\frac{dx}{x}
=
\Theta_\omega(z)
}
\]

in the initial absolute-convergence half-plane.

Suzuki also records

\[
h_\omega(x)=0
\qquad(0<x<1)
\]

and

\[
h_\omega\in L^1_{\mathrm{loc}}
\qquad(\omega>0).
\]

His Theorem 2.2 states that \(\Theta_\omega\) is meromorphic inner iff, equivalently, the multiplicative convolution

\[
(h_\omega*g)(x)
=
\int_0^\infty
h_\omega(x/y)g(y)\frac{dy}{y}
\]

belongs to \(L^2(0,\infty)\) for every

\[
g\in L^2(1,\infty).
\]

His Lemma 4.1 gives the forward direction used here: if \(\Theta_\omega\) is inner, the full Hankel operator

\[
(H_\omega f)(x)
=
\int_0^\infty h_\omega(xy)f(y)\,dy
\]

extends to an isometry of \(L^2(0,\infty)\).

---

# 2. Forward implication

If \(\Theta_\omega\) is inner, Suzuki's Lemma 4.1 gives

\[
\|H_\omega f\|_2=\|f\|_2.
\]

Therefore every finite compression

\[
H_{\omega,a}=P_aH_\omega P_a
\]

satisfies

\[
\boxed{
\|H_{\omega,a}\|\le1.
}
\]

No new work is needed.

---

# 3. Reverse implication by exhaustion

Assume

\[
\boxed{
\|H_{\omega,a}\|\le1
\qquad\forall a>0.
}
\]

For compactly supported \(f\in L^2(0,\infty)\), choose \(a\) larger than its support.

The locally defined integral gives

\[
P_aH_\omega f
=
H_{\omega,a}f.
\]

Hence

\[
\|P_aH_\omega f\|_2
\le
\|f\|_2.
\]

As \(a\to\infty\), monotone convergence of the output energy gives

\[
\boxed{
H_\omega f\in L^2(0,\infty),
\qquad
\|H_\omega f\|_2\le\|f\|_2.
}
\]

By density, \(H_\omega\) extends uniquely to a global \(L^2\) contraction.

This already eliminates the principal analytic obstruction that exists when \(\Theta_\omega\) is not known to be inner.

---

# 4. Exact inversion converts Hankel output to Suzuki's convolution

Define the unitary involution

\[
\boxed{
(Jg)(y)=y^{-1}g(1/y).
}
\]

If

\[
g\in L^2(1,\infty),
\]

then

\[
Jg\in L^2(0,1).
\]

A direct change of variables gives

\[
\begin{aligned}
(H_\omega Jg)(x)
&=
\int_0^\infty
h_\omega(xy)y^{-1}g(1/y)\,dy\\
&=
\int_0^\infty
h_\omega(x/t)g(t)\frac{dt}{t}\\
&=
\boxed{
(h_\omega*g)(x).
}
\end{aligned}
\]

Thus the global bounded Hankel extension sends every \(Jg\) into \(L^2\), and therefore Suzuki's Theorem 2.2 condition (3) is satisfied.

Consequently,

\[
\boxed{
\Theta_\omega
\text{ is meromorphic inner.}
}
\]

This supplies a direct published-theorem route for the reverse implication.

For maximal functional-analytic caution, the equality for arbitrary \(g\in L^2(1,\infty)\) may be obtained first on compactly supported \(g\) and then extended by density through the global contraction. The local \(L^1\) nature of \(h_\omega\) provides the finite-interval integral representatives.

---

# 5. Independent Hardy-space proof

The companion causal-Toeplitz note gives an independent route.

Under log coordinates and reflection,

\[
H_{\omega,a}
\]

is unitarily equivalent to finite causal convolution

\[
(C_{\omega,T}f)(t)
=
\int_0^t k_\omega(t-s)f(s)\,ds.
\]

If all finite truncations are contractions, exhaustion gives a bounded causal convolution operator on \(L^2(0,\infty)\).

The Laplace transform identifies \(L^2(0,\infty)\) with \(H^2(\Re s>0)\). Suzuki's Proposition 2.1 identifies its multiplier with

\[
B_\delta(s)
=
\Theta_\omega(is).
\]

Every bounded \(H^2\) multiplier belongs to \(H^\infty\), with equal multiplier and supremum norms. Hence

\[
|B_\delta(s)|\le1
\qquad(\Re s>0).
\]

Suzuki's functional-equation identity gives unimodular boundary values. Therefore \(B_\delta\), equivalently \(\Theta_\omega\), is inner.

The two proofs are logically independent enough to make the bridge well triangulated.

---

# 6. Audited theorem

For every fixed \(\omega>0\),

\[
\boxed{
\Theta_\omega
\text{ is meromorphic inner}
\iff
\|H_{\omega,a}\|\le1
\quad
\forall a>0.
}
\]

Combining with Suzuki Proposition 1.2:

\[
\boxed{
\zeta(s)\ne0
\quad(\Re s>\tfrac12+\omega_0)
}
\]

if and only if

\[
\boxed{
\|H_{\omega,a}\|\le1
\quad
\forall a>0,\ \forall\omega>\omega_0.
}
\]

Taking all \(\omega_0>0\) gives

\[
\boxed{
\mathrm{RH}
\iff
\|H_{\omega,a}\|\le1
\quad
\forall\omega>0,\ \forall a>0.
}
\]

---

# 7. Scope / claim ledger

### Disclosed

The finite-Hankel contraction criterion above, conditional only on standard \(L^2\)/Hardy closure facts and Suzuki's published Proposition 2.1 / Theorem 2.2 / Lemma 4.1.

### Externally corroborated

Suzuki's Proposition 1.2 fixes the zero-free/innerness equivalence.

### Not proved by this criterion

No inequality

\[
\|H_{\omega,a}\|\le1
\]

has yet been proved in the genuinely subcritical range solely from arithmetic. That is the RH-bearing theorem still missing.

The point of this audit is to freeze the bridge so future work does not move the goalpost again.
