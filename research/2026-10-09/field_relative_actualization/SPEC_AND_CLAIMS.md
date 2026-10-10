# Field-relative actualization: frozen specification and local claims

Research date: 2026-10-09. Software schema: `field-relative-actualization/1`.
User request: build the finite field-relative actualization framework in the repo.
**This is an executable reference model, not a proof of RH or a theory of physics.**

## User requirements versus engineering choices

The user specified: (1) SUCC advances one unit step in the chosen field/space,
with higher constructions attaching synthetic bases; (2) shadow is unrealized
state-space/field data; (3) preserve the field's conservation laws and coherent
history, with potentially lossy finite observation windows; (4) direct observation
is coordinate/context-specific information which propagates into a model; (5)
distinguish bare inversion, shadow inversion and conjugate/global causal reversal.
They explicitly place 6 in shadow at wavefront 3, weighted by combinatorial
occurrences, and directly actualize it at wavefront 6.

Our choices: exact rational coordinate adapters; exact Q(i) coefficient/fiber
arithmetic; two transactional event phases; finite ordered-factor DAG with a
named Dirichlet-logarithm weight policy; append-only checksummed before/after
records with deterministic replay; declared unitary matrix lifts; bounded witness
and storage budgets. These choices instantiate some finite models of the user's
specification; they are not claims that the user's whole semantic theory reduces
to this particular ring, weight, data structure, or probability law.

## Formal object

A configuration fixes (X,e,F,B,C), where X is a supported exact additive space,
e its nonzero successor direction, F a finite list of declared synthetic fiber
transports, B explicit resource bounds, and C a declared conductor for a natural
arithmetic source when that adapter is selected. The state is

    (coordinate, event_tick, pending_observation, integrated_facts,
     predictions, integrated_source_coefficients, fiber_values).

The journal is a separate finite sequence. Its sequence number is not identified
with a field coordinate or with event_tick. A step creates an observation; filing
it is another operation. A complete reverse changes the active state while
preserving the increasing audit journal. The arithmetic shadow is a deterministic
bounded function of the integrated source data and configuration, hence can be
reconstructed without storing every expanded witness as an independent record.

## Local claims and proof sketches

**FRA-1 — history versus coordinates (demonstrated).** On Z/mZ with successor +1,
coordinate 0 repeats after m steps. Distinct journal event numbers retain the
encounters separately. No map depending on coordinate alone can identify which
encounter occurred. Exact tests use moduli 2,3,5,6,11.

**FRA-2 — contextual observation is not propagation (implemented contract).** The
`step` transition registers coordinate, tick, frame, context, probe, value and
unique event id, but leaves source leaves and model facts unchanged. `propagate`
files it and updates those objects exactly once. Failure of model integration
preserves the pending raw event. Prediction is a different journal action and
cannot create an observed coefficient.

**FRA-3 — bounded shadow recurrence (demonstrated).** Let A contain only integrated
labels >=2. For n<=B, length-r histories have counts

    C_1(n)=1_{n in A},
    C_r(n)=sum_{d|n, d in A, 2<=d<n} C_{r-1}(n/d), r>=2.

Their coefficient-product sums satisfy the same recurrence with the additional
factor a(d). Induction on n, then r, proves the DAG counts every ordered history
exactly once (partition by its first factor). Consequently the alternating
length weight (-1)^(r+1)/r is exactly the formal convolution logarithm when all
required events and the unit have been integrated. A separate longest-feasible-
path recurrence marks depth truncation without using numerical cancellation.
The recursive witness oracle is an independent implementation, not an independent
source of arithmetic truth. A product of previously available labels is a
structural path, not automatically a position-prefix-executable program.

**FRA-4 — source locality (demonstrated).** A coefficient at n depends only on
observations at divisors <=n; predictions and future source-provider values
are never queried by the DAG. Two providers agreeing through event N produce
identical traces and shadows through N. A fake a(6)=1+delta first creates
(log_*a)(6)=delta. A true unitary prime value and zero at a declared ramified
prime are distinguished using the conductor. These are finite degree-one
consistency checks, not classification of all global L-functions.

**FRA-5 — coordinate covariance and explicit conservation (demonstrated in the
implemented model).** For an invertible diagonal affine map g(x)=Ax+b on Q^d,
g(x+e)=g(x)+Ae. The unit direction transforms. For each declared unitary matrix
M over Q(i), ||Mv||²=||v||² by M* M=I. Nothing asserts arbitrary space changes are
physical inertial-frame equivalences or that these laws imply Weil positivity.

**FRA-6 — history uncomputation (demonstrated within the protocol).** Each active
transition stores its exact before-state s and after-state s'. Reverse is
admitted only when the current state is s' and the transition is the latest
active one. It restores s and appends a reverse witness. Induction on the active
stack restores the initial state without erasing records. This is not inversion
from the observed coordinate alone, and is not a physical or analytic
antiunitary construction. Full reverse preflights record and byte capacity.

**FRA-7 — explicit observation loss (implemented and tested).** A view lacks the
schema/configuration and full before/after history needed by replay. It is
rejected as a reconstruction input. Budget exhaustion never evicts history;
truncated shadow weights cannot be promoted through exact_weight().

## Calibrations and failure protocol declared before broad testing

Known targets: the 6,8,12 trajectories; direct encounter versus propagation;
periodic-coordinate history; path 2->1->2 versus 2->4->2; genuine zeta/chi5;
source mutation at 6; declared unramified |alpha_2|!=1; shifted symbolic log2
and half-density; exact CRT mixed-probe means; replay and conjugation involution.
Fresh tests: conductors to 256; all targets 2..48 at source prefixes 1..12;
random exact complex coefficient tables and targets through 64; rational frame
covariance in dimensions 1,2,3,7; byte-budget failure; rehashed but semantically
invalid histories; dropped and reordered records; cyclic revisits.

Hostile code mutations provide falsifiers, not theorem proofs. The first run
exposed a float-input exception mismatch. The first mutation audit exposed a
confounded context test (both context and probe were changed). Both were corrected
and the failed outputs preserved. The N=4 shadow of 12 has FIVE witnesses with
zero total weight; an earlier explanatory count of four was corrected before
the broad tests.

## Claim boundary

Implemented/tested: the finite mechanics above, typed limits, source-locality,
replay, context-sensitive model revision, shadow combinatorics, explicit inverse
notions and finite character controls. Unproved/unbuilt: a global semantic
ontology, a lossless completion deciding all truths, arbitrary field/geometry
adapters, physical time reversal, an Archimedean Gamma/Poisson transport,
continuity into the logarithmic Weil form domain, or independent Weil positivity.
No zeta-zero input or all-horizon sign test was used.

Classical source normalization: NIST DLMF 25.2.1 and 25.2.11,
https://dlmf.nist.gov/25.2 . Predecessor repo context is pinned in PROVENANCE.md.
