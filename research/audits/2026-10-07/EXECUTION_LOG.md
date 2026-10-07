# Execution record — RH critical provenance audit, 2026-10-07

**Repository:** \`femboy2112/FuckingRH\`  
**Audit branch:** \`audit/claude-critique-provenance-2026-10-07\`  
**Environment:** isolated Python **3.13.5**; NumPy **2.3.5**; SciPy **1.17.0**.

This is a record of **commands actually run** in this audit, not a GitHub Actions/CI attestation. The independent temporary scripts used to run the checks were \`/tmp/rh_hostile_check.py\` and \`/tmp/rh_cube_critique_checks.py\`; those exact temporary files were **not committed**, and so this record gives input/output values rather than pretending they are GitHub test artifacts. Related durable tests are committed separately:

- \`scripts/rh_log_bathtub_boundary_probe.py\`
- \`scripts/rh_prime_ray_toeplitz_probe.py\`
- \`scripts/rh_critical_provenance_controls.py\`

The literal committed scripts have **not** been executed by this audit through GitHub Actions. They should be run by a local checkout/CI before merging; the independent checks below are not a substitute for that step.

## Command

\`\`\`bash
python /tmp/rh_hostile_check.py
python /tmp/rh_cube_critique_checks.py
\`\`\`

## Observed output

\`\`\`text
prime ray 2 2 (5, 6, 1.0493632888258406, 0.8409777814619263)
prime ray 2 3 (8, 9, 0.9495972072341, 0.6996693962273486)
prime ray 3 2 (3, 4, 0.9783921940070269, 0.8199070976598364)
prime ray 5 3 (3, 4, 0.8586422662441398, 0.7407649027108905)
prime ray 2 0.8 (2, 3, 0.7856387690015739, 0.6336845531885744)
bathtub lower 1 0.6482776387045073
bathtub lower 2 1.4376533930572242
bathtub lower 4 2.114356551002743
bathtub lower 8 2.8029556454520614
bathtub lower 16 3.4949291263050926
bathtub lower 100 5.327125868241555
boundary source 100 mass 1.39699672 target 1.45493641 error -0.0579397
boundary source 1000 mass 1.44359687 target 1.45493641 error -0.01133955
boundary source 10000 mass 1.45690563 target 1.45493641 error 0.00196921
1. Projectivity counterexample L=2 <- L=4: {1: 1/2, 2: 1/2} {1: 1/4, 2: 3/4}
2. Two rotations create top probability 0.9999999999999996 vs 1/2 expected Markov
3. Mellin e^-x 0.8862269254527579 Mellin (1-x)e^-x -0.4431134627263791
4. Inverse Blaschke modulus=1 on real axis, pole at i*1.2
5. Fake Weil 2pt eigen= -0.12565239951829277 Hodge primitive norm= 4.897803970299185
6. First jet n=8 half derivative ~ 0.24506487559 expected 0.24506453587
6. First jet n=6 half derivative ~ 6.21762e-7 expected 0
PASS: six concrete mathematical hostile controls.
\`\`\`

## Interpretation limits

- Small Toeplitz matrices check constants and a closed-form matrix identity; they do **not** verify a whole-horizon spectral positivity statement.
- The first few bathtub bound values are evaluations of the **lower-bound expression**, not measured operator eigenvalues. The eigenvalue inequality rests on its analytical Bessel/bathtub/Ky Fan derivation.
- Finite \(X=100,1000,10000\) boundary masses are a calibration of the PNT normalization, not a convergence proof.
- The counterexamples against projective weights, coherent Markov rotation, and unmodified Mellin multiplier are exact finite identities and **do** refute their respective universal claims.
- The fake off-axis quartet demonstrates that functional-equation symmetry plus a scalar Hodge norm cannot alone force positivity. It is a **synthetic model**, not a zeta counterexample.
- The exact RH-equivalent exponential boundary-discrepancy rate remains unproved.

## Source validation

The primary Weil normalization was separately checked against Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3 (September 2026), especially (2.5), (2.6) and (2.7) in the original 33-page PDF. The paper explicitly attributes prior discrete spectral results to Connes–Consani–Moscovici and does not claim RH.

See [RH_CLAIM_PROVENANCE_LEDGER.md](RH_CLAIM_PROVENANCE_LEDGER.md) for claim-by-claim source and commit lineage.
