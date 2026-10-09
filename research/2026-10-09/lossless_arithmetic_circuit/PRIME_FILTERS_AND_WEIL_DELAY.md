# Prime filters and the completed Weil form as a delay pairing

**Truth state:** the identities below are proved on their stated domains. They provide a circuit normalization of the classical local explicit formula, not a new proof of that formula or of RH. Burnol's conductor and local scattering work already connects local Gamma logarithmic derivatives, time delay, and the explicit formula; see the provenance note.

## 1. Fix the clock and the meaning of lossless

Use a Laplace variable `q` with `Re q>0`; a delay by `L>0` has transfer `exp(-qL)`. Boundary frequency is `q=iu`. For a scalar transfer `b` of boundary modulus one, define its group delay by

\[
\tau_b(u)=-\frac{d}{du}\arg b(iu)
=i\overline{b(iu)}\frac{d}{du}b(iu).
\tag{1}
\]

The derivative is independent of the local choice of phase. With this convention `exp(-qL)` has delay `L`. Some scattering literature uses the opposite frequency convention; the displayed definition controls every sign below.

Lossless on the boundary means norm preservation of the bilateral Fourier multiplier. A causal stable lossless transfer is additionally analytic and contractive in the right Laplace half-plane. These are different statements. Nothing here identifies the archimedean place with a limit of fields Q_p.

## 2. The exact half-density prime filter

For a prime p, put

\[
L_p=\log p,\qquad r_p=p^{-1/2},\qquad w=e^{-qL_p},
\qquad b_p(q)=\frac{w-r_p}{1-r_pw}.
\tag{2}
\]

For `Re q>0`, `|w|<1`. Direct subtraction gives

\[
1-\left|\frac{w-r}{1-rw}\right|^2
=\frac{(1-r^2)(1-|w|^2)}{|1-rw|^2}>0.
\tag{3}
\]

Thus b_p is a causal Schur transfer with unit boundary modulus. Its absolutely summable impulse coefficients are

\[
b_p(q)=-r_p+(1-r_p^2)
\sum_{k\ge1}r_p^{k-1}e^{-qkL_p}.
\tag{4}
\]

This is a coherent feedback filter: an immediate reflected amplitude and an infinite sequence of returns, one prime clock apart. The critical weight and log clock are precisely the inherited half-density and arithmetic length. Equation (3), rather than an analogy, proves its passive transfer property.

There is also a literal positive storage realization. With `c=sqrt(1-r^2)`, use

\[
\binom{x_{n+1}}{y_n}=
\begin{pmatrix}r&c\\c&-r\end{pmatrix}
\binom{x_n}{u_n}.
\]

The matrix is unitary, so `|x_{n+1}|^2+|y_n|^2=|x_n|^2+|u_n|^2`. Its zero-state transfer, with one step lasting `L_p`, is (2). At frequency u and unit incident amplitude, the stored state has squared amplitude `P_r(uL_p)`. Equation (5) is therefore one clock times stored energy.

Let `P_r(theta)=(1-r^2)/(1-2r cos(theta)+r^2)` be the Poisson kernel. Differentiating (2) gives

\[
\tau_{b_p}(u)=L_pP_{r_p}(uL_p)
=L_p\left(1+2\sum_{k\ge1}r_p^k\cos(kuL_p)\right)>0.
\tag{5}
\]

Consequently its delay drop from zero frequency is

\[
\epsilon_p(u):=\tau_{b_p}(0)-\tau_{b_p}(u)
=2L_p\sum_{k\ge1}r_p^k(1-\cos(kuL_p))\ge0.
\tag{6}
\]

This is exactly the previously proved prime-tower energy symbol. Its sign is independent of RH. The sign is special to this filter: group-delay differences of arbitrary all-pass filters need not have their maximum at frequency zero.

### The actual local L-factor ratio contains an advance

For `gamma_p(s)=(1-p^{-s})^{-1}`, define `rho_p(s)=gamma_p(s)/gamma_p(1-s)`. Algebra gives

\[
\rho_p(1/2+q)
=\frac{1-r_pe^{qL_p}}{1-r_pe^{-qL_p}}
=e^{qL_p}b_p(q).
\tag{7}
\]

The actual local scattering ratio is therefore the stable filter with one clock of delay removed. It is still lossless on the boundary, but the advance moves the immediate term to negative time. Its group delay is

\[
\tau_{\rho_p}(u)=\tau_{b_p}(u)-L_p
=2L_p\sum_{k\ge1}r_p^k\cos(kuL_p).
\tag{8}
\]

