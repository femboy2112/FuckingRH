# Factorial/primorial atoms under ℕ: the odometer is the BC clock; support of a loop-family is the conductor

**Round 008. Branch `claude/arithmetic-curvature-loops-008`.** **RH IS OPEN.**
**Reproduce:** `scripts/r008_primorial_odometer.py` (all checks pass; no zeta zeros).

Three externally-supplied intuitions, answered honestly: (i) *build ℕ from atoms of
factorials/primorials*; (ii) *for large N and a small loop-family F, a finite value-set completely
supports F*; (iii) *shadow succ support — 1 is bare succ, 2 = 1+1 is its minimal actualization*. Two
of these are RH-inert re-derivations of structure the frontier already uses; the third is a clean
identification with the finite-conductor truncation. Nothing here moves RH.

---

## 1. The primorial/factorial increment IS the odometer, and the odometer is the braid

The primorial number system writes `n = \sum_k d_k\,P_k` with place values the primorials
`P_k = 2\cdot3\cdots p_k` and digits `0\le d_k< p_{k+1}` (factorial base: `P_k=k!`, `0\le d_k\le k`).
This is a bijection `ℕ↔` digits (verified on `[0,2310]`), and:

- **SUCC = odometer.** `n\mapsto n+1` is exactly the carry-propagating increment (verified on
  `[0,2310]`).
- **The carry is FUCC.** The carry *depth* of `n\mapsto n+1` equals the largest `d` with
  `P_d \mid (n+1)` (verified). So SUCC's hidden multiplicative content is primorial divisibility: the
  odometer *is* the SUCC↔FUCC braid in coordinates (this is the Round-005 carry-curvature C95–C99,
  now read in the primorial atoms).

So "atoms of factorials/primorials" is the correct mixed-radix coordinate for SUCC — but it adds no
new operator: it is the braid again.

## 2. The prime-power (LCM) odometer is `+1` on `\hat{\mathbb Z}` — the Bost–Connes / frontier clock

Primorial radices are squarefree; the *full* arithmetic clock needs prime **powers**. The LCM clock
period `L_M=\mathrm{lcm}(1,\dots,M)=\prod_p p^{k_p(M)}` (verified: `L_6=60`, `L_{12}=27720`,
`L_{24}=5354228880`) gives, by CRT, `\mathbb Z/L_M\cong\prod_p \mathbb Z/p^{k_p}`, and `+1` is the
truncated odometer. As `M\to\infty`,

\[
\mathbb Z/L_M \;\longrightarrow\; \hat{\mathbb Z}=\prod_p \mathbb Z_p,\qquad \text{SUCC}=+1\ \text{on}\ \hat{\mathbb Z}.
\]

This is the **Bost–Connes phase space**, and it is *exactly* the frontier's conductor operator
`\mathcal C` on `L^2(\mathbb Z/L_M)\to L^2(\hat{\mathbb Z})` (SUCC_FUCC_TO_SUZUKI_CANONICAL_SYSTEM.md,
`\mathrm{Tr}\,\mathcal C^{-(s+1/2)}=\zeta(s-1/2)/\zeta(s+1/2)`). Round-006 **C100/C103** already placed
this whole arena — BC `+` the additive Cuntz generator `+` Connes/Tate half-density — at the Weil
wall. **So the factorial/primorial construction re-derives the finite-conductor arena; it is not new
structure.** (Honest: the user's instinct correctly reconstructs the frontier's clock from below.)

## 3. "A value-set completely supports a finite loop-family F" = the finite conductor truncation

A finite family `F` of succ-loops uses finitely many prime-power displacements `\{k\log p\}`. The
family *active at horizon `a`* is exactly `\{p^k\le e^{2a}\}` (Suzuki finite-interval), and the
minimal integer window realizing all those displacements as ratios `n/m` is `\{n\le e^{2a}\}` — the
conductor set. Verified the family sizes

\[
|F|=\#\{p^k\le e^{2a}\} = 5,\,12,\,24,\,98 \quad (a=1,\,1.5,\,2,\,3),
\]

matching the prime-ray symbol's edge counts (ckpt2). **So the user's "for large `N` and small `F`
there is a value-set that completely supports `F`" is, precisely, the finite-conductor truncation:**
a finite horizon supports exactly a finite loop-family, and the "sweep over families" is the horizon
`a\uparrow`. This is why the frontier's finite-conductor reduction is the natural home for the
loop-family idea — and why its proven-negative (`g(a)\to0`) applies: enlarging the supporting
value-set is exactly `a\uparrow`, along which no margin survives.

## 4. Shadow succ support: `1` is bare SUCC, `2=1+1` is the minimal curvature cell

- `1` = the additive unit = the **source** `|1\rangle`: the Round-006 boundary
  `E_S=I-SS^*=|1\rangle\langle1|`, the deleted `0`. "Bare succ, atomic basis for future fucc" is
  exactly this source vector from which every prime ray is transported (Round-006 `\Lambda_{op}=\sum
  (\log p)V_{p^k}E_S V_{p^k}^*`).
- `2=1+1` = first composite **and** first prime: the first place SUCC and FUCC coincide. The braid
  curvature `[T,D_p]=p-1` is minimized at `p=2`, value `1` — the **bare quantum of arithmetic
  interaction curvature**. "`2` contains the minimal actualization of shadow succ support" = the
  `p=2` minimal-curvature cell. (The user's "`1-1`, `x^2-x^2`, `2a-3b` coherent" are the vanishing
  balanced combinations = the relations/loops of ckpt1; the "shadow from `0`" is the deleted-`0`
  source boundary.)

---

## 5. Ledger

- **C107 (RH-inert placement).** Primorial/factorial mixed-radix increment = the odometer = SUCC; its
  carry depth = primorial divisibility = the SUCC↔FUCC braid (Round-005 carry, in atoms). The
  prime-power (LCM) odometer `L_M=\mathrm{lcm}(1..M)=\prod p^k` is `+1` on `\hat{\mathbb Z}=\prod_p
  \mathbb Z_p` = Bost–Connes = the frontier's conductor clock `\mathcal C` (C100/C103: at the Weil
  wall; not new). The user's "finite value-set supporting a finite loop-family `F`" = the
  finite-conductor truncation `\{n\le e^{2a}\}`, `|F|=\#\{p^k\le e^{2a}\}` (= ckpt2 edge counts),
  "sweep over families" = horizon `a\uparrow` (so the proven-negative `g(a)\to0` applies). Shadow:
  `1`=source `|1\rangle` (deleted-0 boundary `E_S`), `2=1+1`=minimal braid-curvature cell `p-1=1`.
  `scripts/r008_primorial_odometer.py`. No RH progress.

RH remains open.
