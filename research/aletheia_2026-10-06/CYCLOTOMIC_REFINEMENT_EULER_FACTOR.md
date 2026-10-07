# Cyclotomic clock refinements telescope to the Euler factors

**Date:** 2026-10-06  
**Status:** exact determinant identity connecting the LCM/SUCC refinement matrices directly to the Euler product in its convergence region. **RH remains open.**

This is the strongest consequence so far of the Ramanujan/cyclotomic innovation blocks.

---

## 1. Local clock innovation determinant

At the refinement event

\[
p^{k-1}\to p^k,
\]

let

\[
W_{p,k}
=
L^2(\mathbb Z/p^k\mathbb Z)
\ominus
L^2(\mathbb Z/p^{k-1}\mathbb Z)
\]

under normalized pullback.

Let

\[
U_{p,k}^{\rm new}
\]

be cyclic SUCC restricted to \(W_{p,k}\).

Its eigenvalues are the primitive \(p^k\)-th roots of unity, hence

\[
\boxed{
\det(zI-U_{p,k}^{\rm new})
=
\Phi_{p^k}(z).
}
\]

Equivalently,

\[
\boxed{
\det(I-xU_{p,k}^{\rm new})
=
\Phi_{p^k}(x)
}
\]

for prime powers, because the reciprocal root set is the same.

---

## 2. Successive prime-clock refinements telescope

For a prime power,

\[
\Phi_{p^k}(x)
=
\frac{1-x^{p^k}}{1-x^{p^{k-1}}}.
\]

Therefore

\[
\boxed{
\prod_{k=1}^{K}
\det(I-xU_{p,k}^{\rm new})
=
\prod_{k=1}^{K}\Phi_{p^k}(x)
=
\frac{1-x^{p^K}}{1-x}.
}
\]

If \(|x|<1\),

\[
x^{p^K}\to0,
\]

so

\[
\boxed{
\prod_{k\ge1}
\det(I-xU_{p,k}^{\rm new})
=
\frac1{1-x}.
}
\]

Now set

\[
x=p^{-s}.
\]

For \(\Re s>0\),

\[
\boxed{
L_p(s)
=
\frac1{1-p^{-s}}
=
\prod_{k\ge1}
\det\!\left(
I-p^{-s}U_{p,k}^{\rm new}
\right).
}
\]

Thus the standard local Euler factor is exactly the accumulated determinant of the successive exact-conductor SUCC innovations of the \(p\)-clock.

No zeta zero and no Euler geometric series is inserted into the clock matrix.

---

## 3. Finite causal horizon

At global SUCC horizon \(N\), the deepest available \(p\)-clock level is

\[
K_p(N)=\lfloor\log_pN\rfloor.
\]

Define the finite causal determinant product

\[
\boxed{
D_N(s)
=
\prod_{p\le N}
\prod_{k=1}^{K_p(N)}
\det\!\left(
I-p^{-s}U_{p,k}^{\rm new}
\right).
}
\]

By telescoping prime by prime,

\[
\boxed{
D_N(s)
=
\prod_{p\le N}
\frac{
1-p^{-s p^{K_p(N)}}
}{
1-p^{-s}
}.
}
\]

Every factor is generated only when the global SUCC wavefront reaches the corresponding prime power.

There is no future information.

For \(\Re s>1\),

\[
\boxed{
D_N(s)\longrightarrow\zeta(s).
}
\]

The numerator correction tends to \(1\) extremely rapidly at every fixed prime, while the denominator tends to the ordinary Euler product.

So zeta in its Euler-product half-plane is the limit of a **causally generated sequence of finite clock-twist determinants**.

---

## 4. Chronological online recursion

Let \(q=N+1\).

If \(q\) is not a prime power,

\[
\boxed{
D_{N+1}(s)=D_N(s).
}
\]

If

\[
q=p^k,
\]

then one exact-conductor clock block is activated and

\[
\boxed{
D_{N+1}(s)
=
D_N(s)
\,
\Phi_{p^k}(p^{-s}).
}
\]

Thus the determinant obeys the causal update law

\[
\boxed{
\text{SUCC pulse}
\to
\begin{cases}
\text{identity},&\text{no new conductor},\\
\text{cyclotomic twist determinant},&N+1=p^k.
\end{cases}
}
\]

This is an exact matrix-domino realization of the Euler product.

---

## 5. Scale-by-scale positive decomposition of the local source response

Take logarithms:

\[
\log L_p(s)
=
\sum_{k\ge1}
\log\Phi_{p^k}(p^{-s}).
\]

Differentiate:

\[
\boxed{
-\partial_s\log L_p(s)
=
\sum_{k\ge1}
\mathcal I_{p,k}(s),
}
\]

