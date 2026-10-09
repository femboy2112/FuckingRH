# Arithmetic solenoid: the lossless global current circuit hiding behind LCM clocks

**Date:** 2026-10-09. **Status:** exact standard adelic/topological/representation-theoretic lemmas, source and RH-sign obstruction distinguished. **RH OPEN.**

## Hypothesis to make precise

The user's analogy is that the finite world at infinite refinement is a coherent recursive circuit carrying prime currents, while the Archimedean place supports a lossless continuous global flow completing that circuit.

The correct mathematical object is the **additive arithmetic solenoid**

\[
\boxed{
\mathcal S_\mathbb Q=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z
\ \cong\ \mathbb A_\mathbb Q/\mathbb Q.
}
\]

It is **NOT** the multiplicative adèle-class quotient \(\mathbb A/\mathbb Q^\times\) of Connes' trace formula, and is not an arithmetic self-product surface. The compactness/duality statements here are classical, not an RH proof.

Sources:
- https://math.mit.edu/~rud/592-siegel/talk4.html (Q discrete/cocompact in A, dense in A_f, product formula);
- https://link.springer.com/chapter/10.1007/978-3-030-56694-4_27 (solenoid identification);
- https://web.stanford.edu/~dkim04/blog/tate-thesis-2/ (Pontryagin dual Q and adelic Poisson).

## 1. SUCC LCM tower directly constructs the finite component

Let

\[
L_N=\operatorname{lcm}(1,\dots,N).
\]

The sequence is cofinal in the divisibility order on positive integers, so

\[
\boxed{
\widehat{\mathbb Z}
=\varprojlim_N\mathbb Z/L_N\mathbb Z.
}
\]

At \(N=p^k\), \(L_N=pL_{N-1}\), and the new reduction \(\mathbb Z/L_N\to\mathbb Z/L_{N-1}\) has p-point fibers. Every other N leaves the clock unchanged.

Introduce the finite suspended clock

\[
\mathcal S_N=(\mathbb R\times\mathbb Z/L_N\mathbb Z)/\mathbb Z
\cong\mathbb R/L_N\mathbb Z.
\]

The isomorphism is \([(t,r)]\mapsto[t-r]_{L_N}\). Each \(\mathcal S_N\) is a real circle of circumference \(L_N\). The bonding maps are reductions mod \(L_N\). Consequently

\[
\boxed{
\mathcal S_\mathbb Q
\cong \varprojlim_N(\mathbb R/L_N\mathbb Z).
}
\]

This is a precise version of "finite recursive clock circuit + continuous flow = one completed host."

## 2. The real flow is aperiodic and dense although the host is compact

The map

\[
\iota:\mathbb R\to\mathcal S_\mathbb Q,\quad
t\mapsto(t\bmod L_N)_N
\]

is injective because \(\bigcap_NL_N\mathbb Z=\{0\}\) (the LCM periods grow unboundedly).

Its image is dense: any basic open set of the inverse limit depends on finitely many coordinate circles, hence on one highest common L_N coordinate; the real line surjects onto that circle, so the image intersects the given open set.

Thus each finite SUCC clock closes after \(L_N\) steps, but the coherent limit has no nontrivial real-flow period and a dense real orbit through every point.

This is the honest mathematical content of the "idealized superconducting current" analogy: a lossless coherent global flow, not physical zero-resistance or literally infinite finite-valued current.

## 3. Why infinity is indispensable to the global quotient

The diagonal \(\mathbb Q\) is **dense** in the finite adeles \(\mathbb A_f\), so \(\mathbb A_f/\mathbb Q\) is a badly behaved non-Hausdorff quotient.

After adding the real place, the diagonal \(\mathbb Q\) becomes discrete and cocompact in \(\mathbb A=\mathbb R\times\mathbb A_f\):

- discreteness: \(\mathbb Q\cap((-\tfrac12,\tfrac12)\times\widehat{\mathbb Z})=\{0\}\);
- compactness: \(\mathbb A=\mathbb Q+([0,1]\times\widehat{\mathbb Z})\); the image of the compact set \([0,1]\times\widehat{\mathbb Z}\) covers the quotient.

Therefore \(\mathcal S_\mathbb Q=\mathbb A/\mathbb Q\) is a compact Hausdorff abelian group.

**Caution:** \(\widehat{\mathbb Z}\) by itself is already compact. It is the complete diagonal \(\mathbb Q\) gluing that needs infinity to turn the adelic quotient into a Hausdorff compact host.

## 4. Exact half-density Kirchhoff law across the places

For any \(q\in\mathbb Q^\times\),

\[
\boxed{\prod_{v\le\infty}|q|_v=1.}
\]

The local dilations

\[
U_{q,v}f(x)=|q|_v^{1/2}f(qx)
\]

are unitary on \(L^2(\mathbb Q_v,dx_v)\). Their scalar half-density normalizations multiply globally to 1. For \(q=3/2\),

\[
\boxed{
|q|_\infty^{1/2}|q|_2^{1/2}|q|_3^{1/2}
=\sqrt{3/2}\sqrt2\,1/\sqrt3=1.
}
\]

This is a strict, source-rigid interplace conservation identity. It cannot accommodate a shifted physical log2 without changing the rational/product-formula structure.

But product-formula conservation only determines the global kinematics, not the Weil positivity sign.

## 5. The complete SUCC/FUCC reversible host is Fourier dual to Q

The Pontryagin dual of \(\mathcal S_\mathbb Q\) is the discrete additive group \(\mathbb Q\). Thus

\[
L^2(\mathcal S_\mathbb Q)
\cong\ell^2(\mathbb Q).
\]

Write the Fourier basis as \(e_r\), \(r\in\mathbb Q\).

