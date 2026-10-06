# Bounded adversarial review: edge square and observation loss

Scope: independent read-only audit of `CARRIER_OBSERVATION_NO_GO.md`,
`scripts/round007_observation.py`, its tests, `WEIL_SQUARE_ATTEMPT.md`, and
`SUZUKI_PUSHFORWARD.md`. No central files were edited by this reviewer.
The conclusions concern the declared constructor/observation classes,
not RH or arbitrary coherent nonlocal operators.

## Findings

The new small-width coercivity proof is sound, with the constants as
written. For `h=1/65536`, `I=(1,1+h)` lies inside `(log2,log3)` and has
width less than every positive prime-event location. Hence all prime
correlations vanish. For `u>=h`, disjoint supports give the exact norm
identity `||tau_u f-f||²=2||f||²`. On `[h,1]`,

\[
 k(u)\ge e^{-1/2}/(2u),
\]

using `1-exp(-2u)<=2u` and `exp(-u/2)>=exp(-1/2)`. Integrating gives
exactly the claimed `exp(-1/2)log(1/h)` coefficient, with no missing
factor of two. The omitted Gamma intervals contribute nonnegative
energy.

For the pole term, separate Cauchy–Schwarz bounds on I give

\[
 |\ell_+f\,\ell_-f|\le h e^{h/2}\|f\|^2.
\]

A sharper bound is `2sinh(h/2)||f||²`, but the stated weaker bound is
valid and sufficient. The script uses `2*gamma_linear()`, which is
exactly `c0=psi(1/4)-log pi`, so its scalar certificate matches the
proved inequality. Independently rerunning the certificate gave

```
[1.3544263302109853398292549335538835383248277762694731 +/- 7.53e-53]
```

at 180-bit Arb precision. `python -m unittest
tests.test_round007_observation -v` passed all three tests. The
polynomial fixture is correctly described only as a finite algebraic
control of the zero-average mechanism; the universal smooth-test
statement is supplied by the analytic proof.

The completed Weil edge-square identity, the exact Gamma difference
multiplier, and the compressed pole/Brownian residual retain the
correct normalizations. The negative-index argument on the orthogonal
complement of the sinh vector is valid for every distinct positive
finite grid inside the fixed support window. The global multiplier
cost argument now states its global positivity hypothesis explicitly;
it does not use a nonexistent constant eigenfunction on a compact
Dirichlet interval. The bounded-cross-term condition on finite-rank
couplings and the exclusion of arbitrary infinite-dimensional coherent
corrections are appropriately stated.

## Two wording/domain corrections requested

1. In the broad observation-first class, identical observations imply
   `T_N f=T_N 0`, not necessarily `T_N f=0`. The latter needs T_N to
   preserve zero (as the actual linear sampling/averaging maps do).
   The strongest stated no-go survives without linearity: any proposed
   recovery based solely on those observations has the same value at f
   and 0 for every N; exact recovery or convergence on all tests would
   require different values, by coercivity. State the zero-preserving
   hypothesis or use this indistinguishability formulation. Similarly,
   the direct indicator kernel's `a_N t u` form presumes the declared
   linear lift after the flat cell averages; arbitrary nonlinear
   postprocessing is excluded by the smooth common-kernel argument,
   not by that rank-one calculation alone.

2. `SUZUKI_PUSHFORWARD.md` writes a formula on `|t|<=log N` with the
   term `-P(t)`. The original arithmetic ramp P is one-sided. Use
   `-P(|t|)` there, declare an even extension explicitly, or restrict
   the displayed assertion to `0<=t<=log N`. The positive-time kernel
   and inertia proof are unaffected.

No further constant, sign, coercivity, or scope defect was found in
this bounded audit. The edge-square result is properly presented as
an explicit general-test/Gamma extension of the earlier Brownian
finite-rank obstruction, not as an external-priority claim or a proof
that every nonlocal square is impossible.

Root resolution: both requested corrections were applied before publication.
The indicator calculation uses the explicitly linear lift; the general
observation-first argument compares f with 0. All ten square/observation
tests were then rerun and passed.
