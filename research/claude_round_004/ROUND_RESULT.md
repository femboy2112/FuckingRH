# Round 004 — Pascal / binomial / Möbius-Hodge / affine attack on an arithmetic B_L

**Status:** RH remains open. Outcome: central commutative-multiplicative route substantially KILLED
(RH-inert), one structural meta-theorem proved, exact local factors constructed, wall sharpened.
Full record: `PROOF_ATTEMPT_004.md`. Dependency map: `THEOREM_DEPENDENCY_DAG.md`.

## CURRENT WALL (final for this round)
Local Route-B factors are exact and manifestly positive (closed-form sigma_p>=0, B_p explicit).
The global problem is now crisp: sum_{p<=e^L} sigma_p(xi) diverges pointwise on the real axis
(~2 sqrt(e^L)); it must renormalize against the pole (a positive atom at IMAGINARY xi=i/2) to the
finite positive zero-measure sum_gamma delta/gamma^2. RH = renormalized real-axis measure >= 0,
uniformly in L (slack-free). No multiplicative/commutative construction reaches this: all are
factorized/RH-inert. The surviving seams are (a) the noncommutative affine Dirac/BC triple / non-diagonal transfer
operator (Berry-Keating/Connes), and (b) a quantitative collapse-rate theorem rad(E_L) <= C e^{-cL}.
Multiple independent routes (Pascal, binomial, Hodge, pre-statistical S_r sectors, affine CRT,
Archimedean) now ALL funnel to this same Berry-Keating/Weil wall -- strong evidence that the wall
is intrinsic, not an artifact of any one construction.

## Checkpoints landed this round (each committed+pushed)
1. Integrated FUCC_IS_PASCAL + PSD_BOUNDARY_CONTINUITY_AUDIT; corrected C84 to the shrinking-window
   statement (reduced K strictly PD; intersection_L E_L={0} conjectured; finite-place-only tilt).
2. Uniform-time Pascal innovation Gram G_L = zero-moment matrix (circular; literal Pascal no-go).
3. Multiplicative binomial Fock J_B is an exact isometry; its contraction = C79 prime-swap (theorem).
4. Mobius = Koszul differential (exact; Lambda=mu*log is discrete exactness); Hodge Laplacian
   factorizes (cross block = commutator = 0) -> RH-inert (no-go).
5. Exact closed-form local operator squares B_p (sigma_p>=0 verified); M_p forced; global residual
   sharpened to real-axis renormalization vs the imaginary-frequency pole atom.
7. Pre-statistical exchange (addendum): ONE diagonal parent A(s)=diag(p^{-s}) gives zeta/1-zeta/
   Mobius/Lambda as four shadows; Pauli exclusion = mu(n)=0 on non-squarefree; ALL S_r/Schur sectors
   of the diagonal parent are symmetric functions of prime zetas = commutative = RH-inert (extends
   C89 to full representation content). Escape = non-diagonal braided/transfer operator (Berry-Keating).
6. Completed shift vs finite-only tilt are different deformations (exponential {0} vs shrinking
   window rad ~ e^{-0.85 T}); affine CRT schematic Gram NOT PSD at beta=1/2 (caution).

## Meta-theorem (the round's main deliverable)
COMMUTATIVE-MULTIPLICATIVE => FACTORIZED => RH-INERT (proved 4 ways: uniform Pascal=zeros, binomial
Fock isometry, Koszul/Hodge factorizes, = GCD kernel C81). RH content needs noncommutative affine
braid V_m S = S^m V_m or the Archimedean place; both are RH-hard (affine not naively positive at
beta=1/2; Archimedean = Weil continuation wall).

## RH status: STILL OPEN.
