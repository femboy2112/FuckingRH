# Bounded adversarial audit: global determinant and small-state claims

Reviewer: Round008 Poisson subtask, same model as principal; this is a
separate derivation and implementation inspection, not independent model
provenance. Date: 2026-10-07. Read-only with respect to the audited files.

Files inspected in full:

- `GLOBAL_INNOVATION_THEOREM.md`
- `CYCLOTOMIC_EULER_CALIBRATION.md`
- `RELATIVE_DETERMINANT.md`
- `BOUNDARY_TRANSFER_STATE.md`

Also inspected their clock/Haar, exact-conductor, boundary-twist definitions,
the relevant Gamma assertions, and `scripts/round008_transfer.py`.
Reproduced `python -m unittest tests.test_round008_transfer -v`: **6 passed**.
No code, central file, or Git operations changed during this audit.

## Verdict

**No mathematical defect found in the stated universal claims.** The notes
keep their no-go boundaries appropriately narrow. In particular, the global
mixed determinant is not silently identified with the local Euler product,
and the finite-linear state bound is not asserted for nonlinear states.
The universal conclusions below rest on the explicit arguments, not the six
finite tests.

## 1. Global innovation determinant

GI1 and GI2 follow from a reducing old clock subspace, not solely matching
dimensions. The adopted orthonormal point basis is `sqrt(L) delta_a` under
normalized Haar, so neither a hidden factor L in a matrix element nor an
unexplained determinant power occurs.

For GI3, on `Re(s)>=delta>0`, with `y_j=p_j^(-s L_(j-1))`,

    |factor_j-1| <= |y_j|/(1-|y_j|)
                  <= 2^(-delta*2^(j-1))/(1-2^(-delta*2^(j-1))).

The majorant is summable independently of Im(s). This establishes compact
uniform product convergence. Each finite factor is the geometric polynomial
`1+y+...+y^(p-1)`; its zeros require |y|=1 and therefore lie on Re(s)=0.
Nonvanishing of the limiting product follows by an absolutely convergent
logarithm of its tail, plus the finitely many nonzero initial factors.
This is stronger than merely observing nonzero finite products, and is valid.

The asymptotic mismatch is sound. Separate the first event factor
`1+2^(-s)` and second factor `1+9^(-s)+81^(-s)`. For real s>=1 the remaining
majorant is O(16^(-s)); hence the product is `1+2^(-s)+O(9^(-s))`.
The missing `3^(-s)` coefficient distinguishes it from zeta in its absolute
convergence half-plane. No information about zeros is required.

The alternative common-x product telescopes to
`(1-x^(L(N)))/(1-x)`. This does not rule out a different, justified spectral
weighting or interaction, and the note explicitly leaves those open.

## 2. Local Euler calibration and the convergence boundary

At fixed p the cyclotomic factors telescope exactly. If
`K_p=floor(log_p N)`, maximality gives `p^K_p>N/p`; separating
`p<=sqrt(N)` and `p>sqrt(N)` proves the asserted strict lower bound
`p^K_p>sqrt(N)` for all p<=N. Thus the total numerator error is bounded by
`N 2^(-delta sqrt(N))` on Re(s)>=delta>0.

Only the numerator has this larger half-plane of convergence. The denominator
Euler product converges locally uniformly for Re(s)>1. On the real interval
0<s<=1 it diverges because `sum_p p^(-s)` diverges, whereas the numerator
still tends to one. The text does not promote that numerator estimate into
an Euler-product continuation theorem. This distinction is essential and
correctly maintained.

## 3. Noncompactness versus regularized determinants

For each fixed p, arbitrarily many mutually orthogonal block vectors are
sent to mutually orthogonal vectors of common norm `p^(-Re(s))>0`. Their
images have no convergent subsequence. Hence both declared infinite direct
sums are noncompact and cannot be trace class or any finite Schatten class.

This proves absence of the ordinary Fredholm determinant for those exact
operators. It does **not** prohibit grouped products or other regularizations.
The manuscript makes that distinction and fixes the grouping explicitly.
Its warning against reordering individual eigenvalue factors is justified:
even within a fixed prime tower the sum of their absolute moduli diverges.

The Gamma comparison is also consistent: for real s0>0 the resolvent
eigenvalues `(2m+s0)^(-1)` are square summable and not summable. Its det_2
therefore exists, while the stated zeta determinant has a separate, explicit
exponential normalization. Neither becomes a joint arithmetic positive
operator through scalar multiplication.

## 4. Scalar closure and exact scope of the linear lower bound

The clock Green function is `g_L(z)=1/(z^L-1)` in the declared orthonormal
point basis. Sherman-Morrison supplies the single-twist Möbius action.
For full refinement, substitution of `z^L=1+1/g` gives

    R_p(g)=g^p/((g+1)^p-g^p).

The denominator has degree p-1 and is nonzero at g=0, so it is coprime to
the numerator. This rational map has degree p; rational automorphisms of
the sphere have degree one, so rational invertible coordinate changes cannot
turn it into a Möbius map. Its conjugacy to `q -> q^p` is exact.
The conclusions hold for any integer refinement ratio p>=2, not only primes.

The explicit local state `u=L Log(z)` with update `u->p u` and readout
`g=1/(exp(u)-1)` is a valid nonlinear/transcendental escape. It assumes a
chosen logarithm branch and uses an unbounded-precision scalar. The notes
acknowledge both the local nature and the separate integer-L encoding.

The d>=L lower bound applies to a **fixed autonomous finite linear
resolvent realization**: such a transfer has at most d poles counted with
multiplicity, while g_L has L distinct poles. It is not a lower bound on
the dimension of arbitrary nonlinear, time-dependent, growing-chain, or
transcendentally parameterized realizations. Likewise the powers
`q^(2^j)` prove nonexistence only of the stated finite rational function
space invariant under substitution. Those scopes are accurately stated.

One caution for downstream use: BT2 keeps z fixed while refining L. The
birth-prime weighting in GI3 changes the spectral argument between events.
Closing g alone at one z therefore does not automatically propagate every
prime-charged response. The present note does not claim otherwise: it
retains L and z and limits the closure to the scalar clock problem.

## 5. Reproduced infinite mismatch certificate

The script's real-s tail bound is mathematically valid, not just a finite
comparison. After a prefix of length L, later old lengths are at least
`L*2^r`. With `z=2^(-sigma L)` one has

    sum_future log(factor) <= sum_{r>=0} z^(2^r)/(1-z^(2^r))
                            <= z/(1-z)^2.

The Arb upper bound `prefix * exp(z/(1-z)^2)` is therefore an upper bound
for the full infinite positive product. Its strict separation from
`pi²/6` at sigma=2 is a valid independent normalization control for GI,
not a claim about RH or positivity of the Weil form.

## Dominance boundary

The audited notes dispose of the named scalar determinant and finite-linear
shortcuts while preserving the nonlinear and genuinely coupled possibilities.
Nothing here proves that all mixed-conductor operators, all continuum lifts,
or all regularized trace constructions are impossible. The next relevant
burden remains the exact prime/Gamma pairing, as the notes state.
