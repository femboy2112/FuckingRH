# Primary-source literature interface (ckpt6 companion)

**Date:** 2026-10-06. Verified against primary sources (full PDFs read for Lagarias 1999, the 2005
correction, and Conrey–Li). This locks the classical facts Round006 stands on. **RH open.**

## 1. Lagarias positivity criterion — the target is standard

J. C. Lagarias, *On a positivity property of the Riemann ξ-function*, Acta Arith. **89** (1999) 217–234.
`xi(s)=½ s(s-1) π^{-s/2} Γ(s/2) ζ(s)`.

- **(1.4), unconditional:** `Re[xi'/xi(s)] > 0` for `Re s > 1`.
- **(1.5):** `RH ⟺ Re[xi'/xi(s)] > 0` for `Re s > 1/2`. Strict `>`. Lagarias attributes the bare
  equivalence to **Hinkkanen** ("These facts are known, and appear in Hinkkanen [4]"). His own
  contribution is the general admissible-zero-set framework (Thm 1.1) and quantitative results
  (Thm 1.2 unconditional: `inf_t Re xi'_K/xi_K` attained on the real axis for `σ ≥ 1 + 9 n_K^{-1/3}`;
  for ζ, `σ>10`; Thm 1.3 conditional on RH: attained on the real axis for all `σ>1/2`).
- **(1.19):** `RH ⟺ i·xi'/xi(½+iτ)` is a **Pick/Herglotz** function — i.e. `xi'/xi` positive-real on
  `H_{1/2}` ⟺ RH. This is exactly Round006's phrasing.
- **Real-part partial fraction (p. 227, verbatim):**
  `Re xi'/xi(σ+it) = Σ_{ρ=β+iγ} (σ-β)/((σ-β)²+(t-γ)²)` — sign of each term `= sign(σ-β)`.
- **Hadamard constant:** symmetric paired sum `xi'/xi(s) = Σ_ρ 1/(s-ρ)` with **no additive constant**
  (`B = -Σ_ρ 1/ρ`, `B = ½log(4π) - 1 - γ/2 ≈ -0.0230957`). Termwise only conditionally convergent;
  pair `ρ ↔ 1-ρ`.

**2005 correction** (Acta Arith. 116 (2005) 293–294; errata credited to K. Broughan): repairs Lemma 3.1
(`σ₀≠0`, add the `t=0` alternative) and the **sign in (3.8)** — correct decomposition
`xi'/xi = 1/s + 1/(s-1) - ½log π + ½ψ(s/2) + ζ'/ζ` with **+**`1/(s-1)`. Only the *conditional* Thm 1.3
proof was affected; (1.4),(1.5),(1.19),Thm 1.1/1.2 **stand**. ⇒ our `A_inf = 1/s + 1/(s-1) - ½log π +
½ψ(s/2)` and `xi'/xi = A_inf - Σ_p m_p` are correct.

## 2. de Branges positivity condition (the natural "structural passivity")

`E(z)` Hermite–Biehler, `H(E)` the de Branges space; condition
`Re⟨F(z), F(z+i)⟩_{H(E)} ≥ 0` for all `F∈H(E)` with `F(·+i)∈H(E)`. With `E(z)=ξ(1-iz)` it **implies RH**
(zeros of `E` on `Im z = -½` ⟺ zeros of ξ on `Re s = ½`). Refs: de Branges, Bull. AMS 15 (1986) 1–17;
J. Funct. Anal. 107 (1992) 122–210; 121 (1994) 117–184; clean restatement in Conrey–Li Thm 1 and
AIM RH article 40a.

## 3. Conrey–Li obstruction (the warning for route (P))

J. B. Conrey, X.-J. Li, *A note on some positivity conditions related to zeta- and L-functions*,
IMRN 2000 no. 18, 929–940 (arXiv:math/9812166). The de Branges Thms 1 & 2 are TRUE (positivity ⇒ zeros on
line). But the **positivity hypotheses FAIL for the ζ/L spaces**:
- ζ, `E(z)=ξ(1-iz)`: at the 34th zero `ρ=½+i·111.0295…`, `Re{Ē'(w)E(w+i)/2πi} < 0`
  (`-5.389…×10^{-69}`). Condition (3.1) not satisfied.
- ζ, `W=1/ξ(1-iz)`: `Re{ξ(1+282i)/ξ(2+282i)} = -0.000131957 < 0`. Condition (3.3) fails.
- Same for `L(s,χ₄)`.
- **Sarnak's remark (numeric-free):** `F(s)=ξ(s)/ξ(s+1)` has `Im log F = Im log ζ + O(1)` on `Re s>½`;
  since `log ζ` is dense in `C` on `½<Re s<2` (Titchmarsh Ch. XI), some `s₀` has
  `Re{W/W(·+i)} < 0`. Extends to all Dirichlet `L`.

**Killed:** verifying the de Branges positivity directly for the natural ζ-spaces. **Survives:** the
structure theory and the one-directional implication; different structure functions / weaker positivity
are not excluded. (de Branges disputes that this refutes his full program.)

## Consequence for Round006 (used in SCHUR_VITALI_LIMIT, PASSIVE_COLLIGATION, PROOF_ATTEMPT)

The Schur–Vitali reduction (C104) needs hypothesis **(P)**: finite `Θ_X` contractive on all of `H_{1/2}`.
The most natural source of (P) is a de Branges space positivity — which Conrey–Li/Sarnak show FAILS for
ζ. So the Sarnak density argument is a *bona fide* obstruction to the obvious realization of (P): any
`F_X → xi'/xi` that inherits the `ξ(s)/ξ(s+1)` phase behaviour will have `Re < 0` somewhere in the strip
in the limit. A crack must dodge this — a structure not governed by the single-space de Branges
positivity, or passivity forced for a reason orthogonal to it.
