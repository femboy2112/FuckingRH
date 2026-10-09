# Provenance, claims, and reproducible evidence

**Date:** 2026-10-09. **RH status:** open. This is a continuation of the authorized repository research, with exact mathematics, finite diagnostics, and open obligations labelled separately.

## 1. Source of the question and frozen repository inputs

Leah proposed the archimedean place as an ideal superconducting description of an infinite recursive prime circuit. The useful mathematical content tested here is lossless transport, preservation of complete return histories, and completion to an exact boundary response. No physical superconducting medium, quasiparticle spectrum, or norm for an unrestricted infinite prime current is postulated.

| Input | Frozen revision | Use in this round |
| --- | --- | --- |
| Working research branch | `research/2026-10-09/reversal-memory-polarization`, `11f9070132c46478fbc6c5de2f8109850ce7d0e7`, tree `0d2b8848319981b7342dae6e2a596a553ef50612` | Parent; inherits RMP-001/002/005/006/007 and the explicit open polarization gate. |
| Live main | `344facc9b9eccadcf7fe98af9361b6e7fd3ea737`, tree `5294e0dda571c8b2aaf114c7934413dbb323f553` | Round066 and the current catalog audited for overlap and scope. |
| Succ–Weil–Suzuki bridge | `e6f2d08716cc699efec10eafd6738e770615bc76` | Exact full tangent, closed Gamma energy, finite-power normalization, and smooth-core/strong rather than operator-norm distinctions. |
| Round006 passive colligation note | Original blob `4fa517e8936ce313dd3e2a5fc79f56dab50c6a96` | Read before constructing new controls; revised here to withdraw invalid universal/no-go inferences. |
| Round006 Schur–Vitali and source-port work | Paths at the frozen working/main revisions | The conditional continuation criterion and failed specific source realizations are prior results, not new discoveries. |

The other October9 research branch heads were inventoried to avoid overwriting concurrent work. No unseen branch theorem is imported into this checkpoint. No `AGENTS.md` or `CLAUDE.md` occurred in the inspected recursive trees. The change continues the research branch; it does not update main or concurrent branches.

All new derivations were produced by the GPT-6 assistant. Three warm same-model forks provided narrow construction, source, and adversarial audits. The principal thread read their proofs, checked the normalizations, ran the integrated scripts, and independently compared the spatial Weil formula with the spectral delay integral. These are internal checks, not independent external peer review. No priority claim is made for the classical formulas used.

## 2. Claim ledger

| ID | Truth state | Statement | Evidence and limit |
| --- | --- | --- | --- |
| LAC-001 | PROVED | The finite Gamma all-pass cascade has an exact Gamma-product formula; its unrenormalized interior limit is zero; the normalized limit needs a divergent advance; its delay drop converges monotonically with an explicit tail bound to the known Gamma energy. | Gamma note. Classical Gamma identities applied explicitly; local channel only. |
| LAC-002 | PROVED | Half-density prime filters satisfy an exact unitary storage law, have Poisson-kernel delay, reproduce the actual local L-factor after a one-clock advance, and retain mixed return histories. | Prime note §§1–3; `log 6` cascade amplitude `1/3`. This is not an intertwiner for the entire SUCC/Hecke host. |
| LAC-003 | PROVED / CLASSICAL NORMALIZATION | The full compact-core Weil form equals the polar correction minus the finite-place total-delay average. Complete prime towers and finite-power truncation differ by an exactly canceled scalar; higher-place cutoff stabilization is exact. | Prime note §§4–5; old full Weil normalization inherited. Burnol already relates local Gamma logarithmic derivatives to the explicit formula. |
| LAC-004 | PROVED | Centering and boundary elimination have an explicit resolvent correction. A positive two-node storage family gives an incorrect positive boundary sign and a correct value `-1/4` at every cutoff; pole cross terms matter too. | Boundary note; exact Fraction controls. The negative witness is a control network, not an arithmetic Weil vector. |
| LAC-005 | PROVED / CONDITIONAL INTERFACE | Boundary losslessness and reversal do not imply causal Hardy preservation. A reciprocal all-pass moves one unit pulse wholly into the past. Contractivity of the specified causal arithmetic source along shifts omega_j decreasing to zero would imply the full Weil sign through the inherited tangent. | Causality note; exact rational/Pick/quartet controls. The arithmetic contraction is not proved. |
| LAC-006 | PROVED COUNTERMODELS / SCOPE CORRECTION | A mixed-composite logarithmic source does not universally force off-line zeros. Logarithmic-derivative positivity differs from shifted-ratio positivity. RH equivalence does not imply impossibility of unconditional construction. | Explicit cosh model; analytic logic; Conrey–Li norm versus extra pairing. Corrected C107–C108 and passive note. |
| LAC-007 | VERIFIED FINITE | Four portable programs and one supplementary high-precision program pass their specified checks. | Reports and stdout in `evidence/`; floating diagnostics are not interval certificates or all-horizon positivity. |
| LAC-008 | OPEN | An arithmetic source-defined positive metric on the correctly completed boundary/history space, identified with the full Q_W; or the corresponding bounded causal extension of the specified Suzuki kernel. | The scalar local circuits and known positive delay drops do not yet construct this object. |

