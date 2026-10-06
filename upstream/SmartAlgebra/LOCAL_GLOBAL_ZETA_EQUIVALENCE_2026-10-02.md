# Local/global zeta equivalence: why Route A and Route B compute the same P

**Date:** 2026-10-02 (Opus 4.8 campaign round). **Status:** classical theorem, stated and
proved; it is **not** a SmartAlgebra discovery. The value SmartAlgebra adds is *two
independent executable realizations* of this identity (`route_a_point_counts` and
`route_b_host_bound` share no construction code), which cross-check each other on every
curve of the finite family (`research/h009_family_sweep_2026-10-02/`).

> **The sweep validates the implementations; it does not prove the theorem.** The theorem
> is the mathematics below. The 162 (and 2500) agreeing curves are evidence that the *code*
> faithfully realizes it, not additional evidence for the *theorem*, which is unconditional.

References: Stichtenoth, *Algebraic Function Fields and Codes* (2nd ed.), III.3.7 (places of
a quadratic extension), V.1 (the zeta function of a function field); Rosen, *Number Theory
in Function Fields*, Ch. 5–7; Weil (the Riemann hypothesis for curves is cited, not reproved).

## 0. Setup

Let `q` be an odd prime power and `f in F_q[x]` monic, squarefree, of odd degree `2g + 1`.
`C: y^2 = f(x)` is a smooth projective geometrically connected curve of genus `g` over
`F_q` with one (rational, ramified) point at infinity. Its function field is the separable
quadratic extension

    K = F_0(sqrt f),   F_0 = F_q(x)   (the rational function field).

Because `f` is squarefree and `q` is odd, `sqrt f ∉ F_0` and `F_q` is algebraically closed in
`K`, so `K/F_q` is a function field of one variable with exact constant field `F_q`.

## 1. The places of K are exactly the decomposed base places

Every place `P` of `K` restricts to a unique place `v = P|_{F_0}` of `F_0`, and the places of
`K` are the disjoint union, over all places `v` of `F_0`, of the places above `v`. A place
`v` of `F_0` is either a monic irreducible `p(x)` (degree `d = deg p`, residue field
`F_{q^d}`) or the degree place `∞`. In the separable quadratic extension `K = F_0(sqrt f)`,
the decomposition of `v` is governed by `f` in the completion `(F_0)_v` (Stichtenoth III.3.7;
for odd residue characteristic the square class is *even valuation + square unit-residue*,
Hensel lifting the simple root of `X^2 - u`):

| case at `v` | `v(f)` | unit residue of `f` | places above `v` | degrees | local factor of `Z_K` |
|---|---|---|---|---|---|
| **RAMIFIED** | odd | — | one, `e = 2` | `deg P = d` | `(1 - T^d)^(-1)` |
| **SPLIT** | even | square | two, `e = f = 1` | `deg P = d` each | `(1 - T^d)^(-2)` |
| **INERT** | even | non-square | one, `f(P\|v) = 2` | `deg P = 2d` | `(1 - T^(2d))^(-1)` |

The three cases are exhaustive and exclusive. The place `∞` is handled identically with its
degree valuation; for an **odd**-degree model `v_∞(f) = -(2g+1)` is odd, so `∞` is ramified
of degree `1` (the single point at infinity). This is exactly the classification implemented
and self-verified by `function_fields.PlaceDecomposition`.

> **Even-degree models (H-010 extension, 2026-10-03).** §0 above fixes an *odd*-degree model
> (`deg f = 2g+1`), the case the 2026-10-02 sweep covered. The same classification applies
> verbatim to **even**-degree models (`deg f = 2g+2`), where `∞` is *unramified* — see the
> new **§7** below for the one line that changes (the infinity row) and why nothing else does.

## 2. Z_K factors as the base-place Euler product

The zeta function of the function field `K` (Rosen Thm 5.9; Stichtenoth V.1.3) is

    Z_K(T) = prod_{P place of K} (1 - T^(deg P))^(-1),   |T| < 1/q.

Group the product over `K`-places by the base place `v` they lie over and substitute the
degrees from §1:

    Z_K(T) = prod_{v place of F_0} L_v(T),
      L_v(T) = (1 - T^d)^(-2)   [v split, d = deg v],
             = (1 - T^d)^(-1)   [v ramified],
             = (1 - T^(2d))^(-1)[v inert].

