# Duality at infinity, the Weil pairing, and compact reconstruction

**2026-10-09. Claims RMP-005 and RMP-006 are proved below.** The proposed arithmetic positive polarization remains open. The source audit corrects an overbroad explanation; it does not diminish the importance of finding an independently positive arithmetic structure.

## 1. Which part of the geometric analogy is exact?

For a curve over F_q, one can form the genuine projective surface C×C, its correspondences, and an ample class. The Hodge index theorem controls the primitive intersection pairing. The companion note spells out the resulting Gram and the Frobenius/Rosati reversal.

For number fields, it is inaccurate to say that the archimedean place simply has no duality, canonical data, Riemann–Roch, or Hodge index theorem:

| Structure | Established scope | Remaining distinction |
|---|---|---|
| Relative dualizing sheaf | Proper, flat, finitely presented families with Gorenstein fibres of pure dimension one admit an invertible relative dualizing sheaf, compatible with base change. | This does not construct an RH-sufficient self-product over F_1. |
| Arithmetic Riemann–Roch | There are proved theorems for suitable regular arithmetic schemes, including archimedean metric and analytic-torsion corrections. | An index equality does not by itself identify or prove the Weil sign. |
| Arithmetic Hodge index | Faltings–Hriljac and later extensions give primitive intersection inequalities under their hypotheses. | One still needs an arithmetic object to which the exact RH pairing maps. |
| Connes–Consani arithmetic curve | Their constructions include Riemann–Roch, Serre duality, a canonical divisor, and more recent Picard/duality structures. | These statements do not establish the required positive pairing on an RH host surface or cohomology. |
| Spectral approaches | Self-adjoint finite or local operators and trace formulas can already be constructed. | Exact limiting recovery of the completed zeta object remains a separate theorem. |

