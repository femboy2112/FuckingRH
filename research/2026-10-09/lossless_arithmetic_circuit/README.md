# The infinite arithmetic circuit

## Lossless transport, completed delay, and the Weil sign

**2026-10-09. Status: proved component identities and scoped obstructions; RH remains open.**

Leah proposed that the archimedean place acts like an ideal superconductor: an indefinitely refined finite arithmetic circuit has a coherent, complete boundary description. This checkpoint gives that proposal a precise mathematical realization. The Gamma factor is a renormalized infinite cascade of causal lossless filters; each prime has an exact half-density feedback filter; their delay differences reproduce the known positive Gamma/prime energy. Their correctly completed total delay gives the full Weil form, with all origin and polar terms restored.

The decisive distinction is what completion does to stored history and to energy. The Gamma cascade requires a divergent advance to recover its nonzero limiting response. The positive energy is a delay *difference*. The Weil form contains an additional prescribed subtraction. Boundary elimination must act on that completed form, including its hidden blocks.

This continues [the reversal-memory-polarization checkpoint](../reversal_memory_polarization/README.md) at `11f9070132c46478fbc6c5de2f8109850ce7d0e7`. Live main Round066 at `344facc9b9eccadcf7fe98af9361b6e7fd3ea737` and the older Round006 passivity work were audited before choosing the new probes. Earlier source, half-density, reversal, energy, and Suzuki tangent results are donors. No new result is claimed merely by renaming them. The local explicit-formula/conductor connection is classical; the new work here is its exact circuit normalization, the completion-order test, and the integrated proof contract.

## Read the proofs

| File | What it establishes |
| --- | --- |
| [GAMMA_CASCADE_AND_DELAY.md](GAMMA_CASCADE_AND_DELAY.md) | An explicit finite lossless cascade, its exact Gamma product, divergent delay normalization, positive dispersion limit with a tail bound, and the Mellin clock conventions. |
| [PRIME_FILTERS_AND_WEIL_DELAY.md](PRIME_FILTERS_AND_WEIL_DELAY.md) | Prime-clock storage, actual local-factor advances, retained mixed histories, full Weil delay identity, and exact finite-place cutoff consistency. |
| [BOUNDARY_RESPONSE_AND_CENTERING.md](BOUNDARY_RESPONSE_AND_CENTERING.md) | Complete transfer with prepared history; dynamic boundary response; exact scalar and pole-block completion corrections; rational sign reversals; actual Gamma/prime matrix checks. |
| [CAUSALITY_PASSIVITY_AND_WEIL.md](CAUSALITY_PASSIVITY_AND_WEIL.md) | A maximal wrong-time-arrow control; the exact Suzuki identification gate; symmetric off-line quartet and connected-source countermodels; corrected passivity claims. |
| [PROVENANCE_AND_CLAIMS.md](PROVENANCE_AND_CLAIMS.md) | Claim states, primary references, inherited dependencies, commands, observed errors, and the scoped audit of Round066. |
| [PROBE_CONTRACT.md](PROBE_CONTRACT.md) | Declared discriminators, dependency cut, adaptive addition, and the result that would actually change the proof frontier. |

## 1. The common local law is conservation of stored history

Use a Laplace variable q, with `exp(-qL)` representing a delay of L. For a prime p, let `r=p^{-1/2}` and `L=log p`. A unitary two-channel update gives the transfer

\[
b_p(q)=\frac{e^{-qL}-r}{1-re^{-qL}}.
\]

Its state and port satisfy `|x_next|^2+|y|^2=|x|^2+|u|^2`. Its impulse contains returns at every `k log p`. In a two-prime cascade the return at `log 6` is present even though the connected prime-power logarithmic source has no mixed-prime event. Keeping that return is compatible with extracting the correct primitive source.

The archimedean stages have decay rates `lambda_j=2j+1/2` and transfers

\[
b_j(q)=\frac{\lambda_j-q}{\lambda_j+q}.
\]

