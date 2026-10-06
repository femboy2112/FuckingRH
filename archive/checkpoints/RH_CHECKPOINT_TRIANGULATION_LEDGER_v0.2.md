# RH Checkpoint Triangulation Ledger

**Proof ledger v0.2 — 3 September 2026**

## Executive result

This document records six adversarial triangulation rounds around the
LCM/checkpoint approach to the Riemann hypothesis.  It does **not** prove RH.
It does make four pieces of proof progress and kills three tempting proof
shortcuts.

The main progress is:

1. the comparison-transform edge is no longer open: Connes--Consani--
   Moscovici already prove that the explicit prolate/Poisson candidate tends
   to \(\Xi\) on every closed substrip of the critical strip;
2. a parity-resolved bordered-Schur theorem certifies a simple even global
   ground state without requiring the candidate Rayleigh quotient to lie
   below the entire odd spectrum;
3. candidate-specific endpoint localization proves that the whole newest
   prime-power range
   \[
   n\ge \lambda A\sqrt{\log\lambda},
   \qquad A>\frac1{\sqrt{2\pi}},
   \]
   is \(o(1)\) after absolute summation at the quadratic-form level;
4. a restricted-log comparison operator gives a continuum Ritz certificate
   for parity, a one-sided gap, the absence of low spectral pollution, and an
   exact residual.

The decisive negative results are:

- no fixed algebraic boundary-birth regularity can make the newborn
  half-window absolutely summable;
- low Fourier modes see coherent \(\sqrt X/\log X\) boundary mass rather than
  prime cancellation;
- the truncated prime shifts are not compact, so their high-mode norm tails
  do not disappear.

After the six rounds, the remaining route is sharply localized:

\[
\boxed{
\text{prove weighted candidate-to-ground locking, with a quantitative gap,
for the old/middle prime shells.}
}
\]

That statement is strictly a route-specific spectral estimate.  It is not a
renaming of RH, although sufficiently uniform uncentered prime cancellation
at frequency zero would be RH-equivalent and is explicitly fenced off below.

## 1. Truth labels and checkpoint conventions

The labels in this ledger mean:

| Label | Meaning |
|---|---|
| **PROVED HERE** | A complete proof is included. |
| **PROVED IN SOURCE** | A cited primary source proves the statement. |
| **DERIVED FROM SOURCE** | The source supplies named estimates; the deduction is written here. |
| **CORROBORATED** | Finite computation checked signs/constants but is not the proof. |
| **REFUTED** | An exact counterexample or asymptotic no-go is supplied. |
| **CONDITIONAL** | The implication is proved, but named quantitative inputs remain open. |
| **DARK** | We do not know whether the proposed mechanism is true or useful. |

Write

\[
M_N=\operatorname{lcm}(1,\ldots,N),
\qquad
\log\frac{M_N}{M_{N-1}}=\Lambda(N).
\]

An order-\(N\) cyclotomic checkpoint is a prime \(q\equiv1\pmod{M_N}\).
Such a carrier realizes all finite cyclic periods through \(N\), but it does
not manufacture the Archimedean phase \(\log n\).  The RH-facing analytic
checkpoint is instead

\[
X=e^L=\lambda^2,
\qquad
I_L=(-L/2,L/2)=(-\log\lambda,\log\lambda).
\]

The exact arithmetic block on \(L^2(I_L)\), with functions zero-extended, is

\[
\mathcal P_L
=
\sum_{1<n<X}\frac{\Lambda(n)}{\sqrt n}H_{\log n},
\qquad
H_y=T_y+T_y^*.
\]

The LCM filtration therefore supplies the von Mangoldt comb exactly.  The
carrier-prime phase grid remains an optional finite quantizer; it is not used
as a source of spectral positivity in the arguments below.

---

## Round 1 — object identity, normalization, and closure

### 2. The canonical transport firewall

Let \(L=2\log\lambda\), let \(f\in L^2(0,L)\), and define

\[
(\kappa_\lambda f)(u)=f(\log(\lambda u)),
\qquad \lambda^{-1}\le u\le\lambda.
\]

Then \(\kappa_\lambda\) is an isometry from \(L^2(0,L,dx)\) to
\(L^2([\lambda^{-1},\lambda],d^*u)\), and with

\[
\mathcal M g(z)=\int_0^\infty g(u)u^{-iz}\,d^*u
\]

one has exactly

\[
\boxed{
\mathcal M(\kappa_\lambda f)(z)
=\lambda^{iz}\int_0^L f(x)e^{-izx}\,dx.
}
\]

This is the declared cross-checkpoint transport.  An arbitrary isometry is
not an acceptable substitute: it need not preserve the entire function whose
zeros are controlled.

### 3. Structural finite real-rootedness **[PROVED IN SOURCE]**

Let \(W=QW_\lambda^N\) be the exact finite Weil matrix in the canonical
Fourier basis used by Connes--van Suijlekom.  Suppose its minimum eigenvalue
\(\epsilon\) is simple and its ground vector \(\phi\) is even.  Then

\[
Q=W-\epsilon I
\]

