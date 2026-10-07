# Reflection positivity is the light cone; the integrate-and-fire domino flow

**Round 009 / Pillar 3. Branch `claude/arithmetic-curvature-loops-008`.** **RH IS OPEN.**
**Reproduce:** `scripts/r009_reflection_lightcone.py` (all checks pass; no zeta zeros used as input).

The user's closing lines — *"this is begging for GR-shaped math to drop out; we literally have an
analogical notion of light cones"* — land on a real, standard equivalence with three faces. All three
are RH-*equivalent*, none is a proof, and the honest names and prior art are given throughout.

## 1. Reflection positivity (the positive-energy / Hilbert–Pólya face)

Suzuki (JLMS 2023, Thm 1.2): **RH `⟺` `g=−Ψ` is a Krein screw function `⟺` the screw/covariance kernel**

$$G_g(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u)\ \succeq\ 0\ \text{on every finite set.}$$

Its honest name is **conditional negative-definiteness / infinite divisibility** (Schoenberg–von
Neumann 1941; Krein; Nakamura–Suzuki `e^{−Ψ}` = an infinitely-divisible characteristic function) — the
probabilistic face of **Osterwalder–Schrader reflection positivity**, i.e. the existence of a
positive-energy Hamiltonian whose "two-point function" is `Ψ` (Hilbert–Pólya). The reflection involved
is the **functional-equation involution `s↔1−s`** (Burnol); calling it OS reflection positivity is
legitimate only once that involution is matched to the OS time-reflection — so we use the screw/CND
name and note the OS reading as a repackaging.

Diagnostic: the finite screw Gram on a 14-point grid `t∈[0.3,2.9]` is PSD (`min eig = 1.8×10^{-2}>0`).
This is an RH-*consistency* check, **not evidence for RH**.

## 2. The integrate-and-fire "domino" flow (the user's first-domino / geodesic picture)

From `SCREW_SINC_LEVY_UNIFICATION.md §7`: write `Ψ(t)=\text{(Archimedean reservoir)}−\sum_{p^k\le e^t}\frac{\Lambda(p^k)}{p^{k/2}}(t-\log p^k)_+`.
Between prime events `Ψ` is **affine plus smooth-Archimedean-curved**; at each event `t=\log p^k` its
**slope jumps down by `\Lambda(p^k)/p^{k/2}`** (verified against finite differences):

| event | `t=\log p^k` | slope jump (right−left) | `−\Lambda/p^{k/2}` |
|------:|-----:|-----:|-----:|
| `2` | 0.69315 | −0.49008 | −0.49013 |
| `3` | 1.09861 | −0.63422 | −0.63428 |
| `2²` | 1.38629 | −0.34649 | −0.34657 |
| `5` | 1.60944 | −0.71967 | −0.71976 |
| `7` | 1.94591 | −0.73538 | −0.73548 |
| `2³` | 2.07944 | −0.24495 | −0.24506 |
| `3²` | 2.19722 | −0.36608 | −0.36620 |

This is **exactly the user's dynamics**: the Archimedean reservoir sets the gradient, each prime
"fires" a downward slope-kick (the domino), and **RH `⟺` the reserve `Ψ` never crosses zero** (verified
`min Ψ>0` on the grid — diagnostic). The curvature is `Ψ''=\text{smooth Archimedean} - \sum_{p^k}\frac{\Lambda(p^k)}{p^{k/2}}\delta_{\log p^k}`,
i.e. `−g''(t−u)` is the **Weil kernel** — the second derivative (curvature) of the screw function. This
is the precise sense in which the first jet (Pillar 1) = velocity and the kernel = curvature.

## 3. The light cone: on-line = null, off-line = timelike (the signature)

The finite Weil tangent Gram `A(t,u)=\sum_\lambda e^{\lambda(t-u)}` (`FINITE_ZERO_SUZUKI_WEIL_TANGENT §8`)
has a clean causal signature (verified with **freely-chosen** `r,γ` — *not* zeta ordinates):

