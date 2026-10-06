# Literature interface: this IS Bost–Connes + Cuntz, and it stops at the Connes/Weil wall

**Round 006. RH IS OPEN.** Honest priority note. The construction of this round is, to ~90%, a
**re-presentation of established frameworks**. This note states exactly which, with primary citations, so
nothing here is mistaken for a new result. (Primary-source scouting by a delegated literature agent; the
one load-bearing computation — the exclude-0 Nica defect — re-verified independently in
`scripts/r006_affine_corner.py` §10c.)

## 1. The multiplicative layer is Bost–Connes — EXACT

**J.-B. Bost, A. Connes,** *Hecke algebras, type III factors and phase transitions with spontaneous
symmetry breaking in number theory*, Selecta Math. **1** (1995) 411–457.

| our object | Bost–Connes object | match |
|---|---|---|
| `H_log|n> = (log n)|n>` | the BC Hamiltonian `H ε_n = (log n) ε_n` | **verbatim** |
| `Tr e^{-βH_log} = Σ n^{-β} = ζ(β)` | BC partition function | **verbatim** |
| `V_p` (and products `V_n`) | BC isometries `μ_p`: `μ_n ε_m = ε_{nm}` | **verbatim** |
| `V_p V_p* =` proj onto `pN` | `μ_n μ_n* =` range proj onto `nℕ` | **verbatim** |
| the source `|1>` | the BC vacuum / multiplicative unit | **verbatim** |

So `H_log = log n` (our `PRIME_JET_STRATIFICATION.md §2`) **is the Bost–Connes Hamiltonian**, full stop. The
only BC feature we do not reproduce is its *additive* part: BC uses the compact group `Q/Z` (roots of unity,
unitary characters `e(r)`), **not** a successor shift. BC has no `S`.

## 2. The additive+multiplicative layer is Cuntz's `Q_ℕ` / the ax+b-semigroup algebra — CLOSE

**J. Cuntz,** *C\*-algebras associated with the ax+b-semigroup over ℕ*, arXiv:math/0611541 (EMS 2008).
**M. Laca, I. Raeburn,** *Phase transition on the Toeplitz algebra of the affine semigroup over the natural
numbers*, Adv. Math. **225** (2010) 643–688, arXiv:0907.3760. **X. Li,** *Semigroup C\*-algebras…*,
J. Funct. Anal. **262** (2012), arXiv:1105.5539.

Cuntz's own one-line description of `Q_ℕ` is *exactly* our construction: *"`Q_ℕ` is obtained from the
algebra considered by Bost and Connes by adding one unitary generator which corresponds to addition."* Our
`S` is that additive generator. The relations match (re-verified §10):

- **Affine braid** `V_p S = S^p V_p` = Laca–Raeburn **(T1)** `v_p s = s^p v_p` = Cuntz `s_n u = u^n s_n`. (This
  is also our Round004 C94 / Round005 C97 irreducible core.)
- **(T3)** `V_p* V_q = V_q V_p*` for `p≠q`. ✓
- The additive range projection `E_S = I − SS* = |1><1|` is Laca–Raeburn's additive boundary projection.

### The one non-standard move: exclude 0

Cuntz/Laca–Raeburn use the **left-regular (Wiener–Hopf) representation** on `l²(ℕ⋊ℕ^×)` with `ℕ ∋ 0`, or the
faithful rep of `Q_ℕ` on `l²(Z)` compressed to `l²({0,1,2,…})` — keeping `0`, the **fixed point** of every
dilation `D_q` on `Q` (`D_q·0 = 0`). **We compress to `l²({1,2,3,…})`, deleting `0`.** Consequence,
re-verified exactly (`§10c`, machine zero for `p=2,3,5,7`):

    ┌──────────────────────────────────────────────────────────────┐
    │   S* V_p − S^{p-1} V_p S*  =  |p−1><1|   (rank one)            │
    └──────────────────────────────────────────────────────────────┘

i.e. the Nica-covariance relation **(T4)** `s* v_p = s^{p-1} v_p s*` **fails by a rank-one boundary term on
`|1>`**. So `(S, V_p)` is a *boundary-perturbation* of the Toeplitz ax+b algebra, not a Nica-covariant
representation of it. In the standard `{0,1,…}` convention `V_p` fixes `|0>`, (T4) holds, and there is no
such defect. This exclude-0 spatial representation, as a boundary-perturbed ax+b rep, we did not find named
in Cuntz/Li/Laca–Raeburn — a genuine but **minor presentational** difference, not a new algebra.

## 3. The adelic half-density is Tate/Connes — EXACT; and it stops at the wall

**A. Connes,** *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*,
Selecta Math. **5** (1999) 29–106, arXiv:math/9811068. **J. Tate,** thesis (1950). **A. Weil,** explicit
formulas (1952).

