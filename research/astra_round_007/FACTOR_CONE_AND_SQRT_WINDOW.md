# Factor cone: exact geometry, full boundary current, and a locality obstruction

Date: 2026-10-06. Status: elementary identities and scoped operator no-go theorems proved here. RH remains open. No claim of historical priority. Companion: `FINITE_CARRIER_CONE.md`. Reproduce with `python -m unittest tests.test_round007_factor_cone -v` and `python -m scripts.round007_factor_cone`.

## 1. Closed factor incidence and its canonical normalization

Write \(\mathscr F_n=\{(a,b):ab=n\}\), \(d(n)=|\mathscr F_n|\), and
\(\mathscr H_F=\bigoplus_{n\ge1}\ell^2(\mathscr F_n)\).
The finite-support map \(M_0 e_{a,b}=e_{ab}\) has closure
\[
(Mx)_n=\sum_{ab=n}x_{a,b},\qquad
\operatorname{Dom}M=\{x\in\mathscr H_F:\sum_n|\sum_{ab=n}x_{a,b}|^2<\infty\}.
\]
It is closed: convergence in the factor Hilbert space gives convergence of each finite fiber sum, and convergence of the image in \(\ell^2\) identifies those sums. Truncation by the product \(ab\le N\) proves that finite support is a graph core. Its adjoint is
\[
(M^*y)_{a,b}=y_{ab},\qquad
\operatorname{Dom}M^*=\{y:\sum_n d(n)|y_n|^2<\infty\}.
\]
Consequently
\[
MM^*=d(X),\qquad \operatorname{Dom}(MM^*)=\{y:\sum_n d(n)^2|y_n|^2<\infty\}.
\]
Neither incidence nor its adjoint is bounded: divisor multiplicities are unbounded.

To avoid confusion with factor swap, use \(J_F\) for the normalized lift:
\[
J_F e_n=\frac1{\sqrt{d(n)}}\sum_{ab=n}e_{a,b},\qquad
J_F^*J_F=I,\qquad M=d(X)^{1/2}J_F^*.
\]
The projection \(J_FJ_F^*\) averages coefficients inside each factor fiber. For a bounded diagonal factor observable \(F(a,b)\),
\[
J_F^*FJ_F e_n=\frac1{d(n)}\sum_{ab=n}F(a,b)e_n.
\]
This fiber normalization is a canonical isometry, not a nontrivial positive Weil factorization. This is precisely the limitation already present in Round004 C87. Likewise, the commuting prime-coordinate Koszul mechanism from C88 is not repaired merely by relabeling its fibers.

## 2. Swap, cone, and the information lost by projection

Let \(R e_{a,b}=e_{b,a}\), \(R^2=I\), and \(\Pi_\triangle=1_{a\le b}\). Then
\[
MR=M,\qquad M(I-R)=0,\qquad
a\le b\iff 2\log a\le\log(ab).
\]
The fixed locus \(a=b\) projects exactly to squares. With \(c=(\log a+\log b)/2\) and \(r=(\log a-\log b)/2\), swap fixes \(c\) and sends \(r\) to \(-r\). These are exact coordinates; they do not impose a measure or an amplitude.

An oriented first-order map with no fitted coefficients is
\[
C_F=(I-R)\Pi_\triangle M^*.
\]
On an off-diagonal unordered factor pair it produces \(e_{a,b}-e_{b,a}\), and on a diagonal pair it vanishes. Thus, on the finite-support core,
\[
C_F^*C_F e_n=(d(n)-1_{n\text{ square}})e_n,
\qquad MC_F=0.
\]
Projection before taking the norm discards a nonzero energy. Conversely, keeping it gives the displayed divisor statistic, not the von-Mangoldt statistic.

Removing units and choosing a single triangular representative gives
\[
D_\triangle e_n=\sum_{\substack{ab=n\\2\le a\le b}}e_{a,b},\qquad
D_\triangle^*D_\triangle e_n=c(n)e_n,
\]
\[
c(n)=\frac{d(n)+1_{n\text{ square}}}{2}-1.
\]
The formula includes \(n=1\), where both sides vanish. For \(n=p^k\), \(c(n)=\lfloor k/2\rfloor\). Thus it vanishes at every prime, where \(\Lambda(p)>0\). The pure count cannot supply the prime-power charge: for example \(18\) and \(32\) have the same divisor count, square indicator, and triangular count, but only \(32\) is a prime power. A weighted or incidence-sensitive construction must therefore contain additional information. This does not prohibit using the full divisor poset: it is a chain exactly for prime powers.

## 3. Ambient cone versus actual divisibility incidence

In carrier-first ordering, on \(\ell^2\{(n,a):n,a\ge1\}\), set
\[
S_Xe_{n,a}=e_{n+1,a},\quad
\Pi e_{n,a}=1_{a^2\le n}e_{n,a},\quad
I_De_{n,a}=1_{a\mid n}e_{n,a},\quad F=I_D\Pi.
\]
The ambient cone identity is
\[
[\Pi,S_X]e_{n,a}=1_{n+1=a^2}e_{n+1,a}.
\]
For prime-clock labels the projection is **\(I\otimes P_{\mathbb P}\)** in this tensor ordering. Section 7 of the integrated side note writes \(P_{\mathbb P}\otimes I\); that ordering is a typo, not a mathematical variant.

The actual divisor-fired current has an additional bulk term:
\[
\boxed{
[F,S_X]e_{n,a}=\left[
1_{n+1=a^2}
+1_{a^2\le n}(1_{a\mid n+1}-1_{a\mid n})
\right]e_{n+1,a}.}
\]
Proof: insert and subtract \(1_{a\mid n+1}1_{a^2\le n}\); at the threshold \(n+1=a^2\), divisibility is automatic. This establishes every term, including its sign.

