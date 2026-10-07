> **Stronger corrected raw-parent theorem (2026-10-07):** [LOG_EXTENSION_FESHBACH_THEOREM.md](LOG_EXTENSION_FESHBACH_THEOREM.md) proves Suzuki's log kinetic **plus boundary potential** equals a single positive zero-extension square minus a finite scalar. The natural positive physical parent is therefore `E_{2a}+E_prime`, not the prime-only degree-zero cube Gram. This parent is source-defined and has explicit log-growing eigenvalue bounds. Remaining low-mode Feshbach positivity is not supplied by the cube and remains RH-equivalent.

# Prime-support superconnection: a global cubical Dirac/Hodge parent for the Suzuki-Weil edge energy

> **2026-10-07 proof-bearing audit:** The finite supercharge and its positive shorted Gram are valid algebraically, but the prime-only degree-zero Gram is bounded on L2 and therefore **cannot equal the full localized Weil form**, which has logarithmically unbounded Archimedean high-frequency energy. See [the exact UV and boundary no-go theorems](RH_PROOF_BEARING_FRAME_AUDIT.md). The claimed completed pushforward remains UNVERIFIED; finite positivity is not RH progress.

**Date:** 2026-10-07  
**Status:** exact finite-dimensional operator architecture and exact two-direction Schur theorem. Multi-prime numerical probes are finite controls. The completed Weil/Suzuki pushforward identity is **UNVERIFIED**.  
**RH remains open.**

This note globalizes the support-cube program.

The finite prime/event support cube is promoted to a graded exterior algebra. The oriented SUCC boundary legs become the coefficients of a covariant exterior derivative. Its failure to square to zero is exactly the arithmetic interaction curvature already derived in the two-prime notes.

The self-adjoint supercharge

\[
\boxed{
\mathcal D_\omega
=
\nabla_\omega+\nabla_\omega^*
}
\]

has

\[
\boxed{
\mathcal H_\omega
=
\mathcal D_\omega^2
\succeq0.
}
\]

The degree-zero block is the positive prime-event edge energy. Higher support sectors couple back through curvature, and their Schur elimination subtracts a positive correction while preserving positivity.

This is the first systematic global cube mechanism found in the repository that:

1. starts from independently defined arithmetic/SUCC data;
2. automatically generates the mixed-conductor hierarchy;
3. avoids the common-mode and forbidden-ratio cross-term pathologies;
4. produces a nontrivial positive renormalization of the degree-zero sector.

The remaining theorem debt is exact identification of that renormalized sector, together with the Archimedean/pole channel, with the localized Weil form.

---

# 1. Finite event directions

Fix a finite horizon \(N\).

Let

\[
\mathcal Q_N
=
\{q=p^k:q\le N\}
\]

be the active prime-power event set.

For each \(q\), choose the normalized exact-depth support wake

\[
\boxed{
\beta_q\in W_q,
\qquad
\|\beta_q\|_{L^2(\mathbb Z/L_N\mathbb Z)}=1.
}
\]

For prime \(q=p\), this is the normalized centered boundary wake

\[
\beta_p(n)
=
\sqrt{\frac p2}
\left(
1_{n\equiv-1\pmod p}
-
1_{n\equiv0\pmod p}
\right).
\]

For higher prime powers, project the analogous boundary wake to the exact-conductor space \(W_{p^k}\) and normalize.

Let

\[
S
\]

be cyclic SUCC on the common finite clock.

Define the oriented support leg

\[
\boxed{
E_q
=
S M_{\beta_q}.
}
\]

This is nonreducing in conductor coordinates because multiplication by \(\beta_q\) fuses conductor labels.

---

# 2. Continuum event leg

Let

\[
\mathcal H_{\rm cont}
=
L^2(\mathbb R)
\]

and

\[
T_q
=
\tau_{\log q}.
\]

The first Suzuki/Weil event weight is

\[
\boxed{
w_q
=
\frac{\Lambda(q)}{\sqrt q}.
}
\]

Define the first-jet oriented continuum leg

\[
\boxed{
A_q
=
\sqrt{w_q}\,
E_q\otimes(T_q-I).
}
\]

For the nonlinear Suzuki deformation one may instead use

