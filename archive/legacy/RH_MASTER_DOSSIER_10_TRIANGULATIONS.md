# RH MASTER DOSSIER
## Prime multisets, Archimedean completion, Weil positivity, and ten triangulation rounds

**Date:** 2026-08-25  
**Status:** research synthesis; **no proof of the Riemann Hypothesis is claimed**  
**Program:** Schrödinger–Archimedean / prime-powerset–multiset / Weil-form moonshot

---

## Executive verdict

The Riemann Hypothesis is

\[
\boxed{
\rho=\beta+i\gamma\text{ nontrivial zero of }\zeta
\quad\Longrightarrow\quad
\beta=\frac12.
}
\]

Every useful formulation in this dossier converges on the same mathematical obstruction:

\[
\boxed{
\text{an identity is available; an independently forced sign is missing.}
}
\]

The most economical exact formulation is Weil's Hermitian form.  With the completed function

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma\!\left(\frac s2\right)\zeta(s),
\qquad
\Xi(z)=\xi\!\left(\frac12+iz\right),
\]

the centered coordinate of a nontrivial zero is

\[
\lambda_\rho=\frac{\rho-\frac12}{i}
=\gamma-i\left(\beta-\frac12\right).
\]

RH is exactly the statement that every \(\lambda_\rho\) is real.

For a suitable test function \(f\), the explicit formula produces a Hermitian quadratic form \(Q_W(f)\).  On RH, each zero contributes a positive rank-one atom.  Off the line, a functional-equation quartet contributes an indefinite block of signature \((1,1)\).  Consequently,

\[
\boxed{
\mathrm{RH}
\iff
Q_W(f)\ge 0\quad\text{for every admissible }f.
}
\]

The universal quantifier is the content.  One positive finite matrix, one accurate numerical spectrum, or one self-adjoint finite-window operator is not enough.

This dossier performs ten independent triangulations around that sign.  The strongest exact conclusions are:

1. **Prime support and prime multiplicity have distinct spectral roles.**  All-prime support creates the physical zeta divisor; unbounded multiplicity cancels towers of scaled ghost divisors.
2. **Unrestricted multiplicity is rigid.**  Within broad local occupation laws it is the unique nonnegative one-species law that leaves only the physical zeta center \(\Re s=1/2\).
3. **The multiset is an infinite coherent stack of powerset-like digit layers.**  Base-\(q\) exponent digits give canonical cyclic prime clocks and an exact Fredholm determinant for each Euler layer.
4. **The Gamma factor has an exact operator home.**  Ratios \(\Gamma_{\mathbb R}(s)/\Gamma_{\mathbb R}(qs)\) are products of zeta-regularized determinants of shifted number operators.  The finite-prime clocks and the Archimedean fractional-shift channels are two sides of one completed \(q\)-layer.
5. **The functional-equation defect of a finite scale tower localizes entirely at its ultraviolet boundary.**  On the critical line the boundary is a unit-modulus phase, asymptotically dominated by Gamma.
6. **The Archimedean Gaussian creates genuine all-body interaction among prime occupations.**  The free Euler gas factorizes; the theta heat ensemble is strictly log-submodular in distinct prime occupations and carries an independently positive covariance/Fisher geometry.
7. **The zero resolvent is the right zero-forward analytic object.**  RH is equivalent to a Stieltjes/Herglotz property, to positivity of all Pick matrices, and to a reflected Hausdorff moment problem whose coefficients can be computed entirely at safe points \(\Re s>1\).
8. **An off-line zero injects a negative direction quadratically in its horizontal displacement.**  This exact local mechanism explains finite Weil rank–inertia methods.
9. **Easy hidden-operator categories are ruled out.**  Prime-occupation diagonals plus additive Fourier generate the full finite matrix algebra, leaving only scalar commutants; finite differential and local-polarizer searches accordingly fail.
10. **The two most credible forward tracks are distinct:**
    - a full-proof analytic track: an exponentially sharp prolate–Weil second-variation estimate;
    - a weaker-theorem track: higher-moment rank–inertia inequalities extending current finite-Weil results.

The dossier also gives an exact geometric moonshot: construct a polarized absolute cohomology independently of the zeros and prove a Lefschetz–Hodge comparison.  That route remains foundationally deeper, but it is the faithful analogue of Weil's proof over finite fields.

---

## Epistemic labels

Every substantial statement is marked implicitly or explicitly by one of these categories:

- **Established:** standard theorem or directly cited current result.
- **Proved here:** a complete deduction supplied in this dossier; no novelty claim.
- **Calibrated:** numerically checked against an exact identity or known value.
- **Hypothesis:** a proposed bridge with a clear test or proof obligation.
- **Roadblock:** a demonstrated obstruction, no-go statement, or logical circularity.
- **RH-complete:** proving the statement would prove RH; this is not the same as making progress toward it.

No numerical experiment below is presented as evidence sufficient for RH.  The uploaded coherent-truncation work explicitly adopts the correct discipline: the finite operator is built from pole, Gamma, and prime data, while known zeros are used only as external calibration targets.

---

## Core notation

\[
\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2),
\qquad
\Lambda(s)=\Gamma_{\mathbb R}(s)\zeta(s).
\]

\[
\xi(s)=\frac12s(s-1)\Lambda(s),
\qquad
\xi(s)=\xi(1-s).
\]

\[
\Xi(z)=\xi\!\left(\frac12+iz\right),
\qquad
\Xi(-z)=\Xi(z).
\]

\[
\Lambda_{\mathrm{vM}}(n)=
\begin{cases}
\log p,&n=p^m,\\
0,&\text{otherwise},
\end{cases}
\]

where the subscript “vM” is used when necessary to distinguish the von Mangoldt function from the completed zeta \(\Lambda(s)\).

For prime exponents,

\[
\omega(n)=\#\{p:p\mid n\},
\qquad
\Omega(n)=\sum_p v_p(n).
\]

For a function \(f\) on the logarithmic scale line,

\[
\widetilde f(u)=\overline{f(-u)},
\qquad
g=f*\widetilde f,
\qquad
F(z)=\int_{\mathbb R}f(u)e^{izu}\,du.
\]

Then

\[
\widehat g(z)=F(z)\overline{F(\overline z)},
\]

which becomes \(|F(t)|^2\) only when \(t\in\mathbb R\).

---

# Triangulation I — One Hermitian form, one universal sign

## I.1 The exact explicit formula

For an even sufficiently regular test function \(g\) and

\[
h(r)=\int_{\mathbb R}g(u)e^{iru}\,du,
\]

one standard Guinand–Weil normalization is

\[
\boxed{
\begin{aligned}
\sum_\rho h(\lambda_\rho)
={}&h(i/2)+h(-i/2)\\
&+\frac1{2\pi}\int_{\mathbb R}h(r)
\left[
\Re\psi\!\left(\frac14+\frac{ir}{2}\right)-\log\pi
\right]dr\\
&-2\sum_{n\ge2}\frac{\Lambda_{\mathrm{vM}}(n)}{\sqrt n}\,g(\log n).
\end{aligned}
}
\tag{I.1}
\]

The three pieces on the right are:

- the pole classes at \(s=0,1\);
- the Archimedean local factor \(\Gamma_{\mathbb R}\);
- the finite prime-power orbits.

The critical precision point is the left-side argument:

\[
\lambda_\rho
=\gamma-i\left(\beta-\frac12\right),
\]

not merely \(\gamma\) unless RH has already been assumed.

Set \(g=f*\widetilde f\).  Then

\[
h(z)=F(z)\overline{F(\overline z)}.
\]

This makes the explicit formula a Hermitian form \(Q_W(f)\).

## I.2 On-line atom versus off-line saddle

Assume a real-even finite test basis \(F_1,\dots,F_d\).  For one centered zero

\[
\lambda=\gamma-i\delta,
\qquad
\delta=\beta-\frac12,
\]

write the evaluation vector

\[
v=(F_1(\lambda),\ldots,F_d(\lambda))=a+ib,
\qquad a,b\in\mathbb R^d.
\]

The full functional-equation/conjugation quartet contributes, up to the conventional multiplicity normalization,

\[
\boxed{
4(aa^{\mathsf T}-bb^{\mathsf T}).
}
\tag{I.2}
\]

On the line, \(\delta=0\), hence \(b=0\), and the block is positive rank one.

Off the line, the block has one positive and one negative direction whenever \(a,b\) are independent.

### Proposition I.1 — quadratic onset of negativity

For small \(\delta\),

\[
a=F(\gamma)+O(\delta^2),
\qquad
b=-\delta F'(\gamma)+O(\delta^3).
\]

Therefore

\[
4(aa^{\mathsf T}-bb^{\mathsf T})
=
4F(\gamma)F(\gamma)^{\mathsf T}
-4\delta^2F'(\gamma)F'(\gamma)^{\mathsf T}
+O(\delta^2\text{ mixed}+\delta^4).
\]

If a coefficient vector \(c\) satisfies

\[
c\cdot F(\gamma)=0,
\qquad
c\cdot F'(\gamma)\ne0,
\]

then

\[
\boxed{
Q_{\mathrm{quartet}}(c)
=-4\delta^2|c\cdot F'(\gamma)|^2+O(\delta^4)<0
}
\]

for sufficiently small nonzero \(\delta\).

This proves the local design principle for an off-line detector:

\[
\boxed{
\text{annihilate the value direction; retain the derivative direction.}
}
\]

The uploaded finite Gram experiments observed exactly this \(\delta^2\) onset.

## I.3 What RH really asks

Weil's criterion can be summarized as

\[
\boxed{
\mathrm{RH}
\iff
Q_W(f)\ge0
\quad\forall f\text{ in the admissible test class}.
}
\tag{I.3}
\]

This is not “one numerical sign.”  It is one form with infinitely many test directions.

The equivalence

\[
Q_W(f)=\|Bf\|^2
\]

is not an extra trick.  For any closed self-adjoint form,

\[
Q\ge0
\iff
A=B^*B
\]

by the spectral theorem.  Therefore “find \(B\)” is useful only if \(B\) arises from an independently constructed geometry or dynamics.  Defining \(B=A^{1/2}\) after assuming positivity is circular.

## I.4 The three walls

This triangulation fixes the three dominant walls:

1. **Identity versus inequality.**  Functional equations and trace formulas give equations; RH is a universal sign.
2. **Independent positivity.**  Over finite fields, Hodge/Rosati geometry supplies the sign before the zeta zeros are analyzed.  Over \(\mathbb Z\), that source is missing.
3. **Selection.**  Even if global positivity were granted, finite-window minimizers live in a large near-radical.  One must prove why the \(\Xi\)-direction is selected.

These walls are logically distinct.  A geometric RH proof could solve Wall 2 without proving a particular prolate minimizer limit; the Connes minimizer strategy must solve Wall 3 in addition to carrying RH-level sign information.

---

# Triangulation II — Prime powersets, multiset fibers, and ghost spectra

## II.1 Exact support decomposition

Every positive integer has a unique finite prime-exponent vector

\[
n=\prod_p p^{e_p},
\qquad e_p\in\mathbb N_0.
\]

Its exact support is

\[
S(n)=\{p:e_p>0\}.
\]

Partitioning all exponent vectors by exact support gives

\[
\boxed{
\zeta(s)
=
\sum_{S\subset_{\mathrm{fin}}\mathbb P}
\prod_{p\in S}
\frac{p^{-s}}{1-p^{-s}},
\qquad \Re s>1.
}
\tag{II.1}
\]

The powerset indexes the support faces; the factors

