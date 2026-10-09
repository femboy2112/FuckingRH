# Finite operational semantics of actualization: SUCC, shadow SUCC, FUCC, and probeability

**Date 2026-10-09. Parent main 8505467ea596b0636f73b655c521f50105d8b06e (Round 067). RH OPEN.**
**Research stage:** elementary but exact finite structure, source-sensitive examples, and a new clearly falsifiable *instrument design*. No RH theorem is claimed.

## 0. Which question is actually being asked?

**User's actual hypothesis, not ours:** SUCC / shadow SUCC / inverse-SUCC / FUCC were intended to build a *finite framework for how mathematical realizations become operationally online/observable*. The finite-vs-Archimedean comparison and RH are stringent examples. In particular, two mathematically accessible descriptions A and B can remain observationally entangled if the current apparatus lacks a probe for their *joint* relationship. Do not replace this by the weaker proposal "find more positive operators" or the stronger, unsupported assertion that RH is undecidable.

**Our interpretive repair:** encode the wavefront using two non-identical filtrations (visited integer positions and available residue/conductor information), a path-category execution relation, an observation family, and a source-connected Dirichlet-logarithm measurement. Ask which operations become available at which finite horizons, and which probes separate rival realized states. Define "online" relative to specified resources, never as ontological creation of mathematical truth.

## 1. A finite object, with two different clocks

For each N>=1 put L_N=lcm(1,2,...,N), and define:

- visited SUCC prefix X_N={0,1,...,N}, with truncated forward/inverse shifts on ell²(X_N);
- residue/conductor clock G_N=Z/L_N Z and H_N=L²(G_N) with normalized counting measure;
- source operators S (successor), V_m (multiplication), and *partial* inverses, with domain and complete intermediate history retained;
- a probe family O_N, to be explicitly declared rather than treated as all conceivable measurements.

If M|M', reduction G_(M')→G_M induces an isometric pullback J_(M,M'):H_M→H_(M'). Its Hilbert adjoint is conditional expectation along fibers:

  E_(M,M') f(r) = (M/M')?  NO: for M'=pM, E f(r)=(1/p)sum_(x mod M':x≡r mod M) f(x).

Precisely, writing M' = dM,

  E_(M,M')f(r) = (1/d) sum_(x∈G_M': x mod M=r)f(x).

Consequently J*J=I, JJ* is the old-information orthogonal projection, and

  I - JJ*

is the new-innovation projection. For nested moduli, the conditional-expectation tower law holds exactly. SUCC intertwines the finite residue shifts with J. No RH assumption enters.

**Important: two shadows.** (a) Future-position shadow Q_N^(position) on ell²(N_0), the complement of {0,...,N}; (b) newly distinguishable conductor-sector shadow Q_N^(resolution) on H_N, the orthogonal complement of J H_(N-1). They are NOT the same projection and often have different activation times. Do not conflate "not visited" with "not constructible".

## 2. Exact conductor-birth theorem

H_N decomposes orthogonally under finite Fourier analysis as

  H_N = ⊕_(d|L_N) W_d,

where W_d is the span of the additive characters of *exact* order d, of dimension φ(d). Hence

  H_N ⊖ J(H_(N-1)) = ⊕_(d|L_N, d ∤ L_(N-1)) W_d

and the innovation rank is L_N-L_(N-1).

The conductor d first becomes *structurally* online at

  b_structure(d)=min{N: d|L_N}=max_(p^k||d) p^k.

Proof: L_N contains the complete maximal p-power p^{floor(log_p N)} and d divides L_N iff every p^k||d obeys p^k≤N. At non-prime-power wavefronts L_N=L_(N-1), so no new conductor Hilbert modes are born. At event N=p^k, L_N=pL_(N-1); innovation rank (p-1)L_(N-1).

