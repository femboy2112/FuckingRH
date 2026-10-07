# LCM support-face birth theorem: shadow conductors are born before visible actualization

**Date:** 2026-10-07  
**Status:** exact finite harmonic theorem. No RH assumption.  
**RH remains open.**

This note identifies exactly what happens to the full finite harmonic substrate when the LCM clock grows at a prime-power event.

The result sharpens the shadow-support idea:

> when \(N=p^k\) enlarges the minimal universal support clock, it does not merely create the visible conductor sector \(W_{p^k}\). It creates an entire orthogonal face of mixed-conductor sectors \(W_{p^ke}\), most of which correspond to integers much larger than \(N\).

Thus the finite support substrate genuinely contains harmonic conductor states before their ordinary SUCC values are causally actualized.

---

# 1. LCM birth event

Let

\[
N=p^k
\]

be a prime power and put

\[
L_-=L_{N-1},
\qquad
L_+=L_N.
\]

Then

\[
\boxed{
L_+=pL_-.
}
\]

Write

\[
\boxed{
L_-
=
p^{k-1}R,
\qquad
(p,R)=1.
}
\]

Hence

\[
L_+=p^kR.
\]

Use normalized Haar Hilbert spaces

\[
\mathcal H_-
=
L^2(\mathbb Z/L_-\mathbb Z),
\]

\[
\mathcal H_+
=
L^2(\mathbb Z/L_+\mathbb Z).
\]

Pullback along reduction embeds

\[
\mathcal H_-\hookrightarrow\mathcal H_+
\]

isometrically.

Define the new-support innovation space

\[
\boxed{
\Delta_N
=
\mathcal H_+
\ominus
\mathcal H_-.
}
\]

---

# 2. Exact-conductor decomposition

For any finite cyclic clock,

\[
\boxed{
L^2(\mathbb Z/L\mathbb Z)
=
\bigoplus_{d\mid L}W_d,
}
\]

where \(W_d\) is the exact-conductor-\(d\) additive-character space and

\[
\dim W_d=\varphi(d).
\]

Therefore

\[
\boxed{
\Delta_N
=
\bigoplus_{\substack{d\mid L_+\\d\nmid L_-}}
W_d.
}
\]

Because only the \(p\)-adic depth changed, the divisors of \(L_+\) not already dividing \(L_-\) are exactly

\[
\boxed{
d=p^ke,
\qquad
e\mid R.
}
\]

Hence:

\[
\boxed{
\Delta_{p^k}
=
\bigoplus_{e\mid R}
W_{p^ke}.
}
\]

This is the LCM support-face birth theorem.

---

# 3. Tensor form

CRT gives

\[
\mathbb Z/L_+\mathbb Z
\cong
\mathbb Z/p^k\mathbb Z
\times
\mathbb Z/R\mathbb Z.
\]

Therefore

\[
\boxed{
W_{p^ke}
\cong
W_{p^k}\otimes W_e.
}
\]

Summing over \(e\mid R\),

\[
\boxed{
\Delta_{p^k}
\cong
W_{p^k}
\otimes
L^2(\mathbb Z/R\mathbb Z).
}
\]

So a new prime-power depth does not create one isolated mode.

It creates the new \(p^k\)-innovation tensored with **every pre-existing coprime harmonic mode**.

That is exactly a new support face.

---

# 4. Dimension identity

The innovation space has dimension

\[
\dim\Delta_N
=
L_+-L_-
=
(p-1)L_-.
\]

From the conductor decomposition,

\[
\sum_{e\mid R}
\varphi(p^ke)
=
\varphi(p^k)
\sum_{e\mid R}\varphi(e).
\]

Using

\[
\sum_{e\mid R}\varphi(e)=R
\]

and

\[
\varphi(p^k)=p^{k-1}(p-1),
\]

we obtain

\[
\boxed{
\sum_{e\mid R}
\dim W_{p^ke}
=
p^{k-1}(p-1)R
=
(p-1)L_-.
}
\]

So the face decomposition is dimension-exact.

---

# 5. The visible sector is only one slice of the new face

The only newly born conductor whose numerical value is exactly the support stage \(N=p^k\) is

\[
W_N=W_{p^k}
\]

corresponding to

\[
e=1.
\]

Every other new sector has

\[
d=p^ke>N.
\]

Therefore all

\[
e>1
\]

are **shadow-supported conductors** at birth.

The visible fraction of the new harmonic dimension is

\[
\frac{\dim W_{p^k}}
{\dim\Delta_{p^k}}
=
\frac{
\varphi(p^k)
}{
\varphi(p^k)R
}
=
\boxed{
\frac1R.
}
\]

The shadow fraction is

\[
\boxed{
1-\frac1R.
}
\]

For large clocks almost all newly created harmonic degrees of freedom are shadow sectors.

---

# 6. Examples

## \(N=2\)

\[
L_-=1,\qquad R=1.
\]

So

\[
\Delta_2=W_2.
\]

The first support birth is entirely visible.

## \(N=3\)

