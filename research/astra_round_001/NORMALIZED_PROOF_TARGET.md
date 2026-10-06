# Normalized proof target

Status: **RH NOT PROVED**. Fourier convention throughout this file:
\(\widehat f(z)=\int_{\mathbb R}f(x)e^{izx}\,dx\), inverse factor \(1/(2\pi)\).
Write \(\psi_0=\Gamma'/\Gamma\); reserve \(\Lambda(n)\) for von Mangoldt.

## Definition and exact endpoint

For \(t\ge0\), put
\[
\begin{aligned}
\Psi(t)={}&4(e^{t/2}+e^{-t/2}-2)
-\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n)\\
&+\frac t2[\psi_0(1/4)-\log\pi]
+\frac14[C-e^{-t/2}\Phi(e^{-2t},2,1/4)],\qquad C=\pi^2+8G.
\end{aligned}
\]
Extend evenly. The formula gives \(\Psi(0)=0\) and continuity. No zero
ordinates enter the definition. For \(t>0\) only finitely many prime powers
contribute; the Archimedean series and all its derivatives converge locally
uniformly away from zero.

**PRIMARY-SOURCE THEOREM:** Suzuki, Theorem 1.7,
\[
\mathrm{RH}\iff\Psi(t)\ge0\quad\text{for all real }t.
\]
Theorem 1.2 also gives \(\mathrm{RH}\iff -\Psi\) is a global screw function.
Theorems 1.1 and 1.6 supply the unconditional transform
\[
\int_0^\infty\Psi(t)e^{izt}dt
=-z^{-2}\frac{\xi'}{\xi}(1/2-iz),\quad\Im z>1/2,
\]
and \(\mathrm{RH}\iff\Psi=O(1)\). Here
\(\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\).
These are accepted source theorems, not new results of this round.

## Rectangle, tent, and the arithmetic Weil functional

Let \(\widetilde f(x)=\overline{f(-x)}\) and
\(R_t=2^{-1/2}1_{[-t/2,t/2]}\). The overlap of the two intervals has
length \((t-|x|)_+\), so
\[
\Delta_t=R_t*\widetilde R_t=\tfrac12(t-|x|)_+.
\]
Direct integration, including removable values at zero, gives
\[
\widehat R_t(z)=\sqrt2\,\frac{\sin(zt/2)}z,\qquad
\widehat\Delta_t(z)=\frac{1-\cos(zt)}{z^2},\qquad
\widehat\Delta_t(0)=t^2/2.
\]
This is an entire identity for complex \(z\); on nonreal arguments it is
not an absolute-value square.

In the centered Weil convention, for suitable tests (including this tent),
\[
\begin{aligned}
W(f)={}&\widehat f(i/2)+\widehat f(-i/2)
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}[f(\log n)+f(-\log n)]\\
&-(\log\pi)f(0)
+\frac1{2\pi}\int_{\mathbb R}\widehat f(v)
\Re\psi_0(1/4+iv/2)\,dv.
\end{aligned}
\]
For the tent this integral converges absolutely, since its transform is
\(O(v^{-2})\) and the digamma grows logarithmically. Thus no smooth-test
extension is being assumed without checking the actual expression.

The pole terms give \(4(e^{t/2}+e^{-t/2}-2)\); the prime terms give
exactly the negative ramp sum. To check the Gamma term independently,
set \(a=1/4\) and use the convergent digamma difference series:
\[
\Re\psi_0(a+iv/2)-\psi_0(a)
=\sum_{k\ge0}\left[\frac1{k+a}
-\frac{k+a}{(k+a)^2+(v/2)^2}\right].
\]
The inverse transform of the second fraction is
\(e^{-2(k+a)|x|}\). Consequently each summand contributes
\[
\frac{t}{2(k+a)}-\int_0^t(t-x)e^{-2(k+a)x}dx
=\frac{1-e^{-2(k+a)t}}{4(k+a)^2}.
\]
Interchange is justified by nonnegativity on the real Fourier side and
Tonelli; the final series converges. Summing proves, from the arithmetic
formula alone,
\[
\boxed{W(\Delta_t)=\Psi(t).}
\]
This agrees exactly with Suzuki §3.4, equations (3.9)–(3.11), and (5.15).
The sinc connection is therefore exact. Positivity of the signed functional
on these tents remains the missing assertion.

## Implementation audit

`scripts/suzuki_psi.py` matches Suzuki (1.1) term by term. The initial
requirements file contained literal `\\n`; the initial tests also treated a
rounded `log(q)` as an exact event, and the `0.1` fixture had been produced
from a binary floating-point input. The round repairs these issues, sorts
supplied event lists, and retains requested precision in the screw kernel
and CLI. These are numerical correctness fixes, not research results.

`scripts/event_dynamics.py` independently evaluates the Archimedean part
using Arb constants and a finite exponential sum with a proven geometric
tail enclosure. Integer event indices replace ambiguous floating-point
event comparisons. Regression fixtures are not attributed to a printed
table in Suzuki. Baseline mpmath output is not itself a sign certificate.

One source typo matters for implementation: in the inspected Suzuki v4
PDF, p. 11, §4.1, the displayed constant in the arctangent formula for
\(\Psi'\) omits \(-\tfrac12\log\pi\). Differentiating (1.1) gives
\[
c=\pi/4-(\gamma_E+3\log2+\log\pi)/2.
\]
The round uses (1.1) and the independently differentiated series; the
printed omission does not change the primary definition or the endpoint
theorems. A regression test checks the derivative against that definition.

Primary sources checked: [Suzuki v4](https://arxiv.org/pdf/2206.03682v4),
[Nakamura–Suzuki v1](https://arxiv.org/pdf/2306.08317v1).
The experimental HTML carries an inconsistent generated date, so theorem
numbers and versioned sources identify the claims used here.
