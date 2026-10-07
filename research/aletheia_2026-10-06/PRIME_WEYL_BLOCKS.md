# Prime Weyl blocks: radial FUCC persistence + cyclotomic carry phase

**Date:** 2026-10-06  
**Status:** exact local operator-valued Weyl construction; global assembly remains open. **RH remains open.**

The local prime machinery has two independently derived pieces:

1. a radial depth-persistence coefficient
   \[
   r_p=p^{-1/2}
   \]
   from normalized nested \(p\)-adic balls;

2. a unitary exact-conductor SUCC twist
   \[
   U_{p,k}^{\rm new}
   \]
   on the innovation space \(W_{p,k}\), with cyclotomic spectrum.

These combine canonically into a strict contraction.

---

## 1. Exact local contraction

At prime-power depth \(k\), let

\[
U_{p,k}^{\rm new}:W_{p,k}\to W_{p,k}
\]

be successor restricted to the exact-conductor innovation space.

It is unitary and

\[
\operatorname{Spec}(U_{p,k}^{\rm new})
=
\{
e^{2\pi ia/p^k}:(a,p)=1
\}.
\]

Set

\[
\boxed{
A_{p,k}
=
r_p U_{p,k}^{\rm new},
\qquad
r_p=p^{-1/2}.
}
\]

Then

\[
\boxed{
A_{p,k}^*A_{p,k}
=
r_p^2I,
\qquad
\|A_{p,k}\|=r_p<1.
}
\]

This uses no zero data and no fitted coefficient.

The radius comes from FUCC-depth Haar geometry.
The angular part comes from the conductor/carry clock.

---

## 2. Operator-valued Carathéodory/Weyl block

For \(|z|<1\), define

\[
\boxed{
F_{p,k}(z)
=
(I+zA_{p,k})
(I-zA_{p,k})^{-1}.
}
\]

Because

\[
\|zA_{p,k}\|<1,
\]

this is analytic in the disk.

Its Hermitian real part is

\[
\boxed{
\Re F_{p,k}(z)
=
(I-\bar zA_{p,k}^*)^{-1}
\left(
I-|z|^2A_{p,k}^*A_{p,k}
\right)
(I-zA_{p,k})^{-1}.
}
\]

Since

\[
A_{p,k}^*A_{p,k}=r_p^2I,
\]

\[
I-|z|^2A_{p,k}^*A_{p,k}
=
(1-r_p^2|z|^2)I>0.
\]

Hence

\[
\boxed{
\Re F_{p,k}(z)\succ0
\qquad(|z|<1).
}
\]

So every exact-conductor prime refinement has a canonical matrix-valued Weyl/Carathéodory block.

---

## 3. Spectral decomposition: phase can dance arbitrarily

If

\[
U_{p,k}^{\rm new}v=\omega v,
\qquad
|\omega|=1,
\]

then

\[
F_{p,k}(z)v
=
\frac{1+r_p\omega z}
{1-r_p\omega z}v.
\]

Thus every conductor mode sees a scalar Carathéodory function

\[
\boxed{
F_{r,\omega}(z)
=
\frac{1+r\omega z}{1-r\omega z}.
}
\]

For any phase \(\omega\in\mathbb T\),

\[
\Re F_{r,\omega}(z)>0
\qquad(|z|<1)
\]

as long as

\[
0\le r<1.
\]

Therefore the phase pattern may be:

- highly irregular;
- gauge transformed;
- pseudorandom-looking;
- replaced by any unitarily equivalent representation;

without damaging local Weyl positivity.

The rigid condition is the radial contraction.

This is the exact structural form of the user's "the map can vary while the support property survives" intuition.

---

## 4. The corresponding operator Schur function

The Cayley transform is

\[
\boxed{
S_{p,k}(z)
=
(F_{p,k}(z)-I)
(F_{p,k}(z)+I)^{-1}
=
zA_{p,k}.
}
\]

Therefore

\[
\boxed{
\|S_{p,k}(z)\|
\le
|z|r_p<1.
}
\]

The local arithmetic block is a strict matrix-valued Schur function.

Again:

- \(U_{p,k}^{\rm new}\) contains the phase/carry geometry;
- \(r_p\) contains the critical local depth persistence;
- contractivity depends only on \(r_p<1\).

---

## 5. Relation to the scalar nested-ball Weyl function

If the conductor phase is trivial,

\[
U=I,
\]

then

\[
F_{p,k}(z)
=
\frac{1+r_pz}{1-r_pz}I,
\]

which is exactly the scalar prime-depth Weyl function previously derived.

So the operator-valued block is the phase-resolved refinement of the old Poisson kernel.

The scalar local Poisson kernel is the phase-forgotten shadow.

---

## 6. Julia unitary colligation

For any contraction \(A\), define defect operators

\[
D_A=(I-A^*A)^{1/2},
\qquad
D_{A^*}=(I-AA^*)^{1/2}.
\]

Here

\[
D_A=D_{A^*}
=
\sqrt{1-r_p^2}\,I.
\]

The Julia operator

\[
\boxed{
\mathcal J(A)
=
\begin{pmatrix}
A&D_{A^*}\\
D_A&-A^*
\end{pmatrix}
}
\]

