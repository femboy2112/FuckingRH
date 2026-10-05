# Convolution support and the exact geometric-prime residual

Status: **NEW LEMMAS PROVED THIS ROUND**, with no priority claim. The canonical
geometric-prime Gaussian-divided residual cannot converge to the desired
characteristic function. Borwein support geometry transfers to event detection,
but does not supply the missing arithmetic positivity. **RH remains open.**

The proofs here use no zero locations, except for an explicitly synthetic
off-line-zero negative control. No prime-number error estimate stronger than the
ordinary, unconditional prime number theorem is used.

## 1. What the Borwein theorem actually preserves

Use the Fourier transform `hat f(z)=integral f(x) exp(izx) dx`. For `a>0`, let
`U_a(x)=1_{[-a,a]}(x)/(2a)`. Then `hat U_a(z)=sinc(az)`. If independent random
variables `Y_j` have densities `U_{a_j}`, Fourier inversion gives, for `n>=1`,

\[
 \int_0^\infty\prod_{j=0}^n\operatorname{sinc}(a_jz)\,dz
 =\frac{\pi}{2a_0}\Pr\left(\left|\sum_{j=1}^nY_j\right|\le a_0\right).
\]

Indeed the product transforms to the density of `Y_0+...+Y_n`; its value at
zero is `(2a_0)^{-1}` times the displayed probability. The product of at least
two sinc factors is integrable; the convolved density is continuous there.
Consequently the integral is exactly `pi/(2a_0)` when
`sum_{j>=1}a_j <= a_0`. After contact, the correction is exactly the nonnegative
probability mass outside `[-a_0,a_0]`. This is a positive-measure statement with a
constant plateau. It is not a general theorem that any distribution evaluated
on a convolution square is nonnegative.

For the RH tent, the exact rectangle convolution is

\[
 R_t=2^{-1/2}\mathbf1_{[-t/2,t/2]},\qquad
 R_t*\widetilde R_t(x)=\Delta_t(x)=\tfrac12(t-|x|)_+.
\]

The overlap length of the two intervals is `(t-|x|)_+`; this proves the first
identity directly. Integrating the even tent, or squaring the rectangle
transform, gives

\[
 \widehat\Delta_t(z)=\frac{1-\cos(tz)}{z^2},\qquad
 \widehat\Delta_t(0)=t^2/2.
\]

The exact Weil-normalization calculation is in `NORMALIZED_PROOF_TARGET.md`.
Its consequence `W(Delta_t)=Psi(t)` does not turn `W` into a positive measure.
The prime part of `W` has *negative* masses at `+/-log(p^k)`.

| Borwein datum | RH tent datum | What transfers |
|---|---|---|
| Accumulated support `sum a_j` | Tent radius `t` | An exact support boundary exists. |
| Fixed plateau boundary `a_0` | Each separate location `log q` | There is a family of contacts, not one plateau. |
| Density at zero of positive convolution | Signed functional `W(Delta_t)` | No positivity transfer has been established. |
| Support first exits the plateau | `t=log q` first reaches an arithmetic atom | The event time transfers exactly. |
| Nonnegative lost probability mass | `-(Lambda(q)/sqrt(q))(t-log q)_+` | The post-contact ramp has known negative sign; no upper bound from support. |

There is no pre-contact constant for `Psi`: before `log 2`, `Psi=A_infinity`
and its curvature is

\[
 A_\infty''(t)=e^{t/2}+e^{-t/2}
               -\frac{e^{-t/2}}{1-e^{-2t}}.
\]

This follows by twice differentiating the absolutely locally uniformly
convergent Lerch series for `t>0`. In particular it is not identically zero on
the initial interval. The same formula gives

\[
 \Psi(t)=\tfrac12t\log(1/t)+O(t)\quad(t\downarrow0).
\]

To justify integration at zero, first integrate `A''=-1/(2t)+O(1)` from any
fixed positive point; then integrate its locally integrable derivative to zero,
using `Psi(0)=0`. Thus `Psi>0` sufficiently near zero, independently of RH.

