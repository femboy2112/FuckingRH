# Arithmetic connection and Poisson completion — result

**Parent:** main at `265bf38dfd6af7d5820396f7e80244122a4aa235`, Round 059.
**Branch:** `aletheia/arithmetic-poisson-connection-2026-10-09`.
**Status:** source construction, finite completion and closed renormalized connection proved;
Weil positivity unproved.

The requested three gates can be enforced by a single compatible system:

1. The integer divisibility connection extracts b=(a log)*a^(-1), without
   inserting prime-power support. For characters it is exactly chi Lambda.
2. A common multiplicative eigenline in the additive residue module forces
   the allowed amplitudes. The same module has its additive Fourier transform.
3. The ordinary integer-lattice dilation fixes log n and the real half-density;
   Poisson summation supplies the actual Gamma, conductor and pole completion.

This is an arithmetic compatibility construction. **A fourth gate is necessary:**
prove that the construction supplies the full Weil pairing with an independent
sign mechanism, including all domain and limiting arguments. The first three
gates by themselves do not imply RH.

## What was proved

- Exact finite identity: `[H_N,C_N(a)] C_N(a)^(-1)=C_N((a log)*a^(-1))`.
- Exact discriminator: `b_DH(6)=(1+kappa^2)log6`, while `b_chi(6)=0`.
- Unit-modulus and clock rigidity from the shared additive representation.
- An explicit Gaussian-derived Poisson seed with Mellin transform
  `xi(s)/(4*pi^2)`, without supplying xi or its zeros as input.
- A hard-cutoff failure: the theta partial-sum norm squared is asymptotic to
  `3*N/(128*sqrt(2)*pi^4)` although the completed theta function is in L2.
- A canonical integral counterterm giving norm error `O(N^(-1/2))` and an
  endpoint correction giving `O(N^(-3/2))`, with explicit integral bounds.
- An exact remaining domain obstruction: `integral X phi=-1/(8*pi^2)`;
  therefore the bare logarithmic sum does not preserve the completed L2
  space. All logarithmic moments cannot be removed on a nontrivial analytic
  Mellin core.
- Its explicit repair: the moment-retaining Müntz lift
  `A_0 f=sum f(nx)-(integral f)/x` is closable on `C_c^infinity(0,infinity)`;
  its graph closure is the maximal Mellin multiplier zeta. The completed
  logarithmic insertion `C_0=[X,A_0]` is closable with multiplier -zeta'.
- The connection defined by `nabla_0(A_0 f)=C_0 f` also has a canonical closed
  graph. Its identification with -zeta'/zeta is an output of the arithmetic
  definition, not an input phase or a chosen zero-dependent domain.
- Finite completed logarithmic approximants converge with norm error
  `O_f((1+log N)/N^(3/2))` after the endpoint correction on the stated core.

The framework is classical Dirichlet/Poisson/Müntz mathematics. The useful
advance in this program is the compatible construction, proved finite
completion, closed moment-retaining operators, and runnable mutation instrument. It is not
a new theorem establishing Weil positivity or a literature-level novelty claim.

## Files

- [CONSTRUCTION.md](CONSTRUCTION.md): hole contract, definitions, proofs,
  arithmetic Weil interface, domain obstruction, sources, and next probe.
- [FRONTIER_CORRECTIONS.md](FRONTIER_CORRECTIONS.md): repairs to the inherited
  mutation interpretation, factorization no-go, and unconditional zero pairing.
- [arithmetic_poisson_connection.py](../../../scripts/arithmetic_poisson_connection.py):
  executable exact and numerical controls.
- [probe_results.json](evidence/probe_results.json): complete raw result, precision,
  environment, base commit, script hash, design/holdout split and limitations.
- [manifest.json](evidence/manifest.json): file hashes and reproduction command.
- [verification.json](evidence/verification.json): the probe status and five passing
  existing Suzuki baseline tests, with their captured output.

## Measured checks

The final root probe passed all eight grouped checks. The coefficient identities
were checked symbolically through n=36, plus an arbitrary nonmultiplicative
12-by-12 incidence matrix and its independently evaluated finite matrix logarithm.

