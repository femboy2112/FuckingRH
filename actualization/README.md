# Field-Relative Actualization System

## v0.3 research layer: categorical phenomenology and finite-to-circle duality

The new [categorical/Yoneda guide](YONEDA_GUIDE.md) documents an executable
source-history observer, full and restricted Yoneda, bounded prime-power
probeability certificates, finite co-Yoneda witness transport, and the exact
finite-clock / real-circle torsion pairing. These constructions are mathematically
meaningful independently of the RH program; they do not supply the Weil sign.

Quick demonstration commands:

```sh
python -m actualization yoneda-demo
python -m actualization local-global-demo
python -m actualization probe-budget --a 6 --b 12 --budget 3
python -m actualization probe-budget --lcm-horizon 10000 --budget 10000
python -m actualization circle-demo
```

The mathematical results, counterexamples and next actual RH interface are
recorded in [the categorical research frontier](../research/2026-10-10/CATEGORICAL_YONEDA_RESOURCE_FRONTIER.md),
with [reproducible CI evidence](../research/2026-10-10/CATEGORICAL_YONEDA_EVIDENCE.json).
The observer's agreement with a global description is always relative to its
declared probes, source context and resource budget; it is not a proof of
unobservable global truth.

A **working, bounded Python research engine** for how field-relative steps,
unrealized combinatorial data, contextual observations, and model integration
interact. Python 3.10+, standard library only. No zeta zeros, numerical fitting,
external services, or RH-based boundary conditions enter the package.

This is an implementation of the user's operational specification, not a claim
that mathematical truth is created by observation, that physical time has been
reversed, or that RH/Navier–Stokes has been solved.

## Start here

From the repository root:

```sh
python -m actualization demo --output /tmp/actualization-demo.json --trace /tmp/actualization-trace.json
python -m actualization shadow --horizon 3 --target 6
python -m actualization run --domain modular --modulus 2 --steps 4
python -m actualization run --source chi5 --steps 12 --output /tmp/chi5.json
python -m actualization replay /tmp/chi5.json
python -m actualization reverse /tmp/chi5.json --conjugate --output /tmp/reversed.json
python scripts/audit_actualization.py --output /tmp/actualization-audit
python scripts/mutate_actualization.py --output /tmp/actualization-mutations
```

A persisted trace is **data, not executable Python**. Replay validates the
configuration, exact operations, before/after states, sequence, and hash chain.
An externally stored `--expected-head` pins a particular trace. Hashes detect
changes but are not signatures or proof of external provenance.

## The five requirements implemented

| User specification | Implementation |
|---|---|
| SUCC is one unit step in a declared space; higher constructions attach synthetic basis data | `Frame` supplies the explicit direction; `BasisLift` carries exact finite unitary fiber transport |
| Shadow is unrealized state-space/field data | `ShadowIndex` retains a bounded ordered-factor history DAG; counts and signed projections are separate |
| Preserve field laws and coherent history; finite observation may be lossy | Exact arithmetic, declared norm checks, affine-chart covariance tests, immutable journal records, explicit non-reconstructible `view()` |
| Observation is specific to place, coordinate and context, then propagates into the model | `step()` registers an event; `propagate()` integrates it; predictions are not observed facts |
| Distinguish bare inverse, shadow inverse, global/conjugate causal reversal | `bare_inverse()`, predecessor-witness `shadow_inverse()`, full-state `reverse_last()/reverse_all()`, and coefficient/fiber `conjugated()` |

The distinction at 6 is literal: at N=3 it remains **shadow**, with paths (2,3)
and (3,2), even though its conductor is structurally available. At the step to
N=6 it is **observed**; only after propagation is it **integrated**. Its connected
Euler coefficient then vanishes. A zero connected coefficient does not erase the
observation or its histories.

## Minimal Python API

```python
from actualization import Engine, Frame, Limits, ONE, Scalar, source_at

engine = Engine(arithmetic=True, limits=Limits(max_target=64, max_depth=8))
engine.predict(6, ONE, "Declared multiplicative model; not a direct observation")
for n in range(1, 4):
    engine.advance(source_at(n), context="zeta", probe="coefficient")

six = engine.shadow(6, witnesses=True)
assert six["stage"] == "shadow"
assert six["weight"] == Scalar(-1).data()
assert six["witnesses"]["paths"] == [[2, 3], [3, 2]]

for n in (4, 5):
    engine.advance(source_at(n), context="zeta", probe="coefficient")
engine.step(source_at(6), context="zeta", probe="coefficient")
assert engine.shadow(6)["stage"] == "observed"
assert 6 not in engine.coefficients  # not filed in the model yet
engine.propagate()
assert engine.shadow(6)["stage"] == "integrated"
assert engine.shadow(6)["source"]["connected"] == Scalar(0).data()

copy = Engine.loads(engine.dumps(), expected_head=engine.head)
assert copy.state == engine.state
copy.reverse_all()  # lossless engine uncomputation, not erasure
assert copy.coordinate == (0,)
assert len(copy.records) == 2 * len(engine.records)
```