Example: N=2 has L_2=2 and modes W_1,W_2. At N=3, L_3=6 and the newborn subspace is W_3⊕W_6, with ranks 2+2=4. Thus conductor 6 exists at N=3, while the integer 6 is first visited by SUCC at N=6. At N=4, W_4⊕W_12 are born. This is an exact, resource-relative distinction; no future integer was physically visited early.

## 3. Actualization is history-sensitive, not a function of the endpoint

A finite path word γ in {SUCC, inverse SUCC, V_p, partial inverse V_p^{-1}} has a full execution history (x_0,...,x_r) whenever every prefix is defined and integral. Call it executable at horizon N iff every intermediate x_i lies in X_N and its primitive operations are enabled. This is a **partial path semigroupoid**, not just a semigroup of endpoint rational-affine maps.

Consider x=2 and p=2:

  γ_short: 2 ->(divide 2) 1 ->(multiply 2) 2.
  γ_long : 2 ->(multiply 2) 4 ->(divide 2) 2.

Their endpoint maps are the same at x=2, yet γ_short is executable at N=2 while γ_long needs N=4. In general an algebraic cancellation cannot erase the first-hit cost of intermediate states.

On the full ell²(N_0), with M_p e_n=e_(pn), D_p=M_p*, the endpoint identity D_p M_p=I holds. For P_N the projection onto states <=N, projection before each step loses an excursion through the future:

  P_N D_p M_p P_N - (P_N D_p P_N)(P_N M_p P_N)
    = P_N D_p (I-P_N) M_p P_N.

At p=n=N=2, the RHS maps e_2 to e_2. This is an exact example where the operational realization of a composite differs from the product of prematurely actualized realizations. It is a generic compression identity, not Weil positivity.

## 4. A genuine joint probe absent from every one-prime observation

At N=3, work with normalized counting measure on Z/6Z. Let

  A(n)=1_(2|n), B(n)=1_(3|n),
  h(n)=(A(n)-1/2)(B(n)-1/3).

CRT yields A,B independent under uniform Haar; explicitly h takes values (1/3,1/6,-1/6,-1/3,-1/6,1/6) at residues 0,1,2,3,4,5. Then

  E[h]=0,
  E[h | residue mod 2]=0,
  E[h | residue mod 3]=0,
  E[|h|²]=1/18 > 0.

Proof: each centered factor has mean zero on its own CRT coordinate; the product is in exact-conductor W_6. Its squared norm is (1/4)(2/9)=1/18.

Thus separate 2-only and 3-only probe families annihilate h, while the joint conductor-6 probe detects it. For an even stronger counterexample define probability snapshots

  μ_±(n)=(1±h(n))/6.

They are strictly positive, have EXACTLY identical marginals on Z/2 and Z/3 (respectively 1/2 each and 1/3 each), but

  E_(μ_±)[h]=±1/18.

This proves operational indistinguishability under the *restricted probe toolkit*, despite a real finite joint discriminator.

**Hostile control:** μ_± are not invariant under cyclic SUCC; if SUCC-invariance is required, finite-rotation Haar uniqueness excludes them. Therefore this is NOT a proof of intrinsic ambiguity between two complete arithmetic universes. It is a proof of a **probe-relative gap** and names its missing lamp: measure the mixed conductor sector.

## 5. Source-connected observability: shadow before the integer arrives

Let a(n) be source Dirichlet coefficients with a(1)=1. Its formal convolution logarithm b=log_*a exists coefficientwise. For n>=2,

  b(n)=a(n)+F_n(a(d): d|n, 1<d<n),

where F_n is the finite sum over ordered multiplicative factorizations of n into >=2 factors, with coefficient (-1)^(r+1)/r for factorizations of length r. Thus F_n depends ONLY on proper divisors: an exact pre-arrival shadow contribution.

For ζ, a(n)=1. Concrete events:

  n=4: F_4=-1/2, b(4)=1/2;
  n=6: F_6=-1  , b(6)=0;
  n=8: F_8=-2/3, b(8)=1/3;
  n=9: F_9=-1/2, b(9)=1/2;
  n=12: F_12=-1 , b(12)=0.