This regrouping is an identity of formal power series (every `K`-place sits over exactly one
`v`), and it is precisely **Route B**: `route_b_host_bound` / `zeta_numerator_via_places`
multiply exactly these local factors, one per base place.

## 3. Z_K = Z_C (places of K are the closed points of C)

The closed points of the smooth projective model `C` are in canonical degree-preserving
bijection with the places of its function field `K` (a closed point is a Galois orbit of
geometric points; its degree is `[k(x):F_q]`, which is the residue degree of the
corresponding place). Hence

    Z_K(T) = prod_{closed x in C} (1 - T^(deg x))^(-1) = Z_C(T).

## 4. The same series is the exponential of the point counts

Taking the formal logarithm of the closed-point Euler product:

    log Z_C(T) = sum_{closed x} sum_{m>=1} T^(m deg x)/m
               = sum_{r>=1} (T^r / r) * sum_{deg x | r} deg x
               = sum_{r>=1} N_r T^r / r,

where `N_r = #C(F_{q^r}) = sum_{d | r} d B_d` (`B_d` = number of closed points of degree `d`;
an `F_{q^r}`-point is a geometric point fixed by `Frob^r`, i.e. one lying on a closed point
of degree dividing `r`). Therefore

    Z_C(T) = exp( sum_{r>=1} N_r T^r / r ).

This is **Route A**: `route_a_point_counts` forms `P` from `N_1, ..., N_{2g}` via Newton's
identities on this exponential (no functional equation inserted as construction data).

## 5. Both routes compute the same numerator P

By Weil (the rationality and Riemann hypothesis for curves, *cited*),

    Z_C(T) = P(T) / ((1 - T)(1 - qT)),   P in Z[T], deg P = 2g, P(0) = 1,

with the reciprocal roots of `P` of absolute value `sqrt q` (purity). Combining:

* **Route A** forms `P(T) = (1 - T)(1 - qT) * exp(sum_r N_r T^r / r)` (truncated to degree
  `2g`), from point counts alone.
* **Route B** forms `P(T) = (1 - T)(1 - qT) * prod_v L_v(T)` (truncated `mod T^(2g+1)`), from
  the base-place decomposition alone.

Steps 2–4 prove `prod_v L_v(T) = Z_C(T) = exp(sum_r N_r T^r / r)` as formal power series, so
the two expressions are `(1-T)(1-qT)` times the *same* series `Z_C`. **Hence Route A and
Route B compute the same `P(T)`.** ∎

### Truncation makes Route B a finite exact computation

`P` has degree `2g`, so everything is read `mod T^(2g+1)`. A base place `v` of degree `d > 2g`
contributes `L_v` whose lowest nontrivial term is `T^d` (split/ramified) or `T^(2d)` (inert),
each `>= T^(2g+1)`, so `L_v ≡ 1 (mod T^(2g+1))` and cannot affect any coefficient of `P`
(the truncation lemma, `LOCAL_ZETA.md`). Route B therefore enumerates only the finitely many
base places of degree `<= 2g`, plus `∞`, and the result is exact — this is the
`LocalAssemblyManifest`'s expected place set.

## 6. What this is and is not

* It **is** a classical identity (Weil/Stichtenoth/Rosen). Nothing here is new mathematics.
* Its **value** in SmartAlgebra is that the two sides are realized by two independent exact
  programs that never call each other, so their agreement on a curve is a genuine
  cross-implementation check (and host provenance is load-bearing on Route B, H-008/H-009).
* The family sweep (§7/§9) over all 162 curves `/F_3` (and 2500 `/F_5`) is a test of the
  *implementations* against this theorem, **not** a proof of the theorem and **not** a claim
  about any curve outside the enumerated finite family.
* Nothing here bears on the number-field Riemann hypothesis; Weil's RH for curves is an input.

## 7. Even-degree models: infinity unramified (H-010 extension, 2026-10-03)

**Status (unchanged):** still a *classical* identity (Weil / Stichtenoth / Rosen). H-010 adds
no new mathematics; it validates that the *same two independent programs* realize the identity
for even-degree models, where the infinity place behaves qualitatively differently.