`advance()` is a convenience for two individual atomic journal operations. If
model integration fails, the raw observation deliberately remains pending;
`reverse_last()` can restore the earlier state. It must not be silently dropped.

## Fields, steps and synthetic bases

`Frame` supports N_0^d, Z^d, Q^d and (Z/mZ)^d with a declared nonzero step. These
are **spaces with operations**, not all fields: Z/mZ is a field only for prime m,
and N_0 has a boundary. A rational vector is not a floating approximation to an
arbitrary continuous field. Additional geometry needs an explicit adapter.

```python
from fractions import Fraction as Q
from actualization import AffineChart, BasisLift, Frame, Engine, I, ONE, Scalar

frame = Frame("Q2", "rational", (Q(1, 2), Q(-2, 3)))
chart = AffineChart((Q(2), Q(-3)), (Q(5), Q(7)))
x = (Q(0), Q(0))
assert chart.point(frame.succ(x)) == chart.frame(frame).succ(chart.point(x))

lift = BasisLift("phase", ((I, Scalar(0)), (Scalar(0), -I)), (ONE, I))
e = Engine(frame, lifts=(lift,))
e.advance(context="local chart")
```

The lift's unitary law is verified exactly before use. This is a **declared
conservation law**, not a derived arithmetic Hodge polarization. Nonunitary
fibers require a different adapter; they are not silently normalized.

In F_2, `0 -> 1 -> 0` revisits a coordinate without revisiting the same event.
The event sequence, field tick, coordinate, context, probe and integrated model
revision are retained separately.

`Operation` and `execute()` record every intermediate point of SUCC, inverse
SUCC, multiplication and partial division. Thus `2 -> 1 -> 2` is executable in
prefix [0,2], whereas `2 -> 4 -> 2` is not. A canceled endpoint expression does
not erase the intermediate execution cost. Structural factor paths in a shadow
are NOT automatically claimed to be prefix-executable trajectories.

## Shadow algebra and resource scope

The implemented arithmetic shadow is one named projection, not a universal
meaning of shadow state. For the set A of **integrated** source labels >=2:

    C_r(n) = number of ordered A-factorizations of n with length r
    W_r(n) = sum of products of their exact source coefficients
    sigma(n) = sum_{r>=2} (-1)^(r+1) W_r(n) / r

The DAG uses a divisor recurrence; witness enumeration is separate. When the
unit and all needed divisor events have arrived, `a(n)+sigma(n)` is the
coefficient of the formal Dirichlet-convolution logarithm. For genuine zeta it
is 1/k at n=p^k and zero at mixed composites. This is classical Euler-product
bookkeeping; see NIST DLMF 25.2.11: https://dlmf.nist.gov/25.2.E11 .

| Target | Earlier shadow weights | Connected value after encounter |
|---|---|---|
| 6 | N=2:0; N=3:-1 | 0 |
| 8 | N=2:1/3; N=4:-2/3 | 1/3 |
| 12 | N=3:1; N=4:0; N=6:-1 | 0 |

At N=4, **five** histories for 12 cancel: three triples contribute +1 and two
pairs contribute -1. Counts remain nonzero. Never use a zero projected weight
as evidence that the underlying shadow is absent.

`Limits` bounds target labels, factor depth, witness expansion, probe cells,
record count and serialized trace bytes. Exhaustion raises a typed error or
returns an explicit `complete=False`; requesting `exact_weight()` on an
incomplete expansion raises. A clipped witness listing does not corrupt a
separately complete aggregate. No full L_N residue space is allocated by the
conductor metadata routine. Default trace budget is 8 MB; no records are evicted
to stay within it. Snapshots take increasing memory: this is an inspectable
finite reference engine, not a scalable persistent database.

Coefficients live in Q(i), encoded as exact rational strings; arbitrary
irrational complex values are not claimed exact. Physical log degrees and the
Weil half-density are retained symbolically, with `clock_contract()` checking
the declared prime coordinates and exponent 1/2. There is no numerical Weil
operator or Gamma solver in this package.

## Observations, predictions and reversal

`predict()` files an explicitly attributed model assumption. It does not create
a source leaf or mark the target encountered. Integration records confirmation
or refutation and preserves the previous assumption in the journal. Repeated
observations at the same coordinate/probe/context can revise the model; a
new context gets a distinct fact key.

- `bare_inverse()`: returns one predecessor coordinate, with natural-boundary
  and modular-domain rules. No state or history is changed.
- `shadow_inverse()`: lists retained predecessor-event witnesses for the
  current coordinate. It does not assert that the coordinate identifies a
  unique past. Cycles provide direct counterexamples.
