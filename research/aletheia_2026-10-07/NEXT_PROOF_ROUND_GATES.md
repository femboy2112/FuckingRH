> **Updated mathematical baseline:** Tasks 2 and the fixed-horizon reduction portion of Task 3 below are now **proved** by [LOG_EXTENSION_FESHBACH_THEOREM.md](LOG_EXTENSION_FESHBACH_THEOREM.md). The preferred positive operator is not the earlier `P_a=K_a+E_prime+W_+`, but the sharper canonical `P_a=E_{2a}+E_prime`, with `D_a=(V_a+log(2a))I+R_a` bounded. The new min–max bound is uniform in `a`: `lambda_n(P_a)>=0.5[gamma+log(pi*n/2)-Ci(pi*n/2)]`. **Do not spend another round reproving qualitative compactness.** The critical gate is a uniform *arithmetic* lower bound for the finite-rank Feshbach effective matrix `S_a` for **all horizons**. No such sign proof is presently known.

# Next proof round: source-forced completed form, not analogical positivity

**Date:** 2026-10-07  
**Parent audit:** \`RH_PROOF_BEARING_FRAME_AUDIT.md\`  
**Status:** executable research specification. **RH is open.**

## Non-negotiable mathematical baseline

Use Suzuki's published finite-interval Weil form on \(H_0^1(-a,a)\). Preserve the complete normalization and all terms:

\[
Q_W^a(v)=P_a(v)-\langle D_av,v\rangle,
\]

where the canonical positive raw form is

\[
P_a(v)=
\frac14\iint\frac{|v(x)-v(y)|^2}{|x-y|}\,dx\,dy
+\sum_{p^k\le e^{2a}}\frac{\log p}{p^{k/2}}\|v-\tau_{k\log p}v\|^2
+\int \left[-\frac12\log(a^2-x^2)\right]_+|v(x)|^2dx,
\]

and

\[
D_a=\mathcal V_a I+R_a+
M_{\left[\frac12\log(a^2-x^2)\right]_+}
\]

is bounded for every fixed \(a\).

This is an **identity**, not a proof of \(Q_W^a\ge0\).

The two no-go theorems in the parent audit prohibit replacing \(P_a\) by just the prime edge squares or by prime edge squares plus the positive logarithmic kinetic part: their Schur shorts cannot equal the full Weil form.

## Work order

### Task 1 — independent normalization and source audit

Read Suzuki (2023, 2026) directly; reconstruct the form from the screw function and its boundary terms using a genuinely different derivation. Prove the specific \(P_a-D_a\) normalization for all \(a>0\); do not trust repository algebra or an agent report on authority.

**Pass:** symbolically identical coefficients, boundedness of \(D_a\), exactly the allowed prime-power atom set.  
**Fail:** any sign/coefficient discrepancy or unaccounted boundary distribution.

### Task 2 — logarithmic kinetic coercivity

Study the closed form associated with \(P_a\). Establish its domain, closability, and whether its Friedrichs operator has compact resolvent. Derive quantitative eigenvalue lower bounds, ideally of order \(\log n\) or stronger for high modes, with constants explicit in \(a\).

Use the plateau lower bound in \`scripts/rh_proof_frame_audit.py\` as a positive control, but do not turn one oscillatory test family into a universal spectral theorem.

**Pass:** exact compact-resolvent theorem with explicit/high-mode lower bounds and controlled boundary behavior.  
**Fail:** a sequence of normalized high-dimensional states with bounded \(P_a\) energy contradicting compactness.

### Task 3 — fixed-horizon finite-dimensional reduction

If compactness is proved, let \(E_a\) be the spectral projection of \(P_a\) onto eigenvalues below \(\|D_a\|+\varepsilon\). Prove \(\operatorname{rank}E_a<\infty\). On \((I-E_a)\mathcal H\), the full Weil form is strictly positive. Its Schur/Feshbach reduction onto \(E_a\mathcal H\) is an exact finite-dimensional sign test.

Every cross block must come from \(P_a,D_a\), not from a freely chosen positive parent.

**Pass:** rigorous equivalence of \(Q_W^a\ge0\) and positivity of a certified finite effective matrix with a controlled high-mode inverse.  
**Fail:** noninvertible high-energy block, uncontrolled form domain, or a sign assertion requiring RH.

### Task 4 — causal/arithmetical control, not brute-force grids

Seek **uniform-in-\(a\)** lower bounds on the effective matrix from the true LCM/carry/prime-power source. Test against chronological mutation and prime-to-composite substitutions. Check the continuum's forbidden \(\log(p/q)\) and \(\log(pq)\) atomic sectors explicitly.

Finite numerical eigenvalue checks are calibration only. A true result needs a proof over all intervals \(a\), including thresholds \(2a=\log(p^k)\).

### Task 5 — independent nonlinear Suzuki interface

Do not confuse the unconditional half-order/omega-\(1/2\) channel with RH. Prove the finite-Hankel criterion at **every \(\omega>0\)** and \(a>0\), or deduce it from an independently established Weil positivity theorem.

The norm margin at \(\omega=1/2\) tends to zero as \(a\to\infty\); no constant perturbative gap is available.

## Claim gates

- **Disclosed:** symbolic theorem with stated domain and proof, or calibrated certified measurement at a stated finite horizon.
- **Corroborated:** a genuinely independent derivation plus mutations/holdouts.
- **UNVERIFIED:** any cross-horizon estimate, positivity statement, or compactness claim without a proof.
- **Refuted:** explicit counterexample to the declared exact class.
- **RH solved:** only if the all-horizon, all-test Weil sign (or all-\(\omega\) Hankel contractivity) follows without having been assumed.

## Kill conditions

Stop immediately and record a no-go if:

1. prime-only or kinetic+prime-only positive shorting is proposed as the full Weil form;
2. scalar product-formula identities are promoted into Hilbert-valued primitive identities without a declared coupled source map;
3. fake prime moduli produce the same claimed arithmetic "proof" with no source sensitivity;
4. an RH-equivalent bound on \(\Psi\), \(\psi(x)-x\), or \(\xi'/\xi\) appears as a premise;
5. a finite positive matrix is extrapolated to all test functions or infinite horizons without certified closure;
6. the test script's output is reported as executed unless it was actually run and logged.

## Ultimate target

A source-forced, non-circular theorem showing

\[
D_a\preceq P_a
\quad
\text{for every }a>0
\]

in quadratic-form order would establish \(Q_W^a\ge0\) for every interval and hence RH. The present work does **not** establish that order.

The opportunity is now exact operator analysis, not another metaphor about quantum cubes, gravity, or Gamma rotation.
