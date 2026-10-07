# Logarithmic bathtub bound and sharp arithmetic shift gaps

**Date:** 2026-10-07  
**Branch:** \`research/rh-log-bathtub-prime-shift-2026-10-07\`  
**Status:** exact unconditional finite-horizon theorems. **RH remains open.**

This note improves the previously proved lower bound for the positive part of Suzuki's localized Weil form from \(\frac12\log n-O(1)\) to \(\log n-O(1)\), and adds a source-sensitive sharp Poincaré gap for every prime-power translation. These are genuine operator estimates; they are **not** a proof of the remaining sign inequality.

The underlying phase-space/bathtub principle and finite-chain sine eigenvectors are standard. The application and explicit constants concern the arithmetic operator of this repository.

## 1. Exact operator from the audited Suzuki normalization

Let \(I=(-a,a)\), \(a>0\), and let \(f_0\) be the zero extension of \(f\in C_c^\infty(I)\).

Write

\[
E_R(f)=\frac14\int_{-R}^R\frac{\|f_0(\cdot+h)-f_0\|_{L^2(\mathbb R)}^2}{|h|}\,dh.
\]

The already-audited zero-extension theorem gives

\[
L_a(f)=E_{2a}(f)-\log(2a)\|f\|_2^2,
\]

where \(L_a\) is Suzuki's complete logarithmic difference **plus** logarithmic boundary potential.

The exact Weil form is

\[
Q_W^a(f)=P_a(f)-\langle D_af,f\rangle,
\]

\[
\boxed{
P_a(f)=E_{2a}(f)+
\sum_{\substack{q=p^k\\q\le e^{2a}}}
w_q\|f_0-\tau_{\log q}f_0\|_2^2,
\quad
w_q=\frac{\log p}{\sqrt q}.
}
\]

The bounded, fully source-determined remainder is

\[
D_a=(\mathcal V_a+\log(2a))I+R_a.
\]

Let \(\lambda_1(P_a)\le\lambda_2(P_a)\le\cdots\) be the ordered eigenvalues of the Friedrichs operator; compact resolvent was established in the parent note and also follows from the known Suzuki/Connes–Consani–Moscovici theory.

## 2. Fourier symbol and the bathtub principle

With the unitary-normalized Fourier density \(\rho_f(\xi)=|\widehat{f_0}(\xi)|^2/(2\pi)\),

\[
\boxed{
P_a(f)=\int_\mathbb R
F_a(\xi)\rho_f(\xi)\,d\xi,
}
\]

where

\[
\boxed{
F_a(\xi)=m_{2a}(\xi)+2\sum_{q\le e^{2a}}w_q(1-\cos(\xi\log q))
}
\]

and

\[
m_R(\xi)=\int_0^R\frac{1-\cos(h\xi)}h\,dh
=\gamma+\log(R|\xi|)-\mathrm{Ci}(R|\xi|).
\]

Here \(m_R(0)=0\), and \(m_R\) increases with \(|\xi|\) because

\[
\frac{d}{d|\xi|}m_R(\xi)=\frac{1-\cos(R|\xi|)}{|\xi|}\ge0.
\]

For any \(n\) orthonormal functions \(f_1,\dots,f_n\) in \(L^2(I)\), put

\[
\rho(\xi)=\sum_{j=1}^n\frac{|\widehat f_j(\xi)|^2}{2\pi}.
\]

Bessel's inequality applied to \(x\mapsto e^{-i\xi x}\) on \(I\) gives

\[
\boxed{
0\le\rho(\xi)\le\frac{|I|}{2\pi}=\frac a\pi,
\quad
\int_\mathbb R\rho(\xi)\,d\xi=n.
}
\]

The minimum of \(\int m_{2a}\rho\) with only these constraints is achieved by filling the lowest-frequency interval \([-B,B]\), where

\[
B=\frac{\pi n}{2a}.
\]

This is the elementary bathtub/rearrangement principle.

Hence

\[
\sum_{j=1}^n P_a(f_j)\ge
\frac a\pi\int_{-B}^B m_{2a}(\xi)\,d\xi.
\]

The elementary antiderivative is

\[
\int_0^B m_R(\xi)\,d\xi
=
B(m_R(B)-1)+\frac{\sin(RB)}R.
\]

Since \(RB=\pi n\), the sine term vanishes.

The Ky Fan minimum principle and \(\lambda_n\ge n^{-1}\sum_{j=1}^n\lambda_j\) prove:

### Theorem A: the sharp-coefficient logarithmic lower bound

\[
\boxed{
\sum_{j=1}^n\lambda_j(P_a)
\ge
n\left[
\gamma+\log(\pi n)-\mathrm{Ci}(\pi n)-1
\right].
}
\]

In particular,

\[
\boxed{
\lambda_n(P_a)
\ge
\gamma+\log(\pi n)-\mathrm{Ci}(\pi n)-1.
}
\]

The right side is independent of \(a\) and the primes.

It improves the prior \(\frac12\log n-O(1)\) lower bound to

\[
\boxed{\lambda_n(P_a)\ge\log n-O(1).}
\]

This estimate follows entirely from the **positive** source form and does not presume any RH sign.

## 3. Sharp support-limited Poincaré constant for a translated prime ray

Let \(I\) have width \(W=2a\), \(h>0\), and let \(f_0\) be zero extended.

Define

\[
N_h=\left\lceil\frac W h\right\rceil.
\]

### Theorem B: exact finite-chain translation constant

\[
\boxed{
\sup_{0\ne f\in L^2(I)}
\frac{\Re\langle f_0,\tau_h f_0\rangle}{\|f\|_2^2}
=
\cos\frac{\pi}{N_h+1}.
}
\]

Consequently

\[
\boxed{
\|f_0-\tau_hf_0\|_2^2
\ge
2\left(1-\cos\frac{\pi}{N_h+1}\right)\|f\|_2^2.
}
\]

Proof: decompose the interval along the residue coordinate modulo \(h\). Each fiber is a finite chain

\[
r,\ r+h,\ldots,r+(N(r)-1)h
\]

of length \(N(r)\le N_h\). The symmetrized shift on a fiber is the Jacobi/path matrix with off-diagonal \(1/2\); its largest eigenvalue is \(\cos(\pi/(N(r)+1))\) with discrete sine eigenvector. Fibers of maximal length have positive measure, hence the essential supremum is the stated number and the bound is optimal. For \(h\ge W\), \(N_h=1\) and the overlap vanishes exactly.

This is a rigorous expression of the maximum possible coherence of one prime-ray shift given finite support.

## 4. Source-sensitive arithmetic spectral floor

Apply Theorem B at each active \(q=p^k\), with \(h_q=\log q\). Define the computable scalar

\[
\boxed{
\mathfrak g_a=
2\sum_{\substack{q=p^k\\q\le e^{2a}}}
\frac{\log p}{\sqrt q}
\left[
1-\cos\frac{\pi}{\lceil 2a/\log q\rceil+1}
\right].
}
\]

Then

\[
E_{{\rm prime},a}(f)\ge\mathfrak g_a\|f\|_2^2.
\]

Combining with Theorem A and the min–max principle yields:

### Theorem C: improved explicit completed-Well eigenvalue bound

\[
\boxed{
\lambda_n(Q_W^a)
\ge
\gamma+\log(\pi n)-\mathrm{Ci}(\pi n)-1
+\mathfrak g_a-\|D_a\|.
}
\]

This is the direct arithmetic strengthening of the former zero-extension theorem.

For \(n\ge1\), the elementary estimate \(|\mathrm{Ci}(\pi n)|<1\) gives the sufficient positivity threshold

\[
\boxed{
n>
\frac1\pi\exp\!\left(
\|D_a\|-\mathfrak g_a+2-\gamma
\right)
\quad\Longrightarrow\quad
\lambda_n(Q_W^a)>0.
}
\]

Thus the dimension of the possibly nonpositive sector is explicitly bounded above by the number of positive integers below that threshold. Compared with the previous exponent \(2\|D_a\|\), the new coefficient is \(1\), and the arithmetic shift floor subtracts \(\mathfrak g_a\) in the exponent.

Every finite-horizon Feshbach reduction from the parent theorem remains valid, now with a strictly smaller certified low-mode budget.

## 5. More faithful arithmetic phase-space rearrangement

Theorem A discarded the nonnegative prime part to retain a closed form. We can instead use the full symbol \(F_a\).

For a measurable nonnegative \(F\), define its increasing rearrangement \(F^\uparrow\) with respect to frequency measure \(a\,d\xi/\pi\). That is, \(F^\uparrow(u)\) is the nondecreasing quantile whose sublevel mass is

\[
\frac a\pi
\operatorname{Leb}\{\xi:F(\xi)\le y\}.
\]

Then the same bathtub principle gives the **exact, source-sensitive** bound

\[
\boxed{
\sum_{j=1}^n\lambda_j(P_a)
\ge
\int_0^n F_a^\uparrow(u)\,du.
}
\]

Hence

\[
\boxed{
\lambda_n(Q_W^a)
\ge
\frac1n\int_0^nF_a^\uparrow(u)\,du-\|D_a\|.
}
\]

This is a potentially stronger arithmetic estimate than Theorem C, but its effective certification requires controlling the sublevel-set geometry of

\[
m_{2a}(\xi)+2\sum_{q}w_q(1-\cos(\xi\log q)).
\]

The latter is exactly a weighted simultaneous prime-phase resonance problem.

It is **not** legitimate to assume equidistribution uniformly over all frequencies: almost-periodic recurrences make that false in operator norm.

## 6. Asymptotic size of the individual prime shift floor

Let

\[
S_a=\sum_{q\le e^{2a}}w_q.
\]

The weighted prime number theorem gives

\[
S_a\sim 2e^a.
\]

For every fixed \(w>0\), prime powers with \(\log q=2a-w\) satisfy

\[
\left\lceil\frac{2a}{\log q}\right\rceil=2
\]

once \(a\) is large. Their individual Poincaré factor is therefore

\[
2(1-\cos(\pi/3))=1.
\]

The normalized source mass is asymptotically concentrated in an \(O(1)\) boundary window \(2a-\log q=O(1)\). Dominated convergence plus PNT therefore gives

\[
\boxed{
\mathfrak g_a\sim S_a\sim2e^a.
}
\]

In particular the sum of individually sharp shift gaps accounts asymptotically for one half of the raw prime difference-square diagonal mass \(2S_a\).

This **does not** mean that the remaining half must be provided by a guessed curvature term. It quantifies exactly why separate-prime lower bounds are insufficient by themselves and why collective boundary interactions and pole/Archimedean cancellation are load-bearing.

## 7. What is and is not achieved

**DISCLOSED, zero-free:** Theorem A (unit coefficient logarithmic eigenvalue lower bound); Theorem B (sharp finite support shift coherence); Theorem C (arithmetic spectral floor and improved finite negative-index bound); the exact full-symbol bathtub inequality; the PNT asymptotic \(\mathfrak g_a\sim2e^a\).

**NOT NEW PRIORITY CLAIM:** Fourier-density/bathtub bounds, finite path-graph eigenvalues, and the PNT are established. The present application yields explicit constraints for Suzuki's completed form.

**UNVERIFIED:** a uniformly positive low-energy Feshbach matrix for all \(a\). The phase-space rearrangement is not known to give it.

**RH remains OPEN.**

## 8. Next seam

The Fourier symbol makes the surviving arithmetic challenge unusually explicit:

\[
F_a(\xi)
=
m_{2a}(\xi)
+
2\sum_{q\le e^{2a}}w_q(1-\cos(\xi\log q)).
\]

The first term suppresses very high-frequency almost-periodic recurrences; the second detects genuine prime-log phase alignment. A successful estimate must use their **joint sublevel geometry** and must also account for the independently fixed \(D_a\).

Do not approximate the prime phases by independent randomness or claim that a finite phase-grid check controls all frequencies.
