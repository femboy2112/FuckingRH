# SUCC/FUCC -> Weyl: exact local derivation and global RH target

**Date:** 2026-10-06  
**Status:** exact derivations + proof target + no-go controls. **RH remains open.**

This note derives Weyl/Carathéodory/Herglotz structure directly from previously constructed SUCC/FUCC objects.

The core result is not that Weyl theory resembles the arithmetic machinery. It is that several objects already derived in the project are *exactly* standard Weyl objects after the correct change of language.

---

## 1. Local prime-depth Gram is a Toeplitz moment matrix

Fix a prime \(p\) and set

\[
r=p^{-1/2}.
\]

The normalized nested-ball vectors

\[
\phi_k=p^{k/2}1_{p^k\mathbb Z_p}
\]

satisfy

\[
\boxed{
\langle\phi_j,\phi_k\rangle
=
r^{|j-k|}.
}
\]

Thus the prime-depth Gram matrix is the Toeplitz matrix

\[
G^{(p)}_{jk}=r^{|j-k|}.
\]

The Poisson kernel

\[
\boxed{
P_r(\theta)
=
\frac{1-r^2}{|1-re^{i\theta}|^2}
}
\]

has Fourier coefficients

\[
\int_0^{2\pi}
e^{in\theta}
P_r(\theta)\frac{d\theta}{2\pi}
=
r^{|n|}.
\]

Therefore

\[
\boxed{
G^{(p)}_{jk}
=
\int_{\mathbb T}
\zeta^j\overline{\zeta^k}\,
d\mu_p(\zeta),
}
\]

where

\[
d\mu_p(e^{i\theta})
=
P_r(\theta)\frac{d\theta}{2\pi}.
\]

So the local FUCC-depth Gram is already the moment matrix of a positive unit-circle spectral measure.

---

## 2. The corresponding Carathéodory/Weyl function

For \(|z|<1\), define

\[
F_p(z)
=
\int_{\mathbb T}
\frac{\zeta+z}{\zeta-z}
\,d\mu_p(\zeta).
\]

Using the Poisson measure above,

\[
\boxed{
F_p(z)
=
\frac{1+rz}{1-rz}.
}
\]

Hence

\[
\boxed{
\Re F_p(z)>0
\qquad(|z|<1).
}
\]

This is exactly a Carathéodory function, the unit-disk counterpart of a Herglotz/Weyl \(m\)-function.

Its Cayley/Schur transform is

\[
\boxed{
S_p(z)
=
\frac{F_p(z)-1}{F_p(z)+1}
=
rz.
}
\]

Thus the normalized prime-depth overlap parameter

\[
r=p^{-1/2}
\]

is literally the contraction coefficient of the local Schur/Weyl system.

No zeta zeros enter.

---

## 3. The previously found whitening filter is the Weyl denominator

The same local work produced

\[
1-rz
\]

as the whitening denominator of the prime-depth chain.

This is now automatic:

\[
F_p(z)=\frac{1+rz}{1-rz}.
\]

The denominator of the local Weyl function is exactly the whitening filter.

The local carry/high-pass factor was

\[
1-z.
\]

Hence the previously derived local transfer filter

\[
\boxed{
B_p(z)
\sim
\frac{1-z}{1-rz}
}
\]

is:

\[
\boxed{
\text{SUCC boundary derivative}
\circ
\text{inverse Weyl/whitening denominator}.
}
\]

This is an exact reinterpretation of the Round005/006 local block.

---

## 4. The local repaired density is a transformed Weyl measure

Recall

\[
D_p(\theta)
=
\ell
\sum_{k\ge1}
r^k(1-\cos k\theta),
\qquad
\ell=\log p.
\]

The identity already derived was

\[
D_p(\theta)
=
\ell\frac{r}{(1-r)^2}
(1-\cos\theta)
P_r(\theta).
\]

Since

\[
|1-e^{i\theta}|^2
=
2(1-\cos\theta),
\]

\[
\boxed{
D_p(\theta)
=
\frac{\ell r}{2(1-r)^2}
|1-e^{i\theta}|^2
P_r(\theta).
}
\]

Therefore the local positive repair is exactly the spectral measure of the Weyl state after applying the discrete SUCC boundary operator

\[
I-U.
\]

If \(U\) is multiplication by \(e^{i\theta}\) on \(L^2(\mu_p)\), then for the cyclic vector \(1\),

\[
d\mu_{(I-U)1}
=
|1-e^{i\theta}|^2d\mu_p.
\]

So the local "carry energy" is not merely analogous to Weyl theory; it is a transformed Weyl spectral measure.

---

## 5. Positive kernel formulation

