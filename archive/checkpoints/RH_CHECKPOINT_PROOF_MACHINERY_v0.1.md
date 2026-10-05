# RH Checkpoint Proof Machinery

**Proof ledger v0.1 — 3 September 2026**

> **Supersession notice.**  The closure contract in Sections 12, 14, and 15
> is corrected and strengthened by `RH_CHECKPOINT_TRIANGULATION_LEDGER_v0.2.md`.
> In particular, the logarithmic transport must be canonical rather than an
> arbitrary isometry, CCM Lemma 7.3 already proves convergence of the explicit
> prolate-candidate transforms to \(\Xi\), and parity-resolved Schur transport
> removes the need for a global candidate threshold above its Rayleigh value.
> The v0.1 results remain the baseline machinery; v0.2 is the governing
> closure statement.

## Executive verdict

This pass turns the LCM/logarithmic checkpoint frame into a small theorem
library.  It does **not** prove RH.  It does four more useful things:

1. proves the exact operator carried by each LCM jump;
2. decomposes every primitive-prime tower into finite resolvents with explicit
   fibers, inverses, determinants, and spectral bounds;
3. identifies the boundary as the sole source of cross-prime
   noncommutativity after finite-window compression;
4. proves a sharp residual-to-Mellin-to-Hurwitz closure theorem and isolates
   the hypotheses still missing in the RH program.

Two attractive shortcuts are now rigorously dead:

- inversion symmetry does not force the Weil ground state to be even;
- inserting the common phase \(n^{-it}\) into the prime translation block
  produces only a unitary gauge, so its spectrum cannot detect \(t\).

The main exact operator identity is

\[
\boxed{
\mathcal A_L
=
\sum_{1<n<e^L}
\log\frac{M_n}{M_{n-1}}\,n^{-1/2}
\bigl(S_{\log n}+S_{\log n}^{*}\bigr),
}
\]

where \(M_n=\operatorname{lcm}(1,\ldots,n)\) and \(S_y\) is the truncated
translation on \(L^2(0,L)\).  Since the logarithmic LCM jump is exactly
\(\Lambda(n)\), this is precisely the finite non-Archimedean block occurring
with a minus sign in the Weil form.

The current Connes--Consani--Moscovici program explicitly leaves two steps
open: proving that the continuous Weil ground state is simple and even, and
proving that its explicit prolate/Poisson candidate approximates that ground
state strongly enough to force convergence of the corresponding entire
functions.  See [*Zeta Spectral Triples*](https://arxiv.org/abs/2511.22755).
The theorems below sharpen the exact estimates such an argument must meet.

## 1. Claim-status vocabulary

Every substantial statement is assigned one of these states.

| Label | Meaning |
|---|---|
| **PROVED** | A proof is included here, or the statement follows immediately from a cited theorem with the hypotheses checked. |
| **CLASSICAL / REPACKAGED** | Correct and reusable here, but not new mathematical progress toward RH. |
| **REFUTED** | A displayed counterexample or exact no-go theorem kills the claim. |
| **CONDITIONAL** | The implication is proved, but one or more named hypotheses remain open. |
| **OPEN** | This is a genuine unsolved edge of the proposed program. |

## 2. Conventions and normalization firewall

Set

\[
M_0=M_1=1,
\qquad
M_n=\operatorname{lcm}(1,\ldots,n),
\qquad
L=\log X=2\log\lambda.
\]

All Hilbert-space inner products are antilinear in the first variable:

\[
\langle f,g\rangle=\int\overline{f(x)}g(x)\,dx.
\]

Let

\[
H_L=L^2(0,L).
\]

Functions in \(H_L\) are extended by zero to 
\(\mathbb R\).  For \(y>0\), define the truncated right translation

\[
(S_yf)(x)=
\begin{cases}
f(x-y),&y<x<L,\\
0,&0<x\le y.
\end{cases}
\]

Then

\[
S_aS_b=S_{a+b},
\qquad
S_y=0\quad\text{if }y\ge L
\]

as operators on \(H_L\), with the endpoint understood almost everywhere.

The raw prime measure always uses \(n<X\).  If a formula writes \(n\le X\),
the endpoint is harmless only when the test kernel is known to vanish there.

The logarithmic circle

\[
C_L=\mathbb R/L\mathbb Z
\]

has orthonormal basis in \(L^2(C_L,du)\)

\[
\phi_r(u)=L^{-1/2}e^{2\pi iru/L}.
\]

Bare characters are orthonormal only for probability Haar measure \(du/L\).
The character identity

\[
e^{-2\pi ir\log n/L}=n^{-it_r},
\qquad t_r=\frac{2\pi r}{L},
\]

is exact, but the finite Weil prime block is built from **zero-extended
convolution**, hence from truncated shifts, not from periodic convolution on
the circle.  This distinction is load-bearing.

## 3. LCM jump calculus

### Theorem 3.1 — LCM jumps and von Mangoldt atoms **[PROVED; CLASSICAL]**

For every prime \(p\) and integer \(n\ge1\),

\[
v_p(M_n)=\max\{a\ge0:p^a\le n\}.
\]

Consequently,

\[
\boxed{
\log M_n-\log M_{n-1}=\Lambda(n)
}
\]

and

\[
\boxed{
\log M_N=\psi(N)=\sum_{n\le N}\Lambda(n).
}
\]

Moreover,

\[
\log n=\sum_{d\mid n}\Lambda(d),
\qquad
\Lambda(n)=\sum_{d\mid n}\mu(d)\log(n/d),
\]

and

\[
\log(N!)=\sum_{d\le N}\left\lfloor\frac Nd\right\rfloor\Lambda(d).
\]

#### Proof

The exponent of \(p\) in the LCM is the largest \(a\) for which \(p^a\le n\).
Passing from \(n-1\) to \(n\) changes an exponent if and only if \(n=p^a\),
and then it raises that exponent by one.  Thus

\[
\frac{M_n}{M_{n-1}}=
\begin{cases}
p,&n=p^a,\\
1,&\text{otherwise},
\end{cases}
\]

which yields the first two identities after taking logarithms and telescoping.
In the divisor sum, each prime \(p\mid n\) contributes 
\(v_p(n)\log p\), so the total is 
\(\log n\).  Möbius inversion gives the inverse formula.  Summing the divisor
identity over \(n\le N\) and switching two finite sums gives the factorial
formula. \(\square\)

### Theorem 3.2 — Stieltjes prime-power measure **[PROVED; CLASSICAL]**

Extend

\[
J(u)=\log M_{\lfloor e^u\rfloor}
\]

right-continuously to \(u\ge0\).  Then, as locally finite
Lebesgue--Stieltjes measures,

\[
\boxed{
dJ=\sum_{n\ge2}\Lambda(n)\delta_{\log n},
}
\]

and therefore

\[
\boxed{
e^{-u/2}dJ(u)
=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(u).
}
\]

For every 
\(\tau\ge0\),

\[
P(\tau)
=\int_{[0,\tau]}(\tau-u)e^{-u/2}\,dJ(u)
=\sum_{n\le e^\tau}
\frac{\Lambda(n)}{\sqrt n}(\tau-\log n).
\]

#### Proof

\(J\) is constant on 
\([\log n,\log(n+1))\), and its jump at 
\(\log n\) is Theorem 3.1's quantity 
\(\Lambda(n)\).  Multiplication by \(e^{-u/2}\) gives the critical weight.
The last identity is integration against the atomic measure.  If
\(e^\tau\) is an integer, the endpoint coefficient 
\(\tau-\log n\) is zero. \(\square\)

The positive infinite critical comb is locally finite but has exponential
mass growth in the log coordinate; by itself it is not a tempered
distribution.  Only finite cutoffs may be Fourier transformed naively on the
critical line.  Temperedness belongs to the fully completed/cancelled Weil
distribution, not to this positive arithmetic sector alone.

### Lemma 3.3 — critical prime-power Möbius sieve **[PROVED; REPACKAGED]**

Put

\[
V=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n},
\qquad
\Theta=\sum_p\frac{\log p}{\sqrt p}\delta_{\log p}.
\]

For \(k\ge1\), define

\[
(R_k\sigma)(E)
=\int \mathbf 1_E(ku)e^{-(k-1)u/2}\,d\sigma(u).
\]

Then

\[
R_jR_k=R_{jk},
\qquad
\boxed{V=\sum_{k\ge1}R_k\Theta},
\qquad
\boxed{\Theta=\sum_{k\ge1}\mu(k)R_kV},
\]

where both series are locally finite.

#### Proof

\(R_k\) sends the primitive atom at 
\(\log p\), of weight 
\((\log p)p^{-1/2}\), to the atom at 
\(k\log p\), of weight 
\((\log p)p^{-k/2}\).  This proves the direct formula.  At
\(m\log p\), the proposed inverse has coefficient

\[
\frac{\log p}{p^{m/2}}
\sum_{k\mid m}\mu(k),
\]

