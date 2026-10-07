# Actualization curvature: finite theorems and the GR-shaped program

**Date:** 2026-10-07  
**Status:** exact finite structure plus an UNVERIFIED global-curvature program. RH remains open.

## 1. Actualization lattice

Write \(n=\prod_p p^{\alpha_p}\) and order valuation vectors coordinatewise, equivalently by divisibility. At horizon

\[
L_X=\operatorname{lcm}(1,\ldots,X),
\]

the finite support region is

\[
\mathcal A_X
=
\{d:d\mid L_X\}
\cong
\prod_{p\le X}
\{0,\ldots,\lfloor\log_pX\rfloor\}.
\]

Meet and join are gcd and lcm. The squarefree layer is a Boolean prime cube.

A natural causal-order analogue is

\[
J^+(m)=\{n:m\mid n\},
\qquad
J^-(m)=\{d:d\mid m\}.
\]

This is exact finite arithmetic structure, not physical spacetime.

## 2. Support time and shadow support

Define

\[
h(n)=\min\{X:n\mid L_X\}.
\]

Then

\[
\boxed{
h(n)=\max_{p^a\parallel n}p^a.
}
\]

The critical Suzuki conductor seam is

\[
A_{\rm event}(n)=\frac12\log n.
\]

The earliest support time is

\[
A_{\rm supp}(n)=\frac12\log h(n).
\]

Therefore

\[
\boxed{
\Delta A(n)
=
\frac12\log\frac{n}{h(n)}
\ge0.
}
\]

Equality holds iff \(n\) is a prime power.

Thus mixed conductors can exist as latent supported modes before the Suzuki wavefront reaches their own event. For a primorial \(P_r\),

\[
h(P_r)=p_r,
\qquad
\Delta A(P_r)=\frac12\log(P_r/p_r).
\]

This is a precise version of shadow SUCC support.

## 3. Minimal-domino theorem

Let \(L\) be an LCM support state and define

\[
q(L)=\min\{m\ge2:m\nmid L\}.
\]

Then

\[
\boxed{
q(L)\text{ is always a prime power.}
}
\]

Otherwise a proper prime-power divisor of \(q\) would already be a smaller unsupported integer.

Hence the greedy recursion

\[
L_0=1,
\qquad
q_{r+1}=\min\{m\ge2:m\nmid L_r\},
\qquad
L_{r+1}=\operatorname{lcm}(L_r,q_{r+1})
\]

generates the prime powers in increasing order:

\[
2,3,4,5,7,8,9,11,13,16,\ldots
\]

If \(q_{r+1}=p^k\), then

\[
\frac{L_{r+1}}{L_r}=p
\]

and therefore

\[
\boxed{
\log L_{r+1}-\log L_r
=
\log p
=
\Lambda(q_{r+1}).
}
\]

So "actualize the least unsupported object" generates the von-Mangoldt birth stream.

## 4. Bare logarithmic geometry is flat

Assign one unit of \(p\)-depth the edge length

\[
\ell_p=\log p.
\]

For \(m\mid n\), every monotone support path has total length

\[
\sum_p(v_p(n)-v_p(m))\log p
=
\boxed{\log(n/m)}.
\]

Thus bare logarithmic path length is endpoint-only.

On normalized finite clock spaces

\[
H_L=L^2(\mathbb Z/L\mathbb Z,\mu_L),
\]

pullback refinement commutes:

\[
\boxed{
J_{pL,pqL}J_{L,pL}
=
J_{qL,pqL}J_{L,qL}.
}
\]

Bare prime-refinement plaquettes therefore have trivial holonomy.

\[
\boxed{
\text{support growth alone is not curvature.}
}
\]

## 5. Minimal state change and innovation

At \(L\to pL\), the genuinely new information is

\[
W=H_{pL}\ominus JH_L.
\]

Any updated state decomposes as

\[
\boxed{
\Psi_{\rm new}=J\Psi_{\rm old}+\eta,
\qquad
\eta\perp JH_L.
}
\]

If actualization imposes an affine constraint set \(\mathcal C\), the least-change update in a declared Hilbert metric is

