# Quotient-residue Boolean convolution: composite factorization as a conductor support cube

**Date:** 2026-10-07  
**Status:** exact algebra/combinatorics + a concrete floor/fractional-part research interface. No RH assumption.  
**RH remains open.**

The user's expansion

\[
(pa+b)(qc+d)(re+f)
\]

contains a precise support hierarchy.

It is not merely distributivity: it is the Boolean/divisor-lattice expansion of a multiaffine function in distinct prime directions.

This supplies:

1. an exact support-rank grading;
2. a subset/Dirichlet convolution formula;
3. Möbius/finite-difference extraction operators for pure interactions;
4. a minimal generating polynomial for sweeping all interaction orders;
5. a natural interface to generalized Dedekind/floor-sum reciprocity when the quotient/residue variables come from actual Euclidean division.

---

# 1. Correct three-prime expansion

Let

\[
x_p=pa+b,\qquad
x_q=qc+d,\qquad
x_r=re+f.
\]

Then

\[
\boxed{
\begin{aligned}
x_px_qx_r
={}&pqr(ace)
\\
&+pq(acf)
+pr(ade)
+qr(bce)
\\
&+p(adf)
+q(bcf)
+r(bde)
\\
&+bdf.
\end{aligned}
}
\]

The terms split by support rank:

\[
\boxed{
3\text{-prime}
+
2\text{-prime}
+
1\text{-prime}
+
0\text{-prime}.
}
\]

The user's regrouping contained one small typo: inside the \(r(\cdots)\) block the \(p\)-term is \(p(ead)\), not \(p(ad)\).

---

# 2. General subset expansion

Let

\[
P=\{p_1,\ldots,p_m\}
\]

be distinct prime labels and write

\[
x_i=p_i a_i+b_i.
\]

For

\[
S\subseteq[m],
\]

define

\[
p_S=\prod_{i\in S}p_i,
\]

\[
a_S=\prod_{i\in S}a_i,
\]

\[
b_{S^c}=\prod_{j\notin S}b_j.
\]

Then

\[
\boxed{
\prod_{i=1}^m(p_i a_i+b_i)
=
\sum_{S\subseteq[m]}
p_Sa_Sb_{S^c}.
}
\]

Thus every face of the Boolean support cube occurs exactly once.

The support rank of a term is

\[
|S|.
\]

This is the same support-rank grading that appears in the Suzuki \(\omega\)-jet hierarchy.

---

# 3. Complementary residue dressing

A term supported on the prime subset \(S\) is

\[
\boxed{
p_Sa_Sb_{S^c}.
}
\]

So an interaction among the directions in \(S\) is **dressed by the residues of every direction outside \(S\)**.

For the three-prime case:

\[
pq\text{ interaction}
=
pq(ac)\,f,
\]

\[
pr\text{ interaction}
=
pr(ae)\,d,
\]

\[
qr\text{ interaction}
=
qr(ce)\,b.
\]

This is important.

The complement is not discarded.

It becomes an environment/context coefficient for the active support cell.

That is exactly the algebraic shape one expects from eliminating or conditioning on complementary support sectors.

---

# 4. Squarefree divisor / Dirichlet-convolution form

Put

\[
R=\prod_{i=1}^m p_i.
\]

Every subset \(S\) corresponds uniquely to a squarefree divisor

\[
d=p_S\mid R.
\]

Define on divisors of \(R\)

\[
\boxed{
A(d)
=
d
\prod_{p_i\mid d}a_i,
}
\]

and

\[
\boxed{
B(d)
=
\prod_{p_i\mid d}b_i.
}
\]

Then

\[
\boxed{
\prod_i(p_i a_i+b_i)
=
\sum_{d\mid R}
A(d)B(R/d).
}
\]

In other words,

\[
\boxed{
X(R)
=
(A*B)(R),
}
\]

where \(*\) is divisor/Dirichlet convolution restricted to the squarefree divisor lattice of \(R\).

