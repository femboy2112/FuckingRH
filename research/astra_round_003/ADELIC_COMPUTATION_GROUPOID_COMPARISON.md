# Adelic, computation-groupoid, and prime-tower comparison

**Verdict:** the arithmetic identities survive, but the proposed identification
of the common Brownian repair with the adelic trace radical does not. A
trace-preserving radical quotient cannot erase that repair. The known
semilocal maps have an exact formula but supply neither the missing Suzuki
Gram map nor a uniform metric bound. This kills the direct identification,
not every possible adelic construction. RH is not proved.

This audit independently read the source results below and the four
Aletheia notes specified in the brief. The primary PDFs were downloaded,
hashed, and the key theorem pages rendered; provenance is in
[reviews/adelic_sources.json](reviews/adelic_sources.json). The mathematical
obstructions below do not use zero locations.

## 1. What the primary sources actually give

| Primary source | Exact location | Verified content relevant here |
|---|---|---|
| Connes–Consani–Marcolli, [*The Weil proof and the geometry of the adeles class space*, arXiv:math/0703392v1](https://arxiv.org/pdf/math/0703392v1) | Definition 4.14, p.23; Lemmas 4.15/4.17, pp.24–25; Remark 4.18 | The periodization range `V` acts trivially on the cohomological quotient and annihilates its trace pairing. |
| Same | Proposition 6.2, Corollary 6.3, Proposition 6.4, p.29; Definition 7.1, p.30 | Half-density trace positivity is RH-equivalent. The radical adjustment changes test representatives. Degree/codegree are Mellin values, not evaluation at the identity. |
| Connes–Consani, [*Quasi-inner functions and local factors*, arXiv:2008.10974v1](https://arxiv.org/pdf/2008.10974v1) | Fact 3.6, p.13; Theorem 4.8, p.22; Definition 5.2 and Theorem 5.3, p.23 | An individual finite ratio is not quasi-inner. A finite product including infinity is quasi-inner; Sonin spaces admit injective multiplier maps. |
| Connes–Consani–Moscovici, [*Zeta zeros and prolate wave operators*, arXiv:2310.18423v2](https://arxiv.org/pdf/2310.18423v2) | Proposition 4.6, pp.21–22, equation (57), p.22; Proposition 4.7, equation (59), pp.22–23; Theorem 4.6 and §4.8, p.23 | The semilocal Sonin map is a Hilbertian isomorphism. The finite set of places still changes the inner product. |
| Suzuki, [*Aspects of the screw function corresponding to the Riemann zeta-function*, arXiv:2206.03682v4](https://arxiv.org/pdf/2206.03682v4) | Equations (11.1)–(11.2), pp.29–30; Theorem 11.1 and final paragraph of §11, p.30 | The shifted family and its semigroup are genuine. Eventual positivity characterizes the shifted zero-free half-plane; `−Psi_(1/2)` is a global screw function. |

These are primary-source theorems, not new results of this round. In
particular, quasi-innerness means a specified off-diagonal compressed
multiplication operator is compact. It does **not** state positivity of
`K_Psi`.

## 2. The exact Mellin/trace square, and the type mismatch

Restrict to the trivial compact character of the idele class group of
`Q`, normalize its compact factor to mass one, and put `u=exp(x)`.
For a smooth compactly supported additive test function `phi`, set

\[
 (J\phi)(u)=u^{-1/2}\phi(\log u),\qquad d^*u=du/u.
\]

Direct change of variables gives

\[
 J(\phi*\psi)=J\phi\star J\psi,
 \qquad
 \widehat{J\phi}(z)=\int_{\mathbb R}\phi(x)e^{(z-1/2)x}\,dx.
\]

Thus the half-density trace functional pulls back to the usual
critical-line Weil functional:

\[
 W(\phi)=\operatorname{Tr}\bigl(\vartheta_m(J\phi)|H^1_{\chi=1}\bigr).
\]

This is the valid comparison square: additive convolution, the map `J`,
multiplicative convolution on norm-dependent tests, and the trace.
The smooth-test statement is primary-source normalization; extension to
Suzuki's tents is the already-proved Round-001 Weil/tent identity.

The CCM radical is a space of **tests**:

\[
 V=\left\{u\mapsto\sum_{q\in\mathbb Q^\times}\xi(qu):
       \xi\in\mathcal S(\mathbb A)_0\right\},
 \quad
 \mathcal S(\mathbb A)_0=\{\xi:\xi(0)=\int\xi=0\}.
\]

For `v in V`, convolution by `v` acts as zero on the quotient. Consequently
changing `f` to `f+v` preserves the trace pairing.

By contrast, the proposed common-mode operation changes the **functional**:

\[
 W\longmapsto W+2c\delta_0,
 \qquad
 \Psi(t)\longmapsto\Psi(t)+c|t|.
\]

Adding a radical test to a representative is not adding an identity
functional to the trace. These operations live in different spaces. The
notes supply no map interchanging them while preserving the pairing.

There is an even sharper diagnostic. If `delta_1` is regarded instead as a
convolution multiplier, it is the identity operator, since
`delta_1 star f=f`. It cannot act as zero on a nonzero primitive quotient.
Nor is that delta distribution an element of the Schwartz test space `V`.
This distinction does not depend on RH.

## 3. Identity, degree, and Brownian energy are different

For `Delta_t(x)=(t-|x|)_+/2`, the identity evaluation is indeed

\[
 2c\delta_0(\Delta_t)=ct.
\]

That exact identity survives the audit. But degree/codegree in the actual
trace formula pull back through `J` to

\[
 \widehat{J\phi}(0)=\int e^{-x/2}\phi(x)\,dx,
 \qquad
 \widehat{J\phi}(1)=\int e^{x/2}\phi(x)\,dx.
\]

Integrating the tent gives, independently,

\[
 \int_{-t}^{t}\Delta_t(x)e^{x/2}\,dx
 =4(\cosh(t/2)-1),
\]

and hence their sum is

\[
 8(\cosh(t/2)-1)
 =4(e^{t/2}+e^{-t/2}-2).
\]

This is Suzuki's smooth pole term, not `ct`. On general tests the
functionals are visibly independent: a nonnegative nonzero test supported
away from zero has zero identity evaluation but positive degree terms.
The identity term in the explicit trace formula is separately associated
with the differential/discriminant normalization (CCM Theorem 6.1 and
§7.1); calling it a degree radical suppresses this distinction.

**New elementary obstruction: no pairing-preserving nulling of the common
mode.** For positive times,

\[
 K_{|\cdot|}(s,u)=2\min(s,u).
\]

Already `K_(|.|)(1,1)=2`. At times `1,2` the matrix is
`[[2,2],[2,4]]`, with positive determinant `4`. Therefore a linear map
which sends `|t|` to a radical class, and whose pulled-back pairing equals
the Suzuki screw pairing on a space including that mode, cannot exist:
the former forces this pairing to vanish and the latter does not.

This refutes exactly a **pairing-preserving** identification of the mode
with a radical. A nonlinear construction on completed classes with a
separately proved positive lift is a different, still unpaid proposal.

## 4. The quotient image of the CND cone is not an order

This strengthens the generic warning about quotient positivity. Let
`ell=log p`, `r=p^(-1/2)`, and let `h_p` be the complete prime tower.
Round 002 gives the sharp CND lifts

\[
 -h_p+\frac{\ell r}{1-r}|t|,\qquad
 h_p+\frac{\ell r}{1+r}|t|.
\]

For completeness the second lift has spectral numerator, with
`c=cos(ell s)`,

\[
 \frac{\ell r}{1+r}
 +\ell\frac{rc-r^2}{1-2rc+r^2}
 =\frac{\ell r(1-r)(1+c)}{(1+r)(1-2rc+r^2)}\ge0.
\]

Its division by `pi s^2` is a positive Lévy density. The first lift is
Round 002's explicit interval Gram representation.

Let `q` quotient even normalized functions by `R|t|`. Then both
`q(h_p)` and `-q(h_p)` belong to `q(CND)`, and `q(h_p) != 0`: the tower
vanishes before `log p` but not afterward, so it is not linear in `|t|`.
Thus `q(CND)` contains a nontrivial line and is **not a pointed cone**.
A positive representative of each prime class therefore does not define
an antisymmetric order capable of paying the completed Brownian debt.
The finite-lift cost/topology must remain part of the problem.

## 5. What matches the semilocal construction exactly

The ratio in the notes agrees with the primary finite local factor:

\[
 \rho_p(1/2+is)=\frac{1-re^{i\ell s}}{1-re^{-i\ell s}},
 \quad
 P_p(s):=\frac i2\partial_s\log\rho_p
 =\ell\sum_{k\ge1}r^k\cos(k\ell s).
\]

Differentiating the absolutely convergent logarithmic series justifies
this formula. `M_p=P_p(0)`, and the repaired Lévy density is exactly

\[
 \nu_p(ds)=\frac{M_p-P_p(s)}{\pi s^2}\,ds.
\]

That is a real scalar bridge. It is not a map from the interval Gram
vectors into a Sonin space, and it is not a trace identity for `K_Dp`.
Indeed `D_p` is CND while its individual `rho_p` is not quasi-inner;
the two positivity/compactness notions are already distinct locally.

The canonical semilocal map on Mellin coordinates is multiplication by

\[
 m_F(s)=\prod_{p\in F}(1-p^{-1/2-is}).
\]

In the notation of CCM equation (57),

\[
 U_F\theta_F f=m_F U_\infty f.
\]

Its composition with their entire-function transform gives their
commuting square (59); it is a comparison of Hilbertian spaces, not a
claim that their norms coincide. The exact one-prime metric discrepancy
is

\[
 \|\theta_{\{p\}}f\|^2-\|f\|^2
 =\int_{\mathbb R}
   [r^2-2r\cos(\ell s)]\,|U_\infty f(s)|^2\,ds.
\]

The bracket changes sign. It is not `M_p-P_p(s)`, which is nonnegative.
As quadratic forms on the full ambient Mellin space, these are not the
same energy; the canonical ambient embedding has an indefinite norm
increment. This does not decide the sign on every restricted Sonin
subspace or after an unspecified choice of test vectors. A map into that
subspace, cross terms, or a different metric would need an additional
theorem before identifying a tower Gram contribution.

**New normalization obstruction for this canonical ambient map.** On the
ambient Mellin `L^2` space,

\[
 \|m_F^{-1}\|_{L^\infty}
 =\prod_{p\in F}(1-p^{-1/2})^{-1}.
\]

Every factor has modulus at least `1-r`, and equality holds at `s=0`;
continuity makes that value an essential extremum. As `F` exhausts the
primes the product diverges, since
`-log(1-r)>=r>=1/p` and Euler's prime reciprocal sum diverges.
Thus these canonical ambient isomorphisms have no uniform inverse norm.
This is not a statement about an optimal alternative map or a sharp
bound on the restricted Sonin subspace.

## 6. Computation histories versus rational action arrows

The adelic transformation groupoid has arrows

\[
 (q,a):a\longrightarrow qa,
 \qquad (r,qa)\circ(q,a)=(rq,a).
\]

If `a != 0`, some component lies nontrivially in a field. Therefore
`qa=ra` implies `q=r`. Between any given reachable nonzero endpoints
there is at most one rational action arrow. At the zero adele the
isotropy group is `Q^times`; it is not a record of computations either.

Consequently the chains `a -> 2a -> 6a` and `a -> 3a -> 6a` compose to
the **same** arrow `(6,a)`. That arrow retains the prime valuations of
`6`, but it forgets operation order, inserted inverse loops, syntactic
parenthesization, successor work, and description length. A computation
path groupoid can retain these; its evaluation functor to the rational
action groupoid is generally not faithful. Any proposed comparison must
exhibit its kernel rather than equating the two groupoids.

The local idele with component `p^k` at `p` and `1` elsewhere has norm
`p^(-k)`, so it does survive the diagonal rational quotient. This correct
observation does not repair the loss of same-endpoint computation
history. Prime orbit data and arbitrary syntax are different invariants.

For a principal rational `p`, the place jets are `+log p` at infinity and
`-log p` at `p`. Their sum is zero but their squared Euclidean norm is
`2(log p)^2`. First-jet cancellation therefore does not itself make
higher energy null. Moreover the derivative of an individual twisted
character at `p^k` is `-k log(p)p^(-k/2)`; the required Suzuki weight
loses `k` through the `1/k` in the Euler logarithm, not through the
product formula alone.

## 7. Shifted-family boundary and the remaining arrow

Suzuki's equations (11.1)–(11.2) verify the note's shifted family and
weights `Lambda(n)n^(-1/2-omega)`. Differentiation gives the claimed
second-derivative identity on `t>0`, including event jumps. His §11
supports CND at `omega=1/2`, as well as the stated nonnegativity for
larger shifts. These facts do not invert the shift to `omega=0`.

An ordinary Fourier/Poisson-convolution statement about the unshifted
accelerant additionally needs a declared distribution class and origin
normalization. `Psi` is not unconditionally known to have polynomial
growth. One must not silently Fourier-transform it as a tempered
function; such growth is itself proof-bearing. This caution does not
invalidate the elementary Laplace-domain semigroup identity.

The remaining useful adelic assertion would be an independently
positive, arithmetic construction whose pullback is
`K_(Psi+c_L|.|)` on each finite horizon, with a uniform finite bound on
`c_L`. Neither radical vanishing, finite quasi-innerness, nor the known
Sonin embeddings supplies this assertion. It is still an RH-equivalent
uniform lift target, not a reduction.

The next distinguishing probe is therefore concrete: propose an explicit
one-prime-plus-infinity test-vector map and calculate its **entire** Gram
pullback and norm change. The canonical ambient map was tested here and fails
the unqualified local energy identification. Any replacement must state how its
metric discrepancy pays the common-mode coefficient before invoking an
inductive limit.

## 8. Reproducibility and scope

Run `python -m unittest tests.test_r3_adelic` from the repository root.
The tests check the exact tent integrals, Brownian non-null matrix,
quotient-cone algebra, local norm discrepancy, character bookkeeping,
and same-endpoint history collapse. The uniform-divergence result is an
analytic theorem; no finite prefix is used to infer it.

No historical note was overwritten in this audit. The theorem statuses
are: exact scalar scattering bridge **PROVED-IN-REPO**; direct
radical/pairing identification and canonical ambient embedding-energy
identification **REFUTED**; nonpointed quotient cone and canonical
ambient inverse-norm obstruction **NEW LEMMA PROVED THIS ROUND**;
positive uniform primitive lift **UNVERIFIED**.
