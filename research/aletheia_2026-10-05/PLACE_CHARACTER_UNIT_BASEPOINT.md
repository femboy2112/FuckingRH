# Unit basepoint and place-character continuation

**Date:** 2026-10-05  
**Status:** structural synthesis / proof-program note. RH is not proved here.

This note makes durable the following observation:

> The trivial valuation is a common basepoint for the finite and Archimedean place branches, and the logarithmic place weights are the first jets of the multiplicative character family at that basepoint.

The point is not to claim a new theory of analytic continuation of rings. The ring/field remains fixed. What is continued is the **place character**.

## 1. Common real deformation to the trivial valuation

For a place \(v\) of \(\mathbb Q\), let \(|\cdot|_v\) be the normalized absolute value. For a real parameter \(\lambda\ge0\), define

\[
|x|_{v,\lambda}=|x|_v^\lambda.
\]

For \(x\neq0\),

\[
|x|_{v,\lambda}=\exp(\lambda\log|x|_v)\longrightarrow1
\qquad(\lambda\downarrow0).
\]

Thus every place branch meets the trivial absolute value

\[
|x|_0=1\quad(x\ne0).
\]

This is compatible with the standard description of the Berkovich spectrum \(\mathcal M(\mathbb Z)\): the trivial absolute value is a common central point, with \(p\)-adic and Archimedean power branches meeting there.

Important distinction:

- for real \(\lambda\) in the allowed branch range, \(|\cdot|_v^\lambda\) is again an absolute value/seminorm;
- for complex \(s\), the object below is a multiplicative character, not an absolute value.

## 2. Complex place-character continuation

Define

\[
\chi_{v,s}(x)=|x|_v^s
=\exp\!\bigl(s\log|x|_v\bigr),
\qquad s\in\mathbb C.
\]

For fixed \(x\ne0\), \(\chi_{v,s}(x)\) is entire in \(s\), and

\[
\chi_{v,0}(x)=1.
\]

Thus \(s=0\) is the common **unit fiber** of every local character family.

This is the same character family underlying local Mellin/Tate zeta integrals.

## 3. Jets at the unit

Differentiating at \(s=0\),

\[
\partial_s^k\chi_{v,s}(x)\big|_{s=0}
=
\bigl(\log|x|_v\bigr)^k.
\]

In particular,

\[
\partial_s\chi_{v,s}(x)\big|_{0}
=
\log|x|_v.
\]

For the standard finite normalization,

\[
\log|x|_p=-v_p(x)\log p.
\]

At infinity,

\[
\log|x|_\infty=\log|x|.
\]

So the familiar \(\log p\) weights are literally first-order tangent data of the finite-place branches leaving the trivial valuation.

## 3.5 Critical half-density twist

For RH, the most relevant basepoint is not the untwisted local character by itself but the critical-line-centered family

\[
\chi^{(1/2)}_{v,z}(x)
=
|x|_v^{1/2+z}
=
|x|_v^{1/2}\chi_{v,z}(x).
\]

The deformation factor satisfies

\[
\chi_{v,0}(x)=1,
\]

while the first derivative of the full twisted character is

\[
\partial_z
\chi^{(1/2)}_{v,z}(x)\big|_{z=0}
=
|x|_v^{1/2}\log|x|_v.
\]

For a finite prime-power element \(p^k\),

\[
|p^k|_p^{1/2}\log|p^k|_p
=
-p^{-k/2}k\log p.
\]

After the standard prime-power bookkeeping, this is exactly the source of the critical weights \(p^{-k/2}\log p\) appearing in Suzuki's event measure.

Globally,

\[
\prod_v |x|_v^{1/2}=1
\]

by the product formula. Therefore the critical half-density is itself globally balanced, and the \(z=0\) deformation direction is again a global unit direction.

This makes the critical line geometrically natural in the present frame:

\[
\boxed{
\text{global half-density balance}
+
\text{unit-centered character deformation}.
}
\]

A future Gram/jet construction should probably be built from this \(1/2\)-twisted family rather than from the untwisted \(s=0\) family alone.

## 4. Product formula as tangent conservation

