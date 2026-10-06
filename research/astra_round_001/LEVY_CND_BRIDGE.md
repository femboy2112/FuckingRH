# Exact screw / negative-type / Lévy bridge

Status: sign and hypothesis normalization, with elementary proofs of the
functional-analytic arrows. RH is not proved. All occurrences of `CND` below
mean **conditionally negative definite**, with the inequality specified below.

## 1. Primary-source audit

Sources inspected on 2026-10-05:

- [Suzuki, arXiv:2206.03682v4](https://arxiv.org/html/2206.03682v4):
  equations (1.1), (1.4), (1.8), Theorems 1.2 and 1.7.
- [Nakamura–Suzuki, arXiv:2306.08317v1](https://arxiv.org/html/2306.08317v1):
  equations (1.2)–(1.7), Theorems 1.1–1.2, and their proofs.

The first defines the explicit even function `Psi`, sets `g=-Psi`, and
identifies RH with the global screw-kernel condition and with scalar
nonnegativity. The second uses its equation (1.5) for `g_zeta`: comparison
term by term gives **exactly `g_zeta=-Psi`**, including the constant
`Phi(1,2,1/4)`, the Gamma linear term, and the even extension. Its main
theorem identifies RH with infinite divisibility of `exp(-Psi)`.
Under RH its Theorem 1.2 gives a compound Poisson law, with zero Gaussian
coefficient and zero drift. There is no missing factor two in this comparison.

The arXiv landing pages label these versions May 2023 and June 2023;
the experimental HTML also displays an inconsistent generated “Version of
August 24, 2026” line. The equations and theorem numbers above, rather than
that display date, identify the statements used here.

## 2. Kernel, CND, and Hilbert normalization

Let `psi:R→R` be continuous, even, and `psi(0)=0`. Define

\[
 K_\psi(t,u)=\psi(t)+\psi(u)-\psi(t-u).
\]

For Suzuki's function, substituting `g=-Psi` into Kreĭn's definition gives
`G_g=K_Psi`. “Global PSD” means PSD on **every finite set of real times**;
a kernel known positive only on `(-a,a)` is insufficient.

Our CND convention is

\[
 \sum_{i,j}c_i\overline{c_j}\psi(t_i-t_j)\le0
 \quad\text{whenever }\sum_i c_i=0.
\]

**Elementary equivalence.** `K_psi` is PSD iff `psi` is CND.
For the forward direction, the terms `psi(t_i)+psi(t_j)` vanish in a
zero-sum quadratic form, so that the CND form is the negative of the
kernel form. For the reverse direction, append the point `0` with
coefficient `-sum_i c_i`; direct expansion of the CND form gives the
negative of `sum_ij c_i conj(c_j)K_psi(t_i,t_j)`.

If this condition holds, form the real vector space of formal finite sums
of symbols `e_t`, give it the bilinear form
`<e_t,e_u>=K_psi(t,u)`, quotient by its nullspace, and complete. The images
`V(t)` satisfy

\[
 V(0)=0,\qquad \langle V(t),V(u)\rangle=K_\psi(t,u),
\]
\[
 \|V(t)\|^2=2\psi(t),\qquad
 \|V(t)-V(u)\|^2=2\psi(t-u).
\]

This quotient construction is a **consequence** of positivity, not an
independent arithmetic proof of it. A proposed noncircular construction
must establish these identities in a separately positive Hilbert space.

The scalar identity `psi(t)=||V(t)-V(0)||^2/2` alone proves
nonnegativity, but does not imply that the same `V` has kernel `K_psi`:
the stationary-distance identity must also hold. For Suzuki's exact
function scalar nonnegativity happens to suffice by his special theorem.

## 3. Schoenberg and infinite divisibility, with signs fixed

For these hypotheses the following are equivalent:

1. `psi` is CND.
2. `exp(-r psi)` is positive definite for every `r>=0`.
3. `exp(-psi)` is the characteristic function of an infinitely divisible
   probability measure on `R`.

Here is the finite-matrix part of the argument. Using the real Hilbert map,

\[
 e^{-r\psi(t-u)}
 =e^{-r\|V(t)\|^2/2}e^{-r\|V(u)\|^2/2}
   e^{r\langle V(t),V(u)\rangle}.
\]

The last kernel is PSD by its power series and the Schur product theorem.
Diagonal multiplication preserves PSD. Conversely, expand the
positive-definite quadratic form at `r=0` with zero-sum coefficients;
the first nonzero coefficient is the negative CND form. Continuity and
value one at zero permit Bochner's theorem; the functions for `r=1/n`
are characteristic functions of convolution roots.

Conversely, if `phi_n^n=exp(-psi)` for a continuous normalized characteristic
function `phi_n`, then `phi_n exp(psi/n)` is a continuous map from `R` to
the finite set of `n`th roots of unity and equals one at zero. It is
identically one. Thus `exp(-psi/n)` is positive definite; products and
pointwise limits give the same property for all `r>=0`.

Accordingly `Psi` is of **negative type**, while `g=-Psi` has the opposite
conditional sign. Neither “`Psi` is positive definite” nor “`g` is CND”
is the desired assertion.

## 4. Lévy–Khintchine convention

Write the characteristic exponent in the convention used by
Nakamura–Suzuki:

\[
 g(t)=-\frac a2t^2+ibt+
 \int_{\mathbb R}\left(e^{itx}-1-\frac{itx}{1+x^2}\right)\nu(dx),
\]

where `a>=0`, `nu>=0`, `nu({0})=0`, and
`integral min(1,x^2)nu(dx)<infinity`. For a real even exponent, uniqueness
gives a symmetric Lévy measure and zero drift in this symmetric truncation.
Thus

\[
 \psi(t)=\frac a2t^2+\int_{\mathbb R}(1-\cos(tx))\nu(dx).
\]

When RH is assumed, the primary-source calibration is

\[
 a=0,\qquad
 \nu_\zeta=\sum_\gamma\frac{m_\gamma}{\gamma^2}\delta_{-\gamma},
 \qquad \nu_\zeta(\mathbb R)<\infty.
\]

The sum here is over **distinct** real zeros of `xi(1/2-iz)` and includes
both signs; `m_gamma` supplies multiplicity. Equivalently sum over zeros
counting multiplicity and omit `m_gamma`. There is no zero at `gamma=0`.
This representation is used only as a conditional control and for the
mutation obstruction below, never to construct the sought arithmetic proof.

The Lévy variable `x` is Fourier-dual to `t`. The prime measure
`mu=sum_q Lambda(q)/sqrt(q) delta_log(q)` lives in the **event-time**
coordinate. It is not `nu_zeta`. Changing the name of its integration
variable does not transport positivity through Fourier inversion.

## 5. Valid closure and invalid Gaussian residual inference

Suppose continuous even CND functions `psi_X`, normalized at zero,
converge pointwise to a continuous function `psi`. Every finite CND
quadratic form passes to the limit, so `psi` is CND. This is already a
sufficient closure topology; compact-uniform convergence is stronger.
For nonsymmetric complex exponents, the Hermitian version and consistent
continuous logarithms are required.

**What must actually be proved:** positivity of each approximating Lévy
measure or Gram kernel, convergence to the complete explicit `Psi`, and
continuity of the limit at zero. Neither a fitted residual nor convergence
after discarding a Gaussian term supplies this.

A residual obtained by dividing out a Gaussian need not be a
characteristic function. An exact control is

\[
 \psi_0(t)=1-\cos t,\qquad
 \psi_{\rm residual}(t)=1-\cos t-\frac12t^2.
\]

The first is a symmetric compound Poisson exponent of negative type.
At `t=2pi` the residual is `-2pi^2`, so its exponential with a minus sign
has modulus larger than one. Even removing the correct quadratic Taylor
term destroys characteristic-function positivity. Mod-Gaussian
convergence therefore provides no Lévy closure by itself.

## 6. Exact endpoint and remaining burden

For the specific arithmetic function in `NORMALIZED_PROOF_TARGET.md`,

\[
 \mathrm{RH}
 \Longleftrightarrow \Psi\ge0
 \Longleftrightarrow K_\Psi\succeq0
 \Longleftrightarrow \Psi\text{ CND}
 \Longleftrightarrow e^{-r\Psi}\text{ PD for all }r\ge0
 \Longleftrightarrow e^{-\Psi}\text{ infinitely divisible characteristic}.
\]

The first two arithmetic arrows are Suzuki's theorems. Their extension
to arbitrary nonnegative functions is false. The intermediate arrows
were proved above under their stated hypotheses. The final RH endpoint
also appears directly in Nakamura–Suzuki. These are coordinate changes
of one unresolved positivity obligation.

For this exact `Psi`, even the weaker assertion that `exp(-Psi)` is an
**ordinary characteristic function** would suffice: every characteristic
function has modulus at most one, and `exp(-Psi)` is positive real, so
`Psi>=0`. Suzuki then gives RH, and Nakamura–Suzuki gives infinite
divisibility afterward. Thus an independently constructed arithmetic
probability law with this characteristic function would finish the proof
without first constructing positive Lévy approximants. This observation
does not itself produce that law. In particular, the finite-cutoff CND
no-go below does not prove that every `exp(-Psi_X)` fails ordinary
positive definiteness; those are different claims.

The arithmetic no-go results, including a finite-event rigidity theorem,
are proved in `GRAM_LEVY_ATTEMPT.md`. They eliminate specific attempted
constructions; they do not establish global PSD or RH.
