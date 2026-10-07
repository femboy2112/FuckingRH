# Weyl assembly no-go controls and the correct scaling coordinate

**Date:** 2026-10-06  
**Status:** exact no-gos for naive global Weyl assembly. **RH remains open.**

Local SUCC/FUCC systems have canonical Weyl structure. Several obvious methods of assembling them globally are nevertheless RH-inert or degenerate.

These controls constrain the proof architecture.

---

## 1. Bare LCM clock Weyl limit is trivial

At horizon \(N\), let

\[
L_N=\operatorname{lcm}(1,\ldots,N)
\]

and let the untwisted cyclic clock have boundary Carathéodory function

\[
\boxed{
F_N(z)
=
\frac{1+z^{L_N}}
{1-z^{L_N}}.
}
\]

For every fixed

\[
|z|<1,
\]

\[
z^{L_N}\to0.
\]

Therefore

\[
\boxed{
F_N(z)\to1.
}
\]

The inductive profinite clock has a trivial interior-disk Weyl limit.

So the arithmetic event pattern encoded in the growth of \(L_N\) is lost if one takes the ordinary Weyl limit after collapsing the clock to its single cyclic boundary function.

---

## 2. Boundary-layer scaling is nontrivial but universal

Take

\[
z_N=e^{-u/L_N},
\qquad
\Re u>0.
\]

Then

\[
z_N^{L_N}\to e^{-u}.
\]

Hence

\[
\boxed{
F_N(z_N)
\to
\frac{1+e^{-u}}{1-e^{-u}}
=
\coth\frac u2.
}
\]

This scaling limit is nontrivial, but it depends only on the fact that the clock length tends to infinity.

It does not remember where the prime-power refinements occurred.

Thus edge scaling of the **bare** cyclic clock is still RH-inert.

---

## 3. The proof-bearing spectral coordinate must retain event time

The arithmetic source measure is supported at

\[
\boxed{
\tau_{p,k}=k\log p.
}
\]

The Euler/log-derivative transform uses

\[
e^{-s\tau_{p,k}}
=
p^{-ks}.
\]

Therefore the spectral parameter must couple to the chronological event coordinate

\[
\tau=\log q,
\]

not merely to the final cyclic angle \(1/L_N\).

This explains why the causal-history transform retains arithmetic while the bare profinite clock limit forgets it.

---

## 4. Naive product of local Schur functions collapses

The local scalar prime-depth Schur function is

\[
S_p(z)=r_pz,
\qquad
r_p=p^{-1/2}.
\]

A naive serial scalar multiplication over primes gives

\[
\prod_{p\le P}S_p(z)
=
z^{\pi(P)}
\prod_{p\le P}p^{-1/2}.
\]

For every fixed \(|z|<1\),

\[
\boxed{
\prod_{p\le P}S_p(z)\to0.
}
\]

Even on \(|z|=1\),

\[
\prod_{p\le P}p^{-1/2}
=
e^{-\theta(P)/2}
\to0.
\]

So simple multiplication of local Schur channels destroys the arithmetic signal rather than assembling zeta.

---

## 5. Direct positive sum of local Weyl measures diverges

The positive prime repairs have total scale

\[
M_p
=
\frac{\log p}{\sqrt p-1}.
\]

The sum

\[
\sum_pM_p
\]

diverges.

The corresponding direct sum of local Weyl measures therefore does not satisfy the global Herglotz integrability required for an ordinary positive measure representation.

This reproduces the Round002/004 global-wall result in Weyl language.

So:

\[
\boxed{
\text{global arithmetic Weyl response}
\ne
\text{direct positive sum of prime Weyl responses}.
}
\]

---

## 6. Bare Clark/cyclotomic determinant recovers Euler only in the safe region

The finite causal determinant

\[
D_N(s)
=
\prod_{p^k\le N}
\det(I-p^{-s}U_{p,k}^{\rm new})
\]

recovers

\[
\zeta(s)
\]

as \(N\to\infty\) only in the ordinary Euler-product region

\[
\Re s>1.
\]

Therefore the cyclotomic determinant construction by itself does not provide the completion or critical-line positivity.

It is an exact finite skeleton, not yet the global Weyl operator.

---

## 7. Gamma cannot be appended as an independent inner channel

The bare Gamma scattering factor has unit boundary modulus but fails the Blaschke condition and is not a Schur/inner function in the upper half-plane.

Therefore a global construction of the form

\[
(\text{positive prime Schur network})
\times
(\text{Gamma inner channel})
\]

is invalid.

Gamma and the arithmetic trivial-zero sector must first undergo their exact completion/cancellation.

---

## 8. Correct architectural conclusion

The arithmetic information that survives to the completed Weyl object must live in the **chronological interconnection history**:

\[
\boxed{
\{(k\log p,\ \log p,\ p^{-k/2},\ \text{carry/conductor state})\}.
}
\]

The global boundary response must be formed from this event-resolved cocycle before taking \(N\to\infty\).

The LCM/profinite clock supplies:

- causal support;
- exact conductor sectors;
- carry boundary maps;

but its final static Weyl function is too coarse.

---

## 9. Correct limit order

The promising order of operations is:

\[
\boxed{
\begin{array}{c}
\text{finite chronological prime/Gamma history}\\
\downarrow\\
\text{boundary transfer / Schur-Weyl cocycle}\\
\downarrow\\
\text{completed cancellation at finite/controlled level}\\
\downarrow\\
N\to\infty\\
\downarrow\\
m_\Xi
\end{array}
}
\]

not

\[
\boxed{
\text{profinite clock limit}
\to
\text{attach arithmetic afterward}.
}
\]

The latter loses the event geometry.

---

## 10. House slogan

\[
\boxed{
\text{The profinite clock remembers where you can be, not how you got there.}
}
\]

\[
\boxed{
\text{RH-sensitive information must survive in the event-time transfer history.}
}
\]

\[
\boxed{
\text{Take the causal cocycle limit, not the bare clock limit.}
}
\]