Every Carathéodory function \(F\) has the positive kernel

\[
\boxed{
K_F(z,w)
=
\frac{
F(z)+\overline{F(w)}
}{
1-z\bar w
}.
}
\]

For \(F_p\),

\[
K_{F_p}(z,w)\succeq0.
\]

Using the integral representation,

\[
K_{F_p}(z,w)
=
2
\int_{\mathbb T}
\frac{
d\mu_p(\zeta)
}{
(1-\bar\zeta z)(1-\zeta\bar w)
}.
\]

Thus every finite matrix

\[
\left[
K_{F_p}(z_i,z_j)
\right]_{i,j=1}^n
\]

is positive semidefinite.

This gives a canonical finite Weyl Gram attached to each prime subsystem.

---

## 6. The finite LCM clock is a Clark/Weyl boundary family

Let

\[
U_{L,\omega}
=
C_L
+
(\omega-1)|0\rangle\langle L-1|,
\qquad
|\omega|=1.
\]

Its eigenvalues satisfy

\[
\lambda^L=\omega.
\]

Seen from the boundary vector \(|0\rangle\), its spectral measure is

\[
\mu_{L,\omega}
=
\frac1L
\sum_{\lambda^L=\omega}\delta_\lambda.
\]

Its Carathéodory function is

\[
\boxed{
F_{L,\omega}(z)
=
\frac{\omega+z^L}{\omega-z^L}
=
\frac{1+\bar\omega z^L}{1-\bar\omega z^L}.
}
\]

Thus

\[
\Re F_{L,\omega}(z)>0
\qquad(|z|<1).
\]

The associated Schur/inner function is

\[
\boxed{
\Theta_{L,\omega}(z)
=
\bar\omega z^L.
}
\]

Equivalently one can regard

\[
\Theta_L(z)=z^L
\]

as the inner function and \(\omega\) as its Clark boundary parameter.

Therefore the prime carry phases previously derived are exactly a finite unitary Weyl/Clark boundary family.

---

## 7. Prime refinement = composition of inner clocks

At a prime-power event,

\[
L\to pL.
\]

The finite-clock inner function changes by

\[
\boxed{
\Theta_{pL}(z)
=
z^{pL}
=
\Theta_L(z)^p.
}
\]

The \(p\) boundary sectors are

\[
\Theta_L(\lambda)=\omega_p^r,
\qquad
r=0,\ldots,p-1.
\]

Thus the exact decomposition

\[
C_{pL}
\cong
\bigoplus_{r=0}^{p-1}
U_L(\omega_p^r)
\]

is simultaneously:

- the carry-digit Fourier decomposition;
- a Clark boundary-family decomposition;
- the cyclotomic conductor decomposition.

For \(L=p^{k-1}\), the nontrivial-sector determinant is

\[
\Phi_{p^k}.
\]

So the Ramanujan/cyclotomic blocks and the finite Weyl boundary family are the same refinement seen in three bases.

---

## 8. Cayley transform to ordinary Weyl--Titchmarsh form

Map the upper half-plane to the disk by

\[
w=\frac{z-i}{z+i}.
\]

If \(F(w)\) has positive real part, define

\[
\boxed{
m(z)=iF\!\left(\frac{z-i}{z+i}\right).
}
\]

Then

\[
\boxed{
\Im m(z)>0
\qquad(\Im z>0).
}
\]

Thus every local prime Carathéodory function and every finite-clock Clark function gives an honest Herglotz/Nevanlinna \(m\)-function after Cayley transport.

This is the first exact SUCC/FUCC -> Weyl--Titchmarsh bridge.

---

# Part II. The global target

## 9. Center the completed zeta function

Define

\[
\boxed{
\Xi(z)
=
\xi\!\left(\frac12+iz\right).
}
\]

Then

\[
\Xi(-z)=\Xi(z),
\qquad
\Xi(\bar z)=\overline{\Xi(z)},
\]

so \(\Xi\) is even and real entire on the real axis.

Define its logarithmic-derivative response

