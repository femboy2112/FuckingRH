# Exact discrepancy and localized-boundary no-go

## 1. Target, not a fitted kernel

For `f in C_c^infinity(R)` supported in an interval of length at most
`log N`, retain the Round007 convention
`F=f*tilde f`, `tau_a f(x)=f(x-a)`, `S_N=sum_(q_j<=N) w_j`, and

\[
 c_0=\psi(1/4)-\log\pi<0,\quad
 \ell_\pm(f)=\int f(x)e^{\pm x/2}dx.
\]

The exact arithmetic Weil form is

\[
 \mathcal W(f)=E_N(f)+(c_0-2S_N)\|f\|²
                         +2\Re(\ell_+f\,\overline{\ell_-f}). \tag{W1}
\]

Its derivation and Suzuki primary conventions are in Round007
`WEIL_SQUARE_ATTEMPT.md`, §§1–3. Substitution of (C3), with no omitted cross
terms, gives

\[
 \boxed{\mathcal W(f)-Q_{N,h}(f)
 =(c_0-2S_N)\|f\|²+2\Re(\ell_+f\,\overline{\ell_-f})
                                  +\kappa\|F_Nf\|².}        \tag{W2}
\]

The correction has infinite continuum rank in general; Round007's finite-rank
boundary obstruction alone would not dismiss it. The following two separate
arguments do.

## 2. Cross-prime ratio atoms: exact finite obstruction

Write `b_j=c_j sqrt(w_j)>0`, `B=sum b_j`. Expanding before scalarization,

\[
 \|F_N f\|²=(B²+\sum_j b_j²)\|f\|²
 -2B\sum_j b_j\Re F(a_j)
 +2\sum_{i<j}b_i b_j\Re F(a_i-a_j).                          \tag{W3}
\]

For different primes, `q_i/q_j=p^k/r^l` is a reduced nonintegral rational.
Unique factorization shows that no different ordered pair of prime powers
has this same ratio. Thus the translation kernel of (C3) contains at
`log(q_i/q_j)` an isolated atom with coefficient `-kappa b_i b_j`.
The target (W1) has atoms only at zero and signed logarithms of integer
prime powers. Its Gamma kernel is smooth away from zero, and its pole
kernel is smooth; neither can cancel this new translated delta line.

In particular for `N>=3`, `h>0`, `r>0`, the atom at `log(3/2)` is nonzero.
It is detectable on any support interval of width greater than `log(3/2)`.
Polarize the forms and take unit-norm smooth bumps of shrinking width around
two points separated by that displacement: the matching translation pairing
persists, while the smooth-kernel pairings tend to zero. Other atom lines
are separated by choosing the width sufficiently small. Equality of forms
would imply equality of these polarized pairings, a contradiction.

More generally, for any constant Hermitian event metric `G_ij` in
`sum sqrt(w_iw_j) G_ij <delta_i f,delta_j f>`, with the same Gamma and
smooth pole sector, exact equality forces `G_ij=0` for distinct prime jets
whenever their displacement is observable in the test window. Complex
polarization recovers imaginary as well as real coefficients. This does
not forbid same-prime tower correlations or non-translation-invariant
couplings that change the continuum Gamma pairing.

An atom may shrink as the horizon grows. Therefore this finite obstruction
alone is **not** a limit obstruction. The next theorem provides that step.

## 3. A vanishing capacity theorem, without a prime-error estimate

Put `A_N=sum_j c_j sqrt(w_j)`. Since each refinement ratio is at least two,

\[
 c_j\le\sqrt{L_j/L_m}\le2^{-(m-j)/2}.                         \tag{W4}
\]

Moreover `w_j<=log(q_j)/sqrt(q_j)->0`. Hence

\[
 A_N\longrightarrow0,\qquad \|F_N\|_{L²\to L²}\le2A_N
                                      \longrightarrow0.     \tag{W5}
\]

Proof with all quantifiers: the sequence `sqrt(w_j)` is bounded. For any
epsilon choose `J` after which it is at most epsilon. The finitely many
`j<J` terms in (W4) tend to zero as `m` grows. The remaining sum is at most
`epsilon/(1-2^(-1/2))`. Let epsilon decrease to zero. No PNT or RH-scale
error bound is used. The operator estimate follows from `||tau_a-I||<=2`.

Thus the entire heat correction in (W2) tends to zero in operator norm,
uniformly even if `h` and `r` depend on `N` in their allowed ranges.

