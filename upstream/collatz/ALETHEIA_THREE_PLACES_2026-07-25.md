# The Three Places in One Equation — the lossless soul

**Round:** Aletheia, 2026-07-25 (second round of the day) · **Label: RECONNAISSANCE /
Computational Observation**
**NOTHING HERE IS MINTED.** No ledger entry, no auditor pass, no operator sign-off, no
disjoint-stack second path. Nothing in this file may be cited as established.
**Collatz remains OPEN.** This file closes no gap and proves no half of the conjecture.

Companion to `research/ALETHEIA_MIRROR_TRICHOTOMY_2026-07-25.md` (same day, earlier round).

Generators (exact integers / `fractions.Fraction` only; no float on any load-bearing path —
floats appear solely as display renderings of exact Fractions, marked as such in the output):

- `tools/recon_scripts/_aletheia_20260725_lossless_soul.py`
- `tools/recon_scripts/_aletheia_20260725_three_places.py`

---

## 0. The operator's question

> *"look at the soul signal of the integers, but in a way that doesn't drop information …
> probe the archimedean structure orthogonally and not lose out on 2-adic and 3-adic
> information … there must be a non-trivial/circular way of doing this."*
> *"try things that don't make sense initially … −1 is 1+2+4+8+…, we can always add 0."*

The diagnosis behind the question is correct and is this project's own AMPUTATION lesson
(C-0394 round): **every instrument we hold amputates at a different place.**

| instrument | keeps | throws |
|---|---|---|
| forward iteration | `\|n\|_∞` | the 2-adic class |
| the seal `H mod 2^{K+1}` | the 2-adic class | `\|n\|_∞`  ← **the amputation** |
| logs / pressure / transfer ops | `\|n\|_∞` | everything non-archimedean |

## 1. The lossless object

For a word `w=(a_1..a_m)`, `K_j = a_1+..+a_j`, `K=K_m`, `C_m = Σ_{i<m} 3^{m-1-i}2^{K_i}`:

    SOUL(w)  =  n*(w)  =  C_m / (2^K − 3^m)   ∈ Q      (exact rational)

the affine fixed point of the m-step map `A(x) = (3^m x + C_m)/2^K`. Its denominator
`2^K − 3^m` is **odd** (2,3 coprime), hence a unit in `Z_2` *and* in `Z_3`, so `n*` has a
face at **every place simultaneously** and nothing is dropped:

| face | what it is | status before this round |
|---|---|---|
| at 2 | its 2-adic digits — truncation **is** the seal `H` | the only face we ever read |
| at 3 | its 3-adic digits | partly read — C-0313/C-0255 (window), C-0347 (Ψ) |
| at p≥5 | `v_p(n*)`, the odd-prime spectrum of the denominator | not read |
| at ∞ | its actual size as a real number | discarded **by the seal**; Ψ is archimedean-valued |

**Gates (all PASS; readings inadmissible without them).**
`G1` L-LIFT `n* ≡ H_+ mod 2^{K+1}`, all 4402 deficient words m≤11 · `G2` L-SIM on 2000 real
orbits · `G3` L-TIP on 1968 seed/word pairs · `G4` periodic `n*(u^k)` constant, recovers
−1, −5, −17 · `G5` L-3RIGID `v_3(n*)=0`, all deficient m≤10 · `GA1`–`GA4` (21000 checks).

## 2. The archimedean face, exactly

    Φ_m := C_m/3^m = Σ_{i<m} 2^{K_i}/3^{i+1}      exact rational, monotone increasing
    Λ_m := n_m·2^{K_m}/3^m

**A-SPLIT** (exact, every orbit, every m; 21000 checks, 0 violations)

    Λ_m = n_0 + Φ_m          ⟹ Λ_m is MONOTONE STRICTLY INCREASING, unconditionally

**A-PROD** (exact; 21000 checks, 0 violations)

    Λ_m = n_0 · Π_{i<m} (1 + 1/(3 n_i))      ⟹ Λ converges ⟺ Σ 1/n_i converges

*Proof of A-PROD.* `Λ_{i+1}/Λ_i = (n_{i+1}/n_i)(2^{a_{i+1}}/3) = (3n_i+1)/(3n_i)`. ∎

**A-SOUL** `n*_m = −Φ_m/(1 − 2^{K_m}/3^m)`, so when `Φ_m → Φ_∞ < ∞` and `2^{K_m}/3^m → 0`
the soul's **archimedean** limit is `−Φ_∞ < 0`, while (L-NEST, earlier round) its **2-adic**
limit is `𝓗`.

