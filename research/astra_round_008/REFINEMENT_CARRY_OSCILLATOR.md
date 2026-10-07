# Next-probe execution: a compatible carry/oscillator family

The localized-boundary theorem leaves repeated interaction and a changed
complementary metric open. We therefore test a concrete refinement-compatible
carry/oscillator, rather than only listing that escape as future work.
This is a positive construction with a precise remaining reduction, not a
claim of a completed Weil square.

## 1. The missing refinement map can be supplied exactly

On `H_L tensor L²(R,dy)` let `U_L` be the Euclidean carry from
`GAMMA_DRIFT.md`: it advances the residue, translating the quotient by one
at the wrap. For `M=pL`, residues `n=a+bL`, define

\[
 (S_{L,M}f)_{a+bL}(y)=\sqrt p\,f_a(b+py).                     \tag{RC1}
\]

Change variables `z=b+py` and sum with normalized Haar `1/(pL)`:
`||S f||²=||f||²`. For successive ratios `p,r`, the combined digit is
`b+pc`, so these embeddings compose exactly. Checking the interior, the
old wrap, and the full wrap separately proves

\[
 U_M S_{L,M}=S_{L,M}U_L.                                    \tag{RC2}
\]

The fixed quotient oscillator in the earlier control does not intertwine:
differentiation of (RC1) introduces a factor `p²`, and its potential changes
from `y²` to `(b+py)²`. Instead choose the physical-coordinate oscillator

\[
 (K_Lf)_a(y)=-L^{-2}f_a''(y)+(a+Ly)^2 f_a(y)-f_a(y).          \tag{RC3}
\]

Then `K_M S=S K_L` on the lane-wise Schwartz core, with compatible
self-adjoint closures as shown next. This choice is explicit; it is not
claimed to be forced by the prime charges.

## 2. The exact coordinate conjugacy exposes what was constructed

Define the unitary

\[
 (R_L f)_a(x)=L^{-1/2}f_a((x-a)/L).
\]

Direct substitution, including the quotient wrap, yields all three
identities

\[
 R_M S_{L,M}=I_{L,M}R_L,\quad
 R_L K_L R_L^*=I\otimes H_{\rm osc},\quad
 R_L U_L R_L^*=C_L\otimes\tau_1.                             \tag{RC4}
\]

Thus the oscillator is self-adjoint and nonnegative on the pulled-back
oscillator domain, and its core/semigroup intertwining follows by unitary
conjugacy. The carry and oscillator still genuinely fail to commute:

\[
 [I\otimes H_{\rm osc},C_L\otimes\tau_1]
       =C_L\otimes(2x-1)\tau_1.
\]

However every conductor projection (and every lifted LCM innovation)
commutes with both operators and their adjoints. Consequently those sectors
reduce every bounded observable in the generated operator algebra and the
associated closed forms defined by its spectral/semigroup operations.
Applying such a common observable to different innovation inputs produces
no cross-event pairing. The response **within** a sector can depend on its
clock phase: on character `h`, the carry is `exp(2*pi*i*h/L) tau_1`.
We do not confuse reduction with identical within-sector responses.

This is the exact hypothesis exposed by the calculation. Real
noncommutation by itself is not noncommutation with the arithmetic strata.
An additional source/interaction not reducing those strata is required to
create the intended cross-event cost. Adding an origin projection would do
that, but then its complete form must be recalculated; it is not contained
in this reduced algebra.

## 3. Trace comparison, derived without spectral zeros

For `t>0` and integer `k`, (RC4) and the Mehler Gaussian integral give

\[
 \operatorname{Tr}(e^{-tK_L}U_L^k)=
 \begin{cases}
 0,&L\nmid k,\\
 \displaystyle\frac L{1-e^{-2t}}
       \exp\!\left[-\frac{k^2}{4}\coth t\right],&L\mid k.
 \end{cases}                                                \tag{RC5}
\]

The trace is ordinary trace class. The difference from (G7) is essential:
in the covariant physical coordinate, one carrier step translates by one;
in the fixed quotient coordinate, only a wrap translates by one. The
respective Gaussian displacements are `k` and `k/L`.

At one refinement the exact innovation trace is therefore

\[
 \operatorname{Tr}(E_{p,L}e^{-tK_{pL}}U_{pL}^k)
 =\frac{pL\,1_{pL\mid k}-L\,1_{L\mid k}}{1-e^{-2t}}
                          e^{-k^2\coth(t)/4}.               \tag{RC6}
\]

This is the complete mixed-conductor/Ramanujan trace, multiplied by a common
Gaussian channel. No mixed factors were deleted to obtain it.

For each fixed nonzero integer `k`, (RC5) is eventually exactly zero along
the LCM sequence, since `L>|k|`. At `k=0` it is `L/(1-e^-2t)`, which
diverges; its normalized value has no prime dependence. This trace does
not approach the prime-weighted explicit formula. Scaling `k` with `L`,
changing the observable, or taking a nonstandard trace is a different
constructor requiring its own derivation and convergence proof.

**Verdict.** A fully compatible carry/Gamma system has actually been built.
The exact coordinate conjugacy and trace classify it: it preserves the
arithmetic innovation sectors, and its plain heat/return trace does not
supply the desired Weil pairing. This does not exclude arbitrary
interactions added to this family. It narrows the next missing operator to
one that breaks this reducing-conductor algebra while controlling the
cross-prime ratio atoms and the bulk degree cost.
