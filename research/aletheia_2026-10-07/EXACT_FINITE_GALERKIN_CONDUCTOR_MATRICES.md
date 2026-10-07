# Exact finite Galerkin matrices for the discrete-conductor Suzuki Hankel system

**Date:** 2026-10-07  
**Status:** exact finite-dimensional compression formula; convergence follows from compactness. Numerical evaluation still needs interval/error certification before a computed crossing is called a proof. **RH remains open.**

---

## 0. Result

The finite Suzuki operator can be represented by an explicit sequence of **finite real symmetric Hankel matrices** whose entries are built from:

1. finitely many exact conductor events \(n\le a^2\);
2. one universal Archimedean second primitive;
3. second finite differences.

The construction is Galerkin, not collocation/Nyström. Therefore every matrix is an honest orthogonal compression of the exact operator.

For mesh dimension \(M\),

\[
\boxed{
\|{\bf H}^{(M)}_{\omega,a}\|
\le
\|H_{\omega,a}\|.
}
\]

Since \(H_{\omega,a}\) is compact and the Galerkin projections converge strongly to the identity,

\[
\boxed{
\|{\bf H}^{(M)}_{\omega,a}\|
\longrightarrow
\|H_{\omega,a}\|
}
\]

along any refining dense mesh family.

Combined with the finite-Hankel contraction criterion, if RH is false then **some finite matrix in this family must eventually have norm \(>1\)** for a suitable subcritical parameter and finite horizon.

---

## 1. Logarithmic unitary transform

Define

\[
(Uf)(u)
=
e^{u/2}f(e^u).
\]

Then

\[
U:L^2((0,\infty),dx)\to L^2(\mathbb R,du)
\]

is unitary.

Write

\[
a=e^A.
\]

For the finite truncation \(H_{\omega,a}\), only the interval

\[
[-A,A]
\]

is dynamically relevant.

Indeed, after the logarithmic transform,

\[
\boxed{
(\mathbb H_{\omega,A}F)(u)
=
\int_{-A}^{A}
\mathfrak h_\omega(u+v)F(v)\,dv,
}
\]

where

\[
\boxed{
\mathfrak h_\omega(t)
=
e^{t/2}h_\omega(e^t)
}
\]

and

\[
\mathfrak h_\omega(t)=0
\qquad(t<0).
\]

Thus the multiplicative finite Hankel problem becomes an ordinary additive Hankel problem on the finite interval \([-A,A]\).

---

## 2. Exact conductor event expansion

Recall

\[
b_\omega(n)
=
\frac{c_\omega(n)}{\sqrt n}
=
n^{\omega-1/2}
\prod_{p\mid n}(1-p^{-2\omega}).
\]

Define the universal causal Archimedean kernel

\[
\boxed{
K_\omega(r)
=
e^{-r/2}g_\omega(e^{-r})\,1_{r>0}.
}
\]

Then

\[
\boxed{
\mathfrak h_\omega(t)
=
\sum_{n\ge1}
b_\omega(n)
K_\omega(t-\log n).
}
\]

For \(t\le2A\), only

\[
n\le e^{2A}=a^2
\]

can occur.

So at every finite horizon the arithmetic event content is finite:

\[
\boxed{
\mathfrak h_{\omega,A}(t)
=
\sum_{n\le a^2}
b_\omega(n)
K_\omega(t-\log n).
}
\]

At the critical endpoint,

\[
b_{1/2}(n)=\frac{\varphi(n)}n,
\]

and

\[
K_{1/2}(r)
=
2\frac{2e^{-2r}-1}{\sqrt{1-e^{-2r}}}.
\]

---

## 3. Integrate the seam twice

The weak conductor seams make point sampling a poor numerical primitive.

Instead define the causal second primitive

\[
\boxed{
F_{\omega,2}(R)
=
\begin{cases}
\displaystyle
\int_0^R (R-r)K_\omega(r)\,dr,&R>0,\\[1.2ex]
0,&R\le0.
\end{cases}
}
\]

Because

\[
K_\omega(r)\sim C_\omega r^{\omega-1},
\qquad
C_\omega=\frac{(2\pi)^\omega}{\Gamma(\omega)},
\]

and \(\omega>0\), this integral is finite.