They satisfy the continuous storage identity `d|x|^2/dT=|u|^2-|y|^2`. Thus finite prime clocks and the Gamma stages have the same mathematical conservation law in discrete and continuous realizations. This is a precise part of the proposed analogy.

The scalar filters reproduce the local factors exactly. A joint intertwiner from the repository's full SUCC/Hecke history space into an RH-sufficient positive completed host has not been constructed.

## 2. The Gamma completion requires an infinite change of time origin

For M stages,

\[
B_M(q)=\prod_{j=0}^{M-1}\frac{2j+1/2-q}{2j+1/2+q}.
\]

Every B_M is causal and contractive for `Re q>0`, with unit boundary modulus. Nevertheless

\[
B_M(q)\longrightarrow0\quad (\Re q>0),
\]

while the desired nonzero archimedean response is

\[
\boxed{
\left(\frac M\pi\right)^q B_M(q)
\longrightarrow
\rho_\infty(1/2+q)
=\pi^{-q}\frac{\Gamma(1/4+q/2)}{\Gamma(1/4-q/2)}.
}
\]

Both limits are locally uniform on the stated right half-plane. The normalizing factor is an advance by `log(M/pi)`, which diverges. It preserves modulus on the boundary but not a uniform causal Schur bound. No fixed finite delay makes this particular Gamma ratio bounded on that half-plane.

This is a real infinite-circuit phenomenon: every finite stage can preserve norm and have positive storage while the completed response needs a normalization that changes its causal class. The exact archimedean Fourier/inversion operator is unitary and two-sided in log time. Bilateral history is mathematically coherent; its conversion into a specified causal source requires an additional theorem.

## 3. The positive component is the delay drop

Define group delay by `tau(u)=-d arg b(iu)/du`. Then

\[
\tau_M(u)=\sum_{j<M}\frac{2\lambda_j}{\lambda_j^2+u^2},
\quad
\tau_\Gamma(u)=\log\pi-\Re\psi(1/4+iu/2),
\]

and

\[
\boxed{
\tau_M(0)-\tau_M(u)\uparrow
\alpha(u)=\Re\psi(1/4+iu/2)-\psi(1/4)\ge0.
}
\]

This is the exact Gamma energy multiplier already used in the previous checkpoint, now obtained as a finite-circuit dispersion difference. It survives every constant time shift. The prime filter has the corresponding delay drop

\[
\epsilon_p(u)=2\log p\sum_{k\ge1}p^{-k/2}
(1-\cos(ku\log p))\ge0.
\]

These signs are proved from the actual filters. They also survive changes of local weights or addition of a fictitious clock, so they do not by themselves enforce the arithmetic source.

## 4. The full Weil form is the completed delay pairing

For `f in C_c^infinity(-A,A)`, take a finite set of primes P containing every prime at most `exp(2A)`. Set

\[
U_P(q)=\rho_\infty(1/2+q)\prod_{p\in P}\rho_p(1/2+q),
\quad \tau_P(u)=-\frac d{du}\arg U_P(iu),
\]

where the genuine prime ratio is `rho_p(1/2+q)=exp(q log p)b_p(q)`. With
`C(f)=int cosh(t/2)f(t)dt` and `S(f)=int sinh(t/2)f(t)dt`,

\[
\boxed{
Q_W(f)=2(|C(f)|^2-|S(f)|^2)
-\frac1{2\pi}\int_{\mathbb R}\tau_P(u)|\widehat f(u)|^2\,du.
}
\]

This includes the Gamma origin constant, all prime powers visible to the test, and both polar channels. The prime cascades include complete towers. Their excess above the support threshold contributes the same scalar to positive storage and to its counterterm, so it cancels exactly.

Equivalently,

\[
Q_W=P_P-D_P,
\quad P_P=E_\Gamma+E_P+2|C|^2,
\quad D_P=(\log\pi-\psi(1/4)+2M_P)\|f\|^2+2|S|^2,
\]

