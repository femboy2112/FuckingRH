# Round002 result

**RH HAS NOT BEEN PROVED.** This round proves scoped transport obstructions
and a positive prime-tower Gram lemma. It does not claim that the remaining
RH-equivalent inequality has become weaker or that all compensated transport
is impossible. “New” means proved in this repository; no priority claim.

Repository: `femboy2112/FuckingRH`. Frozen parent:
`77ba6793be220c2fb5c2f0a6c250c54774acb9ea`, tree
`a8cad1b351706f7f734205ba0fc64bf412b6f97f`.
Branch: `astra/prime-transport-martingale-002`, created directly from that
commit locally and remotely. Parent tree was clean and its 35 tests passed.
No merge of PR #2 or main; no Round001/archive files changed.

## What became a theorem

1. **Exact boundary-aware service transport.** Smooth curvature pushes to
   Lebesgue mass on `[sigma0,infinity)`. T is strictly concave there, but
   its restricted-conjugate clamp is not. A concave extension pays the
   explicit charge `sigma0²/(2c0)`, leaving `K0≈0.0420819619`.
2. **Independent minimal order-repair theorem.** The Winfinity distance to
   the increasing-concave-order cone is the maximal lower-quantile average
   deficit; an upward translation attains it. For actual prime prefixes it
   is an exact finite maximum over their endpoints.
3. **Episode cost rigidity.** Every recovered episode has an ordered
   positive transport from its balanced prime arrivals to flat service.
   Their strictly unequal means exclude a martingale. Their optimal physical
   W1 cost is exactly the drawdown, fixed by the marginals. Selecting another
   coupling cannot pay it.
4. **Bernstein construction and its limits.** Exact prime weights define
   a positive barycentric weighted-binomial kernel on the node hull. Its
   output masses are not automatically those weights. A sharp grid convex-
   order criterion and unavoidable Jensen debit are proved.
5. **Prime-tower Gram lemma.** For each prime,
   `Dp=Mp*abs(t)−hp=sum_k(log p)p^(−k/2)min(abs(t),k log p)` has an explicit
   interval Gram representation and finite positive Levy measure. The linear
   repair `Mp=log p/(sqrt p−1)` is sharp. Positive aggregation diverges;
   normalization tends to the Cauchy exponent `abs(t)`, losing the arithmetic
   residual. Each complete tower has infinite first service moment.
6. **Workload recurrence.** A direct Landau argument excludes either
   eventual sign of Y. The audited Part5 terminal theorem is sound. This
   controls recovery, not reserve positivity, and uses no zero ordinates.

## What was refuted

- Universal uncompensated stochastic, convex, concave and martingale orders
  on the exact prefix laws: earliest failures at q2; reverse increasing-
  convex order first fails at q4, despite its favorable mean inequality.
- Fixed-capital payment for minimal one-sided physical repair fails at q5.
  Winfinity repair's Lipschitz budget fails at q7, and its exact translating
  cost fails at q13. All those actual reserves remain positive.
- Exact uniform-source / prime-marginal / barycentric Bernstein factorization.
  Forward concave Jensen also has the wrong reserve direction.
- The universal claim that positive ordered episode transport plus eventual
  recovery pays its incoming capital. Arbitrarily large single-backlog
  episodes satisfy that geometry and exceed any fixed capital.
- Independent whole-tower summation or finite-first-service-moment closure.
- Part4's promotion of a drawdown software-branch count to a certified strict
  recovery count: a left-derivative upper-sign guard is missing. This does
  not invalidate its conservative positivity bound or prove its reported
  numerical counts false.

The pinned-tail discriminator **refutes the original-entry, height-optimized
constructor at an actual recovery witness beyond 10^10**. Its episode enters
at x=10,275,204,761 and recovers after q=10,381,395,137, before the next event
10,381,395,223. The actual reserve lies in `[0.031213 +/- 0.000000946]`,
while `Cq-Jhat_pin` lies in `[-0.28808 +/- 0.00000562]`. An analytic bound
excludes every admissible height, not just a sampled choice. A separate
monotonicity lemma shows that fixed-anchor pinned excess cannot improve
within an episode. The exact integer stream, interval evidence, and scope
are in `PINNED_TAIL_SLACK.md`. This refutes that sufficient constructor,
not RH, all possible reanchoring schemes, or an eventual claim beyond an
unspecified larger cutoff.

## What remains open

For every actual recovered episode, with incoming capital E and the exact
balanced measures alpha,lambda,

\[
 \boxed{\int T\,d\lambda-\int T\,d\alpha\le E.}
\]

This is still `Jq<=Cq`, hence RH-equivalent. No existing stochastic-order,
nearby-peacock, shadow, or martingale Benamou–Brenier theorem discharges it:
their order/compatibility hypotheses are additional arithmetic obligations.
Nonuniform compensated repair and coupled prime-tower/Archimedean completion
remain unconstructed. The successful local Gram formula has not crossed the
divergent-compensation obstruction.

## Verification and review boundary

All **78 tests passed** on the final Round-002 tree. The full suite includes
all frozen parent controls plus symbolic, rational,
Arb, independently sieved, and source-ledger tests for this round. Raw outputs
and environment are retained in `evidence/`; rerun:

```sh
python -m unittest discover -s tests -v
python scripts/service_transport.py --limit 31 --shifted --output /tmp/service_transport.json
```

The large pinned calculation has a separate documented reproduction command.
Its fresh beyond-10^10 candidate and arithmetic enclosures were built
independently of the source episode diagnostics. The root independently
reproduced 471,600,819 primes plus 10,251 higher powers at the recovery
witness with a structurally different prime-counting method. Candidate-selection floating point is never
a sign certificate. The full external positivity run through 10^10 was not
rerun. All finite positivity statements retain their finite scope.

The principal thread derived the transport and order accounting. Bounded
forks audited primary sources, Bernstein obstructions, prime towers and the
pinned discriminator. A separate read-only proof audit caught and corrected
one derivative-sign typo; the extrema and counterexamples were unaffected.
Same-model collaboration is supplementary scrutiny, not independent empirical
replication. All surviving proof obligations are explicit in
`THEOREM_DEPENDENCY_DAG.md` and `PROOF_ATTEMPT_002.md`.

## Single next verdict-changing probe

Compute a rigorous lower bound for the **minimal nonuniform upward order
repair cost at the optimal Winfinity radius**, beginning with q13; the exact
variational problem is in `PROOF_ATTEMPT_002.md`. A value above K0 refutes the
entire bounded-displacement upward-repair class, extending the present
translation no-go. Feasible finite repairs would be calibration only; an
all-episode arithmetic payment theorem would still be required.
