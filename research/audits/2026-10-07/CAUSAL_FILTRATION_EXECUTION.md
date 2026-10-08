# Execution and provenance — causal filtration and bounded event source

**Date:** 2026-10-07  
**Branch:** \`research/causal-filtration-energy-2026-10-07\`  
**Mathematical derivation:** [CAUSAL_FILTRATION_INFORMATION_ENERGY.md](CAUSAL_FILTRATION_INFORMATION_ENERGY.md)  
**Code:** \`scripts/rh_causal_filtration_checks.py\`  
**Status:** finite exact/machine-control execution; **RH remains OPEN**.

## What was actually executed

The local file \`/mnt/data/rh_causal_filtration_checks.py\` was written and executed in the assistant's isolated container, using

\`\`\`bash
python /mnt/data/rh_causal_filtration_checks.py
\`\`\`

The same source was subsequently committed under \`scripts/rh_causal_filtration_checks.py\` to the branch at commit \`1a74902affb7d525bd8fd7d7b28e146df54b49e6\`. This is **not** a GitHub Actions test execution or peer review.

Actual stdout:

\`\`\`text
PASS: lcm increment is von Mangoldt using only past L and current n (n<=250)
PASS: Haar energy old=2.0, innovation=0.5, new=2.5; cyclic SUCC projection flat
PASS: 14 encountered-event commutators equal the rank-one next-state birth
X=   16: bounded_source_norm²=0.73548490, coherent_readout_at_zero=5.14517119
X=  100: bounded_source_norm²=0.73548490, coherent_readout_at_zero=16.89620134
X= 1000: bounded_source_norm²=0.73548490, coherent_readout_at_zero=60.50775647
X=10000: bounded_source_norm²=0.73548490, coherent_readout_at_zero=197.46605269
PASS: event injection bounded independently of event horizon; coherent readout not
PASS: no-future-data adapted doubling still amplifies to 4096 in 12 steps
ALL 5 CAUSAL-FILTRATION CONTROLS PASS. RH OPEN.
\`\`\`

## What the tests establish and what they don't

- They check the full exact LCM/von-Mangoldt identity at finite \(n\le250\), independently of zeta zeros.
- They verify one finite conditional-expectation Pythagorean norm decomposition and stationary CRT shift commutation.
- They verify rank-one prefix shift commutators at 14 finite event cutoffs.
- They verify matrix-source Gram/weighted-operator norm for small horizons and the boundedness inequality \(\|D_X\|^2\le2/e\) numerically through \(X=10000\).
- They display growth of the scalar coherent readout \(a_X(0)\), **not** a computed norm for Suzuki's completed transfer.
- They verify an explicit causal adaptation that nevertheless amplifies energy.

The infinite/operator statements are proved by elementary identities in the companion note (not by these finite samples). Classical PNT supplies the asymptotic \(\sum w_q\sim2\sqrt X\).

No code has tested, let alone proved, the Suzuki all-\(\omega\) Hardy-innerness condition. Any future claim that this causal source operator proves RH is **unverified and invalid without the independently derived Gamma/pole observation/storage theorem**.

## Origin and priority

- The user supplied the actualization-wavefront/no-lookahead principle in direct conversation on 2026-10-07.
- GPT-6 generated the formal Hilbert/LCM/SUCC derivation and code; first proof note commit \`aff6cc2b85823c5b380797da489404b1279d66df\`, later addenda \`3ee4c686b5e62e3479fe28ec194157b0e7338ef1\` and \`ead21a9f3c76916381154b3277f71845bd3618fe\`.
- The von Mangoldt source through prime-dilated SUCC boundary defects was already known in this repository (Claude Round006 C100). Conditional expectation, unilateral shift, LCM/von Mangoldt, triangular-unitary rigidity, and PNT are classical; this is a precise organizational reexpression, **not a novelty/priority claim**.
- Suzuki's source-support and all-\(\omega\) innerness criteria are cited in the proof note with versioned primary references.


---

## Additional executed finite controls — isometric digit refinement

A second independent local test script \`/mnt/data/rh_fresh_digit_isometry.py\` was executed with

\`\`\`bash
python /mnt/data/rh_fresh_digit_isometry.py
\`\`\`

It checked 8 old modulus/prime pairs \((L,p)\) for \(\omega=0.1,0.5,1.0\). All asserts passed for normalized-Haar \(J^*J=V^*V=I,\ J^*V=0\), the new isometry \(W^*W=I\), inherited SUCC intertwining, the chosen-section rank-one commutator, and its norm formula \(2\sin(\pi/p)\sqrt{1-p^{-2\omega}}\). Representative observed omega-one norm:

\`\`\`text
L= 2, p=2: norm=1.732050808
L= 4, p=2: norm=1.732050808
L= 6, p=2: norm=1.732050808
L= 3, p=3: norm=1.632993162
L= 4, p=3: norm=1.632993162
L= 6, p=3: norm=1.632993162
L= 3, p=5: norm=1.151819157
L= 6, p=5: norm=1.151819157
PASS: exact fresh-digit causal isometry and SUCC carry defect for all tested refinements.
\`\`\`

An additional control at \(\omega=0\) confirmed the carry defect vanishes in every one of these 8 refinements. The durable companion is \`scripts/rh_fresh_digit_isometry.py\` (committed at \`aa4b7d6fe24d25b7bf4b082e6afe2a2ef69d82b0\`).

**Hostile correction:** this rank-one commutator is tied to the *global mixed-radix section*, not a gauge-invariant curvature. See \`INTRINSIC_CARRY_EXTENSION_CLASS.md\`.

## Additional executed finite controls — intrinsic cyclic group extension

A third local script \`/mnt/data/rh_carry_extension_controls.py\` was executed:

\`\`\`bash
python /mnt/data/rh_carry_extension_controls.py
\`\`\`

It checked 10 pairs \((L,p)\) for the associativity/cocycle law, explicit coboundary trivialization when \(p\nmid L\), impossible splitting conditions when \(p\mid L\), and the *local p-adic-digit* isometric refinement and shift-carry support.

Actual observed summary:

\`\`\`text
L= 2, p=3: split=True,  local p-adic carry rank=2, norm=1.41421356
L= 3, p=2: split=True,  local p-adic carry rank=3, norm=1.41421356
L= 4, p=3: split=True,  local p-adic carry rank=4, norm=1.41421356
L= 6, p=5: split=True,  local p-adic carry rank=6, norm=1.05146222
L= 2, p=2: split=False, local p-adic carry rank=1, norm=1.41421356
L= 4, p=2: split=False, local p-adic carry rank=1, norm=1.41421356
L= 6, p=2: split=False, local p-adic carry rank=3, norm=1.41421356
L= 6, p=3: split=False, local p-adic carry rank=2, norm=1.41421356
L=12, p=2: split=False, local p-adic carry rank=3, norm=1.41421356
L=18, p=3: split=False, local p-adic carry rank=2, norm=1.41421356
PASS: exact cocycle class split iff p∤L; local Fourier refinement isometric; carry support/rank verified.
\`\`\`

The durable counterpart \`scripts/rh_carry_extension_controls.py\` was committed at \`b6583b239d75e306ab840043d33481a224a05a00\`.

**Execution scope:** isolated local Python+NumPy finite tests, not GitHub CI; infinite statements follow their elementary proofs in the companion notes, not extrapolation. None proves all-\(\omega\) Hardy innerness. RH OPEN.
