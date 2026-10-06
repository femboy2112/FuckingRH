# Critical SUCC-lightcone gain: a non-cheating stability probe

**Date:** 2026-10-06  
**Status:** exact zero-free construction + sharp no-go + RH-equivalent stability formulation. **RH remains open.**

This note takes the "off-line zero = SUCC gain/loss" intuition seriously but imposes one rule:

> **No zeta zero may appear in the definition of the dynamics.**

Everything below is built first from the SUCC lightcone:
\(L_N=\operatorname{lcm}(1,\ldots,N)\), its prime-power refinements, the continuous exponential reference scale,
and the known Archimedean completion. Zeros enter only afterward, through the explicit formula, as a spectral
diagnostic.

---

## 1. Bare causal history evolution is automatically stable — and therefore RH-inert

Let \(q_1<q_2<\cdots\) be the prime powers and let \(r_j\) be the underlying prime of \(q_j\).

At the \(j\)-th refinement event define

\[
\mathcal H_j
=
\bigotimes_{i\le j}\mathbb C^{r_i}.
\]

Let

\[
u_r
=
\frac1{\sqrt r}(1,\ldots,1)
\in\mathbb C^r
\]

and define the causal refinement embedding

\[
J_j(v)=v\otimes u_{r_j}.
\]

Then

\[
\boxed{J_j^*J_j=I.}
\]

Hence every finite evolution

\[
J_{j\leftarrow i}
=
J_j\cdots J_{i+1}
\]

is an isometry.

This holds for **every possible radix schedule**, not only the prime-power schedule.

Therefore:

\[
\boxed{
\text{bare causality + normalized branching cannot imply RH.}
}
\]

Any argument saying "the lightcone evolution is norm-preserving, therefore off-line zeros are impossible"
is cheating: the norm-preserving property does not see the arithmetic placement of the events.

The RH-sensitive object must compare the arithmetic refinement clock with an independently defined reference clock.

---

## 2. Two canonical resolutions

The arithmetic lightcone has

\[
L_N
=
\operatorname{lcm}(1,\ldots,N)
\]

distinguishable cells, so its spatial resolution is

\[
\boxed{
\delta_{\rm ar}(N)=L_N^{-1}=e^{-\psi(N)}.
}
\]

Independently, continuous SUCC \(t\mapsto t+1\) becomes multiplicative scaling by \(e\) under the exponential map.
Thus the canonical continuous-SUCC reference resolution after \(N\) unit ticks is

\[
\boxed{
\delta_{\rm vac}(N)=e^{-N}.
}
\]

No prime information is used in this reference clock.

The square-root relative volume/gain is therefore

\[
\boxed{
G_N
:=
\sqrt{\frac{\delta_{\rm vac}(N)}{\delta_{\rm ar}(N)}}
=
\sqrt{\frac{L_N}{e^N}}
=
\exp\!\left(\frac{\psi(N)-N}{2}\right).
}
\]

This is the **critical lightcone gain cocycle**.

It compares two independently defined geometries:

- actual arithmetic branching;
- continuous exponential SUCC/FUCC conversion.

---

## 3. Exact local gain law: prime impulses versus vacuum damping

Set \(L_0=1\) and

\[
b_N:=\frac{L_N}{L_{N-1}}.
\]

Then

\[
b_N=e^{\Lambda(N)}
=
\begin{cases}
p,&N=p^k,\\
1,&\text{otherwise}.
\end{cases}
\]

Therefore

\[
\boxed{
\frac{G_N}{G_{N-1}}
=
g_N
=
\sqrt{\frac{b_N}{e}}
=
\exp\!\left(\frac{\Lambda(N)-1}{2}\right).
}
\]

So every SUCC tick contains a canonical signed logarithmic impulse

\[
\boxed{
a_N:=2\log g_N=\Lambda(N)-1.
}
\]

Interpretation:

- **vacuum/reference demand:** every SUCC tick asks for \(1\) nat of continuum refinement;
- **arithmetic supply:** a prime-power event supplies \(\log p\) nats;
- **non-event:** supplies \(0\), hence a \(-1\) nat deficit relative to the reference;
- cumulative log gain:

\[
\boxed{
2\log G_N
=
\sum_{n\le N}a_n
=
\psi(N)-N.
}
\]

This realizes the user's qualitative picture exactly:

\[
\boxed{
\text{prime-power pulses}
\quad\text{vs}\quad
\text{continuous-vacuum damping}.
}
\]

Caveat: the \(p=2\) event has \(\log2<1\), so it is still a net deficit relative to the \(e\)-per-tick reference.
The "impulse" is positive compared with a non-event, not necessarily positive compared with the continuum rate.

---

## 4. PNT = zero Lyapunov exponent of the gain cocycle

