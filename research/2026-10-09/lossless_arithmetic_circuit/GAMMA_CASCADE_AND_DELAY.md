# Gamma scattering as a renormalized lossless cascade

2026-10-09. This note is part of the lossless-arithmetic-circuit checkpoint. The elementary calculations below were derived by the GPT-6 assistant from the stated Gamma identities and checked by a bounded same-model calculation. They are not a priority or independent peer-review claim. No RH assumption occurs.

## 1. Fix the clocks and the transform order

On H=L²((0,infinity),dx), let C be the unitary cosine transform

\[
(Cf)(x)=2\int_0^\infty\cos(2\pi xy)f(y)\,dy,
\qquad (If)(x)=x^{-1}f(x^{-1}).
\]

C and the **linear** inversion I are unitary involutions. The displayed integrals can first be used on smooth compactly supported tests away from zero; the operators extend to H. This I is not the conjugate-linear antiunitary used in the previous duality note.

Use the Mellin transform M f(s)=int_0^infinity f(x)x^(s-1)dx. Set

\[
\gamma_\infty(s)=\pi^{-s/2}\Gamma(s/2),\qquad
\rho_\infty(s)=\frac{\gamma_\infty(s)}{\gamma_\infty(1-s)}.
\]

The standard cosine Mellin identity, initially in its convergence strip and then by continuation/Plancherel, gives

\[
M(Cf)(s)=\rho_\infty(s)Mf(1-s),\qquad
M(CIf)(s)=\rho_\infty(s)Mf(s).
\tag{1}
\]

Thus S=CI is an exactly unitary dilation-invariant operator. On Re(s)=1/2, |rho_infinity(s)|=1. Its inverse IC has the reciprocal multiplier.

| Coordinate / convention | Transformed test | Transform | Kernel of CI |
|---|---|---|---|
| t=log x | v(t)=exp(t/2)f(exp t) | Mf(1/2+i omega)=int v(t)exp(i omega t)dt | k(t)=2exp(t/2)cos(2 pi exp t) |
| T=-log x | w(T)=exp(-T/2)f(exp(-T))=v(-T) | Mf(1/2+q)=int w(T)exp(-qT)dT | k(-T)=2exp(-T/2)cos(2 pi exp(-T)) |

The second row uses a bilateral Laplace transform, first on compact tests; causal convolution in T has transfer holomorphic in Re(q)>0 when it is a bounded Hardy multiplier. The first row's positive-time causal convention corresponds to Re(s)<1/2. Changing this clock reverses the half-plane.

To verify the kernel directly, substitute z=1/y in CIf and then z=exp r:

\[
(CIf)(x)=2\int_0^\infty\cos(2\pi x/z)f(z)\frac{dz}{z},
\]
\[
e^{t/2}(CIf)(e^t)=\int_{\mathbb R}
2e^{(t-r)/2}\cos(2\pi e^{t-r})v(r)\,dr.
\tag{2}
\]

This kernel is naturally an oscillatory tempered distribution, and (2) is an ordinary finite integral for compact v. Its support is all of R. Neither it nor its reversal becomes one-sided under any finite translation. Exact local unitarity therefore does not give causal log-time propagation.

Primary anchors: Burnol, *Spectral Analysis of the local Conductor Operator*, pp.4-5 and 8-10, https://arxiv.org/pdf/math/9811040; Connes–Consani, *Quasi-inner functions and local factors*, equations (1)-(4), https://arxiv.org/pdf/2008.10974. The coordinate calculation (2) is supplied here explicitly.

## 2. An exact sequence of causal lossless circuits

For integers M>=1, define

\[
\lambda_j=2j+\tfrac12,\quad 0\le j<M,\qquad
b_j(q)=\frac{\lambda_j-q}{\lambda_j+q},\qquad
B_M(q)=\prod_{j=0}^{M-1}b_j(q).
\tag{3}
\]

Each factor is holomorphic and bounded by one in Re(q)>0 and has unit modulus on q=i omega. Indeed,