The worked sufficient boundary criterion is exact: if the *centered* interior block `Q_ii` is strictly positive, then `Q>=0` iff its centered Schur complement is nonnegative. A usable infinite-dimensional certificate needs the interior lower bound, bounded couplings or a closed-form framework, and limit control. There is no inverse formula at an unhandled zero mode.

## 3. What changes in the interpretation of Round066

The frozen [Round066 catalog](https://github.com/femboy2112/FuckingRH/blob/344facc9b9eccadcf7fe98af9361b6e7fd3ea737/wiki/08-the-reformulations-catalog.md) contains several statements requiring narrower scope.

1. A finite zero-spacing sample cannot establish an infinite no-hard-gap theorem or prove GUE statistics. Nearest-neighbor spacing and a gap in an excitation spectrum are also different quantities. Such a sample does not decide the lossless-transport interpretation tested here. We did not rerun a zero-based diagnostic or use zeros as construction input.
2. `Lambda(n)=0` off prime powers does not mean zero source at every composite: `Lambda(4)=log 2`. Integers with at least two distinct prime factors are the mixed-composite support test.
3. The Davenport–Heilbronn mixed-source defect is a useful failure of the required Euler coherence. The assertion that this defect *is* its off-line zeros needs a separate theorem. The elementary `D(s)=1+sqrt(6)6^{-s}` countermodel has a connected coefficient at 6 but a completed cosh function whose zeros all lie on the critical line. This model lacks zeta's Euler/Gamma/conductor axioms; it refutes the universal implication, not a statement proved within those stronger axioms.
4. Closed operators, entire continuation, and a unitary local Fourier response each have precise meanings. None alone constructs the positive completed Weil pairing. Conversely, an RH-equivalent construction is not logically forbidden; proving it would prove RH.

A final ref check also observed main at `8505467ea596b0636f73b655c521f50105d8b06e` (Round067, child of Round066). Its commit describes consolidation rather than a new verified construction. No general impossibility of a finite mathematical proof, or equivalence of verifiability with sign-blind finite experiments, is established here. A finite argument with uniform control could prove an infinitary assertion.

Main is not edited by this branch. The working branch's directly relevant historical passivity note and C107–C108 are corrected, with the original version preserved by commit permalink.

## 4. Primary sources checked

| Source | Precise role |
| --- | --- |
| [NIST DLMF §5.5](https://dlmf.nist.gov/5.5) and [§5.11](https://dlmf.nist.gov/5.11) | Gamma recurrence/reflection and Gamma-ratio asymptotics. The finite product, phase, and tail calculations are written out in the note. |
| [Burnol, The Explicit Formula and the conductor operator](https://arxiv.org/pdf/math/9902080), §§E, H, I | Local Fourier/inversion multiplier and logarithmic-derivative/conductor interpretation of the explicit formula. |
| [Burnol, Scattering on the p-adic field and a trace formula](https://arxiv.org/pdf/math/9901051) | Local scattering/time-delay and Weil trace connection. The chosen group-delay sign is explicitly fixed here. |
| [Connes–Consani, Quasi-inner functions and local factors](https://arxiv.org/pdf/2008.10974), Theorems 2.1, 4.1, 4.8 | Finite sets containing infinity have compact off-diagonal Hardy leakage on the left critical half-plane. Compactness is not vanishing or a uniform infinite-place limit. |
| [Burnol, An adelic causality problem related to abelian L-functions](https://arxiv.org/pdf/math/0001013), Theorem 1.7 | Precise global causality/orthogonality criterion; a conditional target, not an independent source of positivity. |
| [Suzuki, A canonical system of differential equations arising from the Riemann zeta-function](https://arxiv.org/pdf/1204.1827), §§1.3–1.7, Proposition 1.2 | Boundary unit modulus/reversal versus innerness of the shifted-xi family and its causal operator realization. The retrieved PDF has an internal September13,2018 version date. |
| [Suzuki, Weil's quadratic form via the screw function, v3](https://arxiv.org/pdf/2606.09096v3) | Current explicit-formula normalization, compact-window form domains, and self-adjoint realization; local realization does not assert the missing global sign. |
| [Ball–Biswas–Fang–ter Horst](https://arxiv.org/pdf/0705.2042), Theorem 1.1 | Correct disk Schur/conservative-realization contract; the finite identity is also proved directly. |
| [Dörfler–Bullo, Kron Reduction of Graphs](https://arxiv.org/pdf/1102.2950), equations (1.1)–(1.2) | Static boundary elimination and induced internal-source term. Our conservative oscillator energy and centering correction are directly proved. |
| [Conrey–Li, A note on some positivity conditions](https://arxiv.org/pdf/math/9812166), §2 | The de Branges Hilbert norm and the additional shifted pairing are different objects. |

## 5. Reproduction

Run from the repository root. The portable environment used Python3.12.14, NumPy2.3.5, and SciPy1.17.0. The standard-library causality probe needs neither numerical package. The supplementary Gamma run used mpmath1.3.0 at 90 decimal digits.

```bash
python scripts/gamma_cascade_probe.py --output research/2026-10-09/lossless_arithmetic_circuit/evidence/gamma_cascade_results.json
python scripts/boundary_centering_probe.py --output research/2026-10-09/lossless_arithmetic_circuit/evidence/boundary_centering_results.json
python scripts/causal_allpass_probe.py --output research/2026-10-09/lossless_arithmetic_circuit/evidence/causal_allpass_results.json
python scripts/semilocal_weil_delay_probe.py --output research/2026-10-09/lossless_arithmetic_circuit/evidence/semilocal_weil_delay_results.json
```

With mpmath available:

```bash
python scripts/gamma_cascade_high_precision_probe.py --output research/2026-10-09/lossless_arithmetic_circuit/evidence/gamma_cascade_high_precision_results.json
```

The actual interpreter used for the supplementary run is recorded in the manifest. Dependency versions and hashes are pinned for reproducibility, not claimed to be generally required versions. The compact tent test belongs to H1 with zero boundary values, where the smooth-core identity extends by approximation as proved in the prime note.

## 6. Results and limits

| Check | Observed result | Meaning |
| --- | --- | --- |
| Finite Gamma product versus special-function expression | Maximum residual `8.26e-14` in the portable run | Checks the finite identity implementation. |
| Gamma boundary modulus / delay recurrence | `8.66e-15` / `5.33e-15` | Finite controls; the universal identities have analytic proofs. |
| Supplementary 90-digit Gamma product | Residual about `1.76e-91` | Higher-precision numerical agreement, not an interval enclosure. |
| Independent spatial Weil / spectral delay | Maximum residual below `1e-10` over three prime cutoffs | Each comparison reports its analytic Fourier-tail bound and non-certified quadrature estimates. |
| Actual Gamma/prime Schur correction | Residual below `6e-14`; correction nonzero at A=0.5,1,2 | Sixteen-cell diagnostics, with one retained even coordinate. No continuum or all-horizon positivity claim. |
| Wrong reduction order | Correct boundary `-1/4`, wrong boundary positive for all integer cutoffs | Analytic all-cutoff counterexample; exact rational sample checks. |
| Wrong time arrow | Leakage norm exactly one for the specified unit pulse | Analytic formula plus exact rational norm computation. |
| Adaptive fictitious primitive clock at log6 | Locally Schur filter; wider-test completed value changes from `0.0008295191` to `-0.0128807449` | Source-fidelity diagnostic. The exact change is a known correlation term; the numerical signs are not advertised as interval certificates. |

The adaptive log6 test was added after the first spatial/spectral run and is disclosed in the probe contract. The original narrow test cannot see that event because its correlation support ends before log6. No result is presented as a held-out statistical discovery.

The proof frontier has moved to a better specified construction problem: preserve the exact source, its complete hidden response, and the centering through boundary elimination or Hardy continuation. The independent sign of that *completed* object remains open.
