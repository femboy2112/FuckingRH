# Collapse law of the finite-place-only stability radius

**Date:** 2026-10-06
**Status:** OBSERVED-FINITE quantitative law + mechanism (toward directive-E / C84 theorem). RH open.
Reproduce: `scripts/collapse_rate.py`.

## Result

For the finite-place-only tilt $w_n\to\Lambda(n)n^{-1/2-\epsilon}$, the reduced-kernel stability radius
(positive side) obeys, empirically to $\pm15\%$ over $T\in[5,10]$,
\[
\boxed{\ \epsilon_+(T)\ \approx\ C\,\frac{\lambda_0(T)}{\|K^{(1)}_T\|},\qquad C\approx34,\ }
\]
where $\lambda_0(T)=\lambda_{\min}(K^\circ_0)$ is the reduced spectral floor (slowly decaying,
$0.00595\to0.00367$) and $K^{(1)}=\mathrm{screw}(\partial_\epsilon\Psi)$ is the tilt-derivative screw
kernel with
\[
\partial_\epsilon\Psi(t)=\sum_{n\le e^t}\frac{\Lambda(n)\log n}{\sqrt n}\,(t-\log n),\qquad
\|K^{(1)}_T\|\sim e^{0.86\,T}\ (\text{an explicit Euler/PNT sum}).
\]
Measured $C=\epsilon_+\|K^{(1)}\|/\lambda_0$: $30.4,28.4,36.3,39.0,34.5,37.9$ for $T=5..10$.

## Mechanism

The crossing is **linear-sensitivity-limited**: as $\epsilon$ grows, the first eigenvalue to reach $0$
is the mode most coupled to the tilt direction $K^{(1)}$ (not necessarily the $\epsilon=0$ minimum), and
it reaches $0$ when $\epsilon\cdot(\text{its sensitivity})\sim\lambda_0$. The sensitivity scale is set by
$\|K^{(1)}\|$, which grows exponentially because $\partial_\epsilon\Psi$ weights the primes by the extra
factor $\log n$ and sums an $n^{-1/2}$ tail to $n\le e^T$ (so $\sim Te^{T/2}$ pointwise, and the screw-kernel
norm $\sim e^{0.86T}$). The spectral floor $\lambda_0$ decays only slowly. Hence
$\operatorname{rad}(\mathcal E_L)\asymp e^{-cL}$ with $c\approx0.86$.

## Toward a theorem (directive E)

A rigorous $\operatorname{rad}(\mathcal E_L)\le Ce^{-cL}$ now reduces to three tractable pieces:
1. **$\|K^{(1)}_L\|\gtrsim e^{cL}$** — a lower bound on an explicit von-Mangoldt–weighted Euler sum (PNT).
2. **$\lambda_0(L)\le \mathrm{poly}(L)$** — an upper bound on the reduced spectral floor (plausible; it is
   observed to *decay*).
3. The **linear-sensitivity crossing** estimate (first-order eigenvalue perturbation along $K^{(1)}$).
This is a genuine quantitative target *short of RH* and independent of zero locations — a clean place to
earn a real theorem. (Status: the law is OBSERVED-FINITE; the bound is CONJECTURED.)
