> **Provenance / causal limitation (2026-10-07):** The finite Gamma phase products are unitary *phase factors*, not unitary stochastic/Markov conductor refinements. In the two-state toy model, repeating the same 45° rotation twice gives occupation 1, whereas fresh Markov births require 1/2; smooth fixed-space unitary activation cannot have a first-order probability birth without an environmental/singular mechanism. The independent audit is archived at [CUBE_ATOM_CRITICAL_AUDIT_IMPORTED.md](../audits/2026-10-07/CUBE_ATOM_CRITICAL_AUDIT_IMPORTED.md). No Gamma rotation or inverse-Gamma finite truncation by itself proves Hardy invariance or RH. See [provenance](../audits/2026-10-07/RH_CLAIM_PROVENANCE_LEDGER.md).

# Gamma as a coherent cascade of finite rotations along the arithmetic height axis

**Date:** 2026-10-07  
**Status:** exact Gamma product/phase identities + a clearly separated geometric completion hypothesis. No RH assumption.  
**RH remains open.**

The user proposed:

1. the arithmetic cube has a distinguished diagonal/axis determined by the primes;
2. Gamma rotates relative to that axis;
3. at infinite slope the local rotation becomes a quarter-turn;
4. finite arithmetic data may be obtained from coherent finite truncations of inverse Gamma.

There is an exact mathematical core to all four statements, provided the truncation is taken in the **Weierstrass/Euler product**, not an arbitrary Taylor polynomial.

---

# 1. The arithmetic cube has a canonical prime-log normal vector

In prime-valuation coordinates,

\[
\alpha=(v_p(n))_{p\le N},
\]

the logarithmic height is

\[
\boxed{
h_N(\alpha)
=
\sum_{p\le N}\alpha_p\log p.
}
\]

Therefore the actualization hyperplane

\[
h_N(\alpha)=T
\]

has canonical normal vector

\[
\boxed{
\ell_N
=
(\log p)_{p\le N}.
}
\]

This is the user's prime-diagonal axis.

It is not chosen by coordinates after the fact.

It is the gradient of multiplicative logarithmic height.

The Mellin phase is

\[
\boxed{
n^{-it}
=
e^{-it h_N(\alpha)}
=
e^{-it\langle\ell_N,\alpha\rangle}.
}
\]

Thus the spectral parameter \(t\) is Fourier momentum along the prime-log diagonal direction.

Prime powers correspond to repeated motion along the same coordinate while remaining measured by the same global normal.

---

# 2. The prime vector becomes vertical relative to a fixed infinity scale

Adjoin one distinguished Archimedean/normal coordinate of fixed finite scale \(\kappa>0\).

Consider the vector

\[
\boxed{
v_N=(\ell_N,\kappa).
}
\]

Relative to the infinity axis, define

\[
\boxed{
\tan\alpha_N
=
\frac{\|\ell_N\|}{\kappa}.
}
\]

As \(N\to\infty\),

\[
\|\ell_N\|\to\infty
\]

simply because the number of positive prime-log coordinates tends to infinity.

Hence

\[
\boxed{
\alpha_N\to\frac\pi2.
}
\]

So the user's “prime vector develops infinite slope and tends to a \(90^\circ\) angle” is an exact finite-dimensional geometric statement.

**Important:** this angle \(\alpha_N\) has not yet been identified with the Gamma/Riemann--Siegel phase. They are distinct quantities until an attachment theorem is proved.

---

# 3. Gamma gives the exact phase rotation on the critical line

Put

\[
a=\frac14,
\qquad
y=\frac t2.
\]

Define the Riemann--Siegel phase

\[
\boxed{
\theta(t)
=
\Im\log\Gamma(a+iy)
-
y\log\pi.
}
\]

Then

\[
\boxed{
e^{2i\theta(t)}
=
\pi^{-it}
\frac{
\Gamma(a+iy)
}{
\Gamma(a-iy)
}.
}
\]

