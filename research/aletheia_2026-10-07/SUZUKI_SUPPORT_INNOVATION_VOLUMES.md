> **Provenance / important distinction (2026-10-07):** The Gram–Schmidt identity `1-p^{-2ω}=||η_{p,ω}||²` and its finite tensor-product factorization are correct **at fixed ω and finite conductor support**, but they do not define a coherent unitary Markov process or a gcd-projective conductor probability measure across LCM levels. That incorrect extrapolation is refuted by [the imported critical audit](../audits/2026-10-07/CUBE_ATOM_CRITICAL_AUDIT_IMPORTED.md). For a causal stochastic realization use fresh independent exponential birth clocks or a specified open-system generator, and separately prove the Hardy/Archimedean coupling. See [claim provenance](../audits/2026-10-07/RH_CLAIM_PROVENANCE_LEDGER.md).

# Suzuki conductor weights as positive support-cell innovation volumes

**Date:** 2026-10-07  
**Branch:** \`aletheia/succ-loop-support-curvature-2026-10-07\`  
**Status:** exact finite-dimensional Hilbert-space factorization of every Suzuki conductor coefficient. No RH assumption.  
**RH remains open.**

This note supplies a canonical positive parent geometry for the full nonlinear conductor weights

\[
b_\omega(n)
=
n^{\omega-\frac12}
\prod_{p\mid n}(1-p^{-2\omega}).
\]

The product over distinct prime supports is exactly a product of local Gram--Schmidt innovation variances.

The higher Suzuki jets are therefore not arbitrary Taylor coefficients: they are the successive dimensions of a positive support-cell innovation filtration.

---

# 1. One prime direction

Fix a prime \(p\) and \(\omega>0\).

Set

\[
\boxed{
q_p(\omega)=p^{-\omega}\in(0,1).
}
\]

Take a two-dimensional real Hilbert space and choose unit vectors

\[
u_p,
\qquad
v_p(\omega)
\]

with overlap

\[
\boxed{
\langle u_p,v_p(\omega)\rangle=q_p(\omega).
}
\]

For example,

\[
u_p=(1,0),
\]

\[
v_p(\omega)
=
\left(
q_p,
\sqrt{1-q_p^2}
\right).
\]

Project \(v_p\) orthogonally away from the old/common direction \(u_p\):

\[
\boxed{
\eta_{p,\omega}
=
v_p-q_pu_p.
}
\]

Then

\[
\boxed{
\|\eta_{p,\omega}\|^2
=
1-q_p^2
=
1-p^{-2\omega}.
}
\]

Thus each local Suzuki factor is exactly an innovation variance.

---

# 2. Gram determinant interpretation

The two-state Gram matrix is

\[
\boxed{
G_{p,\omega}
=
\begin{pmatrix}
1&p^{-\omega}\\
p^{-\omega}&1
\end{pmatrix}.
}
\]

Therefore

\[
\boxed{
\det G_{p,\omega}
=
1-p^{-2\omega}.
}
\]

Equivalently,

\[
\det G_{p,\omega}
=
\|u_p\wedge v_p\|^2.
\]

So the local factor is the squared oriented area created when the new prime-support state ceases to coincide with the old state.

At

\[
\omega=0,
\]

the two states coalesce,

\[
q_p(0)=1,
\]

and the local support cell has zero area.

For \(\omega>0\), the prime direction opens.

---

# 3. A conductor with several distinct prime supports

Let

\[
n=\prod_{p\in P}p^{k_p},
\]

where

\[
P=\operatorname{supp}(n)
\]

and

\[
r=|P|.
\]

Define the top support innovation vector

\[
\boxed{
\eta_{n,\omega}
=
\bigotimes_{p\in P}
\eta_{p,\omega}.
}
\]

Then by tensor-product multiplicativity,

\[
\boxed{
\|\eta_{n,\omega}\|^2
=
\prod_{p\mid n}
(1-p^{-2\omega}).
}
\]

Therefore Suzuki's causal conductor coefficient satisfies

\[
\boxed{
b_\omega(n)
=
n^{\omega-\frac12}
\|\eta_{n,\omega}\|^2.
}
\]

If one absorbs the depth carrier into the vector,

\[
\boxed{
\Psi_{n,\omega}
=
n^{\frac{\omega}{2}-\frac14}
\eta_{n,\omega},
}
\]

then

\[
\boxed{
b_\omega(n)
=
\|\Psi_{n,\omega}\|^2.
}
\]

Every individual conductor event weight is therefore manifestly positive.

---

# 4. Support and depth separate exactly

The factorization is

\[
\boxed{
b_\omega(n)
=
\underbrace{
n^{\omega-\frac12}
}_{\text{depth/time carrier}}
\;
\underbrace{
\prod_{p\mid n}(1-p^{-2\omega})
}_{\text{support-cell innovation volume}}.
}
\]

The second factor depends only on

\[
\operatorname{rad}(n).
\]

The first factor knows the full prime-power depths.

Thus the nonlinear conductor family already separates:

\[
\boxed{
\text{which prime directions interact}
}
\]

from

\[
\boxed{
\text{how deep along those directions the event occurs}.
}
\]

This is exactly the distinction suggested by the shadow-support picture.

---

# 5. Critical half-density removes depth from the amplitude

At

\[
\omega=\frac12,
\]

the carrier becomes

\[
n^{\omega-\frac12}=1.
\]

Therefore

\[
\boxed{
b_{1/2}(n)
=
\prod_{p\mid n}
\left(1-\frac1p\right)
=
\frac{\varphi(n)}n.
}
\]

So at criticality the event amplitude depends **only on the support skeleton**:

\[
\boxed{
\operatorname{rad}(n).
}
\]

If two integers have the same radical,

\[
\operatorname{rad}(m)=\operatorname{rad}(n),
\]

then

\[
\boxed{
b_{1/2}(m)=b_{1/2}(n).
}
\]

Their difference in the critical Suzuki causal machine is purely temporal:

\[
\log m
\quad\text{versus}\quad
\log n.
\]

This gives an exact harmonic interpretation.

For one prime ray,

\[
p,p^2,p^3,\ldots
\]

all events have the same support amplitude

\[
1-\frac1p,
\]

but occur at equally spaced log times

\[
\log p,\quad2\log p,\quad3\log p,\ldots.
\]

Hence:

\[
\boxed{
\text{critical amplitude}
=
\text{prime-support geometry},
}
\]

\[
\boxed{
\text{prime-power depth}
=
\text{harmonic time/frequency index}.
}
\]

---

# 6. Small-omega opening law

As

\[
\omega\downarrow0,
\]

\[
p^{-\omega}
=
1-\omega\log p+O(\omega^2).
\]

Therefore

\[
\boxed{
\|\eta_{p,\omega}\|^2
=
1-p^{-2\omega}
=
2\omega\log p
+
O(\omega^2).
}
\]

At the amplitude level,

\[
\boxed{
\|\eta_{p,\omega}\|
=
\sqrt{2\omega\log p}
\left(
1+O(\omega)
\right).
}
\]

For a conductor with \(r\) distinct prime supports,

\[
\boxed{
\|\eta_{n,\omega}\|^2
=
(2\omega)^r
\prod_{p\mid n}\log p
+
O(\omega^{r+1}).
}
\]

Therefore

\[
\boxed{
b_\omega(n)
=
\frac{
(2\omega)^r
}{
\sqrt n
}
\prod_{p\mid n}\log p
+
O(\omega^{r+1}),
}
\]

recovering the omega-zero conductor-jet theorem from a positive Hilbert-space geometry.

The first nonzero jet order is the number of independent local innovations required to create the support cell.

---

# 7. Boolean/ANOVA interpretation

For

\[
P=\{p_1,\ldots,p_r\},
\]

the tensor product

\[
\bigotimes_{p\in P}
\operatorname{span}\{u_p,v_p\}
\]

has a natural Boolean subset decomposition.

At each prime one may retain:

- the common/old direction \(u_p\);
- the orthogonal innovation direction \(\eta_p\).

Thus the tensor product splits into subset-labelled orthogonal cells

\[
\boxed{
\mathcal K_P
=
\bigoplus_{A\subseteq P}
\mathcal K_A,
}
\]

where \(\mathcal K_A\) uses the innovation coordinate precisely on primes in \(A\).

The top cell is

\[
\boxed{
\mathcal K_P^{\rm top}
=
\bigotimes_{p\in P}\operatorname{span}\{\eta_p\}.
}
\]

Its energy is exactly

\[
\boxed{
\prod_{p\in P}(1-p^{-2\omega}).
}
\]

This is the Hilbert-space analogue of the exact-conductor fusion/ANOVA hierarchy found independently in the loop-undertone branch.

Bare CRT independence is therefore not an obstruction to this construction.

It is the reason the interaction hierarchy is orthogonal before chronological dressing.

---

# 8. Inclusion-exclusion is the coordinate expansion of a positive projection

The support factor has the familiar expansion

\[
\prod_{p\mid n}
(1-p^{-2\omega})
=
\sum_{A\subseteq P}
(-1)^{|A|}
\prod_{p\in A}p^{-2\omega}.
\]

Seen only as scalars, this looks like alternating cancellation.

But in the innovation Hilbert space it is

\[
\boxed{
\left\|
\bigotimes_{p\in P}
(I-P_{u_p})v_p
\right\|^2.
}
\]

So the alternating Möbius/augmentation signs are simply the coordinate expansion of an orthogonal projection.

This is important for the RH program:

\[
\boxed{
\text{signed inclusion-exclusion}
=
\text{shadow of a positive parent square}.
}
\]

The same pattern has appeared repeatedly in the repository:

- Ramanujan exact-conductor projectors;
- carry carré-du-champ;
- augmentation \(1-X\);
- prime-ray Dirichlet squares.

The support-cell factorization unifies these at the level of the full nonlinear conductor weights.

---

# 9. Exact-conductor harmonic space matches the support tensor product

By CRT,

\[
\boxed{
W_n
\cong
\bigotimes_{p^k\parallel n}
W_{p^k}.
}
\]

And

\[
\dim W_n
=
\prod_{p^k\parallel n}\varphi(p^k)
=
\varphi(n).
\]

Thus there are two compatible tensor structures:

### harmonic exact-conductor tensor

\[
W_n
\cong
\bigotimes W_{p^k};
\]

### support-innovation tensor

\[
\eta_{n,\omega}
=
\bigotimes_{p\mid n}\eta_{p,\omega}.
\]

The first remembers full local depth.

The second contributes one orthogonal innovation factor for each **distinct** prime direction.

This is exactly why:

\[
\boxed{
\text{dimension/depth}
\neq
\text{interaction order}.
}
\]

Interaction order is support rank.

Prime-power depth is harmonic repetition along an already-open direction.

---

# 10. Relation to the user's affine loop

The supplied affine loop has primitive central holonomy

\[
24=2^3\cdot3.
\]

Its central-holonomy support set has two prime directions:

\[
\{2,3\}.
\]

Therefore its support-innovation vector is

\[
\boxed{
\eta_{24,\omega}
=
\eta_{2,\omega}\otimes\eta_{3,\omega}.
}
\]

Its squared support volume is

\[
\boxed{
(1-2^{-2\omega})(1-3^{-2\omega}).
}
\]

Its full Suzuki conductor weight is

\[
\boxed{
b_\omega(24)
=
24^{\omega-\frac12}
(1-2^{-2\omega})(1-3^{-2\omega}).
}
\]

As \(\omega\to0\),

\[
b_\omega(24)
=
\frac{
4\omega^2\log2\log3
}{
\sqrt{24}
}
+
O(\omega^3).
\]

So its first nonzero appearance is exactly the two-innovation support cell.

This is independent of the loop's **integer-prefix support conductor**, which for the supplied word is \(2\).

The two invariants answer different questions:

\[
\boxed{
M_\gamma=2
=
\text{where the word is executable over }\mathbb Z,
}
\]

\[
\boxed{
\kappa(\gamma)=24
=
\text{central history retained by the primitive affine lift}.
}
\]

The Suzuki conductor cell associated with the central holonomy is \(W_{24}\).

The arithmetic support cylinder of the particular word is the odd residue class modulo \(2\).

Neither should be substituted for the other.

---

# 11. A canonical positive parent operator

For a finite support set \(P\), define the local innovation projections

\[
Q_{p,\omega}
=
I-|u_p\rangle\langle u_p|.
\]

Let

\[
v_{P,\omega}
=
\bigotimes_{p\in P}v_p(\omega).
\]

Then the top-support projector is

\[
\boxed{
Q_{P,\omega}
=
\bigotimes_{p\in P}Q_{p,\omega},
}
\]

and

\[
\boxed{
\langle
v_{P,\omega},
Q_{P,\omega}v_{P,\omega}
\rangle
=
\prod_{p\in P}(1-p^{-2\omega}).
}
\]

Therefore

\[
\boxed{
b_\omega(n)
=
n^{\omega-\frac12}
\langle
v_{P,\omega},
Q_{P,\omega}v_{P,\omega}
\rangle.
}
\]

Every scalar conductor weight is a matrix coefficient of a positive projection.

This is a genuine positive parent geometry.

It does **not** yet prove finite Suzuki passivity, because the remaining universal Archimedean Hankel block and chronological coupling between different conductor events are not represented by this scalar square alone.

But it gives a non-arbitrary place from which to build them.

---

# 12. The next curvature question

Bare support innovations are orthogonal and hence flat in the CRT/product geometry.

Let chronological SUCC/carry transport introduce a connection

\[
U_{p,d}
\]

between support cells.

Then the smallest nontrivial curvature lives on a two-prime innovation square:

\[
\boxed{
F_{p,q}(d)
=
U_{q,pd}U_{p,d}
-
U_{p,qd}U_{q,d}.
}
\]

The support-cell Hilbert geometry supplies the canonical positive norm

\[
\boxed{
\|F_{p,q}(d)\|^2.
}
\]

Because the bare tensor product has zero curvature, any nonzero \(F\) is automatically a **dressed chronological residual**, exactly as demanded by the hostile CRT-flat control.

The two-prime top-support weights already have the correct small-\(\omega\) scale

\[
\boxed{
4\omega^2\log p\log q.
}
\]

Thus a history-dressed curvature square can be compared directly with the second Suzuki jet without arbitrary normalization.

That is the next finite experiment.

---

# 13. What this explains

The factor

\[
\prod_{p\mid n}(1-p^{-2\omega})
\]

now has four simultaneous exact readings:

1. Euler/inclusion-exclusion factor;
2. support-cell Gram determinant;
3. squared norm of the top orthogonal innovation;
4. energy of the highest-order Boolean/ANOVA conductor interaction.

At criticality,

\[
\omega=\frac12,
\]

it becomes

\[
\frac{\varphi(n)}n,
\]

the primitive-conductor fraction.

At the true RH endpoint,

\[
\omega=0,
\]

all nontrivial support cells collapse, and their first opening rates produce:

\[
\Lambda(n)/\sqrt n
\]

for the one-prime cells and the higher support-jet hierarchy for mixed conductors.

This is the current cleanest mathematical meaning of the harmonic undertones beneath the finite Suzuki system.
