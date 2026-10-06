# Continuity audit of the finite PSD-boundary claim

**Date:** 2026-10-06  
**Status:** independent numerical audit / correction of finite-scope wording. RH remains open.

This note audits C84 / \`PRIME_KERNEL_PSD_BOUNDARY.md\` at commit
\`7b334f864cb52f1fe2cc59f3ee3fb15e8100f07d\`.

## 1. The structural t=0 null cannot diagnose the boundary

Every screw kernel in this family has

\[
K(0,t)=0.
\]

Therefore the full sampled matrix is singular for **every** arithmetic weight
choice and every exponent tilt. Consequently

\[
\lambda_{\min}(K)=0
\]

at the critical data does not by itself show that the arithmetic point lies
on a distinguished boundary of the PSD cone: the entire family already lies
on the structural boundary caused by the zero row/column whenever it is PSD.

The meaningful finite-dimensional diagnostic is the quotient/reduced matrix

\[
K^\circ=K[\{t_i>0\},\{t_j>0\}].
\]

## 2. The reduced critical matrix is strictly positive definite

Using the exact same evaluator and the working grid

\[
T=8,\qquad \Delta t=0.04,
\]

the smallest eigenvalue of the reduced matrix is

\[
\boxed{
\lambda_{\min}(K^\circ_0)
\approx 0.004671850652709.
}
\]

Hence, by continuity of finite-matrix eigenvalues, there must be a nonzero open
interval of exponent tilts around \(\epsilon=0\) on which the reduced matrix
remains PSD.

This immediately rules out the literal finite-grid statement

> every nonzero tilt destroys positivity.

## 3. The PSD interval is real but extremely narrow

For the finite-place tilt used by the existing script,

\[
w_n(\epsilon)
=
\Lambda(n)n^{-1/2-\epsilon},
\]

with the Archimedean block held fixed, bisection of the reduced smallest
eigenvalue gives approximately

\[
\boxed{
-8.27\times10^{-7}
<
\epsilon
<
2.30\times10^{-6}
}
\]

on the \(T=8,\Delta t=0.04\) grid.

Inside this interval the reduced matrix remains positive definite. Outside it
a genuine nontrivial negative mode appears.

Thus the observed phenomenon should be described as **extreme finite-window
sensitivity near the critical exponent**, not exact isolation of epsilon=0 on
a fixed finite grid.

## 4. The admissible interval appears to collapse rapidly with the horizon

Repeating the same reduced-matrix calculation at fixed \(\Delta t=0.04\) gives:

| horizon T | lambda_min at epsilon=0 | negative-side crossing | positive-side crossing |
|---:|---:|---:|---:|
| 4 | 0.00678353 | -3.87e-5 | +1.25e-4 |
| 6 | 0.00560241 | -5.59e-6 | +1.15e-5 |
| 8 | 0.00467185 | -8.27e-7 | +2.30e-6 |
| 10 | 0.00367186 | -2.31e-7 | +3.81e-7 |

These are ordinary double-precision exploratory values, not interval
certificates.

The important new conjectural pattern is therefore

\[
\boxed{
\delta_L^\pm\to0
\quad\text{as}\quad L\to\infty,
}
\]

where \((-\delta_L^-,\delta_L^+)\) is the maximal exponent-tilt interval for
which the reduced sampled kernel remains PSD.

That is a coherent finite-window manifestation of a possible global
knife-edge:

\[
\boxed{
\bigcap_{L>0}
\{\epsilon:K_{\epsilon,L}\succeq0\}
=
\{0\}.
}
\]

Proving this statement would be much stronger and logically correct. It is
not established by the present finite computations.

## 5. The current exponent sweep is not the fully completed Suzuki shift

The script changes only the finite arithmetic weights

\[
\Lambda(n)n^{-1/2}
\mapsto
\Lambda(n)n^{-1/2-\epsilon}
\]

while keeping fixed:

- the pole term;
- the Gamma/digamma linear term;
- the Lerch/Gamma block.

Therefore this is a **finite-place-only mismatch deformation** around the
critical completed kernel.

It should not be identified without qualification with the full shifted
Suzuki family

\[
\frac{\xi'}{\xi}\left(\frac12+\omega-iz\right),
\]

whose Archimedean contribution shifts together with the prime weights.

Likewise it is not by itself the full affine/Bost-Connes thermal deformation
of the completed arithmetic object.

The correct next comparison is to run two distinct deformations:

1. **finite-place-only tilt** — the current experiment;
2. **fully completed shift** — finite and infinite local factors moved
   coherently.

If the shrinking-window knife edge survives the completed deformation, the
interpretation becomes substantially stronger.

## 6. Single-prime mutation has the same continuity issue

At a finite reduced grid, strict positive definiteness at the exact arithmetic
weights also implies an open neighborhood in weight space remains PSD.

For the \(T=8,\Delta t=0.04\) grid, infinitesimal mutations of the weight at
\(n=2\) remain PSD; the existing 2-percent mutation examples are far outside
that small neighborhood.

Thus the correct finite claim is:

> sufficiently large declared mutations break positivity, and the permissible
> neighborhood appears small.

The stronger statement that **every** nonzero single-weight mutation breaks
finite-window positivity cannot hold when the reduced exact matrix is
strictly positive definite.

## 7. What remains genuinely striking

The correction does not erase the observed rigidity.

The numerical evidence now points to a sharper and mathematically plausible
phenomenon:

> finite windows have a small positive stability neighborhood, but its width
> may collapse to zero as the arithmetic horizon tends to infinity.

That would reconcile:

- ordinary finite-dimensional continuity;
- the observed enormous sensitivity;
- the global RH-equivalent kernel being slack-free.

The verdict-changing theorem target is therefore an asymptotic stability-radius
result, not a finite-grid exact-boundary statement.

## 8. Revised theorem target

Define, after removing the structural \(t=0\) null and taking all finite test
sets in \([0,L]\),

\[
\mathcal E_L
=
\{\epsilon:
K_{\Psi_\epsilon}\succeq0
\text{ on }[0,L]\}.
\]

For the declared deformation, prove or refute

\[
\boxed{
0\in\operatorname{int}\mathcal E_L
\quad\text{for each finite }L,
\qquad
\bigcap_{L>0}\mathcal E_L=\{0\}.
}
\]

A stronger quantitative target is an analytic upper bound

\[
\operatorname{rad}(\mathcal E_L)
\le Ce^{-cL}
\]

or whatever the true decay law is.

This would turn the current numerical "knife edge" into a rigorous global
rigidity statement without violating finite-dimensional continuity.
