# Round008 hostile controls and limits

Proofs, not numerical PSD, carry every universal claim. The following table
records all twenty requested controls. 'Survives' means an identity is
universal under that mutation, which **limits its RH significance**. It is
not evidence that the mutated system satisfies RH.

| Control | Exact outcome / evidence | Consequence |
|---|---|---|
| 1. Random nested modulus refinements | Seed 8008, integer ratios in 2..6: the full common-x determinant still telescopes; `round008_transfer.controls` | Clock algebra does not single out primes |
| 2. Fake composite event | Add q=6 to 2,3,4: the ratio 3/2 acquires both G_23 and G_46 terms; exact rational-key kernel | Prime-power ratio uniqueness is arithmetic, not a generic point-set claim |
| 3. Delete a real event | Delete q=3: the 3/2 atom disappears; Euler denominator and LCM path also change | An unchanged square after deletion cannot equal the same target |
| 4. Mutate Ramanujan projector | Exact divisor/Möbius matrix compared to primitive-character sum | Wrong coefficients lose idempotence/rank |
| 5. Remove Möbius signs | Absolute-Möbius fixture loses idempotence | Signed entries belong to a positive projection; entrywise positivity is irrelevant |
| 6. Change p^-s to p^-alpha*s | Local telescope yields zeta(alpha*s), not zeta(s); exact alpha=2 factor witness | Spectral charge is load-bearing |
| 7. Mutate half-density | Edge remains a square but log(2) versus log(2)/sqrt(2) changes the exact translation atom | Positivity alone does not identify Weil |
| 8. Raw counting versus Haar | Unscaled coordinate pullback has J*J=pI and its alleged projection is not idempotent | Normalization error detected |
| 9. Drop mixed conductors | Rank deficit and finite Fourier noninvariance; L=6 conductor-6 deletion is Arb-detected in theta | Full Poisson coupling requires all sectors |
| 10. Diagonalize primewise before coupling | Unitary basis change preserves all cross terms if carried along; deleting them removes the coherent correction | Diagonalization itself is harmless; discarding matrix entries changes the form |
| 11. Randomize carry phase | Seeded phase conjugation preserves the characteristic polynomial but destroys old-space reduction | Eigenphase multisets do not certify the intertwiner |
| 12. Destroy CRT/tensor compatibility | Omitting the explicit n=a+bL tensor permutation falsifies (B1) | Basis ordering is tested entrywise |
| 13. Remove Gamma | Omits the positive digamma-difference multiplier and its c0 normalization in (W1) | Prime square alone is not the completed form |
| 14. Arbitrary drift | Change oscillator spacing 2 to b: determinant becomes b^(1/2-s/b)sqrt(2pi)/Gamma(s/b) | A generic phase ODE does not derive the required Gamma term |
| 15. Remove inverse orientation | A single tau_a is unitary with no negative translation correlation; centered bilateral difference has exactly the inherited edge square | Orientation helps reproduce the prime sign but does not erase its degree |
| 16. Forward-only transfer | Exact nilpotent 5-state fixture has det(I-zF)=1; inherited trace-class theorem remains active | Clock loops, not chronology alone, make the determinant nontrivial |
| 17. Scalar Euler factors before coupling | Local and full-global factors differ already at q=3; infinite global mismatch certified at s=2 with analytic tail | Euler calibration is not the global determinant |
| 18. Change horizon order | 2-then-3 and 3-then-2 birth-charge products differ as exact rational numbers, although final uncharged clock agrees | Charge history matters; common-x telescope hides it |
| 19. Reorder uncontrolled infinite products | Direct-sum charge operator is noncompact even at one fixed prime; individual eigenfactor absolute sum diverges | Only the proved grouped products may be used; no ordinary Fredholm shortcut |
| 20. Insert zero ordinates | No Round008 constructor uses them; scripts compute from integers, clock matrices, translations, Gamma and Gaussian data | An explicit source audit, not a fictitious numerical mutation |

Additional controls discovered during the round:

- A fixed-L twist is Möbius; the full refinement map has degree p. The exact
  nonlinear scalar closure is a counterexample to an overbroad finite-state
  no-go. A time-varying 2x2 Gamma-phase ODE is another scope control.
- The naive same-embedding Fourier diagram fails already on the constant
  vector by `2-2/sqrt(r)`. A shifted/modulated Gaussian distinguishes Fourier
  orientation; even theta alone cannot do that.
- A positive 2x2 metric with off-diagonal gain `1/epsilon` cancels input
  `(1,epsilon)`. This refutes the boundary-capacity theorem if its cross-block
  restrictions are omitted and saturates its sharpened gain bound.
- The shared-origin atom at log(3/2) has certified coefficient
  approximately `-0.04399976547` for the declared N=3, r=1/2, h=2/3 fixture.
  The analytic proof covers all positive h and 0<r<1 in the stated window.
- The amplitude A_N need not decrease: the evidence increases between N=3
  and N=10. Its limit zero is proved by a geometric-convolution estimate,
  not monotonicity or finite samples.
- The covariant oscillator uses displacement k in its Gaussian return
  trace, whereas the fixed quotient oscillator uses k/L. Confusing these
  would falsely claim refinement compatibility of the original control.

All inherited 184 tests are retained, including previous synthetic/mutated
arithmetic controls. No zero-set symmetry, finite sign sample, PNT error
estimate, or Schoenberg reformulation supplies an unproved arrow here.
S_N divergence needs only Euler's divergence of sum_p 1/p; A_N decay needs
only log(q)/sqrt(q)->0. Neither estimate conceals an RH-equivalent bound.

## Reproduction

Run `python -m unittest discover -s tests -v`. Rebuild the five raw evidence
files with `python -m scripts.round008_NAME --output
research/astra_round_008/evidence/NAME.json`, for NAME in clock, transfer,
gamma, poisson, coupling. Scripts use exact SymPy algebra and Arb balls for
transcendental signs. Matrix fixtures are small; large carrier horizons use
integer LCM dimensions and analytic formulas, not fitted eigenvectors.

Reviews under `reviews/` are bounded same-model adversarial checks. They are
not independent primary sources and do not substitute for the printed proofs.
