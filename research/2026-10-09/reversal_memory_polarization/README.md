# Reversing the complete history: memory, duality, and polarization

**2026-10-09. RH remains open.** This checkpoint develops Leah's teacup/time-reversal axis into exact operator and test-space statements. It also audits the proposed “missing dualizing sheaf” explanation against primary literature available on this date.

The central finding is that **reversal needs a complete history, while the RH step needs a positive pairing compatible with that history**. These are different requirements. We now have explicit tests that distinguish them.

This work extends the existing history-conditioned-reversal, Hecke–Tate, arithmetic–Poisson, and succ–Weil–Suzuki branches. Their results are not counted again as discoveries. The frozen base is main at f2fe8b3f2e2953061bcc64c51c86521a66e72bcf, including Round064. Exact donor commits, claim states, commands, and primary sources are in [PROVENANCE_AND_CLAIMS.md](PROVENANCE_AND_CLAIMS.md).

## Read the mathematical development

- [HISTORY_AND_POLARIZATION.md](HISTORY_AND_POLARIZATION.md): full-history memory theorem; positive primitive-erasure obstruction; duality versus polarization; Frobenius common-history Grams; singular energy clock; the ordinary Hilbert-cokernel obstruction.
- [DUALITY_WEIL_AND_GREEN.md](DUALITY_WEIL_AND_GREEN.md): the corrected geometric comparison; exact Connes–Consani/Weil normalization; compact retarded/advanced reconstruction; the concrete role of duality at infinity.
- [Reproducible probe](../../../scripts/reversal_memory_polarization_probe.py) and [raw results](evidence/probe_results.json). Integer/rational certificates are explicitly separated from numerical quadrature diagnostics.

## 1. What the teacup analogy becomes

Suppose the full state is (x,e), with x the recorded shadow and e the unresolved environment. Full reversible dynamics can reconstruct the earlier state from the **complete final state**. The current x alone need not determine the earlier x.

This is more than changing the sign of an increment. Reversing a sequence reverses its order, reverses each microscopic operation, and restores the environmental state and phase correlations that the forward observation omitted. An adjoint requires a specified pairing; it equals an inverse only under the corresponding isometry/unitarity conditions. A Bayes reverse depends on the actual distribution and is generally a conditional law, not an inverse trajectory.

The earlier branch already made these distinctions and derived normalized child recombination and mixed inverse/forward ratio echoes. This checkpoint adds an explicit memory law. If a unitary has observable/environment blocks

$$
U=\begin{pmatrix}A&B\\C&D\end{pmatrix},
$$

then eliminating an initially empty environment gives

$$
x_{n+1}=Ax_n+\sum_{j=0}^{n-1}BD^{n-1-j}Cx_j.
$$

Repeated use of A drops the memory term. A three-state exact example has A=0, yet the full state returns at the third step. Two examples with identical first-step shadows have opposite third-step return amplitudes. The missing quantity is a history correlation, not an unobserved change of sign.

“Advanced reconstruction” below is an analysis of a completed history. It does not authorize an online shadow-succ process to consume future arithmetic events.

## 2. An exact bridge to the primitive Weil core

Put

$$
L=\partial_t^2-\tfrac14,\qquad
M_\pm(v)=\int_{\mathbb R}e^{\pm t/2}v(t)\,dt.
$$

We prove

$$
L:C_c^\infty(\mathbb R)\overset{\sim}{\longrightarrow}
\{v\in C_c^\infty:M_+(v)=M_-(v)=0\}.
$$

The retarded, advanced, and decaying Green inverses agree on this domain. Their disagreement on an arbitrary test v is exactly

$$
(G_+-G_-)*v
=e^{t/2}M_-(v)-e^{-t/2}M_+(v).
$$

Under the half-density substitution f(u)=u^{-1/2}v(log u), these two moments are precisely Connes–Consani's degree/codegree constraints. This is a rigorous connection between “past and future reconstruct the same object” and the actual primitive test space. Ordinary zero mean does not suffice.

We also derive the exact real-test comparison

$$
Q_W(v)=2(C(v)^2-S(v)^2)-2s_{\rm CC}(f,f).
$$

On the primitive core, C=S=0 and Q_W=-2s_CC. Thus there is an exact common Weil pairing after declaring coordinates, sign, factor, and domain. This does **not** identify every repository-specific splitting Q=P-K with a particular Connes–Consani operator construction.

Neither the Green identity nor the coordinate comparison proves the remaining sign.

## 3. Composite history is needed even when its connected source vanishes

For the Euler partition series, the state at 6 is present while its **independent connected log-derivative charge** is zero. These statements are compatible. The logarithm extracts connected contributions; it does not erase the state or its correlations.

We prove a sharper obstruction to literal positive erasure. A unital completely positive map that fixes the prime unitaries must also fix their mixed products. A weighted four-point version at {1,2,3,6}, with half-density weights 1/sqrt(2),1/sqrt(3), becomes indefinite if both mixed correlations are erased:

$$
\lambda_{\min}=1-\frac1{\sqrt2}-\frac1{\sqrt3}<0.
$$

Retaining the product correlations instead gives minimum eigenvalue

$$
(1-1/\sqrt2)(1-1/\sqrt3)>0.
$$

This rules out a specific architecture: “keep each prime channel exactly and delete all composite/ratio histories by a positive map.” It does not rule out nonlinear connected extraction, source-sensitive signed intermediate maps, or a larger positive global representation.

