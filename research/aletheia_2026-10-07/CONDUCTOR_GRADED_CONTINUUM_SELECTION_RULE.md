# Conductor-graded continuum selection rule: ratios are hidden, products are physical interaction lengths

**Date:** 2026-10-07  
**Status:** exact finite-horizon operator identities. No RH assumption and no zeta-zero input.  
**Primary comparison:** Astra Round007/008 exact Weil event square and the \(\log(3/2)\) obstruction.  
**RH remains open.**

Astra's completed-square program identified a sharp local discriminator.

If different prime-power event channels are coupled through one scalar origin, their adjoint cross terms create continuum translations

\[
\log(q/r),
\]

including the forbidden atom

\[
\log(3/2).
\]

The Weil target has atomic translations only at signed logarithms of **integer prime powers**. Its Gamma and pole kernels are smooth away from zero, so an isolated rational-ratio atom cannot be canceled.

The exact-conductor support geometry supplies a canonical selection rule:

\[
\boxed{
\text{adjoint cross-prime ratios leave the scalar channel and land in hidden product conductors}.
}
\]

Meanwhile chronological ordered products carry the **sum** of loop lengths,

\[
\log q+\log r=\log(qr),
\]

so their continuum location is an allowed integer product.

This passes Astra's first finite obstruction while preserving the exact prime event square.

---

# 1. Exact-depth event labels

Let

\[
q=p^k
\]

run over active prime powers

\[
q\le N.
\]

Choose a normalized exact-conductor support wake

\[
\boxed{
\beta_q\in W_q,
\qquad
\|\beta_q\|_2=1.
}
\]

Because exact-conductor spaces are orthogonal,

\[
\boxed{
\langle\beta_q,\beta_r\rangle=0
\qquad(q\ne r).
}
\]

Let

\[
\mathcal K_N
=
L^2(\mathbb Z/L_N\mathbb Z)
\]

be the common finite support clock.

Let

\[
\mathcal H=L^2(\mathbb R)
\]

be the continuum log-coordinate test space.

Define

\[
\boxed{
T_q
=
\tau_{\log q}.
}
\]

Finally use the exact first-jet Weil weight

\[
\boxed{
w_q
=
\frac{\Lambda(q)}{\sqrt q}.
}
\]

---

# 2. Conductor-labelled oriented event square

Define the lifted event analysis operator

\[
\boxed{
\mathcal D_N f
=
\sum_{q=p^k\le N}
\sqrt{w_q}\,
\beta_q
\otimes
(T_q-I)f.
}
\]

Then exact-conductor orthogonality gives

\[
\begin{aligned}
\|\mathcal D_Nf\|^2
&=
\sum_{q,r}
\sqrt{w_qw_r}
\langle\beta_q,\beta_r\rangle
\langle(T_q-I)f,(T_r-I)f\rangle
\\
&=
\boxed{
\sum_{q=p^k\le N}
w_q
\|(T_q-I)f\|^2.
}
\end{aligned}
\]

This is exactly the arithmetic event part of Astra Round007's positive Weil edge square.

So the conductor labels do not alter the required one-body prime term.

---

# 3. The bulk identity coefficient is exactly sharp

Since each \(T_q\) is unitary,

\[
\|(T_q-I)f\|^2
=
2\|f\|^2
-
2\Re\langle T_qf,f\rangle.
\]

Therefore

\[
\boxed{
\|\mathcal D_Nf\|^2
=
2S_N\|f\|^2
-
2\sum_{q\le N}
w_q
\Re F(\log q),
}
\]

where

\[
\boxed{
S_N
=
\sum_{q=p^k\le N}
w_q.
}
\]

This has exactly the sharp minimal scalar cost proved in Round007:

\[
\boxed{
2S_N.
}
\]

Thus the support lift passes the one-body normalization test but does **not** by itself pay the completed Weil debit.

The remaining completed target is still

\[
\mathcal W(f)
=
E_N(f)
+
(c_0-2S_N)\|f\|^2
+
2\Re(\ell_+f\,\overline{\ell_-f}),
\]

