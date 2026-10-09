# Exact Hecke-twisted edge square and the unavoidable diagonal tax

**Date:** 2026-10-09. **Status:** exact identities for degree-one primitive Dirichlet characters; no RH/GRH proof.

This extends the already-proved zeta prime/Gamma square calculation in Round007 to unitary prime-character phases, and identifies the precise local obstruction to an independent-square proof.

## 1. Conventions

Take a primitive Dirichlet character chi modulo q with parity a (chi(-1)=(-1)^a). Work with f in C_c^\infty(-A,A), extended by zero to L²(R). Inner product is linear in its first argument. Define

\[
F(h)=\langle f,\tau_hf\rangle,\quad
\tau_hf(x)=f(x-h),\quad
w_{p,k}=(\log p)p^{-k/2}.
\]

At primes dividing q, chi(p)=0 and the corresponding local Euler factors are absent.

## 2. Twisted first-order arithmetic edge

For each active unramified prime power p^k with k log p <= 2A set

\[
\boxed{D_{p,k,\chi}f=\sqrt{w_{p,k}}(\tau_{k\log p}f-\chi(p)^k f).}
\]

Since |chi(p)|=1 for p not dividing q, unitarity of translation gives

\[
\boxed{
\|D_{p,k,\chi}f\|²
=2w_{p,k}\|f\|²
-2w_{p,k}\Re\bigl(\chi(p)^kF(k\log p)\bigr).
}
\]

Thus the full prime term in the Weil explicit formula is obtained *exactly* by the sum of positive edge squares minus their forced diagonal norm debit.

Set

\[
M_{\chi,A}=\sum_{p^k\le e^{2A},\,p\nmid q}w_{p,k}.
\]

Then

\[
\boxed{
-2\Re\sum_{p^k\le e^{2A}}w_{p,k}\chi(p)^kF(k\log p)
=E_{\mathrm{prime},\chi,A}(f)-2M_{\chi,A}\|f\|².
}
\]

The source phases are given by a single global Hecke character, not independently fitted per event.

## 3. Exact Archimedean positive difference energy

Let z_a=(2a+1)/4 and

\[
k_{\Gamma,a}(h)=\frac{e^{-(a+1/2)h}}{1-e^{-2h}}.
\]

The digamma difference identity yields, for all real u,

\[
\Re\psi(z_a+iu/2)-\psi(z_a)
=2\int_0^\infty k_{\Gamma,a}(h)(1-\cos(uh))\,dh.
\]

Therefore

\[
\boxed{
E_{\Gamma,a}(f)=\int_0^\infty k_{\Gamma,a}(h)\|\tau_hf-f\|²\,dh
=\frac1{2\pi}\int_{\mathbb R}
|\widehat f(u)|²[\Re\psi(z_a+iu/2)-\psi(z_a)]du.
}
\]

This is the correct Gamma square for parity a. At a=0 it is precisely the inherited zeta Gamma channel.

Set

\[
c_{\chi,\infty}
=\psi(z_a)+\log(q/\pi).
\]

Then the full Archimedean contribution is \(E_{\Gamma,a}(f)+c_{\chi,\infty}\|f\|²\).

## 4. The complete signed identity

For nonprincipal primitive chi there are no polar terms. The completed Weil arithmetic quadratic form equals

\[
\boxed{
Q_{\chi,A}(f)
=
E_{\Gamma,a}(f)
+
E_{\mathrm{prime},\chi,A}(f)
+
(c_{\chi,\infty}-2M_{\chi,A})\|f\|².
}
\]

For the trivial primitive character (zeta, q=1, a=0), add the exact pole term

\[
2|C_f|²-2|S_f|²,
\quad C_f=\langle f,\cosh(x/2)\rangle,\quad
S_f=\langle f,\sinh(x/2)\rangle.
\]

This specializes exactly to the existing Round007/SWS identity. Everything has been defined from character/prime powers, the logarithmic clock and Gamma. Zeros are not used.

Polarizing the displayed form gives the full sesquilinear Weil-form identity.

## 5. The local diagonal tax is forced even with arbitrary unitary phases

Suppose a Hilbert-channel first-order edge has the form

\[
Af=v\,f+z\,\tau_hf,
\]

where v,z are arbitrary fixed target vectors. Matching a desired negative correlation coefficient of magnitude w forces

\[
|\langle v,z\rangle|=w.
\]

By Cauchy–Schwarz and arithmetic–geometric mean,

\[
\boxed{
\|v\|²+\|z\|²\ge2w.
}
\]

Equality is achieved by the twisted difference edge above. Thus phases chi(p)^k do not decrease the diagonal norm debit, even though they preserve the true multiplicative source.

Summing separate prime channels costs at least \(2M_{\chi,A}\|f\|²\). A successful proof must construct a **coherent infinite-dimensional coupling across prime labels and the Archimedean place** before claiming positivity.

This is a degree-one Hecke-phase extension of the repository's previously proved local-square obstruction, not an independent global no-go theorem.

## 6. Why the three mutations really change the algebra

- Nonunitary alpha_p: \(\|\tau_hf-\alpha_pf\|²=(1+|\alpha_p|²)\|f\|²-2\Re(\alpha_pF(h))\); the exact 2w diagonal law fails.
- Fake n=6: no primitive Hecke edge exists there; adding one changes the Dirichlet-convolution logarithm at 6.
- Shifted log2: changes the shift input and violates [H,V_2]=(log2)V_2 and the fixed Archimedean product formula.

A Davenport--Heilbronn-like mixture has an actual connected source at 6, \(4ab\log6\); it cannot be represented by this single-character prime-power edge family.

## 7. The exact unpaid theorem

The construction yields a **signed** completed quadratic form. Positivity is still GRH-equivalent.

For zeta, the previously proved positive-parent/compact-sign-operator reduction remains

\[
Q_A=P_A-D_A,\qquad
B_A=P_A^{-1/2}D_AP_A^{-1/2},\qquad
Q_A\ge0\iff\|B_A\|\le1.
\]

The first two objects are rigorously defined; the all-horizon inequality is unproved. It cannot be inferred from the positive separate edge squares or from the local Hecke-character compatibility.

**Next genuine step:** derive an oriented, nonlocal, prime--Gamma interconnection from the global theta/Hecke diagonal whose cross terms pay the diagonal tax, and prove the full polarized Weil identity *before* asking for positivity. If the identity itself is assumed, or the metric is chosen to equal Q, the attempt is circular.

**RH remains open.**