**Support-only no-go lemma.** Keep `A_infinity` and every event location fixed.
At an existing event `q`, increase its weight `w_q` by any `c>0`. The reserve
changes by exactly `-c(t-log q)_+`. It is unchanged through the contact time and
becomes negative at any prescribed later `t_*` if
`c > max(Psi(t_*),0)/(t_*-log q)`. Thus support, the rectangle identity, positive
arithmetic weights, and the contact schedule do not imply reserve positivity.
Exact arithmetic amplitudes and a global comparison are indispensable.
This refutes that proof class, not the possibility of a new theorem using the
exact amplitudes.

One additional mismatch is decisive for the proposed geometric-prime mapping:
even a *single* geometric variable `K_p log p` has unbounded support. The finite
prime product has infinite support diameter already. Its support cannot be the
finite accumulated rectangle support in the Borwein plateau theorem.

## 2. Reproduce the aggregate-prime central limit theorem

Write `r_p=p^{-1/2}` and let independent `K_p` have probabilities
`Pr(K_p=k)=(1-r_p)r_p^k`, `k>=0`. For

\[
 S_X=\sum_{p\le X}K_p\log p
\]

the exact mean, variance and cumulants are

\[
 m_X=\sum_{p\le X}\frac{r_p\log p}{1-r_p},\quad
 V_X=\sum_{p\le X}\frac{r_p(\log p)^2}{(1-r_p)^2},
\]

\[
 \kappa_j(X)=\sum_{p\le X}(\log p)^j
                  \sum_{k\ge1}k^{j-1}r_p^k\quad(j\ge1).
\]

The cumulant formula follows by expanding the logarithm of the geometric
generating function in its absolutely convergent power series near zero.
For every fixed integer `j>=1`, PNT and partial summation give

\[
 \sum_{p\le X}\frac{(\log p)^j}{\sqrt p}
       \sim2\sqrt X(\log X)^{j-1}.
\]

The `k>=2` part is bounded by a constant depending on `j` times
`sum_{p<=X}(log p)^j/p=O((log X)^{j+1})` (even summing over all integers proves
this sufficient bound). Hence

\[
 m_X\sim2\sqrt X,\quad V_X\sim2\sqrt X\log X,\quad
 \kappa_j(X)\sim2\sqrt X(\log X)^{j-1}.
\]

For completeness, `E K^3=r(1+4r+r^2)/(1-r)^3`. The inequality
`|x-y|^3<=4(|x|^3+|y|^3)` and `r_p<=1/sqrt(2)` give
`E|K_p-EK_p|^3<=C r_p` with one absolute constant. The Lyapunov ratio is therefore

\[
 \frac{\sum_{p\le X}(\log p)^3\mathbb E|K_p-\mathbb EK_p|^3}{V_X^{3/2}}
 =O(X^{-1/4}\sqrt{\log X})\longrightarrow0.
\]

Lyapunov's theorem proves `(S_X-m_X)/sqrt(V_X) => N(0,1)`. This is the precise
CLT stated in the prior repository. No RH-sized PNT error was needed.

The deterministic identity `(sum a_p log p)^2` does contain cross-prime terms.
For independent *centered* variables their expectations vanish, so variances
add. Gaussian evaluation of the summed coordinate and independent primewise
Gaussian evaluation are different operations. The cross terms do not, by
themselves, provide the missing correlations or an RH residual.

## 3. Exact residual obstruction: finite, infinite and normalized

Define the centered characteristic function `chi_X(t)` and its Gaussian-divided
residual `R_X(t)` by

\[
 \chi_X(t)=\mathbb E e^{it(S_X-m_X)},\qquad
 R_X(t)=e^{V_Xt^2/2}\chi_X(t).
\]

There is an exact factorization, with no cumulants discarded:

\[
 \chi_X(t)=e^{-V_Xt^2/2}R_X(t),
\]

\[
 \log R_X(t)=\sum_{p\le X}\sum_{k\ge1}\frac{r_p^k}{k}
 \left[e^{itk\log p}-1-itk\log p+\tfrac12t^2k^2(\log p)^2\right].
\]

