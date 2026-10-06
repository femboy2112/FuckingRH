# Zero clocks, bulk-boundary defect, and the hidden-resonance problem

**Date:** 2026-10-06  
**Status:** exact zero-counting reformulation + hostile correction + spectral target. **RH remains open.**

## 0. Necessary correction

The quantity

\[
N(T)
=
1+\frac{\vartheta(T)}{\pi}+S(T)
\]

does **not** count only critical-line zeros.

It counts **all nontrivial zeros in the critical strip with \(0<\Im\rho\le T\)**, with multiplicity.

Therefore using the generalized inverse of \(N(T)\) as "the next critical-line zero" is circular unless RH is already known.

This correction produces a sharper architecture.

---

## 1. Two zero clocks

Define

\[
N(T)
=
\#\{\rho:\zeta(\rho)=0,\ 0<\Im\rho\le T\}
\]

with multiplicity.

Define separately

\[
N_0(T)
=
\#\{t\in(0,T]:Z(t)=0\}
\]

with multiplicity, where

\[
Z(t)=e^{i\vartheta(t)}\zeta(\tfrac12+it)\in\mathbb R.
\]

Thus:

- \(N(T)\) counts the **bulk/global resonances** in the whole strip;
- \(N_0(T)\) counts the **observable critical-line phase-slip events**.

Plainly,

\[
\boxed{N_0(T)\le N(T).}
\]

And

\[
\boxed{
RH
\iff
N_0(T)=N(T)\ \text{for every }T>0.
}
\]

---

## 2. Hidden-mode defect

Define

\[
\boxed{
D(T):=N(T)-N_0(T).
}
\]

Then \(D(T)\ge0\).

By functional-equation reflection, every off-critical zero

\[
\beta+i\gamma,
\qquad
\beta\ne\frac12,
\]

has a reflected partner

\[
1-\beta+i\gamma.
\]

Therefore, counting multiplicity,

\[
\boxed{
D(T)\in2\mathbb N_0
}
\]

away from bookkeeping conventions at zero ordinates.

So:

\[
\boxed{
RH
\iff
D(T)\equiv0.
}
\]

Interpretation:

\[
\boxed{
D(T)
=
\text{global zero-count winding not realized as critical-line phase slips}.
}
\]

This is the exact version of a "hidden resonance count."

---

## 3. Boundary phase knows about bulk zeros

The Riemann-von Mangoldt formula

\[
N(T)
=
1+\frac{\vartheta(T)}{\pi}+S(T)
\]

uses only boundary-phase data along the critical line / standard contour, yet it counts **all** zeros in the strip.

Thus the arithmetic phase correction \(S(T)\) is not merely local noise on the critical line.

Through the argument principle it contains information about bulk zeros away from that line.

The completed geometry therefore has a genuine bulk-boundary structure:

\[
\boxed{
\text{bulk zeros}
\to
\text{boundary winding}.
}
\]

RH says something stronger:

\[
\boxed{
\text{every unit of bulk winding is realized by an actual boundary crossing}.
}
\]

In the present language, every global resonance must become a physical critical-line phase slip.

---

## 4. Two generalized successor clocks

Let

\[
\gamma_n^{\rm bulk}
=
\inf\{T:N(T)\ge n\}
\]

with heights repeated according to multiplicity.

Let

\[
\gamma_n^{\rm line}
=
\inf\{T:N_0(T)\ge n\}.
\]

Then these define two nonlinear SUCC systems:

\[
\mathcal S_{\rm bulk}:
\gamma_n^{\rm bulk}\mapsto\gamma_{n+1}^{\rm bulk},
\]

\[
\mathcal S_{\rm line}:
\gamma_n^{\rm line}\mapsto\gamma_{n+1}^{\rm line}.
\]

The first exists unconditionally.

The second follows the zeros of Hardy \(Z\).

Then

\[
\boxed{
RH
\iff
\{\gamma_n^{\rm bulk}\}_{n\ge1}
=
\{\gamma_n^{\rm line}\}_{n\ge1}
}
\]

as multisets with multiplicity.

So the correct "zero SUCC" problem is not to invent one successor but to prove the **bulk and boundary successor clocks coincide**.

---

## 5. The free Gamma clock

For sufficiently large \(t\), \(\vartheta(t)\) is monotone increasing.

Define the free clock coordinate

\[
C_0(t)=\frac{\vartheta(t)}{\pi}.
\]

Then ordinary SUCC in clock space pulls back to

\[
\boxed{
\mathcal S_\vartheta(t)
=
C_0^{-1}(C_0(t)+1),
}
\]

equivalently

\[
\vartheta(\mathcal S_\vartheta(t))
=
\vartheta(t)+\pi.
\]

If

\[
\Delta_\vartheta(t)
=
\mathcal S_\vartheta(t)-t,
\]

then exactly

\[
\int_t^{t+\Delta_\vartheta(t)}
\vartheta'(u)\,du
=
\pi.
\]

Hence by the mean-value theorem,

