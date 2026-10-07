# Local Euler calibration and its exact limit

At a single prime let `K_p=floor(log_p N)`. The local primitive-block
determinant identity is classical:

\[
 \prod_{k=1}^{K_p}\det(I-p^{-s}C_{p^k}|_{\mathrm{primitive}})
 =\frac{1-p^{-s p^{K_p}}}{1-p^{-s}}.                           \tag{CE1}
\]

It follows either from cyclotomic factorization or by telescoping
`(1-x^(p^k))/(1-x^(p^(k-1)))`. Hence the product over `p<=N` converges to
`zeta(s)` locally uniformly on `Re s>1`. Here is a useful bound that retains
the exact finite remainder: for every such prime, `p^(K_p)>sqrt(N)`.
If `p>sqrt(N)` this is immediate, and otherwise `p^(K_p)>N/p>=sqrt(N)`.
Thus on `Re s>=delta>0`,

\[
 \sum_{p\le N}|p^{-s p^{K_p}}|\le N2^{-\delta\sqrt N}\longrightarrow0.
\]

The numerator product tends to one uniformly on these compact sets. The
denominator product converges on `Re s>1` by the absolutely convergent Euler
product. For real `0<s<=1` it diverges, so this calculation does not supply
continuation across that boundary. Analytic continuation is a separate
theorem, not convergence of these positive finite factors.

These are independent prime-axis blocks. In the full LCM innovation the
denominator exponent is `L_(j-1)`, rather than `p^(k-1)`. The difference is
not a normalization convention: it is precisely the multiplicity and
phase content of the other prime directions. See (GI3). The local formula
is a correct calibration and an Euler-product encoding; it is not the
determinant of the global innovation filtration with all sectors retained.
