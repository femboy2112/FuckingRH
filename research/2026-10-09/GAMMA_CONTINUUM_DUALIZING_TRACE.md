# The missing archimedean environment as a compensated continuum of shifts

Date 2026-10-09. **RH OPEN.** Built after the HTR-12 range-invariance no-go. This is a classical, zero-free representation of the digamma symbol in an explicitly testable SUCC/reversal common basis, not an actual dualizing sheaf or a proof of Hodge index.

## 0. Changed object after a decisive no-go

The rational-height Tate embedding J_tau is bounded/injective for tau>1 but its range excludes A_inf J_tau e_1, where the true Weil archimedean multiplier A_inf(t)=Re psi(1/4+it/2)-log pi grows logarithmically. Thus no source-ell² internal operator implements the entire arch contribution. Instead define a *singular continuum shift form* on the actual L²(R) archimedean environment; the singular measure is selected by Gamma, not fitted from the Weil sign.

**Pre-registered outcomes:**
- H5: the suggested density gives precisely A_inf(t)-A_inf(0), simultaneously as Fourier multiplier and positive real-space energy, without zeros. Fail if mismatched at ordinary and hostile frequencies, including odd parity.
- H6: the continuous gamma energy plus prime-ray discrete energy automatically yields global positivity by individual Poincare bounds. Fail if the best explicit separate-shift bound remains negative in nontrivial/known positivity windows. No pole-sign assumptions allowed.
- H7: cutting out infinitesimal environmental shifts could yield a bounded kernel still matching full Gamma. Fail if the truncated symbol is bounded while true Gamma is logarithmically unbounded.

## 1. Exact source-derived Levy/Dirichlet form (PROVED)

Put
$$
A_\infty(t)=\Re\psi(1/4+it/2)-\log\pi,\quad
a_0=A_\infty(0)=\psi(1/4)-\log\pi.
$$
For u>0 define
$$
\nu_\infty(u)=\frac{e^{-u/2}}{1-e^{-2u}}>0.
$$
From the convergent digamma difference representation, for every real t,
$$
\boxed{A_\infty(t)-a_0
=2\int_0^\infty \nu_\infty(u)(1-\cos(tu))\,du.}
$$
Proof: the digamma difference is
Re psi(a+iy)-psi(a)=integral_0^infty e^{-av}(1-cos(yv))/(1-e^{-v}) dv for a>0; set a=1/4, y=t/2 and v=2u. This is absolutely convergent: nu(u)~1/(2u) as u->0 and nu(u)=O(e^{-u/2}) at infinity; 1-cos(tu)=O(u²).

Let S_u f(x)=f(x-u) act unitarily on L²(R). For smooth compactly supported f define
$$
\mathcal E_\infty(f)=\int_0^\infty \nu_\infty(u)\,\|f-S_u f\|_2^2\,du\ge0.
$$
By Plancherel,
$$
\mathcal E_\infty(f)=\frac1{2\pi}\int_{\mathbb R}
|\widehat f(t)|^2[A_\infty(t)-a_0]\,dt.
$$
Hence its associated nonnegative selfadjoint generator has **formal** symmetric difference formula on Schwartz functions:
$$
(\mathcal L_\infty f)(x)
=\int_0^\infty \nu_\infty(u)
[2f(x)-f(x-u)-f(x+u)]\,du.
$$
Near u=0 the bracket is O(u²), making the integral convergent. The closed quadratic-form domain is the Fourier-log space with integral |hat f|²(A_inf-a0) finite; equivalent at high frequency to integral log(2+|t|)|hat f|² finite (up to finite-frequency constants). This is the canonical unbounded archimedean environmental form selected by the genuine Gamma factor, not a bounded Gram or a free parameter.

The symmetric measure nu_infty(|u|) du on R\{0} satisfies integral min(1,u²)nu<infinity. So A_inf(t)-a0 is a continuous conditionally negative definite Levy-Khintchine exponent. The **positive shifted form itself is generic CND**, insufficient for RH.

