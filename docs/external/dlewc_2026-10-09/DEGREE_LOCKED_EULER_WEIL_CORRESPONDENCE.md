# Degree-Locked Euler–Weil Correspondence (DLEWC)

**Research note, 2026-10-09.** Source-only construction for the degree-one primitive Dirichlet family; no zeros used to *define* anything here. Status: exact arithmetic rigidity identities and a full source-side quadratic-form prescription; **global sign remains GRH-equivalent / unproved**. No claim that this construction solves RH or GRH.

## 0. Object and task

Given a primitive Dirichlet character \(\chi\) of conductor \(q\), parity \(a\in\{0,1\}\), and a log-window \(L>0\), construct

\[
\boxed{\mathfrak C_{\chi,L}=(\mathcal A_\chi;\,\mathcal B_{\chi,L};\,Q_{\chi,L})}
\]

where \(\mathcal A_\chi\) is the source arithmetic algebra, \(\mathcal B\) is a **hidden conductor-graded chronology layer**, and \(Q\) is the **full, generally indefinite** Hermitian Weil form on a single physical test space. The form is NOT defined through zeros, a scattering phase, or an inverse fitted spectral measure. The primitive source is derived by formal Dirichlet convolution logarithm of genuine coefficients.

Three independent source gates are mandatory:

1. **E** (Euler primitivity): the logarithm has the exact prime-power coefficients of a degree-one Euler product. Mixed composites carry no *primitive* atoms.
2. **U** (unitary finite character): \(\chi(n)\) comes from a unitary character of \((\mathbb Z/q\mathbb Z)^\times\), extended by zero to nonunits. This explicitly excludes multiplicative but nonunit local parameters.
3. **D** (degree-clock): the label of \(n\) is the Archimedean length \(\ell(n)=\log\deg(z\mapsto z^n)=\log n\). The clock is independently fixed by the endomorphism degree, not fitted to the prime-impulse frequencies.

**E, U, and D are necessary source integrity constraints, not substitutes for a positivity theorem.** A source may satisfy all three and the sign of its completed Weil form still remains unknown.

## 1. The source Hilbert representation

Take \(\mathscr H=\ell^2(\mathbb N_{\ge1})\) with basis \(e_n\), and define
\[
S e_n=e_{n+1},\qquad V_m e_n=e_{mn},\qquad
H e_n=(\log n)e_n,\qquad X_\chi e_n=\chi(n)e_n.
\]
The domain of \(H\) includes the finite-span core. On that core,
\[
V_mS=S^mV_m,\qquad [H,V_m]=(\log m)V_m,\qquad
X_\chi V_m=\chi(m)V_mX_\chi.
\]
For a true primitive Dirichlet character,
\[
X_\chi^*X_\chi=P_{(n,q)=1}.
\]
Each relation is checked from finite integer arithmetic and the finite character table. None needs \(L(s,\chi)\)'s zeros.

A nonmultiplicative coefficient system \(a(n)\) is detected by
\[
(X_aV_m-a(m)V_mX_a)e_n=(a(mn)-a(m)a(n))e_{mn}.
\]
A nonunit prime parameter may still satisfy the covariance relation, but violates the partial-unitary requirement. A shifted prime frequency may satisfy an *alternative* grading, but violates the **independently anchored** degree-clock \([H,V_m]\).

## 2. Locally finite convolution logarithm (Euler gate)

For normalized coefficients \(a(1)=1\), work in the Dirichlet-convolution algebra \((\mathbb C^{\mathbb N},*)\), with \((u*v)(n)=\sum_{d\mid n}u(d)v(n/d)\). Let \(\mathbf1\) be the convolution identity supported at \(n=1\). The formal logarithm
\[
\eta_a=\log_*a=\sum_{r\ge1}\frac{(-1)^{r+1}}r(a-\mathbf1)^{*r}
\]
is **locally finite at every integer**: a nonzero \(r\)-fold factorization of \(n\) requires \(2^r\le n\). Thus the construction is causal under the ordinary integer wavefront.

