# Source-wired prime rays: SUCC boots the multiplicative bus

**Date:** 2026-10-06  
**Status:** exact operator identities + a sharpened global passivity/limit target. RH remains open.

This note formalizes the observation:

> Wire every primitive prime channel directly to the multiplicative source.  
> The first SUCC pulse moves the additive vacuum \(0\) to the multiplicative identity \(1\), after which the scaling \(t\)-action and all prime rays are live.

The resulting source response is exactly \(-\zeta'/\zeta\) in its ordinary half-plane of convergence.

The completed source response is \(\xi'/\xi\). By the classical Lagarias/Hinkkanen positivity criterion,
\[
\mathrm{RH}
\iff
\Re \frac{\xi'(s)}{\xi(s)}>0
\quad (\Re s>1/2).
\]
Thus the proof-bearing target becomes:

> construct the completed source port as a genuinely passive / positive-real limit of finite arithmetic networks, without assuming RH.

The positivity criterion itself is classical; the source-wired carry realization below is the new research interface.

---

## 1. Additive vacuum and multiplicative source

Let

\[
\mathcal H_{\rm add}
=
\ell^2(\mathbb N_0)
\]

with basis \(|n\rangle\), and let the unilateral successor shift be

\[
S|n\rangle=|n+1\rangle.
\]

Take the additive vacuum

\[
|0\rangle.
\]

The first successor pulse produces

\[
\boxed{
\Omega:=S|0\rangle=|1\rangle.
}
\]

The state \(|1\rangle\) is simultaneously the multiplicative identity, so this is the canonical source state for the multiplicative system.

On the positive-integer sector define multiplicative isometries

\[
V_m|n\rangle=|mn\rangle.
\]

For each prime \(p\),

\[
\boxed{
V_p^k\Omega=|p^k\rangle.
}
\]

Thus every primitive prime-power ray emanates from the same source \(\Omega\).

---

## 2. SUCC/FUCC intersections detect prime powers

The additive worldline is

\[
S^n|0\rangle=|n\rangle.
\]

The multiplicative \(p\)-ray is

\[
V_p^k\Omega=|p^k\rangle.
\]

Therefore

\[
\boxed{
\langle S^n0\,|\,V_p^k\Omega\rangle
=
\delta_{n,p^k}.
}
\]

Equivalently,

\[
\boxed{
n\text{ lies on a primitive FUCC ray}
\iff
n=p^k.
}
\]

This gives the exact incidence formula

\[
\boxed{
\Lambda(n)
=
\sum_{p}\sum_{k\ge1}
(\log p)\,
\langle n|V_p^k\Omega\rangle.
}
\]

Because an integer \(n>1\) is a prime power for at most one prime \(p\), the sum has at most one nonzero term.

At critical half-density,

\[
\boxed{
\frac{\Lambda(n)}{\sqrt n}
=
\sum_{p,k}
(\log p)p^{-k/2}\,
\langle n|V_p^k\Omega\rangle.
}
\]

So Suzuki's prime-event coefficient is literally:

- primitive-wire label \(\log p\);
- ray depth \(k\);
- half-density attenuation \(p^{-k/2}\);
- incidence with the SUCC wavefront.

---

## 3. Ray Hilbert space and the event-factor operator

Introduce the primitive-ray Hilbert space

\[
\mathcal H_{\rm ray}
=
\ell^2\{(p,k):p\text{ prime},\ k\ge1\}
\]

with basis \(|p,k\rangle\).

Define the incidence isometry

\[
E:\mathcal H_{\rm ray}\to\mathcal H_{\rm add},
\qquad
E|p,k\rangle=|p^k\rangle.
\]

Distinct \((p,k)\) give distinct positive integers, so

\[
\boxed{
E^*E=I_{\rm ray}.
}
\]

Define two commuting diagonal operators on \(\mathcal H_{\rm ray}\):

\[
H|p,k\rangle
=
k\log p\,|p,k\rangle,
\]

and

\[
Q|p,k\rangle
=
\log p\,|p,k\rangle.
\]

Interpretation:

- \(H\) is total multiplicative log-energy / ray proper time;
- \(Q\) remembers the primitive generator carried by the ray.

For real \(\beta>0\), define

\[
W_\beta
=
E Q e^{-\beta H}E^*.
\]

Then, exactly,

\[
\boxed{
W_\beta|n\rangle
=
\Lambda(n)n^{-\beta}|n\rangle.
}
\]

In particular,

\[
\boxed{
W_{1/2}|n\rangle
=
\frac{\Lambda(n)}{\sqrt n}|n\rangle.
}
\]

So the critical Suzuki event weights form a positive diagonal operator with a non-circular arithmetic factor

\[
\boxed{
B_\beta
=
Q^{1/2}e^{-\beta H/2}E^*,
\qquad
B_\beta^*B_\beta=W_\beta.
}
\]

This factors the **event-weight operator**, not the completed Suzuki screw kernel. No RH claim follows from this local/event positivity alone.

---

## 4. The first SUCC pulse gates the source-wiring operator

For \(\sigma>1\), define the source-to-ray emission operator

\[
\boxed{
J_\sigma
=
\sum_{p,k\ge1}
\sqrt{\log p}\,p^{-k\sigma/2}
|p,k\rangle\langle\Omega|.
}
\]

Since

\[
\sum_{p,k}(\log p)p^{-k\sigma}<\infty
\qquad(\sigma>1),
\]

this is a bounded rank-one source coupling.

Before the first SUCC pulse the system is in \(|0\rangle\), orthogonal to the source line.

After

\[
|0\rangle\xrightarrow{S}\Omega,
\]

the entire multiplicative network is energized:

\[
J_\sigma S|0\rangle
=
\sum_{p,k}
\sqrt{\log p}\,p^{-k\sigma/2}|p,k\rangle.
\]

This is an exact source-gating realization of the "first pulse turns on the multiplicative bus" picture.

Its source load is

\[
\boxed{
J_\sigma^*J_\sigma
=
\left(
\sum_{p,k}(\log p)p^{-k\sigma}
\right)
|\Omega\rangle\langle\Omega|.
}
\]

For \(\sigma>1\),

\[
\sum_{p,k}(\log p)p^{-k\sigma}
=
\sum_p\frac{\log p}{p^\sigma-1}
=
-\frac{\zeta'}{\zeta}(\sigma).
\]

Hence

\[
\boxed{
J_\sigma^*J_\sigma
=
-\frac{\zeta'}{\zeta}(\sigma)
|\Omega\rangle\langle\Omega|.
}
\]

The prime Euler logarithmic derivative is literally the scalar load seen by the common source.

---

## 5. The \(t\)-action is the ray log-energy evolution

Let

\[
U_t=e^{itH}
\]

on the ray space.

Then

\[
U_t|p,k\rangle
=
e^{itk\log p}|p,k\rangle
=
p^{ikt}|p,k\rangle.
\]

Therefore, for \(\sigma>1\),

\[
\boxed{
J_\sigma^*U_tJ_\sigma
=
\left(
\sum_{p,k}
(\log p)p^{-k\sigma}e^{itk\log p}
\right)
|\Omega\rangle\langle\Omega|.
}
\]

Equivalently,

\[
\boxed{
J_\sigma^*U_tJ_\sigma
=
-\frac{\zeta'}{\zeta}(\sigma-it)
|\Omega\rangle\langle\Omega|.
}
\]

So the \(t\)-action does not need to be imposed later as an interpretation: it is the modular/log-energy evolution of the already-wired prime rays.

The same incidence map intertwines the ray log-energy with the ordinary logarithmic multiplication operator on prime-power integer states.

---

## 6. Each prime ray contributes one elementary source admittance

For \(\Re s>1\), define

\[
m_p(s)
=
(\log p)\sum_{k\ge1}p^{-ks}
=
\boxed{
\frac{\log p}{p^s-1}.
}
\]

Then

\[
\boxed{
-\frac{\zeta'}{\zeta}(s)
=
\sum_pm_p(s)
}
\qquad(\Re s>1).
\]

This is the source-network form of the Euler logarithmic derivative:

- each primitive prime is one branch;
- repeated traversal of the branch gives \(p^k\);
- its ray response is geometric;
- all ray responses add at the common source.

This is analogous to a parallel network of branch admittances, but no physical electrical identification is assumed.

---

## 7. Completion is a source-boundary term

Write

\[
\xi(s)
=
\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Then

\[
\frac{\xi'}{\xi}(s)
=
\underbrace{
\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\psi(s/2)
}_{=:A_\infty(s)}
+
\frac{\zeta'}{\zeta}(s).
\]

In the Euler half-plane,

\[
\boxed{
\frac{\xi'}{\xi}(s)
=
A_\infty(s)
-
\sum_pm_p(s).
}
\]

Thus the completed object has a clean source-balance reading:

\[
\boxed{
\text{completed source response}
=
\text{Archimedean/pole boundary response}
-
\text{aggregate primitive-ray response}.
}
\]

This is the global coupling that the independent positive local factors do not by themselves control.

---

## 8. Literature hook: the positive-real frontier is classical

A classical criterion, stated explicitly by Lagarias (Acta Arith. 89 (1999), with a 2005 correction to an auxiliary formula), is

\[
\boxed{
\mathrm{RH}
\iff
\Re\frac{\xi'(s)}{\xi(s)}>0
\quad\text{for }\Re s>1/2.
}
\]

So merely rewriting RH as "the completed source response is positive-real" is not new.

The potentially useful contribution of the present construction is different:

> it provides an explicit arithmetic source/ray realization of the finite-place logarithmic derivative and asks whether the completion can be realized as the driving-point function / Weyl function of one passive self-adjoint source-coupled operator.

If that realization were obtained independently of RH, positivity would follow from operator theory rather than from the zero set.

---

## 9. Why a source-coupled star may be different from an independent direct sum

Round004–005 showed that the direct positive sum of local repaired prime factors diverges globally.

The source-wired architecture suggests a different ordering:

1. attach every local ray to one common source;
2. form the finite coupled operator;
3. eliminate/internalize the rays;
4. obtain a scalar source response by Schur complement / Weyl function;
5. include the Archimedean source boundary;
6. only then take the prime/depth limit.

For a finite block operator

\[
\mathcal D_X(z)
=
\begin{pmatrix}
A_X(z) & C_X^*\\
C_X & D_X(z)
\end{pmatrix},
\]

eliminating the internal ray block produces a source Schur complement

\[
\boxed{
M_X(z)
=
A_X(z)-C_X^*D_X(z)^{-1}C_X.
}
\]

The central research question is whether one can choose the **arithmetically forced** ray blocks, couplings, and Archimedean boundary so that

\[
M_X(s)
\longrightarrow
\frac{\xi'}{\xi}(s)
\]

on \(\Re s>1/2\), while every finite \(M_X\) is a positive-real / Herglotz-type source response for structural reasons.

If yes, then positive-realness survives the locally uniform limit and the Lagarias criterion yields RH.

This is a stronger target than summing local \(B_p^*B_p\) and subtracting a divergent correction afterward.

---

## 10. The critical obstruction becomes a limit/domain question

For \(\sigma>1\),

\[
\|J_\sigma\Omega\|^2
=
-\frac{\zeta'}{\zeta}(\sigma)
<\infty.
\]

At critical half-density,

\[
\sigma=\frac12,
\]

the same source vector is not in the naive ray Hilbert space:

\[
\sum_{p,k}(\log p)p^{-k/2}
=
\infty.
\]

So the desired critical object cannot be obtained by norm-converging the naive source vector.

Any proof must instead use a completed/renormalized topology or a larger source-coupled operator in which the Archimedean/pole sector is present **before** taking the limit.

This gives an especially crisp target:

\[
\boxed{
\text{construct finite positive/passive completed source ports }M_X
\text{ whose limit is }\xi'/\xi.
}
\]

The order is load-bearing:

\[
\boxed{
\text{couple + complete first}
\quad\longrightarrow\quad
\text{take the limit second}.
}
\]

Not:

\[
\text{sum divergent prime responses}
\quad\longrightarrow\quad
\text{subtract infinity afterward}.
\]

---

## 11. Relation to the composition-history branch

A separate side branch formalizes ordered compositions as the causal ways to insert FUCC boundaries into SUCC and encodes each history by a polynomial \(P_\alpha\).

That construction lives **upstream** of the integer/ray quotient.

A future source-network construction should compare two spaces:

1. the quotient ray space, where all histories reaching \(p^k\) have been collapsed;
2. the full causal FUCC/SUCC history space before this quotient.

If a source Schur-complement construction fails after quotienting, the history space is the natural place to look for the missing phases/cross terms.

---

## 12. Immediate theorem/experiment targets

1. **Finite source response.** Build finite-depth, finite-prime source-star matrices and derive their exact Schur complements.
2. **Local ray realization.** Make each \(m_p(s)=\log p/(p^s-1)\) arise as an actual Weyl/transfer function of a declared ray operator, not just a scalar series.
3. **Archimedean port.** Construct a source-side operator/channel whose Weyl function is
   \[
   A_\infty(s)
   =
   \frac1s+\frac1{s-1}
   -\frac12\log\pi
   +\frac12\psi(s/2).
   \]
4. **Passivity.** Determine whether the finite completed source response is positive-real on a half-plane by construction.
5. **Limit.** Prove local-uniform / strong-resolvent / form convergence to \(\xi'/\xi\).
6. **Hostile controls.** Mutate a prime weight, delete a wire, change the half-density, or replace prime rays by fake periods; a genuine arithmetic construction should lose the exact completion/passivity identity.
7. **History-space comparison.** Test whether source-coupling before quotienting causal FUCC/SUCC programs changes the effective source port.

---

## 13. Current frontier

The exact finite-place source identity is now:

\[
\boxed{
|0\rangle
\xrightarrow{S}
\Omega=|1\rangle
\xrightarrow{\text{all prime wires}}
\{\,|p^k\rangle\,\},
}
\]

with

\[
\boxed{
\Lambda(n)
=
\sum_{p,k}
(\log p)\,
\langle n|V_p^k\Omega\rangle,
}
\]

and

\[
\boxed{
-\frac{\zeta'}{\zeta}(\sigma-it)
=
\langle J_\sigma\Omega,\,
U_tJ_\sigma\Omega\rangle
\qquad(\sigma>1).
}
\]

The completed frontier is:

\[
\boxed{
\frac{\xi'}{\xi}
=
\text{Archimedean source boundary}
-
\text{prime-ray source load}.
}
\]

The proof problem is no longer "find the primes" or "find local positivity."

It is:

\[
\boxed{
\textbf{Build the completed common-source operator before taking the critical limit, and prove the resulting source port is passive.}
}
\]

That is a concrete operator/limit form of the RH wall.