- **on-line** pair `λ=±iγ`: kernel `2\cos(γ(t-u))` → **PSD, rank ≤ 2** (`eig∈[−10^{-16},25.2]`). A null /
  rotational mode — **on the light cone**.
- **off-line** quartet `{λ,\barλ,−λ,−\barλ}`, `λ=r+iγ`, `r≠0`: kernel `4\cosh(r(t-u))\cos(γ(t-u))` →
  **indefinite** (`r=0.2`: `eig∈[−3.3,53.6]`; `r=0.5`: `eig∈[−24.9,75.3]`). A **timelike / boost** mode
  (the `\cosh` is the hyperbolic factor; `r=β−1/2` is the boost rapidity) — **off the light cone**, and
  a *negative direction* in the Weil form.

So **RH `⟺` every zero is null (on the light cone), where the Weil/reflection form is PSD**; moving a
zero off-line is a timelike boost that breaks positivity. This is the literal light cone of
Lax–Phillips scattering (finite propagation speed; **Lax–Phillips 1976**, **Faddeev–Pavlov 1972**) and
of Sierra's Rindler-spacetime Dirac zeta model (**Sierra 2014**); it is the same `|z|=μ` Dirac mass
shell of Pillar 2, and the same `α=β−1/2` rapidity of the frontier's `CRITICAL_LIGHTCONE_GAIN.md`.

## 4. Honest status

These three faces are **one standard RH-equivalent** seen three ways (reflection positivity / screw /
light cone). Credit: Suzuki 2023 (Thm 1.2/1.7); Schoenberg–von Neumann 1941 (CND); Nakamura–Suzuki
(infinite divisibility); Weil 1952 and Bombieri 2000 (the quadratic form); Connes 1999 (trace-formula
positivity); **Lax–Phillips 1976**, Faddeev–Pavlov 1972 (the literal light cone); Burnol (propagator /
conductor operator); Berry–Keating 1999 and **Sierra 2014** (Dirac/Rindler light-cone Hamiltonian). The
GR picture is **real but is a dictionary, not a mechanism**: "**causality `⟺` RH**" (adelic
Lax–Phillips) is a *program*, not a theorem, and the positivity it would need is the open wall
(**Conrey–Li 2000** having refuted the naive de Branges positivity route). Nothing here is evidence for
RH; the diagnostics are consistency checks only.

## 5. Ledger

- **C110 (RH-inert; standard, three faces + light-cone framing).** (1) Reflection positivity: screw
  kernel `G_g(t,u)=Ψ(t)+Ψ(u)−Ψ(t−u)` PSD `⟺` RH (Suzuki 2023 Thm 1.2; CND/inf-divisible,
  Schoenberg–von Neumann 1941); finite Gram PSD (min eig `1.8e-2`, diagnostic). (2) Integrate-and-fire:
  `Ψ` slope jumps down by `Λ(p^k)/p^{k/2}` at `t=\log p^k` (verified to ~1e-4), affine-between-events,
  RH `⟺` reserve `Ψ>0`; `Ψ''=`Archimedean`−`prime impulse train `=−g''=` Weil kernel. (3) Light cone:
  Weil Gram `\sum e^{λ(t-u)}` — on-line `λ=±iγ` → `2\cos` PSD (null); off-line `λ=r±iγ` → `4\cosh(r·)\cos`
  indefinite (timelike boost, `r=β−1/2`); verified with freely-chosen `r,γ`. RH `⟺` all modes null.
  Credit Suzuki 2023, Schoenberg–vN 1941, Weil/Bombieri, Connes 1999, Lax–Phillips 1976, Faddeev–Pavlov
  1972, Burnol, Berry–Keating, Sierra 2014. "Causality `⟺` RH" = program; Conrey–Li 2000 refuted de
  Branges positivity. `scripts/r009_reflection_lightcone.py`. No RH progress; no zeta zeros as input.

RH remains open.
