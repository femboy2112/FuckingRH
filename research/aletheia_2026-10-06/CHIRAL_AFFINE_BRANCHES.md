# Chiral affine branches: 2x±1 factor SUCC and its carry energy

**Date:** 2026-10-06  
**Status:** exact operator identities + a candidate first-order refinement of the carry geometry. RH remains open.

This note formalizes the intuition that

\[
2x+1
\]

is not merely another affine map: together with its mirror

\[
2x-1
\]

it forms a genuinely two-sided / chiral pair around the binary FUCC scaffold \(2x\).

The key result is that the two oriented affine branches factor both the SUCC carrier and the Round005 carry-energy operator.

---

## 1. Setup

Work on

\[
\mathcal H=\ell^2(\mathbb N_{>0})
\]

with basis \(|n\rangle\).

Let

\[
S|n\rangle=|n+1\rangle
\]

be the unilateral SUCC shift, with

\[
S^*|1\rangle=0,
\qquad
S^*|n\rangle=|n-1\rangle
\quad(n>1).
\]

Let

\[
V_2|n\rangle=|2n\rangle
\]

be binary FUCC/dilation.

Define the two oriented affine branches

\[
\boxed{
A_+ := S V_2,
\qquad
A_- := S^*V_2.
}
\]

Then

\[
A_+|n\rangle=|2n+1\rangle,
\qquad
A_-|n\rangle=|2n-1\rangle.
\]

Since the range of \(V_2\) lies in the even states, it never hits the \(S^*\) boundary at \(|1\rangle\), so both \(A_+\) and \(A_-\) are isometries.

The multiplicative source \(\Omega=|1\rangle\) satisfies

\[
A_+\Omega=|3\rangle,
\qquad
A_-\Omega=|1\rangle.
\]

Thus \(3\) is the first nontrivial positive-orientation affine excitation of the boot source under binary FUCC.

This is an interpretation, not a primality theorem.

---

## 2. SUCC is the cross-term of the two chiral branches

Use the affine braid

\[
V_2S=S^2V_2.
\]

Equivalently,

\[
V_2^*S^2V_2=S,
\qquad
V_2^*S^{*2}V_2=S^*.
\]

Then

\[
\boxed{
A_-^*A_+
=
V_2^*SSV_2
=
S,
}
\]

and

\[
\boxed{
A_+^*A_-
=
V_2^*S^*S^*V_2
=
S^*.
}
\]

So the additive carrier is literally the interference / overlap operator between the two affine orientations:

\[
\boxed{
S=A_-^*A_+.
}
\]

This is stronger than saying \(2x\pm1\) “look chiral.”

The two branches together reconstruct SUCC.

---

## 3. Chiral difference squares to the carry Laplacian

Define the first-order chiral difference operator

\[
\boxed{
C_2:=A_+-A_-.
}
\]

Because \(A_\pm^*A_\pm=I\),

\[
\begin{aligned}
C_2^*C_2
&=
A_+^*A_+
+
A_-^*A_-
-
A_+^*A_-
-
A_-^*A_+\\
&=
2I-S^*-S.
\end{aligned}
\]

Therefore

\[
\boxed{
C_2^*C_2
=
2I-S-S^*.
}
\]

But Round005 identified

\[
(S-I)^*(S-I)=2I-S-S^*
\]

as the basic SUCC/carry carré-du-champ.

Hence

\[
\boxed{
(A_+-A_-)^*(A_+-A_-)
=
(S-I)^*(S-I).
}
\]

So the Round005 positive carry energy admits a genuinely oriented/chiral first-order square root.

This means there are at least two distinct first-order factorizations of the same local carry energy:

\[
I-S
\]

and

\[
A_+-A_-.
\]

They have the same energy but retain different phase/orientation information before squaring.

That distinction may matter globally.

---

## 4. Exact chiral Dirac form

Double the Hilbert space:

\[
\mathcal K=\mathcal H\oplus\mathcal H.
\]

Define the grading

\[
\boxed{
\Gamma
=
\begin{pmatrix}
I&0\\
0&-I
\end{pmatrix}.
}
\]

Define the self-adjoint off-diagonal operator

\[
\boxed{
D_{\rm ch}
=
\begin{pmatrix}
0&C_2^*\\
C_2&0
\end{pmatrix}.
}
\]

Then

\[
\boxed{
\Gamma D_{\rm ch}+D_{\rm ch}\Gamma=0.
}
\]

So \(D_{\rm ch}\) is chiral in the standard graded-operator sense.

Its square is

\[
\boxed{
D_{\rm ch}^2
=
\begin{pmatrix}
C_2^*C_2&0\\
0&C_2C_2^*
\end{pmatrix}.
}
\]

The first diagonal block is exactly the carry/SUCC Laplacian

\[
2I-S-S^*.
\]

Thus chirality does not merely label the branches: it provides a Dirac-type first-order factorization of carry curvature.

---

