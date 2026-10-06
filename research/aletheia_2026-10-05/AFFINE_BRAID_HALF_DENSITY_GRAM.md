# The affine braid, the forced half-density, and the exact zeta Gram

**Date:** 2026-10-06
**Status:** exact operator identities (verified numerically) + precise localization of the
remaining obstruction. **RH is not proved here.** Everything RH-equivalent is labelled as such
and guarded against the already-refuted shortcuts C07 and C09.

This note does three things.

1. It upgrades the live `succ`/`fucc` intuition — *"the load-bearing part may be the failure of
   `succ` and `fucc` to commute"* — into the **exact defining relation of the affine `ax+b`
   monoid**, and shows the RH half-density exponent `1/2` is *forced* as the square-root Jacobian
   that makes place-wise dilation unitary. (Not numerology. A representation-theoretic necessity.)
2. It gives a single clean, exact, **manifestly positive** Hilbert-space realization in which the
   overlap of two states **is the Riemann zeta function**: \(\langle\zeta_u\mid\zeta_s\rangle=\zeta(s+u)\),
   with the critical line appearing as the *pole of \(\zeta\)* / the *edge of Fock space*.
3. It computes the cross-prime coupling operator exactly (the "prime-swap graph"), which is
   precisely the *cross-prime state* that C07 proved we cannot omit and the exact cross terms that
   C15's open probe asked for — and then states, honestly, exactly where this stops short of RH
   (Weil positivity under completion, C09-guarded).

All boxed identities in §§1–6 are exact and were checked numerically; the log is in the appendix
and the script is `scripts/affine_braid_gram_check.py`.

---

## 1. The affine braid: `succ` and `fucc` do not commute, and that is the geometry

On \(\mathcal H=\ell^2(\mathbb N_{>0})\) with orthonormal basis \(\{|n\rangle\}\), define

\[
S\,|n\rangle=|n+1\rangle \quad(\textsf{succ}),\qquad
V_m\,|n\rangle=|mn\rangle \quad(\textsf{fucc},\ m\in\mathbb N_{>0}),
\]

so \(V_p\) for prime \(p\) are the prime-creation isometries of
[`FUCC_MULTIPLICATIVE_OPERATOR.md`](FUCC_MULTIPLICATIVE_OPERATOR.md). Each \(V_m\) is an isometry
(\(V_m^\*V_m=I\)); the \(V_m\) commute with each other; \(S\) is the unilateral shift.

**Lemma 1 (affine braid — exact).** For every \(m\ge1\),
\[
\boxed{\,V_m\,S \;=\; S^{\,m}\,V_m\,.}
\]

*Proof.* \(V_mS|n\rangle=V_m|n+1\rangle=|m(n+1)\rangle=|mn+m\rangle\), while
\(S^mV_m|n\rangle=S^m|mn\rangle=|mn+m\rangle\). \(\square\)