\[
\boxed{
A_{q,\omega}
=
\sqrt{
\frac{b_\omega(q)}{2\omega}
}
E_q\otimes(T_q-I),
}
\]

because

\[
\frac{
b_\omega(q)
}{
2\omega
}
\longrightarrow
\frac{\Lambda(q)}{\sqrt q}
=
w_q
\]

for every prime power \(q\).

Thus

\[
A_{q,\omega}\to A_q
\]

as \(\omega\downarrow0\).

---

# 3. The support cube as an exterior algebra

Let

\[
V_N
=
\mathbb C^{\mathcal Q_N}
\]

with orthonormal basis

\[
e_q,
\qquad
q\in\mathcal Q_N.
\]

Form the exterior algebra

\[
\boxed{
\mathcal F_N
=
\Lambda^\bullet V_N.
}
\]

The basis vectors

\[
e_{q_1}\wedge\cdots\wedge e_{q_r}
\]

are oriented \(r\)-faces of the event cube.

Let

\[
c_q^\dagger
\]

be exterior creation

\[
c_q^\dagger\alpha
=
e_q\wedge\alpha,
\]

and

\[
c_q=(c_q^\dagger)^*.
\]

They satisfy the CAR relations

\[
\boxed{
c_q^\dagger c_r^\dagger
=
-c_r^\dagger c_q^\dagger,
}
\]

\[
\boxed{
c_qc_r^\dagger+c_r^\dagger c_q
=
\delta_{qr}I.
}
\]

If one wants the coarser **prime-support** rather than prime-power-event cube, replace \(V_N\) by one odd local prime space with depth as an internal color. The event cube is used here because it reproduces the Weil prime-power edge energy exactly at degree zero.

---

# 4. Arithmetic covariant exterior derivative

On

\[
\mathcal F_N
\otimes
L^2(\mathbb Z/L_N\mathbb Z)
\otimes
\mathcal H_{\rm cont},
\]

define

\[
\boxed{
\nabla
=
\sum_{q\in\mathcal Q_N}
c_q^\dagger\otimes A_q.
}
\]

This is the arithmetic covariant exterior derivative.

If all \(A_q\) commuted, then the CAR antisymmetry would give

\[
\nabla^2=0.
\]

But the SUCC-oriented support legs do not commute.

Directly:

\[
\boxed{
\nabla^2
=
\sum_{q<r}
c_q^\dagger c_r^\dagger
\otimes
[A_q,A_r].
}
\]

Thus:

\[
\boxed{
F=\nabla^2
}
\]

is literally the curvature of the support-cube connection.

This gives a mathematically standard meaning to the phrase **arithmetic interaction curvature**.

---

# 5. Bare CRT is flat

If one removes the common SUCC transport and uses only multiplication fields

\[
M_{\beta_q},
\]

then they commute:

\[
[M_{\beta_q},M_{\beta_r}]=0.
\]

Therefore

\[
\boxed{
\nabla_{\rm CRT}^2=0.
}
\]

So the bare support cube is flat.

The nonzero curvature is generated specifically by chronological SUCC transport.

This passes the required hostile control.

---

# 6. Curvature has the exact mixed-conductor grading

For coprime prime-power directions \(q,r\),

\[
[E_q,E_r]
=
S^2M_{\Omega_{q,r}},
\]

with

\[
\Omega_{q,r}\in W_{qr}.
\]

The continuum difference factors commute, hence

\[
\boxed{
[A_q,A_r]
=
\sqrt{w_qw_r}\,
[E_q,E_r]
\otimes
(T_q-I)(T_r-I).
}
\]

Every term in the continuum factor occurs at

\[
0,\qquad
\log q,\qquad
\log r,\qquad
\log(qr).
\]

There is no ratio displacement

\[
\log(q/r).
\]

Thus curvature is **product-locked**:

\[
\boxed{
(q,r)
\longmapsto
\left(
W_{qr},
\log(qr)
\right).
}
\]

This is compatible with the conductor-graded continuum selection rule.

---

# 7. Self-adjoint supercharge and positive Hamiltonian

Define

\[
\boxed{
\mathcal D
=
\nabla+\nabla^*.
}
\]

Then

\[
\mathcal D=\mathcal D^*
\]

on the natural finite-event/common smooth continuum core.

Set

