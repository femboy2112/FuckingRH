# Profinite successor dynamics: the lifted arithmetic light cone

**Date:** 2026-10-05  
**Status:** exact structural synthesis / new proof probe. RH is not proved here.

## 1. Bare successor is only the visible base coordinate

The additive successor ray

\[
0\to1\to2\to3\to\cdots
\]

is canonical, but it suppresses the residue/divisibility state carried by every
integer.

The canonical completion retaining all congruence data is

\[
\widehat{\mathbb Z}
=
\varprojlim_m\mathbb Z/m\mathbb Z
\cong
\prod_p\mathbb Z_p.
\]

The diagonal embedding

\[
\iota:\mathbb Z\hookrightarrow\widehat{\mathbb Z}
\]

has dense image.

Successor lifts to the translation/odometer

\[
T(x)=x+1
\]

on \(\widehat{\mathbb Z}\).

Thus the bare natural-number trajectory is the visible orbit

\[
\iota(0),\iota(1),\iota(2),\ldots
\]

of a much richer profinite dynamical system.

## 2. Residue clocks

Projecting to

\[
\mathbb Z/m\mathbb Z
\]

turns successor into the cyclic clock

\[
r\mapsto r+1\pmod m.
\]

At prime \(p\), the full \(p\)-adic coordinate retains all clocks

\[
\bmod p,\ \bmod p^2,\ \bmod p^3,\ldots
\]

compatibly.

Hence successor simultaneously advances every finite congruence clock.

This makes the arithmetic "light cone" naturally a path in a growing or
completed residue-state space, not merely a path through scalar values.

## 3. Prime-power events are first entrances into nested p-adic balls

Normalize the \(p\)-adic valuation by

\[
|x|_p=p^{-v_p(x)}.
\]

The depth-\(k\) divisibility region is

\[
p^k\mathbb Z_p.
\]

For a positive integer \(n\),

\[
p^k\mid n
\iff
\iota(n)_p\in p^k\mathbb Z_p.
\]

Moreover

\[
p^k
=
\min\{n\ge1:\ \iota(n)_p\in p^k\mathbb Z_p\}.
\]

Therefore the prime-power sequence

\[
p,\ p^2,\ p^3,\ldots
\]

is exactly the sequence of **first-hitting times** of the successor orbit into
the nested \(p\)-adic balls

\[
p\mathbb Z_p\supset
p^2\mathbb Z_p\supset
p^3\mathbb Z_p\supset\cdots.
\]

Taking logarithms gives the Suzuki event locations

\[
\log p^k=k\log p.
\]

This gives an exact dynamical interpretation of a prime tower.

## 4. Critical half-density is the L2 norm of a p-adic ball

Let \(\mu_p\) be additive Haar measure on \(\mathbb Z_p\), normalized by

\[
\mu_p(\mathbb Z_p)=1.
\]

Multiplication by \(p^k\) scales measure by \(p^{-k}\), hence

\[
\mu_p(p^k\mathbb Z_p)=p^{-k}.
\]

Therefore

\[
\boxed{
\left\|\mathbf1_{p^k\mathbb Z_p}\right\|_{L^2(\mathbb Z_p,\mu_p)}
=
p^{-k/2}.
}
\]

Suzuki's critical event weight is

\[
w_{p,k}
=
\frac{\Lambda(p^k)}{\sqrt{p^k}}
=
(\log p)p^{-k/2}.
\]

Hence

\[
\boxed{
w_{p,k}
=
(\log p)
\left\|\mathbf1_{p^k\mathbb Z_p}\right\|_2.
}
\]

Interpretation:

- \(p^{-k}\) is the recurrence frequency/Haar volume of depth-\(k\) divisibility;
- \(p^{-k/2}\) is its canonical Hilbert half-density;
- \(\log p\) is the logarithmic radial spacing between successive valuation layers.

Thus the Suzuki prime-tower weights arise canonically from the profinite
successor state at critical half-density.

## 5. Local Euler factors are partition functions of nested p-adic volumes

Since

\[
\mu_p(p^k\mathbb Z_p)=p^{-k},
\]

