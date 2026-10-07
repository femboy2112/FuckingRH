# Round 008 — arithmetic interaction curvature: succ-loops land exactly on the frontier wall

**Branch** `claude/arithmetic-curvature-loops-008` (from the Suzuki finite-conductor frontier
`aletheia/finite-hankel-contraction-frontier-2026-10-07`, head `0840c39`). **RH IS OPEN.**
**Outcome (2):** an externally-supplied loop/curvature intuition re-derives the finite-conductor
geometry from the ground up and pins the live wall to one sentence — in *exact, new coordinates* —
but supplies none of the missing analytic positivity. The wall is sharpened and re-expressed, not
breached.

## What was asked
Treat the SUCC/FUCC moves as a category of arithmetic phase-changes whose graph closes into loops;
ask whether the loops carry weight/energy (an "arithmetic interaction curvature"); build ℕ from
factorial/primorial atoms; and characterize the finite loop-families a finite value-set can support.

## What was established (all verified, no zeta zeros as input)

**1. Loops are relations; the curvature is `[SUCC,FUCC]` and nothing else** (C105,
`r008_loop_curvature.py`). A closed succ-loop is an identity word (the Collatz loop `3→13→5→3`
composes to `x` exactly, primes `{2,3}` balanced). **Prime-ray flatness (Theorem 1):** every
pure-FUCC loop has zero net log-displacement and trivial holonomy — this is *exactly* UFD
(`{\log p}` ℤ-independent) — so the frontier's prime-ray Dirichlet energy is **curl-free**. The only
curvature generator is the braid `[T,D_p]=p-1`. **Location (Theorem 2):** Suzuki's prime counterterm
`= 2\sum\log p/p^{k/2} = 2\deg`, and the prime-ray Laplacian kills constants, so the counterterm
*cannot* be dominated by the prime-ray energy alone — the Archimedean coupling is mandatory. Hence
**Suzuki positivity `Q_W^a\ge0` is a nonnegativity of the cross (curvature) energy, not of the flat
prime arithmetic** — reproducing the frontier's own `DISCRETE_CONDUCTOR §13` verdict from the loop side.

**2. The prime-ray symbol: counterterm = its mean, zeros = its continuation poles** (C106,
`r008_prime_ray_symbol.py`). `\mathcal E_{\mathrm{prime},a}(v)=\frac1{2\pi}\int M_a|\hat v|^2`,
`M_a(\xi)=\sum_{p^k\le e^{2a}}(\log p/p^{k/2})\,4\sin^2(k\log p\,\xi/2)\ge0` (prime Laplacian PSD — no
prime negativity). Exactly: **`\langle M_a\rangle = ` Suzuki prime counterterm `= 2\deg`** (0.03%), and
**`\langle M_a\rangle - M_a(\xi) = 2\Re[(-\zeta'/\zeta)(1/2-i\xi)]_{\text{trunc}}`** (5e-14). The
loop-weight generating function `\sum w\,e^{-sh}=(-\zeta'/\zeta)(s+1/2)` confirms the dynamical-zeta
instinct: the prime rays are the length spectrum of the arithmetic flow, dynamical zeta `=\zeta`
(Berry–Keating — no self-adjoint generator supplied). The deciding resonances sit at the zeros, in
the **continuation** of the symbol, invisible to any finite horizon — Round-006 **C103** on the symbol.

**3. Factorial/primorial atoms = the odometer = the BC/frontier clock; loop-family support = the
conductor** (C107, `r008_primorial_odometer.py`). SUCC = the primorial odometer; its carry depth =
primorial divisibility = the braid. The prime-power (LCM) odometer is `+1` on `\hat{\mathbb Z}` = the
Bost–Connes phase space = the frontier's conductor clock (C100/C103: at the Weil wall; not new). The
user's "finite value-set supporting a finite loop-family `F`" = the finite-conductor truncation
`\{n\le e^{2a}\}`, `|F|=\#\{p^k\le e^{2a}\}` (= the symbol's edge counts); "sweep over families" =
horizon `a\uparrow`. Shadow: `1` = source `|1\rangle` (deleted-0 boundary `E_S`), `2=1+1` = the
minimal braid-curvature cell `p-1=1`.

## The wall, in the new coordinates (fully explicit)

\[
\underbrace{c|\xi|}_{\text{Archimedean }(-\Delta)^{1/2}}
\;+\;
\underbrace{\big(M_a(\xi)-\langle M_a\rangle\big)}_{=\,2\Re[(-\zeta'/\zeta)(1/2-i\xi)]\ \text{sign-indefinite}}
\;\gtrsim\;
\underbrace{\widehat{R_a}}_{\text{Archimedean completion}} .
\]

The prime side is flat and PSD; its mean is the counterterm; its fluctuation is the truncated
`-\zeta'/\zeta`. **RH = the Archimedean `|\xi|`-energy covering that sign-indefinite fluctuation**,
marginally (no uniform gap: frontier proven-negative `g(a)=1-\|H_{1/2,a}\|\to0`), with the deciding
resonances living only in the analytic continuation (C103). No new positivity is produced; the
coordinates are new, the obstruction is the same Weil/Connes gap.

## Honest status and the direction this constrains

Round 008 is a **clean negative with a sharp gain in coordinates.** The loop/curvature intuition was
worth pursuing — it independently rebuilt the finite-conductor geometry and named the wall as a
curvature statement — but it is *flat where it is computable* (the primes) and *continuation-bound
where it decides* (the zeros). This tightens the Round-006/007 direction constraint once more:

> The prime/loop side is curl-free (UFD) and PSD; all RH content is the **Archimedean coupling**
> covering the prime symbol's fluctuation, whose sign is set by resonances in the **continuation**
> (the zeros). A new structure helps only if it supplies that Archimedean `(-\Delta)^{1/2}`
> covering non-circularly — i.e. constructs the functional-equation / `\Gamma`-factor positivity
> directly — not if it rearranges or re-weights the (flat) primes.

Concretely, the live thread is the frontier's **route 3** (CONDUCTOR_FIRST_JET / WEIL_PRIME_RAY §9):
derive the whole quadratic form by differentiating the exact finite-conductor factorization
`H_{\omega,a}=V^*_{\omega,a}\mathbb G_{\omega,a}V_{\omega,a}` at `\omega=0`, keeping the unit-conductor
(Archimedean) and prime-power channels in **one block** — so the `|\xi|`-covering and the fluctuation
are produced together, never estimated apart. The curvature picture says why: the two must stay
coupled because the counterterm is the degree of the flat prime graph and only the cross term can pay it.

RH remains open.