\[
|\lambda_j+q|^2-|\lambda_j-q|^2
=4\lambda_j\operatorname{Re}q>0.
\]

Its causal Laplace impulse is

\[
-\delta_0+2\lambda_j e^{-\lambda_j T}1_{T\ge0}.
\tag{4}
\]

Each B_M is consequently a stable causal lossless all-pass transfer. There is no arithmetic positivity assumption in this finite construction.

An explicit continuous storage law realizes each stage. For an input u, output y, and scalar state x, take

\[
\dot x=-\lambda_jx+\sqrt{2\lambda_j}\,u,
\qquad y=\sqrt{2\lambda_j}\,x-u.
\]

Then `d|x|^2/dT=|u|^2-|y|^2`. Its zero-state transfer is (3), and at frequency omega with unit incident amplitude the stored energy is `2 lambda_j/(lambda_j^2+omega^2)`, exactly the stage's delay. This is the continuous counterpart of the unitary prime-clock storage identity in the companion note.

Put a=1/4. The Gamma recurrence proves the exact identity

\[
B_M(q)=
\frac{\Gamma(a+q/2)}{\Gamma(a-q/2)}
\frac{\Gamma(M+a-q/2)}{\Gamma(M+a+q/2)}.
\tag{5}
\]

At zeros of the reciprocal Gamma factor this is interpreted by continuation. The standard Gamma-ratio asymptotic is locally uniform for q in a fixed compact set:

\[
\frac{\Gamma(M+a-q/2)}{\Gamma(M+a+q/2)}
=M^{-q}\left(1+\frac{q}{4M}+O_K(M^{-2})\right).
\tag{6}
\]

Therefore B_M tends locally uniformly to zero in Re(q)>0, whereas

\[
\boxed{
\left(\frac M\pi\right)^q B_M(q)
\longrightarrow
\rho_\infty(\tfrac12+q)
=\pi^{-q}\frac{\Gamma(a+q/2)}{\Gamma(a-q/2)}.}
\tag{7}
\]

If a product is instead indexed 0<=j<=N, its number of stages is M=N+1 and the normalizer is ((N+1)/pi)^q. This resolves the cutoff-index convention.

The factor exp(q log(M/pi)) is a time **advance** in the Laplace convention in the second row of the table. Its advance diverges with M. It has unit modulus on the boundary, but it is not a Schur multiplier for M>pi. Recovering the nonzero Gamma response from these finite circuits does not preserve causal contractivity on a fixed Hardy space.

No fixed delay repairs this particular Gamma transfer. For m>=1,

\[
\rho_\infty(2m)
=\frac{2(-1)^m(2m-1)!}{(2\pi)^{2m}}.
\tag{8}
\]

Factorial growth beats exp(d(2m-1/2)) for every fixed real d. Hence exp(-dq)rho_infinity(1/2+q) is unbounded in Re(q)>0 for every finite d. On the opposite half-plane rho_infinity has poles at s=0,-2,-4,... .

This gives a concrete discriminator: finite lossless circuit approximants plus boundary modulus one do not establish a nonzero causal limit. The normalization, time origin, topology, and exact nonzero limiting response must be verified.

## 3. The finite delay difference has an unconditional positive limit

Choose the continuous boundary phase of B_M with phase zero at omega=0. With group delay defined as minus the phase derivative,

\[
\tau_M(\omega)
=-\frac d{d\omega}\arg B_M(i\omega)
=\sum_{j=0}^{M-1}\frac{2\lambda_j}{\lambda_j^2+\omega^2}>0.
\tag{9}
\]

The digamma recurrence gives an exact second formula:

\[
\tau_M(\omega)=
\operatorname{Re}\psi(M+a+i\omega/2)
-\operatorname{Re}\psi(a+i\omega/2).
\tag{10}
\]

After the advance in (7), the delay becomes

