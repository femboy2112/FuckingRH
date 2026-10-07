# Exact discrete-conductor realization of Suzuki's finite Hankel operator

**Date:** 2026-10-06  
**Status:** exact finite-horizon factorization. No RH assumption.  
**Main result:** Suzuki's scalar finite Hankel operator is the boundary compression / conductor trace of a finite direct sum of universal Archimedean blocks indexed by exact additive conductors. At \(\omega=\tfrac12\), every primitive conductor mode couples with the same amplitude \(n^{-1/2}\).

---

## 1. Suzuki's finite Hankel operator

For \(\omega>0\), Suzuki defines

\[
c_\omega(n)
=
n^\omega
\prod_{p\mid n}
(1-p^{-2\omega}),
\]

an Archimedean profile \(g_\omega\) supported on \(0<x<1\), and

\[
h_\omega(x)
=
\frac1x
\sum_{n\le x}
c_\omega(n)g_\omega(n/x)
\qquad(x>1),
\]

with \(h_\omega(x)=0\) on \(0<x<1\).

At horizon \(a>0\),

\[
\boxed{
(H_{\omega,a}f)(x)
=
\int_0^a
h_\omega(xy)f(y)\,dy.
}
\]

Since \(xy<a^2\), only integers

\[
\boxed{n<a^2}
\]

can contribute.

So the arithmetic content of every finite truncation is genuinely finite.

---

## 2. Split the kernel one conductor at a time

Define

\[
H_{\omega,a}^{(n)}
\]

by the kernel

\[
\boxed{
K_{\omega,a}^{(n)}(x,y)
=
\frac{c_\omega(n)}{xy}
g_\omega\!\left(\frac n{xy}\right).
}
\]

Because \(g_\omega(t)=0\) for \(t>1\), this automatically vanishes unless

\[
xy\ge n.
\]

Hence

\[
\boxed{
H_{\omega,a}
=
\sum_{n<a^2}
H_{\omega,a}^{(n)}.
}
\]

There is no infinite sum at finite \(a\).

---

## 3. Every conductor block is a rescaled copy of ONE universal Archimedean operator

Set

\[
\boxed{
b_\omega(n)
=
\frac{c_\omega(n)}{\sqrt n}
=
n^{\omega-\frac12}
\prod_{p\mid n}(1-p^{-2\omega}).
}
\]

For \(A>0\), define the universal operator

\[
\mathcal G_{\omega,A}:L^2(0,A)\to L^2(0,A)
\]

by

\[
\boxed{
(\mathcal G_{\omega,A}F)(u)
=
\int_0^A
\frac1{uv}
g_\omega\!\left(\frac1{uv}\right)
F(v)\,dv.
}
\]

For each \(n<a^2\), define the unitary dilation

\[
\boxed{
(T_{n,a}f)(u)
=
n^{1/4}f(\sqrt n\,u),
\qquad
0<u<a/\sqrt n.
}
\]

Indeed,

\[
\int_0^{a/\sqrt n}
|T_{n,a}f(u)|^2du
=
\int_0^a|f(x)|^2dx.
\]

A direct change of variables gives the exact identity

\[
\boxed{
T_{n,a}
H_{\omega,a}^{(n)}
T_{n,a}^{-1}
=
b_\omega(n)\,
\mathcal G_{\omega,a/\sqrt n}.
}
\]

Equivalently,

\[
\boxed{
H_{\omega,a}^{(n)}
=
b_\omega(n)\,
T_{n,a}^*
\mathcal G_{\omega,a/\sqrt n}
T_{n,a}.
}
\]

Thus Suzuki's finite operator is

\[
\boxed{
H_{\omega,a}
=
\sum_{n<a^2}
b_\omega(n)\,
T_{n,a}^*
\mathcal G_{\omega,a/\sqrt n}
T_{n,a}.
}
\]

This separates the construction exactly into:

