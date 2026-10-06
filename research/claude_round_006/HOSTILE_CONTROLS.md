# Hostile controls (Round 006, mandatory)

**RH IS OPEN. Reproduce:** `scripts/r006_hostile_controls.py`, `scripts/r006_adelic_checks.py`,
`scripts/r006_affine_corner.py`, `scripts/r006_intersect_before_squaring.py`. Every control below is run or
cited to an exact computation. A no-go is a result.

## Main controls (directive §19)

| # | control | result | verdict |
|---|---|---|---|
| **A** | `N`-only (isometries, no inverses) | defects `E_S=|1><1|`, `E_p` present; `Λ_op=diag Λ` | arithmetic lives in the corner |
| **B** | `Z` (inverse SUCC, no rational inverse FUCC) | `U` unitary ⟹ `E_S=I−UU*=0` (verified `0.00e+00`) ⟹ **`Λ_op ≡ 0`** | **von Mangoldt is a compression artifact of the deleted `0`**; `Z` adds no RH content (it is the standard minimal unitary dilation of `S`) |
| **C** | remove the corner (work upstairs on `Q`) | all `T_a,D_q` unitary; every defect vanishes | **compression is load-bearing**; the arithmetic event structure is created by projection, not by the parent |
| **E** | naked overlap `Π*Π = V_{p^k}*V_{q^l}` | exact coprime shuffle `m↦q^l m/p^k` (verified §9) | collapses to the GCD/factorized kernel (C81/C88/C89) — **RH-inert** |
| **F** | boundary-dressed overlap (insert `I−S` before intersecting) | uniform boundary ⟹ `CROSS ~ +2π(N)²` (C101) | **worse than the sum**: common-mode boundary adds coherently; no escape |
| **G** | composite fake-prime `V_6` | `V_6=V_2V_3` exact; `V_6V_6*=Q_2Q_3`; `Λ(6)=0` | construction is **redundancy-aware**: composites get no von-Mangoldt weight automatically |
| **H** | wrong half-density `1/2+ε` | `‖U_a f‖/‖f‖=|a|^{-ε}≠1` for `ε≠0` | **local unitarity selects `1/2` exactly**; `ε≠0` breaks the isometry (and moves the self-dual point / functional equation) |
| **I** | direct-sum `Σ_p B_p^*B_p` | `DIAG ~ 2π(N)` (bulk divergence) | the Round005 divergence persists (C91/C98) |
| **J** | quotient-history (average away branch/carry) | cyclic SUCC on `Z/L` is a circulant, DFT-diagonal (off-diag `3e-16`) | **commutative convolution ⟹ RH-inert** (C94/C97); carry survives only in the irregular `Z`-lift |

(Controls A, B/C, G, J verified in `r006_hostile_controls.py`; E in `r006_affine_corner.py §9`; F/I in
`r006_intersect_before_squaring.py`; H in `r006_adelic_checks.py`.)

## Addendum controls (directive §M)

| # | control | result / verdict |
|---|---|---|
| **M1** | `Q` without topological completion → Gamma? | **No.** Rational fractional SUCC gives the recursion `Γ(z+1)=zΓ(z)` but not `Γ`; Bohr–Mollerup shows the missing datum is log-convexity (analytic, not algebraic). `FRACTIONAL_SUCC_GAMMA_INTERTWINER.md §D/G`. |
| **M2** | `R`-translation without prime dilations | generic translation flow; **no Euler/arithmetic** `ζ` structure (no multiplicative lattice). |
| **M3** | continuous dilations without the integer/prime lattice | recovers generic Mellin harmonic analysis (the `Γ`/Archimedean side) but **loses Euler arithmetic**. |
| **M4** | wrong lattice (random dilation generators) | the Archimedean `Γ`/Mellin structure survives; the **arithmetic `ζ` structure does not** (it is specifically the *primes*). |
| **M5** | fractional difference `(I−S)^α` without FUCC | `(I−S)^α` and the `(log n)^α` weights are **generic** (any Dirichlet series); the arithmetic enters only through the prime dilations. `§K`. |
| **M6** | Gamma inserted by hand | **disallowed** as proof-bearing; `Γ` must be *derived* as the Archimedean intertwiner (`§E`), which it is, but that derivation is Tate's — RH-inert. |
| **M7** | Hardy `Z` plot | **diagnostic only**; `Z(t)` real verified (`Im=O(10^{-31})`), no RH inference. |

## Net

Every control either confirms an inherited no-go (E→GCD, I→bulk divergence, J→circulant) or produces a new
sharp one:

- **B/C (the sharpest):** the von-Mangoldt/prime signature is created by the exclude-`0` compression; it
  **vanishes on `Z`**. The arithmetic is a shadow effect, exactly the round's hypothesis — and exactly why
  it is RH-inert on its own.
- **F (C101):** a uniform boundary assembled before squaring is *anti-helpful* (quadratic divergence),
  naming the required signed prime-specific wiring (= Weil cross terms).
- **H:** the critical `1/2` is forced by local unitarity / self-dual measure — necessary, not sufficient.
- **M1–M5:** `Γ`/Mellin is generic (survives wrong lattices); the primes carry the arithmetic; the two meet
  only in the functional equation, which is the analytic datum group completion cannot supply.

No control opens a route through the Weil wall. Several close natural-looking ones decisively.
