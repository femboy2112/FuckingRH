# Cubical shorting theorem: the physical Schur complement is a conditional innovation variance

> **2026-10-07 proof-bearing audit:** Conditional-variance/Schur positivity is automatic, not the missing RH theorem. With only prime edges the parent is UV-bounded and cannot equal Weil; even adding the bare logarithmic difference energy fails operator order near the interval boundary. The exact repaired decomposition must include the positive part of Suzuki's boundary log potential in the raw block. See [proof-bearing frame audit](RH_PROOF_BEARING_FRAME_AUDIT.md).

**Date:** 2026-10-07  
**Status:** exact Hilbert-space linear algebra applied to the prime-support superconnection. No RH assumption. The identification with the Weil quadratic form is an explicit theorem target, not a claimed result.  
**RH remains open.**

The cubical Dirac construction gives a positive Hamiltonian

\[
\mathcal H=\mathcal D^2.
\]

The physical degree-zero sector is coupled to all higher even support faces.

The correct semidefinite Schur elimination has a simple and powerful interpretation:

\[
\boxed{
\text{effective physical energy}
=
\text{squared norm of the raw physical response orthogonal to everything synthesizable by higher support faces}.
}
\]

This turns the proposed RH mechanism into a conditional-variance / innovation statement.

---

# 1. General Gram shorting theorem

Let

\[
B:
\mathcal X_0\oplus\mathcal X_h
\to
\mathcal Y
\]

be a bounded operator, written

\[
\boxed{
B=[B_0\;\;B_h].
}
\]

Its Gram operator is

\[
G=B^*B
=
\begin{pmatrix}
B_0^*B_0&B_0^*B_h\\
B_h^*B_0&B_h^*B_h
\end{pmatrix}.
\]

Let

\[
P_h
\]

be the orthogonal projection in \(\mathcal Y\) onto

\[
\overline{\operatorname{Ran}B_h}.
\]

Then the shorted operator of \(G\) to \(\mathcal X_0\) is

\[
\boxed{
\operatorname{Short}_{\mathcal X_0}(G)
=
B_0^*(I-P_h)B_0.
}
\]

In finite dimensions this is exactly the Moore--Penrose Schur formula

\[
\boxed{
B_0^*B_0
-
B_0^*B_h
(B_h^*B_h)^\dagger
B_h^*B_0.
}
\]

Proof: \(B_h(B_h^*B_h)^\dagger B_h^*\) is the orthogonal projection onto \(\operatorname{Ran}B_h\).

Therefore:

\[
\boxed{
\operatorname{Short}_{\mathcal X_0}(G)\succeq0.
}
\]

---

# 2. Variational form

For

\[
x\in\mathcal X_0,
\]

\[
\boxed{
\langle x,
\operatorname{Short}_{\mathcal X_0}(G)x
\rangle
=
\inf_{y\in\mathcal X_h}
\|B_0x+B_hy\|^2.
}
\]

Equivalently,

\[
\boxed{
=
\|(I-P_h)B_0x\|^2.
}
\]

So hidden-state elimination is not mysterious subtraction.

It is least-squares regression:

\[
\boxed{
\text{raw physical response}
-
\text{best response synthesizable from hidden states}.
}
\]

The residual energy is automatically nonnegative.

---

# 3. Apply to the cubical Dirac Hamiltonian

Let

\[
\mathcal D
=
\nabla+\nabla^*
\]

be the support-cube supercharge.

It exchanges exterior parity.

Write

\[
\mathcal F^{\rm even}
=
\Lambda^0
\oplus
\Lambda^{\ge2,\rm even},
\]

and

\[
\mathcal F^{\rm odd}
=
\Lambda^1
\oplus
\Lambda^{\ge3,\rm odd}.
\]

Let

\[
\boxed{
B
=
P_{\rm odd}
\mathcal D
P_{\rm even}.
}
\]

Then

\[
\boxed{
\mathcal H_{\rm even}
=
P_{\rm even}\mathcal D^2P_{\rm even}
=
B^*B.
}
\]

Split

\[
B=[B_0\;\;B_h]
\]

according to

\[
\Lambda^0
\oplus
\Lambda^{\ge2,\rm even}.
\]

Therefore the effective vacuum/physical Hamiltonian is

\[
\boxed{
H_{\rm phys}
=
B_0^*
\left(
I-P_{\operatorname{Ran}B_h}
\right)
B_0.
}
\]

This is exact.

---

# 4. The raw physical response is the prime-event channel

For a continuum test \(f\), the vacuum response under the first-jet supercharge is

\[
\boxed{
B_0f
=
\sum_{q=p^k\le N}
e_q
\otimes
\sqrt{w_q}\,
E_q
\otimes
(T_q-I)f.
}
\]

Because the one-event exterior states \(e_q\) are orthogonal,

\[
\boxed{
\|B_0f\|^2
=
\sum_q
w_q
\|(T_q-I)f\|^2
}
\]

after normalized support trace.

This is precisely the raw positive prime-power edge energy.