\[
\boxed{
m_\Xi(z)
:=
-\frac{\Xi'(z)}{\Xi(z)}
=
i
\left[
-\frac{\xi'}{\xi}
\left(\frac12+iz\right)
\right].
}
\]

This is the exact completed causal transfer function previously derived, rotated into the Weyl spectral coordinate.

---

## 10. The Weyl criterion is exactly RH

### Theorem

\[
\boxed{
RH
\iff
m_\Xi
\text{ is a meromorphic Herglotz/Nevanlinna function on }\mathbb C_+.
}
\]

Here Herglotz means:

- analytic on the upper half-plane;
- \(\Im m_\Xi(z)\ge0\) there.

### Proof: RH implies Herglotz

Under RH the zeros of \(\Xi\) are real:

\[
\pm\gamma.
\]

Because the zero count is \(O(T\log T)\),

\[
\sum_\gamma\frac1{\gamma^2}<\infty.
\]

The symmetric canonical product yields

\[
\Xi(z)
=
\Xi(0)
\prod_{\gamma>0}
\left(
1-\frac{z^2}{\gamma^2}
\right)^{m_\gamma}.
\]

Hence

\[
\boxed{
m_\Xi(z)
=
\sum_{\gamma>0}
m_\gamma
\left[
\frac1{\gamma-z}
-
\frac1{\gamma+z}
\right].
}
\]

For \(\Im z>0\),

\[
\Im\frac1{\gamma-z}>0
\]

and

\[
\Im\left(-\frac1{\gamma+z}\right)>0.
\]

Thus

\[
\Im m_\Xi(z)>0
\]

unless the zero measure is empty.

So \(m_\Xi\) is Herglotz.

### Proof: Herglotz implies RH

A Herglotz function is analytic on \(\mathbb C_+\).

Every zero of \(\Xi\) is a pole of

\[
-\Xi'/\Xi
\]

with residue equal to minus its positive multiplicity.

If an off-critical zeta zero has

\[
\rho=\beta+i\gamma,
\qquad
\beta<\frac12,
\]

then its \(z\)-coordinate is

\[
z_\rho
=
\gamma+i\left(\frac12-\beta\right)
\in\mathbb C_+.
\]

Hence \(m_\Xi\) would have a pole in the upper half-plane, contradicting the Herglotz property.

Functional-equation symmetry pairs every \(\beta>1/2\) zero with one having \(\beta<1/2\).

Therefore no off-critical zeros exist.

\[
\boxed{RH.}
\]

---

## 11. Off-line zero = forbidden Weyl pole

The earlier gain/loss picture becomes exact in Weyl coordinates.

For

\[
\rho=\frac12+\alpha+i\gamma,
\]

the corresponding \(\Xi\)-zero is

\[
\boxed{
z_\rho
=
\gamma-i\alpha.
}
\]

So:

- \(\alpha=0\): pole lies on the real Weyl spectrum;
- \(\alpha<0\): pole enters \(\mathbb C_+\);
- \(\alpha>0\): reflected partner enters \(\mathbb C_+\).

Thus an off-line quartet is exactly a non-real pole pair of the candidate Weyl function.

RH says:

\[
\boxed{
\text{the completed boundary response has no poles off the self-adjoint spectral boundary.}
}
\]

---

## 12. The Pick kernel form

For a Herglotz function,

\[
\boxed{
K_m(z,w)
=
\frac{
m(z)-\overline{m(w)}
}{
z-\bar w
}
}
\]

is positive semidefinite.

Under RH,

\[
\boxed{
K_\Xi(z,w)
=
\sum_{\lambda\in\mathcal Z_\Xi}
\frac{
m_\lambda
}{
(\lambda-z)(\lambda-\bar w)
}
\succeq0,
}
\]

with the usual symmetric/regularized interpretation.

Therefore RH is equivalently a positivity statement for every finite Weyl Pick matrix

\[
\left[
K_\Xi(z_i,z_j)
\right]_{i,j=1}^n.
\]

This is the spectral-domain Weyl counterpart of the Suzuki/Weil Gram positivity already studied in the repository.

---

## 13. Relation to Suzuki's screw function

Under RH the same positive zero measure gives

\[
\Psi(t)
=
\sum_\gamma
\frac{1-\cos(\gamma t)}{\gamma^2}.
\]

Thus the Weyl spectral measure behind \(m_\Xi\) also gives

\[
\boxed{
\Psi(t)
=
\int_{\mathbb R}
\frac{1-\cos(\lambda t)}{\lambda^2}
\,d\nu_\Xi(\lambda).
}
\]

Therefore:

\[
\boxed{
\text{Weyl/Herglotz positivity}
\quad\leftrightarrow\quad
\text{positive zero spectral measure}
\quad\leftrightarrow\quad
\text{Suzuki screw positivity}.
}
\]

This is not a new proof criterion.

It identifies the Weyl program as the **spectral-domain realization of the same global positivity wall**.

The proof-bearing value must come from deriving the Herglotz property from the SUCC/FUCC causal construction rather than assuming the zero measure.

---

# Part III. What the causal arithmetic must construct

## 14. Exact completed causal transform

Previous work constructed

\[
d\mathfrak W(t)
=
d\mu_P(t)
+
\left[
\frac1{1-e^{-2t}}
-1-e^t
\right]dt,
\]

where

\[
d\mu_P(t)
=
\sum_{p,k}
(\log p)\delta_{k\log p}(dt).
\]

For suitable basepoints in the initial convergence region,

\[
-\frac{\xi'}{\xi}(s)
+
\frac{\xi'}{\xi}(s_0)
=
\int_0^\infty
\left(
e^{-st}-e^{-s_0t}
\right)
d\mathfrak W(t).
\]

Therefore \(m_\Xi\) is already known as the analytic continuation of a causal prime/Gamma history transform.

The remaining task is to realize this same function as the Weyl boundary coefficient of a positive/self-adjoint system.

---

## 15. The required commutative diagram

The desired derivation is

\[
\boxed{
\begin{array}{ccc}
\text{SUCC/FUCC causal history}
&\longrightarrow&
\text{boundary transfer cocycle}
\\[1mm]
\downarrow
&&
\downarrow
\\[1mm]
-\xi'/\xi
&\longrightarrow&
m_\Xi=-\Xi'/\Xi
\\[1mm]
&&
\downarrow
\\[1mm]
&&
\text{Herglotz}
\end{array}
}
\]

The top-right-to-bottom arrow must be proved structurally from passivity/positivity of the causal system.

The left-to-right identification must be proved from the explicit prime/Gamma history.

Doing either one alone does not prove RH.

Doing both independently would.

---

## 16. The local prime systems already satisfy the Weyl positivity axiom

For every prime:

\[
F_p(z)=\frac{1+p^{-1/2}z}{1-p^{-1/2}z}
\]

has positive real part.

Thus every local FUCC-depth system is passive/Weyl.

Every finite LCM clock boundary family likewise has positive Carathéodory response.

So local Weyl positivity is **already proved**.

The obstruction is global assembly.

This precisely matches prior rounds:

- each prime repair is positive;
- the direct positive sum diverges;
- the completion requires signed prime/Gamma interaction.

---

## 17. Why direct summation is the wrong Weyl assembly

A Herglotz function has representation

\[
m(z)
=
a+bz
+
\int_{\mathbb R}
\left(
\frac1{t-z}
-\frac{t}{1+t^2}
\right)
d\nu(t),
\]

with

\[
\int\frac{d\nu(t)}{1+t^2}<\infty.
\]

The direct sum of all local prime Weyl measures fails the required global integrability for the same reason the local positive repairs diverge.

Therefore the global Weyl measure cannot be obtained as the naive positive direct sum of the local prime measures.

The arithmetic must **interconnect/cascade** the local systems before taking the global boundary response.

This is a strong structural constraint.

---

## 18. What success would look like

Construct finite causal systems

\[
\mathcal S_N
\]

from:

- LCM clock refinement;
- exact-conductor Ramanujan blocks;
- cyclotomic carry twists;
- critical half-density normalization;
- the inverse-SUCC/Gamma completion;

and boundary responses

\[
m_N(z).
\]

Prove:

### A. Causal consistency

\[
\mathcal S_N
\hookrightarrow
\mathcal S_{N+1}
\]

is generated only from the previous state and the next SUCC event.

### B. Weyl positivity

\[
\Im m_N(z)\ge0
\qquad
(\Im z>0)
\]

for every \(N\), by a structural passive/self-adjoint realization.

### C. Limit-point uniqueness

\[
m_N(z)\to m(z)
\]

locally uniformly, independently of tail/gauge choices.

### D. Arithmetic identification

\[
\boxed{
m(z)=m_\Xi(z)
=
-\frac{\Xi'(z)}{\Xi(z)}.
}
\]

Then \(m_\Xi\) is Herglotz and RH follows.

---

## 19. Honest conclusion

The SUCC/FUCC machinery already contains exact local Weyl theory:

\[
\boxed{
\text{p-adic FUCC ball overlaps}
\to
\text{Poisson spectral measure}
\to
\text{Carathéodory function}
}
\]

and

\[
\boxed{
\text{LCM carry boundary}
\to
\text{Clark family}
\to
\text{finite unitary Weyl function}.
}
\]

The completed zeta side supplies an exact global Weyl target:

\[
\boxed{
RH
\iff
-\Xi'/\Xi
\text{ is Herglotz}.
}
\]

The missing theorem is now sharply isolated:

\[
\boxed{
\textbf{show that the causal interconnection of the local SUCC/FUCC Weyl systems has boundary response }-\Xi'/\Xi.
}
\]

If the interconnection is positive/passive by construction, RH then follows from standard Weyl theory.

That is the precise program.
