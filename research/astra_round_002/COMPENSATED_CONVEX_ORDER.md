# Compensated order: independent costs and failed capital constructors

**NEW LEMMAS PROVED THIS ROUND (in this repository; no priority claim).**
Two independently defined transport repairs are rigorous, but their proposed
fixed-capital certificates fail for actual primes. This excludes the precise
constructors below, not every possible arithmetic-dependent compensation.

Use the laws `X,Y`, mass `S`, and constants `A0,K0,c0` in
`SERVICE_CLOCK_TRANSPORT.md`. The exact reserve is
`M=K0+S(E barT(Y)-E barT(X))`.

## 1. Minimal W-infinity repair into increasing-concave order

For any two compactly supported probability laws define, independently of T,

\[
 \delta(\mu,\nu)=\inf_{\nu':\ \mu\le_{icv}\nu'}W_\infty(\nu,\nu'),
\quad W_\infty(\nu,\nu')=\inf_{\pi\in\Pi(\nu,\nu')}
 \mathop{\rm ess\ sup}_{(y,z)\sim\pi}|y-z|.
\]

Let `L_mu(v)=integral_0^v Q_mu(u)du`, `0<v<=1`. Then

\[
 \boxed{\delta=\sup_{0<v\le1}
 \left[\frac{L_\mu(v)-L_\nu(v)}v\right]_+.}
\]

**Proof.** Increasing-concave order is equivalent to `L_mu<=L_nu`.
Indeed increasing concave functions are generated, up to constants and
limits, by `min(x,k)` and `x`. Their tests are equivalent to reversed put
inequalities. The conjugate identity
`L_mu(v)=sup_k(vk-E(k-X)_+)` and its reverse give the integrated-quantile
criterion. If a coupling moves points by at most d, its quantiles obey
`Q_nu'<=Q_nu+d`, hence `L_nu'<=L_nu+dv`; the displayed lower bound follows.
Conversely the translated law `nu'=law(Y+delta)` has
`L_nu'=L_nu+delta*v>=L_mu`, and translation costs exactly delta. This
attains the bound. Compact supports avoid integrability/attainment issues.
The usual quantile formula for W-infinity follows directly from ordered
coupling and the necessary shifted CDF inequalities. QED.

For the actual prefix, put `Nk=sum_{i<=k}wi sigmai`. In unnormalized mass
coordinate b the expression to maximize is
`b/2-(integral_0^b Qsvc)/b`. On a mass bin it is
`b/2-sigmai-(N_{i-1}-S_{i-1}sigmai)/b`.
The parenthesized constant is nonpositive, so this expression is convex;
its maximum lies at an endpoint. Its limit at zero is `-sigma0`. Thus

\[
 \boxed{\delta_j=\max_{1\le k\le j}
 (S_k/2-N_k/S_k)_+.}
\]

This defect uses all lower-quantile mean constraints. It is not `M`, does
not use T, and has the independent optimal-transport characterization above.
It repairs increasing-concave order (equivalently, increasing-convex order
after reflection), not equal-mean convex order.

Concavity and monotonicity now supply the valid sufficient certificate

\[
 D_j^{\rm shift}:=\sum_{i\le j}w_i
 [T(\sigma_i+\delta_j)-T(\sigma_i)]\le K_0
 \quad\Longrightarrow\quad M_j\ge0.
\]

To prove it, apply `barT` to `X<=icv Y+delta`, subtract the shift cost,
and use the exact reserve identity. All shifted nodes are in T's natural
domain. The still stronger Lipschitz certificate is
`Sj*delta_j/c0<=K0`. Both statements are elementary transport theorems;
no arithmetic estimate establishes their hypotheses universally.

**True-prime refutations of universal payment.**

| Constructor's cost | First prefix exceeding its capital | Certified cost | Capital | Actual M |
|---|---:|---:|---:|---:|
| `Sj delta_j/c0` | q=7 | (0.04988,0.04989) | K0 in (0.04208,0.04209) | (0.04787,0.04789) |
| Exact `Dshift` | q=13 | (0.04407,0.04408) | same K0 | (0.03106,0.03108) |