Now define the completed finite-conductor primitive

\[
\boxed{
Q_{\omega,A}(t)
=
\sum_{n\le a^2}
b_\omega(n)
F_{\omega,2}(t-\log n).
}
\]

In distributions,

\[
\boxed{
Q_{\omega,A}''(t)
=
\mathfrak h_\omega(t)
\qquad
(-2A<t<2A).
}
\]

All square-root/fractional seams have been absorbed into an ordinary continuous primitive.

---

## 4. Uniform-cell Galerkin basis

Partition

\[
[-A,A]
\]

into \(M\) cells of width

\[
\boxed{
h=\frac{2A}{M}.
}
\]

Let

\[
I_j=[-A+jh,-A+(j+1)h),
\qquad
0\le j<M,
\]

and use normalized indicator basis functions

\[
\boxed{
e_j(u)=h^{-1/2}1_{I_j}(u).
}
\]

Let \(P_M\) be orthogonal projection onto their span.

The Galerkin compression is

\[
\boxed{
{\bf H}^{(M)}_{\omega,a}
=
P_M\mathbb H_{\omega,A}P_M.
}
\]

Its matrix entries are

\[
H^{(M)}_{ij}
=
\frac1h
\int_{I_i}\int_{I_j}
\mathfrak h_\omega(u+v)\,dv\,du.
\]

---

## 5. Exact second-difference formula

Put

\[
s_{ij}
=
-2A+(i+j)h.
\]

Since \(Q''=\mathfrak h\),

\[
\int_{I_i}\int_{I_j}
\mathfrak h_\omega(u+v)\,dv\,du
\]

is exactly the rectangular second difference

\[
Q(s_{ij}+2h)
-
2Q(s_{ij}+h)
+
Q(s_{ij}).
\]

Therefore

\[
\boxed{
H^{(M)}_{ij}
=
\frac{
Q_{\omega,A}(s_{ij}+2h)
-
2Q_{\omega,A}(s_{ij}+h)
+
Q_{\omega,A}(s_{ij})
}{h}.
}
\]

This is the central finite-matrix realization.

The entry depends only on

\[
i+j.
\]

Hence

\[
\boxed{
{\bf H}^{(M)}_{\omega,a}
\text{ is a real symmetric Hankel matrix.}
}
\]

Only \(2M+1\) values of \(Q_{\omega,A}\) are required to assemble all \(M^2\) entries.

---

## 6. The arithmetic data are explicitly finite

Each required primitive value has the form

\[
\boxed{
Q_{\omega,A}(t)
=
\sum_{\substack{n\le a^2\\ \log n<t}}
b_\omega(n)
F_{\omega,2}(t-\log n).
}
\]

Thus a matrix of arbitrary Galerkin dimension \(M\) uses only the finite conductor list

\[
1\le n\le a^2.
\]

The growth of \(M\) refines the **boundary function space**, not the arithmetic horizon.

This cleanly separates two limits:

### arithmetic/horizon limit

\[
a\to\infty
\quad\Longrightarrow\quad
n\le a^2\text{ grows};
\]

### Galerkin resolution limit

\[
M\to\infty
\quad\Longrightarrow\quad
P_M\to I
\text{ on the fixed finite interval}.
\]

These should not be conflated.

---

## 7. Exact compression and one-sided certification

Because \(P_M\) is an orthogonal projection,

\[
\boxed{
\|{\bf H}^{(M)}_{\omega,a}\|
=
\|P_M\mathbb H_{\omega,A}P_M\|
\le
\|\mathbb H_{\omega,A}\|
=
\|H_{\omega,a}\|.
}
\]

Therefore:

\[
\boxed{
\|{\bf H}^{(M)}_{\omega,a}\|>1
\Longrightarrow
\|H_{\omega,a}\|>1.
}
\]

This implication is exact.

So a rigorously evaluated finite matrix crossing is a genuine certificate of loss of finite-horizon contractivity.

The converse does not hold at a fixed \(M\): a matrix below one can miss an unresolved dangerous direction.

---

## 8. Compactness makes the finite matrices complete

For every \(\omega>0\) and finite \(a\), the weakly singular operator

\[
H_{\omega,a}
\]

is compact.