## 3. A-DUAL — the centrepiece

> **The 2-adic seal is computable with no 2-adic inverse anywhere.**
>
>     H_m = (2^{K_m}·ñ − C_m)/3^m
>
> where `ñ` = least **odd** positive integer `≡ C_m·2^{−K} (mod 3^m)` with `2^{K_m}ñ > C_m`.

`ñ` is a **3-adic** reduction; `2^{K}ñ > C_m` and "least" are **archimedean**; and the
**parity bit on `ñ` is a 2-adic constraint** — so "no 2-adic inverse" is literal but the
enumeration is (3-adic class + archimedean minimisation + one 2-adic parity bit).

> **NOT NEW, AND NOT TWO DERIVATIONS. Read this before the counts.**
>
> **(a) `ñ` IS `n_m`.** A-DUAL is the convolution identity `2^K n_m = 3^m n_0 + C_m` solved
> for `n_0`. Saying so removes most of the appearance of discovery.
> **(b) Already in the ledger.** `ledger/claims.yaml:16196-16197` (C-0345, Theorem 1 proof)
> records *"n0=(2^P n_k − C_k)/3^k is increasing; the least valid n_k carries a CRT offset …
> (the fixed prefix confines n_k to an AP mod 2·3^k)"* — "AP mod `2·3^k`" **is** "least odd
> positive `≡ C·2^{−K} mod 3^k`". This is a ledger-recorded, already-corrected mechanism.
> **(c) One identity, two implementations.** `H()` reduces the identity mod `2^{K+1}` and
> kills `n_m` by oddness; `H_via_3adic()` reduces the **same** equation mod `3^m` and kills
> `n_0`. Their equality is a five-line theorem, so these runs cross-check **two
> implementations, not two derivations** (`certification-certifies-reproducibility-not-derivation`).
> The check *can* fail — drop "odd" or `2^Kñ > C_m` and it does — so it is a real test of the
> characterisation of `ñ`, and nothing more.

**Runs:** 4402 deficient words m=1..11 exhaustively, 0 violations; 3000 random arbitrary
(incl. non-deficient) words, 0 violations; ground-truth realization check **scope: m ≤ 8,
deficient only**, 0 violations.

The three places are not three coordinates — they are **one equation**. **Boundary, stated
here and not 90 lines away:** this is a restatement, it makes neither side easier to control,
and reading it as progress on `OPEN-0004` would be false.

## 4. A-GHOST — the operator's `−1 = 1+2+4+8+…`, exactly

**NOT NEW — C-0347 (ii), flagged as such in the companion doc the same day and at the same
range.** `Φ_m` itself is a ledger object: `Φ_∞ = −Ψ` (`claims.yaml:16308-16309`) and the
partial-sum identity `Σ_{j<m}2^{K_j}/3^{j+1} = C_m/3^m` is C-0347's machine-checked identity
(`:16311-16312`). What follows is that statement in archimedean language, nothing more.

For the all-ones word, `Φ_m = 1 − (2/3)^m` **exactly** (confirmed m ≤ 39), so `Φ_∞ = 1` and
the soul's archimedean limit is **−1** — the same `−1` that `1+2+4+8+… ` gives 2-adically.
`H_+(1^m) = 2^{m+1}−1` was the *amputation*, not the object. **The climber was never
climbing.** Both faces agree: the ghost is a **diagonal** point of `R × Q_2`.

Confirmed at the other periodic anchors: `(1,2)^∞ → Φ_∞ = 5`, soul `−5`; `(1,1,2)^∞ →
Φ_∞ = 19/11`, soul `−19/11`; the 7-block → soul `−17`.

**CORRECTED — this is NOT a second, disjoint proof, and the restatement I first wrote
was FALSE.**

*The false version:* "last round proved `𝓗 < 0` for **periodic** words." **Deficiency
dropped.** The all-twos word (the trivial 1-cycle) is periodic with
`𝓗 = C_p/(2^A−3^p) = +1 > 0` — verified for p = 1,2,3. `ledger/claims.yaml:16325`
(C-0347 (iii)) already records *"Psi(all-twos) = +1 exactly (the attractor pole)."* The
archimedean argument silently needs `Φ_∞ < ∞`, and for all-twos `Φ_∞ = ∞`. The companion
doc states T-PERIODIC **with** deficiency and is unaffected; this restatement dropped it.

