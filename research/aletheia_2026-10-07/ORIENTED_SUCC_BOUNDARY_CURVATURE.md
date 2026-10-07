# Oriented SUCC boundary commutators give exact two-prime curvature

**Date:** 2026-10-07  
**Status:** exact finite arithmetic/operator theorem. No RH assumption. The relation to the completed Suzuki/Weil form beyond coefficient scale is still open.  
**RH remains open.**

Bare CRT support is flat.

Pure divisibility projectors commute.

But once a support boundary is transported by the common SUCC step, distinct prime directions acquire a nonzero commutator.

This produces a canonical two-prime curvature field:

\[
\boxed{
\Omega_{p,q}
=
[[P_p,S],[P_q,S]].
}
\]

It is centered, chronology-dependent, supported purely at exact conductor \(pq\), and its weighted norm has exactly the mixed-conductor scale of Suzuki's second support jet.

This is the cleanest exact realization so far of the phrase **arithmetic interaction curvature**.

---

# 1. Divisibility projector and SUCC

Work on a finite clock whose modulus is divisible by the primes under discussion, or on the corresponding profinite cylinder space.

Let

\[
P_p
\]

be multiplication by

\[
d_p(n)=1_{p\mid n}.
\]

Let

\[
S|n\rangle=|n+1\rangle
\]

be cyclic SUCC on the finite clock.

Define the oriented \(p\)-boundary wake

\[
\boxed{
\varepsilon_p(n)
=
d_p(n+1)-d_p(n).
}
\]

Explicitly,

\[
\boxed{
\varepsilon_p(n)
=
1_{n\equiv-1\pmod p}
-
1_{n\equiv0\pmod p}.
}
\]

Then

\[
\mathbb E\varepsilon_p=0,
\]

and

\[
\boxed{
\|\varepsilon_p\|_2^2
=
\frac2p.
}
\]

---

# 2. The wake is exactly a commutator

Compute on a basis state:

\[
P_pS|n\rangle
=
d_p(n+1)|n+1\rangle,
\]

while

\[
SP_p|n\rangle
=
d_p(n)|n+1\rangle.
\]

Therefore

\[
\boxed{
[P_p,S]
=
P_pS-SP_p
=
S M_{\varepsilon_p},
}
\]

where \(M_f\) denotes multiplication by \(f\).

So the centered wake is not an ad hoc statistic.

It is the exact support/SUCC commutator.

If SUCC is removed, the support projectors commute and there is no interaction.

---

# 3. Exact conductor purity

The wake

\[
\varepsilon_p
\]

has zero mean and depends only on the residue modulo \(p\).

Since \(p\) is prime, its only possible Fourier conductors are \(1\) and \(p\).

The zero mean removes conductor \(1\).

Hence

\[
\boxed{
\varepsilon_p\in W_p.
}
\]

Normalize:

\[
\boxed{
\beta_p
=
\sqrt{\frac p2}\,
\varepsilon_p.
}
\]

Then

\[
\boxed{
\|\beta_p\|_2=1.
}
\]

For distinct primes, CRT gives

\[
\boxed{
\langle\beta_p,\beta_q\rangle=0.
}
\]

---

# 4. Cross Gram fuses conductors

Define the normalized oriented leg

\[
\boxed{
E_p
=
S M_{\beta_p}.
}
\]

Then

\[
E_p^*E_q
=
M_{\beta_p\beta_q}
\]

because

\[
S^*S=I.
\]

For distinct \(p,q\),

\[
\beta_p\beta_q
\]

is a tensor product of nontrivial functions on the two CRT factors.

Therefore

\[
\boxed{
\beta_p\beta_q\in W_{pq}.
}
\]

And

\[
\boxed{
\|\beta_p\beta_q\|_2^2=1.
}
\]

Thus the cross Gram of two oriented one-prime legs is a unit-energy exact-\(pq\) interaction.

This is the operator version of the conductor-fusion theorem from the parallel loop-undertone branch.

---