\[
\widetilde\tau_M(\omega)=\tau_M(\omega)-\log(M/\pi)
\longrightarrow
\tau_\Gamma(\omega)
=\log\pi-\operatorname{Re}\psi(a+i\omega/2).
\tag{11}
\]

Uniformly on each bounded frequency interval,

\[
\widetilde\tau_M(\omega)-\tau_\Gamma(\omega)
=-\frac1{4M}+O_\Omega(M^{-2}).
\tag{12}
\]

The limit delay itself is not everywhere nonnegative: it tends to minus infinity as |omega| tends to infinity. Its subtraction at zero, however, eliminates every constant time shift and every divergent cutoff term:

\[
\begin{aligned}
\alpha_M(\omega)
&:=\tau_M(0)-\tau_M(\omega)\\
&=2\sum_{j=0}^{M-1}
\frac{\omega^2}{\lambda_j(\lambda_j^2+\omega^2)}\ge0,
\end{aligned}
\tag{13}
\]
\[
\boxed{
\alpha_M(\omega)\uparrow\alpha(\omega)
=\operatorname{Re}\psi(\tfrac14+i\omega/2)-\psi(\tfrac14)
=\tau_\Gamma(0)-\tau_\Gamma(\omega).}
\tag{14}
\]

This is exactly the already established positive Gamma-energy multiplier from the RMP note, now recovered from a finite circuit's delay difference. It does not identify it with the full Weil form.

There is a rigorous elementary truncation bound. Since lambda_j=2(j+a),

\[
0\le\alpha(\omega)-\alpha_M(\omega)
\le\frac{\omega^2}{4}
\left[\frac1{(M+a)^3}+\frac1{2(M+a)^2}\right].
\tag{15}
\]

Proof: majorize each omitted term by omega²/[4(j+a)³] and use the first term plus the integral for the decreasing positive series. Replacing omega² by Omega² makes this uniform for |omega|<=Omega. The positivity and bound are analytic; the numerical control does not certify them.

Burnol's even archimedean conductor operator has multiplier

\[
h_\infty(\omega)=\operatorname{Re}\psi(\tfrac14+i\omega/2)-\log\pi
=-\tau_\Gamma(\omega).
\]

It is represented initially by log(x)+C log(x) C. A precise self-adjoint multiplier realization has domain {f in H : h_infinity(omega) Mf(1/2+i omega) in L²(d omega/(2 pi))}. Its origin value is negative. Self-adjoint local propagation is not itself a positive global energy; subtracting the origin gives alpha.

## 4. One finite prime is an exact one-clock advance of a causal lossless filter

This is an independent elementary comparison using the same Laplace convention q=s-1/2. For p prime set r=p^(-1/2), ell=log p and w=exp(-q ell). Then

\[
\rho_p(\tfrac12+q)
=\frac{1-re^{q\ell}}{1-re^{-q\ell}}
=w^{-1}\frac{w-r}{1-rw}.
\tag{16}
\]

The delayed factor b_r(w)=(w-r)/(1-rw) is Schur in Re(q)>0 and unimodular on q=i omega. The raw local factor is that filter advanced by one clock ell. Its impulse is

\[
-r\delta_{-\ell}+(1-r^2)\sum_{k\ge0}r^k\delta_{k\ell}.
\tag{17}
\]

Multiplication by exp(-q ell) shifts this to causal support. The bounded stable filter has delay

\[
\tau_{b,p}(\omega)=\ell P_r(\omega\ell),\qquad
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}.
\]

The raw ratio has delay tau_p=ell(P_r-1). Both have the same delay difference:

\[
\tau_p(0)-\tau_p(\omega)
=2\ell\sum_{k\ge1}r^k(1-\cos(k\omega\ell))\ge0.
\tag{18}
\]

Again this is exactly the positive prime-power energy contribution, not the full centered Weil form. In the first row's log-x time, the impulse in (17) is reflected; this is purely the clock change.

## 5. What the source audit adds, and what remains missing

