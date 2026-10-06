# Exact Weil edge square and the bulk-deficit theorem

Status: exact identities and scoped obstruction proved here; RH OPEN.
This extends the earlier Brownian rank obstruction to the completed form on
arbitrary tests and determines the sharp scalar cost in the stated edge class.
It is not an external novelty claim or a no-go for all nonlocal operators.

## 1. Exact target and domain

Use Fourier transform `hat f(v)=integral f(x) exp(ivx) dx`,
`tilde f(x)=conj(f(-x))`, and `F=f*tilde f`. Initially `f in C_c^infinity(R)`.
For `supp(f)` contained in an interval of length `L=log N`, put
`a_n=log n`, `w_n=Lambda(n)/sqrt n`, `S_N=sum_(n<=N) w_n`.
Suzuki v4, §3.2 and (5.15), gives the centered arithmetic functional

\[
\mathcal W(f)=W(F)=2\Re(\ell_+(f)\overline{\ell_-(f)})
-2\sum_{n\le N}w_n\Re F(a_n)
+\frac1{2\pi}\int_{\mathbb R}|\widehat f(v)|^2
 [\Re\psi(1/4+iv/2)-\log\pi],dv,
\]
where `ell_+(f)=integral f(x)e^(x/2)dx`, `ell_-(f)=integral f(x)e^(-x/2)dx`.
The pole term is a **cross product**, not two absolute-value squares:
`hat F(i/2)=hat f(i/2) conj(hat f(-i/2))`.
No zeros are needed to define or evaluate the displayed expression.
The primary-source theorem is RH iff this is nonnegative for every such test.

## 2. Derive the positive infinite-place difference channel

Set
\[
c_0=\psi(1/4)-\log\pi
=-\gamma-\pi/2-3\log2-\log\pi<0,\qquad
k(u)=\frac{e^{-u/2}}{1-e^{-2u}}.
\]
The digamma difference integral (NIST DLMF 5.9.16, with variable `2u`) gives
\[
\Re\psi(1/4+iv/2)-\psi(1/4)
=2\int_0^\infty k(u)(1-\cos vu),du.
\]
Let `tau_u f(x)=f(x-u)`. Plancherel and Tonelli yield
\[
\frac1{2\pi}\int|\widehat f|^2
 [\Re\psi(1/4+iv/2)-\log\pi]
=c_0\|f\|_2^2+\int_0^\infty k(u)\|\tau_u f-f\|_2^2,du.
\]
Here `k(u)~1/(2u)` at zero, while `||tau_u f-f||_2<=u||f'||_2`;
at infinity `k` decays exponentially. Every integral is finite. The first-order
Gamma channel is `D_Gamma f(u,x)=sqrt(k(u))(f(x-u)-f(x))`.
It is a closed operator on its natural finite-energy domain: translations
are bounded, and convergence in the graph identifies its pointwise-in-u
L2 limits. Its squared Fourier multiplier is the nonnegative digamma
**difference**, not the parent's incorrectly named passive scalar digamma.

## 3. Couple orientations before squaring

The logarithmic image of multiplicative dilation is `tau_(log n)`.
For each visible prime-power event the two-endpoint oriented channel is
\[
D_n f=\sqrt{w_n}(\tau_{a_n}f-f).
\]
Its cross term is exactly the required negative prime correlation:
\[
\|D_nf\|^2=2w_n\|f\|^2-2w_n\Re F(a_n).
\]
Thus this construction retains orientation and makes subtraction internal
to each square. It is not a fitted square root of the target.
Include the continuous Gamma channel **before** the limit and define
\[
D_Nf=(D_\Gamma f,(D_nf)_{n\le N}),\qquad E_N(f)=\|D_Nf\|^2.
\]
The block operator `[[0,D_N*],[D_N,0]]` is self-adjoint on
`Dom(D_N) direct-sum Dom(D_N*)`, odd under the domain/codomain grading.
The carrier restriction is `n<=N`, not complete independent towers.
This is a continuous test-space lift of the visible event geometry. It
escapes the fixed sampling obstruction, but uses continuum translations;
it is not claimed to be a new exact SUCC-coupled operator.