\[
\frac{p^{-s}}{1-p^{-s}}
=p^{-s}+p^{-2s}+\cdots
\]

fill each support face with every positive multiplicity.

Equivalently,

\[
\mathbb N_0^{(\mathbb P)}
=
\bigsqcup_{S\subset_{\mathrm{fin}}\mathbb P}
\mathbb N_{>0}^{S}.
\]

The squarefree radical

\[
\operatorname{rad}(n)=\prod_{p\mid n}p
\]

is the base point in the Boolean support lattice, and the remaining exponent vector is the multiplicity fiber.

## II.2 The two-parameter occupation deformation

Introduce

\[
\boxed{
Z_{a,b}(s)
=
\prod_p
\left(
1+a\frac{p^{-s}}{1-bp^{-s}}
\right).
}
\tag{II.2}
\]

Coefficientwise,

\[
\boxed{
Z_{a,b}(s)
=
\sum_{n\ge1}
 a^{\omega(n)}b^{\Omega(n)-\omega(n)}n^{-s}.
}
\tag{II.3}
\]

Interpretation:

- \(a\) weights the first occupation of a prime, i.e. support selection;
- \(b\) weights every extra copy beyond the first.

The physical point is

\[
Z_{1,1}(s)=\zeta(s).
\]

Other specializations are

\[
Z_{1,0}(s)=\frac{\zeta(s)}{\zeta(2s)}
\]

for squarefree integers, and

\[
Z_{-1,0}(s)=\frac1{\zeta(s)}
\]

for the signed support/Möbius sector.

## II.3 Witt–necklace decomposition

Write \(x=p^{-s}\).  Then

\[
\log\frac{1+(a-b)x}{1-bx}
=
\sum_{m\ge1}\frac{c_m(a,b)}m x^m,
\]

with

\[
\boxed{
c_m(a,b)=b^m+(-1)^{m+1}(a-b)^m.}
\tag{II.4}
\]

Let

\[
P(s)=\sum_p p^{-s}
\]

be the prime zeta function.  Then

\[
\log Z_{a,b}(s)
=
\sum_{m\ge1}\frac{c_m(a,b)}mP(ms).
\]

Möbius inversion

\[
P(u)=\sum_{k\ge1}\frac{\mu(k)}k\log\zeta(ku)
\]

gives

\[
\boxed{
\log Z_{a,b}(s)
=
\sum_{n\ge1}d_n(a,b)\log\zeta(ns),
}
\tag{II.5}
\]

where

\[
\boxed{
d_n(a,b)
=
\frac1n\sum_{m\mid n}
\mu(n/m)
\left[b^m+(-1)^{m+1}(a-b)^m\right].
}
\tag{II.6}
\]

Formally,

\[
Z_{a,b}(s)=\prod_{n\ge1}\zeta(ns)^{d_n(a,b)}.
\]

A generic occupation deformation therefore produces zeros and poles at

\[
s=\frac{\rho}{n},
\]

with scaled reflection centers

\[
\Re s=\frac1{2n}.
\]

These are the **ghost critical lines**.

## II.4 Single-center rigidity

### Theorem II.1 — unrestricted multiplicity is the unique positive single-center law

Within the two-parameter family, if

\[
d_n(a,b)=0\qquad(n\ge2),
\]

then either:

- \(a=0\), giving the trivial local factor \(1\);
- \((a,b)=(1,1)\), giving \(\zeta\);
- \((a,b)=(-1,0)\), giving \(1/\zeta\).

Among nonnegative nontrivial occupation weights, only

\[
\boxed{(a,b)=(1,1)}
\]

survives.

#### Proof

The first two nontrivial Witt coordinates are

\[
d_2=-\frac a2(a-2b+1),
\]

\[
d_3=\frac a3(a^2-3ab+3b^2-1).
\]

If \(a=0\), the local numerator and denominator cancel.  Otherwise \(d_2=0\) implies

\[
b=\frac{a+1}{2}.
\]

Substitution into \(d_3=0\) gives

\[
a(a-1)(a+1)=0.
\]

The two nontrivial cases are \(a=1,b=1\) and \(a=-1,b=0\), and direct substitution shows all higher \(d_n\) vanish. ∎

There is a broader formal version.  If a local occupation law \(F(x)\in1+x\mathbb C[[x]]\) has

\[
\prod_pF(p^{-s})=\zeta(s)^c
\]

with no scaled zeta factors, then

\[
\boxed{F(x)=(1-x)^{-c}.}
\]

If the coefficients are nonnegative integers and the one-particle coefficient is \(1\), then \(c=1\) and

\[
F(x)=\frac1{1-x}.
\]

This makes “maximal coherent multiset completion” mathematically rigid rather than metaphorical.

## II.5 Tangent directions at the physical point

At \((a,b)=(1,1)\),

\[
\boxed{
\left.\partial_a d_n\right|_{1,1}
=\frac{\mu(n)}n,
}
\tag{II.7}
\]

while

\[
\boxed{
\left.\partial_b d_1\right|_{1,1}=0,
\qquad
\left.\partial_b d_n\right|_{1,1}
=\frac{\varphi(n)-\mu(n)}n
\quad(n\ge2).
}
\tag{II.8}
\]

The support tangent therefore creates a Möbius-weighted scaled-zero tower; the repetition tangent creates a totient-minus-Möbius tower.

At the logarithmic derivative level,

\[
P_{a,b}(s)=-\partial_s\log Z_{a,b}(s)
\]

satisfies

\[
\boxed{
\left.\partial_aP_{a,b}(s)\right|_{1,1}
=
\sum_p(\log p)p^{-s},
}
\tag{II.9}
\]

which isolates primitive primes, and

\[
\boxed{
\left.\partial_bP_{a,b}(s)\right|_{1,1}
=
\sum_p\sum_{m\ge2}m(\log p)p^{-ms},
}
\tag{II.10}
\]

which isolates repetitions.

This gives natural perturbation coordinates for any finite Weil or transfer operator.

---

# Triangulation III — q-ary exponent clocks and canonical Fredholm determinants

## III.1 The multiset as an infinite stack of digit powersets

Every \(k\in\mathbb N_0\) has a unique base-\(q\) expansion

\[
k=\sum_{j\ge0}d_jq^j,
\qquad d_j\in\{0,1,\dots,q-1\}.
\]

Therefore, for \(|x|<1\),

\[
\boxed{
\frac1{1-x}
=
\prod_{j\ge0}
\left(1+x^{q^j}+\cdots+x^{(q-1)q^j}\right).
}
\tag{III.1}
\]

At finite depth,

\[
\prod_{j=0}^{J-1}
\left(1+x^{q^j}+\cdots+x^{(q-1)q^j}\right)
=
\frac{1-x^{q^J}}{1-x}.
\]

Putting \(x=p^{-s}\) and multiplying over primes gives

\[
\boxed{
\frac{\zeta(s)}{\zeta(q^Js)}
=
\prod_{j=0}^{J-1}
\frac{\zeta(q^js)}{\zeta(q^{j+1}s)}.
}
\tag{III.2}
\]

For \(\Re s>1\),

\[
\boxed{
\zeta(s)
=
\prod_{j\ge0}
\frac{\zeta(q^js)}{\zeta(q^{j+1}s)}.
}
\tag{III.3}
\]

For \(q=2\), arbitrary bosonic prime occupation becomes an infinite register of binary support bits.

## III.2 Cyclic clock determinant

Let \(C_q\) be the cyclic shift on \(\mathbb C^q\), and let \(C_q^\circ\) denote its restriction to the mean-zero subspace, whose eigenvalues are

\[
\omega_q,\omega_q^2,\dots,\omega_q^{q-1},
\qquad
\omega_q=e^{2\pi i/q}.
\]

### Theorem III.1

\[
\boxed{
\det(I-xC_q^\circ)
=1+x+\cdots+x^{q-1}.
}
\tag{III.4}
\]

#### Proof

\[
\det(I-xC_q^\circ)
=
\prod_{r=1}^{q-1}(1-\omega_q^r x)
=
\frac{1-x^q}{1-x}.
\]

∎

This gives a canonical finite clock for each prime and exponent scale.

## III.3 Trace-class prime-clock operator

For \(\Re s>1\), define on

\[
\mathcal H_{q,j}=\bigoplus_{p\in\mathbb P}\mathbb C^{q-1}
\]

the block-diagonal operator

\[
\boxed{
T_{q,j}(s)
=
\bigoplus_p p^{-q^js}C_q^\circ.
}
\tag{III.5}
\]

It is trace class because

\[
\sum_p\|p^{-q^js}C_q^\circ\|_1
=(q-1)\sum_p p^{-q^j\Re s}<\infty.
\]

### Theorem III.2 — exact Fredholm layer

\[
\boxed{
\det(I-T_{q,j}(s))
=
\frac{\zeta(q^js)}{\zeta(q^{j+1}s)}.
}
\tag{III.6}
\]

#### Proof

Fredholm determinants multiply over trace-class direct sums:

\[
\begin{aligned}
\det(I-T_{q,j}(s))
&=
\prod_p\det(I-p^{-q^js}C_q^\circ)\\
&=
\prod_p\frac{1-p^{-q^{j+1}s}}{1-p^{-q^js}}.
\end{aligned}
\]

∎

Now take the direct sum over all digit scales:

\[
\mathbb T_q(s)=\bigoplus_{j\ge0}T_{q,j}(s).
\]

The total trace norm converges for \(\Re s>1\), and

\[
\boxed{
\det(I-\mathbb T_q(s))=\zeta(s).
}
\tag{III.7}
\]

This is a canonical operator realization of the q-ary prime-multiset decomposition.

**Boundary:** \(\mathbb T_q(s)\) depends on the spectral parameter \(s\), is not a self-adjoint Hilbert–Pólya operator, and is defined initially only in the Euler-product half-plane.  It is nevertheless a genuine trace-class prime-clock determinant, not a fitted orbit model.

## III.4 Carry cancellation

The clock moments are

\[
\operatorname{tr}((C_q^\circ)^m)
=
q\mathbf1_{q\mid m}-1.
\]

Hence

\[
-\operatorname{tr}((C_q^\circ)^m)
=
1-q\mathbf1_{q\mid m}.
\]

For a prime-power repetition number \(r\), let \(v=v_q(r)\).  Contributions from the scales \(j=0,\dots,v\) satisfy

\[
\boxed{
\sum_{j=0}^{v}
\frac{1-q\mathbf1_{j<v}}{r/q^j}
=
\frac1r.
}
\tag{III.8}
\]

This is the exact carry law: every q-fold repetition at scale \(j\) is removed and reappears as one occupation at scale \(j+1\).  Summing over all digit scales reproduces

\[
\log\zeta(s)
=
\sum_p\sum_{r\ge1}\frac{p^{-rs}}r.
\]

## III.5 Support infinity versus multiplicity infinity

For finite prime support \(P\) and exponent cap \(K\),

\[
Z_{P,K}(s)
=
\prod_{p\in P}\frac{1-p^{-Ks}}{1-p^{-s}}.
\]

Every zero of this finite product lies on \(\Re s=0\); it is a local root-of-unity zero.  No finite \(P,K\) object contains a nontrivial Riemann zero.

If all primes are admitted but multiplicity remains capped,

\[
Z_K(s)=\frac{\zeta(s)}{\zeta(Ks)}.
\]

Now the physical zero divisor of \(\zeta(s)\) appears, together with a scaled ghost divisor at \(s=\rho/K\).

If multiplicities are unlimited but prime support stays finite, the product has no zeros.

Therefore:

\[
\boxed{
\text{all-prime support creates the physical zero divisor;}
}
\]