Thus:

\[
\boxed{
\text{Weil prime edge square}
=
\text{raw vacuum response energy}.
}
\]

---

# 5. Hidden cube responses

A degree-two support face

\[
e_q\wedge e_r
\]

is sent by \(\mathcal D\) into odd degree-one and degree-three channels.

Its image contains the same oriented support/continuum operators that appear in the curvature

\[
[A_q,A_r].
\]

Degree four feeds degree three/five, and so on.

Therefore

\[
\operatorname{Ran}B_h
\]

is the space of continuum/support responses synthesizable by **higher arithmetic interaction faces**.

The shorted physical energy is consequently

\[
\boxed{
\|B_0f\|^2
-
\|P_{\operatorname{Ran}B_h}B_0f\|^2.
}
\]

The second term is the automatically generated global counterterm.

---

# 6. Probability/ANOVA interpretation

The flat support cube already has an orthogonal Hoeffding/ANOVA decomposition:

\[
\text{constant}
\oplus
\text{one-body innovations}
\oplus
\text{two-body innovations}
\oplus\cdots.
\]

Bare CRT independence makes these levels orthogonal and dynamically uncoupled.

SUCC chronology turns the flat ANOVA grading into a covariant complex.

The hidden-range projection then asks:

> which portion of the one-body response is predictable from higher-order chronological interactions?

Thus

\[
\boxed{
H_{\rm phys}
=
\text{conditional residual covariance}.
}
\]

If the completed Weil form equals this operator, Weil positivity would be an arithmetic analogue of the elementary fact

\[
\boxed{
\operatorname{Var}(X\mid\text{unexplained directions})\ge0.
}
\]

That is a theorem target, not yet an identity.

---

# 7. Relation to the two-prime exact theorem

With only two support atoms,

\[
\mathcal F^{\rm even}
=
\Lambda^0\oplus\Lambda^2.
\]

The hidden range is generated by the two-face.

The exact shorted energy derived in the superconnection note is

\[
\boxed{
H_{\rm phys}(n)
=
\frac{
|\langle v_n,v_{n+1}\rangle|^2
}{
\|v_{n+1}\|^2
}.
}
\]

This is precisely the squared norm of the component of the raw one-body vector that remains after projecting out the exterior-area/curvature direction.

So the finite formula is the \(2\)-dimensional instance of the general Gram shorting theorem.

---

# 8. Why the earlier carry-square parent saturated to zero

The carry-square parent used

\[
\sum_j C_j^*C_j
\]

after each local interaction had already been squared.

In the resulting Gram geometry, the hidden conductor columns spanned the entire physical column space:

\[
\operatorname{Ran}B_0
\subseteq
\operatorname{Ran}B_h.
\]

Therefore

\[
(I-P_h)B_0=0
\]

and the Schur residual vanished.

The cubical superconnection assembles **oriented first-order legs before squaring**.

Its hidden range is different, and the finite \(2,3\) and \(2,3,5\) controls show

\[
(I-P_h)B_0\ne0.
\]

This explains the difference between the failed and live constructions.

---

# 9. Exact RH-facing theorem target

Let

\[
A_a^{\rm Weil}
\]

be Suzuki's localized Weil operator on the finite interval.

Construct a completed cubical supercharge

\[
\mathcal D_a^{\rm comp}
\]

from:

- exact conductor support wakes;
- chronological SUCC transport;
- log-time translations;
- the exact Archimedean/Gamma state-space;
- the pole/boundary sector.

Write

\[
B_a
=
P_{\rm odd}\mathcal D_a^{\rm comp}P_{\rm even}
=
[B_{0,a}\;\;B_{h,a}].
\]

The decisive theorem would be

\[
\boxed{
A_a^{\rm Weil}
=
B_{0,a}^*
\left(
I-P_{\overline{\operatorname{Ran}B_{h,a}}
\right)
B_{0,a}.
}
\]

Then immediately

\[
\boxed{
A_a^{\rm Weil}\succeq0
}
\]

for every finite \(a\).

By the Weil/Suzuki criterion this would prove RH.

No zero locations would occur in the construction.

---

# 10. What must not happen

The identity above would be circular if:

- \(B_h\) were defined using the desired Weil kernel;
- the projection metric were chosen to force equality;
- zeta zeros selected the hidden states;
- RH-equivalent positivity were assumed to prove range inclusion or convergence.

The hidden response space must come independently from the support cube + Archimedean chronology.

This makes the theorem genuinely falsifiable.

---

# 11. Current interpretation

The cube proposal can now be stated without physics metaphor:

\[
\boxed{
\textbf{RH may be the statement that the localized Weil form is the shorted Gram operator of the completed arithmetic support complex.}
}
\]

The quantum/Hodge language is then simply the natural representation:

- support subsets = graded states;
- oriented event maps = supercharge;
- chronology defect = curvature;
- Dirac square = positive parent Gram;
- hidden-face elimination = conditional variance;
- Weil form = proposed physical residual.

That is the exact object to prove or kill next.
