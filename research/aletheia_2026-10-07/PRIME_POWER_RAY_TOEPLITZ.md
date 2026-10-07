> **2026-10-07 provenance:** The AR(1)/Kac–Murdock–Szegő Toeplitz covariance `(r^{|i-j|})` and tridiagonal precision matrix are **classical**, not an RH discovery. This finite Suzuki prime-ray application first entered at `2e18621f6d3e802034f65cc8b937862811dfc58f` and was independently checked numerically for the stated finite cases. Correctly distinguish exact finite gap from the unresolved collective cross-prime/Gamma form. [Claim ledger PV-2026-004](../audits/2026-10-07/RH_CLAIM_PROVENANCE_LEDGER.md).

# Exact prime-power ray compression: AR(1) Toeplitz covariance and tridiagonal inverse

**Date:** 2026-10-07  
**Branch:** \`research/rh-log-bathtub-prime-shift-2026-10-07\`  
**Status:** exact finite-source operator theorem with sharp prime-tower gap. **RH remains OPEN.**

The independent-shift Poincaré bound in LOG_BATHTUB_PRIME_SHIFT_BOUND.md discards all correlations between the \(p,p^2,p^3,\ldots\) translations along the **same prime axis**.

They can be retained **exactly**. The critical half-density \(p^{-k/2}\) is geometric in the prime-depth index. Once we decompose a bounded spatial interval into residue fibers modulo \(\log p\), the entire \(p\)-power Dirichlet form becomes a single Kac–Murdock–Szegő covariance matrix. Its inverse is tridiagonal.

This is a substantial compression of the SUCC/FUCC prime-ray problem: no infinite tower or giant LCM clock is required to compute its exact finite support gap.

## 1. One prime ray

Fix \(p\) prime and let

\[
h=\log p,\qquad
r=p^{-1/2}\in(0,1).
\]

For a horizon interval \(I=(-a,a)\) of width \(W=2a\), let

\[
K=\left\lfloor\frac W h\right\rfloor,\qquad
N=\left\lceil\frac W h\right\rceil.
\]

The active \(p\)-powers are \(p,p^2,\ldots,p^K\) (interpret equality at the threshold in the closed sense). Their exact Suzuki half-density weights are

\[
\boxed{
w_{p,k}=h\,r^k.
}
\]

Let

\[
S_p=h\sum_{k=1}^{K}r^k
=h\,\frac{r(1-r^K)}{1-r}.
\]

Define the full prime-ray form

\[
\boxed{
\mathcal E_{p,a}(f)
=
\sum_{k=1}^{K}
hr^k\,
\|f_0-\tau_{kh}f_0\|^2.
}
\]

The zero extension is to \(L^2(\mathbb R)\).

## 2. Fiber decomposition

Choose a residue coordinate \(s\in[0,h)\). A real point in the interval has the form \(s+jh\).

For almost every \(s\), the admissible \(j\)'s form a consecutive chain of length

\[
N(s)\le N.
\]

A positive-measure set of fibers realizes the maximal length \(N\).

Under the unitary direct-integral decomposition

\[
L^2(I)
\cong
\int_{[0,h)}^\oplus\mathbb C^{N(s)}\,ds,
\]

translation by \(kh\) acts as the \(k\)-step unilateral shift \(J_{N(s)}^k\) between nodes of that chain.

Therefore the form on a fiber of length \(d=N(s)\) is

\[
\boxed{
G_{p,d}
=
2S_pI_d
-h\sum_{k=1}^{K}
r^k\bigl(J_d^k+(J_d^*)^k\bigr).
}
\]

Since \(K\ge N-1\) (with the endpoint convention) and \(d\le N\), every off-diagonal \(k=|i-j|\) is present.

Define the positive Toeplitz correlation matrix

\[
\boxed{
C_d(r)=\bigl(r^{|i-j|}\bigr)_{1\le i,j\le d}.
}
\]

Then the entire prime-power ray is

\[
\boxed{
G_{p,d}
=
(2S_p+h)I_d-h\,C_d(r).
}
\]

This is **exact**, not a spectral approximation.

## 3. Sharp finite prime-tower gap

Because the fiber matrices \(G_{p,d}\) are principal compressions of \(G_{p,N}\), Cauchy interlacing gives

\[
\lambda_{\min}(G_{p,d})\ge\lambda_{\min}(G_{p,N}).
\]

The maximal chain \(N\) occurs on a set of positive residue measure, so the resulting constant is sharp.

### Theorem

\[
\boxed{
\gamma_p(a)
:=
\inf_{f\ne0}
\frac{\mathcal E_{p,a}(f)}{\|f\|_2^2}
=
2S_p+h-h\,\lambda_{\max}\!\left(C_N(r)\right).
}
\]

Thus

\[
\boxed{
\mathcal E_{p,a}(f)\ge\gamma_p(a)\|f\|_2^2
}
\]

with equality in the spectral-infimum sense.

There is no RH assumption.

### Exact tridiagonal inversion

For \(N\ge2\),

\[
\boxed{
C_N(r)^{-1}
=
\frac1{1-r^2}
\begin{pmatrix}
1&-r&&\\
-r&1+r^2&-r&\\
&\ddots&\ddots&\ddots\\
&&-r&1
\end{pmatrix}.
}
\]

For \(N=1\), \(C_1=[1]\).

Therefore \(\gamma_p(a)\) is determined by the smallest eigenvalue of a **tridiagonal Jacobi operator**, computable in \(O(N)\)-scale work using bisection/Sturm or standard tridiagonal eigensolvers.

The geometric prime depth has become an exact finite AR(1) covariance problem.

## 4. Strengthen the full Weil positive part

Sum the sharp prime-ray gaps:

\[
\boxed{
\Gamma_a
=
\sum_{p\le e^{2a}}\gamma_p(a).
}
\]

Because each prime ray contributes nonnegatively,

\[
\boxed{
E_{\rm prime,a}(f)
=
\sum_p\mathcal E_{p,a}(f)
\ge
\Gamma_a\|f\|_2^2.
}
\]

This improves the former independent-shift floor \(\mathfrak g_a\), because for every prime

\[
\gamma_p(a)
\ge
2\sum_{k\le K}
w_{p,k}
\left(
1-\cos\frac{\pi}{\lceil W/(kh)\rceil+1}
\right).
\]

The inequality is generally strict for primes with at least two active depths.

Combining with the earlier logarithmic bathtub bound gives

\[
\boxed{
\lambda_n(Q_W^a)
\ge
\gamma+\log(\pi n)-\operatorname{Ci}(\pi n)-1
+\Gamma_a-\|D_a\|.
}
\]

This is an explicit **prime-tower-aware** lower bound on every ordered eigenvalue of the completed finite Weil form.

It is again a lower bound, not the missing positivity proof.

## 5. Fixed-prime large-horizon behavior

The infinite Toeplitz covariance symbol is

\[
C_\infty(\theta)
=
\frac{1-r^2}{1-2r\cos\theta+r^2},
\]

with maximum

\[
\frac{1+r}{1-r}.
\]

Also

\[
S_p\longrightarrow \frac{hr}{1-r}
\qquad(a\to\infty).
\]

The leading constant in \(\gamma_p(a)\) cancels:

\[
2\frac{hr}{1-r}+h-h\frac{1+r}{1-r}=0.
\]

Thus

\[
\boxed{
\gamma_p(a)\longrightarrow0
}
\]

for each fixed prime. This is necessary: a fixed translation ray has no positive Poincaré gap on the full real line.

More quantitatively, the \(k=1\) term gives

\[
\gamma_p(a)
\ge
2hr\left(1-\cos\frac{\pi}{N+1}\right)
=\Omega_p(N^{-2}).
\]

A discrete sine test vector in the maximal fiber gives an **explicit upper bound**. Let

\[
v_j=\sqrt{\frac2{N+1}}\sin\frac{\pi j}{N+1},
\qquad j=1,\dots,N,
\]

and extend the chain by zero to \(\mathbb Z\). Then

\[
\|v-S^k v\|_2
\le k\|v-Sv\|_2,
\qquad
\|v-Sv\|_2^2=2\left(1-\cos\frac{\pi}{N+1}\right).
\]

Since

\[
\sum_{k\ge1}k^2r^k=\frac{r(1+r)}{(1-r)^3},
\]

the sharp Rayleigh infimum obeys

\[
\boxed{
\gamma_p(a)\le
2h\left(1-\cos\frac{\pi}{N+1}\right)
\frac{r(1+r)}{(1-r)^3}.
}
\]

In particular \(\gamma_p(a)=O_p(N^{-2})\) as \(N\to\infty\). Hence

\[
\boxed{
\gamma_p(a)=\Theta_p(a^{-2})
}
\]

at fixed \(p\).

No all-horizon prime-by-prime gap can prove RH. The proof must exploit **joint, changing-prime interactions** and the completed pole/Gamma sector.

## 6. Computable finite examples

Exact eigensolver checks in the accompanying script reproduce:

| Prime \(p\) | Horizon \(a\) | \(N\) | Exact ray gap | Sum of individual shift gaps |
|---:|---:|---:|---:|---:|
| 2 | 2 | 6 | 1.049363289 | 0.840977781 |
| 2 | 3 | 9 | 0.949597207 | 0.699669396 |
| 3 | 2 | 4 | 0.978392194 | 0.819907098 |
| 5 | 3 | 4 | 0.858642266 | 0.740764903 |

These are finite calculations, not global estimates. They explicitly demonstrate strict improvement from preserving within-ray correlations.

## 7. Relation to the user's actualization geometry

The minimal support chain along \(p\) is

\[
1\to p\to p^2\to\cdots.
\]

The half-density weights are geometric, making the full overlap Gram a Markov/AR(1) covariance. The tridiagonal inverse is a nearest-neighbor **precision/connection** operator on prime depth.

This is a precise form of the idea that higher actualizations inherit the earlier state and interact through a minimal local connection. It uses established operator algebra, not a physical quantum or gravitational assertion.

## 8. Proof status

**DISCLOSED:** exact direct-integral prime-fiber model; Toeplitz covariance identity; sharp finite-horizon gap; tridiagonal inverse; stronger full Weil eigenvalue bound.

**STANDARD TOOLS:** residue fibers, Cauchy interlacing, Kac–Murdock–Szegő covariance, finite Jacobi spectra.

**UNVERIFIED:** a sufficiently sharp collective across-prime estimate or all-horizon positive Weil/Feshbach matrix.

**RH:** OPEN.


---

## Addendum — exact identification with the Euler local Weyl/Poisson channel

The matrix

\[
C_N(r)=(r^{|i-j|})_{1\le i,j\le N}
\]

is the \(N\)-section of the Toeplitz operator with symbol

\[
\boxed{
P_r(\theta)
=
\frac{1-r^2}{1-2r\cos\theta+r^2}
=
\Re\frac{1+re^{i\theta}}{1-re^{i\theta}}.
}
\]

But the existing repository note
\`research/aletheia_2026-10-06/EULER_AS_CENTERED_WEYL_SUM.md\`
already identified

\[
\frac{1+q_p(z)}{1-q_p(z)},
\qquad
q_p(z)=p^{-1/2+iz},
\]

as the prime-local positive-real Weyl response. On the real spectral axis, with \(\theta=z\log p\), its real part is precisely \(P_{p^{-1/2}}(\theta)\).

Therefore we have an exact identification across three constructions:

\[
\boxed{
\text{Euler local Cayley/Weyl response}
=
\text{Poisson covariance symbol}
=
\text{finite prime-depth AR(1) Toeplitz Gram}.
}
\]

This is a **consistency closure**, not an independently new proof of a prime positivity property. What is new to the current finite-boundary analysis is the explicit exact Dirichlet chain compression and the resulting sharp gap \(\gamma_p(a)\).

The global obstruction is unchanged: centering/summing these otherwise positive local Weyl channels together with the signed Archimedean/pole completion does **not** automatically preserve positive-realness.


---

## Addendum — exact closed finite-ray Fourier symbol

The full positive Fourier symbol of the finite Weil parent is

\[
F_a(\xi)
=
m_{2a}(\xi)
+
\sum_{p\le e^{2a}}F_{p,a}(\xi).
\]

Let

\[
h_p=\log p,\quad
r_p=p^{-1/2},\quad
K_p=\left\lfloor\frac{2a}{h_p}\right\rfloor,\quad
z_p=r_pe^{i\xi h_p}.
\]

The entire \(p\)-power contribution is the finite geometric expression

\[
\boxed{
F_{p,a}(\xi)
=
2h_p\left[
\frac{r_p(1-r_p^{K_p})}{1-r_p}
-
\Re\frac{z_p(1-z_p^{K_p})}{1-z_p}
\right].
}
\]

This follows exactly from

\[
F_{p,a}(\xi)
=
2h_p\sum_{k=1}^{K_p}
r_p^k(1-\cos(kh_p\xi)).
\]

No prime-power iteration is needed in the frequency evaluation: the entire ray is represented by one rational expression.

In the infinite-depth limit for fixed \(p\),

\[
\boxed{
F_{p,\infty}(\xi)
=
h_p\left[
\frac{1+r_p}{1-r_p}
-
\frac{1-r_p^2}{1-2r_p\cos(\xi h_p)+r_p^2}
\right].
}
\]

The second fraction is exactly the Poisson/Weyl symbol from the previous addendum.

This provides an exact starting point for the **joint-prime phase-space sublevel problem** in LOG_BATHTUB_PRIME_SHIFT_BOUND.md. It does not turn positivity of the *completed* Weil form into an elementary per-prime fact, because the required signed diagonal/pole/Gamma terms have not vanished.
