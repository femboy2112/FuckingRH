# Spectral charge is part of the operator

There are three inequivalent choices:

| Choice | Finite expression | Consequence |
|---|---|---|
| One scalar x on the entire clock | `det(I-x C_L)` | `1-x^L` |
| Local prime block evaluated at `x=p^(-s)` | (CE1) | Euler product in its convergence domain |
| Full global innovation evaluated at its birth-prime `p^(-s)` | (GI3) | Different zero-free function on `Re s>0` |

The last two can each be written `det(I-exp(-s P_N) U_N)` at finite volume,
where `P_N` is the diagonal block charge `log p`, and `U_N` the specified
block clock. This unifies the parameter **s**, but inserts a nonconstant
charge operator and does not identify the two Hilbert spaces or spectra.
It also does not fix the noncompact infinite limit in `RELATIVE_DETERMINANT.md`.

A fixed-origin Green function at one complex `z` evolves by (BT2). Evaluating
the next prime event at `z=p^s` changes that evaluation point. One old Green
value alone need not determine a new spectral evaluation without retaining
the clock length/functional dependence. With the length retained this is
explicitly possible: compute `g_L(p^s)=1/(p^(sL)-1)` afresh and use
`partial_s g=-L log(p) g(g+1)`. This is an exact finite scalar description,
not a proof that a constant `2x2` transfer carries the completed response.

The mutation `p^(-s) -> p^(-alpha s)` in the local construction gives
`zeta(alpha s)` on `Re(alpha s)>1`, directly from (CE1). The corresponding
event weight and critical Mellin normalization change. Therefore the
parameter exponent is not dispensable. Affine Lebesgue unitarity fixes one
half-density only after the measure and representation are selected; it
does not license moving that power between these determinant conventions.

The charge history itself is exact: `log L(N)=sum_(p^k<=N) log p=psi(N)`.
As a distribution in log carrier time `u`,

\[
 d\log L(e^u)=\sum_{p,k\ge1}\log p\,\delta_{k\log p}(du).
\]

Multiplication by `exp(-u/2)` gives the Suzuki prime-wavefront measure.
Taking a feature square root gives `sqrt(log p) p^(-k/4)`. This is a faithful
pushforward of the dimension-growth measure. It is not yet a positive
representation of its completed signed Weil functional.
