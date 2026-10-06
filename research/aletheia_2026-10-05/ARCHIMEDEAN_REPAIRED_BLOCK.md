# Archimedean repaired block and Fock-axis prime projection

**Date:** 2026-10-05  
**Status:** exact structural reduction / local positive blocks. RH is not proved.

## 1. Positive prime ramp as an axis-sector trace

Identify the multiplicative Hilbert space with the bosonic occupation basis

\[
\mathcal F
=
\bigotimes_p \ell^2(\mathbb N_0)
\cong
\ell^2(\mathbb N_{>0}),
\]

where

\[
|n\rangle
\leftrightarrow
(v_p(n))_p.
\]

Let

\[
H|n\rangle=(\log n)|n\rangle,
\qquad
N|n\rangle=\Omega(n)|n\rangle.
\]

Let \(Q_{\rm axis}\) be the orthogonal projection onto the states whose prime-support has size exactly one:

\[
Q_{\rm axis}\mathcal F
=
\overline{\operatorname{span}}\{|p^k\rangle:p\text{ prime},k\ge1\}.
\]

On that sector,

\[
HN^{-1}|p^k\rangle
=
(\log p)|p^k\rangle.
\]

Therefore for every \(t\ge0\),

\[
\boxed{
P(t)
=
\operatorname{Tr}\left(
Q_{\rm axis}\,
HN^{-1}e^{-H/2}
(t-H)_+\,
Q_{\rm axis}
\right).
}
\]

The operator under the trace is finite-rank for fixed \(t\), positive, and diagonal. Its trace is exactly

\[
\sum_{p^k\le e^t}
(\log p)p^{-k/2}(t-k\log p).
\]

Thus the whole Suzuki prime ramp is already a manifestly positive operator trace in the completed multiplicative/Fock state space.

This avoids the Round-003 old-support obstruction because all prime modes are present from the beginning; the primitive operation is the positive orthogonal projection to the one-prime-support sector, not a grading-preserving logarithm of an old-monoid partition series.

## 2. Archimedean local scattering derivative

Let

\[
L_\infty(z)
=
\pi^{-z/2}\Gamma(z/2).
\]

On the critical line put

\[
\rho_\infty(1/2+is)
=
\frac{L_\infty(1/2+is)}
     {L_\infty(1/2-is)}.
\]

Define

\[
P_\infty(s)
=
\frac{i}{2}
\frac{d}{ds}
\log \rho_\infty(1/2+is).
\]

Direct differentiation gives

\[
\boxed{
P_\infty(s)
=
\frac12
\left[
\log\pi
-
\Re\psi\left(\frac14+\frac{is}{2}\right)
\right].
}
\]

Its zero-frequency value is

\[
\boxed{
M_\infty
=
P_\infty(0)
=
\frac12
\left[
\log\pi-\psi(1/4)
\right]
=
-B,
}
\]

where

\[
B=\frac12[\psi(1/4)-\log\pi]
\]

is Suzuki's Archimedean linear coefficient.

## 3. The Archimedean repaired spectral density is positive

The digamma series gives, with \(a_n=n+1/4\),

\[
\Re\psi(a_n+is/2)-\psi(a_n)
\]

termwise positive after subtraction at \(s=0\). Hence

\[
\boxed{
M_\infty-P_\infty(s)
=
\frac12
\left[
\Re\psi\left(\frac14+\frac{is}{2}\right)
-
\psi\left(\frac14\right)
\right]
\ge0.
}
\]

More explicitly,

\[
M_\infty-P_\infty(s)
=
\sum_{n\ge0}
\frac{s^2}
     {2a_n[s^2+(2a_n)^2]}.
\]

Thus

\[
\nu_\infty^\Gamma(ds)
=
\frac{M_\infty-P_\infty(s)}
     {\pi s^2}\,ds
\]

is a positive Lévy measure.

## 4. Its CND exponent is exactly Suzuki's Gamma/Lerch term

Define

\[
D_\infty^\Gamma(t)
=
\int_{\mathbb R}
(1-\cos ts)\,
\nu_\infty^\Gamma(ds).
\]

Using

\[
\int_{\mathbb R}
\frac{1-\cos(ts)}{s^2+c^2}\,ds
=
\frac{\pi}{c}(1-e^{-c|t|})
\]

termwise gives

\[
D_\infty^\Gamma(t)
=
4\sum_{n\ge0}
\frac{1-e^{-(2n+1/2)|t|}}
     {(4n+1)^2}.
\]

