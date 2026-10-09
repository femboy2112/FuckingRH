# Genuine Hodge-index sign on a local Tate surface — and why it is RH-inert

**2026-10-09. A completely explicit positive-control surface with an exact primitive intersection sign; NOT a zeta RH proof.**

For any real m>1, E_m=C×/m^Z is a complex elliptic curve. It is algebraic, smooth, and projective. Form the honest projective complex surface

\[
S_m=E_m\times E_m.
\]

Its dualizing/canonical bundle is trivial (abelian surface). Classical Hodge index holds.

## 1. Compute the intersection matrix

Let

\[
F_1=E_m\times\{0\},\quad
F_2=\{0\}\times E_m,\quad
\Delta=\{(x,x):x\in E_m\}.
\]

All three curves have self-intersection zero (their normal bundles are trivial; equivalently use adjunction with genus one and K_S=0). Each pair intersects transversely at one point. Therefore

\[
\boxed{
I=
\begin{pmatrix}
0&1&1\\
1&0&1\\
1&1&0
\end{pmatrix},\qquad
\operatorname{Spec}(I)=\{2,-1,-1\}.
}
\]

The class H=F_1+F_2 is ample, with H²=2. For

\[
D=aF_1+bF_2+c\Delta,
\]

the primitive condition D·H=0 is

\[
a+b+2c=0.
\]

Then b=-a-2c and direct expansion gives

\[
\boxed{
D²=2(ab+ac+bc)=-2[(a+c)^2+c^2]\le0.
}
\]

Thus the exact Hodge-index sign is positive for \(-D²\). A simple primitive witness is D=Delta-F1-F2, for which D²=-2.

This is a real *complete surface* with a real *dualizing bundle* and a real *Hodge-index inequality*.

## 2. Why none of this is the zeta Weil sign

The matrix I is independent of m and the full arithmetic source. In particular, it is identical for E_2, E_3, E_6 and E_{e^{sqrt2}}. It survives fake frequencies, fake connected impulses, and an arbitrary altered modulus.

Therefore it fails the source-fidelity/mutation conditions in the RH research program unless one first builds an independently arithmetic-dependent map f->D_f and proves

\[
-D_f\cdot\overline{D_g}=Q_W(f,g)
\]

for all admissible test functions, *including the completed Gamma/pole/contact and actual prime-power terms*.

Choosing D_f after computing Q_W to force agreement is circular. Merely observing that -D²>=0 is also useless.

Moreover the span of F1,F2,Delta is finite-dimensional, whereas Q_W on any nontrivial smooth test window has infinite algebraic rank (its Gamma high-frequency multiplier grows logarithmically and the finite prime/pole part is bounded on a fixed window). This three-class model cannot reproduce the whole form even abstractly.

## 3. Conclusion

The crude claim "RH is open because number fields have no dualizing sheaf, RR, or Hodge-index theorem at infinity" is demonstrably too strong.

The exact missing object is a **global arithmetic source-faithful self-correspondence host**, possibly with infinite-dimensional/coherent analytic cohomology, on which the full Weil form is identified with primitive intersection *before* invoking an independent Hodge-index sign.

The first truly relevant geometric experiment is thus NOT to re-prove Hodge index on E_p×E_p. It is to derive a functorial, source-rigid correspondence gluing the different local Tate curves and the Archimedean twistor component across the noncompact history spans.

**RH OPEN.**