It can be negative. At `uL_p=pi`, it is `-2L_pr_p/(1+r_p)`. This is a normalization fact about the genuine local factor, not evidence of energy dissipation or of an off-line zero.

### Mixed histories survive connected-source extraction

The cascade `b_2 b_3` has a return at `log 6=log 2+log 3`: by (4), its coefficient is

\[
(1-r_2^2)(1-r_3^2)=\frac12\cdot\frac23=\frac13.
\tag{9}
\]

The connected logarithmic derivative is additive across the cascade and has no mixed-prime frequency. Thus a mixed return in the full transport can coexist with zero mixed-prime charge in a logarithmic source. This is the concrete filter version of the previous RMP distinction between retaining mixed histories and extracting a prime-power source. The Euler logarithmic source vanishes at integers with at least two distinct prime factors; it does not vanish at every composite integer (`Lambda(4)=log 2`).

## 3. The Gamma cascade supplies the other positive delay drop

The companion Gamma note proves that the archimedean local ratio

\[
\rho_\infty(1/2+q)
=\pi^{-q}\frac{\Gamma(1/4+q/2)}{\Gamma(1/4-q/2)}
\tag{10}
\]

is a renormalized infinite cascade with decay rates `lambda_j=2j+1/2`. Its boundary group delay is

\[
\tau_\Gamma(u)=\log\pi-\Re\psi(1/4+iu/2),
\qquad c_\Gamma:=\tau_\Gamma(0)=\log\pi-\psi(1/4).
\tag{11}
\]

Its delay drop is the known Gamma energy symbol,

\[
\alpha(u)=\tau_\Gamma(0)-\tau_\Gamma(u)
=2\sum_{j\ge0}\frac{u^2}{\lambda_j(\lambda_j^2+u^2)}\ge0.
\tag{12}
\]

Equivalently, if `w_Gamma(h)=e^{-h/2}/(1-e^{-2h})`,

\[
\alpha(u)=2\int_0^\infty w_\Gamma(h)(1-\cos(uh))\,dh.
\tag{13}
\]

The finite cascades have positive absolute delay. Their divergent delay subtraction produces (11), whose sign varies with frequency. The difference (12) survives that subtraction and keeps its independent positive sign.

## 4. An exact finite-place formula for the full Weil pairing

Take `f in C_c^infinity(-A,A)`, extend it by zero, and put

\[
\widehat f(u)=\int_{\mathbb R}f(t)e^{-iut}\,dt,
\quad F(h)=\int_{\mathbb R}f(t+h)\overline{f(t)}\,dt,
\quad C(f)=\int\cosh(t/2)f(t)\,dt,
\quad S(f)=\int\sinh(t/2)f(t)\,dt.
\tag{14}
\]

The Fourier sign differs from the positive-exponent notation used in the October7 tangent note, but all the multipliers here are even in u, so the quadratic identities agree exactly. Let `P` be any finite set of primes containing every prime at most `exp(2A)`. Define

\[
U_P(q)=\rho_\infty(1/2+q)\prod_{p\in P}\rho_p(1/2+q),
\tag{15}
\]

and define its boundary group delay by (1). Every factor has boundary modulus one, hence so does U_P. From (8) and (11),

\[
\tau_P(u)=\log\pi-\Re\psi(1/4+iu/2)
+2\sum_{p\in P}(\log p)\sum_{k\ge1}p^{-k/2}\cos(ku\log p).
\tag{16}
\]

**Exact normalized delay identity.** In the inherited Suzuki/Weil convention,

\[
\boxed{
Q_W(f)=2\bigl(|C(f)|^2-|S(f)|^2\bigr)
-\frac1{2\pi}\int_{\mathbb R}\tau_P(u)|\widehat f(u)|^2\,du.
}
\tag{17}
\]

**Proof.** The prime series for each fixed p converges absolutely and uniformly in u, while the Gamma term grows only logarithmically. Since `fhat` is Schwartz, every displayed integral converges. Plancherel gives

\[
\frac1{2\pi}\int\cos(hu)|\widehat f(u)|^2du=\Re F(h).
\]

Thus each prime contributes `-2 sum_k (log p)p^{-k/2} Re F(k log p)`. The correlation vanishes for `|h|>=2A`, so this is precisely the full finite prime-power sum in W, regardless of which additional primes belong to P. By (12)–(13), the Gamma integral is `E_Gamma(f)-c_Gamma||f||^2`, exactly the Gamma and origin contribution already normalized in the October7 and RMP notes. Finally the two polynomial factors of xi contribute `2(|C|^2-|S|^2)`. This proves (17), including the polar and origin terms. No sign has been inferred. □

