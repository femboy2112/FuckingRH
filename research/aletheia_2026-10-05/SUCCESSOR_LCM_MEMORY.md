# Successor proper time, LCM memory, and prime-power crests

**Date:** 2026-10-05  
**Status:** exact structural dynamics / new control model. RH remains open.

## 1. Logarithmic proper time on the successor path

The bare successor path is

\[
1\to2\to3\to\cdots.
\]

Assign edge \(n\to n+1\) the length

\[
\Delta\tau_n
=
\log(n+1)-\log n.
\]

Then the accumulated path length telescopes:

\[
\boxed{
\tau(n)
=
\sum_{m=1}^{n-1}\Delta\tau_m
=
\log n.
}
\]

Thus the multiplicative/zeta coordinate \(\log n\) is an exact time-change of the successor ray.

For a prime tower,

\[
\tau(p^k)=k\log p.
\]

The Suzuki event locations are therefore proper-time locations on the successor path.

## 2. Valuation state and carry-depth interpretation

At each integer \(n\), the finite-place state is

\[
v(n)=(v_p(n))_p.
\]

In base \(p\), if \(v_p(n)=k\), then the predecessor step \(n\mapsto n-1\) rewrites \(k+1\) least-significant base-\(p\) digits: k trailing zeros become p-1 and the next digit decreases.

Taking one changed digit as the unavoidable baseline, the excess borrow/carry work is exactly

\[
v_p(n).
\]

Under the critical local KMS measure,

\[
\mathbb E[v_p]=\frac{p^{-1/2}}{1-p^{-1/2}},
\]

so

\[
\boxed{
M_p
=
(\log p)\,
\mathbb E[\text{excess base-p carry depth}].
}
\]

Hence the common Brownian coefficient \(M_L\) is the total expected logarithmically weighted fiber-work surcharge over the visible prime clocks.

## 3. Deterministic successor work and the product formula

For an actual integer \(n\),

\[
\sum_p v_p(n)\log p=\log n.
\]

Thus the logarithmic proper-time energy of one successor state is exactly the sum of its finite-place carry-depth energies.

Accumulating along the successor path gives

\[
\sum_{n=1}^{N}\log n
=
\sum_p(\log p)\sum_{n=1}^{N}v_p(n)
=
\log(N!).
\]

Equivalently,

\[
\boxed{
\log\Gamma(N+1)
=
\text{total logarithmically weighted finite-place execution depth accumulated along successor}.
}
\]

This is a structural Gamma/factorial link. It is not by itself the completed-zeta Gamma factor, whose variable is the Mellin parameter.

## 4. Cumulative divisibility memory

Define

\[
L_N=\operatorname{lcm}(1,2,\ldots,N).
\]

Its prime-depth vector is

\[
R_p(N)=v_p(L_N)=\max_{m\le N}v_p(m)=\lfloor\log_pN\rfloor.
\]

As N increases by successor,

\[
R(N)-R(N-1)
=
\begin{cases}
e_p,&N=p^k,\\
0,&\text{otherwise}.
\end{cases}
\]

Therefore

\[
\boxed{
\log L_N-\log L_{N-1}
=
\Lambda(N).
}
\]

Prime powers are exactly the state-change times of the cumulative divisibility memory of the successor past.

This makes the von Mangoldt function a literal execution/update cost of the LCM memory state.

## 5. Prime powers as join-irreducibles

Order positive integers by divisibility. This is a distributive lattice with

\[
a\vee b=\operatorname{lcm}(a,b),
\qquad
a\wedge b=\gcd(a,b).
\]

Its join-irreducible elements are exactly the prime powers \(p^k\).

An integer

\[
n=\prod_pp^{v_p(n)}
\]

corresponds to the finite order ideal

\[
I(n)
=
\{p^j:\ 1\le j\le v_p(n)\}.
\]

The cumulative LCM state has

\[
\boxed{
I(L_N)
=
\{p^k:\ p^k\le N\}.
}
\]

Thus successor reveals the prime-power poset one join-irreducible crest at a time.

The Chebyshev function is simply the total primitive weight of the revealed ideal:

\[
\boxed{
\psi(N)
=
\log L_N
=
\sum_{p^k\le N}\log p.
}
\]

## 6. Suzuki event measure as discounted LCM-memory action

Let

\[
C(t)=\psi(e^t).
\]

Distributionally,

\[
dC(t)
=
\sum_{n\ge2}\Lambda(n)\delta_{\log n}(dt).
\]

Hence the critical prime-power event measure is

\[
\boxed{
\mu_P(dt)
=
e^{-t/2}\,dC(t)
=
\sum_n\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(dt).
}
\]

And Suzuki's prime ramp is

\[
\boxed{
P(t)
=
\int_0^t(t-u)e^{-u/2}\,dC(u).
}
\]

So the finite-prime side is exactly the critically discounted accumulated work of updating the successor LCM-memory state.

## 7. Critical KMS state as a random order ideal

Under the critical Bost-Connes local measure,

\[
V_p=v_p(x)
\]

is geometric and

\[
\Pr(V_p\ge k)=p^{-k/2}.
\]

Thus the random set

\[
I(x)=\{p^k:\ k\le V_p(x)\}
\]

is a random order ideal of the disjoint union of prime-power chains.

For every join-irreducible,

\[
\boxed{
\Pr(p^k\in I)=p^{-k/2}.
}
\]

Therefore

\[
\boxed{
\frac{\Lambda(p^k)}{\sqrt{p^k}}
=
(\log p)\Pr(p^k\in I).
}
\]

Suzuki's prime measure is the logarithmic weight times the inclusion intensity of primitive events in the critical random ideal.

## 8. Repaired tower as expected capped depth

For one prime,

\[
D_p(t)
=
\frac{\log p}{1-p^{-1/2}}
\mathbb E[\min(t,V_p\log p)].
\]

Thus \(D_p\) is the expected capped overlap with the random depth of the p-chain.

This explains its CND/Gram geometry as an averaged cut/interval metric.

## 9. Successor translates distinct critical fibers

The critical KMS measure is not invariant under additive translation.

Modulo p, the class 0 has mass \(p^{-1/2}\), while each nonzero residue class has mass

\[
\frac{1-p^{-1/2}}{p-1}.
\]

Successor moves the heavy residue class.

Across the infinite product of primes, these local discrepancies accumulate; the critical measure and its successor translate lie in different measure sectors rather than one translation-invariant Haar sector.

Thus the succ-light-cone should be modeled as a path through a family of critical fibers/states, not as a unitary symmetry inside one fixed critical Hilbert space.

## 10. New geometry

A minimal lifted successor state should retain at least

\[
\boxed{
X_N=
\bigl(
\tau(N),
\iota(N),
R(N)
\bigr),
}
\]

where

- \(\tau(N)=\log N\) is successor proper time;
- \(\iota(N)\in\widehat{\mathbb Z}\) is the complete residue state;
- \(R(N)\) is the cumulative prime-depth/LCM-memory envelope.

The last component is determined by N but makes primitive state changes explicit.

Complexity/defect observables can be placed on top of this state.

## 11. Remaining proof problem

This model supplies exact positive primitive intensities, event locations, and local Gram blocks.

It does not prove the completed inequality

\[
A_\infty(t)\ge P(t).
\]

The next noncircular theorem must identify the Archimedean component as the positive compensator/metric completion of this critically discounted successor-memory process, strong enough to imply the Suzuki screw kernel (possibly after a uniformly bounded Brownian lift).

That is the remaining global seam.