*Not disjoint either.* For a period-`p` block,
`Φ_∞ = Σ_k (2^A/3^p)^k · Φ_p = C_p/(3^p − 2^A) = −𝓗` — the **same rational, geometrically
resummed**. §2's own `n*_m = −Φ_m/(1 − 2^{K_m}/3^m)` *is* that rearrangement, and both routes
take their sign from the **same** archimedean input `2^A < 3^p`. There is one proof here,
written twice.

## 5. `Φ_∞ ≥ 1`, and why the squeeze does NOT close

*Proof.* Every letter `a_i ≥ 1`, so `K_i ≥ i`, so `2^{K_i} ≥ 2^i`, so
`Φ_∞ = Σ 2^{K_i}/3^{i+1} ≥ Σ 2^i/3^{i+1} = 1`, **with equality iff `K_i = i` for all i, i.e.
iff the word is all-ones.** ∎

So the ghost is not merely *an* example of a phantom — it is the **unique extremizer of the
archimedean constraint**, the boundary case.

**And the squeeze fails, provably.** A single defect at position `j` gives
`Φ_∞ = 1 + (2/3)^j` exactly (verified j = 2,3,5,8,13). These decrease to 1 without reaching
it: **there is no gap in the value set of `Φ_∞` above 1.** ("Spectral gap" is a loaded term
in this branch and is deliberately not used.)

**Scope of the kill, corrected.** Only threshold arguments with `T > 1` are dead. The shape
"a divergent orbit needs `Φ_∞ < 1`, and no word achieves it" is **valid**, since the infimum
1 is attained only at all-ones. And the kill ignores realizability: near-all-ones words are
*proven* phantoms by C-0347 (iii), so a threshold argument **combined with** a realizability
constraint is untouched by this section.

## 6. The correction — where the 3-adic information actually is

Earlier in this round I reported, from `L-3RIGID` (`v_3(n*_m) = 0` for every finite m) and
from the Phase-3 window probe, that **there is no 3-adic information to lose.**
**That reading is correct at finite level and does not extend to the limit.** The probe I
built to test it is what caught it:

    single defect at j :  𝓗 = −(3^j + 2^j)/3^j       v_3(𝓗) = −j

verified 2-adically at m = 20, 60, 120, 240, 399 for j = 2,3,5,8,13 by
`tools/recon_scripts/_aletheia_20260725_phi_limits.py` (exact `Fraction` equality; the tail is
`Φ_∞ − Φ_M = 2·(2/3)^M` exactly, **not** a tolerance).

`v_3(n*_m) = 0` at every finite m, and `v_3(𝓗) = −j` in the limit.

> **The closed form is NOT new and the fate was ALREADY DECIDED in the ledger.**
> `claims.yaml:16327-16328` (C-0347 (iii)) proves, for **every** prefix and by a **one-line
> proof**, `Ψ(prefix ++ all-ones) = −(C_p + 2^{K_p})/3^p < 0`, with the corollary *"hence the
> C-0345 family never has a positive-integer source"*. My `−(3^j+2^j)/3^j` is the `p = j`
> instance. **The genuine increment is only the `v_3` reading** of an already-held closed form.
> Two mis-citations also corrected: `H = 2^{m+1}−1` for the climber is **C-0343**, not C-0345;
> and C-0345 Theorem 1 **does** cover the single-defect family (it covers all words that are
> all-ones from some position on), contrary to what an earlier draft said.

So the trichotomy refines:

**For every infinite DEFICIENT word `w`** — the hypothesis is load-bearing and an earlier
draft of this table dropped it, making row (a) **false as printed**: without deficiency,
`ledger/claims.yaml:16326` records `Psi(word(n) ++ all-twos) == n` for every odd `n ≤ 3999`,
so every ordinary **convergent** orbit yields `𝓗 ∈ Z_{>0}` and `n = 1` refutes the row.

| case | condition | meaning (deficient `w` only) |
|---|---|---|
| (a) | `𝓗 ∈ Z_{>0}` | genuine +1 orbit — a counterexample **modulo the gaps below** |
| (b) | `𝓗 ∈ Z_{<0}` | genuine −1 object (a cycle; COR-QUARANTINE) |
| (c) | `𝓗 ∈ Q \ Z` | phantom, and **the denominator's primes name the place it dies** |
| (d) | `𝓗 ∉ Q` | phantom at no place in particular |

