# Current literature map — refreshed 2026-10-05

This file contains only sources re-checked during the 2026-10-05 consolidation. It is not a complete bibliography.

## Core positivity / semilocal operator line

### Connes–Consani — Weil positivity and Trace formula, the archimedean place
- arXiv:2006.13771
- https://arxiv.org/abs/2006.13771
- Verified claim: develops a Hilbert-space/semi-local trace approach to the Archimedean Weil functional, with prolate/Toeplitz control; the paper explicitly frames the semilocal generalization as RH-bearing.
- Use here: canonical Archimedean positivity control and warning that the full semilocal/all-place step is the hard one.

### Connes–Consani — The Scaling Hamiltonian
- arXiv:1910.14368
- https://arxiv.org/abs/1910.14368
- Verified claim: analyzes a failed Weil-positivity attempt and formulates an operator-theoretic semilocal framework.
- Use here: negative-control provenance; finite-place truncation and positivity do not automatically globalize.

### Connes–Consani — Spectral Triples and Zeta-Cycles
- arXiv:2106.01715
- https://arxiv.org/abs/2106.01715
- Verified claim: very small eigenvalues of fixed-support Weil quadratic forms, prolate spheroidal structure, perturbed spectral triples, numerical reproduction of low zeros.
- Use here: prolate/selection ancestry.

### Connes–Consani–Moscovici — Zeta zeros and prolate wave operators
- arXiv:2310.18423
- https://arxiv.org/abs/2310.18423
- Verified claim: semilocal prolate wave operator; positive part relates to low zeros, negative/Sonin part to UV behavior; stability under enlarging the finite set of places.
- Use here: finite-S functional-analytic host and prolate/Sonin machinery.

### Connes–van Suijlekom — Quadratic Forms, Real Zeros and Echoes of the Spectral Action
- arXiv:2511.23257
- https://arxiv.org/abs/2511.23257
- Verified claim: for a lower-bounded self-adjoint finite-interval convolution operator with a simple isolated lowest eigenvalue and even ground state, the Fourier transform of that ground state has only real zeros; proof uses finite Toeplitz analogues and Hurwitz passage.
- Use here: exact real-zero endpoint for a finite self-adjoint ground-state construction.

### Connes–Consani–Moscovici — Zeta Spectral Triples
- arXiv:2511.22755
- https://arxiv.org/abs/2511.22755
- Verified claim: self-adjoint operators built from Euler products over primes \(p\le x=\lambda^2\); spectra numerically track low zeta zeros. The abstract explicitly states that rigorous spectral convergence as \(N,\lambda\to\infty\) would establish RH; regularized determinants are proposed to converge, after normalization, to \(\Xi\).
- Use here: the closest external match to PWCT-Spectral. The closure/convergence theorem is explicitly open.

## Compact-window / finite-rank Weil line

### Masatoshi Suzuki — Weil's quadratic form via the screw function
- arXiv:2606.09096
- https://arxiv.org/abs/2606.09096
- Verified claim: continuous-function/screw-function treatment unifying earlier Weil-form results; formulates a conjectural limit of finite-interval self-adjoint operators whose eigenvalues are the zero ordinates, without assuming RH.
- Use here: independent confirmation that the wall is finite-self-adjoint \(\to\) global spectral limit.

### Akiva Groskin — A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil quadratic form
- arXiv:2607.02828
- https://arxiv.org/abs/2607.02828
- Verified claim: exact dictionary between finite Galerkin vectors and band-limited Guinand-Weil tests; omitted Archimedean tail is a totally positive Cauchy-Stieltjes increment; gives certified two-sided finite-cutoff rules.
- Use here: exact finite dictionary, tail-order control, and a guardrail against pretending a tiny finite eigenvalue is automatically decisive.

### Marcus Chuk — Weil positivity in compact windows: certified two-sided bounds and a Landau-Widom decay law
- arXiv:2608.24827
- https://arxiv.org/abs/2608.24827
- Verified claim: compact-window positivity reduces to finite PSD; unconditional positive certificate at \(L=0.8\); extremely small upper bounds at larger \(L\); identifies \(T^*=2\pi e^{2L}\) and a Landau-Widom plunge law; naive envelope certification faces a doubly exponential barrier.
- Use here: exact arithmetic/spectral wavefront and proof that the positivity margin collapses brutally with window size.

## Probability / infinite-divisibility line

### Nakamura–Suzuki — On infinitely divisible distributions related to the Riemann hypothesis
- arXiv:2306.08317
- https://arxiv.org/abs/2306.08317
- Verified claim: introduces a function that is a characteristic function of an infinitely divisible probability distribution iff RH is true.
- Use here: PWCT-Lévy endpoint.

### Takashi Nakamura — A complete Riemann zeta distribution and the Riemann hypothesis
- arXiv:1504.03438
- https://arxiv.org/abs/1504.03438
- Verified claim: complete-zeta ratios as characteristic functions and RH-equivalent divisibility conditions.
- Use here: earlier probability-theoretic RH formulations; exact normalization must be distinguished from the 2023 Nakamura-Suzuki construction.

### Martin Wahl — On the mod-Gaussian convergence of a sum over primes
- arXiv:1201.5295
- https://arxiv.org/abs/1201.5295
- Verified claim: mod-Gaussian convergence for a prime Dirichlet polynomial approximating \(\operatorname{Im}\log\zeta(1/2+it)\); complex-plane extension there is conditional on RH.
- Use here: precedent for "Gaussian bulk + arithmetic residual"; do not import the conditional extension as evidence.

## Heat-flow phase boundary

### Rodgers–Tao — The De Bruijn-Newman constant is non-negative
- arXiv:1801.05914
- https://arxiv.org/abs/1801.05914
- Verified claim: establishes \(\Lambda\ge0\). Since RH is equivalent to \(\Lambda\le0\), RH is equivalent to \(\Lambda=0\).
- Use here: exact heat-flow phase-boundary formulation.

## Convolution / small-number boundary control

### Bäsel–Baillie — Sinc integrals and tiny numbers
- arXiv:1510.03200
- https://arxiv.org/abs/1510.03200
- Verified claim: Borwein-type products of sinc functions exhibit exact/near-exact plateau behavior with tiny post-threshold corrections.
- Use here: concrete model of support accumulation reaching a boundary; Fourier side of bounded-increment convolution.

## Absolute/Archimedean host line

### Connes–Consani — The Absolute Twistor Line and the Geometry of the compactified Spec Z
- arXiv:2609.00299
- https://arxiv.org/abs/2609.00299
- Verified claim: constructs an absolute-geometry compactification with an Archimedean component over a signed \(\mathbb F_1\)-extension and a global absolute curve.
- Use here: candidate host geometry only. This source, by itself, does not discharge the required square-host Gram identity plus Hodge-index positivity.

## Source-discipline rule

A literature result may be used as:
- an exact theorem,
- a candidate construction,
- or a statement of an open convergence problem.

These roles must never be collapsed. In particular:
- numerical convergence of finite spectra is not spectral convergence;
- local/finite positivity is not global Weil positivity;
- functional equation / Fourier self-duality is not zero localization;
- Gaussian CLT behavior is not the RH residual.
