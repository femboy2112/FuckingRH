# Aletheia RH Master Dossier

## Ten triangulation rounds from Weil positivity to arithmetic deformation, localized selection, and unconditional density

**Research date:** 25 August 2026  
**Status:** self-contained research synthesis; exact lemmas, source-audited theorems, calibrated finite experiments, conjectural proof programs.  
**Global verdict:** **the Riemann Hypothesis is not proved here.** The dossier isolates the exact sign, proves several auxiliary structural theorems, repairs several overclaims, and separates a full-RH route from a theorem-producing partial-progress route.

---

## Truth-state convention

- **DISCLOSED** — proved here, or a cited theorem whose hypotheses match the stated claim.
- **CORROBORATED** — supported by independent derivations or source families, with no decisive unresolved defect.
- **OBSERVED** — measured in a finite computation with exact scope recorded.
- **CONJECTURED** — structurally supported, but a verdict-changing theorem remains unpaid.
- **UNVERIFIED** — an appropriate source check or proof has not been completed.
- **DARK** — no present discriminator reaches the claim; the missing instrument is named.
- **REFUTED** — killed by a proof, counterexample, or source mismatch.

Conclusions inherit the weakest load-bearing premise. Finite calculations are never promoted to asymptotic theorems.

---

# Executive synthesis

The entire program can be organized around one Hermitian form,

\[
Q_W(f)=W(f*f^\sharp),
\qquad
f^\sharp(u)=\overline{f(-u)},
\]

and one universal condition,

\[
\boxed{\mathrm{RH}\iff Q_W(f)\ge 0\quad\text{for every admissible }f.}
\]

That statement is exact, but it hides three mathematically different problems:

\[
\boxed{\text{arithmetic uniqueness}}
\quad\neq\quad
\boxed{\text{global positivity}}
\quad\neq\quad
\boxed{\text{localized spectral selection}}.
\]

1. **Arithmetic uniqueness.** The unrestricted prime multiset is the unique nonnegative one-species occupancy rule with no scaled Witt layers beyond the physical \(\zeta(s)\) layer.
2. **Global positivity.** Weil’s form must be positive on every test function. This is RH itself.
3. **Localized selection.** A finite localized Weil operator has a large near-radical; a proof through real-rooted finite approximants must show that its boundary defect selects the particular radical direction whose transform tends to \(\Xi\). Positivity alone does not identify that direction.

The ten rounds produce the following strongest outputs.

### Exact structural advances

- The correct zero coordinate is
  \[
  z_\rho=\frac{\rho-\tfrac12}{i};
  \]
  off-line pairs contribute signature \((1,1)\) blocks.
- The support/multiplicity deformation has Witt coordinates
  \[
  d_n(a,b)=M_n(b)-M_n(b-a),
  \]
  where \(M_n\) is the necklace polynomial.
- The complete real finite-Witt-support locus is classified.
- The physical point \((a,b)=(1,1)\) is first-order isolated: every nonzero infinitesimal support/repetition perturbation activates the second or third scaled layer.
- Prime occupations and additive Fourier mixing generate the full finite matrix algebra; their common commutant is scalar.
- The localized Weil form is exactly a positive nonlocal jump energy minus a scalar, plus one rank-one pole update in each parity sector.
- Pole plus smooth prime density combine into a positive Cauchy kernel; the remaining arithmetic term depends only on the centered prime fluctuation.
- A fixed self-Fourier Hermite combination generates \(\Xi/4\) exactly under the co-Poisson/Mellin map.
- A rank-one base-resolvent preconditioner replaces the exponentially tiny full-Weil gap by the conditioning of a pole-free base operator.
- A sharp four-moment finite-matrix theorem yields the conditional constants
  \[
  \frac{16}{21}\quad\text{simple on the line},
  \qquad
  \frac{37}{42}\quad\text{distinct},
  \]
  under the predicted first four trace moments and the zero-block decomposition.

### Major kills and corrections

- Writing the zero side as \(h(\Im\rho)\) before RH is established erases the horizontal displacement and is incorrect.
- A generic nonintegral Witt layer is a branch singularity, not necessarily a meromorphic zero or pole.
- Functional equations, Gamma multiplication, theta self-duality, local clock unitarity, and finite Fourier closure are identities—not positivity.
- Scalar common commutant does **not** mean the desired operator cannot be built from the generators; it means those generators impose no finite selector because they generate everything.
- A positive heat kernel or positive measure can have a transform with nonreal zeros.
- Support alone does not impose an absolute finite-zero horizon.
- A small Rayleigh quotient does not select a minimizer inside a high-dimensional near-radical.
- The previously asserted theorem “positivity persists beyond total support \(\log 2\)” is **UNVERIFIED**. Suzuki’s current source audit certifies positivity only for sufficiently small support and continuity of the lowest eigenvalue; no exact Yoshida theorem at the full \(\log 2\) threshold was verified here.
- Generic Christoffel minimization does not by itself lower-bound positive spectral mass; a one-sided majorization certificate is required.
- All fixed-moment density methods can leave a sparse off-line exceptional set; density one is not RH.

### Two selected forward tracks

\[
\boxed{\textbf{Full-RH track: pole-free base inertia, conditioning, and boundary selection.}}
\]

\[
\boxed{\textbf{Partial-theorem track: a quartic prime-side idempotence-defect bound.}}
\]

The first can imply RH if completed along one unbounded sequence. The second cannot prove RH, but any nontrivial saving can raise the unconditional proportion of simple critical-line zeros.

---

# Common notation and normalization

We use

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad
\Xi(z)=\xi\!\left(\frac12+iz\right).
\]

For \(f\in C_c^\infty(\mathbb R)\), define

\[
F(z)=\widehat f(z)=\int_{\mathbb R}f(u)e^{izu}\,du,
\qquad
f^\sharp(u)=\overline{f(-u)},
\]

\[
g=f*f^\sharp,
\qquad
h(z)=\widehat g(z).
\]

Then

\[
\boxed{h(z)=F(z)\overline{F(\bar z)}.}
\]

For real \(r\), this is \(|F(r)|^2\); for nonreal \(z\), it is generally not a modulus square.

We write

\[
\Psi(x)=\sum_{n\le x}\Lambda(n),
\qquad
\Theta(x)=\sum_{p\le x}\log p.
\]

The support interval

\[
I_L=(-L/2,L/2)
\]

has total length \(L\). Functions on \(I_L\) are extended by zero to \(\mathbb R\).

---

# Triangulation Round 1 — Recover the exact Hermitian object

## 1.1 The corrected explicit formula

For a nontrivial zero

\[
\rho=\beta+i\gamma,
\]

define its centered spectral coordinate

\[
\boxed{
z_\rho:=\frac{\rho-\tfrac12}{i}
=\gamma-i\left(\beta-\frac12\right).
}
\]

Thus

\[
z_\rho\in\mathbb R
\iff
\beta=\frac12.
\]

With the above Fourier convention, the Guinand–Weil formula can be written

\[
\begin{aligned}
\sum_\rho m_\rho h(z_\rho)
={}&h(i/2)+h(-i/2)\\
&+\frac1{2\pi}\int_{\mathbb R}h(r)
\left[
\Re\psi\!\left(\frac14+\frac{ir}{2}\right)-\log\pi
\right]dr\\
&-2\Re\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,g(\log n),
\end{aligned}
\tag{1.1}
\]

under the standard smoothness, support, and decay hypotheses. For real even autocorrelations, the final real part can be suppressed.

Writing only \(h(\gamma)\) before proving RH replaces \(z_\rho\) by its real projection and loses exactly the datum the criterion must detect. That shortcut is **REFUTED**.

## 1.2 Zero-side anatomy

The zero-side Hermitian form is

\[
Q_W(f)
=
\sum_\rho m_\rho
F(z_\rho)\overline{F(\bar z_\rho)}.
\tag{1.2}
\]

### On-line zero

If \(\rho=1/2+i\gamma\), then \(z_\rho=\gamma\in\mathbb R\), so

\[
m_\rho F(\gamma)\overline{F(\gamma)}
=m_\rho|F(\gamma)|^2.
\]

This is a positive rank-one atom.

### Off-line pair

The functional equation pairs \(\rho\) with \(1-\bar\rho\), whose centered coordinates are \(z\) and \(\bar z\). On their two evaluation coordinates \((a,b)=(F(z),F(\bar z))\), the contribution is

\[
a\bar b+b\bar a
=
\begin{bmatrix}\bar a&\bar b\end{bmatrix}
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\begin{bmatrix}a\\b\end{bmatrix}.
\]

Diagonalizing,

\[
a\bar b+b\bar a
=
\left|\frac{a+b}{\sqrt2}\right|^2
-
\left|\frac{a-b}{\sqrt2}\right|^2.
\tag{1.3}
\]

Hence every resolvable off-line pair contributes a signature \((1,1)\) block.

In the real finite-compression form used by Alpöge–Furman, if an evaluation vector is \(v=a+ib\), the pair contributes

\[
vv^{\mathsf T}+\bar v\bar v^{\mathsf T}
=2(aa^{\mathsf T}-bb^{\mathsf T}).
\tag{1.4}
\]

## 1.3 Weil’s criterion

A sufficiently rich compactly supported test class can interpolate and isolate any finite off-line pair while controlling the remaining spectrum. Consequently,

\[
\boxed{
\mathrm{RH}
\iff
Q_W(f)\ge0
\quad\text{for every admissible }f.
}
\tag{1.5}
\]

This is **DISCLOSED**: it is Weil’s positivity criterion. The infinite universal quantifier is the content. “One sign” does not mean one finite numerical inequality.

## 1.4 What symmetry gives—and what it does not

The functional equation gives an involution and a Hermitian exchange matrix. It does not select the positive diagonal polarization.

The Davenport–Heilbronn control proves the point: a Riemann-type reflection symmetry can coexist with off-line zeros. It does not have the Euler product, so it refutes “functional equation alone,” not every arithmetic positivity mechanism.

### Round-1 verdict

- Exact Hermitian target: **DISCLOSED**.
- Off-line signature mechanism: **DISCLOSED**.
- Symmetry \(\Rightarrow\) positivity: **REFUTED**.
- The first wall is best named the **polarization gap**.

---

# Triangulation Round 2 — Prime multisets, Witt layers, and q-ary clocks

## 2.1 Prime multiset Hilbert space

Let

\[
\mathcal F_{\mathbb P}
=
\ell^2\!\left(\mathbb N_0^{(\mathbb P)}\right),
\]

whose basis states are finite prime-exponent vectors

\[
|\mathbf k\rangle=|k_2,k_3,k_5,\ldots\rangle.
\]

Define occupation operators

\[
N_p|\mathbf k\rangle=k_p|\mathbf k\rangle
\]

and the multiplicative Hamiltonian

\[
\boxed{
H_\times=\sum_p(\log p)N_p.
}
\tag{2.1}
\]

Then

