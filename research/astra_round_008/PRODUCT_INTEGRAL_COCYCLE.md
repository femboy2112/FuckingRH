# What a coherent history transports

Spaces change at events. A product of square matrices of unrelated sizes is
not a defined cocycle. With `H_j=H_(L_j) tensor K`, specify isometries
`S_j:H_(j-1)->H_j` and between-event semigroups `P_j(t)` on `H_j`.
Then, for declared event times, the finite evolution
`P_m(t_m) S_m P_(m-1)(t_(m-1)) ... S_1 P_0(t_0)` is well defined.
If `S_j=I_(L_(j-1),L_j) tensor I` and `P_j(t)=I tensor exp(-tH_Gamma)`,
the exact intertwining relation makes it
`I_(1,L_m) tensor exp(-(sum t_j)H_Gamma)`. No prime/Gamma cross pairing
has been created. To change this conclusion, a kick or drift must fail that
intertwining relation, with its domain and coefficients specified.

**Isometric-history theorem.** For arbitrary isometries `S_j`, let
`J_j=H_j minus S_j H_(j-1)` be their orthogonal innovation spaces. Their
images at a later horizon under the same subsequent isometries are mutually
orthogonal.

Proof: for `i<j`, the transported `J_i` lies in `S_j H_(j-1)`, hence is
orthogonal to `J_j`. Every later isometry preserves this inner product.
The proof works with an infinite-dimensional continuum tensor factor and
does not require commutation of different kicks. Consequently a common
isometric history, including a common final Fourier/unitary change of basis,
cannot by itself generate cross-event Gram terms between its *own*
innovations. New source inputs or a non-isometric observation/interaction
are additional mathematical choices.

For example, if `S_j=F_(L_j) I_j`, the correct innovation is `F_(L_j) J_j`
of the untwisted embedding. Retaining the previous arithmetic labels while
calling them orthogonal innovations for the new embedding is false. The
same-basis Fourier refinement defect is computed in the Poisson note.

This is a scope theorem, not a ban on interacting dynamics. A subsequent
compression, positive metric, or nonunitary drift can produce correlations.
`COMPLETED_CLOCK_OPERATOR.md` constructs such a shared-origin heat metric
before squaring and computes its full cross terms. The important distinction
is between a change of coordinates, which preserves inner products, and an
interaction/observation, which may change them.

The Gamma oscillator control in `GAMMA_DRIFT.md` is a second actual hybrid:
the carry at the boundary translates its real coordinate and fails to commute
with the oscillator. Its exact heat trace has been derived, rather than
inferred from the word 'hybrid'. No refinement-compatible completed Weil
pairing is established for that control.