## 5. Dirichlet character mod 4 reads the two affine orientations on odd parents

For odd \(n\),

\[
2n+1\equiv3\pmod4,
\qquad
2n-1\equiv1\pmod4.
\]

Hence

\[
\boxed{
\chi_4(2n-1)=+1,
\qquad
\chi_4(2n+1)=-1
}
\qquad(n\text{ odd}).
\]

So on the odd-parent sector, the real character modulo \(4\) is literally the orientation/chirality observable of the two affine branches.

More generally,

\[
\chi_4(2n+1)=(-1)^n,
\qquad
\chi_4(2n-1)=(-1)^{n+1}.
\]

This ties the earlier prime-graph character transport directly to the chiral binary branch geometry.

---

## 6. Why radix 2 is uniquely special for the nearest ±1 pair

For general \(m\ge2\), define

\[
A_{m,+}=SV_m,
\qquad
A_{m,-}=S^*V_m,
\]

so

\[
A_{m,\pm}|n\rangle=|mn\pm1\rangle
\]

where defined.

Their cross term is

\[
A_{m,-}^*A_{m,+}
=
V_m^*S^2V_m.
\]

Now

\[
V_m^*S^rV_m
\]

is nonzero only when the shift \(r\) matches the \(m\)-adic branch spacing, i.e. \(m\mid r\). For the nearest symmetric pair \(r=2\), this occurs nontrivially only at

\[
\boxed{m=2.}
\]

Indeed:

\[
\boxed{
V_2^*S^2V_2=S,
}
\]

whereas for \(m>2\),

\[
\boxed{
V_m^*S^2V_m=0.
}
\]

So binary dilation is uniquely the radix for which the nearest two-sided affine branches \(mn\pm1\) interfere to reproduce one SUCC step.

This is a precise mathematical reason that \(2\) behaves differently from higher radices in the chiral picture.

---

## 7. Connection to Round005 local carry filter

Round005 obtained the local prime factor in the form

\[
B_p
=
c_p
(I-U_{\rm depth})
(I-p^{-1/2}U_{\rm depth})^{-1}.
\]

The local positive energy only sees

\[
(I-U)^*(I-U).
\]

The chiral construction shows that the same discrete-Laplacian energy can arise from a first-order oriented branch difference before squaring.

This suggests a new question:

> Is the global source/carry completion sensitive to the first-order chiral factor even though the local squared energy is not?

Round004–005 repeatedly showed that quotienting or squaring too early can erase phase/noncommutative information.

So a proof-bearing global construction should compare:

1. the squared local carry energy;
2. the unsquared chiral branch operator.

If the second retains source-phase information lost by the first, chirality may be a genuine escape from a local-energy-only formulation.

No RH claim is made here.

---

## 8. Potential source-port use

The current source-port program seeks a completed finite passive operator before taking the limit.

A natural chiral candidate is to replace a scalar local difference channel by the doubled Dirac block

\[
D_{\rm ch}
=
\begin{pmatrix}
0&C_2^*\\
C_2&0
\end{pmatrix}
\]

or an arithmetic generalization in which the binary branch orientation is coupled to the prime-ray/source structure.

Desirable properties would be:

- self-adjointness;
- exact \(\mathbb Z_2\) grading;
- spectral symmetry \(\lambda\leftrightarrow-\lambda\);
- positive square;
- a source Weyl function whose completed response matches the arithmetic port.

The \(\pm\) symmetry is structurally compatible with the expected \(\pm\gamma\) symmetry of a Hilbert–Pólya operator, but this is only a shape constraint, not evidence that the Riemann zeros are the spectrum.

---

## 9. Immediate hostile tests

1. Replace \(m=2\) by \(m>2\). The nearest ±1 chiral cross term should vanish.
2. Remove one orientation. SUCC reconstruction \(A_-^*A_+=S\) must disappear.
3. Square before source coupling vs couple the first-order chiral branches before squaring.
4. Compare the resulting finite source-port transfer functions.
5. Mutate the affine offset \(1\to r\); determine when \(V_m^*S^{2r}V_m\) reproduces a nontrivial carrier step.
6. Test whether any generalized pair \(S^{\pm r}V_m\) with \(2r=m\) yields
   \[
   V_m^*S^{2r}V_m=S.
   \]
   For even \(m\), this gives a wider chiral pair around \(mn\); determine whether binary \(r=1\) remains uniquely primitive/minimal.

---

## 10. Current theorem package

The exact core is:

\[
\boxed{
A_+=SV_2,\qquad A_-=S^*V_2,
}
\]

\[
\boxed{
A_-^*A_+=S,
\qquad
A_+^*A_-=S^*,
}
\]

and

\[
\boxed{
(A_+-A_-)^*(A_+-A_-)
=
2I-S-S^*.
}
\]

Thus:

> **binary FUCC plus the two opposite SUCC orientations factor the carrier itself; their chiral difference factors the carry energy.**

That is the precise mathematical content of the original intuition.
