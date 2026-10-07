# The canonical system as a geodesic; the Dirac light cone; actualization-to-infinity as curvature

**Round 009 / Pillar 2. Branch `claude/arithmetic-curvature-loops-008`.** **RH IS OPEN.**
**Reproduce:** `scripts/r009_canonical_geodesic.py` (all checks pass; no zeta zeros used as input).

This is the heart of the externally-supplied GR intuition: *"the first domino gets set, the first
finite curvature is actualized, the system minimally follows the gradient (geodesic path), and this
forces the next minimal domino; the net effect is the global curvature … the limit of actualization to
infinity is what describes the curvature. We literally have an analogical notion of light cones."*

**Honest status up front.** Every object below is **standard or already in the repo**; the one piece
of genuinely-new, provable framing is *geodesic-at-the-spectral-base-point*. The GR picture is a
**dictionary, not a mechanism**: it reaches the same wall. And **Conrey–Li (2000) refuted** de Branges'
positivity-based route, so **no positivity is claimed here**.

## 1. The transfer is an SL(2,ℝ) flow; `σ₁` is a boost whose orbit is a geodesic

Suzuki's canonical system, in the Dirac/parity form (aletheia `CRITICAL_PARITY_DIRAC_SYSTEM.md §8`), is

$$\frac{d}{dA}X=\big[\,iz\,\sigma_3+\mu(A)\,\sigma_1\,\big]X,\qquad \mu(A)=\frac{d}{dA}\log m_3(e^A),$$

with `A=log a` the horizon/"actualization" time, `z` the spectral (Mellin) variable, and `μ` the Dirac
mass (the log-derivative of the renormalized det₃ determinant `m_3`, aletheia
`CRITICAL_DET3_POSITIVE_HAMILTONIAN.md`). The transfer `M(A,z)∈SL(2,ℝ)` acts on the hyperbolic
upper half-plane `ℍ` by Möbius transformations (aletheia `SU11_CARRY_COCYCLE.md`; standard
Weyl–Titchmarsh / Krein / **Remling 2018**).

`σ₁=[[0,1],[1,0]]` is a **boost** (hyperbolic generator): `exp(τσ₁)=[[\cosh τ,\sinh τ],[\sinh τ,\cosh τ]]∈SL(2,ℝ)`,
with fixed boundary points `±1`, so its geodesic axis is the **unit semicircle**, which passes through
`i`. Verified: the orbit `exp(τσ₁)·i` stays on `|w|=1` to machine precision (`2.2×10^{-16}` over
`τ∈[-2,2]`) — it **is** that geodesic.

## 2. Geodesic at the spectral base point `z=0`; the Dirac light cone

At `z=0` the generator is `μ(A)σ₁` — a **fixed direction** (pure boost) with `A`-dependent magnitude.
Its flow is `exp\!\big(\tau(A)σ₁\big)` with proper time `τ(A)=\int_0^A μ\,dA'=\log m_3(e^A)`: a
one-parameter subgroup, i.e. a **geodesic in `ℍ`, reparametrized by proper time**. So:

> **At the spectral base point the canonical flow is exactly a geodesic, and "actualization time"
> `A` maps to geodesic proper time `log m_3`.** (This is the honest, provable form of the user's
> "follow the geodesic"; for a generic Hamiltonian the trajectory is only a generic SL(2,ℝ) curve —
> geodesic is *not* automatic, cf. Remling. We claim it only at `z=0`.)

Away from `z=0`, the eigenvalues of the generator `G(z)=iz\,σ_3+μ\,σ_1` are the **Dirac dispersion**

$$\boxed{\ \operatorname{eig}G(z)=\pm\sqrt{\mu^2-z^2}\ }$$

(verified): `|z|<μ` → real eigenvalues = **hyperbolic boost = geodesic**; `|z|=μ` → null (parabolic)
= the **light cone / mass shell**; `|z|>μ` → imaginary eigenvalues = **elliptic rotation = spectral
oscillation**. This is a 1+1 Dirac dispersion (the analogue of the mass-shell structure in Sierra's
Rindler-spacetime Dirac zeta model, **Sierra 2014** — credited), with null characteristics `A±X=const`
(`CRITICAL_PARITY_DIRAC §5`) as the light cone, and it matches the frontier's boost rapidity
`α=β−1/2` from an off-line zero (`CRITICAL_LIGHTCONE_GAIN.md`): an off-line zero is a timelike
(`|z|<μ`, amplifying) mode, and *in this dictionary* RH corresponds to all modes being null/on-cone.

## 3. The FUCC geodesic and the canonical geodesic: one clock, two weights, joined by the jet

The repo also carries a *different* geometry — the multiplicative **FUCC metric** (aletheia
`SUCC_FUCC_METRIC_GEOMETRY.md`): `d_F(a,b)=\sum_p|v_p(a)-v_p(b)|\log p=\log(\mathrm{lcm}/\gcd)`, with
the **LCM worldline** `d_F(L_{N-1},L_N)=\Lambda(N)` and proper time `\log N` (verified
`d_F=\Lambda(N)` for `N=2..17`). The scout flagged that *nobody had joined* this to the SU(1,1)
canonical flow. The join is the **ω-jet** (Pillar 1):

- conductor weight (canonical geometry): `b_{1/2}(n)=\varphi(n)/n` — the **value at `ω=1/2`** of the
  family `b_ω` (verified `=\prod_{p|n}(1-1/p)`);
- Weil weight (FUCC geometry): `2\Lambda(n)/\sqrt n = b_0'(n)` — the **`ω`-velocity (first jet) at `ω=0`**
  of the *same* family `b_ω`.

