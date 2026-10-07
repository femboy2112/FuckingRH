# The composite-factorization pattern is the Euler/Möbius tensor skeleton (the flat side)

**Round 010 / Part B. Branch `claude/arithmetic-curvature-loops-008`.** **RH IS OPEN.**
**Reproduce:** `scripts/r010_factorization_tensor.py` (all checks pass; no zeta zeros used as input).

An externally-supplied idea: write each factor in **division-algorithm form** `N = p·a + b` (prime `p`
× index `a` + residue `b`) and multiply. The question: *is there an arithmetic pattern in how composites
factor this way that we can exploit?* The answer is yes — and it is exactly the backbone we keep meeting.

## 1. The pattern: multilinear subset expansion

A product of factors `(p_i a_i + b_i)` expands by one **binary choice per factor** — take the prime
part `p_i a_i` or the residue part `b_i`:

$$\prod_i (p_i a_i + b_i)=\sum_{S\subseteq\{1,\dots,k\}}\Big(\prod_{i\in S}p_i a_i\Big)\Big(\prod_{i\notin S}b_i\Big).$$

Verified against the hand expansion (`N=2,3`): e.g. `(re+f)(pa+b)(qc+d)` graded by `|S|` =
#prime-parts chosen:

| `|S|` | term(s) | meaning |
|---:|---|---|
| 0 | `bdf` | pure residue (all-additive) |
| 1 | `adf·p + bcf·q + bde·r` | one prime chosen |
| 2 | `acf·pq + ade·pr + bce·qr` | two primes |
| 3 | `ace·pqr` | pure prime (all-multiplicative) |

So the "pure-prime" corner (`S` = all) and the "pure-residue" corner (`S=∅`) are the extremes; the
**mixed terms are the inter-channel interference**, the thing the curvature program (Round 008) is about.

## 2. It *is* the conductor coefficient (subset over the prime support)

The same structure is Suzuki's conductor coefficient — verified numerically for `n=6,12,30,36`:

$$b_\omega(n)=n^{\omega-1/2}\prod_{p\mid n}\big(1-p^{-2\omega}\big)
=n^{\omega-1/2}\sum_{d\mid \mathrm{rad}(n)}\mu(d)\,d^{-2\omega}.$$

Each prime contributes `1` (not chosen / residue side) or `−p^{-2\omega}` (chosen / prime side); the
subset `d=\prod_{p\in S}p` carries sign `\mu(d)=(-1)^{|S|}`. The user's "prime part vs residue part" is
exactly "`−p^{-2\omega}` vs `1`."

## 3. Subset size = the ω-jet order = `ν(n)`

The **size** `|S|` is the Taylor order in `ω`: the leading power of `\prod_{p\mid n}(1-p^{-2\omega})` is

$$(2\omega)^{\nu(n)}\prod_{p\mid n}\log p\qquad(\nu(n)=\#\text{distinct primes}),$$

verified for `n=6,12,30`. Choosing *all* `ν` primes at leading order is the pure-prime subset
`|S|=ν`, which is Pillar-1's `b_0^{(\nu)}(n)=\nu!\,2^{\nu}\prod\log p/\sqrt n`. So the factorization
grading, the Möbius grading, and the ω-jet grading are **one and the same**.

## 4. This is the flat (tensor) side — RH-inert — and what it buys the attack

The expansion is a **tensor product over primes**: each prime is an independent 2-state channel
`{1, −p^{-2\omega}}`, and `\prod_p(1-p^{-2\omega})` is their tensor. By unique factorization the prime
log-scales `\{\log p\}` are `ℤ`-independent (Round 008), so **the cross-terms do not resonate** — they
are exact, finite Möbius inclusion–exclusion, carrying no analytic content. This is the combinatorial
form of the Round-008 flatness theorem: *the multiplicative side is flat.*

So the honest answer to "can we exploit the factorization pattern?": **yes, as exact bookkeeping, but it
is RH-inert.** Its real use is structural — it **factors the one-block conductor coupling `V` into an
independent tensor of flat prime channels**, which means the only channel that can carry the RH
positivity is the **Archimedean** block. That isolation is exactly what Part A (the attack on `Ψ≥0`)
needs: the prime side is a known, flat tensor; the fight is the Archimedean reserve dominating the prime
impulse train.

## 5. Ledger

- **C112 (RH-inert, standard; new framing + use).** The division-algorithm factorization
  `N=pa+b` multiplied out = the multilinear subset-over-primes expansion
  `\prod(p_ia_i+b_i)=\sum_S(\prod_{S}p_ia_i)(\prod_{\bar S}b_i)` (verified vs hand expansion, `N=2,3`).
  Same structure = `b_\omega(n)=n^{\omega-1/2}\prod(1-p^{-2\omega})=n^{\omega-1/2}\sum_{d|\mathrm{rad}\,n}\mu(d)d^{-2\omega}`
  (verified `n=6,12,30,36`); subset size `|S|` = ω-jet order = `\nu(n)`, leading `(2\omega)^\nu\prod\log p`
  = `b_0^{(\nu)}` (verified). It is a tensor over independent prime channels; UFD ⟹ cross-terms are
  non-resonant Möbius inclusion–exclusion = the flat multiplicative side (Round-008 flatness, combinatorial
  form), RH-inert. Use: factors the conductor coupling `V` into a flat prime tensor, isolating the
  Archimedean block as the sole RH-bearing channel (feeds Part A). Credit: Euler product / Möbius /
  Dirichlet convolution / Bost–Connes tensor-over-primes (standard). `scripts/r010_factorization_tensor.py`.
  No RH progress.

RH remains open.
