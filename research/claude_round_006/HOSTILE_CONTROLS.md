# Hostile controls (ckpt11)

**Date:** 2026-10-06. **Status:** DISCLOSED (controls passed). **RH open.**
**Reproduce:** `scripts/hostile_controls_006.py`.

A genuinely arithmetic completion must be **mutation-sensitive**: break the arithmetic and the two
load-bearing identities must break —

- (C) source correlation `J_σ^* J_σ(σ) = -zeta'/zeta(σ)` (Re s>1),
- (F) finite completion `F_P(s) → xi'/xi(s)` (Re s>1).

If a mutated ("fake arithmetic") version still reproduced the targets, the construction would be generic
and RH-inert. It does not. Battery at `P=3000`, targets `-zeta'/zeta(2)=0.569961`, `xi'/xi(2+i)=0.0694+0.0458i`:

| mutation | err vs `-ζ'/ζ` | err vs `ξ'/ξ` | verdict |
|---|---|---|---|
| baseline (true arithmetic) | 3.3e-4 | 5.3e-7 | reference (matches; residual = prime tail) |
| delete prime p=3 | 1.2e-1 | 1.2e-1 | **breaks** |
| fake composite wires (6,10) | 7.2e-2 | 7.1e-2 | **breaks** |
| charge `log p → 1` | 1.8e-2 | 1.1e-1 | **breaks** |
| half-density exponent tilt (+0.1) | 9.8e-2 | 4.9e-2 | **breaks** |
| remove Archimedean boundary | — | 3.8e-1 | **breaks** |
| perturb Γ (`ψ` shift +0.3) | — | 1.7e-1 | **breaks** |
| random periods (same density) | 4.7e-1 | 3.2e-1 | **breaks** |

**Every** arithmetic mutation breaks the identities by `O(0.1–0.5)`; only the true primes, true `log p`
charge, true half-density `p^{-1/2}`, and the true Archimedean/Γ boundary reproduce `-ζ'/ζ` and `ξ'/ξ`.

**Consequence.** The Round006 objects are the *genuine* arithmetic ones — so the round's no-go (the
completed source response is **not passive** on `H_{1/2}`, C106–C108) is a statement about the **real**
RH problem, not about a generic passive network that would survive fake arithmetic. (A random-period or
fake-wire version is simply a different, non-ζ function; it is *also* non-passive, which confirms that
non-passivity itself is generic — the special, mutation-sensitive content is that the *target* is exactly
`ξ'/ξ`, whose passivity ⟺ RH.)

Controls specific to coupling order (#9 direct-sum vs common source, #10 quotient-before vs
couple-before) are handled structurally: #9 leaves the scalar sum unchanged (independent arms ⇒ sum,
C103/C106), and #10 is settled by the parent-independence lemma (C108) — the endpoint `ξ'/ξ` is the same
either way, so neither reorders positivity.

## Ledger

New row **C109**: hostile-control battery passed — the source correlation `=-ζ'/ζ` and completion
`=ξ'/ξ` are mutation-sensitive (every arithmetic mutation — delete/insert prime, wrong charge, wrong
half-density, remove/perturb Archimedean, random periods — breaks them by `O(0.1–0.5)`). The Round006
no-go is therefore about the genuine arithmetic target, not a generic artifact.
