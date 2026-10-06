# Prime frontier, old-monoid moat, and density-one midpoint stencils

**Date:** 2026-10-05  
**Status:** exact elementary lemmas + sieve consequence + speculative RH probe. RH is not proved here.

## 1. Exact old-monoid frontier lemma

Let \(p<q\) be consecutive primes. Bertrand's postulate gives

\[
q<2p.
\]

If

\[
p<n<q,
\]

then \(n\) is composite. Moreover **every prime factor of \(n\) is strictly less than \(p\)**.

Proof: if a prime factor \(r\mid n\) satisfied \(r\ge p\), then because \(n\) is composite,

\[
n\ge2r\ge2p>q,
\]

contradiction.

Hence the entire open prime gap satisfies

\[
\boxed{
(p,q)\cap\mathbb N
\subset
\langle r:\ r<p,\ r\text{ prime}\rangle_{\times}.
}
\]

In fact the new prime \(p\) itself does not divide any integer in \((p,q)\), because its first larger multiple is \(2p>q\).

Interpretation: when a new prime generator \(p\) arrives, all integers produced before the next new prime arrives are generated solely by **strictly older primes**.

## 2. Unique factorization as an expanding coordinate space

Multiplicatively,

\[
\mathbb N_{>0}
\cong
\bigoplus_{r\ {\rm prime}}\mathbb N e_r,
\]

via

\[
n\longmapsto(v_r(n))_r.
\]

At the numerical frontier \(p\), the prime \(p\) introduces the new coordinate vector \(e_p\).

But every composite \(n\) with

\[
p<n<q
\]

has

\[
v_r(n)=0\qquad(r\ge p),
\]

so it lies entirely in the old coordinate submonoid

\[
\bigoplus_{r<p}\mathbb N e_r.
\]

Thus a prime is locally a **new multiplicative basis direction surrounded by old-span outputs**.

## 3. Fixed-radius isolation is density one among primes

Fix an integer \(R\ge1\).

For every fixed nonzero even offset \(h\), standard Brun/Selberg upper-bound sieve estimates give

\[
\#\{p\le x:\ p,\ p+h\text{ both prime}\}
=
O_h\!\left(\frac{x}{(\log x)^2}\right).
\]

For odd \(h\), two sufficiently large odd primes cannot differ by \(h\) because of parity.

Since

\[
\pi(x)\sim\frac{x}{\log x},
\]

the proportion, among primes \(p\le x\), having another prime at any one fixed offset \(h\) is

\[
O_h\left(\frac1{\log x}\right)\to0.
\]

Taking a union over the finitely many offsets

\[
1\le |h|\le R
\]

gives

\[
\boxed{
\frac{
\#\{p\le x:\exists q\ne p\text{ prime},\ |q-p|\le R\}
}{
\pi(x)
}
\to0.
}
\]

Equivalently:

> For every fixed radius \(R\), a density-one proportion of primes are the unique prime in \([p-R,p+R]\).

This does **not** mean every sufficiently large prime is isolated by \(R\). Bounded prime gaps occur infinitely often. The exceptional close-cluster primes have relative density zero for each fixed offset/window.

## 4. Old-support midpoint stencils

Fix \(d\ge1\). For a prime \(p>d\), if both

\[
p-d,\qquad p+d
\]

are composite, then every prime factor of both endpoints is \(<p\):

- for \(p-d<p\), this is immediate;
- for \(p+d<2p\), any factor \(\ge p\) would force the composite to be at least \(2p\).

Thus for a density-one proportion of primes \(p\), for every fixed finite collection \(d=1,\dots,R\), each symmetric endpoint pair

\[
p-d,\quad p+d
\]

lies entirely in the old-prime multiplicative monoid.

For odd \(d\), this is eventually automatic by parity: \(p\pm d\) are even and \(>2\).

## 5. Additive midpoint versus multiplicative support

For every symmetric pair,

\[
p=\frac{(p-d)+(p+d)}2.
\]

