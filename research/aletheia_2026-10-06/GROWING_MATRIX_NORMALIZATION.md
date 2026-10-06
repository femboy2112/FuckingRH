# Normalization of the growing prime-clock matrices

**Date:** 2026-10-06  
**Status:** design constraints and exact normalization identities for the finite-section / transfer-matrix program. RH remains open.

## 0. Why normalization is load-bearing

The growing matrix must distinguish three different structures:

1. **event mass** — how strongly a prime-power event enters the causal measure;
2. **Hilbert half-density** — how that mass is split between the two legs of a Gram/kernel matrix;
3. **transfer gain vs twist** — scalar growth should not masquerade as spectral winding.

Ad hoc normalization by matrix dimension, prime count, or Frobenius norm can destroy the arithmetic scale and should not be used in the proof-bearing object.

---

## 1. Event mass vs matrix-leg amplitude

For a prime-power event

\[
q=p^k,
\]

the critical causal event weight is

\[
\boxed{
w_{p,k}
=
\frac{\Lambda(p^k)}{\sqrt{p^k}}
=
(\log p)p^{-k/2}.
}
\]

If the finite operator is represented as an integral kernel on the atomic measure

\[
d\mu
=
\sum_j w_j\delta_{\tau_j},
\qquad
\tau_j=\log q_j,
\]

then in the orthonormal atomic basis the matrix is

\[
\boxed{
K_{ij}
=
\sqrt{w_i}\,
\kappa(\tau_i,\tau_j)\,
\sqrt{w_j}.
}
\]

Therefore the natural **one-leg amplitude** is

\[
\boxed{
a_{p,k}
=
\sqrt{w_{p,k}}
=
\sqrt{\log p}\;p^{-k/4}.
}
\]

This is the factor-level normalization appropriate to

\[
K=B^*B.
\]

The critical half-density \(p^{-k/2}\) lives at the **kernel/energy level**; the factor \(B\) carries quarter-density \(p^{-k/4}\) on each leg.

This avoids a common double-counting mistake: if a feature vector already contains \(a_{p,k}\), do not multiply the Gram entry by \(w_{p,k}\) again.

---

## 2. Atomic measures need no spacing quadrature factor

The prime events are genuine atoms at

\[
\tau_j=k\log p.
\]

For the atomic integral

\[
\int f\,d\mu
=
\sum_jw_jf(\tau_j),
\]

there is **no additional \(\Delta\tau_j\)** factor.

Adding one would change the measure.

By contrast, when the continuous Gamma/Archimedean channel is numerically discretized, quadrature weights are required.

If the continuous integral is approximated by nodes \(t_r\) with quadrature masses \(h_r\), then its matrix legs carry

\[
\sqrt{h_r}
\]

exactly as atomic prime legs carry \(\sqrt{w_j}\).

Thus both discrete and continuous sectors follow the same half-density rule:

\[
\boxed{
\text{measure mass }m
\longrightarrow
\sqrt m\text{ on each matrix leg}.
}
\]

---

## 3. Correlation normalization preserves positivity exactly

Suppose a finite Gram candidate \(G_m\) has positive diagonal entries.

Let

\[
D=\operatorname{diag}(G_{11},\ldots,G_{mm})
\]

and define the correlation-normalized matrix

\[
\boxed{
C
=
D^{-1/2}G D^{-1/2}.
}
\]

Then

\[
C_{ii}=1.
\]

Because this is a positive diagonal congruence,

\[
\boxed{
G\succeq0
\iff
C\succeq0,
}
\]

and more generally \(G\) and \(C\) have the same inertia by Sylvester's law.

Therefore unit-diagonal normalization is a **safe diagnostic gauge**:

- it removes trivial local amplitude variation;
- it keeps every positivity/sign obstruction exactly;
- it reveals the pure angular/correlation geometry.

The raw matrix \(G\) must still be retained because its scale contains the physical arithmetic weights.

