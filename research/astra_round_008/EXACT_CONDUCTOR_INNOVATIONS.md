# Exact conductors and signed Ramanujan kernels

On `H_n` use the orthonormal characters
`chi_h(a)=exp(-2*pi*i*h*a/n)`. Their clock eigenvalues are
`exp(2*pi*i*h/n)` and their exact conductor is `n/gcd(h,n)`.
For `d|n` the projection onto conductor `d` has matrix

\[
 P_d^{(n)}(a,b)=\frac1n c_d(a-b),\qquad
 c_d(r)=\sum_{e\mid(d,r)}e\,\mu(d/e).                         \tag{E1}
\]

The *integral kernel relative to normalized Haar* is `c_d(a-b)`; the extra
`1/n` is the matrix summation convention. The signs in (E1) are forced by
Möbius inversion of the sum of all characters whose conductor divides `d`.
They do not assert that every pointwise entry of a positive projection is
positive. Character orthogonality proves
`P_d*=P_d`, `P_d P_e=0` for `d!=e`, `rank P_d=phi(d)`, and
`sum_(d|n) P_d=I`.

At `L=p^(k-1)M -> pL=p^k M`, the old characters are precisely those with
index divisible by `p`. Thus

\[
 E_{p,L}=\bigoplus_{d\mid M}P_{p^k d}^{(pL)},\qquad
 \dim E_{p,L}=\varphi(p^k)\sum_{d\mid M}\varphi(d)=(p-1)L.       \tag{E2}
\]

Under the CRT identification of residue groups, this is
`(primitive p^k sector) tensor H_M`. In particular it includes every mixed
conductor `p^k d`; discarding `d>1` changes the operator. The clock itself is
`C_(p^k) tensor C_M` in CRT coordinates. This is a tensor decomposition of
a commuting operator, so mixed conductor labels alone are not cross-sector
dynamics. Finite Fourier transform does mix those sectors, as proved in
`FINITE_ADELIC_POISSON.md`.

Exact matrix checks include both `p|L` and `p` not dividing `L`. The
absolute-Möbius mutation loses idempotence, and dropping mixed sectors loses
the stated dimension and the Poisson diagram.
