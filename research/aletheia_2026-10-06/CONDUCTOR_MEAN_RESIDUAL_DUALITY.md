# Conductor mean/residual duality: the arithmetic shadow of the subcritical RH wall

**Date:** 2026-10-06  
**Status:** unconditional elementary asymptotic for Suzuki's conductor event weights. It explains why \(\omega=\tfrac12\) is a special endpoint and identifies a complementary residual exponent below it. **RH remains open.**

---

## 1. Parameterization

Let

\[
\delta=\frac12-\omega,
\qquad
0\le\delta<\frac12.
\]

Then

\[
\omega=\frac12-\delta.
\]

The causal conductor-event weight is

\[
b_\omega(n)
=
n^{\omega-1/2}
\prod_{p\mid n}(1-p^{-2\omega}).
\]

Therefore

\[
\boxed{
b_\omega(n)
=
n^{-\delta}
\prod_{p\mid n}
(1-p^{-1+2\delta}).
}
\]

Using the squarefree Möbius expansion,

\[
\boxed{
b_\omega(n)
=
n^{-\delta}
\sum_{d\mid n}
\mu(d)d^{-1+2\delta}.
}
\]

---

## 2. Summatory function

Define

\[
\boxed{
B_\delta(X)
=
\sum_{n\le X}b_\omega(n).
}
\]

Write \(n=dm\). Then

\[
\begin{aligned}
B_\delta(X)
&=
\sum_{d\le X}
\mu(d)d^{-1+\delta}
\sum_{m\le X/d}
m^{-\delta}.
\end{aligned}
\]

For

\[
0\le\delta<1,
\]

\[
\sum_{m\le Y}m^{-\delta}
=
\frac{Y^{1-\delta}}{1-\delta}
+
O(1).
\]

Hence

\[
B_\delta(X)
=
\frac{
X^{1-\delta}
}{
1-\delta
}
\sum_{d\le X}
\frac{\mu(d)}{d^{2-2\delta}}
+
O\left(
\sum_{d\le X}d^{-1+\delta}
\right).
\]

---

## 3. Main term

Because

\[
2-2\delta>1,
\]

the Möbius Dirichlet series converges absolutely:

\[
\sum_{d\ge1}
\frac{\mu(d)}{d^{2-2\delta}}
=
\frac1{\zeta(2-2\delta)}.
\]

The tail satisfies

\[
\sum_{d>X}d^{-2+2\delta}
=
O(X^{-1+2\delta}).
\]

Multiplying by \(X^{1-\delta}\) gives

\[
O(X^\delta).
\]

Also, for \(\delta>0\),

\[
\sum_{d\le X}d^{-1+\delta}
=
O(X^\delta).
\]

Therefore, for

\[
0<\delta<\frac12,
\]

\[
\boxed{
B_\delta(X)
=
\frac{
X^{1-\delta}
}{
(1-\delta)\zeta(2-2\delta)
}
+
O(X^\delta).
}
\]

In \(\omega\)-notation,

\[
\boxed{
\sum_{n\le X}b_\omega(n)
=
\frac{
X^{1/2+\omega}
}{
(\frac12+\omega)\zeta(1+2\omega)
}
+
O(X^{1/2-\omega}).
}
\]

This requires no PNT or RH.

---

# 4. Endpoint improvement at \(\delta=0\)

At

\[
\omega=\frac12,
\qquad
\delta=0,
\]

\[
b_{1/2}(n)
=
\frac{\varphi(n)}n.
\]

The same calculation gives

\[
\boxed{
\sum_{n\le X}
\frac{\varphi(n)}n
=
\frac X{\zeta(2)}
+
O(\log X).
}
\]

So the generic complementary power error

\[
X^\delta
\]

degenerates at the endpoint into a logarithm.

This is a real improvement, not merely the formal substitution \(X^0=1\).

It comes from the borderline harmonic sum

\[
\sum_{d\le X}\frac1d
=
O(\log X).
\]

---

## 5. Mean/residual reflection

Define

\[
\boxed{
\lambda_+
=
1-\delta
=
\frac12+\omega
}
\]

and

\[
\boxed{
\lambda_-
=
\delta
=
\frac12-\omega.
}
\]

Then the elementary conductor asymptotic is

\[
\boxed{
B_\delta(X)
=
C_\delta X^{\lambda_+}
+
O(X^{\lambda_-}),
}
\]

with

\[
C_\delta
=
\frac1{
(1-\delta)\zeta(2-2\delta)
}.
\]

The two exponents satisfy

\[
\boxed{
\lambda_++\lambda_-=1.
}
\]

Thus the main arithmetic flow and the naive residual are reflected around the critical half-density.

---

# 6. Log-time interpretation

Put

\[
X=e^t.
\]

Then

\[
\boxed{
B_\delta(e^t)
=
C_\delta e^{(1-\delta)t}
+
O(e^{\delta t}).
}
\]

So the conductor event stream consists of:

1. a deterministic mean mode
   \[
   e^{(1-\delta)t};
   \]

2. a residual bounded absolutely only by
   \[
   e^{\delta t}.
   \]

But the subcritical Archimedean state-space has exactly one unstable mode

\[
e^{\delta t}.
\]

Therefore:

