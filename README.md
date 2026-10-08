> **Research update:** [Encountered information vs causal energy](research/audits/2026-10-07/CAUSAL_FILTRATION_INFORMATION_ENERGY.md). `Lambda(n)=log lcm(1..n)/lcm(1..n-1)` is computed locally at each event; its rank-one SUCC boundary injection has a uniform finite `L²` bound, but the coherent prime output grows like `2sqrt(X)`. This distinction is tracked with [primary source and claim provenance](research/audits/2026-10-07/RH_CLAIM_PROVENANCE_LEDGER.md) and [executed controls](research/audits/2026-10-07/CAUSAL_FILTRATION_EXECUTION.md). RH remains open.

> **Research update (2026-10-07):** [Wavefront causality is not Hardy passivity](research/audits/2026-10-07/ACTIVATION_CAUSALITY_HARDY_PASSIVITY.md). Suzuki's (h_\omega(x)=0) for (x<1) and real-line (|\Theta_\omega|=1) are both unconditional. The RH-bearing condition is *stable global Hardy causality for the completed transfer*, not mere positive local event activation. [Claim provenance](research/audits/2026-10-07/RH_CLAIM_PROVENANCE_LEDGER.md) tracks original source, first proof commit, executed counterexamples and the unproved step.

> **Actual RH proof interface:** [The corrected Markov-to-Hardy proof gates](research/audits/2026-10-07/CAUSAL_HARDY_RH_PROOF_GATES.md) show why finite unitary/Markov/Gamma positivity is insufficient and what completed all-ω causal property would prove RH. The [actual execution log](research/audits/2026-10-07/EXECUTION_LOG.md) avoids invented CI claims. Future PRs use the [provenance checklist](.github/PULL_REQUEST_TEMPLATE.md).

> **2026-10-07 research provenance:** The [active claim-by-claim provenance ledger](research/audits/2026-10-07/RH_CLAIM_PROVENANCE_LEDGER.md) distinguishes Suzuki and classical source theorems from assistant-derived finite identities, hostile control results, imported critiques and RH-equivalent unproved statements. It records precise source versions, proof commits, test status and correction history. The [imported cube-atom critical audit](research/audits/2026-10-07/CUBE_ATOM_CRITICAL_AUDIT_IMPORTED.md) is archived with authorship uncertainty stated explicitly. RH remains open.

# FuckingRH

Research repository for a proof-first attack on the Riemann Hypothesis.

**Status:** RH remains open. This repository distinguishes exact identities, verified controls, conjectural bridges, refuted shortcuts, and the load-bearing theorem still owed.

## Start here

1. [CURRENT_STATE.md](CURRENT_STATE.md) — canonical governing frame.
2. [docs/SCREW_SINC_LEVY_UNIFICATION.md](docs/SCREW_SINC_LEVY_UNIFICATION.md) — **current shortest RH-equivalent attack surface**: Suzuki's explicit prime-wavefront function, sinc/triangle convolution squares, screw-kernel positivity, and infinite divisibility.
3. [CLAIM_LEDGER.md](CLAIM_LEDGER.md) — what is proved, corroborated, conjectured, unverified, dark, or refuted.
4. [docs/NEGATIVE_CONTROLS.md](docs/NEGATIVE_CONTROLS.md) — attractive dead ends that have already failed.
5. [PROVENANCE_MAP.md](PROVENANCE_MAP.md) — where the archived conversation and cross-repo material came from.
6. [docs/LITERATURE_CURRENT_2026-10-05.md](docs/LITERATURE_CURRENT_2026-10-05.md) — refreshed current literature map.
7. [research/2026-10-05/FOURIER_MELLIN_TRANSPORT_PROBE.md](research/2026-10-05/FOURIER_MELLIN_TRANSPORT_PROBE.md) — exact finite/Archimedean transport probe and its two-prime obstruction.

## Current dominant reduction

Masatoshi Suzuki gives an explicit even function \(\Psi(t)\), defined directly from prime powers plus the Archimedean completion, for which

\[
\boxed{\mathrm{RH}\iff \Psi(t)\ge0\quad\forall t\in\mathbb R.}
\]

Moreover \(\Psi(t)=W(R_t*\widetilde R_t)\), where \(R_t\) is a rectangular window; its Fourier transform is a sinc. Writing \(g=-\Psi\), RH is also equivalent to global positivity of the Kreĭn screw kernel and, by Nakamura–Suzuki, to \(e^{-\Psi}\) being an infinitely divisible characteristic function.

That is the first object to attack. The broader Weil/prolate/adelic/absolute-geometry programs remain in the repo as independent routes and controls.

Substantial consolidation work lives on branch `aletheia/rh-consolidation-2026-10-05`; `main` is intentionally minimal until the research branch is reviewed.

## Astra proof attempt 001

[Round result](research/astra_round_001/ROUND_RESULT.md): **RH remains open**. The round proves finite-event rigidity, rules out the canonical geometric-prime Gaussian residual, and reconstructs the event/tail obligation with certified controls. See the [proof attempt](research/astra_round_001/PROOF_ATTEMPT_001.md) for the first unpaid lemma.
