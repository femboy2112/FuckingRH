# Integer-corner compression defects: the boundary is the successor's self-commutator

**Round 006. RH IS OPEN. Reproduce:** `scripts/r006_affine_corner.py` §2a, §3.

## 1. The additive defect is rank one

With `N = {1,2,3,...}`, the successor isometry `S` satisfies `S*S = I` but `SS* ≠ I`. The **cokernel**
is one-dimensional — the single state `|1>` that has no SUCC-preimage in `N` (its preimage `0` was deleted
in the compression `Q → N`):

    ┌───────────────────────────────────────────────┐
    │   E_S := I - S S*  =  |1><1|                    │   (verified exactly, ‖·‖=0)
    └───────────────────────────────────────────────┘

Equivalently, because `S*S = I`, the defect is the **self-commutator of the successor**:

    ┌───────────────────────────────────────────────┐
    │   [S*, S]  =  S*S - S S*  =  |1><1|  =  E_S      │
    └───────────────────────────────────────────────┘

So `S` is an isometry that fails to be normal by exactly one dimension, and that dimension is the deleted
`0`. In Fredholm language `index(S) = dim ker S* − dim ker S = 1 − 0 = 1`; the index is carried entirely
by `|1>`. (Finite windows also show a top atom `|N><N|` from `S*S` truncation; it dies as `N→∞` and is
not a genuine defect.)

This is the operator-theoretic meaning of "put the inverse instruction back": the boundary `|1>` is not an
arbitrary source vector — it is **forced** as the non-normality of the compressed successor. In earlier
rounds the multiplicative source `Ω=|1>` was posited; here it is *derived* as `E_S = [S*,S]`.

## 2. The multiplicative defects (the sieve)

For each prime `p`, `Q_p := V_p V_p*` is the projection onto multiples of `p`, and

    E_p := I - Q_p  =  Σ_{p∤n} |n><n|

projects onto integers **not** divisible by `p`: `E_p|n> ≠ 0 ⟺ n/p ∉ N ⟺` inverse-FUCC by `p` leaves the
corner. The elementary sieve is the family `{E_p}` of multiplicative compression defects. Unlike the
additive defect (rank 1), each `E_p` has infinite rank (density `1 − 1/p`).

## 3. Commutators with arithmetic support

Not every commutator is meaningful; the ones with clean arithmetic support are:

- `[Q_p, S] |n>` is supported exactly on the **divisibility boundaries mod p**: it is nonzero only when
  `n` and `n+1` straddle a multiple of `p` (i.e. `p | n` or `p | n+1`), since `Q_p` is diagonal in `n` and
  `S` shifts by one. `[Q_p,S] = Q_p S - S Q_p` has matrix elements `<m|[Q_p,S]|n> = (1_{p|m} - 1_{p|n})δ_{m,n+1}`,
  nonzero iff `p|(n+1)` xor `p|n` — a unit-width shell at each multiple of `p`.
- `V_p* E_S V_p = V_p* |1><1| V_p = 0` (since `V_p|...>` never hits `|1>` from the right unless acting on
  `|1/p>`, which is outside `N`): the additive boundary **does not survive pull-back** through a dilation.
- `V_p E_S V_p* = |p><p|`: the additive boundary **pushed forward** through `V_p` lands on `|p>`. This is
  the seed of the von Mangoldt identity (next note): transporting the single boundary `|1>` through every
  prime-power dilation tiles out exactly the prime powers.

The asymmetry between `V_p* E_S V_p = 0` (pull-back kills it) and `V_p E_S V_p* = |p><p|` (push-forward
transports it) is the whole mechanism: **the boundary propagates multiplicatively in the forward
direction only**, which is why the prime-power heads, not the fractions, are what the corner records.

## 4. Status

All identities here are exact and RH-inert *by themselves* (a diagonal/rank-one bookkeeping of the
compression `Q → N`). Their value is structural: they pin down **what the corner creates** — a single
additive boundary `|1>`, forced as `[S*,S]`, that the multiplicative group transports into the
prime-power skeleton. That transport is the content of the next note.
