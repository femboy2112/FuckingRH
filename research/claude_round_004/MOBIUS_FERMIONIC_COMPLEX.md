# Möbius = Koszul differential; the Hodge Laplacian factorizes (no-go, with exact positives)

**Date:** 2026-10-06
**Status:** one exact reformulation (DISCLOSED) + a clean no-go (DISCLOSED) for the naive Hodge route.
RH remains open. Reproduce: `scripts/hodge_koszul_check.py`.

## 1. The Euler identity is discrete exactness (exact, and genuinely clean)

On the prime-exponent lattice, a divisor $d\mid n$ is $v_p(d)\le v_p(n)$, and the number-theoretic
Möbius transform factors as a product of **per-mode backward differences**
\[
\mu*=\prod_p\nabla_p,\qquad \nabla_p=I-E_p^{-1},\quad (E_p^{-1}|\dots v_p\dots\rangle=|\dots v_p-1\dots\rangle).
\]
Since $\log n=\sum_p v_p\log p$ is **additive (first order)** in the exponents,
\[
\boxed{\ \Lambda=\mu*\log=\Big(\textstyle\prod_{p\mid n}\nabla_p\Big)\log
=\begin{cases}\log p,&n=p^k\ (\text{one mode}),\\[2pt]0,&\omega(n)\ge2.\end{cases}\ }
\]
The vanishing on composite support is exactly *"a mixed second (or higher) difference of an additive
function is zero."* This is the discrete-harmonicity / cohomological-exactness content of
$\Lambda=\mu*\log$, and it is the cleanest statement of why the prime weight lives only on the
one-mode (single-prime-axis) sector. *(DISCLOSED; verified.)*

## 2. Critical weights turn $\nabla_p$ into the local whitening (ties to C06)

With the half-density weight $\tilde\nabla_p=I-p^{-1/2}E_p^{-1}$,
\[
\tilde\nabla_p^\*\tilde\nabla_p=(1+p^{-1})I-p^{-1/2}(E_p+E_p^{-1}),
\]
the tridiagonal **AR(1) precision matrix** — i.e. the inverse of the $p$-adic depth covariance
$r^{|k-\ell|}$ and the operator form of the inverse local Euler factor (LOCAL_L_FACTOR_WHITENING, C06).
Confirmed numerically (diagonal block $(2.5,-0.577,\dots)$, $r=2^{-1/2}=0.707$). The signs sit inside
$\tilde\nabla_p$; $\tilde\nabla_p^\*\tilde\nabla_p$ is manifestly positive.

## 3. Koszul/Hodge wrapper — and why it is RH-inert (the no-go)

Build the Koszul differential $D=\sum_p\tilde\nabla_p\otimes a_p^\*$ on $\bigwedge^\bullet(\mathbb C^{P})\otimes$(towers).
Then $D^2=0$ and $Q=D+D^\*$ gives Hodge Laplacians $\Delta_d=D^\*D+DD^\*\succeq0$ (verified $\ge0$, $D^2=0$).
The hope (§11): the degree-1 off-diagonal block carries the cross-prime coupling $\tilde\nabla_p\tilde\nabla_q^\*$.

**It cancels.** The off-diagonal $(p,q)$ block of $\Delta_1$ is
\[
\tilde\nabla_p\tilde\nabla_q^\*\ (\text{from }DD^\*)\ -\ \tilde\nabla_q^\*\tilde\nabla_p\ (\text{from }D^\*D)
=[\tilde\nabla_p,\tilde\nabla_q^\*]=0,
\]
because $\tilde\nabla_p,\tilde\nabla_q$ act on **different, commuting** modes. Verified: the cross block
is exactly $0$ (Frobenius norm $0$). By Künneth, the Koszul Laplacian of the product-of-chains lattice
is $\Delta=\sum_p\tilde\nabla_p^\*\tilde\nabla_p$ — **diagonal/factorized**, hence the same RH-inert
factorized object as the GCD kernel (C81) and the degree-0 case.

> **No-go.** The multiplicative Hodge/Koszul complex reproduces the local whitening blocks exactly but
> its Laplacian factorizes over primes; the cross-prime coupling cancels as a commutator of commuting
> differentials. Signed Möbius does sit cleanly inside a positive $Q^2$, but that $Q^2$ carries no
> cross-prime (RH-bearing) information.

## 4. Where this sends us

The nonzero cross terms $V_p^\*V_q$ (C79) are **products** of commuting isometries, not commutators, so
they survive; the Hodge Laplacian only ever sees the commutator, which vanishes. Therefore the
RH-bearing cross coupling cannot come from the commutative multiplicative complex — it requires the
**noncommutative affine braid** $V_mS=S^mV_m$ (succ×fucc), where $[\,\cdot,\cdot\,]\ne0$. That is the
next target (AFFINE_CROSS_TERM_GRAM). The Koszul picture still contributes the exact local whitening
factors and the clean exactness statement of §1.
