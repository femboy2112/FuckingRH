# Hostile control: naive cubical shorting creates forbidden mixed-composite atoms

**Date:** 2026-10-07  
**Branch:** \`aletheia/cubical-gamma-rh-proof-attempt-2026-10-07\`  
**Status:** exact support restriction + numerical two-torus coefficient diagnostic. The qualitative obstruction is decisive once a nonzero mixed Fourier coefficient is certified; the current coefficient should be enclosed rigorously before promotion to a formal theorem.  
**RH remains open.**

The prime-support superconnection produced a positive finite parent and nontrivial Schur renormalization.

However, a physical Weil pushforward has a stricter support law:

\[
\boxed{
\text{its atomic arithmetic translations occur only at }\pm\log(p^k).
}
\]

Mixed composites such as

\[
pq,\qquad p\ne q
\]

have

\[
\Lambda(pq)=0.
\]

Therefore any physical delta atom at

\[
\log(pq)
\]

is forbidden.

This note tests the naive product-locked continuum version of the cubical superconnection and finds precisely such an atom already in the \(2,3\) model.

---

# 1. Exact target support

The Weil prime term is

\[
-2
\sum_{q=p^k}
\frac{\Lambda(q)}{\sqrt q}
\Re\langle\tau_{\log q}f,f\rangle.
\]

Hence the discrete translation support is

\[
\boxed{
\{\pm\log(p^k)\}.
}
\]

There is no atom at

\[
\log6,
\]

or more generally at

\[
\log(p^kq^\ell),
\qquad
p\ne q.
\]

The Archimedean Gamma contribution is represented by a continuous/smooth kernel away from the origin, and the pole sector is finite-rank/smooth in the translation variable.

Thus an isolated mixed-composite delta line cannot be canceled by completion.

---

# 2. Two-prime cubical shorting with independent phases

Use normalized \(2\)- and \(3\)-wakes on the common \(6\)-clock.

Let

\[
z_2=e^{-i\theta_2}-1,
\qquad
z_3=e^{-i\theta_3}-1.
\]

The continuum Fourier variable restricts to the one-dimensional dense orbit

\[
\theta_2=\xi\log2,
\qquad
\theta_3=\xi\log3,
\]

but because

\[
\log2/\log3\notin\mathbb Q,
\]

the correct atomic-support diagnostic is the full torus

\[
(\theta_2,\theta_3)\in\mathbb T^2.
\]

For each support residue \(n\), set

\[
v_n=
(z_2\beta_2(n),z_3\beta_3(n)).
\]

The exact two-face shorted energy from the cubical Dirac theorem is

\[
\boxed{
h_n(\theta_2,\theta_3)
=
\frac{
|\langle v_n,v_{n+1}\rangle|^2
}{
\|v_{n+1}\|^2
}
}
\]

with the removable zero case defined continuously.

Average over the support clock:

\[
\boxed{
m_{\rm cub}(\theta_2,\theta_3)
=
\frac16
\sum_{n\bmod6}
h_n(\theta_2,\theta_3).
}
\]

---

# 3. Fourier modes have direct arithmetic meaning

Expand

\[
m_{\rm cub}
=
\sum_{k,\ell\in\mathbb Z}
c_{k,\ell}
e^{i(k\theta_2+\ell\theta_3)}.
\]

On the physical one-dimensional spectral orbit,

\[
e^{i(k\theta_2+\ell\theta_3)}
=
e^{i\xi(k\log2+\ell\log3)}
=
e^{i\xi\log(2^k3^\ell)}.
\]

Therefore:

\[
\boxed{
(k,\ell)=(1,0)
\leftrightarrow
\log2,
}
\]

\[
\boxed{
(k,\ell)=(0,1)
\leftrightarrow
\log3,
}
\]

\[
\boxed{
(k,\ell)=(1,1)
\leftrightarrow
\log6.
}
\]

A nonzero \(c_{1,1}\) is exactly a forbidden mixed-composite translation coefficient.

Similarly \(c_{1,-1}\) is the forbidden ratio atom \(\log(2/3)\).

---

# 4. Numerical hostile control

A \(256\times256\) torus quadrature/FFT gives

\[
\boxed{
c_{1,1}
\approx
-0.0483955411880,
}
\]

and

\[
\boxed{
c_{1,-1}
\approx
-0.0483955411880.
}
\]

Representative additional coefficients are

\[
c_{1,0}\approx-0.8831103380,
\]

\[
c_{0,1}\approx-0.3982109856,
\]

\[
c_{2,0}\approx0.0218056599,
\]

\[
c_{0,2}\approx0.0293281629.
\]

So the shorted symbol is not supported only on the permitted prime-power axes.

It contains mixed Fourier modes.

---

# 5. Consequence

If the nonzero coefficient is certified analytically or by interval quadrature, then the naive continuum attachment

\[
\text{higher support conductor }W_{pq}
\quad+\quad
\text{continuum displacement }\log(pq)
\]

cannot push forward to the exact Weil form.

Gamma cannot repair the isolated \(\log6\) atom.

Therefore:

\[
\boxed{
\text{higher support faces may exist internally but their mixed log-lengths must be invisible under the physical scalar pushforward.}
}
\]

This corrects the earlier overly permissive statement that integer-product translations were automatically allowed.

Only prime-power translations are allowed in the Weil arithmetic atom set.

---

# 6. Surviving architecture

The cube remains useful at the **support/fiber level**:

- exact-conductor fusion;
- curvature;
- positive Dirac/Hodge parent;
- hidden-face Schur geometry.

But the physical continuum observation map must obey a selection rule stronger than conductor fusion:

\[
\boxed{
\mathcal O_{\rm phys}(W_d)=0
\qquad
\text{for mixed }d\text{ in atomic translation channels}.
}
\]

Higher mixed conductors may renormalize:

- zero-displacement/diagonal terms;
- continuous Archimedean channels;
- boundary/pole data;

but they cannot survive as new scalar delta lines.

This is now a hard acceptance criterion.

---

# 7. Interpretation

The support cube and continuum loop-length spectrum are **not** the same grading.

The internal conductor multiplication

\[
W_p\cdot W_q\subset W_{pq}
\]

is valid.

But physical explicit-formula observation applies the von-Mangoldt projector

\[
\boxed{
Q_1:
d\mapsto
\begin{cases}
\log p,&d=p^k,\\
0,&\omega_0(d)\ne1.
\end{cases}
}
\]

after the internal geometry.

Thus mixed support faces are virtual/internal states.

The physical arithmetic translation channel observes only the one-support stratum.

This fits the omega-zero conductor-jet theorem:

\[
\Lambda
=
\text{first support jet}.
\]

The higher support hierarchy may renormalize that first jet, but must disappear from the final atomic support.

---

# 8. Next theorem target

Construct a completed cube/Gamma Dirac system with observation map

\[
\mathcal O:
\mathcal H_{\rm internal}
\to
\mathcal H_{\rm Weil}
\]

such that:

1. on one-support cells, \(\mathcal O\) yields the prime-power translations;
2. mixed-conductor atomic translations are annihilated exactly;
3. mixed faces can still alter the diagonal/Archimedean/pole sectors through hidden-state elimination;
4. the full pushforward equals Suzuki's finite Weil operator.

The observation map is now as important as the internal positive Hamiltonian.

A positive internal cube alone is not sufficient.