# 5. Exact Suzuki weighting of the cross Gram

For one prime,

\[
\boxed{
b_\omega(p)
=
p^{\omega-\frac12}
(1-p^{-2\omega}).
}
\]

Define the weighted leg

\[
\boxed{
D_{p,\omega}
=
\sqrt{b_\omega(p)}\,
E_p.
}
\]

Use normalized Haar trace \(\tau\) on the finite CRT clock.

Since

\[
\tau(M_{|\beta_p|^2})=1,
\]

\[
\boxed{
\tau(D_{p,\omega}^*D_{p,\omega})
=
b_\omega(p).
}
\]

For distinct \(p,q\),

\[
D_{p,\omega}^*D_{q,\omega}
=
\sqrt{b_\omega(p)b_\omega(q)}
M_{\beta_p\beta_q}.
\]

Hence

\[
\boxed{
\left\|
D_{p,\omega}^*D_{q,\omega}
\right\|_{2,\tau}^2
=
b_\omega(p)b_\omega(q).
}
\]

But \(b_\omega\) is multiplicative on coprime integers:

\[
b_\omega(pq)
=
b_\omega(p)b_\omega(q).
\]

Therefore

\[
\boxed{
\left\|
D_{p,\omega}^*D_{q,\omega}
\right\|_{2,\tau}^2
=
b_\omega(pq).
}
\]

This is exact.

The Suzuki mixed conductor coefficient is literally the Hilbert--Schmidt energy of the cross Gram between the two one-prime oriented support legs.

---

# 6. Small-omega second jet

As \(\omega\downarrow0\),

\[
b_\omega(p)
=
2\omega
\frac{\log p}{\sqrt p}
+
O(\omega^2).
\]

Therefore

\[
b_\omega(pq)
=
4\omega^2
\frac{\log p\log q}{\sqrt{pq}}
+
O(\omega^3).
\]

The cross-Gram theorem gives the same result automatically:

\[
\left\|
D_{p,\omega}^*D_{q,\omega}
\right\|_{2,\tau}^2
=
4\omega^2
\frac{\log p\log q}{\sqrt{pq}}
+
O(\omega^3).
\]

So the second Suzuki support jet is the first nonlinear interaction energy of the normalized one-prime boundary legs.

This is stronger than a coefficient coincidence.

It is an exact finite Hilbert-space factorization.

---

# 7. Genuine order curvature

The cross Gram above measures interaction but not ordering.

To measure path/order dependence, take the commutator of the oriented legs.

Because

\[
M_fS
=
S M_{f(\cdot+1)},
\]

we have

\[
E_pE_q
=
S^2
M_{
\beta_p(\cdot+1)\beta_q
},
\]

while

\[
E_qE_p
=
S^2
M_{
\beta_q(\cdot+1)\beta_p
}.
\]

Therefore

\[
\boxed{
[E_p,E_q]
=
S^2M_{\Omega_{p,q}},
}
\]

where

\[
\boxed{
\Omega_{p,q}(n)
=
\beta_p(n+1)\beta_q(n)
-
\beta_q(n+1)\beta_p(n).
}
\]

This field changes sign under

\[
p\leftrightarrow q.
\]

It is a genuine oriented two-form.

---

# 8. Curvature lives purely at conductor pq

Translation preserves exact conductor.

Thus

\[
\beta_p(\cdot+1)\in W_p,
\]

\[
\beta_q(\cdot+1)\in W_q.
\]

Products of a nontrivial \(p\)-mode and a nontrivial \(q\)-mode lie in

\[
W_{pq}.
\]

Therefore both terms in \(\Omega_{p,q}\) lie in \(W_{pq}\), and hence

\[
\boxed{
\Omega_{p,q}\in W_{pq}.
}
\]

Its mean is automatically zero.

So the curvature does not leak into one-body or DC sectors.

---

# 9. Universal curvature norm

First use the unnormalized wakes.

Define

