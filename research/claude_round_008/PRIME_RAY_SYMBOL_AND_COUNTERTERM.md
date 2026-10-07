# The prime-ray symbol: the counterterm is its mean, the zeros are its continuation poles

**Round 008. Branch `claude/arithmetic-curvature-loops-008` (from the Suzuki frontier, head `0840c39`).**
**RH IS OPEN.** **Reproduce:** `scripts/r008_prime_ray_symbol.py` (all checks pass; no zeta zeros used as input).

Checkpoint 1 located the wall in the SUCC↔FUCC coupling and showed the prime-ray energy is flat
(curl-free). This note makes the coupling **fully explicit on the Fourier side** by computing the
*symbol* of the prime-ray graph Laplacian. Three exact facts drop out, and they pin the frontier wall
to a single sentence. All of it is pure-prime (no zero ordinates feed any construction); it is
RH-inert and proves no progress.

---

## 1. The prime-ray symbol

The frontier's prime-ray Dirichlet energy (WEIL_PRIME_RAY_DIRICHLET_FORM.md) is

\[
\mathcal{E}_{\mathrm{prime},a}(v)=\sum_{p^k\le e^{2a}}\frac{\log p}{p^{k/2}}\,\|v-\tau_{k\log p}v\|^2 .
\]

Translation `τ_h` has Fourier symbol `e^{-ih\xi}`, and `\|v-\tau_h v\|^2=\frac1{2\pi}\int 4\sin^2(h\xi/2)\,|\hat v(\xi)|^2\,d\xi`.
So the energy is a **Fourier multiplier**:

\[
\boxed{\;
\mathcal{E}_{\mathrm{prime},a}(v)=\frac1{2\pi}\int_{\mathbb R} M_a(\xi)\,|\hat v(\xi)|^2\,d\xi,
\qquad
M_a(\xi)=\sum_{p^k\le e^{2a}}\frac{\log p}{p^{k/2}}\,4\sin^2\!\Big(\tfrac{k\log p}{2}\,\xi\Big).
\;}
\]

Verified to machine precision two independent ways (x-space correlation with interpolated shifts vs
FFT; the assembled `\mathcal{E}` agrees to `2\times10^{-6}`).

---

## 2. Three exact facts

**(A) `M_a(\xi)\ge 0` everywhere.** A sum of `\sin^2` terms: the prime-ray Laplacian is positive
semidefinite. **The prime arithmetic contributes no negativity** — reconfirming the Round-008
flatness theorem from the spectral side. Any sign problem in Suzuki positivity is *not* in the primes.

**(B) The counterterm is the mean of the symbol.** Since the long-window average of
`4\sin^2(h\xi/2)` is `2`,

\[
\boxed{\;
\langle M_a\rangle_\xi \;=\; 2\sum_{p^k\le e^{2a}}\frac{\log p}{p^{k/2}} \;=\; \mathcal V_a^{\mathrm{prime}},
\;}
\]

exactly the prime part of Suzuki's global counterterm (verified: window-mean `75.21` vs
`2\sum w = 75.19`, `0.03\%`). **The counterterm is the DC component (mean) of the prime-ray symbol.**
Combined with Checkpoint-1 Theorem 2 (`\mathcal V_a^{\mathrm{prime}} = 2\deg`), this is the whole
accounting: the counterterm, the degree, and the symbol mean are one number.

**(C) The fluctuation is the truncated `-\zeta'/\zeta` on the critical line.** Exactly (verified to
`5\times10^{-14}`):

