# Round008 result

**RH is not proved.** This round proves a scoped obstruction to a concrete
mixed-clock/Gamma completion class and constructs/checks the next compatible
operator control. It does not claim that every nonlocal clock architecture
is impossible, or that the remaining RH sign has been strictly reduced to
an independently known theorem.

## The main theorem

For the full LCM innovation lift, the total event amplitude visible through
one normalized clock coordinate is bounded by

\[
 A_N=\sum_{j\le m}\sqrt{d_j/L_m}\sqrt{\log(p_j)/\sqrt{q_j}}
 \longrightarrow0.
\]

An arbitrary positive metric confined to `R` fixed clock-coordinate sites
with unchanged complementary metric can remove at most
`4 R A_N²||f||²` of energy. The completed Weil residual requires removal of
`2 S_N||f||²+O_f(1)`, and `S_N -> infinity`. Such completions cannot work.
With boundary/complement cross blocks, a necessary condition becomes

\[
 2\sqrt R A_N\|B_N\|\ge\sqrt{2S_N}-O_f(1).
\]

Uniformly bounded gain is therefore also excluded. These are genuine
class obstructions with explicit escape hypotheses, not renamed RH
inequalities. Proof: `WEIL_PUSHFORWARD.md`, §§3–4.

## What else became exact

- Every mixed-conductor innovation and the full boundary-twist unitary,
  including Haar factors, CRT labels and phases.
- A scalar nonlinear clock-state recursion. A single twist is Möbius;
  full refinement is degree p. Finite-LTI pole/rank obstructions do not
  rule out this nonlinear closure or time-varying 2x2 phase equations.
- The full birth-charge global determinant differs from the local Euler
  product; its different infinite value is analytically and interval-certified.
- Gamma determinant constants, relative det_2 normalization, a quantitative
  positive Gamma-mode approximation, and exact real/p-adic overlap distinctions.
- The correct dual Fourier refinement, a balanced continuum sampling map,
  and the complete vector theta/Mellin continuation. These are classical
  Poisson structures, not an RH positivity result.
- A shared-origin heat square with all cross terms calculated. It fails
  finite equality through isolated prime-ratio atoms and fails convergence
  through the independent vanishing-capacity theorem.
- A refinement-compatible carry/oscillator family with exact heat and
  innovation traces. It remains conductor-reducing after explicit unitary
  conjugacy, so its generated algebra creates no cross-conductor pairing.

## What was refuted, and what was not

Refuted: identifying local and global clock determinants; calling the
noncompact direct sum Fredholm; treating full refinement as one Möbius step;
using the same embedding on both sides of finite Fourier refinement;
letting a fixed number of coordinate-boundary modes with bounded cross gain
pay the Weil debit; inferring conductor mixing from oscillator/carry
noncommutation alone.

Not refuted: arbitrary nonlocal interactions, growing boundary sectors,
unbounded gains meeting the necessary bound, different continuum test maps,
or operators that change the complementary metric and break conductor
reduction. These are remaining possibilities, not constructed solutions.

The small-state intuition was partly vindicated. The real obstruction is
the completed **pairing**, not the storage size of the scalar clock formula.

## Single next verdict-changing probe

Specify one nonreducing observable in the compatible carry/oscillator
family and compute its complete continuum Gram/Duhamel kernel. Before an
infinite limit, test the isolated log(3/2) component and the bulk identity
coefficient against Weil. This is the first local discriminator for a new
interaction; passing it alone would not prove the all-test identity.

## Provenance and verification

Branch: `astra/lcm-cyclotomic-gamma-008`, directly from frozen Round007
`8da6cf92d276961356497486048163f0aff08233`. Side-branch content was audited
and rederived without merging its ancestry; no main merge. Historical
rounds and archive files were left unchanged. Exact source heads and the
environment are in `INTEGRATION_AUDIT.md` and `evidence/environment.json`.

The inherited baseline has 184 passing tests; all **227 tests pass** after
adding 43 Round008 tests. The final suite and evidence
manifest are recorded in `evidence/full_tests.txt` and `evidence/manifest.json`.
Five new scripts use exact algebra and Arb enclosures. The twenty requested
hostile classes are documented in `HOSTILE_CONTROLS.md`, including mutations
that preserve generic positivity but change the required arithmetic pairing.
Bounded same-model reviews are preserved honestly as reviews, not independent
primary sources. No zero ordinates enter any Round008 construction.
