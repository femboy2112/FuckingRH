# Finite Haar refinement, dual refinement, and the missing Fourier diagram

Status: exact theorems proved below; classical finite Pontryagin duality, with
its consequences for this repository's LCM filtration made explicit. No RH
positivity arrow is discharged by these identities.

## 1. Measures before matrices

For a positive integer L, let H_L be functions on Z/LZ with

    <f,g>_L = (1/L) sum_a f(a) conjugate(g(a)).

The finite Fourier coefficients with normalized Haar are
`fhat(b)=(1/L) sum_a f(a) exp(-2 pi i ab/L)`.
This is an isometry from H_L to the dual group with **counting** measure.
The unitary endomorphism of H_L is instead

    F_L f(b) = (1/sqrt(L)) sum_a exp(-2 pi i ab/L) f(a).

Thus F_L=sqrt(L) fhat. Calling the 1/L matrix a unitary endomorphism of the
normalized-Haar H_L loses a factor sqrt(L). Character orthogonality proves
`F_L^*F_L=I`, `F_L^2 f(a)=f(-a)`.

## 2. Exact correction to the refinement square

Let M=rL and define the canonical pullback and its dual injection by

    (I_LM f)(a) = f(a mod L),
    (J_LM g)(b) = sqrt(r) 1_{r divides b} g(b/r).

Both are isometries for the normalized Haar inner products. Their adjoints are

    (I_LM^*h)(a) = (1/r) sum_{j=0}^{r-1} h(a+jL),
    (J_LM^*h)(a) = h(ra)/sqrt(r).

The actual commuting identities are

    F_M I_LM = J_LM F_L,             F_M J_LM = I_LM F_L.        (P1)

Proof: in the first formula, split a=c+jL in the Fourier sum. The inner
geometric sum is zero unless r divides b and equals r otherwise. For the
second, sum only over a=rc. These computations retain all harmonics.

**The same-embedding square fails for every proper refinement.** For f=1,
`F_M I f=sqrt(M) delta_0`, while `I F_L f=sqrt(L) 1_{L divides a}`.
The exact normalized squared distance is

    ||F_M I 1 - I F_L 1||_M^2 = 2 - 2/sqrt(r) > 0.             (P2)

Consequently the endomorphisms F_L do not define a compatible operator on the
inductive system with embeddings I. No limiting argument repairs this exact
diagram. This is a scoped obstruction to that proposed diagram, not to
Fourier analysis on the limit: ordinary Fourier coefficients give the valid
unitary map `L²(Zhat) -> l²(Q/Z)`, with extension by zero on the dual side.
The two limits have different natural descriptions; identifying their finite
bases anew at every horizon hid the distinction.

## 3. Mixed conductor sectors cannot be deleted before this Fourier map

Let E be the orthogonal projection onto any union of the harmonic sectors
whose character has exact conductor d dividing L. It is a circulant matrix:

    E(a,b) = (1/L) sum_{d selected} c_d(a-b),
    c_d(n) = sum_{e | gcd(d,n)} e mu(d/e).

Fourier conjugation gives the coordinate diagonal projection
`F_L E F_L^*=diag(1_{L/gcd(k,L) selected})`.
If E commutes with F_L, E is therefore both diagonal and circulant. Such a
matrix is a scalar identity; a projection is consequently 0 or I.

**No nonzero proper union of exact-conductor harmonic sectors is invariant
under F_L.** This includes a prime-power-only union that omits mixed
conductors. At L=6, deleting conductor 6 leaves rank 4 and breaks the theta
Fourier identity by a certified nonzero amount. This does not forbid using
individual sectors as coordinates; it forbids declaring their deletion
compatible with the full self-duality.

## 4. The actual finite adelic model

The compact inverse limit Zhat is not the full finite adele ring. One also
needs rational dilations:

    A_f = union_{L>=1} L^{-1} Zhat.

Under the standard additive character and `vol(Zhat)=1`, a finite coset has
`vol(a+L Zhat)=1/L`, and its Fourier transform is supported on
`L^{-1} Zhat`, with coefficient 1/L and the dual character of a. This is
exactly the quotient/inclusion distinction in (P1), before identifying finite
groups with their duals.

For the adelic test `f(x_infinity/sqrt(L)) 1_{a+L Zhat}(x_f)`, the rational
diagonal meets the finite coset precisely in a+L Z. The real transform
contributes sqrt(L), while the finite transform contributes 1/L. Their
combined coefficient is 1/sqrt(L). The resulting relation is exactly the
residue-Poisson identity in `THETA_SELF_DUALITY.md`.

This is a standard Tate/Poisson test object with a chosen finite conductor;
the LCM schedule selects a cofinal sequence of such tests. The schedule alone
does not create the rational diagonal, real Fourier transform, Gaussian, or
self-dual Haar choices. Those are the additional structures required.

## 5. Provenance, controls, and remaining burden

The proofs in sections 1–3 are explicit finite sums, independently checked in
`scripts/round008_poisson.py` using cyclotomic polynomial reduction. Arb
checks include fresh pairs 6|30 and 10|60, unequal theta times, and mutations
of Haar normalization, real mesh scale, and conductor deletion.

Primary context: André Weil, *Fonction zêta et distributions*, Séminaire
Bourbaki 312 (1966), §§1–2, pp.525–530, identifies self-dual Haar measures,
local Gamma distributions, and the global rational-diagonal Poisson step.
[Original scan](https://www.numdam.org/item/SB_1964-1966__9__523_0.pdf).
The available text of the scan was read; the screenshot interface returned
placeholders rather than inspectable image data in this subtask. Its hypotheses concern
Schwartz–Bruhat tests on the actual adele ring, not an arbitrary matrix
clock. We rederive the finite formulas here; we do not import an RH theorem.

The unpaid arrow is a completed Weil **energy** identity. Poisson supplies a
Fourier relation and functional equation, not the positive norm giving that
energy. In particular, neither this correction nor finite DFT unitarity
removes Round007's exact negative identity residual.
