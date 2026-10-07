# RH proof-bearing frame audit: four obstructions and an exact corrected completion form

**Date:** 2026-10-07  
**Base:** \`aletheia/cubical-gamma-rh-proof-attempt-2026-10-07\` at \`347bb04f93791971a554d5251013ee1b83cb574e\`  
**Status:** proved finite operator/form obstructions and a corrected exact decomposition. **RH IS OPEN.**

## 0. Correction to the previous framing

The cubical, Hodge, SUCC, Mellin-Dirac and Gamma identities contain valid mathematics. They do **not** yet provide an independent sign theorem for the Weil quadratic form. An automatically positive parent Gram, a Schur complement, an \(\mathrm{SU}(1,1)\) transfer, or a product-formula primitive norm is only a potential proof mechanism after an **exact, source-derived equality** to the full completed arithmetic Weil form has been proved.

This note gives rigorous reasons why several apparently natural equalities cannot hold and prescribes a smaller, non-circular target. Its conclusions are scoped to the explicitly named constructions, not all possible positive dilations.

Primary anchors:

- Masatoshi Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function* (JLMS, 2023), Theorem 1.7: RH iff \(\Psi(t)\ge0\) on all real \(t\).
- Suzuki, *Weil's quadratic form via the screw function* (arXiv:2606.09096, 2026): the finite-interval Weil operator and its exact arithmetic/Archimedean form.
- Suzuki, *A canonical system of differential equations arising from the Riemann zeta-function* (arXiv:1204.1827): the \(\Theta_\omega\) meromorphic-inner criterion.
- In-repo: \`WEIL_PRIME_RAY_DIRICHLET_FORM.md\`, \`PRIME_SUPPORT_SUPERCONNECTION.md\`, \`CUBICAL_SHORTING_CONDITIONAL_VARIANCE.md\`, \`CUBICAL_HODGE_PRODUCT_FORMULA.md\`, and \`PROOF_ATTEMPT_FORBIDDEN_COMPOSITE_ATOMS.md\`.

---

## 1. Freeze the exact finite Weil form

Let \(a>0\), let \(v\in C_c^\infty(-a,a)\), and extend \(v\) by zero.

The repository's audited Suzuki normalization is

\[
\boxed{
Q_W^a(v)
=
K_a(v)
+
E_{\rm prime,a}(v)
-
\frac12\int_{-a}^{a}\log(a^2-x^2)|v(x)|^2\,dx
-
\mathcal V_a\|v\|_2^2
-
\langle R_av,v\rangle,
}
\]

where

\[
K_a(v)=
\frac14\int_{-a}^{a}\int_{-a}^{a}
\frac{|v(x)-v(y)|^2}{|x-y|}\,dx\,dy,
\]

\[
E_{\rm prime,a}(v)
=
\sum_{q=p^k\le e^{2a}}
w_q\|v-\tau_{\log q}v\|_{L^2(\mathbb R)}^2,
\qquad
w_q=\frac{\log p}{\sqrt q}.
\]

Here \(\mathcal V_a\) is the explicit finite diagonal counterterm of the audited Suzuki formula, and \(R_a\) is its bounded smooth remainder operator on a finite interval. **Do not alter normalization to improve an empirical fit.**

The arithmetic sum is finite at every fixed \(a\).

---

## 2. Obstruction theorem I: prime-only cubical shorting cannot be Weil

Let

\[
G_{\rm prime,a}(v)=E_{\rm prime,a}(v).
\]

Since \(\tau_h\) is unitary on the zero-extended line,

\[
\|I-\tau_h\|\le2,
\]

so

\[
\boxed{
0\le G_{\rm prime,a}(v)\le4S_a\|v\|_2^2,
\qquad
S_a=\sum_{q\le e^{2a}}w_q<\infty.
}
\]

Any positive shorted Gram of a parent whose degree-zero block is **only** this prime-edge form obeys

\[
0\preceq H_{\rm short,a}\preceq G_{\rm prime,a}.
\]

Consequently it is bounded in the \(L^2\) norm.

### Theorem: the complete localized Weil form is unbounded above

Fix \(0<c<a\) and choose \(\chi\in C_c^\infty(-a,a)\) with \(\chi=1\) on \([-c,c]\).

Put

\[
v_k(x)=\chi(x)e^{ikx}.
\]

Then \(\|v_k\|_2=\|\chi\|_2\) is independent of \(k\).

The nonnegative double integral defining \(K_a\) can be restricted to the plateau \([-c,c]^2\), where \(v_k=e^{ikx}\). Hence

\[
\begin{aligned}
K_a(v_k)
&\ge
\frac14\iint_{[-c,c]^2}
\frac{|e^{ikx}-e^{iky}|^2}{|x-y|}\,dx\,dy\\
&=
\int_0^{2c}(2c-h)\frac{1-\cos(kh)}h\,dh\\
&=
2c[\gamma+\log(2ck)-\operatorname{Ci}(2ck)]
-2c+\frac{\sin(2ck)}k\\
&=
\boxed{2c\log k+O_c(1)}.
\end{aligned}
\]

The remaining nonprime terms of \(Q_W^a\) are uniformly bounded on these particular \(v_k\): \(\chi\) is supported strictly inside the interval, \(R_a\) is bounded, and the prime form is nonnegative. Thus

\[
\boxed{
Q_W^a(v_k)\ge2c\log k-O_{a,\chi}(1)\longrightarrow+\infty.
}
\]

Therefore

\[
\boxed{
Q_W^a\ne H_{\rm short,a}
}
\]

for **every** shorted positive Gram whose raw degree-zero form is the bounded prime-only edge form.

This is a categorical failure of operator order and principal ultraviolet behavior, not a failure of numerical precision.

**Required repair:** the logarithmic Archimedean difference energy must be present in the raw physical block *before* hidden-state elimination.

---

## 3. Obstruction theorem II: merely adding the positive Gamma kinetic energy still fails

A tempting repair is

\[
G_{\rm raw,a}=K_a+E_{\rm prime,a}
\]

and to identify \(Q_W^a\) with a positive Schur short of this raw form.

Every positive short satisfies

\[
H_{\rm short,a}\preceq G_{\rm raw,a}.
\]

But \(Q_W^a\not\preceq G_{\rm raw,a}\).

### Proof by boundary localization

Choose \(0<\varepsilon<a/4\). Take any normalized smooth bump \(f_\varepsilon\) supported in

\[
(a-2\varepsilon,\ a-\varepsilon)
\]

with \(\|f_\varepsilon\|_2=1\).

On this support,

\[
a^2-x^2=(a-x)(a+x)\le4a\varepsilon.
\]

Therefore

\[
\int\log(a^2-x^2)|f_\varepsilon(x)|^2\,dx
\le\log(4a\varepsilon).
\]

Subtract the proposed raw form from the complete Weil form:

\[
Q_W^a(f_\varepsilon)-G_{\rm raw,a}(f_\varepsilon)
=
-\frac12\int\log(a^2-x^2)|f_\varepsilon|^2
-\mathcal V_a
-\langle R_af_\varepsilon,f_\varepsilon\rangle.
\]

Thus

\[
\boxed{
Q_W^a(f_\varepsilon)-G_{\rm raw,a}(f_\varepsilon)
\ge
-\frac12\log(4a\varepsilon)-\mathcal V_a-\|R_a\|.
}
\]

The right side tends to \(+\infty\) as \(\varepsilon\downarrow0\).

Hence for sufficiently small \(\varepsilon\),

\[
\boxed{
Q_W^a(f_\varepsilon)>G_{\rm raw,a}(f_\varepsilon).
}
\]

No Schur short of that raw positive form can equal \(Q_W^a\) on the smooth test core.

**Required repair:** the positive part of the logarithmic boundary potential must also be included in the raw parent before shorting.

---

## 4. Exact corrected positive/remaining decomposition

Define the real boundary potential

\[
W_a(x)=-\frac12\log(a^2-x^2),
\]

and its pointwise Jordan pieces

\[
W_{a,+}=\max(W_a,0),\qquad W_{a,-}=\max(-W_a,0).
\]

Then

\[
W_a=W_{a,+}-W_{a,-}.
\]

Define a **canonical positive raw form**

\[
\boxed{
P_a(v)
=
K_a(v)+E_{\rm prime,a}(v)
+\int_{-a}^a W_{a,+}(x)|v(x)|^2\,dx.
}
\]

Define the bounded self-adjoint residual operator

\[
\boxed{
D_a=\mathcal V_a I+R_a+M_{W_{a,-}}.
}
\]

Indeed \(W_{a,-}\in L^\infty(-a,a)\) for every fixed \(a\) and \(R_a\) is bounded.

The complete form is **exactly**

\[
\boxed{
Q_W^a(v)=P_a(v)-\langle D_av,v\rangle.
}
\]

This is the correct completed finite form to work with. It contains all the necessary ultraviolet and boundary growth before any Schur elimination is attempted.

A bound follows immediately:

\[
Q_W^a(v)\ge P_a(v)-\|D_a\|\|v\|_2^2.
\]

Consequently every state with \(P_a(v)>\|D_a\|\|v\|_2^2\) is automatically Weil-positive.

### Conditional low-energy spectral reduction

If the Friedrichs operator associated with \(P_a\) has compact resolvent (to be proved or sourced in this exact normalization), then only finitely many \(P_a\)-eigenmodes lie below \(\|D_a\|+\varepsilon\).

On their orthogonal complement the full form is strictly positive. A Schur elimination of this **already-positive high-energy block** then reduces the finite-\(a\) sign test to an exact finite-dimensional low-energy matrix.

This is a useful operator-theoretic proof direction, but the compact-resolvent premise and the uniform-in-\(a\) bounds are UNVERIFIED in this note.

A finite-dimensional reduction at every fixed \(a\) does not itself prove RH.

---

## 5. Obstruction theorem III: the direct adelic/Hodge response lift is rigid

The product formula says, for every \(q\in\mathbb Q^\times\),

\[
\sum_v\lambda_v(q)=0,
\qquad
\lambda_v(q)=\log|q|_v.
\]

On \(X_m=(\mathbf P^1)^m\), the primitive cubical Hodge form yields a positive scalar norm when the coefficients satisfy this sum rule. That theorem is correct.

But the proposed proof requires **Hilbert-valued place responses**, not just scalars.

Suppose one tries the natural separable response ansatz

\[
h_v(q;f)=\lambda_v(q)\,A_vf
\]

with fixed bounded operators \(A_v:\mathcal H\to\mathcal K\).

Require the Hilbert-valued primitive identity

\[
\boxed{
\sum_v h_v(q;f)=0
\quad\text{for all }q\in\mathbb Q^\times,\ f\in\mathcal H.
}
\]

Set \(q=p\), a rational prime. Only \(\lambda_p(p)=-\log p\) and \(\lambda_\infty(p)=+\log p\) are nonzero. Hence

\[
0=(\log p)(A_\infty-A_p)f
\quad\forall f,
\]

so

\[
\boxed{
A_p=A_\infty\quad\text{for every prime }p.
}
\]

Conversely, a single universal \(A\) satisfies the identity by the scalar product formula.

### Consequence

The simplest factorized Hilbert response lift is forced to be place-independent. It cannot supply the genuinely different prime translation, carry and Gamma response operators needed by the Weil form.

**An independently defined non-factorized/coupled response is mandatory.** The scalar product formula alone does not make a place-dependent Hilbert response primitive.

This is a theorem about the specified linear ansatz, not a no-go against all adelic constructions.

---

## 6. Hostile control IV: functional equation plus Hodge positivity is insufficient

Construct an even real polynomial

\[
\Xi_{\rm fake}(s)
=
\prod_{\lambda\in\{\pm a\pm i\omega\}}(s-\lambda),
\]

with \(a=1/4,\ \omega=2\pi\).

It has reflection symmetry \(\Xi_{\rm fake}(s)=\Xi_{\rm fake}(-s)\) and conjugation symmetry, but possesses off-axis zeros.

Its finite Weil/zero-tangent kernel is

\[
K(h)=\sum_\lambda e^{\lambda h}
=
4\cosh(ah)\cos(\omega h).
\]

Evaluate the two-point Gram at \(0,1\). The eigenvalues are

\[
4(1\pm\cosh(a)).
\]

One is strictly negative:

\[
\boxed{
4(1-\cosh(1/4))<0.
}
\]

The negativity persists for sufficiently narrow smooth approximations to those point masses.

Yet the cubical product-formula Hodge norm of the rational \(q=6\) vector is

\[
(\log6)^2+(\log2)^2+(\log3)^2>0.
\]

The Hodge norm does not know about the fake off-axis zero quartet.

Therefore functional-equation-style reflection and scalar product-formula positivity do not by themselves force Weil positivity. Any proposed equality of these two types of form must encode genuinely extra analytic/arithmetic information.

This is a synthetic control, not an assertion that the fake polynomial is a zeta/L-function Euler product.

---

## 7. Mutation control: automatic finite positivity is cheap

The two-event exterior shorting formula

\[
H_{\rm eff}(n)
=
\frac{|\langle v_n,v_{n+1}\rangle|^2}{\|v_{n+1}\|^2}
\]

when the denominator is nonzero, with the appropriate zero-denominator continuation, is nonnegative by Gram/Lagrange algebra.

It works with prime moduli \(2,3\) and with fake composite moduli \(4,9\). Hence nonnegative finite shorting is not sensitive to authentic primes.

A proof-relevant observable must survive the mutation controls **only** when they preserve the exact source weights and support conditions; replacing prime powers with fake events must break the purported exact Weil identification.

---

## 8. Sharper, non-circular proof target

The correct goal is not

> find any positive parent whose Schur complement is the Weil form.

That is circular unless the parent is constructed and its pushforward equality derived independently.

The acceptable target has five separate gates.

**G1 — Source correctness.** Recover Suzuki's entire completed form exactly, including the logarithmic kinetic term, boundary potential, smooth remainder, counterterm, and prime-power translations. No comparison merely on a few moments or spectral zeros.

**G2 — Microlocal correctness.** The positive raw parent must reproduce the \(2c\log k\) ultraviolet growth and the \(-\tfrac12\log(a^2-x^2)\) boundary singularity. Theorems 2 and 3 rule out smaller naive parents.

**G3 — Arithmetic observation correctness.** Internal cube faces may carry mixed conductors, but the physical scalar atomic translation spectrum must contain \(\log(p^k)\) only—not \(\log(pq)\) or \(\log(p/q)\) as extra delta lines.

**G4 — Non-circular positivity.** The place-response maps and hidden-state projection must be derived entirely from SUCC/FUCC/Gamma/source data, not chosen by factoring the target Weil operator. Exhibit the exact intertwiner/pushforward identity *before* claiming any sign.

**G5 — All horizons / subcriticality.** Prove positivity for every finite interval \(a\), or equivalently prove the Suzuki finite-Hankel contractivity criterion for every \(\omega>0,a>0\). The unconditional \(\omega=1/2\) boundary and its vanishing margin as \(a\to\infty\) do not solve the \(\omega\downarrow0\) problem.

**Proving G1--G5 would be a genuine RH proof.** No current branch completes them.

---

## 9. A defensible next mathematical attack

Study the source-defined operator pair

\[
\boxed{
Q_W^a = P_a-D_a
}
\]

with the exact positive \(P_a\) and bounded \(D_a\) from Section 4.

Do the following in order:

1. Prove compact resolvent and quantitative eigenvalue lower bounds for \(P_a\) in the same \(H_0^1(-a,a)\) normalization as Suzuki.
2. Build certified finite Galerkin low-mode matrices and rigorous high-mode coercivity bounds (no unknown zero ordinates).
3. Apply Feshbach/Schur elimination to the genuinely positive high-energy block, rather than introducing a freely chosen hidden Gram parent.
4. Derive a uniform all-\(a\) control on the resulting low-mode effective matrix **from arithmetic source/carry**, or find a finite counterexample to a proposed structural inequality.
5. Independently check the nonlinear Suzuki family \(\Theta_\omega\) for \(\omega\downarrow0\). Any proof must pay the lost critical passivity margin.

This is still difficult; it is at least an exact operator problem with explicit coefficients and no source-map ambiguity.

---

## 10. Proof-status ledger

**DISCLOSED (elementary operator/form arguments):** bounded prime Gram versus unbounded Weil UV; boundary-localization no-go for raw kinetic+prime shorting; exact \(P_a-D_a\) split with bounded \(D_a\); place-factorized primitive-response rigidity; synthetic off-line quartet defeating automatic Hodge implication.

**OBSERVED:** finite hostile numerical controls from \`scripts/rh_proof_frame_audit.py\`, run locally against the derived formulas, including prime and composite-mutation cases.

**UNVERIFIED:** compact-resolvent and uniform low-mode spectral estimates in this specific split; canonical primitive/non-factorized response map; an exact source-derived positive completion whose pushforward equals all of Suzuki/Weil.

**REFUTED within stated classes:** prime-only Schur parent; kinetic+prime-only Schur parent; separable place-by-place Hodge lift as a nontrivial prime/Gamma coupling; inference of RH from generic cubical/Hodge positivity.

**RH:** OPEN.

---

### Final correction

The arithmetic cube is a valuable **indexing and interaction space**. Gamma is a valuable **exact Archimedean operator**. Their existence is not what RH asks.

RH asks for a sign estimate on the **completed, exact Weil form** for every admissible test function. The missing sign must be created by a source-forced identity or inequality. Everything else is scaffolding.