- **discrete arithmetic event:** \(n\);
- **event coupling:** \(b_\omega(n)\);
- **scale:** \(a/\sqrt n\);
- **one universal Archimedean interaction:** \(\mathcal G_\omega\).

---

## 4. Exact-conductor SUCC spaces

Let

\[
W_n
\]

be the exact-conductor-\(n\) additive-character subspace of the finite cyclic SUCC clock.

Equivalently, \(W_n\) is spanned by

\[
\chi_{r,n}(m)
=
e^{2\pi irm/n},
\qquad
(r,n)=1.
\]

Then

\[
\boxed{
\dim W_n=\varphi(n).
}
\]

Let

\[
P_n
\]

be the corresponding Ramanujan projector.

Choose the canonical "carry-boundary" vector

\[
\boxed{
\eta_n
=
\sum_{\substack{r\bmod n\\(r,n)=1}}
\chi_{r,n}.
}
\]

Then

\[
\boxed{
\|\eta_n\|^2=\varphi(n).
}
\]

Equivalently, if \(\delta_0^{(n)}\) is the normalized residue-\(0\) point state, then

\[
\eta_n
=
\sqrt n\,P_n\delta_0^{(n)}.
\]

So this vector is determined canonically by the SUCC carry boundary.

---

## 5. Conductor-channel coupling operator

Define

\[
V_{\omega,n,a}:
L^2(0,a)
\longrightarrow
L^2(0,a/\sqrt n)\otimes W_n
\]

by

\[
\boxed{
V_{\omega,n,a}f
=
\sqrt{
\frac{b_\omega(n)}{\varphi(n)}
}\,
T_{n,a}f
\otimes
\eta_n.
}
\]

Let

\[
\mathbb G_{\omega,n,a}
=
\mathcal G_{\omega,a/\sqrt n}\otimes I_{W_n}.
\]

Then

\[
\begin{aligned}
V_{\omega,n,a}^*
\mathbb G_{\omega,n,a}
V_{\omega,n,a}
&=
\frac{b_\omega(n)}{\varphi(n)}
\|\eta_n\|^2
T_{n,a}^*\mathcal G_{\omega,a/\sqrt n}T_{n,a}\\
&=
b_\omega(n)
T_{n,a}^*\mathcal G_{\omega,a/\sqrt n}T_{n,a}.
\end{aligned}
\]

Therefore

\[
\boxed{
H_{\omega,a}^{(n)}
=
V_{\omega,n,a}^*
\mathbb G_{\omega,n,a}
V_{\omega,n,a}.
}
\]

---

## 6. Exact finite direct-sum factorization

Define the finite arithmetic environment

\[
\boxed{
\mathfrak E_{\omega,a}
=
\bigoplus_{n<a^2}
\left[
L^2(0,a/\sqrt n)\otimes W_n
\right].
}
\]

Define

\[
V_{\omega,a}
=
\bigoplus_{n<a^2}
V_{\omega,n,a}
\]

and

\[
\mathbb G_{\omega,a}
=
\bigoplus_{n<a^2}
\mathbb G_{\omega,n,a}.
\]

Then the exact factorization is

\[
\boxed{
H_{\omega,a}
=
V_{\omega,a}^*
\mathbb G_{\omega,a}
V_{\omega,a}.
}
\]

This is a discrete-conductor realization of Suzuki's finite Hankel system.

The arithmetic is entirely in the finite coupling map \(V_{\omega,a}\).

The same Archimedean block \(\mathcal G_\omega\) is reused at every conductor, merely at a rescaled horizon.

---

# 7. Critical point: every primitive mode couples with amplitude \(n^{-1/2}\)

At

\[
\omega=\frac12,
\]

\[
c_{1/2}(n)
=
\frac{\varphi(n)}{\sqrt n},
\]

so

\[
\boxed{
b_{1/2}(n)
=
\frac{\varphi(n)}{n}.
}
\]

Therefore

