# Prime scattering as a Blaschke/Weyl channel

**Date:** 2026-10-06  
**Status:** exact local identity; global infinite product still obstructed. **RH remains open.**

The local prime scattering factor found in earlier rounds is, after stripping one bare carrier phase, an elementary Blaschke factor.

Its phase derivative is exactly the \(p\)-adic Poisson/Weyl density.

---

## 1. Critical Weyl coordinate

Let

\[
s=\frac12-iz,
\qquad
\ell=\log p,
\qquad
r=p^{-1/2},
\]

and define

\[
\boxed{
w=e^{i\ell z}.
}
\]

For \(z\in\mathbb C_+\),

\[
|w|=e^{-\ell\Im z}<1.
\]

The local Euler variables are

\[
p^{-s}=rw,
\qquad
p^{-(1-s)}=rw^{-1}.
\]

---

## 2. Local functional-equation scattering factor

Define

\[
\rho_p(s)
=
\frac{L_p(s)}
{L_p(1-s)}.
\]

Since

\[
L_p(s)=\frac1{1-p^{-s}},
\]

\[
\rho_p(s)
=
\frac{
1-p^{-(1-s)}
}{
1-p^{-s}
}.
\]

At \(s=1/2-iz\),

\[
\boxed{
\rho_p
=
\frac{
1-rw^{-1}
}{
1-rw
}.
}
\]

Multiply by the bare carrier \(w\):

\[
\boxed{
\widetilde\rho_p(z)
:=
w\rho_p
=
\frac{
w-r
}{
1-rw
}.
}
\]

---

## 3. This is an elementary Blaschke factor

Define

\[
b_r(w)
=
\frac{w-r}{1-rw},
\qquad
0<r<1.
\]

Then

\[
\boxed{
\widetilde\rho_p(z)
=
b_r(e^{i\ell z}).
}
\]

Since \(w=e^{i\ell z}\) maps the upper half-plane to the disk and \(b_r\) is a disk automorphism,

\[
\boxed{
|\widetilde\rho_p(z)|<1
\qquad
(\Im z>0),
}
\]

and for real \(t\),

\[
\boxed{
|\widetilde\rho_p(t)|=1.
}
\]

So the normalized prime scattering channel is an inner/Schur function.

---

## 4. Phase velocity = Poisson kernel

On the unit circle,

\[
w=e^{i\theta}.
\]

For the Blaschke factor,

\[
\boxed{
\frac{d}{d\theta}
\arg b_r(e^{i\theta})
=
\frac{
1-r^2
}{
1-2r\cos\theta+r^2
}
=
P_r(\theta).
}
\]

Therefore, with

\[
\theta=t\log p,
\]

\[
\boxed{
\frac{d}{dt}
\arg\widetilde\rho_p(t)
=
(\log p)
P_r(t\log p).
}
\]

But \(P_r\) is exactly the spectral density obtained from the normalized \(p\)-adic ball Gram

\[
r^{|j-k|}.
\]

Hence:

\[
\boxed{
\text{p-adic overlap spectrum}
=
\text{phase velocity of normalized prime scattering}.
}
\]

---

## 5. Relation to the local Weyl response

The local Carathéodory function is

\[
F_p(z)
=
\frac{
1+rw
}{
1-rw
}.
\]

Its boundary real part is

\[
\Re F_p(t)
=
P_r(t\log p).
\]

Therefore

\[
\boxed{
\frac{d}{dt}
\arg\widetilde\rho_p(t)
=
(\log p)\Re F_p(t).
}
\]

This is a standard scattering/Weyl relation in exact arithmetic form:

\[
\boxed{
\text{phase shift derivative}
=
\text{local density of states}.
}
\]

---

## 6. Relation to the carry repair

The positive local repair was

\[
D_p(\theta)
=
\log p\,
\frac{r}{(1-r)^2}
(1-\cos\theta)
P_r(\theta).
\]

Thus

\[
\boxed{
D_p
=
\frac{r}{(1-r)^2}
(1-\cos\theta)
\frac{d}{dt}
\arg\widetilde\rho_p(t)
}
\]

with \(\theta=t\log p\), up to the obvious variable conversion.

So the carry/high-pass factor weights the local scattering density of states.

---

## 7. Local zeros sit on the half-shift line

The normalized prime Blaschke factor vanishes when

\[
w=r.
\]

Thus

\[
e^{i\ell z}=e^{-\ell/2}.
\]

Hence

\[
\boxed{
z
=
\frac{2\pi n}{\log p}
+
\frac{i}{2},
\qquad
n\in\mathbb Z.
}
\]

So each local prime scattering channel has its Blaschke zero lattice exactly on the line

\[
\Im z=\frac12.
\]

This is another appearance of the critical half-shift.

These are local scattering zeros, not zeta zeros.

They must not be confused with the nontrivial global spectrum.

---

## 8. Global product no-go

For a finite prime set,

\[
\prod_{p\le P}\widetilde\rho_p(z)
\]

is inner.

But the union of all local Blaschke zero lattices does not satisfy the global upper-half-plane Blaschke condition.

Even for one zero string per prime, the total zero density is too large; summing over all primes diverges strongly.

Therefore the naive infinite product of the local normalized prime scattering factors does not define an ordinary bounded inner function.

Again, finite local passivity does not automatically survive the infinite assembly.

This is the scattering version of the global divergence wall.

---

## 9. Functional-equation interpretation

Formally,

\[
\prod_p\rho_p(s)
=
\frac{\zeta(s)}{\zeta(1-s)}
\]

in a region where both sides make appropriate sense through finite products/continuation.

The completed functional equation says the global prime scattering is canceled/renormalized by the Archimedean factor.

So the Gamma/trivial sector is the global counter-channel required to complete the divergent prime scattering phase.

This must happen before a global inner/Weyl statement can be made.

---

## 10. House slogan

\[
\boxed{
\text{A prime is a Blaschke scattering channel wrapped around a FUCC clock.}
}
\]

\[
\boxed{
\text{Its phase velocity is the p-adic Poisson/Weyl density.}
}
\]

\[
\boxed{
\text{Carry is the high-pass weighting of that density.}
}
\]

\[
\boxed{
\text{The infinite product is where the real RH difficulty begins.}
}
\]