Take any sequence of piecewise-constant spaces with mesh size tending to zero, preferably nested dyadic refinements. Then

\[
P_M\to I
\]

strongly.

For a compact operator \(T\), strong convergence of orthogonal projections gives

\[
\|(I-P_M)T\|\to0,
\qquad
\|T(I-P_M)\|\to0.
\]

Hence

\[
\boxed{
\|P_MTP_M-T\|\to0.
}
\]

Applying this to \(T=\mathbb H_{\omega,A}\),

\[
\boxed{
\|{\bf H}^{(M)}_{\omega,a}-\mathbb H_{\omega,A}\|
\to0.
}
\]

Consequently,

\[
\boxed{
\|{\bf H}^{(M)}_{\omega,a}\|
\to
\|H_{\omega,a}\|.
}
\]

The extremal nonzero eigenvalues converge as well.

Thus the finite matrices do not merely sample the operator. They recover it in operator norm.

---

## 9. Finite-dimensional witness theorem

Combine the previous section with the finite-Hankel contraction criterion.

### Theorem

For fixed \((\omega,a)\),

\[
\|H_{\omega,a}\|>1
\]

if and only if, along any refining dense Galerkin sequence, there exists a finite \(M\) such that

\[
\boxed{
\|{\bf H}^{(M)}_{\omega,a}\|>1.
}
\]

Therefore if RH is false, the previous contraction criterion guarantees the existence of

\[
\boxed{
(\omega,a,M)
}
\]

with all three finite parameters such that

\[
\boxed{
\lambda_{\max}({\bf H}^{(M)}_{\omega,a})>1
\quad\text{or}\quad
\lambda_{\min}({\bf H}^{(M)}_{\omega,a})<-1.
}
\]

This is an exact existential finite-matrix witness for failure of the required zero-free region.

No zeta zeros need be inserted into the matrix.

---

## 10. The critical matrix is especially explicit

At

\[
\omega=\frac12,
\]

\[
b_{1/2}(n)=\frac{\varphi(n)}n
\]

and

\[
K_{1/2}(r)
=
2\frac{2e^{-2r}-1}{\sqrt{1-e^{-2r}}}.
\]

Its first primitive is elementary. Let

\[
y(R)=\sqrt{1-e^{-2R}}.
\]

Then

\[
\boxed{
F_{1/2,1}(R)
=
\int_0^R K_{1/2}(r)\,dr
=
4y(R)-2\operatorname{artanh}y(R).
}
\]

Hence

\[
F_{1/2,2}(R)
=
\int_0^R F_{1/2,1}(u)\,du.
\]

Even without writing the resulting dilogarithmic closed form, this is a smooth one-dimensional scalar integral with no conductor seam.

The matrix entries are therefore computable from:

\[
\boxed{
\varphi(n)/n,\quad
\log n,\quad
F_{1/2,2}.
}
\]

---

## 11. Stable endpoint quadrature substitution

For general \(\omega>0\), direct quadrature of

\[
F_{\omega,2}(R)
=
\int_0^R(R-r)K_\omega(r)\,dr
\]

must respect

\[
K_\omega(r)\sim C_\omega r^{\omega-1}.
\]

Use

\[
\boxed{
r=R y^{1/\omega},
\qquad 0\le y\le1.
}
\]

Then

\[
dr
=
\frac{R}{\omega}
y^{1/\omega-1}dy,
\]

and the singular power cancels exactly:

\[
r^{\omega-1}dr
\sim
\frac{R^\omega}{\omega}\,dy.
\]

The transformed integrand has a finite \(y\to0\) limit

\[
\boxed{
\frac{C_\omega}{\omega}R^{\omega+1}.
}
\]

This is the preferred numerical route.

---

## 12. Critical numerical sanity check

A prototype implementation using the exact Galerkin formula gives, at modest mesh sizes, critical compression norms below one and increasing under refinement, as required for lower approximants to the true norm.

Representative **observed, not certified** values:

- \(a=1.2\):
  \[
  \|{\bf H}^{(48)}_{1/2,1.2}\|\approx0.9336;
  \]
- \(a=1.5\):
  \[
  \|{\bf H}^{(80)}_{1/2,1.5}\|\approx0.99978;
  \]