The right side has modulus one.

Thus Gamma defines an exact frequency-dependent rotation.

The classical Hardy function is

\[
\boxed{
Z(t)
=
e^{i\theta(t)}
\zeta\left(\frac12+it\right),
}
\]

which is real for real \(t\).

Therefore the **half Gamma phase** rotates the complex zeta boundary value onto the self-dual real line.

This is a literal rotation, not an analogy.

---

# 4. Reciprocal Gamma has a canonical nested finite product

The Weierstrass product is

\[
\boxed{
\frac1{\Gamma(z)}
=
ze^{\gamma z}
\prod_{m=1}^{\infty}
\left(
1+\frac zm
\right)
e^{-z/m}.
}
\]

Define the finite truncation

\[
\boxed{
W_M(z)
=
ze^{\gamma z}
\prod_{m=1}^{M}
\left(
1+\frac zm
\right)
e^{-z/m}.
}
\]

Then

\[
\boxed{
W_M(z)\to\frac1{\Gamma(z)}
}
\]

locally uniformly.

The truncations are nested:

\[
\boxed{
W_M(z)
=
W_{M-1}(z)
\left(
1+\frac zM
\right)
e^{-z/M}.
}
\]

So every new Gamma mode is attached by one explicit multiplicative update.

This is exactly the kind of coherent finite-to-infinite construction sought by the cubical tower program.

---

# 5. Every finite truncation has the correct first Gamma zeros

Since the exponential factors never vanish,

\[
W_M(z)
\]

has zeros exactly at

\[
\boxed{
z=0,-1,-2,\ldots,-M.
}
\]

Therefore with

\[
z=\frac s2,
\]

the corresponding zeros are

\[
\boxed{
s=0,-2,-4,\ldots,-2M.
}
\]

These are precisely the first \(M+1\) modes of the even inverse-SUCC/trivial-zero ladder.

Thus a finite reciprocal-Gamma product is an honest finite-dimensional truncation of the Archimedean spectral ladder.

---

# 6. Finite determinant realization

Let

\[
N_M
=
\operatorname{diag}(0,1,\ldots,M).
\]

Then

\[
\boxed{
\det(zI+N_M)
=
z(z+1)\cdots(z+M).
}
\]

Euler's finite approximation to reciprocal Gamma is

\[
\boxed{
G_M(z)
=
\frac{
\det(zI+N_M)
}{
M!\,M^z
}.
}
\]

And

\[
\boxed{
G_M(z)\to\frac1{\Gamma(z)}.
}
\]

For the even ladder

\[
D_M
=
2N_M
=
\operatorname{diag}(0,2,\ldots,2M),
\]

the finite determinant is

\[
\det(sI+D_M)
=
\prod_{m=0}^M(s+2m).
\]

Therefore inverse Gamma is literally the renormalized infinite-dimensional limit of characteristic determinants of finite Gamma ladders.

This is the correct finite-matrix version of “truncate inverse Gamma at coherent points.”

---

# 7. Finite Gamma phase is a product of elementary Cayley rotations

Let

\[
z=a+iy,
\qquad
a>0.
\]

For the Euler finite approximant,

\[
\frac{G_M(\bar z)}{G_M(z)}
=
M^{2iy}
\prod_{m=0}^M
\frac{m+a-iy}{m+a+iy}.
\]

At the zeta critical-line value

\[
a=\frac14,\qquad y=\frac t2,
\]

define

\[
\boxed{
R_M(t)
=
\pi^{-it}
\frac{G_M(\bar z)}{G_M(z)}.
}
\]

Then

\[
\boxed{
R_M(t)
=
e^{it\log(M/\pi)}
\prod_{m=0}^M
\frac{
m+\frac14-\frac{it}{2}
}{
m+\frac14+\frac{it}{2}
}.
}
\]

Every finite factor has modulus one, so

