# Exact event system and the unpaid reserve invariant

Status: identities and local convexity **PROVED-IN-REPO**; global reserve
positivity **UNVERIFIED**. The conjugate reduction has an external predecessor
in Mittermeier Part 3 v3; it is not claimed as a new reduction in logical strength.

Write \(a_q=\log q\), \(w_q=\Lambda(q)/\sqrt q\),
\(\mu=\sum_qw_q\delta_{a_q}\), and \(r(t)=t_+\). On the positive half-line,
\[
P(t)=(r*\mu)(t)=\sum_{q\le e^t}w_q(t-a_q),\qquad\Psi(t)=A(t)-P(t).
\]
The measure is locally finite. Differentiation against compactly supported
test functions therefore proves \(P''=\mu\) on \(\mathbb R\), taking the
causal ramp definition of \(P\). The even extension instead has atoms at
both signs. Every event starts with zero value and adds slope \(w_q\) to
\(P\). Thus \(\Psi\) is continuous and
\[
\Psi'(a_q+)-\Psi'(a_q-)=-w_q.
\]

## Exact smooth functions and initial boundary

Set \(B=(\psi_0(1/4)-\log\pi)/2\). For \(t>0\),
\[
A(t)=4(e^{t/2}+e^{-t/2}-2)+Bt+C/4
-4\sum_{k\ge0}\frac{e^{-(4k+1)t/2}}{(4k+1)^2},
\]
\[
A'(t)=2(e^{t/2}-e^{-t/2})+B
+\operatorname{atanh}(e^{-t/2})+\arctan(e^{-t/2}),
\]
\[
A''(t)=e^{t/2}+e^{-t/2}-\frac{e^{-t/2}}{1-e^{-2t}}
=\frac{x^3-x-1}{\sqrt x(x^2-1)},\qquad x=e^t.
\]
These follow by termwise differentiation on compact subsets of \(t>0\).
The numerator has exactly one root \(\vartheta>1\), the plastic constant.
Thus \(A\) is concave before \(\log\vartheta\), convex after it, and strictly
convex on every prime-power interval (the first event is 2).

For \(t>0\), with \(k(t)=e^{-t/2}/(1-e^{-2t})\),
\[
A'''(t)=\tfrac12(e^{t/2}-e^{-t/2})
+\tfrac12k(t)+\frac{2e^{-2t}k(t)}{1-e^{-2t}}>0.
\]
So the smooth curvature itself increases. This does not mean \(\Psi\)
is globally convex: every event contributes a **negative** Dirac mass.

At the origin the correct expansion is
\[
\Psi(t)=\tfrac12t\log(1/t)
+\tfrac12(1-\gamma_E-\log(2\pi))t+O(t^2).
\]
In particular \(A'(0+)\) is infinite. An induction initialized with a
finite derivative at zero is invalid. On the full line the second derivative
must be read distributionally; a nonintegrable \(-1/(2|t|)\) expression
cannot be extended across zero as an ordinary density.

The finite initial certificate in `event_dynamics.py` encloses
\(\vartheta\) between 1.3247179572 and 1.3247179573, proves \(A(\log\vartheta)>0\),
and brackets the convex-part minimum in [0.46400,0.46401] with a strictly
positive value enclosure. Concavity with \(A(0)=0\) proves positivity on
the first segment; the unique convex minimum covers the rest through
\(\log2\). This supplies a genuine initial interval, not sampled points.

## Deterministic state and one constrained minimum

List prime powers increasingly as \(q_j\), put \(a_j=\log q_j\), and set
\[
S_j=\sum_{i\le j}w_i,\quad H_j=\sum_{i\le j}w_i a_i,\quad
E_j=\Psi(a_j),\quad d_j=\Psi'(a_j+)=A'(a_j)-S_j.
\]
For \(0\le h\le a_{j+1}-a_j\),
\[
\Psi(a_j+h)=E_j+d_jh+D_A(a_j+h,a_j),
\quad D_A(v,u)=A(v)-A(u)-A'(u)(v-u)\ge0.
\]
Writing \(h_j=a_{j+1}-a_j\), the complete recurrence is
\[
E_{j+1}=E_j+d_jh_j+D_A(a_{j+1},a_j),\qquad
d_{j+1}=d_j+A'(a_{j+1})-A'(a_j)-w_{j+1}.
\]
Also \(S_{j+1}=S_j+w_{j+1}\), \(H_{j+1}=H_j+w_{j+1}a_{j+1}\).

The constrained minimum is the left endpoint if \(d_j\ge0\), the right
endpoint if \(A'(a_{j+1})-S_j\le0\), and otherwise the unique
\(t_*\in(a_j,a_{j+1})\) satisfying \(A'(t_*)=S_j\). Values at event
endpoints are unambiguous despite derivative jumps. The initial segment,
this trichotomy, and the recurrence fully determine the continuous reserve.

## The global envelope and its exact debit

For every real \(t\ge0\),
\[
P(t)=\sup_{j\ge0}(S_jt-H_j),\qquad S_0=H_0=0.
\]
Proof: the increment of the displayed prefix expression at event \(j\)
is \(w_j(t-a_j)\), positive before the active cutoff and negative after
it; the active prefix maximizes it. Equivalently, every frozen prefix lies
above \(\Psi\), even outside its physical interval.

On \([a_0,\infty)\), \(a_0=\log2\), define
\[
A^*(s)=\sup_{t\ge a_0}(st-A(t)),\quad
\tau(s)=\begin{cases}a_0,&s\le A'(a_0),\\(A')^{-1}(s),&s>A'(a_0).\end{cases}
\]
Superlinear growth of \(A\) and strict convexity give a unique maximizer,
\((A^*)'(s)=\tau(s)\), and
\[
M_j=H_j-A^*(S_j)=\min_{t\ge a_0}[A(t)-S_jt+H_j].
\]
Consequently the already-certified initial interval gives exactly
\[
\boxed{\mathrm{RH}\iff M_j\ge0\text{ for every }j\ge0.}
\]
This is an equivalent target, **not** a weaker proved theorem.

The precise jump is
\[
M_{j+1}-M_j=\int_0^{w_{j+1}}[a_{j+1}-\tau(S_j+v)]dv
\]
\[
=w_{j+1}[a_{j+1}-\tau(S_j)]
-D_{A^*}(S_j+w_{j+1},S_j).
\]
The last term is nonnegative and is subtracted. A bare Bregman argument
therefore does not prove reserve accumulation. The arithmetic arrival
term must pay this debit. The tempting monotone-reserve conjecture is
**REFUTED** even for the true primes: certified enclosures give
\(M_{q=4}\in(0.04310,0.04311)\) and
\(M_{q=5}\in(0.03261,0.03263)\). The reserve decreases while remaining
positive. See `tests/test_event_dynamics.py`.

No global invariant paying all these debits was found. The external
smoothed-sum formulation is audited separately; it retains this same
unpaid arithmetic sign condition.

## Computational boundary

`evidence/event_certificate.json` certifies 35 complete intervals and the
initial segment, precisely \(0<t\le\log101\), using 200-bit Arb balls
and a proven exponential tail bound. This is a calibration certificate,
not an extension of the external \(10^{10}\) run and not an infinite-tail
argument. Exact/Fraction and symbolic tests check the algebra, and
deliberate event/Gamma/tail mutations produce negative certified signs.