On this complete Hilbert space define the two unitary maps

\[
\boxed{
S e_r=e_{r+1},\qquad
V_qe_r=e_{qr}.
}
\]

These arise respectively from multiplication by the integer-1 character of the compact solenoid and the Koopman action of rational scaling. For every positive integer m,

\[
\boxed{
V_mS=S^mV_m.
}
\]

Both maps are *fully invertible* on \(\ell^2(\mathbb Q)\).

Let \(P_+\) project onto the positive integer-label subspace \(\ell^2(\mathbb N_{\ge1})\). Then \(P_+SP_+\) is the unilateral SUCC, and \(P_+V_pP_+\) is the familiar multiplicative FUCC isometry.

Its compressed inverse is

\[
(P_+V_pP_+)^*e_n=
\begin{cases}e_{n/p},&p\mid n\\0,&p\nmid n.\end{cases}
\]

The "information lost" by the finite shadow survives in the complementary rational-label space. One global rational reverse path gives the exact 2–3 echo

\[
V_2^{-1}V_3e_n=e_{3n/2},
\]

even when the projected integer shadow kills it for odd n.

**Caution:** this is representation-theoretic kinematics. It is not yet an independently constructed zeta spectral operator or Weil positive pairing.

## 6. Reversal at finite clock stages requires deeper history

On \(\mathcal S_N=\mathbb R/L_N\mathbb Z\), multiplication by a prime p is generally a p-to-one circle covering after p divides L_N. Its inverse is not single-valued on that coarse circle.

But multiplication by p on the full solenoid is a **group automorphism**, because its Pontryagin dual is multiplication by p on Q, which is bijective.

To recover the N-th coordinate of \(x=p^{-1}y\), choose a later stage M with \(pL_N\mid L_M\), then set

\[
\boxed{
x_N=\frac{y_M}{p}\bmod L_N.
}
\]

This is well-defined because changing a lift of \(y_M\) by \(L_M\) changes the quotient by a multiple of \(L_N\). Compatibility across M follows from the inverse limit. It is an exact "reassemble from more of the past/finer information" mechanism.

On normalized Haar circle Hilbert spaces, the forward pullback \(J_{N,M}f=f\circ\pi_{M,N}\) is isometric. At p-fold refinement, its adjoint averages coherently over p sheets,

\[
(J^*g)(t)=\frac1p\sum_{j=0}^{p-1}g(t+jL_N).
\]

In normalized orthonormal sheet coordinates the branching amplitude is \(1/\sqrt p\). The adjoint is not a two-sided inverse on arbitrary refined states; the invisible new-conductor sector is the kernel of the average.

## 7. Why this "superconductor" cannot itself prove RH

The global unitary \(V_p\) is a bilateral shift on every multiplicative orbit \(r p^\mathbb Z\subset\mathbb Q^\times\). Its spectrum is the full unit circle, for every prime p; it does not know the nontrivial zeta zeros.

Likewise, the solenoid and its dense R-flow exist for many arbitrary chains of covering degrees, so compactness and unitarity do not by themselves pass the fake-prime/half-density/Gamma/Weil fourth gate.

The arithmetic explicit-formula source still requires

\[
d\mu_P(t)=\sum_{p,k}(\log p)p^{-k/2}\delta_{k\log p}(dt)
\]

and the coupled completed Gamma/pole/contact functional. The raw total current at s=1/2 diverges:

\[
\sum_{p^k\le X}\frac{\log p}{p^{k/2}}\sim2\sqrt X
\]

by PNT (the k=1 primes dominate). Thus the "infinite current" is not an ordinary finite current that the real place effortlessly conducts. It requires a test/distributional notion and a source-derived coupled renormalization.

In the rigorous existing Weil square on f supported in (-A,A),

\[
Q_W(f)
=E_\Gamma(f)+E_{\rm prime,A}(f)
+2|C_f|^2-2|S_f|^2
-\left[\log\pi-\psi(1/4)+2M_A\right]\|f\|^2,
\quad
M_A=\sum_{p^k\le e^{2A}}\frac{\log p}{p^{k/2}}.
\]

The large \(2M_A\) term arises because positive difference energies contain a diagonal norm tax that must be removed to recover the arithmetic trace. One may not simply label the real place a positive absorber of this divergence. The independent all-horizon sign remains **RH-equivalent and OPEN**.

## 8. The genuinely promising compatibility test

The completed solenoid gives a rigorous common Hilbert host and global inverse kinematics. The next step is **NOT** to declare its unitarity the zeta Hilbert–Pólya operator. A candidate must:

1. Build the genuine prime-power current from the actual source \(\Lambda(n)n^{-1/2}\) and physical log p frequencies;
2. couple the full adelic Fourier/Poisson Gaussian and pole/contact renormalization **before** taking a quadratic-form sign;
3. retain nonlocal rational echoes, e.g. 3/2, but cancel nonprimitive "log6" source atoms;
4. define a *nonfactorized* source-derived polarization on a sufficiently large completed correspondence sector;
5. prove the **fully polarized identity** with the Weil form and derive its nonnegative sign independently.

The compact additive solenoid is a correct kinematic **closed circuit**. It is not the missing absolute arithmetic surface, canonical class or Hodge index.

### Verdict

This is a crisp mathematical refinement of the user's picture:

\[
\boxed{
\text{inverse-limit finite clocks}
+\text{a continuous real gluing coordinate}
\Rightarrow
\text{compact solenoid with a dense aperiodic flow}.
}
\]

Its globally reversible Q×-action reproduces the full SUCC/FUCC affine braid, while finite shadows become noninvertible. The missing RH theorem is the exact prime–Archimedean **polarization/energy coupling**, not existence of a lossless global host.