after adjoining the exact positive Gamma-difference channel to \(E_N\).

---

# 4. Why the forbidden ratio atoms vanish

Suppose instead one used a single scalar channel

\[
\sum_q
\sqrt{w_q}(T_q-I)f.
\]

Its square would contain cross terms

\[
T_q^*T_r
=
\tau_{\log(r/q)},
\]

which generate the forbidden rational-ratio atoms diagnosed by Astra.

In the conductor-labelled lift, the coefficient of this continuum cross term is

\[
\boxed{
\langle\beta_q,\beta_r\rangle.
}
\]

For

\[
q\ne r,
\]

this is zero.

Therefore:

\[
\boxed{
\text{no }\log(r/q)\text{ atom appears in the physical scalar event square.}
}
\]

In particular,

\[
\boxed{
\text{the }\log(3/2)\text{ coefficient is exactly zero.}
}
\]

This is a theorem, not a numerical cancellation.

---

# 5. The ratio interaction has not disappeared; it changed conductor

The previous section is a scalar compression statement.

Retain the support operator rather than immediately taking its expectation.

For an exact-conductor wake, define

\[
\boxed{
E_q
=
S M_{\beta_q}
}
\]

on the common support clock, and the coupled support/continuum leg

\[
\boxed{
\mathscr E_q
=
E_q\otimes T_q.
}
\]

For distinct coprime prime-power bases,

\[
E_q^*E_r
=
M_{\beta_q\beta_r}.
\]

Hence

\[
\boxed{
\mathscr E_q^*\mathscr E_r
=
M_{\beta_q\beta_r}
\otimes
\tau_{\log(r/q)}.
}
\]

The multiplication field satisfies

\[
\boxed{
\beta_q\beta_r\in W_{qr}.
}
\]

So the forbidden scalar ratio term is not destroyed algebraically.

It is diverted into the hidden exact-conductor product sector

\[
\boxed{
W_{qr}.
}
\]

Its vacuum/scalar matrix coefficient is zero because

\[
W_{qr}\perp W_1.
\]

This is the conductor selection rule.

---

# 6. Chronological products add lengths instead of subtracting them

Now compose the oriented legs in chronological order.

Since continuum translations commute,

\[
T_qT_r
=
\tau_{\log q+\log r}
=
\boxed{
\tau_{\log(qr)}.
}
\]

Thus

\[
\boxed{
\mathscr E_q\mathscr E_r
=
E_qE_r
\otimes
\tau_{\log(qr)}.
}
\]

The support product also fuses the two prime directions into conductor \(qr\).

Therefore both coordinates agree:

\[
\boxed{
\text{support conductor fusion}
\quad
q,r\mapsto qr
}
\]

and

\[
\boxed{
\text{continuum loop-length addition}
\quad
\log q+\log r=\log(qr).
}
\]

Call this **conductor--length locking**.

The interaction sits at an integer logarithmic location, not a rational-ratio location.

---

# 7. Curvature is also product-locked

From the oriented boundary curvature theorem,

\[
[E_q,E_r]
=
S^2M_{\Omega_{q,r}},
\]

with

\[
\Omega_{q,r}\in W_{qr}
\]

for coprime prime-power directions.

Therefore

\[
\boxed{
[\mathscr E_q,\mathscr E_r]
=
[E_q,E_r]
\otimes
\tau_{\log(qr)}.
}
\]

So the first genuine two-direction curvature is simultaneously:

- exact conductor \(qr\);
- continuum displacement \(\log(qr)\).

It is automatically located on an allowed integer product.

This sharply differs from an ungraded shared-origin cross square.

---

# 8. Weighted two-prime scale

Weight the support legs by Suzuki's nonlinear conductor amplitudes:

\[
D_{q,\omega}
=
\sqrt{b_\omega(q)}E_q.
\]

Define

\[
\mathscr D_{q,\omega}
=
D_{q,\omega}\otimes T_q.
\]

Then for coprime prime-power directions,

