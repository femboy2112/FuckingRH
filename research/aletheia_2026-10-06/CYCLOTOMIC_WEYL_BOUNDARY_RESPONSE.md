# Cyclotomic innovation as a finite Weyl boundary response

**Date:** 2026-10-06  
**Status:** exact identity linking conductor blocks, boundary Green functions, and Euler-factor innovations. **RH remains open.**

The exact-conductor cyclotomic blocks have a canonical boundary vector, and their boundary resolvent reproduces the scale-by-scale Euler innovation.

This closes another loop between the finite LCM clock and Weyl theory.

---

## 1. Exact-conductor unitary

Let

\[
q=p^k.
\]

Let

\[
W_q
\]

be the exact-conductor-\(q\) innovation subspace.

Successor restricted to this space is a unitary

\[
U_q
\]

with spectrum

\[
\operatorname{Spec}(U_q)
=
\{
\omega:
\omega^q=1,\ \omega\text{ primitive}
\}.
\]

Its characteristic polynomial is

\[
\boxed{
\det(zI-U_q)
=
\Phi_q(z).
}
\]

---

## 2. Canonical carry-boundary vector

Take the point/carry state at residue \(0\) and project it orthogonally into \(W_q\).

After normalization, obtain

\[
\boxed{
v_q\in W_q.
}
\]

In the primitive-character eigenbasis of \(U_q\),

\[
\boxed{
v_q
=
\frac1{\sqrt{\varphi(q)}}
\sum_{\omega\ {\rm primitive}\ q}
e_\omega.
}
\]

So every primitive conductor phase couples equally to the carry boundary.

This vector is canonical; no phase fitting is required.

---

## 3. Boundary resolvent

For \(|x|<1\), define

\[
\boxed{
R_q(x)
=
\langle
v_q,
(I-xU_q)^{-1}
v_q
\rangle.
}
\]

In the eigenbasis,

\[
R_q(x)
=
\frac1{\varphi(q)}
\sum_{\omega\ {\rm primitive}\ q}
\frac1{1-x\omega}.
\]

---

## 4. Exact cyclotomic formula

Because the primitive roots are closed under reciprocal,

\[
\Phi_q(x)
=
\prod_{\omega\ {\rm primitive}\ q}
(1-x\omega)
\]

up to the standard harmless unit/sign convention, which is \(1\) at \(x=0\).

Therefore

\[
\frac{d}{dx}\log\Phi_q(x)
=
-\sum_{\omega}
\frac{\omega}{1-x\omega}.
\]

Use

\[
\frac1{1-x\omega}
=
1+
\frac{x\omega}{1-x\omega}.
\]

Summing gives

\[
\sum_\omega
\frac1{1-x\omega}
=
\varphi(q)
-
x\frac{\Phi_q'(x)}{\Phi_q(x)}.
\]

Hence

\[
\boxed{
R_q(x)
=
1
-
\frac{x}{\varphi(q)}
\frac{\Phi_q'(x)}{\Phi_q(x)}.
}
\]

This is exact.

---

## 5. Carathéodory version

Define the boundary Carathéodory response

\[
\boxed{
F_q(x)
=
\langle
v_q,
(I+xU_q)(I-xU_q)^{-1}
v_q
\rangle.
}
\]

Since

\[
(I+xU)(I-xU)^{-1}
=
2(I-xU)^{-1}-I,
\]

\[
\boxed{
F_q(x)
=
2R_q(x)-1.
}
\]

Thus

\[
\boxed{
1-R_q(x)
=
\frac{1-F_q(x)}2.
}
\]

For disk spectral variable \(x\), \(F_q\) is the scalar boundary compression of a finite unitary Weyl/Carathéodory block.

---

## 6. Euler innovation is the centered boundary response

Previous work defined

\[
\mathcal I_{p,k}(s)
=
-\partial_s
\log\Phi_{p^k}(p^{-s}).
\]

Let

\[
x=p^{-s}.
\]

Then

\[
\frac{dx}{ds}
=
-(\log p)x.
\]

Therefore

\[
\mathcal I_{p,k}(s)
=
(\log p)x
\frac{\Phi_q'(x)}{\Phi_q(x)}.
\]

Using the boundary-resolvent formula,

\[
\boxed{
\mathcal I_{p,k}(s)
=
(\log p)
\varphi(q)
[1-R_q(p^{-s})].
}
\]

Equivalently,

\[
\boxed{
\mathcal I_{p,k}(s)
=
\frac{
(\log p)\varphi(q)
}{2}
[
1-F_q(p^{-s})
].
}
\]

So the positive scale-by-scale source response is a **centered finite Weyl boundary response of the new conductor block**.

---

## 7. Positivity on the real safe axis

For real

\[
s>0,
\qquad
0<x=p^{-s}<1,
\]

the prime-power cyclotomic polynomial

\[
\Phi_{p^k}(x)
=
1+x^{p^{k-1}}+\cdots+x^{(p-1)p^{k-1}}
\]

is positive and increasing.

Therefore

\[
\mathcal I_{p,k}(s)>0.
\]

So

\[
R_q(x)<1
\]

on the real radial interval \(0<x<1\).

This is the finite Weyl boundary form of the previously observed positive conductor innovation.

---

## 8. Telescoping becomes a sum of Weyl boundary deficits

Since

\[
-\partial_s\log L_p(s)
=
\sum_{k\ge1}
\mathcal I_{p,k}(s),
\]

we now have

\[
\boxed{
-\partial_s\log L_p(s)
=
\sum_{k\ge1}
(\log p)\varphi(p^k)
\left[
1-
R_{p^k}(p^{-s})
\right].
}
\]

At

\[
s=\frac12,
\]

\[
\boxed{
M_p
=
\sum_{k\ge1}
(\log p)\varphi(p^k)
\left[
1-
R_{p^k}(p^{-1/2})
\right].
}
\]

Thus the local Brownian repair coefficient is the total boundary-response deficit accumulated over all exact-conductor Weyl refinements.

---

## 9. Conceptual closure

We previously had:

\[
\text{cyclotomic determinant}
\to
\text{Euler factor}.
\]

Now we have:

\[
\boxed{
\text{cyclotomic boundary Weyl response}
\to
\text{logarithmic derivative of the Euler factor}.
}
\]

So both the local determinant and its source/log-derivative live inside the same finite Weyl block.

---

## 10. Why this matters for the global program

A prime-power event does not merely append an abstract determinant factor.

It supplies:

- a finite unitary state space \(W_q\);
- a canonical carry-boundary vector \(v_q\);
- a Weyl boundary response \(R_q\);
- a determinant \(\Phi_q\);
- a positive source innovation \(\mathcal I_{p,k}\).

This is exactly the data needed for a network/scattering interpretation.

The remaining problem is to interconnect these finite Weyl blocks chronologically and incorporate the paired Archimedean completion while retaining passivity.

---

## 11. House slogan

\[
\boxed{
\text{The cyclotomic factor is the block determinant.}
}
\]

\[
\boxed{
\text{Its logarithmic derivative is what the carry boundary sees.}
}
\]

\[
\boxed{
\text{Euler's local source is the accumulated Weyl boundary deficit of conductor refinement.}
}
\]
