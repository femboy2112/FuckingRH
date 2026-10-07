# Exact carry formula for the Suzuki conductor discrepancy

**Date:** 2026-10-06  
**Status:** exact finite arithmetic identity. **RH remains open.**

The subcritical conductor residual can be written exactly as a Möbius-weighted quotient/carry-phase observable.

At the critical endpoint, the local carry kernel collapses to the ordinary sawtooth

\[
-\{X/d\}.
\]

This directly links the Suzuki canonical-system arithmetic to the SUCC/FUCC divisibility/carry network.

---

## 1. Conductor weights

Let

\[
\delta=\frac12-\omega,
\qquad
0\le\delta<\frac12.
\]

Then

\[
b_\omega(n)
=
n^{-\delta}
\prod_{p\mid n}(1-p^{-1+2\delta}).
\]

Expand the product by Möbius inversion:

\[
\boxed{
b_\omega(n)
=
n^{-\delta}
\sum_{d\mid n}
\mu(d)d^{-1+2\delta}.
}
\]

Define

\[
\boxed{
B_\delta(X)
=
\sum_{n\le X}b_\omega(n).
}
\]

---

## 2. Exact divisor/quotient decomposition

Write

\[
n=dm.
\]

Then

\[
\begin{aligned}
B_\delta(X)
&=
\sum_{d\le X}
\mu(d)d^{-1+2\delta}
\sum_{m\le X/d}
(dm)^{-\delta}\\
&=
\boxed{
\sum_{d\le X}
\mu(d)d^{-1+\delta}
H_\delta(X/d),
}
\end{aligned}
\]

where

\[
\boxed{
H_\delta(y)
=
\sum_{1\le m\le y}
m^{-\delta}
=
\sum_{m=1}^{\lfloor y\rfloor}m^{-\delta}.
}
\]

This is exact.

Every term depends on the integer quotient

\[
\lfloor X/d\rfloor,
\]

so the residual is already written in SUCC/FUCC quotient/carry coordinates.

---

# 3. Local fractional carry kernel

Define

\[
\boxed{
\mathscr C_\delta(y)
=
H_\delta(y)
-
\frac{y^{1-\delta}}{1-\delta}.
}
\]

Then

\[
H_\delta(X/d)
=
\frac{
(X/d)^{1-\delta}
}{
1-\delta
}
+
\mathscr C_\delta(X/d).
\]

Substitute:

\[
\begin{aligned}
B_\delta(X)
&=
\frac{
X^{1-\delta}
}{
1-\delta
}
\sum_{d\le X}
\frac{\mu(d)}{d^{2-2\delta}}
\\
&\qquad+
\sum_{d\le X}
\mu(d)d^{-1+\delta}
\mathscr C_\delta(X/d).
\end{aligned}
\]

---

## 4. Subtract the global mean exactly

Let

\[
\boxed{
C_\delta
=
\frac1{
(1-\delta)\zeta(2-2\delta)
}.
}
\]

Define

\[
\boxed{
E_\delta(X)
=
B_\delta(X)-C_\delta X^{1-\delta}.
}
\]

Since

\[
\frac1{\zeta(2-2\delta)}
=
\sum_{d\ge1}
\frac{\mu(d)}{d^{2-2\delta}}
\]

absolutely, subtraction gives the exact identity

\[
\boxed{
E_\delta(X)
=
\sum_{d\le X}
\mu(d)d^{-1+\delta}
\mathscr C_\delta(X/d)
-
\frac{
X^{1-\delta}
}{
1-\delta
}
\sum_{d>X}
\frac{\mu(d)}{d^{2-2\delta}}.
}
\]

No asymptotic approximation has been made.

---

# 5. Critical endpoint: the carry kernel becomes a sawtooth

At

\[
\delta=0,
\]

\[
H_0(y)
=
\lfloor y\rfloor.
\]

Therefore

\[
\boxed{
\mathscr C_0(y)
=
\lfloor y\rfloor-y
=
-\{y\}.
}
\]

Also

\[
C_0=\frac1{\zeta(2)}.
\]

Hence

\[
\boxed{
E_0(X)
=
-\sum_{d\le X}
\frac{\mu(d)}d
\left\{
\frac Xd
\right\}
-
X
\sum_{d>X}
\frac{\mu(d)}{d^2}.
}
\]

This is the exact critical conductor discrepancy.

The main finite term is literally:

\[
\boxed{
\text{inverse-divisibility sign }\mu(d)
\times
\text{carry phase }\{X/d\}
\times
\text{half-density-like weight }1/d.
}
\]

---

## 6. Elementary bound becomes transparent

At criticality,

\[
0\le\{X/d\}<1.
\]

Therefore

\[
\left|
\sum_{d\le X}
\frac{\mu(d)}d
\left\{
\frac Xd
\right\}
\right|
\le
\sum_{d\le X}\frac1d
=
O(\log X).
\]

Also

\[
X
\sum_{d>X}\frac1{d^2}
=
O(1).
\]

Thus

\[
\boxed{
E_0(X)=O(\log X).
}
\]

The previously derived critical mean/residual estimate is now seen directly as an absolute bound on the finite carry phases.