---

## 4. Dimensionless Schur innovation

For

\[
G_{m+1}
=
\begin{pmatrix}
G_m&v\\
v^*&c
\end{pmatrix},
\]

the raw Schur innovation is

\[
\Delta
=
c-v^*G_m^{-1}v.
\]

Normalize the new event by its own diagonal mass \(c>0\).

Then

\[
\boxed{
\delta
=
\frac{\Delta}{c}
=
1-r^*C_m^{-1}r,
}
\]

where

\[
r_i
=
\frac{v_i}{\sqrt{G_{ii}c}}
\]

is the correlation vector of the new event against the old ones.

This quantity is dimensionless and invariant under independent positive rescaling of all event basis vectors.

For a genuine Gram system,

\[
0\le\delta\le1.
\]

Geometrically,

\[
\boxed{
\delta
=
\text{squared fraction of the new event lying outside the old span}.
}
\]

This is likely a better causal diagnostic than raw \(\Delta\), because it separates innovation geometry from event size.

---

## 5. Transfer matrices should separate gain from twist

If a local \(2\times2\) event transfer matrix is \(M_j(z)\), its scalar determinant/volume growth should not be confused with the geometric twist.

Whenever a real/complex branch can be chosen consistently, write

\[
\boxed{
M_j
=
g_j\,\widehat M_j,
\qquad
\det\widehat M_j=1.
}
\]

For a \(2\times2\) matrix,

\[
g_j=(\det M_j)^{1/2}
\]

up to phase/sign convention.

Then:

- \(g_j\) = scalar gain/volume;
- \(\widehat M_j\in SL(2)\) = shape/twist.

For self-adjoint canonical/Jacobi realizations the natural transfer group is symplectic, which in dimension two is \(SL(2,\mathbb R)\).

For an indefinite scattering realization the natural target may instead be \(SU(1,1)\) or a \(J\)-unitary group.

The proof-bearing matrix product should therefore preserve a canonical Wronskian/signature rather than permit arbitrary determinant drift.

---

## 6. Canonical-system gauge: trace-normalize the Hamiltonian

A canonical system

\[
JY'=zH(t)Y,
\qquad
H(t)\succeq0,
\]

has a reparameterization freedom.

A standard gauge is

\[
\boxed{
\operatorname{tr}H(t)=1
}
\]

almost everywhere (or the measure-valued analogue).

This is potentially ideal for the SUCC/FUCC clock:

- cumulative trace mass becomes the canonical clock coordinate;
- \(H/\operatorname{tr}H\) contains only local shape/twist information;
- event strength is moved into the amount of clock time consumed rather than into arbitrary matrix magnitude.

In the causal lightcone, natural cumulative clock candidates include

\[
N,\qquad
\psi(N)=\log L_N,
\qquad
\vartheta(t)/\pi.
\]

Which one gives the correct canonical gauge must be derived, not chosen for convenience.

---

## 7. Vacuum/continuum centering should be additive, not arbitrary rescaling

The lightcone gain calculation produced the exact centered scalar impulse

\[
\boxed{
\Lambda(n)-1.
}
\]

At the completed transfer level the exact signed history is

\[
d\mu_P
+
\left(
\frac1{1-e^{-2t}}
-1-e^t
\right)dt.
\]

Therefore the correct removal of leading growth is already supplied by the Archimedean/boundary sector.

One should **not** additionally divide the prime matrix by

\[
\pi(N),\quad
N,\quad
\|G_N\|_F,
\]

or any other horizon-dependent scalar merely to make it numerically finite.

Such normalization can erase the exact bulk/sign structure being tested.

Use exact analytic centering first; use correlation normalization only as an inertia-preserving diagnostic.

---

## 8. Signed completed sector: separate magnitude from signature

The completed prime+Archimedean distribution is signed.

Do not take arbitrary complex square roots of negative event masses.

Instead use:

