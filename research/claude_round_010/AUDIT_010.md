# Adversarial audit of Round 010 — outcome and fixes applied

**RH IS OPEN.** A hostile audit (Part B via workflow; Part A re-run as a direct agent after the
workflow's Part-A agent hit the structured-output cap) ran both scripts, re-derived the load-bearing
claims, and specifically probed the unconditional-vs-RH boundary. **Verdict: the unconditional backbone
is clean — no zeta-zero leakage, `A−P=Ψ` identity exact, leading `4√X` cancellation is genuinely PNT,
attributions present — but the interpretive layer carried one RH-leak, one math error, and conflations
that have now been fixed.** The core reductions stand; nothing claimed RH progress before or after.

## Confirmed by the audit (independently re-derived)

- **Part A:** `A−P=Ψ` vs `suzuki_psi` to `~10^{-15}`; `P(t)\sim 4\sqrt X` is unconditional (PNT, partial
  summation from `ψ(u)\sim u`); `A(t)\sim 4e^{t/2}` from the closed form; **no** zeta-zero leakage (the
  zero-side formula is stated only); Suzuki 2023 / Weil 1952 / Bombieri 2000 / Conrey–Li 2000 all cited.
- **Part B:** the multilinear subset expansion and `b_ω(n)=n^{ω-1/2}\sum_{d|\mathrm{rad}\,n}\mu(d)d^{-2ω}`
  are exactly correct (`μ(d)=(-1)^{|S|}` since `d` squarefree); subset size = ω-jet order; standard
  (Euler/Möbius) and labeled as such; no leakage.

## Fixes applied (this commit)

**Part A (`RESERVE_CURVATURE_ATTACK.md`, `r010_reserve_curvature.py`, ledger C113):**
1. **RH-leak — "Ψ bounded" (critical).** The payoff asserted `Ψ` is bounded `O(1)` as a "verified fact."
   Boundedness of `Ψ` is **itself RH-equivalent** (an off-line zero `β>½` gives `Ψ\sim e^{(β-½)t}`,
   sign-indefinite). Fixed everywhere: *unconditionally (PNT) only the leading `4√X` cancels, leaving an
   `o(√X)` remainder; its boundedness AND positivity for all `t` are each RH-equivalent, not shown.*
2. **Math error — "`A''>0` strictly" is false.** `A''` changes sign at `s≈0.2812` (`<0` on `(0,0.281)`).
   I had sampled only `s≥0.5`. Fixed: `A''<0` on the prime-free `(0,0.281)`, `A''>0` for all `s≥\log2`
   (where every prime impulse lives) — so the curvature-domination framing is scoped to the bulk and
   remains honest. Script now samples `s=0.05..4` with an analytic (`mp.diff`) second derivative and
   asserts `A''>0` only for `s≥\log2`.
3. **Conflation / misattribution.** "`P` is a flat tensor over primes / the prime side is flat" was both
   a category error and a misquote of Part B (which says the opposite). Fixed: `P(t)` is a **monotone
   nonnegative sum, not a tensor** (the tensor is the per-`n` coefficient `b_ω(n)`); the positivity
   obstruction is in the `A−P` balance.
4. **Overstatement.** "independent evaluator `suzuki_psi.py`" → "a separate evaluator (same closed form,
   different code path)"; the `~10^{-15}` agreement is a transcription cross-check of the `A/P` split,
   not independent validation of Suzuki's formula.

**Part B (`FACTORIZATION_TENSOR_SKELETON.md`, `r010_factorization_tensor.py`, ledger C112) — fixed in the
prior commit `ac01dc4`:** scoped the flatness/RH-inert claim to the **finite per-`n`** product and added
the caveat that the unrestricted Euler product `\prod_{\text{all }p}(1-p^{-2ω})=1/\zeta(2ω)` carries every
zero; removed the unsupported "the only channel that can carry RH positivity is the Archimedean block";
separated `b_ω(n)` (a tensor) from `P(t)` (not a tensor); added the Conrey–Li flag.

## Net

Round 010 stands as pushed: an **exact reduction** of `Ψ≥0` to the `A−P` curvature balance, a **genuinely
unconditional** (PNT) total `O(√X)` cancellation, and the factorization/tensor skeleton as exact finite
bookkeeping — with every overclaim in the interpretive layer corrected. The audit changed no conclusion;
it removed an RH-evidence leak, corrected a false `A''>0`, and fixed a tensor/flatness misattribution.
Both scripts re-run clean. RH remains open.