So ordinary composite multiplication naturally lives in the same incidence algebra whose inverse is Möbius inversion.

---

# 5. Prime-innovation projectors

Introduce the residue projection

\[
R_i:
p_i a_i+b_i
\longmapsto
b_i
\]

and the prime innovation

\[
\boxed{
Q_i=I-R_i.
}
\]

Then

\[
Q_i(p_i a_i+b_i)=p_i a_i.
\]

The projections commute because they act on distinct variables.

Therefore

\[
\boxed{
I
=
\prod_{i=1}^m(R_i+Q_i)
=
\sum_{S\subseteq[m]}
Q_SR_{S^c}.
}
\]

Applied to the composite product,

\[
\boxed{
Q_SR_{S^c}
\prod_i(p_i a_i+b_i)
=
p_Sa_Sb_{S^c}.
}
\]

Thus every support face is extracted by a canonical finite-difference/augmentation projector.

The top interaction is

\[
\boxed{
Q_1Q_2\cdots Q_m
\prod_i(p_i a_i+b_i)
=
\left(\prod_ip_i\right)
\left(\prod_i a_i\right).
}
\]

This is the raw quotient-residue analogue of the top support innovation in the Suzuki conductor factor.

---

# 6. One-variable support-spectrum generating polynomial

Introduce one bookkeeping parameter \(t\):

\[
\boxed{
\mathcal P(t)
=
\prod_{i=1}^m
(b_i+t\,p_ia_i).
}
\]

Then

\[
\boxed{
\mathcal P(t)
=
\sum_{k=0}^m
H_k\,t^k,
}
\]

where

\[
\boxed{
H_k
=
\sum_{\substack{S\subseteq[m]\\|S|=k}}
p_Sa_Sb_{S^c}.
}
\]

So:

- \(H_0\) is pure residue;
- \(H_1\) is the one-prime layer;
- \(H_2\) is the pair layer;
- \(\cdots\);
- \(H_m\) is the full-support cell.

This gives a minimal sweep of the entire interaction hierarchy without enumerating it conceptually one term at a time.

---

# 7. Newton compression when all residues are nonzero

If

\[
b_i\ne0
\]

for every \(i\), let

\[
z_i=\frac{p_ia_i}{b_i},
\qquad
B=\prod_i b_i.
\]

Then

\[
\boxed{
\mathcal P(t)
=
B\prod_i(1+t z_i).
}
\]

Hence

\[
\boxed{
H_k
=
B\,e_k(z_1,\ldots,z_m),
}
\]

where \(e_k\) is the \(k\)-th elementary symmetric polynomial.

Therefore all \(2^m\) support-face amplitudes, grouped by rank, are controlled by only the \(m\) power sums

\[
\boxed{
s_j
=
\sum_i z_i^j,
\qquad
1\le j\le m,
}
\]

through Newton's identities

\[
\boxed{
k e_k
=
\sum_{j=1}^k
(-1)^{j-1}
e_{k-j}s_j.
}
\]

This is a concrete answer to the user's earlier desire for a **minimal sweep/characterization of loop families**:

\[
\boxed{
\text{support-rank spectrum}
\quad\text{can be reconstructed from a short moment sequence}.
}
\]

The ratio form should not be used when some residue vanishes; the polynomial formulation remains valid without that assumption.

---

# 8. Logarithmic derivative linearizes the composite

Again assuming nonzero \(b_i\),

