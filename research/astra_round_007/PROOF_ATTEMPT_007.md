# Proof attempt 007: the completed square and its unpaid bulk correction

**Verdict: RH not proved. A sharp obstruction to a specified family is proved.**
The program uses no zero ordinates and does not retry xi'/xi passivity.

## 1. Build, rather than assume, the square

The valuation graph supplies exact positive jet weights
`w_n=Lambda(n)/sqrt(n)`. In logarithmic test coordinates multiplication by n
becomes translation `tau_(log n)`. Keep its two endpoint orientations and set

    D_n f = sqrt(w_n) (tau_(log n) f-f),  n<=N.

The Archimedean digamma identity independently supplies

    D_Gamma f(u,x) = sqrt(e^(-u/2)/(1-e^(-2u))) (f(x-u)-f(x)).

Take their orthogonal sum D_N. It is a closed, explicitly defined
first-order operator with positive norm square. Its doubled operator is
self-adjoint on the stated graph domain. No matrix factorization or
target-positivity assumption has entered.

This continuum operator is the natural event-edge implementation of the
geometry, not a claim that SUCC has already selected its global metric.
The purely discrete, coherently coupled chiral operator C_2-B_jet was also
built. Its actual cross terms are affine carrier incidences; the missing
test-function map is addressed in Step 5.

## 2. Calculate all terms before claiming an identity

For any compact smooth test of support width at most log N, direct
polarization and the exact prime/Archimedean formula give

\[
\mathcal W(f)=\|D_Nf\|^2
 +(c_0-2S_N)\|f\|^2
 +2\Re(\ell_+f\,\overline{\ell_-f}),
\]

with `S_N=sum_(n<=N)w_n`, `c0=psi(1/4)-log pi<0`, and
`ell_±f=integral f(x)exp(±x/2)dx`. The negative prime correlations do occur
internally in the square. They cost exactly `2S_N||f||²` in diagonal norm.
The Gamma difference is positive but leaves the additional negative scalar
`c0||f||²`. The pole form has rank two and is indefinite.

This proves the target-minus-square discrepancy, rather than fitting it.
The prime cutoff follows `n<=N`; trial-prime activation at `p²<=N` is not
mistaken for the jet-hit horizon. The infinite-place channel is already
present at every finite horizon.

## 3. Prove the finite-boundary repair impossible

On the infinite-dimensional smooth subspace `ell_+f=ell_-f=0`, the
discrepancy is exactly `(c0-2S_N)||f||²<0`. Thus it cannot be an added
positive sector or any finite-rank form. Finite-rank perturbations with
bounded cross forms also fail. No large-N limit removes this defect: its
essential norm is `2S_N-c0`, which increases without bound.

Moreover, independent two-endpoint channels already attain the sharp
minimum diagonal price by Cauchy–Schwarz. For the specified global
translation-invariant multiplier class, evaluation at frequency zero gives
the same lower bound even after coherent filters cancel unwanted frequencies.
Window-only positivity is not used to infer a global multiplier bound.

At indicator tests the exact residual is

\[
R_N=8(ss^*-cc^*)-(S_N-c_0/2)B,
\quad s(t)=\sinh(t/2),\quad c(t)=\cosh(t/2)-1,
\quad B(t,u)=2\min(t,u).
\]

It has at least m-1 negative eigenvalues on every m distinct positive times
up to log N. This is the same obstruction in Suzuki coordinates. It is a
statement about the residual, not a negative witness for the true kernel.

## 4. Locate the first unpaid lemma without renaming RH

To turn this square into a proof one would need an independently constructed
infinite-dimensional coherent correction, with domain and cross pairing
derived from the arithmetic geometry, whose completed norm is exactly
the displayed Weil form. No such correction is supplied. Defining it to be
the square root of Weil, or assuming its positivity, is circular.

The residual identity is not a strict reduction of RH. What it contributes
is a proved exclusion of finite-rank/orthogonal repairs and of attempts to
lower the same global edge-channel scalar price. The failed class now has
an explicit, growing essential obstruction, not an unexplained numerical gap.

## 5. Triangulate the alternative lifted constructions

* **Observation-first carrier squares:** point/derivative sampling on log n
  and single unrefined log-cell averages have a common invisible subspace.
  On tests inside `(1,1+2^-16)`, Weil is at least `1.3544...||f||²>0`.
  Therefore no internal D_N after those observations can recover the form,
  exactly or by all-test pointwise convergence. Refinement or continuum input
  is an explicit escape, not a construction already obtained.
* **Factor-local squares:** any nonunit factor-label-preserving lift has
  `L*S_XL=0`; h-step coupling requires a divisor of gcd(n,h). The natural
  factor-coordinate graph produces divisor-difference entries, and its unit
  axes supply all nearest-carrier edges. Label mixing/unbounded propagation
  is required to escape that theorem.
* **Forward return transfers:** all trace-class strictly height-increasing
  transfers have determinant 1. Adding such currents to a diagonal Euler
  operator cannot change its determinant. Reverse edges produce actual
  cycles but the simplest symmetrization has a continuant, not an Euler factor.
* **Half-density from symmetry alone:** the exact family J_F X^(-beta)
  preserves factor cone and swap for every beta>=0. Half-density requires
  an additional measure/normalization principle; the repeated numeral 1/2
  is not a derivation.

These probes share the exact target, but attack different failed arrows:
information loss, incidence support, absence of cycles, normalization, and
the completed metric. None uses finite PSD to claim an infinite result.

## 6. Stopping boundary and next verdict-changing probe

The productive natural constructors specified in the brief have now been
built or classified and tested against their missing arrows. Their precise
failure mechanisms are established. Continuing by inventing unrestricted
operators named Dirac would remove the hypotheses without proving anything.

The single next probe is a **specified continuum, nonlocal factor-label-mixing
first-order channel**, followed immediately by its polarized Weil discrepancy
on a common test core. It must change the negative bulk term coherently, not
hide it in a boundary name or an assumed metric. An exact new discrepancy or
a proved cancellation would change the verdict. No existing theorem in this
round pays that requirement, and no claim of RH progress beyond the scoped
obstructions is made.