\[
\boxed{
\text{multiplicity infinity cancels the scaled ghosts.}
}
\]

## III.6 Rare coefficient tail, dense spectral tail

The density of \(K\)-free integers is

\[
\frac1{\zeta(K)}=1-2^{-K}+O(3^{-K}).
\]

Thus the omitted coefficient density is exponentially tiny.  Yet the residual denominator \(\zeta(Ks)\) contains roughly

\[
N(KT)\sim\frac{KT}{2\pi}\log\frac{KT}{2\pi}
\]

scaled zero modes below height \(T\).

This is a sharp warning for all finite approximations:

\[
\boxed{
\text{a tiny coefficient tail can carry a huge spectral divisor.}
}
\]

An elementary weaker theorem is the standard \(K\)-free count

\[
\boxed{
Q_K(x)=\frac{x}{\zeta(K)}+O_K(x^{1/K}),
}
\]

obtained from

\[
\mathbf1_{K\text{-free}}(n)=\sum_{d^K\mid n}\mu(d).
\]

The RH-scale error would be \(x^{1/(2K)+\varepsilon}\), exactly matching the scaled ghost center \(1/(2K)\).

---

# Triangulation IV — Gamma as the Archimedean q-clock and ultraviolet boundary

## IV.1 Why Gamma appears

The Gaussian local zeta integral is

\[
\int_{\mathbb R^\times}e^{-\pi x^2}|x|^s\,d^\times x
=
\pi^{-s/2}\Gamma(s/2)
=
\Gamma_{\mathbb R}(s).
\]

Equivalently,

\[
\Gamma_{\mathbb R}(s)\zeta(s)
=
\int_0^\infty
\left(\sum_{n\ge1}e^{-\pi n^2t}\right)
 t^{s/2}\frac{dt}{t}.
\]

The prime multiset produces every integer \(n\); the Gaussian assigns one nonlinear global weight \(e^{-\pi n^2t}\) to the completed integer value; Mellin integration then averages over every continuous scale.  Gamma is the continuous-scale converter, not an extra family of prime copies.

## IV.2 Zeta-regularized shifted number determinants

Let

\[
Ne_n=ne_n,
\qquad n=0,1,2,\dots
\]

on \(\ell^2(\mathbb N_0)\).  The spectral zeta function of \(N+a\) is the Hurwitz zeta \(\zeta_H(z,a)\).  Since

\[
\zeta_H'(0,a)=\log\Gamma(a)-\frac12\log(2\pi),
\]

we have the exact zeta determinant

\[
\boxed{
\det_\zeta(N+a)
=\frac{\sqrt{2\pi}}{\Gamma(a)}.
}
\tag{IV.1}
\]

This gives an operator-theoretic home for the Gamma factors.

## IV.3 Archimedean q-clock determinant

Gauss's multiplication formula yields

\[
\Gamma(qz)
=(2\pi)^{(1-q)/2}q^{qz-1/2}
\prod_{r=0}^{q-1}\Gamma\!\left(z+\frac rq\right).
\]

Set \(z=s/2\).  Then

\[
\boxed{
\frac{\Gamma_{\mathbb R}(s)}{\Gamma_{\mathbb R}(qs)}
=
\pi^{(q-1)s/2}q^{1/2-qs/2}
\prod_{r=1}^{q-1}
\det_\zeta\!\left(N+\frac s2+\frac rq\right).
}
\tag{IV.2}\]

The \(q-1\) nontrivial finite clock phases \(r/q\) have become \(q-1\) fractional Archimedean shifts.

This is the exact local dictionary:

| finite prime layer | Archimedean layer |
|---|---|
| cyclic eigenphase \(r/q\) | shift \(s/2+r/q\) |
| ordinary Fredholm determinant | zeta-regularized determinant |
| exponent carry | Gauss multiplication |
| discrete scale | continuous scale |

## IV.4 Completed q-layer

Define

\[
\boxed{
\mathcal D_q(s)
=
\frac{\Lambda(s)}{\Lambda(qs)}.
}
\tag{IV.3}
\]

Combining Theorems III.2 and IV.2 gives

\[
\boxed{
\mathcal D_q(s)
=
\left[
\pi^{(q-1)s/2}q^{1/2-qs/2}
\prod_{r=1}^{q-1}
\det_\zeta\!\left(N+\frac s2+\frac rq\right)
\right]
\det(I-T_{q,0}(s)).
}
\tag{IV.4}
\]

At scale \(j\), replace \(s\) by \(q^js\).

This produces an exact completed prime-clock layer: finite primes contribute an ordinary trace-class determinant, while infinity contributes regularized fractional-shift determinants.

## IV.5 Scale cocycle and connection

For positive scale factors \(q,r\),

\[
\boxed{
\mathcal D_{qr}(s)
=
\mathcal D_q(s)\mathcal D_r(qs)
=
\mathcal D_r(s)\mathcal D_q(rs).
}
\tag{IV.5}
\]

In continuous form, let

\[
C_\tau(s)=\frac{\Lambda(s)}{\Lambda(e^\tau s)}.
\]

Then

\[
C_{\tau+\sigma}(s)
=C_\tau(s)C_\sigma(e^\tau s).
\]

Define a transport semigroup

\[
(U_\tau f)(s)=C_\tau(s)f(e^\tau s).
\]

It is conjugate to ordinary dilation:

\[
U_\tau=M_\Lambda D_\tau M_\Lambda^{-1}.
\]

Its infinitesimal generator is

\[
\boxed{
Af(s)
=s f'(s)-s\frac{\Lambda'(s)}{\Lambda(s)}f(s).
}
\tag{IV.6}
\]

Thus the completed logarithmic derivative is literally a **connection term for scale transport**.  Its poles are the spectral defects—zeros and poles of the completed zeta object.

This is zero-forward and structurally useful, but it is not a self-adjoint operator on a positive Hilbert space.  Establishing the correct metric and domain is precisely where RH-level content can enter.

## IV.6 Scaling and reflection fail to commute

Let

\[
D_q(s)=qs,
\qquad
R(s)=1-s.
\]

Then the affine group commutator is

\[
\boxed{
D_q R D_q^{-1}R(s)=s+q-1.
}
\tag{IV.7}
\]

This exact translation defect explains why finite multiplicity scaling and functional reflection do not share a center:

- dilation is centered at \(0\);
- the zeta functional equation is centered at \(1/2\).

A finite scale layer therefore carries a two-center obstruction.  Only the complete tower can telescope the internal centers away.

## IV.7 Ultraviolet boundary localization theorem

Define the finite completed tower

\[
P_{q,J}(s)
=
\prod_{j=0}^{J-1}\mathcal D_q(q^js)
=
\frac{\Lambda(s)}{\Lambda(q^Js)}.
\]

### Theorem IV.1

\[
\boxed{
\frac{P_{q,J}(1-s)}{P_{q,J}(s)}
=
\frac{\Lambda(q^Js)}{\Lambda(q^J(1-s))}
=
\frac{\Lambda(q^Js)}
{\Lambda(q^Js-(q^J-1))}.
}
\tag{IV.8}
\]

#### Proof

Use \(\Lambda(1-s)=\Lambda(s)\) in the first quotient.  Apply the functional equation once more to the denominator:

\[
\Lambda(q^J(1-s))
=
\Lambda(1-q^J(1-s))
=
\Lambda(q^Js-(q^J-1)).
\]

∎

Every interior reflection defect has telescoped to a single ultraviolet boundary ratio.

On the critical line \(s=1/2+it\),

\[
q^J(1-s)=\overline{q^Js},
\]

so

\[
\boxed{
\left|
\frac{P_{q,J}(1-s)}{P_{q,J}(s)}
\right|=1.
}
\tag{IV.9}
\]

The remaining defect is a pure phase:

\[
\frac{\Lambda(q^Js)}{\overline{\Lambda(q^Js)}}
=e^{2i\arg\Lambda(q^Js)}.
\]

As \(J\to\infty\), \(\zeta(q^Js)\to1\) rapidly in the right half-plane, while Stirling makes the Gamma contribution enormous.  Therefore the ultraviolet polarizer is asymptotically Archimedean.

This theorem formalizes the intuition that the Gamma term is where the infinite tower's unresolved phase accumulates.

## IV.8 The regularization warning

The determinant in IV.1 is zeta-regularized.  Zeta regularization preserves analytic identities but not positivity:

\[
1+2+3+\cdots\rightsquigarrow\zeta(-1)=-\frac1{12}.
\]

Therefore a regularized determinant can provide the correct completed analytic object without providing a nonnegative count.  Finite-field RH succeeds because the relevant degree is an actual cardinality/intersection number.  The Archimedean determinant gives finiteness; the missing theorem is positivity.

---
# Triangulation V — Archimedean heat geometry and an independent positive structure

## V.1 The free prime-multiset Hamiltonian

Let

\[
\mathcal F_{\mathbb P}
=
\ell^2\!\left(\mathbb N_0^{(\mathbb P)}\right)
\]

with basis \(|\mathbf k\rangle\), where \(\mathbf k=(k_p)_p\) has finite support.  Define

\[
N_p|\mathbf k\rangle=k_p|\mathbf k\rangle,
\]

\[
\boxed{
H_\times=\sum_p(\log p)N_p.
}
\tag{V.1}
\]

Then

\[
H_\times|\mathbf k\rangle
=\log n(\mathbf k)|\mathbf k\rangle,
\qquad
n(\mathbf k)=\prod_pp^{k_p},
\]

and

\[
\operatorname{Tr}e^{-sH_\times}=\zeta(s)
\]

for \(\Re s>1\).

At this level the prime modes are independent.

## V.2 Gaussian completion creates all-body interaction

Define

\[
\widehat n=e^{H_\times}
\]

and

\[
G_t=e^{-\pi t\widehat n^{\,2}}.
\]

The state weight is

\[
W_t(\mathbf k)
=
\exp\!\left[-\pi t\left(\prod_pp^{k_p}\right)^2\right].
\]

This does not factorize over primes.

### Theorem V.1 — strict log-submodularity of prime occupation

For distinct primes \(p,q\), let \(\Delta_p\) add one copy of \(p\).  Then

\[
\boxed{
\Delta_p\Delta_q\log W_t(\mathbf k)
=-\pi t\,n(\mathbf k)^2(p^2-1)(q^2-1)<0.
}
\tag{V.2}
\]

#### Proof

Adding \(p\) multiplies \(n\) by \(p\).  Hence

\[
\begin{aligned}
\Delta_p\Delta_q\log W_t
&=-\pi t n^2(p^2q^2-p^2-q^2+1)\\
&=-\pi t n^2(p^2-1)(q^2-1).
\end{aligned}
\]

∎

Equivalently,

\[
\frac{W_t(\mathbf k+e_p+e_q)W_t(\mathbf k)}
{W_t(\mathbf k+e_p)W_t(\mathbf k+e_q)}<1.
\]

This is a genuine repulsive all-body correlation created by the Archimedean Gaussian.  The free Euler gas is factorized; the completed theta ensemble is not.

## V.3 Positive Fisher/covariance geometry

Introduce occupation sources \(u_p\):

\[
K_t(\mathbf u)
=
\sum_{\mathbf k}
\exp\left(
-\pi t n(\mathbf k)^2+
\sum_pu_pk_p
\right).
\]

Then

\[
\boxed{
\frac{\partial^2}{\partial u_p\partial u_q}
\log K_t(\mathbf u)
=
\operatorname{Cov}_{t,\mathbf u}(N_p,N_q).
}
\tag{V.3}
\]

