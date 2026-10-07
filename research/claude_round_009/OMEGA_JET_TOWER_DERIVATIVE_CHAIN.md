# The ω-jet tower is the chain of derivatives; the first jet is the velocity of the inner curve

**Round 009 / Pillar 1. Branch `claude/arithmetic-curvature-loops-008` (continuing on the Suzuki
finite-conductor frontier).** **RH IS OPEN.** **Reproduce:** `scripts/r009_jet_tower.py` (all checks
pass; no zeta zeros used as input).

The externally-supplied intuition was: *"how strongly the first actualization affects the state — this
feels like polynomial approximation and chains of first/second/third-order derivatives."* That is
**exactly** the `ω`-jet of Suzuki's inner family. This is standard structure (Suzuki 2012; the jet
stratification is aletheia `OMEGA_ZERO_CONDUCTOR_JET.md`); the contribution here is only the
**differential-geometric reading** — the jet is the Taylor expansion of a *curve* off a flat base
point, and the first jet is its *velocity*.

## 1. The curve and its base point

Suzuki's inner function `Θ_ω(z)=ξ(½−ω−iz)/ξ(½+ω−iz)`, in the causal/Laplace variable, is the
scattering ratio

$$B_\omega(s)=\frac{\xi(s+\tfrac12-\omega)}{\xi(s+\tfrac12+\omega)},\qquad B_0(s)\equiv 1.$$

So `ω` is a deformation parameter and `B_0=1` is a **flat base point** (the identity scattering).
"Actualization" is turning `ω` on; the question "how strongly does the first actualization affect the
state" is the question of the **first derivative** `dB_\omega/d\omega|_0`.

## 2. The velocity is the Weil generator (verified)

$$\boxed{\ \frac{d}{d\omega}B_\omega(s)\Big|_{0}=-2\,\frac{\xi'}{\xi}\!\left(s+\tfrac12\right)\ }$$

verified to machine precision (`|diff| ≲ 10^{-15}` at `s=1.5, 2+i, 1.2+0.8i`). This is the **velocity
vector** of the inner curve at the flat base point — and it is exactly the **Weil/Lagarias** object (the
inner-function / de Branges–space machinery under `Θ_ω, B_ω` is de Branges 1968 / Krein; see Pillar 2).
The honest, sign-correct positivity statement: RH `⟺` `−Ξ'/Ξ` is **Herglotz** (`Im>0` in the upper
half-plane) — equivalently `+ξ'/ξ(s+½)`, i.e. `−½` times this velocity, is a positive-real function on
`Re s>0`. (`−2 ξ'/ξ(s+½)` itself has *negative* real part in the right half-plane, so it is not itself
positive-real; the positive object is its `−½` multiple.) **Conrey–Li (2000) refuted** the naive de
Branges positivity program built on such criteria, so this equivalence is *not* a proof route.
So "the first actualization" = the first jet = the Weil tangent. On the Dirichlet side, the arithmetic
coefficients expose the same velocity as von Mangoldt:

$$A_\omega(s)=\sum_n \frac{b_\omega(n)}{n^s}=\frac{\zeta(s+\tfrac12-\omega)}{\zeta(s+\tfrac12+\omega)},
\qquad A_0'(s)=-2\frac{\zeta'}{\zeta}\!\left(s+\tfrac12\right)=2\sum_n\frac{\Lambda(n)}{n^{\,s+1/2}}$$

(verified at `s=2`: `A_0'(2)=0.57748…` vs the truncated von Mangoldt sum `0.57748…`).

## 3. The chain of derivatives = the `ν(n)` filtration

The conductor coefficient `b_ω(n)=n^{ω−1/2}∏_{p|n}(1−p^{−2ω})` has a jet **stratified by the number of
distinct primes** `ν(n)` (verified symbolically; this is aletheia `OMEGA_ZERO`):

$$b_0^{(j)}(n)=0\ \ (0\le j<\nu(n)),\qquad
b_0^{(\nu)}(n)=\nu!\,2^{\nu}\,\frac{\prod_{p\mid n}\log p}{\sqrt n},\qquad
b_0'(n)=\frac{2\Lambda(n)}{\sqrt n}.$$

So the Taylor **order in `ω` literally is the number of distinct primes**:

| order | layer | members ≤ 60 |
|------:|-------|--------------|
| `O(ω^0)` | flat base `n=1` | `1` |
| `O(ω^1)` | prime powers (Weil / von Mangoldt) | `2,3,4,5,7,8,9,11,13,16,…` |
| `O(ω^2)` | two-prime conductors | `6,10,12,14,15,18,…` |
| `O(ω^3)` | three-prime conductors | `30,42,60,…` |

This is the user's "polynomial approximation / chain of 1st/2nd/3rd-order derivatives" made exact: the
**first domino** is the prime-power/von-Mangoldt layer (order 1), and each higher order switches on the
integers that need that many prime interactions.

## 4. GR reading (framing, not theorem)

`B_ω` is a **curve in the space of scattering functions** starting at the flat identity `B_0=1`. Its
**velocity** is the Weil generator `−2ξ'/ξ(s+½)`; its higher jets (`ν≥2`, the two- and three-prime
conductors) are the **acceleration / curvature** terms. Pillar 2 integrates this velocity into the
canonical system, **read as a geodesic flow**, and asks what the `ω→0⁺` / `a→∞` limit — the user's
"actualization to infinity" — does to the accumulated curvature. Here we have only fixed the *initial
tangent*: the first actualization is the Weil tangent, and that is the object whose positivity is RH
(open).

## 5. Ledger

- **C108 (RH-inert, standard; new framing).** The user's "chain of 1st/2nd/3rd-order derivatives" = the
  `ω`-jet of Suzuki's inner curve `B_ω(s)=ξ(s+½−ω)/ξ(s+½+ω)` off the flat base `B_0=1`. Verified:
  velocity `dB/dω|_0 = −2(ξ'/ξ)(s+½)` (machine precision) = the Weil/Lagarias generator; Dirichlet
  `A_0'(s)=2∑Λ(n)/n^{s+½}`; jet stratified by `ν(n)` (`b_0^{(j)}=0` for `j<ν`, `b_0^{(ν)}=ν!2^ν∏log p/√n`,
  `b_0'=2Λ/√n`). Order-in-`ω` = #distinct primes; first jet = prime-power/von-Mangoldt (Weil) layer.
  Credit Suzuki 2012 (RIMS B34); aletheia OMEGA_ZERO_CONDUCTOR_JET.md. `scripts/r009_jet_tower.py`.
  No RH progress; the velocity's positivity is RH, open.

RH remains open.
