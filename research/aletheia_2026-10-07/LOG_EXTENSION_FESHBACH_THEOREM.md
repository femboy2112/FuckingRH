# Exact zero-extension Weil form, logarithmic spectral gap, and finite-horizon Feshbach theorem

**Date:** 2026-10-07
**Scope:** mathematical theorem and source-normalization audit; **RH IS OPEN**.
**Parent audit:** [RH_PROOF_BEARING_FRAME_AUDIT.md](RH_PROOF_BEARING_FRAME_AUDIT.md).
**Primary source:** Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3, (2.3)–(2.7), especially page 9's log boundary form and page 10's Fourier multiplier. Suzuki credits Connes–Consani–Moscovici for the established discrete lower-bounded finite-interval spectrum; we claim no priority for compactness/discreteness itself.

## 0. Why this replaces the previous guesswork

The first audit separated the positive parts of Suzuki's logarithmic boundary potential pointwise. That was valid but not canonical. This theorem instead absorbs the **entire** singular boundary potential into one exact, finite-range *zero-extension difference square*. It then proves a quantitative, horizon-independent **lower bound for ordered eigenvalues** via a time-frequency trace estimate. An exact finite-dimensional Feshbach test follows at each fixed interval, with every coefficient forced from the published source.

This is structural theorem progress, **not** the missing all-horizon RH positivity inequality.

## 1. Fix the exact source normalization

Let \(I=(-a,a)\), \(a>0\), and \(v\in C_c^\infty(I)\). Let \(v_0\) be its zero extension to the real line.

Suzuki defines the logarithmic part of the localized Weil form by

\[
\boxed{
L_a(v)=\frac14\int_I\int_I
\frac{|v(x)-v(y)|^2}{|x-y|}\,dx\,dy
-\frac12\int_I\log(a^2-x^2)|v(x)|^2\,dx.
}
\]

The complete finite form, after completing the prime correlations into difference squares, is (with the remaining primary-source constants unchanged)

\[
\boxed{
Q_W^a(v)
=
L_a(v)
+
E_{{\rm prime},a}(v)
-\mathcal V_a\|v\|_2^2
-\langle R_av,v\rangle,
}
\]

where

\[
E_{{\rm prime},a}(v)
=
\sum_{\substack{q=p^k\\q\le e^{2a}}}
\frac{\log p}{\sqrt q}\,
\|v_0-\tau_{\log q}v_0\|_2^2\ge0,
\]

\(R_a\) is the source's bounded smooth-remainder operator, and \(\mathcal V_a\) is the source's explicit finite scalar counterterm. The prime sum has finitely many terms for each fixed \(a\).

## 2. Zero-extension identity — theorem

Define, for \(R\ge2a\),

\[
\boxed{
E_R(v)
=
\frac14\int_{-R}^{R}
\frac{\|v_0(\cdot+h)-v_0\|_{L^2(\mathbb R)}^2}{|h|}\,dh.
}
\]

The integral is nonnegative. Splitting the equivalent double integral into pairs \(x,y\in I\) and one point outside \(I\), we obtain the exact identity

\[
\boxed{
E_R(v)=
\frac14\int_I\int_I\frac{|v(x)-v(y)|^2}{|x-y|}\,dx\,dy
+\log R\|v\|_2^2
-\frac12\int_I\log(a^2-x^2)|v(x)|^2\,dx.
}
\]

### Proof

The integrand is invariant under swapping \(x,y\). The \(I\times I\) contribution is the original nonlocal difference kernel because \(|x-y|<2a\le R\).

For a fixed \(x\in I\), the contribution of outside points within distance \(R\) is

\[
\int_{\substack{y\notin I\\|x-y|<R}}\frac{dy}{|x-y|}
=
\int_{a}^{x+R}\frac{dy}{y-x}
+\int_{x-R}^{-a}\frac{dy}{x-y}
=
2\log R-\log(a^2-x^2).
\]

These outside-inside pairs occur twice in the full double integral, with global coefficient \(1/4\), producing \(\frac12[2\log R-\log(a^2-x^2)]|v(x)|^2\). This proves the identity.

Therefore at the canonical cutoff \(R=2a\),

\[
\boxed{
L_a(v)=E_{2a}(v)-\log(2a)\|v\|_2^2.
}
\]

