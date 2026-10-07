> **2026-10-07 critical review:** The log-eigenvalue bound, prime-ray AR(1)/KMS identities and PNT source limits are finite/operator-theoretic results; none proves the all-`a` completed Weil sign or Suzuki `Θ_ω` Hardy innerness for all ω>0. [CAUSAL_HARDY_RH_PROOF_GATES.md](../audits/2026-10-07/CAUSAL_HARDY_RH_PROOF_GATES.md) and [the source/agent/test provenance ledger](../audits/2026-10-07/RH_CLAIM_PROVENANCE_LEDGER.md) are the current interpretation. The older cube projective-probability and unitary-Markov analogies are explicitly refuted.

# Round result — logarithmic spectrum, prime towers, and boundary actualization

**Date:** 2026-10-07  
**Branch:** \`research/rh-log-bathtub-prime-shift-2026-10-07\`  
**Verdict:** multiple unconditional proof steps and sharp obstructions. **RH OPEN.**

## Mathematical results

### 1. Explicit logarithmic phase-space spectral inequality

For the positive part \(P_a\) of Suzuki's exact finite-interval Weil form,

\[
\boxed{
\lambda_n(P_a)\ge
\gamma+\log(\pi n)-\operatorname{Ci}(\pi n)-1
=\log n+O(1).
}
\]

Stronger than the previous \(\tfrac12\log n+O(1)\) bound. Derived by Bessel's density cap, bathtub filling, and Ky Fan/min-max, not by sampling spectral zeros.

### 2. Sharp individual prime-shift Poincaré constant

For width \(2a\), shift \(h>0\), and zero-extended \(f\),

\[
\boxed{
\|f-\tau_h f\|^2\ge
2\left(1-\cos\frac{\pi}{\lceil2a/h\rceil+1}\right)\|f\|^2.
}
\]

Exact by finite-chain fiber decomposition.

### 3. Exact full prime-power tower as AR(1) Toeplitz matrix

For \(p\), let \(h=\log p\), \(r=p^{-1/2}\), \(K=\lfloor2a/h\rfloor\), \(N=\lceil2a/h\rceil\), and \(S_p=h\sum_{k=1}^Kr^k\). The sharp \(p\)-ray gap is

\[
\boxed{
\gamma_p(a)
=
2S_p+h-h\lambda_{\max}
\left((r^{|i-j|})_{1\le i,j\le N}\right).
}
\]

The covariance inverse is tridiagonal. The sum

\[
\Gamma_a=\sum_p\gamma_p(a)
\]

is a **stronger, source-sensitive** scalar floor than summing each depth separately.

Consequently, for all \(n\),

\[
\boxed{
\lambda_n(Q_W^a)\ge
\gamma+\log(\pi n)-\operatorname{Ci}(\pi n)-1
+\Gamma_a-\|D_a\|.
}
\]

This reduces the explicit potentially negative spectral rank to an exponential in \(\|D_a\|-\Gamma_a\) instead of \(2\|D_a\|\).

### 4. Strong prime–pole matching at opposite boundaries

At interval \((-A,A)\), in fixed opposite boundary strips of width \(\ell\), define

\[
\mu_A=e^{-A}\sum_{e^{2A-2\ell}\le q\le e^{2A}}
\frac{\Lambda(q)}{\sqrt q}\,\delta_{2A-\log q}.
\]

Unconditional PNT gives

\[
\boxed{\mu_A\Rightarrow e^{-w/2}dw.}
\]

The rescaled prime Hankel block \(H_A\) therefore converges strongly on \(L^2(0,\ell)\) to

\[
\boxed{
P=|e^{-u/2}\rangle\langle e^{-u/2}|,
}
\]

which is exactly the normalized Archimedean pole block.

This is a genuine **operator-level** version of the leading \(4\sqrt X\) cancellation.

### 5. Topology no-go

Every finite prime boundary source is atomic. Simultaneous phase recurrence implies

\[
\boxed{
\liminf_{A\to\infty}
\|H_A-P\|_{L^2\to L^2}
\ge1-e^{-\ell}>0.
}
\]

So there is **no** full \(L^2\)-operator-norm completion.

On the natural logarithmic Weil energy domain \(\mathscr V_\ell\), compact embedding instead gives

\[
\boxed{
\|H_A-P\|_{\mathscr V_\ell\to L^2}\to0.
}
\]

Classical de la Vallée Poussin quantitative PNT even implies an unconditional \(O_\ell(A^{-1/4})\) bound for this graph-norm convergence.

### 6. The RH-strength rate

For fixed \(\ell>0\), let

\[
\eta_A(\ell)
=
\sup_{0\le w\le2\ell}
\bigl|
\mu_A([0,w])-2(1-e^{-w/2})
\bigr|.
\]

Then

\[
\boxed{
RH
\iff
\eta_A(\ell)=O_\ell(e^{-A}(1+A)^K)
\text{ for some finite }K.
}
\]

This is a new zero-free *coordinate* on the same RH wall, not a proof of the rate. PNT gives only \(\eta_A=o(1)\).

### 7. Exact conductor-entry topology ladder

For a new prime-power shift \(h=\log q\) and interval \(a=h/2+\delta\):

- a smoothly transported Dirichlet profile has correlation \(O(\delta^3)\), with explicit cubic coefficient;
- general \(H_0^1\) states satisfy a uniform \(O(\delta^2\|v'\|^2)\) bound;
- constant/indicator vectors in the logarithmic form domain have **linear** onset;
- the compressed shift has operator norm \(1\) immediately after entering, hence an operator-norm jump.

The cubic statement is deliberately **not** extrapolated to the full spectral form domain.

### 8. Shift-curvature selection rule

For positive scalar continuum shifts compressed to an interval,

\[
\boxed{T_hT_k=T_{h+k}=T_kT_h.}
\]

Curvature cannot arise from reordering these forward shifts. Mixed adjoint commutators are boundary-supported partial shifts at ratio displacement \(k-h\). When \(h=\log p^j\), \(k=\log q^r\) with **distinct prime bases** \(p\ne q\), those are forbidden extra \(\log(q^r/p^j)\) scalar atoms; same-prime ratios may already be allowed, but their weights still need checking; any physical observation of the internal curvature must eliminate them.

This constraint is scoped to bare continuum shifts and does not kill residue-dressed SUCC commutators.

## Reproduction

- \`scripts/rh_log_bathtub_boundary_probe.py\`
- \`scripts/rh_prime_ray_toeplitz_probe.py\`
- \`scripts/rh_causal_shift_commutators.py\`

The finite identities have independently reproduced calculations and explicit proofs in the companion theorem notes. The GitHub scripts are committed; do not represent unrun CI as executed.

## Three hard no-go rules now established

1. **No norm limit** of the rescaled atomic boundary source to the smooth pole block on all \(L^2\).
2. **No uniform prime-ray gap** as \(a\to\infty\) for fixed \(p\); \(\gamma_p(a)=\Theta_p(a^{-2})\).
3. **No forward-only translation curvature**; these shifts commute exactly.

## Remaining mathematical task

The safe, exact starting point is

\[
Q_W^a=P_a-D_a,
\]

with

\[
P_a=E_{2a}+\sum_p \mathcal E_{p,a}.
\]

One-prime rays are now compressed exactly into finite Jacobi precision operators; the logarithmic ultraviolet spectrum has a nearly optimal coefficient-one lower estimate; and the leading pole-vs-prime boundary correlation is understood at the strong-operator level.

What is missing is a **joint-prime/carry/Archimedean inequality** strong enough to prove, for every \(a\),

\[
\boxed{P_a\succeq D_a.}
\]

Equivalently, show the exact finite low-energy Feshbach operator is nonnegative at every horizon. The sharp boundary discrepancy rate is another equivalent formulation.

A successful next round should attack the **simultaneous prime-log phase sublevel geometry** of

\[
m_{2a}(\xi)+2\sum_{q\le e^{2a}}
\frac{\Lambda(q)}{\sqrt q}
(1-\cos(\xi\log q))
\]

together with the exact pole/Gamma remainder, without assuming independence of prime phases or inventing a positive metric.

**RH: OPEN.**
