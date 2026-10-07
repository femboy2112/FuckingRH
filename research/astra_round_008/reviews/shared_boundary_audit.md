# Hostile audit: normalized shared-origin Gamma coupling

Status: the two proposed obstructions are valid with the scope qualifications
below. This review is a same-model, separate derivation, not an independent
source or proof of RH. No new external theorem is needed.

## 1. Required conventions

Let `L_0=1`, `L_j=p_j L_{j-1}`, and `d_j=L_j-L_{j-1}`. Embed all old clock
spaces isometrically into the normalized-Haar space `H_{L_m}`. Let `E_j` be
the mutually orthogonal lifted innovation projections. Write `L=L_m`.

The vector `e_0` must be the **unit** point mass in the orthonormal coordinate
basis. Every innovation projector is circulant and has rank `d_j`, hence

\[
 \|E_je_0\|^2=\langle e_0,E_je_0\rangle=d_j/L.
\]

Thus, with `c_j=sqrt(d_j/L)` and `v_j=E_j e_0/c_j`, the vectors `v_j` are
orthonormal and `Qv_j=c_j e_0` for `Q=|e_0><e_0|`. Also

\[
 \sum_{j=1}^m c_j^2=1-1/L.
\]

The formula below for `kappa` requires the **unshifted** ladder
`H_Gamma e_l=2l e_l`. If the intended ladder is `2l+1/2`, its scalar heat
expectation acquires the extra factor `exp(-h)`. The no-go conclusions survive,
but the displayed scalar formula must not mix those two conventions.

## 2. Exact contraction formula

Take `tau_a f(x)=f(x-a)`, `a_j=log q_j`,
`w_j=log(p_j)/sqrt(q_j)>0`, and the unit vector

\[
 g=\sqrt{1-r^2}\sum_{\ell\ge0}r^\ell e_\ell,
 \qquad 0<r<1.
\]

Define `X_j f=(tau_{a_j}-I)f` and

\[
 Vf=\sum_j\sqrt{w_j}\,v_j\otimes g\otimes X_jf,
 \qquad F_m=\sum_j c_j\sqrt{w_j}\,X_j.
\]

Tensor factors may be permuted consistently. The contraction
`B_h=exp(-h Q tensor H_Gamma) tensor I_time`, `h>=0`, obeys

\[
 B_h^*B_h=(I-Q)\otimes I+Q\otimes e^{-2hH_\Gamma},
\]

and therefore

\[
 \|B_hVf\|^2=\sum_j w_j\|X_jf\|^2-\kappa\|F_mf\|^2,
 \quad
 \kappa=1-\frac{1-r^2}{1-r^2e^{-4h}}.
\]

Here `0<=kappa<1`, and `kappa>0` if `h>0`. For fixed `r`, its limit as
`h->infinity` is `r^2`, not `1`. Adding an orthogonal Gamma difference
channel adds its exact positive energy without changing this calculation.

This is a genuine positive square; the subtraction is its internal cross
term. The audit does not challenge that positivity. It challenges equality
to the completed Weil form.

## 3. Finite obstruction: a forbidden ratio atom

Put `b_j=c_j sqrt(w_j)>0` and `A=sum_j b_j`. Expansion gives

\[
 F_m^*F_m=
 \sum_{i,j}b_i b_j\tau_{a_j-a_i}
 -A\sum_jb_j(\tau_{a_j}+\tau_{-a_j})+A^2I.
\]

Once the events `q=2` and `q=3` have appeared, the coefficient of
`tau_{log(3/2)}` in the correction `-kappa F_m^*F_m` is exactly

\[
 -\kappa c_2 c_3\sqrt{w_2w_3}<0.
\]

There is no competing pair of prime powers with this ratio. Indeed, if
`v/u=3/2` and both `u,v` are positive prime powers, the valuations at `2`
and `3` force `u=2`, `v=3`. Neither a single event shift nor the identity
has shift `log(3/2)`. The reversed pair supplies the conjugate negative shift.

For the first two refinements, `L=6`, `d_1=1`, `d_2=4`, so
`c_2 c_3=1/3`; this is a convenient independent normalization check.