\[
\boxed{
\mathcal H
=
\mathcal D^2.
}
\]

Automatically,

\[
\boxed{
\mathcal H\succeq0.
}
\]

Expanding,

\[
\boxed{
\mathcal H
=
\nabla^*\nabla
+
\nabla\nabla^*
+
\nabla^2
+
(\nabla^*)^2.
}
\]

The first two terms are Hodge/Laplacian pieces.

The last two are curvature terms changing support degree by \(\pm2\).

Thus the mixed conductor interaction is not added by hand.

It is forced by squaring the covariant cubical Dirac operator.

---

# 8. Degree-zero block is exactly the event square

Let

\[
P_0
\]

project onto exterior degree zero.

Because

\[
\nabla^*P_0=0,
\]

we have

\[
P_0\mathcal H P_0
=
P_0\nabla^*\nabla P_0.
\]

The CAR orthogonality kills cross-event terms:

\[
\boxed{
P_0\mathcal H P_0
=
\sum_q A_q^*A_q.
}
\]

After normalized trace over the support clock,

\[
\boxed{
\tau_{\rm clock}
\langle
f,
P_0\mathcal H P_0f
\rangle
=
\sum_{q=p^k\le N}
w_q
\|(T_q-I)f\|_2^2.
}
\]

This is exactly the prime-power event contribution in the Round007 positive Weil edge square.

Therefore the cube Hamiltonian starts from the correct physical degree-zero operator.

---

# 9. Why higher support cells affect the first jet

For the nonlinear family,

\[
b_\omega(q)
=
2\omega w_q
+
O(\omega^2).
\]

Hence the unscaled nonlinear supercharge satisfies

\[
\boxed{
\widetilde{\mathcal D}_\omega
=
\sqrt{2\omega}\,
\mathcal D
+
O(\omega^{3/2}).
}
\]

Therefore

\[
\boxed{
\frac{
\widetilde{\mathcal D}_\omega^2
}{
2\omega
}
\longrightarrow
\mathcal D^2
=
\mathcal H.
}
\]

So the **first** Suzuki/Weil tangent already contains the entire cubical curvature hierarchy generated by the square-root opening amplitudes.

This is the key scaling mechanism.

Although a scalar mixed-conductor event \(qr\) has direct weight

\[
b_\omega(qr)=O(\omega^2),
\]

the curvature **amplitude**

\[
[A_{q,\omega},A_{r,\omega}]
\]

is already \(O(\omega)\), because it is a product of two \(O(\sqrt\omega)\) legs.

Thus higher support geometry can renormalize the first Weil jet without singular rescaling.

---

# 10. Even-sector Schur renormalization

Because \(\mathcal H=\mathcal D^2\) changes support degree by \(0,\pm2\), it preserves exterior parity.

The even sector is

\[
\boxed{
\mathcal F_N^{\rm even}
=
\Lambda^0V_N
\oplus
\Lambda^2V_N
\oplus
\Lambda^4V_N
\oplus\cdots.
}
\]

Write

\[
\mathcal H_{\rm even}
=
\begin{pmatrix}
H_{00}&H_{0h}\\
H_{h0}&H_{hh}
\end{pmatrix}
\]

relative to

\[
\Lambda^0
\oplus
\Lambda^{\ge2,\rm even}.
\]

Whenever the hidden block is invertible, or using the Moore--Penrose shorted operator in the semidefinite case, define

\[
\boxed{
H_{\rm eff}
=
H_{00}
-
H_{0h}H_{hh}^{\dagger}H_{h0}.
}
\]

Because

\[
\mathcal H_{\rm even}\succeq0,
\]

\[
\boxed{
H_{\rm eff}\succeq0.
}
\]

And

\[
\boxed{
H_{\rm eff}\preceq H_{00}.
}
\]

Therefore the higher support cube **subtracts a positive counterterm from the raw prime-event energy while preserving positivity**.

That is precisely the algebraic sign required by the Weil completion problem.

---

# 11. Exact two-direction theorem

Take two event directions and, for clarity, first suppress the continuum factor.

Let

\[
E_1=SM_{\beta_1},
\qquad
E_2=SM_{\beta_2},
\]

with real support wakes.

Define

