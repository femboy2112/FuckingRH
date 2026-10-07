# Critical endpoint strict contraction: unconditional invertibility of \(I\pm H_{1/2,a}\)

**Date:** 2026-10-06  
**Status:** theorem/proof extending Suzuki's finite-horizon strict-contraction argument to the endpoint \(\omega=\tfrac12\). **RH remains open.**

## 0. Result

Let \(H_{\omega}\) be Suzuki's full multiplicative Hankel operator and

\[
H_{\omega,a}=P_aH_\omega P_a
\]

its truncation to \(L^2(0,a)\).

Then at the exact critical endpoint,

\[
\boxed{
\|H_{1/2,a}\|<1
\qquad(a>1).
}
\]

Consequently,

\[
\boxed{
I\pm H_{1/2,a}
\text{ are boundedly invertible on }L^2(0,a).
}
\]

This removes the finite-horizon invertibility obstruction at the half-density point. It does **not** by itself construct the critical canonical system, because the determinant/variation machinery must still be adapted to the non-Hilbert--Schmidt kernel.

---

## 1. Inputs already available unconditionally at \(\omega=1/2\)

Suzuki's Lemma 4.1 says:

> If \(\Theta_\omega\) is inner in \(\mathbb C_+\), then \(H_\omega\) extends to an isometry on \(L^2(0,\infty)\).

Suzuki explicitly notes that innerness holds unconditionally for

\[
\omega\ge \frac12.
\]

Therefore

\[
\boxed{
H_{1/2}:L^2(0,\infty)\to L^2(0,\infty)
\text{ is an isometry}.
}
\]

So

\[
\|H_{1/2}f\|=\|f\|.
\]

The second required input is finite-horizon compactness. Suzuki later states that \(H_{\omega,a}\) remains compact for every \(\omega>0\), because the kernel is a finite sum of weakly singular kernels. A direct proof also follows from local \(L^1\) approximation plus the Schur test.

Thus

\[
\boxed{
H_{1/2,a}
\text{ is compact and self-adjoint}.
}
\]

---

# 2. Endpoint support lemma

We extend Suzuki's Lemma 4.3 to \(\omega=1/2\).

### Theorem

Let \(a>0\). If

\[
f\in L^2(0,\infty)
\]

and \(P_af\) is compactly supported, then

\[
H_{1/2}P_af
\]

cannot have compact support unless it is identically zero.

### Proof

Assume for contradiction that

\[
H_{1/2}P_af\neq0
\]

has compact support.

By the Paley--Wiener theorem, its shifted Mellin/Fourier transform

\[
\mathcal F_{1/2}H_{1/2}P_af(z)
\]

is an entire function of exponential type.

Because \(\Theta_{1/2}\) is inner, Suzuki's transform identity holds in the upper half-plane:

\[
\boxed{
\mathcal F_{1/2}H_{1/2}P_af(z)
=
\Theta_{1/2}(z)
\mathcal F_{1/2}P_af(-z).
}
\]

At the endpoint,

\[
\Theta_{1/2}(z)
=
\frac{
\xi(-iz)
}{
\xi(1-iz)
}.
\]

Let

\[
F(z)=\mathcal F_{1/2}P_af(-z).
\]

The denominator

\[
E(z)=\xi(1-iz)
\]

has no zeros on the real \(z\)-axis, by the classical zero-free theorem on

\[
\Re s=1.
\]

The same pole-cancellation argument used by Suzuki therefore applies: because the left-hand side is entire, all denominator zeros encountered in the analytic continuation must be canceled by zeros of \(F\), and

\[
\boxed{
G(z):=\frac{F(z)}{\xi(1-iz)}
}
\]

extends to an entire function.

Hence

\[
\boxed{
\mathcal F_{1/2}H_{1/2}P_af(z)
=
\xi(-iz)\,G(z)
}
\]

as an entire identity.

Now \(\xi(-iz)\) has exactly the nontrivial xi zeros transported linearly into the \(z\)-plane. Its zero count in \(|z|\le T\) is

\[
\asymp T\log T.
\]

Therefore the nonzero entire function on the left would have at least

\[
cT\log T
\]

zeros in the disk of radius \(T\), counting multiplicity, for large \(T\).

But every nonzero entire function of exponential type has only

\[
O(T)
\]

zeros in such disks, by Jensen-type zero counting.

Contradiction.

Thus

\[
\boxed{
H_{1/2}P_af
\text{ cannot be nonzero and compactly supported}.
}
\]

\(\square\)

---

## 3. Strict contraction of the finite truncation

Take nonzero

\[
f\in L^2(0,a).
\]

Extend \(f\) by zero outside \((0,a)\), so \(P_af=f\).

