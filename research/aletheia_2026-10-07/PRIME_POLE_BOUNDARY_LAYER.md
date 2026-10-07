# Prime–Gamma boundary-layer cancellation: strong convergence, norm obstruction, and the RH rate

**Date:** 2026-10-07  
**Branch:** \`research/rh-log-bathtub-prime-shift-2026-10-07\`  
**Status:** exact unconditional operator-limit theorem, topology no-go, and an RH-equivalent quantitative rate. **RH remains OPEN.**

The right finite/infinite seam is not merely scalar cancellation of \(4\sqrt X\). In the *two opposite boundary strips* of Suzuki's finite Weil operator, the rescaled prime-power translation kernel converges **strongly** to the rank-one Archimedean pole kernel, solely by PNT.

The same convergence **fails in \(L^2\)-operator norm** because every finite atomic prime train exhibits arbitrarily high-frequency simultaneous phase recurrences. On the natural compactly embedded logarithmic Weil-energy domain, however, the convergence becomes uniform.

This isolates both the legitimate topology for first-order cancellation and the sharper RH-bearing quantitative rate.

## 1. Fix the exact source and boundary coordinates

Suzuki's Weil operator has arithmetic kernel

\[
-\sum_{q=p^k}
\frac{\Lambda(q)}{\sqrt q}
\bigl[\delta(x-y-\log q)+\delta(x-y+\log q)\bigr]
\]

and an Archimedean pole contribution

\[
e^{(x-y)/2}+e^{-(x-y)/2}.
\]

These coefficients follow from Suzuki (2026), (2.5) and (2.11), and the decomposition \(r_0(t)=-4(e^{t/2}+e^{-t/2}-2)\).

Fix an independent boundary-strip width \(\ell>0\). Take the full Suzuki interval \((-A,A)\), with \(A>\ell\), and the opposite boundary coordinates

\[
x=A-u,\quad y=-A+v,
\qquad 0\le u,v\le\ell.
\]

Put \(X=e^{2A}\). Then

\[
x-y=2A-u-v.
\]

The relevant rescaled prime source is the finite positive measure

\[
\boxed{
\mu_A
=
e^{-A}
\sum_{\substack{q=p^k\\
Xe^{-2\ell}\le q\le X}}
\frac{\Lambda(q)}{\sqrt q}
\delta_{\,2A-\log q}
}
\]

on \([0,2\ell]\).

Define the prime Hankel boundary operator \(H_A\) on \(L^2(0,\ell)\) by

\[
\boxed{
(H_A f)(u)=
\int_{[0,2\ell]}
f(w-u)\,\mu_A(dw),
}
\]

where \(f\) is zero extended outside \((0,\ell)\). Each \(H_A\) is a finite weighted sum of truncated reflections \(f(u)\mapsto f(w-u)\).

The normalized pole block has kernel

\[
\boxed{
P_A(u,v)
=
e^{-A}\left(e^{A-(u+v)/2}+e^{-A+(u+v)/2}\right)
=
e^{-(u+v)/2}+e^{-2A}e^{(u+v)/2}.
}
\]

Thus the limiting pole operator is rank one:

\[
\boxed{
(Pf)(u)=g(u)\langle g,f\rangle,
\qquad
g(u)=e^{-u/2},
\quad 0<u<\ell.
}
\]

Its operator norm is

\[
\boxed{\|P\|=\|g\|_2^2=1-e^{-\ell}.}
\]

## 2. Exact weighted PNT limit

Let

\[
S(Y)=\sum_{q\le Y}\frac{\Lambda(q)}{\sqrt q}.
\]

Abel summation applied to \(\psi(Y)\sim Y\) gives

\[
\boxed{S(Y)\sim 2\sqrt Y.}
\]

For fixed \(w\in[0,2\ell]\),

\[
\begin{aligned}
\mu_A([0,w])
&=
e^{-A}\sum_{Xe^{-w}\le q\le X}
\frac{\Lambda(q)}{\sqrt q}\\
&\longrightarrow
2(1-e^{-w/2}).
\end{aligned}
\]

Uniformity on the compact \(w\)-range follows directly from \(S(Y)=2\sqrt Y+o(\sqrt Y)\), since every \(Y\) in the range obeys \(Y\ge Xe^{-2\ell}\to\infty\).

Therefore:

### Theorem A: PNT boundary-source convergence

\[
\boxed{
\mu_A \xRightarrow[A\to\infty]{\rm weak}
e^{-w/2}\,dw
\quad\text{on }[0,2\ell].
}
\]

This is **unconditional** and uses no zero locations.

The total rescaled source mass satisfies

\[
\mu_A([0,2\ell])\longrightarrow 2(1-e^{-\ell}).
\]

## 3. Strong operator prime–pole matching

For continuous, compactly supported \(f\) on \((0,\ell)\), the test functions \(w\mapsto f(w-u)\), \(u\in[0,\ell]\), form an equicontinuous compact family. Theorem A gives uniform convergence in \(u\):

\[
\begin{aligned}
(H_A f)(u)
&\longrightarrow
\int_{0}^{2\ell}e^{-w/2}f(w-u)\,dw\\
&=e^{-u/2}\int_0^\ell e^{-v/2}f(v)\,dv\\
&=(Pf)(u).
\end{aligned}
\]

Moreover,

\[
\|H_A\|_{2\to2}
\le\mu_A([0,2\ell])
\]

by Young's inequality for the reflection/convolution formulation, so the operators are uniformly bounded for large \(A\).

Density yields:

### Theorem B: strong but not norm prime–pole cancellation

\[
\boxed{H_A\to P\quad\text{strongly on }L^2(0,\ell).}
\]

The exact rescaled pole block \(P_A\to P\) even in norm. Hence

\[
\boxed{P_A-H_A\to0\quad\text{strongly}.}
\]

This is an operator-level, zero-free realization of the unconditional leading PNT cancellation.

## 4. The norm-convergence obstruction

The convergence above is **not** convergence in the \(L^2\) operator norm.

Fix \(A\). The measure \(\mu_A\) has finite atomic support \(\{w_1,\ldots,w_M\}\).

For every \(\varepsilon>0\) and every \(T>0\), simultaneous Diophantine approximation provides \(t>T\) such that

\[
|e^{-itw_j}-1|<\varepsilon
\quad\text{for every }j.
\]

Let \(g(u)=e^{-u/2}\), let \(\phi=g/\|g\|_2\), and consider the unit vectors

\[
f_t(u)=e^{itu}\phi(u),
\qquad
h_t(v)=e^{-itv}\phi(v).
\]

The finite atomic Hankel bilinear form obeys

\[
\begin{aligned}
\langle f_t,H_Ah_t\rangle
&=
\sum_j\mu_A(\{w_j\})e^{-itw_j}
\int_0^\ell\phi(u)\phi(w_j-u)\,du\\
&\xrightarrow[\text{phase recurrence}]{}\langle\phi,H_A\phi\rangle.
\end{aligned}
\]

But the rank-one limit has

\[
\langle f_t,Ph_t\rangle
=
\left(
\int_0^\ell
e^{-itu}g(u)\phi(u)\,du
\right)^2
\longrightarrow0
\]

as \(t\to\infty\) by the Riemann–Lebesgue lemma.

Therefore, for every \(A\),

\[
\boxed{
\|H_A-P\|_{2\to2}
\ge
\langle\phi,H_A\phi\rangle.
}
\]

Using the strong convergence from Theorem B,

\[
\langle\phi,H_A\phi\rangle
\longrightarrow
\langle\phi,P\phi\rangle
=
1-e^{-\ell}.
\]

Hence:

### Theorem C: exact topology no-go

\[
\boxed{
\liminf_{A\to\infty}
\|H_A-P\|_{2\to2}
\ge
1-e^{-\ell}
>0.
}
\]

So a proof argument that requires the normalized prime atomic boundary block to converge to the smooth pole block **uniformly on all \(L^2\) states is impossible**.

This is the arithmetic analogue of high-frequency, almost-periodic phase recurrence surviving a weak/strong continuum limit.

## 5. Uniform convergence on the natural logarithmic energy ball

Let \(\mathscr V_\ell\) be the zero-extension logarithmic energy space on \((0,\ell)\), equipped with the graph norm

\[
\|f\|_{\mathscr V_\ell}^2
=
\|f\|_2^2+
\frac14\int_{-\ell}^{\ell}
\frac{\|\tau_h f_0-f_0\|_2^2}{|h|}\,dh.
\]

The Fourier multiplier grows like \(\log|\xi|\), so the unit ball of \(\mathscr V_\ell\) is **relatively compact in \(L^2(0,\ell)\)**, by the same Fréchet–Kolmogorov argument established in the zero-extension theorem.

A uniformly bounded family of operators converging strongly converges uniformly on every norm-compact set. Applying that fact to the unit ball of \(\mathscr V_\ell\):

### Theorem D: the completed energy topology is admissible

\[
\boxed{
\|H_A-P\|_{\mathscr V_\ell\to L^2(0,\ell)}
\longrightarrow0.
}
\]

The critical logarithmic domain is not an arbitrary norm chosen to conceal the high-frequency obstruction; it is the canonical source domain of Suzuki's Archimedean difference operator.

### Effective convergence on \(H_0^1\)

Define the cumulative source discrepancy

\[
\eta_A(\ell)
=
\sup_{0\le w\le2\ell}
\left|
\mu_A([0,w])-2(1-e^{-w/2})
\right|.
\]

For \(f\in H_0^1(0,\ell)\), extend it by zero. Stieltjes integration by parts gives

\[
|(H_A-P)f(u)|
\le
\eta_A(\ell)\|f'\|_{L^1(0,\ell)}.
\]

Therefore

\[
\boxed{
\|H_A-P\|_{H_0^1\to L^2}
\le
\ell\,\eta_A(\ell).
}
\]

Unconditional PNT gives \(\eta_A(\ell)\to0\).

This estimate offers a controlled finite-source approximation for smooth boundary inputs.

## 6. The exact RH-level rate

PNT determines only

\[
\eta_A(\ell)=o(1).
\]

The Riemann Hypothesis demands a dramatically sharper rate.

### Theorem E: fixed-window source discrepancy criterion

Fix any \(\ell>0\). Then

\[
\boxed{
\mathrm{RH}
\iff
\exists\,C,K<\infty:
\quad
\eta_A(\ell)\le C e^{-A}(1+A)^K
\quad
\text{for all sufficiently large }A.
}
\]

**Proof, RH implies rate.** The von Koch bound from RH is

\[
\psi(X)-X=O(\sqrt X\log^2X).
\]

Abel summation implies

\[
S(X)=2\sqrt X+O(\log^3X).
\]

For \(X=e^{2A}\) and \(Y=Xe^{-w}\), both endpoint weighted sums have errors \(O_\ell(A^3)\). Multiplying by \(e^{-A}\) gives

\[
\eta_A(\ell)=O_\ell(e^{-A}A^3).
\]

**Proof, rate implies RH.** Choose the fixed window \(w_0=2\ell\). The assumed estimate implies

\[
S(X)-S(Xe^{-w_0})
=
2(\sqrt X-\sqrt X e^{-w_0/2})
+
O((\log X)^K).
\]

Iterate across the geometric sequence \(X,Xe^{-w_0},Xe^{-2w_0},\ldots\) down to a bounded basepoint. Summing the errors gives

\[
S(X)=2\sqrt X+O((\log X)^{K+1}).
\]

The inverse Stieltjes partial summation identity

\[
\psi(X)=\sqrt X S(X)
-\frac12\int_1^X S(u)u^{-1/2}\,du
\]

then gives

\[
\psi(X)=X+O(\sqrt X(\log X)^{K+1}).
\]

Every such polylogarithmic square-root error implies RH (zero-free half-plane \(\Re s>1/2\) by the standard explicit-formula/von-Koch implication).

This theorem is an **RH-equivalent rate criterion**, not an unconditional proof of that rate.

## 7. What this says about the arithmetic curvature program

There are now three distinct mathematical levels:

\[
\boxed{\text{PNT: strong boundary prime–pole matching}}
\]

\[
\boxed{\text{RH: exponential-in-horizon rate of the source matching}}
\]

\[
\boxed{\text{bare }L^2\text{ operator norm: no matching, ever}}
\]

The norm obstruction explains why generic Hilbert-space dilation claims and uncontrolled finite-to-infinite spectral limits fail.

The logarithmic Weil graph norm is strong enough to suppress fake high-frequency recurrences **qualitatively**, but proving the RH-scale rate in a form stable under the global completed operator remains the missing step.

The boundary-layer theorem is not a proof that RH follows from causality, Gamma, the arithmetic cube, or PNT.

It isolates the exact scale and topology in which a further arithmetic estimate must be found.

## 8. Falsification and reproduction

The companion \`scripts/rh_log_bathtub_boundary_probe.py\` verifies:

1. the improved bathtub lower bound at explicit indices;
2. the exact finite-chain shift constants;
3. prime-support gap asymptotics;
4. the normalized weighted von-Mangoldt boundary measures;
5. the strong convergence of the prime boundary operator on a fixed positive test profile;
6. the exact rank-one pole response.

No zeta zeros are used.

Numerical results are calibration, not proof of the infinite/source-rate claims.

## 9. Claim ledger

**DISCLOSED:** PNT weak source convergence, strong boundary operator convergence, exact rank-one pole matching, failure of \(L^2\) operator-norm convergence with quantitative lower bound, uniform convergence in the compact logarithmic graph topology, \(H^1\) discrepancy estimate, and RH-equivalent exponential window-rate criterion.

**UNVERIFIED:** the exponential rate itself; any all-horizon Weil positivity conclusion.

**RH:** OPEN.