The exact Weil prime distribution has atoms at the signed logarithms of
integer prime powers, not at `log(3/2)`. Its Gamma kernel is a smooth density
in a neighborhood of this nonzero shift; its pole kernel is smooth there as
well. They cannot cancel a nonzero delta distribution.

**Test-class qualification.** The discrepancy is visible on all compact
smooth tests, or on a fixed interval whose width is **strictly greater**
than `log(3/2)`. It need not be visible on a smaller fixed window. To prove
visibility without relying on a drawing of distributional support, polarize
the forms and take two `L^2`-normalized smooth bumps of width `epsilon`
separated by `log(3/2)`. The indicated translation pairs them with a fixed
nonzero limit; kernels smooth near that difference contribute `O(epsilon)`.
At a fixed finite horizon, all other distinct shift atoms can be avoided by
taking sufficiently small `epsilon`. Polarization recovers this mixed
pairing from the quadratic form.

**Limit qualification.** This proves failure of exact finite equality when
`h>0`, not failure of convergence by itself. The coefficient of this atom
tends to zero in the construction. The separate operator-norm theorem below
is essential.

## 4. The entire correction vanishes in operator norm

For `j<=m`,

\[
 c_j^2=
 \frac{1-1/p_j}{p_{j+1}\cdots p_m}
 \le 2^{-(m-j)}.
\]

Along the increasing sequence of prime-power events, `q_j->infinity` and

\[
 0<w_j\le\frac{\log q_j}{\sqrt{q_j}}\longrightarrow0.
\]

Set `a_m=sum_{j<=m} c_j sqrt(w_j)`. The geometric-convolution bound gives

\[
 a_m\le\sum_{j=1}^m2^{-(m-j)/2}\sqrt{w_j}\longrightarrow0.
\]

For completeness, split the sum at a fixed `J`. Each of its finitely many
old terms tends to zero. The tail is at most
`sup_{j>J} sqrt(w_j)/(1-2^{-1/2})`, which tends to zero as `J->infinity`.
This proves convergence without exchanging an uncontrolled infinite sum.

Since translations are unitary,

\[
 \|F_m\|\le2a_m,
 \qquad
 \|\kappa F_m^*F_m\|\le4a_m^2\longrightarrow0.
\]

The bound is uniform over all `h>=0` and all `0<r<1`, including parameters
depending on the horizon. No prime number theorem or zero information is
used.

## 5. Why the vanishing correction cannot supply completion

Fix a nonzero compact smooth test `f`, with support diameter `R`. For all
events with `log q_j>R`, the translate and original have disjoint supports,
so `||X_jf||^2=2||f||^2`. Consequently

\[
 \sum_{j\le m}w_j\|X_jf\|^2
 =2S_m\|f\|^2+C_f,
 \qquad S_m=\sum_{j\le m}w_j,
\]

once the horizon contains all events up to `exp(R)`. The quantity `C_f` is
then independent of the horizon. Moreover `S_m->infinity`: it already
dominates a constant-tail portion of `sum_p 1/p`, whose divergence follows
from Euler's product and divergence of the harmonic series. This elementary
fact is much weaker than RH or the PNT.

The exact orthogonal Gamma energy is fixed and finite on this `f`, while
the shared-origin correction tends to zero. The proposed squared form
therefore tends to `+infinity`, not to the finite completed Weil form.

Equivalently, the Round007 completion residual contains the bulk debit
`-2S_m I` (plus the fixed Archimedean scalar and pole terms); an operator
tending to zero in norm cannot supply it. This is a discrepancy of the
candidate square, not a negative value or disproof of the target form.

## 6. Scope of the boundary-metric extension

A precise sufficient hypothesis is a boundary metric of the form

\[
 G_m=(I-Q)\otimes I+Q\otimes T_m,
\]

on clock times ladder, with time left unchanged. On the event input above,
the energy change is

\[
 (\langle g,T_mg\rangle-1)\,\|F_mf\|^2.
\]

