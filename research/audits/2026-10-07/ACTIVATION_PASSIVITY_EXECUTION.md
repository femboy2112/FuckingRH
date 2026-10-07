# Execution record — activation / causality / Hardy passivity controls

**Date:** 2026-10-07  
**Branch:** \`research/rh-activation-causality-passivity-2026-10-07\`  
**Claim note:** [ACTIVATION_CAUSALITY_HARDY_PASSIVITY.md](ACTIVATION_CAUSALITY_HARDY_PASSIVITY.md)  
**Mathematical status:** finite synthetic counterexample verification, NOT a proof of RH.

An independent local test script \`/tmp/rh_activation_passivity_check.py\` was executed using \`python\` in an isolated container during the mathematical derivation. It tested five statements, with all assertions passing.

### Observed stdout (actual execution)

\`\`\`text
PASS: stable and unstable causal rational transfer functions are both boundary-all-pass.
PASS: positive activating unstable kernel produces y(4)=69.025226220 from unit-amplitude input.
PASS: stable all-pass state-space storage dE/dt=|u|^2-|y|^2 (3 controls).
PASS: probability-preserving activating coalescence has L2 operator norm=1.414213562.
PASS: nontrivial positive causal impulse measure is not all-pass (two-atom counterexample).
\`\`\`

### What was run

1. Evaluate \((i\xi+a)/(i\xi-a)\) and its reciprocal on five real frequencies, asserting boundary modulus \(1\).
2. For a unit input on \([0,1]\), evaluate the unstable positive causal output at \(t=4\), \(a=1\), giving \(2(e-1)e^3\).
3. Check the exact stable storage equality with three explicit real states and inputs.
4. Compute the largest singular value of the two-state column-stochastic coalescence matrix \(\begin{pmatrix}1&1\\0&0\end{pmatrix}\), obtaining \(\sqrt2\).
5. Check that \((\delta_0+\delta_1)/2\) has characteristic function \(0\) at frequency \(\pi\).

The durable repository counterpart \`scripts/rh_activation_vs_passivity_controls.py\` was created and subsequently corrected to remove an inert test placeholder. The **literal committed script was not run via GitHub Actions**, and no CI attestation is claimed. Core finite claims were checked independently, as listed above.

### Primary external evidence

Suzuki [arXiv:1204.1827v2](https://arxiv.org/html/1204.1827v2): his (2.3) gives \(h_\omega(x)=0\) for \(x<1\) unconditionally; (1.9) gives \(|\Theta_\omega(t)|=1\) on real \(t\); Theorem 2.2 equates all-input global \(L^2\) convolution mapping with meromorphic innerness; Proposition 1.2 supplies the RH-equivalent all-\(\omega\) gate.

The synthetic counterexamples are not Suzuki's actual transfer. The full arithmetical Hardy contractivity remains unproved; RH OPEN.
