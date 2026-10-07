# Corrected RH proof interface — Markov source versus causal Hardy innerness

**Date:** 2026-10-07  
**Branch:** \`audit/claude-critique-provenance-2026-10-07\`  
**Status:** rigorous separation of exact finite stochastic arithmetic from the RH-strength analytic continuation/causality gate. **RH remains open.**

**Provenance:**
- User-origin heuristic: cube/actualization, prime conductor birth, Mellin–Dirac/Gamma bridge, causal light-cone intuition.
- Prior independent critical input: [CUBE_ATOM_CRITICAL_AUDIT_IMPORTED.md](CUBE_ATOM_CRITICAL_AUDIT_IMPORTED.md) (original user-Library authorship **not independently established**).
- Published base: Masatoshi Suzuki, *A canonical system of differential equations arising from the Riemann zeta-function*, [arXiv:1204.1827v2](https://arxiv.org/abs/1204.1827v2), Proposition 1.2, Proposition 2.1, Theorem 2.2; and Suzuki, *Weil's quadratic form via the screw function*, [arXiv:2606.09096v3](https://arxiv.org/abs/2606.09096v3), (2.3)–(2.11).
- Claim-by-claim first-commit attribution and verification status: [RH_CLAIM_PROVENANCE_LEDGER.md](RH_CLAIM_PROVENANCE_LEDGER.md).

## 1. Finite prime-source process is exactly solvable

Fix a **finite** set \(\mathcal E\) of prime-power conductor events \(e=p^k\). Let independent clock times satisfy

\[
T_e\sim\operatorname{Exp}(2\log p).
\]

The birth bit

\[
B_e(\omega)=1_{T_e\le\omega}
\]

has

\[
\boxed{
\Pr(B_e(\omega)=1)=1-p^{-2\omega}.
}
\]

For \(n=\prod_{p\mid n}p^{k_p}\), let

\[
I_n(\omega)=\prod_{p\mid n}B_{p^{k_p}}(\omega).
\]

Then, exactly,

\[
\boxed{
b_\omega(n)=n^{\omega-\frac12}\,\mathbb E I_n(\omega)
=n^{\omega-\frac12}\prod_{p\mid n}(1-p^{-2\omega}).
}
\]

This is the standard Jordan-totient/Suzuki coefficient. It needs no zeros and is nonnegative for real \(\omega>0\).

The finite-\(\mathcal E\) backward generator is

\[
\boxed{
(\mathcal L_{\mathcal E}f)(b)
=
\sum_{e=p^k\in\mathcal E}
2(\log p)(1-b_e)\bigl[f(b^{e\to1})-f(b)\bigr].
}
\]

Its coordinatewise first derivative at \(\omega=0^+\) satisfies

\[
\boxed{
\frac12\partial_\omega b_\omega(n)\big|_{0^+}
=
\frac{\Lambda(n)}{\sqrt n}.
}
\]

This proves the **finite source**. It does not establish Hardy invariance, a projectively consistent conductor measure under gcd, or global analytic continuation.

## 2. Genuine obstruction to smooth finite-dimensional coherent activation

Suppose a fixed-Hilbert-space family \(U_\omega\Omega\) is norm differentiable at \(\omega=0\), and \(P\) projects onto a channel initially unoccupied:

\[
PU_0\Omega=0.
\]

Then

\[
PU_\omega\Omega
=\omega v+o(\omega)
\]

and

\[
\boxed{\|PU_\omega\Omega\|^2=O(\omega^2).}
\]

The true birth probability is instead

\[
1-p^{-2\omega}=2\omega\log p+O(\omega^2).
\]

Thus a **smooth fixed-space unitary birth** cannot realize this law. A fresh environment/ancilla, singular \(\sqrt\omega\) amplitude, or a Markov/Lindblad semigroup is required.

The rotation

\[
R_\omega=\begin{pmatrix}p^{-\omega}&-\sqrt{1-p^{-2\omega}}\\
\sqrt{1-p^{-2\omega}}&p^{-\omega}\end{pmatrix}
\]

is unitary for each fixed \(\omega\), but repeating it on the same two-state system coherently does not produce repeated Markov birth probabilities. At \(p=2,\omega=\frac12\), \(R_\omega\) is a \(45^\circ\) rotation, and \(R_\omega^2\) takes the vacuum to the excited channel with probability \(1\), not \(1/2\).

Therefore unitarity of an isolated Gamma or cube phase is not a causal stochastic refinement theorem.

## 3. Safe-region transfer and what is missing

For

\[
\Re s>\frac12+\omega,
\]

the coefficients have an absolutely convergent Dirichlet series

\[
\boxed{
D_\omega(s)
=
\sum_{n\ge1}b_\omega(n)n^{-s}
=
\frac{\zeta(s+\frac12-\omega)}
{\zeta(s+\frac12+\omega)}.
}
\]

Multiply by the **explicit** pole/Gamma factor to obtain the completed ratio

\[
B_\omega(s)
=
\frac{\xi(s+\frac12-\omega)}
{\xi(s+\frac12+\omega)}.
\]

With \(s=-iz\), this is Suzuki's

\[
\boxed{
\Theta_\omega(z)=
\frac{\xi(\frac12-\omega-iz)}
{\xi(\frac12+\omega-iz)}.
}
\]

The product/functional equation gives

\[
|\Theta_\omega(t)|=1
\qquad(t\in\mathbb R)
\]

without assuming RH.

This real-boundary identity is **not** Hardy invariance. For example,

\[
F(z)=\frac{z+ia}{z-ia}
\]

has modulus \(1\) on the real line but a pole at \(z=ia\) in the upper half-plane.

### Exact RH proof gate

Suzuki's Proposition 1.2 and Theorem 2.2 distinguish the missing condition:

\[
\boxed{
\Theta_\omega\text{ is meromorphic inner in }\mathbb C_+
\qquad\text{for every }\omega>0.
}
\]

That is RH-equivalent; it requires that the **complete transfer** is holomorphic/contractive in the upper half-plane, not merely unimodular on the boundary. A model realizing only the finite positive Markov coefficients and Gamma factors, without this property, has not progressed beyond the safe Euler half-plane.

## 4. Why generic finite positivity cannot settle the issue

Replace the true rates \(2\log p\) by any arbitrary positive rates \(\lambda_e\). The independent-birth generator remains a perfectly valid Markov generator; its associated finite probabilities and positive Gram matrices are still nonnegative. Yet the Euler coefficients no longer match \(\zeta\) in general.

Therefore:

\[
\boxed{
\text{Markov positivity alone is RH-inert}.
}
\]

The analytic obstruction resides in coupling the **true arithmetic rates and conductors** to the completed Archimedean/pole transfer so as to preserve the causal Hardy subspace. This coupling must be *derived*, not selected after seeing the desired \(\Theta_\omega\) or Weil form.

## 5. Physical observation must respect the Weil atomic spectrum

Finite cubical interactions may create mixed internal conductors. But the arithmetic distribution in Weil's formula has translation atoms only at

\[
\pm\log p^k.
\]

A generic unreflected Gram of mixed prime features produces ratio lines \(\log(p^j/q^k)\). A generic Hankel reflection changes those into product lines \(\log(p^jq^k)\). For distinct prime bases, neither family may appear as an extra scalar Weil atom.

Thus a candidate source-derived observation must simultaneously:

1. produce the exact prime-power coefficients;
2. eliminate spurious product/ratio atoms;
3. produce the exact Gamma/pole/boundary scalar correction;
4. establish Hardy causality for **all** \(\omega>0\);
5. respect the fixed-horizon finite Weil \(Q_W^a=P_a-D_a\) with the exact Suzuki normalization.

## 6. Noncircular acceptance gate

A genuinely proof-bearing theorem would independently construct an operator/network \(\mathscr U_\omega\) from SUCC/carry/conductor birth and Gamma state-space data, such that:

- its transfer agrees with \(B_\omega(s)\) on the **Euler-safe half-plane**, verified algebraically;
- **without using zeros or RH-equivalent sign bounds**, it extends as a contraction multiplier of \(H^2(\Re s>0)\);
- the extension is proved uniformly in the necessary deformation parameters and on every causal horizon;
- the exact completed Weil first variation is recovered, rather than a positive proxy;
- fake-prime, gamma perturbation, product/ratio atomic, and inverse Blaschke controls fail appropriately.

Then Suzuki's published equivalence would imply RH.

We have not constructed this network. The statement above is **a specification of the missing RH theorem**, not an unconditional reduction.

## 7. Relationship to the finite Feshbach route

The audited finite spectral program gives

\[
Q_W^a=P_a-D_a,
\]

where \(P_a\) is the exact positive zero-extended logarithmic energy plus genuine prime-power Dirichlet squares, and \(D_a\) is source-derived and bounded for each finite \(a\). The finite low-mode Feshbach matrix is an exact *coordinate choice* for the remaining sign.

The Suzuki inner-function route is the **causal/transfer** form of the same unresolved analytic positivity, not a second proof.

Do not claim that proving compact resolvent, a logarithmic eigenvalue lower bound, or a finite KMS prime-ray gap proves upper-half-plane analyticity. Those statements are true for much wider classes of fake arithmetic sources.

## 8. Verdict

**Proved/standard:** finite Markov conductor source; first von-Mangoldt jet; smooth fixed-unitary birth obstruction; Hardy-invariance counterexample; Suzuki published innerness criterion.

**Refuted:** gcd-projective measure, repeated coherent unitary Markov refinement, Mellin-transfer-preserving singularity removal, real-axis unitarity as RH evidence.

**Unpaid and RH-equivalent:** all-\(\omega\) completed causal Hardy contractivity or all-interval Weil positivity.

**RH remains open.**
