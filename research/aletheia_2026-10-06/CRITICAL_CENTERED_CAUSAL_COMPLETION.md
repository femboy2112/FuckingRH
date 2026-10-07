# Critical conductor centering: two exact completion cancellations in causal state space

**Date:** 2026-10-06  
**Status:** exact unconditional identities at \(\omega=\tfrac12\). **RH remains open.**

This note decomposes the critical arithmetic conductor channel into its deterministic mean plus a centered causal residual, and shows that the completed Suzuki transfer performs two exact stabilizing cancellations:

1. the arithmetic pole at \(s=1\) is killed by the Archimedean zero;
2. the Archimedean marginal pole at \(s=0\) is killed by the centered arithmetic zero.

Both cancellations can be expressed directly from finite/integer data.

---

## 1. Critical conductor event measure

Define

\[
b(n)=\frac{\varphi(n)}n
\]

and the log-time event measure

\[
\boxed{
d\nu(t)
=
\sum_{n\ge1}
b(n)\delta_{\log n}(dt).
}
\]

Its Laplace transform is

\[
\boxed{
A(s)
=
\int_0^\infty e^{-st}\,d\nu(t)
=
\sum_{n\ge1}\frac{\varphi(n)}{n^{s+1}}
=
\frac{\zeta(s)}{\zeta(s+1)}
}
\]

for \(\Re s>1\).

---

## 2. Elementary conductor mean

Classically,

\[
\boxed{
\sum_{n\le X}\frac{\varphi(n)}n
=
cX+O(\log X),
\qquad
c=\frac1{\zeta(2)}.
}
\]

In log time,

\[
\nu([0,t])
=
ce^t+O(t).
\]

Define the centered signed measure

\[
\boxed{
d\mu(t)
=
d\nu(t)-ce^t\,dt.
}
\]

Its cumulative function

\[
M(t):=\mu([0,t])
\]

satisfies

\[
\boxed{
M(t)=O(t).
}
\]

---

## 3. Centered causal transform exists on the full right half-plane

Define

\[
\boxed{
R(s)
=
\int_0^\infty
e^{-st}\,d\mu(t).
}
\]

For \(\Re s>0\), integration by parts gives, with the standard endpoint convention,

\[
\boxed{
R(s)
=
s\int_0^\infty
e^{-st}M(t)\,dt
}
\]

up to the finite atom/basepoint term at \(t=0\), which can equivalently be absorbed into the definition of \(M\).

Since

\[
M(t)=O(t),
\]

the integral converges absolutely for every

\[
\boxed{\Re s>0.}
\]

Hence \(R\) is analytic on the full open right half-plane.

On the overlap \(\Re s>1\),

\[
\boxed{
A(s)
=
\frac{c}{s-1}
+
R(s).
}
\]

By analytic continuation this identity provides the natural centered representation throughout the common meromorphic domain.

No nontrivial zero locations are used.

---

## 4. Critical Archimedean transfer

The exact critical Archimedean transfer is

\[
\boxed{
G(s)
=
\sqrt\pi
\frac{s-1}{s+1}
\frac{\Gamma(s/2)}
{\Gamma((s+1)/2)}
=
-\frac2s
+
2\sum_{m\ge1}
\frac{a_m}{s+2m}.
}
\]

It has:

- a zero at \(s=1\);
- a simple pole at \(s=0\) with residue \(-2\);
- stable poles at the negative even integers.

The critical completed scattering channel is

\[
\boxed{
\Theta_{1/2}(is)
=
A(s)G(s)
=
\frac{\xi(s)}{\xi(s+1)}.
}
\]

---

# 5. First stabilization seam: \(s=1\)

The arithmetic mean transform is

\[
\frac{c}{s-1}.
\]

The Archimedean transfer has

\[
G(s)
=
\frac{\pi}{2}(s-1)+O((s-1)^2)
\]

because

\[
\sqrt\pi\,
\frac{\Gamma(1/2)}{\Gamma(1)}
\frac1{2}
=
\frac{\pi}{2}.
\]

Therefore

\[
\boxed{
\lim_{s\to1}
c\frac{G(s)}{s-1}
=
c\frac{\pi}{2}
=
\frac3\pi.
}
\]

This equals

\[
\frac{\xi(1)}{\xi(2)}.
\]

So the exponentially growing conductor mean is stabilized exactly by the Archimedean zero.

---

## 6. Time-domain form of the stabilized mean

The transform identity

\[
\boxed{
\frac{G(s)}{s-1}
=
\sqrt\pi
\frac1{s+1}
\frac{\Gamma(s/2)}
{\Gamma((s+1)/2)}
}
\]

has inverse Laplace transform

\[
\boxed{
\mathcal L^{-1}
\left[
\frac{G(s)}{s-1}
\right](t)
=
2\sqrt{1-e^{-2t}}.
}
\]

Therefore the deterministic mean input

\[
ce^t
\]

produces the bounded completed response

\[
\boxed{
y_{\rm mean}(t)
=
2c\sqrt{1-e^{-2t}}.
}
\]

