# Encountered-information filtration and the exact causal prime-source budget

**Date:** 2026-10-07
**Status:** elementary exact finite arithmetic/Hilbert-space theorems and a sharp causal-vs-passivity obstruction. **RH OPEN.**
**Motivation / user-origin:** shadow SUCC is restricted to information already encountered at the moving wavefront; event updates must not depend on not-yet-actualized states.
**Derivation / contribution:** GPT-6 organized the known LCM/von-Mangoldt and SUCC-boundary facts into a source-limited filtration/birth operator and tested finite controls. This **repackages established results** rather than claiming priority.

## 0. Primary and in-repo provenance

- Arithmetic: unique factorization, lcm identities, von Mangoldt \(\Lambda(n)\), classical PNT. No original priority claim.
- Probability/analysis: nested sub-\(\sigma\)-algebras, conditional expectation as orthogonal projection in \(L^2\), martingale difference orthogonality. Standard Doob/Hilbert-space theory.
- Suzuki: *A canonical system of differential equations arising from the Riemann zeta-function*, arXiv:1204.1827v2, Proposition 1.2, Theorem 2.2: causal source support and the *separate* RH-strength Hardy-inner condition. https://arxiv.org/abs/1204.1827v2
- Previously derived in repo: Round006 \`research/claude_round_006/ROUND_RESULT.md\` C100 expresses von Mangoldt support via the integer-corner SUCC defect; \`research/aletheia_2026-10-06/EULER_AS_CENTERED_WEYL_SUM.md\` and \`research/audits/2026-10-07/ACTIVATION_CAUSALITY_HARDY_PASSIVITY.md\` independently delimit positivity/causality. These are **predecessor results**, not results newly proved here.
- Test script: \`scripts/rh_causal_filtration_checks.py\`; independent finite local test \`/tmp/causal_filtration_checks.py\` executed 2026-10-07, with output in \`CAUSAL_FILTRATION_EXECUTION.md\`. No GitHub Actions run is claimed.
- Git history: this file is the provenance anchor for any downstream claim. Corrections must append their SHA and reason.

## 1. First: use only the information available at the event

Let

\[
L_n=\operatorname{lcm}(1,\dots,n),\qquad L_1=1.
\]

At time \(n\), the causal state knows \(L_{n-1}\) and the newly encountered integer \(n\). It can therefore compute

\[
L_n=\frac{nL_{n-1}}{\gcd(n,L_{n-1})}
\]

*without referring to any future integer*.

Define the event-weight source

\[
\boxed{w_n=\frac1{\sqrt n}\log\frac{n}{\gcd(n,L_{n-1})}.}
\]

### Theorem A — local LCM increment is von Mangoldt

For every \(n\ge2\),

\[
\boxed{
\log L_n-\log L_{n-1}=\Lambda(n),
\qquad
w_n=\frac{\Lambda(n)}{\sqrt n}.
}
\]

Proof: all proper prime-power divisors of \(n\) occur before \(n\). If \(n\) is not a pure prime power, each constituent maximal prime power \(p_i^{k_i}\) is a proper divisor \(<n\), hence \(n\mid L_{n-1}\) and \(L_n=L_{n-1}\). If \(n=p^k\), the preceding LCM already contains \(p^{k-1}\) but not \(p^k\), while all other prime valuations are unaffected. Thus \(L_n/L_{n-1}=p\). This is exactly \(\Lambda(n)=\log p\). QED.

This is the **strongest literal mathematical expression of the user's no-lookahead event rule**. The prime-power source is read off from the already-actualized support boundary.

## 2. Haar-CRT filtration has an exact information decomposition

For \(L\mid L'\) define

\[
H_L=L^2(\mathbb Z/L\mathbb Z,{\rm Haar}),\quad
H_{L'}=L^2(\mathbb Z/L'\mathbb Z,{\rm Haar}).
\]

The pullback isometry

\[
(Jf)(r)=f(r\bmod L)
\]

obeys \(J^*J=I\). The conditional expectation/projection onto old residue information is \(Q=JJ^*\). Every \(g\in H_{L'}\) satisfies the *exact Pythagorean information budget*

\[
\boxed{
\|g\|^2_{H_{L'}}
=
\|J^*g\|^2_{H_L}
+
\|(I-JJ^*)g\|^2_{H_{L'}}.
}
\]

The two terms are old information and its orthogonal innovation. This is a standard \(L^2\)-projection theorem, not a dynamical energy conservation law when genuinely new source power is injected.

Equivalently, on the profinite probability space \(\widehat{\mathbb Z}\) with Haar measure, \(\mathcal F_n=\sigma(r\bmod L_n)\) is an increasing filtration. For any **fixed independently defined** \(Z\in L^2\), \(M_n=\mathbb E[Z|\mathcal F_n]\) is a martingale with pairwise orthogonal increments and

\[
\|M_N\|_2^2=\|M_1\|_2^2+\sum_{j=2}^N\|M_j-M_{j-1}\|_2^2\le\|Z\|_2^2.
\]

**Circularity warning:** choosing \(Z\) to equal a hypothetical RH-positive *completed* Weil observable would hide the entire problem in the choice of the terminal variable. A static projection martingale does not construct a source-derived completed transfer.

## 3. Sharp flatness null: stationary CRT filtration is SUCC invariant

Let \(S_L\) be cyclic successor on \(\mathbb Z/L\mathbb Z\). The quotient map intertwines successors:

\[
S_{L'}J=JS_L,
\]

and, since cyclic successor is unitary, the old-information projection satisfies

\[
\boxed{[S_{L'},JJ^*]=0.}
\]

So nested stationary CRT expectation and ordinary cyclic SUCC are compatible, but the resulting projection/transport curvature is **zero**.

This is already consistent with older repository no-go results on profinite/quotient filtration: static residue information alone is too symmetric to furnish the noncommutative RH interaction.

## 4. Encountered-prefix filtration restores exactly one boundary defect

Move from stationary Haar residues to the actual encountered integer prefixes.

On \(\ell^2(\mathbb N_{\ge1})\), let

\[
S|n\rangle=|n+1\rangle,\qquad
P_{n}=\sum_{1\le m\le n}|m\rangle\langle m|.
\]

Then for every \(n\ge2\),

\[
\boxed{
B_n:=[S,P_{n-1}]=|n\rangle\langle n-1|.
}
\]

This is a rank-one **actualization boundary commutator**. It uses the already-encountered prefix and the one newly admitted state, without looking ahead.

Weight it by the causally computed LCM increment:

\[
\boxed{
D_X=
\sum_{n=2}^X\sqrt{w_n}\,B_n
=
\sum_{p^k\le X}
\sqrt{\frac{\log p}{p^{k/2}}}
\,|p^k\rangle\langle p^k-1|.
}
\]

Because the event sources and targets are distinct orthonormal basis vectors,

\[
\boxed{
D_X^*D_X=
\sum_{p^k\le X}w_{p^k}
|p^k-1\rangle\langle p^k-1|,
}
\]

\[
\boxed{
D_XD_X^*=
\sum_{p^k\le X}w_{p^k}
|p^k\rangle\langle p^k|.
}
\]

Therefore

\[
\boxed{
\|D_X\|^2=\max_{p^k\le X}\frac{\log p}{p^{k/2}}
\le
\sup_{x>1}\frac{\log x}{\sqrt x}
=\frac2e.
}
\]

**This is an unconditional, uniformly bounded, non-anticipating arithmetic birth operator.** The bound is a finite orthogonality fact; it uses no zeta zeros, and is not novel relative to the established diagonal von-Mangoldt defect construction.

## 5. Why this still does not establish Hardy passivity: scalar readout re-coheres the events

The scalar critical prime source is the Fourier transform of the positive atomic distribution:

\[
a_X(\xi)=
\sum_{p^k\le X}
w_{p^k}e^{-i\xi\log(p^k)}.
\]

Let the output event vector and the phase diagonal be

\[
u_X=\sum_{p^k\le X}\sqrt{w_{p^k}}\,|p^k\rangle,
\qquad
V_\xi|q\rangle=e^{-i\xi\log q}|q\rangle.
\]

Then

\[
\boxed{
a_X(\xi)=\langle u_X,V_\xi u_X\rangle,
\qquad
\|u_X\|^2=\sum_{p^k\le X}w_{p^k}.
}
\]

By the classical PNT and partial summation,

\[
\boxed{\|u_X\|^2\sim2\sqrt X.}
\]

The **event-injection operator** \(D_X\) has uniformly bounded norm, but the **coherent scalar observation** uses an event vector of diverging norm. At \(\xi=0\), every permitted past event aligns constructively and

\[
a_X(0)=\|u_X\|^2\sim2\sqrt X.
\]

Thus causal admission and orthogonal event-level encoding do not provide a uniform operator norm for the scalar completed transfer.

Even squared-weight accumulation diverges:

\[
\sum_{p^k\le X}w_{p^k}^2
=
\sum_{p\le X}\frac{(\log p)^2}{p}+O(1)
\sim\frac12(\log X)^2.
\]

So neither the coherent \(\ell^1\)-sum nor the naive orthogonal \(\ell^2\)-sum has a finite infinite-horizon budget.

## 6. Pure adaptation alone does not imply contraction

If \(X_j\) is \(\mathcal F_j\)-measurable, then \(X_{j+1}=2X_j\) is equally adapted with no future data. Yet

\[
\|X_{j+1}\|_2^2=4\|X_j\|_2^2.
\]

Even positivity and a one-way wavefront cannot replace a **storage inequality**.

The actual theorem needed for an RH-strength completed transfer is an independently derived positive state storage \(E_j\) such that

\[
\boxed{
E_{j+1}-E_j+\|y_j\|^2\le\|u_j\|^2
}
\]

on each causal event, and whose completed transfer agrees with Suzuki's \(\Theta_\omega\) in the initially absolutely convergent half-plane for every \(\omega>0\). This is the source-based discrete analogue of passivity/KYP, **not yet constructed**.

A pure unitary update on a larger space can conserve total internal energy, but unless its output is exactly the completed Suzuki observable, such conservation remains RH-inert. The choice of observation and counterterms is the real mathematical debt.

## 7. Next decisive experiment — no cheating

Construct a **chronological, event-adapted observation** \(\mathcal O_{X,\omega}\) between the bounded prefix source \(D_X\) and the completed Gamma/pole state bank. It must be computable from the past filtration and true arithmetic source alone, and must satisfy all of:

1. exact Weil/Suzuki transfer coefficients (including the Archimedean/pole correction) in the Euler-safe domain;
2. exact elimination of forbidden mixed-prime ratio/product Dirac atoms in the physical scalar observation;
3. positive storage / finite-horizon dissipation inequality *derived from a source-defined metric*;
4. correct distinction between \(\omega=1/2\), where known contractivity is unconditional, and all \(\omega>0\), which is RH-equivalent;
5. no fit to zeta zeros, no post hoc target-kernel Gram factorization, no invocation of \(\Psi\ge0\) upstream.

Failure of these conditions should be recorded as a mathematical no-go, not an invitation to invent a different metaphor.

## 8. Claim ledger

**EXACT / STANDARD:** LCM increment \(\Lambda\); Haar conditional expectation identity; filtration orthogonal increments; stationary CRT-SUCC commuting; prefix rank-one commutator; uniform bound on weighted event birth operator.

**KNOWN PRIOR IN REPO:** integer-corner von Mangoldt source and boundary defect (Round006 C100); CRT flatness/no-go; positive local Weyl factors and global renormalization wall.

**UNCONDITIONAL LIMIT:** PNT source bulk \(\sum w_q\sim2\sqrt X\), squared-weight growth \(\sim\frac12\log^2X\).

**STILL UNPROVED:** source-derived completed adapted observation with all-\(\omega\) Hardy passivity; Weil positivity; RH.

**Research interpretation:** The user's "conserve causality" intuition genuinely determines the local source/admissibility operator. It does not yet determine the completed scalar readout or its \(L^2\) passivity.


---

## 9. Rigidity of finite causal unitaries; unilateral SUCC is an isometry with a boundary defect

A particularly important operator-theoretic correction to the "QM cube" analogy is the distinction between **causal isometry** and **finite time-ordered unitary dynamics**.

### Theorem D (classical triangular-unitary rigidity)

Let \(U\) be an \(N\times N\) complex matrix that is both lower triangular in a chronological basis and unitary:

\[
U^*U=UU^*=I,\qquad U_{ij}=0\quad(i<j).
\]

Then \(U\) is diagonal, with diagonal entries of modulus \(1\).

**Proof.** The first row has only \(U_{11}\). Unitarity forces \(|U_{11}|=1\); orthogonality and the norm of the first column force every \(U_{j1}=0\) for \(j>1\). Remove the first row/column and repeat. QED.

Thus **a nontrivial finite-memory causal all-pass system cannot be represented as one finite square lower-triangular unitary on the same input/output timeline.** Additional internal storage, delay/output compression, infinite time, or an enlarged/environmental system is required.

### The unilateral successor is the exact counterpoint

On \(\ell^2(\mathbb N_{\ge1})\),

\[
S|n\rangle=|n+1\rangle.
\]

Then

\[
\boxed{
S^*S=I,\qquad
SS^*=I-|1\rangle\langle1|.
}
\]

It is **causal and isometric** (no energy amplification) but is **not onto**. The boundary defect is exactly

\[
\boxed{
[S^*,S]=|1\rangle\langle1|.
}
\]

This is the standard unilateral-shift/Wold-defect construction; the repository's earlier Round006 C100 already used the source \(|1\rangle\langle1|\) and prime-dilation transport. No novelty is claimed for the basic identity.

At encountered event \(n\), the prefix boundary commutator

\[
[S,P_{n-1}]=|n\rangle\langle n-1|
\]

is the **translated moving wavefront** version of a one-dimensional defect.

### Crucial limit

An isometric \(S\) does **not** mean that a source-weighted superposition \(\sum_q w_q S_q\) is isometric, and it does **not** mean that the scalar Gamma-completed observable is contractive. The latter requires the correct source-defined readout and global storage law.

This theorem is the precise place where "conserve causality" intersects an actual Hilbert-energy invariant without silently assuming RH.


---

## 10. Exact reconciliation with the old integer-corner source (Round006 C100)

Let

\[
E_S=I-SS^*=|1\rangle\langle1|.
\]

Let \(V_m\) be multiplicative dilation on \(\ell^2(\mathbb N_{\ge1})\):

\[
V_m|n\rangle=|mn\rangle.
\]

The earlier repo Round006 identity states

\[
\boxed{
\Lambda_{\mathrm{op}}
=
\sum_{p,k\ge1}
(\log p)\,V_{p^k}E_SV_{p^k}^*
=
\sum_{q=p^k}(\log p)|q\rangle\langle q|.
}
\]

With the diagonal half-density \(R|n\rangle=n^{-1/2}|n\rangle\), the encountered-boundary injection from §4 satisfies

\[
\boxed{
D_XD_X^*
=
P_X R\Lambda_{\mathrm{op}}P_X.
}
\]

So the same von Mangoldt source has **two source-forced forms**:

1. transported initial SUCC defect \(E_S\) along all prime-power dilation rays;
2. weighted moving-prefix SUCC boundary commutators at the actual encountered events.

This equality is a useful reconciliation of *stationary source transport* and *moving event causality*. It is **not new priority**, and the source remains a diagonal positive operator until the completed observation couples the different rays.

The exact missing theorem is still to derive a **stable scalar observation** of this source (coupled to Gamma/pole) without postulating all-\(\omega\) Hardy contractivity.
