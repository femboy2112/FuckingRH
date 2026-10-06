# Complexity-stratified arithmetic wave crests

**Date:** 2026-10-05  
**Status:** conceptual refinement / research program. RH is not proved here.

## 1. Refine, do not discard, the exact wavefront

The existing support statement remains exact:

\[
\operatorname{supp}(f)\subset[-L,L]
\quad\Longrightarrow\quad
\text{prime-power visibility } n\le e^{2L}
\]

under the fixed autocorrelation convention.

That is a literal information horizon.

But the arithmetic *inside* that horizon should not be modeled as one featureless expanding front. The new proposal is:

\[
\boxed{
\text{support gives the radius; complexity/defect stratifies the visible arithmetic into crests.}
}
\]

So the better picture is a **series of arithmetic wave crests**, layered by operational or description-theoretic defect.

## 2. Successor substrate and operator histories

Take successor as the universal additive substrate:

\[
S(n)=n+1,\qquad n=S^n(0).
\]

Higher arithmetic operations are recursively reconstructed over this substrate:

\[
+\quad\to\quad\times\quad\to\quad\exp\quad\to\cdots.
\]

A computation history \(E\to n\) carries more information than its endpoint \(n\).

Fix a machine-independent reduction semantics and let

\[
\tau(E)
\]

be its abstract execution cost.

The direct successor path has baseline value-changing cost

\[
G(n)=n.
\]

For a *given derivation* define excess action

\[
\Delta_\tau(E)=\tau(E)-G(n).
\]

Caution: if one minimizes \(\Delta_\tau\) over all derivations while allowing the direct successor path, the minimum is trivially zero. Therefore a useful invariant must either:

- compare restricted operator families;
- retain derivations/morphisms rather than only endpoints;
- or combine description length and execution cost.

## 3. Description defect gives a nontrivial scalar stratification

A standard control model is integer complexity:

