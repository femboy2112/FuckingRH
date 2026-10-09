# Hecke–Tate connected causal connection

**2026-10-09. Parent: latest main, Round 059. RH OPEN.** This is a source-rigid arithmetic construction, NOT a proved positive polarization or RH proof.

## 1. The connected Euler/Hecke condition

Let d be an arithmetic function with d(1)=1, with Dirichlet convolution *, and set

\[
b=\log_*d=\sum_{j\ge1}\frac{(-1)^{j+1}}j(d-\mathbf1_{\{1\}})^{*j}.
\]

Each coefficient is a finite exact algebraic sum. Where the Dirichlet series converges and is nonzero,

\[
-\frac{D'}D(s)=\sum_{n\ge2}(\log n)b(n)n^{-s}.
\]

For a primitive Dirichlet character chi with conductor q,

\[
b(p^k)=\chi(p)^k/k,\qquad
b(n)=0\quad\text{when n is not a prime power}.
\]

Consequently \((\log n)b(n)=\Lambda(n)\chi(n)\). If p divides q, chi(p)=0 is the legitimate ramified exception.

This is a connected/primitive-event criterion. An Euler product may produce a composite coefficient at 6 in D(s), but it cannot produce an *independent* connected log-derivative impulse at 6.

### Exact nonmultiplicative separator

For the quartic primitive character modulo 5, choose chi(2)=i, chi(3)=-i, chi(6)=1. Set D(s)=a L(s,chi)+b L(s,bar chi), with a+b=1, and denote its coefficients by d(n). Then

\[
d(2)=i(a-b),\quad d(3)=-i(a-b),\quad d(6)=1.
\]

The coefficient at 6 of the convolution logarithm is

\[
\boxed{[\log_*d](6)=d(6)-d(2)d(3)=4ab.}
\]

Thus the coefficient at 6 of -D'/D is \(4ab\log6\), nonzero for any nontrivial mixture ab != 0. For each genuine Dirichlet character it is identically zero. This is a zero-free mathematical discriminator of multiplicativity, not a theorem about zero locations.

## 2. The SUCC/FUCC/Hecke representation

On H=ell²(N), let

\[
Se_n=e_{n+1},\qquad V_me_n=e_{mn},\qquad He_n=(\log n)e_n,\qquad E=|e_1\rangle\langle e_1|.
\]

On finite vectors these satisfy

\[
V_mS=S^mV_m,\qquad [H,V_m]=(\log m)V_m.
\]

For primitive chi put \(U_\chi e_n=\chi(n)e_n\). Then

\[
U_\chi V_m=\chi(m)V_mU_\chi,\qquad
U_\chi^*U_\chi=P_{(n,q)=1}.
\]

The coefficient may vanish at ramified primes; at every unramified prime it must have modulus one.

Set \(P_{p,k}=V_{p^k}EV_{p^k}^*=|e_{p^k}\rangle\langle e_{p^k}|\). Define the **connected half-density source operator**

\[
\boxed{
\mathscr J_\chi=\sum_{p,k\ge1}\frac{\log p}{p^{k/2}}\,U_\chi P_{p,k}.
}
\]

It is a bounded diagonal operator; it is NOT claimed to be trace class. For any compactly supported smooth test phi on the logarithmic line,

\[
\boxed{
\operatorname{Tr}(\mathscr J_\chi\phi(H))
=\sum_{p,k}(\log p)\chi(p)^kp^{-k/2}\phi(k\log p).
}
\]

The trace has finitely many terms. No zeros enter. This is the exact prime-power source of the completed explicit formula, obtained from SUCC/FUCC operators and the physical clock.

## 3. The three mutation certificates

**Fake impulse at n=6.** No primitive prime-ray projector exists at 6. Adding a nonzero von-Mangoldt-like impulse epsilon there creates a composite connected logarithm coefficient epsilon/log(6), violating the Euler/Hecke support constraint.

**Unramified |alpha_2| != 1.** The relation U*U=P_coprime fails on the 2-ray. This is an exact source obstruction; a ramified alpha_p=0 remains legal.

**Shifted log 2.** The physical H is fixed as diag(log n), so [H,V_2]=(log 2)V_2. An alternative event time log2+epsilon violates this and, with the Archimedean norm held fixed, the rational product formula by -epsilon. Merely replacing H with a new arbitrary additive length homomorphism is NOT the same arithmetic geometry.

These are algebraic certificates of source mismatch. They do not prove that the completed Weil form becomes negative under every mutation at every finite horizon; those are separately measured effects.

## 4. Global additive/Archimedean compatibility: a nonfactorizing requirement

Local multiplicativity/unitarity is insufficient: arbitrary unimodular alpha_p have an Euler product in Re(s)>1 but may have no Dirichlet/Hecke functional equation.

Therefore admit only a **global primitive Dirichlet/Hecke character with its actual conductor and parity**, and require the common additive Fourier/Poisson completion.

For a primitive character chi modulo q with chi(-1)=(-1)^a, define

\[
\theta_{\chi,a}(t)=\sum_{n\in\mathbb Z}n^a\chi(n)e^{-\pi n^2t/q},\quad t>0.
\]

For a nonprincipal character the zero term vanishes. Mellin transformation yields

\[
\boxed{
\int_0^\infty\theta_{\chi,a}(t)t^{(s+a)/2}\frac{dt}{t}
=2(q/\pi)^{(s+a)/2}\Gamma((s+a)/2)L(s,\chi)
}
\]

initially for Re(s)>1. Additive Poisson summation yields

\[
\boxed{
\theta_{\chi,a}(t)=\varepsilon_\chi t^{-a-1/2}\theta_{\bar\chi,a}(1/t),
\qquad \varepsilon_\chi=\tau(\chi)/(i^a\sqrt q),\quad |\varepsilon_\chi|=1.
}
\]

For zeta use the full Gaussian theta with the zero-mode/pole correction. Theta by itself does not distinguish Davenport–Heilbronn; the primitive Hecke condition must be coupled to it.

## 5. The actual completed Weil form is a separate, RH-bearing layer

For f smooth with support (-A,A), zero-extend and put F=f*tilde(f), h_n=log n, and
\(\widehat f(u)=\int f(x)e^{iux}dx\). The source defines the completed Hermitian form

\[
\boxed{
Q_{\chi,A}(f)=\mathcal P_\chi(f)+
\frac1{2\pi}\int_{\mathbb R}|\widehat f(u)|^2
\left[\Re\psi\left(\frac{1/2+a+iu}{2}\right)+\log(q/\pi)\right]du
-2\Re\sum_{p^k\le e^{2A}}(\log p)\chi(p)^kp^{-k/2}F(k\log p).
}
\]

For nonprincipal primitive chi, \(\mathcal P_\chi=0\). For zeta the pole term is the exact cross pairing \(2\Re(\ell_+(f)\overline{\ell_-(f)})\). This is a zero-free arithmetic-side definition; Weil's explicit formula subsequently connects it to zero data, without using them to build it.

The existing exact zeta decomposition on this program is

\[
Q_A(f)=E_\Gamma(f)+E_{\rm prime,A}(f)+2|C_f|^2-2|S_f|^2-d_A\|f\|^2,
\]

or \(Q_A=P_A-D_A\), with P_A positive on its natural form domain and D_A bounded positive. The exact **unpaid** condition is \(P_A^{-1/2}D_AP_A^{-1/2}\le I\) for all A. It is RH-equivalent and NOT proved here.

## 6. The first genuinely mixed-prime boundary observable

Let \(T_h=P_A\tau_hP_A\) be the zero-padded log-shift on L²(-A,A). Define the single source operator

\[
C_{\chi,A}=\sum_{p^k\le e^{2A}}(\log p)\chi(p)^kp^{-k/2}T_{k\log p}.
\]

Its chiral boundary curvature

\[
\boxed{
\mathfrak K_{\chi,A}=[C_{\chi,A}^*,C_{\chi,A}]
=\sum_{m,n}\overline{w_\chi(m)}w_\chi(n)[T_{\log m}^*,T_{\log n}]
}
\]

contains genuine mixed-prime boundary terms without selecting pairwise coefficients by hand. It is source and phase sensitive, and its commutators encode precisely the noncommutativity generated by finite-horizon boundaries.

**Sharp obstruction.** The antiunitary chiral reversal \(\mathcal Jf(x)=\overline{f(-x)}\) obeys \(\mathcal J C_{\chi,A}\mathcal J=C_{\chi,A}^*\), hence

\[
\boxed{
\mathcal J\mathfrak K_{\chi,A}\mathcal J=-\mathfrak K_{\chi,A}.
}
\]

The self-adjoint curvature has spectrum symmetric about zero. It **cannot be positive semidefinite unless it vanishes**. The raw curvature is therefore NOT the arithmetic ample class.

An admissible next construction must use an independently forced oriented/primitive compression and an **infinite-dimensional prime–Gamma coupling**. Taking the positive spectral part by hand would be circular.

## 7. A useful causal theorem

Adding a fake impulse epsilon/sqrt(6) at log6 changes the finite-window arithmetic form by

\[
\Delta Q_A(f)=-2\Re\left[\epsilon\,F(\log6)/\sqrt6\right].
\]

Since F is supported on [-2A,2A], the mutation is entirely invisible whenever \(2A\le\log6\); for \(2A>\log6\) there exist smooth witnesses. Thus \(\log6/2\) is the exact first possible detection half-horizon. Detection is not negativity.

## 8. Scorecard and next theorem

- Genuine zeta and primitive Dirichlet chi: exact Hecke/clock/Poisson source compatibilities, no zero inputs.
- Davenport–Heilbronn-like nontrivial mixture: fails at composite connected cumulant 6.
- Fake connected 6 impulse: fails prime-power primitive support.
- Nonunit alpha2: fails partial-unitary Hecke law.
- Moved log2: fails fixed Archimedean generator/product formula.
- Mixed-prime boundary curvature: exists unconditionally, but is chiral-indefinite.
- Completed Weil positivity: still missing.

The companion zero-free test suite verifies the algebraic cases exactly and the quartic character's odd theta/Poisson equation at 55 digits.

**The next potentially proof-bearing theorem:** derive from the *actual global theta/Hecke diagonal* a continuum, nonlocal, factor-mixing, oriented pairing that reproduces the **full polarized** Q_A, including the exact pole, Gamma and large negative bulk counterterm, and prove its positivity on the relevant primitive/image sector without using zeros. Merely rediscovering the Weil equivalence or choosing a positive metric is not a result.

**RH REMAINS OPEN.**
