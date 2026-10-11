# Carrier impedance and the one-way finite-certificate diode

**2026-10-10. RH OPEN.** Companion to OBSERVATIONAL_SUCC_GODEL_BRIDGE.md. Branch \`aletheia/observational-succ-godel-2026-10-10\` (draft PR #22). This note implements the user's **carrier-first** refinement of observational SUCC. It is a new formalization of what the finite observer is *permitted to access*, not a proof that RH is unprovable in PA/ZFC, not an actual physical thermodynamic law and not an observer-to-Weil identification.

## 0. The user's distinction: two evolutions inside the carrier

1. Carrier -> observation -> model -> further observation -> eventual certificate, if a finite certificate happens to exist.
2. Global structure -> finite-carrier channel -> observation -> internal model -> verification -> continued updating.

In a "fucked field" the second process may be asymptotically accurate and nevertheless have no finite **observation-only** terminal certificate. The global mathematical structure need not be underdetermined by all the observations: it may be completely determined in their infinite union. A fixed pair of globally indistinguishable objects is **not required**.

This paper formalizes \`carrier-relative\` observation and strict one-way finite witnesses. An independent finite symbolic proof can shortcut sampling, and a physical observer can reason over universal quantifiers. Thus "no finite observation-only terminal certificate" is strictly weaker than "no finite proof in T" and vastly weaker than "no finite proof in any conceivable future system."

## 1. Typed carrier process and access filtration

Let G belong to a declared class A of global source models. At stage n the carrier has a finite, authenticated history H_n, a finite internal model M_n, and an observation protocol P_n. Every new datum o_{n+1} must be computed from its permitted observation channel, with no future source reads:

\[
o_{n+1}=\operatorname{Observe}(G,P_n,H_n),\qquad
M_{n+1}=\operatorname{Update}(M_n,o_{n+1}),\qquad
P_{n+1}=\operatorname{Choose}(M_{n+1},H_{n+1}).
\]

Write \(\mathcal F_n=\sigma(o_1,\dots,o_n,\text{initially allowed side-information})\) for a probabilistic model, or the finite partition induced by these observations for a deterministic one. The information grows, \(\mathcal F_n\subseteq\mathcal F_{n+1}\), but no theorem says the global property of G becomes \(\mathcal F_n\)-measurable at some finite n. **Probe adaptive** choices are allowed. A finite proof using knowledge not in \(\mathcal F_n\) (an axiom, a closed-form definition or a structural theorem) is a different channel and must be logged separately.

### Exact logic: finite observation certificate iff property separates a fiber

For a deterministic observation transcript map \(\mathcal O_n:A\to D_n\) and Boolean target \(T:A\to\{0,1\}\), any correct terminal decision of T on transcript y requires T to be constant on the fiber \(\mathcal O_n^{-1}(y)\). This is immediate: any two models in that fiber produce the same input to the decision. Conversely, if T is constant on that fiber, a mathematical decision map can be defined on y; whether it is *computable* under the carrier's resources is separate.

For an unrestricted all-zero stream \(G_0=000\dots\), each n allows \(G_n=0^n10\dots\), identical through n and globally different for \(T(G)=1\iff\forall k\,g_k=0\). Every complete stream is uniquely determined by all of its prefixes; nevertheless, \(T(G_0)\) has no finite positive data-only certificate across this class. Refutation has an immediate finite witness (one observed 1). This is **one-sided openness**, not an absolute incompleteness theorem.

## 2. The key kernel theorem: exact correlation access, no finite global-PSD certificate

Work in the space S of continuous even real functions \(\Psi:\mathbb R\to\mathbb R\) with \(\Psi(0)=0\), endowed with the compact-open topology (locally uniform convergence). Define the screw-form kernel:

\[
K_\Psi(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u).
\]

The carrier's complete observation at budget B is \(O_B(\Psi)=K_\Psi|_{[-B,B]^2}\). At all budgets the observation map is **injective**, since

\[
K_\Psi(t,t)=2\Psi(t).
\]

**Theorem (finite-carrier PSD diode).** On S, the set
\[
\mathcal P=\{\Psi:K_\Psi\text{ is positive semidefinite at every finite sample}\}
\]
is closed and has empty interior in the compact-open topology. Thus it is nowhere dense. In particular, **for every finite observation bound B and every globally PSD \(\Psi\in\mathcal P\)** there is \(\widetilde\Psi\in S\setminus\mathcal P\) for which
\[
O_B(\widetilde\Psi)=O_B(\Psi)
\]
exactly. There is no correct data-only finite terminal certificate of global PSD on S at any positive model.

**Proof.** For a finite sample \(t_1,\ldots,t_r\) and coefficients \(c\), the quadratic form \(Q_{\mathbf t,c}(\Psi)=\sum_{i,j}\overline c_i c_j K_\Psi(t_i,t_j)\) is a continuous function of finitely many evaluations. Therefore \(\mathcal P=\bigcap_{\mathbf t,c}\{Q_{\mathbf t,c}\ge0\}\) is closed. Fix any \(\Psi\in\mathcal P\) and any compact-open neighborhood that constrains its values only on bounded sets; take B large enough to cover those sets and the intended kernel observation square. Choose \(a>2B\), \(t_* = a+1\) and a positive A with \(A>\Psi(t_*)\). Put \(\widetilde\Psi(t)=\Psi(t)-A(|t|-a)_+\). This is continuous, even, anchored at zero and agrees exactly with \(\Psi\) for \(|t|\le a\), hence produces identical kernel values for \(|t|,|u|\le B\) and belongs to the arbitrary neighborhood. But \(\widetilde\Psi(t_*)=\Psi(t_*)-A<0\), so \(K_{\widetilde\Psi}(t_*,t_*)=2\widetilde\Psi(t_*)<0\). QED.

**One exact rational control.** Choose \(\Psi_+(t)=t^2\), for which \(K_+(t,u)=2tu\succeq0\). At finite integer budget B let
\[
a=2B+1,\quad t_*=a+1,\quad A=t_*^2+1,\quad
\Psi_-(t)=t^2-A(|t|-a)_+.
\]
Then \(\Psi_+(t)=\Psi_-(t)\) for \(|t|\le 2B\), so the kernels are exactly identical throughout \([-B,B]^2\), while \(K_-(t_*,t_*)=-2\). No approximation, floating point or zeta zeros enter.

This is **not** a statement that Suzuki's actual arithmetic source can be perturbed this way and remain Euler-admissible, automorphic or functionally completed. The perturbation belongs to a broad function class. If a proposed arithmetic class is rigid enough, the theorem's conclusion might fail there. An independently known finite symbolic formula for \(\Psi\) may prove global PSD despite the inability of an *observation-only* protocol to certify it.

This theorem applies to noncompact observation time domains with unrestricted late perturbations. It does not claim all analytic completions are undecidable or that a PSD limit does not exist. Positive definiteness remains closed under appropriate convergence; the obstruction is that a finite observer has no **admissibility-preserving global certificate** based solely on its bounded readings.

## 3. A stronger channel model: distinct almost-sure global worlds, never perfect finite discrimination

Fix a hidden binary model \(H\in\{-,+\}\), equal prior probabilities. Under + the carrier observes i.i.d. Bernoulli(2/3) bits, under - i.i.d. Bernoulli(1/3) bits. The observer sees only the bit history, never the hidden model.

At n observations let \(S_n\) count ones. Both models assign strictly positive probability to **every** length-n word, while their likelihood ratio is

\[
L_n=\frac{P(X_{1:n}\mid+)}{P(X_{1:n}\mid-)}=2^{2S_n-n}.
\]

The exact posterior is

\[
P(+\mid X_{1:n})=\frac{L_n}{1+L_n}=
\frac{1}{1+2^{n-2S_n}}\in(0,1)
\]

for every finite observed word. Each additional bit changes the log-likelihood ratio by precisely \(+\log 2\) or \(-\log 2\): a finite-transport information increment. For any n and any history, zero-error identification is impossible from that history alone, and the smallest posterior error for any n-bit history is \(1/(1+2^n)>0\). No adaptive almost-surely finite stopping decision based only on those finite histories is zero-error under both hypotheses: a positive-probability terminal cylinder under one model also has positive probability under the other.

But by the strong law of large numbers,

\[
S_n/n\to 2/3\text{ under +},\qquad
S_n/n\to 1/3\text{ under -}
\]
almost surely. Thus the infinite sequence identifies the hidden model almost surely, although no finite sample gives *certainty*. This is a very concrete **carrier-to-global certificate gap with no permanent infinite observational ambiguity**. The expected log-odds drift under the true + model is \((\log 2)/3\) per observation. The finite statistical resistance is real relative to the declared channel; it is not a thermodynamic entropy-production theorem.

For a random hidden G, observation Y and subsequent model/decision V satisfying the Markov chain \(G\to Y\to V\), the data-processing inequality \(I(G;V)\le I(G;Y)\) formalizes that **processing the observations cannot recreate unknown signal information lost by that channel**, unless external information is introduced. This result concerns a specified probabilistic ensemble, not a nonprobabilistic cosmic truth measure. See Polyanskiy–Wu, MIT 6.441 *Information Theory*, Chapters 2-3, https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/pages/lecture-notes/ .

## 3a. A literal *quantum Hilbert carrier* has the same finite-to-infinite resistance

The user's physically embedded observer premise deserves an explicit quantum positive control, not just a classical coin analogy. Suppose the carrier must discriminate two **known** nonorthogonal pure-state preparations, \(|0\rangle\) and \(|+\rangle=(|0\rangle+|1\rangle)/\sqrt 2\), with equal priors. After n independent supplied copies, the alternative joint vectors are \(|0\rangle^{\otimes n}\) and \(|+\rangle^{\otimes n}\). Their Gram matrix is
\[
G_n=\begin{pmatrix}1&2^{-n/2}\\2^{-n/2}&1\end{pmatrix}
\]
and their squared overlap is exactly \(2^{-n}\).

By the Holevo–Helstrom state-discrimination theorem, even the *optimal global quantum measurement on all n copies* has minimum average error
\[
e_n = \tfrac12\bigl(1-\sqrt{1-2^{-n}}\bigr)>0
\]
for every finite n, while \(e_n\to0\). Rationalizing yields exact arithmetic bounds for n>=1:
\[
2^{-n-2}<e_n<2^{-n-1}.
\]
The carrier's globally optimal finite quantum apparatus cannot achieve perfect deterministic discrimination between these two hypotheses, even though the Gram overlap converges to zero, and asymptotically the alternatives can be distinguished with vanishing error.

This is a **genuine physical-Hilbert information-access theorem** with rigorously finite per-copy progress; it does **not** establish a thermodynamic law of dissipative resistance, a theorem about human proof ability, or anything about the Weil source. It is a calibrated model of why Hilbert-space embedding by itself doesn't make a global label finitely available.

Reference: John Watrous, *The Theory of Quantum Information* (2018), Chapter 3, Holevo–Helstrom theorem, https://cs.uwaterloo.ca/~watrous/TQI/ . The local module returns the **rational intervals**, not floating-point false-zero error values.

## 4. RH-facing translation and a discriminating next probe

Suzuki (2023), Theorem 1.2, establishes RH iff the *specific* completed arithmetic kernel \(K_{\Psi_\zeta}\) is globally PSD. A false RH would yield a strictly negative **finite** Gram witness. A true RH may or may not have a finite mathematical proof. The two facts do not tell us what the finite carrier can deduce from its accessible observations; this must be specified.

The key RH research question is now *not* whether the full kernel is determined by its complete observations (it is), but whether the source-admissible information that a finite carrier can certify is sufficient to establish the sign for all future test horizons:

1. Define the admissible class \(\mathcal A\) using authentic multiplicativity, unitary local phases where appropriate, log-prime clocks, exact half-density, gamma/conductor factors, and the relevant functional equation; do not silently conflate generic Euler products with completed arithmetic L-functions.
2. Define a bounded observation/proof protocol \(\mathcal O_B\) that includes all presently available source-correlated second-order probes and records the available proof rules, rather than merely kernel values.
3. **Adversarial pair test.** For each B, seek two *genuinely admissible* candidates that share the carrier's finite transcript but require different global PSD verdicts. Unlike unrestricted delayed impulses, this test may be impossible, since even the existence of an RH-violating admissible object in some constrained classes is unknown. Record ACCESS GAP/UNVERIFIED rather than forcing a mutant.
4. **Structural shortcut test.** Seek a finitely describable source identity or analytic coercivity bound that gives a uniform global sign without enumerating every horizon. Its existence would disprove the thesis that the *source class* is structurally barred from finite proof. This negative-to-the-hypothesis control is essential.
5. **Quantitative impedance.** If an independently justified probabilistic channel model exists, evaluate finite-sample likelihood separation, relative entropy and noise budget. In deterministic source classes, instead compute *certification-fiber diameter*: whether available observation/proof data are consistent with opposite target signs. These are distinct instruments; don't collapse them into a single RH truth score.

### Relation to the physical-Hilbert carrier

The parent ω-SUCC branch already proves that normalized half-density vectors
\[
|\Omega_N\rangle=H_N^{-1/2}\sum_{n\le N}n^{-1/2-it}|n\rangle
\]
have \(\langle\Omega_N,P_M\Omega_N\rangle=H_M/H_N\to0\) for fixed M, despite unit norm. This is a **real nonuniformity of a particular Hilbert carrier** (weak convergence without strong convergence), not a physical derivation of the Weil sign or impossibility theorem for finite arithmetic proofs.

### Claim ledger

- **Disclosed (elementary):** correlation observation map injective at infinite access; PSD cone closed with empty interior in compact-open topology of broad even continuous screw-source functions; exact delayed quadratic-kernel counterexample; nonzero finite Bayesian posterior error with infinite almost-sure discrimination.
- **Observed (bounded):** exact-Fraction delayed-kernel and posterior unit tests.
- **Conjectured:** authentic arithmetic source-and-carrier map exhibits analogous *admissibility-preserving* no-finite-certificate behavior.
- **UNVERIFIED:** operator intertwiner from actual carrier/source/Gamma to completed Weil distribution; proof-system independence; any thermodynamic information-flow law intrinsic to RH; global Weil positivity.
- **RH status:** OPEN.

Reproduce with \`python -m unittest discover -s tests/actualization -p 'test_carrier_impedance.py' -v\`. The modules do not read zeta zeros.