\[
\frac{b_{1/2}(n)}{\varphi(n)}
=
\boxed{\frac1n}.
\]

Hence

\[
\boxed{
V_{1/2,n,a}f
=
\frac1{\sqrt n}
T_{n,a}f
\otimes
\eta_n.
}
\]

Expanding

\[
\eta_n
=
\sum_{(r,n)=1}\chi_{r,n},
\]

we obtain the key statement:

\[
\boxed{
\textbf{each individual primitive conductor mode at level }n
\textbf{ couples with exactly the same amplitude }n^{-1/2}.
}
\]

There are \(\varphi(n)\) such modes, so the total squared coupling is

\[
\boxed{
\varphi(n)\cdot\frac1n
=
\frac{\varphi(n)}n.
}
\]

Thus Suzuki's critical coefficient is not an opaque scalar weight.

It is:

\[
\boxed{
\text{number of primitive SUCC modes}
\times
\text{half-density coupling squared per mode}.
}
\]

This is the cleanest finite-channel meaning of \(b_{1/2}(n)\).

---

# 8. One finite global LCM clock contains every active conductor block

Let

\[
M=\lfloor a^2\rfloor
\]

and

\[
L_M=\operatorname{lcm}(1,\ldots,M).
\]

Every

\[
n\le M
\]

divides \(L_M\).

Therefore the single finite clock

\[
\boxed{
\mathcal H_M
=
L^2(\mathbb Z/L_M\mathbb Z)
}
\]

contains an orthogonal exact-conductor subspace \(W_n\) for every arithmetic block active at horizon \(a\).

Define the conductor operator

\[
\boxed{
\mathcal C_M
=
\sum_{d\mid L_M}
dP_d.
}
\]

Then

\[
\mathcal C_M|_{W_d}
=
dI.
\]

So the whole finite arithmetic sector can be represented inside one causal LCM clock.

---

## 9. Suzuki's critical scalar kernel is a conductor spectral trace

At \(\omega=\tfrac12\), for \(0<x,y<a\),

\[
h_{1/2}(xy)
=
\frac1{xy}
\sum_n
\frac{\varphi(n)}{\sqrt n}
g_{1/2}\!\left(\frac n{xy}\right).
\]

Since

\[
\operatorname{Tr}P_n=\varphi(n),
\]

functional calculus of \(\mathcal C_M\) gives

\[
\boxed{
h_{1/2}(xy)
=
\frac1{xy}
\operatorname{Tr}_{\mathcal H_M}
\left[
\mathcal C_M^{-1/2}
g_{1/2}\!\left(
\frac{\mathcal C_M}{xy}
\right)
\right].
}
\]

The support of \(g_{1/2}\) automatically kills conductor eigenvalues \(n>xy\), so no extra cutoff is needed.

This is an exact **finite-matrix trace formula** for Suzuki's critical arithmetic kernel.

---

## 10. General \(\omega\): weighted conductor functional calculus

Define the positive conductor weight

\[
\boxed{
q_\omega(n)
=
\frac{c_\omega(n)}{\varphi(n)}.
}
\]

Define

\[
Q_{\omega,M}
=
\sum_{d\mid L_M}
q_\omega(d)P_d.
\]

Then

\[
\boxed{
h_\omega(xy)
=
\frac1{xy}
\operatorname{Tr}_{\mathcal H_M}
\left[
Q_{\omega,M}
g_\omega\!\left(
\frac{\mathcal C_M}{xy}
\right)
\right].
}
\]

At \(\omega=1/2\),

\[
Q_{1/2,M}=\mathcal C_M^{-1/2}.
\]

So the critical point is the unique place in this family where Suzuki's arithmetic weight becomes the simple canonical power

\[
\boxed{\mathcal C^{-1/2}}
\]

of the exact-conductor operator.

---

# 11. Spectral-zeta identity of the conductor operator