For a primitive Dirichlet L(s,chi), conductor q and parity epsilon in {0,1}, the local archimedean family is
$$
A_{q,\epsilon}(t)=\log(q/\pi)+\Re\psi\!\left(\frac{1/2+\epsilon+it}{2}\right).
$$
Exactly the same derivation works with
$$
\nu_{\infty,\epsilon}(u)
=\frac{e^{-(1/2+\epsilon)u}}{1-e^{-2u}}.
$$
The conductor appears as a constant, not in the jump energy. This is calibrated for the ODD primitive mod-5 quartic character, matching the Davenport–Heilbronn control's arch parity, without claiming RH for either system.

## 2. Explicit completed zeta Weil-symbol energy (IDENTITY, not positivity)

Fix L>0 and f in C_c^\infty((-L,L)), regarded as zero extended in L²(R). Put
$$
w_{p^k}=\frac{\log p}{p^{k/2}},\quad a_{p^k}=k\log p,\quad
S_L=\sum_{p^k<e^{2L}}w_{p^k}.
$$
In the repo's explicit-formula normalization
$$
\Psi_L(t)=A_\infty(t)-2\sum_{p^k<e^{2L}}w_{p^k}\cos(t a_{p^k})
$$
(the additional pole term is separate). Define the positive *discrete* source energy
$$
\mathcal E_{P,L}(f)=\sum_{p^k<e^{2L}}w_{p^k}\|f-S_{a_{p^k}}f\|_2^2.
$$
Then the exact zero-free quadratic identity is
$$
\boxed{
Q_L(f)=\mathrm{Pole}_L(f)
+\mathcal E_\infty(f)+\mathcal E_{P,L}(f)
+(a_0-2S_L)\|f\|_2^2.
}
$$
It follows by Plancherel and the elementary identity ||f-S_a f||²=2||f||²-2 Re<f,S_a f>. The pole is the correctly normalized rank-two evaluation form specified in the repo; no positivity is assumed for it. Endpoint a=2L can be included with no overlap for smooth compact support.

**This earns a representation of the Gamma environment on the SAME two-sided shift group as the actual prime rays**, with a singular continuum of small shifts plus discrete prime-power impulses, and it explains the failed bounded Tate-range lift. It does NOT give Weil positivity. The positive energies also exist after a fake positive impulse at n=6: the extra negative scalar debit precisely accompanies that new jump, and the sign still fails unless an independent GLOBAL constraint holds.

## 3. Two falsifiers and their outcomes

**Falsifier A — delete the ultraviolet environment:** For epsilon>0, define
Phi_epsilon(t)=2 integral_epsilon^infinity nu(u)(1-cos(tu))du.
Then
$$
0\le\Phi_\epsilon(t)\le4\int_\epsilon^\infty\nu(u)\,du<\infty
$$
for all real t. But A_inf(t)-a0~log |t|->infinity. Hence NO FIXED positive cutoff epsilon can reproduce the exact archimedean operator at arbitrarily high frequency. The near-origin 1/u singularity is necessary; fitting a bounded return operator fails by an exact unboundedness obstruction.

