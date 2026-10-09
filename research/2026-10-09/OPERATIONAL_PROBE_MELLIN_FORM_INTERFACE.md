# Operational observability II: joint-probe arity, Mellin jets, and a causal anti-spoof theorem

**2026-10-09.** Continuation of \`research/2026-10-09/operational-observability-wavefront\` at verified parent \`00a20f5e1fbc27e8c7fb29d3c95c1f3ae1effe9c\`. **RH OPEN.** These are finite operational/marginal theorems, exact Dirichlet-series identities, and an analytic form-domain obstruction. None is a new RH estimate or an independent positive Weil pairing. Main was \`8505467ea596b0636f73b655c521f50105d8b06e\` at start; preserve it.

## 0. Intent and pre-registered outcomes

**User's proposal:** SUCC, inverse/shadow SUCC and FUCC are fundamentally a **finite apparatus for the conditions under which mathematical realizations become constructible, executable, and distinguishable**. The finite/Archimedean interface and RH are test objects, not the definition of the apparatus. Local observables A and B may each be accessible while their joint relation requires a qualitatively new probe.

**Our repairs, not user assertions:** Define (i) exact prime-subset marginal probe order, (ii) a Mellin/Dirichlet lift of a particular Haar-centered mixed probe, (iii) source-fidelity tests under Hecke phases and composite mutations, (iv) a form-norm obstruction preventing finite linear sensors from controlling a completed Weil form. Predeclare likely outcomes: the Haar mixed tensor should be invisible to lower-arity probes; its Mellin lift should have a quantifiable zero at the pole s=1; a different exact-conductor Fourier probe should disprove universal jet-order claims; fake source events and nonunit/shifted p=2 should violate calibration; **later finite mutations should be able to spoof finitely many Mellin jets**; for complex characters Haar and Hecke centering should disagree; finite L2 linear sensors should not control the logarithmically unbounded archimedean energy. Failures should force a revised notion of observation, not claims of undecidability.

## 1. Correct inherited frontier and provenance

- Existing operational branch, head \`00a20f5\`, proved conductor birth \`b(d)=max_{p^k||d}p^k\`, two different SUCC execution histories with the same endpoint, an exact W_6 marginal-observation gap and the causal Dirichlet convolution-logarithm. See \`research/2026-10-09/FINITE_ACTUALIZATION_AND_PROBEABILITY.md\` and \`scripts/operational_actualization_probe.py\`.
- Main \`8505467\`, Round 067: Weil \`Q_L=P_L-K_L\` full positivity still RH-equivalent; do not confuse finite window observations with an independent global sign. Main R62: chiral boundary curvature indefinite; R63: simple Mellin time reversal sign-blind (Davenport–Heilbronn passes); R64: function-field Hodge-sign positive only in actual surface geometry; R65–67: local and continuous/current descriptions insufficient.
- External sibling \`research/2026-10-09/hecke-tate-connected-connection\` head \`e96b48f\`: \`log_*a\` detects the first fake connected composite 6. \`research/2026-10-09/even-frobenius-shadow-reconstruction\` head \`4b86eea\`: two-sector twistor repair, no global polarization. All such branches share substantial causal provenance, not independent RH proof evidence.
- Methodology: main \`wiki/07-methodology-and-discipline.md\`: exact proofs/controls, no zero input, report false avenues. Main and operational branch have no AGENTS.md/CLAUDE.md instructions.
- Primary external checks: Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, JLMS **2023**, DOI 10.1112/jlms.12785, establishes the exact explicit-formula \`Psi\` and \`Psi(t)>=0 all t iff RH\`; DLMF §5.11.2 \`psi(z)~log z\` is the load-bearing large-frequency fact; Dirichlet/Hurwitz continuation is classical. Connes–Consani arXiv:2006.13771 is a *prime-free/semilocal* positivity model, not a theorem proving the full Weil sign. Links below.

## 2. Theorem A — minimum marginal probe arity on the finite CRT clock

Let S be r>=1 distinct primes, d=product(S), G=Z/dZ with normalized Haar counting measure. Define

  h_S(n) = product_(p in S) (1_(p|n)-1/p).

Each local factor is centered, has squared L2 norm (p-1)/p² and Fourier support on *nontrivial* additive characters modulo p. CRT gives:

1. h_S belongs to the exact-conductor-d character space W_d and is nonzero.
2. For every proper subset T subsetneq S, the conditional expectation E[h_S | (n mod p)_(p in T)] is identically zero, while ||h_S||² = product_(p in S) (p-1)/p² >0.
3. Probability snapshots μ_±(n)= (1±h_S(n))/d are strictly positive, share **all** marginals on at most r-1 prime coordinates, but E_μ±[h_S]=±||h_S||².
4. Structural birth is b(d)=max S, while direct SUCC encounter of integer d is at N=d. Thus interaction **availability** and marginal **detectability** differ from direct numerical encounter.

This is classical finite-product/Hoeffding-ANOVA orthogonality, reorganized as a finite actualization theorem. **Probe class matters:** if an observer may multiply co-observed pointwise p-probes, h_S is already available; the theorem is about marginal distributions/subset conditional expectations, not metaphysical impossibility. Also μ± are NOT invariant under the full successor rotation. No statement of RH or logical independence follows.

## 3. Theorem B — a special joint arity ↔ Archimedean pole-jet law

In Re(s)>1 define F_S(s)=sum_(n>=1)h_S(n)n^{-s}. By expanding the product and using sum_(m>=1)(dm)^{-s}=d^{-s}ζ(s),

  **F_S(s)=ζ(s) product_(p in S)(p^{-s}-p^{-1}).**

The RHS is meromorphic globally and *entire* after the pole at s=1 is cancelled. Each factor has a simple zero at s=1:

  p^{-s}-p^{-1}=-(log p)/p (s-1)+O((s-1)^2).

Since ζ(s)=1/(s-1)+O(1), for r=|S|,

  **F_S(s)=(-1)^r [product_(p in S)(log p)/p] (s-1)^(r-1)+O((s-1)^r).**

Thus the first nonzero Mellin jet has index **r-1**. In particular,
S={2,3}: F(1)=0, F'(1)=(log2 log3)/6;
S={2,3,5}: F(1)=F'(1)=0, F''(1)= -2(log2 log3 log5)/30.

This is an exact, unconditional **finite-probe → global pole-jet** relation, but it is pole cancellation at s=1, NOT a theorem at the RH critical line s=1/2 and NOT a new positivity statement. The ζ pole is an essential global input. The special centering is essential.

**Counterexample to an overclaim:** g(n)=exp(2πi n/6) has exact conductor 6, vanishes under both mod-2 and mod-3 conditional expectations, but
  sum_(n>=1)g(n)n^{-s}=Li_s(e^{iπ/3}),
  evaluated by continuation at s=1 = -log(1-e^{iπ/3})=iπ/3 ≠ 0.
Hence *exact conductor* and *minimum marginal arity* DO NOT universally determine Mellin jet order.

Independent triangulation: evaluate F_S at s=2.37+0.41i using (i) the above Euler/divisibility expansion and (ii) the finite-period Hurwitz expression d^{-s} sum_(r=1)^d h_S(r) ζ(s,r/d). Local high-precision residuals ~10^-78 for S of 2, 3, and 4 primes; this is a numerical check of an elementary proved identity.

## 4. Theorem C — source mutations are seen by the first jet, but can be spoofed

For S={2,3}, h(6)=h(30)=1/3. Perturb ζ's coefficient a(6)=1 to 1+δ. Then

  ΔF(s)=δ(1/3)6^{-s},  ΔF(1)=δ/18.

A single fake connected composite at 6 is audible at the Mellin basepoint. But adding δa(30)=-5δ gives

  ΔF(s)=δ/3(6^{-s}-5·30^{-s}),  ΔF(1)=0,

while the coefficientwise **connected Euler-source defect** log_*a(6)=δ remains! This makes precise why early SUCC source histories and global aggregate sensors have different information.

**General anti-spoof theorem.** For any m>=1, take m+1 distinct composites n_0=6,n_1,...,n_m with h(n_j)≠0, t_j=log n_j. Let
  c_j=1/product_(k≠j)(t_j-t_k),   δa(n_j)=ε n_j c_j/h(n_j).
Polynomial interpolation implies sum_j c_j t_j^k=0 for k=0,...,m-1. Therefore the perturbation ΔF(s)=sum δa(n_j)h(n_j)n_j^{-s} has its first m jets at s=1 exactly zero, yet log_*a(6)=δa(6)≠0. Any fixed finite set of these Mellin derivatives admits a source-invalid perturbation passing all of them. ε may be arbitrarily small so all changed coefficients remain positive.

**Scope:** this adversary is outside the genuine completely-multiplicative/Euler-source class; that is exactly why the **causal source test** defeats it. This is not a claim of RH undecidability, nor of indistinguishability under unlimited observations. A full analytic germ would detect finite perturbations.

**Independent source mutation controls:**
- for a completely multiplicative local α_2 mutation and unmutated other primes, the 2–3 Haar probe is
  F_α(s)=ζ(s)(3^{-s}-1/3) ((α2^{-s}-1/2)(1-2^{-s})/(1-α2^{-s})).
  Thus F_α(1)=-(α-1)log3/[12(1-α/2)] (for α near 1, α≠2), nonzero for α=1.03;
- shifting 2's multiplicative log degree to log2+η replaces α by α(s)=exp(-sη), so F(1)=-(e^{-η}-1)log3/[12(1-e^{-η}/2)], nonzero for η=.01.
These are checks of the *defined* local deformations. They do not prove the full completed Weil form becomes negative after mutation.

## 5. Theorem D — **Haar** and **complex Hecke** probe centering cannot be the same scalar

For an unramified primitive Dirichlet character χ with χ(p)≠1, use the local probe 1_(p|n)-c.

- Haar centering on Z/pZ requires c=1/p.
- To force its χ-weighted Euler/Dirichlet transform to vanish at s=1, the exact local identity
  sum_(n>=1)χ(n)(1_(p|n)-c)n^{-s}=L(s,χ)[χ(p)p^{-s}-c]
  requires c=χ(p)/p, as L(1,χ)≠0 for nonprincipal primitive χ.

These constraints are incompatible when χ(p)≠1. They are not merely different notation; Haar marginal orthogonality and the Dirichlet pole-jet cancellation select **different covectors**.

For quartic χ mod 5, χ(2)=i, χ(3)=-i:
- Haar-centered h_{2,3} produces F_{χ,h}(1)=L(1,χ)/3 ≠0;
- Hecke-centered h_{χ}(n)=prod_(p=2,3)(1_(p|n)-χ(p)/p) produces an order-2 zero at s=1;
- for the normalized Davenport–Heilbronn mixture D=aL(s,χ)+conj(a)L(s,barχ), with a=(1-iκ)/2 and κ=sqrt(1+φ²)-φ, the SAME χ-adapted probe instead yields
  F_{D,hχ}(1)=conj(a)·(2/3)L(1,barχ) ≠0.

The L and D comparisons use the same declared χ-centered test, and were independently checked via (a) local Euler factors and (b) a period-30 Hurwitz sum at a generic safe complex s. No zeros are used. The exact positive mod-5 control demonstrates an analytic *source-separator*, not GRH.

**Caveat:** this refutes **one common scalar Haar-centering prescription**, not every possible positive Hecke local-system polarization. The χ-centered probes are complex-valued and generally NOT Haar-mean-zero. A nontrivial change of test space/pairing (possibly χ⊕barχ with matrix fibers) would be needed to make their operational roles compatible.

## 6. Theorem E — finite bounded sensors miss the Archimedean Weil form norm

Fix L>0 and 0≠φ∈C_c^∞(-L,L). For T→∞ set f_T(x)=φ(x)e^{iTx}. The full completed Weil form on the test core has
  Q_L(f)=pole_L(f)+(1/2π)∫ Ω(ξ)|hat f(ξ)|²dξ - finite_prime_L(f),
  Ω(ξ)=Re ψ(1/4+iξ/2)-logπ.

Suzuki/Weil normalization is held fixed; a test on (-L,L) has autocorrelation support (-2L,2L), so the prime contribution contains only p^k≤e^(2L) and is a bounded quadratic form. The polar piece is also a bounded finite-rank form at fixed L.

DLMF 5.11.2 gives Ω(ξ)=log|ξ|−log(2π)+o(1) as |ξ|→∞. Fourier modulation translates hat φ by T, so dominated/tail estimates yield

  **Q_L(f_T)=||φ||²_2 log T + O(1) → +∞.**

On the other hand, for EVERY finite collection of continuous linear L² sensors ℓ_j(f)=<f,v_j>, weak convergence f_T ⇀0 follows from Riemann–Lebesgue (φ conjugate(v_j)∈L¹), hence ℓ_j(f_T)→0. For v_j themselves smooth on the chosen compact test core, project f_T onto the orthogonal complement of span{v_j}: the modified packets have EXACTLY zero sensor outputs and still possess Q_L energy ~||φ||² log T, because the projection coefficients decay rapidly and the fixed vectors have finite form energy.

This is a rigorous **finite-probe NON-CONTROL of the full quadratic-form value**, not a demonstration that finite probes cannot detect NEGATIVE directions (the invisible high-frequency packets are positive-energy). A global positivity inequality may be proved by a nonlocal theorem; no undecidability follows.

**Topology lesson:** the inductive union of finite conductor cylinders is L²-dense in L²(Z-hat), but that does not yield a Weil *form-core* after an unspecified arithmetic→Archimedean transform. On the log-window, the natural positive control topology is roughly
  ||f||_V²=∫(1+log(2+|ξ|))|hat f(ξ)|² dξ,
with zero extension outside (-L,L); bounded prime/polar pieces are continuous perturbations. Any proposed operational transport must control this stronger form domain, not just bounded Hilbert probes.

**Fixed-test exception:** each particular smooth compactly supported f needs only finitely many prime powers p^k≤e^(2L) plus the independently known Gamma and poles, so an individual strict negative Weil witness is potentially finitely accessible. The unproved universal **all f/all L** inequality, not an absolute blindness of every finite f, is the RH-sized claim.

Independent numerical illustrations use g(x)=(1+cosπx)/2 on [-1,1] (piecewise C¹; the general theorem uses C_c^∞), with exact ||g||²=3/4. Its gamma energy increases approximately (3/4)log T while its first four low-frequency linear readings decay as T grows. These are illustrative quadrature checks, not an interval-certified sign test.

## 7. False starts, negative controls, and why the result is worthwhile

**Falsified interpretation 1:** "Every exact conductor-d sector has first nonzero Mellin jet ω(d)-1." False: the additive conductor-6 Fourier character has value iπ/3 at s=1.
**Falsified interpretation 2:** "A zero at s=1 authenticates the arithmetic coefficients." False: δa6=δ, δa30=-5δ keeps F(1)=0; any finite jet family can be spoofed by Vandermonde mutations.
**Falsified interpretation 3:** "Haar-conditional expectation automatically becomes the correct Hecke-weighted adjoint for a complex character." False for χ(p)≠1 without twisting observables.
**Falsified interpretation 4:** "Finite L² probe convergence suffices for Weil continuity." False by modulated log-energy packets.
**Known positive controls:** Haar CRT conditional expectations and exact conductor (2,3),(2,3,5),(2,3,5,7); ζ Mellin factorization/jet lead; primitive quartic mod-5 L with χ-adapted probe.
**Known negative controls:** additive Fourier exact conductor; Davenport–Heilbronn matched function; fake coefficient at 6; nonunit α2; displaced log2; compensating future composites; high-frequency packets. None uses ζ zeros.
**No independence inflation:** all calculations use classical CRT/ANOVA, Euler factors, Hurwitz continuation, Weil/Suzuki, and DLMF; repeated mathematical consequences are not independent evidence for RH.

## 8. Claim ledger, reproducibility, handoff

| ID | Mathematical content | Status | Proof/experiment |
|---|---|---|---|
| OA2-A | joint arity, exact conductor, μ± marginal indistinguishability | **Demonstrated**, finite classical | §2; exact rational script |
| OA2-B | special centered Haar Mellin jet order r-1 | **Demonstrated**, classical | §3; independent Hurwitz calculation |
| OA2-C | m Mellin jets can be spoofed while log_*a(6)≠0 | **Demonstrated**, interpolation theorem | §4; high-precision 1–4-jet tests |
| OA2-D | Haar vs Hecke centering incompatibility | **Demonstrated**, elementary local obstruction | §5; χ/DH safe-point tests |
| OA2-E | finite L² sensor non-control of Weil form energy | **Demonstrated**, standard asymptotic argument | §6; illustrative quadrature |
| OA2-F | independent signed arithmetic Hodge polarization | **UNVERIFIED** | not constructed |
| OA2-G | RH or any new uniform RH estimate | **OPEN** | no proof |

Executable tests (Python >=3.10, mpmath>=1.3, scipy>=1.9, numpy>=1.20):
- \`scripts/operational_probe_arity_mellin.py\` (75-digit arithmetic / Hurwitz / χ / DH / mutation tests);
- \`scripts/operational_weil_probe_completeness.py\` (numerical digamma energy and sensor decay).
- recorded actual JSON output in \`research/2026-10-09/OPERATIONAL_PROBE_ARITY_RESULTS.json\` and \`research/2026-10-09/OPERATIONAL_WEIL_PROBE_RESULTS.json\`. The proofs do not depend on these observations. Distinguish execution of exact committed bytes from independent local runs in the handoff.

**Next attack (two distinct instruments):** build an actually *source-dependent, history-preserving* map from the finite CRT probe hierarchy / connected Euler innovations into a χ⊕barχ Archimedean test bundle, with an explicitly declared positive Hilbert metric and exact log-period clocks. FIRST test whether Haar versus Hecke centering can coexist after doubling and whether composite/log-ratio atoms are absent; THEN test continuity in the real log-Weil form norm, full Gamma/pole trace and finally independently proved Hodge-index sign. It is NOT enough to show an innocuous L² isometry or a rank-one square. A failed rank/domain/trace test is a useful concrete obstruction.

**Primary sources**
- Suzuki JLMS 2023: https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.12785
- DLMF digamma asymptotics: https://dlmf.nist.gov/5.11
- Connes–Consani 2020/2021 (archimedean positive window, not full RH): https://arxiv.org/abs/2006.13771
- Hoeffding decomposition (modern overview): https://www.sciencedirect.com/science/article/pii/S0047259X25000399