- Our `p^{-k/2} = |p^k|^{1/2}` local half-density and `∏_v |q|_v = 1` are **Tate's self-dual Haar
  normalization**, verbatim. Connes makes the idele-class action unitary on `L²` via the isometry
  `E(f)(g) = |g|^{1/2} Σ_{q∈k^×} f(qg)` — the exact square-root-of-modulus we rederive in
  `ADELIC_HALF_DENSITY.md`.
- Our local Hardy factor `B_p = (1−z)/(1−p^{-1/2}z)` is a critical-line (`s=1/2`) realization of the local
  Euler factor on `H²` (Burnol/Connes flavor). Standard ingredient. *(Uncertainty flag: we did not find a
  source writing this exact symbol; the `p^{-1/2}` weight is unambiguously the Tate self-dual weight.)*
- **Crucial:** Connes proves the trace formula ⟺ RH (for all Grössencharakter L-functions) via **Weil
  positivity**, but **does not construct an explicit positive operator** realizing it — the global trace
  formula / positivity is left open (math/9811068, Thm 5 is an *equivalence*, not a proof). **Our target —
  a non-circular `B` with `K_Ψ = B*B` — is exactly the gap Connes did not close.** Suzuki's screw function
  (arXiv:1204.1827, 2206.03682, 2301.00421) is the same wall in de Branges–Kreĭn language; `K_Ψ ⪰ 0` **is**
  the Weil positivity criterion. The ongoing Connes–Consani "Weil positivity" program is the same
  equivalence.

## 4. Verdict (four parts, non-diplomatic)

**(a) New, or BC/ax+b?** Not new. It is **Bost–Connes (multiplicative) + an additive generator = Cuntz's
`Q_ℕ` program**, realized as the spatial compression of the `l²(Q)` affine representation. The sole
non-standard element is the **exclude-0** compression (a rank-one boundary variant, not a new object).

**(b) Is "Λ = transported boundary `|1><1|`" new?** **Novel *framing* of a trivial fact.** We found no prior
source writing it this way, but `Σ(log p)|p^k><p^k|` is just the diagonal von Mangoldt operator, and the
transport `V_{p^k}|1><1|V_{p^k}* = |p^k><p^k|` is a one-line consequence of `V_{p^k}|1>=|p^k>` — which holds
*only* because the exclude-0 choice puts the additive boundary on the multiplicative unit. The `log p`
weighting of prime powers is already the geometric side of the Connes–Weil explicit formula. **It is
exposition, not a theorem.** (See the honesty note appended to `VON_MANGOLDT_AS_SUCC_BOUNDARY.md`.)

**(c) Does any framework break the Weil wall?** **No.** Connes 1999, Weil, Suzuki/de Branges–Kreĭn,
Connes–Consani all reduce RH to the identical positivity statement and stop. Our construction reaches the
same wall; the isometry/adelic machinery does **not** supply the missing non-circular `B`.

**(d) What is genuinely not in the literature?** Very little, and nothing load-bearing for RH: the specific
exclude-0 spatial rep that fuses the BC vacuum with the additive floor at `|1>` (and its rank-one Nica
defect `|p−1><1|`), plus the von-Mangoldt packaging — both *presentational*. Everything else (BC Hamiltonian,
`ζ` partition function, the braid, `E_S`, Tate half-density, product formula, Hardy Euler factor, `K_Ψ`
positivity ⟺ RH) is established.

## 5. Uncertainty flags (carried faithfully)

1. The `(T4)`-defect `|p−1><1|` is re-derived and verified here (`§10c`, machine zero) — robust.
2. Exact arXiv numbers for Cuntz–Li *The regular C\*-algebra of an integral domain* and the latest
   Connes–Consani Weil-positivity papers were **not** verified; titles/venues reliable.
3. `B_p = (1−z)/(1−p^{-1/2}z)` not found in exactly that form; identification by content (Tate weight), not
   matched citation. Closest: Burnol, *The explicit formula and the conductor operator*; Connes–Marcolli.
4. The precise ideal-theoretic relation between our `l²({1,2,…})` rep and the Laca–Raeburn
   `l²(ℕ⋊ℕ^×)` Toeplitz algebra is left to a specialist; we are confident they are different reps on
   different spaces and ours is not Nica-covariant.

## 6. What this buys the program

A clean, honest coordinate fix: **we now know exactly where we stand** — inside the Bost–Connes/Cuntz/Connes
circle, at the Connes gap (no explicit positive `B`) = Weil positivity = RH. The round's *new* content is
therefore not a framework but three sharp **structural markers** on that known wall: (i) the exclude-0
boundary as the thing that even makes `Λ` appear (so `Λ` is a compression artifact, `Z`-ablatable); (ii) the
quadratic common-mode divergence of naive intersect-before-squaring (C101), which names the required
signed-wiring; (iii) the explicit identification of the missing object as the Weil cross-term signs. See
`PROOF_ATTEMPT_006.md`.
