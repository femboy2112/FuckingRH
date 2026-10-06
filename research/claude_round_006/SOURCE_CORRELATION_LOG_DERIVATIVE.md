# Source correlation = -zeta'/zeta, and the category it lives in (ckpt4)

**Date:** 2026-10-06. **Status:** DISCLOSED (exact for Re s>1). **RH open.**
**Reproduce:** `scripts/source_port_core.py` (checks IV–V).

## The source-emission operator

For `sigma>1`, define the rank-(into-ray) emission operator

    J_sigma = sum_{p,k} sqrt(log p)\, p^{-k sigma/2}\, |p,k><Omega|,   Omega=|1>.

It is bounded for `sigma>1` (`||J_sigma||^2 = sum log p\, p^{-k sigma} = -zeta'/zeta(sigma) < infty`).

## Theorem 4 (static source load)

    J_sigma^* J_sigma = (-zeta'/zeta(sigma)) |Omega><Omega|,   sigma>1.   (6)

*Proof.* `J_sigma^*J_sigma = (sum_{p,k}|c_{p,k}|^2)|Omega><Omega|` with `c_{p,k}=sqrt(log p)p^{-k sigma/2}`
(rays orthonormal), and `sum_{p,k>=1} log p\, p^{-k sigma} = sum_p (log p) p^{-sigma}/(1-p^{-sigma})
= sum_p log p/(p^sigma-1) = sum_n Lambda(n) n^{-sigma} = -zeta'/zeta(sigma)`. ∎

## Theorem 5 (the first pulse turns on the t-action)

With the log-energy evolution `U_t = e^{itH}` (`U_t|p,k>=p^{itk}|p,k>`),

    J_sigma^* U_t J_sigma = (-zeta'/zeta(sigma - it)) |Omega><Omega|.     (7)

*Proof.* `J_sigma^* U_t J_sigma = (sum_{p,k}|c_{p,k}|^2 p^{itk})|Omega><Omega|`, and
`sum log p\, p^{-k sigma} p^{itk} = sum log p\, p^{-k(sigma-it)} = -zeta'/zeta(sigma-it)`. ∎

**This is the exact form of "SUCC boots the source; the first pulse starts the clock."** The `t`-action is
literally the log-energy flow on the prewired rays; its `Omega`-autocorrelation is the Euler logarithmic
derivative. Verified numerically (N=400): at `(sigma,t)=(3,5)` err `1.2e-6`; larger errors at
`(1.5,2)` are the prime-cutoff tail, shrinking with N.

## The category (directive §13) — this is a CORRELATION, not a Weyl function

`(6)-(7)` are **matrix elements** `<Omega| (dressed flow) |Omega>` — an autocorrelation of the emitted
state along the flow. Precisely:

    -zeta'/zeta(sigma - it) = sum_n a_n e^{i t log n},   a_n = Lambda(n) n^{-sigma} >= 0.   (8)

So for each fixed `sigma>1`, as a function of `t`, `-zeta'/zeta(sigma-it)` is **positive-definite**
(Bochner): the Fourier transform of the nonnegative discrete measure `sum_n a_n delta_{log n}`.

**But positive-definite-in-`t` is NOT positive-real-in-`s`.** Concretely the numerics show
`Re(-zeta'/zeta) < 0` at several points with `Re s>1`: `(2,1.3)->-0.018`, `(1.5,2)->-0.282`,
`(3,5)->-0.051`. A positive-definite function of `t` can have negative real part; a *positive-real*
(Herglotz) function on the half-plane cannot. The two positivities are different theorems about different
objects:

| object | positivity it has | positivity RH needs |
|---|---|---|
| `-zeta'/zeta(sigma-it)`, `sigma` fixed | positive-DEFINITE in `t` (Bochner), always | — |
| `xi'/xi(s)` on `Re s>1/2` | positive-REAL (Herglotz) ⟺ **RH** | this one |

**Why this matters.** The temptation is to parlay the free Bochner positivity of the correlation into a
half-plane positivity. It does not transfer: a rank-1 autocorrelation `<Omega|U_t^{dressed}|Omega>` is an
ordinary (scalar) correlation function, **not** a driving-point impedance / Weyl `m`-function of a passive
system. To get a positive-real object we need a genuinely different construction — a coupled colligation
whose transfer/`m`-function is `xi'/xi` — and the completion by the Archimedean boundary. That is ckpts
5–11. The classification of what object each scalar is (matrix element vs trace vs Schur complement vs
`m`-function) is tracked explicitly so no positivity theorem is applied to the wrong category.

## What is exact and what is open

- EXACT (Re s>1): `-zeta'/zeta = sum_p m_p`, `m_p(s)=log p/(p^s-1)`, as the `Omega`-correlation of the
  log-energy flow on prewired rays.
- OPEN: realize the **completed** `xi'/xi` as a **positive-real / passive** object (not merely a
  positive-definite correlation) on `Re s>1/2`. RH remains open.
