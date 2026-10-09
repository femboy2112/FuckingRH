# 3. The Diophantine & semigroup frame

*This page is the program's current working picture of **where the difficulty actually
lives**. The operator constructions here are proved (and verified numerically in
`scripts/`); their *sufficiency for RH* is not — the whole point is that they reshape an
RH-equivalent target without yet discharging it.*

---

## 3.1 Prime-frequency independence and coefficient multiplicativity

Take logarithms of the prime powers. The explicit formula's arithmetic side is a sum of
oscillations at the **prime frequencies** $\{\log p\}$. The decisive structural fact:

> The numbers $\{\log 2, \log 3, \log 5, \ldots\}$ are **linearly independent over the
> rationals.**

This is just unique factorization written in the language of frequencies: a rational relation
$\sum a_p \log p = 0$ would say $\prod p^{a_p} = 1$ with not-all-zero integer exponents, which
unique factorization forbids. This is a fact about the integer frequencies. It is not equivalent
to multiplicativity of an arbitrary Dirichlet coefficient sequence: Davenport–Heilbronn uses
the same integer logarithms as a character $L$-function.

The coefficient discriminator is the connected source $b_a=(a\log)*a^{-1}$. Prime-power
support of $b_a$ is equivalent to ordinary coefficient multiplicativity. For a character,
$b_\chi=\chi\Lambda$; the normalized Davenport–Heilbronn sequence instead has
$b_D(6)=(1+\kappa^2)\log6\ne0$. These are exact identities from the
[integer incidence connection](../research/aletheia_2026-10-09/arithmetic_poisson/CONSTRUCTION.md#2-the-integer-incidence-connection).

## 3.2 The phases align — this is a theorem, not a hope

By the **Kronecker–Weyl equidistribution theorem**, $\mathbb{Q}$-independent frequencies drive
phases that fill out the torus: the vector of phases
$(t\log 2, t\log 3, \ldots, t\log p_N) \bmod 2\pi$ equidistributes as $t$ varies, and in
particular comes **arbitrarily close to full alignment** (all phases near $0$). Numerically, for
the first seven primes the comb $\sum \cos(t\log p)$ reaches $\approx 6.85/7$ near
$t \approx 63752$ — the phases really do conspire.

This corrects a tempting but false slogan ("RH is that the prime phases never align"). They *do*
align; that is forced. The Weil "symbol"

$$\Psi_L(t) = [\text{archimedean background}] - [\text{prime comb}](t)$$

has a large prime-comb contribution where the phases line up. A negative well occurs only
where that contribution also exceeds the archimedean background. For a fixed finite comb the
background grows like $\log|t|$, whereas the comb is bounded; alignment alone cannot force
negative wells at arbitrarily large height.

## 3.3 Why the wells are not (obviously) exploitable: the band-limit

A negative *pointwise* value of the symbol $\Psi_L(t)$ is **not** the same as a negative
*direction* of the quadratic form. The Weil form is

$$Q(f) = P_{\mathrm{pole}}(f)+\frac1{2\pi}\int \lvert \hat f(t)\rvert^2\, \Psi_L(t)\, dt,
\qquad \text{with } f \text{ supported in }
[-L, L].$$

The pole term is present for $\zeta$ and absent for primitive nontrivial characters. It is part
of the full sign problem and cannot be dropped in a general well comparison.

If $f$ is supported in a finite window of length $2L$, then $\hat f$ is **band-limited**: by the
uncertainty principle it cannot be concentrated inside a narrow well. It must average the well
against the positive background around it. So the question is never "does the symbol go negative?"
(it does) but "**can a finite-window $f$ place enough mass inside the wells to make $Q(f) < 0$?**"
— and that is a quantitative, falsifiable question about well width/density versus the band-limit
$1/L$.

This rehabilitates the frame's wavefront picture precisely: the **finite support $L$ is the
band-limit**, "positive for free, primes erode it, never crossing" becomes "positivity holds up to
support $L$ because the wells are too narrow for any support-$L$ function to resolve — until $L$
grows enough to resolve one." For $\zeta$ that never happens iff RH; for a non-multiplicative
control it happens exactly when its off-line zero comes into resolution (see the crossover on
[page 4](04-the-symbol-and-the-wells.md)).

How deep the wells actually get — and therefore how large $L$ must be to resolve one — turns out
to be a **large-deviation** question about the comb, not a question about how tightly the prime
phases can align. Partial alignment of a constant fraction of the comb's weight is enough to make
a deep well, and the first height at which that happens is set by *measure*, not by Diophantine
gaps. This is developed, with its consequences for what is unconditionally provable, in
[§4.6](04-the-symbol-and-the-wells.md).

## 3.4 The finite-window multiplicative semigroup

The band-limit intuition can be made into operator algebra. Work in $H_L = L^2([-L, L])$ and let
$T_a$ be the **log-shift** (rightward translation by $a$, zero-padded at the boundary). Then
multiplicativity becomes a **semigroup**:

$$T_{\log m}\, T_{\log n} = T_{\log mn}, \qquad T_a^\dagger = T_{-a}, \qquad
[T_a, T_a^\dagger] = \text{boundary operator}.$$

The composition law $T_{\log m}\, T_{\log n} = T_{\log mn}$ *is* $m\cdot n = mn$ realized as
operators — the $\bullet$ of [§1.2](01-the-successor-frame.md) made concrete. The adjoint reverses
the walk; the commutator is a pure **boundary term**, which gives the frame's "chirality" an honest
operational meaning (it is the failure of the shift to be unitary at the window edge).

Two facts (both verified exactly in `scripts/`):

- **Sum-of-squares identity.**

  $$I - \tfrac12(T_a + T_a^\dagger) = \tfrac12 (I - T_a)^\dagger(I - T_a) +
  \tfrac12 (I - T_a^\dagger T_a),$$

  a decomposition of the prime term into a *shift-gradient energy* plus a *boundary-loss energy*,
  both manifestly positive semidefinite. Multiplicativity's finite-window geometry **supplies
  positive energy**, rather than destroying it.

- **Nonalignment theorem.** The symmetric shift has largest eigenvalue

  $$\lambda_{\max}\!\left( \tfrac12(T_a + T_a^\dagger) \right) = \cos\!\left( \frac{\pi}{m+1}
  \right) < 1, \qquad m = \lceil 2L/a \rceil.$$

  Because $\cos(\pi/(m+1)) < 1$ strictly, **a finite-window $f$ cannot reach the full alignment**
  of [§3.2](#32-the-phases-align--this-is-a-theorem-not-a-hope). The band-limit is now a *theorem*,
  with a constant.

Summing the per-shift bound over the primes gives an integrated operator-norm bound $C_L$ on the
prime term that is strictly smaller than the worst-case pointwise comb mass $A_L$ (by
$\approx 45\%$ across the tested range). This is a genuine, unconditional buy-back of positivity.

## 3.5 What this reframe did and did not do

- **Did:** it replaced a wrong slogan ("multiplicativity is the enemy / the phases must not
  align") with a correct one — *do not abandon multiplicativity; stop demanding the wrong
  positivity from it.* Multiplicativity supplies a finite-window translation semigroup and a
  positive phase-defect energy. Chirality, shadow-succ, and the band-limit all acquire exact
  operator meanings.

- **Did not:** it did not prove RH, and it did not even clear the window method's known wall. The
  $C_L$ reduction is a crude operator-norm bound, not the tight cancellation RH needs. The missing
  object, now sharply named, is a **joint coercivity** coupling the prime semigroup's positive
  energy to the archimedean term with the correct boundary flux — and, as the measurements on
  [page 6](06-state-of-the-program.md) show, that coercivity is exactly RH-equivalent.

---

**Next:** [The symbol face and the wells →](04-the-symbol-and-the-wells.md) — the band-limited
symbol as an explicit, zero-free function, its exact action on entire tests and the qualified
real-zero-measure interpretation, and the diggability of its wells.