\[
H_\times|\mathbf k\rangle
=\log n(\mathbf k)|\mathbf k\rangle,
\qquad
n(\mathbf k)=\prod_pp^{k_p},
\]

and

\[
\operatorname{Tr}e^{-sH_\times}=\zeta(s),
\qquad \Re s>1.
\tag{2.2}
\]

The Euler trace factorizes over primes. The Gaussian heat trace

\[
K(t)=\operatorname{Tr}e^{-\pi t e^{2H_\times}}
=\sum_{n\ge1}e^{-\pi n^2t}
\tag{2.3}
\]

does not factorize over occupation coordinates: the complete prime multiset is collapsed to the single integer value and weighted globally.

Its Mellin transform gives

\[
\Gamma_{\mathbb R}(s)\zeta(s)
=
\int_0^\infty K(t)t^{s/2}\frac{dt}{t},
\qquad
\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2).
\tag{2.4}
\]

This explains the completed functional equation, but still only as an identity.

## 2.2 Support/multiplicity deformation

Define

\[
\boxed{
Z_{a,b}(s)
=
\prod_p\left(1+a\frac{p^{-s}}{1-bp^{-s}}\right)
=
\sum_{n\ge1}a^{\omega(n)}b^{\Omega(n)-\omega(n)}n^{-s}.
}
\tag{2.5}
\]

The local factor is

\[
F_{a,b}(x)=\frac{1+(a-b)x}{1-bx}
=\frac{1-(b-a)x}{1-bx}.
\]

Write

\[
\log F_{a,b}(x)=\sum_{m\ge1}\frac{c_m(a,b)}m x^m,
\]

where

\[
c_m(a,b)=b^m-(b-a)^m.
\tag{2.6}
\]

Prime-zeta Möbius inversion yields

\[
\boxed{
\log Z_{a,b}(s)
=
\sum_{n\ge1}d_n(a,b)\log\zeta(ns),
}
\tag{2.7}
\]

with

\[
\boxed{
d_n(a,b)
=
\frac1n\sum_{m\mid n}\mu(n/m)
\left[b^m-(b-a)^m\right].
}
\tag{2.8}
\]

Let the necklace polynomial be

\[
M_n(x)=\frac1n\sum_{m\mid n}\mu(n/m)x^m.
\]

Then the deformation coordinates have the elegant exact form

\[
\boxed{
d_n(a,b)=M_n(b)-M_n(b-a).
}
\tag{2.9}
\]

This is **DISCLOSED**.

## 2.3 What the scaled layers actually are

Formally,

\[
Z_{a,b}(s)=\prod_{n\ge1}\zeta(ns)^{d_n(a,b)}.
\tag{2.10}
\]

Every nonzero \(d_n\) activates singularities at

\[
s=\rho/n,
\]

with inherited reflection center

\[
\Re s=\frac1{2n}.
\]

But there is a crucial distinction:

- if \(d_n\in\mathbb Z\), the layer produces meromorphic zeros or poles;
- if \(d_n\notin\mathbb Z\), it generally produces a branch singularity.

Therefore the correct theorem is

\[
\boxed{
\text{generic support/multiplicity deformation creates a scaled zeta singularity tower.}
}
\tag{2.11}
\]

The phrase “zero tower” is valid only on integral subfamilies or after a declared branched cover.

## 2.4 Single-layer rigidity

The first coordinates are

\[
d_1=a,
\]

\[
d_2=-\frac a2(a-2b+1),
\]

\[
d_3=\frac a3(a^2-3ab+3b^2-1).
\]

If \(d_n=0\) for every \(n\ge2\), then either \(a=0\), or \(d_2=d_3=0\) gives

\[
(a,b)=(1,1),
\qquad
(a,b)=(-1,0).
\]

Thus among nonnegative weights,

\[
\boxed{(a,b)=(1,1)}
\]

is the unique nontrivial single-layer point.

## 2.5 New theorem: complete finite-Witt-support classification

### Theorem 2.1

For real \(a,b\), the sequence \((d_n(a,b))\) has finite support if and only if either

1. \(a=0\), in which case \(Z_{a,b}=1\), or
2. both \(b\) and \(b-a\) lie in \(\{0,1,-1\}\).

The nontrivial real points are exactly

\[
(-1,-1),\ (-2,-1),\ (1,0),\ (-1,0),\ (2,1),\ (1,1).
\tag{2.12}
\]

Their nonzero Witt supports are contained in \(\{1,2\}\).

### Proof

The local Euler transform is

\[
F_{a,b}(x)=\prod_{n\ge1}(1-x^n)^{-d_n}.
\]

If only finitely many \(d_n\) are nonzero, then

\[
x\frac{F'_{a,b}(x)}{F_{a,b}(x)}
=
\sum_{n\le N}\frac{nd_nx^n}{1-x^n}.
\tag{2.13}
\]

The right side can have poles only at roots of unity. The left side is

\[
\frac{bx}{1-bx}
-
\frac{(b-a)x}{1-(b-a)x}.
\tag{2.14}
\]

If \(a\ne0\), its noncancelled poles occur at \(x=1/b\) and \(x=1/(b-a)\), whenever the corresponding denominator is nonconstant. Since \(a,b\) are real, these poles can be roots of unity only when each nonzero number among \(b,b-a\) is \(1\) or \(-1\). This proves necessity. Conversely, the factors \(1-x\), \(1+x=(1-x^2)/(1-x)\), and their reciprocals have Witt support in \(\{1,2\}\), proving sufficiency. ∎

Among \(a,b\ge0\), the nontrivial finite-support points are

\[
(1,0),\qquad(1,1),\qquad(2,1).
\]

Thus the infinite tower is generic but not universal.

## 2.6 First-order isolation of the physical point

At \((1,1)\),

\[
\partial_a d_n=\frac{\mu(n)}n,
\qquad
\partial_b d_1=0,
\qquad
\partial_b d_n=\frac{\varphi(n)-\mu(n)}n\quad(n\ge2).
\tag{2.15}
\]

For \((d_2,d_3)\), the tangent Jacobian is

\[
J=
\begin{pmatrix}
-1/2&1\\
-1/3&1
\end{pmatrix},
\qquad
\det J=-\frac16\ne0.
\tag{2.16}
\]

Therefore every nonzero infinitesimal perturbation of support or repetition activates at least one of the second or third layers:

\[
\boxed{
(\delta a,\delta b)\ne(0,0)
\Longrightarrow
\delta d_2\ne0\ \text{or}\ \delta d_3\ne0.
}
\tag{2.17}
\]

The physical multiset point is transversely isolated.

## 2.7 q-ary bosonization

Every exponent has a base-\(q\) expansion. Hence

\[
\boxed{
\frac1{1-x}
=
\prod_{j\ge0}
\left(1+x^{q^j}+\cdots+x^{(q-1)q^j}\right).
}
\tag{2.18}
\]

At finite depth \(J\),

\[
\prod_{j=0}^{J-1}
\left(1+x^{q^j}+\cdots+x^{(q-1)q^j}\right)
=
\frac{1-x^{q^J}}{1-x}.
\tag{2.19}
\]

Globally,

\[
\boxed{
\frac{\zeta(s)}{\zeta(q^Js)}
=
\prod_{j=0}^{J-1}
\frac{\zeta(q^js)}{\zeta(q^{j+1}s)}.
}
\tag{2.20}
\]

For \(q=2\), one bosonic prime occupation is an infinite stack of binary bits:

\[
\zeta(s)=\prod_p\prod_{j\ge0}(1+p^{-2^js}),
\qquad \Re s>1.
\tag{2.21}
\]

Let \(C_q^\circ\) be the cyclic shift on the mean-zero subspace of \(\mathbb C^q\). Then

\[
\boxed{
\det(I-xC_q^\circ)=1+x+\cdots+x^{q-1}.
}
\tag{2.22}
\]

Furthermore,

\[
-\operatorname{tr}\bigl((C_q^\circ)^m\bigr)
=1-q\mathbf1_{q\mid m}.
\tag{2.23}
\]

Across all digit scales, carry corrections cancel exactly:

\[
\sum_{j=0}^{v_q(r)}
\frac{1-q\mathbf1_{j<v_q(r)}}{r/q^j}
=
\frac1r.
\tag{2.24}
\]

This reconstructs the prime-power coefficient in \(\log\zeta\) from canonical finite clocks.

## 2.8 Support creates; multiplicity purifies

If prime support is finite, the finite Euler product has no nontrivial zeta zeros. If all primes are present but exponents are capped at \(K-1\),

\[
Z_K(s)=\frac{\zeta(s)}{\zeta(Ks)}.
\tag{2.25}
\]

The numerator already contains the physical zeta divisor, while the denominator contributes a residual scaled divisor at \(s=\rho/K\). Therefore

\[
\boxed{
\text{all-prime support creates the physical divisor; unlimited multiplicity removes the residual scaled divisor.}
}
\tag{2.26}
\]

### Round-2 verdict

- Multiset uniqueness: **DISCLOSED within the declared family**.
- Generic scaled singularity tower: **DISCLOSED**.
- Universal “zero tower” wording: **REFUTED without integrality**.
- Finite-Witt-support classification: **DISCLOSED here; literature priority UNVERIFIED**.
- q-ary clock decomposition: **DISCLOSED**.

---

# Triangulation Round 3 — Additive–multiplicative irreducibility

## 3.1 Full finite matrix algebra

Take a finite family of distinct positive integers as basis states. Their joint valuation vectors

\[
(v_p(n))_p
\]

separate the states, so the algebra generated by the prime-occupation matrices contains every diagonal projector \(E_{ii}\).

Let \(F_N\) be a discrete Fourier matrix; every entry is nonzero. Then

\[
E_{ii}F_NE_{jj}=(F_N)_{ij}E_{ij}.
\]

Thus every matrix unit belongs to the generated algebra:

\[
\boxed{
\operatorname{Alg}(\{N_p\},F_N)=M_N(\mathbb C).
}
\tag{3.1}
\]

By Burnside’s theorem,

\[
\boxed{
\{N_p,F_N\}'=\mathbb CI.
}
\tag{3.2}
\]

This is **DISCLOSED**.

## 3.2 Correct interpretation

The theorem kills the easy plan

\[
\text{find a nontrivial observable commuting separately with every }N_p\text{ and }F_N.
\]

It does **not** imply that an RH operator cannot be built from those generators. Since they generate all matrices, every finite candidate can be written from them. Membership in the generated algebra is therefore vacuous as a selector.

The missing constraints must survive the infinite limit:

- scale covariance;
- locality or controlled nonlocality;
- compatibility of truncations;
- a trace formula;
- positivity established independently of the zeros;
- norm-, strong-, or resolvent convergence.

The prior finite search for an operator commuting with the localized Weil matrix is a different problem. Scalar common commutant of \(\{N_p,F_N\}\) does not prove that no operator can commute with the composite localized Weil operator.

## 3.3 New positive door: commutator energy

Irreducibility suggests reversing the question. Instead of seeking a common symmetry, use incompatibility as a positive energy. Define

\[
\boxed{
\mathcal E_N(X)
=
\sum_p w_p\|[N_p,X]\|_{\mathrm{HS}}^2
+
\|[F_N,X]\|_{\mathrm{HS}}^2,
\qquad w_p>0.
}
\tag{3.3}
\]

Then

\[
\mathcal E_N(X)\ge0,
\]

and

\[
\ker\mathcal E_N=\mathbb CI.
\]

On trace-zero matrices, \(\mathcal E_N\) is positive definite.

The RH-bearing conjecture is not that (3.3) already equals the Weil form. It is:

> **Commutator-energy conjecture.** Construct a compatible infinite family and a linear map \(f\mapsto X_f\), independently of the zeros, such that
> \[
> Q_W(f)=\mathcal E(X_f)+\text{explicit finite-rank or boundary terms}.
> \]

A successful construction would provide positivity before invoking the zero locations. A failed coefficient or Gamma match would kill the naive version without harming the rest of the program.

## 3.4 Mutation controls forced by Round 2

Any candidate additive–multiplicative operator should be tested against

\[
\zeta(s),
\qquad
\frac{\zeta(s)}{\zeta(2s)},
\qquad
\frac{\zeta(s)^2}{\zeta(2s)},
\]

and tangent perturbations around \((1,1)\). It should detect the predicted second-layer signs and charges.

### Round-3 verdict

- Raw common symmetry: **REFUTED**.
- Finite generated-algebra membership as evidence: **REFUTED**.
- Noncommutative commutator energy: **CONJECTURED**, with a clean coefficient-matching falsifier.

---

# Triangulation Round 4 — Center the explicit formula and expose the Lévy–Schur structure

## 4.1 Archimedean term as positive jump energy

The digamma identity gives

\[
\Re\psi\!\left(\frac14+\frac{ir}{2}\right)-\psi(1/4)
=
2\int_0^\infty
\frac{e^{-t/2}}{1-e^{-2t}}
[1-\cos(rt)]\,dt.
\tag{4.1}
\]

By Plancherel,

\[
\boxed{
\frac1{2\pi}\int_{\mathbb R}|F(r)|^2
\left[
\Re\psi\!\left(\frac14+\frac{ir}{2}\right)-\psi(1/4)
\right]dr
=
\int_0^\infty K(t)\|f-\tau_tf\|_2^2dt,
}
\tag{4.2}
\]

where

\[
K(t)=\frac{e^{-t/2}}{1-e^{-2t}}>0,
\qquad
(\tau_tf)(x)=f(x-t).
\]

Thus the real place already contains an exact positive nonlocal Dirichlet energy.

The remaining Archimedean scalar is

\[
\kappa_{\mathrm{arch}}
=
\log\pi-\psi(1/4)
=
\log\pi+\gamma+\frac\pi2+3\log2
=5.372183419225665\ldots.
\tag{4.3}
\]

## 4.2 Prime shifts as jump energies minus mass

Let

\[
c_n=\frac{\Lambda(n)}{\sqrt n},
\qquad a_n=\log n.
\]

Then

\[
-2c_n\Re\langle f,\tau_{a_n}f\rangle
=
c_n\|f-\tau_{a_n}f\|_2^2-2c_n\|f\|_2^2.
\tag{4.4}
\]

If \(a_n\ge L\), the zero-extended supports do not overlap and the two right-hand terms cancel. Hence only finitely many prime powers enter each localized form.

Define

\[
\mathcal E_L(f)
=
\int_0^\infty K(t)\|f-\tau_tf\|_2^2dt
+
\sum_{\log n<L}c_n\|f-\tau_{\log n}f\|_2^2,
\tag{4.5}
\]

\[
\kappa_L
=
\kappa_{\mathrm{arch}}
+2\sum_{\log n<L}c_n,
\qquad
B_L=\mathcal E_L-\kappa_LI.
\tag{4.6}
\]

The form \(\mathcal E_L\) is positive. All indefiniteness of the pole-free base is caused by one scalar subtraction.

## 4.3 Pole terms are rank one in each parity sector

For real even \(f\), set \(C(x)=\cosh(x/2)\). For real odd \(f\), set \(S(x)=\sinh(x/2)\). The pole bracket becomes

\[
h(i/2)+h(-i/2)
=
\begin{cases}
2|\langle C,f\rangle|^2,& f\text{ even},\\
-2|\langle S,f\rangle|^2,& f\text{ odd}.
\end{cases}
\]

Therefore

\[
\boxed{
A_{L,+}=B_{L,+}+2|C\rangle\langle C|,
\qquad
A_{L,-}=B_{L,-}-2|S\rangle\langle S|.
}
\tag{4.7}
\]

The localized Weil form has collapsed to:

\[
\boxed{
\text{positive jump energy}
-
\text{one scalar mass}
+
\text{one parity-dependent rank-one update}.
}
\]

## 4.4 Birman–Schwinger reduction

Assume the pole-free Morse pattern

\[
n_-(B_{L,+})=1,
\qquad
B_{L,-}>0,
\tag{4.8}
\]

and invertibility. Rank-one inertia gives

\[
\boxed{
A_{L,+}\ge0
\iff
1+2\langle C,B_{L,+}^{-1}C\rangle\le0,
}
\tag{4.9}
\]

\[
\boxed{
A_{L,-}\ge0
\iff
2\langle S,B_{L,-}^{-1}S\rangle\le1.
}
\tag{4.10}
\]

The associated secular functions

\[
S_+(z)=1+2\langle C,(B_{L,+}-z)^{-1}C\rangle,
\]

\[
S_-(z)=1-2\langle S,(B_{L,-}-z)^{-1}S\rangle
\]

satisfy

\[
S_+'(z)=2\|(B_{L,+}-z)^{-1}C\|^2>0,
\]
\[
S_-'(z)=-2\|(B_{L,-}-z)^{-1}S\|^2<0
\]

between base poles. Once the base inertia is known, the full sign becomes two scalar crossing problems.

A positive, simple, even ground of the base does **not** imply an even ground after the positive rank-one update. A two-dimensional parity crossing gives an exact counterexample. Perron structure alone is insufficient.

## 4.5 PNT centering

Define the prime-power measure

\[
d\nu(a)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}(a),
\]

