# Round 004 — Pascal / binomial / Hodge attack on an arithmetic B_L

**Status:** IN PROGRESS. RH remains open.

Central question: can K_{Psi,L} = B_L^* B_L with B_L built directly from arithmetic
(SUCC/FUCC=Pascal, Euler/Mobius, affine braid, Archimedean), without diagonalizing
K_Psi, assuming PSD, or inserting zero ordinates?

## CURRENT WALL
STRUCTURAL THEOREM EMERGING (proved across 3 routes): every COMMUTATIVE MULTIPLICATIVE
construction is factorized and RH-inert --
  - uniform Pascal innovation Gram = zero-moment matrix (circular);
  - binomial Fock J_B is an isometry (J^*J=I, trivial Gram);
  - Koszul/Hodge Laplacian factorizes (cross block = commutator = 0);
  - == the GCD kernel gcd/sqrt(ab) (C81).
The RH-bearing cross terms survive only as PRODUCTS V_p^*V_q (noncommutative affine
braid V_m S = S^m V_m), never as commutators. Now testing the noncommutative affine/CRT
Gram: does it give genuine non-factorized positive coupling, or also collapse?

## Checkpoints landed this round
- Integrated FUCC_IS_PASCAL + PSD_BOUNDARY_CONTINUITY_AUDIT; corrected C84 to the
  shrinking-window statement (finite reduced K strictly PD; intersection_L E_L={0} conjectured).