is positive semidefinite, remains in the required divided-difference class,
and has the one-dimensional even kernel \(\mathbf C\phi\).  Theorem 5.6 of
[Connes--van Suijlekom](https://arxiv.org/html/2511.23257v1) therefore implies
that the Fourier transform of the zero-extended trigonometric polynomial
defined by \(\phi\) has only real zeros.  The canonical map \(\kappa_\lambda\)
changes that transform only by centering and a zero-free exponential.

The Weil matrix's real-symmetric divided-difference structure is supplied by
CCM Lemma 5.1 and equation (5.2); CvS Theorem 5.6(ii) supplies the real-zero
conclusion.  CCM Theorem 5.10(iii) is a direct finite-route formulation of
the same implication.

This is structural, not generic spectral theory.

#### Negative control

In the Fourier basis \(U_k(x)=e^{2\pi ikx}\), \(k=-1,0,1\), put

\[
\xi=\frac1{\sqrt3}(-1,1,-1),
\qquad
W=I-|\xi\rangle\langle\xi|
=
\begin{pmatrix}
2/3&1/3&-1/3\\
1/3&2/3&1/3\\
-1/3&1/3&2/3
\end{pmatrix}.
\]

The matrix is Hermitian, reversal invariant, and has the unique even ground
\(\xi\).  After centering to \([-1/2,1/2]\), its ground function is

\[
f(t)=\frac{1+2\cos(2\pi t)}{\sqrt3}.
\]

Direct integration gives the entire function

\[
F(z)
=-
\frac{2\sin(z/2)(z^2+4\pi^2)}
{\sqrt3\,z(z^2-4\pi^2)},
\]

where the apparent poles are removable.  It has the nonreal zeros

\[
F(2\pi i)=F(-2\pi i)=0.
\]

The mutation fails the divided-difference identities: its three
off-diagonal entries are \((1/3,1/3,-1/3)\), whereas at \(N=1\) the required
class forces them to coincide.  Hence

\[
\boxed{
\text{simple}+\text{even}+\text{Hermitian}
\not\Rightarrow\text{real-rooted ground transform}.}
\]

### 4. The candidate-transform edge is closed **[SOURCE THEOREM + DERIVED COROLLARIES]**

Let \(k_\lambda\) be the explicit prolate/Poisson candidate of
[Connes--Consani--Moscovici](https://arxiv.org/html/2511.22755v1).
Their Lemma 7.3 proves

\[
\boxed{
\mathcal M k_\lambda\longrightarrow\Xi
}
\]

uniformly on every closed substrip \(|\Im z|\le\alpha<1/2\).
Consequently, comparison-transform convergence must not remain on the OPEN
ledger.  CCM Section 8 leaves the simple-even ground-state problem and
quantitative comparison of that ground state with a scalar multiple of
\(k_\lambda\).

There is a free exact parity repair.  Let

\[
(Jg)(u)=g(u^{-1}),
\qquad
k_\lambda^+=\frac12(k_\lambda+Jk_\lambda).
\]

Then

\[
\mathcal M(Jg)(z)=\mathcal Mg(-z).
\]

Since \(\Xi\) is even, CCM Lemma 7.3 immediately gives

\[
\boxed{\mathcal M k_\lambda^+\longrightarrow\Xi}
\]

uniformly on the same closed substrips.  Moreover \(J\) is unitary and the
limiting \(k\) is \(J\)-invariant, so
\(\|k_\lambda^+-k\|_2\le\|k_\lambda-k\|_2\).

The following is **derived here from their estimates**, rather than stated
as a separate source theorem: after zero extension,

\[
\|k_\lambda-k\|_{L^2(d^*u)}\to0.
\]

Indeed, on \([\lambda^{-1},\lambda]\),

\[
|k_\lambda(u)-k(u)|
\le \lambda\delta(\lambda)u^{-1/2},
\qquad \delta(\lambda)=O(\lambda^{-2}),
\]

with the omitted Gaussian tail
\(u^{1/2}\sum_{n>\lambda/u}|h(nu)|\) absorbed into the same order,

so the squared interior error is bounded by

\[
\lambda^2\delta(\lambda)^2
\int_{1/\lambda}^{\lambda}u^{-2}\,du
=O(\lambda^{-1}),
\]

while the fixed \(k\)-tail tends to zero.

### 5. Two scalars that must not be conflated

Let \(\Gamma f(x)=f(L-x)\), and choose the canonical Fourier projection
\(P_N\) symmetrically so that it commutes with \(\Gamma\).  The function
\(\kappa_\lambda^{-1}k_\lambda^+\) is exactly even.  Define

\[
p_{\lambda,N}
=
\frac{P_N\kappa_\lambda^{-1}k_\lambda^+}
{\|P_N\kappa_\lambda^{-1}k_\lambda^+\|_2}.
\]

Here and below the denominator is assumed nonzero; any schedule satisfying
the weighted projection condition in Section 6 has this property eventually.

The candidate-matching amplitude is

\[
c_{\lambda,N}
=\|P_N\kappa_\lambda^{-1}k_\lambda^+\|_2.
\]

It is bounded above by \(\|k_\lambda^+\|_2=O(1)\), and it is precisely the
scale for which

\[
c_{\lambda,N}\kappa_\lambda p_{\lambda,N}
=\kappa_\lambda P_N\kappa_\lambda^{-1}k_\lambda^+.
\]

The weighted projection error in Section 6 now pays only for finite-mode
truncation.  Evenization preserves transform convergence exactly; it is not
an unquantified approximation.

Scaling a real-rooted transform by this positive constant preserves its
zeros and makes the comparison to \(k_\lambda^+\) quantitative.

The CCM determinant normalization is different.  For a unit ground vector
\(\phi\), it uses \(\xi=\phi/\delta_N(\phi)\) and

\[
\det_{\mathrm{reg}}(D-z)
=-i\lambda^{-iz}\delta_N(\phi)^{-1}\widehat\phi(z).
\]

Neither \(\delta_N(\phi)^{-1}\) nor the \(z\)-dependent zero-free factor
\(\lambda^{-iz}\) is controlled by the candidate norm.  Therefore:

- the candidate-scaled ground transforms may be used for a Rouché/Hurwitz
  zero argument;
- convergence of the canonically normalized determinants is a different,
  stronger statement and is not claimed here.

### 6. Corrected closure theorem **[CONDITIONAL]**

Put

\[
C_\alpha(X)^2
=2\log X+\frac{X^\alpha-X^{-\alpha}}\alpha,
\qquad X=\lambda^2.
\]

For \(\lambda_j\to\infty\), let \(W_j=QW_{\lambda_j}^{N_j}\) be the exact
finite Weil matrices, let \(p_j=p_{\lambda_j,N_j}\), and let \(\phi_j\) be
their phase-aligned unit ground vectors.  All additive and multiplicative
functions are zero-extended outside their declared intervals.  Define the
two entire functions

\[
F_j(z)=\mathcal M(c_j\kappa_{\lambda_j}\phi_j)(z),
\qquad
G_j(z)=\mathcal M k_{\lambda_j}^+(z).
\]

Assume:

1. a structural certificate proves that each \(\phi_j\) is simple and even;
2. a proved estimate \(d_j\) satisfies \(\|p_j-\phi_j\|_2\le d_j\);
3. for every \(0<\alpha<1/2\),
   \[
   c_jC_\alpha(X_j)d_j+\tau_{j,\alpha}\to0,
   \]
   where
   \[
   \tau_{j,\alpha}
   =\|c_j\kappa_{\lambda_j}p_j-k_{\lambda_j}^+\|_{L^1(w_\alpha d^*u)},
   \qquad w_\alpha(u)=u^\alpha+u^{-\alpha}.
   \]

Then RH holds.

#### Proof

Cauchy--Schwarz on \([X_j^{-1/2},X_j^{1/2}]\) gives

\[
\|c_j\kappa_{\lambda_j}(\phi_j-p_j)\|_{1,\alpha}
\le c_jC_\alpha(X_j)d_j.
\]

Thus the candidate-scaled ground transforms converge to the transforms of
\(k_{\lambda_j}^+\) uniformly on each closed substrip.  Section 4 supplies
convergence of the latter to \(\Xi\).  Section 3 supplies real-rootedness of
every finite ground transform.  Hurwitz, or Rouché on a small disk around a
hypothetical nonreal zero of \(\Xi\), gives a contradiction. \(\square\)

Since \(C_\alpha(\lambda^2)\asymp\lambda^\alpha/\sqrt\alpha\), ordinary
\(L^2\) convergence is not enough.  The ground-locking rate must beat every
\(\lambda^{-\alpha}\), \(\alpha<1/2\), after Galerkin error is included.

### 6A. Form-core lift of finite real-rootedness **[PROVED HERE FROM STRUCTURAL INPUTS]**

Let \(q\) be a closed lower-bounded reflection-invariant form on
\(L^2(0,L)\), with compact-resolvent associated operator \(A\).  Let
\(E_N\) be nested finite-dimensional reflection-invariant subspaces forming
a form core.  Assume every exact restricted matrix belongs to the
divided-difference class required by CvS Theorem 5.6.

Suppose \(A\) has a simple even ground state \(\phi\), with eigenvalue
\(\lambda\), and

\[
\sigma(A)\setminus\{\lambda\}\subset[\lambda+\delta,\infty)
\qquad(\delta>0).
\]

Then, for all sufficiently large \(N\), the restricted matrix has a simple
even ground vector \(\phi_N\), one may phase-align it so that
\(\phi_N\to\phi\) in \(L^2\), and the Fourier transform of the zero-extended
\(\phi\) has only real zeros.

#### Proof

Let \(\lambda_N\) be the lowest restricted Rayleigh value.  Min--max gives
\(\lambda_N\ge\lambda\).  The form-core property supplies unit
\(\eta_N\in E_N\) converging to \(\phi\) in form norm, so
\(\lambda_N\le q[\eta_N]\to\lambda\).  The second restricted eigenvalue is
at least the continuum second eigenvalue, hence at least
\(\lambda+\delta\).  Thus the restricted ground is simple eventually.

Write its unit vector as \(\phi_N=a_N\phi+h_N\), with
\(h_N\perp\phi\).  The spectral gap gives

\[
\lambda_N=q[\phi_N]
\ge\lambda+\delta\|h_N\|^2,
\]

so \(\|h_N\|\to0\).  A simple finite ground has definite parity; it cannot be
odd for large \(N\), because every odd vector is orthogonal to the even
\(\phi\).  Hence it is even.

For large \(N\), set

\[
Q_N=W_N-\lambda_NI\succeq0.
\]

The scalar shift preserves the divided-difference class and gives
\(\ker Q_N=\mathbf C\phi_N\).  CvS Theorem 5.6 now makes every finite ground
transform real-rooted.  On the
fixed interval, \(L^2\)-convergence implies \(L^1\)-convergence, hence local
uniform convergence of the zero-extended Fourier transforms.  A nonreal zero
of the limiting transform would, by Rouché on a small disk disjoint from the
real axis, force nonreal zeros of the finite transforms.  Contradiction.
\(\square\)

For the CCM continuum Weil form, the needed finite matrix class comes from
CCM Lemma 5.1/equation (5.2), and the form-core input is supplied by their
Proposition 3.4; compact resolvent/discreteness is their Theorem 3.6.  This
lemma extracts the form-core mechanism already visible in the proof of CvS
Theorem 6.1.  No literature-originality claim is attached to the extraction,
and it does not assume that a form core is automatically an operator core.

---

## Round 2 — parity-resolved Schur and Feshbach machinery

### 7. Sector-decoupled bordered-Schur theorem **[PROVED HERE; CLASSICAL INGREDIENTS, ROUTE-SPECIFIC SYNTHESIS]**

Either let \(A\) be a finite-dimensional Hermitian operator, or let \(A\) be
a lower-semibounded self-adjoint operator whose closed quadratic form is
reduced by an involution \(\Gamma\).  Thus

\[
\mathcal H=\mathcal H_+\oplus\mathcal H_-.
\]

Assume \(k\in\operatorname{Dom}(A)\cap\mathcal H_+\) is unit, and put

\[
\rho=\langle k,Ak\rangle,
\qquad
r=(A-\rho)k\in\mathcal H_+\cap k^\perp.
\]

In the continuum case, let \(D\) be the self-adjoint operator associated with the
restriction of the closed form of \(A_+\) to
\(\mathcal Q(A_+)\cap k^\perp\); all block identities are then understood in
quadratic-form sense.  Relative to
\(\mathbf Ck\oplus(\mathcal H_+\cap k^\perp)\), write

\[
A_+
=
\begin{pmatrix}
\rho&r^*\\
r&D
\end{pmatrix},
\qquad
\epsilon=\|r\|.
\]

Assume

\[
D\succeq\delta I,
\qquad
A_-\succeq\omega I,
\qquad
\rho<\delta.
\]

Choose \(\theta\le\omega\) with \(\theta<\delta\), and put

\[
\mathfrak s(\theta)
=\rho-\theta-
\langle r,(D-\theta)^{-1}r\rangle.
\]

If

\[
\boxed{\mathfrak s(\theta)<0,}
\]

then \(A\) has a unique simple even ground eigenvalue \(\lambda<\theta\),
and

\[
\sigma(A)\setminus\{\lambda\}
\subseteq[\min(\delta,\omega),\infty).
\]

Set

\[
g=\delta-\rho,
\qquad
R=\sqrt{g^2+4\epsilon^2},
\qquad
E=\frac{R-g}{2}.
\]

For the phase-aligned ground state \(\phi\),

\[
\rho-E\le\lambda\le\rho,
\]

\[
|\langle k,\phi\rangle|^2
\ge\frac12\left(1+\frac gR\right),
\]

and

\[
\boxed{
\|k-\phi\|
\le
\mathfrak B(\epsilon/g),
}
\]

where

\[
\mathfrak B(q)
=
\sqrt{2\left(
1-\sqrt{\frac{1+(1+4q^2)^{-1/2}}2}
\right)}.
\]

#### Proof

For \(a\in\mathbf C\) and \(h\perp k\), completing the square gives

\[
\begin{aligned}
\langle ak+h,(A_+-\theta)(ak+h)\rangle
={}&\mathfrak s(\theta)|a|^2\\
&+\left\|(D-\theta)^{1/2}
\bigl(h+a(D-\theta)^{-1}r\bigr)\right\|^2.
\end{aligned}
\]

Thus \(A_+-\theta\) has exactly one negative direction.  The codimension-one
min--max principle gives

\[
\dim\mathbf 1_{(-\infty,\delta)}(A_+)\le1.
\]

Indeed, a two-dimensional spectral subspace below \(\delta\) would contain a
nonzero vector orthogonal to \(k\), contradicting \(D\succeq\delta I\).
Since one eigenvalue already lies below \(\theta<\delta\), all remaining even
spectrum lies in \([\delta,\infty)\).  The odd spectrum lies above
\(\omega\ge\theta\), so the eigenvalue below \(\theta\) is the unique global
ground and is even.

For any \(v=ak+h\),

\[
\langle v,A_+v\rangle
\ge
\rho|a|^2+\delta\|h\|^2-2\epsilon|a|\|h\|.
\]

The lower eigenvalue of the comparison matrix
\(\begin{psmallmatrix}\rho&-\epsilon\\-\epsilon&\delta\end{psmallmatrix}\)
is \(\rho-E\).  This proves the energy bound.

Writing \(x=\rho-\lambda\), the lower block of the eigenvalue equation gives

\[
\phi\propto k-(D-\lambda)^{-1}r,
\qquad
x=\langle r,(D-\lambda)^{-1}r\rangle.
\]

Hence

\[
x\le\frac{\epsilon^2}{g+x},
\qquad
\|(D-\lambda)^{-1}r\|^2
\le\frac{x}{g+x}.
\]

Solving the quadratic inequality, normalizing the eigenvector, and using
\(\|k-\phi\|^2=2(1-|\langle k,\phi\rangle|)\) gives the displayed constants.
\(\square\)

For the same fixed even candidate \(k\), this strictly extends the global
condition requiring \(\rho\) to lie below the entire nonground spectrum.  For
example,

\[
A_+=\begin{pmatrix}2&2\\2&4\end{pmatrix},
\qquad A_-=[1],
\qquad k=e_1
\]

has \(\mathfrak s(1)=-1/3\) and even ground
\(3-\sqrt5<1\), even though the candidate Rayleigh value \(2\) lies above
the first nonground eigenvalue \(1\).

### 8. Pollution-free finite Schur witnesses **[PROVED HERE; VARIATIONALLY ONE-SIDED]**

For \(B=D-\theta\succ0\),

\[
\boxed{
\langle r,B^{-1}r\rangle
=
\sup_{h\in\mathcal Q(D)}\left(
2\Re\langle r,h\rangle-\langle h,Bh\rangle
\right).
}
\]

In the continuum case the final term means
\(\|(D-\theta)^{1/2}h\|^2\).

Indeed, the right side equals

\[
\langle r,B^{-1}r\rangle
-\|B^{1/2}(h-B^{-1}r)\|^2.
\]

Therefore any trial vector in a finite-dimensional subspace of
\(\mathcal Q(D)\) satisfying

\[
2\Re\langle r,h\rangle-
\langle h,(D-\theta)h\rangle>\rho-\theta
\]

is already a rigorous continuum parity certificate.  If nested trial spaces
form a form core, their suprema increase to the full resolvent scalar.  A
finite failure is inconclusive; a finite strict success has no
spectral-pollution false positive.

This one-sided statement is pollution-free only when the finite functional
is the exact restriction of the continuum quadratic form, or when every
quadrature, truncation, and tail error is rigorously enclosed.  An
uncertified numerical Galerkin matrix can still create a false positive.

If the witness exceeds \(\rho-\theta\) by \(m>0\), then

\[
\operatorname{gap}_0(A)
:=
\inf\bigl(\sigma(A)\setminus\{\lambda\}\bigr)-\lambda
\]

satisfies

\[
\boxed{
\operatorname{gap}_0(A)
\ge
\frac{m}{1+\epsilon^2/(\delta-\theta)^2}.}
\]

To prove it, set

\[
s(u)=\rho-u-\langle r,(D-u)^{-1}r\rangle.
\]

On \([\lambda,\theta]\),

\[
1\le-s'(u)
\le1+\frac{\epsilon^2}{(\delta-\theta)^2}.
\]

Since \(s(\lambda)=0\) and \(s(\theta)\le-m\), the mean-value estimate
gives \(\theta-\lambda\ge m/(1+\epsilon^2/(\delta-\theta)^2)\).  All other
spectrum lies at or above \(\theta\).

### 9. Exact Schur-corrected candidate **[PROVED HERE; FESHBACH REPACKAGING]**

Suppose \(\mathfrak s(\theta)<0\), and set

\[
h=(D-\theta)^{-1}r,
\qquad
v=k-h,
\qquad
k^\sharp=\frac v{\sqrt{1+\|h\|^2}}.
\]

Then the following identities are exact:

\[
(A_+-\theta)v=\mathfrak s(\theta)k,
\]

\[
\rho^\sharp
:=\langle k^\sharp,A_+k^\sharp\rangle
=\theta+\frac{\mathfrak s(\theta)}{1+\|h\|^2}<\theta,
\]

\[
\|(A_+-\rho^\sharp)k^\sharp\|
=
\frac{|\mathfrak s(\theta)|\|h\|}{1+\|h\|^2},
\]

and therefore

\[
\boxed{
\frac{\|(A_+-\rho^\sharp)k^\sharp\|}
{\theta-\rho^\sharp}=\|h\|.}
\]

Also

\[
\mathfrak D(q)
:=
\sqrt{2\left(1-\frac1{\sqrt{1+q^2}}\right)},
\]

and

\[
\boxed{
\|k^\sharp-k\|
=\mathfrak D(\|h\|).}
\]

Thus an exactly evaluated negative Schur scalar and its full resolvent
correction can be converted into a legal one-sided residual certificate.
Applying the sharp residual theorem to \(k^\sharp\), with threshold
\(\theta\), gives separately

\[
\|k^\sharp-\phi\|\le\mathfrak D(\|h\|).
\]

Therefore this route gives

\[
\boxed{\|k-\phi\|\le2\mathfrak D(\|h\|).}
\]

The direct sector estimate in Section 7 may be sharper.  An arbitrary finite
witness \(h_V\) is not the full correction: it leaves the lower-block defect

\[
(A_+-\theta)(k-h_V)
=
\bigl(\rho-\theta-\langle r,h_V\rangle\bigr)k
+
\bigl(r-(D-\theta)h_V\bigr).
\]

A large resolvent correction can prove parity without proving candidate
locking.

### 10. One Feshbach step gives a quartic scalar defect **[PROVED HERE; FESHBACH REPACKAGING]**

Under the finite-dimensional or closed-form setup of Section 7, assume
\(D-\rho I\succeq gI\), \(g>0\).  Put

\[
q=\langle r,(D-\rho)^{-1}r\rangle,
\qquad
\mu_1=\rho-q,
\]

and

\[
F(\mu)=\rho-\mu-
\langle r,(D-\mu)^{-1}r\rangle.
\]

Then \(F\) is strictly decreasing below \(\inf\sigma(D)\), the unique even
eigenvalue below \(\inf\sigma(D)\) is the unique zero \(\lambda\) of \(F\),
and

\[
\mu_1\le\lambda\le\rho.
\]

Moreover,

\[
\begin{aligned}
F(\mu_1)
&=q\langle r,(D-\rho I)^{-1}
(D-\rho I+qI)^{-1}r\rangle\\
&\le\frac{q\epsilon^2}{g(g+q)}
\le\frac{\epsilon^4}{g^3}.
\end{aligned}
\]

Since \(-F'\ge1\),

\[
\boxed{
0\le\lambda-\mu_1\le F(\mu_1)
\le\frac{\epsilon^4}{g^3}.}
\]

Finally, with

\[
v_1=k-(D-\mu_1)^{-1}r,
\]

one has the exact defect identity

\[
\boxed{(A_+-\mu_1)v_1=F(\mu_1)k.}
\]

This is a genuine acceleration of the scalar/eigenvalue defect.  It is not a
quartic vector approximation: \(\|v_1-k\|\le\epsilon/(g+q)\) is still first
order.  “Quartic” refers to the fixed-gap perturbative regime; if \(g\)
collapses at Landau--Widom scale, the displayed bound need not tend to zero.
Calling the theorem an RH advance without these qualifications would be
heuristic drift.

---

## Round 3 — cumulative boundary-shell falsification

### 11. A PNT transfer lemma

Let \(F_X\ge0\) be decreasing on \([\sqrt X,X]\), and define

\[
\Delta_X=\sup_{t\ge\sqrt X}\left|\frac{\psi(t)}t-1\right|.
\]

Stieltjes integration by parts gives

\[
\left|\int_{\sqrt X}^XF_X\,d\psi-
\int_{\sqrt X}^XF_X\,dt\right|
\le
\Delta_X\left(
2\sqrt X F_X(\sqrt X)+
\int_{\sqrt X}^XF_X(t)\,dt
\right).
\]

The PNT says \(\Delta_X\to0\).  This lemma will transfer each monotone
boundary envelope to an elementary Laplace integral.

### 12. Fixed-regularity absolute-summation no-go **[PROVED HERE]**

For every fixed \(\beta\ge0\),

\[
\boxed{
\sum_{\sqrt X\le n<X}
\frac{\Lambda(n)}{\sqrt n}
\left(\frac{\log(X/n)}{\log X}\right)^\beta
\sim
2^{\beta+1}\Gamma(\beta+1)
\frac{\sqrt X}{(\log X)^\beta}.}
\]

#### Proof

Apply the transfer lemma and set \(v=\log(X/t)\).  The continuous integral
is

\[
\frac{\sqrt X}{(\log X)^\beta}
\int_0^{(\log X)/2}e^{-v/2}v^\beta\,dv.
\]

Monotone convergence gives

\[
\int_0^\infty e^{-v/2}v^\beta\,dv
=2^{\beta+1}\Gamma(\beta+1).
\]

For the present weight the endpoint contribution is explicitly

\[
2\sqrt X F_X(\sqrt X)
=2^{1-\beta}X^{1/4}
=o\left(\frac{\sqrt X}{(\log X)^\beta}\right).
\]

For the strict cutoff \(n<X\), define the point value \(F_X(X)=0\).
Equivalently, omitting a possible prime-power atom at \(X\) costs only
\(O((\log X)/\sqrt X)\).  The remaining PNT error is therefore little-oh of
the main term. \(\square\)

Consequently no fixed polynomial order of boundary vanishing makes the full
newborn half-window absolutely small.  After the Mellin embedding cost
\(C_\alpha(X)\asymp X^{\alpha/2}/\sqrt\alpha\), the envelope grows like

\[
\frac{X^{(1+\alpha)/2}}{(\log X)^\beta}.
\]

This refutes an absolute proof method, not the completed Weil operator.

### 13. Two exact corollaries

For

\[
\eta(m)=\frac{2\sqrt m}{\pi}
+\frac2{\log(e+m^{-1/2})},
\]

with \(\eta(0)=0\), the same argument gives

\[
\boxed{
\sum_{\sqrt X\le n<X}
\frac{\Lambda(n)}{\sqrt n}
\eta\left(\frac{2\log(X/n)}{\log X}\right)
\sim\frac{8\sqrt X}{\log\log X}.}
\]

The square-root part is only

\[
\sim\frac4{\sqrt\pi}\frac{\sqrt X}{\sqrt{\log X}},
\]

while the logarithmic-capacity part supplies the dominant
\(8\sqrt X/\log\log X\).

For completeness, put \(L=\log X\) and \(v=\log(X/t)\).  For each fixed
\(v>0\),

\[
(\log L)\,
\frac2{\log(e+\sqrt{L/(2v)})}\longrightarrow4.
\]

Splitting the Laplace integral at \(v=\sqrt L\) gives an integrable majorant
on the first part and an exponentially small second part.  Dominated
convergence yields \(4\int_0^\infty e^{-v/2}dv=8\).

Likewise, for the finite-mode quadratic envelope,

\[
\boxed{
\frac{\pi^2K^2}{\sqrt6}
\sum_{\sqrt X\le n<X}\frac{\Lambda(n)}{\sqrt n}
\left(\frac{\log(X/n)}{\log X}\right)^2
\sim
\frac{16\pi^2}{\sqrt6}
\frac{K^2\sqrt X}{(\log X)^2}.}
\]

It diverges even for \(K=1\).

### 14. Low modes are coherent, not random **[PROVED HERE]**

For an integer \(r\), define

\[B_r(X)=
2\sum_{\sqrt X\le n<X}
\frac{\Lambda(n)}{\sqrt n}
\frac{\log(X/n)}{\log X}
\cos\left(\frac{2\pi r\log n}{\log X}\right).
\]

If \(r_X/\log X\to c\), put

\[
I(c)=
\frac{\frac14-4\pi^2c^2}
{(\frac14+4\pi^2c^2)^2}.
\]

Then the PNT gives the additive asymptotic

\[
\boxed{
B_{r_X}(X)
=
\frac{2\sqrt X}{\log X}\bigl(I(c)+o(1)\bigr).}
\]

This is a ratio asymptotic only when \(I(c)\ne0\).  The signed weight requires
a bounded-variation version of partial summation.  With

\[
G_X(t)=2t^{-1/2}\frac v{\log X}
\cos\left(2\pi\frac{r_X}{\log X}v\right),
\qquad v=\log(X/t),
\]

and bounded \(r_X/\log X\), direct differentiation gives

\[
\int_{\sqrt X}^{X}t\,|dG_X(t)|
=O\left(\frac{\sqrt X}{\log X}\right),
\qquad
\sqrt X\,|G_X(\sqrt X)|=O(X^{1/4}).
\]

Thus the PNT remainder is \(o(\sqrt X/\log X)\).  After
\(n=Xe^{-v}\), the phase becomes
\(\cos(2\pi(r_X/\log X)v)\), and

\[
\int_0^\infty ve^{-v/2}\cos(2\pi cv)\,dv
=
\frac{\frac14-4\pi^2c^2}
{(\frac14+4\pi^2c^2)^2}.
\]

In particular, every \(r=o(\log X)\) obeys

\[
B_r(X)\sim\frac{8\sqrt X}{\log X}.
\]

The leading coefficient changes sign at
\(|r|/\log X=1/(4\pi)\).  Modes capable of resolving the boundary therefore
have \(|r|\asymp\log X\), precisely where the absolute finite-mode envelope
has grown to order \(\sqrt X\).

### 15. A coherent endpoint witness **[PROVED HERE]**

Fix \(0<d<L/2\) and let

\[
v_L=(2d)^{-1/2}
\left(
1_{[-L/2,-L/2+d]}+1_{[L/2-d,L/2]}
\right).
\]

For \(b=L-s\), \(0<s<d\), the two translated endpoint slabs overlap in an
interval of length \(s\), so

\[
\langle H_bv_L,v_L\rangle=\frac{s}{d}.
\]

Consequently, for each fixed \(d>0\), with \(X=e^L\) and \(X\to\infty\),

\[
\begin{aligned}
&\left\langle
\sum_{Xe^{-d}<n<X}\frac{\Lambda(n)}{\sqrt n}H_{\log n}v_L,v_L
\right\rangle\\
&\qquad\sim
\frac{\sqrt X}{d}
\left[4-(2d+4)e^{-d/2}\right].
\end{aligned}
\]

The coefficient has the separate expansion

\[
\frac{4-(2d+4)e^{-d/2}}d
=\frac d2+O(d^2)
\qquad(d\downarrow0).
\]

This is an iterated limit.  Ordinary PNT does not justify a joint
\(d=d(X)\downarrow0\) assertion.

For the form comparison, rescale to a unit interval and put
\(\delta=d/L\).  The Fourier transform of the two-slab vector satisfies

\[
|\widehat v(\xi)|^2
\le C\min\left(\delta,\frac1{\delta\xi^2}\right).
\]

Splitting the logarithmic multiplier integral at
\(|\xi|=\delta^{-1}\) gives

\[
\mathcal E_{\log}(v_L)=O(\log(e+L/d)).
\]

Thus, for fixed \(d\), the cumulative witness divided by its logarithmic
energy diverges.  Per-shell \(H^{\log}\) continuity cannot be summed
uniformly, even relatively.  A successful proof must exploit the actual
candidate's endpoint decay or cancellation with the pole/Archimedean sector.

---

## Round 4 — the cancellation translator and a surviving boundary estimate

### 16. Exact Fourier/Mellin translator **[PROVED HERE]**

Use

\[
\widehat v(\xi)=\int_{\mathbb R}v(x)e^{-i\xi x}\,dx,
\qquad
\|v\|_2^2=\frac1{2\pi}\int|\widehat v(\xi)|^2\,d\xi.
\]

For zero-extended \(v\), let

\[
a_v(y)=\langle (T_y+T_y^*)v,v\rangle.
\]

Wiener--Khinchin gives

\[
a_v(y)=\frac1\pi\int|\widehat v(\xi)|^2\cos(\xi y)\,d\xi.
\]

Therefore, if

\[
D_X(\xi)=\sum_{1<n<X}\frac{\Lambda(n)}{n^{1/2+i\xi}},
\]

then exactly

\[
\boxed{
\sum_{1<n<X}\frac{\Lambda(n)}{\sqrt n}a_v(\log n)
=\frac1\pi\int|\widehat v(\xi)|^2\Re D_X(\xi)\,d\xi.}
\]

Thus the entire prime-shift form is an average of a critical-line von
Mangoldt polynomial against the positive spectral measure
\(|\widehat v(\xi)|^2d\xi\); the integrand itself is not positive.  Its
continuous density component is

\[
D_X^{\mathrm{cont}}(\xi)
=\frac{X^{1/2-i\xi}-1}{1/2-i\xi},
\]

which is order \(\sqrt X\) at bounded frequency.  Random-phase rhetoric at
low frequency is therefore mathematically wrong unless the pole-density term
has first been removed.

Define the entire extension

\[
\widehat a_v(z)=\int_{\mathbb R}a_v(u)e^{-izu}\,du.
\]

For even \(a_v\), the exact pole/prime rearrangement is

\[
\begin{aligned}
&\widehat a_v(i/2)+\widehat a_v(-i/2)
-2\sum_{n<X}\frac{\Lambda(n)}{\sqrt n}a_v(\log n)\\
&\quad=
2\int_0^Le^{-u/2}a_v(u)\,du
-2\left[
\sum_{n<X}\frac{\Lambda(n)}{\sqrt n}a_v(\log n)
-\int_0^Le^{u/2}a_v(u)\,du
\right].
\end{aligned}
\]

This identity names the right centered object.  The factor \(2\) and the
critical coefficient \(\Lambda(n)/\sqrt n\) are load-bearing.

### 17. Prolate newest-shell theorem **[DERIVED HERE FROM CCM INPUTS]**

The CCM candidate has

\[
h(u)=\frac\pi2u^2(2\pi u^2-3)e^{-\pi u^2},
\qquad
k(u)=E(h)(u)=u^{1/2}\sum_{m\ge1}h(mu),
\]

and \(k_\lambda=E(h_\lambda)\), with the support/truncation in \(E\)
understood as in CCM, on
\([\lambda^{-1},\lambda]\).  We use exactly the following source inputs:

\[
|k_\lambda(u)-k(u)|
\le C_1\lambda^{-1}u^{-1/2},
\]

\[
k(u)=k(u^{-1}),
\]

and, for

\[
\tau(R)=\int_R^\infty|k(u)|^2\,d^*u,
\]

the explicit Gaussian formula implies

\[
\tau(R)\le C R^7e^{-2\pi R^2}
\qquad(R\ge1).
\]

Normalize

\[
v_\lambda(x)
=N_\lambda^{-1}k_\lambda(e^x),
\qquad
N_\lambda^2
=\int_{1/\lambda}^{\lambda}|k_\lambda(u)|^2d^*u.
\]

The uniform comparison on \([1,2]\) and \(k(1)>0\) give
\(\inf_{\lambda\gg1}N_\lambda>0\); indeed \(h(m)>0\) for every integer
\(m\ge1\).  The comparison estimate is extracted from CCM equation (7.6),
Lemma 7.2/equation (7.8), and the proof of Lemma 7.3.  The Gaussian
\(m u>\lambda\) tail implicit in the truncation is absorbed by the same
\(C_1\lambda^{-1}u^{-1/2}\) bound.

For \(\lambda\le n<\lambda^2\), put \(r=n/\lambda\).  The shift by
\(\log n\) couples only the endpoint strips

\[
[1/\lambda,1/r]
\quad\text{and}\quad
[r,\lambda].
\]

The source comparison and inversion of the limiting \(k\) give

\[
\int_r^\lambda|k_\lambda|^2d^*u
\le2\tau(r)+\frac{2C_1^2}{\lambda n},
\]

\[
\int_{1/\lambda}^{1/r}|k_\lambda|^2d^*u
\le2\tau(r)+\frac{2C_1^2}{\lambda}.
\]

Cauchy--Schwarz across these strips first yields

\[
|\langle H_{\log n}v_\lambda,v_\lambda\rangle|
\le
\frac2{N_\lambda^2}\sqrt{E_-(n)E_+(n)},
\]

where \(E_-(n)\) and \(E_+(n)\) are the two displayed strip energies.
Their bounds and \(\inf N_\lambda>0\) imply

\[
|\langle H_{\log n}v_\lambda,v_\lambda\rangle|
\le
C\sqrt{\left(\tau(r)+\frac1{\lambda n}\right)
\left(\tau(r)+\frac1\lambda\right)}.
\]

Using only

\[
\sum_{n<\lambda^2}\frac{\Lambda(n)}{\sqrt n}\ll\lambda,
\qquad
\sum_{n<\lambda^2}\frac{\Lambda(n)}n\ll\log\lambda,
\]

one obtains, for sufficiently large \(\lambda\), uniformly for
\(1\le R\le\lambda\),

\[
\begin{aligned}
Q_{\lambda,R}
&:=\sum_{\lambda R\le n<\lambda^2}
\frac{\Lambda(n)}{\sqrt n}
|\langle H_{\log n}v_\lambda,v_\lambda\rangle|\\
&\ll
\lambda\tau(R)+\sqrt{\lambda\tau(R)}
+\frac{\log\lambda}{\sqrt\lambda}\sqrt{\tau(R)}
+\frac{\log\lambda}{\lambda}.
\end{aligned}
\]

Taking \(R=A\sqrt{\log\lambda}\) with
\(A>1/\sqrt{2\pi}\) proves

\[
\boxed{
Q_{\lambda,A\sqrt{\log\lambda}}\longrightarrow0.}
\]

This theorem is unconditional and candidate-specific.  It is only a
quadratic-form estimate.  It does **not** prove that the norm of the summed
high-shell vector tends to zero, and it leaves

\[
n\lesssim\lambda\sqrt{\log\lambda}
\]

untreated.

There is also a parity firewall: this estimate is for the unsymmetrized
finite \(k_\lambda\).  The exact sector candidate in Section 5 uses
\(k_\lambda^+=(k_\lambda+Jk_\lambda)/2\).  A naive endpoint estimate after
symmetrization exchanges
the two endpoint errors and can lose the little-oh gain.  Therefore Section
17 is not yet a high-shell estimate for the actual even closure candidate;
that transfer is a named open subproblem.

### 18. Dirichlet boundary benchmark **[PROVED HERE]**

For

\[
s_{k,L}(x)=\sqrt{\frac2L}\sin\frac{k\pi x}{L},
\qquad0<x<L,
\]

direct integration gives

\[
\boxed{
\langle H_ys_{k,L},s_{k,L}\rangle
=2\left[
\left(1-\frac yL\right)\cos\frac{k\pi y}{L}
+\frac{\sin(k\pi y/L)}{k\pi}
\right].}
\]

At \(y=L-d\), the two linear terms cancel and the birth is cubic:

\[
\langle H_{L-d}s_{k,L},s_{k,L}\rangle
=O_k(d^3/L^3).
\]

Nevertheless its continuous prime-density contribution is, with
\(a=k\pi/L\) and \(q=1/4+a^2\),

\[
M_{k,L}
:=\int_0^Le^{u/2}
\langle H_us_{k,L},s_{k,L}\rangle\,du
=
-\frac1q-
\frac{4a^2}{Lq^2}\left((-1)^k\sqrt X-1\right).
\]

For fixed \(k\) and \(L\to\infty\),

\[
M_{k,L}
\sim(-1)^{k+1}\frac{64\pi^2k^2\sqrt X}{L^3}.
\]

So Dirichlet cancellation buys two powers of \(L\), but an uncentered
deterministic \(\sqrt X/L^3\) term survives.

### 19. RH-equivalence firewall

Define the centered frequency-zero statistic

\[
B(X)=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}-2(\sqrt X-1).
\]

Put \(E_0(X)=\psi(X)-X+1\).  Partial summation gives exactly

\[
B(X)
=\frac{E_0(X)}{\sqrt X}
+\frac12\int_1^X\frac{E_0(t)}{t^{3/2}}\,dt,
\]

and Volterra inversion gives

\[
E_0(X)
=\sqrt X B(X)-\frac12\int_1^X\frac{B(t)}{\sqrt t}\,dt.
\]

Also \(\psi(X)-X=E_0(X)-1\).

Hence the standard PNT-error characterization of RH yields

\[
\boxed{
\mathrm{RH}
\iff
B(X)=O_\varepsilon(X^\varepsilon)
\quad\text{for every }\varepsilon>0.}
\]

Any proposed subpower cancellation theorem containing this unsmoothed
frequency-zero statistic has merely hidden RH.  The theorem in Section 17
does not: it controls only a candidate-specific upper boundary sector.

---

## Round 5 — continuum coercivity and no-pollution certification

### 20. The restricted logarithmic comparison operator **[DERIVED HERE FROM SUZUKI]**

On \(I=(-a,a)\), zero-extend \(v\) and put

\[
p(\xi)=\frac12\log(e^2+\xi^2),
\qquad
\ell_a[v]=\frac1{2\pi}\int p(\xi)|\widehat v(\xi)|^2\,d\xi.
\]

Let \(L_a\) be the self-adjoint operator associated with this closed form.
This is the restricted full-line logarithmic Bessel operator.  It is **not**
automatically \(\frac12\log(e^2-\Delta_D)\); substituting the spectral
Dirichlet functional calculus would require a boundary theorem that we do
not have.

Let \(\mathcal D_{\log,a}\) be the \(\ell_a+\|\cdot\|_2^2\) closure of
\(C_c^\infty(I)\).  Suzuki's explicit formula, common form core, and
form-norm equivalence identify the localized Weil form domain with
\(\mathcal D_{\log,a}\) and give the closed-form identity

\[
q_a
=\ell_a-\log(2\pi)\|\cdot\|_2^2
+\langle\cdot,
(K_{\Gamma,a}+P_{\mathrm{pole},a}
-\mathcal P_a^{\mathrm{Suz}})\cdot\rangle,
\]

where, to avoid collision with the \(L\)-notation of Section 1,

\[
\mathcal P_a^{\mathrm{Suz}}
=\sum_{2\le n\le e^{2a}}
\frac{\Lambda(n)}{\sqrt n}H_{\log n}.
\]

The remainder is a bounded self-adjoint operator.  The bounded-perturbation
theorem therefore yields the operator identity

\[
A_a
=L_a-\log(2\pi)I+K_{\Gamma,a}
+P_{\mathrm{pole},a}-\mathcal P_a^{\mathrm{Suz}},
\qquad
\operatorname{Dom}(A_a)=\operatorname{Dom}(L_a).
\]

where

\[
P_{\mathrm{pole},a}
=2|C\rangle\langle C|-2|S\rangle\langle S|,
\quad C(x)=\cosh(x/2),\quad S(x)=\sinh(x/2),
\]

and \(K_{\Gamma,a}\) is the compression of the multiplier

\[
r_\Gamma(\xi)
=\Re\psi(1/4+i\xi/2)-\log\pi-p(\xi)+\log(2\pi).
\]

Since \(r_\Gamma(\xi)=O(|\xi|^{-2})\),

\[
\|K_{\Gamma,a}\|_{\mathrm{HS}}
\le\sqrt{a/\pi}\,\|r_\Gamma\|_2.
\]

The underlying identities are Suzuki equations (2.5), (2.7), and
(2.9)--(2.11); the common form realization and compact embedding are supplied
by his Theorem 1.1 and Proposition 4.1 in
[Suzuki, v2](https://arxiv.org/html/2606.09096v2).

### 21. Explicit restricted-log eigenvalue floor **[PROVED HERE]**

The compact embedding
\(\mathcal D_{\log,a}\hookrightarrow L^2(I)\) gives \(L_a\) compact
resolvent.  Let \(\mu_1\le\mu_2\le\cdots\) be its eigenvalues.  Then

\[
\boxed{
\mu_N\ge h(R_N),
\qquad
R_N=\frac{\pi N}{2a},}
\]

where

\[
\boxed{
h(R)=
\frac12\log(e^2+R^2)-1+
\frac eR\arctan(R/e).}
\]

#### Proof

For orthonormal eigenfunctions \(\phi_1,\ldots,\phi_N\), Bessel's
inequality gives

\[
F(\xi):=\sum_{j=1}^N|\widehat\phi_j(\xi)|^2\le2a,
\]

while Parseval gives \((2\pi)^{-1}\int F=N\).  Since \(p\) is even and
increasing in \(|\xi|\), the bathtub principle minimizes
\((2\pi)^{-1}\int pF\) by filling \([-R_N,R_N]\) at height \(2a\).  Thus

\[
\frac1N\sum_{j=1}^N\mu_j
\ge\frac1{R_N}\int_0^{R_N}p(t)\,dt=h(R_N).
\]

Finally \(\mu_N\) dominates the mean of the first \(N\) eigenvalues.
\(\square\)

This proof includes the interval boundary exactly.

### 22. Continuum Ritz certificate **[PROVED HERE]**

Choose a spectral threshold \(\Lambda\) of \(L_a\) between multiplicity
blocks and let
\[
P=\mathbf1_{(-\infty,\Lambda]}(L_a),
\qquad K=\operatorname{rank}P,
\qquad Q=I-P.
\]
Reflection commutes with \(L_a\), so \(P\) is parity invariant.  Moreover
\(\operatorname{Ran}P\subset\operatorname{Dom}(L_a)=\operatorname{Dom}(A_a)\).
Let \(k\in\operatorname{Ran}P\) be a normalized even lowest Ritz vector:

\[
P A_a Pk=\rho k.
\]

Define

\[
\alpha_2
=\inf_{\substack{u\in\operatorname{Ran}P\cap k^\perp\\\|u\|=1}}
\langle u,A_au\rangle,
\]

\[
\kappa_K=\|QK_{\Gamma,a}Q\|,
\qquad
s_K=\|QS\|,
\]

\[
\pi_K
=\sup_{\substack{v\in\operatorname{Ran}Q\\\|v\|=1}}
\langle\mathcal P_a^{\mathrm{Suz}}v,v\rangle,
\]

and

\[
\beta_K
=\mu_{K+1}-\log(2\pi)-\kappa_K-2s_K^2-\pi_K.
\]

The cross-block norm is

\[
\varepsilon_K
=\|Q(K_{\Gamma,a}+P_{\mathrm{pole},a}-\mathcal P_a^{\mathrm{Suz}})
(P-|k\rangle\langle k|)\|.
\]

Put

\[
b_K
=\frac{\alpha_2+\beta_K-
\sqrt{(\alpha_2-\beta_K)^2+4\varepsilon_K^2}}2.
\]

If

\[
\boxed{\rho<b_K,}
\]

then

\[
\lambda_2(A_a)\ge b_K,
\]

the continuum ground is simple and even, and

\[
\boxed{
(A_a-\rho)k
=Q(K_{\Gamma,a}+P_{\mathrm{pole},a}
-\mathcal P_a^{\mathrm{Suz}})k}
\]

is its exact residual relative to the Ritz candidate.

#### Proof

For \(v\in\operatorname{Ran}Q\), the comparison spectrum and the negative
parts of the bounded remainder give

\[
\langle v,A_av\rangle\ge\beta_K\|v\|^2.
\]

For \(x=u+v\perp k\), with \(u\in\operatorname{Ran}P\cap k^\perp\),

\[
\langle x,A_ax\rangle
\ge
\alpha_2\|u\|^2+\beta_K\|v\|^2
-2\varepsilon_K\|u\|\|v\|
\ge b_K\|x\|^2.
\]

The bounded perturbation preserves compact resolvent.  The codimension-one
min--max principle gives \(\lambda_2(A_a)\ge b_K\),
while \(\lambda_1(A_a)\le\rho<b_K\).  Thus the ground is simple.  Every odd
vector is orthogonal to the even \(k\), so an odd ground would have energy at
least \(b_K\); hence the ground is even.  Finally the Ritz equation kills the
\(P\)-component of \((A_a-\rho)k\), while \(L_a\) and the scalar term have no
\(P\)-to-\(Q\) block. \(\square\)

This single inequality supplies parity, a continuum one-sided gap, absence
of low spectral pollution, and the residual required by Section 6.

### 23. Why this does not yet scale to RH

Every nonzero truncated shift \(H_b\) is noncompact.  Choose a smooth bump
\(\varphi\) supported in a small interval near the left endpoint so that its
translate by \(b\) remains in \(I\), while its translate by \(-b\) exits
\(I\).  The normalized modulations \(v_t=e^{itx}\varphi(x)\) converge weakly
to zero and satisfy \(\|H_bv_t\|=1\).  For every fixed finite-rank \(P_K\),
\(P_Kv_t\to0\) and \(P_KH_bv_t\to0\), so
\(Q_KH_bQ_Kv_t\to H_bv_t\).  Hence, for every finite \(K\),

\[
\boxed{\|Q_KH_bQ_K\|\ge1.}
\]

At fixed \(a\), the prime sector is bounded, so the theorem is a valid
fixed-window certificate.  But

\[
\sum_{n<e^{2a}}\frac{\Lambda(n)}{\sqrt n}\asymp e^a,
\]

whereas the explicit certified comparison floor satisfies

\[
h\left(\frac{\pi K}{2a}\right)=\log(K/a)+O(1).
\]

The crude absolute version of this particular certificate therefore does
not become positive until roughly

\[
K\gtrsim a\exp(c e^a),
\]

which is asymptotically useless.  This is not a universal lower bound on
every possible method.  The large-window target is a joint
\((a,K)\) bound on

\[
\lambda_{\max}(Q_K\mathcal P_a^{\mathrm{Suz}}Q_K),
\quad
\|Q_K\mathcal P_a^{\mathrm{Suz}}P_K\|,
\quad
\|Q_K\mathcal P_a^{\mathrm{Suz}}k_K\|,
\]

using boundary structure rather than total prime mass.

---

## Round 6 — tail lifting, adversarial closure, and the reduced contract

### 24. Positive tail-budget ground lift **[PROVED HERE]**

Let \(A_T\) be lower-bounded self-adjoint with compact resolvent, let \(E\)
be bounded self-adjoint, and assume that both operators commute with parity.
Put \(A_\infty=A_T+E\) and suppose

\[
0\preceq E\preceq BI.
\]

Let \(k\in\operatorname{Dom}(A_T)\) be unit and even, and set

\[
\rho_T=\langle k,A_Tk\rangle,
\qquad
\epsilon_T=\|(A_T-\rho_T)k\|.
\]

Suppose

\[
s\le\min\{\lambda_2(A_{T,+}),\lambda_1(A_{T,-})\},
\qquad
d=s-\rho_T-B>0.
\]

Then \(A_\infty\) has a unique simple even ground, every other spectral
value is at least \(s\), and

\[
\boxed{
\|k-\phi_0\|
\le
\mathfrak D\left(\frac{\epsilon_T+B/2}{s-\rho_T-B}\right).}
\]

Also

\[
0\le\rho_\infty-\lambda_0
\le
\frac{(\epsilon_T+B/2)^2}{s-\rho_T-B}.
\]

#### Proof

Monotonicity under \(E\succeq0\) gives

\[
\lambda_2(A_{\infty,+})\ge s,
\qquad
\lambda_1(A_{\infty,-})\ge s.
\]

But the Rayleigh value

\[
\rho_\infty=\rho_T+e,
\qquad e=\langle k,Ek\rangle\le B,
\]

is below \(s\).  Hence there is exactly one eigenvalue below \(s\), and it
is even.  Moreover

\[
\|(E-eI)k\|^2
=\langle E^2\rangle-e^2
\le e(B-e)\le B^2/4.
\]

Thus the full residual is at most \(\epsilon_T+B/2\), while the one-sided
Rayleigh gap is at least \(s-\rho_T-B\).  The sharp residual/gap theorem
gives both conclusions. \(\square\)

If \(e\) is known exactly, replace \(B/2\) by
\(\sqrt{e(B-e)}\) and the denominator by \(s-\rho_T-e\).  If only
\(e\in[e_-,e_+]\) is enclosed, use

\[
\max_{x\in[e_-,e_+]}\sqrt{x(B-x)}
\quad\text{and}\quad
s-\rho_T-e_+
\]

instead.

Groskin's positive omitted-Archimedean-tail formula supplies precisely such
an \(E\) and a computable \(B_T\) at fixed Galerkin band \(N\), for
\(T>\max(\varrho N,7)\), where
\(\varrho=2\pi/L_{\mathrm{Groskin}}\) in the source's notation; see
[Groskin, Theorem 3.2 and Corollary 3.3, v3](https://arxiv.org/html/2607.02828v3).
This lemma removes the
Archimedean integration cutoff.  It does not remove the Galerkin cutoff.

The subtraction of \(B\) is indispensable: for

\[
A_T=\operatorname{diag}(0,1),
\qquad E=\operatorname{diag}(1.1,0),
\]

the tail flips the ground state.

### 25. Final reduced RH contract **[CONDITIONAL]**

There are two valid routes.  They must not be mixed.

#### Route F — finite real-rooted matrices

For an unbounded sequence \(\lambda_j\), choose exact finite matrices
\(W_j=QW_{\lambda_j}^{N_j}\) and the canonical even projected candidates
\(p_j\) of Section 5.  Prove the sector-Schur hypotheses of Section 7 for
the finite ground vectors \(\phi_j\), and prove, for every
\(0<\alpha<1/2\),

\[
\boxed{
c_jC_\alpha(\lambda_j^2)
\mathfrak B\left(
\frac{\epsilon_j}{\delta_j-\rho_j}
\right)
+\tau_{j,\alpha}\longrightarrow0.}
\]

Every matrix, basis, transport, projection, and candidate amplitude must be
the canonical object of Sections 2--5.  Then Section 6 applies directly,
using CvS Theorem 5.6 for finite real-rootedness.

#### Route C — continuum ground with a form-core lift

Let \(A_{a_j}\) be the exact continuum CCM Weil operator under the canonical
logarithmic transport, with \(a_j=\log\lambda_j\).  Verify the exact
identification of this operator/form with the one used in Sections 20--22.
Use the continuum Ritz theorem to prove a simple even ground
\(\phi_j\), with a certified Ritz vector \(r_j\), residual
\(\varepsilon_j^{\mathrm{Ritz}}\), and one-sided threshold \(b_j\).

Define the continuum even prolate direction and its matching amplitude by

\[
p_j=
\frac{\kappa_{\lambda_j}^{-1}k_{\lambda_j}^+}
{\|k_{\lambda_j}^+\|_2},
\qquad
c_j=\|k_{\lambda_j}^+\|_2,
\]

assuming the denominator is nonzero, and put

\[
\tau_{j,\alpha}
=
\|c_j\kappa_{\lambda_j}p_j-k_{\lambda_j}^+\|_{1,\alpha}=0.
\]

The Ritz vector \(r_j\) is not automatically this \(p_j\).  The mismatch
must be charged:

\[
d_j
:=
\|p_j-r_j\|_2
+
\mathfrak D\left(
\frac{\varepsilon_j^{\mathrm{Ritz}}}{b_j-\rho_j^{\mathrm{Ritz}}}
\right).
\]

If, for every \(0<\alpha<1/2\),

\[
\boxed{
c_jC_\alpha(\lambda_j^2)d_j
+\tau_{j,\alpha}\longrightarrow0,}
\]

then Section 6A supplies real-rootedness of the continuum ground transform
from the exact finite form restrictions, and the same weighted
Rouché/Hurwitz argument proves RH.

Section 24 may enclose a positive omitted Archimedean integration tail at
fixed Galerkin band.  It does not control a Galerkin complement, indefinite
cross-blocks, or a generic finite-to-continuum passage; those are handled by
Section 22 and the form-core lemma.

No separate comparison-transform conjecture is needed.

### 26. The live hole after six rounds

The problem is no longer “find a pretty phase stabilization.”  In either
route, the exact remaining estimate is

\[
\boxed{
c_jC_\alpha(\lambda_j^2)d_j
+\tau_{j,\alpha}\longrightarrow0
\qquad(0<\alpha<1/2),
}
\]

with \(d_j\) supplied by the appropriate finite Schur or continuum Ritz
certificate, and with parity and the gap proved on the same canonical Weil
object.

The newest-shell quadratic form is now controlled on the unsymmetrized
\(k_\lambda\) for \(n\ge\lambda A\sqrt{\log\lambda}\), but four debts
remain:

- transfer that bound to the exact even \(k_\lambda^+\);
- upgrade a quadratic expectation to a residual/vector estimate;
- control the old/middle shells
  \(n\lesssim\lambda\sqrt{\log\lambda}\) together with the Archimedean and
  pole terms;
- obtain a gap estimate strong enough to survive the
  \(\lambda^\alpha\) Mellin amplification.

## 27. Triangulation verdict table

| Round | Candidate claim | Adversarial bearing | Verdict |
|---|---|---|---|
| 1 | finite ground transforms can converge to \(\Xi\) | arbitrary transport and determinant normalization break object identity | **PASS after canonical repair** |
| 2 | parity and transport require one global threshold | Schur complement separates parity from even-sector locking | **STRICTLY IMPROVED** |
| 3 | shell-birth continuity can be summed absolutely | PNT gives \(\sqrt X/(\log X)^\beta\); endpoint slabs add coherently | **REFUTED** |
| 4 | candidate endpoint localization may beat the no-go | explicit Gaussian tail controls upper shells for unsymmetrized \(k_\lambda\) | **PARTIAL PASS, quadratic only** |
| 5 | high modes remove Galerkin pollution automatically | restricted-log coercivity works, but prime shifts are noncompact | **FIXED-WINDOW PASS; RH-SCALE FAIL** |
| 6 | certified truncations can close the route | positive tail lift works; weighted middle-shell locking remains | **CONDITIONAL** |

## 28. Claim ledger

### Proved or source-discharged

- canonical finite real-rootedness under the exact divided-difference and
  simple-even hypotheses;
- explicit prolate-candidate transform convergence to \(\Xi\);
- sector-decoupled parity, angle, and finite-witness theorems;
- exact Schur-corrected candidate and quartic Feshbach scalar defect;
- fixed-regularity boundary no-go and low-mode coherence asymptotics;
- exact Fourier/Mellin cancellation translator;
- candidate-specific newest-shell quadratic \(o(1)\) for the unsymmetrized
  \(k_\lambda\);
- restricted-log eigenvalue floor and continuum Ritz certificate;
- positive Archimedean tail-budget lift.

### Refuted

- Hermitian + simple + even implies a real-rooted ground transform;
- any fixed algebraic shell-birth modulus is absolutely summable;
- low checkpoint modes see random prime phases near \(X\);
- the prime-shift remainder is compact;
- an arbitrary isometry or an undeclared zero-free renormalization preserves
  the cross-checkpoint object;
- an unweighted small residual is enough on expanding windows.

### Open

- quantitative parity/gap certificates along an unbounded sequence of the
  genuine Weil operators;
- vector-norm control of the candidate residual, especially for the
  old/middle prime shells;
- transfer of the newest-shell quadratic bound from \(k_\lambda\) to the
  exact even candidate \(k_\lambda^+\);
- a Galerkin schedule whose weighted projection error beats
  \(\lambda^{-\alpha}\) for every \(\alpha<1/2\);
- a joint \((a,K)\) projected-prime estimate that improves on absolute mass.

### Dark

- whether the needed middle-shell cancellation is true;
- whether its proof can avoid an RH-equivalent frequency-zero estimate;
- whether the relevant gap survives the observed large-window collapse;
- RH.

## 29. Immediate next attacks

The next experiments should be discriminating, not decorative:

1. compute the three projected-prime quantities in Section 23 on the exact   prolate candidate and compare them with the generic total-mass envelope;
2. split the residual into
   \(n<\lambda\),
   \(\lambda\le n<\lambda A\sqrt{\log\lambda}\), and the now-controlled
   upper range, keeping the pole-density cancellation before taking norms;
3. certify finite Schur witnesses and continuum Ritz complements on the same
   matrices, then test whether their margins decay slower or faster than the
   Mellin weight \(\lambda^{-\alpha}\);
4. treat any theorem that uniformly controls the centered \(t=0\) statistic
   of Section 19 as RH-equivalent until proved otherwise.
5. attack the Section 17 parity debt through the prolate concentration
   defect: CCM's discussion around equation (7.12) gives exponentially small
   \(1-\chi_n(\lambda)\) for the two relevant time-limited prolate modes.
   Poisson summation converts the inversion defect of \(E(h_\lambda)\) into
   an \(E(\mathcal Fh_\lambda-h_\lambda)\) term plus the exponentially small
   value \(h_\lambda(0)\).  The missing lemma is a weighted endpoint bound
   for \(E\) on this special two-mode defect, not generic symmetrization.

The checkpoint frame has therefore done its job: it has converted a broad
finite-to-Archimedean metaphor into a falsifiable spectral contract with one
localized boundary obstruction.