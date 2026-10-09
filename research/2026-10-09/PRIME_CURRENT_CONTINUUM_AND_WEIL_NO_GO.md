# Prime current -> continuum: an exact PNT limit, an RH-rate criterion, and a completed-sign no-go

**Date:** 2026-10-09. **Parent:** main at 344facc9b9eccadcf7fe98af9361b6e7fd3ea737 (Round 066). **Status:** classical theorems sharpened as source/limit diagnostics plus an unconditional counterexample to naive continuum replacement; **RH OPEN**. No zeta zeros are used in the constructions or scripts. This note makes no novelty claim for PNT, von Koch, Bohr orthogonality, or Suzuki's explicit formula.

## 0. User hypothesis, and our proposed mathematical test

The user proposes the Archimedean place as an idealized, closed, coherent "superconducting" description of infinitely many prime currents flowing through the finite SUCC/FUCC arithmetic circuit. Preserve this as a *scale/representation-change heuristic*, not literal zero-resistance physics: actual superconductors have finite critical current, and the real place is a distinct completion of Q, not literally p→infinity.

Our falsifiable mathematical reading: does the true source
rho = sum_(p,k>=1) (log p)/p^(k/2) delta_(k log p)
(a) homogenize after macroscopic scaling; (b) retain the arithmetic/phase data; (c) substitute for the prime source inside the actual Suzuki completion with a correct global sign? Outcomes predicted before probe: (a) YES by PNT, (b) NO for coarse limit, (c) NO because positive completed sign needs the exact prime impulses. Source mutation controls and a fake-all-integer source should distinguish (a) from source fidelity.

This is **distinct** from main's Round 066 zero-spacing diagnostic (which used a finite zero list after the fact); the proofs and tests here read only prime powers, PNT, Gamma, and the original Suzuki source formula. Main's wiki and Round 066 (and earlier Round 010 PNT cancellation) already caution that continuum/closure is sign-blind.

## 1. Source measure and continuum homogenization — unconditional theorem

Let Lambda(n)=log p for n=p^k, zero otherwise. On u>=0 define the locally finite measure

  rho = sum_(n>=2) Lambda(n)/sqrt(n) delta_(log n).

Let J(T)=rho([0,T])=sum_(n<=e^T) Lambda(n)/sqrt(n).

**Theorem (PNT pushforward).** For each finite interval [a,b] in real log displacement with a<b,

  lim_(T->infinity) e^(-T/2) rho([T+a,T+b])
    = 2(e^(b/2)-e^(a/2))
    = integral_a^b e^(u/2) du.

In particular J(T)=2e^(T/2)+o(e^(T/2)). On smooth compactly supported test functions, the shifted normalized measures converge vaguely to e^(u/2)du.

**Proof.** With psi(x)=sum_(n<=x) Lambda(n), the prime number theorem is psi(x)=x+o(x). Then rho([T+a,T+b]) equals integral_(e^(T+a),e^(T+b)] x^(-1/2)d psi(x). Stieltjes partial summation (PNT applied at both endpoints and to the integral) yields 2(e^((T+b)/2)-e^((T+a)/2))+o(e^(T/2)). Divide by e^(T/2). QED.

**What this means.** The finite prime-power current has a precise smooth macroscopic envelope. It is NOT the local archimedean Gamma factor; this envelope is a consequence of the PNT/pole at s=1, while Gamma comes from the independent real local Gaussian/Mellin integral.

## 2. How much of RH is in the convergence rate?

Use the SOURCE-INDEPENDENT continuum measure lambda=e^(u/2)1_(u>=0)du, and let

  D(T) = (rho-lambda)([0,T])
       = J(T) - 2(e^(T/2)-1).

**Theorem (exact restatement, not a new proof).**

  RH <=> D(T)=O((1+T)^3) as T->infinity.

**RH -> rate.** The classical von Koch bound under RH is psi(x)-x=O(sqrt(x)log²x). Since psi(1)=0, write E(x)=psi(x)-(x-1). Stieltjes integration by parts gives, x=e^T,

  D(T)=E(x)/sqrt(x) + (1/2) integral_1^x E(t)t^(-3/2)dt.

Therefore D(T)=O((1+T)^3).

