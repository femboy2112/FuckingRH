# Global innovation theorem and the determinant it actually gives

With all notation fixed in the preceding notes,

\[
 \det(zI-C_{pL}|_{E_{p,L}})
 =\prod_{d\mid M}\Phi_{p^k d}(z)
 =\frac{z^{pL}-1}{z^L-1}.                                    \tag{GI1}
\]

Proof: the old space is reducing and carries `C_L`, so divide the two
characteristic polynomials. Equivalently, multiply the exact conductor
factors in (E2), or the `p-1` twisted blocks in (B2). Their equivalence is
by the explicit intertwiner, not a dimension guess. In determinant-at-zero
convention this is

\[
 \det(I-x C_{pL}|_E)=\frac{1-x^{pL}}{1-x^L}
                    =\sum_{b=0}^{p-1}x^{bL}.                 \tag{GI2}
\]

Let prime powers be listed increasingly as `q_j=p_j^(k_j)`, let `L_0=1`
and `L_j=p_j L_(j-1)`. At the true carrier horizon retain the complete
innovation and assign its birth-prime charge `log p_j`. Its determinant is

\[
 Z_N^{\rm mix}(s)=\prod_{q_j\le N}
 \frac{1-p_j^{-sL_j}}{1-p_j^{-sL_{j-1}}}.                      \tag{GI3}
\]

**Theorem GI.** This product converges locally uniformly to a holomorphic
zero-free function on `Re s>0`. It is not `zeta(s)` on `Re s>1`.

For a compact set with `Re s>=delta>0`, write
`y_j=p_j^(-s L_(j-1))`. Since `L_(j-1)>=2^(j-1)`,

\[
 |\text{factor}_j-1|\le\frac{2^{-\delta 2^{j-1}}}
                                  {1-2^{-\delta 2^{j-1}}}.
\]

This is summable. Each polynomial factor has all its zeros on `Re s=0`;
the usual convergent-product argument (choose the logarithm of the small
tail near one) proves nonvanishing. Already the second event, `q=3`, has
factor `1+3^(-2s)+3^(-4s)`, whereas the local prime block is
`1+3^(-s)+3^(-2s)`. More quantitatively, as real `s -> +infinity`, (GI3) is
`1+2^(-s)+O(9^(-s))`: all subsequent bases are at least 9, with the displayed
double-exponential summable bound controlling the tail. In contrast
`zeta(s)=1+2^(-s)+3^(-s)+O(4^(-s))`. The functions differ.

For a common parameter `x`, without the varying prime charge, the full
product telescopes instead to `(1-x^(L(N)))/(1-x)`, tending to `1/(1-x)`
for `|x|<1`. Thus neither natural scalar choice supplies the Euler product
while retaining the global innovation multiplicities.

**Scope.** This excludes the prescribed full-innovation determinant, not
every mixed-conductor interaction or regularized trace. The next construction
must change the interaction/observation or spectral weighting and prove why.
Deleting the mixed factors to obtain the desired answer is not that theorem.