\[
L_-=2,
\qquad
R=2.
\]

Hence

\[
\boxed{
\Delta_3
=
W_3\oplus W_6.
}
\]

The visible prime sector \(W_3\) and the mixed shadow conductor \(W_6\) are born simultaneously.

The ordinary SUCC backbone has reached only \(3\), but the harmonic support for conductor \(6\) already exists.

## \(N=8\)

\[
L_-=L_7=420=2^2\cdot105.
\]

Thus

\[
R=105.
\]

The new face is

\[
\boxed{
\Delta_8
=
\bigoplus_{e\mid105}W_{8e}.
}
\]

Explicitly:

\[
W_8,\;
W_{24},\;
W_{40},\;
W_{56},\;
W_{120},\;
W_{168},\;
W_{280},\;
W_{840}.
\]

Its dimension is

\[
840-420=420.
\]

The visible piece has

\[
\dim W_8=\varphi(8)=4.
\]

So only

\[
\boxed{
\frac4{420}
=
\frac1{105}
}
\]

of the new harmonic dimension is the visible conductor \(8\).

The remaining

\[
\boxed{
\frac{104}{105}
}
\]

is shadow support.

The user's central-holonomy conductor

\[
24=8\cdot3
\]

is one of these shadow sectors.

So \(W_{24}\) is born harmonically at support stage \(8\), before ordinary SUCC reaches \(24\).

---

# 7. Support birth map partitions the entire conductor spectrum

Define

\[
\boxed{
\beta(d)
=
\min\{N:d\mid L_N\}
=
\max_{p^j\parallel d}p^j.
}
\]

Then an exact conductor sector \(W_d\) first appears precisely in

\[
\boxed{
\Delta_{\beta(d)}.
}
\]

Therefore

\[
\boxed{
\Delta_N
=
\bigoplus_{\beta(d)=N}W_d.
}
\]

The possible birth stages \(N>1\) are exactly prime powers.

So the LCM martingale filtration partitions the complete conductor spectrum according to its **largest prime-power atom**.

This is the harmonic version of the support box.

---

# 8. Martingale/wavelet formulation

On

\[
L^2(\widehat{\mathbb Z}),
\]

let

\[
E_N
\]

be conditional expectation onto functions measurable modulo \(L_N\).

Then

\[
E_N
\]

is the orthogonal projection onto

\[
L^2(\mathbb Z/L_N\mathbb Z).
\]

Define

\[
\boxed{
D_N=E_N-E_{N-1}.
}
\]

Then

\[
D_N=0
\]

unless \(N\) is a prime power.

At

\[
N=p^k,
\]

\[
\operatorname{Ran}D_N=\Delta_N.
\]

Hence

\[
\boxed{
L^2(\widehat{\mathbb Z})
=
W_1
\oplus
\bigoplus_{p^k}
\Delta_{p^k}
}
\]

orthogonally.

Equivalently,

\[
\boxed{
L^2(\widehat{\mathbb Z})
=
W_1
\oplus
\bigoplus_{p^k}
\bigoplus_{\beta(d)=p^k}
W_d.
}
\]

This is an LCM-adapted arithmetic wavelet decomposition.

---

# 9. Single-cylinder innovation spectrum

Let

\[
M'=bM
\]

