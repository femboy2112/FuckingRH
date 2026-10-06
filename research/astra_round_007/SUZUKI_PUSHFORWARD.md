# Exact pushforward to Suzuki and the residual inertia theorem

RH OPEN. All formulas below follow from the prime/Archimedean definition;
no zero ordinates enter the construction.

Put `I_t=1_[0,t]` for `t>=0`. These indicators belong to the finite Gamma
logarithmic-energy domain: `||tau_u I_t-I_t||²=2min(u,t)`, integrable against
`k(u)`. Polarization extends the Weil form to their finite linear span.
Since their autocorrelations are twice the normalized tents,
\[
\mathcal W(I_t)=2\Psi(t),\qquad
W(I_t*\widetilde I_u)=K_\Psi(t,u).
\]
The second identity follows by polarization and translation invariance:
`I_t-I_u` is a translate, up to sign, of `I_|t-u|`.
This establishes the kernel comparison without a spectral representation.

## 1. Positive square pushforward

Use the first-order `D_N` from `WEIL_SQUARE_ATTEMPT.md`. Define
\[
G(t)=\int_0^\infty k(a)\min(|t|,a)da
=\sum_{j\ge0}\frac{1-e^{-(2j+1/2)|t|}}{(2j+1/2)^2}.
\]
Tonelli applies since all summands are nonnegative. The series is exactly
Suzuki's positive Lerch block. On `|t|<=log N`,
\[
E_N^{\rm var}(t)=G(t)+\sum_{n\le N}w_n\min(|t|,\log n)
=G(t)+S_N|t|-P(|t|).
\]
For the convention `K_h(t,u)=h(t)+h(u)-h(t-u)`,
\[
\langle D_N I_t,D_N I_u\rangle
=K_G(t,u)+\sum_{n\le N}w_n K_{\min(\cdot,\log n)}(t,u).
\]
In particular, the kernel for one capped distance is
`min(t,a)+min(u,a)-min(|t-u|,a)`; no normalization factor is hidden.
This is a carrier-truncated event square, and its Gamma component is exact.

## 2. Residual structure and arbitrary grid inertia

Write `B(t,u)=2min(t,u)`, `s(t)=sinh(t/2)`, and
`c(t)=cosh(t/2)-1`. With `c0=psi(1/4)-log pi`, exact subtraction gives
\[
\boxed{R_N(t,u)=K_\Psi(t,u)-\langle D_N I_t,D_N I_u\rangle
=8[s(t)s(u)-c(t)c(u)]-(S_N-c_0/2)B(t,u).} \tag{2}
\]
The hyperbolic pole term is rank at most two and indefinite; the other term
is a strictly negative Brownian kernel. The residual is not confined to the
last carrier slice or square threshold and does not vanish on a fixed window
as `N` grows. For fixed positive `t,u`, its Brownian coefficient diverges.

**Theorem.** On any `m` distinct positive grid points at most `log N`, the
matrix of `R_N` has at least `m-1` strictly negative eigenvalues.

**Proof.** The Brownian matrix is strictly positive definite: with increasing
times it factors as `2C diag(t_i-t_(i-1)) C*`, where C is the lower triangular
matrix of ones. On the codimension-one subspace orthogonal to the vector s,
\[
v^*R_Nv=-8|c^*v|^2-(S_N-c_0/2)v^*Bv<0.
\]
Min–max gives the assertion. This proves every grid size, not just the
computed cases. QED.

A concrete two-coordinate witness is `v=(s(t_2),-s(t_1),0,...)`. Arb certifies
its strict negative quadratic value at four horizons in
`evidence/square_residual.json`; separate horizons appear in the tests.
The sign certificate concerns **the discrepancy**, not `K_Psi` itself.
The numerical kernel identity check is implementation consistency; the
independent proof is (1), polarization and the elementary hyperbolic identity.

## 3. Consequences for the new geometry

Keeping orientations before squaring does recover the right negative prime
cross terms. The resulting positive square still overpays the scalar norm
by the exact amount above. An orthogonal extra sector cannot supply a negative
residual. Any fixed-rank boundary/coupling correction fails once enough test
directions are present. This is the promised exact comparison rather than a
Frobenius norm or a fitted PSD factor.

The square-root trial clock (`p²<=N`) must not replace the jet-hit horizon
(`p^k<=N`): doing that would delete the `k=1` events with `sqrt N<p<=N`.
The present calculation retains all visible events. Completing towers
independently merely changes `S_N` to a larger repair mass; it does not remove
the debit.

What remains is an infinite-dimensional coherent prime/Archimedean coupling,
with an exact map to the continuum test sector. Equation (2) specifies what
it must change. It does not supply that coupling or a strict reduction of RH.
