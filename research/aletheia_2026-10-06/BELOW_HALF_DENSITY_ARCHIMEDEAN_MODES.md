# Below half-density: one unstable Archimedean mode plus a positive inverse-SUCC tower

**Date:** 2026-10-06  
**Status:** exact pole/residue structure of the Archimedean factor for \(0<\omega\le\tfrac12\); global innerness remains the RH-linked problem.

---

## 1. Parameterize distance below the half-density point

Let

\[
\boxed{
\delta
=
\frac12-\omega.
}
\]

For

\[
0<\omega\le\frac12,
\]

\[
0\le\delta<\frac12.
\]

Suzuki's critical-family scattering function on the Laplace axis factors as

\[
\Theta_\omega(is)
=
A_\omega(s)
G_{\infty,\omega}(s),
\]

where

\[
\boxed{
A_\omega(s)
=
\frac{
\zeta(s+\delta)
}{
\zeta(s+1-\delta)
}
}
\]

is the arithmetic/conductor factor and

\[
\boxed{
G_{\infty,\omega}(s)
=
\pi^\omega
\frac{
(s+\delta)(s+\delta-1)
}{
(s+1-\delta)(s-\delta)
}
\frac{
\Gamma((s+\delta)/2)
}{
\Gamma((s+1-\delta)/2)
}
}
\]

is the Archimedean factor.

Their product is

\[
\boxed{
A_\omega(s)G_{\infty,\omega}(s)
=
\frac{
\xi(s+\delta)
}{
\xi(s+1-\delta)
}.
}
\]

---

## 2. The distinguished Archimedean pole

For

\[
0<\omega<\frac12,
\]

the rational factor produces a pole at

\[
\boxed{
s=\delta
=
\frac12-\omega
>0.
}
\]

Its residue is negative.

Write

\[
\boxed{
\operatorname{Res}_{s=\delta}
G_{\infty,\omega}(s)
=
-\kappa_0(\omega),
}
\]

where

\[
\boxed{
\kappa_0(\omega)
=
2\omega(1-2\omega)
\pi^{\omega-1/2}
\Gamma\!\left(\frac12-\omega\right)
>0.
}
\]

As

\[
\omega\uparrow\frac12,
\]

\[
\boxed{
\kappa_0(\omega)\to2
}
\]

and

\[
\delta\to0.
\]

Thus the critical negative zero-frequency contribution

\[
-\frac2s
\]

is the endpoint of a genuine unstable mode

\[
\boxed{
-\frac{\kappa_0(\omega)}{s-\delta}.
}
\]

---

# 3. The remaining Gamma poles form a stable positive tower

The numerator Gamma factor has poles at

\[
\frac{s+\delta}{2}=-m.
\]

The \(m=0\) pole is canceled by the explicit factor \(s+\delta\).

For every

\[
m\ge1,
\]

there remains a pole at

\[
\boxed{
s_m
=
-(\delta+2m)
<0.
}
\]

Its residue is positive:

\[
\boxed{
\operatorname{Res}_{s=s_m}
G_{\infty,\omega}(s)
=
\kappa_m(\omega)>0,
}
\]

with

\[
\boxed{
\kappa_m(\omega)
=
\pi^{\omega-1}
\sin(\pi\omega)
\frac{
\Gamma(m-\omega)
}{
(m-1)!
}
\frac{
2m+1
}{
m+\frac12-\omega
}.
}
\]

Every factor is positive for

\[
0<\omega<1,
\qquad
m\ge1.
\]

At the critical endpoint,

\[
\boxed{
\kappa_m(1/2)
=
2a_m,
}
\]

where \(a_m\) are the positive coefficients of the exact critical expansion.

---

## 4. Modal form

The resulting Mittag--Leffler/state-space expansion is

\[
\boxed{
G_{\infty,\omega}(s)
=
-\frac{
\kappa_0(\omega)
}{
s-\delta
}
+
\sum_{m\ge1}
\frac{
\kappa_m(\omega)
}{
s+\delta+2m
},
}
\]

with the endpoint interpreted by the \(\omega\to1/2\) limit.

The series converges locally away from its poles; the residues have asymptotic size

\[
\kappa_m(\omega)\asymp m^{-\omega},
\]

so the summands are

\[
O(m^{-1-\omega}).
\]

This is the resolvent of:

- one negative-residue mode with growth rate \(\delta\);
- a positive stable tower with decay rates
  \[
  \delta+2,\delta+4,\delta+6,\ldots.
  \]

---

## 5. Time-domain interpretation

The Archimedean impulse response has the form

