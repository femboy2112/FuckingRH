# The Archimedean dualizing host: absolute twistor reversal versus the Hodge-index sign

**Date:** 2026-10-09. Parent: main after Round 063. **Status:** exact local classical geometry, a newly targeted odd/even obstruction, and a rigorously identified unsolved global intersection problem. RH OPEN.

## 0. The user's hypothesis, corrected against the newest primary literature

Conjectural RH geometry often seeks a self-product of an absolute arithmetic curve, a Lefschetz/trace formula for correspondences, and a positivity mechanism analogous to Weil's proof over finite fields.

However the sentence "there is no dualizing sheaf or Serre duality for Spec Z" is **false as an unrestricted claim**. Connes and Consani established an arithmetic Riemann–Roch and Serre-duality theory for the Arakelov compactification of Spec Z in 2022/23:

- https://arxiv.org/html/2205.01391v2, Theorem 1.2 and §5.
- In their S[±1]-model the canonical-divisor analogue is K=-2{2}, degree -2 log 2.
- A dualizing module U(1)_{1/4} appears in their Pontryagin/Serre duality.
- Their later S-base RR for the ring Z is a different refinement: https://arxiv.org/abs/2306.00456.

Nor is it correct that RR mechanically proves positivity. RR is an Euler-characteristic identity. Hodge index is an **additional** signature theorem involving an independently selected ample class.

The honest missing thing is a **surface-level RH-compatible dualizing/intersection/polarization theory** on an absolute arithmetic self-correspondence host, together with a zero-free identification of its primitive intersection pairing with the COMPLETE completed Weil form.

## 1. A startling 2026 primary-source alignment

Connes and Consani's **The Absolute Twistor Line and the Geometry of the Compactification of Spec Z**, arXiv:2609.00299 (submitted 2026-08-31), constructs an absolute archimedean component over the signed base F_{1²}, glued to an absolute arithmetic curve.

Source: https://arxiv.org/html/2609.00299v1

The two affine orderings at infinity are exchanged. At the sheaf level the signed orientation reversal is modeled by T -> -1/T. On complex points the twistor real structure is the anti-holomorphic involution

\[
\boxed{\jmath(z)=-1/\bar z.}
\]

This is NOT the same thing as naive time inversion z->1/z. It is fixed-point-free and incorporates a real structure. The paper also restricts its intrinsic Frobenius/Adams action to ODD positive integers because of the signed base.

This is an actual geometric realization of part of the user's proposed *reversal axis*. The paper DOES NOT establish a self-product Hodge-index inequality or RH.

## 2. Concrete local dualizing bundle at infinity (complex-point model, NOT an established absolute sheaf)

On the familiar complex projective line X=P¹_C with charts U_0 (coordinate z) and U_infty (w=1/z), the ordinary dualizing/canonical line bundle is

\[
\boxed{\omega_X=\Omega_X^1\cong\mathcal O(-2).}
\]

The transition is

\[
dw=-z^{-2}dz.
\]

For the signed chart inversion w=-1/z one instead obtains

\[
dw=z^{-2}dz,\qquad d\log w=-d\log z.
\]

A Čech representative of the one-dimensional group H¹(X,omega_X) is dz/z. Serre duality has the explicit residue pairing

\[
\boxed{
H^0(X,\mathcal O)\times H^1(X,\omega_X)\to\mathbb C,\quad
(c,[g(z)dz])\mapsto c\,\operatorname{Res}_{z=0}(g(z)dz).
}
\]

For the generator [dz/z], the value on 1 is 1. Under z->-1/w, dz/z=-dw/w: the two chart residues have opposite signs and cancel globally.

This is a mathematically explicit *local complex-point dualizing model* for the Archimedean twistor component. It is **not** by itself a dualizing complex of the new F_{1²}-topos, still less of the absolute arithmetic self-product.

## 3. The half-canonical spinor has quaternionic reversal

On P¹_C, \(\omega_X^{1/2}=\mathcal O(-1)\).

Use homogeneous coordinates and the anti-linear map on C²,

\[
\boxed{
J(v_0,v_1)=(-\bar v_1,\bar v_0).
}
\]

It induces \(\jmath([v_0:v_1])=[J(v_0,v_1)]\), the twistor involution z->-1/conj(z), and

\[
\boxed{J^2=-I.}
\]

Thus the induced real structure on the tautological/half-canonical line \(\mathcal O(-1)\) is quaternionic (squares to -1 on fibers).

On its tensor square \(\mathcal O(-2)\), the induced real structure squares to +1.

This gives an exact *orientation/chirality distinction*:

