# Critical KMS bridge for prime towers

**Date:** 2026-10-05  
**Status:** exact local bridge + global proof target. RH remains open.

This note records a concrete bridge between Astra Round 002's repaired prime-tower Gram block, the profinite successor picture, and the Bost-Connes critical KMS state.

## 1. Bost-Connes local measure at critical half-density

Neshveyev's formulation of the Bost-Connes system gives, for each beta>0, a product measure

\[
\mu_\beta=\bigotimes_p\mu_{\beta,p}
\]

on the finite adeles, normalized by

\[
\mu_\beta(\widehat{\mathbb Z})=1,
\]

and satisfying the scaling rule

\[
\mu_\beta(q^{-1}X)=q^\beta\mu_\beta(X).
\]

Equivalently, on one local factor,

\[
\mu_{\beta,p}(p^k\mathbb Z_p)=p^{-k\beta}.
\]

At the critical value beta=1/2,

\[
\boxed{
\mu_{1/2,p}(p^k\mathbb Z_p)=p^{-k/2}.
}
\]

Thus Suzuki's exact event weight is

\[
\boxed{
\frac{\Lambda(p^k)}{\sqrt{p^k}}
=
(\log p)\,\mu_{1/2,p}(p^k\mathbb Z_p).
}
\]

So the critical half-density weight is literally the critical KMS mass of the depth-k p-adic divisibility ball.

## 2. Valuation distribution

Put

\[
r=p^{-1/2}.
\]

For the valuation random variable

\[
V_p(x)=v_p(x)
\]

under the normalized local critical KMS measure on \(\mathbb Z_p\),

\[
\Pr(V_p\ge k)=r^k,
\]

and therefore

\[
\boxed{
\Pr(V_p=k)=(1-r)r^k,\qquad k\ge0.
}
\]

Hence

\[
\mathbb E[V_p]=\frac{r}{1-r}.
\]

The Round-002 sharp repair coefficient is therefore

\[
\boxed{
M_p
=
\frac{\log p}{\sqrt p-1}
=
(\log p)\,\mathbb E_{\mu_{1/2,p}}[V_p].
}
\]

The common Brownian repair tax is exactly the critical KMS mean valuation energy.

## 3. Raw and repaired towers as critical KMS expectations

Round 002 defines

\[
h_p(t)
=
(\log p)\sum_{k\ge1}r^k(t-k\log p)_+
\]

for t>=0 and

\[
D_p(t)=M_p t-h_p(t)
=
(\log p)\sum_{k\ge1}r^k\min(t,k\log p).
\]

Using the valuation law above gives the exact formulas

\[
\boxed{
h_p(t)
=
\frac{\log p}{1-r}
\mathbb E\left[
(t-V_p\log p)_+\mathbf1_{V_p\ge1}
\right],
}
\]

\[
\boxed{
D_p(t)
=
\frac{\log p}{1-r}
\mathbb E\left[
\min(t,V_p\log p)
\right].
}
\]

Equivalently, conditioning on p-divisibility,

\[
\boxed{
D_p(t)
=
M_p\,
\mathbb E\left[
\min(t,V_p\log p)\mid V_p\ge1
\right].
}
\]

Thus the spring-bank interpretation is exact: a prime tower is a random critical-KMS depth threshold, the raw tower is the expected post-threshold ramp, and the positive repair is the expected stored/pre-threshold length.

## 4. Round-002 vector amplitudes are the critical KMS Hilbert normalization

Neshveyev's local Hilbert-space decomposition shows that

\[
n^{-\beta/2}V_n^*
\]

is isometric between the corresponding valuation-shell subspaces.

At beta=1/2, the normalization is

\[
n^{-1/4}.
\]

For n=p^k this is

\[
p^{-k/4}.
\]

Round 002's interval Gram vector for the kth tower level has amplitude

\[
\sqrt{(\log p)p^{-k/2}}
=
\sqrt{\log p}\,p^{-k/4}.
\]

Hence the nontrivial quarter-density amplitude in the Gram vector is exactly the critical KMS isometric normalization.

## 5. Nested-ball chain and its Gram matrix