**rate -> RH.** For Re w>1/2, the Laplace transform of the discrepancy measure is

  C(w) = integral_0^infinity e^(-wu) d(rho-lambda)(u)
       = -zeta'/zeta(1/2+w) - 1/(w-1/2).

Since D(0)=0, integration by parts gives

  C(w)=w integral_0^infinity e^(-wT)D(T)dT.

If D(T)=O((1+T)^3), this last integral gives a holomorphic extension to Re w>0, initially identical to the Euler-region expression. The pole at w=1/2 is already cancelled; any nontrivial zero with Re s>1/2 would yield an uncancelled pole of -zeta'/zeta(1/2+w). Thus there are none. The functional equation then forces all nontrivial zeros onto Re s=1/2. QED.

**Interpretation:** PNT supplies macroscopic continuous flow. RH demands a *critical rate* of approach. This is an RH equivalent estimate, and no positivity mechanism has been derived.

## 3. Microscopically the current has no finite Bohr mean-square limit

For each X>=2, define the prime-phase finite trigonometric polynomial

  S_X(t)=sum_(n<=X) Lambda(n)/sqrt(n) exp(-it log n).

By distinct-frequency orthogonality,

  lim_(R->infinity) (1/(2R)) integral_(-R)^R |S_X(t)|²dt
    = sum_(n<=X) Lambda(n)²/n.

The higher powers k>=2 contribute a finite total, while PNT and partial summation yield

  sum_(p<=X) (log p)²/p ~ (log X)²/2.

Hence ||S_X||_(Bohr-mean L²) ~ (log X)/sqrt(2), which DIVERGES. The "unrestricted superconducting current" is not literally a finite-energy Hilbert-space infinite sum. A cutoff, distributional topology, or justified renormalization is necessary.

## 4. Exact no-go: replace the source by its continuum, lose Suzuki positivity

Use Suzuki's explicitly normalized time-domain arithmetic/archimedean function, t>=0:

  Psi(t)=A(t)-integral_0^t (t-u)rho(du),

  A(t)=4(e^(t/2)+e^(-t/2)-2)+b t+G(t),

  b=[digamma(1/4)-log(pi)]/2,

  G(t)=sum_(m>=0) [1-e^(-(2m+1/2)t)]/(2m+1/2)^2.

In the exact source formula, RH <=> Psi(t)>=0 for all t (Suzuki, 2023). This is NOT a positive function proven here for all t.

Replace *only* rho by its homogenized continuum lambda=e^(u/2)du, holding the true Gamma and pole terms fixed. Since

  integral_0^t (t-u)e^(u/2)du=4(e^(t/2)-1)-2t,

the resulting completed function is **exactly**

  Psi_cont(t)=4(e^(-t/2)-1)+(b+2)t+G(t).

Use b+2=-0.68609170961283279...<0 and 0<=G(t)<=C/4,
C=zeta_Hurwitz(2,1/4), C/4=4.29933228862677768... . Thus

  Psi_cont(t) <= 4(e^(-t/2)-1)+(b+2)t+C/4.

The right side is strictly decreasing for t>=0 and already < -0.86 at t=3. Consequently

  **Psi_cont(t)<0 for EVERY t>=3, unconditionally.**

This is a decisive falsifier of "the Archimedean smooth bulk can replace the discrete prime circuit without changing the completed sign." The continuum reproduces the large-scale PNT current but loses exactly the fine arithmetic structure needed for the full Weil/Suzuki pairing.

Numerical independent probes (not certified interval estimates): at t=3, genuine source Psi ~+0.039709 while Psi_cont ~-1.75903; at t=4, +0.035141 vs -2.44504. The rigorous negative bound for Psi_cont is independent of these comparisons.

Primary Suzuki source: https://arxiv.org/abs/2606.09096 and Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function* (JLMS 2023). See repo wiki/02 for normalization.

## 5. Hostile controls: the homogenized current and RH-rate criterion are SOURCE-BLIND

