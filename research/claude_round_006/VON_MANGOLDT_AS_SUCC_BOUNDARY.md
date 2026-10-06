# Von Mangoldt is the transported successor boundary  (clean exposition — it is Bost–Connes)

**Round 006. RH IS OPEN. Reproduce:** `scripts/r006_affine_corner.py` §4 (verified exactly: `max|diag−Λ|=0`,
off-diagonal `=0`, window N=120, **no zeta zeros used**).

> **PRIORITY / HONESTY (read first).** A primary-source check (`LITERATURE_INTERFACE.md`) establishes that
> this identity is a **novel framing of a trivial fact**, not a new theorem. The operators here are
> **Bost–Connes**: `V_p` are the BC multiplicative isometries `μ_p`, `|1>` is the BC vacuum,
> `H_log = log n` is the BC Hamiltonian, and `Σ(log p)|p^k><p^k|` is just the diagonal von Mangoldt
> operator — the geometric side of the Connes–Weil explicit formula. The *transport*
> `V_{p^k}|1><1|V_{p^k}* = |p^k><p^k|` is one line from `V_{p^k}|1>=|p^k>`, holding **only** because we put
> the additive boundary on the multiplicative unit (the exclude-0 convention, `§3`/`LITERATURE_INTERFACE`).
> Present what follows as *exposition with explicit priority to BC95 / Cuntz 2008 / Connes 1999* — the
> clean "what the corner creates" story — and **not** as progress toward RH. It is RH-inert (`§Status`).

## The identity

Take the additive compression boundary `E_S = I − SS* = |1><1| = [S*,S]` (see `INTEGER_CORNER_DEFECTS.md`)
and transport it through every prime-power dilation `V_{p^k}`:

    ┌──────────────────────────────────────────────────────────────────────┐
    │   Λ_op  :=  Σ_{p prime} Σ_{k≥1} (log p) · V_{p^k} (I − SS*) V_{p^k}*    │
    │                                                                        │
    │         =  Σ_{p,k} (log p) |p^k><p^k|   =   diag( Λ(n) )                │
    └──────────────────────────────────────────────────────────────────────┘

so `Λ_op |n> = Λ(n) |n>`, the **von Mangoldt operator**. The proof is one line:

    V_{p^k} E_S V_{p^k}*  =  V_{p^k} |1><1| V_{p^k}*  =  |p^k><p^k|       (since V_{p^k}|1> = |p^k>),

and `Σ_{p,k}(log p)|p^k><p^k|` is diagonal with entry at `|n>` equal to `Σ_{p^k=n} log p = Λ(n)`
(`= log p` if `n` is a prime power `p^k`, else `0`). ∎

## What it says

Read it structurally:

- The **successor** `S` supplies a single universal boundary — its self-commutator `[S*,S] = |1><1|`, the
  one dimension lost when `0` was deleted from the additive backbone.
- The **multiplicative group** `{V_{p^k}}` carries that *same* boundary form onto every prime-power site.
- The **heads** `|p^k>` are its images; `Λ` is just the weighted tally of those heads.

> **Von Mangoldt = the successor's index defect `|1><1|`, dilated over all prime powers.**
> The prime-power event measure is the SUCC boundary transported through every FUCC depth — exactly the
> "stratified geometry" picture: SUCC gives the universal boundary form, FUCC attaches it to each prime jet.

This *derives* the source wiring that earlier rounds posited (`Ω = |1>`, `Λ(n) = Σ log p ⟨n|V_{p^k}Ω⟩`):
the source `Ω` is not chosen, it is `E_S = [S*,S]`.

## Heads vs. occupancy

The same prime sheets carry two different diagonal observables, distinguished by **what sits at the bottom
of each sheet**:

| operator | bottom insert | result | meaning |
|---|---|---|---|
| `Σ (log p) V_{p^k} E_S V_{p^k}*` | boundary `|1><1|` | `Λ(n)` | **heads** — prime-power sites only |
| `Σ (log p) V_{p^k} I   V_{p^k}*` | identity (full sheet) | `log n` | **occupancy** — every multiple of `p^k` |

(The second is `H_log`; see `PRIME_JET_STRATIFICATION.md`.) They are tied by the classical divisor relation,
verified here as an operator fact: `log n = Σ_{d|n} Λ(d)` (§5b). So **occupancy = divisor-sum of the
transported heads**: `H_log = ζ-style summation of Λ_op over the divisibility order`. The head is the
"primitive" (`Λ = μ * log`), the occupancy its antiderivative along divisibility.

## Honest status (RH-inert)

`Λ_op` is a **diagonal** operator; by itself it is RH-inert (it is just the prime side written cleanly). It
does **not** move RH. Its force is twofold and purely structural:

1. It **forces the source**: the boundary is `[S*,S]`, not a free parameter. Any construction built on the
   source vector `|1>` is thereby pinned to the compression geometry.
2. It **localizes RH-relevance away from itself**: the ablation to `Z` (`HOSTILE_CONTROLS.md`, control A/B)
   shows that on `l²(Z)` the successor becomes the *unitary* bilateral shift `U`, so `E_S = I − UU* = 0`,
   and therefore **`Λ_op ≡ 0` on `Z`**. The entire von-Mangoldt/prime signature is a *compression
   artifact of the deleted `0`*. RH does not live in `Λ_op`; it lives in how `Λ_op` is **squared and
   completed against the Archimedean place** (see `GLOBAL_AFFINE_FACTOR.md`, `PROOF_ATTEMPT_006.md`).

That second point is the deranged-but-true gem of this round: *the primes' additive signature `Λ` exists
only because we sawed `0` off the bottom of the number line.* It is real, exact, and still RH-inert — a
sharper statement of where the wall is **not**.
