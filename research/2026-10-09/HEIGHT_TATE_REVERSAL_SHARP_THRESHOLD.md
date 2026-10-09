# A sharp Tate/height bridge: coherent reversal versus source-specific Weil polarization

2026-10-09. Parent main f2fe8b3 (R64); continue pre-existing branch aletheia/archimedean-dualizing-reversal-2026-10-09 at 1790dc9. **RH open.** This note adds a theorem about a precisely specified candidate finite/Archimedean coupling, not a proof of RH, not a claim of academic novelty.

## 0. Provenance, user hypothesis, rival interpretations and preregistration

**User-origin proposal:** SUCC/shadow-SUCC activation produces complete histories; a physically/mathematically coherent backward reconstruction must account for environmental correlations, not flip an observed coordinate. The finite and archimedean places should obey compatible global laws under reversal. Probe the missing dualizing/polarization at infinity and the arithmetic self-product, not just more symmetric formulas.

**Assistant operational repair:** Test whether a two-sided rational-history Hilbert space can be mapped *boundedly and injectively* to the single real logarithmic clock. Rational states r=a/b carry the height h(r)=log max(a,b) and net clock log r; the image of e_r is a fixed archimedean wavepacket centered at log r, attenuated by e^{-tau h(r)}. This is a chosen model, not asserted as the unique geometric realization or the arithmetic self-product.

**Declared outcome gates, prior to numerical probes:**
- H1: tau=1/2 half-height wavepackets synthesize boundedly and can be reversibly recovered. Pass: a Bessel/synthesis upper bound and bounded inverse, with source fidelity. Fail: a norm-divergence sequence; ambiguous: a finite-only observation.
- H2: stronger positive height regularization yields a bounded coupling without losing arithmetic labels. Pass: bounded injective operator and explicitly compatible rational shifts; fail: no bounded map or loss of injectivity.
- H3: the successful bridge supplies the *Weil sign* from its geometry. Pass: independent sign and exact FULL completed Weil identity including conductor, gamma and poles, source controls. Fail: positivity remains valid after fake source atoms; unresolved: actual Weil identification not constructed.
- Independent probes: exact totient combinatorics versus exhaustive coprime enumeration; analytic Tate overlap versus real integration; different box and Gaussian wavepackets; independent algebra of rational covariance; the DH-like mixture and fake-n=6 mutants; fresh high-precision Gamma-Fourier tests. Numerical controls are not independent mathematical proofs.

## 1. The sharp analytic theorem (proved, scoped)

Let G=Q_{>0}^× and write r=a/b in lowest terms. Put h(r)=log max(a,b). Let g be any nonzero L²(R) function and T_xg(u)=g(u-x). Define J_{tau,g} initially on the finitely supported sequences in ell²(G) by

$$
J_{\tau,g} e_r=e^{-\tau h(r)}T_{\log r}g,\qquad\tau\ge0.
$$

**THEOREM 1.** J_{tau,g} extends to a bounded operator ell²(G)->L²(R) **if and only if tau>1**. For tau>1 it is Hilbert-Schmidt and

$$
\|J_{\tau,g}\|_{\mathrm{HS}}^2
=\|g\|_2^2\left(2\frac{\zeta(2\tau-1)}{\zeta(2\tau)}-1\right).
$$

PROOF (sufficiency): There are 1+2 sum_{m=2}^M phi(m) reduced positive rational numbers with max(numerator,denominator)<=M: at height m>=2 the numerator or denominator is m, giving 2 phi(m) mutually disjoint cases. Hence

$$
\sum_{r\in G} e^{-2\tau h(r)}
=1+2\sum_{m\ge2}\frac{\varphi(m)}{m^{2\tau}}
=2\frac{\zeta(2\tau-1)}{\zeta(2\tau)}-1
$$

for tau>1, using sum phi(m)/m^s = zeta(s-1)/zeta(s), Re s>2. The squared image norms sum to the above quantity times ||g||², establishing a Hilbert-Schmidt extension.

PROOF (necessity): Strong continuity of translations on L² ensures an epsilon>0 and c>0 with |<g,T_log r g>|>=c for all 1<r<1+epsilon. There are asymptotically order M² coprime fractions r=(b+k)/b with b<=M and 0<k<=epsilon b: by elementary Mobius inversion the count is epsilon sum_{b<=M}phi(b)+O(M log M) = (3epsilon/pi²)M²+O(M log M). Restricting to b in dyadic shells [M/2,M], the number is >=c_epsilon M² for large M. Their max numerator is <=(1+epsilon)M. Thus sum_{r}e^{-2tau h(r)}|<g,T_log r g>|² diverges for tau<1 by a single large shell, and for tau=1 by summing disjoint dyadic shells (each contributes >=c_epsilon). If J were bounded, this sum would equal ||J* g||²<infinity by Bessel/Parseval on the standard ell² basis. Contradiction.

