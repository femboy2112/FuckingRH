# Theorem dependency DAG — Round 006

**RH IS OPEN.** Nodes are this round's results; `[exact]` = verified operator identity, `[no-go]` =
obstruction, `[lit]` = established-literature placement, `[concept]` = conceptual result. Arrows = "feeds".

```
                         Q ⋊ Q^×  on  l²(Q)            [exact: affine braid D_q T_a D_q^-1 = T_qa]
                                   |
                          P_N compression to l²(N)
                                   |
        ┌──────────────────────────┼───────────────────────────────┐
        v                          v                                v
  S,V_p isometries           E_S = I-SS* = [S*,S]            V_p*|n>=|n/p| iff p|n
  [exact]                    = |1><1|  [exact]               [exact: divisibility
        |                          |                          = inverse-FUCC survival]
        |         ┌────────────────┼──────────────────┐             |
        |         v                v                  v             v
        |   Λ_op = Σ(log p)   H_log = Σ(log p)   Π_{p,k}S̃=S^{p^k}Π   v_p = survival depth
        |   V_{p^k}E_S V_{p^k}* V_{p^k}V_{p^k}*   [exact: strat.    [exact]
        |   = diag Λ(n)       = diag(log n)      diagonal]           |
        |   [exact]           [exact]                                |
        |         \                |                                 |
        |          \               v                                 |
        |           \      =========================================>  all diagonal/multiplicative
        |            \     |  = Bost–Connes + Cuntz Q_ℕ  [lit]    |    => RH-INERT (C89, C100)
        |             \    |  H_log = BC Hamiltonian, V_p = μ_p   |
        v              v   |  exclude-0 Nica defect |p-1><1|      |
   B_p = (I-S)(I-p^-1/2 S)^-1 = analytic Toeplitz  [exact]        |
   [BILATERAL_SUCC_TOEPLITZ, C100]                                |
        |                                                          |
        v                                                          v
   INTERSECT BEFORE SQUARING  ---uniform boundary--->  CROSS ~ +2π(N)²  [no-go C101]
        |                                              (common mode amplifies the bulk)
        v                                                          |
   adelic completion: p^-k/2 = √modulus (Tate),  ∏_v|q|_v=1        |
   [exact + lit]                                                   v
        |                                     product formula = modulus identity;
        v                                     does NOT cancel bulk Σ_p M_p  [no-go C102]
   group completion ≠ analytic continuation                       |
   (Bohr–Mollerup / Γ control)  [concept C103]  <------------------┘
        |
        v
   ===================  THE WALL  ===================
   Weil positivity of the completed (signed, prime+Archimedean) explicit formula
   = the Connes gap (no explicit positive B)  =  K_Ψ ⪰ 0  =  RH
   ==================================================
```

## Reading

- **Everything above the wall is exact and RH-inert.** The whole upper DAG is the Bost–Connes/Cuntz
  machine in exact coordinates; by C89/C100 it carries no RH content on its own.
- **Three arrows into the wall are this round's new no-gos:** C101 (uniform-boundary assembly diverges
  quadratically), C102 (product formula ≠ bulk cancellation), C103 (completion ≠ continuation). Each names,
  from a different side, the same missing object: the **signed Weil cross terms / analytic positivity**.
- **No node produces `B`.** The DAG is a proof that this family of moves reaches the Weil wall and stops —
  the honest Round-006 outcome.

## Relation to prior rounds

This DAG is the Round-004/005 wall (C91: Weil positivity of the Cuntz/braid carry trace; C94: the affine
braid is the irreducible core; C98: renormalization is analytic) re-derived from the *invertible parent*
and *enriched* with: the exclude-0 boundary origin of `Λ` (C100/B-C), the quadratic common-mode obstruction
(C101), and the explicit group-completion-vs-continuation diagnosis (C103). Same wall, sharper map.
