# Arithmetic reversal, dualizing objects, and the missing polarization

Research note — 2026-10-09, parent \`f2fe8b3\` (Round 064). **RH OPEN.** Source-derived objects only; no zeta-zero input, scattering phase, or fitted boundary. This is a testable research handoff, not a proof.

## 1. Literature corrections and the actual host

Weil's function-field proof uses the *existing* surface C×C and the Hodge-index/intersection positivity for Frobenius correspondences. Riemann–Roch and Serre duality help build the theory, but formal duality is not itself the positivity theorem.

The slogan “no Serre duality/Riemann–Roch exists over Spec Z” is false. Connes–Consani (2023, Theorem 5.3, https://arxiv.org/html/2205.01391v2) construct a Serre-like duality for the Arakelov compactification, including model-specific canonical-divisor analogue K=−2{2} and dualizing module U(1)_{1/4}. Their 2024 refinement over the absolute base S replaces S[±1] and obtains a cleaner base-2 arithmetic Riemann–Roch (https://doi.org/10.5802/crmath.543). Neither is a verified dualizing sheaf of the *required arithmetic self-product* nor proves Weil positivity.

The Connes–Consani arithmetic-site **square and Frobenius correspondences exist** (https://arxiv.org/abs/1502.05580). What is not established for RH is a global *intersection theory/polarization* on the appropriate self-product with an independently proven Hodge-index sign that reproduces the full Weil distribution.

Extremely relevant NEW literature: Connes–Consani, June 2026, https://arxiv.org/abs/2606.06604, construct an absolute arithmetic curve with p-adic and archimedean torsors and the periodic orbit C_p=R_+^×/p^Z. Their Aug/Sept 2026 paper https://arxiv.org/abs/2609.00299 constructs an archimedean component over signed F_{1^2} with **canonical geometric inversion** and a twistor real structure. The abstract states the Frobenius action is restricted to **odd integers**. A zeta-complete construction importing it must EXPLICITLY retain the 2-adic tower (2,4,8,...); do not conflate geometric inversion with physical time reversal or assert RH progress from the abstract.

Conventional Gillet–Soulé arithmetic Riemann–Roch and Faltings–Hriljac/Arakelov height positivity on genuine arithmetic surfaces are also known; neither gives RH for ζ.

## 2. Principal rational divisors and the two clocks

For r=∏p p^{v_p(r)}∈Q_{>0}, put u_p(r)=v_p(r) log p and u_∞(r)=−log r. Then ∑_v u_v(r)=0 (product formula). Under inversion r→r^{-1}, each u_v changes sign. This is a mathematical change of orientation, not physical reverse-time evolution.

For r=a/b reduced, h(r)=log max(a,b) satisfies

$$
2h(r)=|\log r|+\sum_p|v_p(r)|\log p,\qquad h(r^{-1})=h(r).
$$

It follows that h(r/s) is a conditionally negative-definite kernel (sum of |x−y| metrics). Thus H_t(r,s)=exp(−t h(r/s)), t>0, is strictly positive definite on finite sets of distinct rationals; the arch factor exp(−t|log r−log s|/2) is strictly PD and the other place factors are PSD. The anchored covariance [h(r)+h(s)−h(r/s)]/2 is PSD.

**Critical negative control:** H_t is global and nonfactorized (h(2/3)=log3, not h(2)+h(1/3)=log6), yet it remains positive if a fake source impulse at n=6 is inserted. This is a source-INERT positive structure, not a Weil form. “Degree ≥0 on principal effective parts” is not the missing Hodge-index theorem.

## 3. A precise teacup/wavefront reversal: winding and carry

For p prime, C_p≅R/(log p)Z. Let t=k_p(t)log p+θ_p(t), 0≤θ_p<log p.

Under t→−t and θ_p>0:
$$(k,\theta)\mapsto(-k-1,\log p-\theta).$$
For θ=0: (k,0)↦(−k,0). A quotient phase forgets the winding needed for inverse reconstruction.

For n=p^a m, (m,p)=1:
$$
k_p(\log n)=a+\left\lfloor\frac{\log m}{\log p}\right\rfloor.
$$
The first term is v_p(n); the second is an archimedean cross-prime carry. At n=6, p=2 has valuation 1, winding 2, carry 1; p=3 has 1,1,0. **Winding ≠ valuation.**

For integers n>1:
$$
n=p^k\quad(k\ge1)
\iff \log n\equiv0\pmod{\log p}.
$$
Therefore
$$
\Lambda(n)=\sum_{p\le n}\log p\ \mathbf1_{\log n=0\ {\rm in}\ C_p}.
$$
This is an exact zero-input orbit-incidence description of prime-power charges, NOT new analytic number theory and NOT Weil positivity. Shifted log2 breaks 2,4,8,... closed-orbit matching.

## 4. Finite causal source cannot be positively unitarized

Set L=log N, Ω_N={a/b reduced: a,b≤N², 1/N≤a/b≤N}, H_N=ℓ²(Ω_N). Define V_n e_r=e_{nr} if nr∈Ω_N, else 0. Then V_m V_n=V_{mn}, the inversion antiunitary J satisfies J V_n J=V_n^*, and V_n≠0 iff n≤N². Define

$$
D_N=\sum_{p^k\le N^2}\frac{\log p}{p^{k/2}}V_{p^k}.
$$

D_N is nonzero and nilpotent for all N≥2 because every term strictly increases log r in a finite space. Formal duality J D_N J=D_N^* holds, even after arbitrary real source-weight mutations.

**THEOREM (causal polarization obstruction).** If 0≠D is a nilpotent finite matrix and H>0 is Hermitian, then D^*H+HD has both signs.

Proof: A=H^{1/2}DH^{-1/2} is nonzero and nilpotent, so tr(A+A^*)=0. If A+A^* were semidefinite it must vanish; then A is skew-Hermitian normal and nilpotent, forcing A=0. Contradiction. Congruence preserves inertia.

So a positive metric CANNOT make the one-sided source D_N a centered unitary time evolution. Full reversible dynamics require a genuinely enlarged parent/coupling, not a renaming of its adjoint.

Independent scratch tests on Ω_2,Ω_3,Ω_4: respectively 7,39,121 states; positive height-kernel minimum eigenvalues 0.4055,0.3284,0.2804; extrema of D_N^*H+HD were (−0.961,3.29), (−2.69,10.2), (−4.87,20.5). Fake n=6 source changes D_N at N≥3 but not the positive height metric; N=2 cannot see n=6 due to activation horizon. These are finite computational controls, NOT infinite conclusions.

## 5. Why formal duality does not imply a RH sign

A putative cohomological generator Θ with true zero-spectrum identification would need a source-derived positive polarization H>0 satisfying

$$
\Theta^*H+H\Theta=H.
$$

Then A=Θ−I/2 is H-skew and spec Θ⊂1/2+iR. This is the conditional Deninger/Hilbert–Pólya argument, not an unconditional construction.

**Exact 2×2 falsifier:** with a>0, G=diag(1,−1), A=[[0,a],[a,0]], one has A^T G+G A=0 (perfect nondegenerate duality), but spec(I/2+A)={1/2±a} is OFF the critical line. A positive metric is the load-bearing ingredient, not mere duality. Compare the function-field elliptic Frobenius degree Gram from repo R64: [[2,a_p],[a_p,2p]] positive from actual geometric degree, thereby rejecting |a_p|>2√p.

The fixed archimedean Gamma factor supplies
$$
A_\infty(t)=2\Re\left.\frac{d}{ds}\log\left(\pi^{-s/2}\Gamma(s/2)\right)\right|_{s=1/2+it}
=\Re\psi(1/4+it/2)-\log\pi.
$$
A_∞(0)=−5.37218341922566... is negative. This is an exact duality/completion contribution, not a standalone positive floor. On Bruhat–Schwartz adeles, Fourier conjugates normalized dilation into inverse dilation; Poisson summation establishes the functional equation, not the Hodge sign. Davenport–Heilbronn warns: symmetry is compatible with off-line zeros.

## 6. Proof-bearing fourth gate and discriminating program

A serious prospective *surface-level* object must provide:

1. Exact dualizing complex/line ω_S and trace/adjunction for ALL primes (including 2) plus ∞; do not pass off the 2023 curve-level U(1)_{1/4} as the missing self-product dualizing object.
2. Source-faithful correspondences: actual Λ(p^k), p^{-k/2}, log p, unitary χ values; NO first-order fake n=6 or log(p/q) impulses. A mixed-prime *interaction* need not be a composite impulse.
3. An explicit correspondence space, degree-zero sector, and pairing whose pushforward equals the FULL Q_L=P_L−K_L with fixed conductor, Gamma, and pole terms; no zeros used in construction.
4. An independently proved Hodge-index-type sign on the source-defined sector and controlled limit/domain. Formal Serre symmetry, Riemann–Roch, height positivity, or finite unitarity do not supply this.
5. Four-way calibrated controls: ζ, primitive χ modulo 5, matched Davenport–Heilbronn, fake 6, |α₂|≠1, shifted log2. Coefficient-admissibility alone does NOT satisfy Gate 4.
6. A negative-test audit of geometric reversal: prove it does more than recover theta/functional equation; exhibit a new sign constraint or report a refuted mechanism.

**Claim ledger:** DISCLOSED: finite orbit/carry/height identities, PD height kernel, nilpotent no-go, 2×2 indefinite-duality counterexample. OBSERVED: N=2,3,4 model results. CONJECTURED: a new dualizing/intersection coupling on the global arithmetic self-product could supply Weil sign. UNVERIFIED: that coupling, trace equality, and Hodge-index inequality. **RH OPEN.**

Further primary sources:
- Deninger on cohomology/polarization: https://arxiv.org/abs/1001.1621
- Connes–Consani Weil positivity, archimedean: https://arxiv.org/abs/2006.13771
- Connes–Consani–Moscovici semilocal: https://arxiv.org/abs/2310.18423
- Kedlaya's function-field Hodge index: https://kskedlaya.org/weil-cohom/chapter-5.html


## 7. Another exact trap: unitary environmental dilation is FREE

Every contraction T has a Halmos/Julia block-unitary completion on H⊕H:
$$
U_T=
\begin{pmatrix}
T&(I-TT^\ast)^{1/2}\\
(I-T^\ast T)^{1/2}&-T^\ast
\end{pmatrix},
\qquad U_T^\ast U_T=I.
$$
The off-diagonal blocks act as information leakage and coherent return. In particular this *automatically works for the compressed true arithmetic shift* V_2 and also the fake source channel 0.02 V_6. A unitary “complete teacup” exists for any contraction, independently of multiplicativity or RH. It therefore supplies NO Hodge-index sign and cannot be the fourth gate. Finite tests on N=2,3,4 verified U_T^\ast U_T=I and exact recovery of T under compression for both controls.

The positive-metric no-go from §4 is not contradicted: a dilation enlarges and changes the ambient dynamical operator, whereas the no-go concerns attempting to turn the original nonzero nilpotent D into a centered unitary flow by changing its positive inner product alone.

The remaining genuinely hard requirement is **arithmetic uniqueness of the global dualizing/polarizing completion** (source, Γ, conductor, poles, geometry) AND an independently proved Hodge-index sign whose pushforward is the full Weil form. Formal reversibility is available for fake arithmetic and therefore cannot, by itself, discriminate RH.