\[
F_{p,q}(n)
=
\varepsilon_p(n+1)\varepsilon_q(n)
-
\varepsilon_q(n+1)\varepsilon_p(n).
\]

For distinct odd primes \(p,q\):

- each ordered product has \(4\) CRT support points;
- they overlap at exactly the common \((-1,-1)\) phase;
- at that phase the two contributions agree and cancel;
- the remaining \(6\) points have magnitude \(1\).

Therefore

\[
\boxed{
\|F_{p,q}\|_2^2
=
\frac6{pq}
\qquad
(p,q\text{ odd}).
}
\]

If one prime is \(2\), the two \(2\)-boundary phases exhaust the local clock and the support collapses to \(4\) nonzero CRT points:

\[
\boxed{
\|F_{2,q}\|_2^2
=
\frac4{2q}
=
\frac2q.
}
\]

Now

\[
\Omega_{p,q}
=
\frac{\sqrt{pq}}2
F_{p,q}.
\]

Hence

\[
\boxed{
\|\Omega_{p,q}\|_2^2
=
\begin{cases}
1,
&
2\in\{p,q\},
\\[2mm]
\frac32,
&
p,q\text{ odd}.
\end{cases}
}
\]

The normalized curvature magnitude is independent of the sizes of the primes.

Only the \(p=2\) parity degeneracy changes the universal constant.

---

# 10. Weighted curvature energy

For the weighted Suzuki legs

\[
D_{p,\omega}
=
\sqrt{b_\omega(p)}E_p,
\]

\[
[D_{p,\omega},D_{q,\omega}]
=
\sqrt{
b_\omega(p)b_\omega(q)
}
[E_p,E_q].
\]

Therefore

\[
\boxed{
\left\|
[D_{p,\omega},D_{q,\omega}]
\right\|_{2,\tau}^2
=
c_{p,q}
\,b_\omega(pq),
}
\]

where

\[
\boxed{
c_{p,q}
=
\begin{cases}
1,&2\in\{p,q\},\\[1mm]
3/2,&p,q\text{ odd}.
\end{cases}
}
\]

So the first genuine order-curvature energy carries exactly the Suzuki mixed-conductor amplitude, up to a universal local combinatorial constant.

At small \(\omega\),

\[
\boxed{
\left\|
[D_{p,\omega},D_{q,\omega}]
\right\|_{2,\tau}^2
\sim
4c_{p,q}\omega^2
\frac{\log p\log q}{\sqrt{pq}}.
}
\]

This is the correct second-support-jet scale.

---

# 11. Relation to the common-mode no-go

Round006 assembled boundaries of the form

\[
I-S^{h_p}.
\]

Every prime leg shared the same identity component, causing positive quadratic cross-amplification.

The present legs are fundamentally different:

\[
\boxed{
E_p
=
S M_{\beta_p},
}
\]

with

\[
\mathbb E\beta_p=0.
\]

There is no shared DC/identity mode.

Indeed,

\[
\tau(E_p^*E_q)
=
\langle\beta_p,\beta_q\rangle
=
0
\qquad(p\ne q).
\]

So the catastrophic common-mode mechanism is absent.

This does **not** prove global usefulness.

It means this oriented centered assembly survives that specific no-go.

---

# 12. Bare CRT curvature versus chronological curvature

If one keeps only the multiplication fields

\[
M_{\beta_p},
\]

then

\[
[M_{\beta_p},M_{\beta_q}]=0.
\]

So the support product itself is flat.

The nonzero curvature appears only because all prime boundaries are transported by the common successor:

\[
E_p=S M_{\beta_p}.
\]

Thus:

\[
\boxed{
\text{CRT support}
=
\text{flat base},
}
\]

\[
\boxed{
\text{SUCC-transported support boundaries}
=
\text{noncommuting connection}.
}
\]

This exactly satisfies the hostile-control requirement for a meaningful arithmetic interaction curvature.

---

# 13. Prime-power depth extension

For

\[
q=p^k,
\]

the raw boundary wake

