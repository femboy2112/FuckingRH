# Research handoff — even Frobenius and reversible dualizing sectors

**Date:** 2026-10-09. **Status:** local theorems/obstructions; RH OPEN. **Branch:** research/2026-10-09/even-frobenius-shadow-reconstruction. **Verified parent:** d8c36e00891ecc60e05fd24013b3f82e4df947e0, itself two commits ahead of main f2fe8b3f2e2953061bcc64c51c86521a66e72bcf at branch creation. No main merge.

## Why this branch exists

The live user proposal is an *axis of investigation*, not an RH proof claim: finite arithmetic SUCC plus its shadow and inverse must be coupled to an Archimedean description by **complete, history-preserving reversal**; a properly constructed Archimedean dualizing/Hodge object could be needed to make the global arithmetic intersection sign. The “shattered teacup” is an analogy about recovering missing correlations, not physical quantum evidence. User-required gates: true multiplicativity, no zero inputs, correct Lambda(p^k), p^(-k/2), log p, reject fake independent n=6, |alpha_2| != 1 and shifted log 2; do not omit the 2,4,8,... tower.

What the assistant supplied is a *new interpretation*: the signed twistor complex-point action has a specifically **even-degree equivariance problem**. Try to repair it with two distinct real structures and a separate spin/Hecke/local-system layer; test exactly where that repair fails. These are not claims the user originally made.

## Verified research heads / conflicts

At the start of this research, main was f2fe8b3 (Round 064). The most relevant branch heads were:
- research/2026-10-09/adelic-reversal-hodge-interface d8c36e0 (our parent): ARCHIMEDEAN_DUALIZING_TWISTOR_HOST and LCM_TATE_TORUS_AND_COVARIANCE.
- aletheia/archimedean-dualizing-reversal-2026-10-09 1790dc9: finite causal nilpotent cannot be made skew-Hermitian by a positive change of metric; formal duality still has off-center spectra; arbitrary unitary dilations remain source-blind.
- research/2026-10-09/history-conditioned-time-reversal 57aec23: Bayes reversals and fresh p-digit half-density; causal shadow-retrodiction is not microscopic reversal.
- research/2026-10-09/hecke-tate-connected-connection e96b48f: the connected Euler/Hecke logarithm gives the correct nonzero source and composite controls.
- aletheia/arithmetic-poisson-connection-2026-10-09 0ef7417: closed source/Muntz connection without an independent Weil sign.
- main's CRUCIFIXION_LEDGER rounds 060–064 and wiki/06 F2–F6 supersede the Round-006-stale CURRENT_STATE.md and CLAIM_LEDGER.md for the active frontier. Identically named claim IDs across remote lineages are NOT reliable global identifiers.

**Important version resolutions:** (a) “No arithmetic Riemann–Roch/Serre duality exists” is false (Connes–Consani 2023/24); the missing RH-bearing theory is a polarized **absolute self-product** with full Weil pairing. (b) formal time reversal/functional-equation symmetry holds for Davenport–Heilbronn too; sign-blind. (c) generic positive Gram/factorized source or causal-history unitary is RH-inert. (d) primitivity/multiplicativity is an exact source discriminator, not a proof that the full form is positive. (e) Hodge-index positivity is independent of Riemann–Roch and duality. (f) the earlier 'commutative-multiplicative implies factorized' slogan was refuted; only certain factorized constructions are inert.

## Delivered findings

1. **Theorem E1:** for monomial covers c z^n between the complex-point real forms j_epsilon(z)=epsilon/conj(z), equivariance holds **iff** epsilon'=epsilon^n and |c|=1. Thus a signed (epsilon=-1) single-sector even-degree endomorphism is impossible; nonunit phases cannot repair it.
2. **Theorem E2:** the two-object (+/-) correspondence closes under the full multiplicative monoid, including the true degree-2 tower, but it is a map **between** real structures, not an endomorphism of the signed Connes–Consani absolute object. A coarse even map erases one orientation bit, recoverable by retaining a source tag.
3. **Theorem E3:** the square-root Jacobian sqrt(n) w^(n-1) lives coherently on z=w² and has deck parity (-1)^(n-1). For even n it does not descend as a scalar. The signed half-spin antiunitary squares to -I, the positive-sector one to +I; there is no nonzero strict linear intertwiner. Exact 8-real-unknown system has rank 8.
4. **Source incompatibility falsifier:** inserting the quartic mod-5 Hecke phase as c_n in c_n z^n gives g3∘g2 phase -1, g2∘g3 phase -i, neither the correct chi(6)=1. The repair is a **separate multiplicative Hecke fiber twist**, with complex characters paired under conjugation, not a monomial point-map phase.
5. **Arithmetical controls:** log_*(chi)(6)=0; log_*(DH)(6)=1+kappa²=1.080700903149283..., fake independent char coefficient +0.03 at n=6 produces a connected +0.03 there. Conductor and Gamma factors have NOT been transported into a new full Weil form by this branch.