Set
\[
c_a(n)=(\log n)\eta_a(n),\qquad
\rho_a=\sum_{n\ge2}\frac{c_a(n)}{\sqrt n}\,\delta_{\log n}.
\]
For a completely multiplicative \(a(n)=\chi(n)\), formal Euler multiplication gives
\[
\eta_\chi(n)=\begin{cases}\chi(p)^k/k&n=p^k,\\0&\text{otherwise},\end{cases}
\qquad
\boxed{c_\chi(n)=\Lambda(n)\chi(n)}.
\]
Conversely, for prescribed \(\alpha_p\), \(\eta(p^k)=\alpha_p^k/k\) and \(\eta(n)=0\) on mixed composites imply \(a(n)=\prod_p\alpha_p^{v_p(n)}\) by formal exponential. This is the exact degree-one Euler rigidity condition; mere prime-power *support without the power law* is weaker.

An independent recurrence computes the same coefficients without factoring an Euler product:
\[
\boxed{c_a(n)=a(n)\log n-\sum_{\substack{d\mid n\\d>1}} a(d)c_a(n/d)}.
\]
It is valid for Davenport–Heilbronn too, where it reveals non-prime-power atoms.

## 3. Davenport–Heilbronn versus its mod-5 Dirichlet twin

Let \(\chi(2)=i,\chi(3)=-i,\chi(4)=-1\), \(\chi(1)=1,\chi(5)=0\) periodically. The normalized Davenport–Heilbronn coefficient system is the real, mod-5 periodic sequence
\[
a_D(n)=\begin{cases}1 &n\equiv1\pmod5,\\ \kappa&n\equiv2\pmod5,\\-\kappa&n\equiv3\pmod5,\\-1&n\equiv4\pmod5,\\0&n\equiv0\pmod5,\end{cases}
\quad \kappa=\sqrt{1+\varphi^2}-\varphi,\quad\varphi=(1+\sqrt5)/2.
\]
Then \(a_D(2)=\kappa\), \(a_D(3)=-\kappa\), \(a_D(6)=1\). Therefore
\[
\boxed{a_D(6)-a_D(2)a_D(3)=1+\kappa^2>0},\qquad
\boxed{c_D(6)=(1+\kappa^2)\log6\ne0}.
\]
This is a forbidden **primitive mixed-composite impulse**. For \(\chi\), \(\chi(2)\chi(3)=\chi(6)=1\) and \(c_\chi(6)=0\). The D-H source also violates \(\|X_a e_2\|=1\) because \(|\kappa|<1\).

Important experimental interpretation: the same conductor and Gamma parity do not make the two coefficient systems identical except for one isolated scalar parameter. Euler covariance and local unit-character structure both change. The observed difference in finite Weil signs does not establish that those algebraic conditions alone imply GRH.

## 4. Global physical quadratic form — NOT a factorized positive surrogate

Fix \(L>0\), \(I_L=(-L,L)\), and \(f\in C_c^\infty(I_L;\mathbb C)\), extended by zero. Put
\[
\phi_f(u)=\int_{\mathbb R}f(x+u)\overline{f(x)}\,dx,
\qquad \widehat\phi_f(t)=|\widehat f(t)|^2.
\]
The finite prime-correlation operator on the **single shared physical test space** is
\[
\boxed{K_{\chi,L}(f)=2\sum_{p^k\le e^{2L}}
\frac{\log p}{p^{k/2}}\Re\big(\chi(p)^k\phi_f(k\log p)\big)}.
\]
All phases and prime frequencies are source-derived. Ramified primes contribute zero. No zero, scattering-phase, or boundary-value fitting enters.

The Archimedean/pole form is fixed by the source conductor and parity:
\[
A_{\chi,L}(f)=\frac1{2\pi}\int_{\mathbb R} |\widehat f(t)|^2
\left[\log\frac q\pi+\Re\psi\left(\frac{1+2a}{4}+\frac{it}{2}\right)\right]dt
+\mathcal P_\chi(f),
\]
where \(a\in\{0,1\}\), \(\chi(-1)=(-1)^a\). For a primitive nonprincipal character \(\mathcal P_\chi=0\); for \(\zeta\) (\(q=1,a=0\)), \(\mathcal P_1(f)=\widehat\phi_f(i/2)+\widehat\phi_f(-i/2)\). The actual completed Hermitian form is
\[
\boxed{Q_{\chi,L}(f)=A_{\chi,L}(f)-K_{\chi,L}(f)}.
\]
This is the arithmetic side of the standard completed Weil explicit formula with the declared Fourier convention; in the complex-character case use the Hermitian dual-character pairing, not a real-only basis. **Q is not asserted positive.** The Gamma contribution and, for zeta, the pole term cannot be omitted.