its smooth model

\[
d\nu_0(a)=e^{a/2}da,
\]

and the residual

\[
dR=d\nu-d\nu_0.
\]

The pole term and \(d\nu_0\) combine exactly:

\[
P-2\int_0^\infty\Re g\,d\nu
=
2\int_0^\infty e^{-a/2}\Re g(a)da
-2\int_0^\infty\Re g\,dR.
\tag{4.11}
\]

The first term has Fourier multiplier

\[
\frac1{r^2+1/4}.
\]

Using \(\psi(z+1)=\psi(z)+1/z\),

\[
\boxed{
Q_W(f)
=
\frac1{2\pi}\int_{\mathbb R}|F(r)|^2
\left[
\Re\psi\!\left(\frac54+\frac{ir}{2}\right)-\log\pi
\right]dr
-2\int_0^\infty\Re g\,dR.
}
\tag{4.12}
\]

The new positive jump kernel is

\[
K_5(a)=\frac{e^{-5a/2}}{1-e^{-2a}},
\]

and the scalar subtraction is reduced by exactly \(4\):

\[
\kappa_5
=
\log\pi-\psi(5/4)
=1.372183419225665\ldots.
\tag{4.13}
\]

This is a cleaner decomposition:

\[
\boxed{
\text{Weil form}
=
\text{deterministic positive Archimedean baseline}
+
\text{centered prime fluctuation}.
}
\]

## 4.6 Exact circularity boundary

For \(\Re z>1/2\),

