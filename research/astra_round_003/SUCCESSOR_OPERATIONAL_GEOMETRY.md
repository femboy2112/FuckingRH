# Successor operational geometry: three costs, one declared machine

**PROVED-IN-REPO control model; no RH positivity implication.** Real elapsed
time is never a coordinate. Abstract costs are reproducible after fixing the
semantics; they are not numerically machine-independent invariants.

## 1. Small-step substrate

Values are immutable unary chains built from `0` by `S`. Only allocating
`S(v)` creates a new arithmetic value. Selecting an existing tail, copying a
pointer, dispatching a rule, and inspecting a unary counter are control work.
Those operations do not construct a new numeral by a unit-cost addition or
multiplication. Memory allocation/representation is part of this explicit
model; it is not a claim about hardware.

Use the following loops, with a control charge of one for each pattern match:

```
Add(v,0)      -> return v
Add(v,S(m))   -> Add(S(v),m)
Mul(n,0;v)    -> return v
Mul(n,S(m);v) -> Mul(n,m;Add(v,n))
```

Multiplication starts at `v=0`. Thus Add on existing inputs `(n,m)` uses
`m` successor operations and `m+1` control matches. Mul uses `nm` successor
operations and `nm+2m+1` matches. The executable loop counts are checked
independently of the formulas. Exponentiation can be repeated multiplication;
it is omitted from the finite grammar rather than given an unexplained cost.

For expression trees over `1,S,+,*`, evaluate children once by value, then
apply the loops. A `1` literal costs one successor and one control dispatch.
Each other syntax node costs one dispatch before its primitive loop.
Description length D counts syntax nodes, with no free decimal literals.
For child values n,m and costs `(W,R,D)`, the exact recurrences are:

| Node | Successor work W | Control work R | Description D |
|---|---|---|---|
| 1 | 1 | 1 | 1 |
| S(E) | W(E)+1 | R(E)+1 | D(E)+1 |
| E+F | W(E)+W(F)+m | R(E)+R(F)+m+2 | D(E)+D(F)+1 |
| E*F | W(E)+W(F)+nm | R(E)+R(F)+nm+2m+2 | D(E)+D(F)+1 |

Operand orientation affects work/control even when the value is commutative.
This is why histories cannot be inferred from the endpoint.

## 2. Geodesic and the zero-defect trap

Any computation that constructs unary n from zero must allocate the n
successor nodes along its output chain. Therefore `W>=n`. Induction in the
displayed grammar gives the same lower bound. The direct chain attains W=n.
Consequently `min_E(W(E)-n)=0` when that chain is allowed. This is a proved
vacuity result, not a proposed arithmetic novelty measure.

For a particular derivation, `W(E)-n` records extra allocated successor work;
R records control overhead; D records description compression. For example,
let `E=S(S(S(1)))`, of value 4. Then `E*E` has value 16, W=24 and D=9,
whereas the direct description of 16 has W=D=16. Compression can therefore
trade description for decompression work in this model.

The finite exact Pareto frontier uses all three coordinates `(D,W,R)`, not
an arbitrary weighted scalar. For each n it exhausts proper positive sums,
proper products, and `S(n-1)`. Identity products by 1 are dominated; no zero
or negative intermediate cancellations are admitted. All child values of
a remaining operation are smaller than n. Induction therefore proves the
dynamic program complete for the declared grammar. Discarding dominated
children is safe because every recurrence is coordinatewise monotone in
their costs. This is restricted-grammar minimality, not Kolmogorov complexity.

## 3. Known controls and representation boundaries

Integer complexity `||n||` minimizes the number of 1 leaves using only +,*.
It is a formula/description problem, not the successor work W. Its classical
bound `||n||>=3 log_3 n` motivates the defect in the atlas. For pure binary
formula trees, D=2||n||-1 at an optimum. Our extra S instruction changes that
description grammar, so we do not equate its D minimum with integer complexity.

An addition chain starts at 1 and reuses earlier computed values through
addition. Its length counts additions, not their unary decompression cost.
No addition step can exceed twice the previous maximum, giving the lower
bound `ell(n)>=ceil(log_2 n)`; the
requested `ell(n)-floor(log_2 n)` is a nonnegative coarse defect. Exact chain
search in the atlas enumerates all sums of earlier entries, not just star
chains. Shared straight-line programs can describe repeated squaring much
more economically than formula trees. Their instruction count is another
cost axis; it does not erase the n-node unary output requirement.

Blum's axiomatic framework distinguishes a program's partial computed
function from a cost function with the same halting domain and decidable
bounded-cost relation. It supports studying abstract cost measures, not a
canonical numerical cost invariant across encodings. Our finite total
grammar is deliberately more restrictive and claims no general speedup or
optimal-program theorem. No raw execution time is substituted for a proof.

Primary controls: Altman's integer-complexity/addition-chain papers are
recorded in `reviews/complexity_sources.json`; Blum, *A machine-independent
theory of the complexity of recursive functions*, JACM 14(2), 322–336,
DOI https://doi.org/10.1145/321386.321395; Allender et al., *On the complexity
of numerical analysis*, https://eccc.weizmann.ac.il/report/2005/037/.
The latter defines division-free straight-line programs; its complexity
results are not premises of any RH arrow here.
The step-counting axioms were checked directly in Blum's own *On the Size
of Machines*, Information and Control 11 (1967), §3, p.261,
https://www.cs.cornell.edu/courses/cs6110/2015sp/docs/Blum-Size-Theorem.pdf.
The exact-cost decision relation there also decides bounded cost by a finite
search. The original JACM DOI did not yield readable full text in this session;
we do not claim to have audited its speedup proof.

## 4. Evidence and boundary

`scripts/successor_geometry.py --limit 64` retains every exact Pareto point
and one witness program. `tests/test_successor_geometry.py` checks the
small-step loops, operand asymmetry, compression tradeoff, Pareto invariants,
and history-cocycle controls. `evidence/successor_frontiers.json` is finite.
The integer-complexity atlas uses a separate implementation/grammar.

Changing a Suzuki event weight leaves these computation costs unchanged.
Therefore no theorem based only on these costs can establish the exact
unmutated scalar reserve. A specific arithmetic-to-Gram map is still owed.
