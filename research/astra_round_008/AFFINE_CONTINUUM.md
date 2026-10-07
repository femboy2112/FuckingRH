# Affine continuum: what the half-density does and does not force

Status: exact identities and counterexamples proved here. This audits the
bilateral/continuum side branches. RH is open.

## 1. Group closure is not a Hilbert-space completion theorem

Affine maps `T_b(x)=x+b`, `D_a(x)=a x` satisfy
`D_a T_b D_a^(-1)=T_(ab)`. Including every prime dilation and its inverse
with unit translation produces rational translations and positive rational
dilations. Their closure **inside the usual real affine group** is the
full positive real affine group.

There is nevertheless no automatic passage from the discrete counting-space
representation to a continuous one. On `ell²(Q)`,

\[
\|T_{1/n}\delta_0-\delta_0\|=\sqrt2
\]

for every `n`, although `1/n -> 0` in `R`. This representation is not
strongly continuous for the subspace topology and cannot be the restriction
of a strongly continuous real-translation representation. A representation
already continuous in that topology extends to the closure by strong
limits: approximating group elements and their inverses both give strongly
Cauchy unitaries, and their limits are mutual inverses. Choosing that representation
is a genuine extra input.

Thus the continuum side note's extension statement is valid only with
this continuity hypothesis. It does not canonically embed the integer or
rational orthonormal basis as point masses in `L²(R,dx)`; those point
masses are not vectors of the latter space.

## 2. Exact real normalization and logarithmic conjugacy

Choose Lebesgue measure. Then

\[
(U_{a,b}f)(x)=a^{-1/2}f((x-b)/a),\qquad
U_{a,b}U_{c,d}=U_{ac,b+ad}
\]

is unitary on `L²(R,dx)`. With an ansatz `a^(-gamma) f(x/a)`, the squared
norm changes by `a^(1-2gamma)`; real `gamma=1/2` is necessary and
sufficient. An additional unitary character `a^(i eta)` is not excluded
by norm preservation and would require a separate convention.

The generators on the Schwartz core are

\[
P=-i\partial_x,\qquad D=-i(x\partial_x+1/2),\qquad [D,P]=iP.
\]

Here `U_(exp(t),0)=exp(-itD)` and `U_(1,b)=exp(-ibP)` with the displayed
sign convention. The self-adjoint closures follow from these explicit
strongly continuous unitary groups; the core identity is not a claim that
unbounded operators commute on arbitrary domains.

Restrict dilation to the positive half-line and use the unitary map

\[
(Vf)(u)=e^{u/2}f(e^u):L^2(R_+,dx)\longrightarrow L^2(R,du).
\]

Then `V U_(a,0) V^(-1)=tau_(log a)` and `V D V^(-1)=-i partial_u`.
The half-density moves into the coordinate transform; it is not a
remaining scalar amplitude of the unitary log translation. All real
translations do **not** preserve the positive half-line, so the full
affine action cannot be silently converted to global ordinary translations
in this one logarithmic chart.

For measure `x^(q-1) dx` the unitary dilation exponent is `q/2` instead.
For multiplicative Haar measure `dx/x`, it is zero. This is why the real
Lebesgue choice forces a half-density while the abstract group and the
factor-swap cone alone do not. Round007 C117 is retained.

## 3. p-adic and real half-densities: same overlap, opposite coefficients

Normalize additive Haar measure on `Q_p` by `vol(Z_p)=1`. The unitary
dilation is

\[
(U_a^{(p)}f)(x)=|a|_p^{-1/2}f(x/a).
\]

For `a=p^k`, `|a|_p=p^(-k)`: the **pointwise coefficient** is
`p^(+k/2)`, not `p^(-k/2)`. Meanwhile the cylinder has measure `p^(-k)`
and indicator norm `p^(-k/2)`. Put `v_p=1_(Z_p)`, which is a unit vector.
For `k>=0`,

\[
U_{p^k}^{(p)}v_p=p^{k/2}1_{p^kZ_p},\qquad
\langle v_p,U_{p^k}^{(p)}v_p\rangle=p^{-k/2}. \tag{A1}
\]

On the real side put `v_R=1_[0,1]`. Then

\[
U_{p^k}^{(R)}v_R=p^{-k/2}1_{[0,p^k]},\qquad
\langle v_R,U_{p^k}^{(R)}v_R\rangle=p^{-k/2}. \tag{A2}
\]

Thus the specified matrix coefficients agree exactly, through opposite
expansion/contraction of supports. For signed `k`, both are
`p^(-|k|/2)`. These cyclic matrix coefficients are genuinely the same
positive-definite function of the integer dilation parameter. This is a
precise bridge, rather than identifying opposite local Jacobians.

