# Corrections to the Round-059 frontier

These corrections concern the requested construction and its proof gates.
They do not constitute a full audit of the historical research corpus. Paths
and sections below refer to parent `265bf38dfd6af7d5820396f7e80244122a4aa235`.
The historical ledgers are preserved as records; current wiki formulas are
corrected on this research branch.

## 1. Multiplicativity is not identical to prime-frequency independence

The genuine mod-5 character and Davenport–Heilbronn use the same integer
frequencies log n. The former has b(n)=chi(n)Lambda(n); the latter has a
nonzero connected coefficient at 6. Rational independence of log p is true
but does not distinguish these coefficient systems.

The matched-character experiment remains useful: conductor and Gamma terms
can be matched in the arithmetic form. The claim that an entire coefficient
change is a causally isolated single-variable toggle is too strong. Root
number phases disappear on logarithmic differentiation, so their difference
does not invalidate the matched Gamma comparison; the full representation
and functional-equation signature still require precise duality conventions.

## 2. The amplitude and clock mutations need separate labels

For a real beta near 1, a(n)=beta^(v_2(n)) is completely multiplicative, with

$$\sum a(n)n^{-s}=\zeta(s)\frac{1-2^{-s}}{1-\beta2^{-s}}.$$

It has exactly the mutated prime-power coefficients beta^k log2. Thus changing
the whole alpha_2 tower does not destroy multiplicativity. It changes local
unitarity and compatibility with the fixed degree-one completion. Moving the
whole log2 tower preserves a log-additive free monoid but violates its
identification with the actual integer lattice.

The stronger example is the fake-6 source:

$$-F'/F=-\zeta'/\zeta+\eta6^{-s}
\Longrightarrow
F=\zeta\exp(\eta6^{-s}/\log6).$$

This entire multiplier never vanishes. The zeros are unchanged; the original
completion/growth package fails. Negativity of a mutated old-form expression
is therefore not automatically a witness of new off-line zeros.

## 3. The universal factorization meta-theorem is false

`research/claude_round_004/PROOF_ATTEMPT_004.md`, “Meta-theorem”, and
`IRREDUCIBLE_NONCOMMUTATIVE_CORE.md`, “The core”, generalize specific failures
to all commuting prime constructions. `wiki/08` promotes that inference to a
governing theorem. It is not valid.

For V_m e_n=e_(mn), the commuting-prime construction B=V_2+V_3 has
B*B=2I+V_2*V_3+V_3*V_2, with a nonfactorized positive mixed-prime Gram.
An example with commuting normal unitaries is |z_2+z_3|^2 on the two-torus.
Its four values at z_2,z_3 in {1,-1} are 4,0,0,4, which cannot be a product
of a function of z_2 and a function of z_3.

The independent-mode Koszul cross commutators in the original calculation
do vanish. Explicit product constructions have their own separability
limitations. Those facts survive; a universal necessity theorem for the
affine braid does not.

## 4. The three gates need a fourth

Round 059 says that anything clearing its three gates “IS the proof”. A
coefficient-admissibility functional can pass true characters and fail all
listed mutants without establishing the sign of Q. The construction in this
checkpoint demonstrates the distinction explicitly.

The necessary fourth gate is an exact identity or inequality for the **full
completed Weil form**, with an independent sign theorem and all required
test-space, domain and limit statements. The theta Gram is not that identity.

## 5. Complex ordinates require the reflected autocorrelation

In `wiki/02`, section 2.3, the unconditional expression sum |F(gamma_rho)|^2
is wrong. For compactly supported g and F(z)=integral g(u)exp(izu)du,

$$\widehat{g*\tilde g}(z)=F(z)\overline{F(\bar z)}.$$

Only for real z does this equal |F(z)|^2. A synthetic control is
g(u)=u on [-1,1]: F(i)=-2/e and F(-i)=2/e, so the correct product at i is
-4/e^2, while the erroneous modulus square is +4/e^2. Smooth odd bumps give
the same sign separation. These are synthetic complex arguments, not actual
zero data. Lagarias, *Li coefficients for automorphic L-functions*, section 3
and Appendix A, states the corresponding reflected Weil pairing.

## 6. The low-pass zero-comb identity needs a test-space qualification

`wiki/04`, section 4.3, cannot unconditionally regard complex ordinates as
Dirac masses on R. They define evaluation functionals on entire tests. Under
RH they become a positive locally finite measure on the real axis.

Even then, the displayed digamma-minus-finite-comb symbol is not literally
equal pointwise to its own sinc projection: its digamma part has not been
band-limited. The safe exact statement is equality of its action, including
the pole term, on the declared band-limited test functions. A pointwise
low-pass representation needs an explicit projection and distributional
prescription. The measured plots remain observations; the unconditional
“Gibbs sidelobes of a positive real zero measure” explanation is not proved.

## 7. Evenness allows a parity split, not an even-only search

A real, reflection-invariant quadratic form decomposes into real/imaginary
parts and into even/odd sectors. It need not have an even lowest vector.
For example, the kernel -2 cos(k(x-y)) on [-1,1], k=3 pi/4, has eigenvalues

$$-2(1-2/(3\pi))\quad\text{on cos}(kx),\qquad
-2(1+2/(3\pi))\quad\text{on sin}(kx).$$

The smaller one is odd. Smoothing the two spectral atoms by sufficiently
narrow even Gaussians preserves the strict gap, giving the same counterexample
with a smooth real even symbol. The parity restriction in `wiki/04` section
4.4 needs this correction.

## 8. Numerical and operator scope

- The recent DH/character/large-matrix scripts are described as scratch-only
  in Rounds 049, 051 and 058. Their numbers are not reproducible from the
  pinned tree alone and have not been rerun here.
- A strictly positive finite matrix has an open positive-definite neighborhood
  under continuous perturbation. Finite observations of tiny margins do not
  prove positivity holds at a unique parameter point. An asymptotic shrinking
  window requires an additional theorem.
- Boundary unimodularity alone is not Hardy innerness. The ratio
  (z+i)/(z-i) has unit modulus on R and a pole in the upper half-plane.
  Analyticity and contractivity have to be checked on the specified domain.
- A real spectrum alone does not imply self-adjointness for an arbitrary
  operator. A proposed equivalence needs an actual operator, domain, and
  normality/diagonal representation hypotheses.

These repairs remove false premises without claiming that a valid route to
full Weil positivity has consequently been found.