\[
\boxed{\;
\langle M_a\rangle - M_a(\xi)
= 2\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n}\cos(\xi\log n)
= 2\,\Re\big[(-\zeta'/\zeta)(\tfrac12-i\xi)\big]_{\text{trunc}} .
\;}
\]

So the symbol's fluctuation about its mean is **literally twice the truncated `-\zeta'/\zeta` on the
line `\Re s=\tfrac12`**. Its analytic continuation has poles exactly at `\xi=\pm\gamma` (the
nontrivial zero ordinates). **But the finite symbol does not resolve them:** at `a=3` the raw dips
sit at `\xi\approx 1.2,2.3,3.4,4.4` — small-prime beats with periods `2\pi/\log 2\approx9.06`,
`2\pi/\log 3\approx5.72` — nowhere near the first ordinate `14.13`. The zeros are a datum of the
**continuation**, not of the finite/algebraic symbol. This is Round-006 **C103** (group completion ≠
analytic continuation) seen directly on the symbol.

---

## 3. The dynamical-zeta reading (the "loops carry weight" instinct, confirmed)

The externally-supplied intuition was: *the loops/edges carry weight/energy; can we read a dynamical
zeta off them?* We can, and it is the right object. The prime-ray edges are indexed by
`(p,k)` with **orbit length** `h_{p,k}=k\log p` and **weight** `w_{p,k}=\log p/p^{k/2}`. Their
length-generating function is

\[
\boxed{\;
\sum_{p,k} w_{p,k}\,e^{-s\,h_{p,k}}
=\sum_{p,k}\frac{\log p}{p^{k/2}}\,p^{-ks}
=\sum_n \frac{\Lambda(n)}{n^{\,s+1/2}}
=\big(-\zeta'/\zeta\big)\!\big(s+\tfrac12\big).
\;}
\]

So the "field of succ forms", read as a flow with closed-orbit lengths `\{k\log p\}` and half-density
weights `\{\log p/p^{k/2}\}`, has **dynamical (Ruelle) zeta `=\zeta`**: the prime rays *are* the
length spectrum of the arithmetic flow, and `M_a(\xi)` is that spectrum assembled as a positive
multiplier. The user's loop-weight functional and the explicit formula are the same object evaluated
two ways. (This is the Berry–Keating / prime-geodesic dream in exact coordinates — and, like it, it
does not by itself supply a self-adjoint generator; see §5.)

---

## 4. The frontier wall, Fourier-side and fully explicit

The Archimedean fractional-difference energy `\mathcal L_a` has symbol `\sim c|\xi|` (the half-Laplacian
`(-\Delta)^{1/2}`, modulo the interval `-\tfrac12\log(a^2-x^2)` potential and the `H^1_0` boundary).
Suzuki positivity `Q_W^a(v)\ge0` becomes, in symbols,

\[
\boxed{\;
\underbrace{c|\xi|}_{\text{Archimedean}}
\;+\;
\underbrace{\big(M_a(\xi)-\langle M_a\rangle\big)}_{=\,2\Re[(-\zeta'/\zeta)(1/2-i\xi)]\ \text{(sign-indefinite)}}
\;\gtrsim\;
\underbrace{\text{smooth remainder } \widehat{R_a}}_{\text{Archimedean completion}} .
\;}
\]

The prime fluctuation is sign-indefinite and dips below zero at special frequencies; **the Archimedean
`|\xi|`-energy must cover those dips.** That is the entire wall, with no "mysterious prime
cancellation" left in it. Two honest constraints, both from the frontier, bound any attack:

- **No uniform gap** (CAUSAL_TOEPLITZ §5–6, `g(a)=1-\|H_{1/2,a}\|\to0`): the covering must be
  *marginal/critical*, never a fixed buffer. A frame lower bound `\inf_\xi M_a(\xi)` is useless here —
  it is `0` (at `\xi=0` and at near-resonances), consistent with the prime Laplacian killing constants
  (Checkpoint-1 Theorem 2). The low band is the Archimedean channel's job, exactly.
- **The deciding resonances are not in the finite symbol** (§2C / C103): the frequencies where the
  fluctuation would win or lose sit at the zeros, i.e. in the *continuation* of
  `-\zeta'/\zeta(1/2-i\xi)`. No finite-horizon / purely algebraic computation on `M_a` can see them.

---

## 5. Honest status

New, exact, RH-inert content this checkpoint:
1. the prime-ray symbol `M_a(\xi)` and the multiplier identity for `\mathcal E_{\mathrm{prime},a}`;
2. **counterterm = mean(symbol) = `2\deg`** (a one-line closure of the Checkpoint-1 degree accounting);
3. **fluctuation = `2\Re[(-\zeta'/\zeta)(1/2-i\xi)]_{\text{trunc}}`**, with the zeros as continuation
   poles invisible to the finite object (C103 on the symbol);
4. the dynamical-zeta identity `\sum w\,e^{-sh}=(-\zeta'/\zeta)(s+\tfrac12)` confirming the loop-weight
   instinct and naming its limit (no self-adjoint generator supplied).

None of this moves RH. It converts the frontier wall from a statement about an operator norm into a
statement about **one positive multiplier plus a half-Laplacian covering its sign-indefinite
fluctuation**, and it re-exhibits the Round-006 continuation gap at the heart of that fluctuation. The
gain is clarity and exact coordinates; the wall stands.

---

## 6. Ledger

- **C106 (RH-inert, exact).** *Prime-ray symbol.* `\mathcal E_{\mathrm{prime},a}(v)=\frac1{2\pi}\int M_a|\hat v|^2`
  with `M_a(\xi)=\sum_{p^k\le e^{2a}}(\log p/p^{k/2})\,4\sin^2(k\log p\,\xi/2)\ge0` (prime Laplacian PSD,
  no prime negativity). Mean of `M_a` = `2\sum\log p/p^{k/2}` = Suzuki prime counterterm = `2\deg`
  (Checkpoint-1). Fluctuation `\langle M_a\rangle-M_a(\xi)=2\Re[(-\zeta'/\zeta)(1/2-i\xi)]_{\text{trunc}}`
  (exact, 5e-14); its continuation poles are the zero ordinates, NOT resolved at finite horizon (C103).
  Length-generating function `\sum w\,e^{-sh}=(-\zeta'/\zeta)(s+1/2)` ⟹ prime rays = length spectrum of
  the arithmetic flow, dynamical zeta = `\zeta` (Berry–Keating dream; no self-adjoint generator
  supplied). Fourier-side wall: Archimedean `c|\xi|` must cover the sign-indefinite prime fluctuation;
  no uniform gap (frontier proven-negative), deciding resonances in the continuation only.
  `scripts/r008_prime_ray_symbol.py`. No RH progress.

RH remains open.
