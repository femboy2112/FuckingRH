# Euler admissibility: a finite exact closed-point-positivity certificate

**Date:** 2026-10-02 (Opus 4.8 campaign round). **Status:** theorem + implementation note.
The bound below was independently audited (an adversarial proof audit): the lower bound
is **approved and sharp**; the horizon corollary's conclusion is correct, with one
monotonicity sub-argument corrected (see §3). Implemented in
`smartalgebra/domains/curve_euler_admissibility.py`.

## 0. The object

Let `q` be an integer `>= 3` and `P(T) = prod_{i=1}^{2g}(1 - alpha_i T)` a degree-`2g`
polynomial with `P(0)=1` that is **pure** (`|alpha_i| = sqrt q`, decided exactly by the
interval-localizing PSD certificate) and (+)-self-dual. Its predicted Frobenius power
sums are `S_r = sum_i alpha_i^r` (`|S_r| <= 2g q^(r/2)`), predicted counts
`N_r = q^r + 1 - S_r`, and predicted **closed-point spectrum**

    B_n = (1/n) sum_{d | n} mu(d) N_(n/d).

For an actual curve, every `B_n` is a nonnegative integer. We call `P` **Euler-admissible**
(equivalently *closed-point positive*) when all `B_n >= 0`. This is **necessary** for `P`
to be a curve zeta numerator and is **not sufficient**: an admissible `P` is **not**
certified curve-realizable.

## 1. Purity does not imply Euler admissibility

The purity cone is strictly larger than the Euler-admissible cone. Two exact controls
over `q = 3` (recomputed independently from the polynomials, not from any curve):

* **Example A** (`g=2`): `P = (1 + 3T + 3T^2)^2 = 1 + 6T + 15T^2 + 18T^3 + 9T^4`. Both
  Frobenius-block traces are `-3`, inside `[-2 sqrt 3, 2 sqrt 3]`, so `P` is pure and
  (+)-self-dual. But `B_1 = 10`, `B_2 = -3`: **purity PASS, Euler FAIL**.
* **Example B** (`g=3`): trace values `(-3, -2, -2)` give
  `P = 1 + 7T + 25T^2 + 54T^3 + 75T^4 + 63T^5 + 27T^6`, again pure and self-dual. Here
  `B_1 = 11`, `B_2 = 0`, `B_3 = -1`: a *later* local obstruction after low-degree
  plausibility. **Purity PASS, Euler FAIL at degree 3.**

So a spectral-purity gate alone admits polynomials no curve can have.

## 2. The finite-tail bound (approved, sharp)

**Theorem.** For `q >= 3`, `g >= 1`, any Weil spectrum (`|alpha_i| = sqrt q`), and every
integer `n > 1`,

    n B_n >= q^n - (tau(n) - 1 + 2g) q^(n/2) - 2g (tau(n) - 1) q^(n/4).

*Proof.* `n B_n = sum_{d|n} mu(d) q^(n/d) + sum_{d|n} mu(d) - sum_{d|n} mu(d) S_(n/d)`.
The middle sum is `[n=1] = 0` for `n>1`. In the first sum the `d=1` term is `q^n`; each
`d>1` has `n/d <= n/2` (since `d>=2`), so the `tau(n)-1` remaining terms are each
`<= q^(n/2)` in absolute value. In the third sum the `d=1` term is `-S_n` with
`|S_n| <= 2g q^(n/2)`, and each `d>=2` has `|S_(n/d)| <= 2g q^(n/(2d)) <= 2g q^(n/4)`
(including the extreme `n/d = 1`). Taking worst-case signs over the two disjoint groups
and adding gives the bound. ∎

The constants are **sharp** — the bound is saturated at `n=2` (verified over thousands of
random conjugate-paired Weil spectra; the minimum slack is `0`, attained at `q=3, g=1,
n=2`). They cannot be shaved.

## 2.5 Integrality for all n (the integral Euler transform)

The tail bound of §2/§3 controls `B_n` as a **real** number: it shows `n B_n > 0` past the
horizon. By itself it does **not** show `B_n` is an **integer** there — the finite window
checks `n | sum_{d|n} mu(d) N_(n/d)` only for `n <= H`. The following elementary theorem
supplies integrality for *every* `n`, with no appeal to positivity.

**Theorem (integral Euler transform).** Every power series `F(T) in 1 + T Z[[T]]` has a
unique factorization

    F(T) = prod_{n>=1} (1 - T^n)^(-b_n),   every b_n in Z.

*Proof (coefficient induction).* `1 + T Z[[T]]` is a group under multiplication (the
inverse of an integer series with constant term `1` again has integer coefficients and
constant term `1`). Set `H_1 = F`. Suppose `b_1, ..., b_{n-1} in Z` are chosen so that
`H_n := F * prod_{m<n} (1 - T^m)^{b_m}` satisfies `H_n ≡ 1 (mod T^n)`. Then `H_n` has
integer coefficients and `[T^n] H_n =: b_n in Z`. Because `(1 - T^n)^{b_n} = 1 - b_n T^n +
O(T^{2n})` (closed-form binomial, integer coefficients for either sign of `b_n`),

    H_{n+1} := H_n * (1 - T^n)^{b_n} ≡ (1 + b_n T^n)(1 - b_n T^n) ≡ 1  (mod T^{n+1}),

