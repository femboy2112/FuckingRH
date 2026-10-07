# Cross-pollination note — 2026-10-07

**Status:** research advice only; no RH claim moves.  
**Branch basis:** consolidated `main` state on 2026-10-07.  
**Purpose:** import useful machinery from sibling repositories without importing their conclusions.

## 1. SmartAlgebra should become the exact control universe for the current seam

The current RH program's live wall is global prime–completion cancellation before positivity is formed. SmartAlgebra already contains an exact function-field laboratory in which:

- local place data and global pole terms are separately visible;
- the product formula is exact;
- the completed zeta object has a finite Weil form;
- positivity has an independent geometric source in the curve case;
- deliberately impure reciprocal polynomials produce exact negative directions.

That is almost perfectly shaped as a **model organism** for the unit-basepoint / second-jet idea.

### Proposed control

Construct the analogue of the current place-character jet proposal over a global function field (K=mathbf F_q(C)).

For a nonzero rational function (xin K^	imes), use the exact degree-weighted product formula

[
sum_v operatorname{ord}_v(x)deg(v)=0.
]

Build the finite place-character family and take the same order of operations currently proposed for (mathbf Q):

1. assemble all participating places globally;
2. cancel the first-order/product-formula direction **before** forming the positive object;
3. retain the second-order/cross-place information;
4. compare the resulting finite matrix with the known curve Weil/Gram matrix.

The key discriminator is not “does something PSD appear?” A Cholesky factor of a known PSD matrix proves nothing. The discriminator is:

> **Does the same local construction and global-before-squaring rule recover the known curve Gram form without inserting its positivity?**

Predeclare outcomes:

- **PASS:** an independently defined jet construction yields the known form or a proved congruent form.
- **FAIL:** the construction cannot recover the known form, or requires importing the target positivity.
- **AMBIGUOUS:** it matches finitely many fixtures but no structural identity is proved.

A failure here should kill or sharply narrow the number-field seam. A success would identify which ingredients are genuinely structural and which are artifacts of the (mathbf Q) presentation. It would still not prove RH: the function-field case has finite cohomology and no number-field Archimedean place.

## 2. EPIC supplies a useful decomposition of the seam, not another truth score

The current program has several candidate routes that can agree numerically while failing for different reasons. EPIC's reader separation is useful here if kept literal.

For each proposed finite conductor/Hankel/jet construction, maintain distinct readouts:

- **fiber / identifiability:** which rival constructions remain observationally equivalent on the current finite probes?
- **provenance:** which “independent” confirmations share the same explicit-formula identity, code path, or normalization?
- **transport:** exactly what map carries a local/place object into the common global basis?
- **probe state:** what finite calculation would split the largest live rival class?
- **adequacy:** is the candidate class itself missing the Archimedean/global mechanism?

Do not collapse these into a confidence number. In particular, several derivations of the same matrix identity are not independent evidence for positivity if all inherit the same hidden completion assumption.

## 3. CompilerCompiler / CGPU suggest a realization-witness discipline for finite matrices

A recurring danger in the current line is that a finite matrix “looks like” the desired operator while the semantic map from arithmetic data to that matrix remains informal.

Borrow the realization idea:

[
	ext{arithmetic specification}
longrightarrow
	ext{finite realization}
longrightarrow
	ext{observable operator contract}.
]

Every serious finite conductor realization should eventually carry a **Realization Witness** recording:

- source arithmetic objects and normalization;
- exact lowering map into matrix entries;
- what information is discarded;
- the observation/equivalence relation being claimed;
- conductor/window dependence;
- transport terms;
- verifier used;
- mutation controls;
- the inverse/limit statement still owed.

This would make “finite model of Suzuki's Hankel system” a checkable statement rather than a visual analogy.

## 4. SmartASM contributes the right mutation doctrine

SmartASM's strongest reusable tactic is not compiler-specific: **candidate generation never upgrades proof status; the independent oracle does**.

For the RH finite system, every promising construction should have hostile mutants that are expected to break the target:

- perturb the product-formula weights;
- delete the Archimedean/completion contribution;
- scramble prime-power multiplicities while preserving gross density;
- preserve row norms while destroying the arithmetic alignment;
- shift the conductor/window convention;
- replace the true prime sequence by matched controls.

A construction that remains “successful” under mutations that should destroy the arithmetic mechanism is probably measuring a generic PSD or finite-size phenomenon.

## 5. Concrete next artifact

The highest-value implementation suggested by this cross-pollination is a small exact script/dossier pair, tentatively:

`scripts/function_field_second_jet_control.py`  
`research/.../FUNCTION_FIELD_SECOND_JET_CONTROL.md`

It should operate entirely on exact finite-field / integer data, reproduce a known curve case from scratch, carry at least one impure negative control, and state the exact algebraic identity being tested.

This is a **control experiment for the seam**, not another RH attack branch. If the seam cannot survive in the universe where the answer and the positive geometry are known, it has not earned further number-field complexity.
