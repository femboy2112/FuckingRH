# Complete boundary response and the order of arithmetic centering

**Date:** 2026-10-09. **Status:** proved finite identities, one exact negative control, and finite floating-point diagnostics of the actual Gamma/prime matrices. No RH positivity claim and no priority claim for the classical realization or Schur-complement identities.

## The new dependency edge

The inherited RMP-001 supplies the full memory recurrence. RMP-007 supplies a genuine reversible environment for the independently known positive Gamma and prime energy. Neither identifies that positive energy with the signed Weil form.

This note makes the next finite-network step explicit:

> Eliminating hidden nodes must be applied to the **completed, centered form**. Applying a counterterm only to an already reduced passive network generally gives the wrong boundary law. The missing term is explicitly computable, has a definite sign for scalar centering, and can reverse the answer even in a two-node lossless network.

The exact negative control below does not change any arithmetic coefficient or claim a negative Weil vector. It rejects an inference from finite passivity to positivity after centering. The actual Gamma/prime diagnostic then measures the same correction in the inherited normalization.

| Item | Exact contract |
|---|---|
| Statement attacked | Does passive boundary elimination preserve the intended arithmetic subtraction? |
| Known input | The sourced positive form \(P_A\), the explicit deficit \(D_A\), and the identity \(Q_W=P_A-D_A\). |
| Proved edge | Exact boundary law \(\mathfrak S(P_A-D_A)\), scalar order correction, and fixed-window cutoff stabilization. |
| Novelty type | Application/proof step within this program; classical matrix identities, not a new general realization theorem. |
| Smallest falsifier | Two real nodes, one hidden, all entries rational. |
| Positive control | Increase the retained diagonal by \(1/2\); the correct boundary sign becomes positive. |
| Degenerate control | Zero boundary/interior coupling makes scalar centering commute. |
| Fresh arithmetic check | Sixteen zero-extended step cells at \(A=1/2,1,2\), with exact prime overlap matrices and the Gamma series. |
| Remaining cut | Prove the exact centered boundary form nonnegative with valid control of the eliminated space; finite passivity does not supply this inequality. |

## 1. A finite lossless network has an exact transfer kernel

Let \(\mathcal H_b\) be the port space and \(\mathcal H_i\) the internal state space. Let

\[
U=\begin{pmatrix}A&B\\C&D\end{pmatrix}
\quad\text{on }\mathcal H_b\oplus\mathcal H_i
\]

be unitary. All spaces can be finite dimensional. The time-domain equations are

\[
y_n=A u_n+B x_n,\qquad x_{n+1}=C u_n+D x_n.
\]

For \(|z|<1\), write \(R(z)=(I-zD)^{-1}\). This inverse exists because \(\|D\|\le1\). The zero-initial-state port transfer is

\[
\boxed{S(z)=A+zB(I-zD)^{-1}C.}\tag{1}
\]

In particular, the coefficients \(BD^kC\) retain every port-visible internal excursion. The factor \((I-zD)^{-1}\) must not be replaced by a single pass through the hidden space.

### Exact positive defect kernel

For \(|w|,|z|<1\),

\[
\boxed{
I-S(w)^*S(z)
=(1-\overline w z)\,C^*R(w)^*R(z)C.
}\tag{2}
\]

**Proof.** For \(v\in\mathcal H_b\), put \(x_z=R(z)Cv\). Then

\[
U\binom{v}{z x_z}=\binom{S(z)v}{x_z}.
\]

Apply preservation of inner products to this equation at \((w,u)\) and \((z,v)\). The difference between the input and output internal inner products is \((1-\overline w z)\langle R(w)Cu,R(z)Cv\rangle\). This gives (2). Thus its quotient by \(1-\overline w z\) is a Gram kernel. In particular \(\|S(z)\|\le1\). On the unit circle, wherever the displayed resolvent exists, \(S(z)^*S(z)=I\). For finite equal input/output port dimensions, this is unitarity. \(\square\)

This is the standard conservative realization identity, stated with a disk variable and a fixed block convention. General Schur realization theory supplies existence of a suitable conservative realization for a Schur function; it does not imply that every proposed nonminimal or indefinite realization of that function has a positive state metric. See Ball–Biswas–Fang–ter Horst, Theorem 1.1, for the classical one-variable context [1].

### Initial history and invisible modes