Since

\[
\Phi(e^{-2t},2,1/4)
=
16\sum_{n\ge0}
\frac{e^{-2nt}}
     {(4n+1)^2},
\]

one obtains exactly

\[
\boxed{
D_\infty^\Gamma(t)
=
\frac14
\left[
C-e^{-|t|/2}
\Phi(e^{-2|t|},2,1/4)
\right].
}
\]

Therefore the non-pole Archimedean Gamma contribution has the same structure as every finite place:

\[
\boxed{
\text{positive repaired CND block}
-
\text{zero-frequency Brownian debt}.
}
\]

## 5. Exact completed decomposition on a finite wavefront

Let

\[
E_{\rm pole}(t)
=
4(e^{|t|/2}+e^{-|t|/2}-2)
=
8(\cosh(|t|/2)-1).
\]

Then

\[
\boxed{
A_\infty(t)
=
E_{\rm pole}(t)
+
D_\infty^\Gamma(t)
-
M_\infty|t|.
}
\]

For a horizon \(L\), define

\[
M_L=\sum_{p\le e^L}M_p.
\]

Using

\[
-h_p=D_p-M_p|t|,
\]

one gets exactly, for \(|t|\le L\),

\[
\boxed{
\Psi(t)
=
E_{\rm pole}(t)
+
D_\infty^\Gamma(t)
+
\sum_{p\le e^L}D_p(t)
-
(M_\infty+M_L)|t|.
}
\]

Every \(D_p\) and \(D_\infty^\Gamma\) is CND.

The remaining non-CND structure is now isolated to:

1. one universal Brownian/common-mode debt;
2. the fixed pole term \(E_{\rm pole}\).

## 6. The pole screw kernel is rank two with one negative direction

For \(s,u\ge0\),

\[
K_E(s,u)
=
E_{\rm pole}(s)
+
E_{\rm pole}(u)
-
E_{\rm pole}(s-u).
\]

A direct hyperbolic factorization gives

\[
\boxed{
K_E(s,u)
=
8
\left[
\sinh(s/2)\sinh(u/2)
-
(\cosh(s/2)-1)(\cosh(u/2)-1)
\right].
}
\]

Hence on any finite positive grid, \(K_E\) has rank at most two.

For two distinct positive times its determinant is negative, so the nonzero
signature is exactly one positive and one negative direction.

Thus after the local finite and Gamma factors are repaired, the only
non-Brownian indefinite shape left by completion is a single pole direction.

This is consistent with the role of degree/codegree modes in Weil-style
primitive formulations, but no pairing-preserving quotient eliminating this
direction is claimed here.

## 7. Archimedean Gaussian scale vacuum

Let

\[
g_\infty(x)=2^{3/4}e^{-\pi x^2},
\qquad x>0,
\]

normalized in \(L^2(\mathbb R_+,dx)\), and let

\[
(U_t f)(x)=e^{t/2}f(e^t x)
\]

be unitary dilation.

Then

\[
\boxed{
\langle g_\infty,U_tg_\infty\rangle
=
\operatorname{sech}(t)^{1/2}.
}
\]

Under the logarithmic/Mellin spectral transform, the cyclic density is proportional to

\[
\boxed{
\left|
L_\infty(1/2+is)
\right|^2.
}
\]

This matches the finite-place result

\[
P_r((\log p)s)
=
(1-p^{-1})
\left|
L_p(1/2+is)
\right|^2.
\]

Thus both the finite vacuum \(\mathbf1_{\mathbb Z_p}\) under p-adic dilation and the real Gaussian under Archimedean dilation have their local \(L\)-factor as the outer spectral factor of a canonical cyclic scale process.

The corresponding local scattering ratios are their phase ratios.

## 8. Revised one-prime-plus-infinity problem

The local positive pieces are no longer missing.

A one-prime-plus-infinity construction must couple:

- the p-adic normalized depth/scale process;
- its one-step gradient, which produces \(D_p\);
- the Gaussian scale process at infinity;
- the positive Gamma repaired block \(D_\infty^\Gamma\);
- the pole two-signature sector;
- the common Brownian debt.

The exact target on the one-prime horizon is

\[
K_{E_{\rm pole}}
+
K_{D_\infty^\Gamma}
+
K_{D_p}
-
(M_\infty+M_p)K_{|\cdot|}.
\]

The next theorem must supply the missing cross terms/metric that make this
kernel positive up to a finite explicitly derived Brownian lift.

No local factor remains to be guessed.
