# Proof attempt 001: where the chain stops

**Outcome: route refutation, not RH closure and not a claimed strict reduction
of the remaining RH-equivalent inequality.** The strongest new repository
theorem is finite-event rigidity. The strongest unconditional elimination of
the proposed aggregate-prime construction is Gaussian-residual rigidity.

## The hole contract

Exact proposed statement, with \(A,A^*,S_j,H_j\) as in `EVENT_DYNAMICS.md`:
\[
\tag{R}\boxed{H_j\ge A^*(S_j)\quad\text{for every prime-power prefix }j\ge0.}
\]

- Truth state: **UNVERIFIED**. Hypotheses are the actual von-Mangoldt weights,
  actual prime-power logarithms, and unmutated Suzuki Archimedean completion.
- Weakest form in this checkpoint argument: it suffices to verify the
  active-event reserves of the external reduction; (R) is the cleaner
  all-prefix statement. Neither is presently proved.
- Edge closed if true: every frozen affine prime prefix lies below \(A\),
  hence the active prefix does, hence \(\Psi\ge0\), hence RH.
- Novelty tax: (R) is **equivalent to RH**, given the certified initial
  range. Naming the convex conjugate has not reduced its strength.
- Known failures: independent eventwise PSD updates; finite truncations with
  exact completion; Gaussian quotient/phase/scalar rescaling; support-only
  comparison; monotonicity of the conjugate reserve.
- Cheapest falsifier for an alleged general invariant: increase one future
  event weight. A valid exact-arithmetic proof must use a premise that fails
  under that mutation; the ramp identity and curvature do not fail.
- Finite boundary: 35 certified intervals here establish only
  \(0<t\le\log101\); the external \(10^{10}\) sign certificate was not rerun.

## Strongest direct arithmetic proof chain actually attempted

1. **PROVED-IN-REPO.** The prime/Archimedean expression equals
   \(W(R_t*\widetilde R_t)\), with every Fourier constant checked directly.
2. **PROVED-IN-REPO.** Curvature has one plastic-constant transition;
   the prime-free initial range is positive, and every later event interval
   has one constrained minimum. All slope jumps and state recurrences are exact.
3. **PROVED-IN-REPO.** The prime ramp is the supremum of its prefix affine
   functions, so the global problem is exactly (R).
4. **ATTEMPTED, NOT PROVED.** Set \(M_j=H_j-A^*(S_j)\). Convex duality gives
   \[
   M_{j+1}=M_j+w_{j+1}[a_{j+1}-\tau(S_j)]
   -D_{A^*}(S_j+w_{j+1},S_j).
   \]
   The Bregman term is a debit. The arrival term has no automatic sign.
   The actual transition from prefix 4 to prefix 5 decreases \(M\), as
   interval-certified in the tests. The hoped-for monotone invariant fails.
5. **FIRST UNPAID LEMMA.** Prove that the exact arithmetic arrival credits
   cover cumulative dual-convexity debits, precisely (R). The smoothed
   von-Mangoldt version \(J_q\le C_q\) is the same unpaid sign theorem.
   Ordinary PNT and the checked finite-height bound do not establish it.
6. **CONDITIONAL FINISH ONLY.** If (R) were supplied, the envelope identity
   would prove \(\Psi(t)\ge0\) for every \(t\ge\log2\); the initial
   certificate covers the remaining range; Suzuki Theorem 1.7 would give RH.

There is no further implicit positivity step after item 5. Item 5 is
unresolved, so this chain is not a proof of RH.

## The proved replacement for the failed local-closure idea

For distinct \(a_1,\ldots,a_N>0\), real \(c_j,b\), let
\[
F(t)=\Psi(t)+\sum_{j=1}^N c_j(|t|-a_j)_++bt^2.
\]
`GRAM_LEVY_ATTEMPT.md`, Theorem 4 proves
\[
\boxed{F\text{ is CND}\iff
\mathrm{RH}\ \text{and}\ c_1=\cdots=c_N=0\ \text{and}\ b\ge0.}
\]
This is a theorem about finite perturbations, not an assumption that RH
holds. Its necessity first obtains RH from CND growth and the arithmetic
Laplace transform; only then does it use the conditional zero measure to
verify that a nonzero cosine-polynomial density cannot be positive.
The zero measure is never a proposed arithmetic Gram construction.

The root audit checked the Fourier constants, growth/analytic continuation,
singular-versus-absolutely-continuous decomposition, and mean-square argument.
A separate same-model adversarial reader checked the proof without editing it;
that is supplementary review, not independent empirical evidence.

**Additional scalar rigidity lemma.** For every \(a,c>0\),
\(\Psi(t)-c(|t|-a)_+\) is negative somewhere.
Proof: if it were globally nonnegative, then \(\Psi\ge0\), hence RH by
Suzuki, hence \(\Psi\) is bounded by his Theorem 1.6. Subtracting the
linear ramp then tends to minus infinity, a contradiction. This uses no
zero ordinates. In particular, *any* positive increase of one prime-event
weight eventually defeats global scalar positivity, or encounters an
already negative original value if RH fails.

This shows why the exact event amplitudes cannot be replaced by a robust
density-only invariant. A mutation beyond any chosen finite window remains
invisible there and preserves ordinary PNT asymptotics, but destroys the
global scalar assertion. This is a no-go for premises stable under that
mutation; it does not exclude arguments using exact Euler-product identities.

## Disposition of the five requested routes

| Route | Result of the actual attempt | Unpaid edge |
|---|---|---|
| A: arithmetic Gram | Literal event kernels are indefinite; finite-event rigidity rules out positive independent event updates. Theta convolution norms already have the wrong distributional kernel. | An independently positive **coupled** arithmetic pairing with exact entries. |
| B: positive Lévy closure | Exact-completion finite truncations grow exponentially; Gaussian corrections cannot make them CND. Uniform first-moment control contradicts the origin cusp. | A different nonlocal tail completion, positivity, and convergence. |
| C: checkpoints | Fully normalized and locally certified; monotone dual reserve refuted. Source tail inequality remains open. | (R), equivalently the true all-event cost-capacity inequality. |
| D: Borwein backwards | Exact sinc/contact geometry retained. A fixed support schedule permits arbitrarily destructive amplitude changes. | No positive functional or amplitude comparison transfers from support alone. |
| E: Gaussian bulk/residual | CLT proved. Exact Gaussian quotient has modulus greater than one; any scalar-rescaled/unit-phase characteristic limit is a point mass. | This canonical residual route is **REFUTED**; an entirely different construction is required. |

No independent adelic/intersection pairing or prolate comparison discharging
(R) was constructed. The function-field model supplies its own independent
positive intersection pairing; importing its name supplies no such identity
for this arithmetic system. These alternatives remain unproved, not refuted
in full generality.

## Single next verdict-changing probe

Test the **pinned finite-height smoothed-cost bound's additive slack** against
the exact reserve at active events beyond its calibration range, with the
height held inside an independently verified range and the omitted
\(h(u)\) restored. Define the certified slack
\(C_q-\widehat J_{T,\mathrm{pin}}\).

- A certified negative slack at one valid event kills that proposed sufficient
  tail certificate, even if the actual \(\Psi\) stays positive.
- A uniform analytic nonnegative bound, with all quantifiers and finite-height
  premises discharged, proves (R) through the source reduction and closes RH.
- Positive finite samples or overlapping intervals are **inconclusive**.

This is a discriminator for a concrete surviving constructor. It is not
another request to extrapolate finite positivity, and it has not been run in
this round. Without a new bound, the single theorem (R) remains standing.