\[
\boxed{
|R_M(t)|=1
}
\]

for every real \(t\) and every finite \(M\).

Moreover,

\[
\boxed{
R_M(t)\to e^{2i\theta(t)}.
}
\]

So the Gamma phase has finite approximants which preserve unitarity **exactly at every truncation**.

---

# 8. Each Gamma mode is a plane rotation

Put

\[
\lambda_m=m+a.
\]

The elementary factor is

\[
\boxed{
C_m(y)
=
\frac{\lambda_m-iy}{\lambda_m+iy}.
}
\]

Write

\[
\phi_m(y)
=
-2\arctan\frac y{\lambda_m}.
\]

Then

\[
\boxed{
C_m(y)=e^{i\phi_m(y)}.
}
\]

As a real \(2\times2\) operator, multiplication by this scalar is the rotation

\[
\boxed{
\mathcal R_m(y)
=
\begin{pmatrix}
\cos\phi_m&-\sin\phi_m\\
\sin\phi_m&\cos\phi_m
\end{pmatrix}.
}
\]

Therefore the finite Gamma phase is a cascade of Givens/Cayley plane rotations plus an explicit scalar counterrotation from the renormalizing exponential.

This is a precise sense in which Gamma performs successive orthogonal rotations.

---

# 9. The exact \(90^\circ\) local limit

The full Cayley factor has angle

\[
\phi_m(y)
=
-2\arctan(y/\lambda_m).
\]

Its **half-phase** is

\[
\boxed{
\frac{\phi_m(y)}2
=
-\arctan\frac y{\lambda_m}.
}
\]

Therefore

\[
\boxed{
\lim_{y/\lambda_m\to\infty}
\frac{\phi_m(y)}2
=
-\frac\pi2.
}
\]

So the half Gamma rotation associated with one finite normal mode becomes a literal quarter-turn at infinite spectral slope.

The full factor tends to

\[
-1,
\]

a half-turn.

The distinction matters:

- Gamma ratio phase: \(180^\circ\) local limit;
- square-root/half phase used to rotate zeta into Hardy \(Z\): \(90^\circ\) local limit.

This is the exact mathematical core of the user's quarter-turn intuition.

---

# 10. Weierstrass phase update is even more naturally chronological

Using the nested Weierstrass truncation rather than Euler normalization, the \(M\)-th update in the Gamma ratio is

\[
\boxed{
U_M(y)
=
\frac{M+a-iy}{M+a+iy}
e^{2iy/M}.
}
\]

Again,

\[
|U_M(y)|=1.
\]

Thus the infinite Gamma phase is built by chronological multiplication of individually unitary rotation updates.

The exponential factor is the local renormalizing counterrotation required for convergence.

This structure strongly resembles the arithmetic program:

\[
\boxed{
\text{new support mode}
+
\text{local twist}
+
\text{renormalizing connection}.
}
\]

No identification with the arithmetic LCM update is claimed yet.

---

# 11. Why ordinary Taylor truncation is the wrong first probe

Because

\[
1/\Gamma(z)
\]

is entire, it also has a Maclaurin series.

But a generic degree-\(M\) Taylor truncation:

- does not retain the exact zeros \(0,-1,\ldots,-M\);
- does not give an exactly unit-modulus critical-line phase quotient;
- is not naturally nested by adding one spectral mode.

Therefore the product/determinant truncations are structurally superior for the present program.

They preserve exactly the properties we care about:

\[
\boxed{
\text{finite zero ladder},
}
\]

\[
\boxed{
\text{finite unitarity},
}
\]

\[
\boxed{
\text{mode-by-mode chronology}.
}
\]

---

# 12. Two independent filtrations must not be prematurely identified

There are currently two finite cutoffs.

### Arithmetic cutoff

\[
N
\]

controls:

- support cube dimension \(\pi(N)\);
- LCM depth;
- active conductor horizon.

### Gamma cutoff

\[
M
\]

