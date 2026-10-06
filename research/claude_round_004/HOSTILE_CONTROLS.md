# Round 004 hostile controls applied

Per the mandatory falsification discipline. "Survives" = the structure/claim holds; "kills" = breaks it.

| control | target | result |
|---|---|---|
| zeros-not-input | all constructions | respected; zeros used only as after-the-fact diagnostics (PASCAL_INNOVATION, COMPLETED_SHIFT) |
| moment-matrix ID vs zeros | uniform Pascal G_L | KILLS it as non-circular (G_L == zero-moment matrix, const ratio 1.065 = tail) |
| single-weight mutation | K_{Psi,L} PSD | breaks PSD for large mutation; small mutation stays PSD (continuity) -> C84 corrected |
| finite-place exponent tilt | K_{Psi,L} PSD | shrinking window rad ~ e^{-0.85 T}; not exact-{0} on finite grid (C84 corrected) |
| completed shift | Psi_omega>=0 | breaks for any omega!=0 (cosh growth); set {0} (diagnostic, small-omega masked by truncation) |
| beta!=1/2 (KMS temperature) | affine CRT Gram | schematic formula NOT PSD even at beta=1/2 (state inconsistency) -> caution |
| fake-arithmetic factorization | GCD / Koszul Laplacian | would survive (factorized kernels are PD for any numbers) => confirms RH-inertness |
| pole/prime separation | rank-2 pole isolation | KILLS it (K_Psi - K_E min eig ~ -2e4; entangled) |

Net: the commutative-multiplicative constructions SURVIVE fake arithmetic (hence RH-inert, bad);
the genuine arithmetic structure appears only in objects that mutation breaks (K_Psi itself, the
local sigma_p tightness M_p, the completed shift). A proof mechanism must be mutation-sensitive.
