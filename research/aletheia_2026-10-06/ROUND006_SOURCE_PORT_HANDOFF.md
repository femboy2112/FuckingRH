# Round 006 handoff — completed source port before the critical limit

**Parent:** Round005 head \`3222f975b6e076f94bd3b9dfdbc5423fb22fe695\`  
**Side results to integrate:** SOURCE_WIRED_PRIME_RAYS + FUCC_WITH_SUCC_COMPOSITION_CARRY  
**Status:** RH open.

## Exact source identity

The first SUCC pulse boots the multiplicative source:

\[
|0\rangle\xrightarrow{S}\Omega=|1\rangle.
\]

Every primitive wire is preattached:

\[
V_p^k\Omega=|p^k\rangle.
\]

Thus

\[
\Lambda(n)
=
\sum_{p,k}(\log p)\langle n|V_p^k\Omega\rangle.
\]

On the ray Hilbert space, with

\[
H|p,k\rangle=k\log p|p,k\rangle,
\qquad
Q|p,k\rangle=\log p|p,k\rangle,
\]

the critical event-weight operator is

\[
W_{1/2}
=
E Qe^{-H/2}E^*,
\]

and factors non-circularly.

For \(\sigma>1\), the source emission operator

\[
J_\sigma
=
\sum_{p,k}
\sqrt{\log p}\,p^{-k\sigma/2}
|p,k\rangle\langle\Omega|
\]

satisfies

\[
J_\sigma^*e^{itH}J_\sigma
=
-\frac{\zeta'}{\zeta}(\sigma-it)
|\Omega\rangle\langle\Omega|.
\]

So the Euler logarithmic derivative is exactly the finite-place source response.

## Completed source response

With

\[
A_\infty(s)
=
\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\psi(s/2),
\]

we have in the Euler half-plane

\[
\boxed{
\frac{\xi'}{\xi}(s)
=
A_\infty(s)
-
\sum_p\frac{\log p}{p^s-1}.
}
\]

The classical Lagarias criterion is

\[
\mathrm{RH}
\iff
\Re\frac{\xi'}{\xi}(s)>0
\quad(\Re s>1/2).
\]

Therefore the proof-producing goal is:

> Construct finite arithmetic source ports whose transfer/driving-point functions are positive-real by structural operator theory and converge locally uniformly to \(\xi'/\xi\) on the right critical half-plane.

If this is achieved without assuming RH or using zero ordinates, RH follows by positivity preserved under locally uniform limits.

## Crucial distinction from Round005's refuted shared-DC idea

Do NOT sum the already-squared local \(B_p^*B_p\) and then subtract a divergent global correction.

Instead:

1. wire finite prime rays to one common source;
2. include the finite Archimedean/boundary completion at that source;
3. form one finite coupled operator/colligation;
4. eliminate internal rays by a Schur complement / Weyl function;
5. prove the source response is positive-real/contractive;
6. only then take the limit.

This is "couple + complete first, limit second."

The specific shared-nonzero-DC positive multiresolution mechanism is refuted. No universal impossibility of source-coupled algebraic renormalization has been proved.

## Potential operator realizations

### 1. Weyl / Schur complement route

For a finite block operator

\[
\mathcal D_X(z)
=
\begin{pmatrix}
A_X(z)&C_X^*\\
C_X&D_X(z)
\end{pmatrix},
\]

the effective source response is

\[
M_X(z)
=
A_X(z)-C_X^*D_X(z)^{-1}C_X.
\]

Find arithmetically forced \(D_X,C_X,A_X\) whose branch contributions recover the prime-ray response and Gamma/pole completion.

### 2. Positive-real / Schur route

For a positive-real completed response \(F\), the Cayley transform

\[
\Theta_a
=
\frac{F-a}{F+a},
\qquad a>0,
\]

is contractive.

A finite unitary/passive colligation produces a Schur transfer function automatically.

Thus an alternative target is:

\[
\Theta_X
\to
\frac{\xi'/\xi-a}{\xi'/\xi+a}
\]

locally uniformly, with every \(\Theta_X\) structurally contractive.

### 3. Rigged / boundary-form route

The naive source vector leaves Hilbert space as \(\sigma\downarrow1/2\).

So the critical object cannot be a norm limit of \(J_\sigma\Omega\).

Look for:

- completed boundary forms;
- strong-resolvent / quadratic-form limits;
- rigged Hilbert realizations;
- Pontryagin/Krein finite-defect embeddings if the rank-2 pole forces them.

Any indefinite-space route must eventually produce the positive Hilbert/Weil form without assuming RH.

## History-space side channel

The separate composition branch shows that the full causal FUCC/SUCC history space is larger than the quotient integer/ray space.

Ordered compositions \(\alpha\models n\) are the \(2^{n-1}\) causal FUCC-placement histories, with

\[
P_\alpha(1)=n,
\]

and evaluation \(P_\alpha(m)\) executes the affine program.

The quotient

\[
\frac{P_\alpha(x)-n}{x-1}
\]

records exact cut positions.

Round005 proved that several commutative quotient spaces lose carry curvature. Therefore compare source-port construction:

- after quotienting histories to integer states;
- before quotienting, on the full ordered history/Fock space.

The latter may retain phases/cross terms needed for a passive realization.

## Non-negotiable hostile controls

- zero ordinates never enter construction;
- fake prime wire;
- delete real prime wire;
- wrong half-density;
- wrong \(\log p\) charge;
- static direct sum vs common-source coupling;
- quotient histories vs retain histories;
- remove Archimedean port;
- perturb Gamma/pole boundary;
- vary cutoff/order of limits.

Any construction that remains valid under fake arithmetic is likely RH-inert.

## The limit theorem to hunt

The strongest desired theorem has the form:

There exist finite arithmetic passive systems \(\mathcal S_X\), constructed without zeros, with completed source response \(F_X\) such that

\[
\Re F_X(s)\ge0
\quad(\Re s>1/2)
\]

for every \(X\), and

\[
F_X\to\xi'/\xi
\]

locally uniformly on \(\Re s>1/2\) away from the target poles/with an equivalent zero-free formulation.

Then

\[
\Re\xi'/\xi\ge0
\]

there, and the Lagarias criterion yields RH.

If strict positivity is needed, isolate the nondegeneracy argument.

If no such finite passive approximants can exist in a declared natural class, prove that obstruction and identify the next smallest class.



## Stronger limit shortcut: Schur normal-family / Vitali route

There is a potentially cleaner theorem architecture than proving local-uniform convergence to \(\xi'/\xi\) directly on the whole critical half-plane.

Fix \(a>0\) and define the Cayley transform of a completed source response:

\[
\Theta_a(s)
=
\frac{F(s)-a}{F(s)+a}.
\]

If \(F_X\) is positive-real on

\[
H_{1/2}:=\{s:\Re s>1/2\},
\]

then

\[
|\Theta_{a,X}(s)|\le1
\]

there. Thus \(\{\Theta_{a,X}\}\) is automatically a normal, locally bounded family.

Now suppose one can prove only the **easy Euler-side convergence**

\[
\Theta_{a,X}(s)
\longrightarrow
\frac{\xi'(s)/\xi(s)-a}{\xi'(s)/\xi(s)+a}
\qquad
(\Re s>1),
\]

where the Euler product/log-derivative is absolutely convergent and no RH input is needed.

Because the \(\Theta_{a,X}\) are uniformly bounded holomorphic functions on the larger connected domain \(H_{1/2}\), Vitali/Montel gives a holomorphic limit on all of \(H_{1/2}\), uniquely determined by its values on the open subset \(\Re s>1\).

Consequently the Cayley inverse gives a positive-real holomorphic continuation of \(\xi'/\xi\) to \(H_{1/2}\). A pole of \(\xi'/\xi\) there would contradict holomorphy, so \(\xi\) has no zero with \(\Re s>1/2\). By the functional equation, RH follows.

This means a Round006 proof does **not** necessarily need to estimate the critical-strip limit directly.

A potentially sufficient route is:

1. construct finite arithmetic source systems with Schur transfer functions \(\Theta_X\) on \(H_{1/2}\);
2. prove \(|\Theta_X|\le1\) structurally for every finite \(X\);
3. prove convergence only in the safe Euler region \(\Re s>1\);
4. let normal-family compactness perform the continuation.

This is still a hard theorem: producing the uniformly contractive finite systems on \(H_{1/2}\) is essentially where the RH content must enter. But it isolates the limit step very sharply and prevents accidental circular assumptions about convergence across possible zeta zeros.

Do **not** write "assume \(F_X\to\xi'/\xi\) on \(H_{1/2}\)" as a premise; that convergence would already force a zero-free half-plane and therefore smuggle in the goal.

## Slogan

\[
\boxed{
\text{SUCC boots the source. Prime rays are prewired. Completion is the source boundary. Couple first. Take the limit last.}
}
\]