\[
\boxed{
\text{elementary arithmetic residual rate}
=
\text{Archimedean unstable-mode rate}.
}
\]

This is an exact exponent match.

---

## 7. The mean mode is canceled by the Archimedean zero

The arithmetic Laplace transform is

\[
A_\omega(s)
=
\frac{
\zeta(s+\delta)
}{
\zeta(s+1-\delta)
}.
\]

Its pole is at

\[
s=1-\delta
\]

with residue

\[
\boxed{
R_\delta
=
\frac1{\zeta(2-2\delta)}.
}
\]

The summatory main coefficient is

\[
C_\delta=\frac{R_\delta}{1-\delta},
\]

as expected from Laplace/Tauberian scaling.

The Archimedean factor has a zero at the same spectral point

\[
s=1-\delta.
\]

Thus the deterministic mean flow is exactly the part removed by the first completion seam.

---

# 8. Critical mean cancellation can be written entirely causally

At \(\delta=0\),

\[
c=\frac1{\zeta(2)}.
\]

Write the conductor measure as

\[
\boxed{
d\nu(t)
=
c\,e^t\,dt
+
d\widetilde\nu(t),
}
\]

where the cumulative residual obeys

\[
\boxed{
\widetilde\nu([0,t])
=
O(t).
}
\]

Equivalently, in the original variable,

\[
\sum_{n\le X}\frac{\varphi(n)}n
-
\frac X{\zeta(2)}
=
O(\log X).
\]

Hence the centered causal transform

\[
\int_0^\infty
e^{-st}
\left[
d\nu(t)-c e^t dt
\right]
\]

converges for the **entire right half-plane**

\[
\boxed{\Re s>0.}
\]

So at the critical endpoint the arithmetic conductor response can be centered causally without analytic continuation all the way across the Weyl domain.

---

## 9. The completed response of the mean mode is explicitly bounded

At criticality the Archimedean transfer is

\[
G_\infty(s).
\]

The transform of the mean input \(ce^t\) is

\[
\frac c{s-1}.
\]

Therefore the completed mean response is

\[
\boxed{
c\,\frac{G_\infty(s)}{s-1}
=
c\sqrt\pi
\frac1{s+1}
\frac{\Gamma(s/2)}
{\Gamma((s+1)/2)}.
}
\]

The inverse Laplace transform is exactly

\[
\boxed{
2c\sqrt{1-e^{-2t}}.
}
\]

Thus the Archimedean completion turns the exponentially growing conductor mean

\[
ce^t
\]

into the bounded causal response

\[
\boxed{
2c\sqrt{1-e^{-2t}}
\longrightarrow
2c.
}
\]

This is completion as an explicit dynamical stabilization.

---

# 10. Why the below-critical range is harder

For

\[
\delta>0,
\]

the elementary centered residual is only

\[
O(e^{\delta t}).
\]

Therefore its Laplace transform is guaranteed from elementary absolute estimates only for

\[
\boxed{
\Re s>\delta.
}
\]

But the full Weyl/passivity problem lives on

\[
\Re s>0.
\]

So there is an unresolved strip

\[
\boxed{
0<\Re s\le\delta.
}
\]

Pushing the centered arithmetic response across this strip requires genuine cancellation beyond the absolute divisor estimate.

That cancellation is controlled by the denominator

\[
\zeta(s+1-\delta),
\]

whose zeros encode exactly the global zeta obstruction.

---

## 11. A concrete arithmetic research target

Define the centered conductor discrepancy

\[
\boxed{
E_\delta(X)
=
B_\delta(X)
-
C_\delta X^{1-\delta}.
}
\]

The elementary estimate is

\[
E_\delta(X)=O(X^\delta).
\]

Study it through the SUCC/FUCC conductor/carry representation.

Any improvement of the form

\[
\boxed{
E_\delta(X)
=
O(X^{\delta-\eta})
}
\]

for some uniform \(\eta>0\) pushes the causal transform deeper into the unresolved strip.

Ultimately, control strong enough to reach

\[
\Re s>0
\]

would force the relevant zero-free region.

This is a concrete \(\mathbb N\)-native shadow problem.

---

## 12. What to inspect in finite arithmetic

The discrepancy can be written exactly as

\[
B_\delta(X)
=
\sum_{d\le X}
\mu(d)d^{-1+\delta}
\sum_{m\le X/d}m^{-\delta}.
\]

So the only nontrivial signs are the Möbius/carry innovations.

The smooth \(m\)-sum supplies the deterministic carrier.

Therefore the below-critical RH wall can be localized to:

\[
\boxed{
\text{cancellation of Möbius-weighted conductor innovations against the reflected carrier}.
}
\]

This is an ideal target for the finite divisibility/carry matrices already developed in the repository.

---

## 13. House result

\[
\boxed{
\text{mean conductor flow exponent}=\frac12+\omega.
}
\]

\[
\boxed{
\text{elementary residual exponent}=\frac12-\omega.
}
\]

\[
\boxed{
\text{Archimedean unstable exponent}=\frac12-\omega.
}
\]

At the half-density endpoint the residual becomes only logarithmic, which is why the entire right-half-plane causal centering becomes unconditional.

Below it, the residual/unstable mode is exactly the seam where global arithmetic cancellation must do real work.