With generating functions \(x(z)=\sum_{n\ge0}x_nz^n\), and similarly for the input/output, direct substitution gives

\[
x(z)=R(z)x_0+zR(z)Cu(z),
\qquad
\boxed{y(z)=S(z)u(z)+BR(z)x_0.}\tag{3}
\]

Therefore the complete boundary law for an arbitrary prepared history includes the second term. A zero-state transfer is not a replacement for the actual environmental state.

There can also be internal states satisfying \(BD^k x_0=0\) for every \(k\ge0\). Boundary data cannot reconstruct those invisible states. Claims of recovery from boundary response alone need an observability assumption or must explicitly restrict to the port-visible part. Unitarity of the full network does not remove this distinction.

For the exact control

\[
U=\begin{pmatrix}3/5&4/5\\-4/5&3/5\end{pmatrix},
\qquad S(z)=\frac{3/5-z}{1-3z/5},
\]

omitting repeated internal returns changes \(S(1/2)\) by \(-24/175\). The initial-history coefficient \(BR(1/2)\) is \(8/7\). These are exact rational checks, not a test of an asymptotic approximation.

## 2. A lossless storage network and its complete dynamic boundary law

Let a finite Hermitian storage matrix be

\[
P=\begin{pmatrix}A&B\\B^*&C\end{pmatrix}>0.
\]

One exact conservative realization is the oscillator system

\[
\ddot q+Pq=0,
\qquad
H(q,\dot q)=\tfrac12\bigl(\|\dot q\|^2+\langle q,Pq\rangle\bigr).
\]

Differentiating \(H\) along the equation gives zero. This provides an ideal lossless linear-network model with a positive conserved energy. It does not use a square root of the Weil form.

For a spectral parameter \(z\notin\sigma(C)\), the boundary/interior equations with no interior forcing are

\[
(A-zI)u+Bv=j_b,
\qquad B^*u+(C-zI)v=0.
\]

Solving the second equation gives the exact dynamic Dirichlet-to-Neumann matrix

\[
\boxed{
F(z)=A-zI-B(C-zI)^{-1}B^*.
}\tag{4}
\]

The inverse retains the internal response at the same spectral parameter. Using the static reduction \(F(0)\), then subtracting \(zI\), generally loses this dependence.

If there is interior forcing \(j_i\), the correct equation is

\[
F(z)u=j_b-B(C-zI)^{-1}j_i.
\]

The induced boundary source must be retained as well. In electrical network language, static elimination of interior variables is Kron reduction; the standard graph-Laplacian formulation and its accompanying source matrix are given in Dörfler–Bullo, equations (1.1)–(1.2) [2]. The oscillator interpretation here uses conservation of stored energy, rather than treating a resistive network as lossless.

### The dynamic response also has an exact kernel

For \(z,w\notin\sigma(C)\),

\[
-\frac{F(z)-F(w)^*}{z-\overline w}
=I+B(C-\overline w I)^{-1}(C-zI)^{-1}B^*.
\tag{5}
\]

The right side is a Gram kernel. This follows from the resolvent identity

\[
(C-zI)^{-1}-(C-\overline w I)^{-1}
=(z-\overline w)(C-\overline w I)^{-1}(C-zI)^{-1}.
\]

Consequently, for \(\operatorname{Im}z>0\),

\[
-\operatorname{Im}F(z)
=(\operatorname{Im}z)\left[I+B(C-\overline z I)^{-1}(C-zI)^{-1}B^*\right]>0.
\]

At a real point away from an interior resonance,

\[
F'(\lambda)=-I-B(C-\lambda I)^{-2}B^*\le-I.
\tag{6}
\]

The derivative records the internal contribution omitted by a static elimination. The sign of \(F(\lambda)\) itself is not forced by losslessness. Equations (5)–(6) hold for every Hermitian \(P\), even if a shifted form \(P-\lambda I\) has negative directions.

## 3. The exact centering-order correction

For a block matrix with an invertible interior block, write

\[
\mathfrak S(P)=A-BC^{-1}B^*.
\]

Let \(\kappa\ge0\) and suppose \(C>\kappa I\). Then

\[
\boxed{
\mathfrak S(P-\kappa I)
=\mathfrak S(P)-\kappa I
-\kappa B(C-\kappa I)^{-1}C^{-1}B^*.
}\tag{7}
\]

