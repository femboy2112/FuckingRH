# Hostile controls and scope of surviving assertions

Every positive conclusion below is a conditional theorem with its stated
hypotheses. No generic transport identity is presented as an RH certificate.
The complete test suite includes all frozen Round001 controls unchanged.

| Hostile change | What survives | What prevents the false proof |
|---|---|---|
| Duplicate/delete/increase an event | Flat service, ordered nodes, interval convexity, the general transport identities | Actual marginal/capital bounds must be recomputed. Round001 finite-event rigidity excludes unchanged global CND after any nonzero finite mutation. |
| Relocate an event keeping its weight | Positive-kernel constructions on the ordered grid | `H` changes by weight times location displacement; reserve changes. Moving a finite ramp is a nonzero two-ramp perturbation subject to Round001 rigidity. |
| Preserve mass but reassign weights among locations | Total mass, possible positive interpolation | First moments and stop-loss functions change; they are explicitly tested, not inferred from mass. |
| Preserve first two moments | Positive four-node weights for a sufficiently small Lagrange perturbation | Calls cross at two interior nodes, so convex order fails despite both matched moments; exact Bernstein tests. |
| Change only the Gamma linear term by `-eta*t`, eta>0 | A'', A''', concavity of the inverse service branch (with its shifted origin) | Global positivity fails: if Psi-eta*abs(t)>=0, then Psi>=0, hence RH and bounded Psi, contradicting the linear subtraction. Curvature is insufficient. |
| Synthetic off-line zeros with functional symmetry | Symmetry and finite calibration | Frozen Round001 tests detect negative reserve/indefinite kernel. They do not define an actual-prime transport marginal; no arithmetic theorem is inferred from them. |
| Individual ramp/CND and Gaussian-residual false friends | Their exact negative-control formulas | All original tests run unchanged; no new use of a Gaussian quotient or independent ramp Gram is made. |
| Plant a negative tail beyond a finite window | Every earlier finite certificate | No arrow from finite positivity to infinite positivity. The local suite retains this mutation. |
| Give only positive event weights, concave T and eventual recovery | Ordered episode coupling | One incoming atom with arbitrarily large backlog has arbitrarily large drawdown and fixed entry capital; `MARTINGALE_TRANSPORT_COST.md` §4. |
| Replace exact prime weights by a two-moment or density fit | Some coarse distributions and CLTs | Neither conditional stochastic-order theorems nor tower positivity provides the required exact Archimedean compensation. |

The new tower Gram construction is deliberately robust under positive changes
of tower weights **when its linear repair is changed accordingly**. This is
not a counterexample to Round001 rigidity: the repair changes the |t| term
at the origin and is not a finite ramp mutation or a Gaussian repair. Its
aggregate compensation diverges, so it supplies no false global closure.

The primary-source recovery ledger was also attacked with valid overlapping
derivative enclosures. A negative left lower bound was insufficient to certify
a negative derivative; a missing upper-bound guard was exposed. The prefix
sieve is tested independently against integer enumeration, and its Taylor
bounds against direct Arb sums. Floating diagnostics select candidates only.