Primary references: [Stacks, Lemma 109.19.3](https://stacks.math.columbia.edu/tag/0E6R); [Gillet–Rossler–Soule, arithmetic RR, Theorem 3.2](https://arxiv.org/pdf/0802.1400); [Moriwaki, TheoremB](https://arxiv.org/pdf/alg-geom/9403011); [Yuan–Zhang, §2.2](https://web.math.princeton.edu/~shouwu/publications/hodge-I-version2.pdf).

For example, the corrected degree-zero arithmetic self-intersection in the Faltings–Hriljac normalization discussed by Yuan–Zhang is minus twice a Neron–Tate height. Infinity is part of that theory. The difficulty is identifying the RH object with a pairing carrying the relevant independent sign.

### The specific “taproot” claim

The chain

> no canonical class, therefore no Serre duality, therefore no RR, therefore no positivity

is not a verified description of all current RH approaches.

In [Connes–Consani 2018, introduction and §3.1](https://arxiv.org/pdf/1805.10501), the intermediate cohomology H¹ on the square is a stated difficulty; their discussion already permits H² to be defined through duality. Their subsequent [RR paper](https://arxiv.org/pdf/2205.01391) includes a Serre-duality theorem. The [later RR refinement, Theorem 1.1](https://arxiv.org/pdf/2306.00456), uses their categorical dimension, a modified ceiling of deg(D)/log2, and canonical divisor K=-2{2}. These are constructions for the arithmetic curve, not a proof of the missing surface positivity.

Their [2026 Jacobian paper, Theorem 8.15 and §9](https://arxiv.org/pdf/2602.15941) develops framed/rooted Picard monoids and a geometric interpretation of a trace formula. Meanwhile [Zeta Spectral Triples, §8](https://arxiv.org/pdf/2511.22755) and [Connes's2026 survey, §6.6](https://arxiv.org/pdf/2602.04022) identify explicit spectral ground-state and approximation obligations. We must not present the 2018 obstacle as the unique unchanged frontier.

A proposed Spec Z ×_{F_1} Spec Z is a serious geometric direction. No cited theorem makes its construction a necessary intermediate step for every possible RH proof.

Finally, on a surface the formula

$$
\chi(O(D))=\chi(O)+\tfrac12D(D-K)
$$

is an Euler-characteristic identity. Its right side can be signed. Extracting the Hodge inequality uses further projective geometry and existence/effectivity arguments. In the genus-one endomorphism proof, nonnegativity of the degree of a genuine morphism has a direct geometric meaning. These are more specific statements than a generic “deg>=0.”

## 2. RMP-005: the exact Connes–Consani/Weil comparison

We now make the claimed common “shadow” precise instead of assigning it by analogy.

### 2.1 Coordinates and the two constraints

Take real v in C_c^infinity(R), put F=v*check(v), with check(v)(t)=v(-t), and define

$$
f(u)=u^{-1/2}v(\log u),\quad u>0.
$$

Use multiplicative convolution with d^*u=du/u and

$$
\widetilde f(u)=u^{-1}f(u^{-1}).
$$

A direct substitution gives

$$
(f*_\times\widetilde f)(e^t)=e^{-t/2}F(t).
\tag{1}
$$

Define

$$
M_\pm(v)=\int e^{\pm t/2}v(t)\,dt,\quad
C(v)=\frac{M_+(v)+M_-(v)}2,\quad
S(v)=\frac{M_+(v)-M_-(v)}2.
$$

Then

$$
\int f(u)\,d^*u=M_-(v),\qquad
\int f(u)\,du=M_+(v).
\tag{2}
$$

Thus the two primitive conditions in Connes–Consani are exactly C=S=0. They are not the single ordinary zero-mean condition on v.

### 2.2 Match the distribution, including its origin constant

Connes–Consani's equations (12)–(14) define s_CC(f,f)=N(f*tilde(f)), with

$$
N(h)=
\sum_{n\ge1}\Lambda(n)h(n)
+\int_1^\infty\frac{u^2h(u)-h(1)}{u^2-1}\frac{du}{u}
+c\,h(1),
\quad
c=\frac{\log\pi+\gamma_E}{2}.
\tag{3}
$$

Using(1) and a_n=Lambda(n)/sqrt(n) gives

$$
s_{\rm CC}(f,f)
=\sum_{n\ge2}a_nF(\log n)+cF(0)+
\int_0^\infty
\frac{e^{-t/2}F(t)-e^{-2t}F(0)}{1-e^{-2t}}\,dt.
\tag{4}
$$

The origin subtraction belongs inside the integral; its two terms cannot be split into independent divergent integrals.

In the repository's additive convention, the completed Weil distribution on the even autocorrelation F is

$$
\begin{aligned}
Q_W(v)={}&2M_+(v)M_-(v)
-2\sum_{n\ge2}a_nF(\log n)
-(\log(4\pi)+\gamma_E)F(0)\\
&-2\int_0^\infty
\frac{e^{-t/2}F(t)-e^{-t}F(0)}{1-e^{-2t}}\,dt.
\end{aligned}
\tag{5}
$$

This is the normalization in [Suzuki 2026, first displayed Weil functional](https://arxiv.org/pdf/2606.09096v3), specialized to real autocorrelations. The compact support makes the prime sum finite.

Subtracting the two renormalized integrals is legitimate, because their difference is integrable:

$$
\int_0^\infty
\frac{e^{-t}-e^{-2t}}{1-e^{-2t}}\,dt
=
\int_0^\infty\frac{e^{-t}}{1+e^{-t}}\,dt
=\log2.
$$

This cancels the difference log(4pi)-log(pi). Since M_+M_-=C²-S², we obtain

$$
\boxed{
Q_W(v)=2(C(v)^2-S(v)^2)-2s_{\rm CC}(f,f).}
\tag{6}
$$

In particular,

$$
\boxed{v\in\mathcal D_0:=\ker M_+\cap\ker M_-
\quad\Longrightarrow\quad
Q_W(v)=-2s_{\rm CC}(f,f).}
\tag{7}
$$

The source's primitive intersection target s_CC<=0 therefore has exactly the sign required for Q_W>=0.

This is a coordinate/sign/normalization identification, not a new positivity theorem. For complex tests one can use the corresponding conjugate involution and Hermitian polarization; equation (6) was derived here on the real core matching the cited source.

### 2.3 What follows, and what does not

It is justified to say that the repository's full Weil form and the Connes–Consani primitive intersection form encode the same criterion after this comparison.

It is not justified to conclude solely from the notation Q=P-K that a particular chosen P, K, Hilbert space, compression, or regularization is literally their trace construction. That stronger statement needs an explicit map, its domain, and an operator/form/trace identity. Even two equal quadratic forms can admit very different positive-minus-positive decompositions.

The probe evaluates(4) and (5) independently on normalized smooth compact bumps and on a primitive derivative bump. The comparison residual is below 3e-16 in the recorded run. The outer quadrature estimates are much larger, and are not rigorous enclosures. Dropping the origin constant produces a residual about 1.72195. The analytic proof above, not the floating-point agreement, establishes(6).

## 3. RMP-006: retarded and advanced reconstruction select the same primitive core

Set

$$
L=\partial_t^2-\tfrac14.
$$

Three fundamental solutions are

$$
G_+(t)=2\sinh(t/2)1_{t\ge0},\qquad
G_-(t)=-2\sinh(t/2)1_{t\le0},
$$

$$
G_{\rm dec}(t)=-e^{-|t|/2}.
$$

Each solves the homogeneous equation away from0, is continuous at 0, and has derivative jump1. Hence LG_+=LG_-=LG_dec=delta_0 as distributions.

Their differences are exactly

$$
G_+-G_{\rm dec}=e^{t/2},\qquad
G_--G_{\rm dec}=e^{-t/2}.
$$

For every compact smooth v,

$$
\boxed{
(G_+-G_-)*v
=e^{t/2}M_-(v)-e^{-t/2}M_+(v).}
\tag{8}
$$

This is the entire advanced/retarded disagreement. It has two homogeneous components, with coefficients equal to the two degree/codegree charges.

### The compact reconstruction theorem

The following are equivalent:

1. M_+(v)=M_-(v)=0.
2. G_+*v=G_-*v as functions.
3. The retarded and advanced reconstructions match in both value and first derivative at any chosen gluing time.
4. There exists g in C_c^infinity(R) with Lg=v.

When they hold, g is unique and

$$
g=G_+*v=G_-*v=G_{\rm dec}*v.
\tag{9}
$$

**Proof.** Equation (8), and independence of the two exponential solutions, establish the first three conditions. Equality of the difference and its derivative at one time forces both coefficients to vanish; equality of the value alone would not suffice.

Integration by parts shows M_pm(Lg)=0 for every compact smooth g, because L(e^{pm t/2})=0.

Conversely let v have support in[a,b] and both moments vanish. The retarded convolution is smooth, satisfies Lg=v, and vanishes for t<a. For t>b it is

$$
g(t)=e^{t/2}M_-(v)-e^{-t/2}M_+(v)=0.
$$

Thus it is compactly supported. A compact solution of Lg=0 must vanish, because every global homogeneous solution is Ae^{t/2}+Be^{-t/2}. This proves existence and uniqueness. The difference identities give the equality with the decaying inverse. Square.

Therefore

$$
\boxed{
(\partial_t^2-\tfrac14)C_c^\infty(\mathbb R)=\mathcal D_0.}
\tag{10}
$$

For nonzero g, L preserves the convex hull of its support; it need not preserve every gap inside the support.

### A falsifier for the wrong primitive condition

Take any nonzero nonnegative smooth compact g and set v=g'. Then

$$
\int v=0,\qquad
M_\pm(v)=\mp\tfrac12M_\pm(g)\ne0.
$$

The source is ordinary-mass neutral, but its retarded and advanced reconstructions disagree and have nonzero exterior tails. The script checks exactly this mutation against v=Lg.

### What the theorem contributes to the reversal axis

The endpoint modes e^{±t/2} are the two polar evaluation modes in the completed Weil form. The correct cancellation of their charges is precisely what allows reconstruction from the past and from the future to define one compact object.

This gives a concrete “reassembly” operation on the actual primitive test space. It is not a claim that this elementary differential operator is a geometric dualizing sheaf. It is a test-space model for the boundary and duality obligations that any proposed host must respect.

The retarded formula at t uses only source values before t. Verifying that the entire reconstructed object closes up uses the completed history and its two moment constraints. An online arithmetic process does not gain knowledge of future prime events from this identity.

The Green boundary concomitant explains the two constraints:

$$
\int_a^b((Lg)h-g(Lh))\,dt=[g'h-gh']_a^b.
$$

Pairing with the homogeneous modes h=e^{±t/2} records the two boundary fluxes. Matching one scalar value loses one of them.

## 4. What can play the role of duality at infinity?

There are several precise levels, which should not be conflated.

### 4.1 Densities, inversion, and Mellin duality already exist

On L²(R_+,dx), the involution

$$
(\Theta f)(x)=x^{-1}\overline{f(1/x)}
$$

is antiunitary. The half-density coordinate v(t)=e^{t/2}f(e^t) changes it into

$$
(\Theta v)(t)=\overline{v(-t)}.
$$

For f in C_c^infinity(R_+), the Mellin transform M f(s)=int_0^infinity f(x)x^{s-1}dx satisfies

$$
M(\Theta f)(s)=\overline{Mf(1-\overline s)}.
\tag{11}
$$

The weight x^{-1} is forced by the density; dropping it changes the duality. The normalization centers the spectral reflection at 1/2.

For the standard real even Tate integral,

$$
\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2),\quad
Z(e^{-\pi x^2},s)=\Gamma_{\mathbb R}(s).
$$

Fourier duality supplies the local factor

$$
Z(\widehat f,1-s)
=
\frac{\Gamma_{\mathbb R}(1-s)}{\Gamma_{\mathbb R}(s)}\,Z(f,s)
$$

in this normalization. On the critical line the ratio has modulus1. See [Poonen, Tate's thesis notes, Theorem 4.18](https://math.mit.edu/~poonen/786/notes.pdf).

This is actual archimedean harmonic duality. It does not make the Gamma function a sheaf, and it does not prove positivity after the arithmetic coupling and primitive subtraction.

### 4.2 The finite and infinite completions are coupled, not interchangeable coordinate charts

R and Q_p have different topologies and are not literally two Lorentz frames. A mathematically meaningful common-law requirement comes from one global rational field and its adelic compatibility.

For a in Q*, the product formula is

$$
|a|_\infty\prod_p|a|_p=1.
$$

A rational dilation by p expands real Haar volume by p and scales p-adic Haar volume by p^{-1}. The global product is preserved. Under the standard self-dual measures, additive Fourier transform interchanges dilation by a and by a^{-1}. Poisson summation couples the local factors. See [Garrett, Iwasawa–Tate, §§3.3–3.6](https://www-users.cse.umn.edu/~garrett/m/mfms/notes_c/Iwasawa-Tate.pdf).

This supplies a rigorous replacement for the reference-frame intuition: require the local actions, measures, and Fourier dualities to arise from one global structure. It does not identify a finite-field curve with a finite place of Q, nor turn the functional equation into physical time reversal.

Keep separate the arithmetic succession index n, logarithmic scaling t=log n, the Suzuki deformation parameter omega, and any auxiliary unitary dilation clock. An equality between them requires proof.

### 4.3 The missing stronger datum is a compatible positive polarization

Deninger's [conjectural cohomological formalism, §2](https://arxiv.org/html/1001.1621v1) first has a cup-product/trace duality pairing rho with1-rho. It separately asks for an antilinear Hodge star making the pairing positive and compatible with the scaling action.

In degree1, the resulting identity is

$$
(\theta x,y)+(x,\theta y)=(x,y).
$$

For an eigenvector theta x=rho x in a positive space,

$$
2\operatorname{Re}\rho\,\|x\|^2=\|x\|^2.
$$

The finite-dimensional proposition in the companion note proves this logic explicitly and supplies a counterexample when positive compatibility is absent.

An arithmetic construction still needs the trace/determinant identity that recovers the completed zeta function and all its relevant zeros, as well as analytic control of domains. Neither a formal star nor a positive space unrelated to the target suffices.

## 5. The sharper research direction

The teacup axis leads to a specific order of work:

1. Retain the complete arithmetic history, including mixed products and reverse/forward ratio paths.
2. Identify the duality and both boundary charges from the actual measures, source operators, and global additive completion.
3. Choose a topology in which the relevant cohomology or source quotient is nontrivial; the ordinary closed zeta multiplier has zero reduced Hilbert cokernel.
4. Derive a canonical positive polarization compatible with this dynamics, or exhibit its failure with the finite Gram controls.
5. Prove that the resulting pairing is the full completed Weil form, with the exact primitive comparison and origin terms above.

Steps1–3 now have additional exact constructions and failure tests. Step4 coupled to step 5 is still the RH-bearing task. Calling it a dualizing sheaf does not discharge it; specifying and verifying the pairing, its domain, and its sign would.

