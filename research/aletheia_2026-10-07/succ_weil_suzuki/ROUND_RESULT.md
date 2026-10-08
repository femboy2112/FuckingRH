# Round result: an exact bridge and further work on the completed form

**Date:** 2026-10-07. **Branch:** `research/succ-weil-suzuki-rigorous-bridge-2026-10-07`.  
**Parent:** `987a67d891879e966c9e0c7fb533a5dc74f805fd`.  
**Verdict:** the succ/conductor route now has a complete normalized smooth-core derivative into the full Weil form. The exact Gamma/prime energy has been retained from Round007 and developed into a closed compact-operator problem with a quantitative tail. A small-interval inequality and a horizon obstruction are proved. RH remains open.

## 1. What was actually added

The [main derivation](README.md) starts from the unilateral successor and multiplicative isometries, carries their arithmetic through the LCM event measure and declared half-density, introduces the classical Gaussian completion explicitly, and reaches the completed Weil distribution, Suzuki's triangle function, and its screw kernel. It states where a new representation or external theorem is used. It does not identify different Hilbert-space realizations merely because they share labels.

The decisive analytic bridge is [SWS-002](FULL_SUZUKI_WEIL_TANGENT.md):
\[
\lim_{\omega\downarrow0}
\frac{\|v\|^2-\|H_{\omega,A}v\|^2}{2\omega}
=Q_W(v)
\quad(v\in C_c^\infty(-A,A)).
\]
The beta/Gamma factor, both elementary xi factors, the prime first derivative, and the contact term at the origin are included. The proof supplies a normalized-power distribution continuation and a cutoff argument for differentiating fixed smooth vectors. SWS-003 proves that operator-norm convergence at zero is impossible.

The [Gamma note](GAMMA_ENERGY_COMPACT_SIGN_OPERATOR.md) develops the inherited energy identity into:
\[
Q_W=P_A-D_A,\qquad
D_A=d_AI+2|s_A\rangle\langle s_A|,
\qquad
B_A=P_A^{-1/2}D_AP_A^{-1/2}.
\]
It proves the natural closed domain, compact smooth core, strict positivity of \(P_A\), compactness of \(B_A\), and the exact criterion \(Q_W\ge0\iff\|B_A\|\le1\) on each interval. The spectral bound
\[
p_n(P_A)\ge\beta\!\left(\frac{\pi n}{2A}\right)
\]
uses the exact digamma multiplier. The positive-series tail, rank-one interlacing, and mixed-block formulas state what a whole-space numerical certificate would have to control. These are applications of classical methods, not a sign proof.

[SWS-007](LOCAL_POSITIVITY_CERTIFICATE.md) proves a concrete unconditional inequality:
\[
Q_W(v)\ge\frac3{100}\|v\|^2,
\qquad 0<A\le1/128,\quad v\in V_A.
\]
The proof gives the stronger strict bound \(39199/10^6\) for nonzero vectors. Nine rational comparisons supporting its explicit constants are reproduced by the durable script. The support range is conservative and contains no prime event. Short-interval positivity is already known in the literature; this is an explicit calibration in the present normalization.

[SWS-009](FINITE_CERTIFICATE_INTERFACE.md) derives a sufficient finite spectral certificate. In the strict baseline case \(p_1(P_A)>d_A\), it reduces the sign to
\[
2\sum_{j\ge1}\frac{|\langle s_A,e_j\rangle|^2}{p_j-d_A}\le1
\]
and gives a finite bound with an explicit remainder. It also treats equality at the baseline and gives a two-block alternative retaining the mixed term. The present floating-point data do not satisfy the requirement of certified spectral enclosures.

## 2. A proof strategy ruled out with exact quantifiers

For every fixed nonzero test \(v\) supported on an old interval, enlarging the horizon adds precisely the same term \(2\Delta M\|v\|^2\) to both positive forms. Thus
\[
\frac{D_A(v)}{P_A(v)}
=1-\frac{Q_W(v)}{P_A(v)}\longrightarrow1.
\]

The central-binomial argument gives \(M_A\ge(\log2)e^A-o(e^A)\) without PNT. A hypothetical fixed negative witness would approach ratio one from above, with an excess of order at most \(e^{-A}\). A uniform bound \(\|B_A\|\le1-\varepsilon\) is consequently impossible, even if RH holds.

This obstruction changes the numerical reporting requirement: retain the algebraically cancelled \(Q_W(v)\), not only a normalized ratio. The theorem permits the required non-strict domination and does not decide its sign.

## 3. Reproducible execution

The literal successful command from the repository root was:

```sh
python scripts/rh_succ_weil_suzuki_probe.py --output research/aletheia_2026-10-07/succ_weil_suzuki/evidence/finite_probe_results.json
```

Environment: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0. The saved run time is `2026-10-07T23:55:16.926382+00:00`. Random seed: 2112. No zero ordinates were used. There are 27 reported step-cell compressions and separate larger-interval embeddings of one fixed box.

All eight grouped checks passed, including all nine exact rational comparisons. No full repository test suite, CI run, interval eigenvalue enclosure, or proof-assistant verification is claimed.

The independent evaluation residuals were:

| Identity control | Maximum absolute discrepancy |
|---|---:|
| gamma_quadrature_vs_series | 2.5693426553e-11 |
| square_vs_direct_weil | 1.4015715671e-12 |
| large_scalar_cancellation | 3.3839597791e-13 |
| box_vs_suzuki_triangle | 1.0391687510e-13 |
| odd_haar_gamma | 1.7763568394e-13 |
| embedded_box_horizon_identity | 3.5527136788e-15 |