one has

\[
\boxed{
L_p(s)
=
\frac1{1-p^{-s}}
=
\sum_{k\ge0}\mu_p(p^k\mathbb Z_p)^s.
}
\]

At \(s=1/2\), the summands are the \(L^2\)-norms of the nested ball indicators.

Taking a logarithmic derivative gives

\[
-\partial_s\log L_p(s)
=
\sum_{k\ge1}(\log p)p^{-ks},
\]

and at \(s=1/2\),

\[
-\partial_s\log L_p(1/2)
=
\sum_{k\ge1}
(\log p)
\left\|\mathbf1_{p^k\mathbb Z_p}\right\|_2.
\]

This is exactly the complete critical prime-tower mass \(M_p\) found in Round
002.

## 6. A canonical positive Koopman representation

Translation by \(1\) on the compact group \(\widehat{\mathbb Z}\) preserves Haar
measure. Therefore the Koopman operator

\[
(Uf)(x)=f(x-1)
\]

is unitary on

\[
L^2(\widehat{\mathbb Z}).
\]

For one local ball,

\[
B_{p,k}=\mathbf1_{p^k\mathbb Z_p},
\]

the orbit correlations satisfy

\[
\langle B_{p,k},U^nB_{p,k}\rangle
=
\mu_p\bigl(
p^k\mathbb Z_p\cap(n+p^k\mathbb Z_p)
\bigr).
\]

Hence

\[
\boxed{
\langle B_{p,k},U^nB_{p,k}\rangle
=
p^{-k}\mathbf1_{p^k\mid n}.
}
\]

After normalizing

\[
\phi_{p,k}=p^{k/2}B_{p,k},
\]

one obtains the exact positive-definite divisibility kernel

\[
\boxed{
\langle\phi_{p,k},U^n\phi_{p,k}\rangle
=
\mathbf1_{p^k\mid n}.
}
\]

Thus divisibility and prime-power depth already have a canonical positive
Hilbert realization under successor dynamics.

This does not yet reproduce Suzuki's log-time ramp/screw kernel; it supplies a
new positive upstairs state space and an exact local observable.

## 7. Integral-adelic lifted worldline

To retain both ordinary successor position and all finite residue state, use

\[
\mathbb A_{\mathbb Z}
=
\mathbb R\times\widehat{\mathbb Z}.
\]

The lifted integer trajectory is

\[
X_n=(n,\iota(n)).
\]

Successor is the diagonal translation

\[
\boxed{
X_{n+1}
=
X_n+
(1,\mathbf1_{\widehat{\mathbb Z}}).
}
\]

The real coordinate records ordinary additive distance. The profinite
coordinate records every finite-place residue/divisibility state.

Thus the bare number line is the projection

\[
(n,\iota(n))\mapsto n
\]

of a canonical integral-adelic worldline.

## 8. Constructive filtration versus completed state

Mathematically every \(p\)-adic coordinate exists in \(\widehat{\mathbb Z}\)
from the beginning.

Constructively, one may reveal them through a filtration:

\[
\widehat{\mathbb Z}_{\le y}
=
\prod_{p\le y}\mathbb Z_p
\]

or through finite residue systems/primorial clocks.

A newly discovered prime does not have to be **created from the old monoid**.
It can instead be understood as the moment at which a previously unresolved
coordinate becomes necessary/visible.

This directly evades the Round-003 old-support theorem:

- the old-monoid Dirichlet logarithm cannot create \(p^k\) support;
- the profinite completion already contains the \(p\)-coordinate;
- the new theorem problem becomes one of **resolution/activation and coupling**,
  not support creation from old primes.

This is a conceptual escape from that specific no-go, not yet an RH proof.

## 9. Sieve dynamics as a finite projection of successor

For a finite set of primes \(S\), project the successor orbit to

\[
\prod_{p\in S}\mathbb Z/p\mathbb Z.
\]

Successor is diagonal translation by \((1,\ldots,1)\).

A number survives the sieve by \(S\) exactly when its state lies in the unit
locus