- half-canonical spinor: antiunitary reversal squared = -1;
- canonical line: induced real structure squared = +1.

This is standard twistor geometry, not a new RH theorem. It does not identify the square root of the geometric canonical bundle with the arithmetic Haar half-density p^{-1/2}; that would need an explicit functor/intertwiner.

## 4. The odd-Frobenius / p=2 obstruction is exact

In Connes–Consani's signed absolute algebra, the generator obeys J²=epsilon, epsilon=-1. Under the naive Frobenius action \(J\mapsto J^n\), preservation of the signed relation requires

\[
(J^n)^2=\epsilon^n=\epsilon,
\]

i.e.

\[
\boxed{n\text{ odd}.}
\]

For even n (in particular n=2), it fails. This matches the paper's restriction to the odd monoid and its interpretation of the special ramification of 2.

There is a classical geometric shadow of exactly this parity constraint. For \(f_n:P¹\to P¹\), \(z\mapsto z^n\),

\[
R_{f_n}=(n-1)[0]+(n-1)[\infty],
\]

and Riemann–Hurwitz gives

\[
\boxed{K_X=f_n^*K_X+R_{f_n}.}
\]

A *branch-supported integral half-ramification divisor* \(R_{f_n}/2\) exists iff n is odd, because each coefficient n-1 must be even. For even n the total ramification bundle admits a square root as a line bundle, but no such canonical integral HALF at each branch point. This limited, precise geometric obstruction must not be exaggerated into nonexistence of all spin lifts.

**Candidate new probe:** identify the correction needed to extend the signed twistor duality through the genuine p=2 prime-power clock while keeping all arithmetic data at the physical log 2. If the lift arbitrarily redefines log 2 or invents fake composite primitive impulses, it fails source fidelity.

The older Connes–Consani model has a canonical-divisor analogue K=-2{2}, also singling out the prime 2. No mathematical equivalence between this older model's K and the 2026 twistor ramification is established here. It is a tempting comparison to TEST, not a proved identification.

## 5. RR is not the missing sign: an exact elementary counterexample

On P¹, the bundle O(-1) has degree -1 yet satisfies both Serre duality and RR:

\[
h^0(O(-1))=h^1(O(-1))=0,\qquad
\chi(O(-1))=0=(-1)+1-g.
\]

So a valid canonical bundle plus perfect Serre duality plus RR does NOT imply deg D >= 0 for arbitrary divisors D.

For a projective surface S and an ample H, the Hodge index theorem separately says

\[
\boxed{D\cdot H=0\implies D^2\le0.}
\]

That primitive negative-square inequality is what supplies the RH-for-curves sign on \(C\times C\), not RR alone. Sources:

- Kiran Kedlaya, Two approaches to RH for curves, https://kskedlaya.org/weil-cohom/chapter-5.html
- P. Deligne/Weil correspondence discussions; function-field CxC Frobenius/diagonal geometry is standard.

## 6. The actual absolute self-product theorem one would need

Let \(\mathscr C=\overline{\operatorname{Spec}\mathbb Z}_{\rm abs}\) in a suitable absolute category, and suppose its properly compactified self-correspondence host \(\mathscr S=\mathscr C\times_{\rm abs}\mathscr C\) has:

1. a dualizing complex or canonical sheaf \(\omega_{\mathscr S}\), compatible with both local orientations and the p=2 ramification;
2. a trace and intersection product on a possibly infinite-dimensional completed space of correspondences;
3. an independently defined ample/polarization class H;
4. a source-constructed map \(f\mapsto D_f\), retaining the actual \(\Lambda(n)n^{-1/2}\), the exact \(\log p\), primitive Hecke phases, full Gaussian/Gamma, the pole and origin terms;
5. the *full polarized* identification

\[
\boxed{
D_f\cdot H=0,\qquad
-(D_f\cdot\overline{D_g})=Q_W(f,g)
}
\]

with no zeta zeros supplied as construction data;
6. an Hodge-index theorem \(-(D_f\cdot\overline{D_f})\ge0\) derived independently of Q_W and robust under the appropriate proper-lift conditions.

Then RH follows by Weil's criterion. **NONE of 1–6 as a COMPLETE RH-bearing package is currently supplied.**

This is a precise specification of the fourth gate, not a proof.

## 7. A finite-rank obstruction to naive host surfaces