At N=3, the mixed factorization (2,3),(3,2) already supplies F_6=-1, before the direct a(6) event. When the wavefront reaches 6, the true a(6)=1 cancels that shadow, so b(6)=0. This is the **difference between mixed-conductor interaction online at 3 and no new primitive impulse at 6**. If a(6) is independently mutated to 1+δ, the primitive coefficient becomes δ, detecting the fake impulse. This is a real source-sensitive observable. It does not force a Weil sign.

The full Dirichlet logarithm yields b(p^k)=1/k and b(n)=0 at mixed composites (ζ); after multiplying by log n and half-density n^(-1/2), one recovers Λ(n)/√n. This uses actual Euler multiplicativity, unlike the generic CRT geometry above. A nonunit unramified Hecke phase or shifted log 2 is a distinct source-domain violation and needs its own probe.

## 6. Relative observability does NOT mean undecidability

For a specified probe family P_N, let two states be equivalent iff every probe in P_N has the same value. An invariant T is *not decidable by that probe closure* on a model class M if there exist M_1,M_2 in M with identical allowed observations but different T. The μ± construction does this for a deliberately restricted finite snapshot model; adding h separates them.

No conclusion about logical independence of RH follows. Each fixed profinite cylinder mode W_d becomes online at some finite b(d), and the union of these cylinder subspaces is dense in L²(Z-hat) under Haar. However **density in L²** does not by itself establish convergence in the *Weil form norm*, nor show the union is a suitable core under any proposed arithmetic–Archimedean transport. That remains a separate analytic/completion gate.

## 7. Precisely what would earn an RH-facing advance

Construct a map from the finite *history-and-resolution* correspondence, together with the source Dirichlet-logarithm and the actual Archimedean Gamma/pole channel, to the **full** completed Weil form Q_L=P_L-K_L, preserving source mutations and forbidden-atom constraints. Demand an independently derived Hodge-index/sign theorem on the image, NOT a generic positive Hilbert norm and NOT a zero-fitted boundary. The local CRT mixed mode is not itself the Weil global coupling; the two show why joint probes may be necessary.

Pre-register the four cheap failure probes:
(1) any proposed map that forgets intermediate history fails the 2→4→2 path;
(2) any map that forgets W_6 loses the joint 2–3 signal;
(3) any scalar primitive response at n=6 for ζ is false (log_* coefficient zero);
(4) any unconditionally positive map that accepts mutated source or Davenport–Heilbronn unchanged is likely sign-blind and has not passed the Weil identification gate.

## Reproducibility and claims

Script: scripts/operational_actualization_probe.py, Python standard library; no zero input. Finite identities were checked locally with exact Fraction arithmetic and tested through N=8 (including novel W_12 activation), factorization values at n=4,6,8,9,12, μ± one-prime and mixed observables. These are finite calculations with direct elementary proofs; do not claim the complete RH suite ran or that source-specific infinite positivity was proved.

**Claim ledger:** Disclosed: two-filtration construction, conductor birth formula, exact mixed-conductor probe gap, shadow-composition identity, Dirichlet-log source locality. Observed: local finite computations. Refuted: endpoint-only execution captures horizon; separate prime marginals determine a joint probe; conductor 6 implies primitive event at 6. Conjectured: this enriched observability construction could be part of a global arithmetic dualizing correspondence. UNVERIFIED: completed Weil identity, independent global sign, form-domain/limit control. RH OPEN.

Primary repo context: wiki/01 (SUCC frame), research/aletheia_2026-10-05/PROFINITE_SUCCESSOR_LIGHTCONE.md (p-adic clocks and normalized divisibility), research/aletheia_2026-10-05/SUCCESSOR_LIGHTCONE_MULTISETS.md (Euler-connected algebra), docs/external/arithmetic-poisson_2026-10-09/CONSTRUCTION.md (connected source), main Round-067 ledger (finite/local versus global and no undecidability claim).
