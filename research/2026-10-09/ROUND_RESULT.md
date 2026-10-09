# Round result: absolute dualizing/twistor geometry and a source-rigid noncompact history seam

**Date:** 2026-10-09. **Parent:** main after Round 063. **RH OPEN. No global Weil positivity or self-product Hodge theorem claimed.**

## New exact synthesis

A genuinely useful finite/Archimedean construction emerged from two recent primary sources:

1. Connes–Consani (2026-06), https://arxiv.org/html/2606.06604v1, construct local complex Tate curves E_p=C×/p^Z with canonical differential dz/z and periods log p, 2pi i.
2. Connes–Consani (2026-08), https://arxiv.org/html/2609.00299v1, build an absolute Archimedean twistor line with signed inversion z->-1/conj(z) and an odd-Frobenius action.

Previous Connes–Consani work (2022/23), https://arxiv.org/html/2205.01391v2, already constructs curve-level Serre duality / a dualizing module and canonical divisor K=-2{2} in its S[±1] framework. Therefore the claim that *all* Serre duality is missing over Spec Z is false. The missing object is a **source-faithful surface-level intersection/polarization with the actual Weil form**.

## Exact facts banked this round

### A. LCM events become areas of complete complex curves

For L_N=lcm(1,...,N), attach E_{L_N}=C×/L_N^Z. Its invariant form eta=dz/z has flat area

\[
\mathscr A_N=\int_{E_{L_N}}\frac{i}{2}\eta\wedge\bar\eta=2\pi\log L_N.
\]

Thus \((\mathscr A_N-\mathscr A_{N-1})/(2\pi)=\Lambda(N)\). Every real p^k event contributes log p, while an n=6 independent impulse is forbidden.

Combine this area increment with normalized finite Haar p^{-k/2} to recover the full prime weight \((\log p)p^{-k/2}\) without zeros.

### B. Dirichlet characters become unitary local-system holonomies

On E_p, a flat rank-one Hermitian local system with holonomy chi(p) along the log p cycle yields k-fold holonomy chi(p)^k. The full degree-one source is

\[
(\mathrm{Area}(E_p)/(2\pi))\,\mathrm{Hol}(a_p^k)\,p^{-k/2}
=(\log p)\chi(p)^kp^{-k/2}.
\]

This fails nonunitary unramified alpha_p; a genuine global Hecke compatibility condition rules out Davenport–Heilbronn mixtures by their connected b(6)=4ab anomaly. Local systems alone, however, survive fake frequency schedules and imply no GRH.

### C. Signed twistor reversal has a forced 2-ramification obstruction

The ordinary complex-point twistor line has K=O(-2), half-canonical O(-1), and anti-linear J(v0,v1)=(-conj(v1),conj(v0)) with J²=-I; its tensor square has reversal squared +I. Explicit residue pairing H0(O) x H1(O(-2)) -> C via Res(dz/z) realizes classical Serre duality.

For f(z)=c z^n, commuting with the antipodal involution j(z)=-1/conj(z) holds **iff n odd and |c|=1**. This matches the 2026 signed F1² construction restricting Frobenius to odd n. Classical Riemann–Hurwitz separately gives branch divisor (n-1)(0+infty), whose local integral half-ramification exists iff n odd. The even n=2 channel needs extra ramification/spin data; a scalar phase cannot fix the naive twistor lift.

**Do not infer the 2022 K=-2{2} equals the 2026 twistor p=2 defect; only a mathematical comparison is proposed.**

### D. The finite clocks nest; the Archimedean tori don't

H_2->H_6 is a canonical normalized finite-clock refinement. But the period lattices of E_2 and E_6 intersect only in 2pi i Z, as log6/log2 irrational by unique factorization. Their common identity-cover is C×, not a compact torus.

Thus the exact reversible span E_2 <- C× -> E_6 exists, but has infinite covering degree and Haar volume. Naive periodization from L²(R) to L²(R/log m Z) is unbounded; its obvious Hilbert adjoint cannot be the reverse-history completion. See the explicit sequence f_N with norm one but periodized norm sqrt(N/log m).

This is an exact no-go for a specific naive construction, not a theorem against all adelic correspondences.

### E. The true zero-free Poisson/Gamma/pole reflection still exists

Finite conductor theta-vector inversion is an antiunitary half-density involution R_m²=I. Its Fourier transform sends exact-conductor harmonic projectors to the primitive unit-residue support projector.

Global Gaussian Poisson yields the exact completed Mellin identity

\[
\pi^{-s/2}\Gamma(s/2)\zeta(s)
=
\frac1{s(s-1)}
+\frac12\int_1^\infty(\theta(t)-1)
(t^{s/2}+t^{(1-s)/2})\,dt/t.
\]