\[
\frac{\mathcal P'(t)}{\mathcal P(t)}
=
\boxed{
\sum_i
\frac{z_i}{1+t z_i}.
}
\]

Expanding at \(t=0\),

\[
\boxed{
\frac{d^k}{dt^k}
\log\mathcal P(t)\Big|_{t=0}
=
(-1)^{k-1}(k-1)!
\sum_i z_i^k.
}
\]

Thus the multiplicative composite hierarchy is linearized into a sum of local prime-direction responses by a logarithmic derivative.

This is structurally analogous to the Euler-product identity

\[
-\frac{\zeta'}{\zeta}
=
\text{sum of local prime-power orbit responses}.
\]

It does **not** make the two functions equal.

It identifies the same algebraic mechanism:

\[
\boxed{
\text{logarithmic derivative}
=
\text{multiplicative hierarchy }\to\text{ additive local source}.
}
\]

---

# 9. Raw mixed terms are not yet genuine interaction

There is an important hostile control.

Because

\[
\mathcal P(t)
=
\prod_i(b_i+t p_i a_i)
\]

factorizes completely into one-direction factors,

\[
\boxed{
\log\mathcal P(t)
=
\sum_i
\log(b_i+t p_i a_i).
}
\]

So all **connected mixed cumulants** of the bare product geometry vanish.

The pair terms

\[
pq(acf),\quad pr(ade),\quad qr(bce)
\]

are real algebraic cross terms, but they are disconnected products of independent local factors.

They are not, by themselves, arithmetic curvature.

This exactly matches the repository's CRT-flat hostile control.

---

# 10. Connected interaction by subset Möbius inversion

Suppose a dressed/history-dependent amplitude

\[
Z(S)
\]

is assigned to every prime subset \(S\).

Define the connected interaction potential by Boolean Möbius inversion:

\[
\boxed{
K(S)
=
\sum_{T\subseteq S}
(-1)^{|S|-|T|}
\log Z(T),
}
\]

whenever the logarithms are defined.

If

\[
Z(S)
=
\prod_{i\in S}Z(\{i\}),
\]

then

\[
\boxed{
K(S)=0
\qquad
(|S|\ge2).
}
\]

So \(K(S)\) is a clean test for genuine nonfactorizing interaction.

The bare quotient-residue product is the null geometry.

Carry/history/Archimedean dressing must make these connected quantities nonzero if they are to encode actual arithmetic curvature.

---

# 11. Exact relation to Suzuki support jets

Suzuki's conductor coefficient is

\[
b_\omega(n)
=
n^{\omega-\frac12}
\prod_{p\mid n}
(1-p^{-2\omega}).
\]

The support product

\[
\prod_{p\mid n}
(1-p^{-2\omega})
\]

has exactly the same Boolean support cube:

\[
\boxed{
\prod_{p\mid n}
(1-p^{-2\omega})
=
\sum_{S\subseteq\operatorname{supp}(n)}
(-1)^{|S|}
\prod_{p\in S}p^{-2\omega}.
}
\]

But it is already the **top centered/innovation cell**, not the raw moment product.

The quotient-residue decomposition therefore supplies a useful dictionary:

\[
\boxed{
\text{raw composite expansion}
=
\text{all support faces},
}
\]

\[
\boxed{
\text{prime-wise centering / augmentation}
=
\text{extract pure support cells},
}
\]

\[
\boxed{
\text{Suzuki factor}
=
\text{positive top-support innovation volume}.
}
\]

This is why the same Boolean/divisor algebra keeps reappearing.

---

# 12. If the variables come from actual Euclidean division

Now specialize to one ordinary integer \(x\).

For each prime \(p\), write

\[
\boxed{
x
=
p\,a_p(x)+b_p(x),
}
\]

where

\[
a_p(x)
=
\left\lfloor\frac xp\right\rfloor,
\qquad
b_p(x)=x\bmod p.
\]

Equivalently,

\[
\boxed{
a_p(x)
=
\frac xp
-
\left\{\frac xp\right\},
}
\]

and

\[
\boxed{
b_p(x)
=
p
\left\{\frac xp\right\}.
}
\]

Therefore every quotient-residue support term becomes a polynomial in \(x\) plus products of fractional-part/carry fields.

For example,

\[
p\,a_p(x)
=
x-p\left\{\frac xp\right\}.
\]

So a two-prime quotient term contains products such as

\[
\left\{\frac xp\right\}
\left\{\frac xq\right\}.
\]

These are the natural arithmetic correlation fields beneath the raw composite expansion.

---

# 13. Full CRT averaging is flat; chronological windows are not

For distinct primes \(p,q,\ldots\), the residue tuple

\[
(x\bmod p,\ x\bmod q,\ldots)
\]

runs uniformly over the product residue space when \(x\) runs over one complete CRT period.

Therefore centered functions of separate residue coordinates are orthogonal over the complete period.

That is the bare CRT flatness theorem again.

But:

- quotient functions
  \[
  \lfloor x/p\rfloor
  \]
  retain the global SUCC position;
- finite prefixes/windows do not average over a complete infinite symmetry;
- carry boundaries break the quotient-only product description.

So the chronology-sensitive information is precisely in **floor/residue correlations before complete-period quotienting**.

---

# 14. Dedekind/Fourier-Dedekind interface

Products and sums of floor/fractional-part functions are a classical source of generalized Dedekind and Fourier--Dedekind sums.

The relevant pattern is:

\[
\boxed{
\text{polynomial bulk}
+
\text{periodic fractional/carry correlation}.
}
\]

Generalized Dedekind-type sums provide exact finite Fourier expansions and reciprocity relations for these periodic remainders.

This is a natural classical toolset for the present program because the critical Suzuki conductor discrepancy is already

\[
E_0(X)
=
-\sum_{d\le X}
\frac{\mu(d)}d
\left\{\frac Xd\right\}
-
X\sum_{d>X}\frac{\mu(d)}{d^2}.
\]

The proposed next bridge is therefore:

\[
\boxed{
\text{quotient-residue composite faces}
\to
\text{generalized Dedekind/Fourier-Dedekind sums}
\to
\text{exact reciprocity/carry identities}
\to
\text{Suzuki conductor residual}.
}
\]

No equality to the Suzuki residual is claimed yet.

---

# 15. Why reciprocity is potentially interesting

The present RH wall has the form

\[
\boxed{
\text{positive local arithmetic/Archimedean energies}
-
\text{global completion counterterm}.
}
\]

A useful carry identity must therefore do more than estimate an oscillatory sum.

It must exchange local quotient/residue descriptions while producing an explicit lower-dimensional/polynomial correction.

That is precisely the *shape* of reciprocity laws in the Dedekind-sum family.

This does not imply those classical reciprocity laws solve the RH wall.

It makes them a mathematically targeted next probe rather than an analogy.

---

# 16. Proposed next exact probe

For distinct small prime powers \(q_1,\ldots,q_r\):

1. write the exact-depth centered residue/carry functions on the common LCM clock;
2. form their quotient-dressed products using
   \[
   a_q(x)=\lfloor x/q\rfloor;
   \]
3. decompose the result into:
   - polynomial bulk;
   - exact-conductor periodic remainder;
4. identify the remainder as a finite Fourier-Dedekind sum or prove it is outside that class;
5. apply known reciprocity identities when available;
6. compare the resulting correction term against:
   \[
   -\sum_d\frac{\mu(d)}d\{X/d\},
   \]
   and against the first nontrivial Suzuki mixed-conductor jets;
7. run complete-period CRT averaging as the required zero-curvature control.

The first useful theorem would be an exact identity showing that chronological quotient/residue dressing turns a flat product-support cell into the same signed carry structure appearing in Suzuki.

---

# 17. Compact answer to the user's observation

For

\[
\prod_i(p_i a_i+b_i),
\]

there is one term for every subset of prime directions:

\[
\boxed{
S
\longmapsto
\left(\prod_{i\in S}p_i a_i\right)
\left(\prod_{j\notin S}b_j\right).
}
\]

So composite multiplication naturally carries:

- a Boolean support cube;
- a squarefree divisor grading;
- complementary-residue dressing;
- a Möbius/finite-difference extraction calculus;
- a short moment/Newton description;
- a floor/fractional-part carry calculus when the variables come from Euclidean division.

The raw cube is flat.

The **failure of that cube to remain factorized under chronological quotient/carry transport** is the object worth calling interaction curvature.