\[
\int_0^\infty e^{-za}dR(a)
=
-\frac{\zeta'}{\zeta}\!\left(z+\frac12\right)
-
\frac1{z-1/2}.
\tag{4.14}
\]

After removal of the pole at \(s=1\), the remaining nontrivial poles are

\[
z=\rho-\frac12.
\]

Therefore any global estimate forcing this transform to be analytic or strongly sign-controlled throughout \(\Re z>0\) is already RH-strength.

Use \(R\) on fixed windows or in restricted dual norms. A global polynomial envelope is not innocent PNT input.

### Round-4 verdict

- Archimedean place as positive jump energy: **DISCLOSED**.
- “Infinity has no positivity”: **REFUTED**.
- Global arithmetic residual as the hard term: **DISCLOSED**.
- Global tame residual estimate as independent input: often **RH in disguise**.

---

# Triangulation Round 5 — Local support, observability, and the horizon correction

## 5.1 What current localized spectral theory proves

Suzuki’s current framework constructs for every support half-width \(a>0\) a canonical lower-bounded self-adjoint operator \(A_a\) with discrete spectrum representing the localized Weil form. It proves:

1. the lowest eigenvalue \(\lambda_a\) is continuous in \(a\);
2. for sufficiently small \(a\), \(\lambda_a>0\), is simple, and its eigenfunction is even;
3. if RH is false, continuity and Weil’s criterion force a zero crossing at some finite support.

The Connes–van Suijlekom theorem separately states that if the lowest eigenvalue is simple and isolated with an even eigenfunction, the Fourier transform of that eigenfunction has only real zeros.

These are current primary-source facts.

## 5.2 Source correction at the first prime threshold

For total support length \(L<\log2\), no prime translation overlaps the support, so the localized form is prime-free. This makes \(\log2\) a natural structural threshold.

However, the fresh source audit found only:

- Yoshida/Suzuki positivity for **sufficiently small** support;
- high-mode coercivity on finite-codimension subspaces;
- continuity of the lowest eigenvalue.

It did **not** verify a theorem asserting full positivity exactly at \(L=\log2\), nor the prior corollary that positivity persists to \(\log2+\varepsilon\).

Therefore:

\[
\boxed{
\text{the claimed post-}\log2\text{ positivity theorem is UNVERIFIED and quarantined.}
}
\tag{5.1}
\]

Define safely

\[
L_*=
\sup\{L>0:\ Q_W\text{ is positive on every support window of total length }<L\}.
\]

Current sources give

\[
L_*>0,
\]

and

\[
\boxed{
\mathrm{RH}\iff L_*=\infty.
}
\tag{5.2}
\]

No stronger numerical value is certified here.

## 5.3 Paley–Wiener observability of an off-line pair

Let \(PW_A\) be the Paley–Wiener space of exponential type \(A\), with reproducing kernel

\[
K_w(z)=\frac{\sin A(z-\bar w)}{\pi(z-\bar w)}.
\]

For a hypothetical centered pair

\[
z=T+iy,
\qquad
\bar z=T-iy,
\]

the two-point Gram matrix is

\[
G_A=
\begin{pmatrix}d&c\\c&d\end{pmatrix},
\]

where

\[
d=\frac{\sinh(2Ay)}{2\pi y},
\qquad
c=\frac A\pi.
\]

The anti-diagonal evaluation direction has strength

\[
\boxed{
\mu_A(y)
=d-c
=
\frac{\sinh(2Ay)-2Ay}{2\pi y}.
}
\tag{5.3}
\]

For \(Ay\ll1\),

\[
\boxed{
\mu_A(y)
=
\frac{2A^3y^2}{3\pi}
+O(A^5y^4).
}
\tag{5.4}
\]

The minimum norm of an interpolant satisfying

\[
F(T+iy)=1,
\qquad
F(T-iy)=-1
\]

is

\[
\boxed{
\|F\|_{\min}^2=\frac{2}{\mu_A(y)}.
}
\tag{5.5}
\]

Thus near-line zeros are quadratically difficult to distinguish. Any finite certification excluding depth \(y\) must control all numerical, basis, complement, and arithmetic errors below the scale \(A^3y^2\).

The full Paley–Wiener law is translation-invariant in \(T\). A finite prolate basis is not; it has a separate vertical-reach problem. Therefore one must measure both:

- horizontal discrimination in \(y\);
- vertical reach in \(T\).

## 5.4 Support alone does not impose a finite-zero horizon

Given any finite ordinates \(\gamma_1,\ldots,\gamma_N\) and any type \(A>0\), set

\[
M=2N+1,
\qquad
\varepsilon=A/M,
\]

and define

\[
F(z)
=
\prod_{j=1}^N(z^2-\gamma_j^2)
\left(
\frac{\sin(\varepsilon z)}{\varepsilon z}
\right)^M.
\tag{5.6}
\]

Then \(F\) has exponential type \(A\), vanishes at every \(\pm\gamma_j\), and satisfies \(F(x)=O(1/x)\) on \(\mathbb R\), hence belongs to \(L^2(\mathbb R)\). Paley–Wiener gives a compactly supported inverse transform.

Therefore a fixed support interval can interpolate an arbitrarily large finite zero list. The universal support-only horizon is **REFUTED**.

## 5.5 What survives of \(T\approx2\pi X\)

The existing finite-minimizer movie exhibits a coherent effective frontier

\[
T\approx2\pi X
\]

for its chosen basis, support, sampling density, and extremal principle. That observation remains valuable.

The correct theorem target is a conditioning law involving

\[
\text{support}
+
\text{basis dimension}
+
\text{sampling density}
+
\text{frame bounds}
+
\text{norm budget}.
\]

### Round-5 verdict

- Small-support positive/simple/even regime: **DISCLOSED**.
- Exact positivity through or beyond \(\log2\): **UNVERIFIED**.
- Near-line observability law: **DISCLOSED**.
- Universal support horizon: **REFUTED**.
- Effective \(2\pi\) frontier for the current construction: **OBSERVED**.

---

# Triangulation Round 6 — Prime-side resolvents, Stieltjes structure, and safe-half-plane probes

## 6.1 Reflected negative-integer ladder

Define

\[
R_\Xi(z)=-\frac{\Xi'(z)}{2z\Xi(z)}.
\tag{6.1}
\]

For \(n\ge1\), set

\[
z=i\left(n+\frac12\right).
\]

Then \(s=1/2+iz=-n\). The functional equation and its derivative give

\[
\boxed{
R_\Xi\!\left(i(n+1/2)\right)
=
\frac1{2n+1}\frac{\xi'(n+1)}{\xi(n+1)}.
}
\tag{6.2}
\]

Since \(n+1>1\),

\[
\boxed{
\begin{aligned}
R_\Xi\!\left(i(n+1/2)\right)
=
\frac1{2n+1}
\Bigg[
&\frac1{n+1}+\frac1n-\frac12\log\pi\\
&+\frac12\psi\!\left(\frac{n+1}{2}\right)
-\sum_p\frac{\log p}{p^{n+1}-1}
\Bigg].
\end{aligned}
}
\tag{6.3}
\]

Every prime sum is absolutely convergent. Under RH,

\[
R_\Xi\!\left(i(n+1/2)\right)
=
\sum_{\gamma>0}\frac{m_\gamma}{\gamma^2+(n+1/2)^2}.
\tag{6.4}
\]

This is a rigorous replacement for formal Euler-product manipulations at negative integers.

## 6.2 Shifted Lorentzian microscope

For \(T\in\mathbb R\) and \(\alpha>1/2\), define

\[
\mathcal R_\alpha(T)
=-\frac1{2i\alpha}
\left[
\frac{\Xi'}{\Xi}(T+i\alpha)
-
\frac{\Xi'}{\Xi}(T-i\alpha)
\right].
\tag{6.5}
\]

The canonical-product constants cancel, giving

\[
\mathcal R_\alpha(T)
=
\sum_\lambda
\frac1{(T-\lambda)^2+\alpha^2}
\tag{6.6}
\]

in centered zero coordinates, with symmetric interpretation off RH.

Let

\[
s=\frac12+\alpha+iT,
\qquad \Re s>1.
\]

Then

\[
\boxed{
\mathcal R_\alpha(T)
=
\frac1\alpha\Re
\left[
\frac1s+\frac1{s-1}-\frac12\log\pi
+\frac12\psi(s/2)
-\sum_p\frac{\log p}{p^s-1}
\right].
}
\tag{6.7}
\]

This is an exact zero-spectrum microscope computed entirely in the convergent Euler region.

At fixed prime cutoff, decreasing \(\alpha\) sharpens the Lorentzian but moves \(\Re s\) toward \(1\), slowing convergence.

## 6.3 Second resolution axis: derivative order

Fix \(\alpha>1/2\). Put

\[
S_T(x)=\mathcal R_{\sqrt x}(T).
\]

Under RH,

\[
\frac{(-1)^k}{k!}S_T^{(k)}(\alpha^2)
=
\sum_\gamma
\frac1{((T-\gamma)^2+\alpha^2)^{k+1}}.
\tag{6.8}
\]

The normalized kernel

\[
\left(
\frac{\alpha^2}{u^2+\alpha^2}
\right)^{k+1}
\]

has half-width

\[
\boxed{
|u|_{1/2}
=
\alpha\sqrt{2^{1/(k+1)}-1}
\sim
\alpha\sqrt{\frac{\log2}{k+1}}.
}
\tag{6.9}
\]

Thus spectral resolution can be purchased in two ways:

\[
\boxed{
\alpha\downarrow1/2
\quad\text{or}\quad
k\uparrow\infty.
}
\]

The second keeps the Euler abscissa fixed but demands higher logarithmic prime moments and creates severe conditioning.

## 6.4 Stieltjes characterization

Define

\[
S(x)=R_\Xi(i\sqrt x).
\tag{6.10}
\]

Under RH,

\[
S(x)
=
\sum_{\gamma>0}\frac{m_\gamma}{\gamma^2+x}
=
\int_0^\infty\frac{d\mu(t)}{t+x},
\qquad
\mu=\sum_{\gamma>0}m_\gamma\delta_{\gamma^2}.
\tag{6.11}
\]

Conversely, if the meromorphic continuation of \(S\) is a Stieltjes transform of a positive measure, its poles lie on the negative real \(x\)-axis with positive residues. Its poles are \(-z_\rho^2\). Since \(\zeta\) has no nontrivial real zero in \((0,1)\), this forces every \(z_\rho\) to be real.

Therefore

\[
\boxed{
\mathrm{RH}
\iff
S\text{ is a positive meromorphic Stieltjes transform.}
}
\tag{6.12}
\]

## 6.5 Loewner and Hausdorff diagnostics

For positive sample points \(x_i\), define

\[
L_{ij}=
\begin{cases}
\dfrac{S(x_i)-S(x_j)}{x_j-x_i},&i\ne j,\\[3mm]
-S'(x_i),&i=j.
\end{cases}
\tag{6.13}
\]

Under RH,

\[
L_{ij}
=
\sum_{\gamma>0}
\frac{m_\gamma}{(\gamma^2+x_i)(\gamma^2+x_j)},
\]

so every finite Loewner matrix is positive semidefinite.

Fix \(x_0>1/4\) and set

\[
m_k(x_0)=\frac{(-1)^k}{k!}S^{(k)}(x_0).
\]

Under RH,

\[
m_k(x_0)=\sum_{\gamma>0}\frac{m_\gamma}{(\gamma^2+x_0)^{k+1}},
\]

which is a compact-support Hausdorff moment sequence after the substitution

\[
y_\gamma=(\gamma^2+x_0)^{-1}.
\]

The full Hankel and localizing hierarchy is therefore positive under RH. Conversely, a complete compatible positive moment representation reconstructs the Stieltjes measure and hence implies RH.

Broad moment/Hankel criteria for \(\Xi\) already exist. The distinctive feature here is that choosing \(x_0>1/4\) puts every derivative in the absolutely convergent prime region. Literature novelty for this exact shift is **UNVERIFIED**.

## 6.6 Finite conditioning and mutation behavior

The six-point Loewner experiment has eigenvalues spanning roughly twenty-two orders of magnitude. A synthetic off-line pair produces a negative atom, but the negative direction can appear only at increasing Hankel order as the pair approaches the line.

This is an instrument, not a proof. Its proper use is to calibrate how much moment order and precision are required to expose a declared off-line mutation.

### Round-6 verdict

- Reflected resolvent ladder: **DISCLOSED**.
- Shifted prime-side microscope: **DISCLOSED**.
- Stieltjes characterization: **DISCLOSED**.
- Finite Loewner positivity: **OBSERVED and necessary**, never sufficient at fixed order.
- All-order positivity from primes without zero input: **OPEN / RH-bearing**.

---

# Triangulation Round 7 — Global radical, rank-one preconditioning, and the full-RH route

## 7.1 An explicit global radical generating \(\Xi\)

Use the \(2\pi\)-Fourier convention

\[
\widehat h(y)=\int_{\mathbb R}h(x)e^{2\pi ixy}\,dx
\]

and define

\[
\boxed{
h_*(x)
=
\frac\pi2x^2(2\pi x^2-3)e^{-\pi x^2}.
}
\tag{7.1}
\]

It is a combination of the zeroth and fourth Hermite functions, so

\[
\widehat h_*=h_*,
\qquad
h_*(0)=0,
\qquad
\int_{\mathbb R}h_*=0.
\tag{7.2}
\]

Its Mellin transform is

\[
\boxed{
\int_0^\infty h_*(x)x^{s-1}dx
=
\frac18s(s-1)\pi^{-s/2}\Gamma(s/2).
}
\tag{7.3}
\]

Define the co-Poisson summation map

\[
(Eh_*)(u)=u^{1/2}\sum_{n\ge1}h_*(nu)
\]

and

\[
\mathcal K(t)=(Eh_*)(e^t).
\]

For \(s=1/2-iz\),

\[
\boxed{
\int_0^\infty(Eh_*)(u)u^{-iz}\frac{du}{u}
=
\frac14\xi(s).
}
\tag{7.4}
\]

Up to Fourier-sign convention,

\[
\widehat{\mathcal K}(z)=\frac14\Xi(z).
\]

Since \(\Xi(z_\rho)=0\) at every centered zero, \(\mathcal K\) lies in the global zero-side radical, subject only to the standard function-space bookkeeping.

For \(u\ge1\),

\[
|(Eh_*)(u)|\le Cu^{9/2}e^{-\pi u^2}.
\tag{7.5}
\]

Let \(a=\log\lambda\) and truncate

\[
k_\lambda=1_{[-a,a]}\mathcal K.
\]

Then

\[
\|\mathcal K-k_\lambda\|_2
\le C\lambda^{7/2}e^{-\pi\lambda^2},
\tag{7.6}
\]

and, on every closed strip \(|\Im z|\le\alpha<1/2\),

\[
\sup
\left|
\widehat{k_\lambda}(z)-\frac14\Xi(z)
\right|
\le C_\alpha\lambda^{5/2+\alpha}e^{-\pi\lambda^2}.
\tag{7.7}
\]

The target is built exactly; it is not fitted to known zeros.

## 7.2 Connes–van Suijlekom’s real-zero engine

For a lower-bounded self-adjoint localized convolution operator, if the lowest eigenvalue is simple and isolated with an even eigenfunction \(u_\lambda\), then every zero of \(\widehat{u_\lambda}\) is real.

This theorem is one-way. It does not say RH implies finite simplicity/evenness, nor that every localized ground converges to \(\Xi\).

Connes’s current program has two outer pieces:

1. the finite real-zero engine above;
2. an explicit prolate candidate whose transform converges to \(\Xi\).

The open bridge is the comparison of the **actual Weil minimizer** with that candidate, together with simplicity and parity.

## 7.3 Exact rank-one preconditioner

In the even sector write

\[
A_\lambda
=
D_\lambda+2|c_\lambda\rangle\langle c_\lambda|,
\qquad
0\notin\sigma(D_\lambda).
\tag{7.8}
\]

Define

\[
w_\lambda(z)=(D_\lambda-z)^{-1}c_\lambda,
\]

\[
S_\lambda(z)
=1+2\langle c_\lambda,(D_\lambda-z)^{-1}c_\lambda\rangle.
\tag{7.9}
\]

Then

\[
(A_\lambda-z)w_\lambda(z)
=c_\lambda S_\lambda(z),
\]

\[
S_\lambda'(z)=2\|w_\lambda(z)\|^2>0.
\tag{7.10}
\]

For any candidate \(k\),

\[
D_\lambda^{-1}A_\lambda k
=k+2\langle c_\lambda,k\rangle D_\lambda^{-1}c_\lambda,
\]

so

\[
\boxed{
k-D_\lambda^{-1}A_\lambda k
=-2\langle c_\lambda,k\rangle D_\lambda^{-1}c_\lambda.
}
\tag{7.11}
\]

Therefore

\[
\boxed{
\operatorname{dist}
\left(k,\operatorname{span}(D_\lambda^{-1}c_\lambda)\right)
\le
\|D_\lambda^{-1}A_\lambda k\|.
}
\tag{7.12}
\]

One base solve maps an approximate radical candidate directly onto the zero-energy secular line.

This changes the perturbation denominator from the exponentially tiny gap of the full Weil operator to

\[
d_\lambda=\
\operatorname{dist}(0,\sigma(D_\lambda)).
\]

If \(d_\lambda^{-1}\) grows only polynomially, the Gaussian radical tail is more than sufficient.

## 7.4 Why the raw residual/gap ratio was too harsh

A full-Weil eigenvalue and its nearest competitors may all be exponentially tiny. Dividing an ordinary residual by that tiny full gap can be exponentially unstable even when the vector is geometrically correct.

The base-resolvent route asks instead:

1. Is the pole-free base Morse index stable?
2. Is \(0\) polynomially separated from the inactive base spectrum?
3. Do the scalar secular functions select one even root below all odd and inactive modes?
4. Does the truncated global radical have polynomial-times-Gaussian dual leakage?

These are structural questions about the base, not the already RH-equivalent positivity of the full form.

## 7.5 Relative block-diagonalization target

Let \(u_{j,\lambda}\) be constrained prolate/co-Poisson near-radical directions and define

\[
B_\lambda(m,n)
=
\langle A_\lambda u_{m,\lambda},u_{n,\lambda}\rangle.
\]

Let \(D_\lambda^{\mathrm{prol}}\) denote the explicit prolate leakage scale. The correct asymptotic target need not be exact commutation. It is the weaker relative statement

\[
\boxed{
(D_\lambda^{\mathrm{prol}})^{-1/2}
\left(B_\lambda-c_\lambda D_\lambda^{\mathrm{prol}}\right)
(D_\lambda^{\mathrm{prol}})^{-1/2}
\longrightarrow0
}
\tag{7.13}
\]

on the first constrained sector, plus a uniform complement gap.

This says the arithmetic boundary is asymptotically diagonal at the leakage scale and selects the correct Hermite/prolate combination. It is weaker than constructing an exact all-primes commuting operator and closer to the actual proof requirement.

## 7.6 A sufficient theorem for RH

Suppose along an unbounded sequence \(\lambda_j\to\infty\):

1. \(D_{\lambda,+}\) has exactly one active negative mode and \(D_{\lambda,-}>0\);
2. inactive base eigenvalues are separated from the active secular root;
3. \(d_\lambda\), \(\|D_\lambda^{-1}c_\lambda\|\), and the relevant overlaps have polynomial upper and lower bounds;
4. an odd-sector scalar barrier places every odd eigenvalue above the selected even root;
5. the fixed-Hermite or true prolate candidate satisfies a preconditioned residual estimate strong enough for compact-substrip Fourier convergence.

Then the normalized full ground eigenfunctions converge to \(k_\lambda\), their transforms have only real zeros, and Hurwitz forces every zero of \(\Xi\) to be real.

\[
\boxed{
\text{Conditions 1–5 along one unbounded sequence imply RH.}
}
\tag{7.14}
\]

This implication is **DISCLOSED CONDITIONAL**. The conditions themselves remain open.

## 7.7 Partial zero-free corridors

For support \([-\log\lambda,\log\lambda]\), Paley–Wiener gives

\[
|F_f(z)-F_g(z)|
\le
\sqrt{2\log\lambda}\,
\lambda^{|\Im z|}\|f-g\|_2.
\tag{7.15}
\]

If real-rooted approximants satisfy

\[
\|u_\lambda-k_\lambda\|_2
=O\!\left(\lambda^{-\sigma}/\sqrt{\log\lambda}\right)
\]

along an unbounded subsequence, then \(\Xi\) has no off-line zero with

\[
0<|\Re\rho-1/2|<\sigma.
\tag{7.16}
\]

Every fixed \(\sigma>0\) is a genuine theorem below RH.

### Round-7 verdict

- Explicit \(\Xi\)-generating radical: **DISCLOSED**.
- Gaussian truncation convergence: **DISCLOSED**.
- Base-resolvent identity: **DISCLOSED**.
- Polynomial base conditioning and parity barrier: **OPEN**, central.
- Full minimizer convergence as “equivalent to RH”: **REFUTED**; it is an RH-sufficient route and may be RH-plus.

---

# Triangulation Round 8 — Finite Weil compressions and the four-moment theorem factory

## 8.1 Current unconditional tide

The August 2026 Alpöge–Furman theorem proves, unconditionally,

\[
\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\frac23-o(1),
\]

\[
\frac{N_d(T,2T)}{N(T,2T)}
\ge
\frac56-o(1).
\tag{8.1}
\]

With the Montgomery–Taylor window the constants are approximately

\[
0.6725007,
\qquad
0.83625035.
\]

The finite compression has, up to trace-norm-small tails, the structure

\[
A=P_1+Q',
\tag{8.2}
\]

where

\[
P_1\succeq0,
\qquad
\operatorname{rank}P_1\le s,
\qquad
\operatorname{tr}P_1\le s,
\]

\[
n_+(Q')\le b,
\qquad
s+2b\le N.
\tag{8.3}
\]

Here \(s\) counts simple on-line zeros; \(b\) absorbs multiple on-line points and off-line pairs. The prime side supplies trace moments.

This proves that finite compressions of an indefinite Weil form can yield actual unconditional information without assuming termwise positivity.

## 8.2 New sharp four-moment theorem with the zero-block structure

### Theorem 8.1

Let \(A=P+Q\) be an \(N\times N\) Hermitian matrix satisfying

\[
P\succeq0,
\quad
\operatorname{rank}P\le s,
\quad
\operatorname{tr}P\le s,
\quad
n_+(Q)\le b,
\quad
s+2b\le N.
\tag{8.4}
\]

Assume

\[
\frac1N\operatorname{tr}A=1+o(1),
\]

and define centered moments

\[
b_2=\frac1N\operatorname{tr}(A-I)^2,
\qquad
b_4=\frac1N\operatorname{tr}(A-I)^4.
\]

If

\[
\sigma_*=\frac{b_2-b_4}{1-b_2}\in(0,3/4),
\]

then

\[
\boxed{
\frac{s}{N}
\ge
\frac{(1-b_2)^2}{1-2b_2+b_4}
-o(1).
}
\tag{8.5}
\]

If the corresponding zero decomposition identifies at least \(s+b\) distinct zero points, then

\[
\boxed{
\frac{N_d}{N}
\ge
\frac12
\left[
1+\frac{(1-b_2)^2}{1-2b_2+b_4}
\right]
-o(1).
}
\tag{8.6}
\]

### Proof

Order eigenvalues decreasingly. Weyl’s inequality implies

\[
\lambda_{i+b}(A)\le
\lambda_i(P)+\lambda_{b+1}(Q)
\le
\lambda_i(P).
\tag{8.7}
\]

After deleting at most the largest \(b\) positive eigenvalues of \(A\), the remaining positive spectrum has at most \(s\) entries and sum at most \(s\).

For \(\sigma<3/4\), set \(u=1-\sigma\) and define

\[
\Phi_\sigma(x)
=u^2+4ux-\bigl((x-1)^2-\sigma\bigr)^2.
\tag{8.8}
\]

Its derivative is

\[
\Phi_\sigma'(x)
=-4(x-2)(x^2-x+1-\sigma).
\]

Since \(x^2-x+1-\sigma>0\) for \(\sigma<3/4\),

\[
\Phi_\sigma(x)\le0\quad(x\le0),
\]

\[
\Phi_\sigma(x)\le u^2+4ux,
\]

and the global maximum is

\[
\Phi_\sigma(2)=8u.
\]

Apply \(\Phi_\sigma\) to the spectrum of \(A\). The deleted \(b\) eigenvalues contribute at most \(8ub\); the remaining positive eigenvalues contribute at most \(u^2s+4us\); nonpositive eigenvalues contribute at most zero. Hence

\[
\operatorname{tr}\Phi_\sigma(A)
\le
u^2s+4us+8ub.
\]

Using \(s+2b\le N\),

\[
\operatorname{tr}\Phi_\sigma(A)
\le
u^2s+4uN.
\tag{8.9}
\]

On the other hand,

\[
\frac1N\operatorname{tr}\Phi_\sigma(A)
=
u^2+4u-b_4+2\sigma b_2-\sigma^2+o(1).
\]

Cancel \(4u\) and optimize

\[
\frac{u^2+2\sigma b_2-\sigma^2-b_4}{u^2}
=
\frac{1-b_4-2\sigma(1-b_2)}{(1-\sigma)^2}.
\]

The stationary point is

\[
\sigma_*=\frac{b_2-b_4}{1-b_2},
\]

and substitution gives (8.5).

For distinct zeros, retain the pre-elimination inequality

\[
(u+4)s+8b
\ge
N\,[4+uR]+o(N),
\]

where \(R\) is the right side of (8.5). Minimize \((s+b)/N\) subject to this and \(s+2b\le N\). The extremal lies at \(s+2b=N\), yielding

\[
\frac{s+b}{N}\ge\frac{1+R}{2}-o(1).
\]

This proves (8.6). ∎

The theorem uses more than arbitrary moment data: it uses the rank/trace structure of the simple-on-line part and the positive-index budget of the remainder. It therefore can improve on a generic Christoffel positive-index bound without contradiction.

## 8.3 Predicted four moments

The sine-kernel prediction is

\[
(m_1,m_2,m_3,m_4)
=
\left(1,\frac43,2,\frac{13}{4}\right).
\]

Hence

\[
b_2=\frac13,
\qquad
b_4=\frac14,
\qquad
\sigma_*=\frac18.
\]

The theorem gives

\[
\boxed{
\frac{s}{N}\ge\frac{16}{21}-o(1),
}
\tag{8.10}
\]

\[
\boxed{
\frac{N_d}{N}\ge\frac{37}{42}-o(1).
}
\tag{8.11}
\]

These constants are sharp for the declared finite matrix constraints. A \(42\)-dimensional equality configuration has

- \(16\) eigenvalues \(1+1/\sqrt8\);
- \(16\) eigenvalues \(1-1/\sqrt8\);
- \(5\) eigenvalues \(2\);
- \(5\) eigenvalues \(0\).

The finite theorem is **DISCLOSED**. The zeta application is **CONDITIONAL** on the fourth trace moment.

## 8.4 Idempotence-defect statistic

Let

\[
H=A(2I-A)=I-(A-I)^2.
\]

Then

\[
\frac1N\operatorname{tr}H=1-b_2,
\]

\[
\frac1N\operatorname{tr}H^2=1-2b_2+b_4.
\]

Thus

\[
R
=
\frac{(\operatorname{tr}H/N)^2}{\operatorname{tr}H^2/N}.
\tag{8.12}
\]

The polynomial \(x(2-x)\) is \(1\) at the ideal simple-zero eigenvalue \(x=1\) and \(0\) at obstruction values \(0,2\). Define

\[
D_T=\frac1N\operatorname{tr}(2A-A^2)^2.
\]

For the flat window, \(\operatorname{tr}H/N\to2/3\), so

\[
\frac{N_0^s}{N}
\ge
\frac4{9D_T}-o(1).
\tag{8.13}
\]

To beat the Montgomery–Taylor constant

\[
\kappa=0.672500703679\ldots,
\]

it suffices to prove

\[
\boxed{
\limsup b_4
<0.327549907402\ldots,
}
\tag{8.14}
\]

or equivalently

\[
\boxed{
\limsup D_T
<0.660883240735\ldots.
}
\tag{8.15}
\]

The sine-kernel prediction is

\[
D_T=\frac7{12}=0.58333\ldots,
\]

leaving substantial slack.

## 8.5 Christoffel warning

For an arbitrary Hamburger moment sequence, the unconstrained degree-\(m\) Christoffel minimizer need not majorize the indicator of the nonpositive half-line. An exact three-atom counterexample has actual positive mass \(5/6\) but an unconstrained degree-two Christoffel calculation would falsely predict a larger lower bound.

Therefore every all-moment positive-index certificate must include an explicit one-sided dual polynomial or sum-of-squares/Sturm verification. This does not affect the proved two-moment Alpöge–Furman theorem.

## 8.6 Arithmetic barrier

At bandwidth one, the current prime-side method obtains the first two required matrix statistics through a special boundary mean-value argument. General higher trace moments fall in the Rudnick–Sarnak range

\[
X^k\le T^{2-\varepsilon}.
\]

At \(X\asymp T\), moments beyond the existing second-moment input require genuinely new off-diagonal prime correlations. The fourth moment contains a \(2+2\) channel involving

\[
(\Lambda*\Lambda)(m)(\Lambda*\Lambda)(m+h).
\]

Therefore the immediate bottleneck is not semidefinite optimization. It is a one-sided quartic prime-correlation inequality.

### Round-8 verdict

- Current \(2/3\) and \(5/6\) theorem: **DISCLOSED in a current preprint, source-audited**.
- Four-moment structural theorem: **DISCLOSED here; priority UNVERIFIED**.
- \(16/21\), \(37/42\) for zeta: **CONDITIONAL**.
- Higher-moment SDP without new arithmetic: **insufficient**.
- Best near-term theorem target: the scalar quartic inequality (8.15).

---

# Triangulation Round 9 — Nicolas, K-free integers, and positive arithmetic structures

## 9.1 Nicolas’s criterion as a scalar RH mirror

Let

\[
N_k=\prod_{j\le k}p_j.
\]

Nicolas’s theorem states

\[
\boxed{
\mathrm{RH}
\iff
\frac{N_k}{\varphi(N_k)}
>e^\gamma\log\log N_k
\quad\text{for every }k.
}
\tag{9.1}
\]

The left side is

\[
\prod_{p\le p_k}\frac p{p-1}
=
\prod_{p\le p_k}
\left(1+\frac1{p-1}\right).
\]

Expanding,

\[
\frac{N_k}{\varphi(N_k)}
=
\sum_{S\subseteq\{p\le p_k\}}
\prod_{p\in S}\frac1{p-1}.
\tag{9.2}
\]

It is literally a norm square. If

\[
v_p=e_0+\frac1{\sqrt{p-1}}e_1,
\]

then

\[
\boxed{
\frac{N_k}{\varphi(N_k)}
=
\left\|\bigotimes_{p\le p_k}v_p\right\|^2.
}
\tag{9.3}
\]

But the RH content is comparison with the sharp growing benchmark, not positivity of the product.

## 9.2 Exact centered Nicolas identity

For real \(x\), define

\[
P(x)=\prod_{p\le x}(1-p^{-1})^{-1},
\qquad
E_\Theta(x)=\Theta(x)-x,
\]

\[
w(t)=\frac{\log t+1}{t^2(\log t)^2},
\]

\[
R_2(x)=\sum_{p>x}\sum_{m\ge2}\frac1{mp^m}>0.
\]

The logarithmic Nicolas margin is

\[
m_N(x)=\log P(x)-\gamma-\log\log\Theta(x).
\]

Stieltjes integration of \(\sum_{p\le x}1/p\), together with the relation between the prime Mertens constant and \(\gamma\), gives

\[
\boxed{
m_N(x)
=
\mathcal B_x(E_\Theta(x))
-
\int_x^\infty E_\Theta(t)w(t)dt
-
R_2(x),
}
\tag{9.4}
\]

where

\[
\boxed{
\mathcal B_x(E)
=
\frac{E}{x\log x}
-
\log
\left(
\frac{\log(x+E)}{\log x}
\right).
}
\tag{9.5}
\]

The local term is always nonnegative. Put

\[
t=\log(1+E/x),
\qquad a=\log x.
\]

Then

\[
\mathcal B_x(E)
=
\frac{e^t-1}{a}
-
\log(1+t/a)
\ge
\frac ta-
\log(1+t/a)
\ge0.
\tag{9.6}
\]

For \(|E|/x\ll1\),

\[
\mathcal B_x(E)
=
\frac{E^2}{2x^2}
\left(
\frac1{\log x}
+
\frac1{(\log x)^2}
\right)
+O\!\left(\frac{|E|^3}{x^3\log x}\right).
\tag{9.7}
\]

The linear local fluctuation cancels. The hard sign resides in a positive local curvature, a signed future prime-error tail, and a negative prime-power correction.

This resembles a near-radical second-variation problem, but it is not literally the Weil form.

## 9.3 Exact \(\Theta\)–\(\Psi\) bridge

Prime powers connect the two natural error terms:

\[
\Psi(x)=\sum_{m\ge1}\Theta(x^{1/m}),
\]

\[
\Theta(x)=\sum_{m\ge1}\mu(m)\Psi(x^{1/m}).
\tag{9.8}
\]

The prime-square contribution is of square-root size and cannot be discarded in an RH-scale argument.

A genuine Nicolas-to-Weil bridge must transport the Nicolas tail kernel into the cone generated by differentiated autocorrelations, with the prime-power correction explicit. That is a concrete convex-cone membership problem, not yet solved.

## 9.4 K-free counting and ghost layers

The all-prime multiplicity cap gives

\[
Z_K(s)=\frac{\zeta(s)}{\zeta(Ks)}.
\]

Its coefficients indicate the \(K\)-free integers. Since

\[
\mathbf1_{K\text{-free}}(n)
=
\sum_{d^K\mid n}\mu(d),
\]

we obtain

\[
\boxed{
Q_K(x)
:=\#\{n\le x:n\text{ is }K\text{-free}\}
=
\frac{x}{\zeta(K)}+O_K(x^{1/K}).
}
\tag{9.9}
\]

The omitted coefficient density is

\[
1-\frac1{\zeta(K)}
=2^{-K}+O(3^{-K}),
\tag{9.10}
\]

but the residual factor contains

\[
N(KT)\asymp KT\log(KT)
\]

zeros below scaled height \(T\). A tiny coefficient tail can carry a dense spectral divisor.

## 9.5 Independent positivity in the safe Euler region

For \(\sigma_0>1\), define

\[
a_k=-\frac{\zeta'(\sigma_0+k)}{\zeta(\sigma_0+k)}
=
\sum_{n\ge2}\Lambda(n)n^{-\sigma_0}\left(\frac1n\right)^k.
\]

Then \((a_k)\) is a Hausdorff moment sequence on \([0,1/2]\):

\[
\boxed{
(-1)^r\Delta^ra_k
=
\sum_{n\ge2}\Lambda(n)n^{-\sigma_0-k}
\left(1-\frac1n\right)^r
\ge0.
}
\tag{9.11}
\]

Hence all Hankel matrices \([a_{i+j}]\) are positive semidefinite.

There is also a positive Gaussian heat geometry. For \(\alpha>0\), set

\[
v_n(t)=e^{-\pi tn^2}t^{(\alpha-1)/2}.
\]

Then

\[
\boxed{
G_\alpha(n,m)
=
\int_0^\infty v_n(t)v_m(t)dt
=
\frac{\Gamma(\alpha)}{\pi^\alpha(n^2+m^2)^\alpha}.
}
\tag{9.12}
\]

Every finite \(G_\alpha\) is positive definite, and

\[
\operatorname{tr}G_\alpha
=
\frac{\Gamma(\alpha)}{(2\pi)^\alpha}\zeta(2\alpha).
\tag{9.13}
\]

These are independent positive arithmetic structures. The missing theorem is a sign-preserving transport from them to the centered zero resolvent or Weil form.

### Round-9 verdict

- Nicolas criterion: **DISCLOSED RH-equivalent scalar mirror**.
- Powerset norm as positivity source for the benchmark: **REFUTED**.
- Centered Nicolas identity: **DISCLOSED**.
- K-free theorem and rare-tail warning: **DISCLOSED**.
- Safe-region prime and heat positivity: **DISCLOSED**.
- Transport to Weil positivity: **OPEN**.

---

# Triangulation Round 10 — Function-field geometry, q-clock boundary data, and final convergence

## 10.1 What function fields actually provide

For a smooth projective curve over \(\mathbb F_q\), Frobenius acts on a finite-dimensional cohomology. The zeta zeros are reciprocals of Frobenius eigenvalues. The crucial positivity comes from the intersection/Rosati/Hodge structure on correspondences of the surface \(C\times C\), not from a naive equation “degree equals a count.”

The geometric polarization precedes and forces the spectral modulus

\[
|\alpha|=\sqrt q.
\]

The number-field problem is to construct an independent global object providing:

1. finite-prime correspondences;
2. the Archimedean boundary;
3. a trace/Lefschetz formula reproducing the explicit formula;
4. a middle cohomology or Hilbert complex;
5. a positive polarization not defined from the zero locations.

## 10.2 Why \(\zeta(-1)=-1/12\) is not a no-go theorem

The value \(-1/12\) shows that zeta regularization is not a literal positivity-preserving cardinality operation. It does not prove that every Archimedean index, heat-kernel norm, cyclic pairing, or Hodge polarization must be indefinite.

A Fredholm index itself cannot equal \(Q_W(f)\) for continuously varying \(f\): the index is integer-valued and locally constant, while

\[
Q_W(tf)=|t|^2Q_W(f).
\]

The viable target is instead a positive real pairing such as

\[
\boxed{
W(f*f^\sharp)
=
\tau(T_f^*T_f)
=
\|T_f\Omega\|^2,
}
\tag{10.1}
\]

constructed independently of the zeros.

## 10.3 q-clock calibration for any geometric model

Define the completed function

\[
\Lambda(s)=\Gamma_{\mathbb R}(s)\zeta(s).
\]

At every scale,

\[
\mathcal D_{q,j}(s)
=
\frac{\Lambda(q^js)}{\Lambda(q^{j+1}s)}.
\tag{10.2}
\]

Its finite-prime part is

\[
\frac{\zeta(q^js)}{\zeta(q^{j+1}s)}
=
\prod_p\det(I-p^{-q^js}C_q^\circ).
\tag{10.3}
\]

Its Archimedean part is

\[
A_q(s)=\frac{\Gamma_{\mathbb R}(s)}{\Gamma_{\mathbb R}(qs)}.
\]

Gauss multiplication gives

\[
\boxed{
A_q(s)
=
(2\pi)^{(q-1)/2}
\pi^{(q-1)s/2}
q^{1/2-qs/2}
\prod_{r=1}^{q-1}
\Gamma\!\left(\frac s2+\frac rq\right)^{-1}.
}
\tag{10.4}
\]

Thus the same fractional phases appear in two channels:

| finite primes | infinite place |
|---|---|
| cyclic phase \(r/q\) | Gamma shift \(s/2+r/q\) |
| finite occupancy digit | fractional scale channel |
| carry cancellation | continuous renormalization |

Any proposed arithmetic-square cohomology or transfer operator should recover this correspondence before claiming global positivity.

## 10.4 The Archimedean boundary does not disappear

For \(\sigma>1\),

\[
\zeta(K\sigma)\to1
\]

exponentially fast as \(K\to\infty\). By contrast,

\[
\log\Gamma_{\mathbb R}(K\sigma)
=
\frac{K\sigma}{2}
\left[
\log\frac{K\sigma}{2\pi}-1
\right]
+O(\log K).
\tag{10.5}
\]

The finite-prime residual saturates in the ordinary Dirichlet region; the continuous-scale boundary does not become a negligible tail. This is why the q-clock tower does not by itself furnish a convergent positive determinant for \(\Xi\).

## 10.5 Tropical Hodge theory: adjacent, not yet transported

Hard Lefschetz and Hodge–Riemann relations are established for substantial classes of smooth projective tropical varieties. This proves that characteristic-one geometry can support genuine positivity.

No comparison theorem currently places the Connes–Consani arithmetic/scaling-site square, with its distorted Frobenius correspondences and Archimedean boundary, inside those hypotheses. Therefore tropical Hodge theory is an adjacent positivity technology, not yet an RH engine.

A valid geometric construction must pass the Davenport–Heilbronn control: if it applies unchanged to a non-Euler-product function with the same reflection symmetry and produces positivity, it is too weak or circular.

## 10.6 Dominance synthesis

The ten routes now separate cleanly.

| Route | Independent mathematical source | Immediate theorem if successful | Ultimate boundary |
|---|---|---|---|
| Witt/necklace deformation | unique factorization and Möbius inversion | structural classification, mutation controls | identity, not positivity |
| q-clock tower | finite cyclic determinants and Gauss multiplication | canonical local model | infinite boundary condition missing |
| commutator energy | noncommutative irreducibility | positive finite/infinite Dirichlet form | coefficient/trace match open |
| localized Lévy–Schur | exact explicit-formula algebra | support-window and inertia theorems | base Morse pattern open |
| safe resolvent | convergent Euler products | Loewner/Hankel finite diagnostics | all-order positivity is RH |
| fixed Hermite radical | Poisson/Mellin self-duality | explicit \(\Xi\)-candidate and tail bounds | selection/conditioning open |
| prolate selection | Slepian concentration | real-rooted approximants | relative second variation open |
| finite rank–inertia | prime-side second moments | current \(2/3\) theorem | sparse exceptions remain |
| quartic selector | one-sided matrix polynomial | stronger density constants | fourth prime moment open |
| tropical/adelic Hodge | independent geometric positivity | potentially direct Weil positivity | comparison object unbuilt |

The program has one summit route and one harvest route:

\[
\boxed{
\textbf{Summit: prove pole-free base Morse index one, polynomial conditioning, and scalar parity selection.}
}
\]

\[
\boxed{
\textbf{Harvest: prove a strict upper bound on the quartic idempotence defect }D_T.
}
\]

### Round-10 verdict

- Function-field analogy: **CORROBORATED after correcting the source of positivity**.
- q-clock/Gamma calibration: **DISCLOSED**.
- Global positive arithmetic square: **DARK**, with the missing comparison theorem named.
- Geometric route remains orthogonal and potentially decisive, but less locally developed than the operator and moment routes.

---

# Master execution program

## Phase I — close low-cost exact lemmas

1. **Publishable algebra note.** Write the necklace-coordinate formula, finite-Witt-support classification, first-order isolation, branch-singularity qualification, and q-ary carry theorem with a dedicated literature search.
2. **Radical-tail lemma.** Complete the operator-domain bookkeeping proving
   \[
   \|A_\lambda k_\lambda\|
   \le
   \lambda^M e^{-\pi\lambda^2}
   \]
   for the fixed-Hermite truncation, using only elementary prime bounds.
3. **Quartic resonance expansion.** Derive the exact prime-side formula for
   \[
   D_T=N^{-1}\operatorname{tr}(2B_T-B_T^2)^2.
   \]
4. **Small-support source audit.** Locate the exact Yoshida constants and theorem numbers. Do not use \(\log2\) as a proved positivity endpoint until this audit closes.

## Phase II — run discriminating, cutoff-free experiments

### Operator experiment

For increasing \(\lambda\) and interval-certified Galerkin size:

1. build full even and odd localized forms without a finite Archimedean cutoff;
2. remove pole rank-one terms to obtain \(D_{\lambda,\pm}\);
3. certify inertia and \(\operatorname{dist}(0,\sigma(D_{\lambda,\pm}))\);
4. interval-solve the secular resolvents;
5. measure
   \[
   \|A_\lambda k_\lambda\|,
   \quad
   \|D_\lambda^{-1}A_\lambda k_\lambda\|,
   \quad
   S_\lambda(0),
   \quad
   d_\lambda,
   \quad
   \text{odd-even separation};
   \]
6. compare fixed-Hermite and exact prolate candidates after preconditioning;
7. repeat on squarefree and \((2,1)\) mutations.

**Pass:** one negative active even base mode, positive odd base, polynomial conditioning, exponentially decaying preconditioned residual, stable parity barrier.  
**Morse failure:** a second negative even base mode appears.  
**Conditioning failure:** \(d_\lambda\) collapses exponentially.  
**Selection failure:** raw energy is tiny but preconditioned residual does not decay.  
**Mutation failure:** predicted scaled layers are not detected.

### Quartic experiment

Expand the \(4+0\), \(3+1\), and \(2+2\) resonance families before taking absolute values. Compare measured values with

\[
\frac23,
\qquad
0.660883240735\ldots,
\qquad
\frac7{12}.
\]

The computation is exploratory until prime tails and transfer from the directly computed matrix to the ideal zero matrix are certified.

### Resolvent experiment

At fixed \(\alpha>1/2\), compute derivative microscopes of increasing order. Insert synthetic off-line pairs with declared depth and verify the predicted order at which Hankel or Loewner negativity becomes visible.

## Phase III — attack the two decisive theorems

### Theorem A: base selection

Prove along an unbounded sequence

\[
n_-(D_{\lambda,+})=1,
\qquad
D_{\lambda,-}>0,
\qquad
\operatorname{dist}(0,\sigma D_\lambda)\ge\lambda^{-M},
\]

with polynomial overlap bounds and a scalar odd-sector barrier.

### Theorem B: quartic prime inequality

Prove any strict saving

\[
\limsup D_T<\frac23-\delta.
\]

This immediately improves the flat-window \(2/3\) theorem. The sharper target

\[
\limsup D_T<0.660883240735\ldots
\]

beats the Montgomery–Taylor record. The sine prediction \(7/12\) yields \(16/21\).

---

# Ten-round claim ledger

| Claim | State | Boundary / weakest premise |
|---|---|---|
| Correct centered zero coordinate \(z_\rho=(\rho-1/2)/i\) | **DISCLOSED** | exact explicit-formula normalization |
| On-line atom positive; off-line pair signature \((1,1)\) | **DISCLOSED** | interpolation richness needed for global criterion |
| Weil positivity for every test is equivalent to RH | **DISCLOSED** | universal test-space quantifier |
| Functional equation alone forces the sign | **REFUTED** | Davenport–Heilbronn control |
| Multiset Witt coordinates equal \(M_n(b)-M_n(b-a)\) | **DISCLOSED** | formal/analytic convergence region declared |
| Generic deformation gives scaled singularity layers | **DISCLOSED** | nonintegral exponents create branches |
| Generic deformation always gives actual zero towers | **REFUTED** | integrality missing |
| \((1,1)\) unique nonnegative single-layer point | **DISCLOSED** | only within the declared occupancy family |
| Complete real finite-Witt-support classification | **DISCLOSED here** | literature priority **UNVERIFIED** |
| Physical point first-order isolated | **DISCLOSED** | Jacobian determinant \(-1/6\) |
| q-ary clock/carry realization | **DISCLOSED** | identity, not positivity |
| Finite occupation + Fourier common commutant scalar | **DISCLOSED** | finite-dimensional theorem |
| Scalar commutant forbids building an operator from the generators | **REFUTED** | generators produce the full matrix algebra |
| Commutator energy reproduces Weil form | **CONJECTURED** | coefficient and boundary match unbuilt |
| Archimedean term is a positive jump energy minus a scalar | **DISCLOSED** | exact digamma identity |
| Full localized form is jump base plus two rank-one parity updates | **DISCLOSED** | real parity decomposition |
| Perron base automatically selects full even ground | **REFUTED** | exact parity-crossing counterexample |
| PNT centering lowers scalar by exactly \(4\) | **DISCLOSED** | exact pole/model cancellation |
| Global tame residual bound is ordinary PNT input | **REFUTED in strong norms** | residual transform poles are centered zeros |
| Localized lowest eigenvalue continuous in support | **DISCLOSED by Suzuki** | current source |
| Positive/simple/even for sufficiently small support | **DISCLOSED by Suzuki/Yoshida** | no explicit maximal interval |
| Positivity through \(\log2\) and beyond | **UNVERIFIED** | prior dossier overreached source audit |
| Paley–Wiener off-line observability \(\sim2A^3y^2/(3\pi)\) | **DISCLOSED** | exact reproducing-kernel computation |
| Support alone imposes a finite zero horizon | **REFUTED** | explicit finite interpolation construction |
| Effective \(T\approx2\pi X\) frontier in current minimizer | **OBSERVED** | basis/conditioning specific |
| Reflected negative-integer prime resolvent | **DISCLOSED** | functional equation and Euler region |
| Stieltjes realization equivalent to RH | **DISCLOSED** | meromorphic positive-measure realization |
| Finite Loewner/Hankel positivity proves RH | **REFUTED** | all orders required |
| Fixed Hermite/co-Poisson transform equals \(\Xi/4\) | **DISCLOSED** | Fourier convention fixed |
| Rank-one base-resolvent preconditioner identity | **DISCLOSED** | \(0\notin\sigma(D_\lambda)\) |
| Polynomial base conditioning | **OPEN** | central full-RH hole |
| Simple-even minimizer convergence along an unbounded sequence implies RH | **DISCLOSED CONDITIONAL** | Hurwitz and strip convergence |
| Ground simplicity/evenness alone is equivalent to RH | **REFUTED** | one-way real-zero theorem only |
| Current \(2/3\), \(5/6\), \(0.6725\) results | **DISCLOSED in current preprint** | very recent publication status |
| Four-moment matrix bound \(R=(1-b_2)^2/(1-2b_2+b_4)\) | **DISCLOSED** | zero-block rank/inertia structure |
| \(16/21\), \(37/42\) for zeta | **CONDITIONAL** | fourth trace moment unproved |
| Unconstrained Christoffel function always bounds positive mass | **REFUTED** | one-sided majorization missing |
| Higher moments are immediately available from current prime method | **REFUTED** | off-diagonal correlation barrier |
| Nicolas powerset positivity forces its RH benchmark | **REFUTED** | comparison, not positivity, is hard |
| Centered Nicolas identity | **DISCLOSED** | classical Mertens constants and Stieltjes integration |
| K-free counting theorem | **DISCLOSED** | elementary inclusion–exclusion |
| Tiny coefficient tail implies tiny spectral tail | **REFUTED** | residual \(\zeta(Ks)\) divisor |
| Tropical Hodge positivity exists | **DISCLOSED in its domain** | smooth projective tropical varieties |
| It already applies to the arithmetic scaling-site square | **UNVERIFIED / DARK** | comparison category unbuilt |
| \(\zeta(-1)=-1/12\) rules out all Archimedean positivity | **REFUTED** | only naive regularized counting is blocked |

---

# Aletheia/TLICA diagnostic vector

These coordinates are kept separate.

- **\(\kappa\) / contact:** high. The program is anchored to the explicit formula, primary operator papers, exact finite matrix theorems, and reproducible scripts.
- **\(\phi\) / toolkit-relative pathway state:** mixed. Many finite and conditional paths are constructible; the full base-conditioning and geometric comparison paths remain unresolved.
- **\(\sigma\) / source-map adequacy:** high for Suzuki, Connes–van Suijlekom, Connes 2026, and Alpöge–Furman; downgraded around the claimed Yoshida \(\log2\) endpoint.
- **\(\rho\) / commitment coupling:** high. The prime-multiset and prolate frames are productive and therefore especially liable to survive beyond their evidence. Mutation controls are mandatory.
- **\(\mu\) / probe availability:** high for finite algebra, synthetic off-line controls, and matrix inertia; low for asymptotic base conditioning and global tropical comparison.
- **Tool closure:** primary-source web, local symbolic algebra, arbitrary precision numerics, finite random controls, and existing Lean verification for the current two-thirds theorem. No independent proof assistant formalization was produced for the new four-moment or finite-Witt theorems.
- **Independence:** exact symbolic checks and distinct mathematical lenses provide partial independence. Same-model repetitions are not blind witnesses.
- **Coherence:** high across explicit formula, operator decomposition, and finite inertia. Coherence is diagnostic, not truth probability.
- **Discrimination:** strongest current discriminators are the squarefree/Witt mutations, synthetic off-line pairs, odd/even interval inertia, and quartic resonance decomposition.

The program is not contextually saturated: several verdict-changing probes are available and have not yet run with certification.

---

# Verification record

The following scripts were rerun in the working environment:

1. `verify_rh_moonshot.py`
   - exact quartic optimizer and constants;
   - \(42\)-dimensional equality configuration;
   - Montgomery–Taylor threshold;
   - Christoffel counterexample;
   - fixed-Hermite Mellin coefficient;
   - 500 random noncommuting rank–inertia controls;
   - finite scalar-commutant and parity-crossing controls.

2. `rh_qary_renormalization.py`
   - q-ary digit identities;
   - cyclic determinant and trace weights;
   - carry cancellation;
   - finite and completed telescoping;
   - Gamma multiplication;
   - rare coefficient / dense spectral tail diagnostics;
   - K-free counts;
   - safe Hausdorff moment and heat Gram positivity.

3. `rh_multiset_triangulations.py`
   - Witt coefficients and single-center solutions;
   - tangent charges;
   - scaled squarefree singularity;
   - reflected resolvent ladder;
   - shifted prime-side zero peaks;
   - Loewner conditioning and off-line atom negativity;
   - scalar finite commutant;
   - fixed-support finite-zero interpolation.

4. `rh_master_new_probes.py`
   - complete nontrivial real finite-Witt-support list;
   - tangent Jacobian determinant \(-1/6\);
   - q-ary carry identity for several bases;
   - Archimedean constants;
   - Paley–Wiener \(A^3y^2\) law;
   - derivative-microscope widths;
   - base-resolvent preconditioner identity;
   - four-moment constants;
   - synthetic Hankel mutation sensitivity;
   - bandwidth/moment accessibility table.

All recorded controls passed. They certify only their finite or exact algebraic scope.

---

# Primary-source map

- A. Connes and W. van Suijlekom, **Quadratic Forms, Real Zeros and Echoes of the Spectral Action**, arXiv:2511.23257: <https://arxiv.org/abs/2511.23257>
- A. Connes, **The Riemann Hypothesis: Past, Present and a Letter Through Time**, arXiv:2602.04022: <https://arxiv.org/abs/2602.04022>
- M. Suzuki, **Weil’s quadratic form via the screw function**, arXiv:2606.09096: <https://arxiv.org/abs/2606.09096>
- L. Alpöge and R. Furman, **More than two thirds of the zeros of the Riemann zeta function are simple and on the critical line**, arXiv:2608.13637v2: <https://arxiv.org/html/2608.13637v2>
- A. Groskin, **A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form**, arXiv:2607.02828: <https://arxiv.org/abs/2607.02828>
- A. Connes, C. Consani, and H. Moscovici, **Zeta Spectral Triples**, arXiv:2511.22755: <https://arxiv.org/abs/2511.22755>
- A. Connes and C. Consani, **Weil positivity and Trace formula, the archimedean place**, arXiv:2006.13771: <https://arxiv.org/abs/2006.13771>
- H. Yoshida, **On Hermitian Forms attached to Zeta Functions** (1992): <https://projecteuclid.org/proceedings/advanced-studies-in-pure-mathematics/Zeta-Functions-in-Geometry/Chapter/On-Hermitian-Forms-attached-to-Zeta-Functions/10.2969/aspm/02110281>
- O. Amini and M. Piquerez, **Hodge theory for tropical varieties**, arXiv:2007.07826: <https://arxiv.org/abs/2007.07826>
- D. Platt and T. Trudgian, rigorous verification of RH to height \(3\cdot10^{12}\), arXiv:2004.09765: <https://arxiv.org/abs/2004.09765>
- B. Rodgers and T. Tao, **The de Bruijn–Newman constant is non-negative**, arXiv:1801.05914: <https://arxiv.org/abs/1801.05914>
- C. Moree, **The formal series Witt transform**, arXiv:math/0311194: <https://arxiv.org/abs/math/0311194>

---

# Final verdict

The tide rose in three distinct senses.

First, the arithmetic frame became exact:

\[
\boxed{
\text{unrestricted multiplicity is the unique nonnegative single-layer occupancy law,}
}
\]

and the exceptional finite-layer deformations are completely classified.

Second, the operator wall became narrower:

\[
\boxed{
\text{the hard object is not an unknown Hermitian operator, but a pole-free base with controlled Morse index and conditioning.}
}
\]

The explicit \(\Xi\)-radical and rank-one preconditioner remove much of the former selection fog.

Third, the partial-progress route became quantitative:

\[
\boxed{
\text{one quartic prime-side scalar can raise the unconditional density theorem.}
}
\]

The full-RH and weaker-theorem tracks now share the same centered arithmetic fluctuation but ask different questions of it:

\[
\text{local base geometry and parity selection}
\quad\text{versus}\quad
\text{high-zero trace moments and inertia}.
\]

No wall was crossed by rhetoric. Several false walls were removed, several mirrors were labeled, and the remaining proof obligations are concrete enough to be attacked or killed.

The most valuable next four deliverables are:

1. a publication-grade finite-Witt/necklace note;
2. a complete fixed-Hermite dual-tail lemma;
3. cutoff-free certified base inertia and conditioning data;
4. the full quartic prime resonance expansion.

That is the current master state of the program.