\[
\Psi_{\rm new}
=
\operatorname{Proj}_{\mathcal C}(J\Psi_{\rm old}).
\]

If two dressed constraint projections fail to commute,

\[
[P_p,P_q]\ne0,
\]

two locally minimal updates produce different endpoints. This is a concrete mechanism by which local least motion can create loop holonomy.

Bare congruence projectors are the flat control. Carry/history dressing must supply any noncommutativity.

## 6. Exact Suzuki light cone

The critical parity system is

\[
(\partial_A-\partial_X)\Psi=\mu(A)\Chi,
\]

\[
(\partial_A+\partial_X)\Chi=\mu(A)\Psi.
\]

Its principal symbol is

\[
P(\xi_A,\xi_X)=\xi_AI-\xi_X\sigma_3
\]

and

\[
\boxed{
\det P=\xi_A^2-\xi_X^2.
}
\]

The null characteristics are

\[
\boxed{
A\pm X=\mathrm{constant}.
}
\]

This is an exact flat \(1+1\) causal cone.

The scalar mass \(\mu(A)\) is lower order and does not alter the cone. Local similarity changes preserve it as well. Therefore

\[
\boxed{
\mu(A)\text{ alone is not metric curvature.}
}
\]

## 7. SU(1,1)-type Lorentzian transfer

After Fourier transform in \(X\),

\[
\partial_AV=M(A,z)V,
\]

with

\[
M(A,z)=iz\sigma_3+\mu(A)\sigma_1.
\]

For real \(z,\mu\),

\[
\boxed{
M^\dagger\sigma_3+\sigma_3M=0,
\qquad
\operatorname{tr}M=0.
}
\]

Hence the transfer satisfies

\[
\boxed{
T^\dagger\sigma_3T=\sigma_3,
\qquad
\det T=1.
}
\]

The parity system therefore has an exact indefinite/Lorentzian connection structure of SU(1,1)-type.

This does not identify arithmetic coordinates with physical spacetime.

## 8. Genuine curvature requires transverse directions

The one-form

\[
\mathcal A=M(A,z)\,dA
\]

has only one base direction. Path ordering can be nontrivial, but a curvature two-form needs transverse directions.

Restore the prime/conductor lattice. Let

\[
T_p(\alpha;z)
\]

be the eventual dressed transport for one more \(p\)-depth. Compare

\[
T_{p\to q}
=
T_q(\alpha+e_p)T_p(\alpha)
\]

with

\[
T_{q\to p}
=
T_p(\alpha+e_q)T_q(\alpha).
\]

Define the plaquette holonomy

\[
\boxed{
\mathcal H_{pq}(\alpha)
=
T_{q\to p}^{-1}T_{p\to q}.
}
\]

Flatness is \(\mathcal H_{pq}=I\).

For small edge generators \(T_p=\exp A_p\),

\[
\boxed{
F_{pq}
=
\Delta_pA_q-\Delta_qA_p+[A_q,A_p]+\cdots.
}
\]

This is the precise mathematical location for "the first actualization changes how the next one acts."


## 9. Exact retarded influence of one event

The critical driven Suzuki realization has

\[
u(t)=\sum_{n\ge1}\frac{\varphi(n)}n\,\delta(t-\log n),
\]

\[
\dot x_0=u,
\qquad
\dot x_m=-2mx_m+u.
\]

An event \(n\) contributes for \(t\ge\log n\)

\[
\boxed{
\delta x_0^{(n)}(t)=\frac{\varphi(n)}n
}
\]

and

\[
\boxed{
\delta x_m^{(n)}(t)
=
\frac{\varphi(n)}n
e^{-2m(t-\log n)}.
}
\]

Thus every actualization leaves one persistent memory component plus a tower of decaying memories.

Its scalar response is

\[
\delta y_n(t)
=
\frac{\varphi(n)}nK_{1/2}(t-\log n).
\]

This is an exact mode-by-mode answer to how strongly an early domino remains in the future state.

## 10. Harmonic undertones and polynomial jets

Remove free propagation by writing

\[
V(A)=e^{izA\sigma_3}W(A).
\]

Then

