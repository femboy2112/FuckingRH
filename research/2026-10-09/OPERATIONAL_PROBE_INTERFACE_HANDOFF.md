# Operational actualization II — verified research handoff

**Date:** 2026-10-09. **Branch:** \`research/2026-10-09/operational-observability-wavefront\`. **Parent:** \`00a20f5e1fbc27e8c7fb29d3c95c1f3ae1effe9c\` (previous operational research checkpoint). Main at start: \`8505467ea596b0636f73b655c521f50105d8b06e\` (Round 067). No main edits or merge.

**User's controlling interpretation:** SUCC / shadow-SUCC / inverse and FUCC are a *finite operational theory of the conditions under which mathematical relations are derivable, executable, observable and distinguishable*, rather than a Hilbert–Pólya construction in disguise. RH is the adversarial global-case target; source-fidelity and forms must remain unassumed. Do not treat a mathematical truth as ontologically created by observation.

## What was executed

1. Read latest main, \`wiki/07-methodology-and-discipline.md\`, existing \`FINITE_ACTUALIZATION_AND_PROBEABILITY.md\`, prior script, and relevant sibling branches. Used primary Suzuki 2023 paper and DLMF §5.11 for the explicit formula and logarithmic Gamma asymptotic.
2. **Round A — finite joint probes and Mellin lift.** Proved exact-conductor/marginal theorem for h_S and factorized Mellin lift, with analytic zero of order |S|-1 at pole s=1. Independent evaluations via finite periodic Hurwitz series for S of 2,3,4 primes, residual <5e-78 at safe complex test point. Holdout conductor 210 requires four-way joint observations and becomes structurally available by N=7 despite n=210 not visited. **Falsifier:** additive exact-conductor-6 character has Mellin value iπ/3≠0 at s=1; hence conductor is NOT enough to determine jet order.
3. **Round B — source authenticity and spoofing.** F_S(1) catches standalone fake6, α2=1.03, shifted log2=.01, but a balancing fake30 cancels a fake6 in the global Mellin value. Proved a general *m+1 composite Vandermonde* construction defeating any prescribed first m Mellin jets while retaining the nonzero earliest connected-source coefficient at6. Numerically verified m=1..4 with maximum analytic jet residual ≤1.35e-79, and exact coefficientwise triangularity proves the stronger assertion.
4. **Round C — complex character and interface.** Proved Haar centering c=1/p and χ-Euler s=1 centering c=χ(p)/p incompatible whenever χ(p)≠1. Quartic χ mod5, χ(2)=i,χ(3)=-i is the positive source control: with χ-centered probes its Mellin lift has a double zero at1. The matched Davenport–Heilbronn mixture gives nonzero value (0.3076006246009636+0.01384009033587265i) at1 for the **same** χ-centered probe. Independent safe-region χ and D-H results were verified via periodic-30 Hurwitz sums, not zero locations. This is a local analytic source discriminator, NOT GRH or a positive Hilbert metric.
5. **Round D — domain probeability.** DLMF digamma asymptotic and Fourier modulation show for fixed test support L: \`Q_L(phi e^{iTx})=||phi||² log T+O(1)\`, while every fixed finite family of bounded L² linear sensor outputs tends zero; after projection away from any finite family of **smooth test vectors**, the readings can be exactly zero while the energy still grows. This is a value/topology NON-CONTROL theorem, not a theorem of RH unknowability and not a witness of Q's negativity. Numerical illustration with C¹ bump, exact norm²=3/4, shows gamma energy rises 0.335→3.468 for T=10→640 while the first four sensor amplitudes fall 0.024→3.6e-8.

## Exact executed-script verification

Both *committed* Python scripts match the Git object hash of the executed local files:

| Script | Git blob SHA | local SHA256 |
|---|---|---|
| \`scripts/operational_probe_arity_mellin.py\` | \`a7d2d4477a3df49555f7851e58665f8d70258d0d\` | \`d01bcb558d3c3a46dbe59040ab166be982ee71cbfae1689fb0e10d5fec00302b\` |
| \`scripts/operational_weil_probe_completeness.py\` | \`e6d9e6ca6771d840595fdf55c1e2ec0d82400217\` | \`d45468c3251af602b8352957b9ba1d889b8c904c63d20e68fba777f853ed4a96\` |

Commands executed locally:

\`\`\`bash
python /mnt/data/actualization_round_20261009/probe_arity_mellin.py
python /mnt/data/actualization_round_20261009/weil_form_probe_completeness.py
\`\`\`

Both returned status PASS, exit code 0. Exact stdout SHA256: arithmetic/mellin JSON \`d29a0f32801d57e5fa52816bad1101a0120abf3f539d14e9e5e8cb580cbba2f3\`; gamma/Weil numerical JSON \`fe9339572dc18c4c30283487404e956f575b5418c8b25efadb7486a14f2cefc2\`. The semantic output JSONs are committed in \`OPERATIONAL_PROBE_ARITY_RESULTS.json\` and \`OPERATIONAL_WEIL_PROBE_RESULTS.json\` (may differ by JSON textual serialization). Python versions used: mpmath 1.3.0, numpy 2.3.5, SymPy 1.14.0 (not needed by these two probes); SciPy installed, version not separately recorded. **GitHub Actions and the entire repo test suite were NOT run.** No zero ordinates were input. The gamma numerical integration is a finite-resolution illustration, not a ball-arithmetic certified inequality.

## Claim ledger and source status

- **PROVED (elementary, classical):** finite CRT marginal arity, centered-probe exact-conductor support, source-independent birth, F_S(s) factorization and |S|-1 jet order *for those probes*, Vandermonde spoof for arbitrary finite jets, scalar Haar/Hecke incompatibility for χ(p)≠1, and fixed-sensor no-control of high-frequency Weil form energy.
- **OBSERVED on separate numerical instruments:** normalized χ/DH values, independent Hurwitz comparisons, 1–4 jet mutation checks, finite-frequency Gamma energy/sensor readings. The analytic claims have direct proofs, not dependent on these outputs.
- **REFUTED:** arbitrary conductor→jet-order; finite Mellin jets→source fidelity; Haar centering = complex-Hecke centering; finite L² probes control Weil energy; “all finite signs are unobservable” as a blanket statement.
- **UNCHANGED:** global Weil positivity \`Q_L>=0\` for all test f,L is RH-equivalent and **unproved**; we constructed NO absolute self-product, NO positive arithmetic polarization, NO RH estimate. Davenport–Heilbronn on the χ-adapted test is a source discriminator, not a proof that multiplicativity by itself forces critical-line zeros.
- **Reconciliation:** main Round 067's “finite/local probes cannot settle global sign” describes absence of a *uniform theorem*, not a universal impossibility for observing individual negative directions. On each fixed finite support L, prime impulses are known for n≤e^(2L), while Gamma/poles remain infinite analytic but computable from the fixed local factor. Strict negative individual tests could in principle be witnessed finitely.

## Most consequential next construction

Develop a **χ⊕barχ matrix-valued observation/retrodiction bundle** whose finite fibers carry physical normalized Haar (so exact conductors and b(d) still have operational meaning), while its covariant Mellin connection implements Hecke-twisted centering and matches the correct conductor/parity-dependent Gamma factor. Specify test core, positive metric independently of zeros, and a source-sensitive trace with **no false primitive impulse at n=6 or ratio at log(3/2)**. Attempt first to disprove existence of an intertwiner implementing BOTH the Haar and Hecke centered covectors with a fixed positive metric. If a candidate survives, prove continuity into the log-Weil form norm and exact full \`P_L-K_L\` identification before considering positivity. A generic isometric dilation or a jet-order match is insufficient. No work was done on this matrix-bundle target yet.

**Verdict:** a substantive, independently verifiable operational-observability gain (especially jet spoofing and scalar-centering incompatibility), but **zero proved new RH sign estimates** and no claim of monotonic progress toward a proof.


## Fifth bounded round — operator multiplicativity versus scalar observability

After the first four rounds, a distinct question was tested: can the SUCC/FUCC operator semantics remain fully multiplicative while a **positive scalar observation** violates Euler connected-source structure?

**Yes, exact theorem** (see \`OPERATIONAL_TWO_SECTOR_REALIZATION.md\`): on C² take \`U2=diag(i,-i), U3=diag(-i,i), U6=U2U3=I\`. For a positive diagonal-algebra state of sector weight t∈[0,1], the scalar observations satisfy \`a6-a2*a3=4t(1-t)\`. Only t∈{0,1} gives a multiplicative character state. Even the rank-one **pure** full Hilbert vector \`(sqrt(t),sqrt(1-t))\` yields this same nonmultiplicative restriction. Thus positivity or full-state purity is NOT sufficient for observable multiplicativity; a character/multiplicative state on the source algebra is the needed constraint. This covariance is exactly the first connected-logarithm defect at 6.

**Davenport–Heilbronn negative control:** its complex weights \`(1-i*kappa)/2\`, \`(1+i*kappa)/2\` produce the known \`1+kappa²=1.080700903...\` defect, but do NOT form a positive state on the two-character algebra: a positive state has purely imaginary expectation of U2, while D-H requires a real nonzero coefficient at 2. **False-positive control:** the perfectly valid positive equal mixture t=1/2 has connected defect 1, so positive-state representability is not an RH or Euler-product certificate.

Reproducible script \`scripts/operational_two_sector_covariance.py\` (SymPy) and actual JSON \`OPERATIONAL_TWO_SECTOR_RESULTS.json\`; the exact locally executed Git blob is \`603b6cd1f6fb421694238004c6297c81daedc8de\`, local SHA256 \`2ea1cb0272fd0d6b3e11ed3cce5fce8f39d31a1cbc71ebdd7ccc26477a006221\`, stdout JSON SHA256 \`1089203c5b12610db3bfdf62c02bc24593a7d89a047b00152eb782fc929eec5f\`. First exploratory SymPy test used structural expression equality \`==\` for an unsimplified polynomial and failed; replacing it with \`simplify(diff)==0\` passed. This was a harness error, not a failed mathematical theorem. No GitHub Actions or complete repo test suite.

**Updated next gate:** construct a Hecke-character/**multiplicative-state** covariant realization on the finite observation filtration; retain nonzero *observable covariance* as shadow history without falsely promoting it to a primitive \`Lambda(6)\` atom. Then attempt a source-derived map into a *form-core* of the completed Archimedean Weil pairing. The first task is identifying a state/probe category whose scalarization reflects the actual Euler-connected projection and whose operator-level history is not erased; this is more precise than adding a generic positive Hilbert-square.
