# gapid_adelic_balance_tension — A2: the -1 archimedean/2-adic tension, made exact via the product formula

**Label: Computational Observation** (Collatz-level recon, stricter protocol — ceiling CO, NEVER "proved"/Verified Fact).
Frozen Convention A. Single-path. ZERO floats in the hashed bare witness.

bare_sha256: `382bc43726dd209633a60e6c1c45b6b59e83ffffc0f44b1eebaf7248f9b4fb9f`

## Statement
Over the place set S = {2, 3, ∞}, the product formula `∏_v |x|_v = 1` holds **exactly** for
the accelerated-odd-map data:

- the per-window **multiplier** `μ = 3^a / 2^b` (a = odd-steps, b = total 2-adic divisions);
- the **orbit ratio** `n_end / n_0`, from the **exact integer orbit relation**
  `n_end · 2^b = 3^a · n_0 + K` (K an exact integer carry).

With `|x|_2 = 2^{-v2(x)}`, `|x|_3 = 3^{-v3(x)}`, `|x|_∞ = |x|`:
for μ, `v2(μ) = -b`, `v3(μ) = +a`, so `|μ|_2 = 2^b`, `|μ|_3 = 3^{-a}`, `|μ|_∞ = 3^a/2^b`, and
`|μ|_2 · |μ|_3 · |μ|_∞ = 1` **exactly**. Same for `n_end/n_0` over all places.

The **tension** (A2 target): under hypothetical unbounded growth `|n|_∞ → ∞` (archimedean
**repulsion**), the 2-adic side is simultaneously pulled toward the unique fixed point
`-1 = …111` of `U(x) = (3x+1)/2` — the strip identity `v2(U(x)+1) = v2(x+1) − 1` grows
`|n+1|_2 = 2^{-v2(n+1)}` toward the 2-adic value of −1 (2-adic **attraction**). The product
formula **balances these exactly**: the 2-adic deficit toward −1 is compensated by the 3-adic
and archimedean parts. There is **no single-place excess** (verified per window: removing any
one place and multiplying back returns exactly 1), hence **no product-formula obstruction**
excluding unbounded growth. The content is the **exact identity**, not an inequality.

`-1` is the unique fixed point over Z and Z₂ (`U(-1) = -1`) but `2^S ≠ 3^L` for all `S,L ≥ 1`
(gcd(2,3)=1): no integer cycle realizes it — the **virtual** fixed point. The same balance
nonetheless leaves unbounded growth **product-formula-admissible**.

## Exact balance table (headline windows)

| n_0 | a | n_end | b | K | μ = 3^a/2^b | \|μ\|_2 | \|μ\|_3 | \|μ\|_∞ | product |
|----:|--:|------:|--:|--:|:-----------:|:------:|:-------:|:-------:|:-------:|
|  7  | 3 |  13   | 4 | 19 | 27/16 | 16 | 1/27 | 27/16 | **1** |
| 27  | 3 |  47   | 4 | 23 | 27/16 | 16 | 1/27 | 27/16 | **1** |
| 31  | 3 | 107   | 3 | 19 | 27/8  |  8 | 1/27 | 27/8  | **1** |
|  7  | 5 |   1   | 11| 347 | 243/2048 | 2048 | 1/243 | 243/2048 | **1** |

Orbit ratio `n_end/n_0` (n_0=27, a=3): `47/27`, places `{3: 27, 47: 1/47, ∞: 47/27}`, product **1**.
All 12 windows (n_0 ∈ {7,27,31}, a ∈ {1,2,3,5}): orbit relation holds, product = 1, no single-place excess.

## Named gap (MANDATORY) — GAP-ADELIC-BALANCE → GAP-NB-3
**GAP-ADELIC-BALANCE (RED).** The product formula gives an **identity**, not a strict
inequality at any single place; balanced across {2, 3, ∞} it **cannot obstruct unbounded
growth**. It **reduces to GAP-NB-3** (gcd(2,3)=1, PERMANENT): the coprimality of 2 and 3 is
exactly what makes the 2-adic and 3-adic contributions independent, with the archimedean place
absorbing the residue, forcing the product to collapse to 1 with no exploitable excess. This is
precisely why adelic methods (C-0148) **stall**: the embedding Q ↪ A over {2,3,∞} is
balanced / measure-preserving.

This **strengthens** the project's permanent-gap framing and **triangulates**
C-0148 (adelic scoping) ⊕ C-0210 (virtual −1) ⊕ C-0198 (2^k ≠ 3^L).

## Rabbithole flag
**NONE.** Every place-wise quantity examined (multiplier μ, orbit ratio n_end/n_0) is exactly
balanced (product = 1, no single-place excess) across all windows. No genuine excess found.

## Boundary
Exact integer / rational / p-adic-valuation arithmetic; zero floats in the bare witness.
Explanatory structural recon via the product-formula angle, **not** a Collatz claim. The product
formula is an identity (=1), so it constrains but cannot exclude unbounded growth; does not cross
GAP-NB-3. No proof / disproof; no undecidability. Single-path **Computational Observation**.

Files: `gapid_adelic_balance_tension.{json, json.sha256, full.json, md}` in `audit/invlimit/`.
Generator: `tools/recon_scripts/gapid_adelic_balance_tension.py`.
