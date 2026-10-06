# Fixed carrier observations cannot recover the completed Weil form

**Theorem class:** all operators following point/derivative observations on
integer logarithms, or one average on each fixed integer-log cell. Internal
operators may be nonlocal, chiral, arbitrarily large, and depend on N. The
obstruction is the common information loss in the declared observation map.
It does not cover increasingly refined meshes or a retained continuum input.

## 1. An explicit positive test region, without RH or zeros

Let `h=2^(-16)` and `I=(1,1+h)`. This lies strictly inside `(log2,log3)`.
For any nonzero `f in C_c^infinity(I)`, the autocorrelation is supported in
`[-h,h]`. Thus every prime correlation in the Weil form is zero, since
`h<log2`. For u>=h, f and tau_u f have disjoint supports, so
`||tau_u f-f||²=2||f||²`.

For `0<u<=1`,
\[
k(u)=\frac{e^{-u/2}}{1-e^{-2u}}\ge\frac{e^{-1/2}}{2u}.
\]
The Gamma difference-square identity therefore gives
\[
E_\Gamma(f)\ge e^{-1/2}\log(1/h)\|f\|^2.
\]
Cauchy–Schwarz on I gives `|ell_+f ell_-f|<=h exp(h/2)||f||²`.
With the exact c0 from `WEIL_SQUARE_ATTEMPT.md`,
\[
\boxed{\mathcal W(f)\ge
\bigl[c_0+e^{-1/2}\log(1/h)-2h e^{h/2}\bigr]\|f\|^2>0.} \tag{O1}
\]
The last scalar sign and the placement of I are certified with Arb in the
companion script. The inequality is universal for the stated tests; the
finite certificate verifies only its explicit scalar constant.

## 2. Common-kernel obstruction on all horizons

**Point/jet sampling.** Every f supported in I and every derivative of f
vanish at all log n. Any linear map T_N determined only by these observations
has `T_Nf=0` for every N. Therefore any linear lifted operator D_N gives zero
energy, contradicting (O1). More generally, an arbitrary observation-first
construction has the same output at f and at 0, so it cannot recover both
their different Weil energies, even in a pointwise limit. Taking larger carrier horizons cannot recover
those functions: the observation nodes inside the fixed interval never refine.

**Cell averages.** Let `I_n=[log n,log(n+1))` and let T_N record
`integral_(I_n) f` (any nonzero normalization is allowed). Choose a nonconstant
`b in C_c^infinity(I)` and `f=b'`. It is nonzero, all cell averages vanish
exactly by the fundamental theorem of calculus, and (O1) still holds.
Thus no D_N following these fixed cell averages can converge to the Weil
energy on every compactly supported smooth test, much less equal it exactly.
The same f is invisible for every N, so there is no interchange-of-limits gap.

Lifting the observed coefficients to graph diagonals, factor fibers, prime
strata or history fibers after T_N does not help: all receive the zero vector.
This excludes that entire observation-first class, independently of which
square is built afterwards. If a completion adds a continuum channel that
sees f directly, it has broken the theorem's hypothesis and needs its own
exact metric identity.

## 3. Direct Suzuki-kernel version

The same obstruction can be seen before differentiating test functions.
Let `I_t=1_[0,t]`, with `0<t<log2`, and try `Phi_(N,t)=D_NT_NI_t`.

* Point sampling at log n gives a vector constant in t throughout this
  interval (apart from an immaterial fixed convention at the origin).
  Every resulting kernel is constant there. Its pointwise finite limit is
  also constant, whereas `K_Psi(t,t)=2Psi(t)` is continuous and nonconstant.
* A single flat cell average gives `T_NI_t=t v_N`, hence its Gram is
  `a_N t u` with `a_N>=0`. A finite pointwise limit at one positive t fixes
  the limit of a_N, so any limiting kernel is again proportional to t u.
  But Suzuki's exact origin expansion is
  `Psi(t)=(t/2)log(1/t)+O(t)`, not a constant times t².

These are analytic all-N statements. They do not depend on sampled target
PSD, a conjectured prime estimate, or zero locations.

## 4. What changes the verdict

A time/test-function lift must retain continuum information or genuinely
refine inside every fixed log cell as N increases. Carrier horizon alone is
not such refinement. A two-parameter discretization could escape; it would
still need a proved energy identity and control of both limits. No arbitrary
continuum interpolation is declared canonical by the discrete geometry.

Reproduce: `python -m unittest tests.test_round007_observation -v` and
`python -m scripts.round007_observation`. The polynomial derivative fixture
checks the exact zero-average mechanism; the theorem uses smooth bumps and
is not inferred from that one polynomial.