\[
\|n\|
=
\text{minimum number of 1's needed to construct }n
\text{ using }+,\times.
\]

Its classical lower bound is

\[
\|n\|\ge 3\log_3 n,
\]

so the integer-complexity defect is

\[
\boxed{
\delta_{\rm IC}(n)
=
\|n\|-3\log_3 n.
}
\]

This is exactly the shape desired here: subtract the unavoidable coarse growth and retain the structural overhead.

Addition-chain length gives another control:

\[
\ell(n)-\lfloor\log_2 n\rfloor.
\]

The present successor-operational program should be compared against these known defects rather than reinventing their basic normalization blindly.

## 4. Crest coordinate

Let \(C(n)\) be a chosen arithmetic complexity measure and \(C_0(n)\) its universal/coarse lower envelope.

Define

\[
\delta_C(n)=C(n)-C_0(n).
\]

For a defect band \(I\subset\mathbb R\), define the arithmetic crest

\[
\mathcal C_I
=
\{n:\delta_C(n)\in I\}.
\]

Then an expanding log-support window sees not one homogeneous wavefront but many strata

\[
\mathcal C_{I_0},\mathcal C_{I_1},\mathcal C_{I_2},\ldots
\]

intersected with the same support horizon.

A useful visualization is therefore two-dimensional:

\[
\boxed{
(\log n,\ \delta_C(n)).
}
\]

Horizontal position is arithmetic scale; vertical position is complexity/defect.

## 5. Prime-frontier interpretation

Unique factorization gives the expanding multiplicative coordinate space

\[
\mathbb N_{>0}^{\times}
\cong
\bigoplus_{p\ {\rm prime}}\mathbb N e_p.
\]

When a new prime \(p\) appears, it introduces a new basis direction \(e_p\).

Between \(p\) and the next prime, composites are produced from already-realized prime directions. More strongly, for a large prime \(p\), a density tending to one of midpoint radii \(d<p\) have both \(p-d\) and \(p+d\) in the old-prime multiplicative monoid.

This suggests a qualitative crest cycle:

\[
\boxed{
\text{new generator}
\longrightarrow
\text{old-state composite relaxation}
\longrightarrow
\text{next new generator}.
}
\]

The prime is a candidate local crest in **multiplicative novelty**, while the surrounding composites are old-span outputs.

This is a hypothesis about the right complexity coordinate, not a theorem that primes maximize standard integer complexity.

## 6. Multiple defect axes are probably necessary

Different grammars make different numbers cheap.

For example:

- prime powers can be compact under exponentiation;
- highly composite numbers can be compact under multiplication;
- raw successor execution remains long for every large \(n\);
- primes have no nontrivial multiplicative factorization but may still have short additive descriptions.

Therefore one scalar complexity is unlikely to capture the whole geometry.

Use a defect vector such as

\[
\boxed{
\boldsymbol\delta(n)
=
(
\delta_{\rm succ},
\delta_{+},
\delta_{\times},
\delta_{\exp},
\delta_{\rm IC},
\ldots
).
}
\]

Then "crest" means a stratum or ridge in this defect space, not merely a local maximum of one number.

## 7. Relation to the RH wavefront

The explicit formula activates a prime-power event at

\[
t=\log p^k.
\]

The new proposal is to enrich each event with a complexity label:

\[
\boxed{
(\log p^k,\ \boldsymbol\delta(p^k)).
}
\]

Likewise composites in the old monoid provide latent positive dilation / midpoint states even though they do not appear explicitly in \(-\zeta'/\zeta\).

The logarithmic derivative may be interpreted as a **primitive/connected projection** that collapses the richer computational/composite state space down to prime-power crests.

This suggests a possible architecture:

\[
\text{successor/operator history space}
\longrightarrow
\text{complexity-stratified positive states}
\longrightarrow
\text{primitive/logarithmic projection}
\longrightarrow
\text{Suzuki prime-power event system}.
\]

## 8. Why this may matter for positivity

The old "wavefront" picture asks whether enough prime mass has crossed a scalar boundary.

The crest picture asks instead whether each new primitive generator is accompanied by enough lower-complexity old-state dispersion to pay its curvature / Brownian debt.

That is closer to the midpoint/martingale mechanism:

\[
\text{new prime crest}
\to
\text{many old-state barycentric decompositions}
\to
\text{first-order cancellation}
\to
\text{second-order positive energy}.
\]

The proof-bearing question is not "are primes sparse?" but:

> Can the exact Suzuki tower contribution at each primitive crest be realized as the primitive projection of positive lower-stratum computation/martingale geometry?

## 9. Immediate experimental program

For \(n\) in a substantial finite range, compute in parallel:

- \(\log n\);
- prime/composite and prime-power status;
- integer complexity \(\|n\|\) and defect \(\delta_{\rm IC}\) where feasible;
- addition-chain defect;
- factorization depth / multiplicative grammar depth;
- old-monoid midpoint count around each prime;
- local Suzuki weight;
- prime-tower repair coefficient \(M_p\).

Then test whether prime events correspond to reproducible ridges, transitions, or curvature changes in defect space.

Negative result is valuable: if ordinary integer-complexity crests do not align with RH event structure, the successor-operational grammar must be refined.

## 10. Strong theorem target

### Complexity-Crest Primitive Dilation Theorem — UNVERIFIED

Construct a positive computation/groupoid/Hilbert space whose:

1. objects are arithmetic values;
2. morphisms retain successor/operator construction histories;
3. a normalized action/defect stratifies histories into crests;
4. diagonal endpoint value is quotiented while construction history remains;
5. new prime generators admit positive dilations into lower/old complexity strata;
6. primitive/logarithmic reduction of those dilations yields the exact Suzuki prime-power weights;
7. the resulting finite-wavefront Gram kernels admit uniformly bounded common-mode lift.

Such a theorem would link the successor model to the current adelic/CND proof seam rather than leaving it as an unrelated complexity metaphor.
