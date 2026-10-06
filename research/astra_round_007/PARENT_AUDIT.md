# Round006 parent audit: retained identities and invalid no-go arrows

Parent: `d3e29723fcf9df107fc55a75716e5255898c1b53`. Date: 2026-10-06.
RH is open. The parent dossiers are frozen. This note corrects the claims
inherited from them; it does not restart the prohibited scalar-passivity
research program.

## Verdict

The Schur–Vitali continuation argument and the exact arithmetic/Archimedean
identities survive. The claimed universal source-response obstruction, the
identification of a shifted xi ratio with its logarithmic derivative, and
the claimed Pontryagin-index evidence do not survive audit. The particular
Euler–Maclaurin finite completion really fails positivity, as the certified
counterexample below confirms. Conrey–Li really excludes their stated
translation-positivity conditions. Neither fact proves the broader claims.

| Parent assertion | Audited status | Exact boundary |
|---|---|---|
| Schur functions on `Re s>1/2` plus Euler-side convergence force RH | PROVED-IN-REPO; retained | Conditional theorem; the Schur hypothesis remains unpaid |
| `xi'/xi=A_inf+zeta'/zeta` | PROVED-IN-REPO; retained | Meromorphic identity; Euler series only for `Re s>1` |
| `½ psi(s/2)` is passive because its poles are outside the domain | REFUTED | It equals `−gamma/2<0` at `s=2` |
| One pole at `s=1` means one negative square in the positive-real convention | REFUTED | Its standard positive-real kernel has infinite negative index |
| `Re xi'/xi>=0` is equivalent to `Re xi(s)/xi(s+1)>=0` | REFUTED as an identification/implication | Different functions and different positivity conditions |
| Conrey–Li makes the `H(E)` Hilbert norm indefinite | REFUTED | The extra translation quadratic form fails; the Hilbert norm stays positive |
| Any permitted cutoff boundary gives `inf Re F_P -> -infinity` unconditionally | UNVERIFIED; stated scope is equivalent to **not RH** | Proof has uncontrolled boundary and recurrence-height gaps |
| Negative excursions count Cayley poles and Pontryagin negative squares | REFUTED | Exact constant counterexample below |
| The particular finite completion is Schur/passive | REFUTED | Arb certificate at `P=200`, `s=51/100` |
| No parent can change a fixed scalar function | PROVED-IN-REPO; retained | Does not prevent a new parent from proving a true property of that function |

## 1. Primary-source boundary

