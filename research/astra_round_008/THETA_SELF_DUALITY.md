# Residue theta, balanced mesh, and what self-duality actually buys

Status: exact classical Poisson identities and repository-level refinements
proved below. The new audit results exclude a naive refinement diagram and
identify a genuine way to avoid fixed-log sampling loss. They do not prove RH.

## 1. A matrix/continuum coupling before scalarization

Use the real transform `fhat(y)=integral f(x) exp(-2 pi i xy) dx` on
Schwartz functions. For h>0 define

    P_(L,h) f(a) = sum_{k in Z} f(h(a+kL)).

All sums converge absolutely. Poisson summation applied to the modulated
function on the mesh h gives

    F_L P_(L,h) f = [1/(h sqrt(L))] P_(L,1/(Lh)) fhat.        (T1)

For example, the b coordinate follows by summing
`f(hn) exp(-2 pi i nb/L)` over n. Thus a transform with the **same mesh on
both sides** forces h=1/sqrt(L). Writing P_L for this balanced choice,

    F_L P_L f = P_L fhat.                                    (T2)

This is an exact coupling of a finite vector to a retained real Schwartz
test. No prime factorization or determinant was used. The finite/real
diagonal comb is the coupling; a bare tensor product of two transforms
would not supply the sampling relation.

The square-root scale is forced by dual lattice spacing once real Lebesgue
measure, the Fourier convention, and L residue classes are chosen. It is
**not** yet a derivation of Lambda(n)/sqrt(n) in the Suzuki form: no prime
charge occurs in (T1), and the lattice index L is not a prime-power event n.

## 2. Exact vector theta identity

Set

    Theta_(L,a)(t) = sum_{n=a mod L} exp(-pi t n²/L),  t>0.

The Gaussian transform and (T2) give

    F_L Theta_L(t) = t^(-1/2) Theta_L(1/t),
    Theta_L(t) = t^(-1/2) F_L Theta_L(1/t).                   (T3)

The second equality uses the evenness under a -> -a. At L=1 this is precisely
the classical theta transformation, not a new continuation mechanism.
Every residue, including all mixed-conductor harmonic content, is retained.

For log time t=exp(u), define `B_L(u)=exp(u/4) Theta_L(exp(u))`.
Then `F_L B_L(u)=B_L(-u)`. The exponent 1/4 is half of the theta weight 1/2;
it is the symmetric distribution of that weight between the reflected sides.
This reflection identity is not positivity of a Suzuki screw kernel.

## 3. Refinement requires the real dilation as well

For M=rL, splitting and rescaling the defining integer sums proves

    Theta_(L,a)(t) = sum_{j=0}^{r-1} Theta_(M,a+jL)(r t),
    Theta_(L,a)(t) = Theta_(M,ra)(t/r).                       (T4)

Thus increasing the conductor changes the balanced real geometry. At fixed
t the theta vector is not simply the canonical pullback of its old value.
These formulas, together with `F_M I=J F_L`, are the corrected finite causal
diagram. Omitting either reciprocal real dilation fails on the explicit
6|30 interval holdout.

For a unitary real dilation `D_c f(x)=sqrt(c) f(cx)`, put
`W_L=L^(1/4) P_L`. The general forms of (T4) are

    W_L = sqrt(r) I_LM^* W_M D_(sqrt(r)),
    W_L = sqrt(r) J_LM^* W_M D_(1/sqrt(r)).                   (T5)

No equality `W_M=I_LM W_L` is asserted. Both adjoints and their normalization
are specified in `FINITE_ADELIC_POISSON.md`.

## 4. A precise escape from the Round007 fixed-observation obstruction

For every Schwartz f,

    ||W_L f||²_(H_L) -> ||f||²_(L²(R))  as L -> infinity.     (T6)

This is an asymptotic isometry on this dense test class, not a bounded
sampling operator on all L². At any fixed L, evaluation at a grid point is
unbounded in L² (concentrate a smooth bump at that point), so such a stronger
claim would be false.

Proof of (T6): put h=1/sqrt(L). Expanding the finite norm before squaring
away the residue structure gives

    ||W_L f||² = h sum_{n,k in Z} f(nh) conjugate(f(nh+k/h)).  (T7)

For k=0 this is the Riemann sum for the Schwartz function |f|². For k!=0,
Schwartz decay and `max(|x|,|x+k/h|)>=|k|/(2h)` imply, for every q>1,

    h sum_n |f(nh) f(nh+k/h)| <= C_q (1+|k|/h)^(-q).

One obtains the bound by assigning half of a decay bound of exponent 2q to
the large factor, then summing the other factor; the shifted lattice sums
`h sum_n (1+|nh+c|)^(-q)` are uniformly bounded for 0<h<=1 and all c.
Summing k!=0 gives O(h^q). This proves (T6). Polarization gives the analogous
bilinear limit. Equation (T2) also gives `F_L W_L=W_L Fourier` exactly.