\[
\left\|
D_{q,\omega}^*D_{r,\omega}
\right\|_{2,\tau}^2
=
\boxed{
b_\omega(qr).
}
\]

And the ordered curvature energy satisfies

\[
\boxed{
\|[\mathscr D_{q,\omega},\mathscr D_{r,\omega}]\|^2
=
c_{q,r}b_\omega(qr)
}
\]

in normalized support trace, with the universal local curvature constant \(c_{q,r}\) determined in the oriented-curvature note.

Thus the product-locked continuum interaction has exactly the correct Suzuki mixed-conductor scale.

---

# 9. Higher interactions

For pairwise coprime prime-power directions

\[
q_1,\ldots,q_r,
\]

exact-conductor fusion gives

\[
\prod_j\beta_{q_j}
\in
W_{\prod_jq_j}.
\]

Continuum translations give

\[
\prod_jT_{q_j}
=
\boxed{
\tau_{\log\prod_jq_j}.
}
\]

Therefore the entire exterior/ordered interaction hierarchy obeys

\[
\boxed{
\text{support product}
\leftrightarrow
\text{integer product}
\leftrightarrow
\text{sum of loop lengths}.
}
\]

The \(r\)-body interaction naturally lives at

\[
\boxed{
\left(
W_{\prod_jq_j},
\log\prod_jq_j
\right).
}
\]

This is the precise harmonic-undertone organization suggested by the user's loop picture.

---

# 10. Comparison with Astra's finite obstruction

Astra's Round008 finite atom theorem states:

> a nonzero scalar event metric \(G_{ij}\) between distinct prime jets creates an isolated atom at
> \[
> \log(q_i/q_j)
> \]
> and exact equality to Weil forces that scalar coefficient to vanish.

The conductor-graded construction satisfies that requirement identically:

\[
\boxed{
G_{qr}^{\rm physical}
=
\langle\beta_q,\beta_r\rangle
=
0.
}
\]

But it does **not** set the operator interaction to zero.

Instead:

\[
\boxed{
E_q^*E_r
\in
W_{qr}.
}
\]

So this is outside the scalar-event-metric failure mode in precisely one controlled way:

\[
\boxed{
\text{cross-prime information is moved into an orthogonal hidden conductor channel}.
}
\]

That is why it is a legitimate nonreducing escape candidate.

---

# 11. What remains unsolved

The construction now passes two necessary local tests:

### Prime-event target

It reproduces exactly

\[
\sum_qw_q\|\tau_{\log q}f-f\|^2.
\]

### Forbidden-ratio target

It gives zero physical coefficient at every

\[
\log(q/r),
\qquad q\ne r.
\]

However the completed Weil form still differs from the positive edge square by

\[
\boxed{
(c_0-2S_N)\|f\|^2
+
2\Re(\ell_+f\,\overline{\ell_-f}).
}
\]

So the true question is now:

> Can the hidden product-conductor hierarchy, coupled to the exact Archimedean channel and then eliminated/compressed, generate precisely this bulk identity + pole correction while preserving the ratio-atom selection rule?

That is not proved.

---

# 12. Next decisive calculation

Build a finite parent containing:

1. physical scalar/prime event continuum;
2. exact active mixed-conductor support channels \(W_{qr},W_{qrs},\ldots\);
3. product-locked continuum translations
   \[
   \tau_{\log(qr)},\tau_{\log(qrs)},\ldots;
   \]
4. the exact Gamma difference channel;
5. the two pole boundary functionals \(\ell_\pm\).

Then compute its full polarized Gram/Schur pushforward.

Acceptance criteria, in order:

1. coefficient at \(\log(3/2)\) is exactly zero;
2. every other noninteger ratio atom is exactly zero;
3. prime translations have coefficient \(-2w_q\);
4. bulk identity correction is exactly \(c_0-2S_N\);
5. pole cross term is exactly
   \[
   2\Re(\ell_+f\,\overline{\ell_-f});
   \]
6. no unrequested atomic lines remain.

Passing 1--3 is now structurally plausible.

Criteria 4--5 are the actual completion wall.

No claim beyond that is made.
