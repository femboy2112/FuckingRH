# Suzuki carry discrepancy meets Nyman--Beurling on the rational SUCC mesh

**Date:** 2026-10-06  
**Status:** exact critical identity plus asymptotic subcritical extension. This is a bridge between two established RH frameworks, not a proof of RH.

---

## 1. The Nyman--Beurling primitive

Let

\[
\rho(x)=x-\lfloor x\rfloor=\{x\}.
\]

A standard Nyman--Beurling family is

\[
\boxed{
\rho_a(x)
=
\rho\!\left(\frac1{ax}\right).
}
\]

The strong Báez-Duarte version restricts the dilation parameter \(a\) to positive integers and relates the \(L^2\)-closure of the resulting span to RH.

Möbius-weighted combinations of these fractional-part functions are a central object in that theory.

---

# 2. Critical Suzuki carry is exactly the same sawtooth

At \(\omega=1/2\), the exact conductor discrepancy is

\[
E_0(X)
=
-\sum_{d\le X}
\frac{\mu(d)}d
\left\{
\frac Xd
\right\}
-
X\sum_{d>X}\frac{\mu(d)}{d^2}.
\]

Set

\[
\boxed{
x_d=\frac dX.
}
\]

Then

\[
\frac Xd=\frac1{x_d}.
\]

Therefore

\[
\boxed{
\left\{\frac Xd\right\}
=
\rho_1(x_d).
}
\]

Hence

\[
\boxed{
E_0(X)
+
X\sum_{d>X}\frac{\mu(d)}{d^2}
=
-\sum_{d\le X}
\frac{\mu(d)}d
\rho_1(d/X).
}
\]

This is an exact finite identity.

So the critical Suzuki conductor residual is a Möbius-weighted sample of the basic Nyman--Beurling sawtooth on the causal mesh

\[
\boxed{
\left\{
\frac1X,\frac2X,\ldots,1
\right\}.
}
\]

---

## 3. Why this mesh is natural in SUCC/FUCC geometry

At carrier horizon \(X\), each divisor channel \(d\le X\) has normalized position

\[
x_d=d/X.
\]

The quotient

\[
\lfloor X/d\rfloor
\]

counts how many \(d\)-sized FUCC cells fit inside the current SUCC horizon.

The fractional remainder

\[
\{X/d\}
\]

is the unresolved carry phase.

Therefore the Nyman fractional-part coordinate is exactly:

\[
\boxed{
\text{normalized residual of dividing the current SUCC horizon by a FUCC scale}.
}
\]

This gives a concrete causal meaning to the NB sawtooth.

---

# 4. Möbius is the inverse-FUCC boundary field

The finite divisibility matrix

\[
Z_X(i,j)=1_{i\mid j}
\]

has inverse with Möbius entries.

Its vacuum boundary row is

\[
(\mu(1),\ldots,\mu(X)).
\]

Thus the critical Suzuki/NB sample can be read as the boundary pairing

\[
\boxed{
\text{inverse-divisibility vacuum field}
\quad\cdot\quad
\text{quotient-carry sawtooth field}.
}
\]

So the same two ingredients appear in both frameworks:

- Möbius inversion;
- fractional-part/carry geometry.

---

# 5. A discrete NB quadrature viewpoint

Define a signed atomic measure on \((0,1]\):

\[
\boxed{
d\sigma_X(x)
=
\sum_{d\le X}
\frac{\mu(d)}d
\delta_{d/X}(dx).
}
\]

Then

\[
\boxed{
E_0(X)+\text{tail}
=
-\int_{(0,1]}
\rho(1/x)
\,d\sigma_X(x).
}
\]

Thus one scalar shadow of the finite arithmetic network is the action of the signed Möbius measure \(\sigma_X\) on the Nyman generator.

The full NB problem asks for \(L^2\) approximation, not merely this one scalar pairing.

Therefore this identity does not reduce RH by itself.

But it identifies the same finite measures/carry phases as natural candidates for a stronger functional comparison.

---

# 6. Suggested stronger object

Instead of retaining only

\[
E_0(X),
\]

define the entire finite carry field

\[
\boxed{
\mathcal R_X(x)
=
\sum_{d\le X}
\frac{\mu(d)}d
\rho_d(x),
\qquad
\rho_d(x)
=
\left\{
\frac1{dx}
\right\}.
}
\]

