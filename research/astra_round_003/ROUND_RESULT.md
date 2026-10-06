# Round003 result

**RH HAS NOT BEEN PROVED.** This round proves exact moment-cone and
primitive-support obstructions. It does not claim that every possible
complexity-based or adelic approach is impossible, or that the remaining
RH-equivalent uniform-lift problem has been weakened.

Repository: `femboy2112/FuckingRH`. Exact parent:
`da0526716f330ca69df985cdf0c3112082ab1dfc`, tree
`a39a224b498a4afcf344fa0d74053a87af2efb04`. Branch:
`astra/complexity-crests-primitive-003`, created directly from that commit.
The clean parent passed all 78 tests before edits. No branch was merged;
the inherited Round001/002 and Aletheia research dossiers remain unchanged.

## What became a theorem

1. **Two-level cone obstruction.** A common positive mixture of old-state
   barycentric inverse-power defects has `m_l>(l/k)m_k`, whereas the required
   normalized tower target is (1,1). Symmetric cells have a sharper optimal
   separator. Including the actual log N jet preserves the obstruction.
2. **Three-level positive reconstruction rigidity.** Without any barycenter
   assumption, positive old-state coefficients matching three equally spaced
   tower levels would have zero tilted variance and hence support only at
   the missing prime p. An explicit dual separates even the closed cone.
3. **Exact feasible-region results.** Finite endpoint laws reduce to two-point
   barycentric cells. Convex/conic hulls and support bounds are explicit.
   One inverse-half-density amplitude first matches at p11, fails again at
   p19, and matches for every prime p>=23. Level-dependent normalized pure
   inverse-power laws nevertheless cannot match an entire tower.
4. **Critical-scale averaging with the singular endpoint retained.** The
   old-generated midpoint average has leading coefficient sqrt(2)-1 at
   scale p^(-1/2). Qualitative PNT plus rearrangement suffices; the sharper
   rate has its additional short-interval sieve dependency exposed.
5. **Primitive-support theorem.** Formal Dirichlet logarithm, derivative and
   inverse preserve old-monoid support. They cannot create p^k. Generic
   positive tensor data also need not have positive connected coefficients.
6. **Common-mode and groupoid obstructions.** Brownian covariance has full
   rank on every distinct positive grid, despite its scalar function-space
   coefficient. The mod-|t| image of the CND cone is nonpointed. Finite
   groupoids cannot carry nontrivial real additive execution holonomy;
   full histories require an infinite arrow space or a lossy finite model.
7. **Canonical adelic comparison.** The identity repair changes a trace
   functional, whereas the actual radical changes test representatives.
   The known Sonin multiplier has a different signed ambient norm increment
   and no uniform ambient inverse norm. The exact scalar scattering bridge
   remains valid; it supplies no missing positivity theorem.

“New” means proved in this repository round, with no external priority claim.
Full proofs, quantifiers, sources and independent review are linked through
`THEOREM_DEPENDENCY_DAG.md` and `PROOF_ATTEMPT_003.md`.

## What the finite probes say

The exact atlas covers integer complexity through 512 and shortest addition
chains through 128. Its odd-only size-normalized integer-complexity contrast
survives the declared holdout and seeded nulls. Addition-chain separation is
weaker. This is finite descriptive evidence; it would be incorrect to claim
the entire prime-crest intuition disappeared. Changing a Suzuki weight leaves
those complexity statistics unchanged, so they cannot carry the sign alone.

Thirteen actual-prime grids have certified zero Brownian lift, including the
larger horizon N=4096. Six surrogate/mutated grids require a positive lift.
Extra tests detect tower, duplicate-event and Archimedean mutations. An event
planted beyond a grid leaves it exactly unchanged while making a later value
negative. These are calibrated finite probes, not an infinite positivity edge.

The execution Pareto atlas records abstract successor, control and description
costs through 64. It is an exact restricted grammar, not physical timing or a
machine-independent complexity invariant. Direct minimum work defect is
correctly proved trivial and is not promoted as a new number-theoretic label.

## What remains open

No positive old-state dilation was connected to the exact Suzuki Gram kernel.
Common positive scalar moment reconstruction and ordinary primitive extraction
are now decisively unavailable in the stated classes. A surviving route needs
an explicit nonlocal operator with signed/compressed cross terms, a proved
positive pairing, exact spectral locations and amplitudes, and a derived
uniform bound on its Brownian lift.

The single next verdict-changing probe is an explicit one-prime-plus-infinity
compressed Gram pullback, including its full metric discrepancy. It must evade
the moment/support no-go theorems by a declared map rather than by a new name.
Even success there would still owe uniformity over all primes. The exact
global lift bound remains RH-equivalent; no hidden tail estimate is called a
reduction.

## Reproduction and evidence boundary

Run from the repository root:

```sh
pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m scripts.successor_geometry --limit 64 --output research/astra_round_003/evidence/successor_frontiers.json
python -m scripts.prime_moment_cone --limit 101 --output research/astra_round_003/evidence/moment_cone.json
python -m scripts.complexity_crest_atlas --output research/astra_round_003/evidence/crest_atlas.json
python -m scripts.finite_grid_lift --output research/astra_round_003/evidence/grid_lift_certificates.json
python -m scripts.round003_controls
```

All **128 tests pass**, including the 78 inherited tests. Final test output,
package versions, source manifests, exact witnesses and
interval certificates are retained under `evidence/` and `reviews/`.
`SOURCE_MANIFEST.json` records primary-source scope and
`evidence/SHA256SUMS.json` fingerprints the round's code, reports and evidence.
The Round002 beyond-10^10 pinned-tail compressed stream was hash-verified and
its stored negative slack checked; the large sieve was not rerun. No existing
no-go was weakened and no finite sign was promoted to an infinite claim.
Same-model audits are supplementary checks, not independent empirical
replication. Their distinct derivations and the root's corrections are
recorded in `TRIANGULATION_ROUNDS.md`.
