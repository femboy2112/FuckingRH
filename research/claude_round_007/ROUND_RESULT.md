# Round 007 — the prime-index lift P: n↦pₙ (testing the "outside the circle" candidate)

**Branch:** `claude/prime-index-lift-007` (from Round006 head). **RH IS OPEN.** **Outcome (2):** a genuinely
new, non-affine operator — but shown (computation + literature) to be **orthogonal to the Riemann zeros**,
not a route to them. The Round-006 requirement (supply the missing *analytic* positivity from outside the
BC/Cuntz/Connes circle) remains **unmet** by this candidate, now for a precisely characterized reason.

## CURRENT WALL (live)

> `P|n>=|p_n>` is new and outside the affine circle, but it reparametrizes the **primal (prime) side** of
> the prime↔zero duality — and specifically its **enumeration**, which ζ is provably blind to. RH lives on
> the **dual (zero) side**, reached through the explicit-formula bridge (a sum over the prime *set*). `P`
> supplies no `Γ`-factor, no functional equation, no continuation, no sign structure — none of the analytic
> bridge C103 identified as missing. Same wall; a candidate honestly tried and precisely located *off to
> the side* of it.

## What was tested (all verified, `scripts/r007_prime_index_lift.py`, M=300, no zeta zeros)

Positives (real, RH-inert): `P` isometry with `PP*=Π_primes`; the superprime tower `P^rP*^r`
(`{3,5,11,17,31,…}`); the log-scale hierarchy `P*(log N)P=diag(log p_n)`, `log p_n−log n ~ log log n`.

Decisive no-gos:
1. **`S_ℙ=PSP*` is unitarily equivalent to `S`** (`P*S_ℙP=S` exactly) — prime gaps are the unit step in a
   nonlinear coordinate, cosmetic not dynamical.
2. **`[P,S]`= prime gaps** — the derivative of the relabeling; gap bounds are strictly weaker than RH.
3. **carré-du-champ `[S,P]*[S,P]` = constant `2`** (variance 0, off-diagonal exactly 0); `P*[S,P]=−S`. No
   `Λ`, no `ψ`, no positive form — inert.
4. **`−ζ'/ζ` is invariant under reordering the primes** (verified identical to 8 digits): the enumeration,
   the entire content of `P`, is **gauge** for ζ.
5. **`P` ≅ infinite-multiplicity unilateral shift** (Wold) — no intrinsic arithmetic.

## Literature confirmation (independent scout; NO known RH connection)

The peer-reviewed superprime / prime-indexed-prime (PIP) literature is **entirely PNT-downstream** and
contains **no** connection to ζ-zeros, RH, the explicit formula, L-functions, or Hilbert–Pólya:

- **Broughan & Barnett (2009)**, *On the subsequence of primes having prime subscripts*, J. Integer Seq.
  **12**, Art. 09.2.3: `π₂(x) = Li(Li(x)) + O(x·exp(−A(log x)^{3/5}(loglog x)^{−1/5}))` — leading order
  `x/(log x)²`, **error = the inherited classical PNT error** (so the superprime count is as good as, and no
  better than, PNT). `q_n = n(log n)² + 3n log n·loglog n + O(n log n)` (Cipolla twice). Gap
  `liminf (q_{n+1}−q_n)/(log q_n)² ≤ 1`.
- **Bayless, Klyve & Oliveira e Silva (2013)**, Integers **13**, A43: `Σ 1/q_n ∈ (1.04299, 1.04365)`
  (**converges**, since `q_n ~ n(log n)²` — contrast `Σ1/p_n = ∞`); explicit bounds for higher orders
  `P^{(r)}`, heuristic `π^{(r)}(x) ~ x/(log x)^r`.
- **Dressler & Parker (1975)**, J. ACM **22**: every integer `>96` is a sum of distinct superprimes.
- **Fernandez (1999)** "order of primeness" = the prime-index **depth** `d(p)` (OEIS A049076) — elementary.
- OEIS **A006450**. The arXiv note *Properties of Higher-Order Prime Number Sequences* (2108.04662)
  catalogues the iterates with **no zeta/RH content**.

**Verdict of the scout, matching ours:** the enumeration `n↦p_n` is *recoverable from `π`, which is
determined by the zeros via the explicit formula* — so the indexing is **downstream** of the zeros
(zeros → π → enumeration → superprimes), a deterministic functional with no independent information, and
there is **no construction making the enumeration feed back to the zeros.** The structural reason is exactly
finding 4: ζ is a symmetric function of the unordered weighted set `{(p, log p)}`, so anything built from
*relabelling* the primes is invisible to it (a tautology of the Dirichlet-series formalism).

**Gap vs RH (confirmed):** von Koch (1901) `RH ⟺ π(x)=Li(x)+O(√x log x)`; Cramér (1920) *conditionally*
`p_{n+1}−p_n=O(√p_n log p_n)` — but **no gap bound is known to imply RH** (even Cramér's conjectural
`O((log p_n)²)` does not), because RH is square-root cancellation in the *signed oscillating* error, not an
`L^∞` constraint on prime locations. Superprime-gap statements sit strictly *below* RH.

## Net ledger addition

- **C104**: the prime-index lift `P:n↦p_n` — genuinely new and non-affine, but orthogonal to the zeros.
  `S_ℙ=PSP*≅S` (gaps cosmetic); `[P,S]`=gaps (weaker than RH); carré-du-champ constant (no `Λ`/`ψ`);
  `−ζ'/ζ` reorder-invariant ⟹ the enumeration is gauge for ζ; `P` ≅ ∞-mult. shift (no intrinsic
  arithmetic). Literature: no known RH/zeta connection; superprimes are PNT-downstream (Broughan–Barnett
  2009; BKO 2013). Supplies none of the C103 analytic bridge.

## Honest status

Round 007 is a **clean negative with a sharp reason.** The prime-index lift is the first *non-affine*
candidate the program has tested since the Round-006 call for one — so testing it was right — but it fails
for a reason that now generalizes: **a reparametrization of the prime side cannot reach RH, because the
prime↔zero bridge (the explicit formula) is a sum over the prime *set* and integrates the enumeration
away.** This refines the Round-006 wall statement into a **direction constraint on any future candidate**:

> A genuinely RH-bearing new structure must act on the **dual (zero / analytic) side**, or supply the
> **explicit-formula bridge itself** (the Archimedean `Γ`-factor / functional equation), not merely
> rearrange the primes. The good "tower" intuition is realized by the **function-field / cohomological**
> tower (where Weil positivity is a *theorem*), which lives on exactly that dual side — not by the
> prime-index tower, which lives on the blind side.

RH remains open.