**The logarithmic endpoint singularity is exactly the exterior part of a positive finite-range translation-difference energy.** No arbitrary metric or counterterm has been inserted.

## 3. Exact repaired completed form

Substitute the zero-extension identity into Suzuki's complete form:

\[
\boxed{
Q_W^a(v)
=
\underbrace{
E_{2a}(v)+E_{{\rm prime},a}(v)
}_{=:P_a(v)\ge0}
-
\left\langle
\left[
(\mathcal V_a+\log(2a))I+R_a
\right]v,v
\right\rangle.
}
\]

Define the bounded self-adjoint operator

\[
\boxed{
D_a=(\mathcal V_a+\log(2a))I+R_a.
}
\]

Then **exactly**

\[
\boxed{Q_W^a=P_a-D_a.}
\]

This sharpens the previous positive-part split: the positive parent \(P_a\) is a single canonical source-defined Dirichlet form, and \(D_a\) has no boundary singularity.

## 4. Fourier symbol and ultraviolet control

Under the unitary Fourier transform of the zero extension,

\[
\boxed{
E_R(v)=\int_{\mathbb R}m_R(\xi)|\widehat{v_0}(\xi)|^2\,d\xi,
}
\]

where

\[
\boxed{
m_R(\xi)=\int_0^R\frac{1-\cos(h\xi)}h\,dh
=\gamma+\log(R|\xi|)-\operatorname{Ci}(R|\xi|)
}
\]

for \(\xi\ne0\), and \(m_R(0)=0\).

The multiplier is nonnegative and nondecreasing in \(|\xi|\):

\[
\frac{d}{d|\xi|}m_R(\xi)
=\frac{1-\cos(R|\xi|)}{|\xi|}\ge0.
\]

Moreover \(m_R(\xi)=\log(R|\xi|)+\gamma+O((R|\xi|)^{-1})\) at large frequency. Consequently

\[
\int_{|\xi|\ge B}
|\widehat{v_0}(\xi)|^2\,d\xi
\le
\frac{E_R(v)}{m_R(B)}
\]

for \(B>0\).

### Independent consistency with Suzuki's Fourier formula

Suzuki (2.6) gives the equivalent interval-domain multiplier \(\log|\xi|+\gamma\) for \(L_a\).

The apparent extra \(\operatorname{Ci}(2a|\xi|)\) term in \(m_{2a}-\log(2a)\) vanishes **in the quadratic form on functions supported in \((-a,a)\)**: for \(R\ge2a\),

\[
\frac{d}{dR}
\int\operatorname{Ci}(R|\xi|)
|\hat v_0(\xi)|^2d\xi
=
\frac1R\Re\langle v_0,\tau_Rv_0\rangle=0,
\]

and the quantity tends to zero as \(R\to\infty\). Thus both Fourier formulas agree exactly. The zero-extension square and Suzuki's spectral log are the same operator form.

## 5. Closed form and compact resolvent

Start with \(C_c^\infty(I)\), and let \(\mathscr V_a\) be its completion under

\[
\|v\|_{\mathscr V_a}^2=\|v\|_2^2+E_{2a}(v).
\]

This is a closed nonnegative densely defined form. Its Fourier representation is a closed weighted \(L^2\) norm restricted to functions supported in \(\overline I\).

A sequence bounded in this form norm has uniformly bounded \(L^2\) mass, supports within a fixed compact interval, and uniformly small Fourier tails by the estimate above. Therefore it is uniformly translation-equicontinuous in \(L^2\). The Fréchet–Kolmogorov criterion gives compact embedding

\[
\boxed{
\mathscr V_a\hookrightarrow L^2(I)\quad\text{compactly}.
}
\]

The finite prime-edge energy is a bounded nonnegative form on \(L^2(I)\):

\[
0\le E_{{\rm prime},a}(v)\le4 S_a\|v\|_2^2,\qquad
S_a=\sum_{q\le e^{2a}}\frac{\Lambda(q)}{\sqrt q}.
\]

It preserves the closed-form domain and compact embedding. Hence the self-adjoint operator \(\mathbf P_a\) of \(P_a\) has

\[
\boxed{
0\le\lambda_1(\mathbf P_a)\le\lambda_2(\mathbf P_a)\le\cdots,\qquad
\lambda_n(\mathbf P_a)\to+\infty.
}
\]