For \(|\chi(p)|=1\), put \(w_{p,k}=\log p/p^{k/2}\). With \(T_uf(x)=f(x+u)\), the exact completed prime edge identity is
\[
\sum_{p^k\le e^{2L}}w_{p,k}\|f-\chi(p)^kT_{k\log p}f\|_2^2
=2S_L\|f\|_2^2-K_{\chi,L}(f),\quad
S_L=\sum_{p^k\le e^{2L}\atop p\nmid q}w_{p,k}.
\]
Thus \(Q=E_{\rm edge}+[A-2S_L\|f\|^2]\). Positivity of the edge alone **does not** sign the full form. This also exposes the exact diagonal subtraction that all local-square-only approaches fail to pay.

If \(|\alpha_2|\ne1\), the raw edge identity instead has \(1+|\alpha_2|^2\) on the diagonal. Replacing it with 2 is an invalid normalization; the mutation is visibly rejected by **U**.

## 5. Hidden mixed-conductor chronology, not fake primitive atoms

The factorized prime edges above cannot themselves solve the joint-sign problem. Retain the actual additive SUCC order. At a physical horizon \(L\), take \(N=\lfloor e^{2L}\rfloor\); on \(G_N=\mathbb Z/L_N\mathbb Z\), put \(P_p e_n=1_{p\mid n}e_n\) and \(S e_n=e_{n+1}\) cyclically. Define
\[
B_p=[P_p,S]=S M_{\varepsilon_p},\qquad
\varepsilon_p(n)=1_{n\equiv-1\pmod p}-1_{n\equiv0\pmod p}.
\]
The mixed chronological field is
\[
\boxed{\Omega_{p,q}=[B_p,B_q]
=S^2M_{\varepsilon_p(n+1)\varepsilon_q(n)-\varepsilon_q(n+1)\varepsilon_p(n)}}.
\]
It is zero for static commutative projectors, nonzero once successor transports the boundaries. For \(p=2,q=3\), the coefficient is \((-1,-1,0,1,1,0)\) on residues mod 6 and
\[
\boxed{\|\Omega_{2,3}\|_{2,\tau}^2=\tfrac23}.
\]
With physical half-density weights \(w_p=\log p/\sqrt p\), \(\sqrt{w_pw_q}\chi(p)\chi(q)\Omega_{p,q}\) has normalized squared norm \(\tfrac23 w_2w_3\) for \(p,q=2,3\) in both zeta and the mod-5 character. This is a **hidden exact-conductor-6 interaction**, not an added primitive atom \(\delta_{\log6}\). Promoting mixed chronology directly to a scalar square can create forbidden ratio frequencies \(\log(p/q)\); a valid eventual elimination must preserve the physical Weil support distribution.

The chronological interaction is source-defined and nonzero, but its effect on the completed form is **UNVERIFIED**. Bare CRT/finite positive Grams are RH-inert. A claim that the mixed field creates RH positivity would be unsupported without an exact full Weil pullback.

## 6. The four gates (with exact falsifiers)

| Gate | Exact requirement | Mutated failure |
|---|---|---|
| E | \(X_aV_m=a(m)V_mX_a\), \(c_a(p^k)=a(p)^k\log p\), \(c_a(n)=0\) off prime powers | D-H: \(c_D(6)=(1+\kappa^2)\log6\); fake \(n=6\) primitive atom |
| U | \(X_a^*X_a=P_{(n,q)=1}\) | \(|\alpha_2|\ne1\) can pass E but fails U |
| D | \([H,V_m]=\log m\,V_m\), with \(H=\log\deg\) | shifted \(\log2\) fails fixed physical clock, even if all powers are coherently shifted |
| W | \(Q_{\chi,L}\succeq0\) **for all** horizons on the full complex test space | GRH-equivalent, not proved; finite numerics only |