\[
\prod_{p\in S}(\mathbb Z/p\mathbb Z)^\times.
\]

By the Chinese remainder theorem this is the standard wheel-sieve orbit modulo

\[
\prod_{p\in S}p.
\]

Hence prime candidates are successive visits of the successor orbit to the
unit locus of an increasingly refined residue state space.

This gives a rigorous version of "complexity crests": each new prime adds a
new cyclic exclusion coordinate to future propagation.

## 10. Crest interpretation

The prime \(p\) itself is a new-generator event in the observed multiplicative
filtration.

The powers

\[
p^k
\]

are first entrances into deeper \(p\)-adic divisibility balls.

Generic composites are recurrent hits of already-resolved finite-place strata.

So the arithmetic trajectory is naturally stratified by:

- new-coordinate discovery;
- shallow recurrent divisibility;
- deeper first-hitting events;
- simultaneous multi-prime intersections.

This is richer than a scalar wavefront and more canonical than an arbitrary
description-complexity label.

Complexity/defect can still be attached as additional observables on this
profinite state.

## 11. Relation to Astra Round 003 no-go results

Round 003 proved:

- positive old-monoid scalar mixtures cannot reconstruct multiple exact tower
  levels;
- ordinary grading-preserving Dirichlet logarithms cannot create the missing
  \(p^k\) support;
- the successor number line and coarse computation groupoid alone do not supply
  the exact Suzuki pairing.

The profinite lift changes the state space in precisely the way those no-go
results suggest:

\[
\boxed{
\text{bare value}
\longrightarrow
\text{value + all finite-place residue/depth state}.
}
\]

It does not contradict the no-go theorems; it steps outside their support
hypotheses.

## 12. New theorem-shaped probe

### Profinite Successor Gram Theorem — UNVERIFIED

Construct from the Koopman representation of successor on

\[
L^2(\widehat{\mathbb Z})
\]

and the Archimedean coordinate a semilocal/adelic vector map \(V_L(t)\) such
that:

1. \(p^k\) events arise from the nested ball vectors
   \(\mathbf1_{p^k\mathbb Z_p}\);
2. their exact half-density amplitudes are
   \(p^{-k/2}\);
3. \(\log p\) arises from the valuation/log-radius generator;
4. cross-prime composite states arise automatically from tensor/product Haar
   structure on \(\prod_p\mathbb Z_p\);
5. the primitive/logarithmic projection has the exact Suzuki locations and
   weights;
6. after coupling the Archimedean place, the Gram pullback equals
   \[
   K_{\Psi+c_L|\cdot|}
   \]
   with \(0\le c_L\le C\) uniformly.

The immediate local control is to compare the existing Round-002 interval Gram
vector for \(D_p\) to the Koopman orbit of the \(p\)-adic nested-ball vectors.

## 13. First exact comparison to attempt

For one prime plus infinity, compute the complete kernel generated by

\[
\{\mathbf1_{p^k\mathbb Z_p}:k\ge1\}
\]

under the successor Koopman operator and compare it to:

- the repaired tower kernel \(K_{D_p}\);
- the local scattering density \(M_p-P_p(s)\);
- the semilocal Sonin multiplier already audited in Round 003.

Any claimed bridge must match both:

- spectral locations \(k\log p\);
- amplitudes \((\log p)p^{-k/2}\).

The profinite construction supplies the latter canonically at the level of
Hilbert norms. The former and the precise ramp/screw geometry remain unpaid.

## 14. Bottom line

The successor "light cone" should not be modeled as motion on bare
\(\mathbb N\).

A canonical lifted state is

\[
\boxed{
X_n=(n,\iota(n))
\in
\mathbb R\times\widehat{\mathbb Z}
=
\mathbb R\times\prod_p\mathbb Z_p.
}
\]

Then:

- successor is one diagonal translation;
- prime towers are nested first-hitting strata;
- critical \(p^{-k/2}\) weights are Hilbert half-densities of those strata;
- composites are intersections/tensor states across finite-place coordinates;
- the bare number line is only the Archimedean/base projection.

This is the current strongest candidate for what the successor causal substrate
must actually traverse.