If the scalar expectations are uniformly bounded, this change tends to zero
in operator norm. The same conclusion holds for a uniformly bounded
operator-valued defect on the time factor, provided it is inserted only
through this single shared-origin projection.

There is also a useful strengthening for positive metrics: whenever
`T_m>=0` and its quadratic form is finite on `g`, the possible energy
**reduction** is at most `||F_mf||^2`, even if `||T_m||` is not uniformly
bounded. Thus arbitrary positive amplification within this one boundary
sector still cannot remove the diverging debit. This follows simply by
discarding the nonnegative `Q`-sector energy and retaining the unchanged
`I-Q` sector.

The hypothesis that the complementary clock sector is unchanged is
load-bearing. This result does **not** cover metrics mixing `Q` with its
complement, a growing collection of boundary projections, an event-dependent
time operator, or a nonlocal interaction whose event-pair matrix is not
factored through the overlaps `c_i c_j`. Those are genuine changes of class,
not counterexamples to this theorem.

## Verdict

The proposed heat coupling is ruled out as an exact finite Weil square and
as a convergent Weil completion. Its general one-origin positive-metric
extension also cannot pay the bulk debit. No universal obstruction to
nonlocal, continuum, event-dependent couplings has been proved here.

## 7. Extension to a bounded number of normalized clock sites

Let `mathcal F_m` denote a set of `R_m` distinct clock sites, and put
`a_m=sum_j c_j sqrt(w_j)` as before. Set

\[
 Q_{\mathcal F_m}=\sum_{x\in\mathcal F_m}|e_x\rangle\langle e_x|.
\]

For every normalized coordinate point state `e_x`, the constant diagonal
of `E_j` and Cauchy--Schwarz in its range give

\[
 |\langle e_x,v_j\rangle|
 =\frac{|\langle E_je_x,E_je_0\rangle|}{c_j}
 \le\frac{(d_j/L)}{\sqrt{d_j/L}}=c_j.
\]

Consequently, using orthogonality of the distinct coordinate point states,

\[
 \|(Q_{\mathcal F_m}\otimes I)Vf\|^2
 =\sum_{x\in\mathcal F_m}
 \left\|\sum_j\sqrt{w_j}\langle e_x,v_j\rangle
                 g\otimes X_jf\right\|^2
 \le4R_m a_m^2\|f\|^2.
\]

This estimate is uniform in the choice of the sites, including choices
depending on the horizon. No random-site averaging is assumed.

Consider any positive boundary metric that is **block diagonal** with
respect to this boundary/complement decomposition,

\[
 G_m=(I-Q_{\mathcal F_m})\otimes I+T_m,
 \qquad T_m\ge0,\quad
 T_m=(Q_{\mathcal F_m}\otimes I)T_m(Q_{\mathcal F_m}\otimes I).
\]

The positive block `T_m` may mix the selected sites, the Gamma ladder, and
the entire time continuum. It may be unbounded, with its quadratic-form
domain containing the input under consideration. It cannot reduce energy
by more than the discarded boundary mass:

\[
 \langle Vf,G_mVf\rangle
 \ge\|Vf\|^2-4R_m a_m^2\|f\|^2.
\]

Thus if `sup_m R_m<infinity`, the possible reduction tends to zero. The
complete square with the unchanged orthogonal Gamma channel still diverges
on every fixed nonzero compact smooth test, so this entire class of
bounded-number-of-clock-sites repairs fails.

For a growing number of sites, matching the fixed completed Weil form on
such a test requires

\[
 4R_m a_m^2\ge 2S_m-C_f-o(1),
\]

for a finite test-dependent constant `C_f`. This is a **necessary capacity
condition only**. It neither constructs a successful growing boundary nor
proves its sufficiency. In particular, `a_m->0` and `S_m->infinity` force
the required number of coordinate sites to diverge. No asymptotic rate in
the carrier horizon is claimed without an additional estimate for `a_m`.

Two limitations are essential:

1. These are normalized **coordinate point states**, not arbitrary
   low-rank clock vectors. A rank-one vector aligned with the event image
   need not obey the overlap bound `c_j`.