Use normalized Haar measure on \(\mathbb Z_p\) and define

\[
\phi_{p,k}
=
p^{k/2}\mathbf1_{p^k\mathbb Z_p}.
\]

Then \(\|\phi_{p,k}\|_2=1\), and for k,l>=0,

\[
\boxed{
\langle\phi_{p,k},\phi_{p,l}\rangle
=
p^{-|k-l|/2}
=
r^{|k-l|}.
}
\]

Thus the p-adic depth chain has the stationary AR(1)/Poisson-kernel Gram matrix.

Its spectral density on the scale circle is

\[
\boxed{
P_r(\theta)
=
\frac{1-r^2}{1-2r\cos\theta+r^2}.
}
\]

This is also

\[
P_r(\theta)
=
(1-r^2)
\left|
L_p\left(\frac12+i\frac{\theta}{\log p}\right)
\right|^2.
\]

So the local Euler factor is an outer spectral factor of the canonical normalized p-adic scale chain.

The local scattering ratio

\[
\rho_p\left(\frac12+is\right)
=
\frac{1-re^{i(\log p)s}}{1-re^{-i(\log p)s}}
\]

is exactly the phase ratio of that spectral factor.

## 6. The complete repaired tower is one scale derivative

Let

\[
g_p
=
\sqrt{\frac{r}{2(1-r)^2}}
(\phi_{p,1}-\phi_{p,0}).
\]

The scale-gradient spectral density is

\[
\frac{r}{2(1-r)^2}
|1-e^{i\theta}|^2P_r(\theta).
\]

But the exact identity

\[
\boxed{
\sum_{k\ge1}r^k(1-\cos k\theta)
=
\frac{r}{(1-r)^2}
(1-\cos\theta)P_r(\theta)
}
\]

shows that this is precisely the positive spectral numerator of the full repaired tower.

Equivalently,

\[
\boxed{
\text{all infinitely many prime-power spring levels}
=
\text{one first-difference energy on the canonical p-adic scale chain}.
}
\]

This is a genuine Occam reduction.

## 7. Relation to the Round-002 Levy measure

Round 002 gives

\[
\nu_p(dx)
=
\frac{\log p}{\pi x^2}
\sum_{k\ge1}r^k
[1-\cos(k\log p\,x)]\,dx.
\]

Using the previous identity,

\[
\boxed{
\nu_p(dx)
=
\frac{\log p}{\pi x^2}
\frac{r}{(1-r)^2}
[1-\cos(\log p\,x)]
P_r(\log p\,x)\,dx.
}
\]

Thus the repaired tower CND exponent is the twice-integrated spectral energy of the p-adic scale gradient.

The \(1/x^2\) factor is the Green/inverse-second-derivative step converting accelerant energy into a variogram.

## 8. Global prime ramp as a positive critical-KMS expectation

For fixed t, only primes p<=e^t contribute to the raw ramp.

Define the local positive observable on \(\mathbb Z_p\)

\[
F_{p,t}(x)
=
\frac{\log p}{1-p^{-1/2}}
\left(t-v_p(x)\log p\right)_+
\mathbf1_{v_p(x)\ge1}.
\]

Then

\[
\boxed{
h_p(t)
=
\int_{\mathbb Z_p}
F_{p,t}(x)\,d\mu_{1/2,p}(x).
}
\]

Therefore on the product critical KMS state,

\[
\boxed{
P(t)
=
\int_{\widehat{\mathbb Z}}
\left(
\sum_{p\le e^t}F_{p,t}(x_p)
\right)
d\mu_{1/2}(x).
}
\]

The finite-prime side of Suzuki's formula is therefore the expectation of an explicitly positive observable in the canonical critical Bost-Connes equilibrium state.

The RH problem becomes

\[
\boxed{
A_\infty(t)
\ge
\phi_{1/2}(F_t)
\qquad
\forall t\ge0.
}
\]

This is still RH-equivalent, but it is now a thermodynamic/operator inequality inside a genuine positive state rather than a formal analytically continued Euler sum.

## 9. Why the critical KMS state is a real renormalization

