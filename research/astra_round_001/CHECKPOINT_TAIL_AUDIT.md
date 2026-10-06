# Independent checkpoint/tail audit

Date: 2026-10-05. Status: the local geometry and exact scalar reduction are reconstructed below; **RH remains open**. No zero data enter these reconstructions. The finite-spectral estimate is audited as an external interface, not used to construct a proof.

## 1. Sources actually retrieved

The following records, their PDFs, and the Part 2 code archive were downloaded directly from Zenodo. PDF equations (75), (84)–(86), and the intervening upper-edge display were visually checked after rendering; they are not extraction artifacts.

| Record | Inspected version and file | SHA-256 of downloaded PDF |
|---|---|---|
| [21979497](https://zenodo.org/records/21979497) | Part 2 v3, `260818_Mittermeier_RH_Prime_Power_Checkpoint_Certificate_Part2_v3.pdf` | `83135d48a2b45174e8187ea20a28f5422eb09ea82979bc9a9b9f5d78f687eaf3` |
| [21979513](https://zenodo.org/records/21979513) | Part 3 v2, `260818_Mittermeier_RH_Prime_Power_Completion_Architecture_Part3_v2.pdf` | `e2a6eebb9074435a618fd3dbffc148a868f0c525972f3f7bcb16c31af0d44598` |
| [22076071](https://zenodo.org/records/22076071) | Part 3 v3, `260823_Mittermeier_RH_Prime_Power_Completion_Architecture_Part3_v3.pdf` | `74ee615e634490f8431bd6731411ef2e177025d1a00bcf2f35008506d77c6e26` |

The first two records flag newer versions. The last is dated August 26, 2026. This audit pins these bytes and does not conflate versions. Part 3 v3 references later Parts 4 and 5; their terminal-excursion claims have **not** been audited here and are not proof inputs.

Additional primary source: Chirre–Helfgott, [arXiv:2512.15709v1](https://arxiv.org/abs/2512.15709), Proposition 9.1, downloaded and read. Its specialization is checked in §5. The Platt–Trudgian finite-height computation is an external premise, not rerun here.

## 2. Independent geometry reconstruction

Set

\[
\alpha=\tfrac12(\log(8\pi)+\gamma_E+\pi/2),\qquad
C_A=\pi^2/4+2G,
\]

and use the repository's Suzuki-normalized smooth part

\[
A(t)=4(e^{t/2}+e^{-t/2}-2)-\alpha t+C_A
 -4\sum_{k\ge0}\frac{e^{-(2k+1/2)t}}{(4k+1)^2}.
\]

Termwise differentiation is justified uniformly on every compact subset of \(t>0\). The series for `atanh` and `atan` give

\[
A'(t)=4\sinh(t/2)-\alpha+
\operatorname{atanh}(e^{-t/2})+\arctan(e^{-t/2}).
\]

With \(x=e^t>1\), direct differentiation gives

\[
A''(\log x)=\sqrt{x}-\frac1{\sqrt{x}(x^2-1)}
=\frac{x^3-x-1}{\sqrt{x}(x^2-1)}.
\]

The numerator is strictly increasing for \(x>1\), is negative at 1 and positive at 2, so it has exactly one root there: the plastic constant. In particular \(A''>0\) on \([\log2,\infty)\). A second calculation gives

\[
A'''(\log x)=
\frac{x^5-2x^3+5x^2+x-1}{2\sqrt{x}(x^2-1)^2}>0\quad(x\ge2),
\]

since \(x^5-2x^3=x^3(x^2-2)>0\) and \(5x^2+x-1>0\).

Thus the curvature and plastic-constant claims survive reconstruction. They involve no prime-distribution theorem. For the prefix states

\[
W_j=\sum_{i\le j}w_i,\quad L_j=\sum_{i\le j}w_i\ell_i,
\quad w_i=\Lambda(q_i)/\sqrt{q_i},\quad\ell_i=\log q_i,
\]

one has \(\Psi(t)=A(t)-W_jt+L_j\) until the next event. Consequently there is exactly one constrained minimum: the left endpoint, right endpoint, or unique zero of \(A'(t)-W_j\), according to the endpoint derivative signs. This is localization, not positivity.

## 3. Exact reserve reduction, with the full quantifier retained

On \(t\ge\log2\), put

\[
A^*_{\rm ar}(W)=\sup_{t\ge\log2}(Wt-A(t)).
\]

At an active event \(s=\log q\), meaning \(W_q>A'(s)\), the unique frozen minimizer is \(\tau=(A')^{-1}(W_q)>s\). Set

\[
V_q=L_q-A^*_{\rm ar}(W_q)=A(\tau)-W_q\tau+L_q.
\]

Future events subtract nonnegative hinges from the frozen continuation. Hence \(V_q<0\) forces an actual negative value by time \(\tau\). Conversely, if every active-event reserve is nonnegative, each next event interval is nonnegative; inactive intervals increase. Given the initial region, this proves

\[
\forall q\text{ active},\ V_q\ge0
\quad\Longleftrightarrow\quad
\forall t\ge0,\ \Psi(t)\ge0
\quad\Longleftrightarrow\quad\mathrm{RH}.
\]

No assumption that an excursion eventually recovers is needed. This is the substance of Part 3 v3 Theorem 3.4, independently justified here. The conjugate and its active-event debit formula already occur in that source; this round claims no novelty for them.

For an earlier event \(a=\log x\), let \(E=\Psi(a)\), \(Y_a=W_x-A'(a)\), \(P=W_q-W_x\), and

\[
S_1(a,\tau)=(\tau-a)A'(\tau)-A(\tau)+A(a).
\]

Since \(A'(\tau)=A'(a)+Y_a+P\), elementary cancellation yields

\[
V_q=C_q-J_q,
\quad C_q=E-S_1(a,\tau)+(s-a)P,
\quad J_q=\sum_{x<n\le q}\frac{\Lambda(n)}{\sqrt n}\log\frac qn.
\]

All prior arithmetic is present in \(E,Y_a,P\). Conditioning on those exact states does not remove its difficulty.

Writing \(\psi(u)=\sum_{n\le u}\Lambda(n)\), Stieltjes integration by parts gives the exact positive-kernel representation

\[
J_q=\int_x^q[\psi(u)-\psi(x)]u^{-3/2}
 \left(1+\tfrac12\log(q/u)\right)du
=\int_x^q\frac{\Sigma_{1/2}(u)-\Sigma_{1/2}(x)}u\,du.
\]

The endpoint at \(q\) contributes zero. Therefore **the all-event inequality \(J_q\le C_q\), using the true sum, is RH-equivalent**. It is not a weaker theorem secretly ready to follow from PNT. For an independently established upper bound \(\widehat J_q\ge J_q\), the condition \(\widehat J_q\le C_q\) is sufficient, potentially strictly stronger, and not automatically equivalent.

## 4. Certificate through \(10^{10}\): what was and was not checked

Part 2's downloaded archive includes C source `src/ppc_certify.c`, a stored MPFR result, an independent event-count script, and separate diagnostics. The stored result reports 455,062,595 intervals, zero nonpositive lower enclosures, and the least lower enclosure

\[
0.021498559834383781734\ldots
\]

at left event \(q=34,186,367\), using 64-bit MPFR arithmetic. This is a **reported external finite certificate**, not a computation reproduced in this round.

Source inspection found the appropriate mathematical safeguards:

- exact integer event coordinates, segmented prime sieve, and ordered merge with higher powers;
- lower/upper MPFR rounding for weights, cumulative states, logs, roots and constants;
- positive-series tails bounded geometrically;
- endpoint derivative tests; otherwise the conservative strong-convexity lower bound
  \(E-r_-^2/(2m)\), with \(m=A''(\ell_j)>0\);
- explicit closure of the last partial interval at the requested cutoff.

A negative/overlapping slope enclosure falls back to the drawdown bound instead of guessing a sign. The polynomial curvature monotonicity above justifies using the left endpoint's curvature on the whole interval.

The count was independently rerun through \(10^{10}\), using the supplied structurally separate SymPy `primepi` method:

\[
\#\{p^k\le10^{10}\}=\sum_{k\ge1}\pi(\lfloor10^{10/k}\rfloor)
=455,052,511+10,084=455,062,595.
\]

This corroborates enumeration size, **not** the sign calculation. Building the MPFR executable failed because the environment lacked official MPFR/GMP development headers. No complete positivity rerun was performed. The original JSON is a summary, not a formally checked proof object. No source-level error was found in the inspected directed-rounding path; that bounded review does not certify every line or the published full run. The initial prime-free interval is a separate analytic input.

## 5. Finite-spectral bound: valid interface, unpaid terminal inequality

Chirre–Helfgott Proposition 9.1 assumes RH only up to height \(T\ge10^7\), with \(u>\max(T,10^9)\). Specializing its displayed bound to \(\sigma=1/2\) and multiplying by \(\sqrt u\) yields

\[
\Sigma_{1/2}(u)\le U_T(u)=(c_T+e_T)\sqrt u-\alpha+d_T,
\]

\[
c_T=\frac\pi T\coth\frac\pi{2T},\quad
e_T=\frac\pi{T-1},\quad
d_T=\frac1{2\pi}\log^2\frac T{2\pi}-\frac1{6\pi}\log\frac T{2\pi}.
\]

The identity \(\zeta'(1/2)/\zeta(1/2)=\alpha\) follows from the completed functional equation. Thus Part 3 v3 equation (61) matches the primary theorem, including its domain. Subtracting the exact left prefix gives an upper envelope \(R_{T,a}=U_T-W_x\); its minimum with the exact preterminal load \(P_q^-\) is another upper envelope. Integrating proves

\[
J_q\le\widehat J_{T,\rm pin}
=\int_x^q\min(P_q^-,R_{T,a}(u))\frac{du}{u}.
\]

This is a genuine one-sided estimate, not an assumption of full RH. However the required \(\widehat J_{T,\rm pin}\le C_q\) for every future active event is not proved. Neither clipping, optimizing a finitely verified height, nor a finite successful run discharges it. A fixed finite height also leaves a strictly positive coefficient \(c_T+e_T-2\) multiplying \(\sqrt u\); it cannot be silently discarded in tail asymptotics.

The global signed-memory version independently follows by the same integration by parts:

\[
\Psi(\log x)=B(x)-I_R(x),\quad
I_R(x)=\int_1^x(\psi(u)-u)u^{-3/2}
\left(1+\tfrac12\log(x/u)\right)du,
\]

\[
B(x)=A(\log x)-4\sqrt x+\log x+4.
\]

Its all-\(x\) sign requirement is likewise exactly Suzuki's target. Replacing the signed error by its absolute value loses the cancellation this identity needs; it supplies no missing reserve theorem.

## 6. Two concrete normalization defects

### 6.1 Part 3 v3 equation (75) omits a nonzero Archimedean remainder

Define, for \(u>1\),

\[
h(u)=\operatorname{atanh}(u^{-1/2})+\arctan(u^{-1/2})-2u^{-1/2}
=2\sum_{k\ge1}\frac{u^{-(4k+1)/2}}{4k+1}>0.
\]

The exact smooth slope is \(A'(\log u)=2\sqrt u-\alpha+h(u)\). Since \(Y=\Sigma_{1/2}-A'\), subtraction proves

\[
\boxed{R_{T,a}(u)-M_a(\log u)
=(c_T+e_T-2)\sqrt u+d_T-Y(\log u)-h(u).}
\]

Equation (75) in the downloaded v3 PDF omits \(-h(u)\). This is an exact-identity error, not an asymptotic objection. At \(u=10^{10}\), which is in the theorem's domain for suitable \(T\), exact rational bounds give

\[
\frac25u^{-5/2}<h(u)<\frac{(2/5)u^{-5/2}}{1-u^{-2}}.
\]

Thus the missing term is strictly nonzero even in the intended range. The main constructor retains the full exact slope in (63), so this finding **does not invalidate (61)–(67)**. It invalidates treating (75) as an identity and any exact computation relying on that omission.

### 6.2 The upper-edge display on page 20 loses a factor of two

The source's (85) is \(\Psi(t)=2\sum_{\gamma>0}(1-\cos\gamma t)/\gamma^2\). Under rational independence, finite phase approximation and the absolutely convergent tail imply

\[
\limsup_{t\to\infty}\Psi(t)=4\sum_{\gamma>0}\gamma^{-2},
\]

not the coefficient 2 printed in the unnumbered display following (86). Each finite summand can approach its maximum \(4/\gamma^2\); the tail has arbitrarily small uniform mass. This discrepancy concerns a conditional zero-side calibration statement, not the prime construction or the lower-edge argument.

The correct lower-edge statement, \(\liminf\Psi=0\) under RH, requires neither simplicity nor rational independence. It follows from uniform almost periodicity and \(\Psi(0)=0\). Part 3 v3 already states this correctly; it does **not** claim a fixed positive tail margin.

## 7. Verdict and remaining obstruction

- **PROVED-IN-REPO by reconstruction:** curvature, convex interval localization, reserve/cost identities, and the precise logical equivalence above. These have external predecessors; no priority claim is made.
- **REFUTED:** Part 3 v3 equation (75) as an exact identity; its page-20 upper-edge normalization.
- **CORROBORATED ONLY:** the finite certificate's enumeration count and the reviewed mathematical rounding strategy.
- **UNVERIFIED here:** the complete directed sign computation through \(10^{10}\), later Parts 4–5, and the all-event tail estimate.
- **Not proved:** RH, any globally sufficient new arithmetic reserve inequality, or the claim that finite-height clipping closes the tail.

The first unpaid theorem is still an arithmetic sign theorem: a zero-free construction or estimate proving \(V_q\ge0\) at every required event. The exact \(J_q\le C_q\) formulation has isolated that theorem cleanly but has not reduced its logical strength. The next decisive probe is to test a proposed *independent* estimate by its **additive excess** \(\widehat J_q-J_q\) against the exact reserve, with the small Archimedean remainder retained. Without that estimate, more checkpoint computation cannot finish RH.

Audit execution: four symbolic/exact tests are retained in `tests/test_checkpoint_audit.py`: curvature, the missing remainder with an exact positive lower bound, the smoothing kernel derivative, and formal reserve cancellation. The independently rerun count is retained in `evidence/independent_event_count.json`; reproduce it with `python scripts/checkpoint_event_count.py`. These outputs check the stated identities and enumeration, not the external full positivity run.
