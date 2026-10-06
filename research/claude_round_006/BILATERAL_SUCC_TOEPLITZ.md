# The local carry filter is the Hardy/Toeplitz compression of a bilateral transfer function

**Round 006. RH IS OPEN. Reproduce:** `scripts/r006_affine_corner.py` §8a (`‖resolvent − Toeplitz‖ ≤ 6e-16`
on the interior), §8b. This upgrades Round005 C96 / the Aletheia augmentation note §5 from "same Fourier
symbol" to an **exact operator-compression identity** — major-crack target (B).

## 1. Successor = Hardy compression of the bilateral shift (classical, Sz.-Nagy)

Inverse SUCC bilateralizes the additive backbone, `N → Z`, and there the successor is the **bilateral
shift** `U` on `l²(Z)`, which is *unitary*. Under the Fourier transform `l²(Z) ≅ L²(T)`, `U =` multiplication
by `z = e^{iθ}`. Compressing to the positive (Hardy) sector `H² = P_+ L²(T)` gives the **unilateral shift**
`S = T_z = P_+ M_z|_{H²}`, our successor. So `S` is precisely the Toeplitz compression of the unitary `U`,
and `U` is its **minimal unitary dilation** (Sz.-Nagy–Foias): `S^n = P_+ U^n|_{H²}` for `n ≥ 0`. The
compression defect `I − SS* = |1><1|` (`INTEGER_CORNER_DEFECTS.md`) is the rank-one Hankel defect of this
compression.

Under this identification the augmentation/difference generator `1 − z` of the Aletheia composition note
(the thing `x ↦ 1` forgets) is exactly `I − S`:

    (I − S) = T_{1−z},        (I − S)*(I − S) = T_{|1−z|²} = T_{2 − 2cos θ}      (verified §8b)

(The second holds with **no Hankel correction** because `1−z` is analytic: for an analytic symbol `ψ∈H^∞`,
`T_φ T_ψ = T_{φψ}` whenever `φ` is co-analytic *or* `ψ` is analytic — here `φ = 1−z̄` is co-analytic and
`ψ=1−z` analytic, so both apply.) This is the carré-du-champ symbol `|1−z|²` that Round005 (C99) and the
Aletheia note (§5) both reached.

## 2. The local prime factor is an analytic Toeplitz operator — exactly

Round005/aletheia had the local repaired factor at the *symbol* level:

    √σ_p  ∼  (1 − e^{i(log p)ξ}) / (1 − p^{-1/2} e^{i(log p)ξ})   =   (1 − z)/(1 − r z),   r = p^{-1/2}.

The Round006 upgrade: this symbol is analytic and bounded in the disk (`|rz| = p^{-1/2} < 1`), so its
Toeplitz operator is a genuine **analytic (lower-triangular) Toeplitz operator**, and it factors
multiplicatively with no Hankel correction:

    ┌────────────────────────────────────────────────────────────────────────┐
    │   B_p  =  T_{(1−z)/(1−rz)}  =  T_{1−z} · T_{1/(1−rz)}                      │
    │       =  (I − S) (I − p^{-1/2} S)^{-1}                                     │
    │       =  P_+  M_{(1−z)/(1−rz)}  |_{H²}      (compression of bilateral mult) │
    └────────────────────────────────────────────────────────────────────────┘

Verified directly (`§8a`): the matrix `(I − S)(I − rS)^{-1}` equals, on the window interior, the
lower-triangular Toeplitz matrix of the Taylor coefficients of `(1−z)/(1−rz)`:

    (1 − z)/(1 − r z)  =  1 − (1 − r) Σ_{k≥1} r^{k-1} z^k,

to `6·10^{-16}`. So the "augmentation boundary × critical memory" `B_p = (1−X)(1−p^{-1/2}X)^{-1}` proposed
in the Aletheia note §8 is **literally** the Hardy compression of multiplication by the bilateral transfer
function `(1−z)/(1−rz)` on `L²(T)` — an invertible-up-to-the-pole object compressed to the positive sector.

> **Factorization structure:** `B_p = (boundary) × (memory)`. The boundary `(I−S)` is the deleted-`0`
> innovation (`= T_{1−z}`, the high-pass); the memory `(I − p^{-1/2}S)^{-1}` is the causal geometric
> depth-resolvent at the critical half-density `r = p^{-1/2}`. Both are analytic ⇒ `B_p` is analytic
> Toeplitz ⇒ `B_p^* B_p = T_{|...|²} = T_{σ_p}` is a single Toeplitz operator with the Round005 density
> `σ_p ≥ 0`. The positivity of `σ_p` is the Fejér–Riesz/Toeplitz positivity of `|B_p-symbol|²`, automatic
> and **local** — hence (as always) RH-inert per prime.

## 3. Why bilateralizing the depth does not symmetrize the memory

One might hope the causal memory `(I − p^{-1/2}S)^{-1}` is itself the Hardy compression of a *symmetric*
bilateral object, so that the critical weight `p^{-1/2}` becomes forced by a two-sided symmetry. It is
**not**: the Neumann series `Σ_{k≥0} p^{-k/2} S^k` converges because `p^{-1/2} < 1` and is intrinsically
one-sided (`k ≥ 0`); on the bilateral carrier the same series still runs over `k ≥ 0` (the two-sided sum
`Σ_{k∈Z} p^{-|k|/2} U^k` is a *different*, genuinely symmetric operator — the Poisson/Abel kernel — whose
compression is **not** the causal resolvent). So:

> The geometric depth-memory is a Hardy/causal object, and bilateralization leaves it causal. The critical
> `p^{-1/2}` is **not** forced by additive-shift symmetry; it is forced by the **local Haar half-density**
> (Round005 C96) — i.e. by the places, not the integers (`ADELIC_HALF_DENSITY.md`).

## 4. Status and what it buys

Exact and local, hence RH-inert per prime (as Round004 C90 and the GCD meta-theorem C89 require). What it
buys the global program:

- a clean, zero-free, closed-form **local factor** `B_p = (I−S)(I−p^{-1/2}S)^{-1}` in Hardy coordinates,
  ready to be wired (not summed — `INTERSECT_BEFORE_SQUARING.md`) across primes and completed at `∞`;
- the exact statement that the universal boundary is `T_{1−z} = I − S` on *every* sheet — the stratified
  "same SUCC form on each prime jet" made operator-precise.

The wall is unchanged: assembling `{B_p}` into a **global** positive `B` with `K_Ψ = B*B`, uniformly in the
horizon, remains the Weil-positivity problem (C91). Toeplitz/Hardy theory gives the local pieces for free;
it does not give the global object. See `PROOF_ATTEMPT_006.md`.
