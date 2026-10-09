# Provenance — Source-faithful arithmetic boundary curvature (external artifact)

**Origin:** supplied by the user 2026-10-09 as an upload
(`rh_source_faithful_euler_operator_2026-10-09.zip`). Same sibling lineage as the DLEWC package
(`../dlewc_2026-10-09/`); the note parents on `main@265bf38` (Round 59) and matches remote branch
`research/2026-10-09/hecke-tate-connected-connection`. **Not produced on `main`.** The `README.md`
beside this file is the *author's* README, shipped inside the zip; this `PROVENANCE.md` is the
repo-side record.

**Status in this repo:** archived for provenance only. Scored in `CRUCIFIXION_LEDGER.md` **Round 61**.

**Execution:** the `scripts/` and `tests/` Python was **NOT run here** (external-code denial stands).
Load-bearing new claims re-derived on an independent instrument:
`/tmp/.../scratchpad/independent_verify2.py`.

**Independent verdict (what reproduced):**
- No zeros read (grep + read): confirmed (`math/numpy/cmath/unittest` only).
- `b(6)=(a(6)−a(2)a(3))log6=(1+κ²)log6=1.9363561` for D-H, `0` for ζ/χ5, via *this note's* recurrence
  (a third independent recurrence agreeing with DLEWC's and the convolution-log): confirmed.
- **`[X, log𝔉]=D`** von Mangoldt-source-as-commutator, discrete `[X,log F_N]=Σ b(n)/√n·V_n` to 1e-15;
  `[X,V_p]=(log p)V_p` exact: confirmed. Elegant, zero-free — but RH-inert for positivity.
- **Boundary commutator** `[T_a*,T_b]` closed form matches a direct grid build to **0.00e+00**
  (exact integer-cell shifts); witnesses `+1`/`−1`; norm `1.0000`: confirmed.
- **PROVED NO-GO (the key result):** positive-step commutator curvature `[B*,B]` is **always
  indefinite** when nonzero — my instrument gives spectrum `±4.68`, left-end witness `>0`,
  right-end `<0` (equal and opposite), exactly the pulse-lemma sign structure. Boundary curvature
  **cannot** be a positive Weil certificate.
- SOS `Q=(P−A_L I)+Σw_n[(I−R_n)*(I−R_n)+(I−R_n*R_n)]=P−K`: verified by hand (exact; bracket PSD iff
  `‖R_n‖≤1`). `P−A_L I` indefinite = this repo's "no archimedean floor."

**Bottom line:** third independent triangulation of the `Q=P−K` coercivity wall, plus a **proved
tombstone** on the most natural gate-3 candidate (mixed-prime boundary curvature). **No brick.
RH/GRH open.** The note itself claims no RH/GRH solution and flags its calibration gate as still owed.
