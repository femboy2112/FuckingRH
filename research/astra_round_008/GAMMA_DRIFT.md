# Gamma drift: exact ladder, finite-state boundary, and a coupled control

Status: the determinant constants and theorems below are proved; the
completed Weil square remains unpaid. No zero ordinates enter a definition.
These results do not restart the scalar-passivity program.

## 1. Spectral determinant, with its normalization retained

On `ell²(N_0)` let `H e_m=2m e_m`, with domain
`sum (2m)²|v_m|²<infinity`. For real `s>0`,

\[
Z(w;s)=\operatorname{Tr}(H+s)^{-w}
      =2^{-w}\zeta_H(w,s/2),\qquad \Re w>1.
\]

NIST DLMF [25.11.13](https://dlmf.nist.gov/25.11.E13) and
[25.11.18](https://dlmf.nist.gov/25.11.E18) state
`zeta_H(0,a)=1/2-a` and
`partial_w zeta_H(0,a)=log Gamma(a)-log(2*pi)/2`, initially `a>0`.
Differentiate **both** factors of `2^(-w) zeta_H(w,s/2)`:

\[
\boxed{D(s):=\det_\zeta(H+s)
=2^{1-s/2}\sqrt\pi\,/\Gamma(s/2).} \tag{G1}
\]

Holomorphy extends this equality first to `Re s>0` with compatible logarithms;
the reciprocal-Gamma expression then supplies its entire continuation.
In particular `D(2)=sqrt(pi)` and `s D(s+2)=D(s)`. The zeros of `D` are
simple at `0,-2,-4,...`. Omitting the `2^(-w)` derivative changes the answer
by a nonconstant exponential and changes the completed phase.

This confirms the side-branch constant. It does **not** construct an
arithmetic determinant whose quotient by `D` has a self-adjoint spectrum.
The algebraic identity

\[
\xi(s)=2^{-s/2}\pi^{(1-s)/2}s(s-1)\,\zeta(s)/D(s)
\]

is a re-expression of the classical completion, not such a construction.

Ordinary Fredholm and regularized determinants must not be interchanged.
`(H+s_0)^(-1)` is Hilbert–Schmidt but not trace class. For `s_0>0`, the
convergent product defining `det_2` gives

\[
\det_2\!\left(I+(s-s_0)(H+s_0)^{-1}\right)
=\frac{\Gamma(s_0/2)}{\Gamma(s/2)}
 \exp\!\left(\frac{s-s_0}{2}\psi(s_0/2)\right). \tag{G2}
\]

Indeed each factor is `(1+(s-s0)/(2m+s0))*exp(-(s-s0)/(2m+s0))`;
its logarithm is summable quadratically, and differentiating the product
gives `(-psi(s/2)+psi(s0/2))/2`, with value one at `s=s0`.
The ratio `D(s)/D(s0)` differs from (G2) by the explicit linear exponential.
That normalization cannot be dropped because it leaves zeros unchanged.

## 2. The heat channel and its finite positive approximants

For `u>0`,

\[
\operatorname{Tr}e^{-uH}=\frac1{1-e^{-2u}},\qquad
k(u):=\operatorname{Tr}e^{-u(H+1/2)}
 =\frac{e^{-u/2}}{1-e^{-2u}}.
\]

For `Re s,Re s0>0`, the resolvent **difference** is trace class and

\[
\begin{aligned}
\operatorname{Tr}[(H+s)^{-1}-(H+s_0)^{-1}]
&=\int_0^\infty\frac{e^{-su}-e^{-s_0u}}{1-e^{-2u}}\,du\\
&=\tfrac12\{\psi(s_0/2)-\psi(s/2)\}.
\end{aligned} \tag{G3}
\]

Near zero the numerator removes the heat singularity; at infinity both
exponentials decay. Equivalently each summand is `O(m^(-2))`, uniformly on
compact parameter sets avoiding poles. This proves interchange and local
holomorphy. The individual resolvent traces diverge. In particular neither
`psi(s/2)/2` nor its zeta-regularized trace is automatically positive-real.
The retained Round007 counterexample is `psi(1)/2=-gamma/2<0`.

Let `lambda_m=2m+1/2`, `k_M(u)=sum_(m<M) exp(-lambda_m u)`.
On the common test space `C_c^infinity(R)` define the genuine positive form

\[
E_{\Gamma,M}(f)=\int_0^\infty k_M(u)
                  \|\tau_u f-f\|_2^2\,du.
\]

With `hat f(v)=integral f(x)exp(ivx)dx`, its multiplier is

\[
g_M(v)=\sum_{m<M}\frac{2v^2}{\lambda_m(\lambda_m^2+v^2)}.
\]

This follows by integrating `2 exp(-lambda*u)(1-cos(v*u))`. The digamma
difference integral [DLMF 5.9.16](https://dlmf.nist.gov/5.9.E16) yields

\[
g(v)=\lim_Mg_M(v)
 =\Re\psi(1/4+iv/2)-\psi(1/4)\ge0. \tag{G4}
\]

The convergence is monotone at the form level, and a quantitative estimate
independent of arithmetic is

\[
0\le g(v)-g_M(v)
\le 2v^2\left(\lambda_M^{-3}+\frac1{4\lambda_M^2}\right).
\]

To prove it, bound each omitted term by `2v²/lambda_m³` and apply the
integral test with step two. Consequently

\[
0\le E_\Gamma(f)-E_{\Gamma,M}(f)
\le\left(2\lambda_M^{-3}+\frac1{2\lambda_M^2}\right)\|f'\|_2^2.
\tag{G5}
\]

Thus the Gamma difference channel really has controlled positive finite-mode
approximants. It supplies exactly the Round007 channel, **including the
same unresolved debit** `c0=psi(1/4)-log(pi)<0`. It does not remove that debit.
For indicators its variogram is explicitly

\[
G_M(t)=\sum_{m<M}\frac{1-e^{-\lambda_m|t|}}{\lambda_m^2},\qquad
\langle D_{\Gamma,M}I_t,D_{\Gamma,M}I_u\rangle
=G_M(t)+G_M(u)-G_M(t-u)
\]

for `I_t=1_[0,t]`, `t>=0`. This last identity follows by polarizing the
translation-invariant energy and `||tau_a I_t-I_t||²=2 min(a,t)`.

## 3. A sharp, restricted finite-state theorem

**Theorem G-LTI.** No fixed-dimensional linear time-invariant state-space
realization with finite matrices and ordinary linear input/output can have
the exact Gamma/digamma transfer on an open analytic set, or heat impulse
response `h(u)=1/(1-e^(-2u))` on an open interval of positive time. No finite number
of ladder modes has the full heat pairing.

There are two independent proofs.

1. A finite-dimensional transfer `D+C(sI-A)^(-1)B` is rational, by the
   adjugate formula. Digamma and Gamma have infinitely many distinct poles;
   equality on an open analytic set would extend meromorphically and is
   impossible. The reciprocal Gamma determinant likewise has infinitely
   many zeros and is not a nonzero rational function.
2. A finite-dimensional impulse `Ce^(uA)B` has time-Hankel matrices
   `h(t_i+t_j)=Ce^(t_i A)e^(t_j A)B` of rank at most `dim A`. But for any
   distinct positive `t_1,...,t_n`, setting `x_i=e^(-2t_i)` gives

   \[
   h(t_i+t_j)=\sum_{m\ge0}x_i^m x_j^m=\frac1{1-x_ix_j}.
   \]

   The first `n` columns `1,x,...,x^(n-1)` form an invertible Vandermonde
   matrix. Their Gram is strictly positive definite, so the full Gram has
   rank `n`. Since `n` is arbitrary, its Hankel rank is infinite. The
   shifted kernel `k(t+u)` is a positive diagonal congruence and has the
   same conclusion. An `M`-mode cutoff has exact rank `min(M,n)`.

The Hankel proof applies on every nonempty positive time interval by taking
distinct `t_i` in a sufficiently small interval whose pairwise sums lie in
the prescribed interval. A feedthrough distribution at time zero changes
none of these matrices.

**Scope matters.** This does not exclude nonlinear state updates, rational
recurrences in a changing parameter, matrix coefficients that already
contain transcendental functions, time-varying ODEs, or an infinite channel
with two boundary ports. In particular define

\[
\theta'(t)=\tfrac12\Re\psi(1/4+it/2)-\tfrac12\log\pi.
\]

Then the `2x2` rotation ODE
`M'=theta'(t)*[[0,-1],[1,0]]*M` exactly propagates the Gamma phase. It
inputs the entire digamma function in its coefficient and does not realize
that function with a two-state LTI system. A claim excluding this ODE by
counting Gamma poles would be false. Likewise G-LTI says nothing against
the one-variable functional recurrence `Gamma(z+1)=z Gamma(z)`.
Also `theta'(0)=(psi(1/4)-log(pi))/2<0`: the phase is not a globally
increasing clock merely because its eventual asymptotic slope is positive.

## 4. Continuum oscillator realization; it is not the dilation generator

On `L²(R,dx)` take the harmonic oscillator

\[
H_{\rm osc}=-\partial_x^2+x^2-1
           =(-\partial_x+x)(\partial_x+x).
\]

Normalized Hermite functions give an orthonormal eigenbasis with eigenvalues
`2m`, so this operator is unitarily equivalent to the ladder in (G1).
Explicitly, `A=partial_x+x` kills `psi_0=pi^(-1/4)exp(-x²/2)`,
`[A,A*]=2`, and `psi_m=(A*)^m psi_0/sqrt(2^m m!)` satisfies
`A*A psi_m=2m psi_m`; Hermite completeness supplies the entire space.
This is a concrete continuous free Gamma channel, constructed from the
Gaussian oscillator without zero ordinates. Its positive heat kernel is
the Mehler kernel ([DLMF 18.18.28](https://dlmf.nist.gov/18.18.E28)).
The frequency/units choice is explicit: replacing `H` by `b H/2` gives
the ladder `b m` and determinant
`b^(1/2-s/b)*sqrt(2*pi)/Gamma(s/b)`. The exact arithmetic Gamma factor
selects `b=2`; bare affine symmetry does not select that scale.

It is **not** unitarily equivalent to the real-affine dilation generator:
the oscillator has compact resolvent and discrete spectrum, whereas on
each half-line dilation becomes `-i partial_u`, with continuous spectrum
`R`. A Gamma Mellin integral does not identify these two generators.

## 5. Clock coupling that can actually be calculated

Let `C_L` be a finite residue clock. If every event acts on the clock alone
and the drift is `I tensor exp(-u Hosc)`, they commute. Every hybrid product
then factors as `clock product tensor exp(-T Hosc)`, even when the clock
maps change dimension. This is a tensor-factorization theorem, not a
Weil-positivity theorem: merely placing Gamma on a tensor factor does not
create an interaction.

There is a concrete noncommuting control from Euclidean division, requiring
no fitted entries. On `C^L tensor L²(R)`, put

\[
U_L(|r\rangle\otimes f)=
\begin{cases}|r+1\rangle\otimes f,&r<L-1,\\
|0\rangle\otimes\tau_1f,&r=L-1.
\end{cases}
\]

Its integer skeleton is exactly `(r,m) -> (r+1 mod L,
m+1_(r=L-1))`, the carry of `Lm+r -> Lm+r+1`. Hence `U_L` is unitary and
`U_L^L=I tensor tau_1`. The common Schwartz core gives

\[
[I\otimes H_{\rm osc},U_L]
 =|0\rangle\langle L-1|\otimes(2x-1)\tau_1. \tag{G6}
\]

Thus an oscillator really can interact with the residue boundary rather
than just multiply a scalar determinant afterward. The interaction is a
domain-sensitive unbounded commutator, not a finite scalar phase.
Continuizing the quotient coordinate and placing a fixed oscillator on
that coordinate are explicit choices of this control; their compatibility
with all LCM refinements is not assumed.

Its heat/return trace is also exact:

\[
\boxed{\operatorname{Tr}[(I\otimes e^{-tH_{\rm osc}})U_L^k]
=\begin{cases}
0,&L\nmid k,\\[1mm]
\displaystyle\frac{L}{1-e^{-2t}}
 \exp\!\left(-\frac{(k/L)^2}{4}\coth t\right),&L\mid k,
\end{cases}\quad t>0.} \tag{G7}
\]

If `L` does not divide `k`, the clock has no diagonal entries. Otherwise
reduce to `L Tr(e^(-tHosc) tau_(k/L))`. Insert the Mehler kernel and complete
the square; the integral is
`(1-e^(-2t))^(-1) exp(-a² coth(t)/4)`. All products are trace class since
the heat operator is trace class and the carry is bounded.

This is a genuine coupled trace, but its universal formula is Gaussian
return data of an ordinary clock of length `L`. It has no von-Mangoldt
coefficient or `log p` roof derived from it. Choosing `L=LCM(1,...,N)`
does not by itself change that fact. No refinement-compatible oscillator
interaction, completed Weil pairing, or trivial-mode contractible complex
has been derived from (G6). Those arrows remain UNVERIFIED.

The optional positive operator
`I tensor Hosc + g(2I-U_L-U_L*)`, `g>=0`, is self-adjoint on the oscillator
domain by bounded perturbation and is nonnegative. Its positivity does not
identify its compressed form with Weil. Varying `g` is a real extra choice,
not a normalization secretly fixed by the arithmetic clock.

## 6. Divisor cancellation and verdict

The classical functional equation and Gamma poles imply simple trivial
zeros at `s=-2m`, `m>=1`. The residues of `zeta'/zeta` and
`psi(s/2)/2` there are `+1` and `-1`. At zero, `zeta(0)=-1/2` is nonzero;
the explicit `s` cancels the Gamma pole. At one, `s-1` cancels the zeta
pole. This divisor cancellation is exact, but no canonical differential
between two independently constructed spectral sectors has been supplied.
The signed causal-history formula in the side branch is likewise correct
with its basepoint subtraction; it is not a positive measure theorem.

**Result:** exact infinite-place drift and a sharp finite-LTI obstruction
are available. The coupled carry/oscillator control demonstrates that
noncommutation itself is easy and still fails to supply the required
prime/Gamma pairing. The next burden is the exact mixed pairing, not
another regularization constant or a smaller matrix fitted to the phase.

Reproduce `python -m unittest tests.test_round008_gamma -v` and
`python -m scripts.round008_gamma --output research/astra_round_008/evidence/gamma.json`.
Ten tests use exact SymPy algebra and Arb balls. Universal rank and tail
claims are proved above; finite ranks are controls, not extrapolations.
