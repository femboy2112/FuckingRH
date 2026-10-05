# Service clock, exact transport area, and the boundary defect

**PROVED-IN-REPO; normalization, not an RH reduction.** Parent:
`77ba6793be220c2fb5c2f0a6c250c54774acb9ea`. Round001 remains frozen.
No zero data enter any construction here.

Let `A` be the complete smooth part of Suzuki's exact formula, including its
Gamma linear constant and Lerch term, as defined in Round001
`EVENT_DYNAMICS.md`. Write `a0=log 2`, `sigma0=A'(a0)`, `c0=A''(a0)`.
On `t>=a0`,

\[
 A''(t)=\sqrt x-\frac1{\sqrt x(x^2-1)}>0,\qquad x=e^t,
\]
\[
 A'''(t)=\frac{x^5-2x^3+5x^2+x-1}
 {2\sqrt x(x^2-1)^2}>0.
\]

For `x>=2`, positivity follows from `x^3(x^2-2)>0` and
`5x^2+x-1>0`. Consequently `A'` maps `[a0,infinity)` bijectively onto
`[sigma0,infinity)`. Its inverse `T` is increasing and strictly concave:

\[
 T'(s)=\frac1{A''(T(s))}>0,\qquad
 T''(s)=-\frac{A'''(T(s))}{A''(T(s))^3}<0.
\]

For any compactly supported continuous test function `f`, substitution proves

\[
 \int_{a_0}^{\infty}f(A'(t))A''(t)\,dt
 =\int_{\sigma_0}^{\infty}f(s)\,ds.
\]

Thus the pushforward of smooth curvature is exactly Lebesgue mass **starting
at sigma0**, not at zero. The service clock is deterministic, not a stochastic
process unless a probability law is separately introduced.

For the actual prime powers set `aj=log qj`, `wj=Lambda(qj)/sqrt(qj)`,
`sigmaj=A'(aj)`, `Sj=sum_{i<=j}wi`, `Hj=sum_{i<=j}wi ai` and `S0=H0=0`.
The pushed prime measure is `sum wj delta_sigmaj`. On every event-free interval,

\[
 Y(t)=-\Psi'(t)=S_j-A'(t),\qquad
 \frac{dY}{d\sigma}=-1.
\]

At an event it jumps by exactly `wj`. The continuous reserve satisfies
`dPsi/dsigma=-Y T'(sigma)` between events. It does not become a constant-rate
capital process merely because service becomes flat.

## Restricted conjugate: every constant

The needed conjugate is `A*(s)=sup_{t>=a0}(st-A(t))`. Define

\[
 \tau(s)=\begin{cases}a_0,&0\le s\le\sigma_0,\\T(s),&s>\sigma_0.\end{cases}
\]

The following certified enclosures (200-bit Arb) also fix the boundary branch:

\[
\begin{split}
 &0.22497<\sigma_0<0.22498,\quad
 0.49012<w_2<0.49014,\\
 &0.06355<A(a_0)<0.06356,\quad
 c_0=5/(3\sqrt2),\\
 &0.04208<K_0:=A(a_0)-\sigma_0^2/(2c_0)<0.04209.
\end{split}
\]

In particular every nonempty actual prefix has `Sj>sigma0`. The unique
maximizer is `tau(s)`. Since `A` increases on `[a0,infinity)`,
`A*(0)=-A(a0)`; the envelope theorem (or differentiation at the matching
boundary) gives `(A*)'=tau`. Therefore, for every `s>=0`,

\[
 A^*(s)=-A(a_0)+\int_0^s\tau(b)\,db.
\]

Define the mass quantile `Qsvc(b)=sigmai` on `S_{i-1}<b<=Si`.
Endpoint choices have Lebesgue measure zero. Then, exactly,

\[
 H_j=\int_0^{S_j}T(Q_{\rm svc}(b))\,db,
\]
\[
 \boxed{M_j=A(a_0)+\int_0^{S_j}
 [T(Q_{\rm svc}(b))-\tau(b)]\,db.}
\]

This proves the requested identity with its mandatory clamp. Using `T(b)`
for `b<sigma0` without an extension is undefined.

## A valid concave extension and its capital charge

The clamp `tau` is **not concave**: its left derivative at `sigma0` is zero,
whereas its right derivative is `1/c0>0`. To use concave order, instead set

\[
 \bar T(b)=\begin{cases}
 a_0+(b-\sigma_0)/c_0,&0\le b<\sigma_0,\\T(b),&b\ge\sigma_0.
 \end{cases}
\]

This is increasing, concave, continuously differentiable, and `1/c0`-Lipschitz.
Its derivative is constant first and then strictly decreases. Since every
nonempty prefix covers `[0,sigma0]`,

\[
 \int_0^{S_j}(\tau-\bar T)\,db=\sigma_0^2/(2c_0),
\qquad
 \boxed{M_j=K_0+\int_0^{S_j}[\bar T(Q_{\rm svc}(b))-\bar T(b)]\,db.}
\]

For a general mass `0<=S<sigma0`, replace the charge by
`(sigma0*S-S^2/2)/c0`; the constant `K0` formula is for actual nonempty
prefixes. The empty prefix remains `M0=A(a0)`.

Uniformizing mass now gives `Xj=Bj`, `Yj=Qsvc(Bj)`,
`Bj~Unif(0,Sj)`, and
`Mj=K0+Sj(E barT(Yj)-E barT(Xj))`. This is one test-function discrepancy,
not an assertion of convex or concave stochastic order.

## Verification

`scripts/service_transport.py` encloses inverse roots by monotonicity and
bisection; its conjugate primitive follows the proven formula above. Tests
independently compare derivatives, Legendre values, event quantile integrals,
clamp/affine charges, and the initial constants. All arithmetic event labels
are integers; exp/log round trips do not decide inclusion.
