# Proof attempt: Mellin-Dirac completion, source balance, and the quantile-geodesic wall

**Date:** 2026-10-07  
**Branch:** \`proof/mellin-dirac-completion-2026-10-07\`  
**Verdict:** RH remains open. The Mellin-Dirac/Gamma machinery gives an exact source-balance and quantile-geodesic formulation, but the final sign is still RH-equivalent. Two tempting proof shortcuts are refuted.

## 0. External status

As of 2026-10-07 the Riemann Hypothesis remains unsolved. This proof attempt therefore treats every positivity claim as suspect until it is reduced to a theorem independent of RH.

The target remains Suzuki's exact equivalence

\[
\mathrm{RH}
\iff
\Psi(t)\ge0
\quad\forall t.
\]

No zero ordinates are used below.

---

## 1. Exact completed source equation

Write

\[
\Psi(t)=A(t)-P(t),
\]

with

\[
P(t)
=
\sum_{q\le e^t}
\frac{\Lambda(q)}{\sqrt q}
(t-\log q).
\]

Distributionally on \(t>0\),

\[
P''(t)
=
\boxed{
\sum_q
\frac{\Lambda(q)}{\sqrt q}
\delta(t-\log q).
}
\]

The smooth Archimedean part satisfies

\[
A''(t)
=
e^{t/2}+e^{-t/2}
-
\frac{e^{-t/2}}{1-e^{-2t}}.
\]

The Mellin-Dirac/Gamma round identified

\[
\boxed{
\frac{e^{-t/2}}{1-e^{-2t}}
=
\operatorname{Tr}
e^{-tD_{1/2}},
}
\]

where

\[
D_{1/2}
=
\operatorname{diag}
\left(
\frac12,\frac52,\frac92,\ldots
\right).
\]

Therefore

\[
\boxed{
\Psi''
=
\underbrace{
(e^{t/2}+e^{-t/2})dt
}_{\text{pole / vacuum curvature}}
-
\underbrace{
\operatorname{Tr}(e^{-tD_{1/2}})dt
}_{\text{Gamma heat source}}
-
\underbrace{
\sum_q
\frac{\Lambda(q)}{\sqrt q}
\delta_{\log q}
}_{\text{prime-power Dirac source}}.
}
\]

This is exact on \(t>0\), with the origin interpreted through the known distributional boundary expansion.

So the completed RH object is a signed balance among three zero-free sources:

1. continuous pole/vacuum supply;
2. continuous Gamma heat trace;
3. discrete prime-power impulses.

---

## 2. The leading pole source is exactly the continuum PNT comparator

Put

\[
x=e^t.
\]

Then

\[
e^{t/2}dt
=
x^{-1/2}dx.
\]

The prime source is

\[
\sum_n
\frac{\Lambda(n)}{\sqrt n}
\delta_{\log n}.
\]

Equivalently, in \(x\)-coordinates,

\[
\boxed{
dM_{\rm prime}
=
x^{-1/2}d\psi(x),
}
\]

while the leading vacuum source is

\[
\boxed{
dM_{\rm vac}
=
x^{-1/2}dx.
}
\]

Thus

\[
\boxed{
dM_{\rm prime}-dM_{\rm vac}
=
x^{-1/2}d(\psi(x)-x).
}
\]

The leading local curvature balance is therefore exactly the weighted prime-number-theorem error.

This explains the asymptotic matching

\[
A''(\log p)\Delta\log p
\sim
\frac{\log p}{\sqrt p}
\]

for a typical prime gap.

---

## 3. Abel identity for the cumulative critical source

Define

\[
S(X)
=
\sum_{n\le X}
\frac{\Lambda(n)}{\sqrt n}.
\]

Finite Stieltjes integration by parts gives

\[
\boxed{
S(X)
=
\frac{\psi(X)}{\sqrt X}
+
\frac12
\int_1^X
\frac{\psi(u)}{u^{3/2}}\,du.
}
\]

Subtract the continuum model

\[
2\sqrt X.
\]

Writing

\[
E(u)=\psi(u)-u,
\]

one gets, up to the fixed lower-end convention,

\[
\boxed{
S(X)-2\sqrt X
=
\frac{E(X)}{\sqrt X}
+
\frac12
\int_1^X
\frac{E(u)}{u^{3/2}}\,du
+
\text{constant}.
}
\]

So the derivative-level mismatch is already an integrated PNT error.

No local positivity principle can erase this arithmetic fluctuation.

---

## 4. First failed proof: each domino paid by preceding curvature

List prime powers

\[
q_1<q_2<\cdots
\]

and let

\[
a_j=\log q_j,
\qquad
w_j=\frac{\Lambda(q_j)}{\sqrt{q_j}}.
\]

The smooth curvature supplied between two events is

\[
\Delta_j^{\rm curv}
=
A'(a_{j+1})-A'(a_j).
\]

The next event debit is

\[
w_{j+1}.
\]

A tempting induction would require

\[
\Delta_j^{\rm curv}\ge w_{j+1}
\]

for all \(j\).

This is false.

Already for

\[
16\to17
\]

the exact numerical ratio is approximately

\[
\boxed{
\frac{
A'(\log17)-A'(\log16)
}{
\log17/\sqrt{17}
}
\approx0.3582.
}
\]

Many true events violate the local payment inequality.

Therefore the correct mechanism must allow reserve/history to flow across multiple events.

---

## 5. Second failed proof: finite characteristic-function positivity

For a finite prime set and \(\sigma>0\),

\[
Z_{P,\sigma}(t)
=
\prod_{p\le P}
\frac{
1-p^{-\sigma}
}{
1-p^{-\sigma-it}
}
\]

is a characteristic function.

The finite Gamma mode product is also a characteristic function.

Hence every finite prime+Gamma hybrid is positive definite.

At \(\sigma=1/2\), however, the prime exponent contains

\[
\sum_{p\le P}
\sum_{k\ge1}
\frac{p^{-k/2}}k
(1-\cos(kt\log p)).
\]

For fixed nonzero generic \(t\), this grows with the prime cutoff rather than converging to the finite Suzuki exponent.

So finite positivity is an RH-inert local fact.

The infinite critical limit needs a signed renormalization before it can equal the completed object.

---

# 6. Convex reserve coordinates

The previous event-dynamics round established that \(A\) is strictly convex on the entire prime-power event region \(t\ge\log2\).

Set

\[
a_0=\log2.
\]

Define the restricted convex conjugate

\[
A^*(s)
=
\sup_{t\ge a_0}
(st-A(t)).
\]

Let

\[
\tau(s)
=
(A^*)'(s),
\]

equivalently the clipped inverse of \(A'\):

\[
\tau(s)
=
\begin{cases}
a_0,&s\le A'(a_0),\\
(A')^{-1}(s),&s>A'(a_0).
\end{cases}
\]

The exact event sums are

\[
S_j
=
\sum_{i\le j}w_i,
\qquad
H_j
=
\sum_{i\le j}w_i a_i.
\]

The exact reserve is

\[
\boxed{
M_j
=
H_j-A^*(S_j).
}
\]

The already-certified initial interval gives

\[
\boxed{
\mathrm{RH}
\iff
M_j\ge0
\quad\forall j.
}
\]

This remains an equivalence, not a proof.

---

# 7. Prime event quantile

Define the arithmetic mass-quantile function

\[
\boxed{
Q_{\rm ar}(v)
=
a_j
\quad
\text{for }
S_{j-1}<v\le S_j.
}
\]

Then

\[
\boxed{
H_j
=
\int_0^{S_j}
Q_{\rm ar}(v)\,dv.
}
\]

Also,

\[
(A^*)'(v)=\tau(v),
\]

and because

\[
A^*(0)=-A(a_0),
\]

\[
\boxed{
A^*(S_j)
=
-A(a_0)
+
\int_0^{S_j}
\tau(v)\,dv.
}
\]

Therefore:

\[
\boxed{
M_j
=
A(a_0)
+
\int_0^{S_j}
\left[
Q_{\rm ar}(v)-\tau(v)
\right]dv.
}
\]

This is an exact identity.

---

# 8. Geodesic interpretation

The smooth map

\[
\tau(v)
\]

is the location selected by the Archimedean convex gradient for cumulative mass coordinate \(v\).

The arithmetic quantile

\[
Q_{\rm ar}(v)
\]

is where the actual prime-power event stream places that same cumulative mass.

Hence the reserve is the initial positive slack plus the signed area between:

\[
\boxed{
\text{discrete actualization path }Q_{\rm ar}
}
\]

and

\[
\boxed{
\text{continuous curvature-gradient path }\tau.
}
\]

The event increment is

\[
\boxed{
M_{j+1}-M_j
=
\int_{S_j}^{S_{j+1}}
\left[
a_{j+1}-\tau(v)
\right]dv.
}
\]

This is exactly the previously derived Bregman jump formula, now read as monotone-transport/quantile geometry.

The event may undershoot the smooth geodesic, producing negative local reserve change.

RH says the accumulated signed transport never exhausts the initial reserve.

---

# 9. Why this does not yet prove RH

A proof would require a non-circular theorem forcing

\[
\boxed{
A(a_0)
+
\int_0^S
(Q_{\rm ar}-\tau)\,dv
\ge0
}
\]

for every arithmetic prefix mass \(S=S_j\).

Known elementary local properties do not force this:

- event weights are positive;
- event times increase;
- \(A\) is convex;
- the leading average supplies match by PNT;
- local payment can fail strongly.

The missing statement is a global discrepancy bound on the placement of the arithmetic quantile relative to the smooth Archimedean quantile.

That statement is another coordinate system for the RH wall.

---

# 10. Exact source-balance form of the proof obligation

Define the signed completed curvature source

\[
\boxed{
d\mathcal C(t)
=
(e^{t/2}+e^{-t/2})dt
-
\frac{e^{-t/2}}{1-e^{-2t}}dt
-
\sum_q
\frac{\Lambda(q)}{\sqrt q}
\delta_{\log q}(dt).
}
\]

Then

\[
\boxed{
\Psi''=d\mathcal C
}
\]

distributionally away from the origin with the known boundary renormalization.

The proof target is not

\[
d\mathcal C\ge0,
\]

which is false because of negative prime atoms.

The proof target is the weaker twice-integrated positivity

\[
\boxed{
\Psi(t)\ge0.
}
\]

Equivalently, the signed source has nonnegative causal ramp potential after the exact initial boundary condition is included.

This is a second-order transport/stop-loss condition, not pointwise measure dominance.

---

# 11. What the Mellin-Dirac framework genuinely adds

The earlier reserve formulation knew the sign problem.

The present work identifies each source as an independent explicit object:

### Pole/vacuum source

\[
e^{t/2}+e^{-t/2}.
\]

### Gamma source

\[
\operatorname{Tr}e^{-tD_{1/2}}.
\]

### Prime source

\[
\sum_q
\Lambda(q)q^{-1/2}\delta_{\log q}.
\]

And the Gamma source admits:

- a heat-trace realization;
- a regularized determinant;
- a self-adjoint Laguerre moment model;
- a finite spectral truncation preserving trivial zeros.

So the remaining sign problem can now be attacked by finite operator interconnection rather than by treating Gamma as a black box.

---

# 12. Surviving proof architecture: positive dilation before elimination

The signed scalar equation suggests the only remaining nontrivial route:

> Do not subtract the prime, Gamma, and pole channels directly. Embed them into a larger positive/self-adjoint system and obtain the signed completed scalar response only after eliminating internal degrees of freedom.

At finite horizon seek a block operator

\[
\boxed{
\mathcal G_{X,M}
=
\begin{pmatrix}
G_{\rm ar} & C_{X,M}\\
C_{X,M}^* & G_\infty
\end{pmatrix}
\succeq0
}
\]

whose Schur complement or boundary compression equals the finite completed Suzuki/Weil kernel.

Then positivity would be structural upstairs while the required subtraction appears downstairs through elimination.

This is not automatically easier: previous generic Schur/passivity attempts collapsed to RH-equivalent positivity.

The Mellin-Dirac advance is that \(G_\infty\) and its finite modes are now explicit and canonical, sharply restricting what \(C_{X,M}\) is allowed to be.

---

# 13. Specific next construction

Use the finite Archimedean mode space

\[
D_M
=
\operatorname{diag}
\left(
\frac12,\frac52,\ldots,2M-\frac32
\right)
\]

and the finite prime atom list

\[
a_q=\log q,
\qquad
w_q=\frac{\Lambda(q)}{\sqrt q}.
\]

The common Laplace kernel suggests testing cross entries generated by actual mode overlaps, for example resolvent/heat overlaps derived from

\[
e^{-\lambda_m r}
\]

evaluated against the prime atoms at \(r=a_q\).

No coefficient may be fit to zeta zeros.

Pass criterion:

1. the resulting block Gram is manifestly positive;
2. its scalar Schur complement reproduces the finite completed source/kernel exactly or with a rigorously vanishing remainder;
3. the two-parameter limit exists in a positivity-preserving topology;
4. the limit equals Suzuki/Weil.

Failure at step 2 kills this specific dilation.

---

# 14. Verdict

This round did **not** prove RH.

It did produce a sharper statement of what "global curvature as the limit of actualization" means:

\[
\boxed{
\text{RH reserve}
=
\text{initial slack}
+
\text{signed area between arithmetic and Archimedean quantile paths}.
}
\]

And equivalently:

\[
\boxed{
\text{completed curvature source}
=
\text{pole vacuum}
-
\text{Gamma heat trace}
-
\text{prime Dirac comb}.
}
\]

The proof must explain why the twice-integrated signed source never becomes negative.

Finite positivity, local convexity, and one-event curvature payment are insufficient.

The only surviving genuinely new route from the Mellin-Dirac work is to realize the signed cancellation as the boundary shadow of a larger positive/self-adjoint finite system and then prove the completed limit.