The logarithm is the continuous branch zero at the origin. The series is
absolutely convergent for each finite `X` and real `t`.

**Lemma R1 — Gaussian removal destroys the necessary characteristic-function
bound.** For every `X>=2` and every real `t!=0`,

\[
 \boxed{\log|R_X(t)|
 =\sum_{p\le X,k\ge1}\frac{r_p^k}{k}
       [\cos(tk\log p)-1+\tfrac12(tk\log p)^2]>0.}
\]

Proof: `cos x >= 1-x^2/2`, strictly for nonzero `x`. For example the derivative
of `x-sin x` is `1-cos x>=0`, and integrating twice proves strictness.
Every summand is positive for `t!=0`. Thus `|R_X(t)|>1`, whereas any
characteristic function `phi` has `|phi(t)|<=phi(0)=1`. More explicitly the
two-point positive-definiteness determinant `1-|R_X(t)|^2` is negative.
Neither `R_X` nor its symmetric counterpart `|R_X|^2` is a characteristic
function. The real part of `-log R_X` is negative, opposite to a negative-type
exponent. **This is a failure already at one prime**, not only in a limiting
interchange. Since `Psi>0` near zero, neither `R_X=e^{-Psi}` nor
`-log R_X=Psi` is even a literal identity for finite `X`.

**Lemma R2 — the unscaled residual diverges.** Put

\[
 M_X=\sum_{p\le X,k\ge1}r_p^k/k
    =\sum_{p\le X}-\log(1-r_p)
    \sim\frac{2\sqrt X}{\log X}.
\]

The asymptotic again follows from PNT and partial summation; the `k>=2` terms
are `O(log X)`, which is sufficient. The elementary bound `-2<=cos x-1<=0`
gives

\[
 \tfrac12V_Xt^2-2M_X\le\log|R_X(t)|\le\tfrac12V_Xt^2.
\]

Since `M_X/V_X ->0`, for each fixed nonzero real `t`,

\[
 \log|R_X(t)|\sim\tfrac12t^2V_X\longrightarrow+\infty.
\]

Consequently this sequence has no finite mod-Gaussian limit at any fixed
nonzero `t`. Multiplication by any fixed finite nonzero Archimedean factor
`B(t)` cannot repair the divergence. In particular, appending the exact,
cutoff-independent `exp(-A_infinity(t))` does not produce `exp(-Psi(t))`.
An `X`-dependent cancellation would require a different, explicitly justified
construction; it is not an application of the claimed residual limit.

**Lemma R3 — normalizing instead removes the entire residual.** The CLT yields

\[
 R_X(t/\sqrt{V_X})=e^{t^2/2}\chi_X(t/\sqrt{V_X})\longrightarrow1.
\]

Thus the two proposed normalizations give either divergence or the trivial
residual. Neither is the nonconstant Suzuki exponent or screw kernel.

**Lemma R4 — no change of scalar scale can turn this quotient into the target.**
Let `b_X>0`, let `theta_X(t)` be any real phases, and suppose
`exp(i*theta_X(t))*R_X(t/b_X)` converges pointwise to a characteristic function
`phi(t)`. Lemma R1 gives `|phi(t)|>=1`; the characteristic-function bound gives
the reverse inequality. Hence `|phi(t)|=1` for all `t`. Such a probability law
is a point mass: equality in the triangle inequality makes `exp(itY)` almost
surely constant for every rational `t`; taking a countable intersection and
using continuity forces any two values in the support to coincide. Therefore
the limit is degenerate. In particular it cannot be `exp(-Psi(t))`, whose
modulus is strictly below one at sufficiently small positive `t`, by the
prime-free initial-range calculation in §1. The same proof applies to the
symmetric quotients `|R_X(t/b_X)|^2`. This rules out *all scalar rescalings and
unit-phase repairs of the exact Gaussian quotient* for the requested target,
without assuming a rate or invoking RH.

