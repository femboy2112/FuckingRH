# Inverse-FUCC survival depth = p-adic valuation = carry depth

**Round 006. RH IS OPEN. Reproduce:** `scripts/r006_affine_corner.py` §7 (verified for `p∈{2,3,5}`, all `n≤120`).

## 1. Survival depth

The compressed inverse dilation is `V_p*|n> = |n/p>` if `p|n`, else `0`. Iterating it runs the integer down
its `p`-tower until the orbit escapes the corner `N`:

    ┌─────────────────────────────────────────────────────┐
    │   v_p(n)  =  max{ k ≥ 0 :  (V_p*)^k |n>  ≠  0 }        │
    └─────────────────────────────────────────────────────┘

i.e. the **survival depth** of the inverse-FUCC orbit equals the `p`-adic valuation. For `n = p^k`:

    p^k  ⟶  p^{k-1}  ⟶ … ⟶  p  ⟶  1   (survives exactly k inverse-FUCC steps)

and the next state `1/p` exists **upstairs in `Q`** but not in the shadow `N` — the orbit falls off the
corner precisely when the valuation is exhausted.

## 2. Two readings of the same integer, now identified

| picture | quantity | realized as |
|---|---|---|
| Round005 carry machine | **carry depth** of `n` under SUCC in base `p` | records of `[R_p(N)−R_p(N−1)]` (C96) |
| Round006 compression | **inverse-FUCC survival depth** of `n` | `max{k:(V_p*)^k|n>≠0}` |

Both equal `v_p(n)`. The identification is exact: the carry-depth record that Round005 read off the
successor's base-`p` carries is the same number as the number of times the compressed inverse dilation
`V_p*` can act before leaving `N`. Hence:

> **Carry depth = inverse-FUCC survival depth = `v_p(n)`.** The Round005 statement "carry-depth records
> give von Mangoldt" (`Σ_p log p·[R_p(N)−R_p(N−1)] = Λ(N)`, C96) is the *occupancy–head* pairing of this
> note with the previous two: summing the per-prime valuations over a boundary gives `Λ`
> (`VON_MANGOLDT_AS_SUCC_BOUNDARY.md`), summing the full occupancy gives `log n`
> (`PRIME_JET_STRATIFICATION.md §2`), and the increment of occupancy as `N` crosses a prime power is `log p`.

## 3. Group-completing the prime depth

Round005 prime towers were one-sided `1, p, p², …`. Inverse FUCC completes each to a **bilateral** tower

    …, p^{-2}, p^{-1}, 1, p, p², …        (depth k ∈ Z, on log-time k·log p)

The depth shift becomes a genuine *unitary* `U_p` (bilateral shift on `Z`) upstairs. Two observations:

1. **The half-density weight is not symmetrized by bilateralization.** The Round005 memory resolvent
   `(I − p^{-1/2} U_depth)^{-1} = Σ_{k≥0} p^{-k/2} U_depth^k` is **causal** (`k≥0`): the Neumann series
   converges because `‖p^{-1/2}U_depth‖ = p^{-1/2} < 1`, and this one-sidedness persists on the bilateral
   carrier (the series still runs `k≥0`). So the geometric depth-memory is an *analytic/Hardy* object even
   on `Z`; bilateralizing the depth does **not** make it a two-sided symmetric operator. This is the depth
   analogue of the Toeplitz/Hardy finding in `BILATERAL_SUCC_TOEPLITZ.md` §3.
2. **The boundary that creates `Λ` is additive, not multiplicative.** Completing the prime depth to `Z`
   (making `U_p` unitary) does *not* remove the von-Mangoldt structure — that structure came from the
   **additive** boundary `E_S = I − SS*`, which only vanishes when the *successor* is bilateralized
   (`N→Z`), not when the *depth* is. The two completions are independent (see `HOSTILE_CONTROLS.md`,
   controls A/B and §15's three "negatives"). Keeping them distinct is essential: `Λ` dies under additive
   bilateralization, survives multiplicative-depth bilateralization.

## 4. Status

Exact and RH-inert. The valuation/survival identity is the cleanest statement of "divisibility is a
compression defect," and it reconciles the carry-depth and inverse-FUCC pictures into one integer. It
feeds the completions program (`ADELIC_HALF_DENSITY.md`) by telling us *which* completion touches `Λ`
(additive) and which only reshapes the memory (multiplicative depth).