\[
\partial_AW
=
\mu(A)
e^{-izA\sigma_3}\sigma_1e^{izA\sigma_3}
W.
\]

Exactly,

\[
\boxed{
e^{-izA\sigma_3}\sigma_1e^{izA\sigma_3}
=
\cos(2zA)\sigma_1+\sin(2zA)\sigma_2.
}
\]

Therefore first-order response is controlled by

\[
\boxed{
\widehat\mu_T(z)
=
\int_0^T\mu(A)e^{2izA}\,dA.
}
\]

Its Taylor derivatives are

\[
\boxed{
\widehat\mu_T^{(k)}(0)
=
(2i)^k\int_0^T A^k\mu(A)\,dA.
}
\]

So the derivative chain is literally the polynomial moment chain of the finite actualization field.

On a finite interval, all moments determine a finite signed measure uniquely because polynomials are dense in continuous functions.

Hence

\[
\boxed{
\text{the complete finite jet tower reconstructs the finite actualization profile.}
}
\]

The difficult step is not finite reconstruction. It is the completed \(T\to\infty\) limit.

## 11. Magnus hierarchy: moments plus connected history

Write

\[
T(T,z)=e^{\Omega(T,z)}.
\]

The first term is

\[
\Omega_1
=
izT\sigma_3
+
\sigma_1\int_0^T\mu(A)\,dA.
\]

The basic commutator is

\[
\boxed{
[M(A_1),M(A_2)]
=
2z(\mu(A_1)-\mu(A_2))\sigma_2.
}
\]

Therefore

\[
\boxed{
\Omega_2
=
z\sigma_2
\int_0^T(2A-T)\mu(A)\,dA.
}
\]

The linear-in-\(\mu\) part of the next level is

\[
\boxed{
\Omega_3^{\rm lin}
=
-\frac{z^2T^2}{3}\sigma_1
\int_0^T
P_2\!\left(\frac{2A}{T}-1\right)
\mu(A)\,dA.
}
\]

The remaining third-order contribution contains genuine ordered quadratic history.

So successive levels separate

\[
\text{one-point polynomial jets}
\]

from

\[
\text{connected chronological interactions}.
\]

This is the operator analogue of the distinction between moments and cumulants.

## 12. Bernoulli-polynomial jet theorem

Introduce a bookkeeping parameter:

\[
M_\varepsilon(A)=A_0+\varepsilon A_1(A),
\]

with

\[
A_0=iz\sigma_3,
\qquad
A_1(A)=\mu(A)\sigma_1.
\]

Let

\[
\Omega_\varepsilon(T)=\log T_\varepsilon(T).
\]

Linearizing the logarithm of the transfer around the free connection gives

\[
\delta\Omega
=
\frac{\operatorname{ad}_{TA_0}}
{1-e^{-\operatorname{ad}_{TA_0}}}
\int_0^T
e^{-A\operatorname{ad}_{A_0}}
A_1(A)\,dA.
\]

Using the Bernoulli-polynomial generating function

\[
\frac{x e^{(1-s)x}}{e^x-1}
=
\sum_{n\ge0}B_n(1-s)\frac{x^n}{n!},
\]

one obtains

\[
\boxed{
\delta\Omega(T,z)
=
\sum_{n\ge0}
\frac{T^n}{n!}
\operatorname{ad}_{A_0}^{\,n}(\sigma_1)
\int_0^T
B_n\!\left(1-\frac AT\right)\mu(A)\,dA.
}
\]

This is the exact finite-horizon realization of the first/second/third/... polynomial-derivative intuition at linear response.

The first levels are constant, centered-linear, and centered-quadratic polynomial probes of the actualization field.

The usual local-invertibility and branch caveats for the matrix logarithm apply.

## 13. What "geodesic" can mean here

The bare support lattice already has a path-independent logarithmic distance.

The greedy prime-power actualization path is therefore best described as a canonical causal geodesic selected by the smallest unresolved horizon, not as a unique shortest path.

A stronger geodesic principle becomes meaningful only after a dressed state metric is derived.

If each new physical constraint is imposed by orthogonal least-change projection, then local minimal motion is exact.