There is an additional precise obstruction to using the *unrenormalized*
positive prime Lévy measures. Their masses beyond `|x|>1` tend to infinity,
contrary to the Lévy-measure condition. Indeed, at each fixed `t!=0`, PNT gives

\[
 \sum_{p\le X}p^{-1/2+it}
 =\frac{X^{1/2+it}}{(1/2+it)\log X}
       +o(\sqrt X/\log X),
\]

by partial summation of `pi(x)~x/log x`; replacing `pi` by its error term gives
`o(sqrt X/log X)` because the integral is weighted by `x^{-1/2}`.
Subtracting the `t=0` expression and observing that `k>=2` contributes only
`O(log X)` shows

\[
 \log|\chi_X(t)|
 =\frac{2\sqrt X}{\log X}
 \left[\Re\frac{e^{it\log X}}{1+2it}-1+o(1)\right]\to-\infty.
\]

The bracket is at most `(1+4t^2)^{-1/2}-1+o(1)<0`. Therefore the pointwise limit
is zero off the origin and one at it, discontinuous at zero. No weak probability
limit exists for these centered unscaled laws. This supplements, rather than
replaces, the stronger exact Gaussian-residual obstruction.

**Scope.** These lemmas rule out this specific canonical geometric-prime
construction, its direct Gaussian quotient, and cutoff-independent
Archimedean repair. They do not rule out every arithmetic Hilbert construction,
every mod-Gaussian problem, or an entirely different positive Lévy sequence.
Wahl's prime Dirichlet-polynomial model is different; its genuine mod-Gaussian
theorem is not a convergence theorem for the `S_X` used here.

## 4. Hostile controls and what each detects

1. **Functional-symmetry off-line zeros.** Take artificial centered parameters
   `z=+/-a+/-ib`, where `a>b>0`; these correspond to a functional-equation and
   conjugation-symmetric quartet. Their tent sum at `t=2*pi/a` is exactly
   `4(1-cosh(2*pi*b/a))(a^2-b^2)/(a^2+b^2)^2<0`. The small-`t` sum begins
   `2t^2+O(t^4)>0`. Symmetry and a locally successful sinc test fail globally.

2. **Two-prime Gaussian transport.** The nonnegative finite-adelic indicator
   `beta_1-beta_p-beta_q+beta_pq` maps under the prescribed Gaussian assignment
   to `g(x)-g(px)-g(qx)+g(pqx)`. Its quadratic coefficient is
   `-pi(p^2-1)(q^2-1)<0`. The tested pair `2,3` has coefficient `-24*pi`.
   This is a global positivity failure of that transport, independent of CLT.

3. **Positive self-dual mixture.** For `g(x)=exp(-pi*x^2)`,
   `(10g(x)+16g(16x)+g(x/16))/27` is positive, Fourier-self-dual, and normalized
   in value and integral. Its Mellin multiplier is
   `P(s)=(16^s+2)(16^s+8)/(27*16^s)`, invariant under `s ->1-s`. Roots with
   `16^s=-2,-8` have real parts `1/4,3/4`. Exact rational polynomial and Fourier
   coefficient tests recover the prior repository's control independently.

4. **Phase mutations with the same Gaussian bulk.** Replace each centered
   summand by `epsilon_p*(K_p-EK_p)*log p`, `epsilon_p in {-1,+1}`; these are
   explicit phase rotations by `0` or `pi` of the jump coordinate, including
   arbitrary independent random sign choices. Conditional on the signs,
   variance and Lyapunov numerator are unchanged, so the same CLT holds for
   every sign pattern. The third cumulant becomes
   `sum epsilon_p*(log p)^3*r_p*(1+r_p)/(1-r_p)^3` and changes. The Gaussian
   bulk therefore does not identify the arithmetic phase/coherence data.
   This is a parity-phase control, not a claim that arbitrary complex Euler
   factors remain probability distributions.