In particular \((\mathbf P_a+I)^{-1}\) is compact.

This provides an elementary constructive recovery of finite-interval spectral discreteness already known from Connes–Consani–Moscovici (as cited by Suzuki), **not an independently new priority claim**.

## 6. Explicit quantitative eigenvalue lower bound

A stronger elementary estimate is available, independent of horizon and prime data.

Let \(B>0\), and let

\[
T_{B,I}
=
1_I\mathcal F^{-1}1_{[-B,B]}\mathcal F1_I.
\]

This is a positive trace-class time-band-limiting operator with

\[
\boxed{
\operatorname{Tr}T_{B,I}
=
\frac{|I|\cdot 2B}{2\pi}
=
\frac{2aB}{\pi}.
}
\]

Take an arbitrary \(n\)-dimensional subspace \(W\subset\mathscr V_a\) and any orthonormal basis \(\{f_1,\ldots,f_n\}\). Then

\[
\sum_{j=1}^{n}
\int_{|\xi|\le B}|\hat f_j(\xi)|^2d\xi
=
\sum_{j=1}^n\langle T_{B,I}f_j,f_j\rangle
\le\frac{2aB}{\pi}.
\]

At least one normalized \(f_j\) therefore has low-frequency mass at most \(2aB/(\pi n)\). Its \(P_a\)-energy obeys

\[
P_a(f_j)\ge E_{2a}(f_j)
\ge
m_{2a}(B)
\left(1-\frac{2aB}{\pi n}\right).
\]

The min–max principle then gives, for every \(n\ge1\) and \(0<B<\pi n/(2a)\),

\[
\boxed{
\lambda_n(\mathbf P_a)
\ge
m_{2a}(B)
\left(1-\frac{2aB}{\pi n}\right).
}
\]

Choose \(B=\pi n/(4a)\). Since \(2aB=\pi n/2\),

\[
\boxed{
\lambda_n(\mathbf P_a)
\ge\frac12\left[
\gamma+\log\frac{\pi n}{2}
-\operatorname{Ci}\!\left(\frac{\pi n}{2}\right)
\right].
}
\]

This lower bound is **uniform in \(a\)** and independent of the prime source. In particular,

\[
\boxed{
\lambda_n(\mathbf P_a)\ge\frac12\log n-O(1).
}
\]

### What this does not say

The bounded negative correction \(D_a\) has norm depending on \(a\), and may grow rapidly with the prime cutoff. A lower bound on the ordered high eigenvalues does not prove \(\mathbf P_a-D_a\ge0\). It only shows that every possible negative mode lies in a finite-dimensional low-energy range at each **fixed** \(a\).

## 7. Exact fixed-horizon finite-dimensional Feshbach reduction

Fix \(a>0\) and \(\varepsilon>0\). Put \(b_a=\|D_a\|\).

Let

\[
E_a=1_{[0,b_a+\varepsilon]}(\mathbf P_a),
\qquad F_a=I-E_a.
\]

Because \(\mathbf P_a\) has compact resolvent,

\[
\boxed{\operatorname{rank}E_a<\infty.}
\]

On the high-energy subspace,

\[
\boxed{
F_a(\mathbf P_a-D_a)F_a\succeq\varepsilon F_a.
}
\]

Thus the high block has a positive bounded inverse on \(F_aL^2(I)\). Define the exact finite-dimensional effective operator on \(E_aL^2(I)\):

\[
\boxed{
\mathscr S_a=
E_a(\mathbf P_a-D_a)E_a
-
E_aD_aF_a
\bigl[F_a(\mathbf P_a-D_a)F_a\bigr]^{-1}
F_aD_aE_a.
}
\]

The Schur/Feshbach form identity and the positive high block give

\[
\boxed{
Q_W^a\succeq0
\quad\Longleftrightarrow\quad
\mathscr S_a\succeq0.
}
\]

This is an **exact**, non-circular, finite-dimensional reduction at each fixed horizon: the projection, inverse, coefficients and residual all come from the source-defined \(\mathbf P_a,D_a\).

It is **not** a proof of RH. The rank and effective matrix change with \(a\), and their positivity has not been established uniformly.

## 8. Explicit finite-rank upper bound for the low sector