\[
\Delta_\vartheta(t)
=
\frac{\pi}{\vartheta'(\xi_t)}
\]

for some \(\xi_t\) in the interval.

Using

\[
\vartheta'(t)
\sim
\frac12\log\frac{t}{2\pi},
\]

one obtains

\[
\boxed{
\Delta_\vartheta(t)
\sim
\frac{2\pi}{\log(t/2\pi)}.
}
\]

So the Gamma clock is a canonical nonlinear SUCC with the correct smooth mean zero-spacing scale.

Its exact integer ticks are the Gram points.

---

## 6. The actual arithmetic clock is not an ordinary invertible coordinate

Because \(N(T)\) is a staircase, the expression

\[
N^{-1}(N(T)+1)
\]

must be interpreted as a generalized inverse.

Moreover, since \(N\) counts all zeros, not only line zeros, this successor is the **bulk-resonance successor**, not automatically the Hardy-zero successor.

This is precisely where an RH argument can accidentally become circular.

The correct comparison is

\[
\boxed{
\mathcal S_{\rm bulk}
\quad\text{versus}\quad
\mathcal S_{\rm line}.
}
\]

---

## 7. Off-line zeros are hidden bulk charges

An off-line pair at height \(\gamma\)

\[
\beta+i\gamma,
\qquad
1-\beta+i\gamma
\]

increases \(N(T)\) by two when \(T\) passes \(\gamma\).

But unless a critical-line zero also occurs at that height, it does not increase \(N_0(T)\).

So it produces a jump

\[
\boxed{
\Delta D=2
}
\]

in the hidden-mode defect.

The boundary phase must account for that pair through winding even though the real Hardy amplitude does not pass through zero there.

Thus:

\[
\boxed{
\text{off-line zero pair}
=
\text{boundary winding without boundary crossing}.
}
\]

This is an exact topological distinction.

---

## 8. Speiser's theorem gives the corresponding local geometric defect

A classical theorem of Speiser states:

\[
\boxed{
RH
\iff
\zeta'(s)\ne0
\quad
\text{for }0<\Re s<\frac12.
}
\]

So an off-critical zero forces a critical point of the zeta map on the left side of the strip.

Since \(\zeta'(s)=0\) is precisely failure of local conformality, this gives a second geometric signature of hidden bulk modes:

\[
\boxed{
\text{off-line zero}
\Rightarrow
\text{left-half-plane fold/branch critical point of the zeta map}.
}
\]

In path language, the hidden resonance is accompanied by a caustic/fold in the complex SUCC/FUCC response map.

This is much closer to the user's original "off-line zero makes the path geometry fail" intuition than a literal discontinuity.

Speiser does not prove RH; it moves the conjecture to a derivative/nonconformality condition.

---

## 9. Why the phase-lock picture alone is insufficient

The critical-line functional equation always forces

\[
Z(t)\in\mathbb R
\]

whether or not \(D(T)\) is zero.

Thus one can have:

- perfect Gamma carrier phase locking on the real critical line;
- real Hardy signal;
- correct total boundary winding;
- and still have hidden off-line resonances.

The missing theorem is exactly

\[
\boxed{
D(T)=0.
}
\]

Any proposed causal/self-adjoint construction must therefore explain why boundary winding cannot occur without an actual phase-slip crossing.

---

## 10. Spectral-flow target

This suggests a sharper operator goal than simply matching the transfer function.

Construct a self-adjoint path \(A(t)\), canonical from SUCC/FUCC history, such that:

1. its spectral flow through zero equals the argument-principle count \(N(T)\);
2. each crossing corresponds exactly to a zero of Hardy \(Z(t)\).

Then self-adjoint spectral flow would force

\[
N(T)=N_0(T)
\]

and RH.

Equivalently, one seeks an index theorem converting the global winding count into actual real-axis crossings with no hidden bulk defect.

This is the operator form of

\[
\boxed{
\text{bulk winding}
=
\text{boundary spectral flow}.
}
\]

No such operator is constructed here.

---

## 11. Relation to the trivial-zero/Gamma clock

The free Archimedean sector supplies

\[
C_0(t)=\vartheta(t)/\pi,
\]

while the prime sector supplies the arithmetic phase distortion.

The exact total count is

\[
N(T)
=
1+C_0(T)+S(T).
\]

Thus the global problem can be phrased as:

> Starting from the inverse-SUCC Gamma clock, couple in the prime lightcone so that the resulting **spectral flow** realizes every argument-principle winding quantum as a physical zero crossing.

The trivial zeros are load-bearing because they construct the free clock and local completion.

The nontrivial RH content is the absence of hidden bulk winding after the prime interaction is installed.

---

## 12. House slogans

\[
\boxed{
\text{Gamma gives the clock.}
}
\]

\[
\boxed{
\text{The argument principle counts every resonance.}
}
\]

\[
\boxed{
\text{Hardy }Z\text{ counts the resonances that actually hit the critical path.}
}
\]

\[
\boxed{
RH
=
\text{no hidden winding:
every bulk resonance becomes a boundary phase slip.}
}
\]

And Speiser adds:

\[
\boxed{
\text{a hidden resonance leaves behind a fold in the left-half-plane path geometry.}
}
\]
