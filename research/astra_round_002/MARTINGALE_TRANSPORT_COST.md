# Recovered episodes: ordered transport exists, but its cost is the unpaid drawdown

**NEW LEMMA PROVED THIS ROUND, with no priority claim.** Every recovered
active episode has a positive ordered transport. The natural martingale
set is empty, and the natural ordered transport cost is fixed by its
marginals. Thus optimizing that coupling does not pay the Suzuki reserve.
This statement uses no prime estimate and holds for arbitrary positive events.

## 1. Balance the incoming backlog before transporting

Let an episode enter at `a=log x`, with post-event `y=Y(a)>0` and
pre-event `Y(a-)<=0`. Put `sigma_a=A'(a)`. Let `r>a` be its first recovery,
so `Y(t)>0` in the episode and `Y(r-)=0`. If recovery meets an event, stop
**before** its jump. Let q be the last included event, `s=log q<r`
(or q=x for a one-event episode). Then

\[
 P=\sum_{a<a_i<r}w_i,\quad L=y+P,\quad A'(r)=\sigma_a+L.
\]

Local finiteness makes P a finite sum. Initial capital is `E=Psi(a)`.
Define equal-mass service measures

\[
 \alpha=y\delta_{\sigma_a}+\sum_{a<a_i<r}w_i\delta_{\sigma_i},
 \qquad \lambda=\mathbf1_{[\sigma_a,\sigma_a+L]}d\sigma.
\]

Using the full weight at x in place of y is generally incorrect: the
pre-entry negative slope already consumed part of that event. The atom y
is the exact incoming backlog. Both measures have total mass L.

## 2. Exact ordered coupling and the strict mean obstruction

For `sigma_a<=z<sigma_a+L`,

\[
 \alpha([\sigma_a,z])-(z-\sigma_a)=Y(T(z))\ge0.
\]

Hence `alpha/L <=st lambda/L`. In mass coordinate `b in (0,L)`, the
ordered quantile coupling is

\[
 z=Q_\alpha(b),\quad z'=\sigma_a+b,\qquad z\le z'.
\]

It is strictly displaced on a set of positive mass: immediately after entry
the positive initial backlog gives a nonempty event-free interval with Y>0.
Thus

\[
 \int z\,d\lambda-\int z\,d\alpha
 =\int_{\sigma_a}^{\sigma_a+L}Y(T(z))\,dz>0.
\]

No martingale coupling with these marginals exists **in either direction**.
A submartingale alpha→lambda and a supermartingale lambda→alpha do exist
by this ordered coupling. Their existence is automatic episode geometry,
not an arithmetic positivity theorem.

## 3. Cost theorem: optimization cannot lower the drawdown

Integration by parts, or Tonelli applied to the ordered transport, gives

\[
 \boxed{D:=\int_a^rY(t)\,dt
 =\int T\,d\lambda-\int T\,d\alpha
 =\int_0^L[T(\sigma_a+b)-T(Q_\alpha(b))]\,db.}
\]

The pushforwards by T retain stochastic order. Therefore their unnormalized
W1 distance is exactly D; equivalently

\[
 D=L\inf_{\pi\in\Pi(T_\#\alpha/L,T_\#\lambda/L)}
 \int|v-u|\,d\pi(u,v).
\]

Every ordered coupling attains this cost. For the signed cost
`T(z')-T(z)`, **every** coupling has the same integral because the cost
separates into a function of each marginal. There is no hidden cheaper
plan. The reserve at recovery is exactly `Psi(r)=E-D`.

To match the source cost, let

\[
 S_1(a,r)=(r-a)A'(r)-A(r)+A(a),\quad
 C_q=E-S_1(a,r)+(s-a)P,
\]
\[
 J_q=\sum_{a<a_i\le s}w_i(s-a_i).
\]

Using `A'(r)=A'(a)+y+P`, direct cancellation proves
`Cq-Jq=E-D`. The episode transport formulation of `D<=E` is thus exactly
the recovery-witness inequality. It is not a strict reduction.

## 4. Why convex dispersion supplies no missing payment

For `phi=-T`, the nonnegative Bregman divergence gives

\[
 T(z')-T(z)=T'(z)(z'-z)-D_{-T}(z',z).
\]

A convexity correction reduces a linear displacement charge, but does not
bound the remaining cost by E. Under a martingale its expectation would
simplify to marginal differences; here that martingale is impossible.
Using an artificial balancing marginal requires paying its alteration and
recovering the original identity, as in the prefix audit.

A sharp generic counterfamily fixes `a,E>0`, takes one incoming atom of
mass L at `sigma_a`, and no further events before recovery. It has the exact
flat service continuum, positive ordered coupling, concave T, and finite
recovery for every L. Yet

\[
 D(L)=\int_0^L[T(\sigma_a+b)-a]db\longrightarrow\infty.
\]

For example `T(s)~2 log(s/2)` from the exact A' formula, so this divergence
is immediate; alternatively T is increasing and unbounded, which suffices.
For large L, `D(L)>E`. Thus these structural hypotheses alone cannot prove
payment. Increasing an actual event weight supplies the corresponding
Round001 hostile control; it leaves the service geometry intact.

The smaller surviving obstruction is **an arithmetic bound on the first
T-moment difference of the balanced arrival/service measures**, sensitive
to their exact prime configuration. Coupling selection and Pascal averaging
cannot alter that difference. No theorem establishing its bound by E was
found in this round. The independent terminal-recovery theorem permits us
to speak about all episodes; it gives no upper bound on their drawdowns.