is unitary.

For the prime block,

\[
\boxed{
\mathcal J_{p,k}
=
\begin{pmatrix}
r_pU_{p,k}^{\rm new}
&
\sqrt{1-r_p^2}\,I
\\[1mm]
\sqrt{1-r_p^2}\,I
&
-r_p(U_{p,k}^{\rm new})^*
\end{pmatrix}.
}
\]

This realizes each prime refinement as a **lossless two-port scattering system**:

- arithmetic/conductor channel;
- complementary defect/vacuum channel.

The unitarity is exact.

---

## 7. Transfer function of one Julia block

For a unitary colligation

\[
\mathcal U
=
\begin{pmatrix}
A&B\\
C&D
\end{pmatrix},
\]

the transfer function is

\[
\Theta_{\mathcal U}(z)
=
A+zB(I-zD)^{-1}C.
\]

For the Julia block,

\[
\boxed{
\Theta_A(z)
=
A
+
z(1-r_p^2)
(I+zA^*)^{-1}.
}
\]

In a scalar eigenchannel

\[
A=\alpha=r_p\omega,
\]

this becomes

\[
\boxed{
\Theta_\alpha(z)
=
\frac{\alpha+z}
{1+\bar\alpha z}.
}
\]

This is an automorphism of the unit disk.

Thus a prime/carry mode gives an explicit disk-preserving Möbius transfer.

---

## 8. Chronological cascades preserve the structural class

Lossless/unitary colligations can be interconnected in series/feedback networks.

When the interconnection is itself unitary, the resulting transfer function stays in the operator Schur class.

Therefore one does **not** need a simple or non-random sequence of prime phases in order to preserve Weyl positivity.

What is required is:

\[
\boxed{
\text{every local block is contractive/passive}
}
\]

and

\[
\boxed{
\text{the boundary interconnection preserves the lossless signature}.
}
\]

The microscopic phase dance may remain complicated.

The global Weyl property can be a structural invariant of the network class.

---

## 9. Quarter-density is a separate normalization layer

The event/kernel mass at \(p^k\) is

\[
w_{p,k}
=
(\log p)p^{-k/2}.
\]

A Gram factor leg therefore carries

\[
a_{p,k}
=
\sqrt{\log p}\,p^{-k/4}.
\]

This should **not automatically be identified** with the local Schur contraction \(r_p\).

They encode different structures:

\[
\boxed{
r_p=p^{-1/2}
=
\text{adjacent FUCC-depth persistence},
}
\]

whereas

\[
\boxed{
a_{p,k}
=
\sqrt{\log p}\,p^{-k/4}
=
\text{physical one-leg event amplitude}.
}
\]

Conflating them would double-count or misplace the critical normalization.

The Weyl state dynamics uses \(r_p\).
The readout/coupling strength uses the event mass/quarter-density.

---

## 10. Nevertheless the one-leg event amplitudes are automatically contractions

A useful independent fact is

\[
\boxed{
0<a_{p,k}<1
}
\]

for every prime \(p\) and \(k\ge1\).

Proof: let

\[
x=\log p>0.
\]

Then

\[
a_{p,k}^2
=
x e^{-kx/2}.
\]

The continuous maximum occurs at

\[
x=\frac2k,
\]

with value

\[
\frac{2}{ke}
\le
\frac2e<1.
\]

Therefore

\[
\boxed{
a_{p,k}
\le
\sqrt{2/e}
<1.
}
\]

So the critical quarter-density amplitudes are admissible Schur/Verblunsky magnitudes if a later theorem identifies the factor channel with a Schur parameter.

That identification is **not** assumed here.

---

## 11. Candidate universality statement

Suppose the detailed carry map is changed by unitary gauges

\[
U_{p,k}\mapsto
G_{p,k}^*
U_{p,k}
G_{p,k}.
\]

Then

\[
A_{p,k}\mapsto
G_{p,k}^*
A_{p,k}
G_{p,k}
\]

and

\[
F_{p,k}(z)\mapsto
G_{p,k}^*
F_{p,k}(z)
G_{p,k}.
\]

Positive-realness is unchanged.

Thus the local Weyl structure depends only on the unitary-equivalence class of the phase dynamics plus the radial coefficient \(r_p\).

This formalizes a broad gauge freedom in the microscopic encoding.

---

## 12. What remains genuinely difficult

Local passivity does not imply that the global completed arithmetic transfer equals

\[
m_\Xi=-\Xi'/\Xi.
\]

The missing work is to derive the actual interconnection law from:

- chronological SUCC;
- carry boundary;
- CRT/conductor overlaps;
- Gamma/inverse-SUCC completion;

and then prove the resulting boundary transfer is the completed zeta logarithmic derivative.

The local Weyl blocks solve the **positivity of the pieces**.

They do not yet solve the **arithmetic identification of the assembled system**.

### House slogan

\[
\boxed{
\text{FUCC gives the radius.}
}
\]

\[
\boxed{
\text{carry/conductor gives the phase.}
}
\]

\[
\boxed{
\text{Weyl positivity does not care how ugly the phase dance is.}
}
\]

\[
\boxed{
\text{the remaining problem is the exact global interconnection.}
}
\]
