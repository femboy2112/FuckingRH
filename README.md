# FuckingRH

A proof-first research program attacking the **Riemann Hypothesis** through one concrete,
RH-equivalent positivity target, pursued across several independent agent lineages (astra, aletheia,
claude) and consolidated here on `main`.

**Status: RH remains open.** Nothing in this repository claims otherwise. The repository is organized to
keep honest the distinction between what is *proved*, *computed*, *conjectured*, and *refuted*, and to
name — precisely — the single load-bearing theorem a genuine proof still owes.

---

## The RH-equivalent target

Masatoshi Suzuki (JLMS 2023) gives an explicit even function `Ψ(t)`, built directly from prime powers
plus the Archimedean completion, with

```
RH  ⟺  Ψ(t) ≥ 0 for all t  ⟺  the Kreĭn screw kernel K_Ψ(t,u)=Ψ(t)+Ψ(u)−Ψ(t−u) ⪰ 0
```

and, by Nakamura–Suzuki, `⟺ e^{−Ψ}` is an infinitely divisible characteristic function. Equivalently
(Lagarias 1999 (1.5)/(1.19); the bare equivalence due to Hinkkanen):

```
RH  ⟺  ξ'/ξ is positive-real (Pick/Herglotz) on H_{1/2} = {Re s > 1/2}
```

where `ξ(s)=½ s(s−1) π^{−s/2} Γ(s/2) ζ(s)`. The unconditional half `Re ξ'/ξ > 0 on Re s > 1` is free;
all RH content is pushing positivity from `Re s>1` down to `Re s>1/2`.

These are **exact reformulations, not a proof.** The whole program is the search for an *independent,
non-circular, mutation-sensitive* structural theorem that discharges one of them.

---

## Where the program stands (the one wall)

Every lineage, from different directions, has converged on the **same** obstruction:

> The local, per-prime objects can be made exactly positive (the repaired Euler prime tower
> `D_p(t)=M_p|t|−h_p(t)` is CND with an explicit positive Lévy measure; the local source filter `B_p` is
> an exact carry-response resolvent). **But the required local corrections diverge when summed**
> (`Σ_p M_p = ∞`), and the only thing that renormalizes them is the Archimedean completion. No current
> theorem performs that **global prime–Archimedean cancellation while preserving positivity**. That — not
> prime density, not a continuum limit, not Gaussian behaviour — is the RH gap.

In Round-006 passivity coordinates the same wall reads:

```
RH  ⟺  ∃ a positive-definite ARITHMETIC state metric with Euler-region limit Cayley[ξ'/ξ]
     ⟺  Re{ξ(s)/ξ(s+1)} ≥ 0 on H_{1/2}.
```

Rounds 004–006 proved this is the *whole* content (see the Schur–Vitali reduction below) and then closed
every natural route to it: the one-port/direct-sum class, the impedance/Laplace completion (an
unconditional obstruction theorem), the fixed-index Krein escape, and — via a parent-independence lemma —
the colligation and history-before-quotient escapes. What survives is a single, named, open door.

---

## The seam (where a real proof would enter)

The surviving open class, pointed to independently by the Round-006 analysis and the
`unit-place-transport` thread, is the **unit-basepoint place-character jet Gram**:

- The critical half-density weight `p^{−k/2} log p` is exactly the **first jet** at `z=0` of the
  1/2-twisted adelic character `χ^{(1/2)}_{v,z}(x)=|x|_v^{1/2+z}`.
- The product formula `∏_v |x|_v^{1/2}=1` makes the half-density **globally balanced**, so the critical
  line is the *global unit deformation direction* — this is the adelic "why 1/2."
- The **cross-prime coupling** that primewise-independent constructions discard lives in the **second
  jets**: `0=(Σ_v log|x|_v)² = Σ_v (log|x|_v)² + 2 Σ_{v<w} log|x|_v log|x|_w`.

The seam is to build the global coupled object from this 1/2-twisted family **at the unit basepoint**, so
that the divergent first-jet corrections cancel **by the product-formula identity before** positivity is
formed (not local positive blocks minus a divergent counterterm, which is proven to fail), yielding a
second-jet Gram whose kernel is exactly `K_Ψ`. This is the **UBRPCT** (Unit-Basepoint Renormalized
Place-Coupling Theorem) — a **proposed architecture, UNVERIFIED**, equivalent in difficulty to RH but
orthogonal to the single-space de Branges positivity that Conrey–Li/Sarnak proved fails for ζ.

Full statement and the honest gap: `research/aletheia_2026-10-05/CURRENT_MISSING_THEOREM.md`,
`PLACE_CHARACTER_UNIT_BASEPOINT.md`, `CND_PROOF_SEAM.md`, and `research/claude_round_006/PROOF_ATTEMPT_006.md`.

---

## Start here

1. **[CLAIM_LEDGER.md](CLAIM_LEDGER.md)** — every claim with status (DISCLOSED / CORROBORATED / OBSERVED /
   CONJECTURED / UNVERIFIED / REFUTED). Rows C01–C111. The spine of the repo.