where `M_P=sum_{p in P} log p/(sqrt p-1)`. Both brackets are positive; their domination is the open sign statement. On the primitive core `C=S=0`, the target is a nonnegative *averaged negative delay*, with the exponential-moment constraints enforced.

For a fixed compact test, adding higher primes changes P_P and D_P by an identical positive scalar. The full pairing stabilizes exactly while both uncentered terms diverge. This is the rigorous replacement for an unspecified infinite prime current of finite norm.

## 5. Closing the circuit has an order that can change the answer

For a block storage matrix `P=[[A,B],[B*,C]]`, define its boundary reduction `S(P)=A-BC^{-1}B*`. When `C>kappa I` and `kappa>=0`,

\[
\boxed{
\mathfrak S(P-\kappa I)
=\mathfrak S(P)-\kappa I
-\kappa B(C-\kappa I)^{-1}C^{-1}B^*.
}
\]

Reducing the positive circuit first omits the last, nonnegative correction. For the exact positive two-node family

\[
P_N=\begin{pmatrix}N+7/4&-1\\-1&N+2\end{pmatrix},
\qquad D_N=(N+1)I,
\]

the incorrect order gives `3/4-1/(N+2)>0` at every cutoff. The correct centered boundary value is `-1/4` at every cutoff. This is a counterexample to a proposed inference, not to RH. Scalar-plus-rank-one controls show that the polar correction must be applied to hidden cross terms too.

In the actual Gamma/prime finite matrices, the omitted correction is substantial at all three horizons tested. Those finite matrices remain positive in the displayed reductions; no continuum sign is inferred.

## 6. The path to Suzuki is now an explicit identification problem

The inherited causal arithmetic distribution k_omega has the shifted-xi transform in its convergence half-plane and satisfies the proved full tangent

\[
\lim_{\omega\downarrow0}
\frac{\|v\|^2-\|H_{\omega,A}v\|^2}{2\omega}=Q_W(v).
\]

Its unitary boundary phase already exists without RH. A reciprocal all-pass control sends an entire unit-norm causal pulse into negative time, even while preserving norm and reversal. Hence that boundary phase cannot simply be substituted for the specified causal kernel.

A sufficient new theorem would identify the causal arithmetic convolution with a bounded contractive global response for shifts approaching zero. Compression and the existing tangent would then give the full Weil sign. A source-built family of finite conservative systems could supply it if its *normalized* transfers have uniform interior Schur bounds and converge to the actual arithmetic transform in the known half-plane. The Gamma cascade proves why checking only the unnormalized systems is inadequate.

The alternative geometric target is a source-defined positive metric on the correctly centered boundary/history space, with its pairing identified with Q_W. This is the circuit form of the polarization requirement from the previous reversal/duality checkpoint. Its existence remains an RH-sufficient research target, not a strict reduction already achieved.

## 7. What was run

Four portable probe programs and a supplementary 90-digit Gamma control passed. The principal independent spatial/spectral check has residual below `1e-10`, with an explicit Fourier-tail bound and separately reported quadrature estimates. Exact rational controls certify the wrong-order sign reversal, the off-line quartet response, and the maximal wrong-time-arrow leakage. Finite arithmetic checks use no zeta zeros.

The adaptive fake `log 6` filter remains locally lossless but changes the completed pairing from approximately `0.0008295` to `-0.0128807` on the wider test. This is a floating-point source-fidelity diagnostic. The exact change formula and its support threshold are given in the report; it is not a new theorem about all arithmetic mutations.

Commands, dependencies, numerical limits, and the claim ledger are in [PROVENANCE_AND_CLAIMS.md](PROVENANCE_AND_CLAIMS.md). The latest scope audit also corrects the assertions that every composite carries zero source, that a mixed-composite defect is itself an off-line zero, and that an RH-equivalent construction is logically impossible to prove.
