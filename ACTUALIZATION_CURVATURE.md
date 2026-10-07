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
