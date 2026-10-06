# Round007 theorem dependencies

RH OPEN. Each arrow below has its own status. “New” means proved in this
round's repository notes, not an external priority claim. The constructor
obstructions are complete theorems in their stated classes; they are not
proofs that an arbitrary arithmetic square cannot exist.

| From → to | Status | Hypotheses and proof location |
|---|---|---|
| Unique factorization → unitary valuation relabeling, local FUCC shifts | PROVED-IN-REPO | Classical arithmetic, formalized in VALUATION_LATTICE_GEOMETRY |
| SUCC + valuation basis → stratum currents, graph diagonal, chiral classification | NEW LEMMA PROVED THIS ROUND | Full boundary terms and common core in STRATUM_FLUX, SUCC_HAMILTONIAN_CARRIER, AFFINE_AND_FACTOR_CHIRALITY |
| Same-jet first returns → constant log roof | PROVED-IN-REPO | Deterministic induced map, not point recurrence; PRIME_JET_RETURN_MAPS |
| Factor incidence + SUCC → gcd-supported cross terms | NEW LEMMA PROVED THIS ROUND | Factor label preserved; arbitrary complex weights; FACTOR_CONE_AND_SQRT_WINDOW |
| Fixed factor cone → half-density uniquely | REFUTED | The family J_F X^(-beta) preserves cone/swap while changing amplitudes |
| Forward trace-class transfer → Fredholm determinant 1 | NEW LEMMA PROVED THIS ROUND | Proper increasing carrier grading; RT1 in DYNAMICAL_ZETA_AUDIT |
| Block triangular trace-class transfer → determinant of diagonal blocks only | NEW LEMMA PROVED THIS ROUND | RT2; excludes determinant interaction from forward currents alone |
| Genuine open jet returns → primitive periodic orbit Euler formula | REFUTED | No periodic points; collapsing depths changes dynamics |
| Suzuki explicit formula → centered Weil functional on convolution squares | PRIMARY-SOURCE THEOREM | Suzuki v4 §3.2, (5.15), Theorem 1.2; convention in WEIL_SQUARE_ATTEMPT |
| DLMF digamma difference → positive Gamma difference channel | PRIMARY-SOURCE THEOREM + PROVED-IN-REPO | DLMF 5.9.16 plus Tonelli/Plancherel; smooth compact tests initially |
| Positive event differences + Gamma channel → exact completed residual | NEW LEMMA PROVED THIS ROUND | Test support width <= log N; equation (1) in WEIL_SQUARE_ATTEMPT |
| Exact residual → infinite negative subspace / no finite-rank repair | NEW LEMMA PROVED THIS ROUND | Negative scalar identity + rank-two pole form on L2(I); bounded cross forms for finite-rank first-order perturbations |
| Global multiplier positivity with prescribed prime cosines → d >= 2 S_N | NEW LEMMA PROVED THIS ROUND | Global continuous multiplier, not positivity on just one fixed support window |
| Weil identity on indicators → exact Suzuki residual kernel | PROVED-IN-REPO | Indicators lie in finite Gamma-energy domain; polarization in SUZUKI_PUSHFORWARD |
| Suzuki residual kernel → at least m-1 negative eigenvalues on any m-point grid | NEW LEMMA PROVED THIS ROUND | Distinct positive times <= log N; Brownian Gram strictly positive |
| Small-width test support → explicit unconditional positive Weil lower bound | NEW LEMMA PROVED THIS ROUND | I=(1,1+2^-16); analytic proof plus Arb scalar certificate in CARRIER_OBSERVATION_NO_GO |
| Positive invisible tests → no recovery from fixed integer-log observations | NEW LEMMA PROVED THIS ROUND | Common unrefined point/derivative samples or one cell average at every horizon; arbitrary observation-only postprocessing |
| Coherent nonlocal label mixing + retained continuum input → completed positive Gram | UNVERIFIED | No such map with the required exact identity is constructed here |
| Pointwise kernel convergence of positive Grams → positive limiting kernel | PROVED-IN-REPO | For every fixed finite set and coefficients, pass the finite quadratic sum to its limit |
| Global completed Weil positivity / Suzuki PSD → RH | PRIMARY-SOURCE THEOREM | Full test class / all finite time configurations, not selected grids |
| Finite target PSD or finitely many successful mutations → global positivity | REFUTED as a proof inference | No arrow of this kind is used; planted-tail controls remain inherited |

The strongest completed proof chain is:

    explicit formula + digamma identity
      → exact positive edge energy and exact discrepancy
      → negative identity on a codimension-two test subspace
      → no finite-rank or orthogonal positive completion of this constructor.

It ends at a class obstruction, not at RH. The alternative observation
chain is even independent of the choice of internal discrete operator.
Its escape hypothesis is genuine refinement or a retained continuum sector.

## Parent dependency corrections

PARENT_AUDIT retains Schur–Vitali, the source correlation, and the exact
Archimedean identity. It does not import passive Gamma, index one from a
single pole, positivity of a shifted ratio from xi'/xi, or the universal
arbitrary-boundary no-go. The last assertion in its stated unrestricted
class is equivalent to not RH. The specific Euler–Maclaurin completion's
failure and infinite negative index are proved with their own hypotheses.

## Role of computation

Exact finite matrices check the operator definitions and expose boundary
mistakes. Arb enclosures certify explicit scalar signs and residual witnesses.
Neither substitutes for the all-dimension proofs above. Same-model audit
agreement is a review, not independent experimental corroboration. No theorem
in this DAG obtains an infinite conclusion by extending a finite scan.