with \(M\mid M'\).

Choose one child residue cylinder

\[
C_1
\]

modulo \(M'\) inside a parent cylinder

\[
C_0
\]

modulo \(M\).

Define the centered support innovation

\[
\boxed{
\eta
=
1_{C_1}
-
\frac1b1_{C_0}.
}
\]

On

\[
\mathbb Z/M'\mathbb Z,
\]

its Fourier coefficient at character \(k\) is:

\[
\boxed{
\widehat\eta(k)
=
0
\quad
\text{if the character factors through }M,
}
\]

and otherwise

\[
\boxed{
|\widehat\eta(k)|=\frac1{M'}.
}
\]

Therefore the innovation is spectrally flat over exactly the newly born character set.

Projecting to exact conductor \(d\),

\[
\boxed{
\|P_d\eta\|_2^2
=
\frac{\varphi(d)}{M'^2}
}
\]

for

\[
d\mid M',
\qquad
d\nmid M,
\]

and zero otherwise.

Its total norm is

\[
\boxed{
\|\eta\|_2^2
=
\frac{M'-M}{M'^2}
=
\frac{b-1}{bM'}.
}
\]

Thus a support refinement is literally a finite arithmetic Haar wavelet whose energy is distributed by exact-conductor multiplicities.

---

# 10. At an LCM birth the wavelet fills the whole new face

For

\[
N=p^k,
\]

\[
M=L_-,
\qquad
M'=L_+=pL_-.
\]

A child-cylinder innovation therefore has nonzero spectrum exactly on

\[
\boxed{
\{W_d:\beta(d)=N\}.
}
\]

Each newly born character receives the same Fourier amplitude magnitude.

The exact-conductor energies are

\[
\boxed{
\|P_{p^ke}\eta\|_2^2
=
\frac{
\varphi(p^ke)
}{
L_N^2
},
\qquad
e\mid R.
}
\]

So the chronological support filtration already produces a canonical conductor-resolved distribution on the full visible-plus-shadow face.

No zeta zeros enter.

---

# 11. Three different birth/actualization scales for one loop

For a closed rational-affine word \(\gamma\), we now have at least three distinct arithmetic scales.

### phase-support scale

\[
\boxed{
M_\gamma
}
\]

from the congruence cylinder on which every prefix is integral.

### central-holonomy harmonic birth

If the primitive affine lift closes with

\[
\kappa(\gamma)I,
\]

then

\[
\boxed{
\beta(\kappa(\gamma))
}
\]

is the first LCM stage containing \(W_{\kappa(\gamma)}\).

### visible SUCC actualization

The ordinary integer

\[
\boxed{
\kappa(\gamma)
}
\]

appears only when the backbone reaches that value.

For the user's loop:

\[
M_\gamma=2,
\]

\[
\kappa(\gamma)=24,
\]

\[
\beta(24)=8.
\]

Thus:

\[
\boxed{
2
\quad\to\quad
8
\quad\to\quad
24
}
\]

are three genuinely different stages:

1. the word becomes arithmetically executable;
2. its full central-holonomy harmonic sector becomes supportable;
3. the corresponding conductor value becomes visibly actualized.

This resolves an ambiguity in the original shadow-support intuition.

---

# 12. One support face already contains the future Suzuki jet hierarchy

At

\[
N=p^k,
\]

every new conductor is

\[
d=Ne,
\qquad
e\mid R.
\]

Its Suzuki interaction order is

\[
\boxed{
r(d)
=
\#\{q:q\mid d\}
=
1+\#\{q:q\mid e\}.
}
\]

Therefore the new face has an intrinsic grading

\[
\boxed{
\Delta_N
=
\bigoplus_{r\ge1}\Delta_N^{(r)},
}
\]

where

\[
\boxed{
\Delta_N^{(r)}
=
\bigoplus_{\substack{e\mid R\\\omega_0(e)=r-1}}
W_{Ne}.
}
\]

The grade \(r=1\) piece is only

\[
W_N.
\]

This is the von-Mangoldt/first-jet support-growth event.

Grades \(r\ge2\) are mixed-prime shadow sectors already present in the support face but whose direct Suzuki weights begin only at higher powers of the deformation parameter.

Thus one LCM support birth contains an entire future interaction hierarchy.

---

# 13. Exact relation to the user's “pre-actualized family” intuition

At support stage \(N\), the LCM clock contains every sector

\[
W_d
\quad
\text{with}
\quad
\beta(d)\le N.
\]

The actual Suzuki causal kernel at horizon \(N\) uses only conductors

\[
d\le N.
\]

Therefore the difference

\[
\boxed{
\mathcal S_N
=
\bigoplus_{\substack{d\mid L_N\\d>N}}W_d
}
\]

is the **shadow-supported harmonic sector**.

It is finite.

It is canonical.

And it is forced by the minimal support clock rather than introduced by hand.

The physical/actualized part is

\[
\boxed{
\mathcal A_N
=
\bigoplus_{d\le N}W_d.
}
\]

So the full support clock splits as

\[
\boxed{
L^2(\mathbb Z/L_N\mathbb Z)
=
\mathcal A_N
\oplus
\mathcal S_N.
}
\]

This is the concrete finite parent space on which a shadow-elimination/Schur-complement construction can now be tested.

---

# 14. Important no-go and the remaining opportunity

The final cyclic successor on

\[
\mathbb Z/L_N\mathbb Z
\]

is Fourier diagonal.

Therefore it preserves each \(W_d\) and does **not** couple

\[
\mathcal A_N
\]

to

\[
\mathcal S_N.
\]

So simply embedding active conductors into the larger support clock does nothing.

The only possible proof-bearing mechanism must retain chronology **before** that final diagonal quotient.

The rank-one carry recursion at each LCM birth does exactly that:

\[
\boxed{
C_{pL}
=
C_L\otimes I_p
+
|0\rangle\langle L-1|
\otimes(C_p-I_p).
}
\]

Thus the next object is not the final clock.

It is the ordered chain of support-face births together with their carry-boundary couplings.

The shadow-support program survives the obvious flatness no-go only in this history-retaining form.

---

# 15. Current theorem-level picture

\[
\boxed{
\text{prime-power LCM event}
}
\]

creates

\[
\boxed{
\text{one entire mixed-conductor support face}.
}
\]

Within that face:

\[
\boxed{
\text{visible }W_N
=
\text{first Suzuki jet},
}
\]

while

\[
\boxed{
\text{shadow }W_{Ne},\ e>1
=
\text{higher interaction grades already supportable}.
}
\]

The full finite support clock therefore knows far more harmonic structure than the causal Suzuki kernel has yet actualized.

The open question is whether chronological elimination of that latent structure produces the exact global completion term required for finite Suzuki/Weil positivity.
