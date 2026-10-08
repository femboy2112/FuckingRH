# Round result — causal information conservation, fresh prime digits, and intrinsic carry

**Date:** 2026-10-07
**Branch:** \`research/causal-filtration-energy-2026-10-07\`
**Outcome:** exact finite isometric actualization and source-derived carry cohomology; exact no-go against causal support alone implying Hardy stability. **RH OPEN.**

## User hypothesis

> The wavefront only uses information available at the time of the event; shadow SUCC acts on encountered history, not future possibilities. Doesn't this conserve causality?

Answer: **yes** for information/non-anticipation. The correct mathematical structure is an increasing filtration of available arithmetic data. With a specific fresh-digit Hilbert lift, this can be made an **exact local norm-preserving actualization law**, not merely an analogy.

The inference to RH still requires a completely separate theorem: the completed scalar output/observation, including prime powers, Gamma and pole, must be causal and \(L^2\)-contractive for every Suzuki \(\omega>0\).

## Source-forced exact mathematics

1. **LCM event source:** at \(n\), \(\Lambda(n)=\log L_n-\log L_{n-1}=\log[n/\gcd(n,L_{n-1})]\). No future arithmetic information is used.
2. **Information budget:** the normalized Haar refinement \(J:H_L\to H_{L'}\) is isometric and has exact old/innovation Pythagorean splitting.
3. **Static CRT null:** cyclic SUCC commutes with the old-information projection. No intrinsic curvature from mere CRT filtration.
4. **Encountered wavefront:** \([S,P_{n-1}]=|n\rangle\langle n-1|\). Weighting true prime-power births by \(\sqrt{\Lambda(n)/\sqrt n}\) produces a uniformly bounded operator \(\|D_X\|^2\le2/e\).
5. **Coherent readout wall:** the associated scalar prime signal has coherent mass \(\sum_{p^k\le X}\Lambda(p^k)/\sqrt{p^k}\sim2\sqrt X\). A bounded internal event operator does not imply a uniformly bounded scalar observation.
6. **Fresh-digit isometry:** at \(L\to pL\), the inherited Haar lift \(J\) and orthogonal local Fourier digit \(V_p\) give \(W_{p,\omega}=p^{-\omega}J+\sqrt{1-p^{-2\omega}}V_p\), satisfying \(W^*W=I\). Local innovation probability equals Suzuki's \(1-p^{-2\omega}\).
7. **Carry group extension:** \(0\to C_p\to C_{pL}\to C_L\to0\) splits iff \(p\nmid L\). The carry 2-cocycle \(c_L(a,b)=\lfloor(a+b)/L\rfloor\bmod p\) is cohomologically nontrivial precisely for higher prime-power births. This is classical group-extension arithmetic.
8. **Gauge correction:** rank-one carry in a chosen *global mixed-radix section* is **not intrinsic**. With the local p-adic digit, the SUCC carry commutator has rank \(L/p^{v_p(L)}\). The split/non-split class is the invariant.
9. **Flat distinct-prime squares:** \(W_{pL,q,\omega}W_{L,p,\omega}=W_{qL,p,\omega}W_{L,q,\omega}\) for \(p\ne q\). Pure local digit refinement does not produce cross-prime curvature.

## Executed checks

See \`CAUSAL_FILTRATION_EXECUTION.md\` for exact commands and stdout. Independent local NumPy/Python scripts checked:
- all LCM source identities for \(n\le250\);
- a nontrivial Haar information decomposition;
- 14 prefix commutators;
- weighted source operator norms, event mass up to \(X=10000\);
- 8 mixed-radix isometries with 3 positive \(\omega\) and zero case;
- 10 intrinsic group-extension cocycle/carry controls;
- 7 exact flat distinct-prime refinement squares, each with 3 \(\omega\).

These are finite calibrations of proofs. No GitHub CI, zero-ordinate testing, or infinite RH certificate claimed.

## Prior art and intellectual provenance

- User supplied the no-lookahead wavefront/cubical-information intuition.
- GPT-6 formalized the finite refinements, conditional-expectation energy budget and tested matrices.
- LCM/von-Mangoldt source, cyclic extensions, group cohomology, Haar Fourier modes, isometric shifts, and martingale Pythagoras are classical.
- Earlier repo Round005–006 C100 already identified the SUCC boundary defect/prime dilation source.
- Suzuki 2012 v2 is the external RH/Hardy innerness criterion.
- Per-claim first commits, corrections and execution evidence are registered as PV-2026-013–019 in \`RH_CLAIM_PROVENANCE_LEDGER.md\`.

## Surviving proof-bearing experiment

Find an **independently defined, chronologically adapted observation and storage law** that couples the finite isometric source to the correct signed Gamma/pole completion, producing the actual Suzuki transfer \(\Theta_\omega\) in the Euler-safe domain, and prove it acts contractively on the global causal Hardy space for **every \(\omega>0\)**.

The observation must cancel forbidden scalar composite-product/ratio frequencies without fitting to zeros or postulating the target Weil positivity.

**Proving that missing transfer+passivity theorem would prove RH; none of the finite exact results above does.**