which survives exactly for \(m=1\).  On a compact interval only finitely many
\(k\) occur, so no rearrangement of an infinite conditionally convergent sum
has been used. \(\square\)

One exact finite consequence is

\[
\sum_{p<X}\frac{\log p}{p^{1/2+it}}
=
\sum_{\substack{k\ge1\\2^k<X}}\mu(k)
\sum_{2\le n<X^{1/k}}
\frac{\Lambda(n)}{n^{k(1/2+it)}}.
\]

This is the correct mutation for deleting repeated prime powers while
preserving the critical weights and phases.

## 4. Exact truncated-shift model of the Weil prime block

For zero-extended \(f,g\in H_L\), set

\[
q(f,g)(y)=(f^**g)(y)+(f^**g)(-y),
\qquad
f^*(x)=\overline{f(-x)}.
\]

This is the convention used in
[*Zeta Spectral Triples*](https://arxiv.org/html/2511.22755v1), where the
finite prime term is written using the same \(q\).

### Theorem 4.1 — convolution is a truncated translation **[PROVED]**

For \(0<y<L\),

\[
(f^**g)(y)=\langle f,S_y^*g\rangle,
\qquad
(f^**g)(-y)=\langle f,S_yg\rangle.
\]

Hence

\[
\boxed{
q(f,g)(y)=\langle f,(S_y+S_y^*)g\rangle.
}
\]

In particular, the prime-power operator in the finite Weil form is

\[
\boxed{
T(n)=n^{-1/2}
\bigl(S_{\log n}+S_{\log n}^{*}\bigr).
}
\]

#### Proof

For \(y>0\), zero extension gives

\[
(f^**g)(y)
=\int_y^L\overline{f(x-y)}g(x)\,dx
=\langle f,S_y^*g\rangle.
\]

Changing \(y\) to \(-y\) gives the other equality.  Adding them proves the
claim. \(\square\)

For the Fourier basis 
\(U_n(x)=L^{-1/2}e^{2\pi inx/L}\), this recovers exactly

\[
q(U_m,U_n)(y)=
\begin{cases}
\dfrac{\sin(2\pi my/L)-\sin(2\pi ny/L)}{\pi(n-m)},&m\ne n,\\[2mm]
2(1-y/L)\cos(2\pi ny/L),&m=n.
\end{cases}
\]

The triangular factor \(1-y/L\) and the divided difference are boundary
effects.  A periodic circle multiplier alone does not contain them.

### Theorem 4.2 — LCM--Weil update law **[PROVED]**

For independent arithmetic cutoff \(N\) and window length \(L\), define

\[
\mathcal A_{L,N}
=\sum_{\substack{2\le n\le N\\\log n<L}}
\log\frac{M_n}{M_{n-1}}\,n^{-1/2}
\bigl(S_{\log n}+S_{\log n}^*\bigr).
\]

Then

\[
\mathcal A_{L,n}-\mathcal A_{L,n-1}=0
\]

unless \(n=p^m<e^L\), in which case

\[
\boxed{
\mathcal A_{L,n}-\mathcal A_{L,n-1}
=(\log p)p^{-m/2}
\bigl(S_{m\log p}+S_{m\log p}^{*}\bigr).
}
\]

The finite Weil form contains 
\(-\mathcal A_{L,N}\).

#### Proof

Substitute Theorem 3.1 into the definition and use Theorem 4.1. \(\square\)

The update is generally indefinite.  LCM depth does **not** give form
monotonicity of the Weil operator.

## 5. Primitive-prime towers and finite KMS fibers

Now saturate the arithmetic cutoff relative to the window:

\[
\mathcal A_L
=\sum_{1<n<e^L}\Lambda(n)n^{-1/2}
\bigl(S_{\log n}+S_{\log n}^*\bigr).
\]

The saturation condition matters.  If an independent cutoff \(N<e^L\) is
retained, every prime tower below must also be truncated by \(p^m\le N\); the
full resolvent formula is then false.

### Theorem 5.1 — prime-tower resolvent decomposition **[PROVED]**

For a primitive prime \(p<e^L\), put

\[
y=\log p,
\qquad
r=p^{-1/2},
\]

and let 
\(\mathcal P_{p,L}\) be the sum of all \(p\)-power shells in
\(\mathcal A_L\).  Then

\[
\begin{aligned}
\mathcal P_{p,L}
&=(\log p)\sum_{m\ge1}r^m
\bigl(S_y^m+(S_y^*)^m\bigr)\\
&=(\log p)(K_{p,L}-I),
\end{aligned}
\]

where

\[
\boxed{
K_{p,L}
=(I-rS_y)^{-1}+(I-rS_y^*)^{-1}-I.
}
\]

The sums are actually finite because \(S_y\) is nilpotent.

#### Proof

The \(p^m\) atom has weight 
\((\log p)p^{-m/2}=(\log p)r^m\), and
\(S_{m\log p}=S_y^m\).  Since 
\(S_y^m=0\) once \(my\ge L\), both Neumann series terminate and give the
displayed resolvents. \(\square\)

This is an additive decomposition over primitive primes, not an Euler-product
factorization.  “Prime-tower resolvent decomposition” is therefore the safer
name.

### Theorem 5.2 — direct-integral chain model **[PROVED]**

Write

\[
L=qy+r_0,
\qquad q=\lfloor L/y\rfloor,
\qquad 0\le r_0<y.
\]

Every \(x\in(0,L)\) can be written uniquely, up to null endpoints, as

\[
x=s+ky,
\qquad 0\le s<y.
\]

The fiber over \(s\) has dimension

\[
d(s)=
\begin{cases}
q+1,&0<s<r_0,\\
q,&r_0<s<y,
\end{cases}
\]

with \(d=q\) almost everywhere when \(r_0=0\).  On a \(d\)-dimensional fiber,
\(S_y\) is the nilpotent shift 
\(J_de_j=e_{j+1}\), and the phase-decorated resolvent is

\[
K_d(z)
=I+\sum_{m=1}^{d-1}
\left(z^mJ_d^m+\bar z^{m}(J_d^*)^m\right),
\qquad |z|<1.
\]

Its entries are

\[
(K_d(z))_{ij}=
\begin{cases}
z^{i-j},&i>j,\\
1,&i=j,\\
\bar z^{j-i},&i<j.
\end{cases}
\]

Thus every prime tower is a direct integral of finite
Kac--Murdock--Szegő covariance matrices.

#### Proof

Fubini's theorem gives the isometry

\[
H_L\cong\int_{[0,y)}^{\oplus}\mathbb C^{d(s)}\,ds,
\qquad
f\longmapsto(f(s+ky))_{k=0}^{d(s)-1}.
\]

On each chain, right translation moves the \(k\)-th coordinate to the
\((k+1)\)-st coordinate and kills the final coordinate.  Substitution into
Theorem 5.1 gives the matrix formula. \(\square\)

### Theorem 5.3 — inverse, determinant, positivity, and bounds **[PROVED]**

For \(d\ge2\) and \(z\in\mathbb C\), 
\(|z|=r<1\),

\[
\boxed{
K_d(z)^{-1}
=\frac1{1-r^2}
\begin{pmatrix}
1&-\bar z&&&\\
-z&1+r^2&-\bar z&&\\
&\ddots&\ddots&\ddots&\\
&&-z&1+r^2&-\bar z\\
&&&-z&1
\end{pmatrix}.
}
\]

For \(d=1\), one instead has 
\(K_1(z)=K_1(z)^{-1}=[1]\).  In every dimension,

\[
\boxed{
\det K_d(z)=(1-r^2)^{d-1}
}
\]

and

\[
\boxed{
\frac{1-r}{1+r}I
\preceq K_d(z)\preceq
\frac{1+r}{1-r}I.
}
\]

In particular, \(K_d(z)\) is strictly positive.

#### Proof

Direct multiplication cancels every off-tridiagonal term and gives the
displayed inverse.  Expanding the determinant of the inverse's tridiagonal
matrix, or applying elementary elimination to \(K_d(z)\), gives
\((1-r^2)^{d-1}\).

For the uniform bounds, after removing the phase as in Theorem 5.4 below, use
the Poisson representation

\[
v^*K_d(r)v
=\int_0^{2\pi}
\frac{1-r^2}{1-2r\cos\theta+r^2}
\left|\sum_{j=0}^{d-1}v_je^{ij\theta}\right|^2
\frac{d\theta}{2\pi}.
\]

The Poisson kernel lies between 
\((1-r)/(1+r)\) and 
\((1+r)/(1-r)\); Parseval finishes the proof. \(\square\)

At the critical weight \(r=p^{-1/2}\), the fiber determinant is

\[
\det K_d=(1-p^{-1})^{d-1}.
\]

This is a fiber determinant and equals a power of the inverse local Euler
factor at \(s=1\).  It is **not** a Fredholm determinant on \(H_L\):
\(K_{p,L}-I\) is noncompact and not trace class.  The decomposable algebra has
no unique normalized trace.  Choose the specific fiber trace

\[
\tau_L(A)
=\frac1L\int_0^{\log p}
\operatorname{Tr}_{\mathbb C^{d(s)}}(A(s))\,ds.
\]

It is normalized because \(\int_0^{\log p}d(s)\,ds=L\).  For this declared
trace, the associated Fuglede--Kadison determinant is

\[
\operatorname{Det}_{\mathrm{FK}}K_{p,L}
=(1-p^{-1})^{(L-\log p)/L},
\]

because

\[
\int_0^{\log p}(d(s)-1)\,ds=L-\log p.
\]

No phase-dependent critical Euler factor is recovered by this determinant.

### Theorem 5.4 — common-phase gauge no-go **[PROVED; STRUCTURAL NO-GO]**

On a \(d\)-chain, let

\[
D_\varphi=\operatorname{diag}(1,e^{i\varphi},\ldots,e^{i(d-1)\varphi}).
\]

Then

\[
K_d(re^{i\varphi})=D_\varphi K_d(r)D_\varphi^*.
\]

More strongly, let

\[
(M_tf)(x)=e^{itx}f(x).
\]

If every prime-power shift is decorated by its RH character, define

\[
\mathcal A_L(t)=
\sum_{1<n<e^L}\Lambda(n)n^{-1/2}
\left(n^{-it}S_{\log n}+n^{it}S_{\log n}^*\right).
\]

Then

\[
\boxed{
\mathcal A_L(t)=M_t^*\mathcal A_L(0)M_t.
}
\]

Therefore the spectrum of the **entire phase-decorated prime operator** is
independent of \(t\).

#### Proof

The finite-dimensional identity follows from
\(D_\varphi J_dD_\varphi^*=e^{i\varphi}J_d\).  On \(H_L\), direct calculation
gives

\[
M_t^*S_yM_t=e^{-ity}S_y.
\]

Putting \(y=\log n\) in every summand proves the global identity. \(\square\)

#### Consequence

The common character \(n^{-it}\) cannot create RH-relevant spectral motion
inside the prime block alone.  Nontrivial \(t\)-dependence must come from
coupling it to structure that is not fixed by this gauge: the differential
scaling operator, the Archimedean Gamma sector, a fixed boundary functional,
or the rank-one perturbation.  This kills a large class of otherwise tempting
“phase coherence” experiments before computation.

### Corollary 5.5 — exact spectrum of one LCM shell **[PROVED]**

Let \(0<y=\log n<L\) and 
\(d_{\max}=\lceil L/y\rceil\).  Then

\[
\sigma(J_d+J_d^*)
=\left\{2\cos\frac{j\pi}{d+1}:1\le j\le d\right\}
\]

on a \(d\)-chain, and hence

\[
\boxed{
\|T(n)\|
=2n^{-1/2}
\cos\frac{\pi}{d_{\max}+1}.
}
\]

At \(y=L\), 
\(T(n)=0\) almost everywhere.

#### Proof

\(J_d+J_d^*\) is the adjacency matrix of the path on \(d\) vertices.  Its
sine eigenvectors give the stated eigenvalues.  The largest fiber controls
the direct-integral norm. \(\square\)

There is no operator-norm damping as \(y\uparrow L\).  For \(L/2<y<L\),
\(d_{\max}=2\), so 
\(\|S_y+S_y^*\|=1\) right up to the endpoint, where it drops to zero.  What
does vanish is strong action on each fixed vector, every fixed matrix
coefficient, and every fixed finite Fourier/Galerkin compression.

## 6. Boundary leakage is exactly the source of compressed noncommutativity

Let \(P\) be the orthogonal projection from 
\(L^2(\mathbb R)\) onto functions
supported in \((0,L)\), and put \(Q=I-P\).

### Theorem 6.1 — boundary commutator identity **[PROVED; STANDARD]**

If bounded full-line operators \(A,B\) commute, then on \(PH\),

\[
\boxed{
[PAP,PBP]=PBQAP-PAQBP.
}
\]

For every \(f\in PH\),

\[
\boxed{
|\langle f,[PAP,PBP]f\rangle|
\le
\|QB^*Pf\|\,\|QAPf\|
+\|QA^*Pf\|\,\|QBPf\|.
}
\]

#### Proof

Insert \(I=P+Q\) into the commuting product:

\[
PABP=PAPBP+PAQBP,
\]

\[
PBAP=PBPAP+PBQAP.
\]

Since \(AB=BA\), subtraction gives the first identity.  The second follows
from Cauchy--Schwarz after moving \(A\) or \(B\) across the inner product and
inserting \(Q\). \(\square\)

Let \(U_y\) be full-line translation and define

\[
\widetilde K_{p}
=(I-rU_y)^{-1}+(I-rU_y^*)^{-1}-I.
\]

All 
\(\widetilde K_p\) commute because translations form an abelian group, while

\[
P(I-zU_y)^{-1}P=(I-zS_y)^{-1}.
\]

Thus Theorem 6.1 applies exactly to different compressed prime towers.  Their
cross-prime noncommutativity is a boundary/exterior-leakage term.

This identity does **not** make that term small.  For example, take
\(A=U_a\), \(B=U_a^*\).  Their compressions are \(S_a,S_a^*\), and for
\(L>2a\),

\[
[S_a,S_a^*]
=1_{(a,L)}-1_{(0,L-a)},
\qquad
\|[S_a,S_a^*]\|=1.
\]

The theorem becomes useful only after proving vector-specific estimates such
as

\[
\|Q\widetilde K_pPk_L\|\ll1
\]

with enough cancellation or summability over the prime powers.  A naive
absolute sum cannot work cheaply because

\[
\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\asymp2\sqrt X.
\]

## 7. Suzuki kernel and the shell-birth regularity dichotomy

Suzuki's screw-function formulation turns the Weil distribution into a
continuous kernel; see
[*Weil's quadratic form via the screw function*](https://arxiv.org/abs/2606.09096).
The correct interval scale is

\[
I_L=(-L/2,L/2),
\qquad L=\log X.
\]

Its difference set is 
\([-L,L]\), so the prime powers are exactly \(n<X\).

For \(b>0\), put

\[
h_b(x)=(|x|-b)_+,
\]

\[
\kappa_{L,b}(x,y)
=h_b(x-y)-h_b(x)-h_b(-y),
\qquad x,y\in I_L,
\]

and let \(K_{L,b}\) be the corresponding integral operator.  Let

\[
(T_bv)(x)=1_{I_L}(x)v(x-b),
\qquad H_{L,b}=T_b+T_b^*.
\]

### Proposition 7.1 — exact LCM screw-kernel decomposition **[PROVED]**

Write Suzuki's even function as

\[
\Psi(\tau)=A_\infty(\tau)-P(\tau),
\qquad
g=-\Psi,
\]

with the distributional identity

\[
W=-g''=\Psi''.
\]

and use the screw-kernel convention

\[
G_g(x,y)=g(x-y)-g(x)-g(-y)+g(0).
\]

Then on \(I_L\times I_L\),

\[
\boxed{
G_g=G_{-A_\infty}
+\sum_{1<n<X}
\frac{\log(M_n/M_{n-1})}{\sqrt n}
\,\kappa_{L,\log n}.
}
\]

If \(X\) is an integer, including \(n=X\) changes nothing because
\(\kappa_{L,L}=0\).

#### Proof

Theorem 3.2 and even extension give

\[
P(|t|)=\sum_n\frac{\Lambda(n)}{\sqrt n}(|t|-\log n)_+.
\]

Substitute \(g=-A_\infty+P\) into the screw kernel, use its linearity, and
replace 
\(\Lambda(n)\) by the LCM jump.  Since 
\(|x|,|y|\le L/2\) and
\(|x-y|\le L\), the endpoint shell is identically zero. \(\square\)

For a direct sign check, let

\[
r_t(x)=\operatorname{sgn}(t)
1_{[\min(0,t),\max(0,t)]}(x).
\]

Then, under smooth mollification,

\[
W(r_t*\widetilde r_u)=G_g(t,u).
\]

On the diagonal,

\[
r_t*\widetilde r_t=(|t|-|x|)_+=2\Delta_{|t|},
\]

so

\[
\boxed{G_g(t,t)=2W(\Delta_{|t|})=2\Psi(|t|).}
\]

This verifies both the sign and the factor \(2\).

### Theorem 7.2 — integrated shell versus shift shell **[PROVED]**

For \(D=i\,d/dx\) with domain 
\(H_0^1(I_L)\),

\[
\boxed{
D^*K_{L,b}D=-H_{L,b}
}
\]

in quadratic-form sense.  If \(L/2\le b<L\), then

\[
\kappa_{L,b}(x,y)=(|x-y|-b)_+
\]

and

\[
\boxed{
\|K_{L,b}\|_{\mathrm{HS}}
=\frac{(L-b)^2}{\sqrt6}.
}
\]

In contrast,

\[
\boxed{
\|H_{L,b}\|
=2\cos\frac{\pi}{\lceil L/b\rceil+1}
}
\]

for \(0<b<L\), and therefore

\[
\|H_{L,b}\|=1
\quad\text{whenever}\quad b<L<2b,
\]

while \(H_{b,b}=0\).

#### Proof

Since 
\(h_b''=\delta_b+\delta_{-b}\) in the distributional sense, two integrations
by parts against functions in 
\(H_0^1(I_L)\) give
\(D^*K_{L,b}D=-(T_b+T_b^*)\).  When \(b\ge L/2\), the subtracted terms
\(h_b(x)\) and \(h_b(-y)\) vanish on \(I_L\).  Consequently,

\[
\begin{aligned}
\|K_{L,b}\|_{\mathrm{HS}}^2
&=2\int_b^L(s-b)^2(L-s)\,ds\\
&=\frac{(L-b)^4}{6}.
\end{aligned}
\]

The norm of \(H_{L,b}\) is Corollary 5.5 with interval length \(L\). \(\square\)

At the birth of the LCM atom \(n=e^b\), the arithmetic weight is

\[
w_n=\frac{\Delta\log M_n}{\sqrt n}
=\frac{\Lambda(n)}{\sqrt n}.
\]
The raw Weil update 
\(-w_nH_{L,b}\) has norm approaching \(w_n\), not zero, as
\(L\downarrow b\).  The integrated screw-kernel update has Hilbert--Schmidt
norm

\[
w_n\frac{(L-b)^2}{\sqrt6}.
\]

Thus integration restores quadratic birth regularity, while conjugation by
the unbounded derivative \(D\) destroys it.  On a fixed finite-dimensional
subspace \(V\subset H_0^1(I_L)\), one recovers

\[
\left\|D^*K_{L,b}D\big|_V\right\|
\le
\|D|_V\|^2\frac{(L-b)^2}{\sqrt6}.
\]

This is the correct mechanism for modewise continuity at a prime-power birth.

### Proposition 7.3 — birth continuity in the logarithmic form topology
**[PROVED]**

Assume \(L/2\le b<L\).  Rescale \(I_L\) unitarily to 
\(I_1=(-1/2,1/2)\), put

\[
\varepsilon=\frac{L-b}{L},
\qquad
m=2\varepsilon,
\]

and let \(E\) be the union of the two endpoint strips of total measure \(m\).
For the rescaled shell 
\(H=T_{b/L}+T_{-b/L}\),

\[
|\langle Hv,v\rangle|\le\|1_Ev\|_2^2.
\]

Define Suzuki's logarithmic energy

\[
\mathcal E_{\log}(v)
=\frac1{2\pi}\int_{\mathbb R}
\log(e+|\xi|)|\widehat v(\xi)|^2\,d\xi.
\]

Then

\[
\boxed{
|\langle Hv,v\rangle|
\le
\eta(m)\mathcal E_{\log}(v),
\qquad
\eta(m)=\frac{2\sqrt m}{\pi}
+\frac{2}{\log(e+m^{-1/2})}
\longrightarrow0.
}
\]

#### Proof

The shifted overlap is supported in the endpoint strips, and
Cauchy--Schwarz gives the first inequality.  Split 
\(v\) at frequency \(R\).
The low-frequency part obeys the elementary uncertainty bound

\[
\|1_Ev_{\le R}\|_2^2
\le\frac{mR}{\pi}\|v\|_2^2,
\]

while Markov's inequality against 
\(\log(e+|\xi|)\) gives

\[
\|v_{>R}\|_2^2
\le\frac{\mathcal E_{\log}(v)}{\log(e+R)}.
\]

Applying
\(\|a+b\|_2^2\le2\|a\|_2^2+2\|b\|_2^2\) to the two frequency pieces,
then using \(\mathcal E_{\log}(v)\ge\|v\|_2^2\) and choosing
\(R=m^{-1/2}\), gives the displayed \(\eta(m)\).
\(\square\)

So the shell birth is discontinuous in the raw \(L^2\)-operator norm but
continuous in the natural 
\(H^{\log}\)-form topology.  This is the correct
topology for any continuum convergence argument.

### Corollary 7.4 — finite-mode positivity transfer **[PROVED]**

Let \(V\subset H_0^1(I_L)\) be finite-dimensional and set

\[
\Omega_V=\sup_{0\ne v\in V}\frac{\|Dv\|_2}{\|v\|_2}.
\]

If a pre-existing Weil compression has lower bound 
\(\alpha\) on \(V\), then
adding a shell \(b\in[L/2,L)\) of weight \(w>0\) leaves the lower bound

\[
\boxed{
\alpha-\frac{w\Omega_V^2(L-b)^2}{\sqrt6}.
}
\]

For the first \(K\) Dirichlet modes,

\[
\Omega_V=\frac{K\pi}{L}.
\]

Hence an atom 
\(n\), with 
\(\sqrt X\le n<X\), moves the compressed bottom by at most

\[
\boxed{
\frac{\Lambda(n)}{\sqrt n}
\frac{\pi^2K^2}{\sqrt6}
\left(\frac{\log(X/n)}{\log X}\right)^2.
}
\]

#### Proof

Theorem 7.2 and 
\(\|K\|_{\mathrm{op}}\le\|K\|_{\mathrm{HS}}\) give

\[
|\langle K_{L,b}Dv,Dv\rangle|
\le\frac{(L-b)^2}{\sqrt6}\Omega_V^2\|v\|_2^2.
\]

Apply the min--max principle, then substitute 
\(b=\log n\), 
\(L=\log X\), and
\(w=\Lambda(n)/\sqrt n\). \(\square\)

This is an unconditional finite-level certificate.  It says nothing by itself
about accumulated old shells or the infinite-window limit.

### Proposition 7.5 — localized bottom is nonincreasing **[PROVED; CLASSICAL]**

Let 
\(\lambda_a\) be the bottom of the closed Weil form on 
\(L^2(-a,a)\).
Then

\[
a_1<a_2\quad\Longrightarrow\quad\lambda_{a_2}\le\lambda_{a_1}.
\]

#### Proof

Compactly supported test functions in 
\((-a_1,a_1)\) form a subset of those in
\((-a_2,a_2)\), after zero extension.  Taking the infimum of the Rayleigh
quotient over a larger set can only lower it. \(\square\)

Consequently, positivity on an unbounded sequence of windows would imply
positivity on every finite window and hence RH.  That consequence is an
RH-equivalent reformulation, not progress; the monotonicity itself is useful
for organizing certificates.

## 8. Parity: exact block calculus and hard counterexamples

Let 
\(\gamma e_j=e_{-j}\) on Fourier indices
\(-N,\ldots,N\).  Any real symmetric matrix \(A\) commuting with 
\(\gamma\)
splits as

\[
A=A_+\oplus A_-
\]

on the even and odd subspaces.

### Proposition 8.1 — exact parity criterion **[PROVED]**

The global ground state of \(A\) is simple and even if and only if

\[
\boxed{
\lambda_0(A_+)<\lambda_0(A_-)
\quad\text{and}\quad
\lambda_0(A_+)\text{ is simple}.
}
\]

#### Proof

The spectrum of the orthogonal direct sum is the multiset union of the two
sector spectra.  The statement follows immediately. \(\square\)

Thus inversion symmetry only block-diagonalizes; it does not order the two
bottom eigenvalues.

### Theorem 8.2 — parity blocks of the divided-difference class **[PROVED]**

Consider the exact Connes--van Suijlekom matrix class

\[
\tau_{ii}=a_i,
\qquad
\tau_{ij}=\frac{b_i-b_j}{i-j}\quad(i\ne j),
\]

where

\[
a_{-i}=a_i,
\qquad
b_{-i}=-b_i.
\]

Use the parity bases

\[
u_0=e_0,
\qquad
u_k=\frac{e_k+e_{-k}}{\sqrt2},
\qquad
v_k=\frac{e_k-e_{-k}}{\sqrt2}.
\]

Writing \(E=\tau|_+\) and \(O=\tau|_-\), one has

\[
E_{00}=a_0,
\qquad
E_{0k}=\sqrt2\frac{b_k}{k},
\qquad
E_{kk}=a_k+\frac{b_k}{k},
\]

\[
E_{k\ell}
=\frac{2(kb_k-\ell b_\ell)}{k^2-\ell^2}
\quad(k\ne\ell),
\]

and

\[
O_{kk}=a_k-\frac{b_k}{k},
\qquad
O_{k\ell}
=\frac{2(\ell b_k-kb_\ell)}{k^2-\ell^2}
\quad(k\ne\ell).
\]

Suppose in addition that \(\psi\) is odd and \(C^1\) on a neighborhood of
the nodes \(-N,\ldots,N\), and that
\(a_k=\psi'(k)\), \(b_k=\psi(k)\).  Define

\[
h(\xi)=\frac{\psi(\sqrt\xi)}{\sqrt\xi},
\qquad
\Phi(\xi)=\xi h(\xi)\quad(\xi>0),
\qquad
h(0)=\psi'(0),\quad\Phi(0)=0.
\]

then

\[
\boxed{
O=2\,\operatorname{diag}(1,\ldots,N)
L_h
\operatorname{diag}(1,\ldots,N),
}
\]

where \(L_h\) is the Loewner matrix at nodes 
\(1^2,\ldots,N^2\), while

\[
\boxed{
E=D_sL_\Phi D_s,
\qquad
D_s=\operatorname{diag}(1,\sqrt2,\ldots,\sqrt2),
}
\]

with nodes \(0,1^2,\ldots,N^2\).

#### Proof

Substitute \(u_k,v_k\) into the quadratic form and use the even/odd relations
for \(a,b\).  The four off-diagonal terms simplify to the displayed rational
expressions.  The Loewner identities follow from

\[
h(k^2)=\frac{b_k}{k},
\qquad
\Phi(k^2)=kb_k
\]

and differentiation on the diagonal.  Oddness gives \(\psi(0)=0\), while
\(C^1\)-regularity gives \(\Phi'(0)=\psi'(0)=a_0\), which supplies the
zero-node diagonal entry of the even Loewner matrix. \(\square\)

This exposes potentially useful matrix-monotonicity structure, but it does not
order 
\(\lambda_0(E)\) and 
\(\lambda_0(O)\) without an additional theorem.

### Counterexample 8.3 — a positive divided-difference matrix with odd ground
**[REFUTED SHORTCUT]**

For indices 
\(-1,0,1\), choose

\[
(a_{-1},a_0,a_1)=(2,12,2),
\qquad
(b_{-1},b_0,b_1)=(-1,0,1).
\]

Then

\[
\tau=
\begin{pmatrix}
2&1&1\\
1&12&1\\
1&1&2
\end{pmatrix}.
\]

This matrix is strictly positive, belongs exactly to the class characterized
in Proposition 4.2 of
[*Quadratic Forms, Real Zeros and Echoes of the Spectral Action*](https://arxiv.org/abs/2511.23257),
and commutes with reversal.  Nevertheless,

\[
\frac1{\sqrt2}(1,0,-1)
\]

is its unique ground state, with eigenvalue \(1\).  The two even eigenvalues
are

\[
\frac{15\pm\sqrt{89}}2,
\]

whose smaller value is approximately \(2.783\).

Hence

\[
\boxed{
\text{positive}+\text{reversal symmetric}+\text{divided difference}
\not\Rightarrow
\text{even ground state}.
}
\]

### Proposition 8.4 — a usable Schur-complement certificate **[PROVED]**

Let \(k\) be a unit even candidate and write

\[
A_+=
\begin{pmatrix}
\rho&r^*\\
r&D
\end{pmatrix}
\]

on 
\(\operatorname{span}\{k\}\oplus(H_+\cap k^\perp)\).  Put

\[
\lambda_o=\lambda_0(A_-).
\]

Assume

\[
\lambda_o<\lambda_0(D).
\]

Then \(A\) has a simple even global ground state if and only if

\[
\boxed{
\rho-\lambda_o
-\langle r,(D-\lambda_o)^{-1}r\rangle<0.
}
\]

A simpler sufficient condition is

\[
\rho<\min\{\lambda_o,\lambda_0(D)\}.
\]

#### Proof

\(D-\lambda_o\) is positive.  The inertia formula for the Schur complement
shows that \(A_+-\lambda_o\) has exactly one negative eigenvalue precisely
when the displayed scalar is negative.  Thus there is exactly one even
eigenvalue below the entire odd spectrum; it is necessarily simple and is the
global ground.  Conversely, interlacing leaves at most one even eigenvalue
below 
\(\lambda_o\), so the same inertia calculation is necessary.  The Rayleigh
value 
\(\rho<\lambda_o\), together with 
\(\lambda_o<\lambda_0(D)\), gives the
cruder sufficient condition. \(\square\)

This certificate is stronger than a raw residual: it explicitly compares the
candidate's even sector with the odd bottom.

### Proposition 8.5 — exact pole-sector Birman--Schwinger test **[PROVED]**

The pole kernel splits as

\[
2\cosh\frac{x-y}{2}
=2C(x)C(y)-2S(x)S(y),
\]

where

\[
C(x)=\cosh(x/2),
\qquad
S(x)=\sinh(x/2).
\]

Thus, after any parity-invariant Galerkin compression, if \(B\) denotes the
remaining operator, then exactly

\[
A_+=B_++2|C\rangle\langle C|,
\qquad
A_-=B_--2|S\rangle\langle S|.
\]

The pole term raises the even sector and lowers the odd sector, so it works
against the desired parity ordering.

Let 
\(\mu=\lambda_0(A_+)\) be simple and suppose

\[
\mu<\lambda_0(B_-).
\]

Then

\[
\boxed{
\lambda_0(A_-) > \mu
\iff
2\langle S,(B_--\mu)^{-1}S\rangle<1.
}
\]

#### Proof

Factor

\[
A_--\mu
=(B_--\mu)^{1/2}
\left(I-2|v\rangle\langle v|\right)
(B_--\mu)^{1/2},
\]

where 
\(v=(B_--\mu)^{-1/2}S\).  The middle rank-one perturbation is positive
if and only if 
\(2\|v\|^2<1\), which is the scalar inequality. \(\square\)

This is a necessary-and-sufficient odd-sector test once the even value 
\(\mu\)
and the pole-free odd localization are controlled.  It does not prove those
inputs.

### Perron--Frobenius routes: two obstructions **[PROVED NO-GO FOR THESE CONES]**

A real symmetric matrix with nonpositive off-diagonal entries and connected
negative-edge graph has a simple strictly positive ground state; reversal
symmetry then forces it to be even.  That standard route does not fit the
natural Fourier coefficient cone of the Weil matrix.  Here is the explicit
obstruction.  In a prime-free window \(1<X=e^L<2\), the Fourier coefficients
in the Connes--Consani--Moscovici normalization satisfy, for every \(n\ge1\),

\[
b_n(QW)
=\frac{32Ln\sinh^2(L/4)}{L^2+16\pi^2n^2}+\alpha_L(n)>0,
\]

where

\[
\alpha_L(n)=\frac1\pi\int_0^L
\sin(2\pi nx/L)\frac{e^{x/2}}{e^x-e^{-x}}\,dx>0.
\]

The last inequality follows by pairing successive positive and negative
half-waves against the strictly decreasing positive weight.  Since
\(b_0=0\) and \(b_{-n}=-b_n\), the divided-difference entries obey

\[
q_{0,n}=q_{0,-n}=q_{n,-n}=\frac{b_n}{n}>0.
\]

Thus the triangle on indices \(-n,0,n\) has three positive off-diagonal
entries.  A diagonal sign gauge commuting with reversal cannot make all three
nonpositive, because the product of edge signs around a triangle is gauge
invariant.

Nor does the natural function cone give a global positivity-preserving
semigroup.  Away from \(0\) and the discrete prime distances, the off-diagonal
kernel of the closed localized form is

\[
K(t)=2\cosh(t/2)-\frac{e^{-t/2}}{1-e^{-2t}}.
\]

It changes sign at

\[
t_*=\log\varrho,
\qquad
\varrho^3-\varrho-1=0,
\]

where 
\(\varrho\approx1.324717957\) is the plastic constant.  If
\(L=\log X>t_*\), choose a separation \(d\in(t_*,L)\) avoiding the finitely
many prime distances and take two nonnegative, disjoint bumps separated by
\(d\).  Their cross form is positive.  The first Beurling--Deny criterion for
a positivity-preserving semigroup requires this cross form to be nonpositive.
Therefore that semigroup route fails whenever

\[
X>\varrho,
\]

in particular for every window containing the prime \(2\).

These obstructions do not disprove simple/even ground states.  They prove that
two obvious Perron--Frobenius cones cannot establish them globally.

## 9. Sharp residual-to-ground-state transport

### Theorem 9.1 — one-sided residual/gap bound **[PROVED; SHARP]**

Let \(A=A^*\) be a self-adjoint operator on a Hilbert space, let
\(k\in\operatorname{Dom}(A)\) be a unit vector, and suppose its lowest
eigenvalue
\(\lambda_0\) is simple, with unit eigenvector 
\(\phi_0\), and

\[
\sigma(A)\setminus\{\lambda_0\}\subset[b,\infty)
\]

for some \(b>\lambda_0\).  Define

\[
\rho=\langle k,Ak\rangle,
\qquad
r=(A-\rho)k,
\qquad
\epsilon=\|r\|.
\]

Assume the one-sided ground isolation

\[
\rho<b,
\qquad
\gamma=b-\rho>0.
\]

Then

\[
\boxed{
0\le\rho-\lambda_0\le\frac{\epsilon^2}{\gamma}.
}
\]

After phase-aligning 
\(\phi_0\) with \(k\),

\[
\boxed{
|\langle\phi_0,k\rangle|
\ge\frac{\gamma}{\sqrt{\gamma^2+\epsilon^2}},
}
\]

\[
\boxed{
\sin\angle(k,\phi_0)
\le\frac{\epsilon}{\sqrt{\gamma^2+\epsilon^2}},
}
\]

and

\[
\boxed{
\|k-\phi_0\|
\le
D(\epsilon/\gamma)
:=\sqrt{2\left(1-\frac1{\sqrt{1+(\epsilon/\gamma)^2}}\right)}
\le\frac\epsilon\gamma.
}
\]

The constants are attained in a two-level system.

#### Proof

Put \(d=\rho-\lambda_0\), and let \(\mu_k\) be the spectral measure of
\(k\).  It is supported on \(\{\lambda_0\}\cup[b,\infty)\), so

\[
0\le\int(\lambda-\lambda_0)(\lambda-b)\,d\mu_k(\lambda)
=\epsilon^2-d\gamma.
\]

The integral is finite because \(k\in\operatorname{Dom}(A)\); its expansion
uses \(\int(\lambda-\rho)\,d\mu_k(\lambda)=0\).  This gives the energy
bound.  If \(Q_0=I-P_{\phi_0}\), then

\[
d
=\langle k,(A-\lambda_0)k\rangle
\ge(b-\lambda_0)\|Q_0k\|^2
=(d+\gamma)\|Q_0k\|^2.
\]

Combining this with 
\(d\le\epsilon^2/\gamma\) yields

\[
\|Q_0k\|^2
\le\frac{\epsilon^2}{\gamma^2+\epsilon^2}.
\]

The overlap and angle bounds follow.  For phase-aligned unit vectors,

\[
\|k-\phi_0\|^2
=2(1-|\langle k,\phi_0\rangle|),
\]

which gives \(D\).  Equality throughout occurs for

\[
A=\operatorname{diag}(0,b),
\qquad
k=(\cos\theta,\sin\theta).
\]

\(\square\)

The \(D\)-expression is an upper bound in general, not an identity for the
actual distance.  Also,

\[
(I-P_k)(A-\rho)k=(A-\rho)k
\]

for unit \(k\); the projection in the old residual definition was redundant.

### Failure modes that must be excluded

- An excited exact eigenvector has zero residual.  The one-sided condition
  
  \(\rho<b\) is what identifies the bottom state.
- A collapsing gap makes absolute residual meaningless.  For
  
  \(A_\delta=\operatorname{diag}(0,\delta)\) and
  
  \(k=2^{-1/2}(1,1)\), the residual tends to zero while the ground-state angle
  stays fixed.
- Applying the theorem in the even sector does not establish a global even
  ground until 
  \(\lambda_0(A_+)<\lambda_0(A_-)\) is certified.
- A Galerkin gap is not automatically a continuum gap.  Spectral enclosure
  and no-pollution estimates are required.

## 10. Weighted Mellin transport

Let

\[
I_X=[X^{-1/2},X^{1/2}],
\qquad
d^*u=\frac{du}{u},
\qquad
w_\alpha(u)=u^\alpha+u^{-\alpha}.
\]

### Theorem 10.1 — exact expanding-window embedding **[PROVED]**

Fix \(0<\alpha<1/2\).  Suppose
\(U:H\to L^2(I_X,d^*u)\) is an isometry.  With the notation of
Theorem 9.1, let

\[
f=c\,U\phi_0,
\qquad
g=c\,Uk.
\]

Then

\[
\|f-g\|_2\le |c|D(\epsilon/\gamma)
\]

and

\[
\boxed{
\|f-g\|_{L^1(w_\alpha d^*u)}
\le
C_\alpha(X)|c|D(\epsilon/\gamma),
}
\]

where

\[
\boxed{
C_\alpha(X)^2
=2\log X+\frac{X^\alpha-X^{-\alpha}}{\alpha}.
}
\]

#### Proof

The \(L^2\) statement is Theorem 9.1 and the isometry.  Cauchy--Schwarz gives

\[
\int_{I_X}|f-g|w_\alpha\,d^*u
\le\|f-g\|_2
\left(\int_{I_X}w_\alpha^2\,d^*u\right)^{1/2}.
\]

Expanding 
\((u^\alpha+u^{-\alpha})^2\) and integrating yields the displayed constant.
\(\square\)

For fixed \(\alpha>0\) and \(X\to\infty\), since \(X=\lambda^2\),

\[
C_\alpha(X)\asymp\frac{\lambda^\alpha}{\sqrt\alpha}.
\]

Thus 
\(\epsilon/\gamma\to0\) alone is insufficient.  A direct sufficient rate is

\[
\boxed{
|c_j|C_\alpha(X_j)D(\epsilon_j/\gamma_j)\to0
\quad\text{for every }0<\alpha<\tfrac12.
}
\]

If the explicit candidate must first be projected into a finite Galerkin
space,

\[
k_{X,K}=\frac{P_{X,K}k_X}{\|P_{X,K}k_X\|},
\]

then one must add the separate truncation error

\[
\tau_{j,\alpha}
=\|c_jU_jk_{X_j,K_j}-k_{X_j}\|_{1,\alpha}.
\]

### Proposition 10.2 — weighted tightness alternative **[PROVED]**

In centered logarithmic coordinates \(t=\log u\), suppose

\[
\|h_j\|_2\to0.
\]

If, for every \(0\le\alpha<1/2\), there is a
\(\beta\) with \(\alpha<\beta<1/2\) such that

\[
\sup_j\int|h_j(t)|\,2\cosh(\beta t)\,dt<\infty,
\]

then

\[
\int|h_j(t)|\,2\cosh(\alpha t)\,dt\to0.
\]

#### Proof

Split at 
\(|t|=R\).  On the compact part, Cauchy--Schwarz bounds the integral by

\[
2\cosh(\alpha R)\sqrt{2R}\,\|h_j\|_2.
\]

On the tail, comparison of the two cosh weights gives

\[
\int_{|t|>R}|h_j|\,2\cosh(\alpha t)\,dt
\le
\frac{\cosh(\alpha R)}{\cosh(\beta R)}M_\beta.
\]

First send \(j\to\infty\), then \(R\to\infty\). \(\square\)

Plain \(L^2\) convergence cannot replace this condition.  For fixed
\(0<\alpha<1/2\),

\[
h_L(t)=e^{-\alpha L/2}
1_{[L/2-1,L/2]}(t)
\]

has 
\(\|h_L\|_2\to0\), while its 
\(e^{\alpha|t|}\)-weighted \(L^1\) norm stays bounded away from zero.

### Lemma 10.3 — weighted \(L^1\) gives uniform Mellin control **[PROVED]**

Use

\[
\mathcal Mf(z)=\int_0^\infty f(u)u^{-iz}\,\frac{du}{u}.
\]

For every 
\(|\operatorname{Im}z|\le\alpha\),

\[
\boxed{
|\mathcal Mf(z)-\mathcal Mg(z)|
\le\|f-g\|_{L^1(w_\alpha d^*u)}.
}
\]

#### Proof

Since

\[
|u^{-iz}|=u^{\operatorname{Im}z}
\le u^\alpha+u^{-\alpha},
\]

the triangle inequality proves the claim. \(\square\)

This is uniform on the whole closed horizontal substrip, hence locally uniform
on the open critical strip.

## 11. Exact Hurwitz/Rouché closure

Normalize

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad
\Xi(z)=\xi(1/2+iz),
\]

and let

\[
\mathcal S=\{z:|\operatorname{Im}z|<1/2\}.
\]

### Theorem 11.1 — real-rooted approximation closure **[PROVED]**

Suppose \(F_j,G_j\) are holomorphic on 
\(\mathcal S\) and:

1. every zero of \(F_j\) in 
   \(\mathcal S\) is real;
2. \(G_j\to\Xi\) locally uniformly on 
   \(\mathcal S\);
3. for every compact substrip,
   
   \(F_j-G_j\to0\) uniformly;
4. 
   \(\Xi\not\equiv0\).

Then every zero of 
\(\Xi\) in 
\(\mathcal S\) is real.  Consequently RH holds.

#### Proof

The hypotheses give \(F_j\to\Xi\) locally uniformly.  If 
\(\Xi\) had a
nonreal zero \(z_0\), choose a closed disk around \(z_0\) contained in one of
the two open half-strips and with no zero of 
\(\Xi\) on its boundary.
Uniform convergence and Rouché's theorem force \(F_j\) to have the same
positive number of zeros in that disk for all sufficiently large \(j\),
contradicting the real-rootedness of \(F_j\).  Every nontrivial zeta zero has
\(0<\Re\rho<1\), so its coordinate 
\(z=(\rho-1/2)/i\) lies in
\(\mathcal S\).  Reality of all such \(z\) is RH. \(\square\)

The limit may be 
\(E(z)\Xi(z)\) instead, provided \(E\) is holomorphic and zero-free on the
strip.

Self-adjointness of an arbitrary finite operator is not enough to supply
hypothesis 1.  For instance,

\[
f(t)=1_{[0,a]}(t)+2\,1_{[1,1+a]}(t)
\]

can be embedded as a one-dimensional self-adjoint ground state, but its
Fourier transform contains the factor

\[
1+2e^{-iz},
\]

with zeros

\[
z=(2m+1)\pi-i\log2.
\]

In the Connes--van Suijlekom construction, real-rootedness follows from the
specific divided-difference theorem under the simple/even ground-state
hypothesis; it is not a generic consequence of Hermiticity.  Their exact
result is summarized in
[*Quadratic Forms, Real Zeros and Echoes of the Spectral Action*](https://arxiv.org/abs/2511.23257).

## 12. Conditional RH bridge with explicit rates

### Theorem 12.1 — checkpoint ground-state closure **[CONDITIONAL; SUPERSEDED BY v0.2]**

Let \(X_j=\lambda_j^2\to\infty\), choose Galerkin cutoffs \(N_j\), and set

\[
H_j=E_{N_j},
\qquad
W_j=QW_{\lambda_j}^{N_j},
\]

the finite Weil compression in the Connes--van Suijlekom normalization.  Let

\[
U_j:H_j\longrightarrow L^2(I_{X_j},d^*u)
\]

be the declared isometry, and let \(k_j\in\operatorname{Dom}(W_j)\) be a unit
candidate.  Choose a scalar \(c_j\) and a same-object explicit comparison
function \(g_j\), supported in \(I_{X_j}\).  For a unit ground state
\(\phi_j\), phase-aligned with \(k_j\), define

\[
F_j(z)=\mathcal M(c_jU_j\phi_j)(z),
\qquad
G_j(z)=\mathcal M g_j(z),
\]

and

\[
\tau_{j,\alpha}
=\|c_jU_jk_j-g_j\|_{L^1(w_\alpha d^*u)}.
\]

Suppose:

1. \(W_j\) is self-adjoint and parity invariant;
2. its global ground state 
   \(\phi_j\) is simple and even;
3. a certified one-sided bound \(b_j\) satisfies
   
   \(\sigma(W_j)\setminus\{\lambda_{0,j}\}\subset[b_j,\infty)\) and   
   \(\rho_j=\langle k_j,W_jk_j\rangle<b_j\);
4. with
   
   \(\epsilon_j=\|(W_j-\rho_j)k_j\|\),
   
   \(\gamma_j=b_j-\rho_j\),
   
   \[
   |c_j|C_\alpha(X_j)D(\epsilon_j/\gamma_j)
   +\tau_{j,\alpha}\longrightarrow0
   \]
   for every 
   \(0<\alpha<1/2\);
5. the same-object transforms \(G_j\) converge locally uniformly to
   \(\Xi\) on \(\mathcal S\);
6. the particular finite ground-state transforms \(F_j\) are the real-rooted
   entire functions furnished by the
   Connes--van Suijlekom/Connes--Consani--Moscovici construction.

Then RH holds.

#### Proof

Theorem 9.1 gives the ground-state error.  Theorem 10.1 and the triangle
inequality give

\[
\|c_jU_j\phi_j-g_j\|_{L^1(w_\alpha d^*u)}
\le |c_j|C_\alpha(X_j)D(\epsilon_j/\gamma_j)+\tau_{j,\alpha}
\longrightarrow0.
\]

Lemma 10.3 therefore gives \(F_j-G_j\to0\) uniformly on each compact
substrip.  Since \(G_j\to\Xi\) locally uniformly and the \(F_j\) are
real-rooted, Theorem 11.1 applies. \(\square\)

This theorem is an exact conditional reduction, not a proof of any one of its
load-bearing hypotheses.

## 13. What the finite cyclotomic grid can approximate

The finite-field carrier remains auxiliary.  Once the Archimedean coordinate

\[
\alpha_X(n)=\frac{\log n}{\log X}
\]

has been supplied, an \(M\)-point cyclotomic grid can quantize it.

Choose \(q_M(\alpha)\in M^{-1}\mathbb Z/\mathbb Z\) nearest to 
\(\alpha\), with a fixed tie rule.  Then

\[
d_{\mathbb T}(\alpha,q_M(\alpha))\le\frac1{2M}
\]

and, for every integer \(r\),

\[
\boxed{
|e^{-2\pi ir\alpha}-e^{-2\pi irq_M(\alpha)}|
\le\min\left(2,\frac{\pi|r|}{M}\right).
}
\]

### Proposition 13.1 — exact DFT aggregation and Toeplitz error **[PROVED]**

Let

\[
w_n=\frac{\Lambda(n)}{\sqrt n},
\qquad
W_X=\sum_{1<n<X}w_n,
\]

and aggregate all atoms sent to bin \(j\) into

\[
c_j=\sum_{n:q_M(\alpha_X(n))=j/M}w_n.
\]

Then

\[
\widehat\mu_M(r)
=\sum_{j=0}^{M-1}c_je^{-2\pi irj/M},
\qquad
\widehat\mu_M(r+M)=\widehat\mu_M(r),
\]

and DFT inversion recovers exactly the bin masses \(c_j\), not the individual
atoms within a bin.  Moreover,

\[
|\widehat\mu_M(r)-\widehat\mu_X(r)|
\le\frac{\pi|r|}{M}W_X.
\]

For 
\(-K\le r,s\le K\), define the moment matrices

\[
T_{rs}=\widehat\mu_X(s-r),
\qquad
(T_M)_{rs}=\widehat\mu_M(s-r).
\]

Then

\[
T=V^*\operatorname{diag}(w_n)V,
\qquad
V_{n,r}=e^{-2\pi ir\alpha_X(n)},
\]

so \(T\succeq0\), and

\[
\boxed{
\|T-T_M\|_{\mathrm{op}}
\le
\frac{\pi W_XK(2K+1)}{M}.
}
\]

#### Proof

The chord bound follows from 
\(|e^{i\theta}-e^{i\varphi}|\le|\theta-\varphi|\).  Summing it with the
positive weights proves the Fourier estimate.  The Gram factorization follows
by expanding its 
\((r,s)\)-entry.  Finally, every entry of \(T-T_M\) is at most
\(\pi W_X|s-r|/M\), and the maximal absolute row sum is bounded by

\[
\frac{\pi W_X}{M}\sum_{j=0}^{2K}j
=\frac{\pi W_XK(2K+1)}M.
\]

For a Hermitian matrix, the operator norm is at most that row-sum bound.
\(\square\)

Thus \(M\gg K\) controls an individual total-mass-normalized Fourier phase,
while uniform relative control of the full 
\(|r|\le K\) Toeplitz block asks for

\[
M\gg K^2.
\]

This positive moment matrix is generic positivity of a positive measure.  The
arithmetic block enters the completed Weil form with a minus sign, so
\(T\succeq0\) is not Weil positivity.

The phase estimate also does not imply operator-norm convergence of the raw
shifts 
\(S_{q_M(\alpha)L}\) to 
\(S_{\alpha L}\).  Translation is strongly but not
norm continuous on full \(L^2\).  Grid-error claims must therefore name a
fixed Fourier/Galerkin band or a weaker topology.

## 14. Current frontier check

As of 3 September 2026, the source record supports the following boundary:

- Connes--Consani--Moscovici prove the finite real-zero construction assuming
  a simple even ground state, and explicitly list global simple/evenness and
  prolate-candidate approximation as the two missing steps in
  [*Zeta Spectral Triples*](https://arxiv.org/abs/2511.22755).
- Connes--van Suijlekom prove the divided-difference real-zero theorem under
  the same simple/even spectral hypothesis in
  [*Quadratic Forms, Real Zeros and Echoes of the Spectral Action*](https://arxiv.org/abs/2511.23257).
- Suzuki supplies an unconditional screw-function and operator framework, and
  proves simple/evenness only in a sufficiently small window in
  [*Weil's quadratic form via the screw function*](https://arxiv.org/abs/2606.09096).
- Zhu's 2 September 2026 revision certifies positivity and a simple even
  ground at the single compact window \(L=0.8\), while also exhibiting a
  Landau--Widom-scale collapse of the bottom margin; it does not prove the
  large-window statement.  See
  [*Weil positivity in compact windows*](https://arxiv.org/abs/2608.24827).
- Groskin proves an exact finite Guinand--Weil dictionary and quantitative
  Archimedean tail budget, sharpening what finite computations do and do not
  certify.  See
  [*A finite Guinand--Weil dictionary and archimedean tail order*](https://arxiv.org/abs/2607.02828).

Therefore none of the open hypotheses in Theorem 12.1 can be imported from
the current literature.

## 15. The next proof contract

The least inflated useful target is not “prove Weil positivity.”  It is the
following stronger, falsifiable route-specific statement.

### Boundary--Schur--Mellin estimate **[OPEN]**

Find an unbounded sequence 
\((X_j,K_j)\) and explicit normalized even candidates

\[
k_j\in E_{X_j,K_j}^+
\]

such that:

1. **Parity certificate.**  If
   
   \(W_{j,+}=\begin{psmallmatrix}\rho_j&r_j^*\\r_j&D_j\end{psmallmatrix}\)
   relative to \(k_j\) and 
   \(\lambda_{j,-}=\lambda_0(W_{j,-})\), then
   
   \[
   \lambda_{j,-}<\lambda_0(D_j)
   \]
   and
   
   \[
   \rho_j-\lambda_{j,-}
   -\langle r_j,(D_j-\lambda_{j,-})^{-1}r_j\rangle<0.
   \]

2. **One-sided spectral enclosure.**  A certified \(b_j\) bounds every
   non-ground eigenvalue from below and 
   \(\gamma_j=b_j-\rho_j>0\).

3. **Weighted residual rate.**  For every 
   \(0<\alpha<1/2\),
   
   \[
   |c_j|C_\alpha(X_j)
   D\!\left(\frac{\epsilon_j}{\gamma_j}\right)
   +\tau_{j,\alpha}\to0.
   \]

4. **Same-object transform limit.**  The normalized candidate transforms
   converge to 
   \(\Xi\), and the finite real-rooted transforms are exactly the transforms
   controlled by item 3, not unrelated spectral determinants.

Items 1--3 mention neither zeta zeros nor Weil positivity.  They can fail even
if RH is true, so this is not a syntactic reformulation of RH.  Together with
the already-proved closure theorem, however, they would finish this route.

The new boundary identities suggest where to attack item 3.  One needs
vector-specific estimates in the natural \(H^{\log}\) topology, then a
summable or cancellation-aware control over all LCM shells.  Operator-norm
smallness is unavailable, and absolute summation pays a 
\(\sqrt X\)-scale cost.

### Alternative finite-window certificate **[PROVED REDUCTION; OPEN ESTIMATES]**

For a fixed window, decompose the closed form domain into a computable finite
space \(V_K\) and its orthogonal complement.  Suppose certified constants

\[
q(u)\ge\alpha\|u\|^2,
\qquad
q(v)\ge\beta\|v\|^2,
\qquad
|q(u,v)|\le\epsilon\|u\|\|v\|
\]

hold for 
\(u\in V_K\) and 
\(v\in V_K^\perp\).  Then

\[
\boxed{
\lambda_0(q)
\ge
\frac{\alpha+\beta
-\sqrt{(\alpha-\beta)^2+4\epsilon^2}}2.
}
\]

In particular, the whole window is certified positive if

\[
\alpha>0,
\qquad
\beta>0,
\qquad
\alpha\beta>\epsilon^2.
\]

#### Proof

For \(f=u+v\), the three assumptions bound \(q(f)\) below by the quadratic
form of the \(2\times2\) matrix

\[
\begin{pmatrix}\alpha&-\epsilon\\-\epsilon&\beta\end{pmatrix}
\]

on 
\((\|u\|,\|v\|)\).  Its smaller eigenvalue is the displayed expression.
\(\square\)

The open work is to obtain high-frequency coercivity 
\(\beta\) and off-block
control 
\(\epsilon\) in the \(H^{\log}\) topology.  This is a cleaner finite-window
target than extrapolating an uncertified Galerkin eigenvalue.

## 16. Executable verification and mutation audit

The companion script

[`checkpoint_proof_probes.py`](checkpoint_proof_probes.py)

performs deterministic numerical checks of the finite identities.  It covers:

- LCM jumps, divisor inversion, and the prime-power Möbius sieve;
- prime-tower resolvents, KMS inverses, determinants, phase gauges, and bounds;
- path-chain spectra;
- the boundary commutator identity;
- the explicit odd-ground parity counterexample;
- the shell-birth Hilbert--Schmidt law and raw norm discontinuity;
- multilevel residual/gap bounds and sharp two-level saturation;
- the exact weighted embedding constant and an expanding-window
  \(L^2\)-counterexample;
- exact DFT aggregation, Toeplitz compression control, and coarse-grid
  collisions.

It also injects corrupted formulas: wrong LCM weights, deleted Möbius signs,
wrong KMS endpoints and determinant exponent, missing adjoints, missing
exterior projection, reversed boundary sign, symmetry-implies-evenness,
operator-norm birth damping, excited-state residual certification, and an
unweighted Mellin closure, inconsistent common phases, and unresolved DFT
collisions.  All are required to be rejected.

Run

```bash
python checkpoint_proof_probes.py
```

or obtain structured output with

```bash
python checkpoint_proof_probes.py --json
```

The current deterministic run passes all 45 checks: 32 identity checks and
13 hostile mutations.
Floating-point checks audit implementations; they do not replace the proofs
above.

## 17. Corrections to the preceding checkpoint ledger

The following corrections should be carried forward from v0.1 of the frame:

1. On \(L^2(C_L,du)\), include the normalization \(L^{-1/2}\) in the Fourier
   basis.
2. The raw circle cutoff is strict: \(n<X\).  Endpoint inclusion is harmless
   only for a kernel vanishing at the endpoint.
3. \(M\gg K\) is a per-phase statement; full Toeplitz compression control
   requires \(M\gg K^2\).
4. The finite Weil prime block is a truncated-shift operator, not periodic
   circle convolution.
5. Prime-tower resolvents require saturation of the arithmetic cutoff relative
   to the window.
6. A common \(n^{-it}\) decoration is a unitary gauge of the entire prime
   operator.
7. Inversion symmetry does not imply an even ground state.
8. Residual control needs one-sided ground isolation and the ratio
   
   \(\epsilon/\gamma\), not an absolute residual.
9. Expanding windows require the weighted rate and scalar normalization in
   Theorem 10.1; plain \(L^2\) convergence is insufficient.
10. Suzuki's function uses 
    \(g=-\Psi\), and its positive-semidefinite kernel is
    
    \(\Psi(t)+\Psi(u)-\Psi(t-u)\).  Reversing this sign reverses the claim.
11. For 
    \(I_L=(-L/2,L/2)\), one has \(L=\log X\), not half or twice that value;
    the difference set has radius \(L\).

## 18. Claim ledger

### Proved here

- the LCM--Weil truncated-shift update law;
- the saturated primitive-prime resolvent decomposition;
- the direct-integral KMS chain model, including inverse, determinant,
  positivity, and uniform spectral bounds;
- the full-prime common-phase gauge no-go theorem;
- the exact boundary commutator and leakage inequality;
- the path-chain spectrum and the operator-norm endpoint discontinuity;
- the LCM screw-kernel decomposition, quadratic shell-birth law, and
  \(H^{\log}\)-form continuity;
- exact even/odd Loewner block formulas;
- the odd-ground counterexample inside the full divided-difference class;
- the parity Schur-complement certificate;
- the sharp residual/gap theorem;
- the weighted embedding, Mellin convergence, and Rouché closure theorems;
- exact DFT aggregation and the \(M\gg K^2\) compression scale.

### Classical or repackaged rather than RH progress

- LCM jumps as 
  \(\Lambda\), Möbius inversion, and the Stieltjes comb;
- Kac--Murdock--Szegő covariance identities;
- compression commutator algebra;
- Kato--Temple, Schur complement, and Hurwitz/Rouché arguments.

Their organization around the checkpoint frame is useful, but no literature
novelty is claimed without a separate search and expert review.

### Refuted

- the prime operator alone has nontrivial spectral dependence on the common
  Archimedean phase;
- reversal symmetry or divided-difference structure forces an even ground;
- either obvious Perron--Frobenius cone works globally;
- a boundary commutator is automatically small in operator norm;
- prime shells damp in raw operator norm at their cutoff birth;
- a small absolute residual identifies the ground;
- \(L^2\)-ground-state convergence automatically yields Mellin convergence on
  the critical strip.

### Open

- a parity certificate along an unbounded sequence of genuine Weil matrices;
- a continuum one-sided gap with no spectral pollution;
- summable vector-specific boundary leakage in the natural form topology;
- the weighted residual and Galerkin-truncation rate;
- weighted convergence of the genuine ground transforms to the already
  source-controlled explicit prolate candidate;
- unconditional large-window convergence of the finite real-rooted objects.

### Dark

- whether this route can beat the Landau--Widom collapse;
- whether the boundary/Archimedean coupling contains a new positivity
  mechanism rather than a very accurate finite encoding of the explicit
  formula;
- RH itself.

## 19. Research decision

Keep the LCM filtration as the exact arithmetic input and discard carrier-prime
phase stabilization as the main experiment.  The next serious proof attempt
should work in this order:

1. use the exact parity blocks and Schur scalar to certify simple/evenness;
2. estimate boundary leakage in \(H^{\log}\), not raw operator norm;
3. convert that estimate into the weighted residual rate, including scalar and
   Galerkin normalizations;
4. only then invoke the finite real-zero theorem and Rouché closure.

That is now a mathematically closed dependency chain.  Every remaining dark
edge is explicit, quantitative, and independently falsifiable.