**Falsifier B — separate Poincare bounds do not pay the sign:** On f supported in [-L,L], let m(u)=ceil(2L/u). The sharp compressed-shift bound gives
||f-S_u f||²>=2(1-cos(pi/(m(u)+1)))||f||².
Therefore
$$
\mathcal E_\infty(f)\ge\gamma_\infty(L)||f||²,\quad
\gamma_\infty(L)=2\int_0^\infty\nu_\infty(u)
\left[1-\cos\frac{\pi}{\lceil 2L/u\rceil+1}\right]du.
$$
The full archimedean PLUS PRIME SYMBOL (NOT including the pole) admits the unconditional lower bound
$$
a_0+\gamma_\infty(L)
-2\sum_{p^k<e^{2L}}w_{p^k}
\cos\!\left(\frac{\pi}{\lceil2L/(k\log p)\rceil+1}\right).
$$
With F(u)=artanh(e^{-u/2})+arctan(e^{-u/2}), integral_a^b nu=F(a)-F(b); gamma_infty is evaluated by the absolutely convergent sum across intervals u in [2L/m,2L/(m-1)] (m>=2) plus u>=2L (m=1). Approximations (M=60,000 terms):
 L=0.04 bound +0.7023 (prime-free);
 L=0.078 +0.0093 (prime-free);
 L=0.080 -0.0174 (prime-free);
 L=0.34 -1.6300 (prime-free);
 L=0.36 -2.1894 (p=2 active);
 L=0.80 -4.4078 (p=2,3,4 active);
 L=1.20 -8.1232 (eight prime-power events).
These are **lower-bound values**, not evidence of any negative Weil eigenvalue. Pole terms are omitted, so do not promote the tiny-window positive numbers to a RH certificate. The bound fails to show positivity well before known prime-free/Zhu windows. H6 REFUTED as a sufficient independent domination method. The missing correlation is joint, source-specific and coupled with the pole; separately positive shift energies cannot force the required cancellation.

## 4. Executed independent calibrations (not proof of infinite signs)

scripts/gamma_arch_continuum.py, mpmath dps40, source-zero-free:
- zeta/even gamma A(0)=-5.37218341922566558; t=.25,1,3,10: integral-vs-digamma errors 1.722e-19,1.657e-19,1.082e-19,1.202e-19 respectively.
- odd conductor-5 gamma: t=.25,1,3,10 gave 0.04040896491705772, 0.4764595239318235, 1.486853755915267, 2.694881392500945, matching the independently evaluated digamma differences.
- independent SciPy u-space vs Fourier Gaussian quadratic energy: 1.888225660762 versus 1.888225660762, absolute residual 4.44e-16.
- fake connected n=6 with delta=.02: direct source contribution -0.01792648010569991, exactly equal to the positive shift-square change MINUS its -2delta diagonal debit.
- New test suite locally: 14/14 tests PASS (9 height bridge, 5 continuum). These tests do not establish global Q positivity.

## 5. What was constructed; where the proof debt remains

HTR-13 (archimedean Gamma as positive singular continuous-shift form): PROVED, classical special-function identity and closed-form realization.
HTR-14 (odd/conductor-5 family with exact density): PROVED by same integral theorem; OBSERVED numerical controls.
HTR-15 (cutting off infinitesimal shifts cannot reproduce Gamma high-frequency): PROVED.
HTR-16 (separate Poincare lower bound suffices through meaningful Weil windows): REFUTED as a certificate by the stated negative bound; no assertion of negative actual Q.
HTR-17 (full arithmetic Q decomposes as arch continuous plus discrete prime energy plus negative scalar and separate pole): PROVED as a Fourier identity in stated test domain. THIS IDENTITY IS NOT AN INDEPENDENT SIGN.
HTR-18 (source-derived self-product dualizing/Hodge intersection giving Q>=0 for all tests): UNVERIFIED/OPEN.

**Next lamp, not another identical bound:** derive a source-only mixed prime/continuum *intersection* or renormalized trace on a declared adelic/categorical correspondence space, with the actual conductor/gamma/poles, and prove a **new joint inequality or exact trace identity**. The negative scalar bulk is the unpaid debt. Use source-true chi versus DH, fake 6, shifted log2, and nonunit alpha2; a generic CND Lévy generator is not the fourth gate.

Primary analytic background: digamma integral (standard, derivable from Euler integral), Tate's local Gaussian Gamma, Connes–Consani 2023 curve-level arithmetic duality, 2015 arithmetic-site square and 2026 absolute inversion papers. The present Lévy form is an analytic shadow of the archimedean place, NOT an actual dualizing sheaf on the arithmetic self-product.
