# Hostile controls: arithmetic sensitivity is not positivity

All 184 tests pass, including all 128 inherited tests. The full unedited run
is `evidence/full_tests.txt`. Universal no-go statements are proved in the
theorem notes; these tests independently check formulas, boundary handling,
and explicit separating signs. They do not extend finite PSD to RH.

The scripts use exact integer/rational/SymPy arithmetic and Arb balls for
numerical signs. The primary new sign battery uses 180 bits. No sign verdict
uses a floating-point eigenvalue. The random generator seed is 20261007;
it is a reproducibility seed, not a claim about a later research date.

| Requested control | Exact mutation / comparison | Observed or proved discrimination | Reproduction |
|---|---|---|---|
| 1. Random coprime generators | Seeded composite generators 77,26,15 | Same first-return arithmetic; wrong Mangoldt event measure. Forward determinants still 1, as the no-go predicts. | round007_hostile; round007_return_transfer |
| 2. Fake composite jet | Add 6 with positive weight | Target changes; exact residual identity remains. Collapsed Euler determinant acquires an extra factor. | round007_squares; round007_return_transfer |
| 3. Delete real prime jet/event | Delete the event at 3; omit a generator in return models | Target changes; forward-transfer obstruction survives. No mutated positivity claim. | round007_squares; round007_return_transfer |
| 4. Change log charge to 1 | Same event support, unit charge | Certified weight separation at n=2; canonical residual still has a negative witness. | round007_hostile |
| 5. Change half-density | Exponent 1/3 instead of 1/2; also J_F X^(-beta) family | Arithmetic weights change; cone/swap do not select the exponent. | round007_hostile; round007_factor_cone |
| 6. Break unique factorization | Generators 2 and 4 | Distinct exponent vectors map to 4; explicit nonzero kernel, so the proposed relabeling is not unitary. | round007_hostile |
| 7. Break factor swap | Multiply factor-lift rows a<b by 2 | R L differs from L; compressed energy at n=2 changes from 1 to 5/2. | round007_hostile |
| 8. Destroy SUCC ordering | Carrier order 1,4,3,2,5,6,7,8 | Valuation basis survives; the 2-jet is visited 1,4,2,8 and log-height decreases. | round007_hostile |
| 9. Randomize jet labels | Fixed carrier/heights/events, permuted log charges | Lambda identity fails. A fully transported coordinate relabeling would instead be unitary and is explicitly distinguished. | round007_hostile |
| 10. Change cone slope | Rational slopes 1/3 and 2/3 | Threshold crossings change by exact integer power comparisons. Half-height is geometrically special for swap, not a proof of half-density. | round007_factor_cone |
| 11. Square before coupling | (C-B)* (C-B) versus C*C+B*B | Nonzero forced affine cross terms disappear in the second expression. | round007_squares |
| 12. Project before energy | Swap-odd factor current before/after multiplication projection | Nonzero energy diag(d(n)-1_square) is annihilated after projection. | round007_factor_cone |
| 13. Complete towers independently | At N=32, same prime heads but all depths | Repair mass increases by 2.7480524...; target below log32 stays unchanged because energy/residual changes cancel. Finite depth extension to 1024 checks this independently. | round007_hostile |
| 14. Remove infinite place | Remove linear digamma and positive Gamma difference terms, keep pole/primes | Target changes by a certified nonzero value; negative residual still survives. | round007_hostile |

The statements in this table are intentionally different kinds of result.
Arithmetic identities should fail when their arithmetic data are changed.
A theorem valid for every positive event model should survive such mutations.
That insensitivity condemns the failed constructor's ability to prove the
specific target; it is not evidence that all mutated targets are positive.

## Additional boundary and information controls

* Cropping the affine output to N before squaring gives a different matrix.
  The correct outgoing halo through 2N+1 retains the exact carry Laplacian.
* The r>=m affine regime has a bottom defect projection. Exact checks include
  this regime, not merely an interior block where the defect is invisible.
* The divisor-gated cone has ordinary bulk crossings at 5->6 and 6->7 in
  the factor-2 channel, although neither is its square threshold.
* Restoring unit factors restores nearest SUCC coupling. Removing them
  kills every prime column in the coordinate-graph example.
* Adding reverse jet edges defeats the strict-forward hypothesis but yields
  a continuant and backtracking trace, not the Euler factor.
* Refining a fixed log cell into two cells detects the previously invisible
  zero-average fixture. This explicitly tests the observation no-go's escape
  condition rather than silently claiming it covers all discretizations.
* Independent grid horizons are used for the residual evidence and tests.
  The universal negative-index result follows from the Brownian Gram proof.

## Inherited adversaries remain active

The full suite includes the synthetic off-line functional-symmetry zero
control, positive self-dual Gaussian-mixture counterexample, Gaussian quotient
failure, ramp/CND no-go, duplicate/event/Archimedean mutations, first-two-moment
counterexamples, and planted negative tails. See `test_convolution_controls`,
`test_gram_levy_obstructions`, `test_finite_grid_lift`, `test_round003_hostile`,
`test_service_transport`, and `test_event_dynamics`. These are calibrations
against specific bad inferences, not constructions from zero ordinates.

The sole prime asymptotic used in the new residual discussion is ordinary
PNT to describe S_N~2sqrt(N). No error term or RH-strength estimate is needed
for any obstruction: S_N>=0 and c0<0 already prove the strict negative bulk.

## Reproduce

From the repository root:

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m scripts.round007_geometry
python -m scripts.round007_factor_cone
python -m scripts.round007_return_transfer
python -m scripts.round007_squares
python -m scripts.round007_observation
python -m scripts.round007_hostile
python -m scripts.round007_parent_audit
```

The parent-audit command prints scalar certificates; its primary-source
record is in `reviews/parent_sources.json`. Other new modules write their
declared evidence files. The integration baseline and final run are kept
separately so environmental setup failure is not confused with a theorem test.
