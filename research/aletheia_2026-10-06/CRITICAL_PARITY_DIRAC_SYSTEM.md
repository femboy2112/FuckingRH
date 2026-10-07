# Critical parity/Dirac system: the SUCC/FUCC history compresses to a \(2\times2\) transfer

**Date:** 2026-10-06  
**Status:** exact algebraic reduction of Suzuki's first-order equations; at the critical endpoint this is the natural distributional theorem target. The endpoint passage still requires a rigorous approximation/distribution argument. **RH remains open.**

The individual critical boundary states \(\phi_a^\pm\) are singular, while their parity combinations expose the correct first-order geometry.

---

## 1. Suzuki's regular first-order relation

In the regular range Suzuki obtains

\[
\boxed{
\left(
a\frac{\partial}{\partial a}
+
\frac12
+
\varepsilon\mu(a)
\right)
\phi_a^\varepsilon(x)
=
\delta_x\phi_a^{-\varepsilon}(x),
\qquad
\varepsilon\in\{\pm1\},
}
\]

where

\[
\boxed{
\delta_x
=
x\frac{\partial}{\partial x}
+
\frac12.
}
\]

The coefficient is

\[
\mu(a)
=
a\phi_a^+(a)+a\phi_a^-(a).
\]

At the critical endpoint we have independently reconstructed the **combined** trace

\[
\mu_{1/2}(a)
=
a[\phi_a^+(a)+\phi_a^-(a)]
\]

through the even resolvent and proved

\[
\mu_{1/2}(a)
=
a\,\frac{d}{da}\log m_3(a)
\]

away from conductor seams, with an integrable extension across them.

So the coefficient needed by Suzuki's system is already available without assigning separate divergent boundary values to \(\phi_a^\pm\).

---

## 2. Parity variables

Define

\[
\boxed{
\psi_a
=
\phi_a^+ + \phi_a^-,
}
\]

\[
\boxed{
\chi_a
=
\phi_a^- - \phi_a^+.
}
\]

Then

\[
\phi_a^+
=
\frac{\psi_a-\chi_a}{2},
\qquad
\phi_a^-
=
\frac{\psi_a+\chi_a}{2}.
\]

The sum \(\psi_a\) is the critical even-resolvent combination:

\[
\boxed{
\psi_a
=
2(I-H_a^2)^{-1}h_a.
}
\]

The difference is

\[
\boxed{
\chi_a
=
2H_a(I-H_a^2)^{-1}h_a.
}
\]

Thus \(\psi\) is one half-integration smoother than the problematic individual odd boundary contribution.

---

## 3. Add Suzuki's two chiral equations

For \(\varepsilon=+1\),

\[
\left(
a\partial_a+\frac12+\mu
\right)\phi^+
=
\delta_x\phi^-.
\]

For \(\varepsilon=-1\),

\[
\left(
a\partial_a+\frac12-\mu
\right)\phi^-
=
\delta_x\phi^+.
\]

Adding,

\[
\left(a\partial_a+\frac12\right)
(\phi^++\phi^-)
+
\mu(\phi^+-\phi^-)
=
\delta_x(\phi^++\phi^-).
\]

Since

\[
\phi^+-\phi^-=-\chi,
\]

\[
\boxed{
\left(
a\partial_a+\frac12-\delta_x
\right)\psi
=
\mu\chi.
}
\]

Using

\[
\delta_x=x\partial_x+\frac12,
\]

the half-density constants cancel:

\[
\boxed{
(a\partial_a-x\partial_x)\psi
=
\mu\chi.
}
\]

---

## 4. Subtract the chiral equations

Take the \(\varepsilon=-1\) equation minus the \(\varepsilon=+1\) equation:

\[
\left(a\partial_a+\frac12\right)
(\phi^--\phi^+)
-
\mu(\phi^-+\phi^+)
=
-\delta_x(\phi^--\phi^+).
\]

Hence

\[
\boxed{
\left(
a\partial_a+\frac12+\delta_x
\right)\chi
=
\mu\psi.
}
\]

Therefore