## 4. Duality is not yet a positive polarization

A perfect duality can pair a spectral value rho with 1-rho without putting either on the critical line. Our exact two-dimensional countermodel has eigenvalues 3/4 and 1/4 and satisfies both the weight-one alternating pairing identity and a normalized reversal identity.

A precise sufficient condition is a compatible positive metric G satisfying

$$
D^TG+GD=G.
$$

Then D-1/2 is skew-adjoint in that finite-dimensional metric. We derive this from a compatible complex structure J with G=BJ>0 and DJ=JD. This is an elementary model of the extra positive-star compatibility in Deninger's conjectural framework. A candidate J must come from arithmetic geometry/dynamics; fitting it to a desired spectrum pays none of the construction debt.

The infinite-dimensional version additionally needs domains, closures, and exact recovery of the completed zeta object. A formal integration-by-parts identity does not by itself give a skew-adjoint generator.

## 5. What the finite-field model actually supplies

For a smooth projective curve over F_q, intersection theory on C×C and the Hodge index theorem give the Hasse–Weil bounds. Equivalently, the Jacobian's polarization gives a positive Rosati trace pairing and

$$
\pi^\dagger\pi=q.
$$

The normalized Frobenius is therefore an isometry in a positive endomorphism-trace model. This is the substantive model for reversal plus positivity.

We extend the repository's one-time genus-one calibration to **one positive pairing across several times**. If a_n=q^n+1-N_n and a_0=2g, then

$$
\left(q^{\min(i,j)}a_{|i-j|}\right)_{i,j=0}^m\succeq0.
$$

Nine actual elliptic curves y²=x³−4 over F_p, p=5 through 31 excluding the bad primes, pass after independent point counts over F_p and F_p².

The forged reciprocal polynomial

$$
X^4+6X^3+27X^2+30X+25
$$

has q=5, g=2, N_1=12 and N_2=44. It passes both individual Hasse bounds and every two-by-two principal Gram check. Its three-time Gram has determinant -12160, and vector (4,1,1) has quadratic value -68. It cannot be a positive Frobenius history. No actual curve is claimed for this polynomial.

This test catches a compatibility failure that separate observations conceal.

## 6. Correcting the “missing sheaf” account

The valuable part of the proposed comparison is the demand for an independently positive structure identified with the arithmetic form. The stronger historical claims need correction:

- Arakelov geometry already contains archimedean metrics, arithmetic intersection theory, arithmetic Riemann–Roch, and arithmetic Hodge index theorems under stated hypotheses.
- Connes–Consani have proved Riemann–Roch/Serre-duality constructions for compactified Spec Z, including subsequent refinements and a 2026 Picard/duality development.
- These results do not establish an RH-sufficient Hodge pairing on the proposed arithmetic self-product.
- Riemann–Roch is an index identity. Deriving the relevant sign requires additional geometry, effectivity/existence arguments, or a positive polarization.
- An F_1 surface is one proposed host. No audited source proves that every possible RH proof must construct its dualizing sheaf.
- The 2025–2026 Connes–Consani–Moscovici spectral route has specifically stated ground-state and convergence obligations. Those cannot be replaced by a blanket “surface absent” diagnosis.

The corresponding forward question is: **what arithmetic construction provides the duality datum, the compatible positive polarization, and an exact trace/form identity on the same nontrivial space?**

## 7. The next proof obligation, made operational

The chosen direction is to retain full arithmetic histories and attack their **polarized sewing**, rather than optimize an isolated scalar defect. “Sewing” here means composing a history with its properly paired reverse in one common representation.

A candidate must specify an algebra of histories, a sourced representation, its test-function topology, its involution, and the functional that evaluates a forward/reverse pair. The finite principal Gram matrices

$$
G_{ij}=\ell(a_i^\dagger a_j)
$$

are its first discriminating probes. Construct them from arithmetic operations and the global additive/Poisson completion before imposing positivity. Include prime, composite, inverse-prime, ratio, and archimedean histories. Preserve encountered-event causality.

Three independent obligations remain:

1. **Arithmetic fidelity:** actual locations log(p^k), weights chi(p)^k log(p)/p^{k/2}, conductor/parity, and global Fourier/Poisson compatibility. Existing donor work provides exact source controls.
2. **Positive compatibility:** one canonical positive pairing for all admissible histories, with the correct reversal and a justified completion. The positive-erasure and forged-history controls must distinguish invalid constructions.
3. **Full target identity:** identify the resulting primitive or completed pairing with Q_W on an adequate core, including Gamma, poles, origin terms, and limits. A construction of the positive Gamma/prime energy alone is insufficient.

Two concrete failures already narrow the search. A smooth microscopic clock gives the wrong order for a nonzero Suzuki defect tangent unless a singular time scaling or dilation is present. We construct a genuine unitary history-translation dilation for the known positive Gamma/prime energy: its prepared history has a sharp present-time boundary, which explains the required lack of differentiability and retains the full outgoing environmental record. The full Weil subtraction is still unpaid. Also, the closed multiplication realization of zeta on ordinary L² has dense range and zero reduced Hilbert cokernel; it cannot by itself be the desired nontrivial spectral cohomology.

The results here settle several necessary structural questions and provide exact falsifiers. They do not supply the remaining arithmetic positive functional or the missing global sign.