- positive half-density magnitudes \(\sqrt{|d\nu|}\);
- an explicit signature operator \(J\) carrying the sign.

Schematically,

\[
\boxed{
\text{completed quadratic form}
=
B^*JB,
}
\]

before any theorem upgrades it to an ordinary positive \(B^*B\).

This keeps the known negative Archimedean/pole direction explicit and avoids hiding the Weil-positivity problem inside a complex normalization convention.

If the final construction is a Krein/Pontryagin system, \(J\) is part of the geometry.

If one later proves positivity on a quotient/subspace, that must be a theorem.

---

## 9. First-prime gauge

The first prime event \(p=2\) can fix an overall phase/orientation of the transfer product, but its physical event mass is

\[
w_{2,1}
=
\frac{\log2}{\sqrt2}.
\]

Setting that mass to \(1\) is only a basis gauge if the corresponding compensating scale is tracked separately.

Safe convention:

1. retain the physical diagonal scale \(D\);
2. use \(C=D^{-1/2}GD^{-1/2}\) for shape;
3. fix the first event's correlation phase/sign as the global orientation.

Then "the first domino sets the clock" means it fixes the gauge, not that its arithmetic weight is overwritten.

---

## 10. Recommended matrix stack

For every finite horizon maintain **three related objects**:

### Physical matrix

\[
\boxed{
G_m
}
\]

with exact prime/Gamma masses.

### Correlation matrix

\[
\boxed{
C_m
=
D_m^{-1/2}G_mD_m^{-1/2}
}
\]

for conditioning, angles, and inertia-preserving positivity diagnostics.

### Transfer matrix product

\[
\boxed{
\widehat U_m
=
\widehat M_m\cdots\widehat M_1
}
\]

with local determinant/gain factored separately.

Track in parallel:

\[
\prod_j g_j
\]

for scalar gain and

\[
\widehat U_m
\]

for twist/winding.

This cleanly separates:

\[
\boxed{
\text{mass}
\quad
\text{geometry}
\quad
\text{dynamical twist}.
}
\]

---

## 11. Concrete normalization tests

Any proposed finite matrix should pass:

1. **half-density test**  
   Does measure mass split as \(\sqrt m\) on each leg?

2. **basis-rescaling test**  
   Does the positivity/sign conclusion survive positive diagonal congruence?

3. **atomic-spacing test**  
   Are no fake \(\Delta\tau\) factors inserted into prime atoms?

4. **Wronskian test**  
   Can transfer matrices be normalized into \(SL(2,\mathbb R)\), \(SU(1,1)\), or the appropriate canonical group?

5. **vacuum-centering test**  
   Is bulk removal supplied by the exact Gamma/boundary sector rather than an arbitrary horizon normalization?

6. **signature test**  
   Are negative Archimedean directions explicit in \(J\), rather than hidden by complex square roots?

7. **quarter-density test**  
   If the target kernel coefficient is
   \((\log p)p^{-k/2}\),
   does the factor-level event amplitude scale as
   \(\sqrt{\log p}\,p^{-k/4}\)?

Failure of these tests should be treated as a normalization bug, not as arithmetic evidence.

---

## 12. Main insight

The matrix entries should indeed be normalized, but there is no single normalization.

The natural stack is:

\[
\boxed{
\text{event mass}
\to
\text{half-density on each matrix leg}
\to
\text{unit-diagonal correlation gauge}
\to
\text{unit-determinant/J-unitary transfer twist}.
}
\]

The critical exponent \(1/2\) lives at the energy/kernel level.

The operator factor therefore naturally sees \(1/4\) on each leg.

### House slogan

\[
\boxed{
\text{Don't normalize away the arithmetic.}
}
\]

\[
\boxed{
\text{Split mass into half-densities, then normalize only the gauge.}
}
\]

\[
\boxed{
\text{The determinant carries gain; the normalized transfer matrix carries twist.}
}
\]
