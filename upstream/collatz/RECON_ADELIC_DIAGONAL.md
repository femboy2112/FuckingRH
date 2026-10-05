# RECON — the Adelic / Diagonal picture of the odd Collatz orbit

**Label:** Computational Observation / reconnaissance. Exact integer arithmetic (`sympy.factorint`
for finite-place content; floats = readout only). This maps a frame and locates the obstruction; it
establishes nothing new about Collatz. Ceiling = **Not-Established**.

**Witness:** `_recon_adelic_witness.json` (bare, sha256
`448c818ca4ad0127522047823f0c899f94829f1d734f4b7dacab1d452b9f45ea`) · `.sha256` · `.full.json`.
**Compute:** `_recon_adelic.py`.

---

## 0. The question
Operator intuition: the 2–3 gap is not a two-prime fact — the integers are the **adelic diagonal**
`ℚ ↪ 𝔸_ℚ`, pinned across **all** primes by the product formula `|n|_∞ · ∏_p |n|_p = 1`; a single place
is structurally blind to them. This recon builds the orbit's adelic picture explicitly and asks what
the product formula forces — and, honestly, where it collapses back onto `GAP-NB-3`.

## 1. What the adelic view confirms (the intuition is right — in *substance*)
- **A. The orbit lives in the primes ≥ 5.** Every iterate `n_m` (`m ≥ 1`) is **coprime to 6**: `n_m`
  is odd (`v₂ = 0`) and `3n_m+1 ≡ 1 (mod 3)` kills 3-content (`v₃ = 0`). Verified on **1,083,682**
  iterates, zero exceptions. So `2` and `3` are the *engine* (`×3`, `+1`, `/2^a`); the orbit's
  *substance* is carried entirely by primes `≥ 5`.
- **B. Product formula = "prime content is the log-size."** `Σ_p v_p(n) log p = log n` exactly
  (max error `3.6×10⁻¹⁵`). The finite places literally carry the archimedean size.
- **C. Interloping primes — confirmed, and dramatic.** As an orbit climbs it is forced into ever
  larger prime factors and visits many distinct primes:

  | seed | peak | largest prime factor over orbit | distinct primes visited |
  |---|---|---|---|
  | 27 | `2^12` | 1 619 | 36 |
  | 703 | `2^17` | 55 667 | 59 |
  | 837799 | `2^30` | 679 270 157 | 209 |
  | 1126015 | `2^35` | 13 188 825 161 | 248 |

  A large odd value *must* be built from large primes — the intuition's `∏_p|n_m|_p = 1/n_m → 0` made
  visible: divergence bleeds mass into the finite places.

## 2. The wall, made exact (why every single place is blind)
- **D. The 2-adic driver DECOUPLES from the prime substance.** `a = v₂(3n+1)` is a function of
  `n mod 2^{a+1}` only; by CRT it is **independent** of `n`'s odd-prime factorization. Measured
  correlation between `a` and `log P⁺(n)/log n` over 4 000 coprime-to-6 integers: **`−0.0044 ≈ 0`.**
  The place that *drives* the dynamics and the places that *carry* the size do not talk to each other
  except through the (tautological) product formula. This is `gcd(2,3)=1` / `GAP-NB-3` as a measured
  decoupling — and it is exactly why 2-adic, 3-adic, and single-prime-sieve methods each see only
  their own shadow.

## 3. What the recon *finds* — the obstruction's exact address
- **E. A valuation word pins `n₀` modulo `2^K` and NOTHING else.** Since `gcd(2, p) = 1` for `p ≥ 5`,
  the word imposes **no** condition mod any `p ≥ 5`: the realizers `H + t·2^K` sweep **all** residues
  mod `5, 7, 11, 13` (verified). So the finite places `p ≥ 5` are **dynamically FREE** — they impose
  *no realizability obstruction* on a divergent word.

> **The divergence obstruction lives at exactly two places: `2` (the valuation word / seed-height)
> and `∞` (the size). The primes `≥ 5` interlope in the orbit's *substance* but carry *no obstruction*.**

**The dichotomy (the real takeaway).** The all-primes coupling *does* bite — but only when the problem
**closes into an equation**. A **cycle** forces `n₀·(2^K − 3^m) = C`, and then the all-prime
factorization of `2^K − 3^m` must divide `C`: the places `p ≥ 5` bite hard (this is the engine of the
sister cycle road am06/am07, and of Steiner/Baker). **Divergence never closes**, so its `p ≥ 5` places
stay free, and its obstruction is `{2, ∞}` (structural, CO) — 2-adic realizability against archimedean
size, i.e. **GAP-LF-APERIODIC (RED / Not-Established)**.

## 4. Verdict — the 6th triangulation of GAP-NB-3, and a redirect
This is the **adelic–dynamical** face of `GAP-NB-3` (after factorization, dilation, dual, adelic-static
/ product-formula, and the sieve): the same wall, now as an exact **place-decoupling** with the
obstruction **localized to `{2, ∞}`** for the open (divergence) problem. Two operational consequences,
both honest and both forward:
1. **Stop seeking an all-primes obstruction to divergence.** The `p ≥ 5` places are elementarily free
   there (E: `gcd(2,p)=1`); a sieve over them cannot bite (this is why `GAP-NB-3-SIEVE` was inevitable).
   Divergence is a `{2, ∞}` problem — 2-adic seed-height vs archimedean size — full stop.
2. **Point the all-primes machinery at cycles.** The closed cycle equation is exactly where the
   interloping-prime divisibility of `2^K − 3^m` is a real, exact lever — the place the adelic view
   earns its keep.

CO ceiling; no Collatz-level claim. This *acquires* the target — it does not cross it.