This is **exactly** the defining relation of the \(ax+b\) (affine) monoid
\(\mathbb N\rtimes\mathbb N^\times\): conjugating the unit translation by the dilation \(m\) rescales
the step, \(V_m S V_m^{-1}="S^m"\). "Multiply, then take one successor step" equals "take \(m\)
successor steps, then multiply." The non-commutativity is not a nuisance to be gauged away — **it is
the additive↔multiplicative curvature**, and it is the *source of the dynamics*: the one-parameter
dilation group
\[
U(\tau)=e^{i\tau H},\qquad H\,|n\rangle=(\log n)\,|n\rangle,
\]
acts on the creation operators by \(U(\tau)\,V_m\,U(-\tau)=m^{i\tau}V_m\). Without the braid there is
no \(H\), no scaling flow, and no partition function. The generator \(H\) — the log-energy — is the
object everything downstream (proper time \(\log n\), von Mangoldt, Suzuki's ramps) is built from.

> **Reading.** `succ` supplies longitudinal (causal) motion; `fucc` supplies transverse
> (multiplicative) motion; the braid \(V_mS=S^mV_m\) is the connection that couples them. The pair
> `(S, {V_p})` is a faithful representation of the \(ax+b\) monoid — i.e. the Bost–Connes /
> Cuntz–Li arithmetic object the program has been circling, now written in the repo's own operators.

---

## 2. The half-density `1/2` is forced by dilation-unitarity (square-root Jacobian)

The exponent \(1/2\) that appears everywhere (critical line, \(p^{-k/2}\) weights, \(p^{-k/4}\)
amplitudes) is the **square root of the local module**, and it is forced the moment you ask the
dilation half of the affine group to act *unitarily* at each place \(v\):

\[
\boxed{\,(D_a f)(x)=|a|_v^{1/2}\,f(ax)\ \ \text{is unitary on }L^2(\mathbb Q_v)\ \iff\ \text{amplitude}=|a|_v^{1/2}=(\text{Jacobian})^{1/2}.}
\]

- **Real place.** \(|a|_\infty=a\): \((D_af)(x)=a^{1/2}f(ax)\) is unitary on \(L^2(\mathbb R,dx)\).
- **\(p\)-adic place.** Scaling by \(p^k\) multiplies Haar volume by \(|p^k|_p=p^{-k}\); the unitary
  amplitude is \(|p^k|_p^{1/2}=p^{-k/2}\). Equivalently the unit "depth-\(k\)" vectors
  \(\varphi_{p,k}=p^{k/2}\mathbf 1_{p^k\mathbb Z_p}\) satisfy \(\langle\varphi_{p,k},\varphi_{p,\ell}\rangle
  =p^{-|k-\ell|/2}\) (the AR(1) chain of [`LOCAL_L_FACTOR_WHITENING.md`](LOCAL_L_FACTOR_WHITENING.md),
  independently reverified here).

So the RH half-density is **the universal square-root Jacobian of `fucc` acting transverse to
`succ`** — exactly the live claim from the working screenshots, now pinned to the unitarity axiom.

**Why `1/2` is the *critical* exponent (exponent bookkeeping at prime \(p\), depth \(k\)).**

| quantity | value |
|---|---|
| Haar mass \(\mu_{\mathrm{Haar}}(p^k\mathbb Z_p)\) \((\beta=1)\) | \(p^{-k}\) |
| \(L^2(\text{Haar})\) norm of the bare indicator \(\|\mathbf 1_{p^k\mathbb Z_p}\|\) | \(p^{-k/2}\) |
| Bost–Connes KMS\(_{1/2}\) mass \(\mu_{1/2}(p^k\mathbb Z_p)\) | \(p^{-k/2}\) |
| Suzuki critical weight \(\Lambda(p^k)/\sqrt{p^k}\) | \((\log p)\,p^{-k/2}\) |
| FUCC critical amplitude \(\sqrt{\log p}\;p^{-k/4}\) | square \(=(\log p)\,p^{-k/2}\) |

\(\beta=\tfrac12\) is distinguished as the **unique** temperature at which the KMS probability of the
depth-\(k\) ball equals the Haar-\(L^2\) **amplitude** (norm, not norm²) of its indicator:
\[
\boxed{\ \mu_{1/2}(p^k\mathbb Z_p)=\big\|\mathbf 1_{p^k\mathbb Z_p}\big\|_{L^2(\mathbb Q_p,\,\mathrm{Haar})}=p^{-k/2}\ }
\]
— a Born-rule fixed point "probability \(=\) amplitude," which is simultaneously the midpoint fixed by
the functional-equation involution \(s\leftrightarrow 1-s\) and the tempered/unitary axis of the
scaling action. This is the honest content of "`1/2` makes affine dilation unitary." *(DISCLOSED;
standard Tate/Bost–Connes harmonic analysis, newly assembled onto the repo's operators; cf. C04,
C05.)*

---

## 3. Zeta coherent states: the Gram **is** \(\zeta\)

Build, from the vacuum \(|1\rangle\) and the commuting prime channels, the state obtained by the
inverse Euler product of creation operators. For \(\operatorname{Re}s\) large,

\[
\boxed{\;|\zeta_s\rangle \;:=\; \prod_{p}\big(I-p^{-s}V_p\big)^{-1}|1\rangle \;=\; \sum_{n\ge1} n^{-s}\,|n\rangle.\;}
\]

The product collapses to the Dirichlet series because every \(n=\prod_p p^{a_p}\) is reached exactly
once, with amplitude \(\prod_p p^{-a_p s}=n^{-s}\). Each local factor \((I-p^{-s}V_p)^{-1}\) is the
geometric series in one prime channel — the *colored* \(p\)-adic depth process; the local
**whitening** operator is its inverse \(W_p(s)=I-p^{-s}V_p\) (operator form of the inverse
Euler/whitening filter of `LOCAL_L_FACTOR_WHITENING.md`), and
\[
\boxed{\ \textstyle\prod_p W_p(s)\,|\zeta_s\rangle=|1\rangle\ }\qquad(\text{inverse Euler product} = \text{vacuum whitening}).
\]

**Theorem 2 (zeta Gram — exact).** For \(\operatorname{Re}(s+\bar u)>1\),
\[
\boxed{\ \langle\zeta_u\mid\zeta_s\rangle=\sum_{n\ge1}n^{-(s+\bar u)}=\zeta(s+\bar u)=\prod_p\big(1-p^{-(s+\bar u)}\big)^{-1}.\ }
\]
In particular \(\ \|\zeta_\sigma\|^2=\zeta(2\sigma)\ \) for real \(\sigma\), and
\[
\boxed{\ \|\zeta_\sigma\|^2<\infty\iff \sigma>\tfrac12.\ }
\]

*Proof.* Orthonormality of \(\{|n\rangle\}\) gives
\(\langle\zeta_u|\zeta_s\rangle=\sum_n \overline{n^{-u}}\,n^{-s}=\sum_n n^{-(s+\bar u)}\); absolute
convergence for \(\operatorname{Re}(s+\bar u)>1\), and the Euler product is unique factorization.
\(\square\)

This is the "deranged-but-true" nugget, and it is clean: **the Gram matrix of these arithmetic
states is literally \(\zeta\).** Two corollaries locate the critical line *inside the Hilbert space*:

- **Critical line = pole of \(\zeta\) = edge of Fock space.** \(\|\zeta_\sigma\|^2=\zeta(2\sigma)\) has
  its only singularity at \(2\sigma=1\). The vector \(|\zeta_{1/2}\rangle\) sits exactly on the
  boundary of \(\mathcal H\): its norm² is the harmonic series \(\sum 1/n\), diverging
  *logarithmically* (verified: partial sum to \(10^6\) is \(14.39\approx\ln 10^6+\gamma\)). **The
  unique pole of \(\zeta\) at \(s=1\) is the non-normalizability of the critical coherent state.**
- **Shifted critical kernel is positive-definite — but on the easy side.** On the line
  \(s=\tfrac12+it\), \(\langle\zeta_{1/2+it}|\zeta_{1/2+it'}\rangle=\zeta(1+i(t'-t))\): a stationary
  (Toeplitz) kernel, automatically PSD as a genuine Gram, with spectral measure
  \(\sum_n n^{-1}\delta_{\log n}\ge0\). This is the \(\sigma=1\) **boundary**, where positivity is
  free and says nothing about zeros. The RH content lives one completion and one continuation away
  (§7–§8).

