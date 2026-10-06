# The local factor B_p IS a carry-response filter (major local theorem)

**Date:** 2026-10-06. **Status:** DISCLOSED, verified `scripts/local_bp_from_carry.py`. RH open.
Turns the Round-004 spectral factor C90 into a literal carry/depth-recursion operator.

## 1. Carry-depth records are von Mangoldt (§7)

In the LCM clock, the p-carry record depth is $R_p(N)=v_p(\operatorname{lcm}(1..N))=\lfloor\log_pN\rfloor$,
so $R_p(N)-R_p(N-1)=\mathbf 1[N=p^k]$ and
\[
\boxed{\ \sum_p(\log p)\,[R_p(N)-R_p(N-1)]=\Lambda(N)\ }\qquad(\text{verified }N=2..299,\ 0\text{ violations}).
\]
*Prime birth* = a new clock survives the sieve; *prime power* $p^k$ = a new record carry depth;
$\Lambda$ = the record-carry update cost. (Carry-machine form of the LCM-memory result.)

## 2. Half-density is forced by the Haar cylinder (§12)

The p-adic depth chain uses cylinders $p^k\mathbb Z_p$ with $\mathrm{Haar}(p^k\mathbb Z_p)=p^{-k}$, hence
amplitude $p^{-k/2}$. The unit depth-states $\phi_{p,k}=p^{k/2}\mathbf1_{p^k\mathbb Z_p}$ satisfy
$\langle\phi_{p,k},\phi_{p,\ell}\rangle=p^{-|k-\ell|/2}=r^{|k-\ell|}$, $r=p^{-1/2}$ — an exact AR(1)/depth
covariance (verified to machine zero, p=2,3,5). **The ratio $r=p^{-1/2}$ is the cylinder amplitude ratio,
not an inserted constant.**

## 3. B_p is the carry-response filter (§11) — exact operator form of C90

Let $U_{\rm depth}$ be the p-adic depth-shift (one level $k\to k+1$ = one carry wrap), symbol
$z=e^{i\theta}$, $\theta=\log p\,\xi$. Then
\[
\boxed{\ B_p=c_p\,(I-U_{\rm depth})\,(I-p^{-1/2}U_{\rm depth})^{-1},\qquad c_p^2=\frac{\log p}{\pi}\,\frac{r(1+r)}{1-r},\ }
\]
and its power spectrum reproduces the Round-004 density **exactly**:
\[
c_p^2\,|H_p(z)|^2=c_p^2\frac{|1-z|^2}{|1-rz|^2}=\sigma_p(\xi)\qquad(\text{ratio }\sigma_p/|H_p|^2\text{ constant to }10^{-10}).
\]
- $(I-U_{\rm depth})$ = **carry / wrap innovation** (the edge detector $1-z$);
- $(I-p^{-1/2}U_{\rm depth})^{-1}$ = **geometric depth memory** (the Euler/Poisson whitening $(1-rz)^{-1}$, C06);
- $c_p$ carries the von-Mangoldt weight $\log p$ and the half-density.

So the local Route-B factor is a one-line carry filter: *detect the wrap, remember the depth with the
Haar half-density, weight by the record cost.* The entire local layer of the program is now derived from
the carry machine with no spectral input. The hard part remains global (how the $B_p$ share a coarse
channel), addressed next in SHARED_DC_RENORMALIZATION.
