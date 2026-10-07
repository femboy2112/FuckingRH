# Prime-power events as rank-one boundary twists of the entire previous clock

**Date:** 2026-10-06  
**Status:** exact finite-matrix recursion for the LCM clock. **RH remains open.**

This is the most literal matrix realization so far of:

> "the next matrix is causally motivated by the previous one, and the prime event performs the twist."

---

## 1. One LCM refinement

Suppose the current global modulus clock has length

\[
L.
\]

At the next prime-power event the LCM ratio is a prime \(p\), so the new clock has length

\[
L'=pL.
\]

Let

\[
C_L|a\rangle=|a+1\bmod L\rangle
\]

and similarly \(C_{pL}\).

Write each residue mod \(pL\) uniquely as

\[
n=a+bL,
\qquad
0\le a<L,
\quad
0\le b<p.
\]

This gives a unitary coordinate identification

\[
\mathcal D:
\ell^2(\mathbb Z/pL\mathbb Z)
\to
\ell^2(\mathbb Z/L\mathbb Z)\otimes\mathbb C^p.
\]

Then cyclic SUCC becomes

\[
\boxed{
\mathcal D C_{pL}\mathcal D^*
=
C_L\otimes I_p
+
|0\rangle\langle L-1|
\otimes
(C_p-I_p).
}
\]

Proof:

- away from \(a=L-1\), successor only increments the old \(L\)-clock coordinate;
- at \(a=L-1\), the old clock wraps and the new \(p\)-digit receives the carry.

Thus the entire refinement is:

\[
\boxed{
\text{old clock}
+
\text{one rank-one carry edge}
\otimes
\text{new }p\text{-clock}.
}
\]

This is the global version of the Round005 radix-carry identity.

---

## 2. Fourier-transform only the new digit

Let

\[
\omega_p=e^{2\pi i/p}.
\]

Diagonalize \(C_p\) by the \(p\)-point DFT.

Then the new global clock decomposes into \(p\) sectors:

\[
\boxed{
\mathcal D' C_{pL}\mathcal D'^*
=
\bigoplus_{r=0}^{p-1}
U_L(\omega_p^r),
}
\]

where

\[
\boxed{
U_L(\omega)
=
C_L
+
(\omega-1)
|0\rangle\langle L-1|.
}
\]

So:

- \(r=0\), \(\omega=1\):
  \[
  U_L(1)=C_L,
  \]
  exactly the old global clock;

- \(r=1,\ldots,p-1\):
  the same old clock is copied, but the single wrap/carry edge receives phase \(\omega_p^r\).

Therefore a prime-power event creates

\[
\boxed{
p-1
}
\]

new **boundary-twisted copies of the complete previous causal history**.

That is the finite-matrix twist mechanism in its cleanest form.

---

## 3. The twist is rank one

For every phase \(\omega\),

\[
\boxed{
U_L(\omega)-C_L
=
(\omega-1)|0\rangle\langle L-1|.
}
\]

So even though each new sector has dimension \(L\), its difference from the old clock is rank one.

All previous history is reused.

The new information is only:

\[
\boxed{
\text{which phase is applied at the carry boundary}.
}
\]

Thus the huge matrix recursion admits an extremely compact online description.

---

## 4. Each twisted sector is unitary

If

\[
|\omega|=1,
\]

then \(U_L(\omega)\) is the cyclic shift with boundary condition

\[
|L-1\rangle
\mapsto
\omega|0\rangle.
\]

Hence

\[
\boxed{
U_L(\omega)^*U_L(\omega)=I.
}
\]

So a pure modulus refinement changes phase geometry without introducing scalar gain.

This cleanly separates:

- clock/refinement twist: unitary;
- arithmetic half-density/event mass: separate amplitude channel;
- Gamma completion: separate continuous signed channel.

---

## 5. Characteristic polynomial of one boundary twist

The eigenvalue equation gives

\[
\lambda^L=\omega.
\]

Therefore

\[
\boxed{
\det(zI-U_L(\omega))
=
z^L-\omega.
}
\]

The old clock is the \(\omega=1\) sector:

\[
\det(zI-C_L)=z^L-1.
\]

So the relative determinant of one twist is

\[
\boxed{
\frac{
\det(zI-U_L(\omega))
}{
\det(zI-C_L)
}
=
\frac{z^L-\omega}{z^L-1}.
}
\]

---

## 6. Matrix determinant lemma exposes the boundary Green function

Since the twist is rank one,

\[
zI-U_L(\omega)
=
(zI-C_L)
-
(\omega-1)|0\rangle\langle L-1|.
\]