**Proof.** Subtract the definitions of the two Schur complements. The difference of inverse interior blocks is

\[
(C-\kappa I)^{-1}-C^{-1}
=\kappa(C-\kappa I)^{-1}C^{-1}.
\]

Since both factors are functions of the same positive Hermitian matrix, their product is positive. This proves (7) and

\[
\mathfrak S(P-\kappa I)\le\mathfrak S(P)-\kappa I.
\]

For \(\kappa>0\), the correction vanishes precisely when \(B=0\). \(\square\)

If \(C\ge cI\) with \(c>\kappa\), its size satisfies

\[
0\le\kappa B(C-\kappa I)^{-1}C^{-1}B^*
\le\frac{\kappa}{c(c-\kappa)}BB^*.
\tag{8}
\]

Thus a proved interior gap and coupling bound can turn a boundary estimate into a valid sufficient certificate. Merely observing a positive static boundary value cannot.

### Exact two-node sign reversal at every cutoff

For every integer \(N\ge0\), set

\[
P_N=\begin{pmatrix}N+7/4&-1\\-1&N+2\end{pmatrix},
\qquad D_N=(N+1)I.
\tag{9}
\]

The storage form is visibly positive:

\[
\langle(u,v),P_N(u,v)\rangle
=|u-v|^2+(N+3/4)|u|^2+(N+1)|v|^2.
\]

It is a two-node network with a positive connecting term and positive grounded storage terms. The associated oscillator dynamics above is lossless for every \(N\).

Its centered form is independent of \(N\):

\[
Q=P_N-D_N=
\begin{pmatrix}3/4&-1\\-1&1\end{pmatrix}.
\]

Reducing the passive storage first and subtracting only at the retained node gives

\[
\mathfrak S(P_N)-(N+1)
=\frac34-\frac1{N+2}>0.
\]

The correct centered boundary form is

\[
\boxed{\mathfrak S(Q)=\frac34-1=-\frac14.}\tag{10}
\]

At retained value \(u=1\), the minimizing hidden value is \(v=1\), and \(Q(1,1)=-1/4\). The omitted correction is \((N+1)/(N+2)\), tending to one. In particular, the wrong sign rule passes at **every** finite cutoff and in its limit, while the correct sign is negative at every cutoff.

If the centered hidden block is \(\varepsilon>0\), the error can be arbitrarily large. The alternative matrix \(P=\left(\begin{smallmatrix}2&-1\\-1&1+\varepsilon\end{smallmatrix}\right)\), \(\kappa=1\), gives

\[
\mathfrak S(P)-1=\frac{\varepsilon}{1+\varepsilon}>0,
\qquad
\mathfrak S(P-I)=1-\frac1\varepsilon.
\]

The omitted amount is \(1/[\varepsilon(1+\varepsilon)]\). This quantifies why a hidden spectral gap is part of the certificate, not a dispensable technical condition.

### Rank-one pole terms must also be subtracted before reduction

For a general explicitly known deficit \(D\), the blocks of \(Q=P-D\) are

\[
Q_{bb}=P_{bb}-D_{bb},\quad
Q_{bi}=P_{bi}-D_{bi},\quad
Q_{ii}=P_{ii}-D_{ii}.
\]

When \(Q_{ii}>0\), the exact law is

\[
\boxed{
\mathfrak S(Q)
=P_{bb}-D_{bb}
-(P_{bi}-D_{bi})(P_{ii}-D_{ii})^{-1}(P_{ib}-D_{ib}).
}\tag{11}
\]

For example, take \(P=2I\), \(D=\frac12I+\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)\). This is a nonnegative scalar-plus-rank-one deficit. The boundary-only subtraction gives \(1/2\). The correct centered matrix is \(\left(\begin{smallmatrix}1/2&-1\\-1&1/2\end{smallmatrix}\right)\), with boundary Schur complement \(-3/2\). Its minimizing witness at boundary value one is \((1,2)\). Thus even an originally uncoupled positive storage matrix can acquire essential boundary/interior coupling from the pole subtraction.

The full finite sign criterion follows by completing the square:

\[
\begin{aligned}
Q(u,v)
={}&\langle v+Q_{ii}^{-1}Q_{ib}u,
Q_{ii}(v+Q_{ii}^{-1}Q_{ib}u)\rangle\\
&+\langle u,\mathfrak S(Q)u\rangle.
\end{aligned}
\tag{12}
\]