\[
Q
=
c_1^\dagger E_1
+
c_2^\dagger E_2,
\]

\[
D=Q+Q^*.
\]

The even exterior sector is only

\[
\Lambda^0
\oplus
\Lambda^2.
\]

Set

\[
\boxed{
a(n)=\beta_1(n)^2+\beta_2(n)^2,
}
\]

and

\[
\boxed{
\Omega(n)
=
\beta_1(n+1)\beta_2(n)
-
\beta_2(n+1)\beta_1(n).
}
\]

Then

\[
\boxed{
D_{\rm even}^2
=
\begin{pmatrix}
M_{a(n)}
&
[E_1,E_2]^*
\\
[E_1,E_2]
&
M_{a(n-1)}
\end{pmatrix},
}
\]

with

\[
[E_1,E_2]
=
S^2M_\Omega.
\]

Assume

\[
a(n+1)>0.
\]

The exact Schur complement of the two-face is

\[
\boxed{
H_{\rm eff}(n)
=
a(n)
-
\frac{
|\Omega(n)|^2
}{
a(n+1)
}.
}
\]

Now put

\[
v_n
=
(\beta_1(n),\beta_2(n)).
\]

Then

\[
a(n)=\|v_n\|^2,
\]

and

\[
|\Omega(n)|
=
|\det(v_{n+1},v_n)|.
\]

Lagrange's identity gives

\[
\|v_n\|^2\|v_{n+1}\|^2
-
|\det(v_{n+1},v_n)|^2
=
|\langle v_n,v_{n+1}\rangle|^2.
\]

Therefore

\[
\boxed{
H_{\rm eff}(n)
=
\frac{
|\langle v_n,v_{n+1}\rangle|^2
}{
\|v_{n+1}\|^2
}
\ge0.
}
\]

This is an exact theorem.

Interpretation:

\[
\boxed{
\text{raw one-body energy}
-
\text{curvature area}
=
\text{parallel transported energy}.
}
\]

The two-face removes precisely the component measured by the exterior area.

---

# 12. Finite \(2,3\) control

Use the normalized prime wakes for \(p=2,3\) on

\[
\mathbb Z/6\mathbb Z.
\]

With unit leg weights, the raw degree-zero mean energy is

\[
\boxed{
2.
}
\]

After exact two-face Schur elimination, the eigenvalues are

\[
\boxed{
\left\{
\frac25,\frac25,
1,1,
\frac52,\frac52
\right\}.
}
\]

Hence the effective mean is

\[
\boxed{
\frac{13}{10}=1.3.
}
\]

The curvature sector removes

\[
\boxed{
\frac7{10}
}
\]

of the normalized mean energy while leaving a strictly positive physical operator.

So the curvature correction is nontrivial and is not the zero-saturation behavior of the carry-square parent.

---

# 13. Finite \(2,3,5\) control

On the \(30\)-clock with normalized wakes for

\[
2,3,5
\]

and unit event weights, the raw vacuum mean energy is

\[
\boxed{
3.
}
\]

Build the full exterior supercharge and eliminate all even support degrees \(2\) and above.

The finite numerical Schur mean is approximately

\[
\boxed{
1.6257142857.
}
\]

The effective spectrum remains nonnegative, with observed range

\[
\boxed{
0.2
\le\lambda
\le5.
}
\]

This is a finite diagnostic, not an asymptotic theorem.

Its role is to show that the multi-face correction remains nontrivial after adding a third support atom.

---

# 14. Relation to Gram/Plücker geometry

The two-direction theorem already exhibits the general pattern.

The one-body data are vectors

\[
v_n
\]

of local support amplitudes.

The curvature is the exterior product

\[
\boxed{
v_{n+1}\wedge v_n.
}
\]

Its squared norm is the \(2\times2\) Gram determinant.

Higher support sectors are naturally controlled by higher exterior products and Gram/Plücker coordinates.

Thus the cube Hamiltonian systematically organizes:

\[
\boxed{
\text{1-face energy}
\leftrightarrow
\text{vector norms},
}
\]

\[
\boxed{
\text{2-face curvature}
\leftrightarrow
\text{Gram determinants / wedge areas},
}
\]

\[
\boxed{
\text{higher faces}
\leftrightarrow
\text{higher Gram minors}.
}
\]

