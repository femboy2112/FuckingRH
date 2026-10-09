# Exact execution verification — 2026-10-09

This supplements the earlier result manifest, which recorded a snapshot BEFORE exact execution. Its previous "not run" field is now superseded by this file.

The committed `scripts/operational_actualization_probe.py` was independently written to the local working container with the same bytes and executed via

```sh
python /mnt/data/operational_actualization_probe.py
```

**Exit status: 0; JSON status: PASS.**

Byte identity is certified by the independently computed local Git object hash matching the GitHub blob SHA fetched from this branch:

```
88d44dccede4a7879caec7542c8f59373f381208
```

Local SHA-256 of executed script:
`409646e844f8c8fcb87b8ba832bfef5b7b02d5322fd1f83f936dfd4c0f959015`.

Local SHA-256 of complete JSON stdout:
`f68f9f2bbe62ccb678dfe15832cc2af914a1536713965b1b836f8206a70b55d2`.

Tests: conductor dimensions and exact-conductor births through N=9; birth formula through conductor d=100 in this script (independent exploratory check to d=200); path histories 2→1→2 and 2→4→2; exact rational mod-2/mod-3 conditional nulls, mixed norm 1/18, and opposite joint expectations ±1/18; convolution-log shadow coefficients at n=4,6,8,9,12; fake-6 source delta=1/7.

No numerical zeros or RH-based positivity assumptions were used. No GitHub Actions run or full repository test-suite run is claimed. The mixed snapshot rivals do not satisfy cyclic-SUCC invariant-distribution constraints. The proof of the global completed Weil sign remains absent.

Next: construct a source-faithful mixed-conductor/Archimedean observation transport and test forbidden n=6 primitive and log(3/2) ratio atoms before attempting a full Weil pairing.
