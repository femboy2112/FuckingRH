# Causality, phase-only response, and the completed Weil form

**2026-10-09.** Mathematical audit within the lossless-arithmetic-circuit checkpoint. Standard tools applied here; no priority claim or RH proof.

## 1. An exact wrong-arrow control

Use Laplace \(p=-iz\), so \(\Re p>0\) corresponds to \(\Im z>0\), with \(\widehat f(z)=\int f(t)e^{izt}\,dt\). Causality means support in \(t\ge0\).

For \(a>0\), set
\[
S_+(p)=\frac{p-a}{p+a},\qquad S_-(p)=\frac{p+a}{p-a}.
\]
Both have real coefficients, boundary modulus one, and \(S_\pm(p)S_\pm(-p)=1\). Only \(S_+\) is Schur in the right half-plane. The other has a pole at \(p=a\).

The stable causal kernel is \(k_+=\delta_0-2ae^{-at}1_{t>0}\). For the bad response there are two different kernels:
\[
k_{-,c}=\delta_0+2ae^{at}1_{t>0},\qquad
k_{-,b}=\delta_0-2ae^{at}1_{t<0}.
\]
The causal kernel has Laplace transform \(S_-\) for \(\Re p>a\) and is unstable on unweighted \(L^2\). The boundary kernel defines the unitary Fourier multiplier with response \(S_-(iu)\), but is anti-causal. Meromorphic continuation does not identify their time supports.

There is a maximal exact Hardy-leakage witness. With
\[
f_+(t)=\sqrt{2a}e^{-at}1_{t>0},\quad
f_-(t)=\sqrt{2a}e^{at}1_{t<0},
\]
both vectors have norm one and direct convolution gives \(U_-f_+=-f_-\). For \(t<0\), the output is
\(-2ae^{at}\int_0^\infty e^{-au}f_+(u)\,du=-f_-(t)\); for \(t>0\), the integral cancels the direct term. Therefore
\[
\boxed{\|P_-U_-P_+\|=1,\qquad \|P_-U_+P_+\|=0.}
\]
This falsifies the inference from boundary norm preservation and reversal to causal recovery.

Even pole-free analyticity plus boundary modulus one is insufficient: \(e^{pT}\), \(T>0\), is entire but unbounded in the right half-plane, and has kernel \(\delta_{-T}\). The opposite \(e^{-pT}\) is a causal inner delay. A Hardy/growth condition matters.

## 2. Impedance, admittance, and interior positivity

For positive reference resistance \(R_0\),
\[
S=\frac{Z-R_0}{Z+R_0},\quad
Z=R_0\frac{1+S}{1-S},\quad
\Re Z=R_0\frac{1-|S|^2}{|1-S|^2}.
\]
Thus analytic Schur scattering corresponds to analytic positive-real impedance, apart from the usual constant/end-point exceptions. Boundary reactance alone does not establish passivity.

The controls give \(Z_+=R_0p/a\), \(Z_-=-R_0p/a\). Both have purely imaginary boundary values; the second has negative storage sign. Admittance cannot fix this because \(\Re(1/Z)=\Re Z/|Z|^2\). The upper-half-plane Herglotz transforms \(iZ(-iz)/R_0\) are \(z/a\) and \(-z/a\).

The right-half-plane Pick kernels are exactly
\[
\mathcal K_{S_\pm}(p,q)
=\frac{1-S_\pm(p)\overline{S_\pm(q)}}{p+\bar q}
=\begin{cases}
2a/((p+a)(\bar q+a)),\\
-2a/((p-a)(\bar q-a)).
\end{cases}
\]
They are respectively positive and negative rank one. At \(a=1,p=q=2\), their values are \(2/9\) and \(-2\), an exact one-point discriminator invisible to boundary-modulus tests.

## 3. A quartet with the elementary xi symmetries

Let \(F(x)=((x-a)^2+\gamma^2)((x+a)^2+\gamma^2)\), with \(a,\gamma>0\), and set \(\Xi_{\rm toy}(s)=F(s-1/2)\). This entire real-type function satisfies \(\Xi_{\rm toy}(1-s)=\Xi_{\rm toy}(s)\) but has zeros \(s=1/2\pm a\pm i\gamma\).

For \(\omega>0\), put \(B_\omega^{\rm toy}(p)=F(p-\omega)/F(p+\omega)\). Reversal, unit boundary modulus, and \(B_\omega^{\rm toy}(0)=1\) follow from evenness and reality. When \(0<\omega<a\), there are uncanceled right-half-plane poles \(p=a-\omega\pm i\gamma\). The same-height numerator cancellation occurs only at \(\omega=a\). When \(\omega>a\), the rational quotient is a finite Blaschke product. One fixed large shift misses the off-line quartet.

The exact-rational probe uses \(a=1/4,\gamma=2,\omega=1/8,p=1/16+2i\), and certifies \(|B_\omega^{\rm toy}(p)|^2>1\).

