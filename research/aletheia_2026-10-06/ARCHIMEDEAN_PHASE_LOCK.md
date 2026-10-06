# Archimedean phase locking: critical-line zeros as phase slips, and why causality alone is insufficient

**Date:** 2026-10-06  
**Status:** exact critical-line coupling + hostile control + operator target. **RH remains open.**

This note sharpens the trivial-zero causal coupling.

## 1. Functional equation = exact phase lock on the critical line

Let

\[
S_\infty(t)
=
\chi\!\left(\frac12+it\right)
=
e^{-2i\vartheta(t)}.
\]

The functional equation gives

\[
\zeta\!\left(\frac12+it\right)
=
S_\infty(t)
\zeta\!\left(\frac12-it\right).
\]

Because

\[
\zeta\!\left(\frac12-it\right)
=
\overline{\zeta(\frac12+it)},
\]

we obtain

\[
\boxed{
\zeta(\tfrac12+it)
=
e^{-2i\vartheta(t)}
\overline{\zeta(\tfrac12+it)}.
}
\]

Whenever \(\zeta(\frac12+it)\ne0\),

\[
\boxed{
\arg\zeta(\tfrac12+it)
\equiv
-\vartheta(t)
\pmod{\pi}.
}
\]

Thus the arithmetic signal is phase-locked to the inverse-SUCC/Gamma carrier modulo a binary \(\pi\)-phase.

Equivalently,

\[
\boxed{
Z(t)
=
e^{i\vartheta(t)}
\zeta(\tfrac12+it)
\in\mathbb R.
}
\]

Away from zeros the completed state therefore lies in one of two real phase sectors:

\[
\operatorname{sgn}Z(t)\in\{+1,-1\}.
\]

## 2. Critical-line zeros are phase-slip defects

At a zero of \(Z(t)\), the locked phase is undefined.

For an odd-multiplicity zero, \(\operatorname{sgn}Z(t)\) flips:

\[
+ \longleftrightarrow -.
\]

Thus a simple critical-line zero is literally a domain wall / \(\pi\)-phase slip relative to the Gamma carrier.

For even multiplicity, the amplitude touches zero without a sign flip; the phase-slip count must therefore retain multiplicity/winding rather than only the sign.

This gives an exact dynamical interpretation:

\[
\boxed{
\text{Gamma/inverse-SUCC ladder}
\to
\text{carrier phase }\vartheta(t),
}
\]

\[
\boxed{
\text{prime/arithmetic sector}
\to
\text{real locked amplitude }Z(t),
}
\]

\[
\boxed{
\text{critical-line zero}
\to
\text{defect of the phase-locked path}.
}
\]

## 3. Zero counting as carrier phase + phase slips

With the conventional continuous argument,

\[
N(T)
=
1+\frac{\vartheta(T)}{\pi}+S(T),
\qquad
S(T)=\frac1\pi\arg\zeta(\tfrac12+iT).
\]

So the nontrivial-zero count splits into:

\[
\boxed{
\text{smooth carrier winding}
+
\text{arithmetic phase slips}.
}
\]

The carrier winding is generated entirely by the inverse-SUCC Gamma ladder.

This is why Gram points

\[
\vartheta(g_n)=n\pi
\]

are natural clock ticks, but Gram's law is not exact: the arithmetic phase-slip term is load-bearing.

## 4. Hostile control: phase locking DOES NOT imply RH

The functional equation gives the phase-lock identity for every real \(t\) whether or not off-critical zeros exist.

Therefore

\[
\boxed{
Z(t)\in\mathbb R
}
\]

and unit-modulus Archimedean scattering on the real critical line are both **RH-inert**.

An off-line quartet can coexist with perfect phase locking of the real-line trace.

So the argument

> "the completed signal is real/unitary on the critical line, therefore every zero lies there"

is invalid.

This is the critical distinction between:

- **real-axis scattering data**, and
- **location of resonances/eigenvalues in the complex spectral plane**.

## 5. Stronger hostile control: causality permits off-axis resonances

The completed causal-history distribution from the companion trivial-zero causal-coupling note has a transfer function whose poles are the nontrivial zeros.

But in ordinary causal/scattering theory, stable or unitary real-axis scattering can still possess complex resonance poles away from the physical axis.

