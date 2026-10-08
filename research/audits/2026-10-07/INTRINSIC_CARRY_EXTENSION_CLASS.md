# The invariant causal carry: split versus nonsplit prime-digit group extensions

**Date:** 2026-10-07  
**Branch:** \`research/causal-filtration-energy-2026-10-07\`  
**Status:** exact classical arithmetic/group-extension theorem and gauge-dependence control; **RH OPEN**.

## Provenance

**User-origin hypothesis:** at each wavefront event, only existing arithmetic information may constrain the next local realization; prime axes and prime-power depths behave differently, with carry encoding their history.

**Current derivation:** GPT-6 using classical finite cyclic groups, CRT, 2-cocycles/group extensions, normalized-Haar Fourier digits, and explicit successor matrices. This is a **precise application of elementary known algebra**, not a claim to have invented extension cohomology.

**Previous repo context:** \`FRESH_DIGIT_ISOMETRIC_ACTUALIZATION.md\` constructed a finite isometric refinement with a chosen global mixed-radix Fourier digit and obtained a *rank-one* SUCC commutator. This theorem **corrects the overinterpretation**: rank one is section-dependent; the extension's split/nonsplit class is invariant. Earlier Round005–006 already identified affine carry and CRT flatness. The present calculation reconciles them.

**Verification:** \`scripts/rh_carry_extension_controls.py\`, independent isolated Python/NumPy test over 10 pairs \((L,p)\), including fresh-prime and repeated-prime cases. The actual executed local source and outputs are logged in \`CAUSAL_FILTRATION_EXECUTION.md\`. Not a CI/peer-review claim.

## 1. The exact finite arithmetic extension

At a prime-power LCM birth \(n=p^k\), set \(L=L_{n-1}\). Then \(L_n=pL\), and reduction modulo \(L\) gives the short exact sequence of additive cyclic groups

\[
\boxed{
0\longrightarrow\mathbb Z/p\mathbb Z
\xrightarrow{\;\iota\;}
\mathbb Z/pL\mathbb Z
\xrightarrow{\;\pi\;}
\mathbb Z/L\mathbb Z
\longrightarrow0,
}
\]

where \(\iota(t)=Lt\bmod pL\) and \(\pi(r)=r\bmod L\).

This is the **actual next arithmetic information fiber**. No future data are required to construct it.

### Theorem A — split iff the prime axis is genuinely new

\[
\boxed{
\text{The extension splits as abelian groups}
\iff
\gcd(p,L)=1.
}
\]

**Proof.** A group-theoretic section \(s:\mathbb Z/L\to\mathbb Z/pL\) must send the old generator \(1\bmod L\) to a lift \(x\bmod pL\) satisfying

\[
x\equiv1\pmod L,\qquad Lx\equiv0\pmod{pL}.
\]

The second congruence is equivalent to \(p\mid x\). Thus the section requires a solution of

\[
x\equiv1\pmod L,\qquad x\equiv0\pmod p,
\]

which exists by CRT iff \(\gcd(p,L)=1\). Conversely, such a solution defines a homomorphic section by \(s(r)=rx\bmod pL\). QED.

Consequently:

- For the **first occurrence of a prime \(p\)** in the LCM clock, \(p\nmid L_{p-1}\). The extension splits. The new prime is an independent CRT axis.
- For an event \(n=p^k\), \(k\ge2\), \(p\mid L_{n-1}\). The extension is **nonsplit**. The new digit extends an already occupied \(p\)-adic axis and necessarily carries across its existing digits.

This is a gauge-independent distinction between "new dimension" and "deeper dimension."

## 2. The explicit carry 2-cocycle

Choose the simple set-theoretic section \(s(r)=r\) with \(0\le r<L\). It need not be a group homomorphism.

Its additivity defect is

\[
\boxed{
c_L(a,b)=\left\lfloor\frac{a+b}{L}\right\rfloor\bmod p,
\qquad 0\le a,b<L.
}
\]

Indeed,

\[
s(a)+s(b)
=
s((a+b)\bmod L)+L\,c_L(a,b)
\quad\text{in }\mathbb Z/pL.
\]

Associativity of addition gives the cocycle identity

\[
\boxed{
c_L(a,b)+c_L((a+b)\bmod L,c)
=
c_L(b,c)+c_L(a,(b+c)\bmod L)
\pmod p.
}
\]

Changing the section changes \(c_L\) by a **coboundary**, but the extension class \([c_L]\) is invariant.

For \(p\nmid L\), let \(t\equiv L^{-1}\pmod p\). Then the 1-cochain \(f(r)=tr\bmod p\) satisfies

\[
f(a)+f(b)-f((a+b)\bmod L)
=
c_L(a,b)\pmod p.
\]

Thus \([c_L]=0\) in the new-prime/CRT-split case.

For \(p\mid L\), Theorem A proves that no such coboundary trivialization exists, so \([c_L]\ne0\).

Equivalently, with trivial action,

\[
\boxed{
H^2(\mathbb Z/L,\mathbb Z/p)
\cong\mathbb Z/\gcd(L,p)\mathbb Z,
}
\]

and our extension is the nonzero class precisely when \(p\mid L\). (The group-cohomology identity is standard; the explicit proof above does not need its citation.)

This is an **intrinsic carry obstruction**, unlike any particular commutator matrix's numerical rank.

## 3. Correct local \(p\)-adic Fourier digit

Let

\[
L=p^aM,\qquad p\nmid M.
\]

At the new stage \(pL\), the genuinely new local \(p\)-adic digit is

\[
\boxed{
d_p(r)=
\left\lfloor
\frac{r\bmod p^{a+1}}{p^a}
\right\rfloor\in\{0,\ldots,p-1\}.
}
\]

Let \(Jf(r)=f(r\bmod L)\), and define the **local** Fourier innovation

\[
(V_pf)(r)=e^{2\pi i d_p(r)/p}\,f(r\bmod L).
\]

For every old residue \(r_0\bmod L\), its \(p\) lifts \(r_0+kL\) realize each value of \(d_p\) exactly once, because \(M\) is invertible mod \(p\).

Therefore \(J^*J=V_p^*V_p=I,\ J^*V_p=0\) in normalized Haar spaces.

For every \(\omega\ge0\),

\[
\boxed{
W_{p,\omega}
=
p^{-\omega}J+\sqrt{1-p^{-2\omega}}\,V_p
}
\]

is isometric, and the old/fresh digit outcome probabilities are exactly

\[
p^{-2\omega},\qquad 1-p^{-2\omega}.
\]

So the local energy conservation and Suzuki support probability survive the correction from a *global mixed-radix* choice to the intrinsic *local \(p\)-adic digit*.

## 4. Where SUCC acts on the local innovation

Write \(\zeta_p=e^{2\pi i/p}\) and \(S_L f(r)=f(r-1\bmod L)\).

For the local \(p\)-adic digit,

\[
\boxed{
(S_{pL}V_p-V_pS_L)f(r)
=
(\zeta_p^{-1}-1)\,
\mathbf1_{\{r\bmod p^a=0\}}\,
\zeta_p^{d_p(r)}
f((r-1)\bmod L).
}
\]

This is supported precisely on the **lower-\(p\)-digit carry hyperface**.

For \(\omega>0\), its weighted refinement defect

\[
S_{pL}W_{p,\omega}-W_{p,\omega}S_L
\]

has **rank \(M=L/p^a\)** (with the interpretation \(a=0\), \(M=L\)) and exact operator norm

\[
\boxed{
2\sin\frac{\pi}{p}\sqrt{1-p^{-2\omega}}.
}
\]

The rank changes with the other-prime CRT multiplicity \(M\), while the operator norm is independent of \(M\).

### Critical scope correction

The earlier choice

\[
V^{\rm mixed}f(r_0+kL)=\zeta_p^k f(r_0)
\]

makes the commutator **rank one** at the single global mixed-radix wrap \(r_0=0\). The local \(p\)-digit convention instead makes the commutator rank \(M\).

Both formulas are exact in their respective chosen coordinates. **Neither rank is an intrinsic arithmetic curvature invariant.** The invariant distinction is the group-extension cohomology class: split at \(p\nmid L\), nonsplit at \(p\mid L\).

## 5. Why this is mathematically cleaner

The user-origin cube framing now has a theorem-level bifurcation:

\[
\boxed{
\text{new prime}
\iff
\text{CRT-split new axis}
}
\]

and

\[
\boxed{
\text{repeated prime power}
\iff
\text{nonsplit carry extension}.
}
\]

The distinction is **causal** (only \(L\) and \(p\) needed), **representation-invariant** (extension class), and **not a physical quantum/GR assertion**.

A plausible next test is to build the completed prime/Archimedean observation on this *intrinsic* distinction, requiring that split axes remain flat under CRT recombination while the nonsplit depth cocycle enters only via genuine source-derived carry.

But a cohomology class and a finite isometry **do not imply Hardy innerness** or Weil positivity. The exact analytic observation and global signed cancellation remain the unpaid RH theorem.

## 6. Claim ledger

**PROVED (classical algebra):** short exact sequence; splitting iff \(p\nmid L\); explicit carry 2-cocycle and its cohomology class.

**PROVED (finite operator algebra):** local \(p\)-adic Fourier digit orthogonal to old Haar state; \(W_{p,\omega}\) is isometric; SUCC commutator support, rank \(L/p^{v_p(L)}\), norm \(2\sin(\pi/p)\sqrt{1-p^{-2\omega}}\).

**CORRECTED:** rank-one global mixed-radix carry is *not* gauge invariant and must not be used as intrinsic curvature.

**UNVERIFIED:** a physically/canonically selected observation realizing Suzuki \(\Theta_\omega\) and all-\(\omega\) Hardy passivity.

**RH:** OPEN.
