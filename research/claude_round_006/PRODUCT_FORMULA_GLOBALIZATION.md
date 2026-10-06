# Product formula vs the bulk divergence: the balance does not cancel it

**Round 006. RH IS OPEN. Reproduce:** `scripts/r006_adelic_checks.py` (product formula verified exactly),
`scripts/r006_intersect_before_squaring.py` (the divergence returns). See `LITERATURE_INTERFACE.md §3`.

## The product formula (verified)

For `q ∈ Q^×`, the reciprocal local half-densities multiply to one across all places (verified exactly for
`q = 12, 50/7, 360/49, 210/143`):

    ┌───────────────────────────────┐
    │   ∏_v |q|_v = 1                 │        (|q|_p = p^{-v_p(q)}, |q|_∞ = |q|)
    └───────────────────────────────┘

So diagonal rational scaling on the adele ring `A_Q` is **globally measure-preserving**, while its local
components carry exactly the reciprocal half-density factors (`p^{-k/2}` at `p`, `p^{+k/2}` at `∞`). This is
the global face of `ADELIC_HALF_DENSITY.md`.

## The FORBIDDEN naive claim, and what is actually true

Round005 established (C98) that `Σ_p σ_p(ξ)` diverges for generic `ξ≠0`, and the divergence is **BULK**
(`~2√(e^L)`), not a duplicated DC mode. Therefore:

> **FORBIDDEN:** "the adelic product formula trivially cancels the divergent `Σ_p M_p`." The product formula
> balances **moduli** (a multiplicative identity `∏|q|_v=1`); it does **not** subtract the additive bulk
> energy `Σ_p M_p`. These are different operations on different objects.

The precise question (directive §14) is whether assembling the places in the globally unitary adelic
representation **before** taking local positive squares makes the completed energy finite:

    DEAD order:          Σ_v (B_v^* B_v)                         (diverges in bulk, C98)
    parent order:        (global completed B)^* (global completed B)   (does assembly cancel it?)

## The answer: no (and the `l²(N)` experiment already shows why)

The finite integer-corner version of exactly this "assemble before squaring" was run in
`INTERSECT_BEFORE_SQUARING.md`: with a **uniform** boundary the cross terms do not cancel the diagonal bulk
— they are a positive common mode that makes the total diverge *quadratically* (`~π(N)²`). The adelic
version inherits the same obstruction with the Archimedean place added:

- The diagonal `p=q` terms are the same divergent `Σ_p` (the product formula does not touch them — it is a
  statement about `∏`, not `Σ`).
- The cross terms (including prime × Archimedean) only cancel the bulk if they are **signed and
  prime-specific** — which is precisely the **Weil explicit formula**: `Σ_p (prime terms) − (Archimedean
  term) = Σ_γ (zero terms)`, where the Archimedean/`Γ`-contribution is the *analytic* renormalizer (the
  `−ζ'/ζ` pole and `Γ`-factor), not an algebraic modulus balance.

So the product formula is the **algebraic** balance of the places; the cancellation of the bulk divergence
is the **analytic** content of the functional equation (`FRACTIONAL_SUCC_GAMMA_INTERTWINER.md §G`:
group/measure completion ≠ analytic continuation). The adelic parent **repackages** the functional equation
/ Tate integral and stops exactly at the Weil positivity wall — the second horn of directive §13, confirmed.

> **No-go (C102).** The adelic product formula `∏_v|q|_v=1` is a modulus identity; it does not cancel the
> additive bulk divergence `Σ_p M_p`. Assembling before squaring reproduces the Weil explicit formula,
> whose prime+Archimedean cancellation is *analytic* (the pole/`Γ`-sector), and whose residual positivity
> is RH. The adelic completion lands on the Weil wall; it does not break it.