2. The unchanged complement is meant in the operator/form block-diagonal
   sense above. It is not enough that its diagonal compression remains the
   identity. For example, on a complement/boundary two-dimensional split,
   the positive matrix
   \[
   \begin{pmatrix}1&-1/\epsilon\\-1/\epsilon&1/\epsilon^2\end{pmatrix}
   \]
   annihilates `(1,epsilon)` although its complement compression is `1`
   and the input's boundary mass is only `epsilon^2`. Arbitrary cross
   blocks, whether applied once or repeatedly, are outside this theorem.

## 8. Cross blocks: a necessary gain bound

Cross blocks can be included with an explicit operator-gain hypothesis.
Decompose the lifted event vector into complement and boundary components

\[
 Vf=u_m\oplus v_m,
 \qquad v_m=(Q_{\mathcal F_m}\otimes I)Vf.
\]

Consider a positive metric, now genuinely allowing off-diagonal coupling,

\[
 G_m=\begin{pmatrix}I&B_m\\B_m^*&T_m\end{pmatrix}.
\]

Assume `B_m` is bounded as an operator from boundary to complement at each
finite horizon. Its norm may depend on the horizon. The boundary block may
be an unbounded quadratic form, with `T_m>=B_m^* B_m` on its form domain
and the input boundary vector in that domain. Equivalently, this is the
Schur-complement positivity condition with the complement block fixed
exactly at the identity. Then

\[
 \begin{aligned}
 q_m[f]
 &=\|u_m+B_mv_m\|^2+
       \langle v_m,(T_m-B_m^*B_m)v_m\rangle\\
 &\ge\bigl(\|u_m\|-\|B_m\|\,\|v_m\|\bigr)_+^2.
 \end{aligned}
\]

The displayed identity is a quadratic-form identity if `T_m` is unbounded.
All estimates use the actual common domain, not a formal subtraction of
undefined expectations.

Put `E_m=||Vf||^2`, `beta_m=||B_m||`, and
`b_m=2 sqrt(R_m) a_m ||f||`. Orthogonality and the coordinate-site bound
yield the more general finite estimate

\[
 q_m[f]\ge
 \left(\sqrt{(E_m-b_m^2)_+}-\beta_m b_m\right)_+^2.
\]

For a fixed number `R>=1` of sites and a fixed nonzero compact smooth test,

\[
 E_m=2S_m\|f\|^2+O_f(1),
 \qquad b_m=2\sqrt R\,a_m\|f\|\longrightarrow0.
\]

Therefore uniformly bounded `beta_m` cannot keep `q_m[f]` finite: its lower
bound tends to infinity. Adding the unchanged orthogonal Gamma channel
cannot repair this divergence.

Conversely, any matching to a finite completed target on this fixed test
requires `q_m[f]=O_f(1)`. From the reverse triangle inequality and the
completed square above,

\[
 \beta_m\|v_m\|\ge\|u_m\|-\sqrt{q_m[f]}.
\]

Since `||u_m||^2=E_m-||v_m||^2`, this implies

\[
 \boxed{\quad
 2\sqrt R\,a_m\,\|B_m\|
 \ge\sqrt{2S_m}-O_f(1).
 \quad}
\]

Thus genuine cross coupling through finitely many coordinate sites needs
an unbounded operator gain of at least this order. This condition is
necessary, not sufficient: no coupling meeting the exact Weil identity is
constructed by imposing the bound.

The two-dimensional matrix in Section 7 calibrates the escape rather than
contradicting this result. There `u=1`, `v=epsilon`, `B=-1/epsilon`, and
`T=1/epsilon^2`. Its metric is positive and its energy vanishes, exactly
saturating `||B|| ||v||=||u||`. The price is unbounded gain as the boundary
component tends to zero.

This theorem allows arbitrary boundary/Gamma/time cross action through
`B_m` and `T_m` satisfying the stated operator assumptions. It does not
assert that an arbitrary sequence of interactions retains the identity
complement block; changing that block is another change of class. Nor does
it cover an unbounded `B_m` at a single finite horizon without a replacement
domain-specific estimate.