For beta>1 the Bost-Connes equilibrium state has an ordinary Gibbs description with partition function

\[
\zeta(\beta).
\]

At beta<=1, the ordinary Gibbs decomposition over integer shells breaks down, but a unique positive KMS state still exists.

At beta=1/2:

- the positive local masses \(p^{-k/2}\) still exist exactly;
- the total prime energy expectation
  \[
  \sum_p\frac{\log p}{\sqrt p-1}
  \]
  diverges;
- the state is nevertheless a valid positive type-III equilibrium state.

Thus the critical system performs positivity **before** decomposing into a divergent trace-class Gibbs sum.

This is precisely the order of operations suggested by the failed local-repair program.

## 10. Successor is not a symmetry of the critical KMS measure

The critical local measure is not additive Haar measure.

At beta=1, the local measure is Haar and translation by 1 is measure-preserving.

At beta=1/2, the residue class 0 mod p has mass

\[
p^{-1/2},
\]

while every nonzero residue class has mass

\[
\frac{1-p^{-1/2}}{p-1}.
\]

Translation by 1 moves the distinguished heavy residue class, so it is not measure-preserving.

In the full product over primes, the mismatch occurs at infinitely many coordinates.

Therefore the succ-light-cone should not be modeled as a unitary translation symmetry of the critical KMS state.

Instead successor is a **path/correspondence through a weighted adelic state space**.

This explains why adding the ordinary translation unitary to the multiplicative Bost-Connes system is not a trivial extension at beta=1/2.

## 11. The ax+b algebra is the natural enlarged state/operator space

Cuntz's arithmetic \(ax+b\) algebra over \(\mathbb N\) is obtained from the Bost-Connes arithmetic system by adjoining a unitary corresponding to addition.

Its stabilization is described using the finite adeles and the affine \(ax+b\) action over \(\mathbb Q\).

Thus the correct enlarged causal object should involve:

- finite-adelic/profinite state;
- multiplicative scaling operators;
- additive successor/translation;
- a nontrivial critical modular/KMS metric.

The bare number line is only the endpoint projection.

## 12. New local theorem accomplished

The immediate one-prime goal posed after Round 003 is now paid:

> Find a canonical positive p-adic operator/Hilbert object whose Gram/spectral data reproduces Astra's repaired tower \(D_p\).

The normalized nested-ball scale chain plus one first difference does exactly that.

What remains unpaid is the **one-prime-plus-infinity coupling**.

## 13. Next exact global target

Construct an Archimedean cyclic scale process from the Gaussian vacuum under unitary dilations.

For the normalized Gaussian \(g_\infty\), the dilation correlation is

\[
\langle g_\infty,U_tg_\infty\rangle
=
\operatorname{sech}(t)^{1/2},
\]

and its Mellin spectral density is proportional to

\[
\left|
\pi^{-(1/2+is)/2}
\Gamma\left(\frac{1/2+is}{2}\right)
\right|^2.
\]

Thus, exactly as at finite p, the Archimedean local factor is the spectral factor of the canonical local vacuum under scale evolution.

The next construction problem is therefore no longer vague:

\[
\boxed{
\text{couple the finite p-adic scale-gradient process and the Archimedean Gaussian scale process in one positive semilocal metric}
}
\]

and calculate its complete Gram pullback.

It must reproduce

\[
K_{A_\infty+D_p-M_p|\cdot|}
\]

for the one-prime-plus-infinity model, or a finite Brownian lift of it with explicitly derived coefficient.

## 14. Proof seam after the local solution

For a finite set F of primes, seek a positive semilocal Gram map whose pullback is

\[
K_{A_\infty}
+
\sum_{p\in F}K_{D_p}
-
M_FK_{|\cdot|}
+
c_FK_{|\cdot|}.
\]

Equivalently,

\[
K_{\Psi_F+c_F|\cdot|}.
\]

If the construction gives

\[
0\le c_F\le C
\]

uniformly along the arithmetic wavefront, Round 003's uniform-lift theorem forces RH.

The remaining theorem is now specifically an Archimedean/finite-place coupling theorem, not a local prime-tower construction problem.