### 7.1 The one line that changes

Let `f ∈ F_q[x]` be squarefree of **even** degree `2g+2` with leading coefficient `c ≠ 0`.
`C : y^2 = f(x)` is a smooth projective curve of genus `g = floor((deg f − 1)/2)`. Everything
in §§1–6 is stated for an arbitrary place `v` of `F_0 = F_q(x)` via `v(f)` and the unit-residue
square class — **including `∞`** — so the finite places are untouched. Only the infinity row of
the §1 table is re-read, through the *same* rule `v(f)` parity + unit-residue square class:

| model at `∞` | `v_∞(f) = −deg f` | leading-coeff square class | `∞` in `K` | local factor |
|---|---|---|---|---|
| **odd** `2g+1` | odd | — | RAMIFIED, `deg 1` | `(1 − T)^(−1)` |
| **even** `2g+2`, `c` a square in `F_q` | even | square | **SPLIT**, two deg-1 places | `(1 − T)^(−2)` |
| **even** `2g+2`, `c` a non-square in `F_q` | even | non-square | **INERT**, one deg-2 place | `(1 − T^2)^(−1)` |

Here the uniformizer at `∞` is `1/x` and the residue field is `F_q`; the unit residue of `f`
at `∞` is its leading coefficient `c`, so the square class *is* the square class of `c` in
`F_q`. This is the classical description of how `∞` decomposes in `F_q(x)(sqrt f)` for an
even-degree `f` (Stichtenoth III.3.7 applied at `∞`; the "imaginary" vs "real" quadratic
function-field dichotomy — odd degree gives the ramified/imaginary model, even degree with
square leading coefficient the split/real model).

### 7.2 Why §§2–6 carry over unchanged

- **§1 classification:** the SPLIT / INERT / RAMIFIED trichotomy is derived from `v(f)` and the
  unit-residue square class for *every* place uniformly; the infinity row is not special-cased,
  so `function_fields.place_decomposition` already produces the even-degree infinity fiber with
  no code change (verified: odd quintic → RAMIFIED, even sextic `c` square → SPLIT, `c`
  non-square → INERT).
- **§2 Euler product:** the regrouping `Z_K = ∏_v L_v` is a formal-series identity independent
  of parity; the infinity factor is now `(1−T)^(−2)` (split) or `(1−T^2)^(−1)` (inert) instead
  of `(1−T)^(−1)`.
- **§3 `Z_K = Z_C`, §4 point-count exponential, §5 both routes:** unchanged — they never used
  the parity of `deg f`, only that `C` is a smooth projective curve of genus `g` with function
  field `K`. `P` still has degree `2g`, so the §5 truncation `mod T^(2g+1)` and the
  `LocalAssemblyManifest` place set are identical.

### 7.3 Point counts at infinity (Route A side)

Route A sees the same decomposition through the *projective* point count. Over `F_(q^r)` the
number of points of `C` at infinity is the number of `F_(q^r)`-points above `∞`, which equals
the number of square roots of the leading coefficient `c` in `F_(q^r)`:

- **odd** degree: `∞` is a single rational (ramified) point — `+1` over every `F_(q^r)`;
- **even** degree: `+2` iff `c` is a square in `F_(q^r)`, else `+0`. For `c` a square in `F_q`
  this is `+2` for all `r` (SPLIT: `[2,2,2,…]`); for `c` a non-square in `F_q` it is `+2`
  exactly when `r` is even (INERT: the degree-2 place contributes only over even extensions,
  `[0,2,0,2,…]`). This is computed exactly in `F_(q^r)` by
  `finite_fields.points_at_infinity` and matches the Route-B local factor term-by-term.

### 7.4 The cleanest instance of "same host, different fiber"

This is the sharpest example of the host/fiber separation the architecture is built on: the
**host** is the completion at `∞` (identical object for odd and even models), while the **fiber**
— the decomposition of that host in `K` — is RAMIFIED, SPLIT, or INERT according to the
*mathematical object* `f`, not the host. The host must not, and does not, encode the
decomposition; the fiber does. The H-010 even-degree sweep (`research/h010_even_degree_2026-10-03/`)
is the exhaustive software validation that both independent routes agree across this regime.