As

\[
t\to\infty,
\]

\[
\boxed{
y_{\rm mean}(t)\to2c.
}
\]

This is explicit dynamical stabilization.

---

# 7. The centered arithmetic response has a forced value at \(s=0\)

The meromorphic arithmetic factor satisfies

\[
A(s)
=
\frac{\zeta(s)}{\zeta(s+1)}.
\]

At \(s=0\), the denominator has the pole of \(\zeta(1)\), while \(\zeta(0)\) is finite.

Hence

\[
\boxed{
A(0)=0.
}
\]

But

\[
A(s)
=
\frac{c}{s-1}+R(s).
\]

Therefore

\[
0
=
-c+R(0),
\]

so

\[
\boxed{
R(0)=c.
}
\]

This is an exact sum rule for the centered conductor channel.

It is the spectral counterpart of the finite arithmetic discrepancy.

---

# 8. Second stabilization seam: \(s=0\)

Near zero,

\[
\boxed{
G(s)
=
-\frac2s+O(1).
}
\]

The split arithmetic bracket is

\[
\frac{c}{s-1}+R(s).
\]

At \(s=0\),

\[
\frac{c}{s-1}\to-c,
\qquad
R(s)\to c.
\]

Thus

\[
\boxed{
\frac{c}{s-1}+R(s)
=
O(s).
}
\]

The zero of the completed arithmetic bracket cancels the Archimedean marginal pole.

So:

\[
\boxed{
\text{mean arithmetic channel}
+
\text{centered arithmetic residual}
\to
\text{zero at }s=0
}
\]

which kills

\[
\boxed{
\text{the negative zero-frequency Archimedean mode}.
}
\]

---

## 9. State-space interpretation

Recall the critical Archimedean machine:

\[
\dot x_0=u,
\]

\[
\dot x_m=-2mx_m+u,
\qquad m\ge1,
\]

with output

\[
y=-2x_0+2\sum_{m\ge1}a_mx_m.
\]

The \(-2/s\) term is the zero-frequency integrator \(x_0\).

The identity

\[
A(0)=0
\]

means the **fully assembled arithmetic input has zero DC gain** after the mean/residual channels are combined.

Therefore the dangerous integrator is not driven at DC by the completed arithmetic signal.

This is a literal feedback/control interpretation of the \(s=0\) cancellation.

---

# 10. Two-stage completion diagram

The critical completed system can be organized as

\[
\boxed{
d\nu
=
ce^t dt
+
d\mu
}
\]

feeding the same Archimedean state-space \(G\).

### Stage 1: high-growth mode

\[
ce^t
\quad\overset{G}{\longrightarrow}\quad
2c\sqrt{1-e^{-2t}}.
\]

The \(s=1\) pole is removed.

### Stage 2: marginal mode

The two arithmetic channels satisfy

\[
-c+R(0)=0.
\]

So the \(s=0\) Archimedean pole is removed.

This gives:

\[
\boxed{
\text{completion}
=
\text{cancellation of both the mean growth mode and the marginal boundary mode}.
}
\]

---

## 11. Why finite truncations must couple before taking limits

For a raw finite conductor sum

\[
A_N(s)
=
\sum_{n\le N}\frac{\varphi(n)}{n^{s+1}},
\]

there is no pole at \(s=1\) and no exact zero at \(s=0\).

If it is multiplied by the fully infinite Archimedean transfer \(G(s)\), the completion seams are mismatched.

This explains the previously observed nonuniformity.

A faithful finite passive approximation must pair:

- a finite approximation to the arithmetic mean pole;
- a finite approximation to the centered zero at \(s=0\);
- a matching finite Archimedean modal bank;

**before** taking the thermodynamic limit.

This is now a concrete finite-network synthesis requirement.

---

## 12. A canonical finite centered arithmetic channel

At horizon \(N\), define

\[
\boxed{
E_N(X)
=
\sum_{n\le \min(X,N)}
\frac{\varphi(n)}n
-
c\,\min(X,N).
}
\]

In log time this yields a compactly supported/terminated centered cumulative signal.

One can realize its Stieltjes transform directly and couple it to a finite Archimedean mode bank.

The finite compensator should be chosen to enforce discrete analogues of:

\[
\boxed{
A(1)\text{ pole }\leftrightarrow G(1)=0,
}
\]

and

\[
\boxed{
A(0)=0\leftrightarrow G(0)\text{ pole}.
}
\]

Constructing such matched finite completions is the next system-synthesis problem.

---

## 13. House result

\[
\boxed{
s=1:
\text{ Gamma/infinity kills the conductor mean growth}.
}
\]

\[
\boxed{
s=0:
\text{ centered arithmetic kills the Gamma/infinity marginal mode}.
}
\]

\[
\boxed{
\text{Critical completion is a two-sided feedback cancellation, not a scalar afterthought.}
}
\]

This is the cleanest causal explanation so far of why the completed critical channel is finite where its separate arithmetic and Archimedean pieces are not.
