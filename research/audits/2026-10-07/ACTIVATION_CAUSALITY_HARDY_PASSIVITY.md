# Wavefront causality versus Hardy passivity: the activation-only no-go

**Date:** 2026-10-07  
**Branch:** \`research/rh-activation-causality-passivity-2026-10-07\`  
**Claim status:** exact elementary controls, a causal/positive/all-pass obstruction, and a precise new proof test. **RH remains open.**

## Provenance

- **User-origin research hypotheses:** shadow SUCC only acts on already encountered event support; a traveling front only *activates* new arithmetic possibilities; the remaining obstacle seems to be frequency losslessness.
- **This round's derivations:** written by the GPT-6 assistant in response to that hypothesis; no claim of mathematical priority for standard signal-processing/Hilbert/Hardy facts.
- **Primary source:** Masatoshi Suzuki, *A canonical system of differential equations arising from the Riemann zeta-function*, [arXiv:1204.1827v2](https://arxiv.org/html/1204.1827v2), original version-revised date 2016-09-23; §§1.3–1.5, Prop. 1.2, Prop. 2.1 and Thm. 2.2. The original HTML was checked 2026-10-07. In particular equation (1.9) states real-axis unit modulus, (2.3) defines the causal-support kernel, and Thm. 2.2 singles out global \(L^2\) mapping as the nontrivial innerness condition.
- **Secondary source:** Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, [JLMS 108 (2023)](https://doi.org/10.1112/jlms.12785), Thm. 1.7, explicit \(\Psi\ge0\) criterion.
- **Existing repository lineage:** [CAUSAL_HARDY_RH_PROOF_GATES.md](CAUSAL_HARDY_RH_PROOF_GATES.md), earlier finite source / cubical / Gamma work and [RH_CLAIM_PROVENANCE_LEDGER.md](RH_CLAIM_PROVENANCE_LEDGER.md). These were inspected; no previous proof of all-\(\omega\) innerness is claimed.
- **Finite test status:** independent local standard-library/NumPy calculations executed in this session (see test script committed with this note); no GitHub CI run or independent peer review is claimed.

## 1. Source causality was already unconditional

Suzuki defines (his (2.3))

\[
h_\omega(x)
=
x^{-1}\sum_{n\le x}c_\omega(n)g_\omega(n/x)
\quad(x>1),\qquad
\boxed{h_\omega(x)=0\quad(0<x<1).}
\]

This support property is true **for every \(\omega>0\)** without RH.

In additive log time,

\[
k_\omega(t)=e^{t/2}h_\omega(e^t)
\]

satisfies

\[
\boxed{k_\omega(t)=0\quad(t<0).}
\]

For inputs already supported in past multiplicative scales \(x\ge1\), the multiplicative convolution \(h_\omega *_\times f\) cannot have support below \(x=1\).

**This establishes the user's ordinary wavefront/past-only causality claim.** It does **not** say that convolution maps every \(L^2\) input to an \(L^2\) output.

Suzuki's Theorem 2.2 states precisely that the missing global mapping property

\[
\boxed{
h_\omega *_\times f\in L^2(0,\infty)
\quad
\text{for every }f\in L^2(1,\infty)
}
\]

is equivalent to \(\Theta_\omega\) being meromorphic inner. The support condition by itself is insufficient.

## 2. Boundary frequency modulus was already unconditional

Suzuki (1.7) and (1.9):

\[
\Theta_\omega(z)
=
\frac{\xi(\tfrac12-\omega-iz)}
{\xi(\tfrac12+\omega-iz)},
\qquad
\boxed{|\Theta_\omega(t)|=1\ (t\in\mathbb R)}
\]

as a boundary identity wherever the quotient is defined. This follows from \(\xi(1-s)=\xi(s)\) and conjugation, no RH assumption.

Thus of the user's three intuitive checks:

- **causal event support:** already unconditionally true;
- **stable global \(L^2\) transport:** **not** implied by activating support and is the RH-bearing condition;
- **real-frequency all-pass modulus:** already unconditionally true but is not the global input/output isometry until the stable Hardy multiplier exists.

Do not infer (2) from (1) and (3).

## 3. Exact counterexample: a strictly positive forward impulse response can be unstable and all-pass

Fix \(a>0\). The causal impulse measure

\[
h_a(t)=\delta_0(t)+2ae^{at}1_{t\ge0}\,dt
\]

is supported in the future and has **nonnegative** coefficients.

For \(\Re s>a\) its Laplace transfer is

\[
\boxed{
B_{\mathrm{unst}}(s)
=
1+\frac{2a}{s-a}
=
\frac{s+a}{s-a}.
}
\]

On the imaginary axis,

\[
\boxed{|B_{\mathrm{unst}}(i\xi)|=1}
\]

for every real \(\xi\). But \(B_{\mathrm{unst}}\) has a pole at \(s=a>0\) and therefore is not a Schur/Hardy multiplier of \(\Re s>0\).

For any nonzero nonnegative compactly supported input \(u\), its output is

\[
y(t)=u(t)+2a\int_0^t e^{a(t-r)}u(r)\,dr,
\]

which grows exponentially after the input stops. Thus \(y\notin L^2(0,\infty)\).

This one example proves the full logical separation:

\[
\boxed{
\text{future support}
+\text{monotone positive activation}
+\text{boundary all-pass}
\;\not\Rightarrow\;
\text{Hardy stability}.
}
\]

This transfer is a deliberately synthetic causal counterexample, **not** Suzuki's \(\Theta_\omega\).

## 4. The stable all-pass analogue requires signed output feedback

For comparison,

\[
B_{\mathrm{stable}}(s)=\frac{s-a}{s+a}
\]

is a Schur inner function of \(\Re s>0\) and is all-pass on the boundary. Its impulse response is

\[
\delta_0(t)-2ae^{-at}1_{t\ge0}\,dt.
\]

It admits the source-activation state-space realization

\[
\dot x=-ax+u,\qquad y=u-2ax.
\]

For real or complex signals define storage

\[
E(t)=2a|x(t)|^2.
\]

A direct computation yields the exact balance

\[
\boxed{
\frac{dE}{dt}=|u|^2-|y|^2.
}
\]

If \(x(0)=0\), integration gives

\[
\boxed{
\int_0^T|y|^2dt+E(T)
=
\int_0^T|u|^2dt.
}
\]

The **internal state** may be activated by a positive input. But the external output contains a **negative coherent feedback term**.

This is a mathematically precise repair of the "strictly activating wave" intuition: distinguish the monotone/birth **substrate** from its completed **observable**.

The Gamma/pole and cross-place terms of the RH program must be handled as a signed/coherent readout with an independently derived storage law; their positivity cannot be inferred from the mere fact that the arithmetic birth source is positive.

## 5. No-go theorem: positive scalar activation cannot realize nontrivial lossless all-pass transport

**Theorem (classical).** Let \(\mu\) be a finite, nonnegative Borel measure on \([0,\infty)\) of total mass one, and define

\[
F(\xi)=\int_0^\infty e^{-i\xi t}\mu(dt).
\]

If \(|F(\xi)|=1\) for every real \(\xi\), then there is some \(\tau\ge0\) with

\[
\boxed{\mu=\delta_\tau,\qquad F(\xi)=e^{-i\xi\tau}.}
\]

**Proof.** Let \(X,Y\) be independent with law \(\mu\). Then

\[
|F(\xi)|^2
=
\mathbb E e^{-i\xi(X-Y)}
=1
\]

for every real \(\xi\). Hence the characteristic function of \(X-Y\) is identically 1, so \(X-Y=0\) almost surely. Since \(X,Y\) are independent and equal almost surely, their common law must be a point mass. QED.

Thus an activation-only **positive scalar response** can be both normalized and perfectly all-pass only if it is a single deterministic delay. Any nontrivial all-pass memory must have signed/complex-valued scalar impulse response, or else use an enlarged internal state with a signed/coherent observable.

**Scope:** this is a theorem about scalar finite nonnegative impulse measures. It does **not** exclude positive Markov birth processes internally, unitary dilations, matrix-valued state dynamics, or Suzuki's actual signed kernel.

## 6. Markov probability is not the Hardy/L2 energy norm

The finite column-stochastic, activation/coalescence matrix

\[
M=\begin{pmatrix}1&1\\0&0\end{pmatrix}
\]

preserves \(\ell^1\) mass on the probability simplex (both columns sum to one), but

\[
\boxed{\|M\|_{\ell^2\to\ell^2}=\sqrt2>1.}
\]

So even *exact stochastic conservation* does not automatically imply Hilbert-space contraction in the specific \(L^2\) metric needed for Hardy innerness.

The measure/state-space metric matters. It must be derived, not chosen post hoc to make the transfer contractive.

## 7. Raw prime activation bulk is norm-divergent

Let \(T_hf(t)=f(t-h)\) be unitary translations on \(L^2(\mathbb R)\), and let

\[
w_q=\frac{\Lambda(q)}{\sqrt q}.
\]

The naive finite positive-activation shift operator

\[
\mathcal A_X=\sum_{q=p^k\le X}w_q T_{\log q}
\]

has Fourier multiplier

\[
a_X(\xi)=\sum_{q\le X}w_qe^{-i\xi\log q}.
\]

Because all \(w_q\ge0\),

\[
\boxed{
\|\mathcal A_X\|_{2\to2}
=
\sup_\xi|a_X(\xi)|
=
\sum_{q\le X}w_q.
}
\]

By PNT and partial summation,

\[
\boxed{
\|\mathcal A_X\|_{2\to2}\sim2\sqrt X.
}
\]

This is **not** the completed Suzuki transfer; it is a hostile control. It proves that a raw forward activation operator may be perfectly causal and positive, yet grow without bound as the event horizon expands. The signed/pole/Gamma normalization is not optional.

## 8. A concrete passivity proof target (classical energy-storage algebra)

For a finite or suitably regularized state-space model

\[
\dot x=A_\omega x+B_\omega u,\qquad
y=C_\omega x+D_\omega u,
\]

an independently defined positive storage operator \(P_\omega\succeq0\) would give contractivity if the dissipation/KYP inequality held:

\[
\boxed{
\begin{pmatrix}
A_\omega^*P_\omega+P_\omega A_\omega+C_\omega^*C_\omega
&
P_\omega B_\omega+C_\omega^*D_\omega\\
B_\omega^*P_\omega+D_\omega^*C_\omega
&
D_\omega^*D_\omega-I
\end{pmatrix}
\preceq0.
}
\]

This means

\[
\frac{d}{dt}\langle P_\omega x,x\rangle
+\|y\|^2
\le\|u\|^2.
\]

For the RH program the required **noncircular** mathematical tasks are:

1. construct \(A_\omega,B_\omega,C_\omega,D_\omega\) from the genuine prime-power birth, SUCC/carry and Gamma/pole state systems;
2. prove the transfer equals the actual \(\Theta_\omega\) in Suzuki's initially convergent Euler region;
3. derive \(P_\omega\succeq0\) from source-defined state geometry—not by factorizing the desired Weil kernel or assuming Hardy innerness;
4. prove the storage inequality for **every** \(\omega>0\) with correct infinite limits, not only at the safe \(\omega\ge\frac12\) endpoint;
5. retain the exact prime-power-only physical atomic spectrum, forbidding extra mixed-prime product/ratio lines.

If all steps succeeded, Suzuki Proposition 1.2 would prove RH. No such construction is currently available, and naming a KYP inequality is **not** a proof step by itself.

## 9. Research ledger

**EXTERNAL (Suzuki):** source support \(h_\omega(x)=0\) for \(x<1\); \(|\Theta_\omega(t)|=1\) on the real boundary; all-\(\omega\) Hardy innerness and global \(L^2\) convolution mapping are the RH-equivalent gate.

**ELEMENTARY / AUDITED IN THIS ROUND:** causal positive all-pass unstable counterexample; stable signed output with exact storage identity; positive scalar all-pass implies pure delay; stochastic \(\ell^1\) conservation need not give \(\ell^2\) contractivity; raw prime-activation operator has norm \(\sum w_q\sim2\sqrt X\).

**USER-ORIGIN HEURISTIC, NOW CORRECTLY SCOPED:** past-only shadow SUCC is an exact finite source-support property; the activation-only description may apply to internal birth states but must **not** be imposed on the completed scalar transfer.

**RH-EQUIVALENT AND UNPROVED:** existence of a source-forced, completed, all-\(\omega\) causal Hardy contractive transfer realizing \(\Theta_\omega\).

**RH:** OPEN.
