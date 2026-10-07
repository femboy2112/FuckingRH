# Causal shift semigroup, mixed boundary commutators, and forbidden ratio atoms

**Date:** 2026-10-07  
**Branch:** \`research/rh-log-bathtub-prime-shift-2026-10-07\`  
**Status:** exact finite-interval translation-algebra theorem. **RH remains OPEN.**

The previous cubical language sometimes conflated the noncommuting **residue-dressed SUCC legs** with ordinary continuum translations. The latter have a much simpler structure: forward shifts commute *even after interval compression*. Any loop noncommutativity in the bare continuum shift algebra necessarily involves at least one reverse shift, and then the defect is supported only at interval boundaries.

This is a hard selection rule for any proposed arithmetic curvature completion.

## 1. Compressed continuum translations

Let

\[
I=(-a,a),\qquad W=2a,
\]

and use the convention

\[
(\tau_hf)(x)=f(x-h).
\]

Let \(P_I\) denote restriction/zero-extension projection and set

\[
\boxed{
T_h=P_I\tau_hP_I
}
\]

on \(L^2(I)\), for \(h>0\).

Then

\[
(T_hf)(x)=1_I(x)f(x-h)
\]

with \(f\) understood as zero outside \(I\).

## 2. Exact forward semigroup: no fake curvature

For \(h,k>0\),

\[
(T_hT_kf)(x)
=
1_I(x)1_I(x-h)f(x-h-k).
\]

If both the final point \(x\) and initial point \(x-h-k\) lie in the interval, the intermediate point \(x-h\) also lies in the interval, by convexity of \(I\).

Therefore

\[
\boxed{T_hT_k=T_{h+k}=T_kT_h.}
\]

The same holds for their adjoints:

\[
\boxed{T_h^*T_k^*=T_{h+k}^*.}
\]

This is an exact semigroup law on every finite interval, not merely a quotient/limit statement.

Consequently:

\[
\boxed{
\text{nontrivial holonomy cannot arise from order-switching bare forward prime translations}.
}
\]

Any noncommutativity must involve:

- mixed forward/backward truncations;
- state-dependent/residue-weighted legs;
- or genuine Archimedean/history coupling.

## 3. Mixed forward/backward commutator

A direct calculation gives

\[
\boxed{
[T_h^*,T_k]f(x)
=
1_I(x)1_I(x+h-k)
\bigl[
1_I(x+h)-1_I(x-k)
\bigr]
f(x+h-k).
}
\]

This is a partial shift by the **difference** of the displacements, multiplied by a signed boundary indicator.

The multiplier is zero throughout the interior where both intermediate points remain in \(I\). It can be nonzero only when either \(x+h\) exits through the right boundary or \(x-k\) exits through the left boundary.

Thus the commutator is an **exact boundary-supported carry/holonomy defect**.

When \(h=k\),

\[
\boxed{
[T_h^*,T_h]
=
M_{1_{I\cap(I-h)}-1_{I\cap(I+h)}}.
}
\]

For \(0<h<a\) the two surviving support pieces are the left and right boundary strips of width \(h\), with opposite signs.

This is the simplest rigorous version of "a loop remembers the boundary crossing even though the net translation is zero."

## 4. Arithmetic selection rule

For prime powers

\[
q=p^j,\qquad r=\ell^k,
\]

take

\[
h=\log q,\qquad k_{\rm shift}=\log r.
\]

The mixed commutator translates by

\[
\boxed{
k_{\rm shift}-h
=
\log(r/q).
}
\]

When \(r/q\) is a nontrivial rational ratio, this is a **forbidden extra scalar delta displacement** in the exact Weil formula, which has arithmetic atoms only at

\[
\pm\log(p^j).
\]

Therefore if a completed cubical/Dirac parent uses mixed shift commutators as internal curvature, its physical scalar observation map must **not** push the ratio-frequency defect forward as a new Weil atomic line.

This does not mean the commutator must vanish internally. It means its observation/renormalization must be compatible with the prime-power support of the true explicit formula.

## 5. One operator norm caution

For every \(h<W\),

\[
\|T_h\|=1.
\]

At \(h=W\), \(T_h=0\). This is the same instant norm-birth phenomenon established in CONDUCTOR_ENTRY_JET_TOPOLOGY.md.

The commutator defects act on shrinking boundary strips as thresholds move. They need not be small in \(L^2\) operator norm, even when their quadratic form contributions vanish on smooth Dirichlet families.

## 6. Scope and relationship to the cubical construction

The identity \(T_hT_k=T_kT_h\) concerns **bare scalar continuum translations** only. It does not say that the full oriented support legs

\[
E_q=S M_{\beta_q}
\]

commute: their nonconstant residue multipliers can still generate conductor-graded commutators.

Likewise, the product \((T_q-I)(T_r-I)\) generates translations at

\[
0,\ \log q,\ \log r,\ \log(qr),
\]

as already audited in PRIME_SUPPORT_SUPERCONNECTION.md. These are *product* interactions, not the forbidden ratio terms of \(T_q^*T_r\).

The important discipline is to keep these two mechanisms separate.

## Claim ledger

**DISCLOSED:** exact compressed forward semigroup, mixed boundary-commutator formula, boundary localization, prime-log ratio selection rule.

**UNVERIFIED:** any canonical physical observation map that removes forbidden ratio atoms while keeping the exact signed Gamma/pole/Weil completion.

**RH:** OPEN.
