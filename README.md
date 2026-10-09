# FuckingRH

A proof-first research program attacking the **Riemann Hypothesis** through one concrete,
RH-equivalent positivity target, pursued across several independent agent lineages (astra,
aletheia, claude) and consolidated here on `main`.

**Status: RH remains open.** Nothing in this repository claims otherwise. The repository is
organized to keep honest the distinction between what is *proved*, *computed*, *conjectured*,
and *refuted*, and to name — precisely — the single load-bearing theorem a genuine proof
still owes.

---

## Read the framing from the ground up

The full account of how this program thinks about the problem lives in the
**[wiki](wiki/README.md)**, written to be read in order:

1. **[The successor frame](wiki/01-the-successor-frame.md)** — the generative idea from first
   principles: successor ($\mathrm{SUCC}$), multiplication as rescaling the successor step (the
   $\bullet$ operator), prime powers as ray–worldline intersections, the finite vs. archimedean
   places, and the archimedean $\Gamma$-factor built from the frame with no zeta.
2. **[The RH-equivalent target](wiki/02-the-rh-equivalent-target.md)** — the completed zeta,
   Weil's explicit formula, Weil positivity $\iff$ RH, the Suzuki / $\xi'/\xi$ / passivity / de
   Branges reformulations, the free half above $\mathrm{Re}\, s = 1$, and the prime-free
   positivity window.
3. **[The Diophantine & semigroup frame](wiki/03-the-diophantine-semigroup-frame.md)** — why
   the prime frequencies $\{\log p\}$ are the real content, phase alignment and the negative
   "wells," the band-limit, and the finite-window multiplicative semigroup with its
   nonalignment theorem.
4. **[The symbol face and the wells](wiki/04-the-symbol-and-the-wells.md)** — the band-limited
   Weil symbol as an explicit, zero-free function; the exact sense in which it *is* the
   low-passed zero comb; diggability of the wells; the Davenport–Heilbronn crossover and the
   matched multiplicative partner; and why no unconditional tool reaches the well regime.
5. **[What ζ is, from every side](wiki/05-what-is-zeta-here.md)** — the same object read through
   all six lenses at once, the dictionary between their "missing theorems," and why they are one
   object and one wall.
6. **[State of the program](wiki/06-state-of-the-program.md)** — the living results board: what
   the calibrated instrument measured (dead brick, nonalignment, razor-thin balance held by
   multiplicativity), the Davenport–Heilbronn crossover and matched partner, the symbol-face
   map, the research arc, and the open seams.
7. **[Methodology & discipline](wiki/07-methodology-and-discipline.md)** — the crucifixion
   method, epistemic labels, hostile controls, the no-zero-input rule, and calibrated
   instruments.
8. **[The reformulations catalog](wiki/08-the-reformulations-catalog.md)** — a map of all ~47
   experimental branches: every lens tried, each as "RH looks like this if you consider X → what
   you get → the wall," with the provenance caveat and the verdict (zero genuine non-circular
   content; every per-prime positivity is RH-inert).

---

## The target, in one screen

Weil's explicit formula makes the zeros and the primes two sides of one identity. Applied to
a self-correlation it yields the **Weil functional**
$W(g) = \sum_\rho \hat g(\gamma_\rho)\,\overline{\hat g(\overline{\gamma_\rho})}$ (the reflected
autocorrelation; $= \sum_\rho \lvert \hat g(\gamma_\rho)\rvert^2$ exactly when every $\gamma_\rho$ is
real), and

$$W(g) \ge 0 \ \text{for all admissible } g \iff \mathrm{RH}.$$

So RH is exactly the statement that the **prime-plus-archimedean** (arithmetic) side of the
formula is non-negative — and the program's job is an *independent, non-circular* reason for
that positivity, one that never reads the zeros. Equivalent repackagings used here (all exact,
none a proof): Suzuki $\Psi(t) \ge 0\ \forall t$; the screw kernel $K_\Psi \succeq 0$; and
$\xi'/\xi$ positive-real on $\mathrm{Re}\, s > \tfrac12$. (The companion coordinate
$\mathrm{Re}\{\xi(s)/\xi(s+1)\} \ge 0$ is *not* an equivalence — a de Branges–type sufficient
condition that is itself false in the strip; see wiki/02.) Full detail:
[wiki/02](wiki/02-the-rh-equivalent-target.md).

The free part is sharp: positivity for $\mathrm{Re}\, s > 1$ is unconditional (the Euler
product), and Connes–Consani (**Theorem 1**, arXiv:2006.13771) give it unconditionally for test
functions supported in the prime-free window $(\tfrac12, 2)$. All RH content is pushing
positivity from there down to $\mathrm{Re}\, s > \tfrac12$.

---

## Where the program stands (the one wall)

On the finite-window test space the completed Weil form splits as $Q = P - K$ — archimedean
+ pole part $P$, prime semigroup $K$ — and the missing theorem is the **joint coercivity
$Q = P - K \succeq 0$**. A calibrated instrument (explicit formula balanced to 60 digits,
$M_{\mathrm{full}} \equiv M_{\mathrm{zeros}}$) measured each piece:

