# Adelic radical and prime-tower repair

**Date:** 2026-10-05  
**Status:** exact identities + literature alignment + proposed theorem. RH is not proved here.

This note records a sharper synthesis of:

- Astra Round 002's complete-prime-tower CND repair;
- the diagonal \(\mathbb Q^\times\) quotient / action-groupoid picture;
- Connes–Consani–Marcolli's primitive adelic cohomology and trace-pairing radical;
- the critical half-density normalization.

The central new observation is that the divergent local repairs all lie in **one common CND direction**, and their coefficients are exactly the local logarithmic-derivative masses at \(s=1/2\).

## 1. Prime tower and its sharp repair

For a prime \(p\), write

\[
\ell=\log p,\qquad r=p^{-1/2}.
\]

The complete Suzuki prime tower is

\[
h_p(t)
=
\ell\sum_{k\ge1}r^k(|t|-k\ell)_+.
\]

Round 002 proves that the sharp linear repair

\[
D_p(t)=M_p|t|-h_p(t),
\qquad
M_p=\frac{\ell r}{1-r}
=\frac{\log p}{\sqrt p-1},
\]

is CND and has an explicit positive interval-Gram realization and positive finite Lévy measure.

The uncorrected \(h_p\) and \(-h_p\) are not CND.

## 2. The repair tax is the local Euler logarithmic derivative at the critical half-density

Let

\[
L_p(s)=(1-p^{-s})^{-1}.
\]

Then

\[
\frac{d}{ds}\log L_p(s)
=
-\frac{(\log p)p^{-s}}{1-p^{-s}}.
\]

Hence

\[
\boxed{
M_p
=
-\left.\frac{d}{ds}\log L_p(s)\right|_{s=1/2}.
}
\]

Thus the divergent total repair

\[
\sum_pM_p
\]

is not an arbitrary artifact of the Gram construction. It is precisely the divergent prime-by-prime logarithmic derivative of the Euler product at the critical half-density.

This makes the required renormalization intrinsically tied to the failure of the Euler product to converge at \(s=1/2\).

## 3. Scattering-phase form of the repair

Define the local ratio

\[
\rho_p(z)
=
\frac{L_p(z)}{L_p(1-z)}
=
\frac{1-p^{-(1-z)}}{1-p^{-z}}.
\]

On the critical line \(z=1/2+is\),

\[
\rho_p(1/2+is)
=
\frac{1-re^{i\ell s}}{1-re^{-i\ell s}}.
\]

Using the absolutely convergent logarithmic expansion for \(0<r<1\),

\[
\log\rho_p(1/2+is)
=
-2i\sum_{k\ge1}\frac{r^k}{k}\sin(k\ell s),
\]

so

\[
\boxed{
\frac{i}{2}\frac{d}{ds}
\log\rho_p(1/2+is)
=
\ell\sum_{k\ge1}r^k\cos(k\ell s).
}
\]

At \(s=0\) this equals \(M_p\). Therefore

\[
\boxed{
M_p
-
\frac{i}{2}\frac{d}{ds}\log\rho_p(1/2+is)
=
\ell\sum_{k\ge1}r^k[1-\cos(k\ell s)]
\ge0.
}
\]

Round 002's positive Lévy density can therefore be rewritten as

\[
\boxed{
\nu_p(ds)
=
\frac{1}{\pi s^2}
\left[
M_p
-
\frac{i}{2}\partial_s
\log\rho_p(1/2+is)
\right]ds.
}
\]

Interpretation: the positive repaired tower is the local critical-line scattering-phase derivative **renormalized by subtracting its zero-frequency value**.

This identity is exact.

## 4. The divergent correction is one-dimensional

Every prime repair has the form

\[
D_p=M_p|t|-h_p.
\]

Although

\[
\sum_pM_p=\infty,
\]

the divergent correction always points in the same function-space direction:

\[
\mathbb R|t|.
\]

Therefore, in the vector-space quotient by that common direction,

\[
\boxed{
[-h_p]=[D_p]\quad\bmod\ \mathbb R|t|.
}
\]

Since \(D_p\) has an independently positive Gram representative, every actual negative prime-tower contribution has a positive representative **modulo the same one-dimensional common mode**.

This is much sharper than saying that infinitely many unrelated counterterms diverge.

## 5. Arithmetic wavefront becomes local finiteness modulo the common mode

Fix \(T>0\). If \(p>e^T\), then no power \(p^k\) satisfies \(k\log p\le T\). Hence for \(|t|\le T\),

\[
h_p(t)=0.
\]

But then

\[
D_p(t)=M_p|t|.
\]

Thus modulo \(\mathbb R|t|\), every prime \(p>e^T\) is invisible on the compact window:

\[
[D_p]|_{[-T,T]}=0.
\]

Therefore only finitely many prime towers remain on every compact wavefront **after quotienting the common mode**.

This recovers the arithmetic wavefront as a local-finiteness statement in the quotient.

## 6. Tent evaluation identifies the common mode with an identity-supported degree term

Suzuki's tent is

\[
\Delta_t(x)=\frac12(t-|x|)_+,
\]