This rules out every fixed-profile, height-power attenuated rational-history synthesis with tau<=1. It does NOT rule out adeles, arbitrary r-dependent profiles, distributional pairings, or different source Hilbert topologies. The height exponent tau is a MODEL REGULARIZER, not identical to the local Euler half-density p^{-1/2}; tau=1/2 is just a deliberately tested naive extension.

## 2. Exactly correct Archimedean Gamma seed (proved)

Choose the true self-dual real Tate Gaussian f_infty(x)=e^{-pi x²} on x>0 with additive dx. After the unitary x=e^u half-density coordinate change, the **normalized** seed is

$$
g_T(u)=2^{3/4}e^{u/2}e^{-\pi e^{2u}},\quad \|g_T\|_2=1.
$$

Direct substitution x=e^u proves

$$
\widehat g_T(t)
=2^{-1/4}\pi^{-1/4+it/2}\Gamma(1/4-it/2)
$$

in the Fourier convention hat g(t)=integral g(u)e^{-itu}du. It is nonzero for every real t because Gamma has no zeros.

The exact Gram kernel, independently obtained by integrating two shifted real Gaussians, is

$$
\langle T_{\log r}g_T,T_{\log s}g_T\rangle
=\frac{1}{\sqrt{\cosh(\log(r/s))}}
=\sqrt{\frac{2rs}{r^2+s^2}}.
$$

Therefore the fully explicit arithmetic/archimedean positive kernel is

$$
K_\tau(r,s)
=e^{-\tau(h(r)+h(s))}\sqrt{\frac{2rs}{r^2+s^2}}.
$$

It is strictly positive definite on every finite set of distinct positive rationals (nonzero Gaussian Fourier transform), but merely being Gram-positive is generic and **source-blind**. It remains positive after a fake connected source atom at n=6, shifted log2, nonunitary alpha2, or a Davenport–Heilbronn-style coefficient mixture; hence it does not satisfy fourth-gate Weil positivity.

For an independent control, the log-coordinate Gaussian g(u)=pi^{-1/4} exp(-u²/2) gives kernel exp(-(log(r/s))²/4). A compact box g=1_{[-1/2,1/2]} gives max(0,1-|log(r/s)|). The threshold tau>1 persists for BOTH, by Theorem 1.

## 3. Full retention but unstable inversion (proved)

**THEOREM 2.** For tau>1 the Tate map J_tau is (i) injective; (ii) of dense range in L²(R); (iii) compact, with unbounded inverse on its range.

Proof: For f in ell²(G), weighted coefficients e^{-tau h(r)} f(r) are ell¹ by Cauchy-Schwarz, so define a finite complex measure mu_f=sum_r e^{-tau h(r)}f(r)delta_{log r}. Then J_tau f=g_T*mu_f (the sum converges in L²). If J_tau f=0, Fourier implies hat g_T hat mu_f=0 a.e.; hat g_T is nowhere zero, and hat mu_f is continuous. Thus mu_f=0 by uniqueness of finite-measure Fourier transforms, so f=0.

Any h orthogonal to the range is orthogonal to every translated g_T at all log r. The log positive rationals form a dense subgroup of R, so by continuity it is orthogonal to every real translate. Since hat g_T is nonzero a.e., h=0. Thus the range is dense.

J_tau is Hilbert-Schmidt (Theorem 1), hence compact. No injective compact operator on an infinite-dimensional Hilbert space can have a bounded inverse on its range. In other words, the inverse reconstruction is mathematically unique but necessarily unstable in the ordinary source ell² norm.

The Gram H_tau=J_tau*J_tau is a strictly positive **non-coercive** metric; 0 belongs to its spectrum, and no lower uniform frame bound exists. This reflects generic crowding, NOT zeta zeros.

## 4. Multiplicative covariance without smuggled continuous evolution (proved)

Define on ell²(G), for q,r>0 rational,

$$
W_q e_r=\frac{e^{-\tau h(r)}}{e^{-\tau h(qr)}}\,e_{qr}
=e^{\tau(h(qr)-h(r))}e_{qr}.
$$

Height subadditivity |h(qr)-h(r)|<=h(q) gives ||W_q||<=e^{tau h(q)}, and r=1 achieves equality:

$$
W_qW_s=W_{qs},\quad W_q^{-1}=W_{1/q},\quad \|W_q\|=e^{\tau h(q)}.
$$

The coupling is *exactly* equivariant:

$$
J_\tau W_q=T_{\log q}J_\tau.
$$

This gives a source-faithful finite Euler logarithmic-derivative operator on the rational parent:
D_X=sum_{p^k<=X}(log p)p^{-k/2} chi(p)^k W_{p^k}, and J_tau D_X=(sum coefficients T_{klogp}) J_tau. It has NO primitive n=6 atom; a fake atom adds a separately detectable extra shift. For X finite, D_X is bounded; NO claim of a cutoff-independent bounded limit at 1/2 follows.

