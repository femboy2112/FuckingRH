# Round 006 — inverse SUCC/FUCC, affine group completion, the integer shadow

**Branch:** `claude/inverse-affine-completion-006` (from Round005 head `3222f97`; isolated from main's later
rounds). **RH IS OPEN.** **Outcome (2):** the proposed class of constructions is killed by precise no-gos;
the wall is re-derived from the invertible parent and sharpened, not moved.

## CURRENT WALL (live)

> The integer corner's arithmetic (`Λ`, `log n`, the sieve, the half-density) is **exactly** the
> compression shadow of the invertible affine parent `Q⋊Q^×` — and that shadow is **Bost–Connes + Cuntz
> `Q_ℕ` + Connes/Tate**, realized in clean exact coordinates. Every ingredient up to "arithmetic `B`" is in
> hand, zero-free, closed-form. The target — a non-circular global positive `B` with `K_Ψ = B^*B` — is
> **not** reached, and three independent no-gos (C101/C102/C103) show this *family* of moves cannot reach
> it: it lands exactly on the **Connes gap = Weil positivity = RH**. The one missing ingredient is named
> precisely: the **signed, analytic Weil cross terms** (primes `+` vs Archimedean pole `−`), which no
> positive/coherent/algebraic assembly supplies.

## The one-line thesis, confirmed

*"Arithmetic defects downstairs are compression defects of perfectly invertible symmetries upstairs"* — **true,
and exactly Bost–Connes.** The von-Mangoldt signature even **vanishes on `Z`** (`Λ_op≡0` once `0` is restored
and `S` becomes unitary): the primes' additive signature is a shadow of deleting `0` (HOSTILE B/C). This is
the deranged-but-true core, and it is RH-inert — a sharp statement of where the wall is *not*.

## Checkpoints landed (committed + pushed as they became coherent)

1. **Rational affine parent + integer corner, exact identities** (C100): braid `D_q T_a D_q^{-1}=T_{qa}`;
   `S,V_p` isometries; `E_S=I−SS*=[S*,S]=|1><1|`; `Λ_op=Σ(log p)V_{p^k}E_S V_{p^k}*=diag Λ`;
   `H_log=Σ(log p)V_{p^k}V_{p^k}*=diag(log n)`; `Π_{p,k}S̃=S^{p^k}Π_{p,k}`; `v_p=`inverse-FUCC survival.
2. **Local carry filter = exact Hardy/Toeplitz compression** (C100): `B_p=(I−U_p)(I−p^{-1/2}U_p)^{-1}` with
   `U_p` the **prime-depth shift** (prime clock `e^{i(log p)ξ}`, = `V_p` on the `p`-tower — *not* the unit
   successor `S`) = analytic Toeplitz of `(1−z)/(1−p^{-1/2}z)` (upgrades Round005 C96 to an operator identity).
3. **Intersect-before-squaring no-go** (C101): uniform boundary → `CROSS~+2π(N)²` (quadratic); strengthened —
   the stratified `(I−S^p)` only halves it, still quadratic. Common mode = the identity `I`/source `|1>`.
4. **Literature interface + honest reframing**: whole construction = BC + Cuntz + Connes/Tate; `H_log`=BC
   Hamiltonian, braid=Laca–Raeburn (T1), half-density=Connes `|g|^{1/2}`; exclude-0 Nica defect `|p−1><1|`
   verified. Von-Mangoldt "headline" reframed as exposition (RH-inert), not a theorem.
5. **Fractional SUCC / Gamma intertwiner** (C103): `T_a D_q=D_q T_{a/q}`, `[A,P]=iP`, `Γ`=Archimedean
   Mellin↔Fourier intertwiner (Fresnel at `s=1/2`); **group completion ≠ analytic continuation** (the
   central conceptual reading, heuristic not a theorem); GL fractional-`ζ` (+ Flammable/Guariglia
   provenance, RH-inert).
6. **Adelic half-density + product formula** (C102): `p^{-k/2}=√|p^k|`=Tate self-dual; `∏_v|q|_v=1`; local
   unitarity selects `1/2` exactly; product formula is modulus-only, does not cancel the bulk.
7. **Hostile controls** (A–J + M), all decisive; **target architecture + DAG + proof attempt**.
8. **Strengthened C101** (stratified boundary tested; dichotomy overlap→quadratic / orthogonal→linear).

## Net ledger additions

- **C100**: the exact integer-corner identity bundle (+ exclude-0 Nica defect). All RH-inert.
- **C101**: intersect-before-squaring diverges quadratically (uniform *and* stratified); escape needs
  destructive signed interference = Weil.
- **C102**: product formula = modulus identity ≠ bulk cancellation; adelic completion lands on the wall.
- **C103**: group completion ≠ analytic continuation (why the family hits the wall) + full literature
  placement (BC/Cuntz/Connes) and the Connes gap = Weil positivity = RH.

## Honest status

Round 006 is a **characterization / rediscovery with sharp new no-gos, RH untouched.** It did **not**
produce a proof step. What it produced:

- the cleanest exact coordinates yet for the prime side and the boundary (`Λ=[S*,S]` transported, `B_p`=Hardy
  compression), with honest priority to Bost–Connes/Cuntz/Connes;
- three independent, quantitative no-gos that *converge on one missing object* — the signed analytic Weil
  cross terms — from the assembly side (C101), the measure side (C102), and the continuation side (C103);
- the sharp meta-statement that **any route inside the BC/Cuntz/Connes circle reaches this same wall**, so a
  genuinely new step must import the analytic positivity from *outside* the algebra (e.g. the function-field
  analogue where Weil positivity is a theorem), or aim at an unconditional non-RH-equivalent sub-result.

RH remains open.
