# Local L-factor whitening and the critical beta flow

**Date:** 2026-10-05  
**Status:** exact local operator identities / global bridge target. RH remains open.

## 1. Finite Euler factors are spectral factors of p-adic depth

Let

\[
r=p^{-1/2},
\qquad
\phi_k=p^{k/2}\mathbf1_{p^k\mathbb Z_p}.
\]

Then

\[
\langle\phi_k,\phi_l\rangle=r^{|k-l|}.
\]

The stationary spectral density of this Toeplitz chain is

\[
P_r(\theta)
=
\frac{1-r^2}{|1-re^{i\theta}|^2}.
\]

But

\[
L_p\left(\frac12+i\frac{\theta}{\log p}\right)
=
\frac1{1-re^{-i\theta}}.
\]

Hence

\[
\boxed{
P_r(\theta)
=
(1-r^2)
\left|
L_p\left(\frac12+i\frac{\theta}{\log p}\right)
\right|^2.
}
\]

Thus the local Euler factor is the outer spectral factor of the canonical p-adic depth process.

## 2. Inverse Euler factor is the whitening filter

Set

\[
m_p(\theta)=1-re^{i\theta}.
\]

Then

\[
\boxed{
|m_p(\theta)|^2P_r(\theta)=1-r^2.
}
\]

Therefore multiplication by

\[
\frac{m_p}{\sqrt{1-r^2}}
\]

maps the cyclic spectral metric of the p-adic depth process to flat white spectral measure.

In signal language:

\[
\boxed{
L_p=\text{coloring filter},
\qquad
L_p^{-1}=\text{whitening filter}.
}
\]

This gives a natural metric interpretation of the finite inverse-local-factor multipliers used in semilocal adelic/Sonin constructions.

## 3. Repaired tower is a high-pass energy of the colored depth process

The exact identity

\[
\sum_{k\ge1}r^k(1-\cos k\theta)
=
\frac{r}{(1-r)^2}(1-\cos\theta)P_r(\theta)
\]

shows

\[
M_p-P_p(\theta)
=
(\log p)\frac{r}{(1-r)^2}
(1-\cos\theta)P_r(\theta).
\]

Equivalently,

\[
M_p-P_p(\theta)
=
\frac{\log p}{2}
\frac{r(1+r)}{1-r}
\left|
\frac{1-e^{i\theta}}
     {1-re^{i\theta}}
\right|^2.
\]

Thus the repaired tower is the energy of a one-step scale high-pass filter applied to the colored local vacuum.

After whitening, the remaining numerator is the universal discrete difference

\[
1-e^{i\theta}.
\]

All prime dependence is then carried by:

- clock scaling \(\theta=(\log p)s\);
- normalization constants;
- the whitening/coloring map.

## 4. Archimedean analogue

For the normalized real Gaussian under unitary dilations, the cyclic Mellin spectral density is proportional to

\[
\left|
L_\infty\left(\frac12+is\right)
\right|^2,
\qquad
L_\infty(z)=\pi^{-z/2}\Gamma(z/2).
\]

Therefore division by \(L_\infty\) whitens the Archimedean scale vacuum in the same spectral sense.

This places finite and infinite places in one template:

\[
\boxed{
\text{canonical local vacuum}
\overset{L_v^{-1}}{\longrightarrow}
\text{flat spectral substrate}.
}
\]

The local scattering ratio

\[
\rho_v(z)=L_v(z)/L_v(1-z)
\]

records the boundary phase of the same spectral factor.

## 5. Relation to the semilocal Sonin multiplier

For a finite set of primes \(F\), the canonical finite multiplier is

\[
m_F(s)
=
\prod_{p\in F}
(1-p^{-1/2-is})
=
\prod_{p\in F}
L_p(1/2+is)^{-1}.
\]

Thus this multiplier is exactly the product of local whitening filters.

Round 003 showed that its norm increment in the **flat ambient Mellin metric** is signed and is not the repaired tower energy.

The present identity explains the type mismatch:

> the multiplier is isometric/whitening relative to the local cyclic/KMS spectral metric, not relative to the unweighted flat metric before the local vacuum is included.

This does not invalidate the Round-003 no-go. It specifies a different, explicit metric that must be used by any new comparison.

The next one-prime-plus-infinity calculation should therefore pull the semilocal map back through the local cyclic spectral factors before comparing Gram energies.

## 6. Critical beta flow on local valuation depth

For general beta>0 let

\[
r_\beta=p^{-\beta}
\]

and let \(V_{\beta,p}\) have geometric law

\[
\Pr(V_{\beta,p}=k)
=
(1-r_\beta)r_\beta^k.
\]

This is exactly the valuation depth under the local Bost-Connes KMS_beta measure.

Its probability generating function is

\[
G_\beta(z)
=
\frac{1-r_\beta}{1-r_\beta z}.
\]

If \(0<\beta_2<\beta_1\), then \(r_{\beta_2}>r_{\beta_1}\), and

\[
\log\frac{G_{\beta_2}(z)}{G_{\beta_1}(z)}
=
\sum_{k\ge1}
\frac{r_{\beta_2}^k-r_{\beta_1}^k}{k}
(z^k-1).
\]

All coefficients are nonnegative.

Therefore there exists an independent compound-Poisson random variable \(J\)
with jump-size-k intensity

\[
\boxed{
\lambda_k
=
\frac{p^{-k\beta_2}-p^{-k\beta_1}}{k}
}
\]

such that

\[
\boxed{
V_{\beta_2,p}
\overset d=
V_{\beta_1,p}+J.
}
\]

Thus lowering beta is a positivity-preserving local jump flow which adds valuation depth.

## 7. Exact match to Suzuki's shifted prime weights

Suzuki's shifted family uses finite-place weights

\[
(\log p)p^{-k(1/2+\omega)}.
\]

Set

\[
\beta=\frac12+\omega.
\]

Then

\[
\boxed{
(\log p)p^{-k(1/2+\omega)}
=
(\log p)\Pr_{\mu_{\beta,p}}(V_p\ge k).
}
\]

So Suzuki's horizontal shift parameter and the Bost-Connes inverse-temperature parameter agree exactly on the finite-place prime-tower data.

At

\[
\omega=\frac12
\quad\Longleftrightarrow\quad
\beta=1,
\]

the local critical measure becomes additive Haar measure on \(\mathbb Z_p\).

At

\[
\omega=0
\quad\Longleftrightarrow\quad
\beta=\frac12,
\]

one reaches the RH-critical half-density.

## 8. Why this still does not prove monotonicity of the completed Suzuki object

The local valuation-depth flow is positive and explicit.

But the completed function also contains:

- the Archimedean Gamma block;
- pole/codegree modes;
- the global Brownian/common-mode subtraction.

No theorem here shows that the full screw kernel remains PSD as beta is lowered from 1 to 1/2.

If such a completely positive completed flow existed, it would close RH.

Thus the KMS beta flow identifies the correct finite-place interpolation and isolates the missing coupling at infinity; it does not silently solve it.
