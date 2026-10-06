# Primary-source audit: recovery witnesses and terminal episodes

Base: `77ba6793be220c2fb5c2f0a6c250c54774acb9ea`.
Branch: `astra/prime-transport-martingale-002`.
Audit date: 2026-10-05.

**Verdict:** the deterministic service clock, recovery window, exact Chebyshev bridge, and no-terminal-episode proof survive reconstruction. They do not establish the reserve inequality. A stronger, symmetric workload-oscillation lemma is reconstructed in §4 below. A finite recovery-count certification inference has a concrete missing guard; several narrower proof/wording defects are repairable. RH remains unproved.

## 1. Retrieved objects and evidence boundary

The primary PDFs and complete reproduction archives were fetched from:

- [Part 4 v1, Zenodo 22076079](https://zenodo.org/records/22076079), August 26, 2026.
- [Part 5 v1, Zenodo 22076088](https://zenodo.org/records/22076088), August 26, 2026.
- [Part 2 v4, Zenodo 22076060](https://zenodo.org/records/22076060), the latest certificate implementation referenced by these papers.
- Suzuki, [On variants of Chebyshev's conjecture, arXiv:2411.07436v3](https://arxiv.org/abs/2411.07436v3), and the [published correction](https://doi.org/10.1007/s11139-025-01289-y).
- Suzuki, [Aspects of the screw function corresponding to the Riemann zeta-function, arXiv:2206.03682v4](https://arxiv.org/abs/2206.03682v4).

No newer-version warning appears on the retrieved Part 4/5 records. All PDF pages were extracted and the proof-bearing portions read; the disputed Part 5 p.9 argument and Part 4 p.10 statement were also checked against rendered pages. The source evidence manifest pins the exact download URLs, SHA-256 values, inherited certificate identity, and inspected code. Part 4's archive manifest matched all 32 listed files; Part 5's matched all 29. The Part 2 v4 C source is byte-identical to the previously audited v3 source.

This audit did not rerun the \(10^{10}\) positivity certificate or the \(2\cdot10^9\) episode scan. The zero-input files in the bundles were not used to construct any lemma or test. Conditional Gaussian/random-phase diagnostics are outside the RH implication chain.

## 2. Exact episode definitions needed by the transport argument

Write \(\ell_j=\log q_j\), \(w_j=\Lambda(q_j)/\sqrt{q_j}\), and use right-continuous prefixes

\[
W(t)=\sum_{\ell_j\le t}w_j,\qquad
Y(t)=W(t)-A'(t)=-\Psi'(t)
\]

off events, with the right derivative at events. Put

\[
\sigma(t)=A'(t),\quad
\delta_j=\sigma(\ell_{j+1})-\sigma(\ell_j)>0.
\]

The exact evolution is \(dY/d\sigma=-1\) between events and \(Y^+=Y^-+w_j\) at an event. Thus:

| Situation | Exact condition |
|---|---|
| Active post-event state | \(Y_j>0\) |
| Strict interior recovery before the next event | \(0<Y_j<\delta_j\) |
| Boundary recovery in the next event's left limit | \(0<Y_j=\delta_j\) |
| No recovery on that event interval | \(Y_j>\delta_j\) |
| Entry at \(a=\log x\) | \(Y(a^-)\le0<Y(a^+)=Y_a\le w_x\) |

At a boundary recovery, the next event can immediately make the right-continuous workload positive again. Therefore “maximal connected component of \(\{Y>0\}\)” is not literally the same definition as “episode split at every continuous left-limit recovery contact.” Adopt the latter convention when boundary recoveries are included, and keep strict crossings separate in counts. This fixes an endpoint ambiguity between Part 4 §3 and Part 5 §2/§4; none of the integral formulas depends on isolated endpoint values.

For an episode entered at \(a\), with subsequent event total \(P\) and recovery at \(b\),

\[
\sigma(b)-\sigma(a)=Y_a+P.
\]

If \(s=\log q\) is the last active event, then

\[
Y_q-Y_a=P-[A'(s)-A'(a)],
\quad -w_x<P-[A'(s)-A'(a)]<\delta_q
\]

for strict recovery; replace the final strict inequality by \(\le\) for boundary recovery. These endpoint constraints leave the interior area uncontrolled.

Part 4 equations (33)–(35) also follow by integrating the affine service-clock path:

\[
\int_{\sigma(a)}^{\sigma(b)}Y\,d\sigma
=\frac12(Y_a+P)^2-
\sum_{a<\ell_i\le s}w_i[\sigma(\ell_i)-\sigma(a)],
\]

\[
\Psi(a)-\Psi(b)=\int_{\sigma(a)}^{\sigma(b)}
\frac{Y(\sigma)}{A''(t(\sigma))}\,d\sigma.
\]

No stochastic assumption appears here. Unit-speed service does not imply a martingale, independence, or nonnegative capital.

## 3. Audit of the original Part 5 terminal theorem

Let

\[
\eta(u)=\sum_{n\le u}\frac{\Lambda(n)}{\sqrt n}-2\sqrt u+\alpha,
\qquad
\alpha=\frac12(\log8\pi+\gamma_E+\pi/2).
\]

The retained Archimedean remainder is

\[
R_A(u)=2\sum_{m\ge1}\frac{u^{-(4m+1)/2}}{4m+1}>0,
\qquad Y(\log u)=\eta(u)-R_A(u).
\]

Part 5 Lemma 3.2 obtains, for \(\Re s>1/2\),

\[
H_\eta(s)=\int_1^\infty\eta(u)u^{-s-1}du
=-\frac1s\frac{\zeta'}\zeta(s+1/2)
-\frac2{s-1/2}+\frac\alpha s.
\]

Both cancellations are exact: the zeta pole removes the singularity at \(s=1/2\), while \(\zeta'(1/2)/\zeta(1/2)=\alpha\) removes it at \(s=0\). The latter identity follows from the completed functional equation. There are no real zeros of zeta between \(1/2\) and 1, as seen from the alternating eta representation, so this transform is regular on the entire real segment \([0,1/2]\).

If a terminal episode existed, \(\eta(u)>R_A(u)>0\) eventually. Theorem 3.5 separates two exhaustive cases:

1. If \(\int\eta(u)du/u=\infty\), its nonnegative tail transform has a finite real convergence abscissa in \([0,1/2]\). Landau's one-sign singularity theorem forces a singularity there, contradicting regularity.
2. If that integral is finite, eventual positivity makes \(\eta\) absolutely integrable. Its transform is holomorphic in the open right half-plane and continuous on its boundary. The meromorphic formula then excludes zeros to the right of the critical line. Functional symmetry and existence of a nontrivial zero force a boundary zero, whose logarithmic-derivative pole contradicts the boundary continuity.

The temporary RH consequence in case 2 is inside a hypothesis subsequently contradicted. It is not circular and is not an RH proof. The source uses PNT for a growth bound; a crude bound suffices, as the next reconstruction shows.

Suzuki's Chebyshev paper, introduction following equation (4), supplies the separate positive weighted-error recurrence used in Part 5 Corollary 3.7. The primed endpoint convention transfers in the required direction because the right-continuous prefix is at least the primed prefix. This yields the source's quantitative \(\limsup Y\ge\alpha\), not a reserve lower bound.

## 4. Independently reconstructed two-sided workload-oscillation lemma

This is a variant of the same classical Landau mechanism, not a priority claim. It strengthens the qualitative terminal conclusion to recurrence of both strict workload signs and avoids the separate weighted-error oscillation theorem. It does **not** establish any sign of \(\Psi\).

**Lemma.** For Suzuki's explicitly normalized prime/Archimedean \(\Psi\), set \(Y=-\Psi'\) off events and use right-continuous event values. For every \(T>0\), there are \(t_+,t_->T\), away from events, with

\[
Y(t_+)>0,\qquad Y(t_-)<0.
\]

**Inputs:** the exact Suzuki Laplace identity; the completed zeta functional equation; absence of real zeros of \(\xi\); existence of at least one nontrivial zero; and Landau's one-sign Laplace singularity theorem. No location or ordinate data and no RH assumption enter.

**Proof.** First check the analytic hypotheses directly. Before the first event,

\[
A'(t)=4\sinh(t/2)-\alpha+
\operatorname{atanh}(e^{-t/2})+\arctan(e^{-t/2}),
\]

so \(Y(t)=\tfrac12\log t+O(1)\) as \(t\downarrow0\). Hence \(Y\) is locally integrable at the origin. It is piecewise smooth and locally integrable elsewhere. Using only \(\Lambda(n)\le\log n\) gives

\[
W(t)=O((1+t)e^{t/2}),\quad
Y(t)=O((1+t)e^{t/2}).
\]

The transforms therefore converge absolutely for \(\Re s>1/2\); PNT is unnecessary.

Let \(F(s)=\xi(1/2+s)\). Suzuki's exact formula, obtained from his Fourier–Laplace convention by putting \(z=is\), is

\[
\int_0^\infty\Psi(t)e^{-st}dt=\frac{F'(s)}{s^2F(s)}.
\]

Integration by parts is valid for \(\Re s>1/2\): continuity across event times cancels internal boundary terms, \(\Psi(0)=0\), and the exponentially damped boundary term at infinity vanishes. Therefore

\[
H_Y(s):=\int_0^\infty Y(t)e^{-st}dt
=-\frac{F'(s)}{sF(s)}. \tag{A}
\]

The sign in (A) is negative. Since \(F\) is even and \(F(0)\ne0\), its apparent pole at zero is removable. Since \(\xi\) has no real zeros, (A) is holomorphic near every real \(s\ge0\). A zero \(z\ne0\) of \(F\), of multiplicity \(m\), instead gives a nonremovable pole with residue \(-m/z\).

Suppose, for either \(\varepsilon\in\{-1,+1\}\), that \(f(t)=\varepsilon Y(t)\ge0\) almost everywhere beyond some \(T\). It cannot vanish on a whole tail: on every event-free interval past \(\log2\), \(Y'=-A''<0\). Consider its tail Laplace transform \(G\). Subtracting the finite head changes \(\varepsilon H_Y\) by an entire function.

If \(\int_T^\infty f=\infty\), the convergence abscissa \(\sigma_c\) is finite and belongs to \([0,1/2]\). Landau's theorem makes \(\sigma_c\) a singularity of \(G\), contradicting (A)'s regularity on that real segment.

If \(\int_T^\infty f<\infty\), eventual one-sidedness gives \(Y\in L^1(0,\infty)\). Its Laplace transform is holomorphic on \(\Re s>0\) and continuous on \(\Re s\ge0\), by dominated convergence. Meromorphic continuation of (A) then excludes every zero of \(F\) in \(\Re s>0\). Because \(F(s)=F(-s)\) and a nontrivial zero exists, a zero must lie on the imaginary axis, say \(z=i\gamma\ne0\). Approaching that zero from the right, (A) is unbounded while the integral transform has a finite limit. Contradiction.

Neither eventual sign is possible. Piecewise continuity then supplies strict-sign points away from events arbitrarily late. This proves the lemma. \(\square\)

**Consequence:** active and nonactive intervals both recur, so every active episode ends and recovery witnesses recur indefinitely. This controls the derivative process. It supplies no inequality comparing an episode's drawdown with its entry capital.

## 5. Chebyshev bridge and exact remaining theorem

Part 5 Theorem 5.1 is recovered by separating the \(m=0\) Archimedean series term. With

\[
S(X)=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\log\frac Xn-4\sqrt X,
\quad
\varrho_\infty(X)=4\sum_{m\ge1}
\frac{X^{-(4m+1)/2}}{(4m+1)^2},
\]

one obtains

\[
\Psi(\log X)=\pi^2/4+2G-8-\alpha\log X-S(X)-\varrho_\infty(X).
\]

The positive series converges at \(X=1\), where the normalization gives zero exactly. Integrating the service-remainder series down to 1 is justified by Tonelli; \(R_A(1)\) itself diverges, so endpointwise absolute convergence is not the justification. The integrated series is finite.

At a recovery witness, the actual episode minimum equals its frozen reserve

\[
V_q=L_q-A^*_{\rm ar}(W_q)=C_q-J_q.
\]

The terminal lemma and pure-debit law justify discarding intermediate checks within each recovered episode. They leave the universal statement

\[
V_q\ge0\quad\text{at every required recovery witness},
\]

which is equivalent to RH. The classical bridge is an exact change of coordinates. Conditional workload distribution, sparse deep-episode bounds, shrinking mean service windows, and the final-local-drawdown estimate \(O(q^{-9/20})\) do not imply this inequality. The latter follows from the cited Baker–Harman–Pintz next-prime bound and strong convexity, but concerns only the last interval's plunge.

## 6. First substantive certification defect: recovery counts

Part 4 §5 equation (36) infers

\[
B(X)-O(X)\le D_{\rm rec}(X)\le B(X)
\]

from the Part 2 conservative drawdown-branch count \(B\) and its precision-overlap counter \(O\); it claims equality if \(O=0\). This inference is not certified by the released implementation.

In latest Part 2 v4 `src/ppc_certify.c`, `close_previous_interval`:

1. the left branch is chosen if `prev_r_lo >= 0`;
2. the right branch is chosen if the right derivative upper bound is nonpositive;
3. otherwise the drawdown branch increments \(B\);
4. \(O\) increments only if the **right** derivative lower bound is nonpositive.

No left derivative upper enclosure is checked to prove the true post-left derivative is strictly negative. A negative lower bound alone does not establish that sign.

**Exact hostile counterexample to the inference.** On a unit interval take the true derivative \(r(v)=1/4+v\). Valid derivative enclosures are

\[
r(0)=1/4\in[-1/4,3/4],\qquad
r(1)=5/4\in[1,3/2].
\]

The released classification gives \(B=1,O=0\), while the exact strict-recovery count is zero. Thus the ledger-to-count implication fails even for a strictly convex interval with valid enclosures. The positive minimum certificate remains conservative: falling back to a drawdown lower bound is safe. What fails is promoting that software branch to a certified crossing.

**Scope:** this does not prove that the published numerical counts are false. It shows that the quoted rigorous lower bound and exact-count claims require an additional sign certificate or rerun. To repair, store a left derivative upper enclosure and count a strict recovery only when that upper bound is negative **and** the right derivative lower bound is positive. Treat either endpoint ambiguity as undecided. The Part 4 Python ledger script only transforms the stored counts and cannot repair missing sign information.

## 7. Repairable proof and quantifier issues

**Part 5 Corollary 3.9, p.9.** Its proof chooses an arbitrary \(\Psi(t_1)<0\), then asserts that this point lies inside an active episode. A negative potential may lie in a subsequent idle interval. The proof's supremum can equal \(t_1\). An exact model is \(A(t)=t^2/2\), one weight-3 event at \(t=1\): at \(t=4\), \(\Psi=-1\) but \(Y=-1\). This refutes that inference, not the intended equivalence.

A clean repair is eventual rather than cutoff-crossing reasoning. Finitely many witnesses have \(q\le q_0\); all their episodes end by the no-terminal lemma. After they have ended, nonnegative reserves at all later witnesses imply eventual nonnegativity of \(\Psi\). Suzuki Theorem 11.1 at \(\omega=0\), checked in the primary paper, then gives RH. Alternatively select a point during a negative descent and handle explicitly the event interval crossing the finite cutoff. Do not silently assume that a witness's last event exceeds the cutoff merely because its recovery time does.

**Boundary contacts.** Split episodes at a pre-event zero if using Part 4's boundary-recovery convention; do not identify these splits literally with connected components of a right-continuous positive set. Boundary recovery need not be a genuine local minimum of the full trajectory after the next instantaneous jump. Strict recovery witnesses are genuine smooth minima.

**Slack quantifier.** Part 5 Corollary 6.3's final wording is too strong if read as requiring the entire sequence of additive errors to converge to zero. From

\[
0\le\widehat J_q-J_q\le V_q
\]

and arbitrarily small witness reserves one can infer arbitrarily small errors, and convergence to zero along a sequence with \(V_q\to0\). One cannot infer convergence along every witness. The exact abstract countermodel \(V_{2n}=1/n,V_{2n+1}=1\), error \(=V/2\), satisfies every certificate inequality but has nonvanishing odd-subsequence error. The valid obstruction is a fixed positive **lower floor** on the additive excess. This correction does not make any reserve estimate sufficient.

**Service-clock origin.** The clock is defined on \(t\ge\log2\), with initial value \(\sigma_0=A'(\log2)\), not necessarily zero. The finite occupation integral in Part 4 equation (32) should start at \(\sigma_0\), or the clock should be translated by that constant. The local-time argument itself then holds with its stated noncontact assumptions. No interchange of infinite-time and shrinking-window limits follows.

## 8. What is and is not admitted into the proof chain

| Arrow | Audit status |
|---|---|
| Explicit \(A'\) to unit service and exact recovery window | PROVED-IN-REPO by reconstruction; present in Part 4 |
| Prime formula to exact Chebyshev bridge | PROVED-IN-REPO by reconstruction; present in Part 5 |
| One-sided terminal activity to contradiction | PROVED-IN-REPO by reconstruction of Part 5's classical argument |
| Either eventual workload sign to contradiction | NEW LEMMA PROVED THIS ROUND, as an independently reconstructed variant; no novelty claim |
| Both service regimes recur to infinitely many recovery witnesses | PROVED-IN-REPO, with endpoint convention explicit |
| Part 4 \(B-O\) to certified strict recovery count | REFUTED as a general inference from the released ledger; actual counts UNVERIFIED |
| Every later recovery reserve nonnegative to RH | PRIMARY-SOURCE THEOREM plus reconstructed episode reduction; repair the stated proof as above |
| Recurrence / endpoint pinning / small final plunge to nonnegative reserve | UNVERIFIED; no such implication proved |
| Conditional random-phase law to RH | Not an admissible arrow |
| Every witness satisfies \(J_q\le C_q\) | OPEN and RH-equivalent |

Seven exact rational hostile/control tests pass in `tests/test_source_audit_round002.py`. They exercise the missing classification guard, negative-but-idle potential, strict versus boundary recovery, the service-area identity, both Mellin principal-part cancellations, and the subsequence/full-limit distinction. They verify these finite logical interfaces; analytic continuation and Landau's theorem are justified in the written proofs, not by finite tests.