Under the stated strict interior positivity, \(Q\ge0\) if and only if \(\mathfrak S(Q)\ge0\). If an interior negative direction exists, it is already a negative direction of the full form. Zero interior modes require a separate range/kernel analysis; an ordinary inverse formula is not valid there.

## 4. What the arithmetic cutoff actually does

Fix \(A>0\) and \(H_A=L^2(-A,A)\). All translates below act on the **zero extension to the real line**. Use the inherited normalization

\[
a_n=\frac{\Lambda(n)}{\sqrt n},\quad
E_{\rm prime,A}[f]=\sum_{n\le e^{2A}}a_n\|f-\tau_{\log n}f\|^2,
\quad M_A=\sum_{n\le e^{2A}}a_n.
\]

Let

\[
P_A[f]=E_\Gamma[f]+E_{\rm prime,A}[f]+2|C_f|^2,
\quad
D_A[f]=d_A\|f\|^2+2|S_f|^2,
\]

where

\[
C_f=\int f(x)\cosh(x/2)\,dx,\quad
S_f=\int f(x)\sinh(x/2)\,dx,
\quad d_A=\log\pi-\psi(1/4)+2M_A.
\]

The previously proved source identity is

\[
Q_W[f]=P_A[f]-D_A[f].\tag{13}
\]

The Gamma form gives a strictly positive closed \(P_A\), with its stated zero-extension form domain. No positivity of (13) is used below.

### Finite prime-power cutoff

If a cutoff \(X\ge e^{2A}\) retains all \(n\le X\), then every newly admitted shift has disjoint support from \(f\), up to a null set. Thus

\[
P_X=P_A+t_XI,\qquad D_X=D_A+t_XI,
\quad t_X=2\sum_{e^{2A}<n\le X}a_n,
\quad P_X-D_X=P_A-D_A.
\tag{14}
\]

These are closed-form identities on the fixed space \(H_A\), not only limits of scalar computations.

### Finite prime cascades include all powers

The finite Euler all-pass cascade indexed by a finite set of primes \(\mathcal P\) includes every power of each prime. Its mass is

\[
\boxed{M_{\mathcal P}
=\sum_{p\in\mathcal P}\sum_{k\ge1}\frac{\log p}{p^{k/2}}
=\sum_{p\in\mathcal P}\frac{\log p}{\sqrt p-1}.}\tag{15}
\]

This mass is finite for a finite prime set. If \(\mathcal P\) contains every prime at most \(e^{2A}\), the powers above the support threshold again contribute only a diagonal tail. Hence

\[
\boxed{
P_{\mathcal P}=P_A+2(M_{\mathcal P}-M_A)I,
\quad D_{\mathcal P}=D_A+2(M_{\mathcal P}-M_A)I.
}\tag{16}
\]

In particular, \(P_{\mathcal P}-D_{\mathcal P}=Q_W\) exactly on the window. A finite-prime cascade and a finite-prime-power cutoff have different positive masses; replacing one by the other without the compensating diagonal tail changes the normalized response.

As the prime set exhausts all primes, \(M_{\mathcal P}\to\infty\). An elementary proof uses

\[
M_{\mathcal P}\ge\sum_{p\in\mathcal P}\frac{\log p}{\sqrt p}
\ge\sum_{\substack{p\in\mathcal P\\p\ge3}}\frac1p.
\]

If the prime reciprocal sum converged, then the finite Euler products \(\prod_{p\le N}(1-1/p)^{-1}\) would stay bounded, since \(-\log(1-1/p)\le2/p\). Their geometric expansions include every reciprocal \(1/n\) with \(n\le N\), so they dominate the divergent harmonic sums. This is a contradiction.

Therefore the uncentered positive storage diverges on every nonzero compactly supported vector. The centered form remains exactly fixed. A full positive prime jump measure is not obtained by dropping this cancellation.

### Relation to scattering delay

The derivation in [PRIME_FILTERS_AND_WEIL_DELAY.md](PRIME_FILTERS_AND_WEIL_DELAY.md) identifies the positive Gamma and prime energies with drops of finite all-pass scattering delays and identifies the signed total delay, including its arithmetic centering, with the Weil formula after the polar terms are restored. Equations (13)–(16) specify the boundary-reduction consequence of that identification: the matrix to eliminate is the completed \(P_{\mathcal P}-D_{\mathcal P}\), with the same all-powers mass in both terms.

