# Branch-transfer classification: the one-port / direct-sum class is dead (ckpt5)

**Date:** 2026-10-06. **Status:** DISCLOSED (no-go, rigorous). **RH open.**
**Reproduce:** `scripts/branch_transfer_passivity.py`.

The directive (§5) warns: *do not assume `m_p` is positive-real; check it.* We check it, and the answer
is a clean obstruction that kills the entire first natural class and explains why coupling is mandatory.

## Lemma 1 (per-ray failure — rigorous, on EVERY right half-plane)

The one-port `m_p(s) = log p/(p^s - 1)` has `Re m_p(s) < 0` at points of every half-plane `Re s > sigma_0`.

*Proof.* Fix `sigma > sigma_0`. The imaginary part `t` is free, and `p^{sigma+it} = p^sigma e^{it log p}`
traces the full circle `|w| = p^sigma` as `t` runs over `R`. Choose `t` with `t log p ≡ pi (mod 2pi)`
(possible: `t` ranges over all reals). Then `w = p^s = -p^sigma`, so
`Re m_p = log p · (Re w - 1)/|w-1|^2 = log p · (-p^sigma - 1)/|{-p^sigma-1}|^2 < 0`. ∎

Numerics (script A): `Re m_p < 0` at `s = sigma + i pi/log p` for all tested `(p, sigma)`, e.g.
`p=2, sigma=2 -> -0.139`; `p=13, sigma=4 -> -9e-5`. **`m_p` is not positive-real on any `Re s>sigma_0`.**

## Lemma 2 (the naive sum also fails)

`-zeta'/zeta(s) = sum_p m_p(s)` has `Re < 0` on `Re s > 1`: e.g. at `s = 2 + i pi/log 2`,
`Re(-zeta'/zeta) = -0.104`; at `3 + i pi/log 2`, `-0.064`; at `1.5 + 2i`, `-0.264` (script B). So the
series/parallel (sum-of-one-ports) combination is **not** positive-real either. A fortiori the Round005
direct sum `sum_p B_p^* B_p` cannot be the completed positive object (directive §8: "Not: direct sum").

## What positivity the arithmetic DOES carry — and why it does not transport

The von Mangoldt **energy measure** `dmu(E) = sum_n Lambda(n) delta_{log n}(E)` is positive, and

    -zeta'/zeta(s) = integral_0^infty e^{-sE} dmu(E)   (Laplace transform).                 (*)

A Laplace transform of a positive measure is **completely monotone** on the real axis:
`(-1)^n (d/ds)^n (-zeta'/zeta)(s) > 0` for real `s>1` — verified (script C: all four derivatives
alternate correctly at `s=1.5, 2, 3`). This is a genuine, automatic positivity.

**But completely-monotone-in-`s` is NOT positive-real-in-`s`.** `Re(e^{-sE}) = e^{-sigma E}cos(tE)` is not
sign-definite, so (*) gives no half-plane positivity (Lemmas 1–2 are this fact in action). The classic
separation: `e^{-s}` = Laplace of `delta_1` is completely monotone but `Re(e^{-s}) = e^{-sigma}cos t < 0`
near `t = pi`.

The *other* standard transform of the same measure — the **Cauchy/resolvent** transform
`G(z) = integral dmu(E)/(E - z) = sum_n Lambda(n)/(log n - z)` — IS Herglotz (positive-real) when it
converges. **It does not converge:** `integral_0^{E} dmu = psi(e^{E}) ~ e^{E}` (Chebyshev; script D shows
`psi(X)~X`), so the measure grows exponentially in `E` and its Cauchy transform diverges. The damping
needed to make it converge is exactly the `e^{-sE}` of (*) — which returns the non-positive-real Laplace
transform. **You cannot extract a free Herglotz object from the raw von Mangoldt measure.**

## The unifying obstruction (the real content of ckpt5)

> Every per-prime one-port is a function of the **bounded** variable `w = p^s` (equivalently
> `zeta = p^{-s}`, `|zeta| < p^{-1/2} < 1` on `Re s>1/2`). The positivity the arithmetic supplies
> (resolvent/Herglotz of a bounded contraction, e.g. Round005's `(I - p^{-1/2}U)^{-1}`) lives in that
> `w`/`zeta` variable. The change of variable `s |-> p^s` is **exponential and periodic**, not a
> half-plane automorphism; it wraps `Re s>1/2` around the annulus infinitely and does **not** carry
> Herglotz-in-`w` to Herglotz-in-`s`. Therefore no per-ray one-port, and no series/parallel sum of them,
> is positive-real on `Re s>1/2`.

**Consequence.** Positive-realness in `s` — the thing RH needs — cannot be a per-ray or sum-of-rays
property. It can only arise from (i) a genuine **coupling** across rays and/or to a boundary node that
mixes the different `p^s` periodicities (so the combined object is no longer a function of any single
`p^s`), and (ii) the **Archimedean completion**, whose `psi(s/2)` and `1/s + 1/(s-1)` are the only pieces
that are *not* functions of any `p^s` and can break the periodicity. This is precisely why the directive
demands *couple + complete before forming the response* (§§6, 8, 16), and it is the structural reason the
Round005 direct-sum picture was always going to be RH-inert.

## Ledger

New row **C103**: per-prime one-port `m_p` (and every sum of one-ports) is not positive-real on any right
half-plane (Lemma 1, periodicity-in-`s`); the arithmetic carries only Cauchy-Herglotz-in-`w` and
real-axis complete-monotonicity, neither of which transports to positive-realness in `s`. Kills the
one-port/direct-sum class; forces coupling + Archimedean completion.