**Theorem LB (localized-boundary completion obstruction).** Keep the event
lift (C1) and exact Gamma difference channel. Let `Q_N` project onto at most
`R` normalized clock point states, at any sites, where `R` is fixed. Permit
an arbitrary nonnegative quadratic metric on
`Q_N H_L tensor K tensor L²(R)`, even an unbounded one on a suitable common
domain, but keep the complementary metric equal to the identity and forbid
cross terms between that complement and the chosen boundary subspace.
No such family has its squared pairing converge to the completed Weil form
on all compact smooth tests as `N -> infinity`.

Indeed the constant diagonal of `E_j` and Cauchy–Schwarz give, for every
point state `e_x`,

\[
 |\langle e_x,v_j\rangle|
 =|\langle E_j e_x,E_j e_0\rangle|/c_j\le c_j.
\]

Consequently the input energy located on `R` clock sites is at most
`4R A_N² ||f||²`. A positive metric can discard at most that energy: the
unchanged complement alone leaves the completed candidate bounded below by

\[
 E_N(f)-4R A_N²\|f\|².                                     \tag{W6}
\]

For any fixed nonzero compact smooth test, once `N` covers its support
width, (W1) holds. Also `S_N -> infinity`: already the prime contribution
dominates a positive constant times `sum_p 1/p`, which diverges by Euler's
elementary product argument. Thus `E_N(f)-W(f)=2S_N||f||²+O_f(1)` tends to
infinity, whereas the maximal subtraction in (W6) tends to zero. This
proves the claimed failure and in fact divergence of the candidate energy.

If the number of sites `R_N` grows, a necessary capacity condition for this
same class to match even one fixed nonzero test is

\[
 4R_N A_N²\ge 2S_N+O_f(1).                                  \tag{W7}
\]

This is only necessary, not a constructor or RH reduction. It identifies
what the theorem actually forces to change.

## 4. Cross blocks: the required gain is unbounded

The preceding theorem cannot simply omit its block-diagonal hypothesis.
For example the positive matrix
`[[1,-1/epsilon],[-1/epsilon,1/epsilon²]]` annihilates `(1,epsilon)`,
although its complementary compressed block is the identity. This is an
exact hostile control against an overbroad no-go.

There is nevertheless a quantitative extension. Relative to complementary
and selected-site inputs `u` and `v`, suppose the positive metric is

\[
 G_N=\begin{pmatrix}I&B_N\\B_N^*&T_N\end{pmatrix},\qquad
 T_N\ge B_N^*B_N,
\]

where `B_N` is bounded at each horizon; `T_N` may be an unbounded positive
form. Completing the square gives

\[
 \langle (u,v),G_N(u,v)\rangle
 =\|u+B_Nv\|²+\langle v,(T_N-B_N^*B_N)v\rangle
 \ge (\|u\|-\|B_N\|\|v\|)_+².                              \tag{W8}
\]

Let `E_event,N=||V_N f||²` and `b_N=2 sqrt(R_N) A_N ||f||`. Then
`||v||<=b_N` and `||u||²=E_event,N-||v||²`, so (W8) is bounded below by

\[
 \left(\sqrt{(E_{\rm event,N}-b_N²)_+}
                         -\|B_N\|b_N\right)_+².             \tag{W9}
\]

For each fixed compact test, `E_event,N=2S_N||f||²+O_f(1)`. Fixed `R` and
uniformly bounded cross gain still force divergence. Indeed, to have even
bounded candidate energy for a fixed nonzero test it is necessary that

\[
 2\sqrt R\,A_N\|B_N\|\ge\sqrt{2S_N}-O_f(1).                 \tag{W10}
\]

Thus permitting genuine boundary/complement cross terms does not save a
uniformly bounded coupling in this class. A required unbounded gain is now
quantified. The two-dimensional counterexample saturates the general
gain-versus-small-input mechanism; it supplies no arithmetic completion.

## 5. Scope and next obstruction

The theorem allows infinitely many Gamma modes, continuum input, all mixed
conductors, arbitrary positive boundary metrics, moving selected sites,
and arbitrary boundary metric size. Its block version requires no cross
terms; its extension allows cross terms but excludes uniformly bounded
gain. Both require the complementary clock block to remain the identity.
Neither covers arbitrary low-rank clock vectors, repeated inter-event mixing
that changes that block, growing-site interactions satisfying (W7),
unbounded gains satisfying (W10), or a nonlocal change of the test map.
Those are genuine escape hypotheses.

The heat candidate is therefore decisively killed, and a whole explicitly
defined localized-boundary completion class is excluded. RH is not proved,
and all mixed-conductor/Gamma transfer architectures are **not** ruled out.
The remaining proof-bearing question is a refinement-compatible interaction
that moves bulk energy into its cross pairing, cancels forbidden rational
atoms, and derives the exact pole and Gamma terms. That interaction has not
been constructed by the clock, theta identity, or scalar boundary recursion.