Every earlier prime-power prefix is enclosed and tested; these are earliest
failures of the specified formulas. Through q=13 the minimal radius is the
first-prefix obstruction `delta2` in (0.020089,0.020090). A better radius
cannot save these constructors. A **nonuniform** repair can have a different
T-cost at the same radius; its impossibility is not asserted here.

Consequently `Dshift<=K0` is strictly stronger than `M>=0`, not equivalent.
The same is true of the Lipschitz sufficient bound. The order repair theorem
is sound; the proposed arithmetic capital premise is false.

## 2. Minimal one-sided physical transport, with no concavity assumption

Let `U=tau(X)`, `V=T(Y)`. Define

\[
 D_j^-:=S_j\inf_{\pi\in\Pi(\mathcal L(U),\mathcal L(V))}
 \int(u-v)_+\,d\pi(u,v).
\]

For any integrable laws,
`(u-v)_+=(|u-v|+u-v)/2`; the signed expectation is fixed by the marginals.
In one dimension the quantile coupling minimizes absolute distance. One
proof integrates the necessary crossing mass at every threshold and notes
that the monotone coupling attains that bound simultaneously. Therefore

\[
 D_j^-=\int_0^{S_j}[\tau(b)-T(Q_{svc}(b))]_+\,db,
\quad
 D_j^+=\int_0^{S_j}[T(Q_{svc}(b))-\tau(b)]_+\,db,
\]
\[
 \boxed{M_j=A_0+D_j^+-D_j^-.}
\]

Equivalently, `Dminus/S` is the minimal W1 movement of V into the cone of
laws stochastically dominating U: monotone coupling and replacing V by
`max(U,V)` attains it; any such dominating repaired law has at least the
integrated positive CDF discrepancy. This is another independent order
repair, not a definition by the reserve.

Discarding future positive transport credits gives the sufficient constructor
`Dminus<=A0`. It fails first at q=5:

\[
 D_5^-\in(0.09692,0.09693)>A_0\in(0.06355,0.06356),
 \qquad M_5\in(0.03261,0.03263)>0.
\]

Earlier costs at q=2,3,4 are below A0. Allowing **exact** accumulated
credits changes the condition to `Dminus<=A0+Dplus`, which is exactly
`M>=0`. This restores equivalence but supplies no theorem paying the cost.
It is precisely the cancellation that the stronger certificate threw away.

## 3. Literature dependencies and their limits

Primary sources inspected on 2026-10-05:

- Leskela–Vihola, [arXiv:1404.0999v3](https://arxiv.org/pdf/1404.0999v3),
  Theorems 1.1–1.4: order is a **hypothesis** for (conditional) martingale
  or submartingale couplings. No automatic order from atomicity or flatness.
- Gerhold–Gulum, [arXiv:1512.06640v2](https://arxiv.org/pdf/1512.06640v2),
  Theorems 3.5 and 6.3: nearby peacocks require explicit compatibility
  inequalities and a common feasible mean. Stop-loss distance is a uniform
  call-function distance. Their constructive approximation does not preserve
  the original prime marginal or establish its capital budget.
- Backhoff-Veraguas et al.,
  [arXiv:1708.04869](https://arxiv.org/pdf/1708.04869), Theorem 1.5:
  martingale Benamou–Brenier assumes convex-ordered P2 marginals.
- Beiglbock–Hobson–Norgilas,
  [arXiv:2008.09936](https://arxiv.org/pdf/2008.09936), §2 and Theorem 2:
  shadow measures require the appropriate extended convex order; they
  construct a coupling once that premise is available.

Kellerer's Markov realization, as precisely stated and sourced in the first
two papers, also starts with a peacock. None of these theorems cancels the
mean, boundary, or call-function violations documented here. The abstract
repair lemmas above are proved directly so no unverified projection theorem
is silently imported.

## 4. Boundary of the no-go

Refuted: fixed initial-capital payment for the two specified optimal-distance
repairs; uncompensated order; fixed-marginal martingale and Bernstein
factorizations. Not refuted: every nonuniform repair or an arithmetic theorem
controlling the **signed** cost using exact Euler-product correlations.
That remaining theorem must supply information absent from positivity,
curvature, support, total mass and first moments. Episode-local analysis
below identifies exactly where it would enter.