controls:

- number of retained Archimedean modes;
- number of trivial-zero factors;
- accuracy of the Gamma phase/kernel.

There is not yet a theorem saying

\[
M=\pi(N),
\]

or

\[
M=\#\{p^k\le N\},
\]

or any other simple equality.

A correct completion theory must **derive** a coherence relation

\[
\boxed{
M=M(N,\text{resolution})
}
\]

from equality/error control of the completed finite operator.

Assuming one would be numerology.

---

# 13. Candidate diagonal-axis attachment

The arithmetic one-form sector has a canonical collective height direction.

At first Weil order define

\[
\boxed{
u_N(t)
=
\sum_{q=p^k\le N}
\sqrt{
\frac{\Lambda(q)}{\sqrt q}
}
q^{-it}
e_q.
}
\]

Its norm is

\[
\boxed{
\|u_N(t)\|^2
=
S_N
=
\sum_{q\le N}
\frac{\Lambda(q)}{\sqrt q},
}
\]

independent of \(t\).

Its phases

\[
q^{-it}
\]

are precisely Mellin phases along the logarithmic arithmetic height direction.

The new geometric hypothesis is:

> Gamma acts primarily on the collective arithmetic height line spanned by \(u_N(t)\), coupling it to the distinguished infinity-normal channel, while the orthogonal arithmetic support directions are handled by the cubical curvature complex.

This would turn the Gamma phase into a canonical rotation in the two-plane

\[
\boxed{
\operatorname{span}
\{
u_N(t),e_\infty
\}.
}
\]

This is **UNVERIFIED**.

---

# 14. What would prove the rotation interpretation

Construct finite unitary operators

\[
\boxed{
\mathcal U_{N,M}(t)
}
\]

on

\[
\text{arithmetic support complex}
\oplus
\text{Gamma normal modes}
\]

such that:

1. restriction to the Gamma chain has determinant/scattering phase \(R_M(t)\);
2. the arithmetic collective direction is the prime-log/Mellin direction \(u_N(t)\);
3. deleting the last Gamma mode gives the previous \(M-1\) truncation coherently;
4. truncating arithmetic support by
   \[
   d\mapsto\gcd(d,L_N)
   \]
   commutes with the construction;
5. the \(M,N\to\infty\) completed shorted Hamiltonian equals the Weil/Suzuki operator.

This would turn “Gamma rotates the cube into its orthogonal completion” into a theorem.

---

# 15. Immediate finite probe

The first calculation should avoid RH completely.

For modest \(N,M\):

1. form the arithmetic height vector \(u_N(t)\);
2. form the exact finite Gamma phase \(R_M(t)\);
3. realize each Cayley factor as a \(2\times2\) Givens rotation;
4. cascade those rotations along one explicit infinity-normal chain;
5. couple the chain only to the normalized height line
   \[
   \widehat u_N(t)=u_N(t)/\sqrt{S_N};
   \]
6. compute the induced Schur correction on the orthogonal arithmetic cube;
7. compare coefficient-by-coefficient with the known finite Gamma difference + scalar + pole terms.

Pass criterion:

\[
\boxed{
\text{exact completed Weil coefficients without zero data}.
}
\]

Anything less is geometric evidence only.

---

# 16. Current picture

There are now three exact layers:

\[
\boxed{
\text{arithmetic support axis}
=
(\log p)_p,
}
\]

\[
\boxed{
\text{spectral motion along that axis}
=
n^{-it},
}
\]

\[
\boxed{
\text{Gamma critical rotation}
=
\text{renormalized infinite cascade of Cayley plane rotations}.
}
\]

And two exact finite hierarchies:

\[
\boxed{
\text{LCM cubical truncation}
}
\]

and

\[
\boxed{
\text{inverse-Gamma product truncation}.
}
\]

The outstanding theorem is to show that these are the tangential and normal pieces of one compatible finite Hodge/Dirac system.