- **The "archimedean floor" does not exist.** $P$ alone, with no primes, is *indefinite* at
  every support ($\lambda_{\min}(P)$ from $-0.08$ to $-16.1$). The clean inequality
  $\text{arch} + \text{pole} \ge \lVert K\rVert$ that would be an unconditional proof **fails
  wide** — positivity is a cancellation, never a floor.
- **The band-limit is a theorem.** The prime term's norm obeys $\lambda_{\max}(K) \le C_L < A_L$
  ($\approx \tfrac13$ of the worst-case comb mass) — a real, unconditional buy-back of positivity.
- **The balance is razor-thin and held by multiplicativity.** $\lambda_{\min}(Q)$ is positive but
  collapses toward $0$ with resolution; the PSD window of the prime weight pinches to
  $[1-1.8\times10^{-13},\, 1+1.8\times10^{-15}]$; and **every** mutation of the arithmetic (fake
  impulse at $n=6$, $\lvert\alpha_2\rvert \ne 1$, scaled weights, shifted $\log 2$) drives it
  negative. Multiplicativity holds the sign — *at zero*. A knife-edge poised at zero **is**
  RH-equivalence.
- **The off-line zero is the negative direction, and multiplicativity is the separator.** On
  the non-multiplicative control Davenport–Heilbronn, the form first goes indefinite at support
  $L^* \approx 4$, and the entire negative eigenvalue is its off-line zero at height $85.699$;
  move only that zero on-line and the form is positive again. The matched multiplicative partner
  $L(s,\chi)$ — same conductor, $\Gamma$-factor, and functional-equation shape, differing *only*
  by carrying an Euler product — stays positive across the whole range where the twin cracks. One
  variable toggled, opposite outcome: positivity's sign tracks zero-location exactly, and
  multiplicativity is the thing that holds it. (That partner's positivity is itself
  GRH-equivalent — this measures the separator, not a brick.)

Every feature the frame predicted is true and measured — and all of it is RH-equivalent.
There is **no unconditional brick**. Full numbers, the research arc, and the two open seams
(the joint coercivity, and the Round-006 unit-basepoint place-coupling / UBRPCT): [wiki/06](wiki/06-state-of-the-program.md).

---

## Start here

1. **[wiki/README.md](wiki/README.md)** — the ground-up framing (read in order).
2. **[CRUCIFIXION_LEDGER.md](CRUCIFIXION_LEDGER.md)** — the live, round-by-round narrative map
   (currently through Round 066).
3. **[CLAIM_LEDGER.md](CLAIM_LEDGER.md)** — every claim with status (Rows C01–C111). The spine
   of the repo.
4. **[CONSOLIDATED_RH_STATE.md](CONSOLIDATED_RH_STATE.md)** — cross-repo consolidation, graded
   by epistemic status; `§8` is the current-session summary.
5. **[docs/NEGATIVE_CONTROLS.md](docs/NEGATIVE_CONTROLS.md)** — attractive dead ends already
   failed (do not re-walk).

---

## Discipline (non-negotiable)

- **RH is open.** No file asserts otherwise without a complete proof that survives hostile
  audit.
- Every claim lands in a ledger with an explicit status (Verified / Demonstrated / Observed /
  Conjectured / UNVERIFIED / Refuted) and a reproduction pointer. Labels never silently
  upgrade; numerics never become proofs by accumulation.
- Every candidate faces **hostile controls** (delete/insert a prime, wrong $\log p$, wrong
  half-density $p^{-1/2}$, perturb the archimedean boundary, fake arithmetic). A construction
  that survives fake arithmetic is RH-inert.
- **No zeta-zero ordinates are ever used as construction input** — only as after-the-fact
  diagnostics.
- Numerical code is a **calibrated instrument**: it must recover a known answer before its
  novel readings count, and load-bearing values are cross-checked by a second implementation.
- Scripts under `scripts/` reproduce the exact identities and the measured no-gos (`numpy`,
  `mpmath`, `sympy`, `scipy`; see `requirements.txt`).

---

## One-paragraph conceptual summary

Primality, von Mangoldt, $\zeta'/\zeta$, and the completion to $\xi'/\xi$ arise cleanly from an
arithmetic *process*: $\mathrm{SUCC}$ boots the additive worldline, $\bullet$ rescales the
successor step into multiplication, prewired prime rays
$\lvert 1\rangle \to \lvert p\rangle \to \lvert p^2\rangle \to \cdots$ meet that worldline
exactly at prime powers, and the archimedean place completes the picture with a self-dual
Gaussian atom whose scaling-Mellin transform is $\Gamma_{\mathbb{R}}$. RH is the positivity of
the completed Weil form built from this data. The local pieces are exactly positive and the
finite-window multiplicative semigroup supplies a genuine, unconditional buy-back of positivity
($C_L < A_L$) — but the archimedean part is itself indefinite, the surviving balance is
razor-thin and held exactly at the arithmetically-correct point, and that balance is provably
RH-equivalent. The one thing missing — and the thing every lineage here has independently
cornered — is the **exact global coercivity that couples the finite prime places to the
archimedean place and stays positive**. It has a precise name and measured pieces; it does not
yet have a proof.