Therefore:

\[
\boxed{
\text{causality + unitary real-axis scattering}
\not\Rightarrow
RH.
}
\]

This kills the naive "Cherenkov/cause-cone forbids off-line zeros" proof architecture in its raw transfer-function form.

To force RH, the zero ordinates must arise as something stronger than generic resonances.

## 6. What would be strong enough: actual self-adjoint spectrum

If one could construct a self-adjoint operator \(H\), independently of the zeros, with

\[
\operatorname{Spec}(H)
=
\{\gamma:\xi(\tfrac12+i\gamma)=0\},
\]

then its spectrum would be real and RH would follow.

The present work gives an explicit **free Archimedean channel**

\[
H_0|m\rangle=(2m+\tfrac12)|m\rangle
\]

and an explicit prime causal interaction measure.

What is missing is the interacting self-adjoint operator.

In the current language:

\[
\boxed{
\text{upgrade the nontrivial zeros from transfer resonances to eigenmodes of a natural completed history operator.}
}
\]

## 7. Spectral-shift formulation

The exact zero count suggests a scattering-theoretic decomposition.

Define the smooth/free counting clock

\[
N_0(T)
=
1+\frac{\vartheta(T)}{\pi}.
\]

Then

\[
\boxed{
N(T)-N_0(T)
=
S(T).
}
\]

This has the formal shape of a **spectral shift function**:

\[
\text{interacting density of states}
-
\text{free density of states}
=
\text{scattering phase shift}.
\]

The inverse-SUCC Gamma ladder supplies the free channel; the prime sector supplies the interaction.

A concrete new theorem target is therefore:

> Construct a self-adjoint pair \((H,H_0)\) from the causal SUCC/FUCC history such that the Krein/Birman spectral-shift function is the arithmetic \(S(T)\), and the discrete spectrum of \(H\) is the nontrivial-zero ordinates.

This would make the phase-clock picture proof-bearing rather than diagnostic.

No such pair is constructed here.

## 8. de Branges / canonical-system target

Another precise route is to seek a Hermite–Biehler entire function \(E(z)\), built from the completed causal history rather than from the zeros, whose real part or symmetric combination is

\[
\Xi(z)=\xi(\tfrac12+iz).
\]

For a genuine Hermite–Biehler function,

\[
|E(z)|>|E^\#(z)|
\quad
(\Im z>0)
\]

produces a de Branges Hilbert space and forces the relevant zeros onto the real spectral axis.

In the present language:

- the Gamma/trivial ladder supplies an explicit free phase/canonical-system background;
- the prime lightcone must supply the positive Hamiltonian perturbation;
- the required positivity is precisely the nontrivial step.

This is structurally compatible with the previous Weil/Suzuki wall: one still has to manufacture the positive geometry rather than assume it.

## 9. New conceptual hierarchy

The coupling discovered so far is:

### Level 1 — divisor cancellation

Trivial zeros cancel Gamma poles.

### Level 2 — scattering phase

The same Gamma ladder defines

\[
S_\infty(t)=e^{-2i\vartheta(t)}.
\]

### Level 3 — phase locking

Functional equation forces

\[
e^{i\vartheta(t)}\zeta(\tfrac12+it)\in\mathbb R.
\]

### Level 4 — real-axis defects

Critical-line zeros are phase-slip/domain-wall events.

### Level 5 — missing theorem

Prove that every global completed mode must manifest as one of those real-axis defects rather than as an off-axis resonance.

That final step is RH.

## 10. House interpretation

The trivial zeros are not the boring zeros.

They define the inverse-SUCC local history that creates the **clock**.

The functional equation locks the arithmetic signal to that clock.

The nontrivial zeros on the line are where the locked path has to pass through zero to change phase branch.

An off-line zero would be a hidden resonance of the completed system that does not appear as a physical real-time phase slip.

So the proof-shaped question is:

\[
\boxed{
\text{Why is the completed arithmetic system spectral rather than merely resonant?}
}
\]

Or:

\[
\boxed{
\text{Why must every global resonance become an observable phase-slip on the critical SUCC time axis?}
\]

Causality alone does not answer this. A natural self-adjoint / de Branges / positive canonical-system realization could.