Direct substitution proves the exact identity
\[
\boxed{\mathcal W(f)=E_N(f)+(c_0-2S_N)\|f\|^2
+2\Re(\ell_+f\,\overline{\ell_-f}).} \tag{1}
\]
The residual is fully classified: a negative scalar multiple of the
identity on the test interval, plus the pole form of rank at most two.

## 4. Bulk-deficit obstruction

**Theorem.** On any nondegenerate bounded interval `I` of length at most
`log N`, the residual in (1) has an infinite-dimensional negative subspace.
It cannot be an additional positive square, a finite-rank correction, or a
correction supported only at finitely many boundary degrees of freedom.

**Proof.** The common kernel of `ell_+` and `ell_-` has codimension at most
two in `L2(I)` and contains infinitely many smooth compactly supported tests.
On it the residual is exactly `(c_0-2S_N)||f||²<0`. The same conclusion
survives imposing finitely many additional linear boundary conditions.
As an operator on `L2(I)`, its essential spectrum is the singleton
`{c_0-2S_N}`; the pole part is finite rank. Thus its distance in operator
norm to finite-rank operators is at least `2S_N-c_0`. QED.

Using ordinary PNT and partial summation, `S_N~2sqrt(N)`. Consequently the
required bulk correction grows like `4sqrt(N)` in this convention. This
asymptotic is not needed for the finite/infinite-rank obstruction. There is
no RH-strength prime-error estimate here.

A finite-rank coupling of a previously fixed `D_N` changes its quadratic
form by finite rank when the cross terms extend boundedly on `L2(I)`.
That entire class is excluded. A continuous boundary trace can have infinite
rank; it is **not** excluded merely because it is called a boundary sector.
Arbitrary coherent infinite-dimensional corrections remain outside the theorem.

## 5. Sharp minimal scalar cost of the prime cross terms

For a single global two-endpoint channel `Af=v f+z tau_a f` in a Hilbert
channel, matching the coefficient `-2w Re F(a)` requires
`<v,z>=-w` (with the appropriate conjugation convention). Cauchy–Schwarz gives
\[
\|v\|^2+\|z\|^2\ge2|\langle v,z\rangle|=2w.
\]
Equality holds for `z=-v`, `||v||²=w`: precisely the difference channel.
Thus independent oriented event channels already incur the least possible
norm cost. Rescaling their two endpoints cannot lower (1)'s debit.

More generally, suppose a **globally** positive translation-invariant square
has continuous multiplier
\[
m(v)=g_\Gamma(v)+d-2\sum_{n\le N}w_n\cos(a_nv),
\quad g_\Gamma(v)=\Re\psi(1/4+iv/2)-\psi(1/4).
\]
Continuity and positivity on all tests force `m(0)>=0`, hence `d>=2S_N`.
The difference-square construction attains equality, since `g_Gamma>=0`.
This covers coherent translation filters if all unwanted difference
frequencies cancel and the stated Gamma multiplier is retained.

**Quantifier boundary:** positivity only on one fixed compact support window
does not imply pointwise multiplier positivity, and is not covered by this
last lower bound. There is no illicit constant-function eigenvector on a
Dirichlet interval.

## 6. What would escape

A successful square must change the construction by an infinite-dimensional
coherent coupling that pays this bulk norm cost while retaining every exact
prime correlation and the full Gamma/pole functional. Finite-rank boundary
modes, better finite PSD fits, or merely preserving first-order orientation
cannot do that within the class just proved. No claim is made that the
needed nonlocal coupling is impossible or independently known.

Primary conventions: https://arxiv.org/pdf/2206.03682v4, §3.2 and (5.15);
https://dlmf.nist.gov/5.9.E16. Proof and constants were independently checked
against the earlier normalized repository convention and a bounded algebra audit.
