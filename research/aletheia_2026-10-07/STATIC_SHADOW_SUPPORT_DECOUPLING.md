# Static shadow-support decoupling in Suzuki's finite Hankel kernel

**Date:** 2026-10-07  
**Status:** exact support theorem. No RH assumption.  
**RH remains open.**

The LCM support clock contains exact-conductor sectors before their ordinary integer values are causally reached.

This is genuine pre-support.

But Suzuki's finite Hankel kernel imposes a strict causal support rule:

\[
\boxed{
\text{pre-supported future conductors are dynamically dormant.}
}
\]

Therefore they cannot be used as hidden states to modify the current finite operator unless an exactly equivalent chronological parent realization is separately derived.

This prevents an acausal misuse of the shadow-support picture.

---

# 1. Full LCM support clock at a finite horizon

Fix

\[
a>1
\]

and put

\[
M=\lfloor a^2\rfloor.
\]

The minimal universal support clock is

\[
\mathcal H_M
=
L^2(\mathbb Z/L_M\mathbb Z),
\]

with exact-conductor decomposition

\[
\boxed{
\mathcal H_M
=
\bigoplus_{d\mid L_M}W_d.
}
\]

This includes many conductors

\[
d>M.
\]

Call

\[
\boxed{
\mathcal S_M
=
\bigoplus_{\substack{d\mid L_M\\d>a^2}}W_d
}
\]

the future shadow-supported sector.

---

# 2. Suzuki kernel support

The finite multiplicative Hankel kernel is

\[
h_\omega(xy)
=
\frac1{xy}
\sum_n
c_\omega(n)
g_\omega\!\left(\frac n{xy}\right).
\]

The Archimedean profile satisfies

\[
\boxed{
g_\omega(t)=0
\qquad
(t>1).
}
\]

For the finite operator,

\[
0<x,y<a.
\]

Hence

\[
\boxed{
xy<a^2.
}
\]

If

\[
d>a^2,
\]

then

\[
\frac d{xy}>1.
\]

Therefore

\[
\boxed{
g_\omega\!\left(\frac d{xy}\right)=0
}
\]

for every kernel point in the finite square.

So every future shadow conductor makes exactly zero contribution.

---

# 3. Functional-calculus statement

On the full LCM clock let

\[
\mathcal C_M
=
\sum_{d\mid L_M}
dP_d
\]

be the conductor operator.

The critical trace formula, and its general-\(\omega\) weighted analogue, contain

\[
g_\omega\!\left(
\frac{\mathcal C_M}{xy}
\right).
\]

On \(W_d\),

\[
g_\omega\!\left(
\frac{\mathcal C_M}{xy}
\right)
=
g_\omega\!\left(
\frac d{xy}
\right)I.
\]

Therefore

\[
\boxed{
P_{\mathcal S_M}
g_\omega\!\left(
\frac{\mathcal C_M}{xy}
\right)
=
0
}
\]

for all

\[
0<x,y<a.
\]

This is exact static shadow decoupling.

---

# 4. Active versus dormant support

The full support clock decomposes more precisely as

\[
\boxed{
\mathcal H_M
=
\mathcal A_a
\oplus
\mathcal S_a,
}
\]

where

\[
\mathcal A_a
=
\bigoplus_{\substack{d\mid L_M\\d<a^2}}W_d
\]

is the causally active conductor space and

\[
\mathcal S_a
=
\bigoplus_{\substack{d\mid L_M\\d\ge a^2}}W_d
\]

is dormant at this horizon.

Thus:

\[
\boxed{
\text{support existence}
\neq
\text{dynamical activation}.
}
\]

The LCM substrate knows a conductor can be represented.

The Suzuki wavefront decides whether it is presently coupled.

---

# 5. Consequence for shadow-sector Schur mechanisms

The previous Schur-scaling theorem remains valid linear algebra.

But at a **fixed Suzuki horizon**, one may not arbitrarily integrate out future conductors

\[
d>a^2
\]

and let them change the physical operator.

The exact static coupling to those sectors is zero.

A shadow-elimination proof is legitimate only in one of two situations.

### A. Active higher-order cells

Use conductors

\[
d<a^2
\]

that are already causally active but whose Suzuki weights begin at higher orders in \(\omega\).

These are legitimate finite-horizon hidden variables.

### B. An exactly equivalent chronological parent

Construct a history-space realization in which dormant support states enter internally but prove that eliminating them reproduces **exactly** the same finite Suzuki transfer.

No such parent has yet been derived.

Without that equivalence, allowing future shadow support to modify the current operator would change the problem.

---

# 6. Corrected hidden sector for the omega-zero first jet

At the true endpoint

\[
\omega=0,
\]

all nontrivial conductor weights vanish.

The first derivative directly sees only active prime powers:

\[
b_0'(n)
=
2\Lambda(n)n^{-1/2}.
\]

However conductors

\[
d<a^2
\]

with two or more distinct prime factors are already inside the causal wavefront.

Their direct energies begin at

\[
O(\omega^2),O(\omega^3),\ldots.
\]

These **active mixed conductors** are the legitimate candidates for singular Schur renormalization of the first jet.

So the fixed-horizon decomposition relevant to that mechanism is:

\[
\boxed{
\mathcal P_a
=
\bigoplus_{\substack{p^k<a^2}}W_{p^k}
}
\]

for the directly visible first-jet prime-power sector,

and

\[
\boxed{
\mathcal H_a^{\rm mixed}
=
\bigoplus_{\substack{d<a^2\\\omega_0(d)\ge2}}W_d
}
\]

for the active higher-order hidden sector.

Future conductors

\[
d\ge a^2
\]

are excluded from the fixed-horizon Schur correction.

---

# 7. Relation to pre-actualized shadow support

The support-face theorem is still meaningful.

At a prime-power support birth \(N=p^k\), the LCM clock creates an entire face

\[
W_{Ne},
\qquad e\mid R.
\]

Most of those sectors are future-shadow at that moment.

As the SUCC/Suzuki wavefront advances, they cross one by one into the active region when

\[
a^2>d.
\]

So the substrate has two stages:

\[
\boxed{
\text{harmonic support birth}
\quad\to\quad
\text{causal activation}.
}
\]

Pre-support is a statement about **available representation capacity**.

Activation is a statement about **actual coupling to the finite Hankel dynamics**.

The distinction should remain explicit in all future work.

---

# 8. User-loop example

The supplied loop has central conductor

\[
24.
\]

Its harmonic sector

\[
W_{24}
\]

is born in the LCM support face at

\[
N=8.
\]

But it does not enter a Suzuki finite kernel until the multiplicative horizon satisfies

\[
\boxed{
a^2>24.
}
\]

Thus:

\[
\boxed{
8
=
\text{support birth},
}
\]

while

\[
\boxed{
\sqrt{24}
=
\text{Suzuki activation scale in }a.
}
\]

The sector exists before it is dynamically active.

That is the exact, non-mystical meaning of pre-actualization here.

---

# 9. Proof-program consequence

The current proof-bearing route should therefore use:

1. the full LCM support filtration to define canonical states and chronology;
2. only causally active mixed conductors in a fixed-horizon effective operator;
3. the dormant sectors only inside an **explicitly proved equivalent history realization**;
4. exact recovery of the finite Suzuki kernel as an acceptance criterion.

Any candidate that violates item 4 is not a proof of the original finite conductor passivity theorem.

This is now a hard boundary condition for the shadow-support program.
