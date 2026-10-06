# Negative-SUCC jet duality: reflection, parity carrier, and positive-side zeta data

**Date:** 2026-10-06  
**Status:** exact classical identities reorganized as SUCC/FUCC path geometry. **RH remains open.**

## 0. Central result

The asymmetric functional equation

\[
\zeta(s)
=
2^s\pi^{s-1}
\sin\frac{\pi s}{2}\,
\Gamma(1-s)\,
\zeta(1-s)
\]

does more than relate a negative point to a positive point.

Let

\[
R(s)=1-s.
\]

Then

\[
\boxed{R T_a R=T_{-a}}
\]

for translations \(T_a(s)=s+a\). In particular,

\[
\boxed{R T_{-1}R=T_{+1}.}
\]

So the functional-equation reflection turns **inverse SUCC on the left** into **forward SUCC on the right**.

At integer points,

\[
-n \xleftrightarrow{R} n+1.
\]

Thus the entire negative inverse-SUCC ray

\[
-1,-2,-3,-4,\ldots
\]

is reflected into the forward positive ray

\[
2,3,4,5,\ldots.
\]

The sine/Gamma factors determine which **jet order** is needed to transport the datum.

---

## 1. Binary carrier split of the inverse-SUCC ray

The carrier factor

\[
\sin\frac{\pi s}{2}
=
\frac{e^{i\pi s/2}-e^{-i\pi s/2}}{2i}
\]

splits the integer lattice by parity.

On the negative side:

\[
\{-1,-3,-5,\ldots\}
\]

are non-nodal carrier sites, while

\[
\{-2,-4,-6,\ldots\}
\]

are sine nodes.

However the sine has nodes at **all** even integers. The reason only the negative even nodes become zeta zeros is directional:

- at \(s=-2m\), \(\Gamma(1-s)=\Gamma(1+2m)\) is finite, so the sine zero survives;
- at \(s=+2m\), \(\Gamma(1-s)=\Gamma(1-2m)\) has a pole that cancels the sine zero;
- at \(s=0\), the sine zero is canceled by the reflected zeta pole \(\zeta(1-s)\).

Thus the trivial-zero pattern is not parity alone. It is

\[
\boxed{
\text{bilateral parity carrier}
+
\text{orientation of the Gamma/reflection channel}.
}
\]

---

## 2. Negative odd sites carry positive even zeta values

Take

\[
s=1-2m,
\qquad m\ge1.
\]

Then \(1-s=2m\), and the sine factor is nonzero.

The functional equation gives the usual Bernoulli special value

\[
\boxed{
\zeta(1-2m)
=
-\frac{B_{2m}}{2m},
}
\]

equivalently a known nonzero scalar multiple of

\[
\boxed{\zeta(2m).}
\]

So the negative-odd branch stores the **positive-even zeta values in its zeroth-order value channel**.

Examples:

\[
\zeta(-1)=-\frac1{12}
\quad\leftrightarrow\quad
\zeta(2)=\frac{\pi^2}{6},
\]

\[
\zeta(-3)=\frac1{120}
\quad\leftrightarrow\quad
\zeta(4)=\frac{\pi^4}{90}.
\]

---

## 3. Negative even sites carry positive odd zeta values in the FIRST JET

Now take a trivial-zero point

\[
s_0=-2m,
\qquad m\ge1.
\]

The sine vanishes simply:

\[
\sin\frac{\pi s}{2}
=
(-1)^m\frac{\pi}{2}(s+2m)
+O((s+2m)^3).
\]

All other factors in the functional equation are finite and nonzero at \(s_0\).

Therefore the first derivative is

\[
\boxed{
\zeta'(-2m)
=
(-1)^m
\frac{(2m)!}{2(2\pi)^{2m}}
\zeta(2m+1).
}
\]

So the datum at the reflected positive odd point is not lost when the negative-side value vanishes.

It moves up one jet order:

\[
\boxed{
\zeta(-2m)=0,
\qquad
\zeta'(-2m)\propto \zeta(2m+1).
}
\]

Examples:

\[
\zeta'(-2)
=
-\frac{\zeta(3)}{4\pi^2},
\]

\[
\zeta'(-4)
=
\frac{3\zeta(5)}{4\pi^4}.
\]

This is the exact mathematical content of the statement:

> **A trivial zero is a carrier node where the positive-side signal survives in the slope rather than the value.**

---

## 4. Staggered jet encoding of the entire positive integer zeta sequence

The reflection map gives

\[
-1\leftrightarrow2,
\quad
-2\leftrightarrow3,
\quad
-3\leftrightarrow4,
\quad
-4\leftrightarrow5,\ldots
\]

and the parity carrier alternates the required observation channel:

\[
\boxed{
\begin{array}{c|c|c}
\text{left site} & \text{right site} & \text{left datum encoding the right}\\
\hline
-(2m-1) & 2m & \zeta(1-2m)\\
-2m & 2m+1 & \zeta'(-2m)
\end{array}
}
\]

Hence **every positive integer value**

\[
\zeta(2),\zeta(3),\zeta(4),\zeta(5),\ldots
\]

