# Passive colligations: corrected hypotheses and the arithmetic construction

**Original checkpoint:** 2026-10-06, ckpt9. **Scope correction:** 2026-10-09. **RH remains open.**

The original version is preserved at [11f9070](https://github.com/femboy2112/FuckingRH/blob/11f9070132c46478fbc6c5de2f8109850ce7d0e7/research/claude_round_006/PASSIVE_COLLIGATION.md), blob `4fa517e8936ce313dd3e2a5fc79f56dab50c6a96`. It contains invalid inferences that this revision withdraws. The tested failures of particular source completions remain useful; they do not establish a universal impossibility of arithmetic passive realization.

## 1. State the whole realization contract

For a unitary discrete colligation on state plus port space,

\[
U=\begin{pmatrix}A&B\\C&D\end{pmatrix},
\qquad S(z)=D+zC(I-zA)^{-1}B,
\]

the transfer is Schur for `|z|<1`. The equivalent resolvent expression `D+C(lambda-A)^{-1}B` uses `z=1/lambda` and is naturally contractive for `|lambda|>1`. A half-plane transfer requires a specified conversion or a continuous energy-balance identity.

Existence of a suitable conservative realization is equivalent to the Schur property; this does not make every chosen realization conservative or every nonminimal hidden state stable. A positive state metric and a dissipative state generator alone also do not control arbitrary port couplings. For example `A=-1`, `B=C=10`, `D=0` gives `100/(p+1)`, which is not Schur on the right half-plane.

The precise classical statement is Ball–Biswas–Fang–ter Horst, [Theorem 1.1](https://arxiv.org/pdf/0705.2042). A direct proof in the port/internal block convention, with the prepared-history term retained, is in [the circuit boundary note](../2026-10-09/lossless_arithmetic_circuit/BOUNDARY_RESPONSE_AND_CENTERING.md).

## 2. The two zeta positivity conditions are different

The standard logarithmic-derivative target is positivity of `Re(xi'/xi)` on `Re s>1/2`. The quantity `Re{xi(s)/xi(s+1)}` is a different shifted-ratio condition and must not be substituted for it. The repository's [literature interface](LITERATURE_INTERFACE.md) and [Schur–Vitali note](SCHUR_VITALI_LIMIT.md) fix the logarithmic-derivative target.

Conrey–Li prove failure of an additional shifted-function positivity condition for the relevant zeta spaces. Their paper separately defines the positive de Branges Hilbert norm. Failure of the extra pairing does **not** make that Hilbert norm indefinite. See [Conrey–Li, Section 2](https://arxiv.org/pdf/math/9812166).

Accordingly, the former claim that the measured negative shifted ratio falsifies the RH-equivalent logarithmic-derivative condition is withdrawn. The former claim that every natural colligation metric is thereby indefinite is also withdrawn.

## 3. What the conditional Schur–Vitali route says

Suppose finite source-defined transfers are analytic and uniformly contractive on the full target half-plane, and converge to the prescribed arithmetic transfer in its known convergence half-plane. The normal-family/uniqueness argument can then give the required analytic contractive continuation. This is the useful conditional statement in C104.

If the existence of such a family is RH-equivalent, that means an unconditional construction would prove RH. It does **not** imply that no unconditional construction can exist. The sentence drawing that impossibility conclusion in the original checkpoint is withdrawn.

The construction has to supply its positive metric, correct port couplings, arithmetic transfer identity, and limit control without assuming the endpoint sign. A bare equivalence, a square root of an unproved positive target, or a unit-modulus boundary function does not supply them.

## 4. Retained negative evidence has a defined scope

The per-prime Laplace one-port `log p/(p^s-1)` is not positive-real on a right half-plane: at `s=sigma+i pi/log p` its real part is negative. The earlier probes also report finite failures of particular Laplace-source completions and negative shifted-ratio values. Those results reject the displayed constructions or extra inequalities.

They do not by themselves prove that every source/history host is impossible, or that a count of negative real-part excursions is a general theorem about every possible realization's negative index. A claimed infinite-dimensional obstruction needs its own kernel, metric, class, and proof.

## 5. The new circuit checkpoint adds an exact normalization test

The Gamma and prime factors admit explicit lossless-filter descriptions, but the Gamma infinite cascade requires a divergent advance and the true local prime ratio removes one clock of delay. Their positive delay drops produce the known positive components of the Weil form. The full pairing includes the source-prescribed centering and both polar channels.

For `P=[[A,B],[B*,C]]`, `C>kappa I`, and `kappa>=0`,

\[
\mathfrak S(P-\kappa I)
=\mathfrak S(P)-\kappa I
-\kappa B(C-\kappa I)^{-1}C^{-1}B^*.
\]

Thus reducing the positive network before centering can give the wrong sign. The new note supplies an exact two-node family with positive incorrect boundary value and correct value `-1/4` at every cutoff, plus actual Gamma/prime matrix diagnostics. A rank-one pole correction must also enter the hidden blocks before elimination.

The open arithmetic task is to construct and identify the correctly completed positive boundary/history object, or prove a bounded contractive causal extension of the specified Suzuki source along a sequence of shifts tending to zero. These are precise remaining proof obligations. They remain available research targets; none is declared solved by local passivity.

See [lossless arithmetic circuit](../2026-10-09/lossless_arithmetic_circuit/README.md), especially its claim ledger and the exact Hardy-leakage control. C107–C108 in the main claim ledger are corrected consistently with this note.
