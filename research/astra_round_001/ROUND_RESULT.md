# Round 001 result

**RH HAS NOT BEEN PROVED.** Outcome: exact refutation of specified plausible
routes, with one precise remaining arithmetic inequality. The new lemmas are
newly proved in this repository; no external novelty or priority claim is made.

Base repository: `https://github.com/femboy2112/FuckingRH`.
Base branch: `aletheia/rh-consolidation-2026-10-05`.
Exact base commit: `4c404f3c490a131330e8e053a2b263ce31812448`.
Verified base tree: `678c61dddaa829e51dcbcca0f4e7d2352469a2dc`.
Research branch: `astra/psi-wavefront-proof-001`. No changes to `main` or
historical archive files. The connector snapshot was verified against all
28 Git blob hashes, its tree hash, and the exact reconstructed commit hash.

## What became a theorem

1. **Finite-event rigidity.** For distinct positive times \(a_j\), real
   coefficients \(c_j,b\),
   \[
   \Psi+\sum_{j=1}^N c_j(|t|-a_j)_++bt^2\text{ is CND}
   \iff \mathrm{RH},\ c_j=0\ \forall j,\ b\ge0.
   \]
   Thus no nonzero finite event-weight change can preserve the full
   screw/Lévy property, even with Gaussian repair. Full proof:
   `GRAM_LEVY_ATTEMPT.md`, Theorem 4.
2. **Canonical residual no-go.** The geometric-prime law divided by its
   Gaussian factor has modulus **greater than one at every nonzero time**.
   Under any scalar rescaling and any unit-phase correction, a
   characteristic-function limit must be a point mass. It cannot be
   \(e^{-\Psi}\). Full proof: `CONVOLUTION_RESIDUAL_AUDIT.md`, R1–R4.
3. **Other precise obstructions.** Individual event kernels are indefinite;
   finite-event truncations retaining the exact completion grow too fast
   to be CND; uniformly bounded first absolute Lévy moments cannot produce
   the origin cusp; any positive increase in a single event weight defeats
   global scalar reserve positivity.
4. **Reconstructed controls.** Exact tent/Weil normalization, event dynamics,
   curvature, constrained minima, dual reserve recurrence, CND signs, and
   geometric-prime CLT. These recover or extend elementary consequences
   of existing results; they are not advertised as new RH progress.

## What was refuted or corrected

- Independent positive event increments, exact-completion finite-cutoff Lévy
  approximants, and the proposed canonical Gaussian-residual closure fail
  by theorems, not by lack of numerical encouragement.
- Borwein support geometry detects contact but cannot by itself control
  signed reserve amplitudes. True arithmetic conjugate reserve monotonicity
  fails already between prefixes 4 and 5.
- Mittermeier Part 3 v3 (75) omits a strictly positive Archimedean remainder;
  its page-20 conditional upper-edge display loses a factor two. The main
  pinned upper bound retains the exact slope and is not invalidated by
  those errors. Its all-event comparison is still unproved.
- Suzuki v4 §4.1's derivative constant omits \(-\tfrac12\log\pi\);
  the defining formula (1.1), used here, is unchanged.
- Repaired malformed requirements, input/fixture precision issues, an
  unsorted-event assumption, and precision loss in the baseline screw
  evaluator. A floating-point log is not an exact event identifier.

## What remains open

With the definitions in `EVENT_DYNAMICS.md`, the one unpaid theorem is
\[
\boxed{H_j\ge A^*(S_j)\quad\text{for every actual prime-power prefix }j.}
\]
This is RH-equivalent, not a newly solved weaker statement. The exact
recurrence identifies a Bregman debit but supplies no arithmetic theorem
paying it. No independent coupled Gram factorization or positive nonlocal
Lévy completion was constructed.

## Verification and boundary

- **35 tests passed** across five modules: exact rational and symbolic
  controls, independent Lerch/series comparison, interval-certified
  signs, event/Gamma mutations, synthetic off-line quartets, phase controls,
  the two prior Gaussian false friends, and hidden negative tails.
- Arb certifies the initial interval plus **35 complete event intervals**,
  precisely \(0<t\le\log101\). This is calibration, not a universal proof.
- Independently reproduced the count **455,062,595** prime-power events
  through \(10^{10}\). The external full positivity calculation was **not**
  rerun; its MPFR build lacked development headers. Count agreement is not
  sign certification.
- Zero spectral data appear only in conditional verification of the
  perturbation no-go and external-source audit. No zeros define an
  arithmetic positive construction or a claimed RH proof.
- Root derivation, source comparison, and a separate adversarial proof
  reading were used. Same-model readers are not independent witnesses.

Reproduce:

```sh
pip install -r requirements.txt
python -m unittest tests/test_suzuki_psi.py
python -m unittest discover -s tests -v
python scripts/event_dynamics.py --last-event 101
python scripts/convolution_controls.py
python scripts/checkpoint_event_count.py --limit 10000000000
```

Exact environment and retained raw results are in `evidence/`. Source
versions/hashes and the external certificate boundary are in
`CHECKPOINT_TAIL_AUDIT.md`. The complete logical graph is
`THEOREM_DEPENDENCY_DAG.md`; the first unpaid proof step and contract are
in `PROOF_ATTEMPT_001.md`.

## Single next verdict-changing probe

Certify the additive slack \(C_q-\widehat J_{T,\mathrm{pin}}\) of the
surviving finite-height cost constructor at active events outside its
calibration range, retaining the exact Archimedean remainder. A negative
slack refutes that sufficient constructor. A uniform analytic nonnegative
bound would close the arithmetic gap. Finite positive samples remain
inconclusive. This next probe has **not** been run here.
