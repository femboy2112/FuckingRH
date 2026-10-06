# What is missing for RH now?

**Date:** 2026-10-05  
**State incorporated:** Astra Round 001 plus the current partial state of \`astra/prime-transport-martingale-002\`.  
**Verdict:** RH remains open.

## 0. What is no longer missing

The program no longer lacks an RH-equivalent target.

Suzuki supplies the explicit arithmetic function \(\Psi\) with

\[
\mathrm{RH}
\iff
\Psi(t)\ge0\quad\forall t
\]

and equivalently

\[
\mathrm{RH}
\iff
K_\Psi(t,u)
=
\Psi(t)+\Psi(u)-\Psi(t-u)
\succeq0.
\]

Nakamura-Suzuki equivalently asks that

\[
e^{-\Psi(t)}
\]

be an infinitely divisible characteristic function.

Nor do we lack an exact finite arithmetic dynamics. Prime powers enter at

\[
a_j=\log q_j,\qquad
w_j=\frac{\Lambda(q_j)}{\sqrt{q_j}},
\]

and on the convex arithmetic branch the reserve has exact prefix state

\[
S_j=\sum_{i\le j}w_i,\qquad
H_j=\sum_{i\le j}w_i a_i.
\]

The exact conjugate reserve is

\[
M_j=H_j-A^*(S_j),
\]

and after the certified initial range,

\[
\mathrm{RH}
\iff
M_j\ge0\quad\forall j.
\]

This is an exact reformulation, not a proof.

## 1. What Round 001 killed

The following shortcuts are no longer live proof strategies in their canonical form:

- independent positive increments for individual prime-power ramps;
- finite event truncations retaining the exact Archimedean completion as global CND approximants;
- Gaussian repair of such truncations;
- the geometric-prime CLT followed by division by its Gaussian factor;
- scalar rescaling/unit-phase repair of that Gaussian quotient;
- a monotone Fenchel reserve;
- support-only/Borwein positivity transfer.

Any new proof must use genuinely nonlocal exact arithmetic coupling.

## 2. What partial Round 002 killed or localized

The service coordinate

\[
\sigma=A'(t)
\]

is exact and useful. It flattens the Archimedean curvature:

\[
A''(t)\,dt\mapsto d\sigma.
\]

Let \(T=(A')^{-1}\) on the convex branch. Then \(T\) is increasing and strictly concave.

For prime service nodes

\[
\sigma_j=A'(a_j)
\]

and cumulative prime mass \(S_j\), the exact service-quantile identity is

\[
M_j
=
K_0+
\int_0^{S_j}
\left[
\bar T(Q_{\rm svc}(b))-\bar T(b)
\right]db,
\]

with the boundary/affine-extension constant \(K_0>0\) fixed explicitly.

However:

- no universal stochastic/convex/increasing-concave order holds between the flat service law and the exact prime service law;
- no exact martingale coupling of the prescribed prefix marginals exists in general because their means mismatch;
- natural fixed-capital convex-order repair certificates fail on small actual prefixes;
- ordinary Bernstein/Pascal positive operators can be built on the prime grid, but their Jensen inequality has the wrong orientation for the reserve and their prescribed-marginal/barycenter conditions are incompatible;
- episode-local ordered transport exists, but its transport cost is exactly the unpaid drawdown, so optimizing the coupling does not reduce the theorem.

Thus standard martingale transport does not solve RH automatically.

## 3. The new positive local object: complete prime towers

For one prime \(p\), with \(\ell=\log p\) and \(r=p^{-1/2}\), the complete event tower is

\[
h_p(t)
=
\ell\sum_{k\ge1}r^k(|t|-k\ell)_+.
\]

The uncorrected tower is not CND.

But the sharp repaired block

\[
D_p(t)
=
M_p|t|-h_p(t),
\qquad
M_p=\frac{\ell r}{1-r},
\]

has an independent positive interval-Gram realization and an explicit positive finite Lévy measure.

This is genuine progress in structure: the correct indivisible local object is closer to a full Euler prime tower than to one prime-power ramp.

But summing the required linear corrections gives

\[
\sum_p M_p=\infty.
\]

The normalized positive aggregate converges only to the universal \(|t|\) object and loses the arithmetic residual.

Therefore the remaining problem is **renormalized global coupling**, not local positivity.

## 4. The current smallest missing theorem

The cleanest scalar statement remains

\[
\boxed{M_j\ge0\quad\forall j.}
\]

But this is merely RH renamed.

A genuine proof must supply an independent structural theorem implying it.

The strongest present description of that missing theorem is:

### Renormalized Prime–Archimedean Coupling Theorem — UNVERIFIED

There exists an arithmetic construction, using the exact Euler/prime data and the Archimedean completion but no zeta-zero locations, which:

1. couples complete finite-place prime towers nonlocally;
2. handles the divergent sharp tower corrections **before** taking the positive limit;
3. makes the cancellation with the Archimedean contribution exact rather than asymptotic;
4. produces an independently positive Gram/CND kernel or a genuine characteristic function;
5. reproduces exactly
   \[
   K_\Psi(t,u)
   \quad\text{or}\quad
   e^{-\Psi(t)};
   \]
6. is mutation-sensitive, hence is not merely a theorem about support, total mass, first moments, Gaussian bulk, or generic convexity.

Proving this theorem would prove RH.

## 5. Why the unit-basepoint insight matters

For each place,

\[
\chi_{v,s}(x)=|x|_v^s
\]

has common value

\[
\chi_{v,0}(x)=1.
\]

The first jets are

\[
\partial_s\chi_{v,s}|_0=\log|x|_v,
\]

and the product formula gives global first-jet balance

\[
\sum_v\log|x|_v=0.
\]

The second and higher jets generate the cross-place products/cumulants that independent Gaussianization discards.

This suggests a possible mechanism for the missing renormalization:

> do not sum positive prime-tower blocks and then subtract the divergent linear corrections. Build the global coupled object at the common trivial-valuation/unit basepoint, where the first-jet balance is exact, and form positivity only after the global cancellation.

This is currently a **program**, not a theorem.

## 6. Three precise proof fronts now worth attacking

### Front A — unit-basepoint global Gram/jet construction

Construct a Hilbert space and arithmetic map \(V(t)\), independently positive, from the global family of place characters/jets, such that

\[
\langle V(t),V(u)\rangle
=
K_\Psi(t,u).
\]

The first-order divergent pieces must cancel globally by construction.

This is the highest-upside route because it could explain both the prime-tower positivity and the Archimedean cancellation.

### Front B — arithmetic compensated service transport

Prove a non-generic, mutation-sensitive theorem controlling the **signed** service-clock transport cost using exact Euler-product correlations.

Generic stochastic orders, martingale existence, and standard Bernstein operators are already insufficient. The missing premise must exploit arithmetic information those generic tools ignore.

In episode language this means independently proving the exact cost-capacity inequality, not renaming it.

### Front C — spectral/absolute-Hodge closure

Independently construct the global positive pairing/spectral limit analogous to the function-field Hodge intersection form or prove the CCM determinant/ground-state convergence strongly enough to reach \(\Xi\).

This remains a separate high-level route and a useful triangulation control.

## 7. What would count as a decisive next lemma?

Any one of the following would materially move the theorem:

1. **Exact global cancellation lemma:** a finite-cutoff identity showing the divergent sum of local tower corrections plus the Archimedean counterterm equals a finite canonical quantity with a positive representation.
2. **Positive jet Gram lemma:** a positive quadratic form built from second/higher place-character jets whose kernel is exactly the screw kernel.
3. **Arithmetic transport domination lemma:** an Euler-sensitive signed-cost inequality strictly stronger than PNT but demonstrably not equivalent to RH by definition, implying \(M_j\ge0\).
4. **Renormalized tower Lévy closure:** positive finite measures/kernels after a coupled (not scalar primewise) renormalization that converge to \(-\Psi\) in a CND-preserving topology.

Without one of these, the remaining statement is still RH itself in another coordinate system.

## 8. Bottom line

The present obstruction is not prime density.

It is not lack of a continuum limit.

It is not lack of Gaussian behavior.

It is not lack of a stochastic-order vocabulary.

It is:

\[
\boxed{
\textbf{we do not yet know how to perform the exact global finite-place/Archimedean renormalization while preserving positivity.}
}
\]

The local finite places can be made positive only after paying a divergent linear correction. The Archimedean completion supplies exactly the kind of global counterstructure that should cancel it, but no noncircular theorem currently performs that cancellation inside a positive Gram/Lévy/transport object.

That is the RH gap as of this note.
