# Positive critical det_3 Hamiltonian candidate

**Date:** 2026-10-06  
**Status:** finite-horizon positivity theorem conditional only on the already established/derived \(S_3\) classification. The canonical-system identification is still open. **RH remains open.**

---

## 1. Finite critical operator facts

For every finite

\[
a>1,
\]

the preceding notes give

\[
\boxed{
T_a:=H_{1/2,a}
=
T_a^*,
}
\]

\[
\boxed{
\|T_a\|<1,
}
\]

and

\[
\boxed{
T_a\in S_3.
}
\]

Therefore its eigenvalues are real,

\[
\lambda_j(a)\in(-1,1),
\]

with

\[
\sum_j|\lambda_j|^3<\infty.
\]

---

## 2. Third regularized determinant eigenvalue product

For self-adjoint \(T\in S_3\),

\[
\boxed{
\det_3(I+T)
=
\prod_j
(1+\lambda_j)
\exp\left(
-\lambda_j+\frac{\lambda_j^2}{2}
\right).
}
\]

Similarly,

\[
\boxed{
\det_3(I-T)
=
\prod_j
(1-\lambda_j)
\exp\left(
\lambda_j+\frac{\lambda_j^2}{2}
\right).
}
\]

Because

\[
-1<\lambda_j<1,
\]

every individual factor in both products is strictly positive.

Hence

\[
\boxed{
\det_3(I+T_a)>0,
\qquad
\det_3(I-T_a)>0.
}
\]

No sign ambiguity remains.

---

## 3. Critical renormalized determinant ratio

Define the finite diagonal counterterm

\[
\boxed{
\tau_1(a)
=
\int_0^a
h_{1/2}(x^2)\,dx.
}
\]

It is real and finite.

Define

\[
\boxed{
m_3(a)
=
e^{2\tau_1(a)}
\frac{
\det_3(I+T_a)
}{
\det_3(I-T_a)
}.
}
\]

Then

\[
\boxed{
m_3(a)>0
\qquad(a>1).
}
\]

This is unconditional once the \(S_3\) theorem and strict contraction are accepted.

---

## 4. Eigenvalue form of the logarithm

Taking logs,

\[
\begin{aligned}
\log m_3(a)
&=
2\tau_1(a)
+
\sum_j
\left[
\log\frac{1+\lambda_j}{1-\lambda_j}
-
2\lambda_j
\right].
\end{aligned}
\]

The summand has expansion

\[
\boxed{
\log\frac{1+\lambda}{1-\lambda}
-
2\lambda
=
2\sum_{m\ge1}
\frac{\lambda^{2m+1}}{2m+1}.
}
\]

Its leading term is

\[
\frac{2}{3}\lambda^3.
\]

Therefore the series converges absolutely because

\[
T_a\in S_3.
\]

This makes the renormalization transparent:

- the non-summable first spectral moment is replaced by the finite kernel-diagonal counterterm \(\tau_1\);
- all remaining spectral contributions start at cubic order and are trace class.

---

## 5. Candidate critical Hamiltonian

Define

\[
\boxed{
\mathcal H_3(a)
=
\begin{pmatrix}
m_3(a)^{-2}&0\\
0&m_3(a)^2
\end{pmatrix}.
}
\]

Since

\[
m_3(a)>0,
\]

\[
\boxed{
\mathcal H_3(a)\succ0
}
\]

for every finite \(a>1\).

Also

\[
\boxed{
\det\mathcal H_3(a)=1.
}
\]

So the candidate has exactly the positive diagonal determinant-one form of Suzuki's canonical Hamiltonian in the regular regime.

---

## 6. Positivity is no longer the endpoint obstruction

The critical endpoint problem can now be separated into:

### solved/available at finite horizon

- boundedness;
- compactness;
- self-adjointness;
- strict contraction;
- \(S_3\) regularity;
- invertibility of \(I\pm T_a\);
- positivity of the regularized determinant ratio;
- positivity of the candidate Hamiltonian.

### still open

- prove \(m_3(a)\) has the correct variation law at and between conductor seams;
- define/verify the Stieltjes jump law at \(a=\sqrt n\);
- construct the corresponding entire canonical solutions \(A_a,B_a\);
- prove the terminal/boundary data reproduce Suzuki's \(\Theta_{1/2}\).

Thus the endpoint wall has become **identification**, not positivity.

---

## 7. Overlap consistency

When \(T_a\) lies in a stronger class where Suzuki's original Fredholm determinant is available,

\[
m_{\rm Suzuki}(a)
=
\frac{D(I+T_a)}{D(I-T_a)}.
\]

The regularized determinant identities give

\[
\boxed{
m_{\rm Suzuki}(a)
=
e^{2\tau_1(a)}
\frac{\det_3(I+T_a)}{\det_3(I-T_a)}
=
m_3(a),
}
\]

provided the diagonal counterterm is the classical first Fredholm trace.

Therefore the candidate is not an arbitrary positive replacement: it agrees with the established object in the common regular regime.

---

## 8. Most important next theorem

### Critical determinant-identification theorem

Prove that \(m_3(a)\) generates the same canonical evolution that Suzuki obtains from the ordinary Fredholm determinant when \(\omega>1\).

Concretely, derive the boundary coefficient \(\mu_3(a)\) from

\[
d\log m_3(a)
\]

as a measure in \(a\), including the conductor-entry seams, and prove that the resulting product-integral canonical system has scattering function

\[
\boxed{
\Theta_{1/2}(z)
=
\frac{\xi(-iz)}{\xi(1-iz)}.
}
\]

This is now the critical endpoint theorem target.

---

## 9. House result

\[
\boxed{
\text{The critical finite Hamiltonian can already be made positive.}
}
\]

\[
\boxed{
\text{The remaining question is whether it is the right Hamiltonian.}
}
\]

That is a substantially narrower wall than the one we started with.