\[
\boxed{
(a\partial_a+x\partial_x+1)\chi
=
\mu\psi.
}
\]

So the regular Suzuki equations are exactly equivalent to

\[
\boxed{
(a\partial_a-x\partial_x)\psi=\mu\chi,
}
\]

\[
\boxed{
(a\partial_a+x\partial_x+1)\chi=\mu\psi.
}
\]

This parity form only uses the **combined** coefficient \(\mu\).

---

# 5. Log coordinates remove the remaining half-density geometry

Put

\[
A=\log a,
\qquad
X=\log x.
\]

Define the doubly half-density-normalized fields

\[
\boxed{
\Psi(A,X)
=
e^{(A+X)/2}
\psi_{e^A}(e^X),
}
\]

\[
\boxed{
\Chi(A,X)
=
e^{(A+X)/2}
\chi_{e^A}(e^X).
}
\]

Because

\[
e^{(A+X)/2}
\left(a\partial_a+\frac12\right)f
=
\partial_A
\left[
e^{(A+X)/2}f
\right],
\]

and similarly

\[
e^{(A+X)/2}
\delta_xf
=
\partial_X
\left[
e^{(A+X)/2}f
\right],
\]

the system becomes

\[
\boxed{
(\partial_A-\partial_X)\Psi
=
\mu(e^A)\Chi,
}
\]

\[
\boxed{
(\partial_A+\partial_X)\Chi
=
\mu(e^A)\Psi.
}
\]

This is a \(1+1\)-dimensional first-order Dirac system.

The characteristic directions are exactly the lightcone directions

\[
A\pm X=\text{constant}.
\]

So the "SUCC lightcone" language is not merely metaphorical after log/half-density normalization: the canonical boundary equations propagate along two null directions.

---

# 6. Fourier/Mellin reduction gives a fixed \(2\times2\) twist matrix

Take Fourier modes in the spatial/logarithmic shadow coordinate:

\[
\Psi(A,X)
=
\widehat\Psi(A,z)e^{izX},
\]

\[
\Chi(A,X)
=
\widehat\Chi(A,z)e^{izX}.
\]

Then

\[
\partial_X\mapsto iz.
\]

Therefore

\[
\boxed{
\partial_A
\begin{pmatrix}
\widehat\Psi\\
\widehat\Chi
\end{pmatrix}
=
\begin{pmatrix}
iz&\mu(e^A)\\
\mu(e^A)&-iz
\end{pmatrix}
\begin{pmatrix}
\widehat\Psi\\
\widehat\Chi
\end{pmatrix}.
}
\]

This is the minimal transfer matrix.

All arithmetic/conductor history is compressed into the single scalar potential

\[
\boxed{
\mu(e^A).
}
\]

At the critical endpoint,

\[
\boxed{
\mu(e^A)
=
\frac{d}{dA}
\log m_3(e^A).
}
\]

Thus the huge growing conductor/Hankel system feeds one time-dependent entry of a \(2\times2\) Dirac transfer.

---

## 7. SUCC conductor events become spikes in the Dirac mass

At

\[
a=\sqrt n,
\]

equivalently

\[
A_n=\frac12\log n,
\]

the critical coefficient has the leading right-hand singularity

\[
\mu(a)
\sim
\frac{
2\varphi(n)
}{
n^{3/4}
}
(a-\sqrt n)^{-1/2}.
\]

Since

\[
a-\sqrt n
\sim
\sqrt n\,(A-A_n),
\]

we obtain

\[
\boxed{
\mu(e^A)
\sim
\frac{
2\varphi(n)
}{
n
}
(A-A_n)^{-1/2}.
}
\]

Thus in canonical log time each new conductor block creates an integrable square-root pulse whose coefficient is

\[
\boxed{
2\frac{\varphi(n)}n
=
2\times
\text{primitive-conductor fraction}.
}
\]

This is an exceptionally concrete causal interpretation of the Dirac potential.

---

# 8. The potential is exactly the derivative of the det_3 gauge

Let

\[
M(A)
=
m_3(e^A).
\]