On the primitive core `C(f)=S(f)=0`, equivalently `int e^{t/2}f=int e^{-t/2}f=0`, (17) reads

\[
Q_W(f)=-\frac1{2\pi}\int\tau_P(u)|\widehat f(u)|^2du.
\tag{18}
\]

This is a sign condition on a restricted family of spectral averages, not the pointwise assertion `tau_P(u)<=0`. In fact `tau_P(0)>0`. The two exponential moments matter; ordinary zero mean is insufficient, as the previous compact Green theorem proved.

The identities also extend to compactly supported `H^1` tests by smooth approximation in a fixed containing window. Indeed `alpha(u)` is bounded by a constant times `1+u^2`, the finite-prime multipliers are bounded, and the polar functionals are continuous on that window. The independent spatial/spectral numerical check uses this extension for a translated tent with known exact autocorrelation and Fourier transform.

## 5. Positive dispersion versus the centered target

Write

\[
M_P=\sum_{p\in P}\frac{(\log p)p^{-1/2}}{1-p^{-1/2}},
\quad E_P(f)=\sum_{p\in P}\sum_{k\ge1}
\frac{\log p}{p^{k/2}}\|f-T_{k\log p}f\|_2^2,
\tag{19}
\]

where `T_hf(t)=f(t-h)`. Equations (6), (12), and Plancherel give

\[
E_\Gamma(f)+E_P(f)
=\frac1{2\pi}\int[\tau_P(0)-\tau_P(u)]|\widehat f(u)|^2du\ge0,
\qquad \tau_P(0)=c_\Gamma+2M_P.
\tag{20}
\]

Accordingly (17) is exactly

\[
\boxed{
Q_W(f)=\underbrace{E_\Gamma(f)+E_P(f)+2|C(f)|^2}_{P_P(f)}
-\underbrace{\bigl[(c_\Gamma+2M_P)\|f\|_2^2+2|S(f)|^2\bigr]}_{D_P(f)}.
}
\tag{21}
\]

Both displayed brackets are positive forms. The independent sign of the delay drop pays for `P_P`; it does not prove that `P_P>=D_P`. This states exactly what the lossless-filter construction contributes and what remains unpaid.

### Relation to the earlier finite-power cutoff

The earlier `E_prime,A` sums only over `p^k<=exp(2A)`. In contrast (19) includes all powers of the finitely many primes in P. Their difference is

\[
E_P(f)-E_{{\rm prime},A}(f)
=2\left(\sum_{p\in P,\ k\log p>2A}\frac{\log p}{p^{k/2}}\right)\|f\|_2^2,
\tag{22}
\]

with the same extra scalar in `2M_P`. It cancels exactly in (21). Boundary equality cases also have zero overlap and may be placed in either term.

### The infinite circuit has local stabilization, not a finite uncentered energy

Once the visible primes have been included, adding a prime `p>exp(2A)` changes both P_P and D_P by precisely

\[
2\frac{(\log p)p^{-1/2}}{1-p^{-1/2}}\|f\|_2^2.
\tag{23}
\]

The centered pairing is unchanged. The positive terms diverge separately as the prime set exhausts all primes; the previous elementary large-jump argument proves this without RH. Therefore no pointwise infinite product or global L2 density is being asserted. Equation (17) is a finite-place identity for each compact test, and (23) provides exact consistency as its place cutoff increases.

One must also distinguish this from formally replacing the product of local ratios by
`Gamma_R(s) zeta(s) / [Gamma_R(1-s) zeta(1-s)]=1`. The two Euler products involved have no common half-plane of absolute convergence. The meromorphic functional-equation identity cannot justify interchanging an infinite local-factor product, its boundary derivative, and these test pairings.

## 6. The operational circuit question

The source-side task is now precise: does arithmetic supply a coherent boundary/history construction for which the *centered* energy (21), with both pole channels, has a positive metric before any sign of Q_W is assumed? Eliminating hidden variables must reproduce the boundary law of `P_P-D_P`; eliminating P_P and subtracting a boundary scalar afterwards is generally a different operation, as the exact two-node counterexample in the companion note shows.

The alternative Suzuki interface is equally precise: identify the already constructed causal arithmetic kernel with its unitary boundary response through a proved bounded causal extension. The existing full tangent then transfers an independent contraction to Q_W. Merely declaring the boundary phase unitary supplies neither this identification nor the centering inequality.