Because \(\mathcal C\) has eigenvalue \(n\) with multiplicity \(\varphi(n)\),

\[
\operatorname{Tr}\mathcal C^{-u}
=
\sum_{n\ge1}
\frac{\varphi(n)}{n^u}.
\]

Classically,

\[
\sum_{n\ge1}
\frac{\varphi(n)}{n^u}
=
\frac{\zeta(u-1)}{\zeta(u)}
\qquad(\Re u>2).
\]

Hence, with

\[
u=s+\frac12,
\]

\[
\boxed{
\operatorname{Tr}
\mathcal C^{-(s+1/2)}
=
\frac{
\zeta(s-\frac12)
}{
\zeta(s+\frac12)
}
}
\]

for

\[
\Re s>\frac32.
\]

But this is exactly the **arithmetic/non-Archimedean factor of Suzuki's**
\(\Theta_{1/2}\).

Therefore:

\[
\boxed{
\text{Suzuki's critical arithmetic scattering ratio}
=
\text{spectral zeta function of the SUCC conductor operator}.
}
\]

This is an exact operator-theoretic bridge.

---

# 12. Profinite realization

The inductive limit of the finite LCM clocks is

\[
L^2(\widehat{\mathbb Z}).
\]

Its additive-character basis is indexed by

\[
\mathbb Q/\mathbb Z.
\]

The order of a character is its exact conductor.

Define on this basis

\[
\boxed{
\mathcal C\chi
=
\operatorname{ord}(\chi)\chi.
}
\]

Then:

- eigenspace at \(n\) is \(W_n\);
- multiplicity is \(\varphi(n)\);
- finite causal restrictions are precisely the \(\mathcal C_M\);
- the critical arithmetic factor is the spectral zeta of \(\mathcal C\).

Thus the conductor operator is not manufactured from \(\zeta\).

It is intrinsic to the SUCC/profinite clock.

---

# 13. What this factorization does and does NOT solve

It solves the arithmetic realization problem at finite horizon:

\[
\boxed{
\text{Suzuki finite arithmetic kernel}
=
\text{finite exact-conductor SUCC system}
+
\text{universal Archimedean coupling}.
}
\]

It does **not** automatically prove:

- positivity of the completed canonical Hamiltonian;
- invertibility of \(1\pm H_{\omega,a}\);
- RH;
- that the critical singularity disappears.

In particular, the universal Archimedean block still has the same boundary singularity at \(\omega=1/2\).

So merely introducing \(\varphi(n)\) separate channels does not regularize the singular integral by magic.

The value is that the arithmetic and Archimedean parts are now cleanly separated, and the arithmetic part is a canonical finite matrix system.

---

# 14. New proof-bearing question

At \(\omega=1/2\), Suzuki's operator is exactly

\[
H_{1/2,a}
=
V_a^*
\mathbb G_a
V_a,
\]

where the arithmetic coupling to each primitive conductor mode is \(n^{-1/2}\).

The next question is therefore:

\[
\boxed{
\textbf{Can the singular universal Archimedean block be replaced by an equivalent passive boundary-state realization before the conductor channels are compressed?}
}
\]

If yes, the non-\(L^2\) obstruction may be a representation artifact rather than a genuine failure of finite passivity.

That is the seam to attack next.

---

## 15. House summary

\[
\boxed{
\text{The active arithmetic system at finite }a\text{ is finite.}
}
\]

\[
\boxed{
\text{Its states are exact-conductor SUCC modes }W_n.
}
\]

\[
\boxed{
\text{At }\omega=\frac12,\text{ every primitive mode couples with amplitude }1/\sqrt n.
}
\]

\[
\boxed{
\frac{\zeta(s-1/2)}{\zeta(s+1/2)}
=
\operatorname{Tr}\mathcal C^{-(s+1/2)}.
}
\]

\[
\boxed{
\text{The remaining wall is Archimedean boundary realization, not arithmetic bookkeeping.}
}
\]