For \(a>1\), consecutive integers cannot both be divisible by \(a\). Therefore the current equals \(+1\) at every entering fire \(n+1=ka\), \(k\ge a\), and \(-1\) at every leaving fire \(n=ka\), \(k\ge a\). Only the first entering fire is a square threshold. The other fires occur arbitrarily far inside the cone. In particular
\[
|[F,S_X]_{(n+1,a),(n,a)}|^2=F(n+1,a)+F(n,a)
\quad(a>1).
\]
At \((n,a)=(5,2)\), the current is \(+1\), with zero square-boundary term; at \((6,2)\) it is \(-1\). The distinction is already visible before taking any infinite limit.

**Verdict:** the ambient cone has a square-supported boundary; the divisor incidence required for arithmetic has a nonzero bulk current. Replacing the second by the first drops an exact term, not a small asymptotic error.

For a positive rational slope \(c=u/v\), replace the gate by \(a^v\le n^u\). Its ambient current is
\[
1_{n^u<a^v\le(n+1)^u}.
\]
Only \(c=1/2\) has the square-threshold interpretation. These masks are tested without floating-point logarithms.

## 4. Same-factor transport obstruction

**Theorem.** Let a lift on the finite-support carrier core have the form
\[
Le_n=\sum_{\substack{a\mid n\\a>1}}\ell(n,a)e_{n,a},
\]
where the coefficients may be complex, weighted, or cone-gated. Whenever the displayed compositions are defined, for \(h\ge1\),
\[
\boxed{
L^*S_X^hLe_n=
\left(\sum_{\substack{a\mid\gcd(n,h)\\a>1}}
\overline{\ell(n+h,a)}\ell(n,a)\right)e_{n+h}.}
\]
Proof: \(S_X^h\) preserves the label \(a\); the target lift has that label only when \(a\mid n+h\). Together with \(a\mid n\), this is exactly \(a\mid\gcd(n,h)\). No assumption on coefficient signs enters.

Three consequences are sharp.

1. **Nearest SUCC transport vanishes:** \(L^*S_XL=0\). Thus
   \[
   L^*(2I-S_X-S_X^*)L=2L^*L,
   \]
   a diagonal carrier energy. No choice of weights repairs its missing cross terms.
2. If carrier propagation is at most \(R\) and preserves factor labels, every channel \(a>R\) has zero off-diagonal compression. Increasing a fixed local stencil cannot couple arbitrarily large prime channels.
3. Restoring \(a=1\) restores the nearest cross term, but it comes **entirely from the unit label**. Nonunit arithmetic channels still contribute none.

This theorem is not a claim against all lifted operators. To escape it one must mix factor labels, allow unbounded carrier propagation, or introduce another coupling before compression. For example \(J_FSJ_F^*\) does mix all source and target fibers, and its compression is tautologically \(S\); constructing it does not establish a Weil identity.

## 5. What forces a half-density, and what does not

The factor cone and swap do not force the amplitude exponent. For every \(\beta\ge0\), define the bounded lift
\[
L_\beta=J_FX^{-\beta}.
\]
All these lifts have identical nonzero factor support, obey \(RL_\beta=L_\beta\), and obey the same cone restrictions. Yet
\[
L_\beta^*L_\beta=X^{-2\beta}.
\]
Thus an entire continuum of square weights is compatible with precisely this geometry. This is a counterexample to determination of the Suzuki half-density by cone/swap/support alone. Adding phase \(n^{it}\) leaves this counterexample intact. Requiring an isometric lift selects the normalization \(\beta=0\), not the Suzuki coefficient.

There is a separate, exact measure-theoretic statement. On \(L^2(\mathbb R_+,x^{q-1}dx)\), an operator
\[
U_af(x)=a^{-\gamma}f(x/a)
\]
has squared norm \(a^{q-2\gamma}\|f\|^2\). For real \(\gamma\), unitarity for every \(a>0\) forces \(\gamma=q/2\). Lebesgue measure \(dx\) gives \(1/2\); multiplicative Haar measure \(dx/x\) gives zero. The unitary coordinate map from the first space to log-coordinate Lebesgue measure is \(f\mapsto e^{qt/2}f(e^t)\).

On the discrete counting space, \(V_pe_n=e_{pn}\) is already an isometry without a factor \(p^{-1/2}\). Therefore a derivation connecting the analytic measure convention to the factor geometry is still required. The geometric number \(1/2\) in a cone boundary and the analytic exponent \(1/2\) in the explicit formula have not been unified by the cone identities.

## 6. Classical accounting and limits of novelty

The factor lift is the adjoint of multiplication, and \(M(f\otimes g)=f*g\) is Dirichlet convolution for finitely supported sequences. Finite divisor sums make the coproduct coassociative. Möbius inversion gives \(\Lambda=\mu*\log\); this has not been promoted into a new positive square. C88 already rules out the stated factorized Koszul repair.

The factor-swap split and hyperbola counting are classical. A primary author exposition is Terence Tao, [254A, Notes 1](https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/), equations (54)–(56), Remark 41; Dirichlet convolution and its series transform occur in the same notes, equations (35), (44). The use here is finite counting with no hypotheses on prime distribution. The current decomposition and locality theorem above are independently proved; no priority claim is made for them.

The new information for this program is the exact obstruction: the divisor gate produces a bulk current, and preserving a nonunit factor across one carrier step kills its compressed cross term. Neither fact is a tail estimate or an RH-equivalent reformulation.
