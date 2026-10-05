# Diagonal rational quotient without erasing prime towers

**Date:** 2026-10-05  
**Status:** structural synthesis / proposed RH architecture. RH is not proved here.

## 1. The apparent paradox

We want to "factor out" a global rational \(x\in\mathbb Q^\times\) as redundant global scale while **not** erasing the local prime towers whose valuations factor \(x\):

\[
x=\pm\prod_p p^{v_p(x)}.
\]

A naive coarse quotient can identify the diagonal principal element with the identity and thereby forget the factorization of that particular representative.

The correct distinction is:

- quotient the **diagonal global action**;
- retain the **local relative data and the action arrows**.

## 2. Ideles: quotient one diagonal subgroup, not every local factor

The idele group is

\[
\mathbb A_\mathbb Q^\times
=
\mathbb R^\times
\times
\prod_p' \mathbb Q_p^\times.
\]

The diagonal embedding sends

\[
x\in\mathbb Q^\times
\longmapsto
(x,x,x,\ldots).
\]

The idele class group is

\[
C_\mathbb Q
=
\mathbb Q^\times\backslash\mathbb A_\mathbb Q^\times.
\]

Thus

\[
(a_v)_v
\sim
(xa_v)_v.
\]

Only **simultaneous global multiplication by the same rational** is gauged away. One does not quotient each \(\mathbb Q_p^\times\) independently.

A local prime excitation

\[
e_{p,k}
=
(1_\infty,1_2,\ldots,p^k\text{ at }p,\ldots)
\]

is not diagonal. Its idele norm is

\[
|e_{p,k}|_\mathbb A
=
|p^k|_p
=
p^{-k},
\]

whereas every principal idele has global norm \(1\) by the product formula. Hence \(e_{p,k}\) represents nontrivial relative local data in the idele-class quotient.

Multiplying \(e_{p,k}\) by the principal idele \(p^{-k}\) does not erase the information; it moves it into a different gauge representative, redistributing the defect among the real and other local components.

## 3. Why the coarse quotient is still insufficient for the factorization history

For a diagonal rational \(x\) itself, its class in \(C_\mathbb Q\) is the identity. The coarse orbit space therefore does **not** remember which prime factorization produced that particular gauge transformation.

To retain the construction history, use the transformation groupoid

\[
\mathbb Q^\times\ltimes\mathbb A_\mathbb Q
\]

or the quotient stack/noncommutative quotient

\[
[\mathbb A_\mathbb Q/\mathbb Q^\times].
\]

Objects are adelic configurations \(a\). A morphism

\[
a\longrightarrow xa
\]

is labeled by the rational \(x\).

Even after \(a\) and \(xa\) represent the same coarse orbit, the arrow still carries

\[
x=\pm\prod_p p^{v_p(x)}.
\]

Thus:

\[
\boxed{
\text{global rational value is gauge}
\quad\text{while}\quad
\text{its prime-tower decomposition remains arrow/cocycle data}.
}
\]

This is the precise categorical form of "factor out \(x\) without factoring out the primes that spectrally construct \(x\)."

## 4. Prime spectral orbits actually survive the quotient

This is not merely an invented analogy.

Connes and Consani use the adele class space

\[
X_\mathbb Q^{ab}
=
\mathbb Q^\times\backslash\mathbb A_\mathbb Q
\]

as a geometric/noncommutative arithmetic object. Their scaling-site construction has periodic prime orbits \(C_p\) of length

\[
\log p.
\]

Thus the quotient by diagonal \(\mathbb Q^\times\) does not erase the prime spectral periods; prime information reappears as orbit geometry of the quotient.

This is strong evidence that the RH program should distinguish:

- principal/global rational gauge;
- local prime orbit/tower data;
- Archimedean scaling flow.

## 5. Relation to the unit-basepoint jet picture

At the common trivial-valuation/unit basepoint, each place character has

\[
\chi_{v,0}=1.
\]

The global diagonal rational is constrained by

\[
\prod_v |x|_v=1.
\]

Therefore its first jet satisfies

\[
\sum_v\log|x|_v=0.
\]

This is exactly the kind of direction one wants to quotient/gauge away **before** forming a positive higher-order object.

The local components \(\log|x|_p=-v_p(x)\log p\), however, remain available as relative/tangent directions in the groupoid.

At the critical half-density,

\[
\chi^{(1/2)}_{v,z}(x)=|x|_v^{1/2+z},
\]

the finite prime-power tangent weights naturally contain \(p^{-k/2}\log p\), matching the Suzuki event scale after prime-power bookkeeping.

## 6. Candidate proof architecture

### Groupoid-Gauge Gram Theorem — UNVERIFIED

Construct a positive representation/Hilbert module of the transformation groupoid

\[
\mathbb Q^\times\ltimes\mathbb A_\mathbb Q
\]

(or a suitable semilocal/critical-line quotient) satisfying:

1. the diagonal principal-rational direction is represented as gauge/null data;
2. local \(p\)-adic prime-tower arrows survive and retain their \(\log p\) periods;
3. the Archimedean scaling direction is included in the same representation;
4. the global product-formula first-jet cancellation occurs **inside** the construction, before positivity is tested;
5. the resulting positive Gram kernel on the scaling variable is exactly
   \[
   K_\Psi(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u);
   \]
6. finite mutations of a prime tower break the groupoid/arithmetic compatibility, satisfying the Round-001 mutation-sensitivity requirement.

If such a theorem is proved independently of zero locations, Suzuki's criterion gives RH.

## 7. Why this may solve the divergence problem

Round 002 found positive repaired local prime-tower blocks

\[
D_p=M_p|t|-h_p
\]

but

\[
\sum_p M_p=\infty.
\]

Summing positive local blocks and subtracting the divergent linear term afterward destroys positivity.

The groupoid/gauge viewpoint suggests the opposite order:

\[
\boxed{
\text{quotient/null the global principal first-jet direction first}
\;\longrightarrow\;
\text{form the coupled positive Gram object second}.
}
\]

The divergent linear correction may be an artifact of choosing separate local gauges before imposing the global principal relation.

This is currently the most concrete interpretation of the missing global renormalization theorem.
