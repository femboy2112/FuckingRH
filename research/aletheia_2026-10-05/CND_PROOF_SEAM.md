# Exact CND seam for Suzuki's prime/Archimedean function

**Date:** 2026-10-05  
**Status:** exact reduction / proof seam. RH remains open.

Let

\[
\Psi(t)=A_\infty(t)-P(t)
\]

be Suzuki's exact even function.

## 1. Negative-definiteness target

Use the conditionally negative definite convention:

\[
\sum_{i,j}c_i\overline{c_j}\Psi(t_i-t_j)\le0
\qquad
\left(\sum_i c_i=0\right).
\]

Equivalently, the anchored screw kernel

\[
K_\Psi(s,u)=\Psi(s)+\Psi(u)-\Psi(s-u)
\]

is positive semidefinite on every finite set.

For Suzuki's exact function,

\[
\boxed{
\Psi\text{ is CND}
\iff
K_\Psi\succeq0
\iff
\mathrm{RH}.
}
\]

Thus an unconditional proof that \(A_\infty-P\) is CND is itself a proof of RH.

## 2. Exact finite-wavefront decomposition

For one prime \(p\), Round 002 defines

\[
h_p(t)
=
(\log p)\sum_{k\ge1}p^{-k/2}(|t|-k\log p)_+,
\]

\[
M_p=\frac{\log p}{\sqrt p-1},
\qquad
D_p(t)=M_p|t|-h_p(t).
\]

Each \(D_p\) is CND and has an explicit positive Hilbert/Gram representation.

Fix \(L>0\). On \(|t|\le L\), every active prime power \(p^k\) has \(p\le e^L\). Hence

\[
P(t)=\sum_{p\le e^L}h_p(t)
\]

on that window. Put

\[
M_L=\sum_{p\le e^L}M_p,
\qquad
D_L=\sum_{p\le e^L}D_p.
\]

Then exactly,

\[
\boxed{
\Psi(t)=A_\infty(t)+D_L(t)-M_L|t|
\qquad(|t|\le L).
}
\]

Passing to anchored kernels,

\[
\boxed{
K_\Psi
=
K_{A_\infty}
+
\sum_{p\le e^L}K_{D_p}
-
M_LK_{|\cdot|}
\qquad\text{on }[0,L].
}
\]

Since

\[
K_{|\cdot|}(s,u)=|s|+|u|-|s-u|
=2\min(s,u)
\]

for \(s,u\ge0\), the rightmost term is a Brownian covariance debt.

Therefore the exact finite-window proof obligation is

\[
\boxed{
K_{A_\infty}
+
\sum_{p\le e^L}K_{D_p}
\succeq
M_LK_{|\cdot|}
\quad\text{for every }L>0.
}
\tag{CND-SEAM}
\]

If CND-SEAM holds for every \(L\), then \(K_\Psi\succeq0\) globally and RH follows.

## 3. What is already paid and what is not

Paid:

- every \(K_{D_p}\) is explicitly PSD;
- the wavefront truncation is exact, not asymptotic;
- \(K_{|\cdot|}\) is explicit Brownian covariance;
- \(M_p=-L_p'/L_p(1/2)\);
- the analytically continued total \(M_p\)-sum matches Suzuki's Archimedean linear coefficient.

Unpaid:

- prove that the Archimedean term plus the positive prime-tower Gram blocks dominates the full Brownian debt \(M_LK_{|\cdot|}\);
- or construct a primitive/adelic quotient in which the same inequality is automatic before pulling back to the Suzuki tent family.

Scalar analytic continuation of \(\sum_pM_p\) is insufficient because it does not preserve the PSD/CND cone.

## 4. Equivalent quadratic-form statement

For every finite set \(t_1,\dots,t_n\in[0,L]\) and vector \(z\in\mathbb C^n\),

\[
z^*
\left(
K_{A_\infty}
+\sum_{p\le e^L}K_{D_p}
\right)z
\ge
M_L\,
z^*K_{|\cdot|}z.
\]

The right side is

\[
2M_L\,
z^*[\min(t_i,t_j)]_{ij}z.
\]

Thus one may view the seam as an operator lower bound: the completed
Archimedean-plus-prime Gram energy must pay an explicit Brownian covariance
budget.

## 5. Spectral form of the same seam

Distributionally,

\[
\Psi''=A_\infty''-
\sum_{p,k}
(\log p)p^{-k/2}
\left(
\delta_{k\log p}+\delta_{-k\log p}
\right),
\]

with the origin handled in the completed distributional normalization.

A continuous even normalized CND function admits a Lévy-Khintchine
representation, so equivalently one wants

\[
\frac1{2\pi}\widehat{\Psi''}
\]

to be a positive measure (including a possible Gaussian atom at zero under
the standard convention).

Under RH this measure becomes the positive atomic spectral measure on the
real zero ordinates. Unconditionally, proving its positivity is another form
of the same seam, not a weaker task.

## 6. Finite common-mode lifts

A slightly weaker finite-window target is to find \(c_L\ge0\) with

\[
K_{\Psi+c_L|\cdot|}\succeq0
\quad\text{on }[0,L].
\]

If one can do this with one uniform bound

\[
0\le c_L\le C<\infty
\]

for all expanding wavefronts, compactness and closure of PSD matrices give a
global finite CND lift \(\Psi+c|\cdot|\). Round 001's polynomial-growth lemma
then forces RH.

Thus exact zero-debt domination is sufficient but not necessary at finite
cutoff; uniformly bounded Brownian debt is already enough.
