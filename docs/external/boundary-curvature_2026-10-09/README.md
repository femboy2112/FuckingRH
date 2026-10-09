# Arithmetic-source-preserving Euler-logarithm candidate

**RH and Dirichlet GRH remain open.** This is a local research bundle, not a committed
change to `femboy2112/FuckingRH`. It was prepared from `main@265bf38dfd6af7d5820396f7e80244122a4aa235`.

The candidate is an operator Euler product on a finite logarithmic window:

    F_chi,L = Product_p (I - conj(chi(p)) p^-1/2 T_log(p))^-1
    D_chi,L = [X, log F_chi,L]
    Q_chi,L = P_chi,L - (D_chi,L + D_chi,L*)

The first two equations are constructed and verified from finite Euler algebra, without
zeros as input; `P_chi,L` is the completed archimedean + conductor/pole part
specified by the Weil explicit formula. **Q_chi,L >= 0 is NOT proved**.

The file `research/2026-10-09/ARITHMETIC_SOURCE_BOUNDARY_CURVATURE.md` includes
complete definitions, proofs, mutation controls and a no-go lemma establishing
that the tempting curvature `[D*,D]` is itself necessarily indefinite.

## Execute

From this bundle root, with Python 3 and NumPy installed:

    python -m unittest discover -s tests -p test_arithmetic_source_boundary.py -v
    python scripts/arithmetic_source_boundary.py

These tests exercise pure Dirichlet-convolution arithmetic, the fixed mod-5 odd
Dirichlet character and its Davenport--Heilbronn-like linear combination,
composite mutation at n=6, local amplitude, character compatibility,
logarithmic clock, finite Euler inversion/logarithm, and boundary commutators.

They are not a calibrated test of the full Weil/Gamma operator and cannot
establish RH or GRH. Next do an **independent arithmetic-side Weil-matrix
calibration** using the existing repo's high-precision instrument, holding out
windows and never supplying zeros to the candidate.
