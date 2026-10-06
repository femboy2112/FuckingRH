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


## 13. Exact analytic continuation of the total repair coefficient

For \(\Re s>1\),

\[
-\frac{\zeta'}{\zeta}(s)
=
\sum_{n\ge2}\frac{\Lambda(n)}{n^s}
=
\sum_p\sum_{k\ge1}\frac{\log p}{p^{ks}}
=
\sum_p\frac{\log p}{p^s-1}.
\]

Thus the \(s\)-deformed sharp tower repair coefficient is

\[
M_p(s)=\frac{\log p}{p^s-1},
\]

and at the critical half-density its literal local value is \(M_p(1/2)=M_p\).

The positive sum \(\sum_p M_p(1/2)\) diverges. However its canonical analytic continuation through the logarithmic derivative is finite because \(\zeta(1/2)\ne0\):

\[
\operatorname{AC}_{s\to1/2}\sum_pM_p(s)
=
-\frac{\zeta'}{\zeta}\left(\frac12\right).
\]

The completed functional equation for

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

gives \(\xi'(1/2)=0\), while the derivatives of \(s(s-1)\) cancel at \(1/2\). Therefore

\[
\boxed{
-\frac{\zeta'}{\zeta}\left(\frac12\right)
=
\frac12\left[
\psi\left(\frac14\right)-\log\pi
\right].
}
\]

But this is **exactly the linear Archimedean coefficient** \(B\) in Suzuki's smooth term:

\[
A(t)=\cdots +Bt+\cdots,
\qquad
B=\frac12\left[\psi\left(\frac14\right)-\log\pi\right].
\]

Numerically,

\[
B\approx -2.6860917096128327911.
\]

Hence:

\[
\boxed{
\text{Suzuki's Archimedean linear coefficient}
=
\text{analytic continuation of the total sharp prime-tower repair tax}.
}
\]

This is an exact identity, not an asymptotic analogy.

It does **not** justify termwise analytic continuation of positive CND sums or preserve positivity by itself. Indeed the continued total coefficient is negative although every literal \(M_p(1/2)\) is positive. The identity instead identifies precisely where the required global renormalization is already encoded in the completed zeta formula.

## 14. A one-parameter positive family above the Euler-product line

For \(\sigma>1\), define

\[
h_{p,\sigma}(t)
=
(\log p)\sum_{k\ge1}p^{-k\sigma}(|t|-k\log p)_+,
\]

\[
M_p(\sigma)=\frac{\log p}{p^\sigma-1},
\qquad
D_{p,\sigma}(t)=M_p(\sigma)|t|-h_{p,\sigma}(t).
\]

The same interval-Gram proof as at \(\sigma=1/2\) shows every \(D_{p,\sigma}\) is CND. Since

\[
\sum_pM_p(\sigma)<\infty\qquad(\sigma>1),
\]

the global sum

\[
D_\sigma(t)=\sum_pD_{p,\sigma}(t)
\]

is manifestly CND there.

For fixed \(t\), only finitely many prime powers enter the ramp part, so

\[
D_\sigma(t)
=
-\frac{\zeta'}{\zeta}(\sigma)|t|
-
\sum_{p^k\le e^{|t|}}
(\log p)p^{-k\sigma}(|t|-k\log p).
\]

Thus, modulo the common direction \(|t|\), the class of \(D_\sigma\) is an entire finite-sum function of \(\sigma\), while the only Euler-product pole at \(\sigma=1\) lies in the common \(|t|\) direction.

This supplies a precise deformation:

\[
\text{manifest CND for }\sigma>1
\longrightarrow
\text{critical half-density }\sigma=\frac12.
\]

Positivity is **not known** to analytically continue across \(\sigma=1\). Establishing an operator/quotient formulation in which the common-mode singularity is removed while positivity survives would be a genuine proof step.

## 15. Linear-gauge rigidity: quotienting by \(|t|\) is logically safe if a finite positive lift exists

Define the class of \(\Psi\) modulo the common mode \(\mathbb R|t|\). Say that the class has a **finite CND lift** if there exists a finite real constant \(c\) such that

\[
F_c(t)=\Psi(t)+c|t|
\]

is CND.

Then

\[
\boxed{
\mathrm{RH}
\iff
\exists c\in\mathbb R:
\Psi+c|t|\text{ is CND}.
}
\]

Proof:

- RH implies \(\Psi\) is CND, so \(c=0\) works.
- Conversely, if \(F_c\) is CND, every continuous normalized CND function on \(\mathbb R\) has at-most-quadratic growth. Therefore
  \[
  \Psi(t)=F_c(t)-c|t|=O(1+t^2).
  \]
  Round 001's transform lemma then forces RH: polynomial growth makes the Suzuki transform holomorphic throughout the upper half-plane, excluding zeros of \(\xi\) to the right of \(1/2\), and functional symmetry finishes.

There is a sharper rigidity statement:

\[
\boxed{
\Psi+c|t|\text{ is CND}
\iff
\mathrm{RH}\text{ and }c\ge0.
}
\]

Under RH, \(\Psi\) has a purely atomic positive Lévy measure on the real zero ordinates, while

\[
|t|
=
\int_{\mathbb R}(1-\cos(tx))\frac{dx}{\pi x^2}.
\]

Thus \(c\ge0\) is sufficient. If \(c<0\), uniqueness of the Lévy–Khintchine decomposition would give a negative absolutely continuous density \(c/(\pi x^2)\) away from the atomic zero measure, impossible for a CND function.

This resolves an important conceptual issue:

- \(|t|\) is **not** a null direction of Suzuki's screw kernel;
- nevertheless, producing **any finite CND lift of the completed class modulo \(|t|\)** is already equivalent to RH.

Therefore a primitive/radical construction need not recover the exact lift \(c=0\) immediately. It is enough to prove that the completed adelic class admits some finite positive lift.

## 16. Brownian/Cauchy meaning of the common mode

The same \(|t|\) direction has two exact probabilistic roles:

1. as a variogram,
   \[
   K_{|t|}(s,u)=|s|+|u|-|s-u|=2\min(s,u)
   \]
   for \(s,u\ge0\), the Brownian covariance kernel;
2. as a Lévy exponent,
   \[
   e^{-c|t|}
   \]
   is the characteristic function of a symmetric Cauchy law, with Lévy density
   \[
   \frac{c}{\pi x^2}\,dx.
   \]

Thus changing the finite lift \(c\) adds or removes a universal Brownian/Cauchy continuum background. Under RH the distinguished Suzuki lift \(c=0\) is purely atomic on zero ordinates; positive \(c\) adds a continuous universal background.

This makes the quotient interpretation precise without falsely calling \(|t|\) itself a radical of the screw kernel.


## 17. Suzuki's shifted family is the canonical deformation toward the Euler-product region

Suzuki already defines, for real \(\omega\),

\[
\Psi_\omega(t)
=
e^{-\omega t}\Psi(t)
+
2\omega\int_0^t e^{-\omega u}\Psi(u)\,du
+
\omega^2\int_0^t(t-u)e^{-\omega u}\Psi(u)\,du
\]

for \(t>0\), extended evenly, and proves

\[
\int_0^\infty\Psi_\omega(t)e^{izt}\,dt
=
-\frac1{z^2}\frac{\xi'}{\xi}
\left(\frac12+\omega-iz\right).
\]

Thus the deformation parameter used above is exactly

\[
\sigma=\frac12+\omega.
\]

The prime-power term in the shifted explicit formula has weights

\[
\Lambda(n)n^{-1/2-\omega}
=
\Lambda(n)n^{-\sigma},
\]

so the \(h_{p,\sigma}\) blocks above are the finite-place tower components of Suzuki's canonical shifted family.

Suzuki's Theorem 11.1 states that zero-freeness in

\[
\Re s>\frac12+\omega
\]

is equivalent to eventual nonnegativity of \(\Psi_\omega\). In particular \(\Psi_\omega\ge0\) is unconditional for \(\omega\ge1/2\), because this reaches the classical zero-free half-plane \(\Re s>1\).

Therefore the route

\[
\sigma>1\longrightarrow\sigma=\frac12
\]

is not an invented interpolation; it is the natural Suzuki zero-free deformation.

## 18. The shifted family is a semigroup and damps the Weil accelerant

Let \(T_\omega\) denote the integral operator defining \(\Psi_\omega=T_\omega\Psi\). In Laplace variable \(p\),

\[
\mathcal L[T_\omega f](p)
=
\left(\frac{p+\omega}{p}\right)^2
\mathcal L[f](p+\omega).
\]

Hence

\[
\boxed{T_\eta T_\omega=T_{\eta+\omega}.}
\]

Moreover, direct differentiation gives, on \(t>0\) and distributionally across the event atoms,

\[
\boxed{
\Psi_\omega''(t)=e^{-\omega t}\Psi''(t).
}
\]

Equivalently, if \(W=\Psi''\) is the Weil accelerant distribution,

\[
W_\omega(t)=e^{-\omega|t|}W(t).
\]

Fourier transformation turns multiplication by \(e^{-\omega|t|}\) into convolution with the Poisson/Cauchy kernel

\[
P_\omega(x)=\frac1\pi\frac{\omega}{\omega^2+x^2}
\]

up to the fixed Fourier convention.

Thus Suzuki's horizontal shift is exactly a **Poisson smoothing semigroup on the spectral/Weil distribution**.

This gives a precise phase-boundary interpretation:

- for sufficiently large \(\omega\) (in particular \(\omega\ge1/2\)), the smoothed object is unconditionally positive;
- RH asks whether the boundary object at \(\omega=0\) is already positive;
- general Poisson smoothing can hide signed boundary mass, so positivity at \(\omega=1/2\) alone cannot be inverted without additional arithmetic structure.

The common \(|t|\) repair has Cauchy Lévy density \(1/(\pi x^2)\), so the Brownian/Cauchy mode and the Suzuki shift semigroup are not merely verbal analogies; they occupy adjacent pieces of the same harmonic-analysis geometry.

## 19. Scalar scattering cancellation is too coarse

If the local factors are denoted \(\gamma_v(s)\) and

\[
\rho_v(s)=\frac{\gamma_v(s)}{\gamma_v(1-s)},
\]

then formally, after completed analytic continuation,

\[
\prod_v\rho_v(s)
=
\frac{\Lambda(s)}{\Lambda(1-s)}
=
1
\]

by the functional equation.

Therefore a proof architecture that merely multiplies all scalar local scattering ratios together destroys the RH-bearing information: the global scalar ratio is identically trivial.

The nontrivial information must survive in an **operator, compressed, cohomological, groupoid, or primitive quotient object**. This is exactly why the quasi-inner/Sonin construction studies off-diagonal compressed multiplication operators rather than only the scalar product of local ratios, and why the adelic trace formula passes to primitive cohomology.

This is a useful no-go constraint on the present route: the local scattering-phase identity for \(D_p\) is a building block, but a scalar product of those phases cannot itself encode RH.

## 20. Scattering translation interpretation of the sharp repair

Let

\[
P_p(s)
=
\frac{i}{2}\partial_s
\log\rho_p\left(\frac12+is\right).
\]

Then

\[
P_p(0)=M_p,
\qquad
M_p-P_p(s)\ge0.
\]

Define the linearly phase-renormalized inverse scattering ratio

\[
\widetilde\rho_p(s)
=
e^{-2iM_ps}\rho_p(1/2+is)^{-1}.
\]

Then

\[
\boxed{
\frac{i}{2}\partial_s\log\widetilde\rho_p(s)
=
M_p-P_p(s)\ge0.
}
\]

Thus the sharp tower repair is equivalent to removing the zero-frequency local scattering delay by a linear phase. A linear phase is a translation in the Fourier-conjugate logarithmic coordinate.

This gives a second interpretation of the common \(|t|\) mode: it is the variogram/Lévy shadow of a common translation/scattering-origin freedom. Whether this freedom is precisely implemented by the adelic primitive radical remains an open bridge.