\[
\boxed{
K_\omega(t)
=
-\kappa_0(\omega)e^{\delta t}
+
\sum_{m\ge1}
\kappa_m(\omega)
e^{-(\delta+2m)t}.
}
\]

Thus for

\[
0<\omega<1/2,
\]

the **bare Archimedean subsystem contains exactly one exponentially growing negative-sign mode**.

All remaining inverse-SUCC modes decay.

At

\[
\omega=1/2,
\]

that mode becomes marginal:

\[
e^{\delta t}\to1.
\]

This recovers the exact critical state-space.

---

# 6. Arithmetic completion cancels the unstable mode algebraically

At

\[
s=\delta,
\]

the denominator of the arithmetic factor is

\[
\zeta(s+1-\delta)
=
\zeta(1),
\]

so

\[
\boxed{
A_\omega(\delta)=0
}
\]

in the meromorphic sense.

Therefore the arithmetic zero cancels the Archimedean unstable pole.

This is one exact local completion seam:

\[
\boxed{
\text{Archimedean unstable pole at }s=\delta
+
\text{arithmetic zero from }\zeta(1)^{-1}
\to
\text{finite completed channel}.
}
\]

---

## 7. The reflected completion seam

At

\[
\boxed{
s=1-\delta
=
\frac12+\omega,
}
\]

the arithmetic numerator is

\[
\zeta(s+\delta)=\zeta(1),
\]

so

\[
A_\omega
\]

has a pole.

But the Archimedean factor has the explicit zero

\[
s+\delta-1=0.
\]

Thus

\[
\boxed{
\text{arithmetic pole at }s=1-\delta
+
\text{Archimedean zero}
\to
\text{finite completed channel}.
}
\]

The two distinguished seams are exchanged by the completed reflection.

---

# 8. Dynamical phase transition at \(\omega=1/2\)

### \(\omega>1/2\)

The distinguished Archimedean mode lies in the stable half-plane.

### \(\omega=1/2\)

It is marginal:

\[
s=0.
\]

### \(0<\omega<1/2\)

It moves into the unstable half-plane:

\[
s=\frac12-\omega>0.
\]

Therefore the half-density point is exactly the **open-loop Archimedean stability threshold**.

This is separate from the global zeta-zero passivity threshold, but the two meet at the same distinguished parameter.

---

## 9. Relation to the user's earlier gain/loss intuition

The exact state-space now supports the following language:

\[
\boxed{
\omega<1/2
\Rightarrow
\text{bare vacuum/Archimedean channel has a growing mode}.
}
\]

The completed arithmetic system supplies the exact local cancellation of that known mode.

What remains nontrivial is whether the **closed-loop infinite system** has any additional nonphysical upper-half-plane poles.

Those additional poles are precisely controlled by the zeta zeros.

So:

\[
\boxed{
\text{known vacuum instability is locally canceled;}
}
\]

\[
\boxed{
\text{RH asks whether there are any residual global instabilities.}
}
\]

---

## 10. Control-theoretic formulation

The factorization suggests an open-loop/closed-loop language:

### Open-loop arithmetic plant

\[
A_\omega(s)
=
\frac{
\zeta(s+\delta)
}{
\zeta(s+1-\delta)
}.
\]

### Open-loop Archimedean compensator

\[
G_{\infty,\omega}(s).
\]

### Completed closed-loop scattering

\[
\boxed{
\Theta_\omega(is)
=
A_\omega(s)G_{\infty,\omega}(s).
}
\]

The known pole-zero pairs at

\[
s=\delta,\qquad s=1-\delta
\]

are structural completion cancellations.

The remaining innerness/stability question is global and RH-sensitive.

---

## 11. Why this matters for extending Suzuki below criticality

For \(\omega<1/2\), one should not demand that the **bare Archimedean block** be passive: it cannot be, because it contains an unstable mode.

Instead, build the finite arithmetic/Archimedean completion so that the distinguished unstable mode and its arithmetic zero are paired **inside the finite realization** before applying a global passivity test.

This parallels the earlier Gamma/trivial-zero Blaschke no-go:

\[
\boxed{
\text{complete first, demand positivity second}.
}
\]

---

## 12. House statement

\[
\boxed{
\text{At }\omega<1/2,\text{ infinity contributes exactly one known unstable mode.}
}
\]

\[
\boxed{
\text{Arithmetic cancels that mode exactly.}
}
\]

\[
\boxed{
\text{The rest of the Archimedean ladder is stable and positive-residue.}
}
\]

\[
\boxed{
\text{RH is the absence of any additional global unstable modes after completion.}
}
\]