and coefficients below `T^n` are untouched. So `b_n` is forced (it is the `T^n`
coefficient — uniqueness) and integral, and the induction continues. The partial products
converge `T`-adically to `F`. ∎

**Corollary (integrality of the closed-point spectrum).** For integer `q` and `P in Z[T]`
with `P(0)=1`, the zeta series `Z(T) = P(T) / ((1-T)(1-qT))` is a *product of integer
power series* (`P`, `(1-T)^{-1} = sum T^k`, `(1-qT)^{-1} = sum q^k T^k`), hence lies in
`1 + T Z[[T]]`. Its Euler-transform exponents are therefore integers for **all** `n`.
Those exponents are exactly `B_n = (1/n) sum_{d|n} mu(d) N_(n/d)` — because for a genuine
closed-point product `Z = prod_n (1 - T^n)^{-B_n}` the two agree by uniqueness, and the
same coefficient recursion computes both. Hence **`B_n in Z` for every `n`**, with no tail
argument.

This is `euler_transform_exponents` (the coefficient induction) and
`zeta_series_of_numerator` in `curve_euler_admissibility.py`. The test asserts it agrees
with the independent Mobius-inversion `closed_point_spectrum` on real curve numerators far
past the horizon — two blind paths to the same integers.

## 3. The computable horizon (integer form used in code)

The implementation uses the crude but clean divisor bound `tau(n) <= n` and
`q^(n/4) <= q^(n/2)` to collapse the bound to a single term:

    n B_n >= q^n - ((2g+1) n - 1) q^(n/2),

so **`n B_n > 0` whenever `q^n > ((2g+1) n - 1)^2`** (square the sufficient condition
`q^(n/2) > (2g+1)n - 1`, both sides positive).

**Horizon corollary.** Let `H(q, g)` be the least integer `n >= 2` with
`q^n > ((2g+1) n - 1)^2`. Then `B_n > 0` for every `n >= H`.

*Proof of permanence (integer ratio induction — no calculus).* Write `a = 2g+1 >= 3` and
`R(n) = (a n - 1)^2`. For `n >= 2`,

    R(n+1)/R(n) = (1 + a/(a n - 1))^2 <= (1 + a/(2a - 1))^2 <= (1 + 3/5)^2 = 2.56 < 3 <= q.

So if `q^n > R(n)` at some `n = H >= 2`, then `q^(n+1) = q * q^n > q * R(n) >= 3 R(n) >
R(n+1)`; by induction the inequality holds for all `n >= H`. ∎

This integer argument deliberately avoids the derivative-based monotonicity of the
`tau(n) <= 2 sqrt n` variant, whose naive form (`d/dn[q^(3n/4) - 8g sqrt n] > 0` for all
`n >= 4`) is **false for large g** — the audit flagged it. The correct repair there is
conditional monotonicity (`f' > 0 wherever the condition holds`); the integer form above
needs no such care because `q >= 3` dominates the fixed ratio `2.56` outright.

**Certificate.** The three ingredients combine with their roles kept explicit:

    integral Euler transform (§2.5)  =>  B_n integral for ALL n;
    purity tail theorem (§2/§3)      =>  B_n > 0 for all n > H;
    finite window (direct)           =>  B_n >= 0 for 1 <= n <= H.

Therefore

    purity  +  (B_n >= 0 for 1 <= n <= H)  =>  B_n >= 0 for all n,

where the integrality at `n > H` is *earned* by the Euler transform, not assumed. The
certificate runs the finite window `B_1, ..., B_H` as an exact integer computation (so
`ADMISSIBLE` is *demonstrated* for that specific `P`, not merely observed) and cites the
two theorems for the tail. Horizons are small: `H(3,1)=5, H(3,2)=7, H(3,3)=8, H(5,3)=5`.
The two controls of §1 fail inside the window — Example A at `n=2`, Example B at `n=3`.

## 4. Honest scope

* `ADMISSIBLE` means **closed-point positivity**, a *necessary* condition for a curve
  zeta numerator. It is **not** sufficient and does **not** certify that a curve with
  numerator `P` exists. The certificate never says "curve-realizable".
* The verdict is three-valued: `OUTSIDE_HYPOTHESIS` (not integer `q >= 3`, wrong degree,
  or not pure — the tail bound needs purity), `ADMISSIBLE`, `NOT_ADMISSIBLE` (a specific
  `B_n < 0` is exhibited).
* `|alpha_i| = sqrt q` (Weil) is an input, not reproved here. The triangle bound
  `|S_r| <= 2g q^(r/2)` uses only the moduli, so the argument is representation-agnostic
  and does not use primality of `q`.
* **`q = 2` is in scope** (§3 permanence split): the bound derivation never used `q >= 3`;
  only the permanence step did, and it is repaired for `q = 2` by the facts that the
  threshold fails at `n = 2` (so `H(2, g) >= 3`) and the ratio is `< (1+3/8)^2 = 1.89 < 2`
  for `n >= 3`. So the finite-tail theorem and the certificate cover every integer
  `q >= 2`. This is a statement about *polynomials* `P` only. It does **not** extend the
  `F_q(t)` local-square decomposition (`function_fields.py`) to characteristic 2 -- that
  module still correctly rejects `q = 2`, because its odd-residue square criterion is
  invalid there (a separate, unrelated scope).
