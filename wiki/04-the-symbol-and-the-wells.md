# 4. The symbol face and the wells

*This page develops the program's sharpest current vantage: the **band-limited symbol**. It is
where the prime side becomes an explicit, zero-free function you can plot — and where the exact
sense in which that function pairs with the zero functional becomes visible. The identity in
[§4.3](#43-the-wells-are-the-low-passed-zero-comb) is an equality on entire test functions;
the positive real zero-measure interpretation is conditional on RH. This qualification repairs
the earlier unconditional low-pass claim; see the
[frontier audit](../research/aletheia_2026-10-09/arithmetic_poisson/FRONTIER_CORRECTIONS.md).
The quantitative well law of
[§4.4](#44-diggability-when-can-a-band-limited-function-reach-a-well) is a **model**, calibrated
on a known off-line zero.*

---

## 4.1 One form, two faces

Weil's explicit formula ([§2.2](02-the-rh-equivalent-target.md)) is an *identity*. Fed a
self-correlation $f = g \star \tilde g$, let $F(z)=\int g(u)e^{izu}\,du$ and
$h(z)=F(z)\overline{F(\bar z)}$. On the real axis $h(t)=|F(t)|^2\ge0$; at complex
arguments the reflected product is essential. The formula reads the same number two ways:

$$\underbrace{\sum_\rho h(\gamma_\rho)}_{\text{zero face}}
= \text{pole} + \underbrace{\frac{1}{2\pi} \int \lvert \hat g(t)\rvert^2\, \Psi_L(t)\,
dt}_{\text{symbol face}}.$$

- **The zero face** $\sum_\rho h(\gamma_\rho)$. If every zero lies on the line, each
  $\gamma_\rho$ is real and this is a sum of non-negative numbers — positive *by inspection*. A
  single off-line zero injects a complex $\gamma_\rho$ and is the only way the sum can turn
  negative. **This face is RH**; you cannot evaluate it without already knowing where the zeros
  are.

- **The symbol face** $\int \lvert \hat g\rvert^2\, \Psi_L$. Here $\Psi_L(t)$ is an **explicit,
  zero-free function** — the archimedean background minus the finite prime comb
  ([§4.2](#42-the-weil-symbol)). You can compute it to any precision from the primes and the
  $\Gamma$-function alone.

The entire program lives in the gap between these two faces: the symbol face is computable and
zero-free, yet it equals the zero face, which is RH. **The symbol swing is the attempt to work
the zero-free face and understand why it is nonetheless pinned to the zeros.**

## 4.2 The Weil symbol

Write the symbol as

$$\Psi_L(t) = \mathrm{Re}\,\psi(\tfrac14 + it/2) - \log\pi - P_L(t),$$

paired against the spectral measure $\mu_f(t) = |\hat f(t)|^2/(2\pi)$ (plus a rank-2 pole term
for $\zeta$), so the completed form is $Q(f) = \mathrm{pole}(f) + \int \mu_f(t)\,\Psi_L(t)\,dt$.
This is the normalization in which the calibrated instrument reproduces the measured form to
$10^{-14}$ (the balancing archimedean constant is $-\log\pi$, not $-\tfrac12\log\pi$ — a slip
in an earlier draft of this page, caught by the gate). Here

- the **archimedean background** $\mathrm{Re}\,\psi(\tfrac14 + it/2) - \log\pi$ is smooth and
  slowly *growing*, like $\log(t/2\pi)$; and
- $P_L(t) = \sum_{n \le e^{2L}} 2\Lambda(n)\, n^{-1/2}\cos(t\log n)$ is the **finite prime comb** —
  a trigonometric polynomial whose frequencies are the prime-power logs $\log n$ of
  [§1.3](01-the-successor-frame.md), each weighted by the ray-incidence charge
  $\Lambda(n)\, n^{-1/2}$. *(Support convention: the cutoff is written $e^{2L}$ for a test
  function on $[-L,L]$; the calibrated instrument's own support parameter puts it near $e^{L}$ —
  a pure factor-of-2 convention, which is why measured values like $L^*\approx4.4$ are quoted in
  the instrument's normalization.)*

Finite support $L$ makes the comb finite: only prime powers with $\log n \le 2L$ (i.e.
$n \le e^{2L}$) contribute, which is the operator-level statement that a support-$L$ test function
only sees the primes it can resolve. The comb has **negative wells** — places where it pokes above
the background, so $\Psi_L(t) < 0$ — and by the Kronecker–Weyl alignment of
[§3.2](03-the-diophantine-semigroup-frame.md) the deepest wells sit where the prime phases
$\{t\log p\}$ conspire.

The key point of [page 3](03-the-diophantine-semigroup-frame.md) survives here in sharp form:
**pointwise $\Psi_L(t) < 0$ is allowed and real; a negative *direction of the quadratic form* is
RH-false.** The symbol can dip below zero all it likes; RH is whether a band-limited
$\lvert \hat g\rvert^2$ can *integrate* against it to something negative.

## 4.3 The wells are the low-passed zero comb

**Qualification of the earlier heading.** For $g\in C_c^\infty([-L,L])$ and the entire
$h$ defined in §4.1, the unconditional statement is

$$\mathcal Z(h):=\sum_\rho h(\gamma_\rho)
=P_{\mathrm{pole}}(g)+\frac1{2\pi}\int_\mathbb R h(t)\Psi_L(t)\,dt.$$

If an ordinate is nonreal, evaluation at it is a functional on entire tests, not a Dirac mass
on the real line. Thus $\mathcal Z$ cannot unconditionally be treated as a positive real
zero measure. Under RH it is represented by the positive locally finite real measure
$\sum_\rho\delta_{\gamma_\rho}$, and its action on these tests is nonnegative.
Conversely, nonnegativity for every admissible test and every support is Weil's criterion.

Even under RH, a literal pointwise sinc identity needs a specified projection and a
distributional prescription. The displayed symbol has an unfiltered digamma term, so it is
not automatically equal to its own low-pass projection. The exact equality above concerns
its action on the declared test class, including the pole term.

The functional equation supplies reflection symmetry, not the missing positivity.
An off-line quartet gives complex evaluation arguments and can produce a negative Weil
pairing. Describing all observed wells as Gibbs side-lobes of an unconditionally positive real
zero measure would already assume the desired zero location. The measured plots survive;
that proposed unconditional explanation does not.

## 4.4 Diggability: when can a band-limited function reach a well?

Treat a single dangerous well as a model: background $b$, depth $d$ below zero, width $w$,

$$\Psi(t) \approx b - (b + d)\, \exp\!\left( -\frac{(t - t_0)^2}{2w^2} \right).$$

The best a support-$L$ test function can do is place a **coherent-state / prolate** bump of
spectral width $\sigma_t \gtrsim c/L$ (the uncertainty floor) on the well. The Gaussian overlap
closes in form and gives a clean threshold for $Q = 0$:

$$L^* = \frac{c\, b}{w\, \sqrt{d(d + 2b)}}.$$

Deeper well → cracks earlier; wider well → cracks earlier; higher archimedean background → harder.
The single free constant $c = O(1)$ is fixed by calibrating on the one well whose answer is
known — Davenport–Heilbronn's off-line zero ([§4.5](#45-the-crossover-and-the-separator)).

Two honesties about this model:

- It is **optimistic**. It treats the well as isolated and ignores the rest of the symbol and
  the pole term. The measured threshold difference records the limitation of this model;
  §4.3 does not supply an unconditional theorem guaranteeing sufficient positive shoulders.
- For $\zeta$ and real-character controls the symbol is **even**, so $Q(f) = Q(\mathrm{Re}\, f) +
  Q(\mathrm{Im}\, f)$. Reflection also splits the real test space into even and odd sectors;
  either can contain the lowest direction, so both must be tested. For a complex character
  the form need not have these symmetries and the full complex test space is required.

## 4.5 The crossover, and the separator

The model is calibrated and sharpened by a two-sided control, both measured on the same instrument
([page 6](06-state-of-the-program.md)):

- **The off-line zero *is* the negative direction (Davenport–Heilbronn) — and it is a *barrier*,
  not a well.** The non-multiplicative control is positive at small support, then first goes
  **indefinite at $L^* = 4.4184$** (bisected). The census turned up the real picture: at $L^*$ the
  symbol *at the zero height* $85.699$ is $\Psi_L = +20.72$ — a **positive peak** — flanked by two
  wells at $84.5$ ($\Psi = -4.16$) and $86.75$ ($\Psi = -11.71$). The off-line zero sits on a
  barrier, and the near-null direction digs the **shoulders** of that barrier. The zero-side split
  is exact: at $L^*$ the on-line zeros contribute $+0.7699$ and the single off-line quartet at
  $85.699$ contributes $-0.76986$, the other four quartets $\le 3.7\times10^{-9}$ — **the entire
  negative eigenvalue is that one off-line quartet.** Move only it onto the line and the form is
  positive again. Fed the measured flanking wells, the model of
  [§4.4](#44-diggability-when-can-a-band-limited-function-reach-a-well) predicts $L^* \approx 3.1$–$3.7$
  against the true $4.4$ — it **over-predicts danger by ~20%**, exactly because it ignores the
  compensating shoulders.

- **The matched multiplicative partner stays positive ($L(s,\chi)$, $\chi \bmod 5$,
  $\chi(2) = i$).** Same conductor, same archimedean factor, same functional-equation shape as
  Davenport–Heilbronn, but with a different, multiplicative coefficient sequence. Under the
  identical instrument it stays positive-semidefinite across the whole tested range
  ($L = 0.4 \ldots 9$), collapsing-but-positive like $\zeta$, at every setting where its
  non-multiplicative twin cracks. This is a matched finite comparison, not a theorem of causal
  sufficiency for multiplicativity. Positivity on every admissible test, beyond the computed
  range, would itself be GRH-equivalent.

The mutation controls of [§6.2](06-state-of-the-program.md) test several distinct compatibilities.
For example, a nonunit local Euler amplitude can remain completely multiplicative. The
[arithmetic connection checkpoint](../research/aletheia_2026-10-09/arithmetic_poisson/README.md)
separates coefficient multiplicativity, local unitarity, the integer clock and completion.

## 4.6 Why the symbol face has no unconditional handle (yet)

Working the zero-free face does not escape RH-equivalence — but it reveals, precisely, *why* no
current tool reaches it:

- **Well depth is a large-deviation question, not a Diophantine-gap one.** A deep well needs only
  *partial* alignment — a constant fraction of the comb's weight at $O(1)$ phase precision — which
  is a large-deviation event timed by **measure** ($\sim 1/\text{probability}$), not by how small
  a prime phase-gap can get. Effective linear-forms-in-logarithms (Baker–Wüstholz, Matveev) are
  the **wrong tool**: the prime phase-forms are logs of rationals, so the elementary bound
  $\lvert \log(u/v)\rvert \ge 1/\max(u,v)$ already beats Baker, and gap bounds only bite near the
  doubly-exponential envelope ceiling, which the dangerous wells never reach. The honest model for
  well depth is the **random-phase (Farmer–Gonek–Hughes) statistics** of the comb — exactly the
  regime of [§4.4](#44-diggability-when-can-a-band-limited-function-reach-a-well).

- **The wells live in the Vinogradov–Korobov blind spot.** The well regime is
  $\log N \sim \log\log t$, nowhere near the range $\log N \gtrsim (\log t)^{2/3}$ where
  unconditional cancellation in $\sum \Lambda(n)\, n^{-it}$ is available. Large-value estimates are
  in the wrong regime too, and the mean-value theorems are $L^2$, not sup. So "no unconditional
  handle" is a **structural coverage gap of the whole field**, not a weakness of one method.

The net: the symbol face is the most explicit, most zero-free way to look at the obstruction — and
it shows the obstruction is the positivity of the zero measure itself, sitting precisely where
every unconditional tool is silent. That is a sharp map coordinate, not a way through.

---

**Next:** [What ζ is, from every side →](05-what-is-zeta-here.md) — the same object read through
each of the program's vantages at once, and why they are all one wall.
