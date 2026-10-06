# Prime-jet stratification: SUCC is diagonal in the geometry, not in the N-shadow

**Round 006. RH IS OPEN. Reproduce:** `scripts/r006_affine_corner.py` §5, §5b, §6.

## 1. The stratified geometry

For each prime `p` and depth `k ≥ 1` give a copy of the SUCC backbone `H_{p,k} ≅ l²(N)` and embed it into
the integer shadow by the **shadow map**

    Π_{p,k} |m> = |p^k m>,          image(Π_{p,k}) = p^k·N.

Put the *same* abstract successor `S̃|m> = |m+1>` on every sheet. Then the unit step on a sheet appears
downstairs as a **displacement by `p^k`** (verified §6 for `(p,k) ∈ {2^1,2^2,2^3,3^1,3^2,5,7,11}`):

    ┌─────────────────────────────────────────────────┐
    │   Π_{p,k} S̃  =  S^{p^k} Π_{p,k}                   │
    └─────────────────────────────────────────────────┘

This is the precise sense of the user's proposal: **SUCC is diagonal on the basis on which the geometry is
built** (one universal unit step per sheet), while in the `N`-shadow that same step reads as the
prime-dependent displacement `p^k`. It is *not* diagonal in `N`. The vertical prime-depth shift
`F_p|p,k,m> = |p,k+1,m>` has shadow `Π F_p = V_p Π`.

The grid:

        horizontal  =  SUCC            (unit step on each sheet)
        vertical    =  prime depth / FUCC   (p ↦ p^{k+1})
        shadow      =  p^k m  in  N

This is exactly the Round005 affine braid `V_m S = S^m V_m` (C94/C97), displayed as a sheet geometry
rather than a relation. No new positivity yet — it is a *change of coordinates* on the same
non-commutative core.

## 2. Occupancy = log n

Let `Q_{p,k} = V_{p^k} V_{p^k}*` project onto multiples of `p^k`, so `Q_{p,k}|n> = 1_{p^k|n}|n>`. Then
(verified §5, `max|diag − log n| = 9e-16`):

    ┌─────────────────────────────────────────────────────────┐
    │   H_log := Σ_{p,k≥1} (log p) Q_{p,k}  =  diag( log n )     │
    └─────────────────────────────────────────────────────────┘

because `Σ_{k≥1} 1_{p^k|n} = v_p(n)` and `Σ_p v_p(n) log p = log n`. So **`log n` is total prime-jet
occupancy**: how many prime-power sheets the integer `n` sits on, weighted by `log p`.

Pairing with the previous note: the **heads** of these sheets (bottom insert `E_S`) give `Λ(n)`; the
**full occupancy** (bottom insert `I`) gives `log n`; and `log n = Σ_{d|n} Λ(d)` ties them (verified §5b).

`H_log` is the natural **Hamiltonian** of the picture: `e^{−β H_log}|n> = n^{−β}|n>`, so
`Tr e^{−β H_log} = Σ_n n^{−β} = ζ(β)` (for `β>1`). This is the Bost–Connes Hamiltonian in these coordinates
(see literature note); `Λ_op = −∂_β`-style weight on the same sheets. Diagonal, hence RH-inert alone.

## 3. Prime powers are diagonal intersections

Two proper-time clocks live on the geometry:

    τ_N(n) = log n          (global SUCC proper time = occupancy)
    τ_p(k) = k log p        (prime-depth proper time on sheet p)

and they **coincide exactly on the prime powers**:

    ┌───────────────────────────────────────────┐
    │   τ_N(n) = τ_p(k)   ⟺   n = p^k            │
    │   i.e.   log n = k log p                   │
    └───────────────────────────────────────────┘

So prime powers are the **diagonal intersections** `log n = k log p` of the global clock with the
prime-depth clocks. This dovetails with the transported-boundary identity
`V_{p^k} E_S V_{p^k}* = |p^k><p^k|`: the head of sheet `(p,k)` sits exactly where the two clocks cross.
`Λ_op` is the weighted incidence operator of these crossings.

## 4. Sheet intersections and the hostile warning

For distinct primes, `p^k·N ∩ q^l·N = p^k q^l·N`, so composite arithmetic is literally the **intersection
geometry** of prime strata. The overlap operator is `Π_{p,k}* Π_{q,l} = V_{p^k}* V_{q^l}` (§9): a clean
coprime shuffle `m ↦ q^l m / p^k`, verified to be the **GCD/factorized** kernel — which Round004 (C81,
C88, C89) already proved **RH-inert**.

> **Do not rediscover the GCD kernel.** The Round006 test is whether applying the universal boundary
> `(I−S)` on each sheet **before** intersecting (`INTERSECT_BEFORE_SQUARING.md`) escapes the factorization,
> or whether the dressed overlaps still collapse to GCD-inert. That is the live computational question;
> the stratification above is only the stage on which it is asked.
