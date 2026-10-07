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

## 4. This is finite per-`n` tensor bookkeeping — RH-inert — and what it buys the attack

For a **fixed `n`**, `\prod_{p\mid n}(1-p^{-2\omega})` is a **finite tensor** over the primes dividing
`n`: each such prime is an independent 2-state factor `{1, −p^{-2\omega}}`, and because the finitely many
squarefree divisors `d\mid\mathrm{rad}(n)` are distinct, the cross-terms are exact Möbius
inclusion–exclusion with nothing to cancel — RH-inert finite bookkeeping. This is the combinatorial,
per-`n` shadow of the Round-008 flatness observation.

**Crucial caveat (scope).** This flatness is *per-`n` and finite*. The **unrestricted** Euler product
over *all* primes is
$$\prod_{p}\big(1-p^{-2\omega}\big)=\frac{1}{\zeta(2\omega)},$$
which carries **every** nontrivial zero — the exact *opposite* of "no analytic content." So "the
multiplicative *bookkeeping* is flat" is a statement about each individual finite conductor coefficient,
**not** a claim that the prime side of RH is analytically trivial. The analytic content reappears the
instant one sums over all `n` (that sum is `\zeta`).

So the honest answer to "can we exploit the factorization pattern?": **yes, as exact finite
bookkeeping** — it factors each conductor coefficient `b_ω(n)` into an independent prime tensor. Its use
for Part A is narrow and precise: the **prime ramp `P(t)` is a monotone sum of nonnegative terms** (it is
*not* itself a tensor — that is the per-`n` coefficient `b_ω(n)`), with **no internal sign cancellation**.
So the positivity obstruction in `Ψ=A−P` cannot come from re-organizing the primes; it lives in the
**`A−P` balance** itself (both grow like `4\sqrt X` and must cancel to a nonnegative remainder — Part A's
"never split the block"). This does **not** localize RH to the Archimedean term alone: `Ψ≥0` is a *joint*
`A−P` property, and **Conrey–Li (2000)** refuted the naive de Branges positivity route to such remainders.

## 5. Ledger

- **C112 (RH-inert, standard; new framing + use).** The division-algorithm factorization
  `N=pa+b` multiplied out = the multilinear subset-over-primes expansion
  `\prod(p_ia_i+b_i)=\sum_S(\prod_{S}p_ia_i)(\prod_{\bar S}b_i)` (verified vs hand expansion, `N=2,3`).
  Same structure = `b_\omega(n)=n^{\omega-1/2}\prod(1-p^{-2\omega})=n^{\omega-1/2}\sum_{d|\mathrm{rad}\,n}\mu(d)d^{-2\omega}`
  (verified `n=6,12,30,36`); subset size `|S|` = ω-jet order = `\nu(n)`, leading `(2\omega)^\nu\prod\log p`
  = `b_0^{(\nu)}` (verified). For fixed `n` it is a finite tensor over the primes `p|n` (distinct
  divisors ⟹ non-resonant Möbius inclusion–exclusion), RH-inert per-`n` bookkeeping — **but the
  unrestricted Euler product `\prod_{\text{all }p}(1-p^{-2\omega})=1/\zeta(2\omega)` carries every zero, so
  this is NOT a claim that the prime side of RH is flat** (scope caveat). Use: factors each conductor
  coefficient `b_\omega(n)` into a prime tensor; and the prime ramp `P(t)` is a monotone sign-definite sum
  (*not* a tensor), so the `Ψ=A−P` positivity obstruction lies in the `A−P` balance, not the prime
  combinatorics (feeds Part A). Does **not** localize RH to the Archimedean term; Conrey–Li 2000 refuted
  the de Branges positivity route. Credit: Euler product / Möbius / Dirichlet convolution / Bost–Connes
  tensor-over-primes (standard). `scripts/r010_factorization_tensor.py`. No RH progress.

RH remains open.