For \(x\in\mathbb Q^\times\),

\[
\prod_v |x|_v=1.
\]

Therefore, for common complex parameter \(s\),

\[
\prod_v\chi_{v,s}(x)
=
\prod_v|x|_v^s
=
1.
\]

Taking logarithmic derivative at \(s=0\) gives

\[
\sum_v\log|x|_v=0,
\]

equivalently

\[
\log|x|_\infty
=
\sum_p v_p(x)\log p.
\]

Thus the Archimedean logarithmic size is the global balancing coordinate of the finite first jets.

Higher derivatives expose cross-place coupling. For example,

\[
0
=
\left(\sum_v\log|x|_v\right)^2
=
\sum_v(\log|x|_v)^2
+
2\sum_{v<w}\log|x|_v\,\log|x|_w.
\]

This identity is elementary, but it is conceptually important: once one passes beyond the first jet, the global constraint naturally contains cross-place terms. That is exactly the kind of information a primewise independent Gaussianization can lose.

## 5. Why this matters for the current RH program

Astra Round 001 and the partial Round 002 establish several constraints:

- literal individual prime-power ramps are not positive CND increments;
- the canonical Gaussian-divided prime convolution residual is not a characteristic function;
- ordinary finite prime truncations with the exact Archimedean term cannot be global CND approximants;
- service-clock transport flattens the Archimedean curvature, but ordinary convex/martingale orders do not hold for the exact prefix marginals;
- full prime towers admit an independently positive repaired block, but the sharp linear repair diverges when summed over all primes.

The unit-basepoint picture suggests that the required cancellation should not be performed **after** constructing independent positive local blocks. The divergent local first-jet corrections may need to cancel **globally at the character/basepoint level**, before the second/higher-jet positive object is formed.

This is the new conceptual distinction:

\[
\text{local positive blocks}+\text{post hoc subtraction}
\quad\text{(known to fail)}
\]

versus

\[
\text{global unit-based renormalization}
\longrightarrow
\text{coupled higher-jet/Gram object}.
\]

## 6. Prime-localization ladder

There is also a useful exact control family.

If primes below a chosen prime \(P\) are inverted ring-theoretically, one obtains

\[
\mathbb Z\bigl[\{q<P\}^{-1}\bigr],
\]

whose first non-inverted rational prime is \(P\). At the Euler-product level, removing a finite set \(S\) of prime factors multiplies zeta by

\[
\prod_{p\in S}(1-p^{-s}).
\]

This is distinct from valuation trivialization, but it supplies a coherent deformation/control ladder of visible finite places.

The ordinary arithmetic system has first visible prime \(2=1+1\), so its first event at \(t=\log2\) is structurally minimal in the ordinary semiring skeleton.

## 7. Candidate global theorem suggested by this note

### Unit-Basepoint Renormalized Place-Coupling Theorem (UBRPCT) — UNVERIFIED

Construct, without using zeta zeros, a global arithmetic Hilbert/CND object from the common place-character family near \(s=0\) such that:

1. finite places enter as complete Euler/prime-tower objects;
2. the Archimedean place enters in the same normalization;
3. first-jet divergences / linear repairs cancel by a global identity at the common unit basepoint, rather than by subtracting an infinite positive quantity after the fact;
4. the resulting second/higher-jet object is independently positive;
5. its kernel or exponent is exactly Suzuki's
   \[
   K_\Psi(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u)
   \]
   or equivalently has characteristic exponent \(-\Psi\);
6. the construction is sensitive to finite event-weight mutations, so it survives Round-001 rigidity controls;
7. all limits are justified in a topology preserving CND / positive definiteness.

If such a theorem is proved, Suzuki/Nakamura-Suzuki close RH.

This is a proposed proof architecture, not a theorem.

## 8. Source pointers

- Jérôme Poineau's description of \(\mathcal M(\mathbb Z)\) as the space of multiplicative seminorms with a trivial central absolute value and Archimedean/\(p\)-adic power branches.
- Tate-style local zeta integrals use the character \(|x|^s\), making the complex \(s\)-family canonical rather than invented for this program.
