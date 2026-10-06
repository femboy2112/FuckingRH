# The Archimedean source port: a passive Γ-channel + one negative square at s=1 (ckpt7)

**Date:** 2026-10-06. **Status:** DISCLOSED (exact structure). **RH open.**
**Reproduce:** `scripts/archimedean_port.py` (all identities to 1e-32 / prime-tail).

The directive (§11) says this is where the round cracks or dies, and demands the port be built as an
explicit `s`-dependent channel, not with `Γ` as a scalar black box. Done: the port splits cleanly, and
the entire non-holomorphic/indefinite obstruction in `H_{1/2}` turns out to be **one pole at `s=1`**.

## The port and its completion identity

    A_inf(s) = 1/s + 1/(s-1) - (1/2)log pi + (1/2) psi(s/2),
    xi'/xi(s) = A_inf(s) + zeta'/zeta(s) = A_inf(s) - sum_p m_p(s)   (Re s>1).

Verified `xi'/xi = A_inf + zeta'/zeta` to `1e-32` (check 1). Cross-check: `xi'/xi(1) = 0.023096… = -B`,
the Hadamard constant `B = ½log(4π)-1-γ/2` from the literature lock — the pole cancellation lands exactly
on the known value.

## Split 1 — the passive Γ-channel (poles at the trivial zeros, outside H_{1/2})

Gauss's series gives, for `z=s/2`,

    (1/2) psi(s/2) = -γ/2 + sum_{n>=0} [ 1/(2n+2) - 1/(2n+s) ].                          (Γ)

Verified (check 4) to `~1e-5` at test points. This is a **regularized resolvent channel**: it is the
(zeta-regularized) diagonal resolvent of the self-adjoint operator

    D_Γ := diag(0, 2, 4, 6, …) = 2·N   (N = number operator on l^2(N_0)),

i.e. `(1/2)psi(s/2) ≐ "Tr_reg (D_Γ + s)^{-1}"` with the `-1/(2n+2)` Krein counterterms. Its poles sit at
`s = 0, -2, -4, …` — **the trivial zeros of ζ**, all with `Re ≤ 0 < 1/2`. So:

> The Γ-channel is a genuinely **passive** (poles outside `H_{1/2}`) `s`-dependent boundary channel: the
> resolvent of a fixed positive self-adjoint operator `D_Γ = 2N`. This is exactly the harmonic-oscillator
> / theta heat-kernel Archimedean factor, now realized as an explicit **s-dependent** resolvent (fixing
> the old caveat that a *fixed* Gaussian vector cannot produce the s-dependent boundary — the
> s-dependence is in the resolvent `(D_Γ+s)^{-1}`, not in a frozen vector).

The spectrum `{0,2,4,…}` is the even number operator; the odd shift `2n+1` would give `ψ((s+1)/2)`. The
`-½log π` is the scale (zeta-regularization) constant.

## Split 2 — the pole part, and the s=0 cancellation

`P(s) = 1/s + 1/(s-1)`. Near `s=0`, `(1/2)psi(s/2) ~ -1/s` (since `psi(z) ~ -1/z`), so the explicit `1/s`
in `P` **cancels** it: `A_inf` is **regular at `s=0`** (check 3: `A_inf(0.1)=-1.93`, finite). So the
`s=0` pole is absorbed into the Γ-channel/ trivial-zero bookkeeping.

**The only pole of `A_inf` inside `H_{1/2}` is the single pole at `s=1`** (residue `+1`, from `1/(s-1)`).
`A_inf(1.001) ≈ 999` (check 2). In the completed `xi'/xi` it cancels against `zeta'/zeta`'s `-1/(s-1)`
(ξ entire, `xi'/xi(1)` finite). This is the one **negative square** (`κ=1`): `1/(s-1)` is
anti-positive-real on `H_{1/2}` (`Re 1/(s-1) < 0` for `1/2<σ<1`); it is the `s`-side image of the
Suzuki rank-2 pole sector (C83, signature `(1,1)`) after the `s=0`/trivial part is absorbed into the
passive Γ-channel.

## The finite-completion obstruction (sets up §16)

For every finite cutoff `P`, the prime sum `sum_{p<=P} m_p(s)` is **holomorphic at `s=1`** (its poles are
on the imaginary axis, where `p^s=1`). So

    F_P(s) := A_inf(s) - sum_{p<=P} m_p(s)   has a genuine pole at s=1 (residue 1) for EVERY finite P.

Verified (check 5–6): `F_P(1+0.01) ≈ 96 ≈ 1/0.01` for `P=50, 500`. The `s=1` pole of the completed object
is an **infinite-cutoff** phenomenon (it appears only as `P→∞`, as `zeta'/zeta` develops its pole).

**Consequence for Schur–Vitali (C104).** The naive finite truncation `F_P` is **not holomorphic on
`H_{1/2}`** (pole at `s=1`), so it fails hypothesis (P) for a trivial reason. The finite completion MUST
use a **cutoff-dependent boundary `A_{inf,P}`** that cancels the `s=1` pole at finite `P` and restores it
only in the limit (directive §16: "do NOT sum primes then subtract infinity"). This **reduces** the
finite-completion problem to two clean sub-problems:

1. **Pole cancellation (solvable):** build `A_{inf,P}` so `F_P = A_{inf,P} - sum_{p<=P} m_p` is
   holomorphic on `H_{1/2}` and `F_P → xi'/xi` on `Re s>1`. The natural source is the
   Euler–Maclaurin / heat-kernel counterterm `N(P)^{1-s}/(s-1)`-type boundary that carries the `1/(s-1)`
   structure but is regular at `s=1` for finite `P` (built explicitly in ckpt8).
2. **Positive-realness of the pole-cancelled `F_P` on `H_{1/2}` (the real wall):** once holomorphic, is
   `F_P` positive-real on `H_{1/2}`? This is the Conrey–Li/Sarnak danger (LITERATURE_INTERFACE §3): the
   `ξ(s)/ξ(s+1)` phase (dense `log ζ`) forces `Re < 0` somewhere in the strip in the limit, unless the
   coupling is engineered to dodge it.

So the Archimedean port does **not** itself kill the round: the `s=1` pole (`κ=1`) is a *removable*
finite-completion nuisance, not an irreducible negative square — IF a cutoff-dependent boundary cancels
it. The round lives or dies on sub-problem 2, which is where the coupling (ckpt8) must do its work.

## Ledger

New row **C105**: `A_inf` splits into (a) a genuinely passive Γ-channel `(1/2)psi(s/2) =` regularized
resolvent of `D_Γ=2N`, poles at the trivial zeros (`Re≤0`, outside `H_{1/2}`); and (b) a pole part
`1/s+1/(s-1)` whose only `H_{1/2}` singularity is the single pole at `s=1` (one negative square `κ=1`,
the `s`-image of the Suzuki rank-2 pole sector). The finite truncation `F_P=A_inf-Σ_{p≤P}m_p` has a pole
at `s=1` for every finite `P` (emergent only as `P→∞`), so the finite completion needs a cutoff-dependent
boundary `A_{inf,P}` to cancel it. This reduces finite completion to (1) pole cancellation [solvable] +
(2) positive-realness of the pole-cancelled finite object [the wall].
