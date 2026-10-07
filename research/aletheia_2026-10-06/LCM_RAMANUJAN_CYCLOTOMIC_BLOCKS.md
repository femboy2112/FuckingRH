# LCM clock innovations: Ramanujan projectors, cyclotomic twist blocks, and quarter-density

**Date:** 2026-10-06  
**Status:** exact finite harmonic analysis of the LCM/SUCC clock; canonical local blocks for the growing-matrix program. **RH remains open.**

This note audits and strengthens the proposed finite-matrix cocycle based on

\[
L_N=\operatorname{lcm}(1,\ldots,N).
\]

The main new result is:

> A prime-power refinement \(p^{k-1}\to p^k\) has a canonical orthogonal innovation subspace. Its normalized Gram kernel is a Ramanujan-sum matrix, and successor restricted to that innovation space has characteristic polynomial \(\Phi_{p^k}\), the cyclotomic polynomial.

Thus the clock/carry data already supply a non-arbitrary finite matrix block at every prime-power domino.

---

## 1. Normalized Haar measure is required

Use

\[
H_L=L^2(\mathbb Z/L\mathbb Z,\mu_L),
\qquad
\mu_L(\{x\})=\frac1L.
\]

If \(L\mid L'\), let

\[
\pi_{L',L}:\mathbb Z/L'\mathbb Z\to\mathbb Z/L\mathbb Z
\]

be reduction and define pullback

\[
J_{L,L'}f=f\circ\pi_{L',L}.
\]

Then

\[
\boxed{
\|J_{L,L'}f\|_{H_{L'}}=\|f\|_{H_L}.
}
\]

With unnormalized counting measure the same pullback has norm \(\sqrt{L'/L}\), so the normalization is load-bearing.

For the LCM filtration \(L_N\mid L_{N+1}\), the normalized spaces form an isometric inductive system whose cylinder-function completion is

\[
L^2(\widehat{\mathbb Z}).
\]

The successor translations intertwine exactly.

---

## 2. Local prime-power refinement

Fix a prime \(p\) and let

\[
H_{p,k}
=
L^2(\mathbb Z/p^k\mathbb Z).
\]

The pullback

\[
J_{k-1,k}:H_{p,k-1}\hookrightarrow H_{p,k}
\]

identifies the old clock states inside the refined clock.

Define the new-detail/innovation space

\[
\boxed{
W_{p,k}
=
H_{p,k}\ominus J_{k-1,k}H_{p,k-1}.
}
\]

Its dimension is

\[
\boxed{
\dim W_{p,k}
=
p^k-p^{k-1}
=
\varphi(p^k).
}
\]

So deepening the \(p\)-clock adds exactly \(\varphi(p^k)\) new local harmonic degrees of freedom.

---

## 3. Fourier description: exact-conductor characters

The normalized additive characters

\[
\chi_a(n)
=
e^{2\pi ian/p^k},
\qquad
a\in\mathbb Z/p^k\mathbb Z,
\]

form an orthonormal basis.

The old pulled-back subspace consists exactly of the characters with

\[
p\mid a.
\]

Therefore

\[
\boxed{
W_{p,k}
=
\operatorname{span}
\{
\chi_a:p\nmid a
\}.
}
\]

These are precisely the additive characters of **exact conductor \(p^k\)**.

Thus one prime-power domino does not merely enlarge the clock dimension. It activates the primitive/exact-conductor harmonic sector at that depth.

---

## 4. Canonical innovation projector = Ramanujan-sum matrix

Let \(P_{p,k}\) be the orthogonal projector onto \(W_{p,k}\).

In the normalized point basis of \(\ell^2(\mathbb Z/p^k\mathbb Z)\),

\[
\boxed{
(P_{p,k})_{mn}
=
\frac1{p^k}
c_{p^k}(m-n),
}
\]

where

\[
c_q(r)
=
\sum_{\substack{a\!\!\!\pmod q\\(a,q)=1}}
e^{2\pi iar/q}
\]

is the Ramanujan sum.

For \(q=p^k\),

\[
c_{p^k}(r)
=
\begin{cases}
\varphi(p^k),&p^k\mid r,\\
-p^{k-1},&p^{k-1}\mid r,\ p^k\nmid r,\\
0,&p^{k-1}\nmid r.
\end{cases}
\]

Hence the diagonal is

\[
(P_{p,k})_{nn}
=
\frac{\varphi(p^k)}{p^k}
=
1-\frac1p.
\]

The projector is positive semidefinite by construction.

---

## 5. Correlation normalization gives a universal \(p\)-simplex block

Normalize the diagonal to \(1\):

\[
\boxed{
C_{p,k}
=
\frac{p^k}{\varphi(p^k)}P_{p,k}.
}
\]

Then

\[
\boxed{
(C_{p,k})_{mn}
=
\frac{c_{p^k}(m-n)}{\varphi(p^k)}
}
\]

takes only three values:

\[
(C_{p,k})_{mn}
=
\begin{cases}
1,&m\equiv n\pmod{p^k},\\[1mm]
-\dfrac1{p-1},
&m\equiv n\pmod{p^{k-1}}
\text{ but }m\not\equiv n\pmod{p^k},\\[2mm]
0,&m\not\equiv n\pmod{p^{k-1}}.
\end{cases}
\]

This is an exact normalized clock/carry kernel.

At \(k=1\), it is the Gram matrix of a regular \((p-1)\)-simplex:

\[
\boxed{
C_{p,1}
=
\begin{cases}
1&\text{diagonal},\\
-1/(p-1)&\text{off diagonal}.
\end{cases}
}
\]

At higher \(k\), the same simplex geometry repeats independently over each depth-\((k-1)\) residue cell.

Thus the new \(p\)-digit is geometrically a **zero-sum \(p\)-ary detail mode**.

This is the finite-clock analogue of a \(p\)-adic Haar wavelet layer.

---

## 6. Möbius is already inside the matrix entries

The general Ramanujan identity

\[
\boxed{
c_q(n)
=
\sum_{d\mid(q,n)}
d\,\mu(q/d)
}
\]

shows that the signed Möbius/inclusion-exclusion structure appears automatically in the exact-conductor projector.

So Möbius signs need not be inserted as a separate fermionic decoration at this level.

They arise from subtracting the old clock subspace from the refined clock.

This gives a new interpretation of earlier Round004 Möbius/Koszul work:

\[
\boxed{
\text{Möbius}
=
\text{signed incidence kernel of conductor innovation}.
}
\]

The pure projector is still RH-inert locally; the value is that the sign structure now has a canonical clock/refinement origin.

---

## 7. Successor on the innovation layer = a cyclotomic twist block

Let

\[
U_{p,k}f(n)=f(n-1)
\]

be cyclic successor on \(\mathbb Z/p^k\mathbb Z\).

In the exact-conductor Fourier basis of \(W_{p,k}\),

\[
U_{p,k}\chi_a
=
e^{-2\pi ia/p^k}\chi_a,
\qquad p\nmid a.
\]

Therefore the characteristic polynomial of successor restricted to the innovation sector is

\[
\boxed{
\det(zI-U_{p,k}|_{W_{p,k}})
=
\Phi_{p^k}(z),
}
\]

the \(p^k\)-th cyclotomic polynomial.

For a prime power,

\[
\boxed{
\Phi_{p^k}(z)
=
\frac{z^{p^k}-1}{z^{p^{k-1}}-1}
=
1+z^{p^{k-1}}+\cdots+z^{(p-1)p^{k-1}}.
}
\]

Thus every prime-power domino supplies a canonical finite **twist matrix**:

- state space = exact-conductor innovations \(W_{p,k}\);
- Gram = Ramanujan projector;
- SUCC twist spectrum = primitive \(p^k\)-th roots of unity;
- spectral determinant = cyclotomic polynomial \(\Phi_{p^k}\).

No zeta zeros are used.

---

## 8. Conductor decomposition of the whole finite global clock

For any finite cyclic clock \(\mathbb Z/L\mathbb Z\),

\[
H_L
=
\bigoplus_{d\mid L}W_d,
\]

where \(W_d\) is the exact-conductor-\(d\) character subspace and

\[
\dim W_d=\varphi(d).
\]

The dimension identity

\[
\boxed{
L=\sum_{d\mid L}\varphi(d)
}
\]

is exactly the orthogonal decomposition of the whole clock into conductor innovations.

Successor restricted to \(W_d\) has characteristic polynomial

\[
\Phi_d(z).
\]

Hence

\[
\boxed{
z^L-1
=
\prod_{d\mid L}\Phi_d(z)
}
\]

is literally the determinant factorization of the finite SUCC clock by its conductor layers.

This supplies mixed-prime conductor sectors \(d\), not merely independent prime towers.

However the pure cyclic successor remains Fourier-diagonal/commutative and therefore inherits the Round005
RH-inert no-go. Arithmetic relevance must come from how boundaries/carry/history operators mix these conductor sectors.

---

## 9. The full LCM filtration: what changes at a prime-power event

Suppose

\[
N+1=p^k.
\]

Then

\[
L_{N+1}=pL_N.
\]

Locally, only the \(p\)-primary conductor depth changes:

\[
p^{k-1}\to p^k.
\]

Globally, the old Hilbert space embeds isometrically into the new one.

The orthogonal complement has dimension

\[
\boxed{
L_{N+1}-L_N
=
(p-1)L_N.
}
\]

This is the old global clock tensored with one new local \(p\)-detail degree.

Because the extension

\[
0\to\mathbb Z/p\mathbb Z
\to
\mathbb Z/pL_N\mathbb Z
\to
\mathbb Z/L_N\mathbb Z
\to0
\]

contains carry, the refinement is not equivariantly a trivial direct product when \(p\mid L_N\).

The quotient/remainder tensor decomposition is a vector-space factorization whose nontrivial addition law is precisely the carry coupling found in Round005.

---

## 10. Quarter-density audit of the proposed harmonic Gram

Consider features

\[
\phi_t(u)
=
e^{-\sigma u}e^{itu}
\]

in

\[
L^2(d\log L).
\]

Their Gram is

\[
G_{jk}^{(N)}
=
\int_0^{\log N}
e^{-2\sigma u}
e^{i(t_j-t_k)u}
\,d\log L(u).
\]

Since

\[
d\log L(u)
=
\sum_{p,r}
(\log p)\delta_{r\log p}(du),
\]

\[
\boxed{
G_{jk}^{(N)}
=
\sum_{p^r\le N}
(\log p)
p^{-2\sigma r}
e^{i(t_j-t_k)r\log p}.
}
\]

Therefore, in the convergent infinite-horizon region,

\[
\boxed{
G_{jk}
=
-\frac{\zeta'}{\zeta}
\bigl(
2\sigma-i(t_j-t_k)
\bigr)
}
\]

with the sign convention determined by the exponential.

Thus if the desired **kernel-level** critical event mass is

\[
(\log p)p^{-r/2},
\]

then one must set

\[
\boxed{
2\sigma=\frac12,
\qquad
\sigma=\frac14.
}
\]

This exactly matches the independent factor-normalization result:

\[
\boxed{
\text{critical half-density in }K=B^*B
\Longleftrightarrow
\text{quarter-density on each }B\text{ leg}.
}
\]

Using \(\sigma=1/2\) in each feature leg would instead produce the safe-line weight \(p^{-r}\).

This is a load-bearing normalization correction.

---

## 11. A canonical small block from each event

The growing-matrix program therefore has a much less arbitrary local ingredient than a generic kernel.

At event \(p^k\), use:

1. **mass amplitude**
   \[
   a_{p,k}
   =
   \sqrt{\log p}\,p^{-k/4};
   \]

2. **normalized innovation Gram**
   \[
   C_{p,k}
   =
   \left[
   c_{p^k}(m-n)/\varphi(p^k)
   \right];
   \]

3. **SUCC twist**
   \[
   U_{p,k}|_{W_{p,k}},
   \]
   whose determinant is \(\Phi_{p^k}\);

4. **carry coupling**
   induced by the nontrivial quotient/remainder embedding into the previous global clock.

So a local event block has the schematic form

\[
\boxed{
M_{p,k}(z)
=
\text{carry/refinement map}
\circ
\text{cyclotomic SUCC twist}
\circ
a_{p,k}.
}
\]

The exact reduction to a minimal \(2\times2\) transfer matrix remains to be derived.

---

## 12. The pure-clock no-go remains

The conductor/Ramanujan/cyclotomic decomposition is highly structured but, by itself, it diagonalizes the finite cyclic SUCC clock.

Thus it cannot be the missing RH mechanism alone.

The new theorem target is more specific:

\[
\boxed{
\text{derive how the SUCC boundary/carry operator mixes exact-conductor sectors under chronological LCM refinement.}
}
\]

That mixing must then be coupled to the continuous Gamma channel before taking the spectral determinant.

If one Fourier-diagonalizes and discards the carry/history mixing first, the construction collapses back to an RH-inert commutative clock.

---

## 13. Short interpretation

At a prime-power event:

\[
\boxed{
\text{old clock}
\to
\text{new exact-conductor detail space}.
}
\]

Its canonical normalized covariance is a Ramanujan-sum matrix.

Its canonical SUCC twist is cyclotomic.

Its one-leg physical amplitude is quarter-density.

Its nontrivial global effect can only come from how carry/history couples this new detail space to the previous conductor strata and to the Gamma carrier.

### House slogan

\[
\boxed{
\text{Prime powers don't just add dimensions; they add primitive conductor modes.}
}
\]

\[
\boxed{
\text{Ramanujan sums are the clock's innovation Gram.}
}
\]

\[
\boxed{
\text{Cyclotomic polynomials are the local SUCC twist determinants.}
}
\]

\[
\boxed{
\text{Quarter-density is the correct matrix-leg normalization.}
}
\]