**Named gaps for row (a)**, reproduced from the companion doc §3 rather than dropped:
"case (a) is empty" is the divergence half **modulo `GAP-PSI-REALIZABILITY` / `OPEN-0005`
(RED, Not-Established)**; and the "divergent" reading additionally needs *bounded ⇒
eventually cyclic ⇒ a tail block with `2^A > 3^p` ⇒ contradicts deficiency*, **not written
in either doc.**

For eventually-all-ones words that place is **3**. This is a mechanism C-0345 Thm 1 does not
carry: C-0345 records `H = 2^{m+1}−1` for the pure climber; this gives the **exact closed
form of `𝓗` for every single-defect word**, and identifies the killing place.

## 7. What the finite-level probes returned — two sharp negatives

Both are **Computational Observation, scope-limited** ("Demonstrated" is not one of the nine
labels) and both are negative results:

1. **The 3-adic face at finite level is a sliding window.** `n* mod 3^r` is a function of the
   last `r` letters alone — max distinct residue per suffix class = **1**, every row, m ∈
   {6,8,10}, r ∈ {1,2,3}. The hand law `n* ≡ 2^{−a_m} mod 3` (1749 words, 0 violations) is the
   `r=1` case and CAN fail, so it is the real evidence here. **The "control (full word) = 1"
   line is struck: it cannot fail** — the grouping keys on the whole word, one word per key, so
   it reads 1 for any implementation including a broken one. **This is our own C-0313/C-0255 width-k window: circular at finite level.**
   The probe was built to refute the round's premise and did.
2. **No association visible at this resolution** between σ (the seal's top bit) and the
   archimedean size, on the exact statistic `bit_length(C_m) − bit_length(D_m)`, to m=13
   (m=13: `+` 5022/3773, `−` 5083/3759 — ratios 1.331 vs 1.352). **Downgraded from
   "Demonstrated decoupling / killed":** no flatness criterion was pre-registered, so this is
   an observation, not a no-go.

Also recorded: `g = gcd(C_m, 3^m−2^{K_m})` — the Door-1 partial-divisibility meter,
`n* ∈ Z ⟺ g = D_m`. Mostly 1 (41869 of 51033 at m=14); `max g` reaches 4766585 at m=14, still
`≪ D_m`; prime support small (5, 7, 11, 13, 17, 19, 23, …), 5 dominant. Never instrumented
before; no law extracted.

## 8. What this does NOT establish

1. **It closes nothing.** Separating case (a) from (c)/(d) is the terminal wall (`OPEN-0004`),
   untouched. The anti-concentration atom is exactly where it was.
2. **`Φ_∞ < ∞` is NOT necessary for divergence** — only for divergence fast enough that
   `Σ1/n_i < ∞`. A hypothetical sub-geometrically divergent orbit has `Φ_∞ = ∞`. Any use of
   §2–§5 must carry this hypothesis explicitly.
3. **A-DUAL is an identity, not a reduction of difficulty.** It shows the 2-adic seal carries
   no information independent of (3-adic tip class + archimedean minimisation). It does **not**
   make either side easier to control. Reading it as progress on `OPEN-0004` would be false.
4. **The §7 negatives are scoped**: r ≤ 3 and m ≤ 10 for the window; one statistic and m ≤ 13
   for the decoupling. Neither is a theorem; a different statistic could couple.
5. **Novelty UNASSESSED.** No literature search. `Λ_m = n_0 + C_m/3^m` is the convolution
   identity divided by `3^m`; the product form and `Φ_∞ ≥ 1` are elementary and **may well be
   known or folklore**. No priority claim.
6. **Single stack.** CPython bigint/Fraction only. No PARI/GP second path. CO ceiling at best,
   and only after an auditor pass it has not had.
7. **My own finite-level reading was wrong past its scope** (§6) and I have corrected it in
   place rather than quietly dropping it. One tolerance in a scratch check was mis-set
   (demanded `< 10^{−80}` where the exact tail is `(2/3)^{400} ≈ 10^{−70}`); rerun with the
   tail stated exactly — `Φ_∞ − Φ_400 = 2·(2/3)^{400}` for every j tested.

## 9. The lamp not yet lit

The odd primes `p ≥ 5`. Of the places carrying the soul, `2` is exhaustively instrumented,
`3` is now instrumented (finite-level window, limit-level killer), `∞` is instrumented here.
**`p ≥ 5` has one measurement (§7's `g` census) and no theory.** By case (c), a phantom's
denominator names its killing place; the primes dividing `3^m − 2^{K_m}` are exactly the
Door-1 divisibility primes, so the odd-prime face is where **Door 1 and Door 2 touch the same
number.** That is the next probe, and it is cheap.