For every finite coefficient vector \(c\),

\[
\sum_{p,q}\overline{c_p}C_t(p,q)c_q
=
\operatorname{Var}_t\left(\sum_pc_pN_p\right)
\ge0.
\]

Thus

\[
\boxed{C_t\succeq0.}
\]

This positivity is independent of any statement about zeta zeros.

A calibrated computation at \(t=0.01\) for \(p=2,3,5\) gave

\[
C_t\approx
\begin{pmatrix}
0.683191&-0.100822&-0.061620\\
-0.100822&0.235047&-0.030557\\
-0.061620&-0.030557&0.098767
\end{pmatrix},
\]

with eigenvalues

\[
0.080354,
\quad0.227048,
\quad0.709603.
\]

The full covariance form is positive although the pairwise correlations are negative in this sample.  The latter is numerical evidence, not a general negative-association theorem.

## V.4 A positive heat Gram matrix

For \(\alpha>0\), define

\[
v_n(t)=e^{-\pi n^2t}t^{(\alpha-1)/2}.
\]

Then

\[
\boxed{
G_\alpha(n,m)
=
\langle v_n,v_m\rangle_{L^2(0,\infty)}
=
\frac{\Gamma(\alpha)}
{\pi^\alpha(n^2+m^2)^\alpha}.
}
\tag{V.4}
\]

Every finite matrix \([G_\alpha(n,m)]\) is positive definite.  For \(\alpha>1/2\),

\[
\boxed{
\operatorname{Tr}G_\alpha
=
\frac{\Gamma(\alpha)}{(2\pi)^\alpha}\zeta(2\alpha).
}
\tag{V.5}
\]

This supplies an honest Hilbert geometry whose atoms are integers/prime multisets and whose kernel is built from the same Gaussian that generates the Archimedean factor.

## V.5 The prospective bridge

The natural moonshot is to derive the Weil form from this independently positive heat geometry:

\[
\boxed{
Q_W(f)
\stackrel{?}{=}
\int_0^\infty
\|B_tf\|_{\mathcal H_t}^2\,d\nu(t),
\qquad d\nu(t)\ge0.
}
\tag{V.6}
\]

Any such identity would prove RH if:

1. \(B_t\) is constructed without using the zeros;
2. the integral reproduces the full pole, Gamma, and prime terms;
3. domains and regularization are controlled;
4. the representation is complete enough to detect every off-line block.

### Roadblock

Mellin transformation on the critical line uses the oscillatory phase

\[
t^{ir/2}.
\]

An oscillatory transform of a positive kernel need not remain positive.  Indeed, a positive measure can have a Fourier transform with nonreal zeros; for example,

\[
3+2\cos z
\]

is the transform of \(\delta_{-1}+3\delta_0+\delta_1\), yet its zeros are nonreal.

Therefore pointwise positivity of the heat kernel is not enough.  The bridge must preserve a stronger structure: total positivity, a Herglotz kernel, a self-adjoint determinant, or a geometric Hodge polarization.

---

# Triangulation VI — The zero resolvent, safe-region reflection, and Hausdorff moments

## VI.1 The zero-forward resolvent

Define