2. **[CURRENT_STATE.md](CURRENT_STATE.md)** — governing frame.
3. **[docs/SCREW_SINC_LEVY_UNIFICATION.md](docs/SCREW_SINC_LEVY_UNIFICATION.md)** — the Suzuki
   screw-kernel / sinc / Lévy attack surface.
4. **[docs/NEGATIVE_CONTROLS.md](docs/NEGATIVE_CONTROLS.md)** — attractive dead ends already failed.
5. **[research/claude_round_006/ROUND_RESULT.md](research/claude_round_006/ROUND_RESULT.md)** — the
   current frontier (source port / passivity) and the living CURRENT WALL.

---

## The research arc (by lineage)

**astra** — the CND / infinite-divisibility / transport attack.
`research/astra_round_001..003/`: finite-event rigidity; the geometric-prime Gaussian residual is not a
characteristic function; prime-transport martingale and complexity-crest controls. Verdict each round: RH
open, with the wall localized to global renormalized coupling.

**aletheia** — the adelic / affine / place-character structure.
`research/aletheia_2026-10-05/` and `_2026-10-06/`: the SUCC/FUCC affine-braid and KMS structure
(`SUCC_FUCC_AFFINE_KMS_THEOREM.md`), the repaired prime tower and adelic radical
(`ADELIC_RADICAL_TOWER_REPAIR.md`), the **unit-basepoint place-character frame** (the seam, above),
`FUCC_IS_PASCAL.md` (FUCC = Pascal translation; `B` factors into binomial propagation), the
`PSD_BOUNDARY_CONTINUITY_AUDIT.md` (the C84 correction: the finite reduced kernel is strictly PD; the
knife-edge is an asymptotic shrinking window), and the Round-006 source-wiring handoff.

**claude** — the operator-algebra / passivity attack.
- `research/claude_round_004/` — meta-theorem (commutative-multiplicative ⇒ factorized ⇒ RH-inert),
  exact local operator squares, four no-gos; the irreducible core is SUCC's irregular log-steps.
- `research/claude_round_005/` — the self-sieving carry machine: `B_p` as a literal carry filter, von
  Mangoldt as the carré-du-champ of carry curvature, carry = Cuntz/affine braid; shared-DC telescoping
  refuted.
- `research/claude_round_006/` — **the source port / passivity round.** Highlights:
  - `SCHUR_VITALI_LIMIT.md` (C104) — the round's clean positive theorem: a *non-circular* reduction of RH
    to one hypothesis (P) — a finite family contractive on all of `H_{1/2}` converging to `Cayley[ξ'/ξ]`
    only on the safe Euler region `Re s>1` forces RH, via normal-family compactness ("take the limit").
  - `ARCHIMEDEAN_SOURCE_PORT.md` (C105) — the port = a passive Γ-channel (resolvent of `2N`, poles at the
    trivial zeros) + a single `κ=1` pole at `s=1`.
  - `FINITE_COMPLETION.md` + `PROOF_ATTEMPT_006.md` — the **obstruction theorem**: the impedance/
    Laplace-source completion is not passive (`inf Re F_P → −∞`; Pontryagin index unbounded), killing that
    class unconditionally and closing the fixed-index Krein escape.
  - `PASSIVE_COLLIGATION.md` + `HISTORY_SPACE_SOURCE_PORT.md` (C107–C108) — the parent-independence lemma:
    the obstruction is a property of the function `ξ` (`Re{ξ(s)/ξ(s+1)}<0` in the strip; Conrey–Li/Sarnak),
    so no coupling order or history lift dodges it.

---

## Discipline (non-negotiable)

- **RH is open.** No file asserts otherwise without a complete proof that survives hostile audit.
- Every claim lands in `CLAIM_LEDGER.md` with an explicit status and a reproduction pointer.
- Every candidate construction faces **hostile controls** (delete/insert a prime, wrong `log p` charge,
  wrong half-density `p^{−1/2}`, remove/perturb the Archimedean boundary, random periods). A construction
  that survives fake arithmetic is RH-inert. See `research/claude_round_006/HOSTILE_CONTROLS.md`.
- **No zeta-zero ordinates are ever used as construction input** — only as after-the-fact diagnostics.
- Scripts under `scripts/` reproduce the exact identities and the measured no-gos (`numpy`, `mpmath`,
  `sympy`, `scipy`; see `requirements.txt`).

---

## One-paragraph conceptual summary

Primality, von Mangoldt, `ζ'/ζ`, and the completion to `ξ'/ξ` all arise cleanly and exactly from an
arithmetic "source": `SUCC` boots a multiplicative source `|1⟩`, prewired prime rays `|1⟩→|p⟩→|p²⟩→…`
intersect the additive worldline exactly at prime powers, and the completed response is `ξ'/ξ`, whose
positive-realness on `Re s>1/2` is RH. The local pieces are exactly positive; the limit mechanism
(Schur–Vitali) is proved and non-circular; the Archimedean port is realized. The one thing missing — and
the thing every lineage here has independently cornered — is the **exact global renormalization that
couples the finite prime places to the Archimedean place and stays positive**, which the unit-basepoint
1/2-twisted place-character second-jet Gram is the leading, still-unproved, candidate to supply.
