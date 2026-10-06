# Proof attempt 002: exact costs, failed constructors, and a positive tower block

**Outcome: scoped route refutations and new repository lemmas. No RH proof
and no claimed strict reduction of the RH-equivalent reserve inequality.**

Frozen parent `77ba6793be220c2fb5c2f0a6c250c54774acb9ea`; all 35 parent tests
passed before edits. Work occurs on `astra/prime-transport-martingale-002`.
Round001's finite-event, Gaussian-residual, ramp and monotone-reserve no-go
results are retained unchanged.

## Hole contract

For every actual recovered episode, let E be its entry reserve, alpha its
balanced prime service measure including the incoming backlog, and lambda
its flat service continuum. T is the inverse exact Archimedean slope. Target:

\[
 \tag{R2}\boxed{\int T\,d\lambda-\int T\,d\alpha\le E.}
\]

Truth state: **UNVERIFIED**. This is exactly `Jq<=Cq` for all recovery
witnesses, hence RH-equivalent. Recasting it as a transport cost is not a
logical-strength reduction. The purpose of this round was to test whether
an independent order/positive-operator theorem supplies (R2).

Known facts: alpha is stochastically smaller than lambda; the two masses
agree but their first service moments differ strictly. Therefore an ordered
coupling exists and a martingale coupling does not. The cost in (R2) is
already the optimal physical W1 cost. Changing the plan cannot lower it.
A valid proof must constrain the **arithmetic marginal cost**, not merely
construct a coupling. An event-weight increase preserves the basic geometry
and defeats generic capital claims, so any sufficient premise must detect it.

## Strongest direct proof chain

1. **Paid.** Start with Suzuki's complete explicit formula `Psi=A−P`.
   Differentiate it distributionally, retain every event and Gamma term,
   and obtain `Y=S−A'` with positive prime jumps.
2. **Paid.** Exact positive curvature on the arithmetic branch gives flat
   service time and concave inverse T. The initial clock is sigma0>0.
   Restricted conjugacy uses a clamp; replacing it by a concave tangent
   extension costs exactly sigma0²/(2c0), leaving capital K0>0.
3. **Paid, analytic input explicit.** The completed logarithmic derivative
   is the Laplace transform of Y up to the exact factor. Landau's theorem,
   functional symmetry and existence of a nontrivial zero exclude either
   eventual workload sign. No terminal active episode remains. This is a
   reconstruction/extension of the primary Part5 mechanism, not RH.
4. **Paid.** Every recovered episode has balanced finite measures alpha,
   lambda with alpha<=st lambda. Their ordered physical transport cost is
   `D=integral Y dt`, and exactly `E−D=Cq−Jq`.
5. **Attempted and blocked.** Martingale coupling fails the mean condition.
   Positive Bernstein interpolation on the node hull is constructible, but
   its output marginal is not automatically the prime marginal; forward
   concave Jensen subtracts capital. Standard Strassen/Kellerer/shadow/MBB
   theorems require order conditions that actual prefixes violate.
6. **Independent repairs tried and refuted.** Minimal Winfinity repair into
   increasing-concave order is explicit. Paying its translating optimizer's
   exact T-cost from K0 fails at q13 (the Lipschitz budget fails at q7).
   Paying minimal one-sided W1 repair from A0 fails at q5. Actual reserves
   at these counterexamples are positive. Restoring all exact positive
   credits turns the latter bound back into the original RH-equivalent M.
7. **FIRST UNPAID LEMMA.** Prove (R2) using an arithmetic-sensitive estimate
   that is not one of the refuted universal order/capital premises. No such
   estimate has been obtained. The surviving pinned-height proposal was
   actually tested beyond 10^10 and refuted at recovery witness
   q=10,381,395,137: slack `[-0.28808 +/- 0.00000562]` for the best
   admissible height. Exact monotonicity of its accumulated overestimate
   explains why recovery conditioning cannot rescue that episode.
8. **Conditional finish only.** If (R2) holds, every episode ends with
   nonnegative reserve; decreasing active portions and increasing idle
   portions, with the proved initial range, give Psi>=0 for all t>=0.
   Suzuki then gives RH. Step 7 is not discharged.

## Prime towers: follow the positive construction to its exact stopping point

In response to the user's added probe, group all powers of each prime.
Write `ell=log p`, `r=p^(-1/2)`, `Mp=ell*r/(1−r)` and
`hp=sum_{k>=1}ell*r^k(abs(t)−k*ell)_+`. Then

\[
 D_p=M_p|t|-h_p=\sum_{k\ge1}\ell r^k\min(|t|,k\ell)
 =\tfrac12\|V_p(t)\|^2
\]

in an explicit direct sum of interval-indicator L2 spaces. Its stationary
screw kernel is exactly the corresponding Gram kernel. The positive Levy
measure is explicit and finite. The coefficient Mp is **necessary and
sufficient** for linear repair of −hp; it is not a disposable normalization.

For X large enough on a fixed compact t-window,

\[
 D_X=M_X|t|-P(|t|),\qquad
 \Psi=A-M_X|t|+D_X.
\]

The sum MX diverges. Hence the direct positive sum diverges, while
`D_X/M_X` tends locally uniformly to `abs(t)`, losing `P/M_X`.
Moreover a complete tower has infinite first service moment even though its
physical first moment is finite. The obvious independent-tower positivity
and integrable-martingale closures are therefore unavailable.

**First unpaid tower lemma:** a separately positive coupled construction
that carries the exact cancellation with A while retaining P. It has not
been constructed. Subtracting the divergent linear term from a CND sum is
not a positivity-preserving operation. This boundary preserves Round001's
no-go results; the new local Gram lemma does not contradict them.

## Single next bounded discriminator

The translating order repair need not minimize its T-cost. Before claiming
that every capital-buffer repair is impossible, solve the following sharper
problem at actual prefixes, beginning with q13. Let delta_j be the already
proved minimal Winfinity radius. Among nondecreasing quantiles z on (0,Sj),
require

\[
 Q_{svc}(b)\le z(b)\le Q_{svc}(b)+\delta_j,
 \qquad \int_0^b z(v)dv\ge b^2/2\quad(0<b\le S_j).
\]

Minimize the independent alteration cost

\[
 \mathcal D_j=\inf_z\int_0^{S_j}
 [\bar T(z(b))-\bar T(Q_{svc}(b))]db.
\]

This is a constrained optimal-transport repair, not a definition by M.
It allows nonuniform upward repairs that the failed translating constructor
excluded. If a certified lower bound gives `Dcal_j>K0` at one actual prefix,
it kills **all** repairs in this bounded-displacement class. A positive finite
result is only feasibility calibration; a universal independent payment
theorem would be needed for RH. This sharper optimization has not been
solved in this round. Arbitrary coupled tower completion remains outside
this bounded class and is not claimed refuted.
