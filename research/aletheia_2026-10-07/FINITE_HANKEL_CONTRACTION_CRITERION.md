# Finite-Hankel contraction criterion: an exact finite-horizon RH interface

**Date:** 2026-10-07  
**Branch:** \`aletheia/finite-hankel-contraction-frontier-2026-10-07\`  
**Status:** theorem/reduction from Suzuki's kernel formula and standard Hardy-space facts. No RH assumption. The final RH equivalence uses Suzuki's Proposition 1.2.  
**Claim discipline:** this does **not** prove RH. It converts the global innerness/zero-free problem into a family of finite-horizon operator-norm inequalities.

---

## 0. Executive result

Let

\[
\Theta_\omega(z)
=
\frac{\xi(\frac12-\omega-iz)}
     {\xi(\frac12+\omega-iz)},
\qquad \omega>0,
\]

and let Suzuki's locally defined multiplicative Hankel kernel be

\[
(H_{\omega,a}f)(x)
=
\int_0^a h_\omega(xy)f(y)\,dy,
\qquad 0<x<a.
\]

For every finite \(a\), this operator is well-defined, bounded, compact, and self-adjoint for every \(\omega>0\).

The key theorem is

\[
\boxed{
\Theta_\omega\text{ is inner in }\mathbb C_+
\iff
\|H_{\omega,a}\|_{2\to2}\le 1
\quad\text{for every finite }a>0.
}
\]

Suzuki proves the forward implication through his global isometry \(H_\omega\).
The reverse implication follows from finite-horizon exhaustion plus a Hardy-space multiplier argument.

Combining this with Suzuki's Proposition 1.2 gives, for \(0<\omega_0<1/2\),

\[
\boxed{
\zeta(s)\neq0\quad(\Re s>\tfrac12+\omega_0)
}
\]

if and only if

\[
\boxed{
\|H_{\omega,a}\|\le1
\quad
\text{for every }a>0
\text{ and every }\omega>\omega_0.
}
\]

Hence

\[
\boxed{
\mathrm{RH}
\iff
\|H_{\omega,a}\|\le1
\quad
\forall\,\omega>0,\ \forall\,a>0.
}
\]

This is an exact finite-horizon contraction criterion.

Because the discrete-conductor factorization gives

\[
H_{\omega,a}
=
V_{\omega,a}^{*}\,
\mathbb G_{\omega,a}\,
V_{\omega,a},
\]

the criterion is simultaneously an exact statement about the finite conductor system active below \(n<a^2\).

---

## 1. Inputs from Suzuki

We use only the following published facts.

### 1.1 Support

Suzuki's arithmetic kernel satisfies

\[
\boxed{
h_\omega(x)=0
\qquad(0<x<1).
}
\]

### 1.2 Mellin transform in the safe half-plane

With the shifted Mellin transform

\[
(\mathcal F_{1/2}f)(z)
=
\int_0^\infty
f(x)x^{1/2+iz}\frac{dx}{x},
\]

Suzuki's Proposition 2.1 gives

\[
\boxed{
\int_0^\infty
h_\omega(x)x^{1/2+iz}\frac{dx}{x}
=
\Theta_\omega(z)
}
\]

initially for sufficiently large \(\Im z\).

Consequently, for compactly supported \(f\),

\[
\boxed{
\mathcal F_{1/2}(H_\omega f)(z)
=
\Theta_\omega(z)
\mathcal F_{1/2}f(-z)
}
\]

in that safe half-plane whenever the left side is formed locally.

### 1.3 Innerness gives an isometry

Suzuki's Lemma 4.1 proves that if \(\Theta_\omega\) is inner in \(\mathbb C_+\), then

\[
H_\omega:L^2(0,\infty)\to L^2(0,\infty)
\]

extends to an isometry satisfying the transform identity.

Therefore every compression

\[
H_{\omega,a}=P_aH_\omega P_a
\]

is a contraction.

This is the easy implication.

---

## 2. Reverse implication: finite contractivity forces a global \(L^2\) contraction

Assume

\[
\boxed{
\|H_{\omega,a}\|\le1
\qquad
\forall a>0.
}
\]

Let

\[
f\in C_c(0,\infty)
\]

and choose \(b\) with

\[
\operatorname{supp}f\subset(0,b).
\]

For every \(a\ge b\), the local integral defining \(H_\omega f\) satisfies

\[
P_aH_\omega f
=
H_{\omega,a}f.
\]

Hence

\[
\|P_aH_\omega f\|_2
\le
\|f\|_2.
\]

The left side is monotone in \(a\). Therefore monotone convergence gives

\[
\boxed{
H_\omega f\in L^2(0,\infty),
\qquad
\|H_\omega f\|_2\le\|f\|_2.
}
\]

Since \(C_c(0,\infty)\) is dense in \(L^2\), the locally defined Hankel transform extends uniquely to a global contraction

\[
\boxed{
H_\omega:L^2(0,\infty)\to L^2(0,\infty).
}
\]

No innerness has been assumed.

---

## 3. The multiplicative inversion that exposes a Hardy multiplier

Define the unitary involution

\[
\boxed{
(Jg)(x)=x^{-1}g(1/x).
}
\]

Indeed,

\[
\int_0^\infty |Jg(x)|^2dx
=
\int_0^\infty |g(u)|^2du.
\]

A direct change of variables gives

\[
\boxed{
\mathcal F_{1/2}(Jg)(-z)
=
\mathcal F_{1/2}g(z).
}
\]

Now take

\[
g\in C_c(1,\infty),
\qquad
f=Jg.
\]

Then

\[
f\in C_c(0,1).
\]

Because \(h_\omega(xy)=0\) whenever \(xy<1\), for \(x<1\) and \(y<1\),

\[
h_\omega(xy)=0.
\]

Thus

\[
\boxed{
H_\omega Jg
\text{ is supported in }[1,\infty).
}
\]

Under \(\mathcal F_{1/2}\), \(L^2(1,\infty)\) identifies with the Hardy space \(H^2(\mathbb C_+)\).

Therefore

\[
\mathcal F_{1/2}(H_\omega Jg)\in H^2(\mathbb C_+).
\]

In the safe half-plane, Suzuki's transform identity becomes

\[
\begin{aligned}
\mathcal F_{1/2}(H_\omega Jg)(z)
&=
\Theta_\omega(z)
\mathcal F_{1/2}(Jg)(-z)\\
&=
\boxed{
\Theta_\omega(z)\mathcal F_{1/2}g(z).
}
\end{aligned}
\]

Moreover,

\[
\|\mathcal F_{1/2}(H_\omega Jg)\|_{H^2}
\le
\|\mathcal F_{1/2}g\|_{H^2}.
\]

So multiplication by \(\Theta_\omega\), initially on the dense set

\[
\mathcal F_{1/2}C_c(1,\infty)
\subset H^2(\mathbb C_+),
\]

extends with operator norm at most one.

---

## 4. Hardy multiplier conclusion

Multipliers of \(H^2(\mathbb C_+)\) are precisely \(H^\infty(\mathbb C_+)\), and the multiplier norm equals the \(H^\infty\) norm.

For completeness, one can identify the symbol without presupposing analyticity of the original meromorphic quotient:

1. let \(T\) be the bounded extension of the multiplication rule above;
2. choose one zero-free \(F_0\in H^2(\mathbb C_+)\), for example a scalar multiple of
   \[
   F_0(z)=\frac1{z+i};
   \]
3. define
   \[
   \theta(z)=\frac{(TF_0)(z)}{F_0(z)}.
   \]
   Then \(\theta\) is analytic in \(\mathbb C_+\);
4. in Suzuki's safe half-plane,
   \[
   \theta(z)=\Theta_\omega(z);
   \]
5. by meromorphic/analytic continuation, the original \(\Theta_\omega\) has no uncancelled pole in \(\mathbb C_+\) and equals \(\theta\) there.

Thus

\[
\boxed{
\Theta_\omega\in H^\infty(\mathbb C_+),
\qquad
\|\Theta_\omega\|_\infty\le1.
}
\]

Suzuki's functional equation gives the unimodular boundary relation

\[
|\Theta_\omega(u)|=1
\]

for almost every real \(u\).

Therefore

\[
\boxed{
\Theta_\omega
\text{ is inner in }\mathbb C_+.
}
\]

This proves the reverse implication.

---

## 5. Finite-Hankel contraction theorem

Combining Sections 1--4:

### Theorem

For every fixed \(\omega>0\),

\[
\boxed{
\Theta_\omega
\text{ inner in }\mathbb C_+
\iff
\|H_{\omega,a}\|\le1
\text{ for every }a>0.
}
\]

The theorem is deliberately stated using \(\le1\), because that is the exact global criterion.

When the support/noncompactness argument used by Suzuki applies, compact self-adjointness upgrades the finite inequalities to

\[
\|H_{\omega,a}\|<1.
\]

At the critical endpoint \(\omega=1/2\), the companion endpoint work on this branch already establishes this strict inequality.

---

## 6. Exact zero-free criterion

Suzuki's Proposition 1.2 states that for \(\omega_0>0\),

\[
\zeta(s)\neq0
\qquad
(\Re s>\tfrac12+\omega_0)
\]

is equivalent to innerness of

\[
\Theta_\omega
\]

for every

\[
\omega>\omega_0.
\]

Using the finite-Hankel theorem:

\[
\boxed{
\zeta(s)\neq0
\quad(\Re s>\tfrac12+\omega_0)
}
\]

if and only if

\[
\boxed{
\|H_{\omega,a}\|\le1
\quad
\forall\,a>0,\ \forall\,\omega>\omega_0.
}
\]

Letting \(\omega_0\downarrow0\) gives

\[
\boxed{
\mathrm{RH}
\iff
\|H_{\omega,a}\|\le1
\quad
\forall\,\omega>0,\ \forall\,a>0.
}
\]

This is not merely a heuristic norm test. It is an exact reformulation once Suzuki's Proposition 1.2 is taken as input.

---

## 7. Insert the discrete-conductor factorization

The previous branch proved

\[
\boxed{
H_{\omega,a}
=
V_{\omega,a}^{*}
\mathbb G_{\omega,a}
V_{\omega,a},
}
\]

with

\[
\mathfrak E_{\omega,a}
=
\bigoplus_{n<a^2}
\left[
L^2(0,a/\sqrt n)\otimes W_n
\right],
\]

where

\[
\dim W_n=\varphi(n).
\]

Therefore the zero-free criterion becomes

\[
\boxed{
\left\|
V_{\omega,a}^{*}
\left[
\bigoplus_{n<a^2}
(\mathcal G_{\omega,a/\sqrt n}\otimes I_{W_n})
\right]
V_{\omega,a}
\right\|
\le1
}
\]

for every required \((\omega,a)\).

At \(\omega=1/2\),

\[
V_{1/2,n,a}f
=
n^{-1/2}T_{n,a}f\otimes\eta_n,
\]

so every primitive exact-conductor mode at level \(n\) has the same half-density coupling \(n^{-1/2}\).

Thus:

\[
\boxed{
\text{RH can be phrased as global passivity of every finite exact-conductor assembly.}
}
\]

The arithmetic state space at each finite horizon is finite in conductor content. The only remaining infinite piece is the universal Archimedean channel, for which the critical and subcritical mode expansions are already explicit.

---

## 8. Local continuation below half density is unconditional at every fixed horizon

Fix finite \(a>1\).

The formula

\[
h_\omega(x)
=
\frac1x
\sum_{n\le x}
c_\omega(n)g_\omega(n/x)
\]

contains only finitely many conductor seams on

\[
1\le x\le a^2.
\]

On every compact parameter interval

\[
0<\omega_-\le\omega\le\omega_+,
\]

the seam singularity

\[
(1-t)^{\omega-1}
\]

is dominated by the integrable majorant

\[
(1-t)^{\omega_--1}.
\]

All arithmetic coefficients \(c_\omega(n)\) depend continuously on \(\omega\).

Hence dominated convergence gives

\[
\boxed{
\|h_\omega-h_{\omega_*}\|_{L^1([1,a^2])}
\to0
\quad(\omega\to\omega_*).
}
\]

The Schur estimate gives

\[
\boxed{
\|H_{\omega,a}-H_{\omega_*,a}\|
\le
a
\|h_\omega-h_{\omega_*}\|_{L^1([1,a^2])}.
}
\]

Therefore

\[
\boxed{
\omega\mapsto H_{\omega,a}
\text{ is operator-norm continuous for every fixed finite }a.
}
\]

At the critical endpoint the previous work established

\[
\|H_{1/2,a}\|<1.
\]

Consequently, for every fixed finite \(a\), there exists

\[
\varepsilon(a)>0
\]

such that

\[
\boxed{
\|H_{\omega,a}\|<1
\qquad
\left(\frac12-\varepsilon(a)<\omega\le\frac12\right).
}
\]

This is unconditional.

So **no finite conductor horizon is itself pinned to the half-density wall**.
The RH difficulty is the loss of control as the horizon tends to infinity.

---

## 9. Define the finite contraction frontier

Use

\[
\delta=\frac12-\omega.
\]

For each finite horizon \(a\), define

\[
\boxed{
\Delta(a)
=
\sup
\left\{
d\in[0,\tfrac12]:
\|H_{1/2-\delta,a}\|\le1
\ \text{for every }0\le\delta<d
\right\}.
}
\]

The endpoint strict-contraction theorem and parameter continuity imply

\[
\boxed{
\Delta(a)>0
\qquad
\text{for every finite }a.
}
\]

For \(0<d<1/2\), Suzuki Proposition 1.2 plus the finite-Hankel theorem gives

\[
\boxed{
\zeta(s)\neq0
\quad(\Re s>1-d)
}
\]

if and only if

\[
\boxed{
\Delta(a)\ge d
\qquad
\forall a>0.
}
\]

Therefore

\[
\boxed{
\mathrm{RH}
\iff
\Delta(a)=\frac12
\qquad
\forall a>0.
}
\]

This isolates the wall:

\[
\boxed{
\text{not finite-horizon existence, but uniform survival of the contraction frontier as }a\to\infty.
}
\]

---

## 10. Any off-line zero forces a finite norm failure

Suppose RH is false.

Then there exists a zero-free half-plane claimed by RH that fails.
By Suzuki's Proposition 1.2, for a suitable \(\omega_0>0\), not every

\[
\Theta_\omega,\qquad \omega>\omega_0,
\]

is inner.

By the finite-Hankel theorem, for at least one such \(\omega\) there must therefore exist a **finite**

\[
a>0
\]

such that

\[
\boxed{
\|H_{\omega,a}\|>1.
}
\]

Since \(H_{\omega,a}\) is compact and self-adjoint, this means a finite truncation has an eigenvalue with

\[
|\lambda|>1.
\]

By continuity in \(a\) and/or \(\omega\), the frontier is crossed through

\[
\boxed{
\lambda=+1
\quad\text{or}\quad
\lambda=-1.
}
\]

So an off-line zero cannot remain an inaccessible infinite-horizon ghost:

\[
\boxed{
\text{it forces a finite conductor assembly to lose passivity somewhere.}
}
\]

This is an exact existential statement, not yet a quantitative localization of the offending horizon.

---

## 11. Relation to the subcritical conductor gain mode

The previous conductor discrepancy work gives

\[
A_\delta(s)
=
\frac{\zeta(s+\delta)}
     {\zeta(s+1-\delta)}.
\]

A denominator zero

\[
\rho=\beta+i\gamma
\]

produces, when uncancelled, a pole at

\[
s_\rho
=
\rho-1+\delta,
\]

whose real part is

\[
\eta
=
\beta-1+\delta.
\]

For

\[
\beta>1-\delta,
\]

\[
\eta>0.
\]

The time-domain conductor response then contains a growing mode of envelope

\[
e^{\eta t}.
\]

Since the finite multiplicative horizon \(a\) corresponds to log-Hankel time up to

\[
t=2\log a,
\]

the natural gain scale is

\[
\boxed{
e^{2\eta\log a}
=
a^{2\eta}.
}
\]

This matches the finite-contraction picture: an upper-half-plane pole should eventually drive a finite Hankel singular/eigenvalue beyond unit gain.

Turning this scaling statement into a uniform lower bound for \(\|H_{\omega,a}\|\) is a separate theorem target. It should be attacked with Hardy reproducing-kernel test states or a residue decomposition of the log-Hankel kernel.

---

## 12. The new proof-bearing target

The old endpoint target was:

> extend Suzuki's canonical determinant system to \(\omega=1/2\).

That remains worthwhile, but it is not itself RH-sensitive because \(\Theta_{1/2}\) is already unconditionally inner.

The sharper target is now:

### Finite conductor passivity theorem

For every

\[
0<\delta<1/2,
\]

prove

\[
\boxed{
\|H_{1/2-\delta,a}\|\le1
\qquad
\forall a>0
}
\]

directly from the discrete-conductor / SUCC-FUCC realization, without using zeta zero locations or assuming RH.

Even a uniform result for

\[
0\le\delta<d
\]

with one fixed

\[
d>0
\]

would yield the zero-free half-plane

\[
\boxed{
\Re s>1-d.
}
\]

Pushing \(d\) to \(1/2\) is RH.

This target is finite at every stage and has a decisive failure mode: an eigenvalue exits \([-1,1]\).

---

## 13. Critical-margin perturbation route

Define the unconditional critical margin

\[
\boxed{
g(a)=1-\|H_{1/2,a}\|>0.
}
\]

For a subcritical tilt \(\delta\), define

\[
\boxed{
L_\delta(a)
=
\|H_{1/2-\delta,a}-H_{1/2,a}\|.
}
\]

Then the elementary perturbation inequality gives the sufficient condition

\[
\boxed{
L_\delta(a)<g(a)
\Longrightarrow
\|H_{1/2-\delta,a}\|<1.
}
\]

Therefore a concrete first attack is to understand both quantities asymptotically:

1. **critical escape margin**
   \[
   g(a);
   \]

2. **subcritical tilt cost**
   \[
   L_\delta(a).
   \]

The naive Schur estimate will almost certainly be too lossy at large \(a\), but it provides a calibrated baseline.

The discrete-conductor realization gives a more structured decomposition of \(L_\delta(a)\) into:

- coupling deformation of each exact-conductor block;
- change of the universal Archimedean block;
- interaction of the distinguished subcritical unstable mode with the arithmetic completion zero.

That is where a proof can gain over absolute-value estimates.

---

## 14. Why this is better aligned with Suzuki 2026

Suzuki's 2026 screw-function paper returns to finite intervals and proves unconditional finite-interval operator statements, while emphasizing that RH is equivalent to positivity/nondegeneracy surviving at every interval length and that the difficult information is in the large-interval limit.

The contraction frontier above has the same geometry:

\[
\boxed{
\text{every fixed finite horizon has room below the critical endpoint;}
}
\]

\[
\boxed{
\text{the wall is whether that room survives uniformly as the horizon grows.}
}
\]

This creates a concrete interface between:

- the 2012 finite Hankel/canonical system;
- the discrete conductor SUCC realization;
- the 2026 finite-interval Weil/screw-function program.

A later round should construct the precise intertwiner, if any, between the Hankel contraction frontier and the lowest-eigenvalue frontier of the localized Weil operator.

---

## 15. Claim ledger

### Disclosed / proved here, modulo standard Hardy-space multiplier theory

- finite contractivity for all horizons implies a global \(L^2\) contraction;
- via \(Jg(x)=x^{-1}g(1/x)\), this yields a contractive Hardy multiplier;
- hence \(\Theta_\omega\) is inner;
- combined with Suzuki's forward implication:
  \[
  \Theta_\omega\text{ inner}
  \iff
  \|H_{\omega,a}\|\le1\ \forall a.
  \]
- fixed-horizon operator-norm continuity in \(\omega>0\);
- unconditional nonzero subcritical neighborhood at every finite horizon.

### Corroborated by Suzuki

- Proposition 2.1 Mellin identity;
- Lemma 4.1 innerness \(\Rightarrow\) global isometry;
- Proposition 1.2 zero-free half-plane \(\Leftrightarrow\) innerness of the parameter family;
- finite compactness for weakly singular kernels.

### Conjectured / next proof debt

- quantitative relation between an off-line zero \(\rho\) and the first horizon \(a\) where the norm crosses one;
- sharp large-\(a\) asymptotics of
  \[
  g(a)=1-\|H_{1/2,a}\|;
  \]
- a structured bound on the subcritical tilt cost stronger than the Schur absolute-value bound;
- an exact intertwiner to Suzuki's 2026 localized Weil/screw operator.

### Refuted framing

- “the critical endpoint itself is the RH wall.”

It is not. It is the last unconditional inner point and therefore the correct launch surface for a subcritical finite-horizon continuation.

---

## 16. Immediate experimental/proof program

1. Compute
   \[
   \|H_{\omega,a}\|
   \]
   with seam-aware quadrature on a grid of \((a,\delta)\).

2. Track the leading positive and negative eigenvalues separately; the norm may cross through either sign.

3. Measure the critical margin
   \[
   g(a).
   \]

4. Measure
   \[
   \partial_\delta H_{1/2-\delta,a}|_{\delta=0}
   \]
   and its matrix element against the leading critical eigenvector.

5. Decompose that derivative by exact conductor \(n\), prime support, and Archimedean mode \(m\).

6. Compare the observed large-\(a\) growth with the exact conductor discrepancy
   \[
   E_\delta(a^2).
   \]

7. Build a certified tail bound so finite arithmetic/modal matrices become rigorous upper/lower norm enclosures, not just plots.

8. Attack the first verdict-changing theorem:
   \[
   \inf_{a>0}\Delta(a)>0?
   \]
   Any positive answer yields a genuine improved zero-free half-plane.

The ultimate theorem is

\[
\boxed{
\inf_{a>0}\Delta(a)=\frac12.
}
\]

That statement is equivalent in force to RH, but unlike a generic restatement it is now expressed in the exact finite conductor machinery we have constructed.
