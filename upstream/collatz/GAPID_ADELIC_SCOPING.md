# Adelic scoping of the GAP-NB avenue — is `𝔸_ℚ` / Tate useful?

**Label: Computational Observation** (exact valuation / product-formula arithmetic; exact
local-factor identities) **/ candidate** (the adelic limiting-zeta identification — Front Z).
Convention A (Frozen), `p=3`, milestone/17.
Witness `audit/invlimit/gapid_adelic_scoping.json`, sha256
`d183909d433e4fbe5742ac0cc83e901a48314be16d25fc5e484e1cf22fae097f`.
**No Collatz claim. GAP-NB-3 Not-Established and PERMANENT.**

---

## The question

The bi-adic saddle (C-0141) lives on `ℤ₂ × ℤ₃`. The natural completion is the adele ring
`𝔸_ℚ = ℝ × ∏′_p ℚ_p` (restricted product). Does the adelic / Tate framing give a genuine new
handle on the avenue — and does it make the C-0146 "identify the limit object with *the* zeta"
step (Front Z) concrete? We test four things exactly and reach a verdict.

## The exact findings

- **(A1) Ramified set = exactly `{2,3}`.** The inverse branch `β_a(x)=(2^a x−1)/3` involves only
  the primes 2 (stable / shift) and 3 (unstable / multiplier); both are units at every other prime
  (`v_p(2)=v_p(3)=0`, `p≥5`). Adelically the operator is **supported at two places** and trivial
  (unramified) everywhere else — adeles add the cofinite trivial places, the honest completion, not
  a new per-place mechanism.
- **(A2) The product formula *is* the coupling.** For every branch quantity `x = 2^a/3` (`a` from
  the certified a0 table) the product formula holds exactly: `|x|_∞ · ∏_p |x|_p = 1`, nontrivial
  only at `{2,3,∞}`. The single integer `a` sets `|x|_2 = 2^{-a}` (the stable rate) **and**, through
  `∏=1`, locks `|x|_3·|x|_∞ = 2^a`. The 2-place and 3-place data of a **global** rational are tied —
  the adelic form of `gcd(2,3)=1` / the C-0144 incommensurate combs.
- **(A3) The certified objects factor by place.** The seed-resolvent geometric `1/(1−ρ)`
  (`ρ=t^{P_r}`) is the `p=2` local factor `L₂` (its finite truncations are the exact geometric
  `(1−ρ^{N+1})/(1−ρ)`; the `J→∞` collapse to `1/(1−ρ)` is the certified C-0145 anchor); the
  cyclotomic `(1−t^{P_r})` is the `p=3` local factor (verified: it divides the certified det-`B`
  denominator at `r=1,2`); the archimedean place is trivial.
- **(A4) No adelic decoupling — permanence, restated.** Over the `{2,3}`-units, a global rational's
  archimedean size is **forced** by its valuations: `|x|_∞ = 2^{v₂}3^{v₃}` — an *equation*, not a
  free choice; no global rational has independently prescribed 2- and 3-adic data. Adeles do **not**
  decouple the places; the diagonal `ℚ ↪ 𝔸_ℚ` / product-formula constraint **is** GAP-NB-3.

## Front Z — the limiting-zeta identification, with an adelic target

The candidate limiting inverse-Collatz zeta is the `{2,3}`-supported product
`Z(t) "=" L_∞ · ∏_p L_p`, with `L₂` the stable geometric and `L₃` the cyclotomic det leg; its
denominator tower `∏_r (1−t^{2·3^r})` is exactly the NB realizer (C-0146), and each `P_r=2·3^r` is
ramified only at `{2,3}`. The Hadamard-gap natural boundary (C-0146) is then the boundary of this
candidate adelic zeta. **GAP-Z** (the open step): identifying this product with *the* dynamical zeta
of inverse-`3x+1` still requires the odometer `=` inverse-Collatz reading — i.e. **exactly GAP-NB-3**.

## Verdict

Adeles are **useful** as **(i)** the natural home / factorization target for the NB limit object —
turning Front Z's vague "*the* zeta" into a concrete `L₂ × L₃` Tate-style target — and **(ii)** a
**fourth independent triangulation** of GAP-NB-3's permanence (the product formula / diagonal
embedding), alongside factorization (C-0141), dilation (C-0142), and the dual (C-0143). They are
**not a bridge**: no adelic mechanism decouples the 2- and 3-places of a global rational — the
constraint that walls the avenue is the same one that defines the adele class group.

## Boundary

The valuations, the product-formula identities, the forced-archimedean equation, and the local-factor
identities are exact rational / `ℚ(t,g)` arithmetic. The identification of the `{2,3}`-local product
with *the* limiting inverse-`3x+1` dynamical zeta (Front Z) is the **candidate** reading, explicitly
not a theorem; it requires the odometer `=` inverse-Collatz step, which is GAP-NB-3. Adeles **restate**
the permanence; they do not bridge it. GAP-NB-3 Not-Established and PERMANENT. Classical inputs (named,
not in the bundle): the adele ring / restricted product, the product formula `∏_v | |_v = 1`, Tate's
thesis (local × global zeta factorization). (CLAUDE.md, Collatz-Level Work Protocol.)

## Pointers

- Generator: `tools/recon_scripts/gapid_adelic_scoping.py` (exact). a0/`period` from
  `tools/spectral.py`; valuations computed directly.
- Ledger: C-0148 (this scoping, CO; the Front-Z identification candidate/Not-Established). Avenue map
  `audit/invlimit/GAP_NB_AVENUE_MAP.md` §4–§5.
