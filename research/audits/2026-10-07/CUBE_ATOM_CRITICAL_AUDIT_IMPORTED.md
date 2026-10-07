# Imported audit provenance

- Original artifact: `CUBE_ATOM_CRITICAL_AUDIT.md` (user Library, original recorded modification `2026-10-07T22:50:43Z`).
- Imported into `femboy2112/FuckingRH` on 2026-10-07 by the GPT-6 assistant at user request for research provenance.
- Attribution: original author/agent **not independently verified** from file metadata; do not claim this was written by Claude without separate evidence.
- Scope: prior critical audit of the cube-atom / Markov / Gamma route, not a hostile peer review of the later log-bathtub or Toeplitz theorems.
- Original text follows, without mathematical edits. This import does not endorse all claims; each must be audited independently.

---

# Cube-atom RH audit: replace unitary folklore with a proved Markov generator

**Date:** 2026-10-07  
**Status:** exact auxiliary statements and a class obstruction; **RH remains open**.  
**Provenance:** audited against Suzuki (arXiv:1204.1827v2, §§1.4–2.2), Suzuki (JLMS 2023, Theorems 1.2, 1.6–1.7), and `femboy2112/FuckingRH` Round007–010 branch notes. No nontrivial zero ordinates are used as input.

## 1. Mathematical corrections

Let \(\alpha=2\omega>0\), \(q_p=p^{-\alpha}\), and \(J_\alpha(n)=n^\alpha\prod_{p\mid n}(1-p^{-\alpha})\). The weights

\[
\pi_{\omega,L}(d)=J_{2\omega}(d)/L^{2\omega},\qquad d\mid L
\]

form a probability distribution because \(\sum_{d\mid L}J_\alpha(d)=L^\alpha\). **They are not projectively consistent under** \(d\mapsto\gcd(d,L)\). For \(\omega=1/2\), \(L=2\) gives probabilities \((1/2,1/2)\) on conductors \(1,2\), and \(L=4\) gives \((1/4,1/4,1/2)\) on \(1,2,4\). The gcd pushforward is \((1/4,3/4)\), not \((1/2,1/2)\). Calling this family a canonical projective conductor measure was false.

A two-state rotation

\[
R_\omega=\begin{pmatrix}p^{-\omega}&-\sqrt{1-p^{-2\omega}}\\ \sqrt{1-p^{-2\omega}}&p^{-\omega}\end{pmatrix}
\]

is unitary for each fixed \(\omega\), but **its coherent repetition is not a Markov refinement**. For \(p=2,\omega=1/2\), \(R_\omega^2=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\), giving probability one in the new level after two rotations, whereas the desired new-top probability at a second birth is \(1/2\). To reproduce Markov branching one needs a fresh environmental ancilla at each birth or an explicitly dissipative reduced dynamics.

Multiplication by \((1-x)\) removes the \(x=1\) singularity of Suzuki's Gamma kernel \(g_\omega(x)\sim C_\omega(1-x)^{\omega-1}\), but changes the Mellin multiplier: \(\mathcal M[(1-x)g](s)=\mathcal M[g](s)-\mathcal M[g](s+1)\). It **does not** prove global \(L^2\) boundedness, Hardy invariance, or RH. Recovering \(g\) via division by \((1-x)\) restores its endpoint singularity.

## 2. Correct causal stochastic realization (theorem)

For every prime power \(e=p^k\), introduce an *independent* exponential waiting time \(T_e\) of rate \(\lambda_e=2\log p\). Define \(B_e(\omega)=\mathbf1_{T_e\le\omega}\). Then

\[
\Pr(B_e(\omega)=1)=1-e^{-\lambda_e\omega}=1-p^{-2\omega}.
\]

For \(n=\prod_p p^{k_p}\), put \(I_n(\omega)=\prod_{p\mid n}B_{p^{k_p}}(\omega)\), and \(I_1=1\). Independence gives the exact identity

\[
\boxed{b_\omega(n):=\frac{c_\omega(n)}{\sqrt n}
=n^{\omega-1/2}\mathbb E I_n(\omega),\quad
c_\omega(n)=n^\omega\prod_{p\mid n}(1-p^{-2\omega}).}
\]

At finite LCM depth \(K\) for prime \(p\), set \(J_{p,K}=\max\{j\le K:B_{p^j}(\omega)=1\}\), with maximum zero if there are no successes. For \(q=p^{-2\omega}\),

\[
\Pr(J_{p,K}=0)=q^K,\quad
\Pr(J_{p,K}=j)=(1-q)q^{K-j}\quad(1\le j\le K).
\]

Thus \(\Pr(J_{p,K}=j)=J_{2\omega}(p^j)/p^{2\omega K}\). Across different primes these distributions tensor. The transitions in **forward birth time K** are Markov: keep the old depth with probability \(q\), or jump to the new top depth \(K+1\) with probability \(1-q\). They provide a *stochastically consistent path law* when all birth histories are retained, **not** a projective consistency claim for final-conductor labels under deterministic gcd.