This note does not derive the source all-pass factors again and does not identify the raw passive cascade with the Suzuki operator. Its result is independent of the sign of the exact completed delay.

## 5. A passive limit can erase the entire centered quantity

The cutoff has an additional precise effect. Let \(P_0>0\) be the closed positive storage operator on a fixed window, and let \(P_t=P_0+tI\), \(t\to\infty\). For a fixed real \(\tau>0\), set

\[
R_t=(P_t+\tau I)^{-1},\qquad
S_t=(P_t-\tau I)(P_t+\tau I)^{-1}=I-2\tau R_t.
\]

The spectral theorem gives

\[
\|R_t\|\le\frac1{t+\tau},\qquad
\|S_t-I\|\le\frac{2\tau}{t+\tau}.
\tag{17}
\]

Every \(S_t\) is contractive; the operator-norm limit is the same identity for every choice of \(P_0\). This known positive-storage Cayley response is not being identified with the completed arithmetic scattering function.

The centered data survives in a subleading, rescaled coefficient:

\[
\boxed{
tI-t^2R_t=t(P_0+\tau I)(tI+P_0+\tau I)^{-1}.
}\tag{18}
\]

On the operator domain of \(P_0\), this tends strongly to \(P_0+\tau I\). On its form domain, the corresponding quadratic forms increase to \(P_0[f]+\tau\|f\|^2\), by monotone convergence of \(t\lambda/(t+\lambda)\). Outside that form domain the limit is infinite. In a fixed finite-dimensional compression the convergence is in operator norm, with error at most \(\|P_0+\tau I\|^2/t\).

Consequently, for \(D_t=D_0+tI\), the exact signed form can be recovered as

\[
Q[f]=\lim_{t\to\infty}\left[
t\|f\|^2-t^2\langle f,R_tf\rangle
-\tau\|f\|^2-D_0[f]\right].\tag{19}
\]

Positivity of \(R_t\), contractivity of \(S_t\), and their unscaled limits do not determine the sign after this subtraction. Already in one dimension, \(P_t=t+1\) and \(P_t=t+3\) have positive unshifted storage. Subtracting the same \(D_t=t+2\) gives opposite signs, while both Cayley responses tend to one.

### Eliminating before centering has a different limit

For a finite matrix

\[
P_t=\begin{pmatrix}A_0+tI&B_0\\B_0^*&C_0+tI\end{pmatrix},
\quad D_t=(d_0+t)I,
\]

one obtains

\[
\mathfrak S(P_t)-(d_0+t)I
=A_0-d_0I-B_0(C_0+tI)^{-1}B_0^*
\longrightarrow A_0-d_0I.
\tag{20}
\]

The correct centered Schur complement is the constant

\[
A_0-d_0I-B_0(C_0-d_0I)^{-1}B_0^*.
\]

Thus the incorrect order suppresses the hidden coupling precisely in the large positive-mass limit. The rational family (9) realizes this error with the wrong and correct signs separated uniformly.

## 6. Executable evidence and its limits

Run `scripts/boundary_centering_probe.py` with the explicit output argument in [PROVENANCE_AND_CLAIMS.md](PROVENANCE_AND_CLAIMS.md). Its complete report is [boundary_centering_results.json](evidence/boundary_centering_results.json).

The exact `Fraction` controls verify the colligation cross-kernel on sixteen rational pairs, reject omission of internal returns, and certify both scalar and rank-one centering sign reversals. The nearly resonant control makes the omitted correction grow from \(100/11\) to \(1000000/1001\), while the incorrect boundary answer remains positive.

For the actual-source diagnostic, normalized step indicators have width \(\delta=2A/16\). The Gamma matrix is evaluated from

\[
G_0=\frac2\delta\sum_{j\ge0}\frac{1-e^{-b_j\delta}}{b_j^2},
\qquad
G_l=-\frac1\delta\sum_{j\ge0}
\frac{e^{-b_j(l-1)\delta}(1-e^{-b_j\delta})^2}{b_j^2},
\quad b_j=2j+\tfrac12.
\]

