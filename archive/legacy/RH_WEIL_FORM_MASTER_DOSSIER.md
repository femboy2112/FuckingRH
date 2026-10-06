# The Weil-Form Program for the Riemann Hypothesis

## A ten-round Aletheia triangulation dossier

**Status:** research program and derived intermediate results; **not a proof of RH**  
**Date:** 25 August 2026  
**Primary object:** Weil's Hermitian form for the completed Riemann zeta function  
**Central compression:**

\[
\boxed{\mathrm{RH}\iff W\succeq 0.}
\]

---

## Abstract

This dossier consolidates the recent Schrödinger--Archimedean / Weil-form work into one self-contained mathematical program. The organizing claim is that the principal spectral, geometric, combinatorial, and analytic approaches to the Riemann hypothesis converge on one infinite-dimensional Hermitian form and one universal sign:

\[
W(f,f)\ge 0\qquad\text{for every admissible test function }f.
\]

The Guinand--Weil explicit formula computes this same form from four sources: nontrivial zeros, the pole, the Archimedean Gamma factor, and prime powers. A zero on the critical line contributes a positive rank-one atom. An off-line functional-equation pair contributes a signature-\((1,1)\) block. Consequently, positivity of the full form is equivalent to RH.

The dossier then performs ten triangulation rounds. Each round uses a different constraint surface: explicit-formula algebra, finite-field intersection theory, total positivity, Paley--Wiener geometry, inertia and moments, parity and Loewner matrices, prolate boundary leakage, explicit positive-type packets, Witt/necklace deformation theory, and a final integrated closure theorem. The goal is not to multiply equivalent formulations. It is to isolate proof-bearing inequalities, extract weaker theorems, kill seductive but non-discriminating routes, and specify the exact next probes.

The strongest concrete outputs are:

1. an exact formula for the positive and negative eigenvalues contributed by one off-line zero pair at finite Paley--Wiener bandwidth;
2. a two-dimensional resolution law in zero height and horizontal depth;
3. a parity-crossing theorem reducing the Connes--van Suijlekom simplicity/evenness condition to one scalar inequality;
4. a parity decomposition of the finite Weil matrices into two Loewner-type matrices;
5. a total-positive Archimedean model in which the simple even ground-state theorem is already unconditional;
6. a radical-cut identity converting the Weil-minimizer problem into exterior leakage geometry;
7. a functional-calculus criterion sufficient to transfer the prolate ground state to the Weil ground state;
8. an explicit hyperbolic-tent family of positive-type Weil tests and pole-neutral combinations;
9. a Witt/necklace factorization of the prime-support/multiplicity deformation, exposing scaled zero spectra \(\rho/n\);
10. a compressed quartic trace inequality that would improve the new unconditional two-thirds theorem.

Publication-level novelty of results labeled **Derived here** has not been established. Every such statement is supplied with a proof or a precise derivation boundary.

---

# Epistemic legend

- **External theorem:** established in a cited primary source.
- **Derived here:** proved in this dossier from stated hypotheses; novelty unverified.
- **Observed:** obtained in the accompanying computational program; not a theorem.
- **Conjectured target:** a proposed statement whose proof would move the program.
- **Refuted:** killed by an exact counterargument, calculation, or incompatible asymptotic.
- **Boundary:** the point at which a conclusion would become equivalent to RH or stronger.
- **Dark:** no present discriminator reaches the claim.

Conclusions inherit the weakest load-bearing premise.

---

# Source and provenance map

## Primary mathematical sources

- **[R1]** A. Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, arXiv:2602.04022 (2026).  
  <https://arxiv.org/abs/2602.04022>
- **[R2]** A. Connes and W. D. van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*, arXiv:2511.23257 (2025).  
  <https://arxiv.org/abs/2511.23257>
- **[R3]** A. Connes, C. Consani, and H. Moscovici, *Zeta Zeros and Prolate Wave Operators*, arXiv:2310.18423.  
  <https://arxiv.org/abs/2310.18423>
- **[R4]** A. Groskin, *A Finite Guinand--Weil Dictionary and Archimedean Tail Order for the Truncated Weil Quadratic Form*, arXiv:2607.02828 (2026).  
  <https://arxiv.org/abs/2607.02828>
- **[R5]** L. Alpöge and R. Furman, *More Than Two Thirds of the Zeta Zeros Are Simple and on the Critical Line*, arXiv:2608.13637 (2026).  
  <https://arxiv.org/abs/2608.13637>
- **[R6]** A. Connes and C. Consani, *Weil Positivity and Trace Formula, the Archimedean Place*, arXiv:2006.13771.  
  <https://arxiv.org/abs/2006.13771>
- **[R7]** A. Connes and C. Consani, *The Arithmetic Site*, arXiv:1405.4527.  
  <https://arxiv.org/abs/1405.4527>
- **[R8]** A. Connes and C. Consani, *Geometry of the Arithmetic Site*, and the Riemann--Roch strategy, arXiv:1805.10501.  
  <https://arxiv.org/abs/1805.10501>
- **[R9]** O. Amini and M. Piquerez, *Hodge Theory for Tropical Varieties*, arXiv:2007.07826.  
  <https://arxiv.org/abs/2007.07826>
- **[R10]** J.-L. Nicolas, *Small Values of the Euler Function and the Riemann Hypothesis*, arXiv:1202.0729.  
  <https://arxiv.org/abs/1202.0729>
- **[R11]** A. Connes, C. Consani, and M. Marcolli, *The Weil Proof and the Geometry of the Adeles Class Space*, arXiv:math/0703392.  
  <https://arxiv.org/abs/math/0703392>
- **[R12]** Clay Mathematics Institute, *Riemann Hypothesis*.  
  <https://www.claymath.org/millennium/riemann-hypothesis/>

## Internal research artifacts

- **[I1]** `SCHRODINGER_ARCHIMEDEAN_DOSSIER(1)(1).md`, especially §§17--70.
- **[I2]** `coherent_truncation.py`.
- **[I3]** `local_patch.py` and `local_patch.log`.
- **[I4]** prior scripts catalogued in [I1]: Weil-form matrices, off-line poisoning, Connes minimizer reproduction, gap probes, Loewner/commutator hunts, and Archimedean checks.
- **[I5]** `rh_master_checks.py`, supplied with this dossier, containing exact or high-precision checks of several derived identities.

The internal experiments are used only as **Observed** evidence. Known zero ordinates were used for calibration and scoring, not as inputs to the prime--pole--Gamma matrices.

---

# Part I. The common mathematical object

## 1. Completed zeta and centered spectral coordinates

Define

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma\!\left(\frac s2\right)\zeta(s).
\]

Then

\[
\xi(s)=\xi(1-s),
\]

and \(\xi\) is entire with zeros exactly at the nontrivial zeros of \(\zeta\).

Center the functional equation by setting

\[
\Xi(z)=\xi\!\left(\frac12+iz\right).
\]

For a zero

\[
\rho=\beta+i\gamma,
\]

define

\[
\boxed{
z_\rho=\frac{\rho-\frac12}{i}
=\gamma-i\left(\beta-\frac12\right).
}
\]

Then

\[
\Xi(z_\rho)=0,
\]

and RH is exactly

\[
\boxed{z_\rho\in\mathbb R\quad\text{for every }\rho.}
\]

This coordinate must remain complex until RH is proved. Any unconditional formula written as a sum over \(h(\gamma)\) rather than \(h(z_\rho)\) has silently projected the zeros onto the critical line.

---

## 2. Fourier conventions and positive-type tests

Use

\[
h(z)=\int_{\mathbb R}g(u)e^{izu}\,du.
\]

Let

\[
\widetilde f(u)=\overline{f(-u)}
\]

and set

\[
g=f*\widetilde f.
\]

If

\[
F(z)=\widehat f(z)=\int_{\mathbb R}f(u)e^{izu}\,du,
\]

then

\[
h(z)=F(z)\overline{F(\bar z)}.
\]

For real \(r\),

\[
\boxed{h(r)=|F(r)|^2\ge0.}
\]

Off the real axis this is not an ordinary modulus square. That failure is precisely where an off-line zero creates an indefinite contribution.

---

## 3. Guinand--Weil explicit formula

For an admissible even test function, one normalization of the explicit formula is

\[
\boxed{
\begin{aligned}
\sum_\rho h(z_\rho)
={}&h(i/2)+h(-i/2)\\
&+\frac1{2\pi}\int_{\mathbb R}h(r)
\left[
\Re\psi_\Gamma\!\left(\frac14+\frac{ir}{2}\right)-\log\pi
\right]dr\\
&-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(\log n).
\end{aligned}}
\tag{GW}
\]

Here:

- \(\Lambda(n)\) is the von Mangoldt function;
- \(\psi_\Gamma=\Gamma'/\Gamma\) is the digamma function;
- \(h(\pm i/2)\) represents the pole/trivial cohomology contribution;
- the integral is the real-place or Archimedean factor;
- the final sum is supported on prime powers.

Fourier conventions can move factors of \(2\pi\), but not the structure.

---

## 4. Weil's Hermitian form

For test functions \(f,g\), define

\[
\boxed{
W(f,g)
=
\sum_\rho m_\rho
\widehat f(z_\rho)
\overline{\widehat g(\overline{z_\rho})}.
}
\tag{W}
\]

The explicit formula evaluates the same form from primes, pole, and infinity.

With our sign convention, Weil's criterion is

\[
\boxed{
\mathrm{RH}
\iff
W(f,f)\ge0
\quad\text{for every admissible }f.
}
\tag{WC}
\]

Some papers absorb a global minus sign and state negative definiteness. Nothing substantive depends on that choice.

---

## 5. The local zero block

Take a finite real test basis \(f_1,\ldots,f_d\), and let

\[
v(z_\rho)=
\left(
\widehat f_1(z_\rho),\ldots,
\widehat f_d(z_\rho)
\right)=a+ib,
\qquad a,b\in\mathbb R^d.
\]

Pair \(\rho\) with \(1-\bar\rho\). Their matrix contribution is

\[
\boxed{
B_\rho=2m_\rho(aa^{\mathsf T}-bb^{\mathsf T}).
}
\tag{B}
\]

- If \(\beta=1/2\), then \(b=0\), and \(B_\rho\) is positive rank one.
- If \(\beta\ne1/2\) and \(a,b\) are independent, \(B_\rho\) has signature \((1,1)\).

Thus RH is not merely associated with positivity. It is the statement that every local zero block is positive rather than hyperbolic.

---

# The ten-round marathon

---

# Round 1 — The Hermitian core and its local curvature

## Target

Recover the exact local mechanism by which an off-line zero produces a negative direction, and identify the optimal sensitivity statistic for finite test families.

## 1.1 Exact eigenvalues of a rank-two off-line block

Let

\[
B=2(aa^{\mathsf T}-bb^{\mathsf T}).
\]

Set

\[
A=\|a\|^2,\qquad B_0=\|b\|^2,\qquad C=a\cdot b.
\]

The two potentially nonzero eigenvalues are

\[
\boxed{
\lambda_\pm
=(A-B_0)\pm\sqrt{(A+B_0)^2-4C^2}.
}
\tag{1.1}
\]

If \(a,b\) are linearly independent, then

\[
AB_0-C^2>0,
\]

so

\[
\lambda_-<0<\lambda_+.
\]

This is the exact signature-\((1,1)\) statement.

## 1.2 Small horizontal displacement

Let a zero move from the line to

\[
z=\gamma+i\delta
\]

in centered coordinates. Let the real evaluation curve be

\[
v(t)\in\mathbb R^d.
\]

Analytic continuation gives

\[
v(\gamma+i\delta)
=v_0+i\delta v_1-\frac{\delta^2}{2}v_2+O(\delta^3),
\]

where

\[
v_0=v(\gamma),\qquad v_1=v'(\gamma).
\]

Substituting into (1.1) yields:

> **Derived theorem 1.1 — projective-curvature onset.**
>
> \[
> \boxed{
> \lambda_-(\delta)
> =-2\delta^2
> \left\|P_{v_0^\perp}v_1\right\|^2
> +O(\delta^4).
> }
> \tag{1.2}
> \]

### Interpretation

The detector is blind to the component of \(v'(\gamma)\) parallel to \(v(\gamma)\). A horizontal displacement is detected only when it rotates the evaluation line in projective space.

Define the **off-line projective curvature**

\[
\boxed{
\kappa_{\rm off}(\gamma)
=\left\|P_{v(\gamma)^\perp}v'(\gamma)\right\|.
}
\tag{1.3}
\]

Then the leading negative curvature is

\[
-2\delta^2\kappa_{\rm off}(\gamma)^2.
\]

## 1.3 Proof

Write

\[
a=v_0+O(\delta^2),\qquad b=\delta v_1+O(\delta^3).
\]

Decompose

\[
v_1=\alpha v_0+v_1^\perp.
\]

The negative eigenvalue of \(aa^{\mathsf T}-bb^{\mathsf T}\) is produced only by the component of \(b\) transverse to \(a\); its leading value is

\[
-\delta^2\|v_1^\perp\|^2.
\]

Restoring the outer factor \(2\) gives (1.2).

## 1.4 What this changes

Earlier numerical poisoning used generic bump bases and found a \(\delta^2\) onset. This theorem explains the coefficient and tells us how to improve the detector.

### New probe design

Choose a pole-neutral test family and maximize

\[
\int_T^{2T}\kappa_{\rm off}(\gamma)^2\,d\gamma
\]

subject to normalization and support constraints.

### Acceptance criteria

- **Pass:** the optimized basis detects a synthetic off-line pair with a negative eigenvalue matching the coefficient in (1.2).
- **Mutation control:** replace the analytic evaluation curve by one with \(v'\parallel v\); the quadratic negative term must vanish.
- **Failure:** the measured onset is basis-conditioning noise and does not scale as \(-2\delta^2\kappa_{\rm off}^2\).

## Round 1 verdict

**Disclosed:** off-line pairs are locally hyperbolic.  
**Derived here:** the exact local sensitivity is projective curvature.  
**Roadblock:** one negative block can be swamped by many positive on-line atoms; local sensitivity alone does not prove global indefiniteness at a fixed finite resolution.

---
# Round 2 — Why the function-field proof works, and what Wall 2 actually demands

## Target

Separate the exact finite-field source of positivity from analogies that merely restate it, then specify what an arithmetic replacement over \(\mathbb Z\) would have to prove.

## 2.1 The finite-field mechanism

Let \(C/\mathbb F_q\) be a smooth projective curve, and let \(F\) denote Frobenius. On the surface

\[
C\times_{\mathbb F_q}C,
\]

correspondences define divisor classes and act on \(H^1(C)\). The key quadratic form is an intersection or degree form. For an elliptic-curve model, one sees the entire mechanism in

\[
\boxed{
\deg(m+nF)=m^2+a_pmn+qn^2.
}
\tag{2.1}
\]

The cross term can tilt the bowl, but degree is geometrically nonnegative:

\[
\deg(m+nF)\ge0
\qquad\text{for all }m,n.
\]

Hence the discriminant cannot be positive:

\[
a_p^2-4q\le0.
\]

The Frobenius eigenvalues therefore have modulus \(\sqrt q\), which is the Riemann hypothesis for the curve.

The high-dimensional version uses:

- a cohomology theory constructed independently of the zeta zeros;
- a Frobenius action;
- a Lefschetz trace formula;
- a polarization/Rosati involution;
- Hodge-index or Castelnuovo--Severi negativity on primitive cycles.

The sign precedes the zero-location theorem. That is the noncircular pattern.

## 2.2 What is missing over \(\mathbb Z\)

The analogous desired package is:

\[
X=\overline{\operatorname{Spec}\mathbb Z}_{/\mathbb F_1},
\qquad
S=X\times_{\mathbb F_1}X,
\]

with:

1. prime/Frobenius correspondences whose primitive periods are \(\log p\);
2. an Archimedean component producing
   \[
   \Re\psi_\Gamma\!\left(\frac14+\frac{it}{2}\right)-\log\pi;
   \]
3. an independently constructed \(H^1_{\rm abs}(X)\);
4. primitive middle cohomology
   \[
   H^2_{\rm prim}(S)(1)
   \simeq
   H^1_{\rm abs}(X)\widehat\otimes\overline{H^1_{\rm abs}(X)};
   \]
5. an absolute Lefschetz--Riemann--Roch formula;
6. a Hodge--Riemann polarization yielding
   \[
   -(D,D)=\operatorname{Tr}(T_DT_D^*)\ge0.
   \]

Arithmetic-site and scaling-site constructions supply significant parts of the correspondence/orbit scaffolding [R7, R8]. Tropical Hodge theory supplies real positivity theorems for smooth projective tropical varieties [R9]. What is not known is a comparison placing the Connes--Consani arithmetic square inside a category where those theorems apply and where the Gamma factor is represented correctly.

## 2.3 An index theorem is not enough

A recurrent overreach is:

\[
Q_W(f)=\operatorname{ind}D_f
\quad\Longrightarrow\quad
Q_W(f)\ge0.
\]

This is false. An index is

\[
\operatorname{ind}D_f
=\dim\ker D_f^+-\dim\ker D_f^-,
\]

and may have either sign.

A valid geometric solution requires at least one additional theorem:

### Route A: vanishing

\[
\ker D_f^-=0
\quad\Longrightarrow\quad
\operatorname{ind}D_f=\dim\ker D_f^+\ge0.
\]

### Route B: polarized trace

\[
Q_W(f)=\operatorname{Tr}_\tau(T_fT_f^*)\ge0.
\]

### Route C: Hodge sign

\[
(D,D)\le0
\quad\text{on primitive classes},
\]

so that

\[
-(D,D)\ge0.
\]

Thus Wall 2 consists of two subwalls:

\[
\boxed{
\text{Lefschetz/index identity}
+
\text{independent polarization or vanishing}.
}
\tag{2.2}
\]

## 2.4 What \(\zeta(-1)=-1/12\) does and does not show

The ordinary series

\[
1+2+3+\cdots
\]

has positive terms and diverges to \(+\infty\), while its zeta-regularized value is

\[
\zeta(-1)=-\frac1{12}.
\]

Therefore zeta regularization is not a positivity-preserving cardinality operation.

This proves:

\[
\boxed{
\text{finite regularized value}
\ne
\text{nonnegative geometric count}.
}
\]

It does **not** prove that no positive Archimedean Hilbert geometry can exist. A positive operator may possess a renormalized trace of either sign after divergent counterterms are subtracted. The lesson is narrower:

> Do not use a regularized scalar trace as the source of Hodge positivity.

## 2.5 The Archimedean obstruction is not uniformly negative

Groskin proves that the omitted high-frequency Archimedean tail of the finite Weil matrix is a positive Cauchy--Stieltjes Gram increment and is strictly totally positive in the natural frequency order [R4]. Thus the distant Gamma tail is not the enemy. It is a positive regularizer.

The sign problem is concentrated in:

- the low-frequency Archimedean core;
- the pole sector;
- the coupling of that core to primitive-prime oscillations.

A more accurate decomposition is

\[
\boxed{
Q_W
=Q_{\infty,\mathrm{tail}}^+
+Q_{\mathrm{repeat}}
+Q_{\mathrm{compact/primitive}}.
}
\tag{2.3}
\]

The first term is known positive. A possible theorem is a relative-form bound

\[
\boxed{
|Q_{\mathrm{compact/primitive}}(f)|
\le(1-\varepsilon)
\bigl[Q_{\infty,\mathrm{tail}}^+(f)+Q_{\mathrm{repeat}}(f)\bigr]
+C\|P_Kf\|^2.
}
\tag{2.4}
\]

This would reduce global positivity to a controlled compact sector.

## Round 2 verdict

**External theorem:** finite-field positivity is supplied by a genuine polarized geometry.  
**Correction:** a Fredholm index alone remains signed.  
**Correction:** \(-1/12\) blocks naive cardinality, not all positive geometry.  
**New avenue:** isolate and dominate only the compact prime--Archimedean core, since the remote Archimedean tail is already positive.

---

# Round 3 — Archimedean total positivity, Loewner matrices, and a solved model of Wall 3

## Target

Exploit the exact finite matrix structure and Groskin's total-positive tail to obtain a complete weaker model in which the Connes ground-state mechanism can be proved.

## 3.1 Divided-difference matrices

The finite Weil matrices studied by Connes--van Suijlekom and Groskin have the form

\[
\boxed{
(Q_\psi)_{mn}
=
\begin{cases}
\dfrac{\psi(m)-\psi(n)}{m-n},&m\ne n,\\[2mm]
\psi'(m),&m=n,
\end{cases}
}
\tag{3.1}
\]

for an odd source function \(\psi\), after an appropriate scaling of the integer frequency indices.

This is a Loewner matrix. If \(\psi\) were operator monotone on the relevant interval, every such matrix would be positive. Complete operator monotonicity is likely stronger than RH needs, but finite matrix monotonicity gives a ladder of weaker results:

\[
\begin{array}{ccl}
\text{order }1&:&\psi'\ge0,\\
\text{order }2&:&\text{every }2\times2\text{ Loewner minor is nonnegative},\\
\text{order }n&:&Q_{\psi,n}\succeq0,\\
\text{all orders}&:&\psi\text{ is Pick/operator monotone}.
\end{array}
\]

Each finite-order theorem is a genuine finite compression of Weil positivity.

## 3.2 Total-positive Archimedean tail

Let

\[
R_{T_1,T_2}
=Q_{\infty,T_2}-Q_{\infty,T_1}
\]

be the omitted Gamma-tail increment between two frequency cutoffs. Groskin proves that it is a strictly totally positive Cauchy--Stieltjes matrix [R4]. It is also real symmetric and centrosymmetric.

For a strictly totally positive \(n\times n\) matrix, the Gantmacher--Krein oscillation theorem gives:

- all eigenvalues are positive and simple;
- the eigenvector for the \(k\)-th largest eigenvalue has exactly \(k-1\) sign changes.

For odd dimension \(n=2N+1\), the smallest eigenvector has \(2N\) sign changes.

Because the matrix commutes with reversal, each simple eigenvector is either even or odd. An even vector has an even number of sign changes; an odd vector has an odd number after zeros are removed. Therefore:

> **Derived theorem 3.1 — Archimedean-tail parity.**  
> The smallest eigenvalue of \(R_{T_1,T_2}\) is simple and its eigenvector is even.

Shift by the smallest eigenvalue:

\[
\widetilde R
=R_{T_1,T_2}-\lambda_{\min}I.
\]

Then \(\widetilde R\succeq0\) has a one-dimensional even kernel. The Connes--van Suijlekom real-zero theorem [R2] applies to the corresponding finite entire function.

Hence:

\[
\boxed{
\text{Wall 3 is already completely solved for the pure total-positive Archimedean tail.}
}
\]

This is a real weaker proof, not a heuristic.

## 3.3 Perturbative total-positive domination

Write the full finite matrix as

\[
Q=R+K,
\]

where \(R\) is a centrosymmetric strictly totally positive reference matrix and \(K\) is the remaining pole/prime/core perturbation.

Let the two smallest eigenvalues of \(R\) be

\[
r_1<r_2,
\]

with \(r_1\) even and \(r_2\) odd.

By Weyl's eigenvalue inequalities,

\[
\lambda_1^+(Q)\le r_1+\|K\|,
\]

and

\[
\lambda_1^-(Q)\ge r_2-\|K\|.
\]

Thus:

> **Derived theorem 3.2 — total-positive parity certificate.**  
> If
> \[
> \boxed{2\|K\|<r_2-r_1,}
> \tag{3.2}
> \]
> then the full ground state is simple and even.

This condition is probably too strong globally, but it gives a calibrated failure metric:

\[
\mathfrak D_{\rm TP}
=\frac{2\|K\|}{r_2-r_1}.
\]

- \(\mathfrak D_{\rm TP}<1\): theorem closes.
- \(\mathfrak D_{\rm TP}\gg1\): the known tail mechanism cannot dominate the core.

## 3.4 Pick representation as Wall-2 target

A Pick function \(\psi\) admits a representation whose divided-difference kernel is a positive mixture of Cauchy kernels. The Groskin tail already has precisely this structure.

A complete analytic Wall-2 solution could therefore take the form:

\[
\boxed{
\psi_{\rm full}(z)
=az+b+
\int_{\mathbb R}
\left(
\frac1{t-z}-\frac{t}{1+t^2}
\right)d\mu(t),
\qquad d\mu\ge0.
}
\tag{3.3}
\]

The prime and low-frequency terms would have to combine into the same positive measure, not merely into an identity.

This is probably stronger than necessary. A more realistic sequence is to prove matrix monotonicity at increasing finite orders, obtaining a hierarchy of positive finite Weil forms.

## Round 3 verdict

**External theorem:** the omitted Archimedean tail is strictly totally positive.  
**Derived here:** its ground state is simple and even; its finite transform is therefore real-rooted.  
**New certificate:** total-positive reference gap versus core norm.  
**Roadblock:** the low core may be much larger than the smallest tail gap.  
**Long-range avenue:** represent the full source as a Pick function or prove finite-order matrix monotonicity.

---

# Round 4 — Exact finite-band geometry and the two-dimensional resolution cone

## Target

Determine exactly how finite support resolves a zero's height and its horizontal displacement from the critical line.

## 4.1 Paley--Wiener reproducing kernel

Let \(PW_A\) be the Paley--Wiener space of entire functions of exponential type at most \(A\), square-integrable on the real axis. Its reproducing kernel is

\[
\boxed{
K_A(z,w)
=\frac{\sin A(z-\bar w)}{\pi(z-\bar w)}.
}
\tag{4.1}
\]

Take an off-line centered zero

\[
z=\gamma-i\delta,
\qquad
\delta=\beta-\frac12.
\]

Let the complex evaluation vector be

\[
k_z=a+ib
\]

in the realification of \(PW_A\).

The kernel gives

\[
K_A(z,z)
=\frac{\sinh(2A\delta)}{2\pi\delta},
\]

and

\[
K_A(z,\bar z)=\frac A\pi.
\]

The second quantity is real, and it implies

\[
a\perp b.
\]

Moreover,

\[
\|a\|^2
=\frac12
\left[
\frac{\sinh(2A\delta)}{2\pi\delta}
+\frac A\pi
\right],
\]

\[
\|b\|^2
=\frac12
\left[
\frac{\sinh(2A\delta)}{2\pi\delta}
-\frac A\pi
\right].
\]

## 4.2 Exact off-line eigenvalues

The block \(2(aa^*-bb^*)\) therefore has exact eigenvalues

\[
\boxed{
\lambda_+
=\frac A\pi
\left(1+\frac{\sinh u}{u}\right),
}
\tag{4.2}
\]

\[
\boxed{
\lambda_-
=\frac A\pi
\left(1-\frac{\sinh u}{u}\right)<0,
}
\tag{4.3}
\]

where

\[
\boxed{u=2A|\delta|.}
\tag{4.4}
\]

The trace is independent of depth:

\[
\boxed{
\lambda_++\lambda_-=\frac{2A}{\pi}.
}
\tag{4.5}
\]

Thus the first moment cannot see horizontal displacement. Depth appears only in the splitting.

## 4.3 Shallow-pair asymptotics

Since

\[
\frac{\sinh u}{u}
=1+\frac{u^2}{6}+O(u^4),
\]

we obtain

\[
\lambda_+
=\frac{2A}{\pi}
+\frac{Au^2}{6\pi}+O(Au^4),
\]

and

\[
\boxed{
\lambda_-
=-\frac{Au^2}{6\pi}+O(Au^4)
=-\frac{2A^3\delta^2}{3\pi}+O(A^5\delta^4).
}
\tag{4.6}
\]

At \(\delta=0\), the pair limits to eigenvalues

\[
\left\{\frac{2A}{\pi},0\right\},
\]

which is exactly the spectrum of a double on-line zero block.

This proves rigorously that shallow off-line pairs are finite-band perturbations of double on-line zeros.

## 4.4 Relative negative signal

Define

\[
R(u)=\frac{|\lambda_-|}{\lambda_+}.
\]

Then

\[
\boxed{
R(u)=\frac{\sinh u-u}{\sinh u+u}
\sim\frac{u^2}{12}.
}
\tag{4.7}
\]

A finite-band detector sees a near-line zero only quadratically in

\[
A\left|\beta-\frac12\right|.
\]

## 4.5 Vertical resolution

The mean zero spacing near height \(T\) is
\[
\Delta\gamma
\sim\frac{2\pi}{\log(T/2\pi)}.
\]

A type-\(A\) function has a characteristic stable interpolation scale \(\pi/A\). Equating these gives

\[
A\sim\frac12\log\frac{T}{2\pi}.
\]

The internal experiments observed the equivalent prime-cutoff law

\[
x=e^{2A}\sim\frac{T}{2\pi}.
\]

This is a **conditioning horizon**, not an existence theorem: multiplying a Paley--Wiener function by a polynomial can force any finite set of zeros at fixed bandwidth, but the norm and interpolation condition number explode.

## 4.6 The two-dimensional resolution cone

To detect height and depth simultaneously, one needs roughly

\[
\boxed{
A_{\rm useful}
\gtrsim
\max\left\{
\frac12\log\frac{T}{2\pi},
\frac{c}{|\beta-\frac12|}
\right\}.
}
\tag{4.8}
\]

In prime-cutoff coordinates,

\[
\boxed{
x_{\rm useful}
\gtrsim
\max\left\{
\frac{T}{2\pi},
\exp\!\left(\frac{2c}{|\beta-\frac12|}\right)
\right\}.
}
\tag{4.9}
\]

This is a decisive explanation for the finite-computation barrier. A zero can be vertically accessible yet horizontally invisible.

## 4.7 Depth moments

Normalize the pair eigenvalues by \(A/\pi\):

\[
\Lambda_\pm=1\pm s,
\qquad
s=\frac{\sinh u}{u}\ge1.
\]

Their moments are

\[
M_k(u)=(1+s)^k+(1-s)^k.
\]

In particular,

\[
M_1=2,
\]

\[
M_2=2(1+s^2),
\]

\[
M_3=2(1+3s^2),
\]

\[
M_4=2(1+6s^2+s^4).
\]

The first moment is depth-blind; every moment from order two upward is strictly depth-sensitive.

## Round 4 verdict

**Derived here:** exact finite-band positive/negative eigenvalues and a horizontal resolution parameter \(u=2A|\delta|\).  
**Observed + explained:** the empirical \(T\sim2\pi x\) law is a stable vertical horizon.  
**Roadblock:** shallow off-line pairs require support exponential in inverse depth.  
**New avenue:** use higher moments to bound the distribution of normalized depths \(u_\rho\).

---
# Round 5 — Inertia, moments, and the fleet of weaker theorems

## Target

Extract unconditional information from finite compressions of \(W\) without assuming that the zero side is already a positive sum over real ordinates.

## 5.1 The rank--inertia breakthrough

Alpöge and Furman replace the RH-dependent reading of the zero side by a finite-dimensional Hermitian matrix. On-line zeros contribute positive rank-one atoms; off-line pairs contribute signature-\((1,1)\) blocks. Sylvester's law of inertia then converts the matrix's positive index into information about zeros on the line.

Their 2026 theorem proves unconditionally:

\[
\boxed{\text{at least }\frac23\text{ of the nontrivial zeros are simple and on the critical line},}
\]

counted with multiplicity, and

\[
\boxed{\text{at least }\frac56\text{ are distinct}.}
\]

A Montgomery--Taylor window gives approximately

\[
0.6725
\]

simple on-line and

\[
0.8362
\]

distinct [R5].

This materially changes Wall 1. Identities do not produce full positivity, but identities plus inertia and moment inequalities produce genuine partial location theorems.

## 5.2 Moment hierarchy

Let \(\widetilde G\) denote the normalized finite Weil compression and write

\[
m_k=\frac1d\operatorname{Tr}\widetilde G^k.
\]

The expected limiting values begin

\[
\boxed{
m_0=1,
\quad
m_1=1,
\quad
m_2=\frac43,
\quad
m_3=2,
\quad
m_4=\frac{13}{4}.
}
\tag{5.1}
\]

The first two nontrivial moments are sufficient for the two-thirds theorem. Higher moments should improve the Christoffel/inertia certificate.

The obstacle is arithmetic: at full natural bandwidth, \(m_4\) contains a difficult additive prime-correlation term of Hardy--Littlewood type. Separate control of every moment may be unnecessarily expensive.

## 5.3 Christoffel optimization

Given moments through degree four, consider polynomials

\[
q(x)=1+ux+vx^2.
\]

The quantity

\[
\int q(x)^2\,d\mu(x)
\]

is minimized subject to \(q(0)=1\) by solving the moment-matrix problem.

At the expected moments (5.1), the exact minimizer is

\[
\boxed{
q_*(x)=1-\frac74x+\frac23x^2.
}
\tag{5.2}
\]

The associated Christoffel value is

\[
\boxed{
\Lambda_2(0)=\frac5{36}.
}
\tag{5.3}
\]

Within the Alpöge--Furman conversion, this gives

\[
1-2\Lambda_2(0)=\frac{13}{18}.
\]

## 5.4 A compressed quartic target

Expand

\[
q_*(x)^2
=1-\frac72x+\frac{211}{48}x^2-\frac73x^3+\frac49x^4.
\]

Therefore

\[
\boxed{
\frac1d\operatorname{Tr}q_*(\widetilde G)^2
=1-\frac72m_1+\frac{211}{48}m_2-\frac73m_3+\frac49m_4.
}
\tag{5.4}
\]

Using \(m_1=1\) and \(m_2=4/3\),

\[
\boxed{
\frac1d\operatorname{Tr}q_*(\widetilde G)^2
=\frac{121-84m_3+16m_4}{36}.
}
\tag{5.5}
\]

Beating \(2/3\) requires this to be less than \(1/6\). Thus:

> **Derived theorem 5.1 — mixed quartic sufficient condition.**
>
> Within the same normalization and asymptotic inertia conversion, the inequality
> \[
> \boxed{84m_3-16m_4>115}
> \tag{5.6}
> \]
> is sufficient to improve the unconditional two-thirds proportion.

At the expected moments, the left side is \(116\), leaving a margin of \(1\).

## 5.5 Why the mixed trace may be easier

Instead of proving

\[
m_3\to2
\]

and

\[
m_4\to\frac{13}{4}
\]

separately, expand the single nonnegative quantity

\[
\boxed{
\operatorname{Tr}
\left(I-\frac74\widetilde G+\frac23\widetilde G^2\right)^2
}
\tag{5.7}
\]

directly on the prime side before applying absolute values or triangle inequalities.

The cubic and quartic terms have opposite signs. The inaccessible fourth-order convolution may:

- cancel exactly;
- cancel partially;
- survive unchanged;
- acquire a usable one-sided sign.

Any of the first three outcomes is informative. The calculation is finite and exact at the combinatorial level.

## 5.6 Local depth penalty of the quartic certificate

For one isolated off-line pair, the normalized block eigenvalues are

\[
1+s,
\qquad
1-s,
\qquad
s=\frac{\sinh u}{u}\ge1.
\]

Its contribution to the mixed quartic is

\[
\boxed{
q_*(1+s)^2+q_*(1-s)^2
=\frac{64s^4+9s^2+1}{72}.
}
\tag{5.8}
\]

This is strictly increasing for \(s\ge1\). Hence the polynomial is naturally depth-sensitive: deep off-line blocks are penalized more strongly than the shallow/double-zero limit \(s=1\).

A simpler local defect polynomial is

\[
\boxed{
\operatorname{Tr}\bigl[(B^2-2B)^2\bigr]
=2(s^2-1)^2.
}
\tag{5.9}
\]

It vanishes exactly for the normalized on-line-double spectrum \(\{2,0\}\) and is positive for every off-line pair.

This does not immediately globalize because zero blocks are not mutually orthogonal. But it supplies a target polynomial for a depth-sensitive inertia theorem.

## 5.7 A corridor theorem target

Define the normalized horizontal depth at height \(T\):

\[
u_\rho
=\left|\beta-\frac12\right|
\log\frac{T}{2\pi}.
\]

A weaker theorem than RH would be

\[
\boxed{
\#\{\rho:T<\gamma\le2T,\ u_\rho\ge U\}
\le C(U)N(T),
\qquad C(U)\downarrow0.
}
\tag{5.10}
\]

Such a result would force all possible off-line zeros into a shrinking corridor

\[
\left|\beta-\frac12\right|
\ll\frac1{\log T}.
\]

The exact local eigenvalues in Round 4 tell us what moments or polynomials should be optimized to obtain \(C(U)\).

## Round 5 verdict

**External theorem:** the tide has already risen to \(2/3\) simple on-line zeros.  
**Derived here:** one mixed quartic inequality is sufficient to rise further.  
**New avenue:** expand the signed polynomial trace directly on the prime side.  
**Weaker-proof program:** use depth-sensitive moments to shrink any possible off-line population into a critical corridor.  
**Roadblock:** all-moment density-one control still may leave a sparse exceptional set and therefore does not automatically prove RH.

---

# Round 6 — Connes--van Suijlekom: parity, simplicity, and a Loewner reduction

## Target

Turn the finite condition “the lowest localized Weil eigenvalue is simple, isolated, and even” into a sharper and more attackable inequality.

## 6.1 The real-zero engine

Connes--van Suijlekom prove [R2]:

> If a lower-bounded convolution-type operator on a symmetric interval has a simple isolated lowest eigenvalue with an even eigenfunction \(\theta\), then every zero of \(\widehat\theta\) is real.

Connes's current RH strategy [R1] therefore separates into:

1. prove the finite Weil ground state is simple and even;
2. prove its transform converges to \(\Xi\).

The first is finite-dimensional at each cutoff. The second is the global selection problem.

## 6.2 Exact commutator structure

On the finite frequency basis \(e_{-N},\ldots,e_N\), let

\[
D e_j=j e_j,
\]

and let \(\Gamma e_j=e_{-j}\) be reflection. The finite Weil matrices satisfy

\[
Q\Gamma=\Gamma Q,
\qquad
D\Gamma=-\Gamma D,
\]

and the rank-two displacement identity

\[
\boxed{
DQ-QD
=|\beta\rangle\langle\eta|
-|\eta\rangle\langle\beta|,
}
\tag{6.1}
\]

where \(\eta\) is even and \(\beta\) is odd [R2].

Decompose

\[
\mathcal H=\mathcal H_+\oplus\mathcal H_-
\]

into even and odd sectors.

## 6.3 Parity-crossing theorem

> **Derived theorem 6.1.**  
> If an eigenvalue \(\lambda\) has multiplicity at least two inside one parity sector, then \(\lambda\) is also an eigenvalue in the opposite parity sector.

### Proof in the even sector

Suppose

\[
\dim\ker(Q-\lambda I)|_{\mathcal H_+}\ge2.
\]

Choose a nonzero even eigenvector \(x\) with

\[
\langle\eta,x\rangle=0.
\]

This is possible because the even eigenspace has dimension at least two. Since \(\beta\) is odd,

\[
\langle\beta,x\rangle=0.
\]

Equation (6.1) gives

\[
[D,Q]x=0.
\]

Therefore

\[
QDx=DQx=\lambda Dx.
\]

Because \(D\) reverses parity, \(Dx\) is odd. It is nonzero: the kernel of \(D\) is spanned by \(e_0\), and \(e_0\) is not orthogonal to \(\eta\). Thus \(\lambda\) is an odd eigenvalue.

The odd-to-even case is identical.

## 6.4 Parity-gap corollary

Define

\[
\lambda_1^+
=\lambda_{\min}(Q|_{\mathcal H_+}),
\]

\[
\lambda_1^-
=\lambda_{\min}(Q|_{\mathcal H_-}).
\]

If

\[
\boxed{
\lambda_1^+<\lambda_1^-,
}
\tag{6.2}
\]

then the global ground state is even. If its even-sector multiplicity were at least two, Theorem 6.1 would force an odd eigenvector with the same eigenvalue, contradicting the strict inequality.

Hence:

> **Derived theorem 6.2 — parity-gap reduction.**  
> The single inequality
> \[
> \boxed{\Delta_{\rm par}:=\lambda_1^--\lambda_1^+>0}
> \tag{6.3}
> \]
> proves that the finite Weil ground state is simple, isolated, and even.

This is the cleanest immediate subproblem in the Connes strategy.

## 6.5 Parity Loewner decomposition

The divided-difference matrix (3.1) admits a more revealing decomposition.

Let \(\psi\) be odd and define

\[
\boxed{
\phi(x)=\frac{\psi(\sqrt x)}{\sqrt x},
\qquad
\phi(0)=\psi'(0).
}
\tag{6.4}
\]

Let

\[
x_j=j^2,
\qquad j=1,\ldots,N.
\]

Use the parity basis

\[
e_0,
\qquad
e_j^+=\frac{e_j+e_{-j}}{\sqrt2},
\qquad
e_j^-=\frac{e_j-e_{-j}}{\sqrt2}.
\]

For divided differences

\[
f[x,y]=\frac{f(x)-f(y)}{x-y},
\]

with diagonal value \(f'(x)\), direct algebra gives:

### Odd block

\[
\boxed{
(Q^-)_{jk}
=2jk\,\phi[x_j,x_k].
}
\tag{6.5}
\]

Equivalently,

\[
Q^-=2D L_\phi D,
\]

where

\[
D=\operatorname{diag}(1,\ldots,N)
\]

and \(L_\phi\) is the Loewner matrix of \(\phi\) on the square nodes \(x_j\).

### Even block

Let

\[
v_j=\phi(x_j).
\]

Then

\[
\boxed{
Q^+
=
\begin{pmatrix}
\phi(0)&\sqrt2\,v^{\mathsf T}\\
\sqrt2\,v&2L_{x\phi}
\end{pmatrix}.
}
\tag{6.6}
\]

This decomposition was checked numerically to approximately \(10^{-14}\) in the companion script.

## 6.6 Why this is valuable

The parity gap has become a comparison of two matrix-monotonicity objects:

\[
Q^-=2D L_\phi D,
\]

versus a bordered Loewner matrix built from \(x\phi(x)\).

Potential routes include:

1. prove a Loewner-order comparison between \(L_\phi\) and \(L_{x\phi}\);
2. control the even Schur complement
   \[
   \phi(0)-v^{\mathsf T}L_{x\phi}^{\dagger}v;
   \]
3. exploit total positivity or Stieltjes representations of \(\phi\);
4. isolate primitive-prime and repeated-prime contributions at the source-function level.

If \(L_{x\phi}\succ0\), the even block is positive precisely when

\[
\boxed{
\phi(0)\ge v^{\mathsf T}L_{x\phi}^{-1}v.
}
\tag{6.7}
\]

This is a Christoffel-type inequality. It provides an unexpected bridge between the parity problem and the moment/Christoffel machinery of Round 5.

## 6.7 Concrete proof program

Construct exact or cutoff-free source functions

\[
\psi=\psi_{\infty}+\psi_{\rm pole}+\psi_{\rm prim}+\psi_{\rm rep}.
\]

For each component, compute

\[
\phi(x)=\frac{\psi(\sqrt x)}{\sqrt x}
\]

and its two Loewner matrices.

The target is not merely numerical positivity. It is a uniform inequality

\[
\boxed{
\lambda_{\min}(Q^-)-\lambda_{\min}(Q^+)
\ge c_\lambda>0
}
\tag{6.8}
\]

with an error budget smaller than \(c_\lambda\).

## Round 6 verdict

**External theorem:** simple isolated even ground state implies a real-rooted transform.  
**Derived here:** multiplicity forces parity crossing; strict even/odd ordering is enough.  
**Derived here:** exact parity Loewner decomposition.  
**Best immediate full-proof foothold:** prove \(\Delta_{\rm par}>0\).  
**Roadblock:** finite numerical gaps do not imply a uniform infinite-support gap.

---

# Round 7 — The global radical, boundary leakage, and functional-calculus selection

## Target

Explain why global positivity does not automatically select the finite Weil minimizer, and reduce the comparison with the prolate candidate to an exterior operator estimate.

## 7.1 The global radical

Connes's summation map is

\[
\boxed{
E(f)(u)=u^{1/2}\sum_{n\ge1}f(nu).
}
\tag{7.1}
\]

On the codimension-two admissible space

\[
f(0)=0,
\qquad
\widehat f(0)=0,
\]

its Mellin transform contains \(\xi\), and its range lies in the radical of the global Weil form:

\[
\operatorname{Ran}E\subseteq\operatorname{Rad}Q_W.
\]

Thus many globally distinct functions have exactly zero Weil energy. The finite-window ground state is chosen only after truncation lifts that degeneracy.

This proves a key conceptual point:

\[
\boxed{
\text{Global positivity is not enough to identify Connes's finite minimizer.}
}
\]

A geometric proof of RH would prove \(W\succeq0\), but the Connes minimizer-convergence route owes additional selection debt.

## 7.2 Radical-cut identity

Let \(Q\) be a Hermitian form, \(u,v\in\operatorname{Rad}Q\), and let \(P\) be an orthogonal projection. Set

\[
R=I-P.
\]

Because \(Q(u,\cdot)=Q(v,\cdot)=0\),

\[
0=Q(Pu+Ru,Pv+Rv).
\]

The cross terms cancel separately through the radical identities, yielding:

> **Derived theorem 7.1 — radical cut.**
>
> \[
> \boxed{Q(Pu,Pv)=Q(Ru,Rv).}
> \tag{7.2}
> \]

Also, if \(g=Pg\),

\[
\boxed{Q(Pu,g)=-Q(Ru,g).}
\tag{7.3}
\]

Therefore the entire finite-window residual is an exterior boundary effect.

## 7.3 Boundary generalized eigenproblems

Choose globally orthonormal radical vectors

\[
u_1,\ldots,u_m.
\]

Define

\[
(G_{\rm out})_{ij}
=\langle Ru_i,Ru_j\rangle,
\]

\[
(W_{\rm out})_{ij}
=Q(Ru_i,Ru_j).
\]

Since

\[
\langle Pu_i,Pu_j\rangle
=\delta_{ij}-(G_{\rm out})_{ij},
\]

the finite Weil minimizer restricted to this radical slice solves

\[
\boxed{
W_{\rm out}c
=\mu(I-G_{\rm out})c.
}
\tag{7.4}
\]

The ordinary prolate leakage minimizer solves

\[
\boxed{
G_{\rm out}c
=\ell(I-G_{\rm out})c.
}
\tag{7.5}
\]

The two problems differ only in the exterior quadratic form.

## 7.4 Strong boundary isotropy

A simple sufficient condition would be

\[
W_{\rm out}
=c_\lambda G_{\rm out}+E_\lambda,
\]

with \(E_\lambda\) small relative to the prolate gap.

But scalar proportionality is unnecessarily rigid.

## 7.5 Functional-calculus selection theorem

Define

\[
L=(I-G)^{-1/2}G(I-G)^{-1/2},
\]

\[
B=(I-G)^{-1/2}W(I-G)^{-1/2}.
\]

The bottom eigenvector of \(L\) is the prolate ground state. The bottom eigenvector of \(B\) is the Weil ground state.

Suppose

\[
\boxed{
B=p_\lambda(L)+E_\lambda,
}
\tag{7.6}
\]

where \(p_\lambda\) is strictly increasing near the first two eigenvalues

\[
\ell_1<\ell_2
\]

of \(L\). Define

\[
\Delta_p
=p_\lambda(\ell_2)-p_\lambda(\ell_1)>0.
\]

> **Derived theorem 7.2 — functional-calculus selection.**  
> If
> \[
> \boxed{\|E_\lambda\|<\frac12\Delta_p,}
> \tag{7.7}
> \]
> then the Weil ground state is simple and
> \[
> \boxed{
> \sin\angle(\theta_\lambda,\kappa_\lambda)
> \le\frac{2\|E_\lambda\|}{\Delta_p}.
> }
> \tag{7.8}
> \]

### Proof

Conjugation converts both generalized pencils into ordinary self-adjoint operators. The bottom eigenvalue of \(p_\lambda(L)\) is isolated by \(\Delta_p\). Apply the Davis--Kahan or reduced-resolvent bound.

## 7.6 New diagnostics

For polynomial degree \(d\), define

\[
\boxed{
\varepsilon_d(\lambda)
=\inf_{\deg p\le d}
\|B_\lambda-p(L_\lambda)\|.
}
\tag{7.9}
\]

Also define the commutator defect

\[
\boxed{
\chi(\lambda)=\|[B_\lambda,L_\lambda]\|.
}
\tag{7.10}
\]

The verdict-changing ratio is

\[
\boxed{
\mathfrak S_d(\lambda)
=
\frac{\varepsilon_d(\lambda)}
{p(\ell_2)-p(\ell_1)}.
}
\tag{7.11}
\]

- \(\mathfrak S_d\to0\): prolate-to-Weil selection is on track.
- \(\mathfrak S_d\asymp1\): the functional-calculus route fails at degree \(d\).
- best-fit \(p\) nonmonotone near the bottom: even approximate common eigenvectors do not give the correct order.

This is a genuinely different operator category from the earlier failed searches for bare differential commutants or finite linear combinations of local prime translations.

## 7.7 Prolate leakage as the exact boundary source

Let \(h_\lambda\) be the finite prolate seed, supported in \([-\lambda,\lambda]\). Poisson summation relates the lower multiplicative tail of \(E(h_\lambda)\) to the out-of-band Fourier leakage

\[
\ell_\lambda=(I-P_\lambda)\widehat h_\lambda.
\]

For prolate eigenmodes, this leakage is explicitly governed by the Slepian eigenvalues. Hence the desired analytic theorem is an amplified leakage estimate

\[
\boxed{
\|E\ell_\lambda\|_{\mathrm{Weil}^*}
\le C\lambda^M
\|\ell_\lambda\|_{\mathrm{prolate}}.
}
\tag{7.12}
\]

Combined with a complementary spectral gap, this closes the residual-to-gap ratio.

Groskin's Archimedean tail budget \(\asymp\log T/T\) blocks brute numerical quadrature at tiny eigenvalue scales [R4]. It does not prohibit the exact analytic mapping estimate (7.12), because the two cutoffs and norms are different.

## 7.8 Why triangle inequalities fail

On the critical line,

\[
\sum_{p\le X}\frac{\log p}{\sqrt p}
\sim2\sqrt X.
\]

Even the repeated-prime mass contains

\[
\sum_{p\le X}\frac{\log p}{p}
\sim\log X.
\]

Therefore an absolute operator-norm summation of prime shells cannot converge. Any successful estimate must be **on-state and phase-sensitive**, exploiting oscillatory cancellation after \(E\) acts.

## Round 7 verdict

**Derived here:** finite Weil energy of global radical vectors is entirely exterior boundary energy.  
**Derived here:** a monotone functional relation between exterior Weil and prolate leakage is sufficient for minimizer transfer.  
**Sharp analytic target:** the \(E\)-amplified leakage estimate.  
**Roadblock:** absolute prime budgets diverge; cancellation must be retained.  
**Boundary:** this selection route is RH-plus—it proves RH but owes more than positivity alone.

---
# Round 8 — Explicit positive packets, pole cancellation, and the Nicolas bridge

## Target

Construct a self-contained family of positive-type Weil tests with finite prime support, expose the pole/Archimedean compensation exactly, and connect the operator form to the elementary primorial criterion.

## 8.1 Hyperbolic-tent seed

For \(t>0\), define

\[
\boxed{
f_t(u)=\frac1{\sqrt2}e^{u/2}\mathbf 1_{[-t/2,t/2]}(u).
}
\tag{8.1}
\]

Its reflected conjugate is

\[
\widetilde f_t(u)=\overline{f_t(-u)}.
\]

A direct convolution calculation gives

\[
\boxed{
g_t(u)
=(f_t*\widetilde f_t)(u)
=\sinh\left(\frac{t-|u|}{2}\right)
\mathbf 1_{\{|u|\le t\}}.
}
\tag{8.2}
\]

The Fourier transform is

\[
\boxed{
F_t(z)
=\sqrt2\,
\frac{\sinh\left(\frac t2(\frac12+iz)\right)}{\frac12+iz}.
}
\tag{8.3}
\]

For real \(r\),

\[
\boxed{
h_t(r)=|F_t(r)|^2
=\frac{\cosh(t/2)-\cos(tr)}{r^2+1/4}.
}
\tag{8.4}
\]

The apparent poles at \(r=\pm i/2\) are removable because the numerator vanishes there. This identity is checked symbolically in `rh_master_checks.py`.

The indicator can be replaced by smooth compactly supported approximations when a strict Schwartz-class hypothesis is required.

## 8.2 Exact finite prime-power packet

Set

\[
x=e^t.
\]

For \(n\le x\),
\[
g_t(\log n)
=\sinh\left(\frac{t-\log n}{2}\right).
\]

Therefore

\[
\boxed{
-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g_t(\log n)
=
rac{\Psi(x)}{\sqrt x}
-\sqrt x\sum_{n\le x}\frac{\Lambda(n)}n,
}
\tag{8.5}
\]

where

\[
\Psi(x)=\sum_{n\le x}\Lambda(n)
\]

is the Chebyshev prime-power function.

Only prime powers \(n\le x\) occur.

The pole values are

\[
\boxed{
h_t(i/2)=h_t(-i/2)=t\sinh(t/2).
}
\tag{8.6}
\]

Thus the explicit formula specializes to

\[
\boxed{
\begin{aligned}
\sum_\rho h_t(z_\rho)
={}&2t\sinh(t/2)+\mathcal A_\infty(t)\\
&+\frac{\Psi(x)}{\sqrt x}
-\sqrt x\sum_{n\le x}\frac{\Lambda(n)}n,
\end{aligned}
}
\tag{8.7}
\]

where

\[
\mathcal A_\infty(t)
=\frac1{2\pi}\int_{\mathbb R}
h_t(r)
\left[
\Re\psi_\Gamma\left(\frac14+\frac{ir}{2}\right)-\log\pi
\right]dr.
\]

This is an exact compactly supported probe linking zeros, pole, Gamma, and a finite prime-power packet.

## 8.3 Archimedean uniqueness of the hyperbolic baseline

Consider

\[
H_{t,c}(z)=\frac{c-\cos(tz)}{z^2+1/4}.
\]

For this to be entire, the numerator must vanish at \(z=i/2\):

\[
c=\cos(ti/2)=\cosh(t/2).
\]

Hence:

> **Derived theorem 8.1 — pole-compatible baseline.**  
> The unique constant making \((c-\cos tz)/(z^2+1/4)\) entire is
> \[
> \boxed{c=\cosh(t/2).}
> \tag{8.8}
> \]

The tempting tight real-axis numerator \(1-\cos(tr)\) does not extend through the pole locations. Analytic compatibility forces the larger hyperbolic baseline.

This is an elementary avatar of Wall 2: the Archimedean completion exacts a compulsory positivity budget.

## 8.4 Pole-neutral two-scale packets

Because

\[
F_t(i/2)=\frac t{\sqrt2},
\]

define

\[
\boxed{
F_{t_1,t_2}(z)
=t_2F_{t_1}(z)-t_1F_{t_2}(z).
}
\tag{8.9}
\]

Then

\[
F_{t_1,t_2}(i/2)=0.
\]

Set

\[
h_{t_1,t_2}(z)
=F_{t_1,t_2}(z)F_{t_1,t_2}(-z).
\]

For real \(r\),

\[
h_{t_1,t_2}(r)=|F_{t_1,t_2}(r)|^2\ge0,
\]

while

\[
\boxed{
h_{t_1,t_2}(\pm i/2)=0.}
\tag{8.10}
\]

These are explicit compactly supported positive-type tests with the pole sector removed.

They are ideal for:

- parity-gap experiments;
- projective-curvature optimization;
- primitive/repetition factorial decompositions;
- pole-free finite Guinand--Weil certification.

## 8.5 Nicolas criterion

Let

\[
N_k=\prod_{j=1}^kp_j
\]

be the \(k\)-th primorial. Then

\[
\frac{N_k}{\varphi(N_k)}
=\prod_{p\le p_k}\left(1-\frac1p\right)^{-1}.
\]

Nicolas's criterion states [R10]:

\[
\boxed{
\mathrm{RH}
\iff
\frac{N_k}{\varphi(N_k)}
>e^\gamma\log\log N_k
\quad\text{for every }k\ge1.
}
\tag{8.11}
\]

Define under RH

\[
\beta_\zeta
=\sum_\rho\frac1{\rho(1-\rho)},
\]

and

\[
W(x)
=\sum_\rho
\frac{x^{i\Im\rho}}{\rho(1-\rho)}.
\]

Nicolas proves that the normalized primorial error has first-order form

\[
\boxed{
\log f(x)
=-\frac{2+W(x)}{\sqrt x\log x}
+O\left(\frac1{\sqrt x\log^2x}\right).
}
\tag{8.12}
\]

The constant \(2\) is principally the prime-square/repetition correction. The oscillatory part \(W(x)\) is the zero spectrum.

## 8.6 Exact bridge to the hyperbolic packet

Under RH,

\[
\rho(1-\rho)=\gamma^2+\frac14.
\]

Using (8.4),

\[
\boxed{
\sum_\rho h_t(\gamma)
=\beta_\zeta\cosh(t/2)-W(e^t).
}
\tag{8.13}
\]

If a Hilbert--Pólya operator \(H\) existed with eigenvalues \(\gamma\), then

\[
\boxed{
W(e^t)
=\operatorname{Tr}
\left[(H^2+1/4)^{-1}e^{itH}\right].
}
\tag{8.14}
\]

Thus the elementary primorial criterion is a one-parameter arithmetic shadow of a resolvent-smoothed spectral trace of the same Hermitian system.

It is not the full Weil form: it samples one cone of test functions. But it is a rigorous bridge from overalls to Hilbert space.

## 8.7 Primitive versus repeated primes

Nicolas's formula strongly suggests the decomposition

\[
Q_W
=Q_\infty+Q_{\rm prim}+Q_{\rm rep}.
\]

The scalar primorial asymptotic assigns different roles:

- repeated prime powers, especially squares, supply a coherent baseline;
- primitive primes carry the delicate oscillation;
- infinity sets the smooth counterbudget.

This motivates a complete fixed-support factorial experiment:

\[
Q_\infty,
\quad
Q_\infty+Q_{\rm prim},
\quad
Q_\infty+Q_{\rm rep},
\quad
Q_{\rm full}.
\]

For each, compute:

\[
\lambda_1^+,\quad
\lambda_1^-,\quad
\Delta_{\rm par},\quad
\kappa_{\rm off},\quad
\theta_\lambda.
\]

Controls should shuffle \(\log p\) while preserving weights and separately shuffle primitive/repetition labels.

## Round 8 verdict

**Derived here:** explicit positive-type and pole-neutral compactly supported test families.  
**External theorem:** Nicolas's primorial criterion is RH-equivalent.  
**Exact bridge:** Nicolas's zero oscillation is the hyperbolic-tent zero trace.  
**New experiment:** test whether repeated prime powers supply a coercive baseline while primitive primes steer phase selection.  
**Boundary:** one scalar primorial cone cannot replace positivity on the whole Weil space.

---

# Round 9 — Witt/necklace deformations, scaled zero ghosts, and resolvent blindness

## Target

Understand the prime-support/powerset deformation without collapsing it back into an Euler-product restatement, and determine whether it supplies a lawful path toward RH.

## 9.1 Support and multiplicity deformation

Define

\[
\boxed{
Z_{a,b}(s)
=\prod_p
\left(1+a\frac{p^{-s}}{1-bp^{-s}}\right).
}
\tag{9.1}
\]

Expanding local occupation numbers gives

\[
\boxed{
Z_{a,b}(s)
=\sum_{n\ge1}
a^{\omega(n)}
b^{\Omega(n)-\omega(n)}n^{-s},
}
\tag{9.2}
\]

where:

- \(\omega(n)\) counts distinct prime factors;
- \(\Omega(n)\) counts prime factors with multiplicity;
- \(a\) marks support occupation;
- \(b\) marks repetitions beyond the first.

The physical point is

\[
Z_{1,1}(s)=\zeta(s).
\]

The squarefree powerset is

\[
Z_{1,0}(s)=\frac{\zeta(s)}{\zeta(2s)}.
\]

## 9.2 Exact Witt/necklace factorization

Write

\[
\frac{1-(b-a)x}{1-bx}
=\prod_{n\ge1}(1-x^n)^{-d_n(a,b)}.
\]

Taking logarithms and applying Möbius inversion gives:

> **Derived theorem 9.1 — Witt factorization.**
>
> \[
> \boxed{
> Z_{a,b}(s)
> =\prod_{n\ge1}\zeta(ns)^{d_n(a,b)},
> }
> \tag{9.3}
> \]
> where
> \[
> \boxed{
> d_n(a,b)
> =\frac1n\sum_{d\mid n}
> \mu\!\left(\frac nd\right)
> \bigl[b^d-(b-a)^d\bigr].
> }
> \tag{9.4}
> \]

The companion script verifies the coefficient identity through order ten.

The first coefficients are

\[
d_1=a,
\]

\[
d_2=-\frac a2(a-2b+1),
\]

\[
d_3=\frac a3(a^2-3ab+3b^2-1).
\]

## 9.3 Zero-forward form

Formally complete each factor and take a logarithmic derivative:

\[
\frac d{ds}\log\prod_{n\ge1}\xi(ns)^{d_n}
=\sum_{n\ge1}nd_n\frac{\xi'(ns)}{\xi(ns)}.
\]

The zero contribution is

\[
\boxed{
\sum_{n\ge1}\sum_\rho
\frac{d_n(a,b)m_\rho}{s-\rho/n}
+\text{regularizing terms}.
}
\tag{9.5}
\]

Thus every original zero generates a signed tower

\[
\boxed{
\rho,\quad\frac\rho2,\quad\frac\rho3,\ldots
}
\tag{9.6}
\]

with weights \(d_n(a,b)\).

The powerset deformation is therefore a Witt/Adams transform of the zero divisor, not a mild motion of one zero spectrum.

## 9.4 Spectral-purity rigidity

Suppose

\[
d_n(a,b)=0
\quad\text{for every }n\ge2.
\]

If \(a\ne0\), \(d_2=0\) gives

\[
b=\frac{a+1}{2}.
\]

Substituting into \(d_3=0\) gives

\[
\frac{a(a-1)(a+1)}{12}=0.
\]

Hence:

> **Derived theorem 9.2 — spectral purity.**  
> The only nontrivial spectrally pure points are
> \[
> \boxed{(a,b)=(1,1)}
> \]
> giving \(\zeta\), and
> \[
> \boxed{(a,b)=(-1,0)}
> \]
> giving \(1/\zeta\). The family \(a=0\) is trivial.

Among nonnegative occupation parameters, \((1,1)\) is the unique nontrivial pure point.

This is a genuine rigidity statement: ordinary zeta is the unique positive-occupation point where all scaled ghost spectra cancel.

## 9.5 Finite Adams-tower classification

If only finitely many \(d_n\) are nonzero, then the local rational function

\[
\frac{1-(b-a)x}{1-bx}
\]

must be a finite product of cyclotomic factors. For real parameters, its nonzero zero and pole must lie at real roots of unity, hence at \(\pm1\).

Therefore finite support occurs only when

\[
b\in\{0,\pm1\},
\qquad
b-a\in\{0,\pm1\}.
\]

The nontrivial cases are

\[
\begin{array}{c|c}
(a,b)&Z_{a,b}(s)\\ \hline
(1,1)&\zeta(s)\\
(-1,0)&\zeta(s)^{-1}\\
(1,0)&\zeta(s)/\zeta(2s)\\
(2,1)&\zeta(s)^2/\zeta(2s)\\
(-1,-1)&\zeta(2s)/\zeta(s)\\
(-2,-1)&\zeta(2s)/\zeta(s)^2.
\end{array}
\tag{9.7}
\]

Generic deformations create an infinite tower or natural-boundary behavior. They are not a smooth family of completed ordinary \(L\)-functions sharing one unitary axis.

## 9.6 Tangent directions

At the physical point,

\[
\boxed{
\left.\partial_a d_n\right|_{1,1}
=\frac{\mu(n)}n,
}
\tag{9.8}
\]

and

\[
\boxed{
\left.\partial_b d_n\right|_{1,1}
=\frac{\varphi(n)-\mu(n)}n.
}
\tag{9.9}
\]

At the Euler-product level,

\[
\left.\partial_a\log Z_{a,b}(s)\right|_{1,1}
=\sum_p p^{-s},
\]

which isolates primitive-prime occupation. The \(b\)-direction isolates repeated occupations.

These are useful tangent coordinates, but not lawful global \(L\)-function deformations.

## 9.7 Deformed summation maps remain inside the radical

Define coefficients

\[
w_{a,b}(n)=a^{\omega(n)}b^{\Omega(n)-\omega(n)}
\]

and

\[
E_{a,b}f(u)
=u^{1/2}\sum_{n\ge1}w_{a,b}(n)f(nu).
\]

Let

\[
c_{a,b}=\mu*w_{a,b}
\]

under Dirichlet convolution and

\[
(C_{a,b}f)(u)
=\sum_{d\ge1}c_{a,b}(d)f(du).
\]

Then coefficient comparison gives:

> **Derived theorem 9.3.**
>
> \[
> \boxed{E_{a,b}=E\circ C_{a,b}.}
> \tag{9.10}
> \]

Therefore the deformation directions remain in the global \(E\)-range and hence in the global Weil radical, on the common admissible domain.

This is the correct role of the powerset variables:

\[
\boxed{
\text{they are coordinates inside the global radical.}
}
\]

Finite truncation assigns them different boundary leakage energies. The physical direction is selected, if at all, by boundary geometry—not by a global deformation of zero locations.

## 9.8 Zero-resolvent form

Define

\[
\boxed{
R_\Xi(z)
=-\frac{\Xi'(z)}{2z\Xi(z)}
=\sum_{\lambda\in\Lambda_+}
\frac1{\lambda^2-z^2}.
}
\tag{9.11}
\]

Under RH, setting \(w=z^2\) makes this the Stieltjes transform of the positive measure

\[
\sum_\gamma m_\gamma\delta_{\gamma^2}.
\]

Hence RH implies the full Herglotz/Stieltjes property.

## 9.9 Low-order resolvent blindness

For an off-line pair with centered coordinates

\[
\gamma\pm i\delta,
\]

the contribution on the imaginary axis is

\[
C_{\gamma,\delta}(x)
=\frac1{x+(\gamma-i\delta)^2}
+\frac1{x+(\gamma+i\delta)^2}.
\]

Let

\[
\theta_{\gamma,\delta}(x)
=\arctan
\frac{2\gamma|\delta|}{x+\gamma^2-\delta^2}.
\]

Then

\[
\boxed{
(-1)^nC_{\gamma,\delta}^{(n)}(x)
=2n!|x+(\gamma-i\delta)^2|^{-n-1}
\cos((n+1)\theta_{\gamma,\delta}(x)).
}
\tag{9.12}
\]

For every nontrivial zero,

\[
\gamma\ge\gamma_1\approx14.13472514,
\qquad
|\delta|<\frac12,
\qquad
x\ge0.
\]

Thus

\[
\theta_{\gamma,\delta}(x)
\le
\theta_*=
\arctan\frac{\gamma_1}{\gamma_1^2-1/4}
\approx0.07071826294.
\]

Since

\[
22\theta_*<\frac\pi2<23\theta_*,
\]

we obtain:

> **Derived theorem 9.4 — unconditional low-order Stieltjes signs.**
>
> Regardless of RH,
> \[
> \boxed{
> (-1)^nR_\Xi^{(n)}(x)>0
> \quad(x\ge0,\ 0\le n\le21).
> }
> \tag{9.13}
> \]

This theorem explains why low-order Hankel, Stieltjes, and \(s=-1\) probes can look impeccably positive even if RH is false.

The first possible detecting order for one pair is approximately

\[
\boxed{
n_{\rm detect}
\sim\frac{\pi\gamma}{4|\delta|}.}
\tag{9.14}
\]

High, shallow off-line zeros evade enormous finite-order tests.

## 9.10 Why \(s=-1\) remains useful but nondiscriminating

The point \(s=-1\) corresponds to

\[
z=\frac{3i}{2},
\qquad
x=\frac94.
\]

Therefore the resolvent value there is positive unconditionally by (9.13), even in a hypothetical RH-false world.

So \(s=-1\) is a powerful structural microscope—especially for detecting hidden scaled sectors through trivial zeros—but its low-order positivity does not discriminate RH.

## Round 9 verdict

**Derived here:** exact Witt factorization, spectral-purity rigidity, finite cyclotomic classification, and radical-coordinate factorization.  
**Killed:** a smooth support/multiplicity homotopy through lawful one-spectrum \(L\)-functions.  
**Derived here:** the first 22 Stieltjes signs are unconditional.  
**Lesson:** low-order positivity and special-value coherence can be structurally forced without RH.  
**Use:** deploy \(a,b\) as boundary/radical coordinates, not as a proof by Euler-product deformation.

---

# Round 10 — Integrated closure theorem, geometric moonshot, and the rising-tide roadmap

## Target

Assemble the strongest analytic and geometric routes without conflating their truth debts, then state the exact closure theorems and the hierarchy of weaker results.

## 10.1 Two genuinely different full-proof routes

### Route P: independent positivity

Construct a space and operators from arithmetic, without using the zeros, such that

\[
\boxed{
W(f,f)=\|T_f\|^2
}
\]

or

\[
\boxed{
W(f,f)=\operatorname{Tr}_\tau(T_fT_f^*).
}
\]

Then

\[
W\succeq0
\]

and RH follows immediately.

This is the finite-field/Hodge/absolute-geometry route. It is RH-complete but need not identify Connes's finite ground states.

### Route S: finite real-rooted approximants plus convergence

For every large cutoff \(\lambda\):

1. prove the finite Weil ground state is simple and even;
2. apply Connes--van Suijlekom to obtain a real-rooted transform;
3. prove those transforms converge locally uniformly to \(\Xi\);
4. apply Hurwitz.

This proves RH but carries additional minimizer-selection debt.

Therefore:

\[
\boxed{
\text{positivity route is RH-complete; selection route is RH-plus.}
}
\tag{10.1}
\]

## 10.2 Analytic closure theorem

Let \(Q_\lambda\) be the cutoff-free localized Weil operator. Let \(\theta_\lambda\) be its normalized ground state. Let \(k_\lambda\) be the normalized prolate candidate whose Mellin transform is already known to converge to \(\Xi\) on closed substrips [R1, R3].

Assume:

### A. Parity gap

\[
\boxed{
\lambda_1^+(\lambda)<\lambda_1^-(\lambda)
}
\tag{A}
\]

for all sufficiently large \(\lambda\).

By Round 6, \(\theta_\lambda\) is simple and even.

### B. Boundary functional calculus

\[
\boxed{
B_\lambda=p_\lambda(L_\lambda)+E_\lambda,
}
\]

with \(p_\lambda\) increasing near \(\ell_1,\ell_2\), and

\[
\boxed{
\frac{\|E_\lambda\|}
{p_\lambda(\ell_2)-p_\lambda(\ell_1)}
\longrightarrow0.
}
\tag{B}
\]

Then

\[
\|\theta_\lambda-k_\lambda\|\to0.
\]

### C. Mellin tightness

For every \(a<1/2\), assume a weighted bound sufficient for

\[
\boxed{
\lambda^a\|\theta_\lambda-k_\lambda\|	o0
}
\tag{C}
\]

or its weighted-tail equivalent.

Then

\[
\mathcal M\theta_\lambda(z)
\longrightarrow\Xi(z)
\]

locally uniformly on closed substrips

\[
|\Im z|<\frac12.
\]

By A and [R2], every \(\mathcal M\theta_\lambda\) has only real zeros. Hurwitz's theorem therefore gives:

> **Conditional closure theorem 10.1.**  
> Assumptions A--C imply RH.

This theorem is not circular: A--C mention only arithmetic operators, prolate leakage, and convergence estimates. But their combined strength is at least RH.

## 10.3 Local finite-height version

Fix \(T>0\). If A--C hold strongly enough to give uniform convergence on a neighborhood of

\[
\{z:|\Re z|\le T,\ |\Im z|\le\eta\},
\]

then every zero of \(\Xi\) in that rectangle is real.

Thus one may seek a sequence of uniform finite-height theorems:

\[
\boxed{
\mathrm{RH}(T):
\text{all zeros with }|\Im\rho|\le T
\text{ lie on the line}.
}
\tag{10.2}
\]

This is mathematically valid only if the estimates are genuinely uniform and do not use prior knowledge of the zeros.

## 10.4 Absolute-geometric closure theorem

Let

\[
X=\overline{\operatorname{Spec}\mathbb Z}_{/\mathbb F_1}
\]

and

\[
S=X\times_{\mathbb F_1}X
\]

be a rigorous arithmetic-site/Witt/tropical realization. Suppose one constructs:

1. \(H^1_{\rm abs}(X)\) independently of zeta zeros;
2. primitive middle cohomology
   \[
   H^2_{\rm prim}(S)(1)
   \simeq
   H^1_{\rm abs}(X)\widehat\otimes\overline{H^1_{\rm abs}(X)};
   \]
3. a flow/correspondence representation \(D\mapsto T_D\);
4. a Lefschetz formula equating diagonal intersections with the explicit formula;
5. a polarization proving
   \[
   -(D,D)=\operatorname{Tr}_\tau(T_DT_D^*)\ge0;
   \]
6. completeness so that no zero modes are invisible to the cohomology.

Then Weil positivity follows and hence RH.

The noncircular requirement is absolute:

> The Hilbert metric and Hodge sign must be constructed from the geometry before the zeta-zero trace is identified.

Defining the intersection form to equal the Weil form and asserting Hodge negativity would merely assume RH.

## 10.5 Semilocal proving grounds

Two bounded programs can calibrate the geometry:

- a one-prime adelic/Poisson--Hodge complex \(\{\infty,2\}\);
- a two-prime tropical square such as the \(2,3\) scaling circles.

A semilocal success would not cross the global wall, because finite-place positivity is already accessible in prolate/Sonin models. But it would establish a genuinely independent mechanism and could reveal the correct boundary terms for globalization.

## 10.6 The rising-tide ladder

\[
\begin{array}{c|l|l}
\text{Level}&\text{Input}&\text{Conclusion}\\ \hline
0&\text{explicit formula}&\text{exact prime--zero identity}\\
1&\text{total-positive Gamma tail}&\text{simple even tail ground state}\\
2&\Delta_{\rm par}>0&\text{real-rooted finite Weil approximant}\\
3&\text{trace, inertia, }m_2&\ge2/3\text{ simple on-line}\\
4&\text{improved window}&\ge0.6725\text{ simple on-line}\\
5&84m_3-16m_4>115&\text{strict improvement beyond }2/3\\
6&\text{all moment control}&\text{density-one simple on-line}\\
7&\text{depth-sensitive moments}&\text{shrinking off-line corridor}\\
8&\text{local A--C through height }T&\mathrm{RH}(T)\\
9&W\succeq0\text{ from independent polarization}&\mathrm{RH}\\
10&\text{global A--C}&\mathrm{RH}\text{ via real-rooted approximants}.
\end{array}
\tag{10.3}
\]

The ladder matters because not every useful theorem must be full RH. Each rung should be judged by whether it adds a new inequality, not merely a new identity.

## 10.7 The three highest-priority targets

### Target 1 — parity gap

\[
\boxed{
\lambda_{\min}(Q|_{\rm even})
<
\lambda_{\min}(Q|_{\rm odd}).
}
\]

This closes the finite simplicity/evenness condition.

### Target 2 — boundary functional calculus

\[
\boxed{
\frac{\inf_p\|B_\lambda-p(L_\lambda)\|}
{p(\ell_2)-p(\ell_1)}	o0.
}
\]

This closes the minimizer-selection condition.

### Target 3 — mixed quartic trace

\[
\boxed{84m_3-16m_4>115.}
\]

This is the strongest currently identified partial-theorem opportunity.

## Round 10 verdict

The program has two honest summits:

\[
\boxed{\text{build positivity independently}}
\]

or

\[
\boxed{\text{prove parity + boundary selection + convergence}.}
\]

The first is geometrically cleaner. The second is analytically more concrete. The moment/inertia staircase can raise weaker boats while either moonshot remains open.

---
# Part II. Cross-formulation map

The following formulations are not equal in practical value, even when they are logically equivalent to RH. Each exposes a different obstruction.

## 11. Hilbert--Pólya

Desired:

\[
H=H^*,
\qquad
\operatorname{Spec}(H)=\{\gamma_\rho\},
\qquad
\rho=\frac12+i\gamma_\rho.
\]

Then the spectrum is real and RH follows.

### What it buys

- reality of the spectrum as a structural theorem;
- unitary evolution;
- trace/resolvent language;- a natural home for pair correlation and determinant formulas.

### What it does not buy automatically

- a construction of \(H\);
- discreteness from the bare dilation generator;
- the correct prime periodic orbits;
- spectral completeness.

The Berry--Keating operator

\[
-i\left(x\frac d{dx}+\frac12\right)
\]

has the right unitary line and smooth counting law, but on \(L^2(\mathbb R_+)\) has continuous spectrum. Prime circles can reproduce prime-orbit trace terms, but fitting those terms does not derive the global self-adjoint spectrum.

## 12. Riemann--Siegel / Hardy \(Z\)

Define

\[
\vartheta(t)
=\arg\Gamma\!\left(\frac14+\frac{it}{2}\right)
-\frac t2\log\pi
\]

and

\[
Z(t)=e^{i\vartheta(t)}\zeta\!\left(\frac12+it\right).
\]

Then

\[
Z(t)\in\mathbb R
\quad(t\in\mathbb R).
\]

### What it buys

- a canonical Archimedean phase transport;
- sign changes detecting critical-line zeros;
- the smooth zero-density clock;
- the approximate functional equation and Riemann--Siegel sum.

### What it does not buy

- exclusion of zeros off the line.

Knowing the polarizer angle exactly does not prove that every zero is seen by the real detector.

## 13. Zero resolvent

\[
\boxed{
R_\Xi(z)
=-\frac{\Xi'(z)}{2z\Xi(z)}
=\sum_{\lambda>0}\frac1{\lambda^2-z^2}.
}
\]

### What it buys

- zeros appear as additive resolvent atoms;
- under RH it is a Stieltjes transform of a positive spectral measure;
- Taylor coefficients give reciprocal zero moments;
- Hankel and Jacobi operators arise naturally.

### What it does not buy

- positivity without an independent measure construction;
- sensitivity at low derivative order to high shallow off-line zeros.

Round 9 proves that the first 22 complete-monotonicity signs are unconditional.

## 14. Li coefficients

The Li coefficients are

\[
\lambda_n
=\frac1{(n-1)!}
\left.\frac{d^n}{ds^n}
\left[s^{n-1}\log\xi(s)\right]\right|_{s=1}.
\]

Li's criterion is

\[
\boxed{\mathrm{RH}\iff\lambda_n\ge0\ \forall n.}
\]

### What it buys

- a scalar sequence of inequalities;
- a Möbius map sending the critical line to the unit circle;
- strong asymptotic diagnostics.

### What it does not buy

- an independent positivity source;
- efficient detection of a high shallow off-line zero.

One off-line pair produces exponentially growing oscillations, but the first negative index can be astronomical.

## 15. Jensen / Laguerre--Pólya / moment operators

The expansion

\[
\log\frac{\Xi(z)}{\Xi(0)}
=-\sum_{k\ge1}\frac{\sigma_k}{k}z^{2k}
\]

uses

\[
\sigma_k=\sum_\gamma\gamma^{-2k}.
\]

Under RH these are moments of a positive measure on \((0,\infty)\), yielding positive Hankel matrices and real Jacobi nodes.

### What it buys

- a noncircular finite operator from Taylor coefficients of \(\xi\);
- accurate recovery of low zeros;
- access to Jensen polynomial and Turán inequality technology.

### What it does not buy

- finite-order certification of all zeros;
- a per-zero-resolved inertia count;
- an independent proof that all moment matrices remain positive.

These forms aggregate every zero into every matrix entry, unlike the atom-resolved Weil form.

## 16. Nicolas primorial criterion

\[
\mathrm{RH}
\iff
\frac{N_k}{\varphi(N_k)}
>e^\gamma\log\log N_k
\quad\forall k.
\]

### What it buys

- an elementary arithmetic inequality;
- literal finite prime products;
- a bridge to the same resolvent-smoothed zero trace \(W(x)\);
- explicit separation between primitive and repeated prime powers.

### What it does not buy

- the full test-function flexibility of Weil positivity;
- a known mechanism forcing the inequality at every primorial.

## 17. Nyman--Beurling and Farey/Franel formulations

These recast RH as approximation or discrepancy rates in \(L^2\) or rational-distribution spaces.

### What they buy

- monotone approximation functionals;
- direct \(\mathbb Z/\mathbb R\) structure;
- potential soft-analysis tools.

### What they do not buy

- an independent structural sign;
- per-zero atomization;
- a known path around the same square-root cancellation wall.

## 18. Witt/powerset formulation

\[
Z_{a,b}(s)
=\sum_n a^{\omega(n)}b^{\Omega(n)-\omega(n)}n^{-s}
=\prod_n\zeta(ns)^{d_n(a,b)}.
\]

### What it buys

- exact separation of prime support and repeated occupancy;
- a zero-forward scaled spectral tower;
- canonical tangent operators for primitive and repeated primes;
- coordinates inside the global Weil radical.

### What it does not buy

- a lawful smooth family of completed \(L\)-functions;
- positivity;
- a direct deformation proof of RH.

---

# Part III. The ten theorem cards

Each card states one result in reusable form.

## Card A — Off-line projective curvature

**Hypotheses:** analytic real evaluation curve \(v(t)\), centered zero displacement \(\delta\).  
**Conclusion:**

\[
\lambda_-
=-2\delta^2\|P_{v^\perp}v'\|^2+O(\delta^4).
\]

**Use:** optimize finite Weil probes for horizontal sensitivity.

---

## Card B — Exact Paley--Wiener pair spectrum

**Hypotheses:** full \(PW_A\) evaluation at \(z=\gamma-i\delta\).  
**Conclusion:**

\[
\lambda_\pm
=\frac A\pi
\left(1\pm\frac{\sinh(2A|\delta|)}{2A|\delta|}\right).
\]

**Use:** quantify finite-band blindness and depth moment excess.

---

## Card C — Parity crossing

**Hypotheses:** \(Q\Gamma=\Gamma Q\), \(D\Gamma=-\Gamma D\), and the rank-two commutator (6.1).  
**Conclusion:** multiplicity at least two in one parity sector forces a crossing with the other sector.

**Corollary:**

\[
\lambda_1^+<\lambda_1^-
\Rightarrow
\text{simple even ground state}.
\]

---

## Card D — Parity Loewner decomposition

**Hypotheses:** odd source \(\psi\), divided-difference matrix on symmetric integer nodes.  
**Conclusion:** with \(\phi(x)=\psi(\sqrt x)/\sqrt x\),

\[
Q^-=2D L_\phi D,
\]

\[
Q^+=
\begin{pmatrix}
\phi(0)&\sqrt2v^T\\
\sqrt2v&2L_{x\phi}
\end{pmatrix}.
\]

**Use:** translate the parity gap into matrix-monotonicity/Christoffel inequalities.

---

## Card E — Total-positive tail ground state

**Hypotheses:** real symmetric centrosymmetric strictly totally positive matrix of odd dimension.  
**Conclusion:** its lowest eigenvalue is simple and its eigenvector is even.

**Use:** complete model of the Connes real-zero engine for the Archimedean tail.

---

## Card F — Radical cut

**Hypotheses:** \(u,v\in\operatorname{Rad}Q\), orthogonal projection \(P\).  
**Conclusion:**

\[
Q(Pu,Pv)=Q((I-P)u,(I-P)v).
\]

**Use:** convert finite Weil energy into exterior boundary energy.

---

## Card G — Functional-calculus selection

**Hypotheses:** exterior operators \(B=p(L)+E\), increasing \(p\), bottom transformed gap \(\Delta_p\).  
**Conclusion:** if \(\|E\|<\Delta_p/2\), the Weil ground state is simple and close to the prolate ground state.

---

## Card H — Hyperbolic-tent packet

\[
f_t(u)=2^{-1/2}e^{u/2}1_{[-t/2,t/2]}(u),
\]

\[
h_t(r)=\frac{\cosh(t/2)-\cos(tr)}{r^2+1/4}.
\]

**Use:** exact positive-type finite-prime probe, with explicit pole and Nicolas connections.

---

## Card I — Witt spectral purity

**Hypotheses:** two-parameter support/multiplicity deformation.  
**Conclusion:** among nonnegative nontrivial parameters, \((1,1)\) is the unique point with no scaled ghost spectra.

---

## Card J — Low-order resolvent blindness

**Conclusion:** the first 22 complete-monotonicity signs of the centered zero resolvent on the positive axis hold unconditionally.

**Use:** reject low-order Stieltjes positivity as strong evidence for RH.

---

# Part IV. Computational evidence and its correct interpretation

## 19. Few-prime reconstruction

The internal Connes reproduction constructed finite Weil matrices from:

- the pole;
- the Gamma factor;
- prime powers below the support cutoff.

No zero ordinates entered the matrix. The minimum eigenvector's transform was compared afterward with known zeros.

The observed progression included:

\[
\begin{array}{c|ccc}
x&\text{error at }\gamma_1&\text{error at }\gamma_2&\text{error at }\gamma_3\\ \hline
2&2.3\times10^{-1}&-&-\\
3&8.3\times10^{-5}&7.4\times10^{-3}&5.9\times10^{-2}\\
4&3.4\times10^{-9}&9.4\times10^{-7}&2.0\times10^{-5}\\
5&3.2\times10^{-13}&1.7\times10^{-10}&6.4\times10^{-9}\\
7&1.2\times10^{-18}&2.0\times10^{-15}&1.9\times10^{-13}.
\end{array}
\]

**Verdict:** spectacular finite interpolation/coherent truncation; not an infinite-limit theorem.

## 20. Fixed-window movie

In the window \(8\le t\le35\):

- cutoff \(x=2\): one of five low zeros resolved;
- cutoff \(x=3\): three of five resolved;
- cutoff \(x=5\): all five resolved, with the fifth closest to the moving horizon and therefore least accurate.

This supports the stable horizon

\[
x\approx T/(2\pi).
\]

**Confound:** the original scripts coupled prime cutoff, support width, basis dimension, and working precision. A causal experiment must vary these independently.

## 21. Gap observations

Observed ratios included

\[
\frac{\lambda_2}{\lambda_1}
\approx457,\quad21169,\quad45000
\]

for early cutoffs. The lowest eigenvalue decayed faster than the second, even though both entered a growing near-radical.

**Use:** evidence for relative ground-state isolation.  
**Limit:** \(\lambda_2/\lambda_1\) is not the exact prolate residual-to-gap ratio.

## 22. Shape alignment

Observed normalized angles between the finite ground-state transform and \(\Xi\) decreased approximately

\[
0.2219,
\quad0.1213,
\quad0.06154,
\quad0.02866
\]

for \(x=2,3,5,7\).

A clean exponential law for the minimum eigenvalue in the coupled variable \(x\) was **refuted** by the later sweep. The local slopes wandered and the proposed envelope residual grew.

## 23. Finite Weil positivity

A calibrated finite matrix built from prime and Archimedean data matched a zero-side Gram matrix to relative error about \(8.6\times10^{-5}\), with eigenvalues approximately

\[
0.861,
\quad0.888,
\quad0.912.
\]

Increasing carrier count decreased the smallest eigenvalue modestly; increasing support improved conditioning. Synthetic off-line blocks were indefinite but often swamped by the positive majority.

**Lesson:** finite positivity confirms the instrument, not RH. The finite margin largely measures basis conditioning.

## 24. Failed commutant searches

The following easy categories were tested and did not yield a useful near-symmetry:

- bare differential operators;
- prolate differential operators without arithmetic dressing;
- finite linear combinations of local prime translations/polarizers.

This does not rule out:

- \(E\)-dressed operators;
- all-prime regularized transfer operators;
- boundary functional calculus \(B\approx p(L)\);
- nonlocal scaling-site operators.

## 25. Required factorial redesign

Future computations should independently vary:

\[
A,\qquad N,\qquad P_{\max},\qquad\text{precision}.
\]

Required controls:

1. pole + Gamma only;
2. primitive primes only;
3. repeated prime powers only;
4. full von Mangoldt sum;
5. shuffled \(\log p\) locations;
6. density-matched synthetic clocks;
7. true finite prolate candidate rather than only the Hermite limit;
8. interval-certified matrix entries and eigenvalue gaps.

---

# Part V. Ten next probes with pass/fail criteria

## Probe 1 — Certified parity gap

Compute

\[
\Delta_{\rm par}(\lambda,N)
=\lambda_1^-(\lambda,N)-\lambda_1^+(\lambda,N)
\]

from cutoff-free entries.

- **Pass:** a positive lower bound survives increasing \(N\) and \(\lambda\), after subtracting rigorous truncation error.
- **Ambiguous:** positive central value but enclosure crosses zero.
- **Fail:** certified parity crossing or persistent negative gap.

## Probe 2 — Parity Loewner component audit

Build \(L_\phi\), \(L_{x\phi}\), and the even Schur complement separately for pole, Gamma, primitive, and repetition sources.

- **Pass:** one component supplies a uniform ordering that survives assembly.
- **Fail:** every component changes sign uncontrollably and no comparison survives.

## Probe 3 — Total-positive domination

Choose an optimized positive Cauchy--Stieltjes reference tail \(R\) and calculate

\[
\mathfrak D_{\rm TP}=2\|K\|/(r_2-r_1).
\]

- **Pass:** \(\mathfrak D_{\rm TP}<1\).
- **Useful failure:** identify the precise frequency block or prime sector responsible for \(\mathfrak D_{\rm TP}\gg1\).

## Probe 4 — Boundary functional calculus

Compute \(B_\lambda,L_\lambda\) on true prolate/Witt-jet radical directions.

- **Pass:** \(\mathfrak S_d(\lambda)\to0\) for low-degree monotone \(p\).
- **Fail:** best residual remains comparable to the transformed bottom gap.

## Probe 5 — \(E\)-amplified leakage

Prove or numerically calibrate a norm inequality

\[
\|E\ell\|_{\mathrm{Weil}^*}
\le C\lambda^M\|\ell\|_{\mathcal X_\lambda}.
\]

- **Pass:** polynomial amplification against exponentially small prolate leakage.
- **Fail:** an explicit leakage sequence is amplified exponentially or loses phase cancellation.

## Probe 6 — Mixed quartic arithmetic expansion

Expand

\[
\operatorname{Tr}q_*(\widetilde G)^2
\]

symbolically on the prime side.

- **Pass:** the unknown fourth-order additive-correlation term cancels or has a favorable one-sided coefficient.
- **Fail:** it survives with the same strength as in \(m_4\).

## Probe 7 — Depth-sensitive polynomial optimization

Solve

\[
\min_q\int q^2d\mu
\]

subject to enhanced penalties on the pair spectrum \(1\pm\sinh u/u\) for \(u\ge U\).

- **Pass:** a rigorous moment inequality yields a shrinking horizontal corridor.
- **Fail:** shallow pairs remain extremal for every accessible degree.

## Probe 8 — Hyperbolic pole-neutral curvature basis

Use modulated \(F_{t_1,t_2}\) packets and maximize projective curvature.

- **Pass:** synthetic off-line block onset matches (1.2) with improved signal-to-background.
- **Fail:** pole neutrality destroys localization or the basis becomes ill-conditioned.

## Probe 9 — Witt-jet boundary Gram

Use

\[
\partial_a^r\partial_b^qE_{a,b}(h_\lambda)|_{1,1}
\]

as radical directions and compare interior and exterior Weil Gram matrices.

- **Calibration:** radical cut equality.
- **Pass:** the physical \((0,0)\) direction becomes the unique boundary minimum with a growing generalized gap.
- **Fail:** a mixed support/repetition jet has lower boundary energy.

## Probe 10 — Semilocal geometric comparison

Construct one/two-prime transverse or tropical cohomology and compare its pairing with the known semilocal Sonin/prolate form.

- **Pass:** an independently derived Hodge pairing reproduces the same local Weil sign.
- **Fail:** the model needs ad hoc corrections or misses the Gamma/pole terms.

---

# Part VI. Pothole registry

## Pothole 1 — projecting zeros onto the line

Never replace \(z_\rho\) by \(\gamma\) before RH is proved.

## Pothole 2 — equation-to-inequality alchemy

Functional equations, explicit formulas, and factorization identities yield equalities. A sign requires inertia, polarization, vanishing, total positivity, or another independent mechanism.

## Pothole 3 — regularized scalar equals count

A finite regularized value can be negative. It cannot substitute for a dimension or norm.

## Pothole 4 — finite self-adjointness

Self-adjoint operators on finite intervals are cheap. The arithmetic content lies in the global limit and the characteristic function.

## Pothole 5 — zero-position accuracy equals function convergence

Finite extremizers are designed to interpolate the zero set. Accurate crossings do not imply local-uniform convergence to \(\Xi\).

## Pothole 6 — tiny Rayleigh quotient equals correct eigenvector

A large near-radical contains many tiny-energy vectors. Selection depends on residual divided by complementary gap.

## Pothole 7 — absolute prime summation

The prime weights are not absolutely summable at the critical line. Triangle inequalities erase the cancellation the theorem needs.

## Pothole 8 — all moments imply RH

All-moment density methods may prove density one while leaving a sparse exceptional set.

## Pothole 9 — arbitrary Euler deformation is lawful

Generic support weights create scaled spectra and natural boundaries. Automorphic/local-global compatibility is a substantive constraint.

## Pothole 10 — geometric vocabulary creates geometry

Naming an absolute surface, Hodge index, or unitary flow does not construct it. Positivity must be earned independently of the zeros.

---

# Part VII. Final claim ledger

## External, current, load-bearing facts

1. RH remains open as a Clay Millennium Prize Problem [R12].
2. Weil positivity is equivalent to RH.
3. Connes's current analytic strategy reduces to finite ground-state simplicity/evenness and prolate-to-Weil minimizer comparison [R1].
4. Connes--van Suijlekom prove real-rootedness of the ground-state transform under the simple/isolated/even hypothesis [R2].
5. Groskin proves an exact finite Guinand--Weil dictionary and a strictly totally positive Archimedean tail [R4].
6. Alpöge--Furman prove more than two thirds simple and on-line, and at least five sixths distinct [R5].
7. Nicolas's primorial inequality is equivalent to RH [R10].

## Derived here; novelty unverified

1. Projective-curvature coefficient (1.2).
2. Exact finite-band pair eigenvalues (4.2)--(4.3).
3. Two-dimensional stable resolution cone (4.8).
4. Depth moment functions and defect polynomial.
5. Mixed quartic sufficient condition (5.6).
6. Parity-crossing theorem and parity-gap reduction.
7. Parity Loewner decomposition (6.5)--(6.6).
8. Archimedean-tail simple-even ground-state corollary.
9. Total-positive perturbation certificate.
10. Radical-cut identity.
11. Functional-calculus selection theorem.
12. Hyperbolic-tent and pole-neutral packet formulas.
13. Witt/necklace factorization and spectral-purity rigidity.
14. First 22 unconditional Stieltjes signs.

## Observed, not proved

1. Few-prime finite minimizers recover low zeros with remarkable accuracy.
2. The ground-state transform aligns increasingly with \(\Xi\) at small cutoffs.
3. The relative bottom gap increases strongly in early experiments.
4. The vertical resolution frontier tracks \(T\approx2\pi x\).
5. One synthetic off-line block is indefinite but can be swamped by the on-line majority.
6. Bare differential and finite local-polarizer commutant searches fail.

## Refuted

1. Functional symmetry alone forces RH.
2. Zeta regularization preserves positivity.
3. Finite self-adjointness is arithmetic evidence.
4. Accurate finite zero crossings prove \(\theta_\lambda\to\Xi\).
5. A tiny minimum eigenvalue identifies the correct ground direction.
6. Generic powerset deformation gives a lawful smooth \(L\)-function family.
7. A clean \(e^{-4\pi x}\) law holds in the coupled small-cutoff variable.
8. Operator-norm summability of incoming prime shells is plausible.

## Conjectured, verdict-changing

1. \(\Delta_{\rm par}(\lambda)>0\) uniformly.
2. \(B_\lambda\approx p_\lambda(L_\lambda)\) at the bottom of the spectrum.
3. The \(E\)-amplified leakage estimate holds with polynomial loss.
4. The mixed quartic prime expansion contains useful cancellation.
5. Repeated prime powers supply a coercive baseline beyond the Nicolas scalar setting.
6. A transverse/tropical Hodge theory for the arithmetic square supplies independent polarization.

## Dark

The global independent mechanism forcing

\[
W\succeq0
\]

or, on the stronger Connes route, forcing both

\[
\Delta_{\rm par}>0
\]

and

\[
B_\lambda\approx p_\lambda(L_\lambda)
\]

at every scale.

---

# Final research directive

The program should now allocate effort in this order:

1. **Parity gap:** it is the narrowest exact missing theorem in the finite real-root engine.
2. **Mixed quartic trace:** it offers the best chance of a genuine unconditional theorem below RH.
3. **Boundary functional calculus:** it is the sharpest formulation of the minimizer-selection wall.
4. **Pole-neutral hyperbolic packets:** they provide a transparent, exact, reusable test basis.
5. **Independent geometry:** continue only when the proposed cohomology supplies a metric and Hodge sign before the explicit formula is invoked.

The governing discipline is:

\[
\boxed{
\text{No new identity counts as progress unless it carries a new inequality, discriminator, or independently positive structure.}
}
\]

The tide has already risen: the explicit formula became a finite Hermitian matrix; inertia raised the unconditional line proportion above two thirds; total positivity solves the Archimedean tail model; parity reduces simplicity to one inequality; boundary geometry isolates the selection defect; and the mixed quartic supplies a concrete next theorem target.

The summit remains:

\[
\boxed{
\text{make the one Hermitian form positive for a reason that exists before the zeros are known.}
}

---

# Companion verification script

The file `rh_master_checks.py` checks:

- Witt/necklace coefficient identities through order ten;
- spectral-purity equations;
- parity Loewner decomposition;
- exact Paley--Wiener off-line eigenvalues;
- the local depth defect polynomial;
- the hyperbolic-tent transform;
- the Christoffel polynomial and \(5/36\) value;
- the 22-sign resolvent-blindness threshold.

It is a calibration artifact, not a proof of RH.