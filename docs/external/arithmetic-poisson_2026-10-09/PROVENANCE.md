# Provenance — An arithmetic connection with Poisson completion (external artifact)

**Origin:** supplied by the user 2026-10-09 as five uploads (`CONSTRUCTION.md`,
`FRONTIER_CORRECTIONS.md`, `manifest.json`, `probe_results.json`,
`arithmetic_poisson_connection.py`). Same aletheia 2026-10-09 lineage as the DLEWC
(`../dlewc_2026-10-09/`) and boundary-curvature (`../boundary-curvature_2026-10-09/`) packages;
manifest declares branch `aletheia/arithmetic-poisson-connection-2026-10-09`, parent
`265bf38dfd6af7d5820396f7e80244122a4aa235` (Round 59), delivered as draft PR #8. **Not produced on
`main`.** The two `.md` files here are the *authors'* documents, shipped as-is; this `PROVENANCE.md`
is the repo-side record.

**Status in this repo:** archived for provenance only. Scored in `CRUCIFIXION_LEDGER.md` **Round 62**.

**Execution:** `arithmetic_poisson_connection.py` was **NOT run here** (external-code denial stands).
Every load-bearing claim was re-derived on an independent instrument,
`/tmp/.../scratchpad/independent_verify3.py` (a second blind path; my own Dirichlet-log recurrence,
grid operators, and antiunitary model). Three of my own verifier bugs were caught by calibration
before any reading counted — never a failure of their claim.

**Independent verdict (what reproduced):**
- **No zeros read** (grep + full read): confirmed. Imports `math/cmath/numpy/scipy/sympy/mpmath`;
  every `"zero"` hit is a disclaimer (`"Zero-input probes"`, `zero_data_used: false`,
  `sp.zeros()` = the sympy zero-matrix constructor). No ordinate tables, `loadtxt`/`np.load`,
  network, LMFDB/Odlyzko.
- **Exact source extraction** `b_a = (a\log)*a^{-1}`, `b_χ(n)=χ(n)Λ(n)`, with calibration
  `b_ζ=Λ` (so `b(6)=0`): confirmed on my own recurrence.
- **The 4ab discriminator (sec. 1/3):** `d(6)−d(2)d(3)=[\log D](6)=4ab` for `D=aL(s,χ)+bL(s,χ̄)`,
  `a+b=1`; `[-D'/D](6)=4ab\log 6`; genuine character `→0`. The DH combination `c=(1−iκ)/2` gives
  `4|c|²=1+κ²=1.0807009031`, unifying R60's `κ` and this mixture framing into one number
  (`κ` agrees with R60's `√(1+φ²)−φ` to `1.1e-16`): confirmed.
- **Antiunitary no-go (sec. 4):** `𝒥[C^*,C]𝒥=−[C^*,C]` for `𝒥=parity∘conjugation`; `K=[C^*,C]`
  self-adjoint with mirror-symmetric spectrum (`‖𝒥K𝒥+K‖=1.1e-15`, `λ_min=−λ_max`, `‖K‖≠0`),
  hence PSD iff `K=0` — for **every** coefficient set and shift set. A symmetry-grade upgrade of the
  R61 pulse-lemma: confirmed.
- **Two-prime window (sec. 3):** `‖[T_{\log 2}^*,T_{\log 3}]‖=1` for `\log 3<L<\log 4` while
  `T_{\log 6}=0` there — interaction(2,3) ≠ impulse at 6: confirmed.
- **Non-factorization (sec. 6, FC §3):** `B=V_2+V_3` ⟹ `B^*B=2I+V_2^*V_3+V_3^*V_2`, eigenvalues
  `1,2,2,3`, nonseparable (`|z_2+z_3|²` torus grid rank 2): confirmed.
- **Reflected autocorrelation (FC §5):** `ĝ(i)·conj(ĝ(−i))=−4/e²` vs `|ĝ(i)|²=+4/e²` for `g(u)=u`
  on `[−1,1]`: confirmed (opposite signs).
- **Closed Müntz lift / connection (sec. 9):** the moment-retaining `𝒜` and `∇=−ζ'/ζ` are closed
  operators by the authors' graph-core argument; read as structurally sound (not re-proved here).
  Zero-free; RH-inert for positivity.

**Three corrections to this repo** (from `FRONTIER_CORRECTIONS.md`, all confirmed and **eaten** here):
`wiki/02` bare `Σ|ĝ(γ_ρ)|²` → reflected pairing; `wiki/08` "commutative-multiplicative ⟹ factorized"
→ false (the true direction "factorized ⟹ inert" kept); R59 "three gates **is** the proof" →
necessary-not-sufficient, needs a **fourth gate** (exact identification with the full Weil form + an
independent sign). See Round 62 and `wiki/06` group F (F6).

**Bottom line:** not a brick and not merely a fourth triangulation — an **external audit** that caught
three overclaims in this map, plus a symmetry-grade no-go and the separator unified to one number. The
authors state plainly: *"Not obtained: a positive realization of the completed Weil form. RH remains
open."* The fourth gate is the open theorem. **RH/GRH open.**