| Check | Root result | Scope |
|---|---:|---|
| Character versus DH | DH eigenline defect squared 2.3358288841...; character defect 0 | Exact formula plus 70-digit evaluation |
| Additive Fourier identities | residual below 8e-71 | Finite mod-5 sums |
| Theta inversion | both chi and DH pass, residual below 6e-71 | Six specified parameters; demonstrates that symmetry alone does not discriminate |
| Mixed-prime Gram | largest quadrature/formula discrepancy below 3e-19 | Three integer pairs, including a held-out pair |
| Arithmetic box form versus Suzuki | discrepancy below 3e-45 | Four widths, no zeros used |
| Nonzero-moment Müntz lift | Mellin discrepancy below 1e-40 | Gaussian lift versus independent finite Euler summation at three complex arguments |
| Amplitude, clock, half-density and fake-6 controls | all violate the intended compatibility identity | These are not new numerical Weil-sign claims |

The finite-completion observations include the following. The displayed error
is the squared L2 error after the endpoint correction.

| N | Raw squared norm / N | Corrected squared error |
|---:|---:|---:|
| 8 | 2.0699085618e-4 | 5.8290813892e-8 |
| 32 | 1.7924336967e-4 | 9.0411359771e-10 |
| 128 | 1.7240600739e-4 | 1.4120243277e-11 |
| 37, holdout | 1.7800834786e-4 | 5.8480864640e-10 |
| 101, holdout | 1.7301357967e-4 | 2.8741940422e-11 |
| 257, holdout | 1.7126610959e-4 | 1.7444665521e-12 |

The proved raw limit is 1.7013622659e-4. The N=1024 raw check gave
1.7041969004e-4. These numbers illustrate the theorem; they do not supply its
infinite quantifier. Quadratures are not certified intervals.

## Reproduce

From the repository root, with numpy, scipy, mpmath and sympy installed:

```bash
python scripts/arithmetic_poisson_connection.py \
  --output research/aletheia_2026-10-09/arithmetic_poisson/evidence/probe_results.json
```

The run prints the grouped check results and exits nonzero if a check fails.
The program never calls a zero finder or imports a zero list. Its small use of
the existing Suzuki evaluator is an arithmetic-to-arithmetic normalization check.

## Claim ledger

| ID | Claim | State | Evidence / boundary |
|---|---|---|---|
| APC-01 | Finite incidence connection and source converses | Proved | Sections 2–3; exact symbolic checks |
| APC-02 | DH fails the actual source at n=6 | Proved | Algebraic expression; no zero input |
| APC-03 | Character amplitude and integer clock rigidity | Proved | Unitary residue module and faithful real translations |
| APC-04 | Gaussian seed supplies the completed Mellin function | Classical identity, derived here | Poisson summation and explicit differentiation |
| APC-05 | Raw theta Gram diverges linearly | Proved | Dominated-convergence proof; quadrature/closed Gram agreement |
| APC-06 | Integral counterterm and endpoint-corrected L2 rates | Proved | Riemann/trapezoid remainder estimates |
| APC-07 | Bare logarithmic-domain obstruction | Proved; repaired by APC-13–14 | Explicit nonzero moment; analyticity prevents deleting all moments |
| APC-08 | Fixed finite Euler mutation can preserve multiplicativity but not the old completion | Proved | Rational reflection identity |
| APC-09 | Fake b(6) can preserve every original zero | Proved | Explicit nonvanishing entire multiplier |
| APC-10 | Universal commutative-to-factorized no-go | Refuted | Exact mixed-prime Gram counterexample |
| APC-11 | Ordinary completed theta Gram equals Weil form | Not established; not asserted | Different Mellin weights; the closed source still lacks the Weil trace/pairing identity |
| APC-12 | Full Weil positivity / RH | Open | No global sign theorem obtained |
| APC-13 | Moment-retaining lift and logarithmic insertion have maximal closed realizations | Classical Müntz structure, proved here | Section 9.1–9.2; joint graph core, no zero input |
| APC-14 | Arithmetic connected graph has a maximal closed realization | Proved | Section 9.4; quotient graph lemma; bare prime series is not asserted convergent |
| APC-15 | Finite completed logarithmic approximants converge at the stated rate | Proved on declared core | Section 9.3; derivative tails with logarithmic weights |

## Provenance and independence

The root read the pinned repository, implemented and ran the probe, checked the
proofs and opened the primary sources. One bounded constructor supplied an
independent construction/limit derivation; an adversary checked the cutoff
constants and domains; a translator checked the character and completion
rigidity. These are same-model internal checks with shared task provenance,
not independent external confirmations. Methodological separation comes from
algebra, Gaussian integration, Riemann/trapezoid estimates, finite Fourier
calculations and primary literature, not from the number of agents.

The old Round 049/051/058 eigenvalue experiments were explicitly scratch-only
in their source session. They were not rerun and were not used as a proof
premise. This checkpoint records new reproducible controls with narrower claims.
