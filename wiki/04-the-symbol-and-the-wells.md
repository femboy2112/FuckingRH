# 4. The symbol face and the wells

*This page develops the program's sharpest current vantage: the **band-limited symbol**. It is
where the prime side becomes an explicit, zero-free function you can plot — and where the exact
sense in which that function "secretly knows the zeros" becomes visible. The structural identity
of [§4.3](#43-the-wells-are-the-low-passed-zero-comb) is **[derived]** (from the Guinand–Weil
formula and the band-limited reduction, cross-checked against the calibrated instrument of
[page 6](06-state-of-the-program.md)); the quantitative well law of
[§4.4](#44-diggability-when-can-a-band-limited-function-reach-a-well) is a **model**, calibrated
on a known off-line zero.*

---

## 4.1 One form, two faces

Weil's explicit formula ([§2.2](02-the-rh-equivalent-target.md)) is an *identity*. Fed a
self-correlation $f = g \star \tilde g$ with $h = \lvert \hat g\rvert^2 \ge 0$, it reads the same
number two ways:

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

$$\Psi_L(t) = W_\infty(t) - P_L(t),$$

where

- $W_\infty(t) = \frac{1}{2\pi} \mathrm{Re}\,\psi(\tfrac14 + it/2) - \tfrac12 \log\pi$ (plus the
  pole contribution) is the **archimedean background** — a smooth, slowly *growing* positive
  density, $W_\infty(t) \sim \frac{1}{2\pi}\log(t/2\pi)$; and
- $P_L(t) = \sum_{n \le e^{2L}} \Lambda(n)\, n^{-1/2} \cdot 2\cos(t\log n)$ is the **finite prime
  comb** — a trigonometric polynomial whose frequencies are the prime-power logs $\log n$ of
  [§1.3](01-the-successor-frame.md), each weighted by the ray-incidence charge
  $\Lambda(n)\, n^{-1/2}$.

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

Here is the identity that explains why the zero-free symbol is nonetheless RH-pinned. For $g$
supported in $[-L, L]$, $h = \lvert \hat g\rvert^2$ is a non-negative Paley–Wiener function of
exponential type $2L$; by Fejér–Riesz every such $h$ is exactly a $\lvert \hat g\rvert^2$. The
explicit formula, read on this cone, says — **unconditionally** —

$$\frac{1}{2\pi}\Psi_L \;=\; \text{the } \mathrm{sinc}_{2L} \text{ low-pass of the zero measure }
\sum_\rho \delta_{\gamma_\rho} \quad (\text{minus the pole}).$$

That is: **$\Psi_L$ is not a separate "prime" object at all. It is the zero comb itself, viewed
through a band-limited window of resolution $1/2L$.** Its negative wells are the **Gibbs
side-lobes** of that low-passed comb — the ringing you always get when you low-pass a sum of
spikes.

The consequence is decisive:

> A positive band-limited $h$ pairs with the comb as $\langle h, \text{comb}\rangle =
> \sum_\rho h(\gamma_\rho) \ge 0$ **if and only if the zero measure is a positive measure on the
> real line** — i.e. **iff the zeros are real, iff RH.** The side-lobes are invisible to every
> positive band-limited $h$ *exactly when* RH holds.

So the compensation that keeps the wells from ever being "dug" is **not** the functional equation.
The functional equation buys only the evenness and the $\rho \leftrightarrow 1-\rho$ pairing of the
comb; an off-line quadruple is symmetric but *signed*. The thing that makes the dig always cancel
is **the positivity of the zero measure, which is RH itself.** (This corrects an earlier internal
framing that named the compensator as "symmetry"; the conclusion *symmetry $\ne$ positivity*
stands, but the mechanism is low-passed-comb positivity — logged 2026-10-09.)

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

- It is **optimistic**. It treats the well as isolated and ignores the compensating shoulders that
  [§4.3](#43-the-wells-are-the-low-passed-zero-comb) guarantees. The gap between the model's $L^*$
  and the *true* $\lambda_{\min}$ measured on the instrument **is** the compensation — i.e. it is
  the zero-measure positivity made quantitative.
- For $\zeta$ and real-character controls the symbol is **even**, so $Q(f) = Q(\mathrm{Re}\, f) +
  Q(\mathrm{Im}\, f)$ and the extremal direction is real/even (prolate-like — consistent with
  Suzuki's "one box test function per width already encodes RH,"
  [§2.4](02-the-rh-equivalent-target.md)). The **complex** near-degeneracy only appears for a
  **complex character** $L(s,\chi)$, whose symbol is not even; there the knife-edge lives in
  complex test-function space.

## 4.5 The crossover, and the separator

The model is calibrated and sharpened by a two-sided control, both measured on the same instrument
([page 6](06-state-of-the-program.md)):

- **The off-line zero *is* the negative direction (Davenport–Heilbronn).** The non-multiplicative
  control is positive at small support, then first goes **indefinite at support $L^* \approx 4$**.
  The entire negative eigenvalue is supplied by its single **off-line zero** at height $85.699$ —
  an **uncompensated well**, one whose shoulders do not close by exactly the amount an on-line zero
  would have supplied. Move only that zero onto the line and the form is positive again; the other
  off-line zeros contribute $\le 1.6\times10^{-6}$; a band with no off-line zero stays positive.
  Feeding this well's measured $(d, w, b)$ into the model fixes $c$ and reproduces
  $L^* \approx 4$.

- **The matched multiplicative partner stays positive ($L(s,\chi)$, $\chi \bmod 5$,
  $\chi(2) = i$).** Same conductor, same archimedean factor, same functional-equation shape as
  Davenport–Heilbronn, differing in **one** thing only — it carries an Euler product. Under the
  identical instrument it stays positive-semidefinite across the whole tested range
  ($L = 0.4 \ldots 9$), collapsing-but-positive like $\zeta$, at every setting where its
  non-multiplicative twin cracks. **One variable toggled, opposite outcome: multiplicativity is the
  operative separator** between a positive form and an indefinite one. (Caveat, pre-registered:
  $L(s,\chi)$ staying positive is *itself* GRH-equivalent — this measures the separator, not a
  mechanism, and not a brick.)

Together with the mutation controls of [§6.2](06-state-of-the-program.md), multiplicativity is
pinned as load-bearing for the sign **from both sides**: destroy it and the form cracks; keep it
against a matched twin and the form holds.

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
