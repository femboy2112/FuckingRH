# Screw–Sinc–Lévy unification

**Status:** canonical current attack surface.  
**Core sources:** Masatoshi Suzuki, JLMS 108 (2023), DOI 10.1112/jlms.12785; Takashi Nakamura & Masatoshi Suzuki, *Statistics & Probability Letters* 2023 / arXiv:2306.08317.

This file records an exact synthesis that emerged during the 2026-10-05 consolidation.

## 1. The explicit prime-wavefront function

For \(t\ge0\), Suzuki defines

\[
\begin{aligned}
\Psi(t)
={}&4(e^{t/2}+e^{-t/2}-2)
-\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n)\\
&+\frac t2\left[\frac{\Gamma'}{\Gamma}\!\left(\frac14\right)-\log\pi\right]\\
&+\frac14\left(C-e^{-t/2}\Phi(e^{-2t},2,1/4)\right),
\end{aligned}
\]

where \(C=\Phi(1,2,1/4)=\pi^2+8G\), and extends it evenly to \(t<0\).

This is already a literal moving arithmetic wavefront:

\[
n\text{ contributes at time }t
\quad\Longleftrightarrow\quad
\log n\le t
\quad\Longleftrightarrow\quad
n\le e^t.
\]

Each prime power enters at the exact event time \(t=\log p^k\) and thereafter contributes a linear ramp

\[
\frac{\Lambda(p^k)}{p^{k/2}}(t-k\log p)_+.
\]

So \(\Psi\) is a smooth Archimedean reservoir minus an integrated prime-power impulse train.

Distributionally,

\[
\frac{d^2}{dt^2}(t-a)_+=\delta_a.
\]

Therefore the prime side of \(\Psi''\) is literally a weighted point process supported on \(\{\log p^k\}\).

## 2. This scalar function is already RH-equivalent

Suzuki, Theorem 1.7:

\[
\boxed{\mathrm{RH}\iff \Psi(t)\ge0\quad\text{for every }t\in\mathbb R.}
\]

If RH holds, \(\Psi(t)>0\) for \(t\ne0\).

This is a genuine simplification of the proof target: it is enough to prove one explicit scalar inequality for all real \(t\). No zero ordinates are needed to *define* \(\Psi\).

The zero-side identity, valid unconditionally as an identity over the complex zero parameters, is

\[
\Psi(t)=\sum_\gamma \frac{1-\cos(\gamma t)}{\gamma^2}.
\]

Under RH every \(\gamma\) is real and each term is nonnegative; conversely Suzuki proves that pointwise nonnegativity forces RH via the one-sided Laplace/Fourier transform

\[
\int_0^\infty \Psi(t)e^{izt}\,dt
=
-\frac1{z^2}\frac{\xi'}{\xi}\!\left(\frac12-iz\right),
\qquad \Im z>\frac12.
\]

## 3. The exact sinc/convolution-square bridge

Let

\[
R_t(x)=\frac1{\sqrt2}\mathbf 1_{[-t/2,t/2]}(x)
\]

(up to irrelevant endpoint conventions). Then

\[
\Delta_t=R_t*\widetilde R_t
=
\frac12(t-|x|)_+.
\]

Its Fourier transform is

\[
\widehat{\Delta_t}(z)
=
\frac{1-\cos(zt)}{z^2}
=
\frac{2\sin^2(zt/2)}{z^2}.
\]

Thus the RH-equivalent scalar function is exactly the Weil quadratic form evaluated on a one-parameter family of rectangular-window convolution squares:

\[
\boxed{\Psi(t)=W(\Delta_t)=W(R_t*\widetilde R_t).}
\]

This is the precise mathematical realization of the "Borwein / backwards Brownian sinc" intuition:

- rectangular windows convolve to triangular/tent kernels;
- Fourier transforms of rectangles are sinc functions;
- the RH-equivalent test is a sinc-squared spectral window;
- increasing \(t\) expands the real-space support while narrowing the spectral sinc scale;
- prime powers enter exactly when the expanding support reaches \(\log p^k\).

Remark: generic Weil positivity requires all admissible convolution squares. The special arithmetic structure of zeta makes this single one-parameter family sufficient, by Suzuki's Theorem 1.7. That is unusually strong and should be exploited.

## 4. Screw kernel = covariance/negative-type kernel

Put

\[
g(t)=-\Psi(t).
\]

Kreĭn's screw kernel is

\[
G_g(t,u)
=
g(t-u)-g(t)-g(-u)+g(0).
\]

Since \(\Psi\) is even and \(\Psi(0)=0\),

\[
\boxed{
G_g(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u).
}
\]

Suzuki, Theorem 1.2:

\[
\boxed{
\mathrm{RH}\iff g=-\Psi\text{ is a screw function on }\mathbb R,
}
\]

equivalently \(G_g\) is positive semidefinite on every finite set.

Under RH,

\[
G_g(t,u)
=
\sum_\gamma
\frac{(e^{i\gamma t}-1)(e^{-i\gamma u}-1)}{\gamma^2},
\]

so it is manifestly a Gram kernel.

This is the exact Brownian connection. If the variogram were \(\Psi(t)=c|t|\), then for \(t,u\ge0\),

\[
\frac12G_g(t,u)=c\,\min(t,u),
\]

the covariance kernel of Brownian motion (up to scale).

Therefore the current "wavefunction/wavefront" intuition has a rigorous non-quantum form:

> \(\Psi\) is the candidate variogram of a stationary-increment Hilbert/probability process; RH says the associated covariance kernel is globally positive.

## 5. Lévy–Khintchine is the same condition in probability language

Nakamura–Suzuki use exactly

\[
g_\zeta(t)=-\Psi(t)
\]

and prove

\[
\boxed{
\mathrm{RH}
\iff
e^{g_\zeta(t)}=e^{-\Psi(t)}
\text{ is the characteristic function of an infinitely divisible probability law.}
}
\]

Under RH its Lévy measure is

\[
\nu_\zeta
=
\sum_\gamma\frac{m_\gamma}{\gamma^2}\delta_{-\gamma},
\]

and

\[
g_\zeta(t)
=
\sum_\gamma m_\gamma\frac{e^{-i\gamma t}-1}{\gamma^2}.
\]

Thus three languages are the same proof gate:

\[
\boxed{
\begin{array}{c}
\Psi(t)\ge0\ \forall t\\
\Updownarrow\ \text{(for this special }\Psi\text{; Suzuki)}\\
g=-\Psi\text{ is a global screw function}\\
\Updownarrow\\
G_g(t,u)\succeq0\\
\Updownarrow\ \text{(negative-type/Schoenberg language)}\\
e^{-\Psi(t)}\text{ is infinitely divisible characteristic}\\
\Updownarrow\\
\mathrm{RH}.
\end{array}
}
\]

The middle equivalences should be written with the precise hypotheses/sign conventions when formalized, but the end RH equivalences are primary-source theorems.

## 6. Why this is better than generic CLT

The aggregate finite-prime convolution picture explains why a Gaussian bulk should emerge, but ordinary CLT discards the higher residual.

The function \(\Psi\) keeps the residual exactly.

It is:
- built directly from prime powers and the Archimedean completion;
- finite-wavefront at each \(t\);
- equivalent to the Weil tent/sinc-squared test;
- equivalent to a screw covariance positivity problem;
- equivalent to an infinite-divisibility problem;
- and its one-sided transform is exactly \(-z^{-2}\xi'/\xi\).

Therefore the first proof attack should work directly on \(\Psi\), not first prove a generic CLT and then attempt to reconstruct the missing arithmetic residual.

The CLT/Lévy picture remains explanatory and may supply the correct decomposition or comparison inequality.

## 7. Event dynamics: a deterministic reserve process

Write

\[
\Psi(t)=A_\infty(t)-P(t)
\]

where \(A_\infty\) contains the explicit smooth/pole/Archimedean terms and

\[
P(t)=
\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n).
\]

Between consecutive event times \(\log q_j< t<\log q_{j+1}\), the active prime-power set is fixed, so \(P(t)\) is affine in \(t\). All curvature comes from \(A_\infty(t)\).

At \(t=\log q\), the new prime-power term starts at zero but changes the derivative thereafter by

\[
-\frac{\Lambda(q)}{\sqrt q}.
\]

So the evolution is:

1. smooth Archimedean curvature rebuilds reserve;
2. a prime-power event causes a downward slope jump;
3. the next interval has a constrained minimum determined by the post-event slope and smooth curvature;
4. RH is exactly the assertion that the reserve never crosses zero.

This is an integrate-and-fire / storage / queue interpretation, not a stochastic assumption.

## 8. Nearby 2026 checkpoint work — UNVERIFIED in this repository

Recent Zenodo preprints by Rainer Andreas Mittermeier claim:
- strict convexity between prime-power events after a small initial range;
- reduction to one constrained minimum per prime-power interval;
- directed-rounding certification through \(q=10^{10}\);
- a remaining infinite-tail inequality involving a smoothed von Mangoldt sum.

These claims are highly relevant because they attack exactly the event-dynamics form above, but they have not been independently reconstructed here and are not promoted to theorem status in this repository.

Astra should audit them as an adversarially useful external lead, not import their conclusions.

## 9. The immediate bona fide proof target

The shortest valid target is now:

\[
\boxed{
\text{Prove }\Psi(t)\ge0\text{ for every }t\ge0
\text{ directly from the prime/Archimedean formula (without zero locations).}
}
\]

Preferred ways to earn this:

### Route A — exact reserve invariant
Find \(E(t)\ge0\), constructed from finite prime-place/convolution data, such that

\[
\Psi(t)=E(t)
\]

identically.

### Route B — screw/negative-type factorization
Construct a Hilbert map \(V(t)\) from arithmetic data only with

\[
G_g(t,u)=\langle V(t),V(u)\rangle.
\]

Then \(G_g\succeq0\), hence RH.

### Route C — Lévy closure
Construct positive finite Lévy measures \(\nu_X\) with exponents \(g_X\) and prove

\[
g_X\to -\Psi
\]

in a topology preserving infinite divisibility / conditional negative definiteness.

### Route D — event/checkpoint invariant
Prove a global inductive inequality that the Archimedean reserve accumulated between successive prime-power events always pays for the next slope jump and leaves nonnegative minimum reserve.

The proof may combine routes, but the final chain must terminate explicitly in Suzuki Theorem 1.7, Theorem 1.2, or Nakamura–Suzuki Theorem 1.1.

## 10. Falsifiers

Any proposed proof must survive:
- synthetic off-line zero models;
- removal/duplication of a prime-power event;
- randomized prime phases with preserved one-point density;
- mutation of the Archimedean term;
- the two-prime Gaussian positivity obstruction;
- positive Fourier-self-dual Gaussian-mixture false friends;
- finite-window success with a planted negative tail;
- checking whether a bound secretly imports an RH-equivalent Chebyshev/PNT error estimate.

A theorem that simply assumes the needed square-root cancellation under another name is not a proof.