The prime number theorem is

\[
\psi(N)=N+o(N).
\]

Hence

\[
\boxed{
\frac1N\log G_N\to0.
}
\]

So the actual arithmetic refinement and the continuous \(e\)-reference have the same asymptotic exponential growth rate.

In dynamical language:

\[
\boxed{
\text{PNT} \iff \text{the critical gain cocycle has zero top scalar Lyapunov exponent.}
}
\]

This is a reformulation, not a new proof of PNT.

---

## 5. RH = critical/diffusive-scale bound on cumulative log gain

The classical von-Koch criterion gives

\[
RH
\iff
\psi(N)-N
=
O(\sqrt N\,\log^2N).
\]

Therefore

\[
\boxed{
RH
\iff
\log G_N
=
O(\sqrt N\,\log^2N).
}
\]

Let

\[
N=e^t
\]

and define the critically normalized gain signal

\[
\boxed{
X(t)
:=
e^{-t/2}\,
\log G_{\lfloor e^t\rfloor}.
}
\]

Then

\[
\boxed{
RH
\iff
X(t)=O(t^2).
}
\]

Thus the critical exponent \(1/2\) is precisely the boundary between polynomially tempered and exponentially amplified
log-time gain modes.

Again: this is an RH-equivalent reformulation, not a proof.

---

## 6. Off-line zero => hyperbolic gain/loss mode (diagnostic only)

Only now invoke the classical explicit formula.

A nontrivial zero

\[
\rho=\beta+i\gamma
\]

contributes schematically

\[
-\frac{N^\rho}{\rho}
\]

to \(\psi(N)-N\), with conjugate/symmetric partners.

In logarithmic time \(N=e^t\), after the critical \(e^{-t/2}\) normalization, the mode has envelope

\[
\boxed{
e^{(\beta-1/2)t}e^{i\gamma t}.
}
\]

Thus:

- \(\beta=1/2\): neutral oscillation;
- \(\beta>1/2\): exponentially amplifying critical gain mode;
- reflected partner \(1-\beta\): exponentially attenuating mode.

The functional-equation quartet therefore produces a hyperbolic squeeze with parameter

\[
\alpha=\beta-\frac12.
\]

On RH, \(\alpha=0\) for every nontrivial zero and the zero-side dynamics are purely oscillatory.

This justifies the language

\[
\boxed{
\text{off-line zero}
\Longrightarrow
\text{hyperbolic SUCC-clock gain/loss mode},
}
\]

but it does **not** prove such modes are forbidden.

---

## 7. Exact causal transfer distribution

The local gain increments can be packaged without zeros as the signed arithmetic-vacuum measure

\[
dA(x):=d\psi(x)-dx.
\]

In logarithmic time, apply the critical half-density:

\[
\boxed{
d\eta(t)
=
e^{-t/2}\left(d\psi(e^t)-e^t\,dt\right),
\qquad t\ge0.
}
\]

This is a causal distribution defined purely from primes plus the continuous reference vacuum.

For \(\Re s>1/2\), its Laplace transform is exactly

