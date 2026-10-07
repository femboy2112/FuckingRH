# Passive finite approximants + safe Euler convergence imply RH

**Date:** 2026-10-06  
**Status:** sharp proof-bearing reduction. Existence of the required causal finite approximants is not yet proved. **RH remains open.**

This theorem substantially reduces the global convergence burden of the SUCC/FUCC Weyl program.

We do **not** need to prove direct convergence of the finite arithmetic systems on the critical line or throughout the critical strip.

It is enough to prove:

1. every finite causal approximation is passive/Weyl;
2. its response converges to the completed zeta response only in the ordinary Euler region.

Normal-family compactness and analytic uniqueness do the rest.

---

## 1. Global target

Define

\[
\Xi(z)
=
\xi\!\left(\frac12-iz\right)
=
\xi\!\left(\frac12+iz\right)
\]

and

\[
m_\Xi(z)
=
-\frac{\Xi'(z)}{\Xi(z)}.
\]

On the safe upper region

\[
\Omega_{\rm safe}
=
\{z:\Im z>1/2\},
\]

we have

\[
\Re(1/2-iz)>1,
\]

so \(m_\Xi\) is given by absolutely convergent prime/Gamma formulas.

Define its Cayley transform

\[
\boxed{
S_\Xi(z)
=
\frac{
m_\Xi(z)-i
}{
m_\Xi(z)+i
}.
}
\]

On any region where \(m_\Xi\) is Herglotz, \(S_\Xi\) lies in the Schur class.

---

## 2. Finite passive-approximation hypothesis

Suppose there is a sequence of finite causal systems indexed by horizon \(N\), built without nontrivial-zero data, with Herglotz boundary functions

\[
m_N:\mathbb C_+\to\mathbb C_+.
\]

Define

\[
\boxed{
S_N(z)
=
\frac{
m_N(z)-i
}{
m_N(z)+i
}.
}
\]

Then

\[
|S_N(z)|\le1
\qquad
(z\in\mathbb C_+).
\]

Assume also that

\[
\boxed{
m_N(z)\to m_\Xi(z)
}
\]

locally uniformly, or merely pointwise with enough local control, on

\[
\Omega_{\rm safe}.
\]

Equivalently,

\[
S_N(z)\to S_\Xi(z)
\]

there.

---

## 3. Normal-family compactness

Because every \(S_N\) maps \(\mathbb C_+\) into the closed unit disk, the family is locally bounded.

By Montel's theorem it is a normal family.

Therefore every sequence has a subsequence

\[
S_{N_j}
\]

converging locally uniformly on \(\mathbb C_+\) to a Schur function

\[
S.
\]

On the safe open set, the assumed arithmetic convergence gives

\[
S(z)=S_\Xi(z).
\]

Hence analytic uniqueness fixes the limiting Schur function completely.

---

## 4. Why an off-line zero is impossible

Suppose RH is false.

By functional-equation symmetry there is a nontrivial zero whose \(z\)-coordinate lies in \(\mathbb C_+\):

\[
z_\rho\in\mathbb C_+.
\]

At that point,

\[
m_\Xi(z)
=
-\Xi'(z)/\Xi(z)
\]

has a pole.

But its Cayley transform has a removable limit:

\[
\boxed{
\lim_{z\to z_\rho}
\frac{
m_\Xi(z)-i
}{
m_\Xi(z)+i
}
=
1.
}
\]

Since \(S\) analytically continues \(S_\Xi\) from the safe region, the removable extension satisfies

\[
S(z_\rho)=1.
\]

But \(S\) is a Schur function:

\[
|S(z)|\le1
\]

throughout the upper half-plane.

By the maximum modulus principle, if a nonconstant analytic disk-valued function attains modulus \(1\) at an interior point, it must be constant.

The safe-region target \(S_\Xi\) is not constant.

Contradiction.

Therefore no off-line zero exists.

\[
\boxed{RH.}
\]

---

## 5. The theorem

### Passive Approximation Criterion

If there exist finite causal Herglotz functions \(m_N\), constructed without nontrivial-zero data, such that

\[
m_N(z)\to
-\frac{\Xi'(z)}{\Xi(z)}
\]

on the safe open region

\[
\Im z>1/2,
\]

then the Riemann Hypothesis holds.

Equivalently, it is enough to construct finite Schur transfer functions \(S_N\) satisfying:

\[
|S_N|\le1
\quad\text{on }\mathbb C_+,
\]

and

\[
S_N\to
\frac{
-\Xi'/\Xi-i
}{
-\Xi'/\Xi+i
}
\]

on the safe region.

---

## 6. Why this is much easier than the original target

The previous target demanded:

\[
m_N\to m_\Xi
\]

throughout the upper half-plane, including the critical regime.

That is essentially asking the finite arithmetic approximants to solve the hard analytic-continuation problem directly.

The new criterion only demands convergence where

\[
\Re s>1,
\]

where the prime series is absolutely convergent.

The difficult continuation is supplied automatically by:

- finite passivity;
- normal-family compactness;
- analytic uniqueness.

This cleanly separates the tasks.

---

## 7. What passivity must mean at finite horizon

A sufficient finite construction would give each horizon \(N\) a unitary/self-adjoint colligation whose Weyl function is \(m_N\).

Then Herglotzness is automatic.

The exact local ingredients already available are:

- \(p\)-adic prime Weyl blocks;
- exact-conductor unitary twists;
- \(SU(1,1)\) transfer matrices;
- rank-one carry-boundary updates;
- critical normalization;
- finite inverse-SUCC/Gamma/trivial pairing.

The missing construction is their **finite completed interconnection**.

---

## 8. Crucial finite-completion requirement

One cannot use:

\[
\text{finite prime Euler product}
+
\text{bare infinite Gamma factor}
\]

because the bare Gamma factor fails the Schur/Blaschke test.

The finite approximant must pair the relevant Archimedean/trivial modes before claiming passivity.

Thus the real engineering problem is:

\[
\boxed{
\text{construct one finite lossless/passive block per causal horizon in which the local completion has already occurred.}
}
\]

If this can be done, global critical-line control is no longer required separately.

---

## 9. Stronger version: one convergent subsequence is enough

Because the \(S_N\) are uniformly bounded Schur functions, a subsequential limit always exists.

If the **full sequence** converges to the target on the safe open set, every subsequential limit must coincide there and hence globally.

So uniqueness automatically removes subsequence ambiguity.

This is an important robustness feature.

---

## 10. No need to know the microscopic phase dance

The finite transfer matrices may have complicated, random-looking phases.

As long as each finite completed network is passive, its transfer function remains in the Schur class.

Thus the theorem depends on:

\[
\boxed{
\text{the invariant transfer class}
}
\]

and safe-region matching, not on an explicit closed formula for every local phase.

This directly implements the user's gauge/universality intuition.

---

## 11. Immediate research target

For each horizon \(N\), construct

\[
\boxed{
\mathfrak S_N
}
\]

from the causal LCM/carry history and define its Schur transfer function

\[
S_N(z).
\]

Prove only:

### P1 — finite passivity

\[
|S_N(z)|\le1
\qquad(\Im z>0).
\]

### P2 — safe convergence

For

\[
\Im z>1/2,
\]

\[
S_N(z)\to S_\Xi(z).
\]

Those two statements imply RH.

This is now the highest-priority theorem target of the Weyl program.

---

## 12. House slogan

\[
\boxed{
\text{Don't analytically continue the primes by force.}
}
\]

\[
\boxed{
\text{Make every finite arithmetic machine passive.}
}
\]

\[
\boxed{
\text{Match it only where Euler already converges.}
}
\]

\[
\boxed{
\text{Normal-family rigidity does the continuation for you.}
}
\]
