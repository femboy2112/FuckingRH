# Computation histories: what a quotient really retains

This is a finite **control model**, not the adele-class groupoid.

## 1. Path category and its free groupoid

Fix objects `{0,...,N}` and a finite directed graph of named arithmetic
macro-derivations e with source s(e), target t(e), and measured abstract
costs `(W(e),R(e),D(e))`. It includes successor paths and may include
alternative evaluations with the same endpoints. Its path category retains
the complete word of derivation labels. Endpoint evaluation sends a word
to its source-target pair and identifies parallel histories only in the
coarse image. The original arrows retain the word.

Adjoin formal inverses and cancel only adjacent `e e^-1`. This gives the
free groupoid of the finite graph. **Its objects/generators are finite, but
its arrow set usually is infinite.** A formal inverse is a bookkeeping
history; it is not a physical inverse algorithm that recovers erased work.

Define on a forward generator

`c(e)=(W(e)-(t(e)-s(e)), R(e), D(e))`,

and on its inverse `c(e^-1)=-c(e)`. Extend by addition along a word.
Cancellation preserves this sum, so c is a well-defined groupoid cocycle.
The endpoint displacement is itself the coboundary of the potential n;
subtracting it normalizes the direct successor baseline. c can distinguish
parallel derivations and nontrivial loops.

For example a direct path `0->4` of W=4 and an alternative of W=6 yield
a closed formal loop with excess-work cocycle 2. Its inverse has -2.
No claim is made that a negative cocycle is negative physical work.

## 2. Two no-go statements often hidden by the word groupoid

**Nonnegative additive work cannot survive inversion.** If an additive
real cocycle on a groupoid is nonnegative on every arrow, then
`c(g)+c(g^-1)=0` forces c=0. Genuine work is nonnegative on the forward
category; its signed extension to the groupoid is a different object.
The absolute reduced-word cost is nonnegative but is only subadditive
under composition, since cancellation can lower it.

**A genuinely finite groupoid has no nonzero real history holonomy.** Every
isotropy element has finite order, so every real additive cocycle vanishes
on loops. Two arrows with the same endpoints differ by a loop; hence their
real cocycle values agree. On each connected component the cocycle is an
endpoint-potential difference. Thus a finite groupoid cannot retain arbitrary
distinct real execution costs as an additive invariant.

These statements are elementary universal theorems, not properties inferred
from one example.

## 3. A genuinely finite action/groupoid control

To retain a limited history signature on a finite object, use

`G_N,m = Pair({0,...,N}) x (Z/mZ)^3`.

An arrow `(a,b,h)` composes with `(b,c,k)` to `(a,c,h+k)`; its inverse is
`(b,a,-h)`. A derivation maps to its endpoints and c modulo m. This is a
finite groupoid with `(N+1)^2 m^3` arrows and a nontrivial group-valued
cocycle. It remembers only the residue of work/history, not its full word
or ordered magnitude. The implementation checks this loss explicitly.

Thus the choices are honest: keep full histories in an infinite arrow
space, keep bounded/residue data in a finite model, or retain a forward
category with irreversible costs. A coarse endpoint quotient alone retains
none of the lost labels automatically.

## 4. Comparison with arithmetic grading

Unique factorization gives the monoid grading `n -> (v_r(n))_r` and
`log n=sum_r v_r(n)log r`. For multiplication histories this is additive.
Successor/addition is not grading-preserving: 2+3=5 creates a new prime
coordinate. The same arithmetic value can have different additive histories,
but its prime factorization is unique. These are different retained data.

An adelic transformation arrow is labeled by an actual rational multiplier
q, with local valuation cocycles; it is not an arbitrary source program
evaluating to q. Factoring q does not retain all programs that compute q.
The product formula kills the sum of local logarithmic cocycles while their
vector can remain nonzero. The corresponding real sum in the finite model
does not create an arithmetic Hilbert metric or a trace pairing.

The only commuting square constructed here is endpoint evaluation together
with additive displacement/cocycle reduction. The stronger square to the
adelic primitive trace space and Suzuki kernel is **UNVERIFIED**; the
precise failures of the proposed radical identification are in
`ADELIC_COMPUTATION_GROUPOID_COMPARISON.md`.
