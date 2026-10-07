# Subcritical conductor discrepancy as a zero detector

**Date:** 2026-10-06  
**Status:** rigorous one-way zero-free criterion by Abel/Mellin continuation; residue formula for simple uncancelled zeros. **RH remains open.**

The conductor discrepancy introduced by the discrete Suzuki realization is not only an arithmetic diagnostic. A subpower bound on it directly forces the zero-free half-plane required for Suzuki's innerness criterion.

This is a proof-bearing \(\mathbb N\)-native target.

---

## 1. Parameterization

Let

\[
0<\omega<\frac12,
\qquad
\delta=\frac12-\omega.
\]

Then

\[
0<\delta<\frac12
\]

and the Suzuki conductor event weight is

\[
b_\delta(n)
=
n^{-\delta}
\prod_{p\mid n}
(1-p^{-1+2\delta}).
\]

Its Dirichlet series is

\[
\boxed{
A_\delta(s)
=
\sum_{n\ge1}
\frac{b_\delta(n)}{n^s}
=
\frac{
\zeta(s+\delta)
}{
\zeta(s+1-\delta)
}
}
\]

in the absolute-convergence region

\[
\Re s>1-\delta.
\]

---

## 2. Main conductor pole

The numerator has the zeta pole at

\[
s+\delta=1,
\]

i.e.

\[
\boxed{
\alpha:=1-\delta
=
\frac12+\omega.
}
\]

Its residue is

\[
\boxed{
R_\delta
=
\frac1{\zeta(2-2\delta)}.
}
\]

Therefore the summatory main coefficient is

\[
\boxed{
C_\delta
=
\frac{R_\delta}{\alpha}
=
\frac1{
(1-\delta)\zeta(2-2\delta)
}.
}
\]

Define

\[
\boxed{
B_\delta(X)
=
\sum_{n\le X}b_\delta(n)
}
\]

and centered discrepancy

\[
\boxed{
E_\delta(X)
=
B_\delta(X)-C_\delta X^\alpha.
}
\]

---

# 3. Abel transform of the centered discrepancy

For \(\Re s>\alpha\),

\[
A_\delta(s)
=
s\int_1^\infty
B_\delta(x)x^{-s-1}\,dx
\]

with the standard convention for the step function.

Insert

\[
B_\delta(x)
=
C_\delta x^\alpha+E_\delta(x).
\]

Then

\[
\boxed{
A_\delta(s)
=
C_\delta\frac{s}{s-\alpha}
+
s\int_1^\infty
E_\delta(x)x^{-s-1}\,dx.
}
\]

Since

\[
C_\delta\frac{s}{s-\alpha}
=
C_\delta
+
\frac{R_\delta}{s-\alpha},
\]

\[
\boxed{
A_\delta(s)
-
\frac{R_\delta}{s-\alpha}
-
C_\delta
=
s\int_1^\infty
E_\delta(x)x^{-s-1}\,dx.
}
\]

This is exact in the initial half-plane.

---

# 4. Subpower conductor cancellation implies the Suzuki zero-free region

Assume:

\[
\boxed{
E_\delta(X)
=
O_\varepsilon(X^\varepsilon)
\qquad
\text{for every }\varepsilon>0.
}
\]

Fix any

\[
\sigma=\Re s>0.
\]

Choose

\[
0<\varepsilon<\sigma.
\]

Then

\[
E_\delta(x)x^{-s-1}
=
O(x^{-1-\sigma+\varepsilon}),
\]

which is integrable at infinity.

Therefore

\[
s\int_1^\infty
E_\delta(x)x^{-s-1}\,dx
\]

defines an analytic function throughout

\[
\boxed{\Re s>0.}
\]

Hence

\[
A_\delta(s)
-
\frac{R_\delta}{s-\alpha}
\]

has an analytic continuation to \(\Re s>0\).

But

\[
A_\delta(s)
=
\frac{\zeta(s+\delta)}
{\zeta(s+1-\delta)}.
\]

If

\[
\rho
\]

were a denominator zero with

\[
\Re\rho>1-\delta,
\]

then

\[
\boxed{
s_\rho
=
\rho-1+\delta
}
\]

would satisfy

\[
\Re s_\rho>0
\]

and would be a pole of \(A_\delta\), except in the exceptional case of exact numerator cancellation.

Such a cancellation would require

\[
\zeta(\rho-1+2\delta)=0
\]

at the reflected shift. Iterating any such finite cancellation chain moves the real part strictly left by

\[
1-2\delta=2\omega>0,
\]

so a rightmost denominator zero cannot be canceled indefinitely.

Therefore the analytic continuation above rules out zeros in

\[
\boxed{
\Re\rho>1-\delta
=
\frac12+\omega.
}
\]

Thus:

\[
\boxed{
E_\delta(X)=O_\varepsilon(X^\varepsilon)
\ \forall\varepsilon>0
\Longrightarrow
\zeta(s)\ne0
\text{ for }\Re s>\frac12+\omega.
}
\]