- **Fake every-integer current.** lambda_fake=sum_(n>=1)n^(-1/2)delta_(log n). Euler–Maclaurin gives sum_(n<=X)n^(-1/2)=2sqrt(X)+zeta(1/2)+O(X^(-1/2)). It has the same limit density AND D_fake(T)=2+zeta(1/2)+O(e^(-T/2)), stronger than the RH-scale polynomial criterion, but its impulse distribution is completely different from Lambda and has mixed composites as primitive atoms. Thus neither PNT homogenization nor polynomial discrepancy by itself certifies arithmetic fidelity.
- **Fake impulse at 6.** Replace rho with rho+0.03/sqrt(6)delta_(log6). This changes D(T) by the bounded step 0.03/sqrt(6) for T>=log6; it does not alter the PNT limit OR the equivalence type of any poly-log residual bound. It DOES violate Euler-connected source primitivity.
- **Nonunit alpha_2 near 1.** Replace the 2^k prime-power weights by alpha_2^k(log2)2^(-k/2), with e.g. alpha_2=1.01. Sum_k abs[(alpha_2^k-1)log2 *2^(-k/2)] converges since |alpha_2|<sqrt(2). The cumulative current changes by a bounded amount, despite failing the local unitary character test.
- **Shifted log2.** Move the 2^k atoms from k log2 to k(log2+delta) with their finite total weights. The total variation of the difference is bounded by twice sum_k (log2)2^(-k/2), so it also preserves the macro-limit/polynomial rate, even though it breaks the true degree clock.

These source mutations can destroy exact Weil-sign positivity (reported finite windows in repo R49) while leaving the continuum theorem and rate criterion invariant. Therefore **the circuit's exact microscopic source must be retained separately from its continuum envelope**.

## 6. The right object and next verdict-changing probe

A possible *non-cheating two-scale object* is

  (rho, lambda, A_infty, Q_L),

where rho comes from exact Dirichlet/Euler-connected source, lambda is its macroscopic PNT envelope, A_infty is the independently fixed real Gaussian/Gamma/pole channel, and Q_L is the exact finite-window Weil pairing. The map rho -> lambda is lossy; it has NO canonical inverse. "Coherent closure" must preserve rho or an equally informative phase/correlation sector in addition to lambda. Infinite-ordinal "superconductivity" is neither a source of Gamma nor independent positivity.

**Next experimental discriminator:** on the *same* Paley–Wiener finite-window test vectors, compare Q_L with Q_L^cont obtained by replacing only the prime impulse distribution by e^(u/2)du. Decompose the difference into individual prime-power impulse contributions and test whether any zero-free, source-derived dualizing/graded correction can reconstruct the *full* difference, with no fake n=6 or log(3/2) atoms. Demonstrate the exact operator equality before asking for an independent Hodge-index sign. Avoid reproducing the already refuted "Archimedean positive floor" or positive generic dilation.

**Claim ledger:**
- PNT homogenization / Bohr energy growth: **DISCLOSED** classical consequences.
- RH iff O(T³) discrepancy: **DISCLOSED** equivalent restatement, not a proof.
- Smooth-source substitution fails Suzuki positivity for t>=3: **DISCLOSED, REFUTES specific replacement**.
- Finite numerical checks and R49 mutation sign results: **OBSERVED** (separate evidence).
- A source-faithful, archimedean-coupled positive polarization: **UNVERIFIED**.
- RH: **OPEN**.

## Reproducibility and literature

Script: scripts/prime_current_homogenization_probe.py (numpy, mpmath; no zeros).
PNT/RH classic estimates: NIST DLMF https://dlmf.nist.gov/25.16 .
Tate real/local Gaussian and global Fourier: https://www.math.columbia.edu/~avizeff/quals/Tate.pdf .
Suzuki 2026 finite Weil object: https://arxiv.org/abs/2606.09096 .
Connes–Consani arithmetic real Tate orbit https://arxiv.org/abs/2606.06604 .
US DOE superconducting critical-current reminder: https://www.energy.gov/science/doe-explainssuperconductivity .
Repo main Round 066 "superconductor" comparison is sign-blind; this work derives a source-only continuum theorem and exact substitution no-go. The script has been authored on this branch. Locally equivalent independent computations were executed at cutoff 2,000,000 and t in {.2,.5,1,2,3,4,6,8}. Do not claim GitHub Actions ran the committed script unless confirmed.