Then

\[
\boxed{
\mu(e^A)
=
\partial_A\log M(A).
}
\]

Hence the Dirac system is

\[
\boxed{
\partial_A
\begin{pmatrix}
\widehat\Psi\\
\widehat\Chi
\end{pmatrix}
=
\left[
iz\sigma_3
+
(\partial_A\log M)\sigma_1
\right]
\begin{pmatrix}
\widehat\Psi\\
\widehat\Chi
\end{pmatrix},
}
\]

where

\[
\sigma_3=
\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
\sigma_1=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

This is the standard Dirac/supersymmetric shape underlying Suzuki's pair of Schrödinger potentials.

---

## 9. Second-order partners

From the first-order system, after the usual chiral basis/gauge rotation, one obtains partner Schrödinger operators with potentials of the schematic form

\[
\boxed{
V_\pm(A)
=
\mu(A)^2
\pm
\partial_A\mu(A)
}
\]

up to the coordinate convention induced by \(a=e^A\).

This is the same supersymmetric pair appearing in de Branges/Suzuki theory.

At the critical endpoint \(\mu\) has integrable square-root spikes, so

\[
\partial_A\mu
\]

is naturally distributional.

This agrees with Suzuki's expectation that the lower-regularity extension should be understood using distributional potentials.

---

# 10. Why the parity variables are the correct endpoint coordinates

The individual \(\phi^\pm\) contain a logarithmically divergent first odd boundary self-interaction.

The physical combination

\[
\psi=\phi^++\phi^-
\]

removes that term.

The parity system above depends only on:

- \(\psi\);
- \(\chi\);
- the combined finite coefficient \(\mu\).

It never requires the separate divergent values

\[
\phi^+(a),
\qquad
\phi^-(a).
\]

Thus it is much better adapted to the critical endpoint than Suzuki's intermediate chiral presentation.

---

# 11. Distributional endpoint theorem target

The exact algebra shows what must be proved.

### Critical parity-system theorem

For \(\omega=1/2\), the \(L^q\) endpoint solutions satisfy, in distributions on each finite \(a,x\) rectangle,

\[
\boxed{
(a\partial_a-x\partial_x)\psi_a(x)
=
\mu_{1/2}(a)\chi_a(x),
}
\]

\[
\boxed{
(a\partial_a+x\partial_x+1)\chi_a(x)
=
\mu_{1/2}(a)\psi_a(x),
}
\]

where

\[
\mu_{1/2}(a)
=
a\partial_a\log m_3(a).
\]

A rigorous proof can be attacked by:

1. smooth seam cutoffs;
2. Suzuki's differentiation/integration-by-parts algebra on each cutoff system;
3. convergence in the \(L^q\)/distribution topology;
4. the already proved combined-trace and det_3 identities to identify the boundary coefficient.

This theorem would extend Suzuki's key equation (4.20) to the critical endpoint in the variables where all divergent boundary pieces cancel.

---

## 12. Consequence if proved

Fourier/Mellin transforming the distributional parity system immediately gives the \(2\times2\) transfer equation

\[
\partial_A V
=
\begin{pmatrix}
iz&\mu(A)\\
\mu(A)&-iz
\end{pmatrix}
V.
\]

Gauge transformation by

\[
M(A)=\exp\int\mu(A)dA=m_3(e^A)
\]

then yields Suzuki's diagonal positive Hamiltonian

\[
\boxed{
\operatorname{diag}
(M^{-2},M^2).
}
\]

So proving the distributional parity equations is now the shortest route from the critical finite Hankel system to a bona fide endpoint canonical system.

---

## 13. House result

\[
\boxed{
\text{The huge arithmetic state space collapses to one scalar mass }\mu(A).
}
\]

\[
\boxed{
\text{The small twist operator is a }2\times2\text{ Dirac transfer matrix}.
}
\]

\[
\boxed{
\text{The conductor history appears as square-root pulses in }\mu(A).
}
\]

This is the cleanest realization yet of the user's original "growing matrix underneath, tiny matrix performs the twist" intuition.
