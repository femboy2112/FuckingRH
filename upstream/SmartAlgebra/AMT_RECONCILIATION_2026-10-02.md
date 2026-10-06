# AMT inputs: what this round used, and why the two branches were not merged

**Decision (2026-10-02):** cite and restate; do not import files from either AMT
branch into this branch.

## The two snapshots

| | `research/additive-multiplicative-transport-2026-09-16` | `research/transport/amt-2026-09-16` |
|---|---|---|
| head | `b234fd634e3a5325a115b2f3957d573810eebb12` (7 commits on `a8ca181`) | `86d7d1ab31fd5048205065e73bcfda6c74808a6e` (2 commits on `a8ca181`) |
| unique files | `CORE.md`, `amt.py`, `verify_amt.py`, `verify_extensions.py`, `extensions.json` | `THEORY.md`, `RH_COMPARISON.md`, `PROVENANCE.md`, `PROJECT_INDEX.md`, `verify_transport.py` |
| colliding paths | `README.md` blob `bd03ecf3…`, `verification.json` blob `7494da59…` | `README.md` blob `cf4ae006…`, `verification.json` blob `8b116df7…` |
| recorded verification | 48 043 baseline assertions + 1 495 extension assertions | 13 743 checks (a separate standalone verifier) |

Both put their material under `research/additive_multiplicative_transport/`. The
two `README.md` files describe different directory contents, and the two
`verification.json` files record different runs of different verifiers. A rote
merge would either conflict or silently let one run's receipt stand for the other's.

## What this round needed, and where it is restated

| Used | Source (blob) | Restated in |
|---|---|---|
| Bounded Hermitian comparison theorem (nested dense subspaces, `|W − ‖B_n·‖²| ≤ ε_n‖·‖²`, `ε_n → 0` ⇒ `W ⪰ 0`) and the remark that it certifies nothing unless `B_n` is independent of `W` | `RH_COMPARISON.md` §2–§3 (`e5895222…`) | `RH_BRIDGE.md` §2 |
| Hidden-negative-direction control `W_N` | `RH_COMPARISON.md` §4 | `RH_BRIDGE.md` §4 (E4, executed exactly) |
| Unitary Fourier–Mellin convention `H_σ`, `σ = 1/2` | `RH_COMPARISON.md` §1 | `RH_BRIDGE.md` §2 (convention row) |
| Q2: positive pivot ⇒ PSD iff Schur complement PSD | `CORE.md` §10 (`d305fb5a…`) | `THEOREM.md` §8 (scalar case, with the zero-pivot rule it does not cover) |
| Q1/Q3: quotient positivity ≠ source positivity; dense closure needs continuity | `CORE.md` §10 | `RH_BRIDGE.md` §2 (closability row) |

Not used: the Fibonacci/89 transport, bounded specialization and reflection
(B1–B4), Collatz words, Gauss/Jacobi transport. Nothing from either AMT branch is
imported as code, and no AMT claim is promoted by this round.

## If the AMT material is consolidated later

Keep both snapshots under distinct, commit-named directories (e.g.
`research/amt/core-b234fd6/` and `research/amt/transport-86d7d1a/`), keep each
`verification.json` beside the verifier that produced it, and rerun both verifiers
from the consolidated location before citing either count.