The cyclic resolvent satisfies

\[
\boxed{
\langle L-1|
(zI-C_L)^{-1}
|0\rangle
=
\frac1{z^L-1}.
}
\]

Therefore the matrix determinant lemma yields exactly

\[
\boxed{
1
-
(\omega-1)
\langle L-1|
(zI-C_L)^{-1}
|0\rangle
=
\frac{z^L-\omega}{z^L-1}.
}
\]

So the entire effect of the new prime event can be computed from **one boundary Green-function entry of the previous clock**.

This is an exceptionally compact causal recursion.

---

## 7. Product over all new phases = innovation determinant

Multiply the \(p-1\) nontrivial sectors:

\[
\prod_{r=1}^{p-1}
\det(zI-U_L(\omega_p^r)).
\]

Using

\[
\prod_{r=0}^{p-1}(x-\omega_p^r)=x^p-1,
\]

with \(x=z^L\),

\[
\boxed{
\prod_{r=1}^{p-1}
(z^L-\omega_p^r)
=
\frac{z^{pL}-1}{z^L-1}.
}
\]

Thus

\[
\boxed{
\det(zI-C_{pL})
=
\det(zI-C_L)
\prod_{r=1}^{p-1}
\det(zI-U_L(\omega_p^r)).
}
\]

The new determinant is literally the old determinant times the determinants of the carry-twisted innovation sectors.

For the pure local tower \(L=p^{k-1}\), this innovation factor is the cyclotomic polynomial

\[
\Phi_{p^k}(z).
\]

---

## 8. Exact recursive algorithm

At every SUCC pulse:

1. update
   \[
   L_{N+1}
   =
   \operatorname{lcm}(L_N,N+1);
   \]

2. compute
   \[
   r=L_{N+1}/L_N;
   \]

3. if
   \[
   r=1,
   \]
   no new matrix sector is created;

4. if
   \[
   r=p,
   \]
   a prime-power event occurred;

5. retain one exact old sector \(C_{L_N}\);

6. append \(p-1\) sectors
   \[
   U_{L_N}(\omega_p^r),
   \qquad r=1,\ldots,p-1;
   \]

7. each sector differs from the old clock by one rank-one carry-boundary phase.

No future prime list and no zero locations are required.

---

## 9. "First prime domino sets the clock" in exact matrix form

At \(N=1\),

\[
L_1=1.
\]

The first event \(2\) creates

\[
C_2.
\]

In the digit-Fourier decomposition, \(p=2\) has one nontrivial phase

\[
\omega_2=-1.
\]

So the very first refinement creates an **antiperiodic boundary twist** of the trivial one-state clock.

Every later prime-power event repeats the same operation at a larger inherited clock:

\[
\boxed{
\text{copy all accumulated history}
+
\text{twist only its carry boundary}.
}
\]

That is a strong literal realization of the user's first-domino intuition.

---

## 10. Relation to the small transfer-matrix program

Because each event is a rank-one boundary perturbation, one does not need to manipulate the full \(L\times L\) matrix to update determinant/resolvent data.

The state needed for one sector can be compressed to boundary quantities such as

\[
G_L(z)
=
\langle L-1|
(zI-C_L)^{-1}
|0\rangle.
\]

The new twist modifies determinant and resolvent by a Möbius/Sherman–Morrison update.

Thus the growing finite matrix has a natural low-dimensional transfer description.

A future step should derive the minimal state vector closed under:

- rank-one carry twist;
- physical quarter-density weighting;
- continuous Gamma drift.

That minimal closure is the precise candidate for the user's "small matrix that performs the twist."

---

## 11. Important no-go

The pure clock recursion remains unitary and Fourier-diagonalizable.

Therefore these boundary twists alone cannot prove RH.

Their significance is that they provide a **canonical non-arbitrary finite matrix skeleton** from the SUCC lightcone.

The proof-bearing structure must arise when this skeleton is coupled, before quotienting/diagonalization, to:

- half-density event masses;
- the additive SUCC boundary/history;
- mixed-prime conductor sectors;
- the continuous signed Gamma channel.

## House slogan

\[
\boxed{
\text{A prime-power event does not rebuild the clock.}
}
\]

\[
\boxed{
\text{It copies the whole previous clock and twists one carry edge.}
}
\]

\[
\boxed{
\text{In the new-digit Fourier basis, the event is }p-1\text{ boundary phases.}
}
\]

\[
\boxed{
\text{The entire determinant update is controlled by one old boundary Green function.}
}
\]