The coefficient first derivative agreed to 6.6613381478e-16, and the separately integrated Suzuki triangle agreed to 1.2351231149e-15. The normalized-Haar isometry, braid, and refinement sample errors were zero in this run.

These small discrepancies support implementation consistency in the specified finite tests. They are not rigorous error bars for the infinite-dimensional operator.

## 4. What the finite eigenvalue scan showed

The following are the 64-cell observations. The exact finite minimum of \(Q_W\) bounds the unrestricted interval infimum from above; the exact finite maximum of \(D/P\) bounds the full compact-operator norm from below. The printed floating-point numbers are not certified enclosures of even those finite quantities.

| Half-width \(A\) | Active prime-power events | Minimum \(Q\) Ritz value | Maximum \(D/P\) Ritz value |
|---:|---:|---:|---:|
| 1/128 | 0 | 2.697346831e+0 | 0.665736821412 |
| 0.125 | 0 | 3.181112407e-1 | 0.944095822843 |
| 0.25 | 0 | 3.414566534e-2 | 0.993684131171 |
| 0.5 | 1 | 1.251586002e-3 | 0.999803014409 |
| 1 | 5 | 7.501028817e-4 | 0.999933178082 |
| 2 | 24 | 7.119303457e-4 | 0.999976074544 |
| 3 | 98 | 3.937456694e-4 | 0.999995112578 |
| 4 | 465 | 8.558208582e-4 | 0.999996090725 |
| 6 | 15040 | 3.023173111e-4 | 0.999999812682 |

Every scanned finite \(Q\) matrix was positive in floating point. That observation does not prove positivity for all vectors at any of the larger horizons.

Refinement illustrates why the complement matters. At \(A=1/2\), the minimum observed \(Q\) value decreased from approximately \(0.0108344\) with 16 cells to \(0.00377560\) with 32 and \(0.00125159\) with 64. A coarse positive margin is not a certified lower bound for the full operator.

## 5. A fixed witness makes the horizon effect visible

For the normalized box supported in \([-1/4,1/4]\), the script actually constructs containing-interval matrices at a common cell width and embeds the same function. It obtains:

| Containing half-width \(A\) | Cancelled \(Q\) from the containing matrix | Fixed-box ratio \(D/P\) |
|---:|---:|---:|
| 0.25 | 0.160650321528 | 0.970964187782 |
| 0.5 | 0.160650321528 | 0.975334246102 |
| 1 | 0.160650321528 | 0.985889674244 |
| 2 | 0.160650321528 | 0.994629975693 |
| 4 | 0.160650321528 | 0.999266706035 |
| 6 | 0.160650321528 | 0.999900469702 |

The quadratic form remains approximately \(0.160650321528\). Its ratio moves much closer to one because both positive pieces grow. This is a check of the algebraic cancellation and an illustration of SWS-006; it is not evidence that the unchanged box is becoming a null direction of \(Q_W\).

## 6. Controls that fail when they should

The deliberate errors are detected:

- Omitting the origin/Gamma scalar changes the independent box comparison by approximately \(5.37218\).
- Measuring the box's Gamma translation only inside the original interval loses half its energy, an error of approximately \(1.41337\) at the chosen control.
- Omitting the triangle's factor \(1/2\) changes the \(T=1\) value by approximately \(0.0440073\).
- Halving the prime first derivative at \(n=2\) misses approximately \(0.490129\).
- The synthetic cosine kernel \(4[1-\cos(2t)\cosh(t/4)]\) has negative anchored-kernel diagonal at \(t=\pi\). It is explicitly artificial, with unit weights at complex frequencies, and is not presented as Suzuki's function or actual zeta data.

The even box and odd Haar tests also check the two polar signs and off-diagonal Gamma entries. These controls are attached to specific mistakes; their success does not validate an untested universal statement.

## 7. Audit changes made before publishing

The bounded same-model audits checked the source normalization, full tangent proof, core and closure, Bessel/bathtub direction, rank-one tails, scalar certificate, exact rational constants, cell overlaps, and finite bound directions. They identified and led to a correction of one description: the inactive sector belongs to the full **finite** multiplicative space \(L^2(0,a)\), not the untruncated half-line operator.

Other clarity fixes made the compact eigenvalue ordering, the local form domain, the zero-coordinate sign convention, and the synthetic control's status explicit. The horizon control was strengthened to compute larger matrices instead of only evaluating the proved scalar-increment formula. Round007's pre-existing energy identity is credited directly.

These are useful internal checks. They share a model and source family and are not independent external peer review.

## 8. The next task has an exact endpoint

The next target is an analytic inequality extending the explicit small-support result into a declared prime-interacting interval, or a certified whole-interval result using SWS-009. A useful first benchmark is \(A=1/2\), where the \(n=2\) event is active, but the certificate must include omitted modes and the mixed block. A failed enclosure at that benchmark should state exactly which bound loses the margin.

An all-horizon proof must then supply a separate propagation or structural domination argument. The target remains
\[
d_A\|v\|^2+2|S(v)|^2
\le E_\Gamma(v)+E_{P,A}(v)+2|C(v)|^2
\quad\text{for every }A>0,\ v\in V_A.
\]
This is explicitly RH-equivalent and unproved. The completed bridge and its domain are now fixed, so further work can attack a specific inequality without repeatedly reconstructing or renormalizing the target.

