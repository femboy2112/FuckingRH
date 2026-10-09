# Source-faithful arithmetic boundary curvature (2026-10-09)

**Working research dossier (local, not yet committed), not a proof.** Parent: `main@265bf38dfd6af7d5820396f7e80244122a4aa235` (Round 59). RH and Dirichlet GRH remain open. The goal is a *zero-free construction* which enforces the three mutation-sensitive arithmetic constraints **before** asking a positivity question. The new finite-window observation is the exact **mixed-prime adjoint commutator**. It provides a genuine mixed-prime shared-boundary interaction, but no unconditional Weil coercivity.

## 1. Three independent algebraic fidelity gates

Fix a primitive Dirichlet character `chi` of conductor `q` (with `q=1` corresponding to zeta). Write `alpha_p=chi(p)`; at ramified primes `p|q`, `alpha_p=0` and the Euler local factor is absent. Unramified `alpha_p` lies on the unit circle. In `Re s > 1`:

\[
F(s)=\sum_{n\ge 1}a(n)n^{-s}=\prod_{p\nmid q}(1-\alpha_p p^{-s})^{-1},\qquad a(n)=\chi(n),
\]
\[
-\frac{F'(s)}{F(s)}=\sum_{n\ge2} b(n)n^{-s},\qquad
 b(n)=\begin{cases}\alpha_p^k\log p,&n=p^k,\\0,&n\text{ not a prime power.}\end{cases}
\]

An arbitrary normalized Dirichlet series with coefficients `a(1)=1` has an exact *finite* recurrence

\[
b(n)=a(n)\log n-\sum_{\substack{d\mid n\\2\le d<n}}b(d)a(n/d).
\]

**Gate A: connected Euler source.** Enforce the recurrence, prime-power support and local-power formula. In particular

\[
b(6)=(a(6)-a(2)a(3))\log6.
\]

The normalized Davenport–Heilbronn combination has `a(2)=kappa, a(3)=-kappa, a(6)=1`, hence `b(6)=(1+kappa^2)log 6 != 0`. No zeros needed. A fabricated atom at 6 fails A; a product over *pseudo-primes including 6* is disallowed because source primes are the ordinary irreducibles of `N`.

**Gate B: local unitarity and character compatibility.** Restrict to a genuine unitary character on `(Z/qZ)^×`, not merely an arbitrary Euler product. `|alpha_p|=1` for `p∤q`; `alpha_p=0` if `p|q`. If `alpha_2` is changed from a unit phase to `1.01 alpha_2`, gate A *still passes* (the formal Euler product survives) while gate B fails. This is an essential distinction. Further, unimodularity alone is not enough: a phase-modified prime might have norm 1 without coming from the fixed global character (conductor and residue classes); test compatibility with the actual character as a separate predicate.

**Gate C: true logarithmic clock.** On `H_arith=ell^2({n>=1:(n,q)=1})`, set

\[
D e_n=(\log n)e_n,\qquad V_p e_n=e_{pn}\quad(p\nmid q),\qquad U_\chi e_n=\chi(n)e_n.
\]

Then exactly

\[
[D,V_p]=(\log p)V_p,\qquad U_\chi V_pU_\chi^*=\chi(p)V_p.
\]

A purported prime period `(1+eta)log 2` fails the first covariance identity for `p=2` unless `eta=0`. Merely assigning a free frequency to each prime would not detect this mutation.

### Half-density and the archimedean boundary

On `L^2(R_+,dx)`, define `U_n h(x)=sqrt(n)h(nx)`; this is unitary (by change of variables). The logarithmic-unitary identification `g(u)=e^{u/2}h(e^u)` sends `U_n` to translation `g(u+log n)`. The `1/2` is fixed here by the Jacobian of this unitary scaling, and evaluating Euler weights on `Re s=1/2` gives `n^{-1/2}`. The critical axis is also selected by `s <-> 1-s` functional-equation symmetry. **Do not claim the adelic product formula alone forces 1/2:** `prod_v |x|_v^s=1` for every complex `s` whenever `x in Q^×`. Also `0=(sum_v log|x|_v)^2` does *not* imply positivity of a renormalized second-jet Gram.

## 2. Shared-boundary compression: a genuine mixed-prime operator

For each window `I_L=[-L,L]`, let `P_L` denote orthogonal projection from `L^2(R)` onto `L^2(I_L)` by zero-extension and `S_a f(x)=f(x-a)` the full-line translation. Define `T_a=P_L S_a P_L` (on the interval). For positive steps `a,b`, `T_aT_b=T_{a+b}`; thus multiplication survives for `a=log m`, `b=log n`.

The crucial *non-factorizing* structure is the **mixed adjoint commutator**:

\[
\boxed{([T_a^*,T_b]f)(x)=\mathbf1_{I_L}(x)\mathbf1_{I_L}(x+a-b)
[\mathbf1_{I_L}(x+a)-\mathbf1_{I_L}(x-b)]f(x+a-b).}
\]

The formula follows by expanding the two nested zero-padded shifts. It is an exact finite-window identity and uses no zeros, analytic continuation, or guessed boundary condition. On the full line `[S_a^*,S_b]=0`; **the shared interval creates the coupling**. Each commutator is a partial translation with amplitude in `{0,+1,-1}`, hence its operator norm is at most 1. For `L=1,a=log2,b=log3`, the amplitude is +1 at `x=-0.2` and -1 at `x=0.6`, each on an open subinterval, so its operator norm is exactly 1. This couples `p=2` and `p=3` through their *common* boundary without creating an artificial first-order source impulse at `n=6`.

For unramified prime powers `n=p^k` with `0<log n<2L`, set `w_n=Lambda(n)/sqrt(n)=(log p)p^{-k/2}` and `R_n=conj(chi(n))T_{log n}`. Define the **coherent boundary-source field** and its curvature

\[
B_{\chi,L}=\sum_{n=p^k} \sqrt{w_n}\,R_n,\qquad
\mathcal C_{\chi,L}=[B_{\chi,L}^*,B_{\chi,L}]
=\sum_{n,m}\sqrt{w_nw_m}\,[R_n^*,R_m].
\]

The sum is finite for each `L`. It includes true `p!=q` mixed terms with character phases. It is Hermitian and source-faithful (after A/B/C); mixed commutators are nonzero because the compressions have a common boundary. This is kinematic noncommutativity, not necessarily a new source of arithmetic information.

**A sharp no-go (proved): this curvature is necessarily indefinite whenever nonzero.** For any finite family of distinct `0<a_j<2L` and nonzero coefficients `c_j`, let `B=sum_j c_j T_{a_j}`. Choose `epsilon>0` smaller than every `a_j`, every `2L-a_j`, and every pairwise gap `|a_i-a_j|`. Let `f_-` and `f_+` be indicators of an `epsilon`-length interval at the left and right ends of `I_L`. The shifted copies have disjoint support and are fully inside the window. Consequently

\[
\langle f_-,[B^*,B]f_-\rangle=\epsilon\sum_j|c_j|^2>0,\qquad
\langle f_+,[B^*,B]f_+\rangle=-\epsilon\sum_j|c_j|^2<0.
\]

Smooth bumps approximate these witnesses. In particular for the prime-source weights `|c_n|^2=w_n`, this yields exactly `+/- epsilon sum_n w_n`. The curvature **cannot itself be a positive Weil certificate**. Its only possible role is in an independently justified *indefinite-to-positive joint coupling with the archimedean term*. Its ability to explain Weil compensation is **UNVERIFIED**, not a theorem.


## Canonical upgrade: the finite Euler logarithm and clock commutator

The field `B` above is one exploratory choice with a square-root source weighting. A more economical, canonical candidate **derives the whole first-order Weil prime source from one multiplicative operator**, without choosing square-root coefficients. This should be the primary arithmetic-source object going forward.

Let `X f(u)=u f(u)` on `L²([-L,L])`. For every `a>0` the right-shift compression obeys the exact identity `[X,T_a]=a T_a`. Since every positive-step `T_a` is nilpotent on the finite interval, each `I-z T_a` is invertible and its logarithm has a canonical terminating polynomial. For a primitive Dirichlet character chi (with `chi(p)=0` on ramified primes), define

\[
\mathfrak F_{\chi,L}=\prod_{p<e^{2L}}(I-\overline{\chi(p)}p^{-1/2}T_{\log p})^{-1}
=\sum_{n<e^{2L}}\overline{\chi(n)}n^{-1/2}T_{\log n}.
\]

Its operator logarithm is

\[
\log\mathfrak F_{\chi,L}=\sum_{p^k<e^{2L}}\frac{\overline{\chi(p)^k}}{k p^{k/2}}T_{k\log p}.
\]

The decisive exact identity is

\[
\boxed{D_{\chi,L}:=[X,\log\mathfrak F_{\chi,L}]
=\sum_{p^k<e^{2L}}\frac{\overline{\chi(p)^k}\log p}{p^{k/2}}T_{k\log p}.}
\]

Thus the `Lambda` prime-power support, each `log p` charge, and the `n^-1/2` density appear without ever querying a zero. **This is the recommended arithmetic-source parent for the actual Weil operator**, `Q=P-(D+D*)`, in the stated Fourier convention. It is source-faithful but does not establish positivity.

The discrete arithmetic-coordinate realization `V_n e_m = e_{nm}` for `nm<=N`, `X e_m=(log m)e_m` gives an *independent arithmetic-coordinate model* of the exact algebraic identity (numerically checked in the supplied tests): with `F_N=sum_{n<=N}a(n)n^-1/2 V_n`,

\[
[X,\log F_N]=\sum_{n<=N}\frac{b(n)}{\sqrt n}V_n,
\qquad -F'(s)/F(s)=\sum_{n>=2}b(n)n^{-s}.
\]

For a true Euler product, `b(6)=0`. If `a(6)` is artificially altered by `delta`, the resulting coefficient of `V_6` changes by `delta (log 6)/sqrt 6`; for normalized Davenport--Heilbronn coefficients `a2=kappa`, `a3=-kappa`, `a6=1` it is `(1+kappa^2)(log 6)/sqrt 6`. This construction *reads Euler multiplicativity* rather than only the numerical prime logarithms.

The more canonical mixed curvature is now `[D*,D]`, with explicit cross-prime terms because the shifts share one window. The pulse-lemma above proves that positive-step commutator curvature is always indefinite: therefore it is **not** the missing positive operator. We have not shown that this curvature constrains the negative archimedean directions. It may prove kinematically inert, and must be tested by a mixed-sector ablation on the independent calibrated Weil matrix.

This construction remains in the realm of standard Euler-product/Dirichlet-convolution algebra and compression, repackaged for the research program. It is not claimed to be a novel RH theorem.

## 3. Exact connection to the actual completed Weil form (not a new equivalence)

With `f in C_c^infty(I_L)`, `tilde f(u)=overline(f(-u))`, `g=f*tilde f`, and `F(t)=int f(u)e^{itu}du`, a standard arithmetic-side Weil form is

\[
Q_{\chi,L}(f) = P_{\chi,L}(f)
-\sum_{n=p^k}\frac{\Lambda(n)}{\sqrt n}
\left[\chi(n)g(\log n)+\overline{\chi(n)}g(-\log n)\right],
\]

with the prime sum restricted to `n<e^{2L}`, omitting ramified primes. In this Fourier convention, for primitive nonprincipal `chi`,

\[
P_{\chi,L}(f)=\frac{1}{2\pi}\int_{\mathbb R}|F(t)|^2
\left[\log\frac q\pi+\mathrm{Re}\,\psi\left(\frac{1/2+\epsilon+it}{2}\right)\right]dt,
\qquad\chi(-1)=(-1)^\epsilon.
\]

For zeta (`q=1,epsilon=0`) add the pole contribution `hat g(i/2)+hat g(-i/2)`. This pole quadratic form is **not automatically nonnegative for arbitrary complex f**; keep both terms, and use the repo's convention-calibrated arithmetic matrix to validate any implementation (especially the complex-character `chi/bar chi` orientation).

Set `K_{chi,L}=sum_n w_n (R_n+R_n^*)` and `A_L=2 sum_n w_n`. Exact source-side operator identity:

\[
Q_{\chi,L}=P_{\chi,L}-K_{\chi,L}
=(P_{\chi,L}-A_L I)
+\sum_n w_n\left[(I-R_n)^*(I-R_n)+(I-R_n^*R_n)\right].
\]

The bracket is PSD for each `n` since `|chi(n)|=1` and `T_a^*T_a` is a projection. But `P-A_LI` is not known PSD and was observed strongly indefinite in the repo. **We have not derived any identity or inequality relating `C_{chi,L}` to a positive lower bound on `P-K`.** Thus the coherent curvature is a candidate *coupling instrument*, not the missing certificate. No step uses `M_zeros`, zero ordinates or scattering phases.

## 4. Why this avoids previous traps, and what still fails

- **Not Euler-blind:** Gate A detects a fake `n=6` logarithmic impulse. Merely including the commutator, without A, would not.
- **Not amplitude-blind:** B detects `|alpha_2|!=1`; a generic degree-one Euler product would not.
- **Not frequency-blind:** C forces actual `log p`; free quasiperiodic phases would not.
- **Not factorized in the window:** `[T_{log p}^*,T_{log q}]!=0`; however this is a **kinematic boundary effect**. It does not imply a global Hodge-index sign.
- **Not a spectral trick:** `B_{chi,L}` is a finite sum of rightward nilpotent shifts. Its eigenvalues are not the zeta-zero ordinates; neither `C` nor the above SOS is a Hilbert–Pólya construction.

## 5. Pre-registered verdict-changing tests

1. **Exact source controls:** `tests/test_arithmetic_source_boundary.py` recovers zeta/chi5 prime-power logarithmic derivative coefficients; produces the D–H `b(6)` discrepancy; and rejects fake 6, `|alpha_2|!=1`, and perturbed `log 2` *for their distinct reasons*. These tests only check finite algebra.
2. **Boundary control:** independently expand `[T_a^*,T_b]` by nested shifts and compare with the closed formula at interior points near both boundaries. Verify the corresponding full-line commutator vanishes and a matrix compression has indefinite curvature.
3. **Calibration gate still owed:** identify the exact `chi` orientation, conductor, Gamma and zeta pole conventions with the main repo's *independent* `M_full` explicit-formula instrument. Until then, the source-to-Weil bridge is a derivation awaiting external matrix calibration, **not a passed test**.
4. **Mixed-sector ablation:** for **preregistered** compactly-supported test families, compare the full mixed curvature contribution against its `p=q`-only deletion. Use zeta, the mod-5 primitive character and D–H as positive/negative controls; do not use zeros as construction inputs. If mixed-sector effects fail to distinguish the calibrated examples, retire this coupling proposal.
5. **Hard mathematics gate:** derive a source-based inequality involving `C_{chi,L}` that gives an independently provable improvement for `P-K`, on a *fresh held-out* support window. A fit to Q's near-null eigenvector, or a Schur complement whose positivity is stipulated, does not qualify. Uniform `Q>=0` remains RH/GRH-equivalent.

**Epistemic status:** Exact identities behind Gates A/B/C, unitary scaling, Euler-log commutator, finite-window commutator, SOS, and curvature no-go: **derived/proved**. The concrete finite tests check these identities and selected controls, but do not verify general character compatibility or positivity. Seventeen small finite tests: **observed**. Cross-prime curvature as mechanism of archimedean compensation: **conjectured/UNVERIFIED**. `Q>=0` for all windows: **unproved**. None of these computations establish RH or GRH.

**References:** Weil's explicit formula (standard); Connes–Consani, *Weil positivity and trace formula, the archimedean place*, arXiv:2006.13771; the repository's `wiki/03`, `wiki/06`, and `CRUCIFIXION_LEDGER.md` Rounds 49/51/59.