Because the full operator is an isometry,

\[
\|H_{1/2}f\|=\|f\|.
\]

The truncation is

\[
H_{1/2,a}f=P_aH_{1/2}f.
\]

Therefore

\[
\|H_{1/2,a}f\|
\le
\|H_{1/2}f\|
=
\|f\|.
\]

Suppose equality held:

\[
\|P_aH_{1/2}f\|
=
\|H_{1/2}f\|.
\]

Then the \(L^2\) mass of \(H_{1/2}f\) outside \((0,a)\) would vanish, so

\[
H_{1/2}f(x)=0
\]

for almost every \(x>a\).

On the other side, the support property

\[
h_{1/2}(u)=0
\qquad(0<u<1)
\]

gives

\[
H_{1/2}f(x)=0
\]

for

\[
0<x<1/a.
\]

Therefore \(H_{1/2}f\) would have compact support contained in

\[
[1/a,a].
\]

The endpoint support lemma says this is impossible for nonzero \(f\).

Hence

\[
\boxed{
\|H_{1/2,a}f\|<\|f\|
\qquad(f\neq0).
}
\]

---

## 4. Compactness upgrades strict vector contraction to a strict operator-norm gap

The previous statement alone does not imply

\[
\|H_{1/2,a}\|<1
\]

for an arbitrary noncompact contraction.

Here compactness is essential.

Since \(H_{1/2,a}\) is compact and self-adjoint, if its norm were \(1\), then one of

\[
+1,\qquad -1
\]

would be an eigenvalue.

So there would exist nonzero \(f\) with

\[
\|H_{1/2,a}f\|=\|f\|,
\]

contradicting the strict inequality above.

Therefore

\[
\boxed{
\|H_{1/2,a}\|<1.
}
\]

Consequently,

\[
\boxed{
\pm1\notin\operatorname{Spec}(H_{1/2,a}),
}
\]

and

\[
\boxed{
(I\pm H_{1/2,a})^{-1}
}
\]

exist and are bounded.

---

# 5. Why Suzuki stated \(>1/2\) in Lemma 4.4

In the local development of Section 4, Suzuki first obtains compactness via the Hilbert--Schmidt estimate

\[
h_\omega\in L^2_{\rm loc},
\]

which requires

\[
\omega>\frac12.
\]

At the endpoint this particular route fails.

However Suzuki later explicitly observes that for every \(\omega>0\),

\[
H_{\omega,a}
\]

is still compact because its kernel is a finite sum of weakly singular kernels.

Thus at \(\omega=1/2\):

- Hilbert--Schmidt fails;
- compactness does not;
- innerness/isometry still holds unconditionally;
- the support argument still works.

This permits the endpoint extension.

---

# 6. Immediate consequence for the critical determinant program

The candidate

\[
m^{[3]}_{1/2}(a)
=
e^{2\tau_1(a)}
\frac{
\det_3(I+H_{1/2,a})
}{
\det_3(I-H_{1/2,a})
}
\]

now has **no finite-horizon denominator-zero obstruction**.

Because

\[
\|H_{1/2,a}\|<1,
\]

both

\[
I+H_{1/2,a},
\qquad
I-H_{1/2,a}
\]

are invertible.

So, once \(S_3\)-membership is fully formalized, the regularized determinant ratio is well-defined for every finite \(a\).

The next wall is not invertibility.

It is the **variation/canonical-system identity** for the regularized determinant.

---

## 7. Relation to the discrete conductor realization

The exact factorization

\[
H_{1/2,a}
=
V_a^*\mathbb G_aV_a
\]

shows that the same strict contraction theorem applies to the completed interaction of all finite conductor channels active at horizon \(a\).

Thus no finite set of SUCC conductor interactions reaches unit gain.

Any RH obstruction cannot appear as a finite-horizon eigenvalue \(\pm1\) at the critical endpoint.

This strongly supports the viewpoint that the remaining difficulty is in the continuous canonical evolution / infinite-horizon organization rather than a finite arithmetic singularity.

---

## 8. What remains open

This theorem does **not** prove:

- that \(m^{[3]}_{1/2}\) is Suzuki's correct critical determinant;
- the first-order canonical-system variation law;
- that the terminal \(a\to\infty\) system has the desired \(\xi\)-data;
- RH.

It removes one concrete finite-horizon wall.

---

## 9. House statement

\[
\boxed{
\text{At critical half-density the finite Suzuki machine is still strictly passive.}
}
\]

\[
\boxed{
\text{What breaks is Hilbert--Schmidt determinant technology, not invertibility.}
}
\]

That materially changes where the next proof attempt should concentrate.