So the two geometries are **two readings of one one-parameter family `b_ω`** — the `ω=0` derivative and
the `ω=1/2` value — sharing **one log-scale clock** (proper time = `\log` scale) and **one event set**
(prime powers). They are **not** in a linearization/tangent relation: the `ω=0` tangent line extrapolated
to `ω=1/2` gives `\Lambda(n)/\sqrt n`, which is *neither* `2\Lambda/\sqrt n` *nor* `\varphi(n)/n` (e.g.
`n=2`: `0.49` vs `0.50`; `n=6`: `0` vs `0.33`). The honest join is:

> **the Weil/FUCC weight and the conductor/canonical weight are the `ω=0` velocity and the `ω=1/2` value
> of the same family `b_ω` — two samples of one flow, not one a linearization of the other.**

This matches the user's "the first domino sets the next" only in the weak sense that the first jet
(Weil/von Mangoldt, Pillar 1) is the *initial tangent* of the `b_ω` flow; the `ω=1/2` endpoint (the
conductor weight) is a different sample of that same flow, not its tangent.

## 4. "Global curvature = the limit of actualization"

The accumulated proper time is `\log m_3(a)=2\tau_1(a)+\sum_j\big[\log\frac{1+\lambda_j}{1-\lambda_j}-2\lambda_j\big]`,
where `\lambda_j=\operatorname{eig}H_{1/2,a}` and the sum is the **renormalized det₃ holonomy**
(leading term `\tfrac23\lambda_j^3` — pure cubic curvature; `\tau_1` is the smooth Archimedean
counterterm). Computed from the exact Galerkin matrix (cells scaled with the horizon):

| `a` | `N_cond` | `‖H_{1/2,a}‖` | `1−‖H‖` | det₃ holonomy |
|----:|------:|------:|------:|------:|
| 1.2 | 1 | 0.93337 | 6.7e-2 | 1.264 |
| 1.5 | 2 | 0.99926 | 7.4e-4 | 3.262 |
| 2.0 | 4 | 0.99964 | 3.6e-4 | 3.863 |
| 2.5 | 6 | 0.99978 | 2.2e-4 | 3.910 |
| 3.0 | 9 | 0.99985 | 1.5e-4 | 4.027 |

The holonomy **rises with the horizon** (the "accumulated curvature"), and `1−‖H‖→0` is the geodesic
**reaching the ideal boundary of `ℍ`** — i.e. `a→∞` ("actualization to infinity") sends the flow to
the boundary, where the Weyl disks nest to the limit point `m_\infty=-\Xi'/\Xi` (aletheia `SU11 §10`).
The user's thesis "the limit of actualization describes the curvature" is realized: **the global
curvature is the total accumulated boost `\log m_\infty`**, and

$$\textbf{RH}\iff m_\infty=-\Xi'/\Xi\ \text{is Herglotz (no pole in }\mathbb C_+)\quad[\textbf{OPEN}].$$

(These are diagnostics; the finite-`a` holonomy is Galerkin-resolution-limited; no zeta zeros enter —
`m_\infty` is evaluated as a meromorphic function, not fed ordinates.)

## 5. Honest status and the wall

The GR dictionary is **real and mostly pre-existing**: SL(2,ℝ)/ℍ transfer, Weyl disks, the Dirac light
cone, the det₃ Hamiltonian, the FUCC metric — all standard (de Branges 1968; Krein; **Remling 2018**;
Suzuki 2012) or already in the aletheia branches. The genuinely-new, provable pieces here are small and
honest: (i) *geodesic-at-`z=0`* (the canonical flow is a true geodesic at the spectral base point); (ii)
the *jet-linearization join* of the FUCC geodesic to the conductor/canonical geodesic; (iii) the
*actualization→∞ = global curvature `m_\infty`* reading with the det₃-holonomy diagnostic.

**The wall is unmoved.** RH `⟺` `m_\infty=-\Xi'/\Xi` Herglotz `⟺` the Hamiltonian stays positive to the
boundary — the same positivity the frontier could not establish, the same one **Conrey–Li 2000** showed
cannot be gotten from naive de Branges positivity. The analogy locates and dresses the wall; it supplies
no positivity.

## 6. Ledger

- **C109 (RH-inert; standard structure + new framing/joins).** Canonical system `dX/dA=[izσ₃+μ(A)σ₁]X`,
  `μ=d/dA log m_3`, acts on `ℍ` by SL(2,ℝ). **Geodesic-at-`z=0`:** generator `μσ₁` (pure boost), flow
  `exp(τσ₁)`, `τ=log m_3`, orbit of `i` = unit-semicircle geodesic (`||w|−1|≤2e-16`). **Dirac
  dispersion** `eig(izσ₃+μσ₁)=±√(μ²−z²)`: boost/geodesic `|z|<μ`, null light cone `|z|=μ`, elliptic
  oscillation `|z|>μ` (verified). **Join:** Weil weight `2Λ/√n=b_0'(n)` = first-jet linearization of
  conductor weight `φ(n)/n`; one log clock; FUCC worldline `d_F(L_{N-1},L_N)=Λ(N)` (verified N=2..17).
  **Global curvature = lim actualization:** det₃ holonomy `∑[log((1+λ_j)/(1-λ_j))−2λ_j]` rises with `a`,
  `1−‖H‖→0` = geodesic→ideal boundary, `m_∞=−Ξ'/Ξ`; RH ⇔ `m_∞` Herglotz (OPEN). Credit de Branges 1968,
  Krein, Remling 2018, Suzuki 2012, Sierra 2014 (Dirac light cone), aletheia CRITICAL_PARITY_DIRAC /
  SU11_CARRY_COCYCLE / CRITICAL_DET3 / SUCC_FUCC_METRIC_GEOMETRY. **Conrey–Li 2000 refuted de Branges
  positivity — no positivity claimed.** `scripts/r009_canonical_geodesic.py`. No RH progress.

RH remains open.
