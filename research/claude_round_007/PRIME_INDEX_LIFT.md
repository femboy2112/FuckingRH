# The prime-index lift P: nⁿ↦pₙ — genuinely new, genuinely outside the circle, but on the wrong side

**Round 007. Branch `claude/prime-index-lift-007` (from Round006 head). RH IS OPEN.**
**Reproduce:** `scripts/r007_prime_index_lift.py` (all checks pass, value window M=300, no zeta zeros used).

## The proposal

Round 006 closed with: *any route inside the Bost–Connes/Cuntz/Connes affine circle reaches the same Weil
wall; a new step must bring structure from outside.* The candidate (ChatGPT-relayed) is the **prime-index
successor**

    P |n> = |p_n>        (p_n = the n-th prime),

with the nested tower `N ⊃ P ⊃ P^(2) ⊃ …` (`P^(2)` = superprimes `{p_{p_n}} = {3,5,11,17,31,…}`), the
inverse direction `π` (prime counting), and the claim that `P` is "neither additive nor multiplicative — a
genuinely new primitive." That last part is **true**. The question this round answers is **which side of RH
it lands on.** Verdict up front: `P` is genuinely new and genuinely non-affine, but it is **orthogonal to
the Riemann zeros, not aimed at them** — it encodes the prime *enumeration*, a structure ζ is provably
blind to.

## What checks out (the honest positives)

- **`P` is an isometry with prime-projector range** (verified): `P*P = I`, `PP* = Π_primes`,
  `I − PP* = Π_non-prime`. The nested tower is real: `P^r P*^r` projects onto the `r`-th prime-index layer;
  `P^2P*^2` → the superprimes `{3,5,11,17,31,…}`. So the "primality-depth filtration" is a bona fide object.
- **A real log-scale hierarchy** (verified): `P* N P = diag(p_n)`, `P*(log N)P = diag(log p_n)`, and
  `log p_n − log n ~ log log n` (PNT). Iterating peels off successive log scales (`log n → log log n → …`).
  This is a genuine renormalization tower — but it is **PNT**, i.e. classical and RH-inert.

## Why it does not help RH — five decisive findings

**1. The "irregular induced successor" is plain SUCC in disguise (the decisive structural fact).**
The induced successor on prime-space, `S_ℙ = P S P*` (`p_n ↦ p_{n+1}`, step = the prime gap `g_n`), is
**unitarily equivalent to the ordinary successor**: verified `P* S_ℙ P = S` exactly. So `P` conjugates `S`
to `S_ℙ`; the "even-more-irregular" step `g_n` is just the uniform unit step `1` read in the nonlinear
coordinate `n ↦ p_n`. **The irregularity is cosmetic — a relabeling, not new dynamics.** This kills the hope
that `S_ℙ` "survives the Round004 no-go by being more irregular": it is the *same operator* as `S`, which
Round004 already placed inside the affine core.

**2. The commutator `[P,S]` is prime-gap geometry — the derivative of the relabeling, and a weaker object
than RH.** Verified `[P,S]|n> = |p_{n+1}> − |p_n+1>`, nonzero exactly when `g_n > 1`. This measures the
failure of `P` to intertwine the two successors, i.e. the nonlinearity of `n ↦ p_n`. Prime gaps are
**strictly weaker than RH**: RH ⟹ `g_n = O(√p_n log p_n)` (von Koch/Cramér), but no gap bound implies RH.
So `[P,S]` trades RH for a murkier, harder, non-equivalent problem.

**3. The carré-du-champ is a constant — it produces no `Λ`, no `ψ`.** The text's sharpest hope was that
`[S,P]*[S,P]` (or `P*[S,P]`) might produce von Mangoldt / Chebyshev `ψ` / a new positive form. It does not:
verified `[S,P]*[S,P]` has diagonal **exactly `2`** (variance `0`; `0` only at `n=1`, the twin `{2,3}`) with
**zero** off-diagonal entries, and `P*[S,P] = −S + sparse`. A constant diagonal carries *no information*.
The prime-index commutator is **inert** — the gap data `{p_n, p_n+1, p_{n+1}}` simply does not align with
the multiplicative/`Λ` structure that connects to ζ.