If those physical projections fail to commute, neighboring minimal paths separate.

That separation is the discrete analogue of geodesic deviation.

For a state \(v\), define

\[
v_{pq}
=
T_q(\alpha+e_p)T_p(\alpha)v,
\]

\[
v_{qp}
=
T_p(\alpha+e_q)T_q(\alpha)v.
\]

Then

\[
\boxed{
D_{pq}(\alpha;v)
=
v_{pq}-v_{qp}
}
\]

is the finite path-deviation probe.

Bare CRT gives \(D_{pq}=0\).

Any nonzero value must survive gauge, chronology, and completion controls before it is interpreted as arithmetic curvature.

## 14. GR-shaped interpretation that survives audit

The defensible chain is

\[
\boxed{
\text{causal support order}
\to
\text{local connection jets}
\to
\text{nested history commutators}
\to
\text{plaquette holonomy}
\to
\text{completed infinite curvature}.
}
\]

This is structurally reminiscent of causal-set and Regge/discrete-holonomy ideas: finite causal cells first, loop curvature second, continuum reconstruction afterward.

No physical equivalence is asserted.

A \(1+1\) metric may only be introduced after the same arithmetic transport independently determines both the characteristic frame and a volume/conformal factor. The present flat Suzuki cone does not yet provide that full metric.

## 15. Infinite actualization target

Earlier rounds prove that the naked critical prime bulk diverges and requires signed Archimedean completion.

Therefore the correct global object cannot be a raw pointwise sum.

It must be a completed limit such as

\[
\boxed{
\mathscr R_\infty
=
\lim_{X\to\infty}
\mathscr R_X^{\rm comp}
}
\]

in a declared topology.

Possible proof-bearing choices include:

- weak/distributional convergence of matrix coefficients;
- strong-resolvent convergence of derived connection operators;
- kernel convergence strong enough to preserve the RH-relevant sign.

The ambitious target is an exact identification with the Suzuki/Weil kernel or quadratic form.

That identification is currently UNVERIFIED.

## 16. Next discriminating probe

For a small support state \(\alpha\) and two prime directions \(p,q\):

1. construct the actual finite dressed edge transports from the critical carry/Hankel machinery;
2. compare \(p\to q\) with \(q\to p\);
3. verify bare pullback is exactly flat;
4. test whether physical dressing gives nontrivial plaquette holonomy;
5. project the residual into exact-conductor sectors;
6. ablate chronology and the Archimedean channel;
7. compare any surviving signed residual with the Suzuki critical carry term and Dirac mass.

This is the first probe that can establish whether the curvature language is load-bearing.

## 17. Claim ledger

**DISCLOSED**

- actualization/divisibility lattice;
- support-height formula;
- support/event lag and prime-power equality criterion;
- minimal prime-power domino theorem;
- von-Mangoldt greedy birth law;
- bare logarithmic path-independence;
- bare-flat LCM plaquettes;
- flat Suzuki principal cone;
- scalar-mass/similarity no-go for cone bending;
- SU(1,1)-type parity transfer;
- exact retarded event influence;
- finite-horizon moment completeness;
- first Magnus moment kernels;
- Bernoulli-polynomial linear-response formula.

**CONJECTURED / UNVERIFIED**

- nonzero dressed arithmetic plaquette holonomy;
- a multidirectional connection whose pullback is the critical Suzuki connection;
- completed finite curvature converging to Suzuki/Weil;
- a canonical metric or zweibein emerging from the same arithmetic transport.

**BLOCKED shortcuts**

- bare support growth as curvature;
- bare CRT synchronization as curvature;
- scalar \(\mu(A)\) alone curving the light cone;
- calling one-dimensional path ordering a curvature two-form;
- imposing a GR metric by analogy rather than derivation.

## 18. House result

The first domino sets the support clock.

The derivative chain reconstructs the finite actualization field.

Path ordering converts variation in that field into connected higher-order history.

But the object deserving the name curvature is

\[
\boxed{
\text{failure of dressed transports in independent arithmetic directions to close around a loop.}
}
\]

The next task is to derive that first plaquette holonomy from the existing critical finite system.
