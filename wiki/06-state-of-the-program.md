# 6. State of the program

*This page is the honest current picture, kept as a **living results board**. Numerical results
are **Observed** on a **calibrated** instrument ([page 7](07-methodology-and-discipline.md) for
what that word buys); structural identities are **[derived]**; nothing here is a proof. The
headline is a confirmed **null**: the target is exactly RH-equivalent, measured from every side,
and no unconditional brick has been found. New results land in [§6.2](#62-the-results-board).*

---

## 6.1 The target, named precisely

All the reformulations of [page 2](02-the-rh-equivalent-target.md), the semigroup of
[page 3](03-the-diophantine-semigroup-frame.md), and the symbol of
[page 4](04-the-symbol-and-the-wells.md) converge on one object. On the finite-window test space
(support $L$), the completed Weil form splits as

$$Q = P - K$$

where $P$ is the **archimedean + pole** part ($\text{pole} + \text{arch} + (-\log\pi)\, I$) and $K$
is the **prime semigroup** $K = \sum_n c_n\, \tfrac12\big(T_{\log n} + T_{\log n}^\dagger\big)$ of
[§3.4](03-the-diophantine-semigroup-frame.md).

> **The missing theorem, as a coercivity.** $Q = P - K \succeq 0$ for all admissible finite-window
> test functions — and it must be proved reading the primes (multiplicativity) and **not** the
> zeros.

This is not a new equivalence; it is RH wearing operator clothes ([§5.7](05-what-is-zeta-here.md)).
Its value is that each piece is now something we can *measure* — and did.

## 6.2 The results board

Every row is one measured or derived fact with its status and its ledger round. Grouped by theme;
read top-to-bottom for the arc from "what is free" to "where the wall is." **Pending work lands in
group E and graduates upward when it clears the gate.**

### A — Local positivity: what is free

| # | Result | Status | Source |
|---|---|---|---|
| A1 | Positivity holds unconditionally for $\mathrm{Re}\, s > 1$ (Euler product, $\log\zeta = \sum c_n n^{-s}$, $c_n \ge 0$). | **Demonstrated** (classical) | [§2.5](02-the-rh-equivalent-target.md) |
| A2 | Weil form positive for self-correlations supported in the prime-free window $(\tfrac12, 2)$. | **Demonstrated** (Yoshida; Connes–Consani Thm 1) | [§2.5](02-the-rh-equivalent-target.md) |
| A3 | An unrefereed preprint certifies a wider window $2L = 1.6$ (primes 2, 3 only) — but Euler-blind, with a self-retracted $2.38$ claim. | **Observed** (cited, unrefereed) | R53 |

### B — The coupled form $P - K$ (calibrated instrument)

| # | Result | Status | Source |
|---|---|---|---|
| B1 | The instrument is calibrated: the explicit formula balances at matrix level, $M_{\mathrm{full}} \equiv M_{\mathrm{zeros}}$, to 60 digits. *(This licenses every reading below; it is **not** a test of RH.)* | **Observed** | R44 |
| B2 | **The "arch dominates primes" brick is dead.** $P$ with no primes is *indefinite*: $\lambda_{\min}(P) = -0.08 \ldots -16.1$ for $L_t = 0.4 \ldots 3.0$. No positive archimedean floor exists. | **Observed** | R49 |
| B3 | **Nonalignment over-delivers.** $\lambda_{\max}(K) \le C_L < A_L$, in fact $\approx \tfrac13$ of the worst-case comb mass. The band-limit genuinely suppresses the prime term. | **Observed** | R49 |
| B4 | **The full form is positive but razor-thin.** $\lambda_{\min}(Q) > 0$, collapsing $\approx 10^{-11} \to 10^{-22}$ with resolution; the PSD band of prime-weight pinches to $[1-1.8\times10^{-13},\, 1+1.8\times10^{-15}]$. A knife-edge, not a margin. | **Observed** | R49 |
| B5 | **Multiplicativity holds the knife-edge.** Every arithmetic mutation (fake impulse at $n=6$, $\lvert\alpha_2\rvert \ne 1$, scaled weights, nudged $\log 2$) drives $\lambda_{\min}(Q)$ clearly negative, $\approx$ linearly. | **Observed** | R49 |

### C — The crossover and the separator (two-sided control)

| # | Result | Status | Source |
|---|---|---|---|
| C1 | **The off-line zero is the negative direction.** Davenport–Heilbronn first goes indefinite at $L^* \approx 4$; the whole negative eigenvalue is its single off-line zero at height $85.699$; moving only it on-line restores positivity. | **Observed** | R49 |
| C2 | **The matched multiplicative partner stays positive.** $L(s,\chi)$ (same conductor, $\Gamma$-factor and FE as D–H, differing only by an Euler product) is PSD across $L = 0.4 \ldots 9$, where its twin cracks. | **Observed** | R51 |
| C3 | $\implies$ **Multiplicativity is the operative separator** (PSD vs indefinite) with everything else matched. Necessary, two-sided (B5 + C2). *Caveat:* $L(s,\chi)$ PSD is itself GRH-equivalent — a separator, not a brick. | **Observed** / **[Inf]** | R51 |

### D — The symbol face (the zero-free vantage)

| # | Result | Status | Source |
|---|---|---|---|
| D1 | On the positive band-limited cone, $\Psi_L$ **is** the sinc-low-passed zero comb; its wells are Gibbs side-lobes. Their non-diggability $=$ positivity of the zero measure $=$ RH; the functional equation buys only evenness. | **[derived]** | R53 |
| D2 | For $\zeta$/real characters the symbol is even and the extremal direction is real; the **complex** near-degeneracy is a *complex-character* feature ($L(s,\chi)$) only. | **[derived]** | R53 |
| D3 | Well depth is a **large-deviation** question, not a Diophantine-gap one; Baker/linear-forms is the wrong tool (phase-forms are logs of rationals; the elementary bound beats Baker). | **[derived]** + cited | R54 |
| D4 | The wells sit in the **Vinogradov–Korobov blind spot** ($\log N \sim \log\log t$); no unconditional exponential-sum tool reaches them — a structural coverage gap, not a weak method. | **[derived]** + cited | R54 |
| D5 | The sharp Carneiro–Chandee–Milinovich extremal-majorant bounds are **RH-conditional** (RH needed for *validity*, not just sharpness). Sharp *unconditional* bounds are the weaker $O(\log T)$ shape. | cited (primary) | R53 |
| D6 | **Well census (symbol gate passes, $M_{\mathrm{sym}} \equiv M_{\mathrm{full}}$ to $10^{-14}$).** Wells are **narrow** (FWHM$\cdot L \approx 2.1$ for all systems) and **deep** (the $t\!\approx\!0$ well tracks $A_L \approx 4e^{L/2}$); the near-null direction $f^*$ digs the best depth/background/resolution-tradeoff wells at **moderate** $t$ ($\sim$17–39), not the deepest. | **Observed** | R58 |
| D7 | **The off-line zero is a *barrier*, not a well.** For Davenport–Heilbronn at $L^*=4.4184$, $\Psi_L(85.699)=+20.72$ (a peak) flanked by wells at $84.5$ and $86.75$; the zero-side split is exact — the **entire** negative eigenvalue is the single off-line quartet ($-0.76986$; the other four $\le 3.7\times10^{-9}$). | **Observed** | R58 |
| D8 | **Shoulder-compensation confirmed.** $\zeta$'s well-part and shoulder-part cancel to $10^{-9}$ (L=7); the flat-well diggability model over-predicts danger by $\sim$20% (predicts $L^*\approx3.1$–$3.7$ vs measured $4.42$); the SOS/Weyl lower bound $\lambda_{\min}(P)-\lambda_{\max}(K)$ is positive only for $L\lesssim3.6$ (band $x_0{=}85.7$), loose beyond by the measured overlap deficit. No reliable $\zeta$ negative (the one negative row was an ill-conditioning artifact, cond $5\times10^{15}$, excluded). | **Observed** / **[derived]** | R58 |

### E — Pending (lands here, then graduates)

| # | Work in flight | Expected landing |
|---|---|---|
| E1 | Well census + eigenvector anatomy + diggability-law calibration (calibrated well instrument). | ✓ **landed R58** → graduated to D6–D8 |
| — | *(no experiment currently in flight)* | — |

## 6.3 The research arc

The program ran as several independent agent lineages that converged on one obstruction.

- **astra** — the CND / infinite-divisibility / transport attack. Finite-event rigidity; the
  geometric-prime Gaussian residual is not a characteristic function; prime-transport martingale
  and complexity-crest controls. (`research/astra_round_001..003/`.)
- **aletheia** — the adelic / affine / place-character structure. The successor/$\bullet$
  affine-braid and KMS structure, the repaired prime tower and adelic radical, the finite reduced
  kernel's strict positive-definiteness (the knife-edge as an asymptotically shrinking window), and
  the **unit-basepoint place-character seam** ([§6.4](#64-the-open-seams)).
  (`research/aletheia_2026-10-05/`, `_2026-10-06/`.)
- **claude** — the operator-algebra / passivity attack. The meta-theorem (commutative-
  multiplicative ⇒ factorized ⇒ RH-inert); exact local operator squares; the self-sieving carry
  machine (von Mangoldt as the carré-du-champ of carry curvature); and Round 006's clean positive
  theorem, the **Schur–Vitali limit** (`C104`): a non-circular reduction of RH to one hypothesis —
  a finite family contractive on all of $H_{1/2}$ and converging to $\mathrm{Cayley}[\xi'/\xi]$
  only on the safe Euler region $\mathrm{Re}\, s > 1$ forces RH.
  (`research/claude_round_004..006/`.)

The current session added the ground-up successor frame, the archimedean $\Gamma$-from-succ
construction, the Diophantine reframe, the finite-window semigroup of
[page 3](03-the-diophantine-semigroup-frame.md), the calibrated coupled-form measurements of
[§6.2](#62-the-results-board), the matched-partner positive control, and the **symbol / well-
geometry** vantage of [page 4](04-the-symbol-and-the-wells.md) — including the identification of
the wells as the low-passed zero comb and the mapping of *why* no unconditional tool reaches them.

## 6.4 The open seams

Two concrete, still-unproven candidate architectures for the one missing theorem. Neither is known
to work; both are RH-hard and are kept precisely because they are *not* obviously circular.

- **The joint coercivity ([§6.1](#61-the-target-named-precisely)).** Prove $P - K \succeq 0$
  unconditionally, using the semigroup's positive SOS energy and a boundary-flux bound against the
  measured-indefinite $P$. The matched partner $L(s,\chi)$ (C2) isolates multiplicativity as the
  operative separator — but that only *names* the open lever; it does not supply an unconditional
  margin, because $L(s,\chi)$'s own positivity is GRH-equivalent. The theorem still owed is a reason
  $P - K \succeq 0$ that reads multiplicativity and does **not** read the zeros.

- **The unit-basepoint place-coupling (UBRPCT, Round 006).** The critical half-density weight
  $p^{-k/2}\log p$ is the *first jet* at $z = 0$ of the $\tfrac12$-twisted adelic character
  $\chi^{(1/2)}_{v,z}(x) = \lvert x\rvert_v^{1/2+z}$; the product formula
  $\prod_v \lvert x\rvert_v^{1/2} = 1$ makes the half-density globally balanced (the adelic "why
  $\tfrac12$"); the cross-prime coupling that primewise-independent constructions discard lives in
  the *second jets*. The seam is to build the global object at the unit basepoint so the divergent
  first-jet corrections cancel **by the product-formula identity before** positivity is formed,
  yielding a second-jet Gram with kernel $K_\Psi$. **Proposed architecture, UNVERIFIED**; orthogonal
  to the single-space de Branges positivity that Conrey–Li/Sarnak proved fails for $\zeta$. Full
  statement and honest gap: `research/aletheia_2026-10-05/CURRENT_MISSING_THEOREM.md`,
  `PLACE_CHARACTER_UNIT_BASEPOINT.md`, `CND_PROOF_SEAM.md`,
  `research/claude_round_006/PROOF_ATTEMPT_006.md`.

## 6.5 The discriminator (what would count as progress)

> A result is real RH progress **iff** it *proves* a statement that was previously only
> conjectured, that statement does **not** reduce to an RH-equivalent, and its proof does **not**
> assume zero locations or Weil positivity. Any result with a load-bearing "if … then RH" is a
> relocated wall.

**Score to date: zero constructions pass.** The honest state is a precisely-shaped target, mapped
from six sides, and a well-mapped graveyard — not a theorem.

---

**Next:** [Methodology & discipline →](07-methodology-and-discipline.md) — how claims are graded,
how constructions are stress-tested, and what "calibrated instrument" means.
