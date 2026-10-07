# Shadow-SUCC support geometry: affine loop holonomy, LCM support, and Suzuki conductor cells

**Date:** 2026-10-07  
**Branch:** \`aletheia/succ-loop-support-curvature-2026-10-07\`  
**Status:** Sections 1--9 are exact algebra/combinatorics. Sections 10--12 give a concrete proof program and clearly marked conjectural curvature layer.  
**RH remains open.**

This note formalizes the user's new idea:

> arithmetic/algebraic SUCC paths can close as loops while a hidden support/history layer remembers the path; finite values of \(N\) can already support whole families of loops before those loop-values are visibly actualized along the ordinary integer ordering.

The central result is that this is not metaphorical.

There is an exact primitive-affine lift in which a visibly closed arithmetic loop can leave a **central integer holonomy**. Those holonomies are naturally supported by the same LCM clocks and exact-conductor spaces \(W_n\) already used in the finite Suzuki realization.

---

# 1. Primitive affine forms and the forgotten central scalar

Consider a rational affine form

\[
f(x)=\frac{ax+b}{c},
\]

with

\[
a,b,c\in\mathbb Z,\qquad a>0,\quad c>0,
\]

written in primitive form

\[
\gcd(a,b,c)=1.
\]

Associate the upper-triangular integer matrix

\[
\boxed{
M_f=
\begin{pmatrix}
a&b\\
0&c
\end{pmatrix}.
}
\]

Projectively,

\[
M_f
\]

acts by

\[
x\longmapsto \frac{ax+b}{c}.
\]

Multiplying \(M_f\) by a nonzero scalar does not change the visible affine map.

The **primitive matrix**, however, retains a canonical representative of the algebraic form.

This gives two levels:

\[
\boxed{
\text{visible affine map}
=
\text{projective quotient},
}
\]

\[
\boxed{
\text{shadow/provenance form}
=
\text{primitive integer lift}.
}
\]

---

# 2. Composition produces an integer 2-cocycle

Let \(f,g\) be primitive affine forms.

Their matrix product is integral:

\[
M_fM_g.
\]

Let

\[
\operatorname{cont}(A)
\]

denote the positive gcd of the nonzero integer entries of an integer matrix \(A\).

The primitive matrix of the composite is

\[
\boxed{
M_{f\circ g}
=
\frac{
M_fM_g
}{
\kappa(f,g)
},
}
\]

where

\[
\boxed{
\kappa(f,g)
=
\operatorname{cont}(M_fM_g)
\in\mathbb N.
}
\]

Associativity of matrix multiplication implies

\[
\boxed{
\kappa(f,g)\,
\kappa(f\circ g,h)
=
\kappa(g,h)\,
\kappa(f,g\circ h).
}
\]

Thus \(\kappa\) is an exact multiplicative 2-cocycle for the primitive section of the projective affine semigroup.

The projective quotient forgets \(\kappa\).

The provenance lift remembers it.

This is a precise candidate for **shadow-SUCC curvature data**.

---

# 3. Universal closed loops have central holonomy

Let

\[
\gamma=(f_1,\ldots,f_r)
\]

be a composable word.

Suppose the visible composite is the identity affine map:

\[
f_r\circ\cdots\circ f_1(x)=x
\qquad\text{for every }x.
\]

Then the primitive matrix of the visible endpoint is \(I\).

Therefore the unnormalized matrix product must be

\[
\boxed{
M_{f_r}\cdots M_{f_1}
=
\kappa(\gamma)\,I
}
\]

for a unique positive integer

\[
\boxed{
\kappa(\gamma)\in\mathbb N.
}
\]

Call \(\kappa(\gamma)\) the **central loop holonomy**.

The base arithmetic path closes.

The lifted path need not be trivial.

That is exactly the requested distinction between visible SUCC and shadow support.

---

# 4. The user's Collatz-style loop has holonomy \(24=4!\)

Take

\[
f_1(x)=4x+1,
\]

\[
f_2(x)=\frac{3x+1}{8},
\]

\[
f_3(x)=\frac{2x-1}{3}.
\]

Their primitive matrices are

\[
M_1=
\begin{pmatrix}
4&1\\
0&1
\end{pmatrix},
\qquad
M_2=
\begin{pmatrix}
3&1\\
0&8
\end{pmatrix},
\qquad
M_3=
\begin{pmatrix}
2&-1\\
0&3
\end{pmatrix}.
\]

Direct multiplication gives

\[
\boxed{
M_3M_2M_1
=
\begin{pmatrix}
24&0\\
0&24
\end{pmatrix}
=
24I.
}
\]

Hence

\[
\boxed{
\kappa(\gamma)=24=2^3\cdot3=4!.
}
\]

And indeed the visible composite simplifies identically:

\[
\frac{
2\left(
\frac{3(4x+1)+1}{8}
\right)-1
}{3}
=x.
\]

So the loop is stronger than a cycle through the point \(3\).

It is an identity relation of affine forms whose primitive lift has nontrivial central content.

This is a genuine closed arithmetic loop carrying hidden multiplicative history.

---

# 5. Every positive integer is a loop holonomy

For every

\[
n\ge1,
\]

consider the two primitive affine forms

\[
u_n(x)=nx+1,
\]

\[
d_n(y)=\frac{y-1}{n}.
\]

Their matrices are

\[
U_n=
\begin{pmatrix}
n&1\\
0&1
\end{pmatrix},
\qquad
D_n=
\begin{pmatrix}
1&-1\\
0&n
\end{pmatrix}.
\]

Then

\[
\boxed{
D_nU_n=nI.
}
\]

Hence

\[
d_n\circ u_n=\operatorname{id},
\]

while the lifted loop has

\[
\boxed{
\kappa(\ell_n)=n.
}
\]

Therefore

\[
\boxed{
\mathbb N_{>0}
=
\{\text{central holonomies of primitive affine identity loops}\}.
}
\]

This gives an exact answer to the idea of constructing an \(\mathbb N\) “underneath” ordinary \(\mathbb N\):

ordinary positive integers can be read as the central support/holonomy spectrum of closed SUCC/FUCC-compatible affine histories.

The visible endpoint is trivial.

The hidden integer labels the amount of algebraic support/history erased by projectivization.

---

# 6. Prime-valuation geometry separates breadth, support, and accumulated history

Write

\[
n=\prod_p p^{v_p(n)}.
\]

There are three different natural profiles.

## 6.1 Prime skeleton / breadth

\[
\boxed{
\operatorname{rad}(n)
=
\prod_{p\mid n}p.
}
\]

This records only **which prime directions are present**.

Its support rank is

\[
\boxed{
\omega_0(n)
=
\#\{p:p\mid n\}.
}
\]

## 6.2 Minimal joint finite support

For a finite family of loop holonomies

\[
F=\{n_1,\ldots,n_r\},
\]

the smallest cyclic clock that contains every exact-conductor sector \(W_{n_j}\) is

\[
\boxed{
S(F)
=
\operatorname{lcm}(n_1,\ldots,n_r).
}
\]

Indeed,

\[
W_d\subset L^2(\mathbb Z/L\mathbb Z)
\]

iff

\[
d\mid L.
\]

Thus any supporting clock must be divisible by all \(n_j\), and the LCM is minimal.

This is the **support join**.

In valuation coordinates it is componentwise maximum:

\[
v_p(S(F))
=
\max_j v_p(n_j).
\]

## 6.3 Accumulated loop history

If all loops in the family are traversed independently, the total central holonomy is

\[
\boxed{
H(F)
=
\prod_j n_j.
}
\]

In valuation coordinates this is componentwise sum:

\[
v_p(H(F))
=
\sum_jv_p(n_j).
\]

Thus:

\[
\boxed{
\text{LCM}=\text{minimal support / max},
}
\]

\[
\boxed{
\text{product}=\text{accumulated history / sum}.
}
\]

This distinction is load-bearing.

Repeatedly using the same prime direction increases history without increasing the depth of the minimal common support.

---

# 7. Factorial, LCM, and primorial are three projections of one loop family

Take the canonical loop family

\[
\mathcal F_N
=
\{\ell_1,\ell_2,\ldots,\ell_N\},
\]

where

\[
\kappa(\ell_n)=n.
\]

Then:

### accumulated history

\[
\boxed{
H(\mathcal F_N)
=
\prod_{n\le N}n
=
N!.
}
\]

### minimal joint support

\[
\boxed{
S(\mathcal F_N)
=
\operatorname{lcm}(1,\ldots,N)
=
L_N.
}
\]

### prime-direction skeleton

\[
\boxed{
\operatorname{rad}(L_N)
=
\prod_{p\le N}p
=
N\#.
}
\]

So the user's factorial/primorial intuition separates exactly into:

\[
\boxed{
N!
=
\text{total path usage},
}
\]

\[
\boxed{
L_N
=
\text{minimal substrate needed to support all paths},
}
\]

\[
\boxed{
N\#
=
\text{which prime directions have been opened at all}.
}
\]

Their prime valuations make the distinction explicit:

\[
\boxed{
v_p(N\#)=1_{p\le N},
}
\]

\[
\boxed{
v_p(L_N)=\lfloor\log_pN\rfloor,
}
\]

\[
\boxed{
v_p(N!)
=
\sum_{j\ge1}
\left\lfloor
\frac{N}{p^j}
\right\rfloor.
}
\]

These are respectively:

- presence;
- maximal required depth;
- total accumulated multiplicity.

---

# 8. The LCM clock is the minimal universal harmonic support

The exact-conductor decomposition is

\[
\boxed{
L^2(\mathbb Z/L_N\mathbb Z)
=
\bigoplus_{d\mid L_N}W_d,
}
\]

with

\[
\dim W_d=\varphi(d).
\]

Every integer

\[
n\le N
\]

divides \(L_N\).

Hence every exact-conductor harmonic sector

\[
W_1,\ldots,W_N
\]

is present.

Conversely, any single cyclic clock containing \(W_n\) for all \(n\le N\) must have modulus divisible by every \(1\le n\le N\), hence by \(L_N\).

Therefore:

\[
\boxed{
L_N
\text{ is the unique minimal single-clock harmonic support for all conductor loops }n\le N.
}
\]

This upgrades the earlier “LCM clock” from a convenient container to a universal minimality statement.

---

# 9. Support birth can precede visible arithmetic actualization

Define the **support-birth threshold**

\[
\boxed{
\beta(n)
=
\min\{N:n\mid L_N\}.
}
\]

If

\[
n=\prod_pp^{k_p},
\]

then

\[
n\mid L_N
\]

iff

\[
p^{k_p}\le N
\]

for every \(p\mid n\).

Hence

\[
\boxed{
\beta(n)
=
\max_{p^k\parallel n}p^k.
}
\]

This is a major distinction.

The ordinary integer \(n\) is actualized along the visible SUCC backbone only at \(n\).

But its exact-conductor harmonic sector \(W_n\) already exists as soon as

\[
N=\beta(n).
\]

For a prime power,

\[
\beta(p^k)=p^k.
\]

So support birth and visible event coincide.

For a mixed conductor,

\[
\boxed{
\beta(n)<n
}
\]

unless one prime-power factor already equals \(n\).

Example:

\[
24=2^3\cdot3,
\]

so

\[
\boxed{
\beta(24)=8.
}
\]

Indeed

\[
24\mid L_8=840.
\]

Thus the harmonic support for the user's \(24\)-loop exists by support scale \(8\), long before visible SUCC reaches the integer \(24\).

This is an exact realization of:

> a sufficiently large \(N\) can already support a loop family whose visible values live much farther out.

For a finite loop family \(F\),

\[
\boxed{
N_F
=
\max_{\gamma\in F}\beta(\kappa(\gamma))
}
\]

is the minimal LCM-filtration stage whose single clock supports every loop holonomy in \(F\).

---

# 10. Support box versus actualization simplex

Prime-valuation coordinates make the geometry stark.

Write

\[
\alpha_p=v_p(n).
\]

The visible multiplicative height is

\[
\boxed{
h_1(\alpha)
=
\sum_p\alpha_p\log p
=
\log n.
}
\]

Support birth is controlled by

\[
\boxed{
h_\infty(\alpha)
=
\max_p\alpha_p\log p
=
\log\beta(n).
}
\]

Thus:

\[
\boxed{
\text{visible size}
=
\ell^1\text{-type height},
}
\]

while

\[
\boxed{
\text{support birth}
=
\ell^\infty\text{-type height}.
}
\]

At support stage \(N=e^T\), the LCM clock contains the finite valuation box

\[
\boxed{
\alpha_p\log p\le T
\quad
\text{for every }p.
}
\]

But a Suzuki causal event at log time \(t\) is active only if

\[
\boxed{
\sum_p\alpha_p\log p
\le t.
}
\]

So the finite conductor system has two geometries:

1. a pre-existing **support box**;
2. an advancing **actualization simplex/wavefront**.

Mixed-prime conductors can lie inside the support box while still outside the visible causal simplex.

That region is the mathematically precise **shadow-support sector**.

---

# 11. Minimal examples

## \(N=1\)

\[
L_1=1.
\]

There is only

\[
W_1.
\]

This is bare SUCC support with no nontrivial harmonic innovation.

## \(N=2\)

\[
L_2=2,
\]

and

\[
L^2(\mathbb Z/2\mathbb Z)
=
W_1\oplus W_2.
\]

The new exact-conductor space has

\[
\dim W_2=\varphi(2)=1.
\]

It is the zero-sum mode spanned by

\[
(1,-1).
\]

So the user's primitive shadow form

\[
1-1
\]

has an exact harmonic realization:

\[
\boxed{
W_2
=
\text{the first nontrivial shadow-SUCC mode}.
}
\]

## \(N=3\)

\[
L_3=6.
\]

Now

\[
W_6
\]

already exists, even though visible SUCC has only reached \(3\).

This is the first mixed-prime shadow conductor.

It is the natural harmonic support for coherent \(2\)-versus-\(3\) relations such as

\[
2a-3b=0.
\]

Thus:

\[
\boxed{
2
=
\text{first nontrivial difference mode},
}
\]

\[
\boxed{
3
=
\text{first support stage at which a genuine two-prime mixed relation }W_6\text{ exists}.
}
\]

---

# 12. Minimal support growth is exactly the von Mangoldt event stream

The LCM support changes only when \(N\) reaches a new prime-power depth.

Indeed,

\[
\boxed{
\log L_N
=
\psi(N),
}
\]

the Chebyshev function.

Therefore

\[
\boxed{
\log L_N-\log L_{N-1}
=
\Lambda(N).
}
\]

This gives a new exact interpretation:

\[
\boxed{
\Lambda(N)
=
\text{increment of logarithmic minimal universal support at SUCC step }N.
}
\]

The omega-zero conductor-jet theorem on the parent branch proved

\[
\boxed{
b_0'(N)
=
\frac{2\Lambda(N)}{\sqrt N}.
}
\]

Hence

\[
\boxed{
\frac12 b_0'(N)
=
\frac{
\log L_N-\log L_{N-1}
}{
\sqrt N
}.
}
\]

So the prime-power weight in the Weil/Suzuki first jet is exactly:

\[
\boxed{
\text{half-density-weighted increment of minimal shadow-support complexity}.
}
\]

This is perhaps the cleanest connection between the user's support picture and the fixed RH proof target.

---

# 13. Mixed conductors are relations inside existing support, not new support atoms

If \(n\) is not a prime power, then

\[
\Lambda(n)=0.
\]

Equivalently,

\[
L_n=L_{n-1}.
\]

So the arrival of the visible integer \(n\) does **not** enlarge the minimal universal clock.

Yet Suzuki's exact conductor family still contains a nonzero coefficient

\[
b_\omega(n)
\]

for every \(\omega>0\).

This says:

\[
\boxed{
\text{prime powers add new support;}
}
\]

\[
\boxed{
\text{mixed composites activate new relations/interactions inside support that already existed.}
}
\]

This precisely separates:

- substrate growth;
- interaction actualization.

That distinction was absent from the static direct-sum conductor picture.

---

# 14. The Suzuki jet filtration is the support-cell filtration

Recall

\[
b_\omega(n)
=
n^{\omega-\frac12}
\prod_{p\mid n}(1-p^{-2\omega}).
\]

Let

\[
r=\omega_0(n)
=
\#\{p:p\mid n\}.
\]

Then

\[
\boxed{
b_\omega(n)
=
\frac{
(2\omega)^r
}{
\sqrt n
}
\prod_{p\mid n}\log p
+
O(\omega^{r+1}).
}
\]

Therefore

\[
\boxed{
b_0^{(j)}(n)=0
\qquad(j<r),
}
\]

and

\[
\boxed{
\frac1{r!}b_0^{(r)}(n)
=
\frac{
2^r
}{
\sqrt n
}
\prod_{p\mid n}\log p.
}
\]

The first nonzero jet order equals the number of prime directions needed to support the interaction.

Thus:

\[
\boxed{
\begin{array}{ccl}
r=1&:&\text{prime-power support edges / Weil layer},\\
r=2&:&\text{two-prime interaction cells},\\
r=3&:&\text{three-prime interaction cells},\\
&\vdots&
\end{array}
}
\]

This is exactly the requested “family of SUCC loops” grading.

The full Suzuki deformation is a generating function over support dimension.

---

# 15. The user's \(24\)-loop is a second-jet interaction

For

\[
24=2^3\cdot3,
\]

the support rank is

\[
r=2.
\]

Hence

\[
b_0'(24)=0,
\]

but

\[
\boxed{
\frac12 b_0''(24)
=
\frac{
4\log2\,\log3
}{
\sqrt{24}}.
}
\]

So the loop

\[
M_3M_2M_1=24I
\]

is invisible to the first/Weil jet and appears at the first genuinely mixed-prime order.

This is not accidental:

\[
\boxed{
\text{central loop holonomy with }r\text{ distinct prime supports}
\Longrightarrow
\text{first appearance at Suzuki jet }r.
}
\]

For the user example, the arithmetic interaction is therefore literally a **second-order conductor cell**.

---

# 16. A positive loop energy

A central holonomy

\[
n
\]

corresponds in log coordinates to the displacement

\[
\log n.
\]

Let

\[
(\tau_{\log n}v)(x)
=
v(x-\log n).
\]

The natural closed-loop Dirichlet energy is

\[
\boxed{
\mathcal E_n(v)
=
\|v-\tau_{\log n}v\|_2^2
\ge0.
}
\]

On Fourier modes \(e^{itx}\),

\[
\mathcal E_n
\]

has symbol

\[
\boxed{
|1-n^{-it}|^2
=
2\bigl(1-\cos(t\log n)\bigr).
}
\]

For a prime-power holonomy

\[
n=p^k,
\]

the first Suzuki jet assigns the weight

\[
\frac{\log p}{p^{k/2}},
\]

and the prime-ray contribution to the localized Weil form is exactly

\[
\boxed{
\sum_{p^k}
\frac{\log p}{p^{k/2}}
\mathcal E_{p^k}(v).
}
\]

So the already-proved Weil prime-ray Dirichlet energy is literally the weighted energy of the **one-prime closed support loops**.

For a mixed conductor \(n\) with \(r\) prime supports, define the top-support \(r\)-jet loop weight

\[
\boxed{
w_r(n)
=
\frac{
2^r
}{
\sqrt n
}
\prod_{p\mid n}\log p.
}
\]

Then

\[
\boxed{
w_r(n)\mathcal E_n(v)
}
\]

is a canonical positive energy associated with the newly appearing \(r\)-support conductor cell.

This is an exact positive object.

It is **not yet** claimed to equal the entire \(r\)-th derivative of Suzuki passivity, because lower-support conductors and Archimedean derivatives also contribute at higher orders.

---

# 17. Divisor cubes and support-cell boundaries

Fix

\[
n=\prod_{j=1}^r p_j^{k_j}.
\]

Forget the internal depth along each prime ray for a moment and ask only whether the full prime-power block

\[
p_j^{k_j}
\]

is present.

The subsets

\[
J\subseteq\{1,\ldots,r\}
\]

form an \(r\)-cube with vertices

\[
\boxed{
n_J
=
\prod_{j\in J}p_j^{k_j}.
}
\]

The Suzuki support factor expands as

\[
\boxed{
\prod_{p\mid n}(1-p^{-2\omega})
=
\sum_{J\subseteq\operatorname{supp}(n)}
(-1)^{|J|}
\prod_{p\in J}p^{-2\omega}.
}
\]

These are exactly the alternating signs of an \(r\)-fold augmentation/cubical boundary.

Thus the exact-conductor coefficient already contains a finite oriented support-cell structure.

The order-\(r\) zero at \(\omega=0\) is the statement that all lower faces cancel until the full \(r\)-dimensional interaction is resolved.

This is an exact algebraic realization of “shadow SUCC support curvature.”

---

# 18. Candidate connection/curvature operator — CONJECTURAL PROGRAM

The divisor/support complex itself is flat: multiplication by distinct primes commutes.

The arithmetic interaction can therefore not live in the bare cube.

It must live in the **connection induced by SUCC/carry/history on that cube**.

For a support edge in prime direction \(p\), let

\[
U_{p,d}
\]

denote the actual refinement/carry transport from the fiber over conductor \(d\) to the fiber over \(pd\).

For a two-prime square, compare the two paths

\[
d
\to
pd
\to
pqd
\]

and

\[
d
\to
qd
\to
pqd.
\]

Define the curvature defect

\[
\boxed{
F_{p,q}(d)
=
U_{q,pd}U_{p,d}
-
U_{p,qd}U_{q,d}.
}
\]

Pure FUCC pullback gives

\[
F_{p,q}=0.
\]

So any nonzero value must come from the same extra structures already known to carry arithmetic information:

- SUCC carrier ordering;
- carry boundaries;
- history/augmentation;
- half-density weighting;
- Archimedean completion.

The corresponding positive curvature energy is

\[
\boxed{
\|F_{p,q}(d)v\|^2.
}
\]

This is the precise next object suggested by the user's “arithmetic interaction curvature” language.

No claim is made yet that this curvature equals the RH kernel.

That is the experiment/theorem target.

---

# 19. Refined finite-conductor Suzuki architecture

The old exact factorization was

\[
H_{\omega,a}
=
V_{\omega,a}^*
\mathbb G_{\omega,a}
V_{\omega,a},
\]

with active exact conductors

\[
n<a^2.
\]

The new support picture says that those active conductors should be regarded as a moving physical slice inside a larger finite parent clock:

\[
\boxed{
L^2(\mathbb Z/L_M\mathbb Z),
\qquad
M\approx a^2.
}
\]

This parent contains:

### active/actualized sectors

\[
W_n,\qquad n\le M;
\]

### shadow-supported sectors

\[
W_d,\qquad
d\mid L_M,\quad d>M.
\]

The shadow sectors are not new zeta data.

They are forced by the minimal finite clock that already supports the active loop family.

The new proof question is whether the finite Suzuki compression can be realized as the physical compression/Schur complement of a **positive loop-energy operator on the whole support clock**, with the shadow sectors supplying the missing completion terms.

If such a construction is possible without inserting zero information, finite conductor passivity would follow structurally.

This is a legitimate new route.

It does not change the fixed goalpost:

\[
\boxed{
\|H_{\omega,a}\|\le1.
}
\]

---

# 20. Why this could address the present global-counterterm wall

The first Suzuki/Weil jet already gave

\[
\boxed{
\text{positive Archimedean difference energy}
+
\text{positive prime-loop energy}
-
\text{global counterterm}.
}
\]

Prime powers are exactly the stages where the minimal LCM support grows:

\[
\Delta\log L_N=\Lambda(N).
\]

Mixed conductors do not enlarge support; they encode relations inside the support already present.

But the nonlinear Suzuki family contains precisely those mixed conductors at higher jet order.

Therefore a plausible mechanism is:

\[
\boxed{
\text{first jet}
=
\text{support-growth energy},
}
\]

\[
\boxed{
\text{higher jets}
=
\text{closed-loop interaction/curvature inside the pre-existing support}.
}
\]

The missing global counterterm may be the diagonal shadow of eliminating those higher-dimensional support cells.

This is a hypothesis, not yet a theorem.

But unlike a new RH characterization, it supplies a concrete positive parent object and a finite falsifiable test.

---

# 21. Immediate probes

1. **Affine-cocycle controls.**  
   Verify primitive normalization, cocycle identity, and loop holonomies on random small affine identities.

2. **Support-birth table.**  
   For \(n\le N\), compute
   \[
   \beta(n)=\max_{p^k\parallel n}p^k
   \]
   and classify the shadow lag
   \[
   \log n-\log\beta(n).
   \]

3. **Collatz-loop placement.**  
   Place the \(24\)-loop in the support box at birth \(8\), confirm its second-jet coefficient, and identify the corresponding \(W_{24}\) block inside \(H_{L_8}\).

4. **Two-prime curvature squares.**  
   Use the already implemented LCM boundary/carry refinement operators to compute
   \[
   F_{p,q}(d)
   \]
   for small \(p,q,d\).

5. **Mutation controls.**  
   Pure commuting FUCC transport must give zero curvature. Randomized carry/boundary wiring should destroy any special arithmetic identities.

6. **Schur-complement test.**  
   Partition the full support clock into active and shadow sectors and test whether eliminating shadow sectors produces the observed Suzuki finite matrix or its first few \(\omega\)-jets.

7. **First-jet recovery.**  
   Any proposed parent must reduce exactly to
   \[
   \sum_{p^k}
   \frac{\log p}{p^{k/2}}
   \|v-\tau_{k\log p}v\|^2
   \]
   at first order.

8. **Second-jet test.**  
   The top-support contribution of a mixed conductor \(n=p^kq^\ell\) must carry
   \[
   \frac{4\log p\log q}{\sqrt n}
   \]
   as its Taylor coefficient.

These are finite, mutation-sensitive, and directly attached to the fixed passivity theorem.

---

# 22. Compact statement of the insight

\[
\boxed{
\text{Visible }\mathbb N
=
\text{actualization order}.
}
\]

\[
\boxed{
L_N
=
\text{minimal harmonic support beneath the first }N\text{ loop holonomies}.
}
\]

\[
\boxed{
N\#
=
\text{opened prime directions}.
}
\]

\[
\boxed{
N!
=
\text{accumulated path history}.
}
\]

\[
\boxed{
\Lambda(N)
=
\Delta\log L_N
=
\text{new support injected at step }N.
}
\]

\[
\boxed{
\text{prime powers}
=
\text{support-growth events / first Suzuki jet}.
}
\]

\[
\boxed{
\text{mixed composites}
=
\text{relations inside support / higher Suzuki jets}.
}
\]

And the user's closed affine example gives

\[
\boxed{
\text{visible identity}
\quad+\quad
\text{hidden central holonomy }24
\quad+\quad
\text{support birth }8
\quad+\quad
\text{second-jet rank }2.
}
\]

That is a concrete arithmetic interaction geometry, not merely a metaphor.