Connes–Consani, https://arxiv.org/pdf/2008.10974, Theorems 2.1, 4.1 and 4.8: for every finite set F of places containing infinity, multiplication by u_F=product rho_v is unitary on the critical-line L² space, and its off-diagonal block (1-P)u_F P is compact for the LEFT Hardy half-plane Re(s)<1/2. Their stronger estimate has singular-value order 1/(2m) for m finite primes. Fact 3.6 shows that an individual rho_p is not quasi-inner. Gamma decay controls the residue contributions; the product has not canceled its poles into a holomorphic inner function. Compact leakage is not zero leakage, and these finite-set estimates do not give a uniform infinite-prime limit. The Sonin spaces have explicit arithmetic transition maps, rather than being replaced by the archimedean space alone.

Burnol, https://arxiv.org/pdf/math/0001013, Theorem 1.7, constructs incoming/outgoing adelic spaces and proves that their orthogonality is equivalent to RH for all abelian L-functions of the global field. In the zeta component the scattering multiplier is ((s-1)/s)² B(s)^(-2), where B is the Blaschke product of right-of-line zeros. It is not simply the product of local Gamma ratios. This is a precise conditional target, not an independent proof of causality.

The global functional equation by itself cannot fill the missing input: after meromorphic continuation, the ratio of completed zeta values Lambda(s)/Lambda(1-s) is identically one. That identity holds whether or not zeros are on the line; common zeros disappear in the ratio. Ordinary Euler products on the critical line cannot be substituted for a proved operator limit.

The constructive next test is to specify a proposed global causal input/output space, its exact source-derived transfer, and its finite-cutoff normalization. Test preservation of the half-line Hardy space and nonzero convergence before interpreting unit modulus as a closed arithmetic circuit. The cascade above gives an explicit failure control: every finite stage passes losslessness and causal passivity, yet the desired Gamma response requires a divergent advance. The surviving delay difference gives a positive component already known to be insufficient without the full Weil origin, polar, and prime-centering terms.

## Numerical control

`scripts/gamma_cascade_probe.py` is the portable NumPy/SciPy control. It checks finite product identities, boundary moduli, delay identities, normalized convergence, the wrong-normalization control, the analytic bound (15), and the finite-prime delay formula. It was run successfully with the primary runtime Python on 2026-10-09. Maximum identity residuals were 8.26e-14 (Gamma product), 8.66e-15 (boundary modulus), and 5.33e-15 (digamma recurrence). The finite-difference phase-sign error was 1.23e-9. The complete output is [gamma_cascade_results.json](evidence/gamma_cascade_results.json).

The supplementary `scripts/gamma_cascade_high_precision_probe.py` was run at 90 decimal digits with mpmath 1.3.0 in an existing environment; all assertions passed, with corresponding identity residuals 1.76e-91, 1.23e-90, and 4.91e-91. Its preserved result is [gamma_cascade_high_precision_results.json](evidence/gamma_cascade_high_precision_results.json). Two initial launches with Python installations lacking mpmath failed at import before any tests. No dependencies were installed.

Both JSON reports are numerical evidence, not interval-certified proofs. Inequalities and limit assertions rest on the analytic arguments above.

Additional provenance for the delay/explicit-formula connection: Burnol, *The Explicit Formula and the conductor operator*, https://arxiv.org/pdf/math/9902080, sections E, H, I (the even real spectral function is on p.20); *Scattering on the p-adic field and a trace formula*, https://arxiv.org/pdf/math/9901051, sections on the time-delay operator and Weil's local supertrace. Thus interpreting local Gamma logarithmic derivatives as local explicit-formula terms is established work. The finite cascade/clock table here supplies a direct normalization and diagnostic for the current analogy. No priority claim is made. Our engineering group-delay convention is tau=-d(arg S)/d(omega)=i S* S'; a Wigner-Smith formula with -i S* S' uses the opposite sign under the same frequency convention.

Reproduction commands with explicit output paths are in [PROVENANCE_AND_CLAIMS.md](PROVENANCE_AND_CLAIMS.md).
