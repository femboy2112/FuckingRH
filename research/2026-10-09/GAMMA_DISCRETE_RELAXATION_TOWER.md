# A countable, uniquely specified archimedean relaxation tower

Date 2026-10-09. **RH OPEN**. Bounded research round R-G from the HTR-13 continuum. The spectrum here is Gamma/trivial-factor pole geometry, **not** zeta's nontrivial zero ordinates. Mathematical novelty outside this research program is NOT claimed; the formula follows from the standard digamma partial fraction expansion.

## Preregistered probe

H8: The true Gamma continuum has a countable, canonical positive-mode decomposition at EXACT frequencies determined by the real place, including a detectable parity shift. Outcomes:
- PASS if the same exact digamma difference arises as a positive monotone sum with explicit certified tail bounds for even and odd parity; reject if wrong Gamma values, signs, parity or cutoff behavior.
- NO RH ADVANCE if the decomposition also exists with fake Euler data; its positivity would be an archimedean property, not the global arithmetic sign.
- Look for a new obstruction if a fake parity gamma factor cannot be confused with the correct arch factor under primary normalization.

## Theorem (proved from the classical Gamma integral)

For epsilon in {0,1} and m>=0 put lambda_(m,eps)=2m+1/2+epsilon. Define
$$
\Phi_\epsilon(t)=\Re\psi((1+2\epsilon)/4+it/2)-\psi((1+2\epsilon)/4).
$$
Then for every real t,
$$
\boxed{\Phi_\epsilon(t)=2\sum_{m=0}^\infty
\frac{t^2}{\lambda_{m,\epsilon}
(\lambda_{m,\epsilon}^2+t^2)}.}
$$
Every term is nonnegative. With the continuum density from GAMMA_CONTINUUM_DUALIZING_TRACE.md,
$$
\nu_{\infty,\epsilon}(u)=\frac{e^{-(1/2+\epsilon)u}}{1-e^{-2u}}
=\sum_{m\ge0}e^{-\lambda_{m,\epsilon}u},\quad u>0.
$$
Tonelli's theorem (nonnegative integrand) gives
$$
2\int_0^\infty\nu_{\infty,\epsilon}(u)(1-\cos tu)\,du
=2\sum_{m\ge0}\int_0^\infty e^{-\lambda_{m,\epsilon}u}(1-\cos tu)\,du,
$$
and the Laplace integral is t²/[lambda(lambda²+t²)]. This proves the identity without zeros or unproved exchange-of-limit claims.

For M>=1, truncation Phi_epsilon,M at m<M has a *rigorous pointwise remainder*
$$
\boxed{0\le\Phi_\epsilon(t)-\Phi_{\epsilon,M}(t)
\le \frac{2t^2}{(2M+1/2+\epsilon)^3}
+\frac{t^2}{2(2M+1/2+\epsilon)^2}.}
$$
Proof: termwise tail ≤2t²/lambda³; decreasing-integral upper bound for the lattice lambda=2m+c yields 2t²[lambda_M^-3+(4lambda_M²)^-1].

The partial jump-density series increases to the full positive density; by monotone convergence, the finite nonnegative quadratic forms increase to the exact closed Gamma form on its declared domain. Conversely, each FINITE M has a bounded Fourier multiplier (sum of bounded rational terms). Thus ultraviolet unboundedness is again an infinite-completion effect, rather than a defect of individual modes.

The two parity spectra are genuinely distinct: lambda_even = {0.5,2.5,4.5,...}, lambda_odd = {1.5,3.5,5.5,...}. They are pole locations for meromorphic digamma Gamma factors in the continued spectral variable, NOT input nontrivial zeros. Conductor q simply adds log q/pi to the full symbol and does not alter these modes.

## Fresh holdout: actual execution of scripts/gamma_tower_holdout.py

Independent of fitting/inspiring data: t=.731, 3.7, 17.25, parities even and odd, partial mode counts M=16,64,256. Each residual was nonnegative and BELOW the proved analytic bound; increasing M decreased the residual. Sample values:
- even, t=.731, M=256: residual 1.02120e−6 versus bound 1.02516e−6.
- even, t=3.7, M=256: residual 2.61619e−5 versus bound 2.62641e−5.
- even, t=17.25, M=256: residual 5.6834e−4 versus bound 5.7087e−4.
- odd, t=.731, M=256: residual 1.01722e−6 versus bound 1.02116e−6.
- odd, t=3.7, M=256: residual 2.60599e−5 versus bound 2.61615e−5.
- odd, t=17.25, M=256: residual 5.66126e−4 versus bound 5.6864e−4.
- Wrong parity at t=3.7 changes the arch digamma *difference* by 3.141536421094, a substantial falsifier of pretending the same archimedean parameter is universal.

The executable contains actual assertions and prints all 18 residual/bound pairs; it was executed locally. This is not independent validation of RH or a novel gamma theorem.

## Result, defect, next lamp

**HTR-19 PROVED (classical derivation):** uniquely normalized even/odd Gamma *candidate* resolves into a countable positive relaxation-mode tower with explicit error bounds. This realizes the archimedean 'environment' as discrete positive relaxation channels whose total infinite accumulation produces the singular u≈0 Gamma continuum.

**HTR-20 REFUTED as implication:** 'mode-by-mode positive Gamma energy forces Weil positivity' is still false as an argument: negative contact/bulk and source-specific prime correlations remain unpaid, and the mode decomposition persists for fake Dirichlet sources. No full Weil sign was proved. Gamma can be recognized independently by its parity-dependent mode spectrum, but not by the sign of its positive pieces alone.

**Next coherent mathematical attack:** build the global coupling/trace between real-place relaxation modes and the true prime rays inside a source-determined adelic or arithmetic surface correspondence, with exact Γ, conductor, pole, connected-atom filters and an independent primitive Hodge sign. The Gamma tower provides a canonical archimedean normalization to falsify candidate dualizing traces. Another isolated positive tower will be RH-inert.