\[
\boxed{
\mathcal L\eta(s)
=
-\frac{\zeta'}{\zeta}\!\left(\frac12+s\right)
-
\frac1{s-\frac12}.
}
\]

The subtraction removes the pole at \(s=1/2\) coming from the continuum \(x\)-term.

Adding the known Archimedean/Gamma correction gives the completed log-derivative transfer function, whose remaining
nontrivial poles are the shifted zeta zeros.

So the EE/stability analogy can be made literal:

- prime-power impulses = causal input;
- continuum \(dx\) = vacuum/reference subtraction;
- Gamma/pole terms = Archimedean completion;
- nontrivial zeros = poles/resonances of the completed causal transfer function.

The construction itself does not use zero locations.

---

## 8. Suzuki's \(\Psi\) is the integrated causal response

The prime term in Suzuki's RH-equivalent screw function is

\[
-\sum_{\log n\le t}
\frac{\Lambda(n)}{\sqrt n}
(t-\log n).
\]

This is exactly the causal Green response of a twice-integrated prime impulse train:

\[
(t-u)_+
\]

applied to events

\[
u=\log n,\qquad
\text{amplitude } \frac{\Lambda(n)}{\sqrt n}.
\]

The remaining explicit terms are the Archimedean/pole completion.

Therefore the SUCC-lightcone language does not produce a new RH criterion here; it recovers Suzuki in dynamical form:

\[
\boxed{
\Psi
=
\text{completed displacement generated by the critical causal gain impulses}.
}
\]

Under RH it decomposes into neutral oscillator energies

\[
\Psi(t)
=
\sum_\gamma
\frac{1-\cos(\gamma t)}{\gamma^2}.
\]

Off-line zeros replace pure rotations by hyperbolic/oscillatory modes.

---

## 9. Why the obvious proof attempt fails without cheating

One might try:

1. causal history evolution is isometric;
2. therefore all modes are neutral;
3. therefore \(\beta=1/2\).

Step 2 is invalid.

The isometric evolution lives in the normalized branching Hilbert space.

The RH-sensitive quantity

\[
G_N
=
e^{(\psi(N)-N)/2}
\]

is a **relative metric/volume cocycle**, not the norm of the branching vacuum.

Causality alone does not bound it.

Indeed, for any integer branching schedule \(r_N\ge1\), the same normalized embeddings

\[
v\mapsto v\otimes r_N^{-1/2}(1,\ldots,1)
\]

are isometric, while the relative gain

\[
\exp\!\left(
\frac12\sum_{n\le N}(\log r_n-1)
\right)
\]

can grow or decay at any prescribed exponential rate.

Therefore:

\[
\boxed{
\text{causality/isometry alone supplies no RH bound on }G_N.
}
\]

The arithmetic placement of the prime-power events — and ultimately the signed Archimedean completion — is load-bearing.

---

## 10. What a genuine proof would now have to establish

The non-cheating theorem target is precise:

Construct, from the causal SUCC/FUCC history geometry **without zeros**, a natural regularity principle that forces

\[
\boxed{
\log G_N
=
O(\sqrt N\,\operatorname{polylog}N),
}
\]

or equivalently forces the completed critical transfer distribution to be tempered in positive Laplace half-plane.

Possible forms of such a principle:

- a canonical martingale-difference structure for the **centered** entropy impulses \(\Lambda(n)-1\);
- a positive/contractive completed transfer operator including the Archimedean sector;
- a natural energy inequality on the lightcone-to-continuum quotient map;
- a Krein/Pontryagin stability theorem in which the pole sector supplies the necessary negative signature but still forbids hyperbolic modes.

Anything that defines the norm using the zeta zeros, assumes the von-Koch bound, or simply postulates power-boundedness is circular.

---

## 11. New geometric interpretation: RH as no superdiffusive coherent gain

The increment sequence

\[
a_n=\Lambda(n)-1
\]

is deterministic, not random.

Nevertheless the critical scale in von Koch is \(\sqrt N\) up to logarithms.

Thus the clean dynamical slogan is

\[
\boxed{
RH
\iff
\text{the integrated entropy-gain error has no coherent mode larger than critical/diffusive scale}.
}
\]

An off-line zero with real part \(\beta>1/2\) creates a coherent contribution of scale

\[
N^\beta
\]

and is therefore **supercritical/superdiffusive** relative to the half-density geometry.

This is more accurate than "faster than light."

---

## 12. Relation to the previous global wall

Rounds 004–006 found:

- local prime carry energies are positive;
- naive positive assembly diverges;
- the missing object is the signed analytic prime/Archimedean cross-term structure.

The present gain cocycle makes that sign visible at the most primitive scalar level:

\[
\boxed{
\Lambda(n)-1
=
\text{arithmetic entropy impulse}
-
\text{continuous vacuum rate}.
}
\]

This subtraction cancels the leading PNT-scale growth, but RH requires the much sharper critical bound.

The Gamma/Archimedean completion supplies the remaining deterministic analytic correction.

So this construction does not bypass the old wall.

It identifies the wall dynamically:

\[
\boxed{
\text{prove critical stability of the completed signed gain cocycle.}
}
\]

That is exactly the same content as Weil/Suzuki positivity when expressed at the completed level.

---

## 13. Honest conclusion

The "off-line zero = SUCC instability" intuition survives a non-cheating derivation in the following precise sense:

\[
\boxed{
\text{off-line zero}
\Rightarrow
\text{exponentially amplifying/attenuating mode of the critically normalized causal gain signal}.
}
\]

What does **not** follow automatically is that the causal lightcone forbids such modes.

The normalized branching Hilbert evolution is always stable and therefore RH-inert.

The actual proof problem has been isolated to a separate, canonical object:

\[
\boxed{
G_N=\exp\!\left(\frac{\psi(N)-N}{2}\right),
}
\]

or its fully completed Gamma-corrected transfer distribution.

A proof must derive critical temperedness/positivity of that object from arithmetic geometry rather than assume it.

### House slogan

\[
\boxed{
\text{The primes supply pulses. The continuum charges one nat per SUCC tick.}
}
\]

\[
\boxed{
\log G_N=\frac12(\text{arithmetic refinement}-\text{vacuum refinement}).
}
\]

\[
\boxed{
RH=\text{no coherent gain mode outruns the critical }1/2\text{ scale}.
}
\]
