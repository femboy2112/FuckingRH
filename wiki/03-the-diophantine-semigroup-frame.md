# 3. The Diophantine & semigroup frame

*This page is the program's current working picture of **where the difficulty actually
lives**. The operator constructions here are proved (and verified numerically in
`scripts/`); their *sufficiency for RH* is not — the whole point is that they reshape an
RH-equivalent target without yet discharging it.*

---

## 3.1 The real content of multiplicativity: independent frequencies

Take logarithms of the prime powers. The explicit formula's arithmetic side is a sum of
oscillations at the **prime frequencies** `{log p}`. The decisive structural fact:

> The numbers `{log 2, log 3, log 5, …}` are **linearly independent over the rationals.**

This is just unique factorization written in the language of frequencies: a rational relation
`Σ a_p log p = 0` would say `∏ p^{a_p} = 1` with not-all-zero integer exponents, which unique
factorization forbids. So *multiplicativity = ℚ-independence of the prime frequencies.* This
is the frequency-domain form of the Euler product, and it is exactly what Davenport–Heilbronn
lacks.

## 3.2 The phases align — this is a theorem, not a hope

By the **Kronecker–Weyl equidistribution theorem**, ℚ-independent frequencies drive phases
that fill out the torus: the vector of phases `(t·log 2, t·log 3, …, t·log p_N) mod 2π`
equidistributes as `t` varies, and in particular comes **arbitrarily close to full
alignment** (all phases near `0`). Numerically, for the first seven primes the comb
`Σ cos(t·log p)` reaches `≈ 6.85 / 7` near `t ≈ 63752` — the phases really do conspire.

This corrects a tempting but false slogan ("RH is that the prime phases never align"). They
*do* align; that is forced. The Weil "symbol"

```
Ψ_L(t) = [archimedean background] − [prime comb](t)
```

therefore has genuine **negative wells** wherever the phases line up. The wells are real, and
multiplicativity (via ℚ-independence) sets their positions and density.

## 3.3 Why the wells are not (obviously) exploitable: the band-limit

A negative *pointwise* value of the symbol `Ψ_L(t)` is **not** the same as a negative
*direction* of the quadratic form. The Weil form is

```
Q(f) = ∫ |f̂(t)|² Ψ_L(t) dt,     with f supported in [-L, L].
```

If `f` is supported in a finite window of length `2L`, then `f̂` is **band-limited**: by the
uncertainty principle it cannot be concentrated inside a narrow well. It must average the
well against the positive background around it. So the question is never "does the symbol go
negative?" (it does) but "**can a finite-window `f` place enough mass inside the wells to make
`Q(f) < 0`?**" — and that is a quantitative, falsifiable question about well width/density
versus the band-limit `1/L`.

This rehabilitates the frame's wavefront picture precisely: the **finite support `L` is the
band-limit**, "positive for free, primes erode it, never crossing" becomes "positivity holds
up to support `L` because the wells are too narrow for any support-`L` function to resolve —
until `L` grows enough to resolve one." For `ζ` that never happens iff RH; for a
non-multiplicative control it happens exactly when its off-line zero comes into resolution
(see the crossover on [page 4](04-state-of-the-program.md)).

## 3.4 The finite-window multiplicative semigroup

The band-limit intuition can be made into operator algebra. Work in `H_L = L²([-L, L])` and
let `T_a` be the **log-shift** (rightward translation by `a`, zero-padded at the boundary).
Then multiplicativity becomes a **semigroup**:

```
T_{log m} T_{log n} = T_{log mn},      T_a† = T_{-a},      [T_a, T_a†] = boundary operator.
```

The composition law `T_{log m} T_{log n} = T_{log mn}` *is* `m·n = mn` realized as operators —
the `●` of [§1.2](01-the-successor-frame.md) made concrete. The adjoint reverses the walk;
the commutator is a pure **boundary term**, which gives the frame's "chirality" an honest
operational meaning (it is the failure of the shift to be unitary at the window edge).

Two facts (both verified exactly in `scripts/`):

- **Sum-of-squares identity.**

  ```
  I − (T_a + T_a†)/2  =  ½ (I − T_a)†(I − T_a)  +  ½ (I − T_a† T_a),
  ```

  a decomposition of the prime term into a *shift-gradient energy* plus a *boundary-loss
  energy*, both manifestly positive semidefinite. Multiplicativity's finite-window geometry
  **supplies positive energy**, rather than destroying it.

- **Nonalignment theorem.** The symmetric shift has largest eigenvalue

  ```
  λ_max( (T_a + T_a†)/2 )  =  cos( π / (m+1) ) < 1,     m = ⌈2L / a⌉.
  ```

  Because `cos(π/(m+1)) < 1` strictly, **a finite-window `f` cannot reach the full
  alignment** of [§3.2](#32-the-phases-align--this-is-a-theorem-not-a-hope). The band-limit is
  now a *theorem*, with a constant.

Summing the per-shift bound over the primes gives an integrated operator-norm bound `C_L` on
the prime term that is strictly smaller than the worst-case pointwise comb mass `A_L` (by
`≈ 45%` across the tested range). This is a genuine, unconditional buy-back of positivity.

## 3.5 What this reframe did and did not do

- **Did:** it replaced a wrong slogan ("multiplicativity is the enemy / the phases must not
  align") with a correct one — *do not abandon multiplicativity; stop demanding the wrong
  positivity from it.* Multiplicativity supplies a finite-window translation semigroup and a
  positive phase-defect energy. Chirality, shadow-succ, and the band-limit all acquire exact
  operator meanings.

- **Did not:** it did not prove RH, and it did not even clear the window method's known wall.
  The `C_L` reduction is a crude operator-norm bound, not the tight cancellation RH needs. The
  missing object, now sharply named, is a **joint coercivity** coupling the prime semigroup's
  positive energy to the archimedean term with the correct boundary flux — and, as the
  measurements on [page 4](04-state-of-the-program.md) show, that coercivity is exactly
  RH-equivalent.

---

**Next:** [State of the program →](04-state-of-the-program.md) — what the calibrated
numerical instrument actually measured, and why it confirms the geometry while leaving the
theorem untouched.