- \(a=2.0\):
  \[
  \|{\bf H}^{(80)}_{1/2,2.0}\|\approx0.99986.
  \]

The very small critical margin by \(a\sim1.5\)--\(2\) is itself important.

It says the subcritical continuation problem is quantitatively delicate almost immediately: a coarse Schur perturbation bound is unlikely to be competitive.

These values must not be promoted to theorem statements until the scalar primitive integration and floating-point eigensolver are enclosed by rigorous error bounds.

---

## 13. Initial subcritical probe

The same prototype, still **uncertified**, gives at \(a=1.2\), \(M=24\):

\[
\begin{array}{c|c}
\omega & \|{\bf H}^{(24)}_{\omega,1.2}\|\\
\hline
0.50 & 0.93319\\
0.49 & 0.93459\\
0.47 & 0.93739\\
0.45 & 0.94017\\
0.40 & 0.94704
\end{array}
\]

and at \(a=1.5\), \(M=24\):

\[
\begin{array}{c|c}
\omega & \|{\bf H}^{(24)}_{\omega,1.5}\|\\
\hline
0.50 & 0.99850\\
0.49 & 0.99852\\
0.47 & 0.99854\\
0.45 & 0.99857\\
0.40 & 0.99864.
\end{array}
\]

The qualitative message is consistent with the theorem:

- every fixed finite horizon has subcritical room;
- the room becomes extremely thin as the horizon grows.

But these data do **not** establish the true contraction frontier because Galerkin norms are lower bounds.

---

## 14. Next certification layer

To turn this into a proof instrument, add two bounds.

### 14.1 Scalar primitive enclosure

Compute

\[
F_{\omega,2}(R)
\]

using interval arithmetic or validated quadrature so every matrix entry lies in a certified interval.

### 14.2 Galerkin tail enclosure

Bound

\[
\|(I-P_M)H_{\omega,a}\|
+
\|H_{\omega,a}(I-P_M)\|.
\]

Then

\[
\|H_{\omega,a}\|
\le
\|{\bf H}^{(M)}_{\omega,a}\|
+
\varepsilon_{\omega,a,M}.
\]

A bound

\[
\boxed{
\|{\bf H}^{(M)}_{\omega,a}\|
+
\varepsilon_{\omega,a,M}
<1
}
\]

would certify contraction at that finite horizon.

Conversely, a certified

\[
\boxed{
\|{\bf H}^{(M)}_{\omega,a}\|>1
}
\]

already certifies failure; no tail upper bound is needed.

---

## 15. Archimedean modal truncation

The previous branch gives, at criticality,

\[
K_{1/2}(r)
=
-2
+
2\sum_{m\ge1}a_m e^{-2mr}.
\]

Below half density,

\[
K_\omega(r)
=
-\kappa_0(\omega)e^{\delta r}
+
\sum_{m\ge1}
\kappa_m(\omega)e^{-(\delta+2m)r}.
\]

Each mode has an elementary second primitive.

Therefore one can replace the scalar quadrature by a finite modal sum plus a rigorous tail.

This produces a completely finite three-index machine:

\[
\boxed{
\text{horizon }a
\;\times\;
\text{Galerkin dimension }M
\;\times\;
\text{Archimedean mode cutoff }L.
}
\]

The conductor content is already finite:

\[
n\le a^2.
\]

This is the most literal realization so far of the original “finite matrices growing causally toward the global structure” program.

---

## 16. Claim ledger

### Disclosed

- exact log-Hankel transform;
- exact finite conductor event expansion;
- exact second-primitive matrix formula;
- exact Galerkin compression property;
- operator-norm convergence by compactness;
- finite-dimensional witness theorem.

### Observed

- the prototype critical and subcritical numerical values above.

### UNVERIFIED

- rigorous interval enclosures for those numerical values;
- a useful explicit rate for Galerkin convergence;
- a scalable modal tail bound sharp enough near \(\omega\downarrow0\).

### Next verdict-changing probe

Build the validated matrix engine and measure the finite contraction frontier

\[
\Delta_M(a)
\]

under dyadic refinement, with certified one-sided bounds.

The first genuinely new zero-free theorem would be obtained from a uniform \(d>0\) such that the **upper** norm enclosure stays below one for

\[
0\le\delta<d
\]

at every horizon.