where

\[
\mathcal I_{p,k}(s)
:=
-\partial_s
\log\Phi_{p^k}(p^{-s}).
\]

For real \(s>0\), each \(\mathcal I_{p,k}(s)>0\), because \(\Phi_{p^k}(x)\) is increasing for \(x\in(0,1)\) while \(x=p^{-s}\) decreases with \(s\).

Explicitly, with \(x=p^{-s}\),

\[
\boxed{
\mathcal I_{p,k}(s)
=
(\log p)
\left[
\frac{
p^{k-1}x^{p^{k-1}}
}{
1-x^{p^{k-1}}
}
-
\frac{
p^kx^{p^k}
}{
1-x^{p^k}
}
\right].
}
\]

The sum telescopes:

\[
\boxed{
\sum_{k\ge1}\mathcal I_{p,k}(s)
=
\frac{\log p}{p^s-1}
=
-\partial_s\log L_p(s).
}
\]

At \(s=1/2\),

\[
\boxed{
\sum_{k\ge1}\mathcal I_{p,k}(1/2)
=
\frac{\log p}{\sqrt p-1}
=
M_p.
}
\]

So the local Brownian repair coefficient \(M_p\), previously found as a geometric prime-depth sum, has a second exact decomposition:

\[
\boxed{
M_p
=
\text{sum of positive exact-conductor clock innovations}.
}
\]

This is a nontrivial change of basis:

- Euler depth basis: \(p^{-ks}\);
- conductor-refinement basis: positive telescoping increments \(\mathcal I_{p,k}(s)\).

Both give the same local source response.

---

## 6. Why this does not yet solve the global divergence

For each prime, the refinement determinant construction is exceptionally well behaved and reconstructs \(L_p(s)\).

But globally,

\[
\prod_pL_p(s)
\]

still converges ordinarily only for

\[
\Re s>1.
\]

Likewise

\[
\sum_pM_p
\]

still diverges at \(s=1/2\).

Therefore the cyclotomic refinement basis solves/repackages the **local** prime tower exactly but does not by itself perform the required prime/Archimedean analytic continuation.

The Round004–006 wall remains.

What is new is that the finite causal matrix skeleton now generates the Euler product itself rather than merely being decorated by it.

---

## 7. Matrix meaning of the Euler factor

The identity

\[
L_p(s)
=
\prod_{k\ge1}
\det(I-p^{-s}U_{p,k}^{\rm new})
\]

can be read as:

> Every time the \(p\)-clock gains one causal digit, it contributes a primitive cyclotomic twist block. The complete local Euler factor is the determinant accumulated by all such twists.

This explains why prime powers are the event schedule even though the Euler factor is usually written using one prime variable.

Prime powers are when the **resolution of the prime clock changes**.

---

## 8. Global matrix architecture suggested by the identity

At finite horizon, one may keep:

1. the global LCM clock \(C_{L_N}\);
2. its exact-conductor innovation decomposition;
3. the event twist blocks \(U_{p,k}^{\rm new}\);
4. the physical one-leg normalization
   \[
   \sqrt{\log p}\,p^{-k/4};
   \]
5. the continuous inverse-SUCC/Gamma channel.

The prime-sector determinant is then generated causally as

\[
D_N(s).
\]

The next theorem target is not to rediscover the Euler factor.

It is:

\[
\boxed{
\text{couple the causally generated determinant }D_N(s)
\text{ to the Gamma channel before taking }N\to\infty,
}
\]

in a way that produces a self-adjoint/positive completed transfer system rather than merely analytically continuing the scalar product afterward.

That is exactly where previous rounds hit the Weil wall.

---

## 9. Important determinant caveat

Although each finite innovation block is unitary and finite dimensional, the formal infinite direct sum

\[
\bigoplus_{p,k}p^{-s}U_{p,k}^{\rm new}
\]

is not generally trace class merely because the scalar determinant product above converges.

The determinant identity is a **chronologically regularized/telescoping product of finite determinants**, not automatically the Fredholm determinant of one naive block-diagonal trace-class operator.

Any global operator construction must preserve this distinction.

---

## 10. House slogan

\[
\boxed{
\text{Prime powers are clock-refinement events.}
}
\]

\[
\boxed{
\text{Each event contributes a cyclotomic twist determinant.}
}
\]

\[
\boxed{
\text{All refinements of one prime telescope into its Euler factor.}
}
\]

\[
\boxed{
\text{The Euler product is the infinite causal determinant of the prime clocks.}
}
\]

In the convergent half-plane, that last sentence is an exact finite-horizon limit statement.