The non-exponential series is included through \(\sum b_j^{-2}=\psi_1(1/4)/4\). Only exponentially decaying remainders are truncated. Prime translates use exact interval-overlap lengths; their energy matrix is \(a_n(2I-T_h-T_h^*)\). Taking the square of a shift compressed to the window/cell space is deliberately tested as a false mutation: it loses escaped energy.

The table uses the eight-dimensional even subspace, where \(S_f=0\), so the deficit is exactly scalar. One coordinate is retained and seven eliminated. Values are floating-point diagnostics, not interval certificates.

| \(A\) | Incorrect reduce-then-center | Correct centered boundary | Required hidden correction |
|---:|---:|---:|---:|
| 0.5 | 1.503938365076 | 0.472315095664 | 1.031623269412 |
| 1.0 | 0.846744319956 | 0.269136831992 | 0.577607487965 |
| 2.0 | 0.213011287131 | 0.123900045781 | 0.089111241350 |

The correction identity residual is below \(6\times10^{-14}\) in these controls. Extra prime terms beyond the fixed support obey the predicted common scalar increment to the same floating-point scale. A separate check includes every power of each prime through 1000 using the geometric tail (15), and verifies the same centered matrix.

These tests measure a real error made by an incorrect reduction order in the sourced matrices. They do not demonstrate a sign change of the actual Weil form. The exact rational witness proves that a method accepting the wrong order could report a false positive on an admissible passive network.

## 7. The resulting proof obligation

For any proposed finite recursive circuit or Galerkin reduction:

1. Specify the full transfer or dynamic boundary law, including internal sources and the port-visible histories.
2. Derive the exact arithmetic completion on that same state space, with the all-powers mass and the scalar/pole blocks fixed by the source normalization.
3. Subtract that completion before eliminating internal variables. Use (11), including its hidden inverse and all pole cross terms.
4. Prove an interior lower bound and a nonnegative resulting boundary form. In an infinite-dimensional reduction, also prove the relevant closed form domain, bounded inverse/coupling maps, and convergence; a formal finite Schur complement is insufficient.

These steps do not assume \(Q_W\ge0\). The final inequality is still the missing arithmetic sign statement. If it is proved for every compact window on the inherited core, the prior Weil criterion and the exact Suzuki form tangent provide the intended downstream bridge. None of the passive identities above is substituted for that inequality.

## Sources and provenance

- **Inherited source identities:** `research/2026-10-09/reversal_memory_polarization/HISTORY_AND_POLARIZATION.md`, RMP-001 and RMP-007; and `research/aletheia_2026-10-07/succ_weil_suzuki/GAMMA_ENERGY_COMPACT_SIGN_OPERATOR.md at e6f2d087`, SWS-004–006. Those files were read before choosing this task, so the recurrence, positive-energy dilation, and horizon cancellation are not claimed as new here.
- **Inherited Suzuki interface:** [FULL_SUZUKI_WEIL_TANGENT.md](https://github.com/femboy2112/FuckingRH/blob/e6f2d08716cc699efec10eafd6738e770615bc76/research/aletheia_2026-10-07/succ_weil_suzuki/FULL_SUZUKI_WEIL_TANGENT.md).
- **Audited older framing:** [Round006 PASSIVE_COLLIGATION.md at 344facc9](https://github.com/femboy2112/FuckingRH/blob/344facc9b9eccadcf7fe98af9361b6e7fd3ea737/research/claude_round_006/PASSIVE_COLLIGATION.md). An RH-equivalent sufficient construction is not thereby logically impossible to prove unconditionally. Positivity of an underlying Hilbert metric must also be distinguished from an additional shifted-function positivity condition. This note does not inherit the older no-go inference.
- **[1]** J. A. Ball, A. Biswas, Q. Fang, S. ter Horst, *Multivariable generalizations of the Schur class: positive kernel characterization and transfer function realization*, arXiv:0705.2042, Theorem 1.1 for the classical one-variable context. [Primary paper](https://arxiv.org/pdf/0705.2042). Equations (1)–(3) above are proved directly in the chosen block convention.
- **[2]** F. Dörfler and F. Bullo, *Kron Reduction of Graphs with Applications to Electrical Networks*, arXiv:1102.2950; especially equations (1.1)–(1.2), the definition of Schur reduction, and the diagonal-perturbation analysis around Theorem 3.7. [Primary paper](https://arxiv.org/pdf/1102.2950). Equations (4)–(12) are directly proved above, so no network assumption is imported without its matrix hypotheses.