5. **A planted negative tail hidden by every prescribed finite window.** For
   `T>0`, `F_T(t)=t^2-5T*(|t|-T)_+` agrees with the negative-type function `t^2`
   on `[-T,T]`, but `F_T(2T)=-T^2`. Its screw kernel agrees with the rank-one
   PSD kernel `2tu` on any point set whose points and differences lie in that
   window, for example `[-T/2,T/2]`. All signs are exact rational arithmetic.
   This is a nonanalytic toy, deliberately matching the ramp-event structure;
   it is not proposed as another zeta function. The support-only mutation
   lemma also hides a negative tail in an actual future prime-power weight.

Duplicate/delete/amplitude mutations of actual events and Gamma mutations are
also treated in the round's event and Gram notes. None of the preceding controls
is a counterexample to RH. They kill implications whose hypotheses they obey.

## 5. Result and the next required theorem

The exact sinc/tent identity is retained. The supposed Borwein positivity
inheritance is rejected. The geometric-prime CLT is proved, but its canonical
Gaussian-divided residual is now decisively rejected as a route to a positive
Lévy limit: it fails a two-point PSD test before taking any limit and then
diverges at every nonzero unscaled frequency.

No equality with the finite-window Weil operator or prolate correction was
obtained. Such an equality would require a newly specified transform and
domain, together with exact Archimedean and prime-amplitude matching; the
factorization above is not that equality. No claim that all such transforms are
impossible is made.

The next verdict-changing probe should test a **new arithmetic construction**
against the exact event weight and Archimedean curvature before any asymptotic
Gaussianization. A putative positive Gram/Lévy construction must pass the
one-prime residual's two-point test and the event-amplitude mutation test.
The remaining global reserve theorem is stated in `PROOF_ATTEMPT_001.md`;
there is no new implication from these no-go lemmas to RH.

## Sources and reproducibility

Primary sources reopened on 2026-10-05:

- U. Bäsel and R. Baillie, *Sinc integrals and tiny numbers*,
  https://arxiv.org/pdf/1510.03200, pp. 1–3, equations (4)–(14): support plateau
  and exact post-contact formula. The probability identity above is derived
  here with its own normalization.
- NIST DLMF §27.12, https://dlmf.nist.gov/27.12: unconditional PNT. Every
  weighted asymptotic above is derived by partial summation; no square-root
  error estimate is assumed.
- M. Wahl, *On the mod-Gaussian convergence of a sum over primes*,
  https://arxiv.org/pdf/1201.5295, Theorems 1.1–1.2: a different prime
  Dirichlet-polynomial model, whose complex extension assumes RH.
- T. Nakamura and M. Suzuki, *On infinitely divisible distributions related to
  the Riemann hypothesis*, https://arxiv.org/pdf/2306.08317: the target is the
  characteristic function `exp(-Psi)`, not a Gaussian-divided geometric Euler
  product. Exact theorem normalization is audited in `LEVY_CND_BRIDGE.md`.

Local provenance: `CURRENT_STATE.md` §9 for the exact geometric model;
`research/2026-10-05/FOURIER_MELLIN_TRANSPORT_PROBE.md` for the two existing
transport counterexamples. Those counterexamples were re-derived algebraically
here rather than accepted from prior numeric runs.

Commands actually run:

```sh
python -m unittest tests/test_convolution_controls.py
python scripts/convolution_controls.py
```

Eight tests passed. Signs are enclosed with `mpmath.iv` at 50 decimal digits;
the Borwein probabilities, mixture identities, phase-moment control, and toy
tail are rational/exact. Representative enclosures (rounded outward here):

| Control | Enclosure/result |
|---|---|
| One-prime `log|R_2(1)|` | `[1.19535950494994, 1.19535950494995]` |
| One-prime two-point PSD determinant | `[-9.92134367490874, -9.92134367490873]` |
| Two-prime Gaussian image at `x=0.1` | `[-0.34383318068279, -0.34383318068278]` |
| Synthetic quartet `a=1,b=1/4` | `[-5.01318802599217, -5.01318802599215]` |
| Borwein post-contact plateau fraction | `11/12` exactly |
| Planted tail `T=10,t=20` | `-100` exactly |

These finite tests corroborate the implementations. The universal no-go
statements rest on the proofs above, not on sampling or floating-point signs.
