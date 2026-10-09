# 2. The RH-equivalent target

*This page states the classical object the program aims at. Everything here is standard,
proved mathematics, cited to its authors. The frame of [page 1](01-the-successor-frame.md)
is a way of thinking about it; this is the thing itself.*

---

## 2.1 The completed zeta function

The Riemann zeta function $\zeta(s) = \sum n^{-s}$ (for $\mathrm{Re}\, s > 1$, continued
elsewhere) has an Euler product $\zeta(s) = \prod_p (1 - p^{-s})^{-1}$ that encodes unique
factorization. Its **completion** folds in the archimedean factor of
[§1.5](01-the-successor-frame.md):

$$\xi(s) = \tfrac12\, s(s-1)\, \pi^{-s/2}\, \Gamma(s/2)\, \zeta(s).$$

$\xi$ is entire, and satisfies the functional equation $\xi(s) = \xi(1-s)$ — the reflection
across the critical line $\mathrm{Re}\, s = \tfrac12$. Its zeros are exactly the **nontrivial**
zeros of $\zeta$ (the $\Gamma$-factor's poles cancel the trivial zeros at $s = -2, -4, \ldots$).

> **The Riemann Hypothesis.** Every zero of $\xi$ lies on the line $\mathrm{Re}\, s = \tfrac12$.

A crucial negative lesson the frame keeps front of mind: **the functional equation alone does
not imply RH.** The Davenport–Heilbronn function has a functional equation of the same shape and
a Dirichlet series, yet has zeros *off* the line. What $\xi$ has and Davenport–Heilbronn lacks is
the **Euler product** (multiplicativity). Any route to RH must use multiplicativity somewhere;
symmetry is not enough. (This is made quantitative on
[page 4, §4.5](04-the-symbol-and-the-wells.md): a matched pair — Davenport–Heilbronn and a
genuine $L(s,\chi)$ with matched conductor and $\Gamma$-factor — measurably separates into an
indefinite form and a positive finite form. This compares different coefficient systems;
it does not prove a sufficient sign theorem from multiplicativity.)

## 2.2 Weil's explicit formula: zeros ↔ primes

The explicit formula pairs a test function $f$ against the zeros and against the primes
simultaneously. Schematically, for a nice even $f$ with transform $\hat f$:

$$\underbrace{\sum_\rho \hat f(\gamma_\rho)}_{\text{zeros}}
= \underbrace{[\text{archimedean term in } f] + [\text{pole terms}] - \sum_{p,k} (\log p)\,
p^{-k/2}\, [f \text{ at } k\log p]}_{\text{arithmetic side: } \Gamma\text{-factor digamma} +
\text{ prime powers}}.$$

The left side is a sum over the zeros $\rho = \tfrac12 + i\gamma_\rho$; the right side is built
only from the archimedean $\Gamma$-data and the von Mangoldt prime powers of
[§1.3](01-the-successor-frame.md). The two sides are *equal* — this is a theorem (Guinand–Weil).
It is the exact bridge between the dynamics (primes) and the spectrum (zeros).

## 2.3 Weil positivity ⟺ RH

Apply the explicit formula to a self-correlation $f = g \star \tilde g$, where
$\tilde g(u)=\overline{g(-u)}$. With $F_g(z)=\int g(u)e^{izu}\,du$, its entire transform is
$F_g(z)\overline{F_g(\bar z)}$. The **Weil functional** is therefore

$$W(g) = \sum_\rho F_g(\gamma_\rho)\overline{F_g(\bar\gamma_\rho)},
\qquad \gamma_\rho=(\rho-1/2)/i.$$

For nonreal ordinates this is not a sum of modulus squares. The reflected pairing is
essential: see Lagarias, [*Li coefficients for automorphic L-functions*, §3 and Appendix A](https://www.numdam.org/item/10.5802/aif.2311.pdf),
and the [exact synthetic sign control](../research/aletheia_2026-10-09/arithmetic_poisson/FRONTIER_CORRECTIONS.md#5-complex-ordinates-require-the-reflected-autocorrelation).

Then:

> **Weil's criterion.** $W(g) \ge 0$ for all admissible $g$ $\iff$ RH.

The direction that matters: if all zeros are on the line, every $\gamma_\rho$ is real and the sum
of $\lvert \hat g(\gamma_\rho)\rvert^2$ is manifestly $\ge 0$; conversely a single off-line zero
produces an admissible $g$ making $W(g) < 0$. So **RH is exactly a positivity statement** — and
because the zero side equals the arithmetic side (prime + archimedean), proving RH means proving
that the *arithmetic* side is non-negative *without ever looking at the zeros*.

This is the whole game. The program's target is: **an independent, non-circular reason the
prime-plus-archimedean form is positive.**

## 2.4 Equivalent reformulations used in this repo

Several exact restatements are used interchangeably; each repackages the same positivity.

- **Suzuki (JLMS 2023).** There is an explicit even function $\Psi(t)$, built from prime powers
  plus the archimedean completion, with

  $$\mathrm{RH} \iff \Psi(t) \ge 0 \ \text{for all } t \iff \text{the Kreĭn screw kernel }
  K_\Psi(t,u) = \Psi(t) + \Psi(u) - \Psi(t-u) \succeq 0,$$

  and (Nakamura–Suzuki) $\iff e^{-\Psi}$ is an infinitely divisible characteristic function.

- **$\xi'/\xi$ positive-real (Lagarias 1999; Hinkkanen).**

  $$\mathrm{RH} \iff \xi'/\xi \ \text{is positive-real (Pick/Herglotz) on }
  H_{1/2} = \{\mathrm{Re}\, s > \tfrac12\}.$$

- **A refuted passivity coordinate (this repo, Round 006 — kept as a tombstone, not a
  reformulation).** It is tempting to also write $\mathrm{Re}\{\xi(s)/\xi(s+1)\} \ge 0$ on
  $H_{1/2}$. This is **not** RH-equivalent: it is a de Branges / Conrey–Li *sufficient* condition
  that is itself **false** — the ratio's real part goes negative inside the strip (e.g.
  $\mathrm{Re}\{\xi(1+282i)/\xi(2+282i)\} = -0.000132 < 0$; verified here). So it is a refuted
  route, never an equivalence; the genuine RH-equivalent passivity statement is the $\xi'/\xi$
  positive-real one above. (This is the correction to ledger row `C108`; see
  `CONSOLIDATED_RH_STATE.md` §6 and [§7.1](07-methodology-and-discipline.md).)

- **de Branges spaces (Lagarias; Suzuki).** Under RH the Weil-form Hilbert space is a de Branges
  space, and $E_h(z) = \xi(\tfrac12 + h - iz)$ is a de Branges structure function for every
  $h \ne 0$ iff RH. This is the natural "canonical system / string" home for the positivity — but
  the single-space version of the de Branges route is **known to fail** for $\zeta$ and for
  $L(s, \chi_{-4})$ (Conrey–Li), which is exactly why this program's live operator seam is a
  *second-jet, cross-place* coupling rather than a single-space contraction
  ([§5.4](05-what-is-zeta-here.md), [§6.4](06-state-of-the-program.md)).

These are **exact reformulations, not progress.** Moving between them reshapes the target; it
never reaches it. The variational form of the same object (Bombieri's Problems A/B — minimize
$Q(v)/\lVert v\rVert^2$ over a test space) is in the same boat: a minimizer exists, but bounding
it below zero *is* RH.

## 2.5 The free half, and the prime-free window

Two unconditional facts fix exactly how much is "for free" and how much is RH.

- **Above $\mathrm{Re}\, s = 1$ it is free.** The Euler product converges,
  $\log \zeta = \sum_{p,k} p^{-ks}/k$ has non-negative coefficients, and positivity
  ($\mathrm{Re}\,\xi'/\xi > 0$ on $\mathrm{Re}\, s > 1$; no zeros on $\mathrm{Re}\, s = 1$ by the
  classical $3 + 4\cos\theta + \cos 2\theta = 2(1+\cos\theta)^2 \ge 0$ argument) follows directly
  from multiplicativity. **All RH content is pushing positivity from $\mathrm{Re}\, s > 1$ down to
  $\mathrm{Re}\, s > \tfrac12$.**

- **The prime-free window (Connes–Consani, *Theorem 1*, arXiv:2006.13771).** Unconditional
  positivity of the Weil form is known for test functions whose self-correlation is supported in
  $(\tfrac12, 2)$ — the window in which *no prime power log appears* — via the Sonin space /
  Toeplitz (Thm 6.11) route (Yoshida). This is the refereed, classical frontier of what positivity
  is unconditionally available.

  > *Historical note / correction.* Earlier internal notes mislabeled this as "Theorem 7.1,
  > positivity at the archimedean place." That was wrong on both counts and was corrected on
  > 2026-10-08 against the paper: it is **Theorem 1**, and it is the **prime-free support window
  > $(\tfrac12, 2)$**, not an "archimedean place" statement. The error and its correction are
  > logged (this is the kind of citation slip the methodology is built to catch — see
  > [page 7](07-methodology-and-discipline.md)).

The gap between "free above $\mathrm{Re}\, s > 1$" and "known on $(\tfrac12, 2)$" and "RH" is
where every construction in this repo lives and dies.

---

**Next:** [The Diophantine & semigroup frame →](03-the-diophantine-semigroup-frame.md) — why the
obstruction is really about the prime *frequencies*, and the finite-window operator model that
gives it a rigorous home.