Its causal logarithmic derivative has inverse Laplace transform
\[
j(t)=4\cosh(at)\cos(\gamma t)1_{t>0}.
\]
The first variation \(B_\omega^{\rm toy}=1-2\omega F'/F+O(\omega^2)\) therefore has even tangent kernel \(W_{\rm toy}(t)=4\cosh(at)\cos(\gamma t)\). At \(T=\pi/\gamma\), the two-point Gram has diagonal 4 and off-diagonal \(-4\cosh(aT)\). The vector \((1,1)\) gives \(8(1-\cosh(aT))<0\). Smooth approximate point masses preserve the strict sign. This is an elementary finite control, not the arithmetic Weil distribution.

## 4. The precise Suzuki gate and connection to the full tangent

Suzuki's actual ratio is
\[
\Theta_\omega(z)=
\frac{\xi(1/2-\omega-iz)}{\xi(1/2+\omega-iz)}.
\]
His equations (1.8)–(1.10) give reversal and boundary modulus one unconditionally. Innerness requires analytic contractivity in the upper half-plane. Proposition 1.2 relates a family of innerness statements to a zero-free half-plane. These are distinct hypotheses. [S12]

In Laplace coordinates \(B_\omega(p)=\xi(1/2+p-\omega)/\xi(1/2+p+\omega)\). An off-line zero \(\rho=\beta+i\gamma\), \(\beta>1/2\), gives an uncanceled pole at \(p=\rho-1/2-\omega\) provided \(\xi(\rho-2\omega)\ne0\). This cancellation caveat is essential at a fixed shift. Zero isolation makes it impossible for all sufficiently small positive shifts to cancel a fixed zero. Analyticity along a sequence \(\omega_j\downarrow0\) therefore excludes such zeros. This is an equivalence diagnostic, not new analytic input.

The Oct7 full tangent note constructs an explicit causal arithmetic distribution \(k_\omega\), with Laplace transform \(B_\omega\) in \(\Re p>1/2+\omega\), and proves
\[
H_{\omega,A}v=(k_\omega*Rv)|_{(-A,A)},\qquad
\lim_{\omega\downarrow0}\frac{\|v\|^2-\|H_{\omega,A}v\|^2}{2\omega}=Q_W(v)
\]
for every fixed \(A>0\) and \(v\in C_c^\infty(-A,A)\).

A concrete sufficient gate is to show that this specified causal convolution extends to a contraction on unweighted \(L^2\) along appropriate shrinking shifts. Compression gives \(\|H_{\omega,A}v\|\le\|v\|\), and the established tangent supplies \(Q_W(v)\ge0\). The weaker per-vector finite-interval condition recorded in the Oct7 note also suffices.

The unconditional unitary boundary multiplier already has contractive compressions, but these are not automatically the specified causal arithmetic operators. Section 1 is an exact falsifier for that identification. In Hardy language the missing condition is \(P_-U_\omega P_+=0\), preservation of the causal Hardy space. For a bounded multiplier, the Hardy multiplier theorem then gives the analytic Schur representative.

A constructive finite-network route should prove both (i) uniform Schur bounds throughout \(\Re p>0\), and (ii) convergence to the arithmetic transfer in its known right half-plane. Normal-family uniqueness then supplies the extension. An advance normalization can destroy (i), even when every unnormalized local factor is inner.

## 5. The finite-prime scattering-delay identity: checked

Let finite \(\mathcal P\) contain every prime \(\le e^{2A}\). Put \(L_p=\log p\), \(r_p=p^{-1/2}\), and
\[
\rho_\infty(q)=\pi^{-q}\frac{\Gamma(1/4+q/2)}{\Gamma(1/4-q/2)},\quad
b_r(w)=\frac{w-r}{1-rw},\quad
\rho_p(q)=b_{r_p}(e^{-qL_p})/e^{-qL_p}.
\]
For \(u_{\mathcal P}=\rho_\infty\prod_{p\in\mathcal P}\rho_p\), the delay convention \(\tau(u)=-d_u\arg u_{\mathcal P}(iu)\) gives
\[
\tau(u)=\log\pi-\Re\psi(1/4+iu/2)
+2\sum_{p\in\mathcal P}L_p\sum_{k\ge1}r_p^k\cos(kL_pu).
\]
For zero-extended \(f\in C_c^\infty(-A,A)\), Plancherel and the completed explicit formula yield exactly
\[
\boxed{Q_W(f)=2(|C_f|^2-|S_f|^2)
-\frac1{2\pi}\int\tau(u)|\widehat f(u)|^2\,du,}
\]
where \(C_f=\int\cosh(t/2)f(t)\,dt\), \(S_f=\int\sinh(t/2)f(t)\,dt\).

All tower correlations with \(kL_p\ge2A\) vanish. The prime series is absolutely convergent for finite \(\mathcal P\); Gamma grows only logarithmically, while \(\widehat f\) is Schwartz.

The positive delay drop \(\tau(0)-\tau(u)\) gives the known Gamma/prime energy. Its full prime towers exceed Oct7's cutoff by the scalar
\[
2\sum_{p\in\mathcal P,\ kL_p>2A}L_pr_p^k\,\|f\|^2.
\]
The same excess is present in \(\tau(0)\|f\|^2\), so it cancels. The exact signed total is
\[
Q_W=E_{\rm delay}-\tau(0)\|f\|^2+2(|C_f|^2-|S_f|^2).
\]
Positive dispersion drop alone does not establish its sign.

The local prime normalization has an explicit negative-time term:
\[
\rho_p(q)=-re^{qL}+(1-r^2)\sum_{k\ge0}r^ke^{-kqL}.
\]
Thus the causal inner filter \(b_r(e^{-qL})\) acquires an advance when divided by the delay. Likewise the finite Gamma factors \((\lambda_j-q)/(\lambda_j+q)\), \(\lambda_j=2j+1/2\), are inner, but the normalization \((M/\pi)^q\) with M stages is an increasing advance. Inner finite factors do not establish innerness of this normalized limit.

For \(Q=P-K\), realizing the two positive terms separately does not prove positivity of their difference. Positivity of a block whose Schur complement is \(P-K\) is circular unless supplied independently.

## 6. Corrections to the inherited passive-colligation no-go

Inspected remote note: research/claude_round_006/PASSIVE_COLLIGATION.md, blob 4fa517e8936ce313dd3e2a5fc79f56dab50c6a96.

- \(P\iff\mathrm{RH}\) does not imply that no unconditional construction of \(P\) can exist; such a construction would prove RH.
- A logarithmic derivative is not a unit-shift ratio. For example \(F(p)=e^{p^2}\) has \(\Re(F'/F)>0\) in \(\Re p>0\), but \(F(p)/F(p+1)=e^{-2p-1}\) has negative real values there. The reverse implication fails for \(F(p)=e^{-p}\). These are algebraic countermodels, not xi-specific claims.
- Failure of the Conrey–Li shifted pairing does not make the original de Branges Hilbert norm indefinite. Their Section 2 defines the positive Hilbert norm and then tests an additional pairing. [CL]
- A discrete unitary colligation has disk transfer \(D+zC(I-zA)^{-1}B\); \(D+C(\lambda-A)^{-1}B\) is naturally contractive for \(|\lambda|>1\). A half-plane formula needs its own conversion/energy identity.
- A positive state metric and dissipative state generator alone do not constrain arbitrary port couplings: \(A=-1,B=C=10,D=0\) gives \(100/(p+1)\), not Schur. A nonminimal realization can also hide unstable unobservable modes behind a Schur transfer.

## 7. Separate connected-composite countermodel

The following exact model
\[
D(s)=1+\sqrt6\,6^{-s},\qquad
F(s)=6^{(s-1/2)/2}D(s)=2\cosh((s-1/2)\log6/2)
\]
is entire, real-type, and symmetric under \(s\mapsto1-s\). All zeros are \(s=1/2+i(2k+1)\pi/\log6\).

In \(\Re s>1/2\),
\[
-D'/D=\log6\sum_{m\ge1}(-1)^{m-1}6^{m/2}6^{-ms}.
\]
The connected log-derivative coefficient at 6 is \(\sqrt6\log6\ne0\), although \(a_2=a_3=0\). This refutes a universal claim that a connected composite charge forces an off-line zero. It does not possess zeta's Euler/Gamma/conductor axioms and is not an actual Davenport–Heilbronn example.

## Primary sources and inherited derivation

- [S12] M. Suzuki, [A canonical system of differential equations arising from the Riemann zeta-function](https://arxiv.org/pdf/1204.1827), Sections 1.3–1.7 and Proposition 1.2. The opened PDF has an internal September 13, 2018 version date.
- [CL] J. B. Conrey and X.-J. Li, [A note on some positivity conditions related to zeta- and L-functions](https://arxiv.org/pdf/math/9812166), Section 2.
- Inherited local full tangent: https://github.com/femboy2112/FuckingRH/blob/e6f2d08716cc699efec10eafd6738e770615bc76/research/aletheia_2026-10-07/succ_weil_suzuki/FULL_SUZUKI_WEIL_TANGENT.md, Sections 3, 7–9.
- Inherited local RMP: ../reversal_memory_polarization/HISTORY_AND_POLARIZATION.md.

The companion probe uses exact Fraction comparisons for the rational controls, with separate labels for floating diagnostics. It does not establish an arithmetic passive realization.

Run `scripts/causal_allpass_probe.py` using the command in [PROVENANCE_AND_CLAIMS.md](PROVENANCE_AND_CLAIMS.md); the report is [causal_allpass_results.json](evidence/causal_allpass_results.json).