Compare:

- its \(L^2\) geometry from Nyman--Beurling;
- its samples at
  \[
  x=d'/X;
  \]
- its image under the conductor/Suzuki Archimedean kernel;
- the finite divisibility Gram induced by the same Möbius coefficients.

The hope is to show that Suzuki's canonical boundary response is a transformed norm/Gram shadow of the same NB approximation field.

This is now a concrete bridge question.

---

# 7. Subcritical carry retains the same sawtooth at leading order

For

\[
0<\delta<1/2,
\]

the local carry kernel is

\[
\mathscr C_\delta(y)
=
\sum_{m\le y}m^{-\delta}
-
\frac{y^{1-\delta}}{1-\delta}.
\]

Using the Hurwitz-zeta/Euler--Maclaurin expansion,

\[
\boxed{
\mathscr C_\delta(y)
=
\zeta(\delta)
+
\left(
\frac12-\{y\}
\right)y^{-\delta}
+
O(y^{-\delta-1})
}
\]

uniformly away from the harmless endpoint convention.

Thus after removing the DC term \(\zeta(\delta)\), the leading subcritical carry geometry is still the same sawtooth:

\[
\boxed{
\frac12-\left\{\frac Xd\right\}.
}
\]

---

## 8. Leading weighted NB sum below criticality

Insert the expansion into the exact discrepancy formula.

The oscillatory carry channel has leading term

\[
\boxed{
Q_\delta(X)
=
X^{-\delta}
\sum_{d\le X}
\mu(d)d^{-1+2\delta}
\left(
\frac12-\left\{\frac Xd\right\}
\right)
+
\text{lower-order remainder}.
}
\]

So descending below \(\omega=1/2\) does not replace the NB/carry geometry.

It changes its weighting:

\[
\boxed{
\frac{\mu(d)}d
\quad\longrightarrow\quad
X^{-\delta}\mu(d)d^{-1+2\delta}.
}
\]

This is a natural **fractionally tilted Nyman--Beurling sum**.

---

# 9. Relation to Estermann/cotangent-sum territory

Möbius-weighted fractional-part sums of Nyman--Beurling type are known to connect to Estermann zeta functions, Fourier expansions, continued fractions, and cotangent sums.

This is close to the Bettin--Conrey / Báez-Duarte / NB cluster already present in the repository.

Therefore the new conductor-carry formula gives a concrete path for importing those analytic estimates into the Suzuki canonical-system problem.

The important point is not a generic literature analogy:

\[
\boxed{
\text{the exact finite Suzuki residual contains the NB sawtooth explicitly}.
}
\]

---

## 10. A two-observable program

At each horizon \(X\), compute:

### Scalar Suzuki residual

\[
E_0(X).
\]

### Functional NB residual

\[
\mathcal R_X(x)
=
\sum_{d\le X}
\frac{\mu(d)}d\rho_d(x).
\]

Then ask whether there is an exact/controlled transform

\[
\boxed{
\mathcal T_{\rm Suzuki}
\mathcal R_X
\longrightarrow
E_0(X)
\ \text{or the finite Hankel/canonical coefficient}.
}
\]

If such a transform is contractive in the NB \(L^2\) geometry, the known RH-equivalent NB closure problem could potentially control the Suzuki passivity seam.

That is a serious bridge to investigate.

---

## 11. What this does NOT establish

The scalar identity does not imply the Nyman--Beurling criterion.

Conversely, known NB criteria do not automatically give Suzuki's finite canonical Hamiltonian.

The missing theorem is an operator/Gram relation between:

\[
\boxed{
\text{NB fractional-part function space}
}
\]

and

\[
\boxed{
\text{Suzuki conductor/Hankel boundary space}.
}
\]

The exact carry identity identifies the common arithmetic coordinates in which to search for it.

---

## 12. House result

\[
\boxed{
\text{Nyman's fractional part is literally FUCC carry phase.}
}
\]

\[
\boxed{
\text{Möbius is the inverse-divisibility boundary field.}
}
\]

\[
\boxed{
\text{Suzuki's critical conductor error pairs those two objects exactly.}
}
\]

So two previously parallel RH programs in the repository now share one explicit finite arithmetic seam.