This is a genuine global Hodge-type organization of the support cube.

---

# 15. Why this escapes several previous no-gos

### Not a direct sum of local squares

The curvature terms

\[
\nabla^2
\]

couple support faces.

### Not the common-mode intersect-first construction

The support wakes are centered and exact-conductor graded; the shared identity mode is absent.

### Not factor-label reducing

Multiplication by \(\beta_q\) fuses conductor sectors.

### Not a fixed finite boundary correction

The number of exterior support sectors grows with the arithmetic horizon.

### No forbidden scalar ratio atoms at first physical compression

Distinct conductor directions are orthogonal in degree zero, while chronological curvature is product-locked into higher support degree.

These are necessary escapes, not a proof.

---

# 16. The Archimedean problem remains

The arithmetic cube by itself produces a positive effective renormalization.

But the exact completed Weil form contains:

\[
\boxed{
\text{Gamma difference energy}
}
\]

plus

\[
\boxed{
(c_0-2S_N)\|f\|^2
+
2\Re(\ell_+f\,\overline{\ell_-f}).
}
\]

A naive orthogonal Gamma exterior leg would commute with the arithmetic translations and would not generate the needed arithmetic--Archimedean curvature.

Therefore the missing object is now precise:

\[
\boxed{
\textbf{an independently derived Archimedean connection on the same cubical superconnection whose mixed curvature produces the exact Gamma/pole completion.}
}
\]

Merely appending the known Gamma square orthogonally is insufficient.

---

# 17. Proof-bearing theorem target

Construct a completed superconnection

\[
\boxed{
\nabla_{\rm comp}
=
\nabla_{\rm arith}
+
\nabla_\infty
}
\]

such that:

1. \(\nabla_{\rm arith}\) is the support-cube connection above;
2. \(\nabla_\infty\) is derived from the exact Suzuki/Gamma state-space, not fitted;
3. the full Hamiltonian
   \[
   \mathcal H_{\rm comp}
   =
   (\nabla_{\rm comp}+\nabla_{\rm comp}^*)^2
   \]
   is positive by construction;
4. its degree-zero physical shorted operator equals the localized Weil operator:
   \[
   \boxed{
   \operatorname{Short}_{0}
   \mathcal H_{\rm comp}
   =
   A_a^{\rm Weil};
   }
   \]
5. equivalently, in the nonlinear finite-Hankel formulation, its boundary transfer recovers Suzuki's
   \[
   H_{\omega,a}
   \]
   and hence finite passivity.

If those identities are proved without zero data or an RH-equivalent metric, RH follows from positivity of the completed parent.

That is the fixed theorem target.

---

# 18. Novelty discipline

Exterior/Koszul complexes, supersymmetric Dirac operators, Hodge Laplacians, adèlic/noncommutative approaches to zeta, and quantum-statistical models of primes are established mathematical themes.

Connes--Consani's arithmetic-site program seeks a geometric positivity/Hodge analogue for RH, and current zeta-spectral-triple work seeks self-adjoint spectral realizations.

No priority claim is made for the general idea “use quantum/Hodge geometry for RH.”

What is specific to this repository's present construction is the chain:

\[
\boxed{
\text{Suzuki exact conductor weights}
\to
\text{centered SUCC support wakes}
\to
\text{exact conductor fusion}
\to
\text{covariant exterior derivative}
\to
\text{curvature }[E_q,E_r]
\to
\text{positive cubical Dirac square}
\to
\text{finite Schur renormalization}.
}
\]

A literature search did not identify this exact finite construction, but that is not a novelty proof.

---

# 19. Current verdict

The cube is load-bearing in a mathematically meaningful sense.

It supplies a global algebra in which:

- support rank is exterior degree;
- prime-power events are one-form legs;
- mixed conductors are wedge sectors;
- SUCC chronology is a connection;
- arithmetic interaction curvature is \(\nabla^2\);
- positivity comes from a self-adjoint Dirac square;
- hidden support faces automatically subtract a positive Schur counterterm.

What remains is not “find a way to make the cube relevant.”

It is now one exact question:

\[
\boxed{
\textbf{Does the completed arithmetic + Archimedean superconnection push forward to Suzuki/Weil exactly?}
}
\]

That can be proved or killed.
