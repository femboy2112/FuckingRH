# Round 003 theorem dependency DAG

No edge leads from finite correlations or finite PSD to all horizons.
“New” means proved in this repository this round, not an external novelty claim.

| From | To | Status | Required scope / missing premise |
|---|---|---|---|
| Exact Suzuki formula | K_Psi PSD iff RH | PRIMARY-SOURCE THEOREM | Frozen Suzuki convention and hypotheses |
| Complete tower Gram + visibility | K_Psi=K_A+sum K_Dp-M_L B on [0,L] | PROVED-IN-REPO | Exact compact support, no asymptotic substitution |
| All-horizon PSD lifts with c_L<=C | Global CND finite lift, then RH | PROVED-IN-REPO | Full finite-matrix quantifier, continuous Psi and arithmetic Laplace identity |
| Additive successor semantics | W>=n and minimum execution excess zero | NEW LEMMA PROVED THIS ROUND | Declared unary allocation machine |
| Restricted grammar recurrence | Exact finite Pareto frontier | NEW LEMMA PROVED THIS ROUND | Positive trees only; no general program optimality claim |
| Finite history graph | Signed action cocycle on free groupoid | NEW LEMMA PROVED THIS ROUND | Infinitely many arrows allowed; inverse cost signed |
| Finite groupoid + real cocycle | No nontrivial history holonomy | NEW LEMMA PROVED THIS ROUND | Finite isotropy forces loop value zero |
| Unique factorization | Exact old-radius count | PROVED-IN-REPO | Unit included; p2 empty |
| Count + ordinary PNT | Density-one midpoint saturation | PRIMARY-SOURCE THEOREM + PROVED-IN-REPO | PNT used only at its classical strength |
| Decreasing-sum bounds + rearrangement + PNT | Retained first-level mean has coefficient sqrt2-1 | NEW LEMMA PROVED THIS ROUND | Singular omitted endpoint retained; elementary O(log^-1/2) relative error |
| Additional Brun-Titchmarsh bound | Sharper omitted-weight asymptotic | PRIMARY-SOURCE THEOREM + NEW LEMMA PROVED THIS ROUND | Source theorem explicitly cited; no hidden RH estimate |
| Barycentric old cells | Positive common mixture hits two inverse-power target levels | REFUTED | Exact dual v_l-(l/k)v_k separates target |
| Same cells plus log N jet | Common full-weight curvature target at two levels | REFUTED | Log Jensen deficit keeps separator strictly positive |
| Arbitrary positive old tower coefficients | Three equally spaced target levels | REFUTED | Zero variance would require n=p; closed-cone support gap |
| One-level hull condition | Explicit positive scalar amplitude match | NEW LEMMA PROVED THIS ROUND | Sometimes feasible; not an event/Gram representation |
| Level-dependent normalized inverse-power cells | Entire tower amplitudes | REFUTED | Nearest-integer chord lower bound diverges with level |
| Finite endpoint laws | Exact hull, two-point extreme cells and support bounds | NEW LEMMA PROVED THIS ROUND | Caratheodory elimination proved; conic/convex cases separated |
| Positive old Euler tensor partition | Old prime-power connected coefficients | PROVED-IN-REPO | Formal algebra; analytic series only Re(s)>1 |
| Old-support data + ordinary Dirichlet log/derivative | New p-power coefficients | REFUTED | Multiplicative support closure |
| Generic positive partition | Positive primitive coefficients | REFUTED | log(1+z) counterexample |
| Scalar common direction | Finite-dimensional Hilbert radical | REFUTED | Brownian covariance rank unbounded |
| Mod-|t| positive representatives | Pointed order paying Brownian debt | REFUTED | Both nonzero tower class signs have positive lifts |
| Actual CCM radical | Identity-functional/Brownian cancellation preserving pairing | REFUTED | Test vs functional type mismatch; Brownian pairing nonzero |
| Primary semilocal Sonin map | Exact ambient multiplier formula | PRIMARY-SOURCE THEOREM | Finite set of places and specified metric |
| That ambient map | Dp norm increment / uniform inverse bound | REFUTED | Signed discrepancy and divergent exact inverse norm |
| Exact finite complexity tables | Declared finite IC association | CORROBORATED ONLY | Independent exact enumeration + seeded controls; finite observational claim |
| Complexity association | Exact arithmetic PSD map | UNVERIFIED | Weight-sensitive projection and norm identity missing |
| Rational Rayleigh + Arb LDL | Selected finite lift enclosures | PROVED-IN-REPO | Thirteen actual grids, specified mutants only |
| Selected finite lift enclosures | Uniform all-horizon bound | UNVERIFIED | Planted tail refutes inference without an additional theorem |
| Nonlocal primitive/Archimedean operator | Exact pullback with bounded c_L | UNVERIFIED | First surviving construction obligation; no candidate proved |

The new no-go arrows narrow classes of constructions. They do not make the
remaining all-horizon positivity statement logically weaker than RH. The
conditional final arrow is explicit in `PROOF_ATTEMPT_003.md`.
