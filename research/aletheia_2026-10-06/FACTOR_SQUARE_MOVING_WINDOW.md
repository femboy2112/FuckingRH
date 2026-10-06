# Factor-square lift: the moving sqrt(x) sieve window is a fixed chiral cone upstairs

**Date:** 2026-10-06  
**Parent:** finished Round006 head \`d3e29723fcf9df107fc55a75716e5255898c1b53\`  
**Status:** exact arithmetic/operator geometry. RH remains open.

## Thesis

The familiar primality cutoff

\[
p\le \sqrt{x}
\]

should not be regarded as an externally resized search window.

It is the projection to \(\mathbb N\) of a **fixed diagonal symmetry / causal cone** in a higher factor space.

This makes the "SUCC wavefront activates new prime clocks at \(p^2\)" picture exact without dynamically manufacturing hardware.

It also formalizes the viewpoint that \(\mathbb N\) is a projected phenomenological space: multiplication forgets orientation and relative-factor information present in the lifted square.

---

## 1. Lift multiplication to the factor square

Let

\[
\mathcal H_N=\ell^2(\mathbb N_{>0}),
\qquad
\mathcal H_\square=\ell^2(\mathbb N_{>0}\times\mathbb N_{>0})
\cong \mathcal H_N\otimes\mathcal H_N.
\]

On the algebraic finite-support core define the multiplication/incidence operator

\[
\mathcal M_0|a,b\rangle=|ab\rangle.
\]

Its adjoint acts on every basis state by the finite divisor sum

\[
\boxed{
\mathcal M_0^*|x\rangle
=
\sum_{ab=x}|a,b\rangle.
}
\]

Thus \(\mathcal M_0^*\) lifts an observed integer into its full factor-pair fiber.

Because divisor multiplicities are unbounded, \(\mathcal M_0\) is not being asserted bounded on the full Hilbert space. All identities below are exact on the natural finite-support/core domain.

---

## 2. Factor-swap is an exact chirality

Define the swap involution

\[
J|a,b\rangle=|b,a\rangle,
\qquad
J^2=I.
\]

Multiplication is symmetric:

\[
\boxed{
\mathcal M_0J=\mathcal M_0.
}
\]

Hence

\[
\boxed{
\mathcal M_0(I-J)=0.
}
\]

So the antisymmetric/chiral factor-pair sector is invisible after projection to \(\mathbb N\).

This is an exact sense in which the integer \(x=ab\) is a quotient observable: it retains the center/product coordinate and forgets the orientation \(a\leftrightarrow b\).

The symmetric/antisymmetric states

\[
|a,b\rangle_\pm
=
\frac{|a,b\rangle\pm|b,a\rangle}{\sqrt2}
\]

carry information that is partly annihilated by multiplication projection.

---

## 3. The sqrt boundary is the fixed locus of factor chirality

Choose the triangular fundamental domain

\[
\Pi_\triangle|a,b\rangle
=
\mathbf1_{a\le b}|a,b\rangle.
\]

On the fiber \(ab=x\),

\[
a\le b
\iff
a^2\le ab=x
\iff
\boxed{a\le\sqrt{x}.}
\]

Therefore the usual trial-division cutoff is not an arbitrary complexity trick.

It is exactly the image of the fixed diagonal boundary

\[
a=b
\]

under the product projection \(x=ab\).

The diagonal maps to the square numbers

\[
x=a^2.
\]

So perfect squares are literally the projected fixed locus of the factor-swap chirality.

---

## 4. Exact prime-defect square operator

Let

\[
Q=I-|1\rangle\langle1|
\]

remove the unit factor.

Define on basis states

\[
\boxed{
D
=
(Q\otimes Q)\Pi_\triangle\mathcal M_0^*.
}
\]

Then

\[
\boxed{
D|x\rangle
=
\sum_{\substack{ab=x\\2\le a\le b}}
|a,b\rangle.
}
\]

Distinct \(x\) have disjoint factor fibers, so the images \(D|x\rangle\) are mutually orthogonal.

Hence

\[
\boxed{
D^*D|x\rangle
=
c(x)|x\rangle,
}
\]

where

\[
c(x)
=
\#\{a:2\le a\le\sqrt{x},\ a\mid x\}.
\]

For every \(x\ge2\),

\[
\boxed{
x\text{ prime}
\iff
D|x\rangle=0
\iff
\langle x|D^*D|x\rangle=0.
}
\]

Thus primality is the zero set of a manifestly positive square operator in the lifted factor geometry.

This is elementary and does **not** solve RH, but it gives a canonical positive operator attached to the factor square rather than to the already-completed zeta function.

---

## 5. Prime-clock version

Let

\[
P_{\mathbb P}
=
\sum_{p\ \mathrm{prime}}|p\rangle\langle p|
\]

formally denote the prime-coordinate projector on the first factor register.

Define

\[
D_{\mathbb P}
=
(P_{\mathbb P}\otimes I)\Pi_\triangle\mathcal M_0^*.
\]

Then

\[
\boxed{
D_{\mathbb P}|x\rangle
=
\sum_{\substack{p\mid x\\p\le\sqrt{x}}}
|p,x/p\rangle.
}
\]

Therefore

\[
\boxed{
\|D_{\mathbb P}|x\rangle\|^2
=
\#\{p\le\sqrt{x}:p\mid x\}.
}
\]

For \(x\ge2\), this is zero exactly for primes.

So the entire set of relevant prime clocks at carrier position \(x\) is already encoded by one triangular projection of the factor fiber.

---

## 6. The "moving window" is a slice of one fixed cone

Introduce a carrier register with number operator

\[
X|x\rangle=x|x\rangle
\]

and a factor/clock register with

\[
A|a\rangle=a|a\rangle.
\]

On

\[
\mathcal H_{\rm carrier}\otimes\mathcal H_{\rm factor}
\]

define the joint spectral projector

\[
\boxed{
\Pi_{\rm cone}
=
\mathbf1_{\{A^2\le X\}}.
}
\]

This operator is fixed.

On the carrier slice \(|x\rangle\), it reduces to

\[
\boxed{
W_x
=
\sum_{a^2\le x}|a\rangle\langle a|
=
\sum_{a\le\sqrt x}|a\rangle\langle a|.
}
\]

Thus the apparent moving \(\sqrt x\) window in \(\mathbb N\) is simply the family of slices of one static cone upstairs.

For prime clocks,

\[
\boxed{
W_x^{\mathbb P}
=
P_{\mathbb P}W_x
=
\sum_{p^2\le x}|p\rangle\langle p|.
}
\]

This is a monotone projection family.

A prime channel enters the active causal window exactly at \(x=p^2\).

---

## 7. SUCC sees only the cone boundary: exact square-threshold flux

Let \(S_X|x\rangle=|x+1\rangle\) act on the carrier register.

For basis states \(|x,a\rangle\),

\[
\Pi_{\rm cone}|x,a\rangle
=
\mathbf1_{a^2\le x}|x,a\rangle.
\]

Therefore

\[
\boxed{
[\Pi_{\rm cone},S_X]|x,a\rangle
=
\mathbf1_{x+1=a^2}|x+1,a\rangle
}
\]

up to the sign convention chosen for the commutator order.

So the commutator of the moving SUCC carrier with the fixed cone projector is supported **exactly on the square boundary**.

After prime projection,

\[
\boxed{
(P_{\mathbb P}\otimes I)[\Pi_{\rm cone},S_X]
}
\]

is supported exactly at

\[
x+1=p^2.
\]

This is the operator-theoretic version of:

> the SUCC wavefront activates the \(p\)-clock precisely when it crosses \(p^2\).

No hardware needs to be born dynamically. The wiring is static; causal relevance is generated by boundary crossing.

---

## 8. Log coordinates straighten the square-root window

Write

\[
t=\log x,
\qquad
u=\log a.
\]

Then

\[
a^2\le x
\iff
\boxed{2u\le t.}
\]

So the nonlinear window

\[
a\le\sqrt x
\]

becomes a linear half-space in log coordinates.

At carrier log-time \(t\), the active factor spectrum is simply

\[
u\le t/2.
\]

Thus the factor window moves at exactly half the carrier speed in log scale.

This is another exact appearance of the coefficient \(1/2\), arising from factor-swap symmetry alone.

No RH significance is claimed merely from the appearance of \(1/2\).

---

## 9. Factor fibers become straight lines in log-space

For a factor pair

\[
ab=x,
\]

set

\[
u=\log a,\qquad v=\log b,\qquad t=\log x.
\]

Then

\[
\boxed{
u+v=t.
}
\]

The hyperbola \(ab=x\) in ordinary coordinates becomes a straight affine line in log coordinates.

Factor swap is

\[
(u,v)\mapsto(v,u).
\]

Introduce center/relative coordinates

\[
\boxed{
c=\frac{u+v}{2}=\frac t2,
\qquad
r=\frac{u-v}{2}.
}
\]

Then swap acts as the literal chirality

\[
\boxed{
r\mapsto-r,
}
\]

while the projected integer \(x\) depends only on

\[
c=\frac12\log x.
\]

So projection to \(\mathbb N\) forgets the relative/chiral coordinate \(r\).

The square-root boundary is simply

\[
r=0.
\]

This is the clean higher-space interpretation:

\[
\boxed{
\mathbb N\text{ records the center coordinate; the factor square contains the hidden relative/chiral geometry.}
}
\]

---

## 10. Moving-window divisibility/fire operator

On carrier \(\otimes\) prime-clock space define the diagonal firing projector

\[
F|x,p\rangle
=
\mathbf1_{p\mid x}|x,p\rangle.
\]

Gate it by the fixed cone:

\[
\boxed{
F_{\rm active}
=
F\,\Pi_{\rm cone}\,(I\otimes P_{\mathbb P}).
}
\]

At carrier state \(x\), its total active firing count is

\[
\boxed{
C(x)
=
\sum_{\substack{p^2\le x\\p\mid x}}1.
}
\]

Hence

\[
\boxed{
x\ge2\text{ prime}
\iff
C(x)=0.
}
\]

Weighted variants

\[
C_w(x)
=
\sum_{\substack{p^2\le x\\p\mid x}}w_p
\]

can use \(w_p=\log p\), half-density weights, carry-response weights, etc., while the causal \(\sqrt x\) gate remains the same fixed geometric cone.

---

## 11. Relation to the chiral affine \(2x\pm1\) result

A separate exact result gave

\[
A_+=SV_2,\qquad A_-=S^*V_2
\]

with

\[
A_-^*A_+=S
\]

and

\[
(A_+-A_-)^*(A_+-A_-)=2I-S-S^*.
\]

That is a **local affine chirality** around the binary scaffold.

The present factor-square geometry gives a second exact chirality:

\[
(a,b)\leftrightarrow(b,a).
\]

Its fixed locus is the square-root boundary.

Both structures say that:

1. orientation exists upstairs;
2. a positive square is natural after taking an oriented first-order object;
3. projection to ordinary \(\mathbb N\) forgets part of the orientation data.

Whether the two chiralities can be assembled into one first-order operator is an open target.

---

## 12. Why this is orthogonal to Round006's closed source-passivity class

Round006 established a sharp obstruction for a class of attempts that try to realize the fixed endpoint function \(\xi'/\xi\) itself as a positive-real/passive source response.

The present operator does **not** attempt to make \(\xi'/\xi\) positive-real by a different parent realization.

Instead it supplies a different positive object

\[
D^*D\succeq0
\]

in a higher factor geometry before the explicit-formula projection.

So if this route contributes to RH, it must do so through a new trace/pushforward/limit theorem connecting this lifted positive geometry to the completed Weil/Suzuki form.

That is genuinely orthogonal to the parent-independence obstruction of Round006.

---

## 13. Immediate next targets

1. **Weighted factor defect.** Determine the canonical weights that turn factor incidence into von-Mangoldt / prime-power data rather than generic compositeness.
2. **Boundary current.** Study the square-threshold operator
   \[
   [\Pi_{\rm cone},S_X]
   \]
   together with carry curvature and half-density.
3. **Log-space Dirac.** Build a first-order operator in the relative coordinate \(r=(\log a-\log b)/2\) whose square yields a natural positive factor energy.
4. **Pushforward.** Compute exactly what \(\mathcal M_0\), partial trace, or conditional expectation does to the lifted square energy.
5. **Prime-power specialization.** Characterize fibers \(x=p^k\) internally in the factor square and recover \(\Lambda(x)\) without inserting primes as a black-box projector if possible.
6. **Moving finite window.** Use
   \[
   \Pi_{\rm cone}=\mathbf1_{2\log A\le\log X}
   \]
   as the finite causal truncation rather than independent prime cutoffs.
7. **Hostile controls.** Replace multiplication by a fake semigroup law or destroy the swap symmetry and determine which identities survive.
8. **Trace-formula target.** Seek a completed trace/energy identity from the lifted geometry rather than another positive-real realization of \(\xi'/\xi\).

---

## 14. Core slogan

\[
\boxed{
\text{The }\sqrt{x}\text{ sieve window is not moving upstairs. SUCC is sliding through a fixed multiplicative cone.}
}
\]

Equivalently:

\[
\boxed{
\text{The diagonal }a=b\text{ is static; }\sqrt{x}\text{ is merely its shadow in }\mathbb N.
}
\]

This is the precise geometry suggested by treating \(\mathbb N\) as the projected space where arithmetic "rubber meets the road."
