# Bilateral affine completion: inverse SUCC/FUCC, centered edge chirality, and degree–adjacency cancellation

**Date:** 2026-10-06  
**Parent:** Astra Round007 head \`8da6cf92d276961356497486048163f0aff08233\`  
**Status:** exact algebraic observations + a new post-Round007 research direction. RH remains open.

## 1. The Round007 prime difference square already contains the bulk term

Round007 uses, for
\[
a_n=\log n,\qquad w_n=\frac{\Lambda(n)}{\sqrt n},
\]
the translation-difference channel
\[
D_nf=\sqrt{w_n}\,(\tau_{a_n}-I)f,
\]
where \(\tau_a f(x)=f(x-a)\) is unitary on \(L^2(\mathbb R)\).

Therefore
\[
D_n^*D_n
=
w_n(2I-\tau_{a_n}-\tau_{-a_n}).
\]

Summing over \(n\le N\),
\[
\boxed{
D_{\rm pr}^*D_{\rm pr}
=
2S_N I-A_N,
}
\]
where
\[
S_N=\sum_{n\le N}w_n,
\qquad
\boxed{
A_N
=
\sum_{n\le N}w_n(\tau_{a_n}+\tau_{-a_n}).
}
\]

Hence
\[
\boxed{
D_{\rm pr}^*D_{\rm pr}-2S_N I=-A_N.
}
\]

So the Round007 \(-2S_N\|f\|^2\) residual is not unrelated to the prime square: it is exactly the weighted **degree subtraction** converting the translation-graph Laplacian into minus its symmetric adjacency.

The prime piece of the Weil form can therefore be read as
\[
\boxed{
-\langle f,A_Nf\rangle
=
\|D_{\rm pr}f\|^2-2S_N\|f\|^2.
}
\]

This does not make it positive; it identifies the precise operator-theoretic role of the bulk debit.

Graph language:
- \(D_{\rm pr}\) is a weighted incidence operator;
- \(D_{\rm pr}^*D_{\rm pr}\) is weighted degree minus adjacency;
- the Weil prime correlation wants minus adjacency.

The failed positive-square construction paid the degree term automatically because every positive edge square must do so.

---

## 2. Center every event using inverse translation

On \(L^2(\mathbb R)\), translations are bilateral:
\[
\tau_a^{-1}=\tau_{-a}.
\]

Define centered chiral branches
\[
U_{a,+}=\tau_{a/2},
\qquad
U_{a,-}=\tau_{-a/2}.
\]

Then
\[
\tau_a-I
=
\tau_{a/2}(\tau_{a/2}-\tau_{-a/2}),
\]
so the Round007 edge operator is unitarily equivalent to the centered chiral difference
\[
C_a:=\tau_{a/2}-\tau_{-a/2}.
\]

Exactly,
\[
\boxed{
C_a^*C_a
=
2I-\tau_a-\tau_{-a}.
}
\]

Define also the centered symmetric channel
\[
E_a:=\tau_{a/2}+\tau_{-a/2}.
\]

Then
\[
E_a^*E_a
=
2I+\tau_a+\tau_{-a},
\]
and therefore
\[
\boxed{
-(\tau_a+\tau_{-a})
=
\frac12(C_a^*C_a-E_a^*E_a).
}
\]

Thus the desired prime correlation is naturally a **graded/chiral difference of two positive sector energies**.

Weighted over the prime-power events,
\[
\boxed{
-A_N
=
\frac12\sum_{n\le N}w_n
\left(
C_{a_n}^*C_{a_n}
-
E_{a_n}^*E_{a_n}
\right).
}
\]

This is equivalent to the \(2S_N\) cancellation above, but exposes the missing structure differently: the bulk debit is the price of discarding the opposite chiral/symmetric sector.

A single positive Hilbert norm cannot remove that price in the independent two-endpoint class (Round007 C120). A graded/supertrace/Krein formulation can encode it exactly, but still requires a separate theorem explaining why the completed physical subspace is positive.

---

## 3. The Gamma difference channel is centered the same way

Round007's Gamma channel is
\[
D_\Gamma f(u,x)
=
\sqrt{k(u)}\,(\tau_u-I)f(x),
\qquad
k(u)=\frac{e^{-u/2}}{1-e^{-2u}}.
\]

For every fixed \(u>0\),
\[
\tau_u-I
=
\tau_{u/2}(\tau_{u/2}-\tau_{-u/2}).
\]

So prime and Gamma channels share the same centered first-order geometry:
\[
\boxed{
\text{forward event edge}
=
\text{midpoint translation}
\times
\text{left/right chiral difference}.
}
\]

However, the separate Gamma symmetric-sector energy is not naively integrable because
\[
k(u)\sim\frac1{2u}\qquad(u\to0).
\]
Thus one cannot split the Gamma channel into two separately finite positive energies without a justified renormalization. The finite constant
\[
c_0=\psi(1/4)-\log\pi
\]
is a natural object to compare against such a renormalized even-sector self-energy, but no identity of that kind is claimed here.

This is an immediate research target.

---

## 4. Inverse SUCC requires group completion

On \(\ell^2(\mathbb N_0)\), the ordinary successor
\[
S|n\rangle=|n+1\rangle
\]
is unilateral. Its adjoint is only a partial inverse:
\[
S^*|0\rangle=0.
\]

Therefore the statement
\[
S^{-1}(0)=-1
\]
is **not** available inside the \(\mathbb N_0\) Hilbert space.

To make it exact, extend the carrier to
\[
\boxed{\mathbb Z}
\]
and define the bilateral shift
\[
T_1|x\rangle=|x+1\rangle,
\qquad
T_1^{-1}=T_{-1}.
\]

Then
\[
T_{-1}|0\rangle=|-1\rangle,
\qquad
T_{-1}^k|0\rangle=|-k\rangle.
\]

This removes the additive boundary at zero and creates an exact left/right carrier chirality.

---

## 5. Inverse FUCC group-completes the valuation lattice

On positive integers,
\[
V_p|n\rangle=|pn\rangle
\]
is an isometry but not surjective. Its adjoint is a partial inverse:
\[
V_p^*|n\rangle
=
\begin{cases}
|n/p\rangle,&p\mid n,\\
0,&p\nmid n.
\end{cases}
\]

In valuation coordinates this is the backward shift with a boundary at
\[
v_p=0.
\]

If FUCC is required to be genuinely invertible, the natural completion is
\[
\boxed{
\mathbb Z^{(\mathbb P)}
}
\]
rather than
\[
\mathbb N_0^{(\mathbb P)}.
\]

Equivalently, the multiplicative state space becomes
\[
\boxed{
\mathbb Q_{>0}^{\times}.
}
\]

A rational
\[
q=\prod_p p^{k_p}
\]
has finite-support exponents
\[
k_p\in\mathbb Z.
\]

Then
\[
V_p:k_p\mapsto k_p+1,
\qquad
V_p^{-1}:k_p\mapsto k_p-1
\]
are true unitaries on the bilateral valuation lattice.

Every prime jet becomes bi-infinite:
\[
\ldots,p^{-2},p^{-1},1,p,p^2,\ldots.
\]

The reflection
\[
q\mapsto q^{-1}
\]
is simply
\[
(k_p)_p\mapsto(-k_p)_p.
\]

This is an exact multiplicative chirality absent in the positive-semigroup shadow.

---

## 6. Requiring both inverse SUCC and inverse FUCC forces rational affine translations

The additive and multiplicative group completions do not remain independent.

Let
\[
T_b(x)=x+b,
\qquad
D_a(x)=ax.
\]

For
\[
a\in\mathbb Q_{>0}^{\times},
\qquad
b\in\mathbb Q,
\]
they satisfy
\[
\boxed{
D_aT_bD_a^{-1}=T_{ab}.
}
\]

In particular,
\[
D_p^{-1}T_1D_p=T_{1/p}.
\]

Thus once inverse FUCC is admitted, conjugating ordinary SUCC by it automatically produces **fractional SUCC**.

Closure therefore forces the carrier from
\[
\mathbb Z
\]
to
\[
\boxed{\mathbb Q}.
\]

The natural reversible completion is the rational affine group
\[
\boxed{
\operatorname{Aff}(\mathbb Q)
=
\mathbb Q\rtimes\mathbb Q_{>0}^{\times},
}
\]
acting by
\[
x\mapsto ax+b.
\]

The original arithmetic semigroup generated by positive SUCC and positive FUCC sits inside this group as a one-sided cone.

This is the group completion of the familiar affine relation
\[
V_pS=S^pV_p.
\]

---

## 7. The full affine group escapes the forward-transfer no-go hypothesis

Round007 proved that any trace-class transfer operator which only moves strictly forward in a proper carrier grading has
\[
\det(I-zT)=1.
\]

A genuinely reversible affine group representation is outside that hypothesis:
- \(T_{-1}\) decreases carrier position;
- \(V_p^{-1}\) decreases valuation depth;
- conjugation generates fractional translations;
- affine relation words create closed group loops.

For example,
\[
\boxed{
D_pT_1D_p^{-1}T_{-p}=I.
}
\]

This is not merely a forward edge followed by its immediate reverse; it is the closed affine braid relation.

The simplest symmetric forward/backward jet operator was already tested in Round007 and produced a continuant rather than an Euler factor. Therefore "add reverse edges" alone is not a solution.

The surviving question is narrower:

> Does the **full affine relation-loop geometry**, with its natural cocycles/log-height weights, generate a nontrivial completed trace or cross pairing that the simple bidirectional jet misses?

No such trace theorem is supplied here.

---

## 8. The group completion exposes the adelic/product-formula balance

For
\[
q=\prod_p p^{k_p}\in\mathbb Q_{>0}^{\times},
\]
the ordinary real absolute value obeys
\[
\log q
=
\sum_p k_p\log p.
\]

Equivalently, with the normalized \(p\)-adic absolute values
\[
|q|_p=p^{-k_p},
\]
the product formula is
\[
\boxed{
\log|q|_\infty+\sum_p\log|q|_p=0.
}
\]

Thus once inverse FUCC permits signed valuations, the finite-prime coordinates and the Archimedean coordinate satisfy an exact linear conservation law.

This is classical adelic arithmetic, not a novelty claim.

It is nevertheless structurally relevant to the present program because the completed Weil form is precisely where finite and infinite places must combine before positivity is assessed.

The positive-semigroup picture hides the signed local-global balance; the rational group completion makes it explicit.

---

## 9. What the two observations jointly suggest

The Round007 edge square currently has the form

\[
\text{Laplacian}
=
\text{degree}
-
\text{adjacency}.
\]

The Weil prime term wants
\[
-\text{adjacency}.
\]

The residual
\[
-2S_N I
\]
is exactly the removal of the degree sector.

Inverse translations recenter every edge into two chiral halves and show
\[
-\text{adjacency}
=
\frac12
\left(
\text{odd-sector energy}
-
\text{even-sector energy}
\right).
\]

Meanwhile inverse FUCC/SUCC naturally moves the arithmetic from a one-sided semigroup to a reversible affine group where:
- both chiral sectors exist globally;
- relation loops exist;
- factor/valuation labels can mix under conjugation;
- finite and infinite valuations satisfy the product formula.

This geometry lies outside several Round007 no-go hypotheses:
- it is not strictly forward;
- it is not factor-label-preserving local propagation;
- it naturally refines below the integer carrier via rational translations;
- it is not an orthogonal direct sum of independent event channels.

That makes it a legitimate next constructor class to test.

---

## 10. Concrete next probe

Do not immediately attempt RH.

First construct the exact reversible representation on a common dense/core state space and calculate:

1. the affine group generators
   \[
   T_{\pm1},\quad D_p^{\pm1};
   \]
2. the rational translations forced by conjugation;
3. the natural grading/chirality
   \[
   q\leftrightarrow q^{-1},
   \qquad
   x\leftrightarrow -x;
   \]
4. affine relation loops and their weighted holonomy/cocycles;
5. the centered prime event channels
   \[
   \tau_{\pm\log n/2};
   \]
6. whether the prime adjacency operator \(A_N\) arises as an off-diagonal block or supertrace of one self-adjoint first-order affine operator;
7. whether the Gamma channel admits the same centered bilateral realization after a mathematically justified renormalization;
8. the exact polarized discrepancy against the completed Weil form.

A verdict-changing result would be either:
- an exact common first-order pairing whose compression is Weil; or
- a new obstruction proving the reversible affine-group class still cannot supply the missing bulk pairing.

---

## Core formulas

\[
\boxed{
D_{\rm pr}^*D_{\rm pr}
=
2S_NI-A_N
}
\]

\[
\boxed{
D_{\rm pr}^*D_{\rm pr}-2S_NI
=
-A_N
}
\]

\[
\boxed{
C_a^*C_a
=
2I-\tau_a-\tau_{-a}
}
\]

\[
\boxed{
-(\tau_a+\tau_{-a})
=
\frac12(C_a^*C_a-E_a^*E_a)
}
\]

\[
\boxed{
D_p^{-1}T_1D_p=T_{1/p}
}
\]

\[
\boxed{
\operatorname{Aff}(\mathbb Q)
=
\mathbb Q\rtimes\mathbb Q_{>0}^{\times}
}
\]

The key conceptual change is:

> **The positive-integer SUCC/FUCC machine is a semigroup shadow. Its reversible completion is a bilateral rational affine geometry, and the Round007 bulk term is exactly the degree sector discarded when one asks for adjacency rather than Laplacian.**