**4. `P` encodes the enumeration, and ζ is provably blind to the enumeration (the deepest point).**
The object that connects to the zeros (Round 006) is `Λ_op = diag Λ(n)` and the explicit formula
`−ζ'/ζ(s) = Σ_p Σ_k (log p) p^{-ks}` — a sum over the primes as an **unordered weighted set** `{(p, log p)}`.
The index `p_n` never appears. Verified numerically: **`−ζ'/ζ(2+i)` is identical whether the primes are
summed in order or randomly shuffled** (`0.093938065 − 0.389422 5i` both ways, to 8 digits). So the prime
*enumeration* — the entire content of `P` — is **gauge** for ζ: reordering the primes changes `P` completely
and changes the zeros not at all. Pulling the zero-connected operator through `P` gives
`P* Λ_op P = diag(log p_n)` — the primes' own logs, no new zero information. **`P` lives on exactly the
feature of the primes that the Riemann zeros cannot see.**

**5. `P` has no intrinsic arithmetic as an operator.** By the Wold decomposition, `P` is a pure isometry
with infinite defect (`dim ker P* = ` #non-primes `→ 1` in density by PNT), hence **unitarily equivalent to
the infinite-multiplicity unilateral shift** — the most generic such operator. All of its arithmetic lives
in the *spatial embedding* (which value sits at which index), and that embedding is the enumeration ζ is
blind to (finding 4).

## The verdict: outside the circle, orthogonal to the zeros

`P` is genuinely outside the affine (SUCC/FUCC) circle — the ChatGPT analysis is right about that. But
Round 006's call was not "find any non-affine operator"; it was "find the **analytic positivity / signed
Weil structure** the algebra cannot supply" (C103: group completion reproduces ζ only in `Re s > 1`; the
step into the critical strip is the functional equation = the Archimedean `Γ`-factor). **`P` supplies none
of that.** It stays entirely on the prime side of the prime↔zero duality, and worse, on the
*enumeration* of the prime side, which the duality map (the explicit formula, a sum over the set) integrates
away. There is no `Γ`, no functional equation, no continuation, no sign structure anywhere in `P`.

> `P` is "outside the circle" the way a sixth finger is outside the hand: new, but not reaching toward the
> thing. RH lives on the **dual (zero) side**, accessed through the explicit-formula bridge; `P` is a
> reparametrization of the **primal (prime) side** that the bridge does not transmit.

## The good intuition, redirected

The underlying instinct — *"RH might need a tower/hierarchy, not a flat prime set"* — is genuinely good, and
it **is** realized in real mathematics. Just not by the prime-*index* tower:

- the **right tower** is the one Round 006 already pointed at: the **function-field analogue**, where RH is a
  **theorem** via a *cohomological* tower (Frobenius eigenvalues on étale cohomology of curves over `F_q`;
  Weil, Deligne). There the "hierarchy" is field extensions `F_{q^n}` and the positivity is a theorem;
- or the **L-function / moment hierarchy** (families of `L`-functions, the Katz–Sarnak symmetry types).

Both are towers on the **dual/analytic** side, where the zeros and the positivity live. The prime-index
tower is a tower on the **blind/enumeration** side. Same word, opposite location.

## One-line summary

`P: n ↦ p_n` is a legitimate new primitive and a real primality-depth hierarchy, but (i) its dynamics are
unitarily equivalent to plain SUCC, (ii) its commutators/carré are inert (gaps, constants — no `Λ`/`ψ`),
and (iii) it encodes the prime *enumeration*, which `−ζ'/ζ` is invariant under. It is outside the affine
circle but **orthogonal to the zeros**; it does not supply the missing analytic bridge. RH remains open, and
the genuinely-new-structure requirement from Round 006 is still unmet by this candidate.
