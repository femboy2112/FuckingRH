# Adversarial audit of Round 009 — outcome and fixes applied

**RH IS OPEN.** A hostile four-agent audit (one skeptic per pillar + one cross-cutting) re-ran all three
scripts, independently re-derived every load-bearing identity, and grepped for RH overclaim and
zeta-zero leakage. **Verdict: all math correct; no RH overclaim anywhere; no zeta-zero ordinate used as
construction input; scripts run clean; "unusually careful and honest."** One substantive precision fix
(the Pillar-2 "linearization" phrasing) and several attribution / sign / wording fixes were found and
**applied** (same commit). Recorded here for provenance.

## Confirmed by the audit (independently re-derived)

- **Pillar 1:** `b_0'(n)=2Λ(n)/√n`, `b_0^{(ν)}(n)=ν!2^ν∏log p/√n` (re-derived for `n=6,12,30`);
  `dB/dω|_0=−2(ξ'/ξ)(s+½)` (quotient rule + numerics to `~1e-15`); no zeta zeros (ξ, ξ'/ξ evaluated as
  meromorphic functions).
- **Pillar 2:** geodesic-at-`z=0` CORRECT (`σ₁` boost, `i` on the axis, `|w|=1` identically because
  `|num|²=|den|²=\sinh²+\cosh²`; the `z=0` generators all `∝σ₁` hence commute, so the time-ordered flow
  is exactly `exp(τσ₁)`); Dirac dispersion `±√(μ²−z²)` CORRECT; det₃ holonomy `=(2/3)λ³+…` correct; no
  zeta-zero leakage (`m_∞=−Ξ'/Ξ` is only *stated*, never numerically evaluated); Conrey–Li flagged.
- **Pillar 3:** slope-jump `=−Λ(p^k)/p^{k/2}` re-derived (one-sided stencils do not cross the kink);
  on-line `2\cos` PSD vs off-line `4\cosh(r·)\cos` genuinely indefinite (Lorentzian identity) — `r,γ`
  freely chosen, not ordinates; screw-PSD labeled diagnostic.

## Fixes applied (this commit)

- **Pillar 2 — the one substantive fix.** Replaced the loose "the Weil weight is the first-ω-jet
  *linearization / tangent* of the conductor weight `φ(n)/n`" (doc, script docstring+prints, ledger
  C109). `2Λ/√n=b_0'(n)` is the `ω=0` **velocity** and `φ(n)/n=b_{1/2}(n)` is the `ω=1/2` **value** of
  the *same* family `b_ω` — two samples of one flow, **not** a linearization (the `ω=0` tangent
  extrapolated to `ω=1/2` gives `Λ/√n`, neither weight). Rephrased everywhere to the precise statement.
- **Pillar 1 — sign precision.** `−2ξ'/ξ(s+½)` is *not* itself positive-real (negative real part in the
  RHP); led instead with the sign-correct form: RH `⟺` `−Ξ'/Ξ` Herglotz, equivalently `+ξ'/ξ(s+½)`
  (`−½`×velocity) positive-real. Fixed doc §2 and ledger C108; made the script docstring's generator
  `−2(ξ'/ξ)` consistent with the verified identity.
- **Attribution.** Added de Branges 1968 / Krein credit (Pillar 1 doc + ledger C108; the inner-function /
  de Branges-space machinery under `Θ_ω,B_ω`); added the Conrey–Li 2000 flag to Pillar 1 (doc+ledger)
  and the Pillar-3 script CREDIT docstring (its doc+ledger already carried it).
- **GR-register wording.** "actual geodesic flow" → "read as a geodesic flow" (P1); "literal 1+1 Dirac
  dispersion" → "a 1+1 Dirac dispersion (the analogue …)" and "RH ⇔ all modes null" → "in this
  dictionary RH corresponds to all modes null" (P2); "the literal light cone of Lax–Phillips" → "matches
  the light-cone structure of Lax–Phillips" (P3, both occurrences).

## Net

Round 009 stands as pushed: an honest **GR dictionary + the missing joins** over Suzuki's
finite-conductor framework, every arrow credited to prior art (de Branges, Krein, Remling, Suzuki,
Lax–Phillips, Faddeev–Pavlov, Burnol, Sierra, Berry–Keating, Connes, Schoenberg–von Neumann), **Conrey–Li
2000 flagged**, the analogy labeled dictionary-not-mechanism, and RH untouched. The audit changed no
conclusion; it corrected one mislabeled relation, one sign convention, and tightened attribution/wording.

All three scripts re-run clean after the fixes.