At any nontrivial window A, the Weil form on C_c^\infty(-A,A) has infinite algebraic rank. One way to see this: its Archimedean Fourier multiplier behaves as log |u|; the finite prime shifts and pole forms are bounded perturbations on that window. The completed Weil operator has compact resolvent and eigenvalues unbounded above (proved in the project's rigorous Weil–Suzuki bridge). Hence it has infinitely many nonzero eigenmodes.

On an ordinary smooth projective surface, NS(S)_R has finite dimension rho(S). Any bilinear intersection form pulled back by a linear map into this finite-dimensional space has rank at most rho(S), so it CANNOT equal Q_W on all tests.

Thus a candidate host must use a much larger completed correspondence/cohomology space (infinite-genus/infinite-dimensional or distributional), rather than the bare finite Néron-Severi lattice of one usual projective surface.

Over F_q the curve genus g and its zeta numerator are finite-dimensional; the corresponding ordinary geometry suffices. Over Q the nontrivial zeta spectrum is infinite, and a genuinely infinite cohomological host is expected.

## 8. The existing source-to-completion duality

For the self-dual real Gaussian g(x)=e^{-pi x²}, the Archimedean Tate zeta integral gives

\[
Z_\infty(g,s)=\pi^{-s/2}\Gamma(s/2).
\]

For each p, the unramified indicator \(1_{\mathbb Z_p}\) has local zeta factor \((1-p^{-s})^{-1}\). The restricted global tensor supplies \(\pi^{-s/2}\Gamma(s/2)\zeta(s)\) in Re s>1.

Let \(\theta(t)=\sum_{n\in\mathbb Z}e^{-\pi n²t}\). Poisson gives \(\theta(t)=t^{-1/2}\theta(1/t)\). Splitting the Mellin integral at t=1 gives the entire zero-free construction

\[
\boxed{
\begin{aligned}
\Lambda(s)&=\pi^{-s/2}\Gamma(s/2)\zeta(s)\\
&=\frac1{s(s-1)}
+\frac12\int_1^\infty[\theta(t)-1]
\big(t^{s/2}+t^{(1-s)/2}\big)\frac{dt}{t}.
\end{aligned}
}
\]

This identity initially agrees with the convergent Euler region and yields meromorphic continuation and reflection \(\Lambda(s)=\Lambda(1-s)\) without zero input. The rational pole term is forced by zero-mode boundary contributions, not fitted.

On the Mellin Hilbert space L²(R_+,dx), \(R f(x)=x^{-1}\overline{f(1/x)}\) is a canonical antiunitary involution. With \(\mathcal M f(s)=\int_0^\infty f(x)x^{s-1}dx\),

\[
\boxed{\mathcal M(Rf)(s)=\overline{\mathcal M f(1-\bar s)}.}
\]

This is the analytic "shadow of Serre duality" at infinity. It supplies *reversal and a perfect pairing*, not a Hodge polarization. Davenport–Heilbronn satisfies a similar functional-equation symmetry; the construction must read connected Euler/Hecke source structure too.

## 9. Next falsifiable test: the 2–3–infinity spin/dualizing triangle

Build a minimal system coupling:

- true source at p=2,3 with the physical log p and p^{-k/2};
- exact conductor W_6 (joint primitive sector), which is invisible to the two single-place amplitude-averaging shadows but exists globally;
- the Archimedean Gaussian/Poisson vector-theta reversal;
- the ordinary complex-point dualizing cocycle O(-2) and its quaternionic half-spin O(-1);
- an explicit *candidate* p=2 ramification correction.

Require in order:

(A) finite conductor theta/Poisson identity and antiunitary R²=I;

(B) exact source admissibility: chi/H_euler support, no independent connected 6-impulse, alpha2 unitary where unramified, log2 fixed;

(C) dualizing/Serre nondegenerate pairing and compatible twistor chiral inversion;

(D) a **new independently defined** global pairing whose full polarized discrepancy with the completed Weil Q_A vanishes, including the Gamma digamma, pole and negative bulk terms;

(E) an independently proved Hodge-index positivity on the primitive image, not the sign assumed by definition.

A construction passing A–C but failing D or E is stage reconstruction; it does not advance RH.

## 10. Epistemic status

The sources show:
- a **curve-level** arithmetic Serre/RR theorem: proved in its declared model;
- a **new 2026 Archimedean absolute-twistor geometry**: proposed/proved within the preprint's framework;
- standard complex-point Serre duality K=O(-2), quaternionic half-canonical O(-1), and Riemann–Hurwitz: classical;
- standard finite-conductor Fourier/Poisson reversal: exact and numerically checked;
- the RH-bearing complete surface correspondence/intersection and independent Hodge sign: **OPEN**.

The next step is to derive or refute a genuine p=2 ramification/spin correction coupled to actual Hecke/Gamma source data, not to postulate a missing "canonical sheaf" that the literature already partially supplied.