These are precise local constructions and no-go results. They are not new analytic estimates for zeta, not the absolute surface, and not RH progress toward an infinite sign bound. There is **no** positive parent or Q=P-K equality built here.

## Executed local probes and honesty about limits

- Python 3.13.5 local container; seeded random trials 20261009; calibration n=1..6; **fresh holdouts** n=7,8,9,10,11,12,15,21,22,25,30. Unphased/phase-unit complex-point covariance residual normalized at most 6.812322634982011e-15.
- Expected signed single-sector failure on 160 even test cases; expected signed odd pass on 180 cases. Exact source-history collision and tagged injection pass for even n=2,4,6,8,10,22.
- SymPy exact antiunitary check: strict spinor intertwiner real matrix system rank 8 in 8 real unknowns, kernel 0.
- Genuine zeta/character log-primitivity passed to n=60; the Davenport–Heilbronn mixture and fake-6 controls failed source admissibility as expected. DH b4=-1.0403504515746413; DH b6=1.080700903149283.
- Initial exploratory 50/50 mixture assertion at n=4 was wrong: its b4 is -1, not -1/2 (the latter is the genuine quartic chi's b4). This was a **harness expectation failure**, corrected, retained as provenance, not hidden.
- Scripts on this branch are reproducing, compact implementations of the executed local scripts, not byte-identical copies. Evidence manifest records actual local stdout-derived values and script hashes. **The committed scripts themselves have not been executed in GitHub Actions**, nor has the entire project's pytest suite been rerun. No source code was published into main.

Useful repeat commands at the branch root:

    python scripts/twistor_even_frobenius_probe.py
    python scripts/twistor_spin_intertwiner_exact.py

The second requires SymPy; the first uses only Python's standard library. See EVEN_FROBENIUS_PROBE_OUTPUTS.json for scope, holdouts, numerical outputs and the exact failed exploratory expectation. The proof note contains all analytic identities so the results do not depend on numerical evidence.

## Fourth gate / exact remaining theorem

Need an **actual graded dualizing correspondence**, source-derived over finite places and infinity, that (i) handles signed/unsigned 2-Frobenius and spin deck memory, (ii) includes compatible Hecke character local systems and actual p^{-k/2} log p, (iii) has trace distribution **exactly** the *complete* prime–Archimedean–polar Weil quadratic form on a specified form domain, and (iv) possesses an **independently proved** Hodge-index-type sign surviving the infinite wavefront limit.

Do not identify complex twistor spin parity with arithmetic half-density or primitive trace without a functor and source calculation. Do not claim unitary recovery from the generic history tag gives Weil positivity. The current two-sector construction is compatible with a fake composite degree-6 *map*; it rejects an independent scalar n=6 *impulse* only when the separate Euler-connected-source constraint is imposed.

## Next discriminating attack, before any positivity claim

Construct and attempt to falsify a **2–3–infinity graded correspondence** with:
- geometric objects X_-, X_+ and maps f_2,f_3 whose composition f_6 is coherent, with deck/spin history retained;
- a Hecke fiber twist carrying chi and its conjugate separately and respecting the *tensor* multiplicative cocycle;
- a source-only trace tested at log 2, log 3, log 4, log 6 and log(3/2). A geometric f_6 is allowed, but its first-order scalar primitive coefficient must be **zero**, and the prime-power weights fixed;
- an independently specified archimedean dualizing distribution checked against the zeroth through third Gamma jets before computing any Weil sign.

Predicted outcomes: a generic naive trace on spin histories will manufacture a forbidden mixed-composite or ratio atom (failure would force a new quotient or graded trace). If all local data match, **do not** promote it to RH until an exact global pairing identification and an independent sign exist. A negative result identifying a concrete forbidden atom or impossible domain can be the next useful no-go; a working source-faithful trace would be new construction-level progress.

**Conclusions graded:** E1–E3, phase-composition no-go are DISCLOSED within the stated complex-point model; local computer checks OBSERVED; proposed global graded dualizing correspondence CONJECTURED; exact full Weil identification and independent Hodge positivity UNVERIFIED; RH OPEN.