\[
\boxed{
R_\Xi(z)
=-\frac{\Xi'(z)}{2z\Xi(z)}.
}
\tag{VI.1}
\]

Using the paired canonical product of the even entire function \(\Xi\),

\[
\boxed{
R_\Xi(z)
=
\sum_{\lambda\in\Lambda_+}
\frac1{\lambda^2-z^2}.
}
\tag{VI.2}
\]

Each nontrivial zero pair is now one additive resolvent atom.  This is the analytic form in which the zeros are most directly exposed.

Set

\[
F_\Xi(w)=R_\Xi(\sqrt w).
\]

Then

\[
F_\Xi(w)=\sum_\lambda\frac1{\lambda^2-w}.
\]

## VI.2 Stieltjes characterization

### Theorem VI.1

\[
\boxed{
\mathrm{RH}
\iff
F_\Xi(w)
\text{ is the Stieltjes transform of a positive atomic measure on }[0,\infty).
}
\tag{VI.3}
\]

#### Proof

If RH holds, \(\lambda=\gamma\in\mathbb R\), and

\[
F_\Xi(w)
=
\int_0^\infty\frac{d\mu(x)}{x-w},
\qquad
\mu=\sum_{\gamma>0}m_\gamma\delta_{\gamma^2}.
\]

Conversely, a meromorphic Stieltjes transform has poles only on its real nonnegative support.  The poles of \(F_\Xi\) are \(\lambda^2\).  Hence every \(\lambda^2\ge0\), so every \(\lambda\) is real. ∎

For \(\Im w>0\), the Herglotz sign is

\[
\Im F_\Xi(w)>0.
\]

The Pick kernel

\[
\boxed{
K_F(w,z)
=
\frac{F_\Xi(w)-\overline{F_\Xi(z)}}{w-\overline z}
}
\tag{VI.4}
\]

must be positive semidefinite on every finite set.

An off-line pair creates a negative Pick direction.  In a calibrated toy displacement, moving one zero pair by \(\delta=0.1\) changed a previously positive least Pick eigenvalue into a negative one.  This is a detector calibration, not a statement about the actual zeta zeros.

## VI.3 Reflection ladder: negative integers without illegal Euler products

Let \(n\ge1\) and put

\[
z=i\left(n+\frac12\right).
\]

Then \(1/2+iz=-n\).

### Theorem VI.2 — reflected zero-resolvent ladder

\[
\boxed{
R_\Xi\!\left(i(n+\tfrac12)\right)
=
\frac1{2n+1}\frac{\xi'(n+1)}{\xi(n+1)}.
}
\tag{VI.5}
\]

#### Proof

Use \(\Xi'(z)=i\xi'(1/2+iz)\) and differentiate \(\xi(s)=\xi(1-s)\), obtaining

\[
\xi'(-n)=-\xi'(n+1).
\]

Substitution gives the formula. ∎

The right side lies in the absolutely convergent Euler-product region.  Explicitly,

\[
\boxed{
\begin{aligned}
R_\Xi\!\left(i(n+\tfrac12)\right)
=
\frac1{2n+1}
\Bigg[
&\frac1{n+1}+\frac1n-\frac12\log\pi\\
&+\frac12\psi\!\left(\frac{n+1}{2}\right)
-\sum_p\frac{\log p}{p^{n+1}-1}
\Bigg].
\end{aligned}
}
\tag{VI.6}
\]

For \(n=1\),

\[
R_\Xi(3i/2)
=0.0230220771766668920750553\ldots
\]

and under RH this equals

\[
\sum_{\gamma>0}\frac1{\gamma^2+9/4}.
\]

This is the rigorous compiler for the \(s=-1\) intuition:

\[
\boxed{
\text{formal negative-integer arithmetic}
\xrightarrow{\text{completion/reflection}}
\text{convergent prime arithmetic at a positive integer}.
}
\]

## VI.4 A safe-region Hausdorff moment criterion

Fix

\[
a>\frac12.
\]

Define

\[
\boxed{
\Phi_a(z)
=a^2R_\Xi\!\left(ia\sqrt{1-z}\right).
}
\tag{VI.7}
\]

Using the functional equation,

\[
\boxed{
\Phi_a(z)
=-\frac{d}{dz}
\log\xi\!\left(\frac12+a\sqrt{1-z}\right).
}
\tag{VI.8}
\]

Near \(z=0\), the argument satisfies

\[
\frac12+a>1,
\]

so every Taylor coefficient of \(\Phi_a\) can be computed from absolutely convergent prime sums and polygamma values.

On the zero side,

\[
\Phi_a(z)
=
\sum_\lambda
\frac{a^2}{\lambda^2+a^2-a^2z}.
\]

Let

\[
y_\lambda=\frac{a^2}{a^2+\lambda^2}.
\]

Then

\[
\boxed{
\Phi_a(z)
=
\sum_{n\ge0}u_n^{(a)}z^n,
\qquad
u_n^{(a)}=
\sum_\lambda y_\lambda^{n+1}.
}
\tag{VI.9}
\]

### Theorem VI.3 — reflected Hausdorff criterion

For any fixed \(a>1/2\),

\[
\boxed{
\mathrm{RH}
\iff
\bigl(u_n^{(a)}\bigr)_{n\ge0}
\text{ is a Hausdorff moment sequence}.
}
\tag{VI.10}
\]

Equivalently,

\[
\boxed{
(-1)^r\Delta^r u_n^{(a)}\ge0
\qquad\forall n,r\ge0.
}
\tag{VI.11}
\]

#### Proof

Under RH, \(0<y_\gamma<1\) and

\[
u_n^{(a)}=
\int_0^1y^n\,d\nu_a(y),
\qquad
\nu_a=
\sum_{\gamma>0}y_\gamma\delta_{y_\gamma}.
\]

Hence

\[
(-1)^r\Delta^r u_n^{(a)}
=
\int_0^1y^n(1-y)^r\,d\nu_a(y)\ge0.
\]

Conversely, the Hausdorff theorem produces a positive measure on \([0,1]\), so the generating function can have singularities only at \(z\in[1,\infty)\).  But its poles are

\[
z_\lambda=1+\lambda^2/a^2.
\]

Thus every \(\lambda^2\ge0\), giving RH. ∎

For the particularly convenient choice \(a=3/2\), every derivative is centered at \(s=2\).  A calibrated extraction gave

\[
\begin{aligned}
u_0&=0.051799673647500507168874439446905,\\
u_1&=0.000184952068736225532452250361614,\\
u_2&=1.592344494432499180359863883\times10^{-6},\\
u_3&=1.627165970967866220348358569\times10^{-8},\\
u_4&=1.753534073992679716968494965\times10^{-10}.
\end{aligned}
\]

The finite-difference inequalities were numerically positive through the tested order, with minimum tested margin approximately

\[
2.94\times10^{-20}.
\]

This is calibration only.  Finite positivity does not imply the infinite Hausdorff property.

## VI.5 Why this criterion may still be useful

Most RH criteria force analytic continuation or zero data into the computation.  Here the entire coefficient sequence can be generated at the safe point \(s=1/2+a>1\).

The proof target is therefore a concrete family of inequalities on convergent prime sums:

\[
(-1)^r\Delta^r
\left[
[z^n]
\left(-\frac d{dz}
\log\xi\!\left(\frac12+a\sqrt{1-z}\right)
\right)
\right]
\ge0.
\]

A real advance would derive these inequalities from an independently positive heat, transfer, or geometric structure.  Simply recognizing that they are equivalent to RH is a mirror.

---

# Triangulation VII — Finite Weil compressions, inertia, and weaker proofs

## VII.1 Why the Weil form can count proportions

The zero-side finite compression is atom-resolved:

- each simple on-line zero contributes a positive rank-one atom;
- each off-line quartet contributes a block with one positive and one negative direction.

This is different from aggregate moment/Hankel formulations, where moving one zero changes every matrix entry and gives only an all-or-nothing positivity test.

The atom resolution permits rank and inertia to give **proportional** results.

## VII.2 Current external frontier

A 2026 preprint by Alpöge and Furman reports an unconditional theorem that at least two thirds of the nontrivial zeta zeros, counted with multiplicity, are simple and lie on the critical line, with a refined constant near \(0.6725\).  The proof uses a finite compression of Weil's Hermitian form, a rank–trace inequality, and Sylvester inertia.  This is precisely the mechanism isolated in Triangulation I.

The strategic lesson is major:

\[
\boxed{
\text{finite Weil inequalities can yield genuine theorems short of RH.}
}
\]

This track is therefore more than numerical reconnaissance.

## VII.3 Moment-based positive-inertia bounds

Let \(G\) be Hermitian and \(n_+(G)\) the number of positive eigenvalues.

### Theorem VII.1 — odd/even moment hierarchy

For odd \(p\ge1\) and even \(q>p\),

\[
\boxed{
 n_+(G)
\ge
\frac{
\max(\operatorname{tr}G^p,0)^{q/(q-p)}
}{
(\operatorname{tr}G^q)^{p/(q-p)}
}.
}
\tag{VII.1}
\]

#### Proof

Let \(\lambda_1,\dots,\lambda_r>0\) be the positive eigenvalues.  Since \(p\) is odd,

\[
\sum_{j=1}^r\lambda_j^p
\ge\operatorname{tr}G^p.
\]

Since \(q\) is even,

\[
\sum_{j=1}^r\lambda_j^q
\le\operatorname{tr}G^q.
\]

The power-mean/Hölder inequality gives

\[
\left(\sum\lambda_j^p\right)^{1/p}
\le
r^{1/p-1/q}
\left(\sum\lambda_j^q\right)^{1/q}.
\]

Rearrange. ∎

Special cases are

\[
\boxed{
n_+(G)\ge
\frac{\max(\operatorname{tr}G,0)^2}
{\operatorname{tr}G^2}
}
\tag{VII.2}
\]

and

\[
\boxed{
n_+(G)\ge
\frac{\max(\operatorname{tr}G^3,0)^4}
{(\operatorname{tr}G^4)^3}.
}
\tag{VII.3}
\]

Calibrated mixed-inertia examples confirmed the bounds and showed that the fourth-moment estimate can add information not present in the first two moments.

## VII.4 The higher-moment program

The concrete research problem is finite-dimensional before it is number-theoretic:

> Given a Hermitian matrix built from positive rank-one on-line atoms and signature-\((1,1)\) off-line atoms, what is the optimal lower bound on the number of positive simple atoms from a prescribed finite set of trace moments?

A disciplined workflow is:

1. encode the atom class as a semidefinite/moment optimization problem;
2. recover the known second-moment theorem as calibration;
3. optimize using \(\operatorname{tr}G^3,\operatorname{tr}G^4\), and possibly mixed window moments;
4. rationalize the numerical certificate;
5. prove the matrix inequality exactly;
6. read backward to identify the precise prime-correlation estimate needed.

The matrix inequality and the analytic trace asymptotics should be kept separate.  A new exact inequality is useful even if the required fourth-moment asymptotic remains open; it tells the field exactly what arithmetic estimate would move the proportion.

## VII.5 A hierarchy of weaker results

This track naturally lifts several boats:

- positivity on restricted test subspaces;
- lower bounds on positive inertia;
- lower bounds on simple critical zeros;
- quantitative exclusion of many off-line pairs;
- eventually, if all moments and all windows were controlled, complete positivity.

Unlike a finite check of Li coefficients or Hankel minors, every improved uniform inertia estimate is a genuine theorem about infinitely many zeros.

### Roadblocks

- Higher moments encode higher zero correlations and increasingly hard prime correlations.
- Enlarging Fourier support beyond currently controlled ranges is a genuine analytic barrier.
- A full local spacing law does not by itself place zeros on the line; the rank–inertia argument must continue to use a form whose off-line atoms have negative signature.
- Numerical optimization must produce exact certifiable inequalities, not floating-point evidence.

---
# Triangulation VIII — Prolate–Weil selection: the live full-proof analytic wall

## VIII.1 The current strategy

The current Connes/Connes–van Suijlekom program supplies two outer pieces:

1. a real-zero theorem for Fourier transforms of suitable simple, isolated, even ground states of lower-bounded convolution operators;
2. an explicit prolate candidate \(k_\lambda\) whose transform converges to \(\Xi\) on closed critical substrips.

The missing bridge is to prove that the actual localized Weil minimizer \(\theta_{\lambda^2}\) is sufficiently close to \(k_\lambda\).

This is not the statement that the lowest eigenvalue tends to zero.  The localized operator has a growing family of tiny prolate directions.  The question is why one particular direction wins.

## VIII.2 Spectral-selection inequality

Let \(A_\lambda\) be the localized Weil operator, with bottom eigenvalue \(\mu_\lambda\), ground projection \(P_\lambda\), and spectral gap

\[
g_\lambda
=
\inf(\sigma(A_\lambda)\setminus\{\mu_\lambda\})-\mu_\lambda.
\]

Normalize the explicit prolate candidate:

\[
\kappa_\lambda=\frac{k_\lambda}{\|k_\lambda\|}.
\]

Define its excess Rayleigh energy

\[
\delta_\lambda
=
\langle A_\lambda\kappa_\lambda,\kappa_\lambda\rangle
-\mu_\lambda.
\]

### Proposition VIII.1

\[
\boxed{
\|(I-P_\lambda)\kappa_\lambda\|^2
\le
\frac{\delta_\lambda}{g_\lambda}.
}
\tag{VIII.1}
\]

If the ground state is simple and phases are aligned,

\[
\boxed{
\|\theta_{\lambda^2}-\kappa_\lambda\|
\le
\sqrt{\frac{2\delta_\lambda}{g_\lambda}}.
}
\tag{VIII.2}
\]

#### Proof

Apply the spectral theorem to \(A_\lambda-\mu_\lambda\).  It vanishes on the ground eigenspace and is at least \(g_\lambda\) on the orthogonal complement.  The second estimate follows from the geometry of normalized vectors. ∎

This is the correct diagnostic:

\[
\boxed{
\delta_\lambda/g_\lambda,
}
\]

not \(\delta_\lambda\) alone and not merely \(\lambda_2/\lambda_1\).

## VIII.3 Strip convergence requires weighted control

The logarithmic support interval grows with \(\lambda\).  For \(z=t+i\eta\), the Mellin weight grows like

\[
e^{|\eta||y|}.
\]

Therefore unweighted \(L^2\) convergence does not automatically imply locally uniform convergence in a strip.

A sufficient target is

\[
\boxed{
\lambda^a
\sqrt{\frac{\delta_\lambda}{g_\lambda}}
\longrightarrow0
\qquad
\forall a<\frac12.}
\tag{VIII.3}
\]

An equivalent Feshbach-style version uses

\[
\rho_\lambda
=\langle A_\lambda\kappa_\lambda,\kappa_\lambda\rangle,
\qquad
q_\lambda=I-|\kappa_\lambda\rangle\langle\kappa_\lambda|,
\]

\[
r_\lambda
=q_\lambda(A_\lambda-\rho_\lambda)\kappa_\lambda,
\]

and the complementary coercivity

\[
G_\lambda
=
\inf\sigma\left(q_\lambda(A_\lambda-\rho_\lambda)q_\lambda\right).
\]

The verdict-changing estimate is

\[
\boxed{
\lambda^a\frac{\|r_\lambda\|}{G_\lambda}
\longrightarrow0
\qquad
\forall a<\frac12.
}
\tag{VIII.4}
\]

This statement is zero-free: it refers only to the arithmetic operator and an explicit prolate vector.  Proving it would imply minimizer convergence, real-zero convergence, and RH.

## VIII.4 Why ordinary approximation is nowhere near enough

The prolate leakage scale is exponentially small, of schematic size

\[
\lambda^C e^{-4\pi\lambda^2}.
\]

An approximation

\[
\|h_\lambda-h\|=O(\lambda^{-2})
\]

is excellent for proving \(\widehat{k}_\lambda\to\Xi\), but

\[
\lambda^{-2}\gg e^{-4\pi\lambda^2}.
\]

It cannot resolve which vector is the ground state inside the tiny near-radical.

The required theorem is therefore a second-order comparison at the leakage scale:

\[
\boxed{
E_\lambda^*(A_\lambda-\beta_\lambda)E_\lambda
=
\alpha_\lambda L_\lambda+R_\lambda,
}
\tag{VIII.5}
\]

with

\[
\boxed{
\|R_\lambda\|
=o\!\left(
\alpha_\lambda\operatorname{gap}(L_\lambda)
\right).
}
\tag{VIII.6}
\]

Here \(L_\lambda\) is the appropriate constrained prolate leakage operator.

This is a second-variation theorem around a large Hodge/Weil radical, not merely a positivity theorem.

## VIII.5 Source-derived numerical evidence

The uploaded fixed-window experiment builds each matrix from Archimedean, pole, and finite-prime data; zeros are external calibration only.  Its reported crossings were:

- cutoff \(x=2\): one of five low zeros resolved;
- cutoff \(x=3\): three of five;
- cutoff \(x=5\): all five, with errors ranging from approximately \(10^{-10}\) to \(10^{-5}\).

The same work observed improving transform shape and growing relative isolation of the bottom eigenvector.  This is meaningful calibration of the finite architecture, not proof of the limit.

Several caveats remain load-bearing:

1. the supplied scripts depend on an external module not bundled with the upload;
2. arithmetic cutoff, support width, basis size, and precision are coupled;
3. root-location accuracy can be excellent while global transform shape remains poor;
4. the initially proposed simple \(e^{-4\pi x}\) law in the variable \(x\) was rejected by the later sweep;
5. no finite computation can establish the uniform gap-normalized asymptotic.

## VIII.6 The next exact experiment

Construct the **true finite prolate candidate**, not its Hermite limit.  At each \(\lambda\), record

\[
\mu_\lambda,
\quad
g_\lambda,
\quad
\delta_\lambda,
\quad
\|r_\lambda\|,
\quad
G_\lambda,
\quad
\lambda^a\|r_\lambda\|/G_\lambda.
\]

Decompose the residual into

\[
r_\lambda
=r_\infty+r_{\mathrm{pole}}
+r_{\mathrm{primitive}}+r_{\mathrm{repeat}}.
\]

The prime-support deformation suggests testing whether primitive primes steer the eigenline while repetitions mainly renormalize energy.

Indeed, by the prime number theorem,

\[
\boxed{
\sum_{p\le x}\frac{\log p}{\sqrt p}
\sim2\sqrt x,
}
\tag{VIII.7}
\]

whereas

\[
\boxed{
\sum_{\substack{p^m\le x\\m\ge2}}
\frac{\log p}{p^{m/2}}
=
\frac12\log x+C+o(1).
}
\tag{VIII.8}
\]

Thus repeated-orbit raw weight is asymptotically negligible relative to primitive-prime weight.  This does not prove eigenvector dominance because the gap is exponentially small, but it gives a clean residual decomposition to test.

---

# Triangulation IX — No-go theorems, the horizon correction, and the transfer-operator target

## IX.1 The finite additive/multiplicative interface is irreducible

Take a finite basis of distinct integers.  The joint prime-valuation operators

\[
N_p|n\rangle=v_p(n)|n\rangle
\]

separate basis states.  Therefore the algebra they generate contains every diagonal matrix unit \(E_{ii}\).

Let \(F\) be an additive discrete Fourier matrix.  Every entry \(F_{ij}\) is nonzero.  Hence

\[
E_{ii}FE_{jj}=F_{ij}E_{ij}.
\]

### Theorem IX.1

\[
\boxed{
\operatorname{Alg}(\{N_p\},F)=M_N(\mathbb C),
}
\tag{IX.1}
\]

and therefore

\[
\boxed{
\{N_p,F\}'=\mathbb CI.
}
\tag{IX.2}
\]

This explains why a nontrivial hidden operator cannot simply commute with every raw prime occupation and with raw additive Fourier.

The uploaded finite searches are consistent with this theorem:

- no stable bare differential commutant;
- finite local prime polarizers did not produce a useful near-commuting direction;
- adding more local polarizers did not lower the commutator substantially.

The desired operator must therefore be something other than an ordinary common symmetry:

\[
\boxed{
\text{transfer operator, quotient, compression, cocycle, boundary realization, or cohomological action.}
}
\]

## IX.2 Positive kernels do not force real zeros

A positive measure need not have a real-rooted Fourier transform.  The example

\[
\mu=\delta_{-1}+3\delta_0+\delta_1
\]

has transform

\[
3+2\cos z,
\]

whose zeros satisfy

\[
\cos z=-3/2
\]

and are nonreal.

Thus neither positive theta coefficients nor a positive heat kernel can prove RH without a stronger self-adjoint/total-positive structure.

## IX.3 Support alone creates no absolute finite zero horizon

A previous empirical horizon law suggested

\[
T\sim2\pi X
\]

for the specific finite Weil minimizer.  This is a useful conditioning and model-capacity law, but it is not a theorem that compact support can encode only finitely many prescribed zeros.

### Theorem IX.2 — fixed exponential type interpolates any finite zero set

Given any finite real set \(\{\gamma_1,\dots,\gamma_N\}\) and any \(A>0\), put

\[
M=2N+1,
\qquad
\varepsilon=A/M,
\]

and define

\[
\boxed{
F(z)
=
\prod_{j=1}^N(z^2-\gamma_j^2)
\left(
\frac{\sin(\varepsilon z)}{\varepsilon z}
\right)^M.
}
\tag{IX.3}
\]

Then:

- \(F\) has exponential type \(A\);
- \(F(\pm\gamma_j)=0\);
- \(F(x)=O(1/x)\) on the real axis;
- \(F\in L^2(\mathbb R)\);
- by Paley–Wiener, \(F\) is the transform of an \(L^2\) function supported in \([-A,A]\).

Therefore fixed support can interpolate arbitrarily many finite prescribed zeros.

The observed relation \(T\sim2\pi X\) must instead involve:

- basis dimension;
- condition number;
- prolate concentration;
- the minimization principle;
- stable sampling density;
- norm and tail control.

This is a correction, not a dismissal.  The horizon movie is evidence about one extremal algorithm, not a universal information-theoretic prohibition.

## IX.4 Why the modular transfer operator has the wrong atoms

The Mayer transfer operator for the Gauss map has a Fredholm determinant tied to Selberg zeta.  Its spectral theory succeeds because a self-adjoint Laplacian supplies positivity.  But its primitive closed-orbit lengths are hyperbolic geodesic lengths—regulators of real quadratic fields—not \(\log p\).

Conversely, the arithmetic/scaling site has prime circles

\[
C_p=\mathbb R_+^\times/p^{\mathbb Z}
\]

with exactly the right periods \(\log p\), but lacks the self-adjoint Laplacian/polarization that the modular surface has.

This gives a sharp trade:

| system | orbit lengths | independent positive operator |
|---|---|---|
| modular/Selberg | wrong atoms: regulators | yes: Laplacian |
| scaling/adelic site | right atoms: \(\log p\) | missing |

A smooth reparametrization cannot simply convert one rigid length spectrum into the other while preserving the trace formula.

## IX.5 The remaining operator category

The finite-linear search has exhausted the easy categories.  The remaining candidate is necessarily:

- all-prime;
- nonlinear or self-similar;
- regularized;
- boundary-sensitive;
- nonlocal in logarithmic scale;
- capable of producing its own prime amplitudes rather than fitting them;
- equipped with an independently positive or self-adjoint realization.

The q-clock construction of Triangulations III–IV gives a concrete input:

\[
\mathcal D_{q,j}(s)
=
\frac{\Lambda(q^js)}{\Lambda(q^{j+1}s)}.
\]

A genuine transfer-operator moonshot is:

> Construct a scale-graded operator whose local determinant is \(\mathcal D_{q,j}\), whose infinite product is renormalized canonically, and whose ultraviolet boundary condition is self-adjoint for geometric—not zero-divisor—reasons.

The scale cocycle and UV boundary phase show what such an operator must reproduce.  They do not yet construct the positive Hilbert space.

---

# Triangulation X — The absolute geometric route: polarized cohomology before zeros

## X.1 The finite-field proof pattern

For a smooth projective curve \(C/\mathbb F_q\), correspondences live on the surface

\[
C\times C.
\]

The primitive middle cohomology is controlled by

\[
H^1(C)\otimes H^1(C).
\]

Frobenius acts on an independently constructed finite-dimensional cohomology.  Rosati duality and Hodge-index/Castelnuovo–Severi positivity imply

\[
\operatorname{Tr}(TT^*)\ge0.
\]

The zeta functional equation and RH then emerge from a geometry whose positivity existed before the zeros were studied.

That order of construction is the noncircular standard.

## X.2 Correct cohomological degree

Let the hypothetical compactified absolute arithmetic curve be

\[
X=\overline{\operatorname{Spec}\mathbb Z}_{/\mathbb F_1}
\]

and its square

\[
S=X\times_{\mathbb F_1}X.
\]

The positive spectral object should be

\[
\boxed{\mathscr H=H^1_{\mathrm{abs}}(X),}
\]

while correspondences live in

\[
\boxed{
H^2_{\mathrm{abs,prim}}(S)(1)
\simeq
\mathscr H\widehat\otimes\overline{\mathscr H}.
}
\tag{X.1}
\]

This corrects the loose phrase “polarized \(H^1(S)\).”  Hodge index operates in the primitive middle degree of the square.

## X.3 Existing scaffolding

Several pieces are real:

- \(\Lambda\)-/Witt geometry and Frobenius lifts;
- the Connes–Consani arithmetic and scaling sites;
- scaling/Frobenius correspondences and prime circles \(C_p\);
- adelic trace formulas reproducing local explicit-formula terms;
- semilocal Sonin/prolate positivity at the Archimedean place and finite sets of places;
- Hard Lefschetz and Hodge–Riemann theorems for significant classes of smooth projective tropical varieties.

What is not known is a construction that combines these into the required global polarized cohomology for the arithmetic square.

## X.4 Candidate Poisson–Hodge complex

For a finite place set

\[
\Sigma=\{\infty,p_1,\dots,p_r\},
\]

let

\[
A_\Sigma=\mathbb R\times\prod_{p\in\Sigma_f}\mathbb Q_p,
\]

and let \(\Gamma_\Sigma\) be the \(\Sigma\)-unit group.  Consider the quotient groupoids

\[
\mathfrak X_\Sigma=[A_\Sigma/\Gamma_\Sigma],
\qquad
\mathfrak C_\Sigma=[A_\Sigma^\times/\Gamma_\Sigma].
\]

Let

\[
\mathcal S_0(A_\Sigma)
=
\{f\in\mathcal S(A_\Sigma):f(0)=\widehat f(0)=0\}.
\]

Define the half-density Poisson/Gysin map

\[
\boxed{
(E_\Sigma f)([x])
=|x|_\Sigma^{1/2}
\sum_{\gamma\in\Gamma_\Sigma}f(\gamma x).
}
\tag{X.2}
\]

The algebraic complex is

\[
\mathsf K_{\Sigma,\mathrm{alg}}^\bullet
=
[\mathcal S_0(A_\Sigma)\xrightarrow{E_\Sigma}\mathcal S(\mathfrak C_\Sigma)].
\]

Its Schwartz quotient is designed to carry the all-zero trace representation.

An independently positive Hilbert realization is

\[
\boxed{
\mathscr H^1_\Sigma
=
L^2(\mathfrak C_\Sigma,d^\times x)
\big/
\overline{\operatorname{Ran}E_\Sigma}^{L^2}
\simeq
\ker\overline E_\Sigma^{\,*}.
}
\tag{X.3}
\]

The quotient metric is positive by construction.  Scaling preserves multiplicative Haar measure and commutes with the half-density map, so it descends unitarily.  Stone's theorem then gives a self-adjoint generator.

This order is noncircular:

\[
\text{geometry/measure}
\Longrightarrow
\text{positive quotient}
\Longrightarrow
\text{unitary scaling}
\Longrightarrow
\text{self-adjoint generator}.
\]

The zeros have not been used.

## X.5 The quarantined comparison theorem

The algebraic and Hilbert quotients need not coincide.  The precise comparison is

\[
\boxed{
\overline{E_\Sigma\mathcal S_0}^{\mathcal S}
=
\mathcal S(\mathfrak C_\Sigma)
\cap
\overline{E_\Sigma\mathcal S_0}^{L^2}.
}
\tag{X.4}
\]

Interpretation:

\[
\boxed{
\text{every algebraic absolute }H^1\text{ class has a unique }L^2\text{-harmonic representative.}
}
\]

After the necessary semisimplification, this comparison would identify the all-zero algebraic cohomology with the intrinsically unitary Hilbert cohomology.  That would force the centered spectral parameters to be real.

The statement is RH-complete.  Its value is not that it is equivalent to RH; its value is that it proposes a possible **geometric proof source** for the equivalence.

## X.6 Absolute Lefschetz–Hodge target

For a correspondence \(D\), build a cycle class independently from derived fixed loci and Archimedean Green/determinant-line geometry.  Let its action on \(\mathscr H\) be \(T_D\).

The desired Lefschetz formula is

\[
\boxed{
D\cdot\Delta
=
\operatorname{Tr}(T_D|H^0)
-\tau(T_D|H^1)
+
\operatorname{Tr}(T_D|H^2).
}
\tag{X.5}
\]

For primitive \(D\), Hodge index should give

\[
\boxed{
-(D\circ D^*)\cdot\Delta
=
\tau(T_DT_D^*)
\ge0.
}
\tag{X.6}
\]

If the local fixed-point intersections reproduce the explicit formula, this is Weil positivity as a geometric squared norm.

The forbidden shortcut is to define the intersection pairing to be the Weil form and then assert Hodge negativity.  The cycle theory, polarization, and positivity must be constructed before the explicit-formula comparison.

## X.7 Tropical and transverse proof engines

Two candidate engines could prove the comparison:

### Transverse elliptic/Hodge route

Construct a leafwise Dolbeault operator

\[
\mathcal D_\Sigma=\bar\partial_{\mathcal F}+\bar\partial_{\mathcal F}^*
\]

on the complex lift and prove an estimate of the form

\[
\boxed{
\|u\|_{W^{1,2}_{\mathrm{abs}}}
\le
C_\Sigma
\left(
\|\mathcal D_\Sigma u\|_2+
\|u\|_2
\right),
}
\tag{X.7}
\]

with compact primitive resolvent and Schwartz regularity of harmonic representatives.

### Tropical Hodge route

Construct the semilocal square as a tropical object to which Hard Lefschetz and Hodge–Riemann apply, including:

- the distorted scaling correspondences;
- the tangential diagonal term;
- the Archimedean boundary;
- an appropriate finite-type approximation and globalization theorem.

The current tropical Hodge theorems do not automatically apply to the Connes–Consani square or its infinite/continuous boundary.

## X.8 Bounded first targets

A responsible first target is semilocal:

\[
\Sigma=\{\infty,2\}
\quad\text{or}\quad
\{\infty,2,3\}.
\]

Required calibration gates:

1. recover the exact finite-prime weight
   \[
   (\log p)p^{-m/2};
   \]
2. recover the exact Archimedean symbol
   \[
   \Re\psi(1/4+it/2)-\log\pi;
   \]
3. recover known semilocal Sonin/prolate positivity;
4. identify the tangential diagonal/pole classes;
5. prove a genuine Hodge signature theorem on primitive classes.

Passing these gates would validate the model, but the RH content remains in uniform globalization over all primes and the Archimedean boundary.

---

# Integrated synthesis — What the ten triangulations jointly say

## S.1 The prime multiset and Gamma are complementary, not redundant

The prime multiset already produces every positive integer.  Gamma does something categorically different:

\[
\boxed{
\text{multiset}
\longrightarrow
\text{integer values}
\longrightarrow
\text{global Gaussian coupling}
\longrightarrow
\text{continuous scale Mellin transform}.
}
\]

The q-clock decomposition makes this exact:

- finite primes: cyclic digit clocks and ordinary Fredholm determinants;
- infinity: fractional number-operator shifts and zeta determinants;
- completion: one scale cocycle whose UV reflection defect is a phase.

## S.2 The physical occupation law is rigid

Generic support/multiplicity perturbations create scaled zeta towers and multiple reflection centers.  Unrestricted multiplicity is the unique nonnegative one-species law that removes all internal ghost centers.

This does not prove RH, but it explains why the ordinary Euler local factor is structurally singled out by global spectral coherence.

## S.3 The Archimedean place both creates geometry and destroys naive counting

The Gaussian heat ensemble gives an independently positive covariance and Gram geometry.  Yet Mellin/Fourier transport introduces oscillatory phases, and zeta regularization can reverse signs.  Infinity therefore supplies both:

- the most promising positive analytic substrate;
- the exact reason positivity is no longer a finite cardinality.

## S.4 The zero resolvent is the cleanest analytic target

\[
R_\Xi(z)
=-\frac{\Xi'(z)}{2z\Xi(z)}
\]

puts every zero pair in one additive term.  RH becomes:

- Stieltjes positivity;
- Herglotz/Pick positivity;
- Hausdorff complete monotonicity after reflection to \(\Re s>1\).

The reflected Hausdorff criterion is especially useful because all coefficients can be computed from absolutely convergent prime and Gamma data at a safe point.

## S.5 The most viable full-proof and partial-proof tracks differ

### Full-proof analytic track

Prove the prolate–Weil second-variation estimate

\[
\lambda^a\|r_\lambda\|/G_\lambda\to0.
\]

This is an RH-plus selection theorem at an exponentially small scale.

### Partial-theorem track

Develop higher-moment finite-Weil inertia inequalities.  This route has already produced a current unconditional critical-line proportion theorem and can plausibly be advanced without solving all of RH.

### Foundational geometric track

Build independent positive absolute cohomology and prove Lefschetz–Hodge comparison.  This is the most faithful analogue of Weil's proof and the least close to completion.

---

# Exact theorem targets for the next campaign

## Target A — Archimedean q-clock transfer operator

Construct an operator family \(\mathfrak L_q\) such that

\[
\det_{\mathrm{ren}}(I-\mathfrak L_{q,j}(s))
=
\mathcal D_{q,j}(s)
=
\frac{\Lambda(q^js)}{\Lambda(q^{j+1}s)},
\]

with:

1. the finite-prime clock determinant derived from actual local dynamics;
2. the Archimedean zeta determinant derived from an operator domain;
3. a canonical all-scale product;
4. a geometric positive metric or self-adjoint boundary condition;
5. no insertion of the zeta zeros.

**Falsification gate:** if the operator is merely defined by its determinant, it is a re-encoding, not a construction.

## Target B — Heat-to-Hausdorff positivity bridge

For \(a>1/2\), prove

\[
(-1)^r\Delta^r u_n^{(a)}
=
\int_0^\infty
\|B_{n,r,a}(t)\|^2\,d\nu_a(t)
\]

from the prime-multiset heat geometry.

**Falsification gate:** the vectors and measure must be defined without \(\Xi\)'s zeros or the Weil form as an assumed inner product.

## Target C — True prolate Feshbach estimate

Build the exact finite prolate candidate and prove

\[
\lambda^a\frac{\|r_\lambda\|}{G_\lambda}\to0
\qquad(a<1/2).
\]

**Falsification gate:** polynomial candidate accuracy is insufficient; the bound must be relative to the exponentially small spectral gap.

## Target D — Higher-moment rank–inertia certificate

Find an exact inequality using moments through order four or higher that improves the current positive-inertia lower bound for Weil compressions.

**Deliverables:**

- an abstract matrix theorem;
- a rational certificate;
- the exact prime-correlation asymptotic needed;
- a clear statement of whether that asymptotic is currently accessible.

## Target E — Absolute Hodge comparison

Construct the positive Hilbert cohomology independently and prove

\[
\overline{E\mathcal S_0}^{\mathcal S}
=
\mathcal S\cap\overline{E\mathcal S_0}^{L^2}.
\]

Then prove the Lefschetz identity and Hodge signature on the square.

**Falsification gate:** any proof using Mellin division by \(\zeta\), zero locations, or the Weil sign as an axiom is circular.

---

# A 90-day execution plan

## Phase 1 — Reproducible foundation

1. Bundle every dependency of the finite Weil scripts.
2. Separate the parameters:
   - prime cutoff;
   - support width;
   - Galerkin dimension;
   - precision.
3. Record signed lowest eigenvalues, residuals, and interval enclosures.
4. Add Archimedean-only, shuffled-prime, synthetic-clock, primes-only, and repetitions-only controls.
5. Reproduce the local-patch movie from a clean environment.

## Phase 2 — True prolate comparison

1. Implement finite prolate modes \(h_{0,\lambda},h_{4,\lambda}\).
2. Construct \(k_\lambda\) with the exact moment constraint.
3. Compute \(\delta_\lambda,g_\lambda,r_\lambda,G_\lambda\).
4. Decompose residuals into pole, infinity, primitive primes, and repetitions.
5. Determine whether the gap-normalized ratio is improving or whether the near-radical defeats selection.

## Phase 3 — Safe-region moment program

1. Generate \(u_n^{(3/2)}\) symbolically/high-precisely from \(\xi'/\xi\) at \(s=2\).
2. Certify large finite rectangles of Hausdorff inequalities.
3. Search for recurrences, integral kernels, or total-positive matrices.
4. Compare with the prime-multiset heat covariance and Gram kernels.
5. Kill any representation that imports zero data.

## Phase 4 — Higher-moment inertia

1. Formalize the atom class.
2. Reproduce the current second-moment certificate.
3. Run SDP searches through fourth moment.
4. Extract exact candidate inequalities.
5. Prove the best candidate and publish the abstract matrix result even if the analytic moment remains open.

## Phase 5 — q-clock operator note

Write a focused paper/note containing:

- trace-class q-clock determinant;
- carry cancellation;
- Archimedean shifted-number determinant;
- completed scale cocycle;
- affine reflection defect;
- UV boundary phase theorem;
- exact statement of the missing positive metric.

This note is structurally coherent and independently checkable even without RH progress.

---

# Claim ledger

## Proved or fully derived in this dossier

- support-fiber decomposition of \(\zeta\);
- Witt/necklace factorization of \(Z_{a,b}\);
- single-center rigidity in the two-parameter family;
- general unrestricted-multiplicity rigidity;
- primitive/repetition tangent formulas;
- q-ary digit decomposition;
- cyclic-clock determinant;
- trace-class q-clock Fredholm determinant;
- carry-cancellation identity;
- zeta-regularized shifted-number determinant;
- Archimedean q-clock determinant;
- scale cocycle and its generator;
- affine scaling/reflection commutator;
- UV-boundary localization and critical-line phase;
- Archimedean heat log-submodularity;
- covariance/Fisher positivity;
- positive heat Gram matrix;
- Stieltjes characterization of RH;
- reflection ladder;
- reflected Hausdorff moment criterion;
- off-line signature block and quadratic onset;
- higher-moment positive-inertia inequality;
- full finite matrix-algebra no-go;
- fixed-type finite interpolation theorem;
- primitive/repetition raw-weight asymptotics;
- elementary \(K\)-free counting theorem.

No claim of literature novelty is attached to these deductions.

## Calibrated numerically

- q-clock Euler layers versus zeta ratios;
- Archimedean q-clock determinant to high precision;
- scale cocycle and UV boundary phase;
- first reflected Hausdorff coefficients and finite differences;
- prime-occupation covariance positivity;
- primitive/repetition weight separation;
- quadratic negative eigenvalue onset under modeled off-line displacement;
- finite higher-moment inertia bounds;
- fixed-type interpolation of the first five ordinates;
- uploaded few-prime local-patch refinement.

## Current external results relied upon

- semilocal Archimedean/Sonin positivity;
- prolate candidate convergence to \(\Xi\);
- real-zero theorem for suitable convolution ground states;
- current finite-Weil critical-line proportion theorem;
- finite Guinand–Weil certification barriers;
- tropical Hard Lefschetz/Hodge–Riemann theorems in their established setting.

## Open and RH-bearing

- global Weil positivity;
- Stieltjes/Pick positivity from primes and infinity;
- all reflected Hausdorff inequalities;
- true prolate Feshbach/second-variation estimate;
- an all-prime self-adjoint transfer operator with prime periods;
- absolute Hodge comparison and Lefschetz–Hodge theorem;
- uniform globalization of semilocal positivity.

---

# Pitfall ledger

1. **Using \(h(\gamma)\) off the line.**  The correct coordinate is \(\lambda_\rho\).
2. **Treating one positive matrix as Weil positivity.**  RH requires every admissible direction.
3. **Equating accurate roots with convergence to \(\Xi\).**  Interpolation can locate roots while missing tails and strip behavior.
4. **Treating finite-window self-adjointness as arithmetic content.**  Momentum in a box is automatically self-adjoint.
5. **Calling a determinant construction noncircular when the determinant is prescribed.**  The operator must generate the determinant from independent dynamics.
6. **Using zeta regularization as positivity.**  Regularized values can be negative for positive spectra.
7. **Assuming Gamma is another prime multiplicity factor.**  It is the continuous-scale Fourier/Mellin completion.
8. **Confusing statistics with location.**  GUE-like spacings do not force \(\Re\rho=1/2\).
9. **Assuming support creates an absolute horizon.**  Fixed exponential type can interpolate any finite zero set.
10. **Defining the desired cohomological norm to be the Weil form.**  That assumes RH.
11. **Ignoring high-dimensional near-radicals.**  A small Rayleigh quotient does not identify the ground direction.
12. **Coupling numerical parameters.**  Prime information, support, basis capacity, and precision must be varied independently.
13. **Losing the sign of a tiny eigenvalue by logging \(|\mu|\).**  The sign is the RH-sensitive datum.
14. **Inferring an asymptotic from a handful of small cutoffs.**  The earlier simple exponential law failed its own later test.
15. **Treating a current preprint as settled literature.**  External results should be labeled by publication status.

---

# Reproducibility map

The companion script

`rh_master_dossier_tests.py`

performs ten independent calibrations:

1. finite q-clock Euler layer versus \(\zeta(q^js)/\zeta(q^{j+1}s)\);
2. Archimedean q-clock determinant;
3. scale cocycle and affine reflection defect;
4. UV boundary phase;
5. reflected Hausdorff coefficients;
6. heat covariance and submodularity;
7. primitive/repetition weights;
8. off-line signature onset;
9. higher-moment inertia bounds;
10. fixed exponential-type interpolation.

The results are saved in

`rh_master_dossier_tests_results.txt`.

These tests certify formulas and instrumentation only.  They do not certify any infinite RH-equivalent limit.

---

# Source map

## User-provided research sources

- `SCHRODINGER_ARCHIMEDEAN_DOSSIER(1)(1).md` — long-form session history, computational descent, wall mapping, Connes/prolate analysis, geometric blueprints, and epistemic ledger.
- `RH_MULTISET_TRIANGULATION_REPORT.md` — multiset deformation, ghost tower, resolvent, Loewner, no-go and partial-theorem analysis.
- `RH_QARY_MOONSHOT_REPORT.md` — q-ary digit layers, prime clocks, Gamma multiplication, support/multiplicity infinities, weaker theorem ladder.
- `coherent_truncation.py` — falsifiable all-prime/coherent-truncation test.
- `local_patch.py` and `local_patch.log` — fixed-window zero-refinement experiment.
- prior reproducible triangulation scripts and output files.

## Primary external references

The following are the main current sources consulted; arXiv identifiers are supplied for precise lookup.

1. Alain Connes, **“The Riemann Hypothesis: Past, Present and a Letter Through Time”**, arXiv:2602.04022 (2026).
2. Alain Connes and Walter D. van Suijlekom, **“Quadratic Forms, Real Zeros and Echoes of the Spectral Action”**, arXiv:2511.23257.
3. Levent Alpöge and Alex Furman, preprint on **more than two thirds of nontrivial zeta zeros being simple and on the critical line**, arXiv:2608.13637.
4. Alexey Groskin, preprint on a **finite Guinand–Weil dictionary and certification barriers**, arXiv:2607.02828.
5. Alain Connes and Caterina Consani, **“Weil Positivity and Trace Formula, the Archimedean Place”**, arXiv:2006.13771.
6. Alain Connes, Caterina Consani, and Henri Moscovici, **“Zeta Zeros and Prolate Wave Operators”**, arXiv:2310.18423.
7. Omid Amini and Matthieu Piquerez, **“Hodge Theory for Tropical Varieties”**, arXiv:2007.07826.
8. Alain Connes and Caterina Consani, work on the **Riemann–Roch strategy and complex lift of the scaling site**, arXiv:1805.10501.
9. NIST Digital Library of Mathematical Functions, chapters on Gamma, zeta, and functional equations.
10. Classical background: Weil's positivity criterion; Tate's thesis; Li's criterion; Paley–Wiener theory; Herglotz/Pick and Hausdorff moment theorems; Slepian–Landau–Pollak prolate theory; tropical Hodge–Riemann theory.

---

# Final research judgment

The powerset/multiset framing has now produced more than an analogy.  It supplies:

- a rigid algebra of local occupation laws;
- an exact tower of scaled zero divisors;
- a canonical q-clock Fredholm determinant;
- an exact Archimedean zeta-determinant partner;
- a completed scale cocycle whose connection term is the logarithmic derivative;
- a theorem localizing the functional-equation defect at an Archimedean UV boundary;
- an independently positive heat/Fisher geometry;
- a safe-region Hausdorff reformulation of the zero resolvent.

What it has **not** yet supplied is the decisive positive transport from the prime/heat side to the zero/Weil side.

That missing arrow can be written in three equivalent research dialects:

\[
\boxed{
\text{analytic: }
\lambda^a\|r_\lambda\|/G_\lambda\to0;
}
\]

\[
\boxed{
\text{operator: }
K_F(w,z)=\langle B_z,B_w\rangle
\text{ from prime+Archimedean data};}
\]

\[
\boxed{
\text{geometric: }
-(D\circ D^*)\cdot\Delta
=\tau(T_DT_D^*)\ge0.
}
\]

The most realistic near-term theorem is a stronger finite-Weil inertia bound.  The most direct current full-RH attack is the prolate second-variation estimate.  The deepest faithful moonshot is an absolute Lefschetz–Hodge theory.

The tide rises by proving increasingly structural statements that remain meaningful if RH is temporarily removed from the room.  That is the standard by which every future move in this program should be judged.

---

# Appendix A — Calibration tables

## A.1 q-clock Euler layers

At

\[
s=2.3+0.4i,
\]

finite prime products through \(200000\) were compared with

\[
\frac{\zeta(q^js)}{\zeta(q^{j+1}s)}.
\]

| \(q\) | \(j\) | absolute truncation error |
|---:|---:|---:|
| 2 | 0 | \(9.72\times10^{-9}\) |
| 2 | 1 | \(1.86\times10^{-21}\) |
| 3 | 0 | \(1.01\times10^{-8}\) |
| 3 | 1 | \(7.14\times10^{-34}\) |
| 4 | 0 | \(1.01\times10^{-8}\) |
| 4 | 1 | \(3.30\times10^{-46}\) |

The \(j=0\) discrepancy is the omitted prime tail; higher digit scales converge much faster.

## A.2 Archimedean q-clock determinant

At

\[
s=1.7+0.2i,
\]

the determinant formula IV.2 was checked at 60-digit precision.

| \(q\) | relative error |
|---:|---:|
| 2 | \(9.60\times10^{-62}\) |
| 3 | \(2.40\times10^{-61}\) |
| 5 | \(2.31\times10^{-62}\) |

The scale cocycle was verified to approximately \(4.1\times10^{-62}\).

## A.3 UV boundary phase

For

\[
q=2,
\qquad J=4,
\qquad s=\frac12+3i,
\]

the finite-tower reflection ratio and the boundary ratio agreed to approximately

\[
1.17\times10^{-61},
\]

and the boundary modulus was

\[
1.00000000000000000000.
\]

The finite zeta factor at the UV endpoint still differed from \(1\) by about \(0.00403\); at larger \(J\) it decays rapidly and Gamma dominates.

## A.4 Reflected Hausdorff coefficients at \(a=3/2\)

| \(n\) | \(u_n^{(3/2)}\) |
|---:|---:|
| 0 | \(5.1799673647500507168874439446905\times10^{-2}\) |
| 1 | \(1.8495206873622553245225036161371\times10^{-4}\) |
| 2 | \(1.5923444944324991803598638829270\times10^{-6}\) |
| 3 | \(1.6271659709678662203483585691477\times10^{-8}\) |
| 4 | \(1.7535340739926797169684949654085\times10^{-10}\) |
| 5 | \(1.9268257495587767635678353569003\times10^{-12}\) |
| 6 | \(2.1336551680636450585501823481819\times10^{-14}\) |
| 7 | \(2.3702894991528826931177604316291\times10^{-16}\) |

The smallest tested signed finite difference was

\[
2.94\times10^{-20}>0.
\]

This is a useful conditioning warning: the margins become tiny rapidly, so interval arithmetic is mandatory at larger orders.

## A.5 Primitive versus repeated critical weights

| \(X\) | primitive \(\sum_{p\le X}\log p/\sqrt p\) | repeated \(\sum_{p^m\le X,m\ge2}\log p/p^{m/2}\) | ratio |
|---:|---:|---:|---:|
| \(10\) | 2.579661 | 0.957842 | 0.371306 |
| \(10^2\) | 14.622526 | 2.273675 | 0.155491 |
| \(10^3\) | 56.574158 | 3.933599 | 0.069530 |
| \(10^4\) | 192.218327 | 5.247726 | 0.027301 |
| \(10^5\) | 623.347136 | 6.594218 | 0.010579 |
| \(10^6\) | 1989.068568 | 7.838240 | 0.003941 |

The table is consistent with the proved asymptotics \(2\sqrt X\) versus \(\tfrac12\log X+C\).

## A.6 Off-line block

For the simple test vector

\[
v(z)=(1,z,z^2),
\qquad z=14.134725\ldots+i\delta,
\]

the least eigenvalue of

\[
4(aa^{\mathsf T}-bb^{\mathsf T})
\]

was:

| \(\delta\) | least eigenvalue |
|---:|---:|
| 0 | numerical zero |
| 0.025 | \(-2.54\times10^{-3}\) |
| 0.050 | \(-1.02\times10^{-2}\) |
| 0.100 | \(-4.06\times10^{-2}\) |
| 0.200 | \(-1.63\times10^{-1}\) |

The factor-of-four progression under doubling \(\delta\) displays the predicted quadratic onset.

## A.7 Uploaded local-patch movie

The source log reports:

| cutoff | crossings identified with true low zeros | headline errors |
|---:|---:|---|
| \(x=2\) | 1 of 5 | \(\gamma_1\) error \(0.227\) |
| \(x=3\) | 3 of 5 | \(8.27\times10^{-5}, 7.41\times10^{-3}, 5.89\times10^{-2}\) |
| \(x=5\) | 5 of 5 | \(2.65\times10^{-10}\) through \(1.08\times10^{-5}\) |

The experiment is noncircular at the construction stage.  Its limitations are the coupled cutoff parameters and the absence of the imported matrix-building module from the uploaded bundle.

---

# Appendix B — Logical dependency graph

The following arrows are established:

\[
\mathrm{RH}
\Longrightarrow
\lambda_\rho\in\mathbb R
\Longrightarrow
Q_W(f)=\sum_\rho|F(\lambda_\rho)|^2\ge0.
\]

Weil's criterion supplies the converse:

\[
Q_W\ge0\ \forall f
\Longrightarrow
\mathrm{RH}.
\]

Likewise,

\[
\mathrm{RH}
\iff
F_\Xi\text{ Stieltjes}
\iff
\text{all Pick matrices PSD}
\iff
(u_n^{(a)})\text{ Hausdorff}.
\]

These are equivalences, not proof progress by themselves.

The Connes/prolate implication chain is:

\[
\text{true Feshbach estimate}
\Longrightarrow
\theta_{\lambda^2}\sim k_\lambda
\Longrightarrow
\widehat\theta_{\lambda^2}\to\Xi
\Longrightarrow
\Xi\text{ has only real zeros}
\Longrightarrow
\mathrm{RH}.
\]

The first arrow is the open analytic theorem.

The geometric implication chain is:

\[
\begin{aligned}
&\text{independent absolute cohomology}
+\text{ polarization}
+\text{ Lefschetz identity}\\
&\hspace{3cm}\Longrightarrow
Q_W(f)=\tau(T_fT_f^*)\ge0\\
&\hspace{3cm}\Longrightarrow
\mathrm{RH}.
\end{aligned}
\]

The construction of the positive cohomology and the comparison identity is open.

The partial-theorem chain is:

\[
\text{finite Weil atom decomposition}
+\text{ trace moments}
+\text{ inertia inequality}
\Longrightarrow
\text{uniform critical-line proportion}.
\]

This is the one chain that has already yielded current unconditional progress without requiring the full sign theorem.

---

# Appendix C — Mirror versus advance test

Before investing in a new formulation, ask:

1. **Does the construction use the zeros, \(\Xi\), or the Weil form to define its positive metric?**  If yes, it is probably circular.
2. **Does it merely rewrite \(\zeta\), \(\xi\), or the explicit formula?**  If yes, it is an identity-level mirror.
3. **Does it produce a positive Hilbert space, count, or intersection pairing from independent data?**  If yes, it may be an advance.
4. **Does it yield a theorem strictly weaker than RH?**  If yes, it may raise the tide even if it cannot finish the summit.
5. **Can it be falsified at a finite or semilocal calibration stage?**  If no, it is not yet a research instrument.
6. **Are the operator's coefficients derived from dynamics, or chosen to reproduce the explicit formula?**  Fitted coefficients describe; derived coefficients constrain.
7. **Is the all-prime/global limit controlled uniformly?**  If not, finite success cannot be promoted.
8. **Does the claimed positivity survive regularization and domain completion?**  A finite value is not a positive form.
9. **Does a proposed symmetry live outside the full finite matrix algebra no-go?**  If not, it is already ruled out.
10. **What exact inequality would be new?**  If no new inequality can be written, the move has not yet reached proof level.
