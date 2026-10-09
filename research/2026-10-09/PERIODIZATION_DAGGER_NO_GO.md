# Why the naïve reverse adjoint on the common Archimedean history cover does not exist boundedly

**2026-10-09. Exact functional-analysis no-go; zero-free. RH OPEN.**

The common cover E_2 <- C× -> E_6 is an exact reversible correspondence, but its obvious periodization maps are not bounded L² operators. This is a mathematically precise obstruction to "simply invert the Archimedean shadow" and is a natural place to investigate a source-derived dualizing/trace renormalization.

## 1. Unbounded periodization

For a period ell>0, define on compactly supported smooth f on R

\[
(\mathcal P_\ell f)(x\bmod\ell)=\sum_{k\in\mathbb Z}f(x+k\ell).
\]

This is the natural pushforward from the logarithmic universal cover to the real cycle of E_m when ell=log m.

The sum is finite for compactly supported f, but

\[
\boxed{
\mathcal P_\ell:L^2(\mathbb R)\to L^2(\mathbb R/\ell\mathbb Z)
\text{ has NO bounded extension.}
}
\]

Proof: choose nonzero smooth phi with compact support in (0,ell/2) and \(\|\phi\|_{L^2(\mathbb R)}=1\). Define

\[
f_N(x)=N^{-1/2}\sum_{j=1}^N\phi(x+j\ell).
\]

The supports are disjoint, so \(\|f_N\|_2=1\). But for x modulo ell,

\[
\mathcal P_\ell f_N(x)=\sqrt N\,\phi(x)
\]

on the fundamental interval. With normalized circle measure dx/ell, its norm is \(\sqrt{N/\ell}\), unbounded. QED.

Thus a naive Hilbert adjoint \(\mathcal P_\ell^*\) defined on the whole circle cannot serve as the complete backward-history reconstruction map.

This is not special to primes; source rigidity requires an *additional* arithmetic/adelic coupling.

## 2. The two-prime correspondence forces the same issue at both ends

For E_2 and E_6, ell_2=log2 and ell_6=log6. Both projections from the common cover C× have infinitely many deck sheets; both naive L² pushforwards are unbounded as above.

The previous note proved

\[
(\log2\,\mathbb Z+2\pi i\mathbb Z)
\cap
(\log6\,\mathbb Z+2\pi i\mathbb Z)
=2\pi i\mathbb Z.
\]

Hence no compact common identity-cover exists; there is no finite-dimensional periodic remedy for this exact gluing class. More general correspondences may exist, but they must specify the trace/adjoints.

## 3. What the actual Gaussian does to this divergence

The canonical Archimedean Tate atom is

\[
g(x)=e^{-\pi x^2}.
\]

On the logarithmic multiplicative coordinate x=e^u,

\[
G(u)=g(e^u)=e^{-\pi e^{2u}}.
\]

Its two tails are very different:

\[
G(u)\to1\quad(u\to-\infty),
\qquad
G(u)\to0\quad(u\to+\infty).
\]

Consequently the bare series

\[
\sum_{k\in\mathbb Z}G(u+k\ell)
\]

diverges at the negative end for any ell>0. A possible elementary tail subtraction is

\[
\boxed{
\widetilde G_\ell(u)
=
\sum_{k\in\mathbb Z}
\left[
G(u+k\ell)-1_{\{k<0\}}
\right].
}
\]

For each fixed u, the summands decay exponentially as k->-infinity after subtraction and super-exponentially as k->+infinity, so this is absolutely convergent. It is a **renormalized scalar function**, not a positive L² transport or a proof of an appropriate global trace.

The chosen cutoff k<0 depends on the section/origin. Any assertion that it yields the completed Weil scalar must include the corresponding section-dependence/contact-term correction. The full theta identity gives a rigorous and canonical *related* zero-mode subtraction, but the displayed scalar periodization is not automatically equivalent to that global formula.

This is the mathematical content of the "the Archimedean environment retains an infinite history and an origin counterterm" intuition.

## 4. Twistor reversal acts on the retained winding data

On the universal logarithmic coordinate z=e^u, with u=x+i theta, the signed involution

\[
j(z)=-1/\bar z
\]

lifts to

\[
\boxed{
u\mapsto-\bar u+i\pi.
}
\]

Applying it twice sends \(u\mapsto u+2\pi i\), which becomes the identity on C× but remembers one angular winding on the simply connected logarithmic universal cover.

This is consistent with the *quaternionic* square -1 of the spinorial lift on O(-1) discussed in the twistor note. It is not an equality between geometric winding 2pi i and the spin lift -1 without a specified representation.

## 5. The exact arithmetic gate this still does not pay

For the zeta Weil form on a finite window, the repo proves

\[
Q_W(f)=E_\Gamma(f)+E_{\rm prime}(f)+2|C(f)|^2-2|S(f)|^2-d_A\|f\|^2.
\]

There is NO derivation in this note of either:

- a bounded source-defined correspondence on the completed history Hilbert space whose polarizations reproduce every term of Q_W;
- a primitive Hodge-index/sign theorem for such a correspondence.

Naively claiming "the positive global history makes the negative bulk a Schur complement" would choose the joint covariance to encode RH and is circular.

## 6. One productive next experiment

Try the *actual* global theta/Poisson kernel (not the toy G-1_{k<0} periodization) as a regulator for the E_2<-C×->E_6 span, with a declared common smooth core.

Derive the adjoint/Serre residue without choosing its sign, and compute the full polarized discrepancy from Weil on the first active 2–3 window. If it outputs extra log6 connected impulses, fails genuine chi/Davenport–Heilbronn separation, or misses the exact Gamma contact and pole terms, retire the candidate.

**Result banked:** any universal-cover reverse-history construction based on naive periodization and Hilbert adjoints is analytically ill-defined in the needed global L² topology. A substantive completion/duality theory really is necessary. This is a narrow exact obstruction, not progress on the RH positivity sign.