By Suzuki's Proposition 1.2 this is exactly the half-plane associated with innerness of \(\Theta_\omega\).

---

## 5. An off-line zero produces a conductor gain mode

Suppose

\[
\rho=\beta+i\gamma
\]

is a simple zero of \(\zeta\), and suppose

\[
\zeta(\rho-1+2\delta)\ne0.
\]

Then \(A_\delta(s)\) has a simple pole at

\[
\boxed{
s_\rho
=
\rho-1+\delta.
}
\]

Its residue is

\[
\boxed{
\operatorname{Res}_{s=s_\rho}
A_\delta(s)
=
\frac{
\zeta(\rho-1+2\delta)
}{
\zeta'(\rho)
}.
}
\]

In a Perron/explicit-formula expansion of the smoothed or suitably endpoint-normalized summatory function, this pole contributes

\[
\boxed{
\frac{
\zeta(\rho-1+2\delta)
}{
(\rho-1+\delta)\zeta'(\rho)
}
X^{\rho-1+\delta}.
}
\]

Its envelope is

\[
\boxed{
X^{\beta-1+\delta}.
}
\]

At the Suzuki boundary

\[
\beta=1-\delta,
\]

the mode is neutral.

If

\[
\beta>1-\delta,
\]

it grows.

So the zero-free boundary is exactly the gain/loss transition of the centered conductor shadow.

---

# 6. Translate into \(\omega\)

Since

\[
\delta=\frac12-\omega,
\]

\[
1-\delta
=
\frac12+\omega.
\]

The zero-mode exponent is

\[
\boxed{
\beta-\frac12-\omega.
}
\]

Therefore:

\[
\beta=\frac12+\omega
\quad\Longrightarrow\quad
\text{neutral conductor oscillation},
\]

\[
\beta>\frac12+\omega
\quad\Longrightarrow\quad
\text{growing conductor mode}.
\]

This is the Suzuki-family generalization of the earlier critical gain picture.

---

## 7. RH target in conductor language

If for every

\[
\omega>0
\]

equivalently every

\[
0<\delta<1/2,
\]

one could prove

\[
\boxed{
E_\delta(X)
=
O_{\delta,\varepsilon}(X^\varepsilon)
\qquad
\forall\varepsilon>0,
}
\]

then zeta would have no zeros in

\[
\Re s>\frac12+\omega
\]

for any \(\omega>0\).

Letting

\[
\omega\downarrow0
\]

would give

\[
\boxed{RH.}
\]

Thus the entire RH problem admits the concrete conductor-discrepancy target:

\[
\boxed{
\textbf{prove subpower cancellation of the Möbius/carry conductor error for every subcritical tilt.}
}
\]

---

## 8. Exact carry form of the target

Recall

\[
E_\delta(X)
=
\sum_{d\le X}
\mu(d)d^{-1+\delta}
\mathscr C_\delta(X/d)
-
\frac{X^{1-\delta}}{1-\delta}
\sum_{d>X}
\frac{\mu(d)}{d^{2-2\delta}}.
\]

Therefore the proof target is specifically a cancellation theorem for

\[
\boxed{
\mu(d)
\times
\mathscr C_\delta(X/d),
}
\]

where \(\mathscr C_\delta\) is the fractional quotient/carry phase.

This is not a generic prime-distribution error term.

It is the exact boundary interaction of:

- inverse-FUCC/Möbius signs;
- SUCC quotient/carry phases.

---

## 9. Connection to the local/global Weyl picture

Each local prime channel remains Schur throughout the entire subcritical deformation.

The growing mode above appears only after:

1. assembling infinitely many conductor channels;
2. centering their deterministic mean;
3. inspecting the global carry/Möbius correlation.

Thus the conductor criterion makes precise:

\[
\boxed{
\text{RH failure cannot be local to a prime;}
}
\]

\[
\boxed{
\text{it is a coherent global mode of the carry-correlation network}.
}
\]

---

## 10. Research priorities

For fixed small \(\delta>0\), analyze

\[
D_\delta(X)
=
\sum_{d\le X}
\mu(d)d^{-1+\delta}
\]

and

\[
Q_\delta(X)
=
\sum_{d\le X}
\mu(d)d^{-1+\delta}
\widetilde{\mathscr C}_\delta(X/d).
\]

Seek:

- reciprocity/functional equations for \(Q_\delta\);
- Estermann-zeta representations;
- continued-fraction decomposition of the sawtooth component;
- finite matrix/operator norms controlling the pairing;
- cancellation between \(D_\delta\) and \(Q_\delta\) stronger than either alone.

The Maier--Rassias / Bettin--Conrey / Nyman--Beurling machinery is directly relevant here.

---

## 11. House theorem target

\[
\boxed{
E_\delta(X)=X^{o(1)}
\quad\forall\,0<\delta<1/2
}
\]

would imply RH.

And an off-line zero would appear in precisely the same observable as a power-law gain mode.

This is currently the sharpest \(\mathbb N\)-native RH target produced by the discrete-conductor Suzuki program.