For fixed finite event set \(E\), the continuous \(\omega\)-generator acting on observables of bit vectors \(b\in\{0,1\}^E\) is

\[
\boxed{(\mathcal L_E f)(b)=\sum_{e\in E}\lambda_e(1-b_e)\bigl[f(b^{e\gets1})-f(b)\bigr].}
\]

This is a Markov generator, not a Hamiltonian. A quantum Lindblad realization on independent two-level atoms uses jump operators \(L_e=\sqrt{\lambda_e}\,|1\rangle_e\langle0|\) and the GKSL equation

\[
\partial_\omega\rho=\sum_e \left(L_e\rho L_e^\dagger-\frac12\{L_e^\dagger L_e,\rho\}\right).
\]

Starting at all zeros gives the same bit occupations. This is an exact *open quantum system* analogy, not a claim that arithmetic is physical quantum mechanics.

## 3. No-go: smooth closed-system dynamics cannot create the prescribed first-order births

**Theorem.** Suppose \(U_\omega\) is a family of unitaries on one fixed Hilbert space, \(\Omega\) is a unit vector, \(P\) an orthogonal projection with \(PU_0\Omega=0\), and \(\omega\mapsto U_\omega\Omega\) is norm-differentiable at \(0\). Then

\[
\|PU_\omega\Omega\|^2=O(\omega^2).
\]

**Proof.** Norm differentiability yields \(U_\omega\Omega=U_0\Omega+\omega v+o(\omega)\). Apply bounded \(P\), use \(PU_0\Omega=0\), and square. QED.

But the required top-depth occupation is \(1-p^{-2\omega}=2\omega\log p+O(\omega^2)\), which is linear rather than quadratic. Therefore the stated smooth unitary model is impossible. The rotation above evades the hypothesis because its new-channel amplitude is \(\sqrt{1-p^{-2\omega}}\sim\sqrt{2\omega\log p}\), not differentiable at \(0\). A Markov/Lindblad or singular/environmental dilation is the precise repair. This is a **class obstruction**, not an RH result.

## 4. Exact first-variation source theorem

For each integer \(n\ge1\), \(b_\omega(n)=n^{\omega-1/2}\prod_{p\mid n}(1-p^{-2\omega})\). Consequently

\[
\boxed{\left.\partial_\omega b_\omega(n)\right|_{\omega=0^+}=\frac{2\Lambda(n)}{\sqrt n}}
\]

with \(\Lambda(1)=0\). **Proof:** when \(n>1\), every distinct prime contributes one simple zero at \(\omega=0\). A first derivative survives if and only if \(n\) has exactly one distinct prime divisor; for \(n=p^k\), it equals \(2\log p/\sqrt{p^k}\). QED.

Thus for any finite wavefront \(X\) and test function \(F\),

\[
\left.\frac12\partial_\omega\sum_{n\le X}b_\omega(n)F(\log n)\right|_{0^+}
=\sum_{p^k\le X}\frac{\log p}{\sqrt{p^k}}F(k\log p).
\]

This is a genuinely causal Markov-generator derivation of the local von-Mangoldt source. It agrees with the earlier static \(\omega\)-jet/Möbius identity, hence has no independent novelty claim or RH consequence. **Taking \(X\to\infty\) or continuing this source in the Mellin variable is not justified by the finite identity.** Its total mass grows like \(2\sqrt X\) by PNT, so the missing signed completion is precisely at the unbounded limit.

In the Euler-safe region, where \(\Re(s)>1/2+\omega\),

\[
\sum_{n\ge1}b_\omega(n)n^{-s}
=\frac{\zeta(s+1/2-\omega)}{\zeta(s+1/2+\omega)}.
\]

The formal identity is exact there. Analytically continuing its *positive Markov source* while preserving causal Hardy boundedness is not supplied by probability theory.

## 5. The true RH gate is causal Hardy invariance, not unitarity

For real \(t\), Suzuki's meromorphic quotient satisfies \(|\Theta_\omega(t)|=1\) **unconditionally**:

\[
\Theta_\omega(z)=\frac{\xi(1/2-\omega-iz)}{\xi(1/2+\omega-iz)}.
\]

Thus the boundary multiplier \(M_{\Theta_\omega}\) is unitary on \(L^2(\mathbb R)\) whether or not RH holds. This alone has no zero-exclusion force. As a bare control, \((z+ia)/(z-ia)\) is unimodular for real \(z\) but has a pole at \(z=ia\) in the upper half-plane.

The required extra property is **Hardy/causal invariance**: the upper-half-plane multiplier must be analytic and bounded (inner). Suzuki's Proposition 1.2 proves that having this for every \(\omega>0\) is equivalent to RH, and his Theorem 2.2 expresses it as an \(L^2\) mapping property of the arithmetic-Gamma kernel. This is the correct proof gate, not generic Hilbert positivity, stochastic normalization, or boundary unitarity.

