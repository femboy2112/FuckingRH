# RH claim provenance ledger — 2026-10-07 critical reconciliation

**Status:** evidence/provenance ledger; **RH is open**.  
**Branch:** \`audit/claude-critique-provenance-2026-10-07\`, based on \`research/rh-log-bathtub-prime-shift-2026-10-07\` at \`b52449857a243395436d80b15ca462c0fc81fcad\`.  
**Purpose:** distinguish primary literature, inherited work, independently reproduced elementary checks, user-supplied intuition, agent-authored conjectures, and genuinely unpaid analytic claims.

This file is **not** a peer-reviewed assessment and does not confer priority. A GitHub commit authored under the connected user's account is an API/account attribution, **not evidence that the user individually wrote the math**. In this workflow, GPT-6 generated and committed the audited 2026-10-07 additions at the user's request. Older Claude/Astra material remains attributed at the *research lineage* level only when supported by its own commit messages and note metadata.

## P.1 Provenance rules — required for any future RH claim

Every load-bearing claim needs all of:

1. **Claim ID + exact hypothesis/quantifiers:** especially \(a\), \(\omega\), function domain and topology; avoid words like "global" where only finite horizons were proved.
2. **Mathematical source:** external author, stable URL, version/date, theorem/equation/page when applicable; separate prior literature from repo-original derivation.
3. **Local proof pointer:** exact repository path, section and *commit SHA at which the proof first appeared*. Later corrections must cite both original and correcting commits.
4. **Verification record:** independent symbolic derivation, executable test command, exact environment/results or "not executed"; finite numerical agreement is not a proof of an infinite theorem.
5. **Failure/negative controls:** explicit counterexamples, mutation conditions, dependence on true arithmetic versus fake primes.
6. **Proof status:** one of *external theorem*, *in-repo proved / needs external hostile audit*, *finite observed*, *RH-equivalent reformulation*, *conjectured*, *refuted*, *unknown*.
7. **Agent/contribution provenance:** user's motivating analogies can be credited separately from assistant-generated derivations; do not assert Claude wrote any unattributed file.

Do not use "DISCLOSED" as a substitute for a verifiable derivation. Do not use "test passed" without execution evidence. Do not report a source match as an independent proof if both calculations descend from the same formula.

## P.2 Primary literature — checked against original versions

### [SRC-SUZ-2026-V3] Suzuki — finite Weil form

Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3, last revised **2026-09-23**.

- Stable abstract/version: https://arxiv.org/abs/2606.09096v3
- Original paper: https://arxiv.org/pdf/2606.09096v3
- **Equations (2.3)–(2.7), printed pp. 8–11:** localized logarithmic difference energy, boundary potential \(-\frac12\log(a^2-x^2)\), prime-power shifts, smooth remainder, and Fourier multiplier \(\log|\xi|+\gamma\).
- **Equations (2.9)–(2.11), pp. 12–13:** distributional realization of the Weil operator.
- **Introduction, printed pp. 1–3:** provenance of Weil/Yoshida/Bombieri/Connes–Consani–Moscovici and already-known discrete lower-bounded spectrum. Suzuki explicitly labels the infinite self-adjoint operator realization *conjectural*.

Audited by reading/screenshotting the original v3 PDF, not merely trusting a repository paraphrase. This is the governing normalization. If future repo formulas disagree with it, fix the repo.

### [SRC-SUZ-2012-V2] Suzuki — innerness/causality criterion

Masatoshi Suzuki, *A canonical system of differential equations arising from the Riemann zeta-function*, arXiv:1204.1827v2, revised **2016-09-23**.

- https://arxiv.org/abs/1204.1827v2
- Proposition 1.2 and Theorem 2.2: meromorphic-inner/Hardy causal condition; refer to the paper for exact domain and \(\Theta_\omega\) normalization.
- **Warning:** \(|\Theta_\omega(t)|=1\) on real \(t\) is not enough; analyticity and boundedness in the proper half-plane are essential.

### [SRC-SUZ-2023] Suzuki — positivity criterion

Masatoshi Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, JLMS 108 (2023), DOI **10.1112/jlms.12785**, arXiv:2206.03682.

- https://arxiv.org/abs/2206.03682
- Theorem 1.7: the explicit screw-function inequality \(\Psi(t)\ge0\) for all \(t\) is RH-equivalent.

### [SRC-KMS-1953] Kac–Murdock–Szegő — Toeplitz covariance

Mark Kac, William L. Murdock, Gábor Szegő, *On the eigen-values of certain Hermitian forms*, Journal of Rational Mechanics and Analysis 2 (1953), pp. 767–800.

- The matrix \(C_N(r)=(r^{|i-j|})\), its geometric/AR(1) covariance interpretation, and tridiagonal inverse are **established mathematics**. Our use of it for a truncated prime-power translation ray is a finite operator application; do not claim invention of the KMS matrix.
- An accessible worked reference also appears in the scientific literature on AR(1) covariance matrices; check exact signs independently before using the inverse in proofs.

### [SRC-BATHTUB] Lieb–Loss — bathtub principle

Elliott H. Lieb and Michael Loss, *Analysis*, Theorem 1.14 (Bathtub principle). The minimization of \(\int f\rho\) under \(0\le\rho\le M\) and fixed mass is classical.

- This is the tool behind the log-spectrum improvement; the **Bessel density cap**, **Ky Fan principle** and Fourier conventions must be stated explicitly.

## P.3 New finite Weil/operator claims — source lineage and limits

### [PV-2026-001] Zero-extension identity — in-repo proved, external normalization

**Claim:** On \(C_c^\infty(-a,a)\),

\[
L_a(v)
=
\frac14\int_{|h|<2a}
\frac{\|\tau_hv_0-v_0\|_2^2}{|h|}dh
-\log(2a)\|v\|^2.
\]

- External dependence: SRC-SUZ-2026-V3 (2.3)–(2.6), *not* a new Weil formula.
- Proof: \`research/aletheia_2026-10-07/LOG_EXTENSION_FESHBACH_THEOREM.md\` §2, first entered at commit \`c332aaaa49b7d084e7f1d07d240bd1f9d9add239\`.
- Independent finite controls: constant and linear compact-support examples in \`scripts/rh_zero_extension_feshbach.py\`. Prior session reported execution, but this turn does **not** independently re-run that exact repository script; independent mathematics/source audit confirms coefficients.
- Result status: **in-repo theorem; third-party hostile audit not claimed**.
- Restriction: zero extension and full logarithmic boundary potential are essential. The prime-only cube cannot reproduce this high-frequency operator.

### [PV-2026-002] Compact spectrum + fixed-horizon Feshbach — in-repo proved / classical tool

**Claim:** The positive form \(P_a=E_{2a}+E_{\rm prime,a}\) has compact resolvent for each \(a\); with explicit bounded \(D_a\), \(Q_W^a=P_a-D_a\). Its finite low-energy Feshbach matrix has the same sign as \(Q_W^a\), **for each fixed \(a\)**.

- Proof: \`LOG_EXTENSION_FESHBACH_THEOREM.md\` §§3–8, \`c332aaaa49b7d084e7f1d07d240bd1f9d9add239\`.
- Prior art: Suzuki v3 Introduction credits Connes–Consani–Moscovici 2025+ for *spectral discreteness/ground state*. No novelty claim for that conclusion.
- Limit: effective low-mode matrix positivity at **every** \(a\) is RH-equivalent and UNVERIFIED. Compactness alone is not progress on global sign.

### [PV-2026-003] Unit-coefficient logarithmic spectral lower bound — in-repo proved, numeric calibration

**Claim:**

\[
\lambda_n(P_a)\ge\gamma+\log(\pi n)-\operatorname{Ci}(\pi n)-1.
\]

- Derivation: Bessel bound \(\sum|\widehat f_j(\xi)|^2/(2\pi)\le a/\pi\), fixed mass \(n\), SRC-BATHTUB, Ky Fan.
- First commit \`d5867267bf335a865b2bd01a2b80516a455692b1\`; file \`research/aletheia_2026-10-07/LOG_BATHTUB_PRIME_SHIFT_BOUND.md\` §2.
- Independent finite checks executed in a separate Python container during the 2026-10-07 audit: for \(n=1,2,4,8,16,100\), lower bounds approximately \(0.648277639,1.437653393,2.114356551,2.802955645,3.494929126,5.327125868\).
- Status: **mathematical argument recorded; finite constants reproduced; no independent peer review**.
- The right side concerns \(P_a\), not the full \(Q_W^a\). Subtract \(\|D_a\|\) before deriving any conclusion about Weil's operator.

### [PV-2026-004] Sharp single-shift and whole-prime-ray gap — in-repo proved, standard KMS input

**Claims:** for interval width \(W\),

\[
\|f-\tau_hf\|^2\ge
2\left(1-\cos\frac{\pi}{\lceil W/h\rceil+1}\right)\|f\|^2.
\]

For a fixed prime \(p\) at horizon \(a\),

\[
\gamma_p(a)=2S_p+\log p-(\log p)\lambda_{\max}C_N(p^{-1/2}),
\quad
N=\lceil 2a/\log p\rceil,
\quad C_N(r)=(r^{|i-j|}).
\]

- Proofs: \`LOG_BATHTUB_PRIME_SHIFT_BOUND.md\` §3 (\`d5867267...\`), \`PRIME_POWER_RAY_TOEPLITZ.md\` §§1–5 (\`2e18621f6d3e802034f65cc8b937862811dfc58f\`). Tridiagonal inverse from standard KMS/AR(1) covariance.
- Independent exact-matrix numeric reimplementation executed 2026-10-07: \((p,a)=(2,2)\) gap \(1.0493632888258406\) versus independent-sum \(0.8409777814619263\); \((3,2)\) \(0.9783921940070269\) versus \(0.8199070976598364\).
- Input data: actual prime powers \(p^k\), coefficients \((\log p)p^{-k/2}\); no zeros.
- Limitation: \(\gamma_p(a)\to0\) for fixed \(p\) as \(a\to\infty\); separate-prime gaps do not settle the cross-prime/Archimedean completion.
- Status: **finite exact theorem + corroborating examples**, not RH progress by itself.

### [PV-2026-005] Prime/pole boundary-layer strong convergence — in-repo theorem, PNT dependence

**Claim:** at fixed opposite boundary strips of width \(\ell\), the normalized weighted von-Mangoldt point measures converge weakly to \(e^{-w/2}dw\), and the associated Hankel operators converge **strongly** to the rank-one kernel \(e^{-(u+v)/2}\).

- Proof: \`research/aletheia_2026-10-07/PRIME_POLE_BOUNDARY_LAYER.md\` §§1–3, first commit \`b18fbdf018a3010c47b46682cc112aa1c6a63a9d\`.
- External input: classical PNT \(\psi(x)\sim x\); no RH input.
- Independent finite calculations executed: normalized source mass over \(\ell=1.3\) at \(X=100,1000,10000\) was \(1.39699672,1.44359687,1.45690563\), versus predicted limit \(1.45493641\). This illustrates convergence, not a proof.
- Status: **in-repo PNT consequence; third-party audit not claimed**.

### [PV-2026-006] No full \(L^2\)-operator-norm convergence — scoped no-go

**Claim:** the same atomic-to-smooth pole matching does not converge in the \(L^2\) operator norm, despite strong convergence, due to simultaneous recurrence of finitely many atomic phases.

- Proof: \`PRIME_POLE_BOUNDARY_LAYER.md\` §4, \`b18fbdf018a3010c47b46682cc112aa1c6a63a9d\`.
- Standard mathematical inputs: simultaneous Diophantine approximation, Riemann–Lebesgue lemma, strong convergence.
- Claim applies to the **isolated normalized prime boundary Hankel block**, not the entire completed Suzuki operator.
- Status: **scoped in-repo no-go**.

### [PV-2026-007] Quantitative RH-equivalent boundary discrepancy — equivalence, NOT sign theorem

**Claim:** with \(\eta_A(\ell)\) precisely defined in \`PRIME_POLE_BOUNDARY_LAYER.md\` §6, a fixed-window rate \(\eta_A=O(e^{-A}A^K)\) for some finite \(K\) is RH-equivalent.

- Proof dependency: Abel partial summation, telescoping a fixed multiplicative window, classical von Koch equivalence for \(\psi(x)-x\).
- **Status: RH-EQUIVALENT REFORMULATION.** No such rate is proved unconditionally.
- Do not call the equivalence a strict reduction or assert that strong/graph-norm operator convergence implies the RH rate.

### [PV-2026-008] Conductor-entry jet order depends on topology — scoped exact identities

**Claim:** a newly entering translation has cubic correlation onset for smoothly transported Dirichlet states, quadratic control on bounded \(H_0^1\) sets, linear onset on indicator vectors in the logarithmic domain, and an immediate shift-operator norm birth in \(L^2\).

- Proof: \`research/aletheia_2026-10-07/CONDUCTOR_ENTRY_JET_TOPOLOGY.md\`, first commit \`0d8ae3e762dcf9396ad1683338eeafb74327fa29\`.
- **No** universal cubic actualization law follows.
- Status: in-repo local theorem; do not infer the total completed Weil eigenvalues are differentiable at thresholds.

### [PV-2026-009] Bare scalar causal shifts commute, mixed adjoints produce boundary ratios

**Claim:** \(T_hT_k=T_{h+k}\) for \(h,k>0\) on an interval; mixed forward/adjoint commutators are boundary partial shifts with difference displacement.

- Proof: \`research/aletheia_2026-10-07/CAUSAL_SHIFT_BOUNDARY_COMMUTATORS.md\`, first commit \`9da59f800deafe1b5034ccda0d1ffab1bd515783\`.
- **Correction:** forbidden ratio atoms apply to **distinct prime bases**; same-prime ratios may be allowed and must be checked for exact weights. Corrected commit \`b52449857a243395436d80b15ca462c0fc81fcad\`.
- Status: exact scoped algebra, not a global curvature theorem.

## P.4 Critique lineage and blocked extrapolations

### [CRIT-CUBE-2026-10-07] Imported prior audit

- Original file: \`CUBE_ATOM_CRITICAL_AUDIT.md\` in the user's Library; source last-modified metadata **2026-10-07T22:50:43Z**.
- Copy in repo: \`research/audits/2026-10-07/CUBE_ATOM_CRITICAL_AUDIT_IMPORTED.md\`, imported commit \`f2cd6b46b7f5bb5f28352859d91f78d28c3ba318\`.
- **Original author identity unknown from the file's metadata.** User reports Claude criticized the form, but this document is not independently verified as Claude's exact newest review.
- Concrete refutations: \(J_\alpha(d)/L^\alpha\) weights are not gcd-projective; two coherent \(45^\circ\) rotations are not two Markov births; multiplication by \((1-x)\) changes the Mellin multiplier; boundary \(|\Theta|=1\) is insufficient without Hardy invariance; naive reflected features generate forbidden \(\log6\) atoms.
- Exact finite counterexamples independently rerun 2026-10-07: \(L=4\to2\) gives \((1/4,3/4)\neq(1/2,1/2)\); two rotations give occupation 1 instead of 1/2; \(g=e^{-x}\) has \(\mathcal M[(1-x)g](3/2)=-0.44311346\) instead of \(\Gamma(3/2)=0.88622693\); inverse Blaschke boundary unit modulus with upper-half-plane pole.
- Durable reproducer: \`scripts/rh_critical_provenance_controls.py\` committed at \`d12ac11ffd13ca0f48f013bbe347c6a396c544f8\`. **An independent finite reproduction was executed**; do not claim the literal committed script was run through GitHub Actions without logs.

### [CRIT-CLAUDE-R010] Claude's Round 010 self-audit (attributed by branch notes)

- \`claude/arithmetic-curvature-loops-008\` at \`262f3da48793f0a109d73f0878dace0d6be3bdbb\`.
- \`research/claude_round_010/AUDIT_010.md\` documents a prior RH-leak (\(\Psi=O(1)\) treated as unconditional), global positivity mistake for \(A''\), and conflation of scalar prime ramp with tensor factorizations.
- Correct lesson: PNT yields leading \(4\sqrt X\) cancellation only. Positivity/critical-size boundedness of the remaining \(\Psi\) is RH-equivalent.
- That critique pre-dates the 2026-10-07 log-bathtub branch; it is **not** evidence Claude has reviewed the latest operator proofs.

### [CRIT-OLD-CUBE-SHORTING] Scope of 2026-10-07 hostile no-go

- \`research/aletheia_2026-10-07/RH_PROOF_BEARING_FRAME_AUDIT.md\`; branch parent \`audit/rh-proof-bearing-frontier-2026-10-07\`, original commit \`e747956d047987c80e0089e992709c9da2775f88\`.
- Prime-only cubical shorted Grams are \(L^2\)-bounded and cannot equal the ultraviolet-unbounded complete Weil form.
- A scalar adelic product formula does not automatically provide a non-factorizing Hilbert-valued place-response map.
- Finite positive shorting and fake-prime mutation do not establish RH.
- The later zero-extension identity removes the logarithmic boundary obstruction by incorporating it into a canonical source-derived positive square; **it does not solve the signed global positivity gate**.

## P.5 Independent execution record from this audit

Two independent finite suites were executed in an isolated Python environment, **not via GitHub CI**:

- \`/tmp/rh_hostile_check.py\`: actual Toeplitz matrices for \((p,a)=(2,2),(2,3),(3,2),(5,3),(2,.8)\), log-bathtub constants \(n=1,2,4,8,16,100\), and normalized prime-boundary masses for \(X=100,1000,10000\). All assertions passed.
- \`/tmp/rh_cube_critique_checks.py\`: six controls — gcd projectivity failure, coherent-vs-Markov rotation, Mellin multiplier change, inverse Blaschke, synthetic off-line Weil quartet, first \(\omega\)-jet. All assertions passed.

The local \`/tmp\` scripts are independent reproduction artifacts, **not present in this GitHub repo**. The repo contains closely related durable scripts. No GitHub Actions run is claimed.

The derivations proving the infinite statements are in the cited notes, not in the finite tests. These arguments have not been independently refereed.

## P.6 Current proof gate

The one complete-source RH inequality remains:

\[
Q_W^a(v)\ge0
\qquad
\text{for all finite }a>0\text{ and all admissible }v.
\]

Equivalently, via Suzuki's innerness theorem, the required causal transfer must be analytic/contractive throughout its **upper half-plane** for all positive deformation parameters. Real-line modulus 1, finite source positivity, compact resolvent, prime-ray Toeplitz gaps and strong prime/pole PNT matching do **not** supply the missing all-horizon sign.

The strongest mathematically correct operative target in the present branch is the source-derived form

\[
Q_W^a=P_a-D_a
\]

with exact prime/Gamma/pole constants, and the genuinely unpaid question is the sign of the full, horizon-dependent low-energy effective Feshbach operator. **RH remains open.**


## SWS. Completed succ–Weil–Suzuki bridge and exact operator work

**Branch:** `research/succ-weil-suzuki-rigorous-bridge-2026-10-07`. **Parent:** `987a67d891879e966c9e0c7fb533a5dc74f805fd`.  
**First complete bundle:** [`bb92df1e0d29a5e0b5126d7debb2d7b5e2c8731d`](https://github.com/femboy2112/FuckingRH/commit/bb92df1e0d29a5e0b5126d7debb2d7b5e2c8731d). The original source/priority of each component remains as recorded in the detailed registry.

The [new claim-by-claim registry](../../aletheia_2026-10-07/succ_weil_suzuki/PROVENANCE_AND_CLAIMS.md) provides source versions, earlier proof commits, precise domains and quantifiers, performed versus unperformed computations, and authorship. The [round result](../../aletheia_2026-10-07/succ_weil_suzuki/ROUND_RESULT.md) records actual execution. This extends the present ledger and retains its existing corrections.

| Claim | Exact result and truth state | Boundary |
|---|---|---|
| SWS-001 | Synthesized exact path: unilateral arithmetic and LCM events, declared half-density/completion, Weil distribution, triangle/screw kernel, and conductor family | Classical/inherited identities retain source attribution; representation choices are not consequences of a bare analogy |
| SWS-002 | Full derivative \((\|v\|^2-\|H_{\omega,A}v\|^2)/(2\omega)\to Q_W(v)\), polarized on every fixed compact smooth core | Gamma, both elementary factors, origin scalar, and prime events included; no uniform unit-ball assertion |
| SWS-003 | Compactness for \(\omega>0\), distance at least one from the zero-parameter reflection, and divergent normalized defect operator norm | Refutes an operator-norm derivative at zero |
| SWS-004 | Exact Gamma/prime energy minus scalar and odd-rank correction, with even-rank term retained positively | Re-derivation of the credited Round007 energy identity; no claim of first discovery |
| SWS-005 | Closed form/domain/core, compact resolvent, quantitative Bessel/bathtub and rank-one tail bounds, positive compact \(B_A\), and local sign equivalence | Classical methods applied explicitly; \(\|B_A\|\le1\) is not proved generally |
| SWS-006 | Old-support cancellation, elementary exponential lower mass growth, quotient limit one, and impossibility of a uniform strict horizon margin | No PNT/RH used; does not exclude non-strict all-horizon domination |
| SWS-007 | \(Q_W(v)\ge(3/100)\|v\|^2\) for every \(0<A\le1/128\), \(v\in V_A\), with explicit rational bounds | Known small-interval type with a concrete proof; no prime event is active in this range |
| SWS-008 | Durable finite controls and 27 floating-point compressions passed; nine exact rational comparisons passed | No interval eigenvalue enclosure, full-spectrum or RH certificate; no full repo-suite/CI claim |
| SWS-009 | Explicit sufficient finite spectral/tail and block/mixed-term certificate, with proof and correct bound directions | Complete certified inputs have not been constructed at arbitrary horizons |
| SWS-010 | \(D_A\le P_A\) for every \(A>0\), equivalently \(\|B_A\|\le1\) | **Unproved and RH-equivalent** |

The user originated the research framing and authorized repository work. GPT-6 generated the new synthesis, proofs, code, and bounded same-model checks. Commit account attribution is not mathematical authorship; these checks are not external peer review. The current bundle does not re-adopt Round006 passive-Gamma, shifted-ratio/log-derivative, or pole-count/index errors.