\[
\varepsilon_q(n)
=
1_{n\equiv-1\pmod q}
-
1_{n\equiv0\pmod q}
\]

contains lower \(p\)-power harmonic components.

Project to the canonical exact-conductor space:

\[
\boxed{
\varepsilon_{p^k}^{\rm ex}
=
P_{p^k}\varepsilon_{p^k}.
}
\]

Normalize

\[
\beta_{p^k}
=
\frac{
\varepsilon_{p^k}^{\rm ex}
}{
\|\varepsilon_{p^k}^{\rm ex}\|_2
}.
\]

Then

\[
\beta_{p^k}\in W_{p^k},
\qquad
\|\beta_{p^k}\|_2=1.
\]

For distinct primes \(p\ne q\),

\[
\boxed{
\beta_{p^k}\beta_{q^\ell}
\in
W_{p^kq^\ell}
}
\]

with unit \(L^2\) norm by CRT.

Therefore define

\[
D_{p^k,\omega}
=
\sqrt{
b_\omega(p^k)
}
S M_{\beta_{p^k}}.
\]

Then exactly:

\[
\boxed{
\left\|
D_{p^k,\omega}^*
D_{q^\ell,\omega}
\right\|_{2,\tau}^2
=
b_\omega(p^kq^\ell).
}
\]

So the cross-Gram/Suzuki-weight identity extends to arbitrary coprime prime-power depths.

The ordered commutator gives the corresponding exact mixed-conductor curvature field.

---

# 14. Higher interaction hierarchy

For distinct prime-power directions

\[
q_1,\ldots,q_r
\]

with coprime moduli, normalized exact-depth wakes satisfy

\[
\boxed{
\prod_{j=1}^r\beta_{q_j}
\in
W_{\prod_jq_j},
}
\]

and the product has unit \(L^2\) norm.

Therefore

\[
\boxed{
b_\omega\!\left(
\prod_jq_j
\right)
=
\prod_jb_\omega(q_j)
}
\]

is exactly the energy of the \(r\)-body support product.

Ordered products of the transported legs

\[
E_{q_1}\cdots E_{q_r}
\]

contain shifted versions of these same exact-conductor products.

Antisymmetrizing over order gives higher discrete curvature forms.

This suggests a full support-cell exterior hierarchy:

\[
\boxed{
\text{1-body}
\to
W_p,
}
\]

\[
\boxed{
\text{2-curvature}
\to
W_{pq},
}
\]

\[
\boxed{
\text{3-curvature}
\to
W_{pqr},
}
\]

and so on.

This is an exact finite construction.

Its connection to the completed RH positivity remains to be established.

---

# 15. What has and has not been achieved

### Proved

- prime wakes are exact support/SUCC commutators;
- normalized one-prime wakes are orthogonal;
- their cross Gram fuses exactly into \(W_{pq}\);
- the squared cross-Gram norm is exactly Suzuki's \(b_\omega(pq)\);
- the order commutator is a genuine chronology-induced curvature field;
- it lies purely in \(W_{pq}\);
- its normalized norm is universal;
- the weighted curvature energy has precisely the Suzuki second-jet arithmetic scale.

### Not proved

- that this curvature supplies the missing Archimedean/global counterterm;
- that its higher-rank Schur elimination reproduces the Weil first jet;
- that the resulting completed operator is contractive;
- RH.

---

# 16. Immediate next test

The curvature object is now explicit enough for a decisive experiment.

At finite horizon:

1. construct all active exact-depth legs
   \[
   D_{p^k,\omega};
   \]

2. retain their oriented ordered products before squaring;

3. form the conductor-resolved curvature hierarchy;

4. couple the hierarchy to the exact critical/subcritical Archimedean state-space;

5. eliminate only causally active higher support cells;

6. compare the resulting first physical Schur block against the known finite Weil/Suzuki passivity defect.

The normalization is fixed.

The bare-CRT null is fixed.

The common-mode no-go is avoided.

The next result can therefore be genuinely verdict-changing.
