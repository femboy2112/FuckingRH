# Height/Tate reversal probe — execution log, claim ledger, handoff

2026-10-09. **RH OPEN.** This file records actual runs, corrections and unrun work, rather than treating a speculative proof program as an established theorem.

## Reconstructed state and instructions

- Verified main parent: f2fe8b3f2e2953061bcc64c51c86521a66e72bcf (Round 064, function-field Rosati Gram and corrected Arakelov claim).
- Existing non-main branch chosen: aletheia/archimedean-dualizing-reversal-2026-10-09, previously at 1790dc9ef6cabda7ebba8382132c2c873dabc44d (draft PR #10). No changes to main; no merge.
- Adjacent UNMERGED: PR #11 28de8c2ecc70c8368d733c893967eb809e0ef0c2 (Tate tori, noncompact 2–6 history cover, L² periodization no-go); PR #9 57aec234b790bcc1b3bbf34fba7c21ddcf080a18 (history-conditioned reversal); PR #8 e96b48f708fc1725548473c2d70a764964f1d287 (Hecke–Tate source).
- Recursive main tree (279 entries) contains no AGENTS.md / CLAUDE.md / CONTRIBUTING.md / INSTRUCTIONS.md. Relevant working instructions are README.md, wiki/07-methodology-and-discipline.md, claim/crucifixion ledgers, and source-audit docs.
- User-origin: entire causal history and environmental record matter for time reversal; finite-to-archimedean comparison should identify structural and dualizing symmetry; conjectural host Hodge sign is the actual RH-bearing gate. Assistant operational repair: specific height-attenuated rational histories mapped to the authentic Tate Gaussian at infinity; NO claim this model was specified by the user.
- Existing correction from R62: commutativity does not imply factorization; raw reflected zero pairing is not automatically |hat g(zero)|²; three arithmetic gates are necessary but insufficient without independent FULL Weil-form sign.

## Hypothesis/test rounds and revisions

### R-A — H1: bounded reversible half-height rational bridge

PREDICTED DIFFERENCES BEFORE TESTING: bounded J_tau at tau=1/2 would require a finite Bessel upper bound; if rational near-unit crowding forces divergence, reject. Exact totient counting and dyadic wedge provide separate analytic probes.

RESULT: REFUTED in the declared wavepacket class. J_tau is bounded iff tau>1. The full Hilbert-Schmidt norm square is 2 zeta(2tau-1)/zeta(2tau)-1, tau>1. Even Bessel boundedness fails for tau<=1 by a coprime near-unit wedge. Positive and negative controls: same threshold with real Tate seed, ordinary Gaussian, and box seed.

REVISED HYPOTHESIS: add genuine arithmetic height regularization (tau>1), then ask if exact multiplicativity and stable reversibility survive.

### R-B — H2: tau>1 retains all rational history and exact multiplications

PREDICTED: Tate wavepackets might become bounded while retaining uniqueness; a loss of injectivity would falsify coherent reconstruction; broken clock should violate intertwining. Direct integral and Gamma Fourier are independent formula/implementation routes.

RESULT: bounded Hilbert-Schmidt, injective, dense range, compact (hence no bounded inverse). Exact cocycle W_qe_r=exp(tau(h(qr)-h(r)))e_qr gives J W_q=T_logq J. But ||W_q||=exp(tau h(q)); q_j->1 of high height prevents a strongly continuous real-flow extension on the OLD source topology. No loss of arithmetic information in exact mathematics; loss of stable inverse.

REVISED: The archimedean completion requires topology change. Next test whether source-dependent gamma polarization earns any Weil sign.

### R-C — H3: the resulting positive Tate kernel equals the completed Weil pairing

PREDICTED: if a candidate Gram is the correct Weil form, it must (i) change with genuine source mutations, (ii) reproduce the unbounded archimedean Gamma energy for high oscillatory tests, and (iii) encode conductor/pole terms. A positive-but-source-blind kernel fails.

RESULT: REFUTED for bounded Gram candidates. Positive K_tau is unchanged by fake n=6 and DH-like mixture; the actual source operator detects b(6)=4ab log6 (for mixture a+b=1). More decisively, on C_c-infinity(-L,L), Q_L(e^{iTu}phi)=(log T)||phi||²+O(1) is unbounded above; a bounded Gram can never be full Weil. Calibrated against the authentic digamma multiplier without zeros.

REVISED: A genuine dualizing/intersection form must live on an unbounded quadratic-form/distributional domain with canonical gamma/pole renormalization, AND must have an independent primitive Hodge-index sign.

## Exact outputs of executed probes (local Python; no repository clone)

RUN 1 (scripts/height_tate_bridge_probe.py, Python 3, numpy, mpmath):

SOURCE-ONLY HEIGHT/TATE BRIDGE — no spectral-zero input
COUNT M=4 states=11 mass=1.735153510233 independent=1.735153510233
COUNT M=8 states=43 mass=2.060379683864 independent=2.060379683864
COUNT M=16 states=159 mass=2.290670453850 independent=2.290670453850
INFINITE HS^2 tau=1.25 2.894744932634
TATE r=1,s=2: direct=0.894427191000, closed=0.894427191000
TATE r=2/3,s=5/4: direct=0.911290199108, closed=0.911290199108
TATE r=17/16,s=33/32: direct=0.999777258044, closed=0.999777258044
GAMMA Fourier t=0: residual=0
GAMMA Fourier t=2.5: residual=8.44e-17
GAMMA Fourier t=14.25: residual=7.36e-17
BOX HOLDOUT M=32: tau=.5 2.558524, tau=1 0.163659, tau=1.25 0.046298
BOX HOLDOUT M=64: tau=.5 5.471285, tau=1 0.221032, tau=1.25 0.054475
BOX HOLDOUT M=128: tau=.5 11.371182, tau=1 0.279491, tau=1.25 0.060388
BOX HOLDOUT M=256: tau=.5 23.091612, tau=1 0.337717, tau=1.25 0.064557
COVARIANCE: 12 exact rational tests PASS
SOURCE mix a=1.0 b=0.0 b6=0.000000000000
SOURCE mix a=0.6 b=0.4 b6=1.720089090459
CLOCK shift log2 eta=0: norm defect=0.000000000000
CLOCK shift log2 eta=0.01: norm defect=0.004901276000
CLOCK shift log2 eta=0.1: norm defect=0.048998193106
CRITICAL limit tau=1.1: normalized mass²=0.650274427 fixed label norm=0.316227766
CRITICAL limit tau=1.01: normalized mass²=0.611904661 fixed label norm=0.100000000
CRITICAL limit tau=1.001: normalized mass²=0.608322198 fixed label norm=0.031622777
ALL CHECKS PASSED (FINITE / DIRECT QUADRATURE; NOT AN RH CLAIM)

RUN 2 (python -m unittest discover -s tests -p test_height_tate_bridge.py -v):
9 tests passed, 0 failures; runtime 0.196s locally. Tests check coprime counting, Gamma/Tate kernel by independent quadrature, character/DH-like connected atom, shifted clock, real rational cocycle, and box-wavepacket holdout. Tested locally against a copy of the exact probe script; the full existing repo suite could NOT be run because the execution container cannot resolve github.com for git clone.

RUN 3 (optional scripts/height_tate_uv_control.py; numpy+scipy; not a required dependency):
T=20  Gamma energy/norm2=1.153764467; log(T/2pi)=1.157855207; residual=-4.090740e-03.
T=50  Gamma energy/norm2=2.073510100; log(T/2pi)=2.074145939; residual=-6.358388e-04.
T=100 Gamma energy/norm2=2.767134860; log(T/2pi)=2.767293120; residual=-1.582592e-04.
T=200 Gamma energy/norm2=3.460400775; log(T/2pi)=3.460440300; residual=-3.952481e-05.
T=400 Gamma energy/norm2=4.153577602; log(T/2pi)=4.153587481; residual=-9.878754e-06.

CALIBRATION INCIDENT (preserved): Initial 60-digit direct x-integral of the Gamma/Fourier seed returned error ~1.94e-32 at t=0, failing a predeclared 1e-40 numerical tolerance due to an integrable endpoint singularity. The test was changed to log-coordinate quadrature (SciPy, then independent dense numpy grid), which matched the closed Gamma formula to 1e-13–1e-17. No failed high-precision run was presented as success.

UNRUN: existing tests outside new nine; GitHub Actions CI; any interval-certified eigenvalue of full Weil form; any actual dualizing-sheaf self-product construction; global ∞-horizon convergence; a proof of RH.

## Compact claim ledger

| ID | Claim | Status | Proof/evidence | Next falsifier |
|---|---|---|---|---|
| HTR-01 | J_tau bounded iff tau>1 for fixed nonzero L² seed; exact HS norm | PROVED | Totient Dirichlet sum + Bessel near-unit wedge | Break wedge estimate or count |
| HTR-02 | Normalized Tate overlap is (cosh log ratio)^-1/2, Fourier is Gamma(1/4-it/2) | PROVED | Direct Gaussian integrals, independent quadrature | Change normalization/convention |
| HTR-03 | J_tau (Tate) injective, dense range, compact noncoercive | PROVED | Finite-measure Fourier uniqueness + total translates | Find nonzero Fourier zero / kernel |
| HTR-04 | W_q bounded invertible, exactly equivariant, ||W_q||=exp(tau h(q)) | PROVED | Height triangle and basis action | Exact rational identity counterexample |
| HTR-05 | No strongly continuous real log-translation extension on old ell² rational basis | PROVED | Dense logQ and nonvanishing shift defects | Counterexample to continuity obstruction |
| HTR-06 | sqrt(tau-1)J_tau -> 0 strongly despite nonzero normalized HS mass | PROVED | Zeta pole, dense finite sequences and uniform boundedness | Incorrect pole normalization |
| HTR-07 | Totient, box/Gaussian, Tate/Gamma, mutations, UV spot values | OBSERVED | Exact outputs above; nine tests | New seed/fresh parameter holdout |
| HTR-08 | Positive Tate Gram itself explains full Weil sign | REFUTED IN SCOPE | Fake-source invariance; boundedness/domain mismatch | A distinct unbounded source-dependent pairing |
| HTR-09 | Full Q_L unbounded above on fixed-window oscillatory tests; no bounded Gram representation | PROVED | Gamma digamma asymptotic, prime shifts bounded, pole oscillatory decay | Wrong term/normalization or domain |
| HTR-10 | A self-product dualizing trace/polarization, source-only, equals full Q_L and independently has Hodge sign | UNVERIFIED / OPEN | Not constructed | Exact adelic intersection and independent sign |
| HTR-11 | Model's convergence/uniqueness gives a quantitative advance toward RH | REFUTED AS INFERENCE | Such properties survive fake arithmetic; no global Weil equality | A new discriminator genuinely tied to Q |

**Dependencies/provenance:** HTR-01–06,09 are local independent derivations but share ONE chosen height/Tate embedding and established analytic facts. Their simultaneous success is NOT independent evidence for RH. The source-literature family is Tate/Connes–Consani; the numerical and proof routes are methodological checks, not independent published validation.

## Next specific attack

A genuinely new instrument would be an unbounded, source-derived adelic Poisson/dualizing transfer on a declared common smooth core. It must explicitly retain finite prime histories and archimedean scaling, have an adjoint fixed by Haar/Serre data, and produce an intersection/trace with the full Weil contact, conductor/Gamma/pole terms. Probe a first mixed two-prime window and check (A) no extra primitive n=6 or log(p/q) impulses, (B) the genuine character vs DH mismatch, (C) unbounded Gamma frequency growth, and (D) a separately proved Hodge-index sign. A future implementation must compare raw and path-adjusted forms without using zeros as inputs; no version of J_tau*J_tau alone can pass.

No main merge requested or performed.


## Continuation R-D/R-E — changed object, tests, falsification (same 2026-10-09 session)

### R-D / H4: can the actual Gamma operator act INTERNAL to rational-height histories?

PREDICTION before probe: if the archimedean Gamma generator A_inf preserves ran J_tau and has a source operator B with A_inf J_tau e_1=J_tau B e_1, then dividing by the nowhere-zero Tate Fourier transform yields the Fourier transform of an **absolutely finite** discrete rational measure. Such transforms are bounded. FALSIFIER: A_inf(t) unbounded. The Γ digamma asymptotic A_inf(t)~log(|t|/(2pi)) proves the falsifier, and g_T belongs to Dom A_inf. Hence A_inf g_T is OUTSIDE ran J_tau, even for source basis e_1. This is HTR-12 **PROVED in the model**, independently of any zeros. Spot test at 0,10,50,100,1000,10000,1e6 corroborated growth; no Γ internal lift exists on that source topology. Pullback J* A_inf J is nevertheless bounded and thus can never reproduce full unbounded Weil Q.

REVISED: change the object, not merely a metric: use a continuum of real-place shifts with a singular Gamma-defined measure on a new quadratic-form domain.

### R-E / H5: exact compensated Gamma continuum, even and odd sources

PREDICTED: the candidate Levy density \(\nu_{\infty,\epsilon}(u)=e^{-(1/2+\epsilon)u}/(1-e^{-2u})\) should yield
\(\Re\psi((1/2+\epsilon+it)/2)-\psi((1/2+\epsilon)/2)
=2\int_0^\infty\nu(u)(1-\cos(tu))du\), for epsilon=0 and 1.
FALSIFIER: wrong digamma normalization in either parity, nonsummable origin, or failure on unseen frequencies.

RESULT: **PROVED analytically** from classical psi integral with v=2u, Plancherel and positive shift-difference norm. Numerical calibrated even t=.25,1,3,10 absolute errors 1.72e-19,1.66e-19,1.08e-19,1.20e-19; odd conductor5 t=.25,1,3,10 outputs .04040896491705772,.4764595239318235,1.486853755915267,2.694881392500945 agree with direct digamma. SciPy x-shift versus Fourier Γ quadratic energy 1.888225660762 on each route, |diff|=4.44e-16. Source term fake n=6 w=.02: exact change -0.01792648010569991 from direct and compensated square. Gamma continuum is real and zero-free, but source-inert in isolation; no Hodge sign.

### R-F / H6–H7: does individual coercivity pay bulk? is the ultraviolet continuum optional?

PREDICTION: if the compensated Gamma and independent prime-shift Poincare bounds force the sign, the symbol lower bound (without pole) should stay ≥0 through known positivity test windows; if small-u jumps are optional, cutting them at ε>0 should preserve the unbounded Γ symbol.

RESULT: Both shortcuts **REFUTED in scope**.
- The independent shift bound a0+gamma_inf(L)−2Σw_n cos(pi/(ceil(2L/a_n)+1)) yields +.7023 at L=.04, +.0093 at .078, then −.0174 at .08 (prime-free!), −1.6300 at .34, −2.1894 at .36, −4.4078 at .8 and −8.1232 at 1.2. These are just conservative lower-bound values, NOT negative full Weil eigenvalues, and OMIT pole. This method does not certify the target positivity.
- For fixed ε>0, truncated jump symbol is bounded by 4∫_ε∞ν, while real Γ symbol is ∼log|t|. Cannot reproduce Γ at high frequency. The infinitely fine archimedean environment is necessary in this model.

REVISED: Build an unbounded *global* source-derived adelic/dualizing trace, retaining discrete prime impulses, continuous singular Γ energy, scalar/contact/pole terms, and a self-product polarizing intersection. A positive generic Lévy form or a summed SOS of independent shifts is not sufficient.

### RUN 4 (actually executed locally after source changes)

Exact Gamma script output:
\`\`\`
ARCHIMEDEAN GAMMA: compensated continuous-shift energy, no zero input
A_inf(0)= -5.37218341922566558
t=0 integral=0.0 Gamma diff=0.0 err=0.0
t=0.25 integral=0.8102885757073178 Gamma diff=0.8102885757073178 err=1.722e-19
t=1 integral=3.347037226122198 Gamma diff=3.347037226122198 err=1.657e-19
t=3 integral=4.627939359485268 Gamma diff=4.627939359485268 err=1.082e-19
t=10 integral=5.836474046090596 Gamma diff=5.836474046090596 err=1.202e-19
ODD gamma / conductor-5 matched source (chi mod5/DH):
odd t=0.25 gamma diff=0.04040896491705772 integral=0.04040896491705772
odd t=1 gamma diff=0.4764595239318235 integral=0.4764595239318235
odd t=3 gamma diff=1.486853755915267 integral=1.486853755915267
odd t=10 gamma diff=2.694881392500945 integral=2.694881392500945
fake n=6 delta=0.0 source change=0.0 SOS-minus-debit=0.0
fake n=6 delta=0.02 source change=-0.01792648010569991 SOS-minus-debit=-0.01792648010569991
ALL FINITE CHECKS PASSED; no positivity inference toward RH
\`\`\`

Actual combined command from locally materialized copies of new files:
\`python -m unittest discover -s tests -p 'test_*.py' -v\`
**14 tests passed in 1.626s** (9 rational-height/Tate tests, 5 Γ continuum tests). Copies of all four test/probe files were individually checked against committed contents; superfluous extra blank line in GitHub main Γ script was normalized to exactly tested bytes. Legacy repo tests and GitHub CI **NOT RUN** due clone DNS/tool environment; no claims of certified interval arithmetic, infinite spectral checks, or zero-spectrum proof.

### Final frontier ledger additions

| ID | Status | Claim |
|---|---|---|
| HTR-12 | PROVED (model scope) | Arch Γ multiplier exits weighted rational-history range even on e_1; cannot be lifted internally into existing source topology |
| HTR-13 | PROVED (classical) | Actual Γ even digamma is a positive compensated continuum of two-sided shifts with 1/u density |
| HTR-14 | PROVED (classical) | Odd parity/q5 Γ factor has analogous density e^{-3u/2}/(1-e^{-2u}) |
| HTR-15 | PROVED | Excluding shifts below ε>0 makes symbol bounded; therefore cannot realize high-frequency Γ |
| HTR-16 | REFUTED (certificate only) | Summing individual Poincare lower bounds does not certify known Weil positivity intervals; full Weil positivity is not refuted |
| HTR-17 | PROVED (identity) | Full zeta Weil form = compensated Γ continuum + discrete prime energies + signed bulk + correct separate pole |
| HTR-18 | UNVERIFIED | Distinguished surface-level dualizing trace and Hodge-index polarization equal complete Q and prove sign |

**Stopping rule:** Further generic positive CND/Lévy/height kernels repeat proved source-blindness; another numerical scan of the same lower bound does not move RH. Needed technology is a genuine source-derived **unbounded** adelic correspondence/dualizing complex with a trace/intersection law and independent Hodge sign. The first discriminating implementation must compare the complete polarized Weil trace in the two-prime interval while enforcing zero connected log6, true χ vs DH and full Γ/pole/negative bulk, before asserting a new theorem.
