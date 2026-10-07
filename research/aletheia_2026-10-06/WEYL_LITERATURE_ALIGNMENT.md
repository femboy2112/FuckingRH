# Weyl/CMV/de Branges literature alignment for the SUCC/FUCC program

**Date:** 2026-10-06  
**Purpose:** identify which pieces of the present program are standard spectral machinery and which pieces remain genuinely arithmetic research.

## 1. Matrix-valued CMV / Weyl--Titchmarsh theory

Stephen Clark, Fritz Gesztesy, Maxim Zinchenko,
**"Weyl-Titchmarsh Theory and Borg-Marchenko-type Uniqueness Results for CMV Operators with Matrix-Valued Verblunsky Coefficients"**, arXiv:1002.0387.

Relevant established facts:

- matrix-valued coefficients with norm \(<1\);
- half/full-lattice unitary CMV operators;
- matrix-valued Weyl--Titchmarsh functions;
- Green-matrix/boundary-response formulation;
- inverse/uniqueness theorems.

Alignment with this repository:

\[
A_{p,k}=p^{-1/2}U_{p,k}^{\rm new}
\]

is exactly of the matrix-contraction type that naturally belongs in block-CMV/Schur theory.

What is *not* supplied by the literature is the arithmetic derivation of these blocks or their chronological carry interconnection.

---

## 2. Operator-valued Schur problem

Yury Arlinskiĭ,
**"The Schur problem and block operator CMV matrices"**, arXiv:1307.0402.

The paper uses block operator CMV matrices to describe contractive analytic operator-valued Schur-class functions.

Alignment:

The local prime blocks

\[
S_{p,k}(z)=zA_{p,k}
\]

are operator-valued Schur functions.

This provides a mature formalism for converting a sequence/network of contractions into a unitary realization.

Again, the arithmetic problem is to prove that the SUCC/carry chronology picks the correct realization whose safe-region response is \(m_\Xi\).

---

## 3. Clark finite-rank perturbations

Constanze Liaw, Sergei Treil,
**"General Clark model for finite rank perturbations"**, arXiv:1706.01993.

Relevant established facts:

- unitary finite-rank perturbations with fixed range can be parametrized by unitary matrices;
- rank-one unitary perturbations give the classical Aleksandrov--Clark family;
- purely contractive parameters give contractions and functional models;
- vector-valued Cauchy-transform boundary machinery exists.

Alignment:

The exact LCM refinement sectors

\[
U_L(\omega)
=
C_L+(\omega-1)|0\rangle\langle L-1|
\]

are rank-one unitary boundary perturbations.

The prime phases \(\omega_p^r\) are therefore naturally Clark-family parameters.

The new arithmetic content is that these parameters are not externally chosen boundary conditions: they are generated causally by prime-power carry refinement.

---

## 4. de Branges inverse spectral theorem

A convenient modern statement appears in:

Matthias Langer, Raphael Pruckner, Harald Woracek,
**"Canonical systems whose Weyl coefficients have regularly varying asymptotics"**, arXiv:2201.01522.

The paper states the de Branges inverse theorem as a bijection, after trace normalization, between positive semidefinite canonical Hamiltonians and Nevanlinna/Weyl functions.

Alignment:

Once a global arithmetic Herglotz function

\[
m_{\rm SF}
\]

has been constructed, a canonical-system realization follows from standard inverse spectral theory.

Therefore the current program does not need to guess the final continuous Hamiltonian first.

It can focus on the finite causal boundary response.

---

## 5. Standard machinery versus arithmetic research

### Standard / available

- Carathéodory \(\leftrightarrow\) Schur Cayley transform;
- Herglotz/Nevanlinna representation;
- \(SU(1,1)\)/\(SL(2,\mathbb R)\) transfer actions;
- Julia unitary colligations;
- block-CMV realizations;
- Clark boundary perturbations;
- Weyl functions and inverse uniqueness;
- de Branges canonical systems.

### Derived here from arithmetic

- p-adic ball Gram
  \[
  r^{|j-k|}
  \]
  with
  \[
  r=p^{-1/2};
  \]

- exact-conductor Ramanujan innovation spaces;

- cyclotomic SUCC twist matrices;

- rank-one global carry-boundary refinement;

- local contraction
  \[
  A_{p,k}=p^{-1/2}U_{p,k}^{\rm new};
  \]

- critical event/quarter-density normalization;

- finite causal Euler determinant;

- completed causal prime/Gamma transform;

- safe-half-plane alignment
  \[
  s=\frac12-iz,\quad \Im z>1/2\Rightarrow\Re s>1.
  \]

### Still missing

The genuinely new theorem would be:

> The finite completed SUCC/FUCC carry network admits a passive/Schur realization whose safe-region boundary response converges to the Cayley transform of \(-\Xi'/\Xi\).

That is not supplied by standard Weyl/CMV theory.

---

## 6. Why the literature is encouraging but not a proof

The literature confirms that the categories of objects we independently reached are mathematically natural:

\[
\text{rank-one boundary twists}
\to
\text{Clark theory},
\]

\[
\text{contractive matrix coefficients}
\to
\text{block CMV},
\]

\[
\text{boundary Green functions}
\to
\text{Weyl--Titchmarsh},
\]

\[
\text{Herglotz limit}
\to
\text{canonical system}.
\]

It does **not** identify the Riemann zeta function with our arithmetic network.

That identification remains the load-bearing research problem.

## 7. Research posture

Use the standard theory aggressively for:

- positivity preservation;
- realization theorems;
- normal-family compactness;
- gauge equivalence;
- inverse uniqueness.

Do not spend research effort re-proving mature spectral facts unless a normalization/sign issue requires it.

Spend effort on:

\[
\boxed{
\text{arithmetic construction}
+
\text{finite completion}
+
\text{safe-region matching}.
}
\]
