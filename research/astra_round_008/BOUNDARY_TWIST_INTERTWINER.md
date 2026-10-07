# The twist/conductor intertwiner, entry by entry

Put `n=pL`, `L=p^(k-1)M`, `(p,M)=1`, and write each residue uniquely as
`a+bL`, `0<=a<L`, `0<=b<p`. The permutation from ordinary residue order to
tensor order `(a,b)` gives

\[
 C_{pL}=C_L\otimes I_p+|0\rangle\langle L-1|\otimes(C_p-I_p).    \tag{B1}
\]

This formula includes the permutation; omitting it is false. Diagonalize
the digit clock in negative-exponent characters. The `r` block is

\[
 U_L(\omega_p^r)=C_L+(\omega_p^r-1)|0\rangle\langle L-1|,
 \qquad U_L(\omega_p^r)^L=\omega_p^r I.                         \tag{B2}
\]

The following explicit orthonormal vectors intertwine this description
with the full conductor decomposition. Let `h=r+pj`, `0<=j<L`. Then

\[
 \chi_h(a+bL)=
 \underbrace{e^{-2\pi i r a/(pL)}e^{-2\pi i j a/L}}_{u_{r,j}(a)}
 \underbrace{e^{-2\pi i r b/p}}_{\eta_r(b)}.                    \tag{B3}
\]

Each factor has unit norm for normalized Haar. For fixed `r`, the vectors
`u_(r,j)` are an ordinary Fourier basis times one unitary chirp. Directly at
the boundary as well as in the interior,
`U_L(omega_p^r)u_(r,j)=exp(2*pi*i*h/(pL))u_(r,j)`.
The `r=0` block is the old space; for `r!=0`, its child average vanishes
and its conductor is

\[
 p^k d,\qquad d=M/\gcd(r+pj,M).                               \tag{B4}
\]

The chirp need not preserve the conductor of the *old index j*. A claim
to that effect would confuse a change of basis with a preserved label.

For an explicit CRT matching, let `c mod p^k` be primitive and `a mod M`
arbitrary. Set
`h=M c+p^k a (mod pL)`, `r=h mod p`, `j=(h-r)/p`. This is a bijection to
all the new characters. Here `d=M/gcd(a,M)` and for each fixed nonzero `r`
and each `d|M` there are exactly `p^(k-1) phi(d)` such characters. Indeed
`c == r M^(-1) mod p` has `p^(k-1)` lifts, and there are `phi(d)` choices
for the old coprime conductor. These formulas give the unitary, phases,
and conductor labels, not only equality of spectral multisets.

**Hostile distinction.** A diagonal phase conjugation of the full clock
preserves its characteristic polynomial while usually destroying its old
subspace. The seeded exact test exhibits this failure. An eigenvalue-list
comparison cannot certify (B1)–(B4).