But the endpoints are old-generated while \(p\) is the newly adjoined multiplicative generator.

Thus the signed midpoint cell

\[
\mu_{p,d}
=
\delta_{p-d}+\delta_{p+d}-2\delta_p
\]

has

\[
\int1\,d\mu_{p,d}=0,
\qquad
\int x\,d\mu_{p,d}=0,
\]

while comparing a nonlinear observable detects curvature.

The Archimedean collapse

\[
W(v(n))=\sum_rv_r(n)\log r=\log n
\]

gives

\[
W(e_p)=\log p,
\]

and

\[
\boxed{
\log p-\frac{\log(p-d)+\log(p+d)}2
=
-\frac12\log\left(1-\frac{d^2}{p^2}\right)>0.
}
\]

So the **new multiplicative basis vector sits above the chord formed by two old-generated additive neighbors after Archimedean log collapse**.

For fixed \(d\),

\[
-\frac12\log\left(1-\frac{d^2}{p^2}\right)
=
\frac{d^2}{2p^2}+O_d(p^{-4}).
\]

The affine/first-order mode cancels exactly; what survives is a positive quadratic curvature defect.

## 6. Critical half-density curvature

Likewise,

\[
x\mapsto x^{-1/2}
\]

is strictly convex, so

\[
\frac{(p-d)^{-1/2}+(p+d)^{-1/2}}2
>
p^{-1/2}.
\]

For fixed \(d\),

\[
\frac{(p-d)^{-1/2}+(p+d)^{-1/2}}2-p^{-1/2}
=
\frac{3d^2}{8p^{5/2}}+O_d(p^{-9/2}).
\]

Again midpoint centering kills the linear term and leaves positive critical-half-density curvature.

## 7. The "law of small numbers" interpretation

Fix a local radius \(R\).

For a typical sufficiently large prime (in prime-relative density),

- the center \(p\) is a genuinely new multiplicative generator;
- every neighboring integer \(p\pm d\), \(1\le d\le R\), is composite;
- those neighbors are generated entirely by primes \(<p\);
- the additive midpoint relation centers the old-generated endpoints on the new generator;
- affine modes cancel;
- nonlinear Archimedean/half-density observables leave positive second-order defects.

Thus the local prime environment becomes, with density one, an increasingly clean laboratory for comparing a new basis direction against old-generated closure.

The phrase "law of small numbers" should be treated as intuition: the rigorous statement is fixed-radius density-one isolation, not an assertion that all sufficiently large primes have monotonically growing gaps.

## 8. Candidate induction mechanism

This suggests a possible prime-frontier induction:

1. Assume a positive/primitive representation has been constructed from primes \(<p\).
2. Use old-generated midpoint cells around \(p\) to create centered, zero-first-moment dispersion cells.
3. Adjoin the new prime/tower \(p\) by identifying its required Gram/CND contribution with the second/higher-order curvature carried by those old-state cells.
4. Show that the exact Suzuki weight/marginal is preserved.
5. Iterate.

The exact obstruction is step 3–4. Density-one availability of midpoint cells does **not** imply that their curvature weights sum to the precise \(p^{-k/2}\log p\) tower mass.

A successful theorem would need a canonical weighted decomposition, not merely existence of many composite neighbors.

## 9. Stronger theorem-shaped question

For a prime frontier \(p\), let \(\mathcal M_{<p}\) be the multiplicative monoid generated by primes \(<p\).

Can one represent the exact new critical tower functional \(h_p\), modulo the common \(|t|\)/degree mode, as a positive combination or limit of second-difference cells

\[
\delta_{n_-}+\delta_{n_+}-2\delta_p,
\qquad
n_\pm\in\mathcal M_{<p},
\qquad
n_-+n_+=2p,
\]

or of a generalized barycentric family with the same zero first moment?

If yes with exact Suzuki weights, the prime tower would be realized as curvature/variance generated by the already-built arithmetic state.

This is unproved and is not implied by Goldbach or sieve isolation alone.