- `reverse_last()` / `reverse_all()`: uncompute recorded transitions using the
  retained exact before-state and strict causal stack order, appending reverse
  records rather than deleting forward records. This is a reversible software
  embedding by retained history, not a physical microscopic inverse.
- `conjugated()`: conjugates the exact coefficient/fiber data and its transport,
  then replays the same protocol. Applying it twice restores the original
  trace. Combining it with reversal is an operational test, NOT a constructed
  Archimedean antiunitary or absolute-geometric duality.

A `view(last=...)` is explicitly lossy; `Engine.loads()` refuses to reconstruct
from it. A hash-consistent but semantically wrong transition is also rejected.
External authenticity still requires an externally pinned head or signature.

## Tests and remaining proof boundary

The audit fans out into three **subprocess workers**, not independent AI agents:
field/path/covariance, exact shadow/source/probe, and observation/replay/reversal.
An independent recursive path enumerator checks the production DAG. Hostile
code mutants erase context, reverse step direction, discard pending events,
forget coefficient products, certify incomplete histories, skip replay checking,
forget conjugation, and reverse in the wrong order.

No passing local tests imply RH. In particular, a positive mixture of character
sectors can still be a nonmultiplicative scalar source; the engine records that
failure rather than declaring its covariance a prime event. Source admissibility,
field covariance, and reversible software history do not supply the missing
Gamma/polar/form-domain/Weil-sign identification.

Next extension: an explicit arithmetic-to-Archimedean probe transport whose
source trace, form-domain continuity and completed Weil comparison can be tested
against this recorded event history. Do not add a generic positive norm and call
it the RH solution.


## Infinite realization of finite observations (Ind/Yoneda)

The exact, bounded extension in [infinite_realization.py](infinite_realization.py)
is the mathematically precise meaning of an endless coherent arithmetic path:
finite stages L_N=lcm(1,...,N) define a **filtered colimit of Yoneda
representables** that is not representable by any finite integer. Each
finite test j eventually succeeds, but no finite L_N satisfies all j at once.
This is a theorem about an infinite directed diagram, NOT a computation
that executes infinitely many steps.

Try the reproducible standard-library demo:

~~~bash
python scripts/infinite_realization_demo.py --stage 12 --terms 12
python -m unittest discover -s tests/actualization -p test_infinite_realization.py -v
~~~

The same module constructs **certified rational intervals** converging to
pi and e, plus safe-half-plane zeta(s) intervals. It separately exhibits
a positive Hilbert-form limit whose *every finite stage is indefinite*,
and a negative-limit control with the same stagewise signature.
The Gamma bridge tests show that genuine Suzuki wavefront readings
stabilize *exactly* at each fixed event after enough observations.

**Do not infer RH from these mechanisms.** The divisibility-only Ind-object
cannot see a fake n=6 coefficient; zeta's analytic continuation uniquely
determines its zeros, but the universal Weil-positive sign remains open.
Full proofs, provenance, boundaries, and the proposed enriched analytic
transport experiment: [Infinite realization research](../research/2026-10-10/INFINITE_REALIZATION_LIMITS.md).


## Prime-path Gamma successor germs

[gamma_succ_path.py](gamma_succ_path.py) makes a previously missing
distinction executable: scalar evaluation at the reflected point m=1
identifies the finite Euler ratio Z_P(2m)/Z_P(2)^m with 1, but does NOT
identify the two analytic construction paths or their derivatives.
The first displacement jet contains explicit finite prime logarithmic
moments and converges with a proved O(log(P)/P) tail bound.

An independent finite factorial SUCC path has Euler gamma approximation
G_N(z)=N! N^z/(z(z+1)...(z+N)), whose recurrence has finite defect
z(z+1)/(N+z+1), vanishing only in the infinite N limit.
The two-cutoff reflected transport replaces pi using the finite Euler
product and gamma using the finite factorial path; it tends to
zeta(1-2m) from the SAFE Euler half-plane Re(m)>1/2, including m=1.

A deliberately deformed Gamma sharing every factorial integer value and
the SUCC recurrence shows why extra analytic log-convexity constraints
are necessary to determine a unique archimedean continuation. Fake
composite Euler slots preserve scalar cancellation but change the jets:
provenance-sensitive does not mean RH-positive.

~~~bash
python scripts/gamma_succ_path_probe.py --prime-bound 53 --gamma-steps 64
python -m unittest discover -s tests/actualization -p 'test_gamma_succ_path.py' -v
~~~

The [derivation and proof boundary](../research/2026-10-10/SUCC_GAMMA_PRIME_PATH_GERMS.md)
explicitly distinguish classical identities, tested finite readouts,
and the still-open arithmetic-to-Weil fourth gate. No divergent Euler
product at -1 is assigned an ordinary sum or product value.