At all places together, for rational `a>0`, the product formula gives

\[
|a|_\infty^{-1/2}\prod_p|a|_p^{-1/2}=1.
\]

One cannot multiply real and p-adic pointwise normalizers and retain an
unexplained extra critical power. Normalized finite-Haar pullback under
residue refinement also differs from raw-counting normalization: it is
isometric without a pointwise `p^(-1/2)` factor; that factor occurs when
one instead expresses normalized vectors in the raw counting basis.

The feature coefficient `p^(-k/4)` is yet a third object. Squaring it gives
the event weight's `p^(-k/2)` by construction. Unless a feature map and its
measure are independently specified, taking this square root is not a
derivation from (A1) or (A2). The extra charge `log p` likewise is not
produced merely by observing a vacuum overlap. Differentiation in the
dilation parameter can supply it only after specifying which response is
differentiated.

## 4. Gamma in log coordinates, with the actual domain

Euler's integral [DLMF 5.2.1](https://dlmf.nist.gov/5.2.E1), under `x=e^u`,
gives

\[
\Gamma(s)=\int_R e^{su-e^u}\,du,\qquad \Re s>0. \tag{A3}
\]

At `u -> -infinity` the integrand behaves as `exp(su)`, so the integral
does not define the meromorphic continuation for `Re s<=0`. Gamma poles
must be obtained by analytic continuation or the ladder determinant, not
by asserting convergence of a bilateral integral there.

For any `sigma>0`, the function `phi_sigma(u)=exp(sigma*u-e^u)` belongs to
both `L¹(R)` and `L²(R)`. In the repository Fourier convention,

\[
\widehat\phi_\sigma(t)=\Gamma(\sigma+it),\qquad
\|\phi_\sigma\|_2^2=2^{-2\sigma}\Gamma(2\sigma).
\]

This identifies a Gamma **Fourier transform of a vector**. It does not make
Gamma the resolvent or a scalar transfer of the dilation generator.
The positive pairing
`integral e^((s+conj(u))*x-e^x)dx=Gamma(s+conj(u))` for
`Re s,Re u>0` is another valid Gram kernel; it is not the Weil kernel.

For the Gaussian the completed local factor follows directly:

\[
\int_0^\infty e^{-\pi x^2}x^{s-1}\,dx
=\tfrac12\pi^{-s/2}\Gamma(s/2),\qquad \Re s>0.
\]

At `s=1/2+it` this is the Fourier transform of
`e^(u/2) exp(-pi e^(2u))`, namely the Lebesgue-half-density log transform
of the positive-half Gaussian. This gives an exact relation between the
critical Mellin line and the chosen unitary normalization. It still does
not derive the global prime coefficient, select a completed positive
subspace, or prove that all zeros lie on this Plancherel line. Different
radial measures have different Plancherel lines.

## 5. Centering the edge does not cancel its degree

For every real `a`, bilateral translations satisfy

\[
\tau_a-I=\tau_{a/2}(\tau_{a/2}-\tau_{-a/2}),\qquad
(\tau_{a/2}-\tau_{-a/2})^*(\tau_{a/2}-\tau_{-a/2})
=2I-\tau_a-\tau_{-a}.
\]

Thus adding inverse translations recenters the old Round007 positive edge
by a unitary. Its norm and its required degree debit are unchanged.
The difference of odd/even sector squares is an exact signed
decomposition, not a positive Hilbert-space norm. Separating the Gamma
even-sector energy diverges at zero because `k(u)~1/(2u)`; no two finite
positive integrals result without an additional regularization theorem.

These observations confirm the valid bilateral side-branch algebra while
retaining the previous obstruction. A new coupling may leave that class;
changing the names of its symmetric and antisymmetric channels does not.

## 6. What survived the audit

| Statement | Verdict |
|---|---|
| Rational affine maps are dense in the real affine group | PROVED; algebraic/topological statement |
| The counting-space affine action extends continuously | REFUTED by `T_(1/n) delta_0` |
| Chosen real Lebesgue unitarity forces exponent `1/2` | PROVED, up to a unitary character |
| Real and p-adic pointwise dilation amplitudes coincide | REFUTED; their signs are opposite |
| The specified real/p-adic vacuum overlaps coincide | PROVED by (A1)–(A2) |
| A Gamma vector transform equals the oscillator generator | REFUTED as an identification; spectra differ |
| Gamma has controlled positive finite-mode difference forms | PROVED in `GAMMA_DRIFT.md` |
| The affine representation alone supplies the completed Weil square | UNVERIFIED; no exact pushforward established |

The useful next test is an exact interaction/pushforward identity. These
normalizations make that test well posed; they do not pay its sign theorem.