so

\[
\Delta_t(0)=t/2.
\]

A distribution supported at the multiplicative identity/logarithmic coordinate \(0\) therefore evaluates on the tent as

\[
2c\,\delta_0(\Delta_t)=ct=c|t|\qquad(t\ge0).
\]

Hence the common \(|t|\) repair direction is exactly the shadow, on Suzuki's one-parameter tent family, of an identity-supported linear functional.

This strongly suggests a relationship with the **degree / trivial-correspondence sector** in Weil-style geometry.

Status: the displayed tent identity is exact. Its identification with the full Connes–Consani–Marcolli radical is a theorem target, not yet proved.

## 7. Connes–Consani–Marcolli alignment

In the adelic trace-formula approach, the relevant quotient is not merely a coarse orbit set. Primitive cohomology is obtained from a cokernel/quotient construction associated with the adele class space, and the trace pairing has a large radical consisting of data extending from the adelic side. This radical is the number-field analogue of the sector of trivial correspondences that can alter degree without contributing to the primitive pairing.

Their RH positivity is formulated after the critical half-density twist \(\Delta^{-1/2}\).

This matches two independently reached requirements of the present program:

1. **quotient/null the global principal or degree-like direction before testing positivity;**
2. **work at the critical half-density rather than adding the factor \(1/2\) afterward.**

The value of the present synthesis is therefore not discovery of the general adelic quotient architecture. It is the candidate identification of the Round-002 tower repair direction with its primitive/radical sector, together with Suzuki's one-parameter RH-equivalent tent family.

## 8. Semilocal evidence: finite places become well behaved only after coupling to infinity

Connes–Consani's local-factor analysis shows that individual finite local scattering ratios need not have the required quasi-inner property, while the product of the Archimedean factor with any finite set of finite local factors does.

This is exact evidence for the order of operations suggested here:

\[
\boxed{
\text{couple finite places with infinity first}
\longrightarrow
\text{test positivity / compactness second}.
}
\]

It is the opposite of summing independently repaired local positive blocks and subtracting a divergent global term afterward.

## 9. Prime orbits survive the diagonal quotient

The adele-class/scaling geometry retains periodic prime orbits of period

\[
\log p.
\]

Moreover, semilocal lifts of a prime orbit carry monodromy/Frobenius information involving the other places. Thus quotienting by diagonal \(\mathbb Q^\times\) does not erase prime spectral data; it reorganizes the primes into orbit and morphism data.

This supports the groupoid formulation:

\[
[\mathbb A_\mathbb Q/\mathbb Q^\times]
\]

rather than a naive quotient that forgets how a principal rational factors.

## 10. The next theorem is now sharper

### Degree-Radical Tower Positivity Theorem — UNVERIFIED

Construct an explicit map from the prime-tower/Suzuki tent system into the primitive adelic trace-pairing space such that:

1. the common repair direction \(|t|\) maps into the trace radical / trivial-correspondence degree sector;
2. for every prime \(p\), the actual tower class \([-h_p]\) equals the positive repaired class \([D_p]\) in the primitive quotient;
3. the Archimedean Suzuki term has a compatible positive semilocal representative in the same quotient;
4. finite semilocal sums are positive by construction after the quotient;
5. on every compact \(t\)-window only finitely many nontrivial prime-tower classes occur;
6. the inductive/closure limit reproduces exactly
   \[
   K_\Psi(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u)
   \]
   on the Suzuki tent family;
7. the positivity-preserving topology of the limit is proved;
8. finite mutations of prime weights break the arithmetic/groupoid compatibility, so Round-001 rigidity controls are respected.

If all eight items hold without using zero locations, Suzuki's theorem gives RH.

## 11. Immediate falsifiers

Before promoting this route, test:

- whether the \(|t|\) identity-supported tent functional really lies in the radical used by the adelic trace pairing, with the exact half-density normalization;
- whether quotient positivity is well defined: quotienting a vector space by a positive direction alone does **not** create a positive cone;
- whether the repaired \(D_p\) Gram kernel is the image of an actual semilocal adelic/trace object rather than merely an isomorphic scalar CND kernel;
- whether the Archimedean correction needed to fix degree is compatible with the semilocal Sonin/quasi-inner constructions;
- whether the inductive Hilbert structures have a common positive limit, since the semilocal inner product can depend on the finite set of places.

These are the first places this idea can die.

## 12. Bottom line

The Round-002 divergence appears to be concentrated in a single, degree-like common mode:

\[
\sum_pM_p|t|.
\]

Its coefficients are exactly the local logarithmic-derivative masses at \(s=1/2\).

The established adelic RH architecture already instructs us to quotient a degree/trivial-correspondence radical and to work at half-density.

The high-value new question is therefore:

\[
\boxed{
\text{Is the common }|t|\text{ tower-repair direction exactly the Suzuki-tent image of the adelic primitive trace radical?}
}
\]

If yes, the supposedly divergent subtraction may be pure gauge, and each prime tower would enter the primitive quotient through a positive representative.

That does not yet prove RH. It gives a sharply defined theorem whose proof would materially change the problem.
