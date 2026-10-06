# Round 004 — Pascal / binomial / Hodge attack on an arithmetic B_L

**Status:** IN PROGRESS. RH remains open.

Central question: can K_{Psi,L} = B_L^* B_L with B_L built directly from arithmetic
(SUCC/FUCC=Pascal, Euler/Mobius, affine braid, Archimedean), without diagonalizing
K_Psi, assuming PSD, or inserting zero ordinates?

## CURRENT WALL
Starting the Pascal innovation Gram experiment: G_L = Pi^{-1} K_{Psi,L} Pi^{-T}.
Next: is G_L structured (sparse/Hankel/prime-localized) and does it survive hostile
arithmetic mutation? If structured -> algebraicize; if dense garbage -> kill literal
Pascal ansatz and move to multiplicative-binomial / Mobius-fermionic routes.

## Checkpoints landed this round
- Integrated FUCC_IS_PASCAL + PSD_BOUNDARY_CONTINUITY_AUDIT; corrected C84 to the
  shrinking-window statement (finite reduced K strictly PD; intersection_L E_L={0} conjectured).