**The missing theorem is not yet reduced**: construct, without zeros, an independently forced non-factorizing interaction/observation of the Markov conductor field with the Archimedean place that preserves the Hardy subspace for every \(\omega>0\), and show its transfer equals \(\Theta_\omega\) on the Euler-safe domain. This is still an RH-strength operator statement. It must survive the audited Round007 bulk deficit and Round008 ratio-atom / vanishing-capacity obstructions, not assume their cancellation.

## 6. A useful null-model phase transition (not RH)

The top-relative defect for one prime has limiting geometric law \(\Pr(R_p=r)=(1-p^{-2\omega})p^{-2\omega r}\). Construct **a new independent product model** of these limiting defects; do not claim that they are an almost-sure limit of the forward depths \(J_{p,K}\). Then

\[
\Pr(R_p>0)=p^{-2\omega}.
\]

By the two Borel–Cantelli lemmas and divergence of \(\sum_p1/p\), this auxiliary infinite defect model has finitely many nonzero defects almost surely if \(\omega>1/2\), and infinitely many if \(0<\omega\le1/2\). This explains a sharp probabilistic threshold at \(1/2\) **using only the Euler pole**, not nontrivial zeta zeros. It is an excellent anti-overclaim control: a beautiful phase transition can be true unconditionally yet completely miss RH.

## 7. A second no-go: naive reflection moves forbidden atoms, it does not eliminate them

Let \(\tau_a f(x)=f(x-a)\) and \(Jf(x)=f(-x)\) on \(L^2(\mathbb R)\). The exact identities are \(J\tau_b=\tau_{-b}J\) and

\[
\boxed{\tau_a^* J\tau_b=\tau_{-(a+b)}J.}
\]

Thus, for a coherent reflected feature sum \(F=\sum_{n\in E}\alpha_n\tau_{\log n}\), the polarized quadratic form \(\langle Ff,JFf\rangle\) contains mixed terms at **sum** frequencies \(\log n+\log m=\log(nm)\). The ordinary unreflected Gram \(F^*F\) instead has mixed terms at **difference** frequencies \(\log(m/n)\). Switching from Toeplitz to Hankel reflection therefore changes the spurious support from ratios to products; it does **not** by itself match the Weil prime-power distribution.

For \(E=\{2,3\}\), positive coefficients produce a nonzero mixed reflected atom at \(\log6\), but \(\Lambda(6)=0\). Unless an additional, independently derived signed interaction or continuum pushforward cancels it, this elementary reflected-feature ansatz cannot be the completed Weil source. Its form is not automatically positive either, since \(J\) has both positive and negative spectral sectors.

**Scope:** this excludes the stated naive reflected-feature constructor; it does *not* exclude Suzuki's actual Hankel operator, a nonstationary cross-conductor metric, or additional pushforwards with exact cancellations. It upgrades the Round008 \(\log(3/2)\) ratio-atom test with the corresponding **product-atom** hostile control.

## 8. Falsifying probes before another round

1. **Conductor pushforward:** show natural gcd coarse-graining fails (above), but retained-history Markov transitions succeed. Do not restore false projective claims.
2. **Smooth-unitary mutation:** compare coherent rotation R² with two fresh independent jumps; any claimed equality must fail.
3. **Mellin innovation:** explicitly compute \(\mathcal M[(1-x)g]\) before calling a Gamma regularization transfer-preserving.
4. **Boundary-modulus control:** an inverse Blaschke factor defeats any attempt to infer upper-half-plane analyticity from real-axis unitarity.
5. **Arithmetic mutation:** replace prime rates \(2\log p\) by arbitrary \(\lambda_p>0\). The Markov source remains positive and unitary-dilatable; only the **exact** zeta coupling disappears. Hence generic source positivity is RH-inert.
6. **Reflected Hankel mutation:** test the forced mixed \(\log6\) composite-product atom as well as the \(\log(3/2)\) ratio atom. A reflection alone does not cancel either.
7. **First genuinely proof-bearing test:** propose one explicitly nonreducing interaction, compute its entire polarized continuum pairing, isolate forbidden \(\log(3/2)\) atoms and the large scalar deficit, and test Hardy invariance without assuming it. An L²/Hankel isometry *chosen to be* the desired operator is a restatement of RH, not a derivation.

## References

- M. Suzuki, *A canonical system of differential equations arising from the Riemann zeta-function*, arXiv:1204.1827v2, §§1.4–2.2, Theorem 2.2, Proposition 1.2. https://arxiv.org/html/1204.1827v2
- M. Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, JLMS 108 (2023), Theorems 1.2, 1.6, 1.7. https://doi.org/10.1112/jlms.12785
- `femboy2112/FuckingRH`: `research/astra_round_007/WEIL_SQUARE_ATTEMPT.md`; `research/astra_round_008/WEIL_PUSHFORWARD.md`; `research/astra_round_008/ROUND_RESULT.md`; `research/claude_round_009/AUDIT_009.md`; `research/claude_round_010/AUDIT_010.md` (branches, as audited in conversation).

**Verdict:** the stochastic and spectral bookkeeping can be made exact. RH is **not** proved or strictly reduced to an easier already-known theorem. The live problem is stable, causal, arithmetic-and-Archimedean coupling that defeats the known global bulk/ratio obstructions.