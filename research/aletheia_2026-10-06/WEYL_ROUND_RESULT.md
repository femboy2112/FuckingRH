# Weyl round result: SUCC/FUCC has reached an established zeta canonical-system seam

**Date:** 2026-10-06  
**Branch:** \`aletheia/succ-fucc-weyl-2026-10-06\`  
**Outcome:** substantial exact structural progress; **RH remains open**.

## 1. Executive result

The project no longer has merely a Weyl analogy.

Several previously derived SUCC/FUCC objects are exactly standard Weyl/Schur/Clark objects, and the finite exact-conductor blocks connect directly to arithmetic coefficients in Masatoshi Suzuki's canonical-system construction for the Riemann xi-function.

The central chain is now:

\[
\boxed{
\text{finite SUCC conductor blocks}
\to
\text{prime Schur defects}
\to
c_\omega(n)
\to
\text{Suzuki causal/Hankel kernel}
\to
\text{Fredholm determinant ratio}
\to
\text{2x2 canonical system}.
}
\]

At the critical half-density point:

\[
\boxed{
c_{1/2}(n)
=
\frac{\varphi(n)}{\sqrt n}
=
n^{-1/2}\dim W_n.
}
\]

In log coordinates, Suzuki's kernel is exactly a causal convolution of arithmetic events at \(\log n\) with one universal Archimedean impulse response.

This is the strongest direct bridge so far from the project's integer/carry geometry to an established zeta canonical system.

---

## 2. Exact local Weyl identifications obtained independently

### p-adic depth Gram

\[
\langle\phi_j,\phi_k\rangle
=
r^{|j-k|},
\qquad
r=p^{-1/2}.
\]

This is the Toeplitz moment matrix of the Poisson measure.

### Local prime Carathéodory function

\[
\boxed{
F_p(z)
=
\frac{1+rz}{1-rz}.
}
\]

### Local Schur function

\[
\boxed{
S_p(z)=rz.
}
\]

### Local carry filter

\[
\boxed{
B_p(z)
\sim
\frac{1-z}{1-rz}.
}
\]

Thus the old whitening denominator is the Weyl denominator, and the SUCC difference supplies the high-pass/carry numerator.

---

## 3. Exact conductor blocks

For conductor \(q\),

\[
W_q
=
\text{exact-conductor additive-character subspace},
\]

\[
\dim W_q=\varphi(q).
\]

The orthogonal projector has Ramanujan-sum matrix

\[
(P_q)_{mn}
=
\frac1q c_q(m-n).
\]

Successor restricted to \(W_q\) has

\[
\boxed{
\det(zI-U_q)=\Phi_q(z).
}
\]

For prime powers these determinants telescope to the local Euler factor.

---

## 4. Cyclotomic boundary Weyl response

Let \(v_q\) be the canonical carry-boundary vector in \(W_q\).

Then

\[
R_q(x)
=
\langle v_q,(I-xU_q)^{-1}v_q\rangle
\]

satisfies

\[
\boxed{
R_q(x)
=
1-\frac{x}{\varphi(q)}
\frac{\Phi_q'(x)}{\Phi_q(x)}.
}
\]

Therefore the scale-by-scale Euler innovation is

\[
\boxed{
-\partial_s\log\Phi_{p^k}(p^{-s})
=
(\log p)\varphi(p^k)
[
1-R_{p^k}(p^{-s})
].
}
\]

So the cyclotomic determinant and its logarithmic source response belong to one finite Weyl boundary block.

---

## 5. Prime channels are Schur on the Weyl half-plane

Use

\[
s=\frac12-iz.
\]

Define

\[
q_p(z)=p^{-s}=p^{-1/2+iz}.
\]

For every \(z\in\mathbb C_+\),

\[
|q_p(z)|<1.
\]

Therefore each prime is already a Schur channel.

Its Cayley response is

\[
F_p(z)
=
\frac{1+q_p(z)}{1-q_p(z)}.
\]

On the real boundary,

\[
\Re F_p(t)
=
P_{p^{-1/2}}(t\log p),
\]

exactly the p-adic Poisson spectral density.

Thus:

\[
\boxed{
\text{FUCC Haar overlap}
=
\text{Euler local coordinate}
=
\text{Weyl density}.
}
\]

---

## 6. Euler log derivative is a centered Weyl sum

In the safe region,

\[
\boxed{
-\frac{\zeta'}{\zeta}
\left(\frac12-iz\right)
=
\frac12
\sum_p
(\log p)
[
F_p(z)-1
].
}
\]

Prime powers are the geometric expansion of the same local Schur channel:

\[
F_p-1
=
2\sum_{k\ge1}q_p^k.
\]

The difficult operation is therefore not local prime dynamics.

It is the infinite **centering/renormalization** and Archimedean completion.

---

## 7. Phase dance can be arbitrary inside a fixed transfer group

For a conductor phase \(\omega\), set

\[
\alpha=p^{-1/2}\omega.
\]

Then

\[
\boxed{
M_\alpha
=
\frac1{\sqrt{1-|\alpha|^2}}
\begin{pmatrix}
1&\alpha\\
\bar\alpha&1
\end{pmatrix}
\in SU(1,1).
}
\]

Arbitrary chronological products remain \(SU(1,1)\).

After Cayley conjugation they act through \(SL(2,\mathbb R)\) on the upper half-plane and preserve the Herglotz class.

Thus the microscopic carry phases need not be simple or predictable.

The invariant group geometry can be rigid while the path looks random.

---

## 8. Global Weyl target

Define

\[
\Xi(z)=\xi(1/2+iz)
\]

and

\[
\boxed{
m_\Xi(z)
=
-\frac{\Xi'(z)}{\Xi(z)}.
}
\]

Then

\[
\boxed{
RH
\iff
m_\Xi
\text{ is a meromorphic Herglotz function on }\mathbb C_+.
}
\]

An off-critical zero becomes a forbidden upper-half-plane Weyl pole.

This is equivalent to the old Suzuki/Weil positivity wall, but in spectral boundary-response language.

---

## 9. Safe-region proof architecture

Using instead

\[
s=\frac12-iz,
\]

the ordinary Euler half-plane

\[
\Re s>1
\]

is exactly

\[
\Im z>\frac12,
\]

an open subset of the Weyl upper half-plane.

Therefore a proof would follow from finite causal Herglotz approximants \(m_N\) satisfying only:

1. finite passivity on all of \(\mathbb C_+\);
2. convergence to \(m_\Xi\) on the safe region \(\Im z>1/2\).

After Cayley transform, Montel normal-family compactness + analytic uniqueness + maximum modulus rule out any off-line zero.

Direct critical-line convergence is not required.

---

## 10. Passivity abscissa

For real \(\sigma\),

\[
m_\sigma(z)
=
i\frac{\xi'}{\xi}(\sigma-iz).
\]

If

\[
\beta_*=\sup_\rho\Re\rho,
\]

then the completed Weyl passivity threshold is

\[
\boxed{
\beta_*
=
\inf\{
\sigma:
m_\sigma\text{ is Herglotz}
\}.
}
\]

Thus

\[
\boxed{
RH
\iff
\beta_*=\frac12.
}
\]

Every individual prime channel is Schur for every \(\sigma>0\).

The nontrivial threshold is therefore collective.

---

## 11. Gamma no-go

The bare centered Gamma scattering factor has real-axis unit modulus, but its upper-half-plane trivial-zero ladder fails the Blaschke condition.

Therefore Gamma alone is not an inner/Schur Weyl channel.

This proves that the arithmetic trivial-zero/Gamma cancellation must occur before the completed global Weyl positivity test.

Boundary unitarity alone is insufficient.

---

# Part II. Exact connection to Suzuki's canonical system

## 12. Suzuki's scattering family

Suzuki studies

\[
\boxed{
\Theta_\omega(z)
=
\frac{
\xi(\frac12-\omega-iz)
}{
\xi(\frac12+\omega-iz)
}.
}
\]

Meromorphic innerness of this family is directly tied to zero-free regions.

A canonical system associated with it is explicitly constructed in a safe parameter range via an arithmetic Hankel operator and Fredholm determinants.

---

## 13. Suzuki's coefficient equals a product of our local Weyl defects

Suzuki's coefficient is

\[
c_\omega(n)
=
n^\omega
\prod_{p\mid n}
(1-p^{-2\omega}).
\]

Our generalized local prime contraction is

\[
A_{p,\omega}=p^{-\omega}U_p.
\]

Its defect mass is

\[
1-\|A_{p,\omega}\|^2
=
1-p^{-2\omega}.
\]

Therefore

\[
\boxed{
c_\omega(n)
=
n^\omega
\prod_{p\mid n}
(\text{prime Weyl defect mass}).
}
\]

This is an exact local-to-global identification.

---

## 14. At \(\omega=1/2\), Suzuki's coefficient is our weighted conductor dimension

\[
\boxed{
c_{1/2}(n)
=
\frac{\varphi(n)}{\sqrt n}
=
n^{-1/2}\dim W_n.
}
\]

Equivalently,

\[
c_{1/2}(n)
=
n^{-1/2}\operatorname{Tr}P_n.
\]

So the critical half-density and exact-conductor multiplicity combine exactly into the established canonical-system arithmetic coefficient.

---

## 15. Suzuki kernel is a causal convolution in log time

Define

\[
\mathfrak h_\omega(t)
=
e^{t/2}h_\omega(e^t).
\]

Then

\[
\boxed{
\mathfrak h_\omega(t)
=
\sum_{\log n\le t}
b_\omega(n)
K_\omega(t-\log n),
}
\]

where

\[
b_\omega(n)
=
\frac{c_\omega(n)}{\sqrt n}
\]

and

\[
K_\omega(r)
=
e^{-r/2}g_\omega(e^{-r})1_{r\ge0}.
\]

At \(\omega=1/2\),

\[
\boxed{
b_{1/2}(n)
=
\frac{\varphi(n)}n
=
\frac{\dim W_n}{n}.
}
\]

Therefore Suzuki's kernel is literally an arithmetic event train convolved with one Archimedean causal response.

---

## 16. Integer seams and critical singularity

Near event birth,

\[
K_\omega(r)\sim C_\omega r^{\omega-1}.
\]

Thus the event response is locally \(L^2\) iff

\[
\omega>\frac12.
\]

At

\[
\omega=\frac12,
\]

the universal event singularity is

\[
r^{-1/2}.
\]

This explains why the half-density threshold simultaneously appears in:

- conductor normalization;
- prime Schur radius;
- kernel regularity;
- canonical-system operator class.

---

## 17. Finite horizon is genuinely finite arithmetically

After logarithmic conjugation, Suzuki's Hankel kernel is

\[
\mathfrak h_\omega(u+v).
\]

The event \(n\) is active only if

\[
u+v\ge\log n.
\]

For truncation \(x,y<a\), only

\[
n<a^2
\]

can contribute.

Thus the finite arithmetic state space

\[
\boxed{
\mathcal K_a
=
\bigoplus_{n\le a^2}W_n
}
\]

contains all causally active conductor blocks.

New arithmetic blocks enter at

\[
a=\sqrt n.
\]

This is the exact growing finite-system shadow.

---

## 18. Established canonical-system endpoint

Suzuki defines a truncated Hankel operator \(H_{\omega,a}\) and, in the established safe range, a determinant ratio

\[
m_\omega(a)
=
\frac{\det(1+H_{\omega,a})}
{\det(1-H_{\omega,a})}.
\]

The canonical Hamiltonian is diagonal, schematically

\[
\boxed{
\begin{pmatrix}
m_\omega(a)^{-2}&0\\
0&m_\omega(a)^2
\end{pmatrix}.
}
\]

So the large boundary-interaction operator is compressed into a \(2\times2\) canonical system.

This is the standard-theory realization of the matrix intuition independently developed in the project.

---

# Part III. What remains genuinely open

## 19. The highest-value seam

The existing continuum/Hilbert--Schmidt construction becomes technically difficult precisely when the integer-boundary singularities cease to be \(L^2\):

\[
0<\omega\le\frac12.
\]

The SUCC/FUCC machinery suggests replacing the smeared arithmetic singularities by explicit finite conductor/carry blocks before taking the operator limit.

The target is:

\[
\boxed{
\text{construct the Suzuki canonical/Hankel system from discrete conductor boundary blocks for }0<\omega\le1/2
}
\]

without assuming RH/innerness.

---

## 20. What would count as genuine progress

A useful next result would be one of:

### A. Exact block factorization

Represent \(H_{\omega,a}\) or an equivalent boundary response as a finite/block interconnection over

\[
W_n,\qquad n\le a^2,
\]

plus one universal Archimedean channel.

### B. Finite passivity theorem

Prove every finite block realization is Schur/Herglotz even in the non-\(L^2\) range.

### C. Fredholm/transfer identity

Prove the block network determinant ratio equals Suzuki's

\[
\det(1+H_{\omega,a})/\det(1-H_{\omega,a})
\]

where both are defined.

### D. Controlled extension below \(1/2\)

Use the block realization to define the same canonical evolution when the scalar kernel representation is not Hilbert--Schmidt, and prove positivity/invertibility.

Any of these would be new bridge work.

---

## 21. What does NOT count

The following are now known to be insufficient:

- naive direct sum of positive prime blocks;
- bare profinite-clock Weyl limit;
- scalar Euler determinant alone;
- bare Gamma as an inner channel;
- phase locking on the critical line;
- simply restating that \(m_\Xi\) must be Herglotz;
- choosing a canonical Hamiltonian from known zeros.

---

## 22. Round conclusion

The project has reached a legitimate established spectral seam.

The exact new synthesis is:

\[
\boxed{
\text{SUCC exact conductors}
\to
\text{local Schur defects}
\to
\text{Suzuki arithmetic coefficients}
\to
\text{causal Hankel kernel}
\to
\text{canonical system}.
}
\]

The half-density point is not merely recurring numerology:

\[
\boxed{
c_{1/2}(n)
=
\frac{\varphi(n)}{\sqrt n}
}
\]

and the associated event response is exactly at the \(L^2\) boundary.

The open problem is no longer "where does Weyl enter?"

It is:

\[
\boxed{
\textbf{Can explicit finite SUCC/FUCC conductor blocks carry Suzuki's canonical system through the critical non-}L^2\textbf{ seam?}
}
\]

That is the next serious research round.