**THEOREM 3 (topology obstruction):** Neither the ordinary regular shifts lambda(q)e_r=e_{qr} nor the height-cocycle shifts W_q extend to a strongly continuous real-parameter group by identifying q with log q. Indeed log(Q_+) is dense in R, and there are q_j !=1 with log q_j->0 (for instance 2^{a_j}/3^{b_j} from irrational approximations). But ||(lambda(q_j)-I)e_1||=sqrt(2), while ||W_{q_j}||=e^{tau h(q_j)}->infinity. A strongly continuous family is locally uniformly bounded; contradiction. Equivariance through a compact, non-invertible J_tau does not contradict this.

Furthermore, the dense proper range of J_tau is NOT invariant under T_t for t outside log G: translating J_tau e_1=g_T by such a t would require a measure delta_t supported on log G, impossible by injectivity of the Fourier transform of finite measures. The completion of range in its transported norm IS L²(R); the arithmetic labels become nonorthogonal/distributionally unstable there. The full archimedean flow is obtained by changing the topology, not a bounded inverse on the old rational basis.

## 5. A second no-go: normalized critical limit forgets each fixed arithmetic state

As tau decreases to 1 from above,

$$
\|J_\tau\|_{\rm HS}^2\sim \frac{1}{(\tau-1)\zeta(2)}.
$$

Hence the rescaled family sqrt(tau-1)J_tau is uniformly bounded, with HS norm tending 1/sqrt(zeta(2)), BUT for each fixed e_r, sqrt(tau-1)J_tau e_r->0. By density of finite-support vectors, it converges STRONGLY to the ZERO operator.

So renormalizing only total Hilbert–Schmidt mass gives no nonzero source-retaining critical coupling. A more sophisticated renormalized trace, distributional domain, subtraction, or adelic topology is required. This is a theorem about this model, not an RH no-go.

## 6. The arithmetic sign is still absent (hostile controls)

For a primitive character mod5 with chi(2)=i, chi(3)=-i, a normalized mixture a L(s,chi)+b L(s,bar chi) (a+b=1) has connected coefficient

$$
[-F'/F](6)
=[a(6)-a(2)a(3)]\log 6=4ab\log 6.
$$

For a=1,b=0 the defect is zero; for a=0.6,b=0.4 it is 0.96 log6. A fake connected n=6 impulse adds an independent shifted term of that frequency; it leaves the Gram K_tau positive unchanged. A shifted log2 breaks physical shift-intertwining if source labels remain real rational 2; and |alpha2|≠1 breaks the unramified unitary-Hecke condition, but neither destroys Gram positivity.

This is the exact failed implication: **positive invertible/symmetric archimedean reconstruction does NOT force the source-specific full Weil sign.** Even this Gamma-faithful J_tau does not contain the conductor, pole, completed Weil pairing, or surface Hodge-index theorem. No spectral zeta-zero data enter any construction.

## 7. Primary literature and distinction from adjacent branches

- Connes–Consani, Riemann–Roch for compactified Spec Z (2023), https://arxiv.org/html/2205.01391v2: Theorem 1.2/5.3 supplies curve-level Serre-like duality, K=-2{2}, U(1)_{1/4}. NOT a complete surface polarization.
- Connes–Consani, Arithmetic Site (2015/2016), https://arxiv.org/abs/1502.05580: the arithmetic-site square and Frobenius correspondences are mathematically constructed, without the claimed missing Hodge-index sign.
- Connes–Consani, absolute twistor (submitted Aug 31, 2026), https://arxiv.org/abs/2609.00299: geometric inversion exists but its intrinsic odd-Frobenius scope makes 2-compatibility a necessary check.
- Connes–Consani, absolute Spec Z geometry (June 2026), https://arxiv.org/abs/2606.06604: local prime-period circles/tori.
- Standard Tate-thesis local Gaussian integral (recoverable by direct elementary integration here) and Schanuel's rational point counting/higher-level height geometry: https://www.sciencedirect.com/science/article/pii/S107157972400056X.
- Adjacent draft PR #11 (head 28de8c2) finds a NONCOMPACT common cover and unbounded naive periodization for E_2<-C×->E_6; this note asks a DIFFERENT sharp analytic question on rational-height-indexed translates. PR #10 is this branch, original head 1790dc9.

**Claim labels:** HTR-01 (sharp threshold), HTR-02 (Tate Gamma/overlap), HTR-03 (dense injective compact bridge), HTR-04 (bounded cocycle covariance), HTR-05 (no strong-continuous discrete-regular identification), HTR-06 (critical HS-normalized strong-zero), all PROVED under their precise hypotheses. HTR-07 (finite controls), OBSERVED (specific logs in probe output). HTR-08 (bridge equals completed Weil or gives independent Hodge sign), UNVERIFIED: in fact the displayed simple Gram candidate is REFUTED as a fourth-gate certificate by fake-source invariance.

**Next verdict-changing probe:** Replace the source-blind height damping with an independently specified global adelic/Poisson dualizing transfer whose *induced trace*, NOT chosen Gram, equals the full Weil form, including two prime interactions and the archimedean/pole subtraction. Test whether it can be bounded/renormalized on an appropriate distributional adelic space while retaining exact p=2, p=3, chi and fake-6 source discrimination. Failing equality is a terminal falsifier for that transfer. No inference from finite spectral agreement to all L.
