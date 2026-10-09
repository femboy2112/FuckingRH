# The noncompact history span at the first prime interaction: E₂ ← C× → E₆

**2026-10-09. Status:** a rigorous local geometric obstruction and a reversal-compatible correspondence; **no completed Weil/Hodge sign**. RH OPEN.

## 1. Finite refinement exists, Archimedean identity-refinement does not

The LCM SUCC clocks are

\[
L_2=2,\qquad L_3=6.
\]

Thus the normalized finite Haar clock H_2 embeds into H_6 by pullback along Z/6 -> Z/2.

The corresponding Archimedean elliptic tori from the Connes–Consani complex Tate-curve construction are

\[
E_2=\mathbb C/(\log2\,\mathbb Z+2\pi i\,\mathbb Z),
\qquad
E_6=\mathbb C/(\log6\,\mathbb Z+2\pi i\,\mathbb Z).
\]

Here the extension to m=6 is the elementary analytic quotient C×/6^Z, not a claim of a primitive orbit associated by Connes–Consani to the composite 6.

Let Lambda_2 and Lambda_6 be the two lattices. Then

\[
\boxed{\Lambda_2\cap\Lambda_6=2\pi i\,\mathbb Z.}
\]

Proof: an element in the intersection has forms a log2+2pi i b = c log6+2pi i d with integers a,b,c,d. Comparing real parts gives a log2=c log6, hence 2^a=6^c for positive or negative exponents, which by unique factorization forces a=c=0. Comparing imaginary parts then gives b=d. QED.

Since this lattice has rank one, it does not define a compact elliptic curve.

## 2. A reversible COMMON COVER is nonetheless exact

The quotient

\[
\mathbb C/(2\pi i\,\mathbb Z)\cong\mathbb C^\times
\]

covers both E_2 and E_6, giving the span

\[
\boxed{
E_2\ \longleftarrow\ \mathbb C^\times\ \longrightarrow\ E_6.
}
\]

The two maps are quotient by the deck groups 2^Z and 6^Z. Each has infinite countable fibers.

The anti-holomorphic inversion

\[
\jmath(z)=-1/\bar z
\]

satisfies

\[
\jmath(2^kz)=2^{-k}\jmath(z),\qquad
\jmath(6^kz)=6^{-k}\jmath(z),
\]

so it descends to both tori and intertwines the two arrows of the span.

Thus **global reversal and finite-place reassembly can be phrased as a real correspondence over the noncompact retained-history space**. The common cover retains winding information that either compact quotient forgets.

This is a valid instance of the user's "shattered teacup" structural axis, not yet a physical time-reversal model of zeta.

## 3. Why naive Haar pushforward cannot be the Weil intersection pairing

On C× in logarithmic polar coordinates z=e^{x+i theta}, the natural invariant measure is dx dtheta. Its total mass is infinite.

For the quotient map pi_m:C×->E_m, the preimage of any positive-area open set consists of infinitely many deck translates. Therefore

\[
(\pi_m)_*(dx\,d\theta)(U)=\infty
\]

for every nonempty open U of positive Haar area in E_m.

So there is no naive finite-mass pushforward of the common-cover Haar measure giving the canonical finite-area forms on both E_2 and E_6.

An averaging/regularization or relative-trace operation is necessary to turn this history span into a finite pairing.

**Important:** existence of such a regularization is easy in many arbitrary senses; positivity-preserving compatibility with the *exact* completed Weil form is the difficult unsupplied theorem. The divergence by itself does not tell us which counterterm, Gamma operator, or sign is correct.

## 4. Compatibility with the source and the mutation controls

This is a geometric interface constructed using the *real* LCM event \(2\to6\), not a new connected prime impulse at n=6. The Euler-log source still satisfies b(6)=0 for zeta and genuine Hecke characters.

It retains both \(\log2\) and \(\log3\) in the lattices. Shifting log2 without changing the physical prime 2 changes the quotient and breaks the prescribed source-period equality.

However a positive span/Haar norm can be constructed for many arbitrary fake frequencies too, so this is **not** a source-complete RH certificate. One must separately retain the Hecke unitarity condition at unramified 2 and the global theta/Poisson identity, and compare the full Weil form.

## 5. The exact next experiment

Define a genuinely arithmetic correspondence transfer on compactly supported smooth functions on C×, using the product-formula diagonal and the Gaussian/Tate kernel. On the two ends, restrict to the actual finite-clock conductor sectors W_2 and W_6.

Prove (or refute):

1. a single common core on which the two quotient/reversal maps have declared adjoints;
2. exact compatibility with half-density finite-clock refinement;
3. no spurious \(\log6\) connected source but a retained mixed W_6 correlation;
4. finite renormalization selected by the global Gaussian/Poisson trace, not an adjustable scalar;
5. full polarized equality to \(Q_W\), including origin, pole, digamma and negative bulk;
6. an independent positive Hodge-index/polarization statement on the primitive image.

If the completion only reproduces the functional equation, Davenport–Heilbronn remains a sign-blind falsifier.

**Conclusion:** the first finite prime interaction already forces the natural common Archimedean-history cover to be noncompact, making a trace/completion step unavoidable. This is a zero-free exact geometric statement, **not** an RH breakthrough.
