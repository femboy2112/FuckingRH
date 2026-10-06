# Adelic half-density: where p^{-k/2} comes from (and why it is Tate, not new)

**Round 006. RH IS OPEN. Reproduce:** `scripts/r006_adelic_checks.py`. See `LITERATURE_INTERFACE.md §3`.

## The problem the counting measure cannot solve

The parent `l²(Q)` uses **counting measure**: `T_a, D_q` are permutations, and dilation by `q` has **no**
Jacobian. So `l²(Q)` by itself cannot explain the critical weight `p^{-k/2}` that Round004/005 found forced
(C90/C96). We do not hide this; the weight comes from passing to **local Haar geometry**, place by place.

## Local half-density (verified orientation)

On `L²(Q_v, dx_v)` the unitary dilation by `a` carries a square-root Jacobian:

    (U_a f)(x) = |a|_v^{-1/2} f(x/a),      ‖U_a f‖ = ‖f‖.

Verified on `L²(R)` (`scripts/r006_adelic_checks.py`): with exponent `1/2+ε`, `‖U_a f‖/‖f‖ = |a|^{-ε}`,
which is `1` **iff `ε=0`** — local unitarity selects the `1/2` power exactly (this is hostile control H;
any other weight is a non-isometry). For `a = p^k`:

    |p^k|_p = p^{-k}   ⟹  half-density |p^k|_p^{1/2} = p^{-k/2}      (p-adic place)
    |p^k|_∞ = p^{+k}   ⟹  half-density |p^k|_∞^{1/2} = p^{+k/2}      (real place, reciprocal)

So the **critical weight `p^{-k/2}` is the square-root of the local modulus** — exactly the Round005 memory
weight `r = p^{-1/2}` (`BILATERAL_SUCC_TOEPLITZ.md §3`), now sourced from the places rather than posited.

## What it is: Tate/Connes self-dual normalization — not a new mechanism

This is the **Tate self-dual Haar normalization**: making the idele-class / dilation action unitary on `L²`
is Connes' isometry `E(f)(g) = |g|^{1/2} Σ_{q∈k^×} f(qg)` (Connes 1999, `math/9811068`); the `|g|^{1/2}` is
"dictated by comparing measures." Our `p^{-k/2}` is that `|g|^{1/2}` at the prime places. The honest
consequence:

> The half-density explains **why `1/2`** (local unitarity / self-dual measure) but supplies **no new
> leverage**: it is the Archimedean/adelic normalization that encodes the functional-equation symmetry
> `s ↔ 1−s` centered at the self-dual point `Re s = 1/2`. Choosing `1/2+ε` would move the self-dual point
> (break the functional equation) *and* break local unitarity — so `1/2` is forced, but forcing `1/2` is
> not forcing RH.

The product-formula balance across places (`PRODUCT_FORMULA_GLOBALIZATION.md`) is the global shadow of these
reciprocal local half-densities. Both are exact and both are classical (Tate). The weight that looked
"critical" and mysterious in the integer corner is simply the local self-dual measure, place by place.