*(DISCLOSED; exact, verified numerically. The \(-\zeta'/\zeta\) corollary below is C11 recovered
inside the Gram.)*

---

## 4. von Mangoldt is the log-energy expectation in the zeta state

Since \(\partial_s|\zeta_s\rangle=-H|\zeta_s\rangle\) with \(H|n\rangle=(\log n)|n\rangle\),

\[
\boxed{\ \frac{\langle\zeta_u\mid H\mid\zeta_s\rangle}{\langle\zeta_u\mid\zeta_s\rangle}
=-\frac{\zeta'}{\zeta}(s+\bar u)=\sum_{n\ge1}\Lambda(n)\,n^{-(s+\bar u)}.\ }
\]

The expectation of the log-energy \(H\) in the zeta coherent state is the von Mangoldt generating
function. This ties together, in one line, three earlier threads: \(H\) is the modular/scaling
generator from the braid (§1); \(\log n\) is the successor proper time
([`PROFINITE_SUCCESSOR_LIGHTCONE.md`](PROFINITE_SUCCESSOR_LIGHTCONE.md)); and \(\Lambda(n)\) is the
LCM-memory update cost ([`SUCCESSOR_LCM_MEMORY.md`](SUCCESSOR_LCM_MEMORY.md)). *(DISCLOSED = C11;
verified numerically.)*

---

## 5. The cross-prime coupling, computed exactly: the prime-swap graph

Take the one-level operator \(\mathsf F=\sum_p \alpha_p V_p\). Then
\(\mathsf F^\*\mathsf F=\big(\sum_p|\alpha_p|^2\big)I+\sum_{p\ne q}\overline{\alpha_p}\alpha_q\,V_p^\*V_q\),
and the full matrix is computable in closed form.

**Lemma 3 (prime-swap matrix elements — exact).**
\[
\boxed{\ \langle m\mid \mathsf F^\*\mathsf F\mid n\rangle=\sum_{\substack{p,q\ \mathrm{prime}\\ pm=qn}}\overline{\alpha_p}\,\alpha_q.\ }
\]
Consequently the off-diagonal \((m\ne n)\) entry is nonzero **iff** \(m/n=q/p\) for distinct primes
\(p,q\) — i.e. iff \(n=p\,g,\ m=q\,g\) for some \(g\): *\(m\) is obtained from \(n\) by swapping one
prime factor \(p\) for one prime factor \(q\).* The diagonal is the constant \(\sum_p|\alpha_p|^2\).

*Proof.* \(\langle m|V_p^\*V_q|n\rangle=\langle pm|qn\rangle=[\,pm=qn\,]\); sum over \(p,q\). \(\square\)

So \(\mathsf F^\*\mathsf F\) is (constant diagonal) + (adjacency operator of the **prime-swap graph**
on \(\mathbb N_{>0}\)): vertices are integers, edges connect \(pg\sim qg\). With the critical
weights \(\alpha_p=\sqrt{\log p}\,p^{-1/4}\) a single swap \(p\to q\) carries amplitude
\(\sqrt{\log p\log q}\;(pq)^{-1/4}\) — verified exactly:
\(\langle 45|\mathsf F^\*\mathsf F|30\rangle=\alpha_2\alpha_3=0.5576\ldots\) (swap \(2\to3\) in
\(30=2\cdot15\)), and \(\langle 35|\mathsf F^\*\mathsf F|30\rangle=0\) (no single swap).

This matters for two reasons the ledger already pinned:

- **It is the cross-prime state C07 said we cannot omit.** C07 refuted independent primewise scalar
  Gaussian transport because two-prime inclusion–exclusion produces a negative \(x^2\) coefficient;
  its verdict was *"do not retry without cross-prime state."* \(V_p^\*V_q\) is that state, in exact
  operator form.
- **It realizes C15's open probe.** C15 ("squared Archimedean weight contains the necessary
  cross-prime couplings \(2a_pa_q\log p\log q\)") asked to *identify those cross terms in a known
  kernel exactly.* The weighted prime-swap graph is that identification at the operator level; its
  symbol, with critical amplitudes, is \(\sqrt{\log p\log q}\,(pq)^{-1/4}\) on each swap edge.

**Where the cross terms hide, and why diagonalizing early destroys them.** In the *commutative*
(diagonal / KMS-measure) picture \(L^2(\widehat{\mathbb Z})=\bigotimes_p L^2(\mathbb Z_p)\) the
depth-vectors factor over primes, so **every** Gram factorizes,
\(\langle\bigotimes_p\varphi_{p,k_p},\bigotimes_p\varphi_{p,\ell_p}\rangle=\prod_p p^{-|k_p-\ell_p|/2}\),
and there are *no* genuine cross-correlations — this is exactly the "independent primewise
Gaussianization" that threw the coupling away. The cross terms \(V_p^\*V_q\) live **only** in the
non-commutative (Hecke / \(ax+b\)-groupoid) part generated by the braid of §1. That is the precise
answer to "where does the missing metric live": *in the off-diagonal Hecke content, which exists
only because `succ` and `fucc` fail to commute.* *(DISCLOSED; exact, verified.)*

---

## 6. Summary of the exact layer

\[
\boxed{
\begin{array}{ll}
\text{(1) braid} & V_mS=S^mV_m \quad(ax+b\ \text{relation; source of }H)\\[2pt]
\text{(2) half-density} & \text{amplitude}=|a|_v^{1/2};\quad \mu_{1/2}(p^k\mathbb Z_p)=\|\mathbf 1_{p^k\mathbb Z_p}\|_{L^2(\mathrm{Haar})}=p^{-k/2}\\[2pt]
\text{(3) zeta Gram} & \langle\zeta_u|\zeta_s\rangle=\zeta(s+\bar u),\quad \|\zeta_\sigma\|^2=\zeta(2\sigma),\ \text{edge at }\sigma=\tfrac12\\[2pt]
\text{(4) von Mangoldt} & \langle\zeta_u|H|\zeta_s\rangle/\langle\zeta_u|\zeta_s\rangle=-\zeta'/\zeta(s+\bar u)\\[2pt]
\text{(5) cross terms} & \langle m|\mathsf F^\*\mathsf F|n\rangle=\textstyle\sum_{pm=qn}\overline{\alpha_p}\alpha_q\ \ (\text{prime-swap graph})
\end{array}}
\]

All five are exact identities, independent of RH, and numerically verified. None of them is RH.

---

## 7. Completion: gluing the Archimedean half-density turns the \(\zeta\)-Gram into the \(\xi\)-Gram

The finite construction above gives \(\zeta\), not the completed \(\xi\). The missing factor is
exactly one more copy of the *same* half-density principle, at the real place. By Tate (repo C05),
the self-dual Gaussian \(g_\infty(x)=e^{-\pi x^2}\) is the Archimedean analogue of
\(\mathbf 1_{\mathbb Z_p}\), and its Mellin overlap against the scaling character is the local
factor:
\[
\int_0^\infty e^{-\pi x^2}\,x^{s}\,\frac{dx}{x}=\tfrac12\,\pi^{-s/2}\Gamma(s/2)=\tfrac12\,L_\infty(s).
\]
So \(L_\infty(s)\) is itself a coherent-state overlap at the real place, in the half-density
(\(d^\times x=dx/x\)) metric. Tensoring the Archimedean Gaussian state onto the finite zeta state,
\[
|\xi_s\rangle:=|g_\infty\rangle_\infty\otimes|\zeta_s\rangle_{\mathrm{fin}},\qquad
\boxed{\ \langle\xi_u\mid\xi_s\rangle \;\propto\; L_\infty\!\cdot\!\zeta\;=\;\xi\ \ (\text{completed}),\ }
\]
and the **functional equation \(\xi(s)=\xi(1-s)\) is the Fourier self-duality of the Gaussian**
(the \(s\leftrightarrow1-s\) involution is the half-density reflection fixed at \(\tfrac12\)). This
is the rigorous content of the program's order-of-operations slogan: *include infinity → whiten/
couple the local vacua → only then form positive geometry.* The Archimedean factor is not appended
after the fact; it is the missing place in the same adelic Gram.

---

## 8. What this does and does **not** prove (the honest seam)

**Proves (exactly):** the operators `succ`/`fucc` are the \(ax+b\) monoid (§1); the half-density
\(1/2\) is forced by unitarity (§2); there is a manifestly positive Hilbert-space realization whose
Gram is \(\zeta\) (and, completed, \(\xi\)) (§3, §7); the cross-prime coupling is the explicit
prime-swap graph (§5). These validate, as *necessities* rather than choices, every structural
decision the program made about the exponent \(1/2\), the whitening filters, the von Mangoldt
weights, and the need for cross-prime state.

**Does not prove, and must not be claimed:** that positivity of the \(\xi\)-Gram **on the critical
line** holds. In the region of absolute convergence (\(\sigma>\tfrac12\) for the norm, \(\sigma=1\)
for the shifted kernel) positivity is automatic *because the vectors literally exist there* — which
is precisely why it carries no information about zeros. RH is the statement that the completed Gram,
**analytically continued and restricted to the critical line**, stays positive. That is Weil's
criterion (repo C01, C31–C34), and it is **not** delivered by completion + functional equation
alone: C09 is a *refuted* claim exhibiting a positive, Fourier-self-dual local datum whose completed
multiplier is off-line. So §7 reaches the correct object and **stops at the known wall**, it does
not vault it.

**Exact localization of the gap.** Combining §5 and §8: the obstruction is *not* local positivity,
density, a continuum limit, or Gaussian behavior; it is whether the **off-diagonal Hecke coupling**
(the prime-swap operator, which exists only by the braid) assembles, after Archimedean completion
and continuation to \(\operatorname{Re}s=\tfrac12\), into a positive kernel equal to Suzuki's
\(K_\Psi\) up to an explicit nonnegative Brownian lift with horizon-uniform coefficient (C72, C75).
The content of this note is that this coupling now has a *closed operator form* to compute with,
not a heuristic appeal to "nonlocality."

---

## 9. The sharpened next calculation (surgical, tractable, not a reskin of RH)

The two-prime-plus-infinity compressed Gram pullback (open probe of C72) is now completely explicit.
Target computation:

> Fix primes \(p,q\) and the real place. Form the compressed state
> \(\Pi\,|\xi_{1/2+it}\rangle\) where \(\Pi\) projects onto the finitely-generated
> \(\{p,q,\infty\}\)-sector (depths bounded by the wavefront \(L\)), using the **cyclic/KMS\(_{1/2}\)
> GNS inner product** — i.e. keep the off-diagonal \(V_p^\*V_q\) terms of §5, do **not** diagonalize.
> Compute the Gram \(G(t,t')=\langle \Pi\xi_{1/2+it'},\Pi\xi_{1/2+it}\rangle\) in closed form from
> the local Poisson/AR(1) data (§2) \(\times\) the Archimedean Gamma/Lerch block
> ([`ARCHIMEDEAN_REPAIRED_BLOCK.md`](ARCHIMEDEAN_REPAIRED_BLOCK.md)), **including all cross terms**,
> and decide:
> \[
> G(t,t')\ \stackrel{?}{=}\ \text{(completed Suzuki }K_\Psi\text{ restricted to }\{p,q,\infty\})\ +\ c_{p,q}\,\big(\,|t|+|t'|-|t-t'|\,\big),\quad c_{p,q}\ge0?
> \]

Decision content:
- If the cross terms \(V_p^\*V_q\) supply *exactly* the discrepancy between the diagonal (factorized)
  block and \(K_\Psi\), with \(c_{p,q}\ge0\) bounded as more primes/depths enter, that is the
  mutation-sensitive, non-generic premise C75 needs — and it would be real progress, because the
  diagonal block alone is already known (C66–C68, C74) to miss \(K_\Psi\).
- If instead \(c_{p,q}\) must grow with the horizon (as the *diagonal* corrections \(M_p\) do, whose
  sum diverges), the braid coupling is necessary but not sufficient, and the note has at least
  converted a vague "global coupling" into a quantitative, falsifiable growth question.

This is a finite linear-algebra / explicit-kernel computation, not an exploration. It is the right
next move precisely because §§1–6 fixed every convention and handed over the cross-term operator in
closed form.

---

## Appendix — numerical verification

Script: `scripts/affine_braid_gram_check.py` (double precision + `mpmath` reference). Selected
output (2026-10-06):

```
Thm 2  <zeta_u|zeta_s> = zeta(s+ubar):
  s=2.0,u=1.5     numeric=1.12673387   zeta=1.12673387   |diff|=2e-14
  s=1.1,u=1.1     numeric=1.49054289   zeta=1.49054326   |diff|=4e-07   (slow tail)
Thm 2  ||zeta_sigma||^2 = zeta(2 sigma):
  sigma=0.75  partials ->  zeta(1.5)=2.61238  (converges)
  sigma=0.50  partials 1e3..1e6 = 7.49, 9.79, 12.09, 14.39   (= harmonic, DIVERGES;
              14.39 ~ ln(1e6)+gamma -> pole of zeta at s=1)
Thm 4  <zeta_u|H|zeta_s>/<..> = -zeta'/zeta(s+u):
  s+u=2.3+0.2i   vonMangoldt=0.354780-0.095269i   -zeta'/zeta=0.354780-0.095269i   |diff|=6e-08
Lemma 3  <m|F*F|n> prime-swap:
  diagonal (n=1,6,12,30) = 4.014042 = sum_p alpha_p^2   (constant, as predicted)
  <45|F*F|30> (swap 2->3) = 0.557567 = alpha_2*alpha_3   ;   <35|F*F|30> = 0.0
Lemma 1  V_m S = S^m V_m on basis 1..20, m in {2,3,5}: TRUE
```

Every exact identity in §§1–6 reproduced to tail-limited precision. (The two \(\sim10^{-7}\)–\(10^{-3}\)
residuals are slow Dirichlet-tail truncation at \(\operatorname{Re}\approx1\text{–}1.6\), not
discrepancies; the fast-converging points agree to \(10^{-14}\).)