**Independence controls:** a nonunit completely multiplicative coefficient system can pass E while failing U; a frequency reassignment can leave E and U intact but fail D. A generic positive direct-sum Euler Gram can pass E/U/D yet says nothing about W.

## 7. Discriminating next theorem (not yet accomplished)

**Canonical chronological shorting target.** Construct a *source-derived*, nonfactorizing, Archimedean-coupled positive parent \(G_{\chi,L}\) from \((S,V_p,H,X_\chi)\), the Gamma/degree channel, and the mixed-conductor chronology, such that its physical Schur complement equals the **entire** \(Q_{\chi,L}\) as a quadratic form on \(C_c^\infty(I_L)\). Prove the identity without zeros, with every counterterm and the logarithmic Archimedean ultraviolet part included *before* shorting. Then prove parent positivity without using a fitted boundary or assuming W.

**Do not define the parent as a square root or preimage of Q.** That is circular. An independently defined positive parent plus exact full completed-form identity would be a GRH-bearing result. The arch/pole block is not itself nonnegative, and previous prime-only parents fail high-frequency and boundary controls. The all-horizon equality/positivity is the missing mathematical theorem, not provided here.

**Hostile probes:** at fixed L, compare full coefficient distribution (including at the origin), test \(2,3,5\) exact-conductor sectors, reject \(\log(3/2)\) and \(\log6\) *primitive* artifacts, require complex Hermitian parity, test Gamma ultraviolet growth, mutate all three sources, and validate against independent known formulas *only after* the no-zero construction is frozen.

## 8. Evidence and provenance

A pure-Python executable is provided as `euler_arch_rigidity_probe.py`, with independent convolution-log and explicit matrix-commutator checks run separately. Tests are source-only. Finite runs are controls, never universal sign proofs. Literature anchors: NIST DLMF 25.15 for primitive Dirichlet L Euler/functional-equation data; Connes–Consani, *Weil positivity and Trace formula, the archimedean place* (2020); Suzuki's completed finite Weil forms. User repo `CRUCIFIXION_LEDGER.md` R49, R51, R58–59 is one provenance lineage with scratch-only numerical data (not independent mathematical evidence). Do not promote finite-window positive eigenvalues into RH claims.


## 9. Zero-free completed-form implementation and observed scope

A second numerical instrument, `euler_arch_weil_window_probe.py`, independently builds the Archimedean digamma/conductor block, source logarithmic-derivative prime (or D-H) block, and ζ polar block on two **complex** polynomial bump modes of support `[-1.22,1.22]`. The modes are smooth enough for the integral form but not `C_c^∞`, so this is a numerical calibration rather than a strict smooth-core proof. It reads no zeros.

- ζ: Hermitian residual `9.61e-17`, eigenvalues `(2.78e-6, 6.83e-5)` in this **two-dimensional subspace**; exact edge+Arch identity residual `1.59e-15`.
- Primitive complex character modulo 5: Hermitian residual `9.85e-18`, eigenvalues `(0.00283, 0.81363)` in the same subspace; edge+Arch identity residual `1.40e-15`.
- Davenport–Heilbronn at the same conductor/parity: Hermitian residual `2.08e-17`, eigenvalues `(0.00159, 0.26733)` in the same subspace. Its Euler source is rejected by E/U although the quadratic form is still positive on this small window and basis, exactly as it *should* be before the D-H crossover horizon.

These are approximate floating-point quadratures with fixed truncations and no rigorous tail error bounds. **Nothing here implies PSD on an entire horizon, a GRH statement, or reproducibility of the repository's larger numerical instrument.** The independent convolution-log implementation agrees with the recursion through `n=40` to `4.5e-16` for ζ, character and D-H; the finite 6×6 matrix commutator agrees exactly with the CRT formula.

Run together in the same directory: `python euler_arch_rigidity_probe.py && python euler_arch_weil_window_probe.py` (the latter requires NumPy/SciPy). GitHub has not been modified as part of this note.
