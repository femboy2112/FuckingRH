# The rational affine parent and the integer corner

**Round 006. Branch `claude/inverse-affine-completion-006` (from Round005 head `3222f97`). RH IS OPEN.**
**Reproduce:** `scripts/r006_affine_corner.py` (all identities below verified exactly, window N=120, no zeta zeros).

## 0. The hypothesis under test

The positive integers may be only a **compressed / positive-integral shadow** of a larger *invertible*
affine geometry. Downstairs the primitive operations are semigroup isometries

    SUCC:   n -> n+1          (additive unit step)
    FUCC_p: n -> p n          (multiplicative prime step)

Their true inverses fail *at the boundary of* `N`: `SUCC^{-1}(1)=0 ∉ N`, and `FUCC_p^{-1}(n)=n/p ∉ N`
whenever `p ∤ n`. The research bet: **arithmetic defects downstairs are compression defects of
perfectly invertible symmetries upstairs.** We test it brutally. It is not assumed to solve RH.

## 1. The parent on `l²(Q)` (exact, verified)

`H_Q = l²(Q)`. For `a ∈ Q`, `q ∈ Q^×`:

    T_a |x> = |x+a>        (translation)
    D_q |x> = |q x>        (dilation)

Both are **unitary permutation operators** (`T_a`, `D_q` permute the basis `{|x> : x∈Q}`). The group laws
and the **affine braid** hold exactly (verified on 2000 random rationals, `scripts/r006_affine_corner.py` §1):

    T_a T_b = T_{a+b},     D_q D_r = D_{qr},
    ┌─────────────────────────────────────────────┐
    │   D_q T_a D_q^{-1} = T_{q a}                  │   (the ax+b / affine relation)
    └─────────────────────────────────────────────┘

Equivalently, moving a dilation past a translation **rescales the step**:

    ┌─────────────────────────────────────────────┐
    │   T_a D_q = D_q T_{a/q}                       │   (first-class Round006 object)
    └─────────────────────────────────────────────┘

This is `Q ⋊ Q^×` acting on `Q`. It is the irreducible non-commutative core identified in Round004
(C94: the braid `V_m S = S^m V_m`) now realized on its natural invertible carrier.

## 2. Compression to the integer corner

Let `P_N : l²(Q) → l²(N)` be orthogonal projection onto `N = {1,2,3,...}`. Define

    S   := P_N T_1 P_N |_{l²(N)}          V_p := P_N D_p P_N |_{l²(N)}

Then (verified):

    S|n> = |n+1>          V_p|n> = |p n>              (compressed generators)
    S*|n> = |n-1> (0 at n=1)     V_p*|n> = |n/p> if p|n, else 0   (compressed inverses)

`S, V_p` are **isometries** (`S*S = I`, `V_p*V_p = I` on the `N→∞` corner — verified; finite-window top
atoms are truncation artifacts). The adjoints are the *compressed inverses*, and this gives the first
clean theorem:

> **Divisibility is the survival of inverse-FUCC under projection.**  `V_p*|n> ≠ 0 ⟺ p | n`.
> The elementary sieve `n ↦ n/p` is the compressed inverse dilation; it annihilates exactly the
> integers whose inverse-FUCC orbit leaves the corner `N`. (§2b verified for `p=2,3,5,7`, all `n≤120`.)

## 3. Why the completion must be `Q`, not `Z`

- Inverse SUCC alone closes the **additive** backbone: `N → Z`.
- But inverse FUCC sends `n ↦ n/p`, which leaves `Z` whenever `p ∤ n`. The multiplicative inverse forces
  **denominators**, hence `Q`.
- Group-completing the *joint* additive+multiplicative affine system lands on `Q ⋊ Q^×` acting on `Q`.

So `Z` is only *half* the completion. The ablation `N → Z → Q` (see `HOSTILE_CONTROLS.md`) is run as a
control: `Z` kills the additive boundary (and, strikingly, the von-Mangoldt operator with it — see
`VON_MANGOLDT_AS_SUCC_BOUNDARY.md` §4); only `Q` carries the full invertible machine.

## 4. The slogan

> *"Stop treating missing inverses as zero. Put the states they land on back into the geometry, then ask
> what arithmetic is created when we project them away."*

The next three notes extract that arithmetic exactly: the **boundary** `|1><1|` (`INTEGER_CORNER_DEFECTS`),
its **prime-power transport** `= Λ` (`VON_MANGOLDT_AS_SUCC_BOUNDARY`), and the **stratified** geometry in
which SUCC is diagonal while its shadow in `N` is not (`PRIME_JET_STRATIFICATION`).