For \(n\ge2\), the classical integration-by-parts estimate gives

\[
\left|\operatorname{Ci}(\tfrac{\pi n}{2})\right|
\le\frac{4}{\pi n}<1.
\]

Thus

\[
\boxed{
\lambda_n(\mathbf P_a)
\ge\frac12\left[
\gamma+\log(\tfrac{\pi n}{2})-1
\right].
}
\]

In particular all indices satisfying

\[
\boxed{
n>\frac2\pi\exp(2\|D_a\|+1-\gamma)
}
\]

lie strictly above \(\|D_a\|\) and hence outside the low-energy spectral sector (for a strictly positive chosen margin use \(\|D_a\|+\varepsilon\) in the exponent). This is a quantitative finite-rank bound, possibly very large, independent of unproved zero-location estimates.

## 9. Independent finite controls

The script \`scripts/rh_zero_extension_feshbach.py\` checks the exact zero-extension identity for:

1. \(v=1_I\), with nontrivial boundary log integral;
2. \(v(x)=x\,1_I(x)\), with independently derived translation-distance polynomial;
3. several interval widths \(a\);
4. the exact Fourier symbol and quantitative spectral bound at logarithmically increasing mode indices.

The polynomial examples are finite-energy functions outside the smooth core; the identity extends to them by its positive quadratic form. Numerical calibrations are **not** proofs of compactness, the min–max bound, or RH.

## 10. New precise proof wall

The earlier cubical shortcut tried to invent a positive parent and force its Schur complement to be Weil. That was underdetermined and failed the UV and boundary tests.

The corrected source-derived object is

\[
\boxed{
\mathscr S_a=
E_aQ_W^aE_a
-
E_aD_aF_a(F_aQ_W^aF_a)^{-1}F_aD_aE_a,
}
\]

where the high block is already positive by an unconditional spectral theorem.

The RH-bearing question is now exactly

\[
\boxed{
\mathscr S_a\succeq0
\quad\text{for every }a>0.
}
\]

Proving this with a uniform arithmetic/carry estimate would prove RH. There is no such proof in this note.

The explicit bound shows why compactness alone is not enough: \(\|D_a\|\) drives an exponentially large possible low-mode budget as \(a\) grows. Any honest proof must control that dependence, not replace it with a finite numerical grid.

## Claim ledger

**DISCLOSED:** exact zero-extension formula; positive corrected \(P_a-D_a\) decomposition; Fourier log symbol; elementary closedness and compactness proof; uniform explicit ordered-eigenvalue lower bound; exact finite-dimensional Feshbach equivalence; quantitative low-sector rank cap.

**CORROBORATED:** the source Fourier form and finite spectral discreteness are already in Suzuki/Connes–Consani–Moscovici; the present proof provides a convenient independent realization, not priority over their theorems.

**UNVERIFIED:** an all-horizon positive bound for the finite effective \(\mathscr S_a\), and a uniform arithmetic mechanism to provide it.

**RH:** OPEN.


---

## Addendum: unconditional finite negative-index bound

Because \(D_a\) is bounded self-adjoint, the min–max principle also gives for the full localized Weil operator

\[
\boxed{
\lambda_n(Q_W^a)
\ge
\lambda_n(\mathbf P_a)-\|D_a\|
\ge
\frac12\left[
\gamma+\log\frac{\pi n}{2}
-\operatorname{Ci}\!\left(\frac{\pi n}{2}\right)
\right]-\|D_a\|.
}
\]

In particular, set \(b_a=\|D_a\|\). For \(n\ge2\), the elementary bound \(|\operatorname{Ci}(\pi n/2)|<1\) gives

\[
\lambda_n(Q_W^a)
\ge
\frac12\left[\gamma+\log(\pi n/2)-1\right]-b_a.
\]

Consequently every eigenvalue with index

\[
\boxed{
n>\max\left\{1,\frac2\pi e^{2b_a+1-\gamma}\right\}
}
\]

is strictly positive, and thus the nonpositive Morse index is finite with an explicit source-computable upper bound. This is **unconditional**, holds for every finite \(a\), and is distinct from (far weaker than) the RH assertion that the negative index is **zero**.

The coefficient \(b_a\) generally grows with the cutoff. This result is not a uniform finite-rank RH certificate as \(a\to\infty\).
