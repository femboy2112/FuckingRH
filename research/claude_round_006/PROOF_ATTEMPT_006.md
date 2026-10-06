# Proof attempt 006 — inverse affine completion

**Date:** 2026-10-06. **Verdict:** RH remains open. This round is **outcome (2)**: the proposed class of
constructions (a non-circular global positive `B` assembled from the invertible affine parent) is **killed
by precise no-gos**, and the wall is re-derived and sharpened, not moved.

## Thesis tested

That the arithmetic defects of `N` are compression shadows of the invertible affine group `Q ⋊ Q^×`, and
that putting the inverse SUCC/FUCC operations back — then assembling the prime sheets with the universal
successor boundary **before** squaring and completing adelically — yields a non-circular positive `B` with
`K_Ψ = B^*B`.

## What the completion gave (exact positives, all RH-inert)

1. **The parent and corner are exact** (C100): `Q⋊Q^×` on `l²(Q)`, the affine braid `D_q T_a D_q^{-1}=T_{qa}`,
   compression to `l²(N)` with `S,V_p` isometries and `V_p*` the compressed inverse (divisibility =
   inverse-FUCC survival).
2. **The boundary is forced** (C100): `E_S = I−SS* = [S*,S] = |1><1|` — the additive boundary is the
   successor's self-commutator, the single deleted `0`. The source `Ω=|1>` of earlier rounds is *derived*,
   not posited.
3. **Von Mangoldt and `log n` are the boundary transported / the occupancy** (C100): `Λ_op = Σ(log p)
   V_{p^k}E_S V_{p^k}* = diag Λ`; `H_log = Σ(log p)V_{p^k}V_{p^k}* = diag(log n)`; tied by `log n=Σ_{d|n}Λ(d)`.
4. **The local factor is an exact Hardy compression** (C100): `B_p=(I−U_p)(I−p^{-1/2}U_p)^{-1}`, `U_p` the
   **prime-depth shift** (prime clock, = `V_p` on the `p`-tower; **not** the unit successor `S`) = analytic
   Toeplitz of `(1−z)/(1−p^{-1/2}z)` — upgrades Round005 C96 from "same symbol" to an operator identity.
5. **The half-density is Tate self-dual** (C102): `p^{-k/2}=√|p^k|`, `∏_v|q|_v=1`, local unitarity selects
   `1/2` exactly.

All of this is **Bost–Connes + Cuntz `Q_ℕ` + Connes/Tate** in exact coordinates (C103,
`LITERATURE_INTERFACE.md`): `H_log` = the BC Hamiltonian, `V_p` = the BC isometries, the braid =
Laca–Raeburn (T1), the half-density = Connes' `|g|^{1/2}`. The only non-standard element is the exclude-0
compression (Nica defect `|p−1><1|`) — presentational.

## What the completion killed (no-gos — the result)

- **Intersect-before-squaring, uniform boundary → quadratic divergence** (C101). The universal `(I−S)` is a
  common mode; assembled, the `π(N)` sheets add coherently and the energy diverges `~π(N)²`, *worse* than
  the direct sum. A working `B` needs a **prime-specific, signed** wiring — the Weil cross terms.
- **Product formula ≠ bulk cancellation** (C102). `∏_v|q|_v=1` is a modulus identity; the additive bulk
  `Σ_p M_p` is cancelled only by the functional equation's analytic `Γ`/pole sector, not by any algebraic
  assembly. The adelic completion repackages Tate and stops at Weil positivity.
- **Group completion ≠ analytic continuation** (C103). The algebra reproduces the arithmetic only in
  `Re s>1`; the continuation into the strip is the extra analytic datum (functional equation = Archimedean
  `Γ` + product formula), which the Bohr–Mollerup control shows a completion cannot supply. RH lives in the
  continued object.
- Inherited controls re-confirmed: naked overlap = GCD (RH-inert, C89/§9); `Z`-ablation kills `Λ`
  (compression artifact, HOSTILE B/C); quotient = circulant (RH-inert, C94/C97); wrong half-density breaks
  unitarity (control H).

## The smallest surviving wall

Identical to Round-004/005 (C91), now reached from the invertible parent and pinned from three sides:

> **The completed, signed, prime + Archimedean Weil distribution must be positive, uniformly in the
> horizon.** Equivalently: `K_Ψ = B^*B` for a horizon-uniform arithmetic `B` built without zeros. This is
> the Connes gap (no explicit positive operator realizing the trace-formula positivity) = Weil positivity
> = RH. The inverse-affine machinery supplies the prime side, the boundary, and the half-density in exact
> closed form, and a proof that the **assembly/completion** step is where RH hides — but it does **not**
> supply `B`, and three independent no-gos show this family of moves cannot.

## Where a future round could still pry

The honest reading is that any route *inside* the Bost–Connes/Cuntz/Connes circle will reach this same wall
(C103 argues this structurally). A genuinely new step must bring the **analytic positivity** from outside
the algebra. Two directions that are *not* re-confirmations of the wall:
1. the **function-field analogue**, where the Weil positivity is a *theorem* (Frobenius eigenvalues on
   étale cohomology), to import the mechanism that supplies the missing sign — and ask what its arithmetic
   shadow is;
2. an **unconditional sub-result** that is not RH-equivalent (a zero-density or gap bound) reachable from
   the exact `B_p`/`H_log` coordinates, which would be real progress without pretending to be RH.

Neither is attempted here; both are flagged honestly as outside this round's closed class.