This forces the functional-equation reflection and the elementary pole correction with no zero input. It does not force Weil positivity; Davenport–Heilbronn is a critical sign-blind control.

### F. A complete local surface has Hodge index already, and still fails RH fidelity

For S_m=E_m x E_m, the horizontal/vertical/diagonal intersection matrix is

\[
\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}
\]

with eigenvalues (2,-1,-1). For H=F1+F2 and primitive D=aF1+bF2+cDelta with a+b+2c=0,

\[
D^2=-2[(a+c)^2+c^2]\le0.
\]

This is genuine Hodge-index positivity **for all m**, including arbitrary fake m. It does not read the zeta source, and so it cannot by itself be the Weil pairing. Its three-dimensional intersection space cannot reproduce the infinite-rank Q_W on all smooth tests.

## Primary clarification of the original "taproot"

The missing chain is NOT simply "no canonical sheaf -> no Serre duality -> no RR -> no positivity". Curve-level arithmetic Serre/RR exists; local P1 and E_p dualizing bundles exist; ordinary Tate surfaces have Hodge index. RR by itself never implies positivity (P1 O(-1) has degree -1 but RR holds).

The actual fourth gate is to construct one source-derived global correspondence map into a sufficiently large *proper arithmetic self-product* host, and prove the two distinct statements:

\[
D_f\cdot H=0,\qquad
-\langle D_f,\overline{D_g}\rangle_{\mathrm{int}}=Q_W(f,g)
\]

for the COMPLETE polarized Weil form, then an independent Hodge-index theorem on that primitive image.

This has not been done. In particular, neither picking a positive metric after inspecting Q_W nor treating the raw chiral commutator as positive is allowed.

## Execution and files

- ARCHIMEDEAN_DUALIZING_TWISTOR_HOST.md: literature correction, ordinary complex-point canonical class and quaternionic half-spin, p=2 parity, precise RH host gate.
- LCM_TATE_TORUS_AND_COVARIANCE.md: complete torus-area source and nonnested finite/infinity correspondence.
- NONCOMPACT_ARCHIMEDEAN_HISTORY_SPAN.md: first 2–6 common cover and infinite Haar trace.
- PERIODIZATION_DAGGER_NO_GO.md: exact L² unboundedness, Gaussian zero-mode subtraction proposal.
- PRIME_TORUS_HOLONOMY_SOURCE.md: period × holonomy × Haar half-density.
- LOCAL_TATE_SURFACE_HODGE_CONTROL.md: authentic finite surface Hodge sign and mutation-insensitive falsifier.
- scripts/adelic_twistor_duality_probe.py: finite theta, completed theta, Fourier conductor, spin, area tests.
- scripts/tate_torus_source_controls.py: mutation source and periodization tests.
- scripts/local_tate_hodge_index_control.py: exact rational/symbolic intersection matrix.

Independent local execution of the mathematical test suite (Python, numpy, mpmath, 78 digits) reported:
- theta/Poisson vector inversion residual < 1.4e-78;
- completed theta/Gamma/pole residual < 1e-79;
- exact finite conductor/unit support and antiunitary involution;
- twistor parity and half-spin;
- exact LCM source increments and RR negative-degree counterexample.

These are *local validation*, not a certified global operator inequality. Scripts committed to GitHub should be rerun in CI before merge.

## Next proper experiment (single principal session)

**Construct a source-rigid bounded/renormalized correspondence spanning E_2 <- C× -> E_6, with theta/Hecke coefficients and a declared dualizing trace.**

First derive its forward and backward adjoints from actual Haar/Tate data. Keep the mixed W_6 conductor correlation but forbid independent connected source at 6. Retain the p=2 twistor ramification obstruction rather than arbitrarily choosing an even-degree action. Then compute the complete polarized Weil discrepancy on C_c^\infty(-A,A) in the first 2–3 interacting interval, including:
- true \(\log2,\log3\) and p^{-1/2},p^{-k/2};
- Archimedean digamma energy and contact subtraction;
- rank-two pole form;
- growing negative scalar bulk debit.

If the discrepancy is nonzero or the coupling is mutation-insensitive, retire it. If equality holds, the *independent Hodge-index sign* is STILL a separate open theorem. No zeros may be used as construction inputs.

## Epistemic verdict

**Proved:** elementary torus areas, nonnested common cover, unbounded periodization, twistor monomial parity, finite-conductor Fourier/Poisson, local Hodge-index control.

**Classical/in current 2026 preprints:** curve-level Serre/RR, absolute twistor structure, prime-local Tate tori.

**Not proved:** a surface dualizing/trace/polarization package coupling ALL places and reproducing/positivizing Weil. **RH remains open.**