No cancellation of Möbius signs is even required at the endpoint.

---

# 7. Below criticality: fractional-harmonic carry phase

For

\[
0<\delta<1/2,
\]

the local function

\[
\mathscr C_\delta(y)
=
\sum_{m\le y}m^{-\delta}
-
\frac{y^{1-\delta}}{1-\delta}
\]

is the exact nonlinear replacement of the sawtooth.

Euler--Maclaurin gives, for large \(y\),

\[
\boxed{
\mathscr C_\delta(y)
=
\zeta(\delta)
+
O(y^{-\delta})
}
\]

away from the usual endpoint convention.

Thus the local carry response acquires a nonzero DC component

\[
\zeta(\delta).
\]

This is a key difference from

\[
\mathscr C_0(y)=-\{y\},
\]

whose size is bounded but whose mean/carry structure is purely order-one.

---

## 8. Separate DC and oscillatory carry components

Define

\[
\boxed{
\widetilde{\mathscr C}_\delta(y)
=
\mathscr C_\delta(y)-\zeta(\delta).
}
\]

Then

\[
\widetilde{\mathscr C}_\delta(y)
=
O(y^{-\delta})
\]

as \(y\to\infty\).

The discrepancy becomes

\[
\boxed{
E_\delta(X)
=
\zeta(\delta)
\sum_{d\le X}
\mu(d)d^{-1+\delta}
+
\sum_{d\le X}
\mu(d)d^{-1+\delta}
\widetilde{\mathscr C}_\delta(X/d)
-
\text{tail}.
}
\]

This decomposition is especially revealing:

### DC channel

\[
\boxed{
\sum_{d\le X}
\frac{\mu(d)}{d^{1-\delta}}
}
\]

is explicitly Möbius/RH-sensitive.

### AC/carry channel

\[
\boxed{
\widetilde{\mathscr C}_\delta(X/d)
}
\]

contains the quotient/modulus phase.

So below criticality, the conductor error splits into:

\[
\boxed{
\text{Möbius DC cancellation}
+
\text{Möbius-weighted carry oscillation}
+
\text{absolutely convergent tail}.
}
\]

---

# 9. Matrix interpretation through inverse divisibility

Let

\[
Z_X(i,j)=1_{i\mid j}
\]

be the finite divisibility/zeta-poset matrix.

Then

\[
Z_X^{-1}
\]

has Möbius entries.

The vector

\[
\mu_X=(\mu(1),\ldots,\mu(X))
\]

is the vacuum boundary row of this inverse network.

Define the carry vector

\[
\boxed{
c_{\delta,X}(d)
=
d^{-1+\delta}
\mathscr C_\delta(X/d).
}
\]

Then the first finite term of the discrepancy is exactly

\[
\boxed{
\langle
\mu_X,
c_{\delta,X}
\rangle.
}
\]

At criticality,

\[
c_{0,X}(d)
=
-\frac1d\{X/d\}.
\]

Thus the critical Suzuki conductor residual is a boundary matrix coefficient of the inverse divisibility network driven by the quotient-carry state.

This directly connects the Redheffer/Möbius seam to the Suzuki/Weyl seam.

---

## 10. What RH-sensitive improvement means in these coordinates

The elementary subcritical estimate

\[
E_\delta(X)=O(X^\delta)
\]

comes from taking absolute values.

Any better estimate requires cancellation in one or both of:

\[
\sum_{d\le X}
\mu(d)d^{-1+\delta}
\]

and

\[
\sum_{d\le X}
\mu(d)d^{-1+\delta}
\widetilde{\mathscr C}_\delta(X/d).
\]

So the exact arithmetic question is now:

\[
\boxed{
\textbf{How does the Möbius/inverse-FUCC sign field correlate with the quotient-carry phase field?}
}
\]

That is precisely the user's original "dance of twists of moduli and carry" question, now as a finite formula.

---

# 11. Candidate observable for experiments

For fixed \(\delta\), track separately

\[
\boxed{
D_\delta(X)
=
\sum_{d\le X}
\mu(d)d^{-1+\delta}
}
\]

and

\[
\boxed{
Q_\delta(X)
=
\sum_{d\le X}
\mu(d)d^{-1+\delta}
\widetilde{\mathscr C}_\delta(X/d).
}
\]

Then

\[
E_\delta(X)
=
\zeta(\delta)D_\delta(X)
+
Q_\delta(X)
-
\text{tail}.
\]

Inspect:

- individual sizes;
- covariance/cancellation;
- behavior at prime-power SUCC events;
- conductor decompositions;
- finite transfer/Schur representations.

This is more informative than plotting \(E_\delta\) alone.

---

## 12. House result

\[
\boxed{
\text{At }\omega=1/2,\text{ the conductor residual is literally Möbius times carry sawtooth.}
}
\]

\[
\boxed{
\text{Below }\omega=1/2,\text{ a Möbius DC mode appears in addition to the carry oscillation.}
}
\]

\[
\boxed{
\text{The RH-sensitive seam is the correlation of those two fields.}
}
\]

This is one of the most concrete \(\mathbb N\)-native shadows of the Suzuki/Weyl wall.
