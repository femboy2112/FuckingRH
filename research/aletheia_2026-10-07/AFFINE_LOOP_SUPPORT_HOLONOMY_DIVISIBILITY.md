# Affine closed loops have nested phase support and central holonomy

**Date:** 2026-10-07  
**Status:** exact theorem for primitive positive-slope rational-affine loops with nonempty integer support.  
**RH remains open.**

The loop program produced two apparently different invariants for the same closed word:

1. the integer-prefix support conductor \(M_\gamma\);
2. the primitive-matrix central holonomy \(\kappa(\gamma)\).

They are not competing definitions.

They are canonically nested:

\[
\boxed{
M_\gamma\mid\kappa(\gamma).
}
\]

So the arithmetic phase on which the word is executable is always a quotient/coarsening of the full multiplicative history hidden by projective closure.

---

# 1. Primitive affine word

Let

\[
f_j(x)
=
\frac{a_jx+b_j}{c_j},
\]

with

\[
a_j,c_j\in\mathbb N_{>0},
\qquad
b_j\in\mathbb Z,
\]

and

\[
\gcd(a_j,b_j,c_j)=1.
\]

Associate the primitive integer matrix

\[
\boxed{
M_j
=
\begin{pmatrix}
a_j&b_j\\
0&c_j
\end{pmatrix}.
}
\]

Assume the visible rational composition closes identically:

\[
\boxed{
f_r\circ\cdots\circ f_1
=
\operatorname{id}.
}
\]

---

# 2. Central holonomy is the total multiplicative numerator/denominator flux

Since upper-triangular matrices multiply diagonals multiplicatively,

\[
M_r\cdots M_1
\]

has diagonal entries

\[
\prod_{j=1}^r a_j
\]

and

\[
\prod_{j=1}^r c_j.
\]

Visible closure to the identity means the matrix product is a scalar multiple of \(I\):

\[
M_r\cdots M_1
=
\kappa(\gamma)I.
\]

Therefore:

\[
\boxed{
\kappa(\gamma)
=
\prod_{j=1}^ra_j
=
\prod_{j=1}^rc_j.
}
\]

Thus the central holonomy is not an arbitrary content gcd.

It is exactly the total multiplicative flux through either diagonal channel.

For the user's word,

\[
(a_1,a_2,a_3)=(4,3,2),
\]

\[
(c_1,c_2,c_3)=(1,8,3),
\]

so

\[
\boxed{
4\cdot3\cdot2
=
1\cdot8\cdot3
=
24.
}
\]

---

# 3. Prefix denominators divide the total holonomy

Let the \(j\)-th prefix map be

\[
F_j=f_j\circ\cdots\circ f_1.
\]

Before primitive reduction, its matrix is

\[
A_j=M_j\cdots M_1.
\]

Its lower-right entry is

\[
\boxed{
C_j=\prod_{i=1}^j c_i.
}
\]

After dividing the integer entries of \(A_j\) by their common content, write the primitive prefix as

\[
F_j(x)
=
\frac{
u_jx+v_j
}{
q_j
}.
\]

Then necessarily

\[
\boxed{
q_j\mid C_j.
}
\]

But

\[
C_j\mid
\prod_{i=1}^rc_i
=
\kappa(\gamma).
\]

Hence

\[
\boxed{
q_j\mid\kappa(\gamma)
}
\]

for every prefix.

---

# 4. Integrality support modulus divides the central holonomy

The integer-prefix condition at stage \(j\) is

\[
u_jx+v_j\equiv0\pmod{q_j}.
\]

When the support is nonempty, it reduces to one residue condition modulo some

\[
m_j\mid q_j.
\]

The support conductor of the whole path is

\[
\boxed{
M_\gamma
=
\operatorname{lcm}(m_1,\ldots,m_r).
}
\]

Since every

\[
m_j\mid q_j\mid\kappa(\gamma),
\]

their least common multiple also divides \(\kappa(\gamma)\):

\[
\boxed{
M_\gamma\mid\kappa(\gamma).
}
\]

This proves the theorem.

---

# 5. Meaning of the two invariants

The support conductor

\[
M_\gamma
\]

answers:

> What modular information about the starting state is required to make every intermediate step an integer?

The central holonomy

\[
\kappa(\gamma)
\]

answers:

> How much primitive multiplicative numerator/denominator history was accumulated and then erased when the projective affine word closed?

Thus:

\[
\boxed{
M_\gamma
=
\text{phase/admissibility support},
}
\]

\[
\boxed{
\kappa(\gamma)
=
\text{history/provenance holonomy}.
}
\]

The divisibility theorem says the phase support is always contained in the full hidden multiplicative history.

---

# 6. Three nested scales

Combine the theorem with the LCM support-birth map

\[
\beta(n)
=
\max_{p^k\parallel n}p^k.
\]

Since

\[
M_\gamma\mid\kappa(\gamma),
\]

we have

\[
\boxed{
\beta(M_\gamma)
\le
\beta(\kappa(\gamma)).
}
\]

And trivially

\[
\beta(\kappa(\gamma))
\le
\kappa(\gamma).
\]

Therefore every loop carries a canonical three-stage hierarchy:

\[
\boxed{
\beta(M_\gamma)
\le
\beta(\kappa(\gamma))
\le
\kappa(\gamma).
}
\]

More concretely:

1. **phase-support birth**
   \[
   \beta(M_\gamma);
   \]

2. **holonomy harmonic birth**
   \[
   \beta(\kappa(\gamma));
   \]

3. **visible holonomy actualization**
   \[
   \kappa(\gamma).
   \]

For the supplied loop:

\[
M_\gamma=2,
\]

\[
\kappa(\gamma)=24,
\]

so

\[
\boxed{
2
<
8
<
24.
}
\]

That is a mathematically clean version of the pre-actualization hierarchy.

---

# 7. A useful defect ratio

Define the hidden-history quotient

\[
\boxed{
D_\gamma
=
\frac{
\kappa(\gamma)
}{
M_\gamma
}
\in\mathbb N.
}
\]

This measures multiplicative history not required merely to specify the executable phase.

For the user's loop,

\[
\boxed{
D_\gamma=12.
}
\]

A loop with

\[
D_\gamma=1
\]

has phase support as fine as its central history.

A loop with large \(D_\gamma\) closes on a relatively coarse arithmetic phase while carrying much richer hidden multiplicative provenance.

This is a useful census statistic.

It is not yet an RH energy.

---

# 8. Consequence for loop census

The existing closed-word census should record at least

\[
\boxed{
(M_\gamma,\kappa(\gamma),D_\gamma)
}
\]

in addition to:

- support filtration;
- conductor birth history;
- residues;
- exact-conductor spectra.

Two words can share terminal support

\[
M_\gamma
\]

while having different

\[
\kappa(\gamma).
\]

Conversely, two words can share the same central holonomy while paying their integrality constraints at different prefixes.

So the combined invariant

\[
\boxed{
\text{support filtration}
+
\text{central holonomy}
}
\]

retains strictly more provenance than either alone.

That is the preferred loop descriptor for the next chronological curvature experiments.