is encoded on the negative inverse-SUCC lattice by an alternating sequence of

- zeroth-order values at negative odd sites;
- first-order jets at negative even sites.

This is a canonical **staggered jet lattice**.

---

## 5. Full germs, not only values, are transported

Write

\[
A(s)
=
2^s\pi^{s-1}\Gamma(1-s).
\]

Near a trivial zero \(s_0=-2m\),

\[
\frac{\zeta(s)}{s-s_0}
=
\left[
\frac{\sin(\pi s/2)}{s-s_0}
\right]
A(s)\zeta(1-s).
\]

The bracketed factor and \(A(s)\) are analytic and nonzero at \(s_0\).

Therefore the full Taylor germ of

\[
\boxed{
\frac{\zeta(s)}{s+2m}
}
\]

near \(-2m\) is related by an invertible analytic multiplier and reflection to the full Taylor germ of

\[
\boxed{
\zeta(w)
}
\]

near

\[
w=1+2m.
\]

So the trivial zero is not information destruction. It is a **change of jet gauge**.

The value channel vanishes, but the desingularized jet retains the entire reflected positive-side germ.

---

## 6. The sine carrier itself is a bilateral even-SUCC determinant

Euler's product gives

\[
\boxed{
\frac{\sin(\pi s/2)}{\pi s/2}
=
\prod_{n\ge1}
\left(
1-\frac{s^2}{4n^2}
\right).
}
\]

Thus the carrier zeros

\[
s=\pm2,\pm4,\pm6,\ldots
\]

are the spectrum of a **bilateral even-SUCC lattice**.

The asymmetric functional equation then orients this bilateral carrier:

- the positive-even nodes are canceled by Gamma poles;
- the negative-even nodes survive as trivial zeros.

So the trivial-zero lattice is naturally a **chiral/oriented half** of a bilateral carrier spectrum.

This is more precise than saying "the trivial zeros are \(2\times\) inverse SUCC."

---

## 7. A two-channel negative-side signal

The preceding identities suggest a natural two-component observable on the negative integer ray:

\[
\Psi_m
=
\begin{pmatrix}
\zeta(1-2m)\\[1mm]
\zeta'(-2m)
\end{pmatrix}.
\]

The first channel carries the reflected positive-even data.

The second carries the reflected positive-odd data.

So the inverse-SUCC ray is a staggered/chiral sampler of the positive-side zeta function:

\[
\boxed{
\text{negative odd site}
\to
\text{value channel},
}
\]

\[
\boxed{
\text{negative even site}
\to
\text{derivative channel}.
}
\]

A genuine first-order operator model should ideally explain this alternation rather than encode it by hand.

---

## 8. Euler–Mascheroni survives into the residual global product

The Archimedean normalization constant does not disappear after the trivial-mode cancellation.

The genus-one Hadamard product can be written

\[
\boxed{
\xi(s)
=
\frac12 e^{Bs}
\prod_\rho
\left(1-\frac{s}{\rho}\right)
e^{s/\rho},
}
\]

where the product runs over the nontrivial zeros and

\[
\boxed{
B
=
\log2+\frac12\log\pi-1-\frac{\gamma}{2}.
}
\]

Equivalently,

\[
\boxed{
B=\frac{\xi'(0)}{\xi(0)}.
}
\]

So Euler–Mascheroni — the discrete/continuous SUCC normalization defect from the harmonic/Gamma control problem — survives completion as part of the **linear renormalization constant of the entire product over the nontrivial zeros**.

This is a direct exact coupling between the local Archimedean normalization and the residual global spectrum.

---

## 9. Interpretation

The negative side is not simply "thrown away."

Under functional-equation reflection:

\[
\boxed{
\text{inverse SUCC on the left}
\longleftrightarrow
\text{forward SUCC on the right}.
}
\]

The bilateral parity carrier then decides whether the reflected datum appears as:

- a value;
- or a higher jet because the value channel sits on a harmonic node.

The trivial zeros are precisely the first-order node sites.

So the sharpened path-history picture is:

\[
\boxed{
\text{inverse SUCC path}
\to
\text{carrier parity}
\to
\text{staggered jets}
\overset{R:s\mapsto1-s}{\longleftrightarrow}
\text{forward positive zeta data}.
}
\]

The negative lattice is therefore a nontrivial local encoding of the positive side, not merely a cemetery of trivial zeros.

---

## 10. What this does NOT prove

The staggered jet duality concerns integer special values and local germs.

It does not constrain the off-axis nontrivial zero set.

Multiplying the completed function by a suitable even real entire factor can preserve the local trivial-zero cancellation and reflection symmetry while inserting off-axis zeros.

Thus this structure is load-bearing completion data, but RH still requires an independent positivity/self-adjointness/global constraint.

## House slogan

\[
\boxed{
\text{Reflection turns inverse SUCC into forward SUCC.}
}
\]

\[
\boxed{
\text{The carrier nodes don't erase the signal; they push it into the jet.}
}
\]

\[
\boxed{
\text{Negative evens store the mysterious positive odd zeta values in their slopes.}
}
\]