[Lagarias, *On a positivity property of the Riemann xi-function*](https://websites.umich.edu/~lagarias/doc/positivity.pdf),
introduction (1.4)–(1.5), states positivity of `Re xi'/xi` for `Re s>1`
and its equivalence to RH on `Re s>1/2`. The author's PDF was rendered because
its text extraction is corrupted. The
[2005 correction](https://www.impan.pl/shop/en/publication/transaction/download/product/81942)
repairs Lemma 3.1 and the sign of `1/(s−1)` in (3.8); it does not replace
the logarithmic derivative by a shifted ratio.

[Conrey–Li, arXiv:math/9812166v1](https://arxiv.org/pdf/math/9812166),
Theorems 1–2 and Section 3.1, concern **additional** translation positivity
on positive reproducing-kernel Hilbert spaces. Their norm is an integral
with positive weight. They show that the prescribed translation form fails
for the xi-associated spaces. Their (3.4) exhibits a negative shifted ratio.
This is not a theorem that `xi'/xi` fails positive-realness, nor that the
original Hilbert norm is indefinite. Their normalization of xi omits the
factor `1/2`; ratios and logarithmic derivatives are unchanged. The Sarnak
remark in Section 4 also concerns the shifted ratio, not the logarithmic
derivative. No density argument is imported here to assert anything else.

These are primary-source constraints, not evidence for or against RH.
Source retrieval details and scalar certificates are in
`reviews/parent_sources.json`.

## 2. What the Schur–Vitali theorem actually gives

Put `H={Re s>1/2}` and `U={Re s>1}`. If holomorphic `Theta_P` on `H`
satisfy `|Theta_P|<=1` and converge on `U` to the nonconstant Cayley
transform of `xi'/xi`, Montel gives subsequential locally uniform limits.
The identity theorem on `U` makes every limit equal. The maximum principle
puts the limit strictly inside the disk. Its inverse Cayley transform is
holomorphic on `H` and agrees with `xi'/xi` on `U`. Thus xi has no zero
in `H`, and the functional equation gives RH. This proof is valid.

The reverse implication obtained by setting every approximant equal to the
limiting Cayley transform concerns **unrestricted analytic sequences**.
It does not construct finite arithmetic hardware. Therefore:

* the conditional continuation theorem survives;
* an iff assertion for a specifically constrained class of finite arithmetic
  realizations needs an additional construction in the reverse direction;
* “a construction would prove RH” does not mean “an unconditional
  construction cannot exist.” The latter is not a mathematical consequence.

## 3. Logarithmic derivative versus shifted ratio

If a zero-free analytic function `f` admits a logarithm along the horizontal
segment, then

\[
\frac{f(s)}{f(s+1)}
=\exp\!\left(-\int_0^1\frac{f'}{f}(s+x)\,dx\right).
\]

Positive real part of the logarithmic derivative controls the **modulus**
of this ratio. It does not control the cosine of its argument.

An exact synthetic control, including the functional symmetry, is
`f(s)=exp((s−1/2)^2)`. It satisfies `f(1−s)=f(s)` and

\[
\Re(f'/f)=2\Re s-1>0\quad(\Re s>1/2),\qquad
f(s)/f(s+1)=e^{-2s}.
\]

At `s=1+i*pi/2` the ratio is `−e^{-2}<0`. This example has order two,
so it is not a replacement xi function or a claim about the RH criterion;
it decisively refutes the purported general positivity implication.

For the actual xi function, Arb certifies at `s=1+282i`:

\[
\Re\frac{\xi(s)}{\xi(s+1)}
\in -0.0001319572933720834407131353022886\ldots\pm 4.46\,10^{-69},
\]
\[
\Re\frac{\xi'}{\xi}(s)
\in 1.6681300586910107675873999590011\ldots\pm 4.39\,10^{-70}.
\]

The full balls, rather than these abbreviated decimal displays, are stored
in the source manifest. No zero ordinates enter this calculation.
The scalar counterexample does not decide global positivity of `xi'/xi`.

## 4. Correct Archimedean formulas, incorrect passivity label

The exact identity is

\[
A_\infty(s)=\frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\psi(s/2),
\qquad \frac{\xi'}{\xi}=A_\infty+\frac{\zeta'}{\zeta}.
\]

The convergent resolvent-difference expansion is

\[
\frac12\psi(s/2)
=-\frac\gamma2+\sum_{n\ge0}
\left(\frac1{2n+2}-\frac1{2n+s}\right).
\]

Equivalently, with `D=diag(0,2,4,...)`, the summand is the trace of
`(D+2)^{-1}−(D+s)^{-1}`. The **minus** sign on the variable resolvent
is essential. The difference is trace class away from its poles;
the separate resolvent traces diverge. This is not a positive trace of a
resolvent. Pole location alone never proves positive-realness.
At `s=2` the sum vanishes and the answer is `−gamma/2<0`, a complete
counterexample to the parent's passive-Gamma assertion.

The `s=0` singularity does cancel:

\[
A_\infty(0)=-1-\tfrac12(\log\pi+\gamma).
\]

The only pole of `A_inf` in `H` is at `s=1`, of residue `+1`.
Its cancellation with `zeta'/zeta` is exact. Finite prime or prime-power
sums are regular there and cannot cancel it without a boundary completion.
Also `s=0` is not a trivial zeta zero: the Gamma pole there is separately
canceled by the explicit `1/s`.

For fixed real `sigma>1/2`, the digamma asymptotic gives
`Re[psi((sigma+it)/2)/2] = (1/2)log(|t|/2)+o(1)` as `|t|` tends to
infinity. This is the growth term omitted in the parent's recurrence
argument; see [DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2).

## 5. A single pole is not a single negative square

Specify the convention before assigning an index. On `H`, the
positive-real kernel is

\[
K_F(s,u)=\frac{F(s)+\overline{F(u)}}{s+\bar u-1}.
\]

For the claimed one-pole example `F(s)=1/(s−1)`, direct algebra gives

\[
K_F(s,u)=\frac{1}{(s-1)(\bar u-1)}
\left(1-\frac1{s+\bar u-1}\right).
\]

Choose any `n` distinct real points `s_i>1`. The kernel matrix is
congruent to `11^T−C`, where `C_ij=1/(s_i+s_j−1)` is strictly positive
definite: it is the Gram of the linearly independent exponentials
`exp(−(s_i−1/2)t)` in `L²(0,infinity)`. On the codimension-one space
orthogonal to `1`, the quadratic form is strictly negative. Its diagonal
is positive, so it has one positive and exactly `n−1` negative
eigenvalues. Since `n` is arbitrary, **the negative-square index is
infinite**. A Cayley transform preserves this kernel inertia by
nonzero diagonal congruence away from its exceptional points.

This does not contradict a separately defined finite-rank Suzuki pole
kernel. Transforming scalar functions does not automatically identify
their underlying positivity kernels or preserve their indices.

The excursion-count claim fails even more simply. For `F=-2`, its
unit-parameter Cayley transform is the constant `3`: it has **no poles**.
But `Re F<-1` everywhere, and

\[
K_F(s,u)=-\frac4{s+\bar u-1}
\]

has `n` negative eigenvalues on every `n` distinct positive-real sample
points in `H`. Thus it has infinite negative index. Neither pole count
nor connected components of a scalar sublevel set count negative squares.
The parent script's excursion measurements remain finite scalar
measurements only; the claimed index growth and finite-index exclusion
were not proved by that script.

## 6. The arbitrary-boundary no-go contains the whole opposite RH verdict

The class as stated in `PROOF_ATTEMPT_006.md` allows **any** holomorphic
`A_P` on `H` with `A_P -> A_inf` locally uniformly on `U`, and sets

\[
D_P(s)=\sum_{n\le P}\Lambda(n)n^{-s},\qquad F_P=A_P-D_P.
\]

Then `F_P -> xi'/xi` on `U`. There is no finite-realization restriction
on `A_P` in that theorem statement.

**Lemma (exact scope of the claimed universal theorem).** For this
unrestricted class, the assertion

> For every admissible family, `inf_H Re F_P -> −infinity`

is equivalent to **RH being false**.

**Proof.** If RH holds, `f=xi'/xi` is holomorphic and positive-real on
`H`. Taking `F_P=f` and `A_P=f+D_P` is admissible, since `D_P` converges
on `U` to `−zeta'/zeta`; the asserted negative divergence fails.

Conversely, if negative divergence fails for an admissible family, some
subsequence has `Re F_P>=−C` on all of `H` for a fixed finite `C`.
Apply the already-valid Montel/Cayley argument to `F_P+C+1` on that
subsequence. Its Euler-side limit is `xi'/xi+C+1`, nonconstant; inverse
Cayley gives a holomorphic continuation of `xi'/xi` across `H`, hence
RH. Contraposition proves the remaining direction. The admissible class
is nonempty, for example by the parent's explicit regularized boundary.
This is a logical audit of the overbroad statement, not a new RH route. ∎

There are two direct defects in the parent's displayed proof:

1. Euler-side convergence puts no bound on an arbitrary boundary in the
   strip. For example `h_P(s)=exp(−P(s−1))` tends to zero locally uniformly
   on `U` and grows exponentially at every fixed real `1/2<s<1`.
   Adding it to a boundary preserves the stated assumptions.
2. Dirichlet simultaneous recurrence gives a height at which finitely many
   prime phases nearly align, but not a sufficiently small height to make
   `log|t|` negligible compared with `P^(1−sigma)`. At fixed `P` the
   prime polynomial is bounded and the Gamma term eventually dominates it.
   Sending `sigma` toward `1/2` afterwards does not supply that missing
   uniform estimate.

No assertion about arbitrary boundaries or index divergence is inherited
as a theorem. This is required by the algebra, not permission to retry the
architecture prohibited by the Round007 brief.

## 7. The specific finite completion still fails

For exactly the parent's explicit choice

\[
F_P^{\rm EM}(s)=\frac1s-\frac12\log\pi+\frac12\psi(s/2)
+\frac{1-P^{1-s}}{s-1}-D_P(s),
\]

the quotient has its removable value `log P` at `s=1`. It is holomorphic
on `H` and has the correct Euler-side limit. Arb certifies

\[
F_{200}^{\rm EM}(51/100)
=-0.5384110930086436120958202229483\ldots<0.
\]

Thus this **particular family**, with all those members, fails the required
positivity. This certificate neither proves eventual failure for every
cutoff nor excludes another boundary. Local Euler factors also genuinely
fail positive-realness: at `s=sigma+i*pi/log p`,
`log p/(p^s−1)=−log p/(p^sigma+1)<0` for every real `sigma>0`.

There is a valid index obstruction for this **specific** completion, but
it has the opposite finite/infinite status from the parent claim. The
formula extends holomorphically across `s=1/2`, and Arb certifies

\[
F_{200}^{\rm EM}(1/2)=-0.56812586486671834114\ldots<0.
\]

**Boundary-negative lemma.** If `F` extends holomorphically across an
open boundary interval of `H` and `Re F<0` there, then `K_F` has infinitely
many negative squares. Indeed, for any `n` choose distinct boundary
ordinates `t_1,...,t_n` in that interval and evaluate at
`s_i=1/2+epsilon+i*t_i`. The diagonal entries are
`Re F(s_i)/epsilon`, tending to negative infinity. Off-diagonal entries
remain bounded as `epsilon` decreases to zero, because their denominators
tend to nonzero `i(t_i−t_j)`. Strict negative diagonal dominance gives
an `n`-dimensional negative definite Gram. Since `n` is arbitrary, the
index is infinite. Continuity and the last scalar certificate supply the
interval for `F_200^EM`. This excludes a finite-index realization of that
specific scalar response under this kernel convention; no family-wide
index growth law is asserted.

## Reproduction and operational consequence

Run:

```sh
python -m unittest tests.test_round007_parent_audit -v
python -m scripts.round007_parent_audit
```

Seven tests check exact algebra, rational matrix inertia, event enumeration,
the removable finite boundary, and certified scalar signs. The proofs of
arbitrary-size inertia and the logical class equivalence are written
above; finite matrices do not substitute for those proofs. A six-point
Arb Gram with strict negative Gershgorin bounds independently checks the
boundary-negative lemma's application to `F_200^EM`.

Round007 should reuse the exact `A_inf`, source charge, and Euler-domain
correlation identities. It must not reuse passive-Gamma, index-one,
ratio/log-derivative, or universal-boundary claims. The research target
remains the completed Weil/Suzuki quadratic form, as the user requested.