Unlike observations at log n, these meshes become dense inside every fixed
real interval. For a compactly supported nonzero smooth function, the
period sqrt(L) eventually exceeds its support width, so periodization cannot
cancel its nearby dense samples. There is no common invisible smooth space.
This is a genuine escape from **that hypothesis** of R007 C121. It still
does not identify a map from the logarithmic Weil test space with a positive
completed energy. The unmodified limiting energy here is ordinary L²,
as (T6) proves. A further operator carrying the exact arithmetic correlations
and Archimedean completion remains necessary.

## 5. Mellin transform: Gamma and functional equation before Euler products

Let e0 be the residue delta at 0 and v=F_L e0=L^(-1/2)1. For Re(s)>1 define

    Z_L(s) = integral_0^infinity [Theta_L(t)-e0] t^(s/2-1) dt.

Termwise integration, justified by absolute convergence, gives each component

    Z_(L,a)(s) = pi^(-s/2) Gamma(s/2) L^(s/2)
                  * sum_{n!=0, n=a mod L} |n|^(-s).         (T8)

This keeps the residue vector until after the Gamma integral. To continue,
let `I_L(s)=integral_1^infinity [Theta_L(t)-e0]t^(s/2-1)dt`, an entire vector
because its entries decay exponentially. Splitting at 1 and using (T3) gives

    Z_L(s) = I_L(s) + F_L I_L(1-s)
               + 2v/(s-1) - 2e0/s,
    Z_L(s) = F_L Z_L(1-s).                                 (T9)

This is a complete proof of the meromorphic vector continuation, with both
pole vectors explicit, and no assumption of a functional equation. The
second identity uses `F_L² I_L=I_L`, `F_L e0=v`, and `F_L v=e0`.

Only now sum residues: writing `Zeta_completed(s)=pi^(-s/2)Gamma(s/2)zeta(s)`,

    sum_a Z_(L,a)(s) = 2 L^(s/2) Zeta_completed(s),
    Z_(L,0)(s) = 2 L^(-s/2) Zeta_completed(s).

The vector equation pairs these two scalar observations and recovers the
usual completed functional equation. This is **classical theta/Tate
mathematics already true at L=1**, not an improvement toward RH because the
LCM system is causal. All higher L versions still include an infinite real
Gaussian periodization over all integers, rather than only integers <=N.
Finite residue dimension must not be misreported as a finite arithmetic
cutoff.

## 6. What the construction does and does not force

| Statement | Verdict and reason |
|---|---|
| Finite DFT plus real Gaussian admits exact matrix self-duality | Proved, (T1)–(T3) |
| The LCM pullback system itself is Fourier self-compatible | Refuted, (P2) |
| Deleting mixed conductors preserves the Fourier coupling | Refuted for every proper harmonic union, section 3 of companion note |
| Balanced meshes retain continuum information asymptotically | Proved on Schwartz tests, (T6) |
| Vector Mellin completion gives the functional equation | Proved by (T8)–(T9), classical |
| The construction singles out primes or von Mangoldt charge | False as stated: it exists for every integer L and arbitrary cofinal schedules |
| The resulting norm is the completed Weil form | Not obtained; the plain norm converges to L² |
| Self-duality implies Weil positivity | No such implication proved; existing R007 controls remain active |

The next discriminating calculation must change the operator, not merely
increase L: retain this continuum lift and compute whether a prescribed
prime-sensitive coupling produces the **exact** R007 Weil pairing, including
its negative identity residual. The theta relation alone cannot supply it.

## 7. Primary-source scope and reproducibility

The lattice Poisson statement for Schwartz functions is rederived in (T1).
Lior Silberman's authored [Fourier/Poisson lecture notes, §3, Exercise 13]
(https://personal.math.ubc.ca/~lior/teaching/1011/613D_F10/Fourier%2BPoissonSum.pdf)
give the lattice/covolume normalization. NIST [DLMF 20.7.32]
(https://dlmf.nist.gov/20.7.E32), specialized to z=0 and tau=it, corroborates
the L=1 transformation. Weil's original 1966 paper cited in the companion
note supplies the adelic distribution context. None asserts the new desired
positive Weil-square factorization. Source metadata and exact scope are in
`reviews/poisson_sources.json`.

Run `python -m unittest tests.test_round008_poisson -v` and
`python -m scripts.round008_poisson`. The latter gives exact finite-algebra
checks and Arb enclosures with a proved geometric Gaussian tail. Positive
finite controls are not used to prove any limit or RH claim.

The non-even holdout is
`f(x)=exp(-pi*(3/2)*(x-1/3)^2) exp(2 pi i*(2/5)*x)` at L=6.
Its exact transform is used separately from theta inversion. Reversing only
the finite Fourier sign produces certified nonzero discrepancies. This
control is necessary: an even theta vector cannot distinguish F_L from
F_L^*. The evidence retains both the correct and deliberately mismatched
phase conventions.
