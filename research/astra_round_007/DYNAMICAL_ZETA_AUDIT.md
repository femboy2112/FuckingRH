# Genuine jet returns have no periodic orbits

**Status:** exact obstruction for forward, height-nondecreasing transfer
operators with ordinary trace-class Fredholm convergence. RH remains open.
This is a proof in this repository, not a priority claim. The obstruction does
not cover operators with backward edges, nontrivial boundary identifications,
or a separately justified distributional trace formula.

## 1. The actual induced system and its clock

Let `S(n)=n+1` on the positive integers. On the section
`J_p={p^k:k>=0}`, the first future return is

\[
F_p(p^k)=p^{k+1},\qquad
\tau_{p,k}=(p-1)p^k.
\]

There is no power of `p` strictly between the two endpoints. After `r`
returns the ordinary SUCC cocycle is exactly

\[
\sum_{j=0}^{r-1}(p-1)p^{k+j}=p^k(p^r-1).
\]

Reparametrize the carrier edge `n -> n+1` by its logarithmic length
`log((n+1)/n)`. The clock telescopes along every path; its induced roof on
the section is `log p`, and the `r`-return roof is `r log p`.

This is an induced map of a deterministic one-sided semiflow. It is not an
application of finite-measure Poincare recurrence: the system has no returning
point, no periodic orbit, and no invariant probability on the one-sided jet.
Indeed invariance gives mass zero at its initial point and then at every
successor point. Returning to a section and returning to the same state are
different assertions.

The suspension over `k -> k+1` with roof `log p` is a half-line, tiled into
equal intervals. Its bilateral extension is a line. Neither has periodic
orbits. A circle of circumference `log p` appears only after identifying all
jet levels, which changes the system.

The nontrivial jets, indexed by `(p,k)` with `k>=1`, are disjoint integer
states. Their common source `1` is excluded from the direct sum. Decorating
that source by a prime label would create multiple copies of one carrier
state; none of the conclusions requires doing so. The induced same-jet return
is also not the one-step compression `P_J S P_J`, and it is not the first
return to the union of all prime-power jets.

## 2. Three operators which must not be identified

Work on `K=l2({(p,k):p prime,k>=1})`, with counting inner product. Define the
forward pushforward shift and two weighted versions by

\[
R e_{p,k}=e_{p,k+1},\qquad
L_s e_{p,k}=p^{-s}e_{p,k+1},\qquad
W_s e_{p,k}=p^{-ks}e_{p,k+1}.
\]

`L_s` weights the actual log-return roof. `W_s` adds absolute-height damping;
its weight is not the roof of the return map. The adjoint gives the reversed
matrix/Koopman convention and has the same determinant obstruction. A sum of
forward and adjoint operators is a different, bidirectional construction.

For `sigma=Re(s)>0`, `L_s` is bounded with norm `2^{-sigma}`. It is not
compact: on the single `p=2` jet the images of orthogonal basis vectors are
orthogonal vectors of common nonzero norm `2^{-sigma}`. Thus the ordinary
Fredholm determinant of `I-L_s` is unavailable, even when `sigma>1`.

For `W_s`, the singular values are exactly the multiset
`{p^{-k sigma}:p prime,k>=1}`. Consequently `W_s` is compact for `sigma>0`
and trace class for `sigma>1`, since

\[
\|W_s\|_1=\sum_{p,k\ge1}p^{-k\sigma}
\le\sum_{n\ge2}n^{-\sigma}<\infty.
\]

Conversely the prime `k=1` terms diverge at `sigma=1` by Euler's theorem
`sum_p 1/p=infinity`, and hence for `0<sigma<=1`. More generally the same
calculation gives membership in Schatten class `S_q` exactly when
`q sigma>1`. These class statements follow from the diagonal operator
`W_s^*W_s`; they are not numerical spectral claims.

The **diagonal event observable** is instead

\[
E_s e_{p,k}=(\log p)p^{-ks}e_{p,k}.
\]

For `sigma>1` it is trace class and

\[
\operatorname{Tr}E_s=\sum_{p,k}(\log p)p^{-ks}
=-\zeta'/\zeta(s).
\]

Absolute convergence follows by comparison with
`sum_{n>=2}(log n)n^{-sigma}`. This records the jet-hit measure exactly. It
does not turn that observable into the trace of a return transfer operator.

## 3. Forward-carrier determinant no-go

**Theorem RT1 (strict increase).** Let `K=direct_sum_{n>=1} K_n`, with each
`K_n` finite dimensional, and let `T` be trace class. Suppose

\[
P_mTP_n=0\quad\text{whenever }m\le n.
\]

Then, for every `r>=1`, `Tr(T^r)=0`, and

\[
\boxed{\det(I-zT)=1\quad(z\in\mathbb C).}
\]

**Proof.** Every multiplication by `T` strictly increases the carrier index,
so a positive power has zero diagonal block. Its trace, legitimately computed
in the orthonormal block basis because it is trace class, vanishes. The
Fredholm logarithmic series near `z=0` is
`-sum_{r>=1} z^r Tr(T^r)/r=0`; analytic continuation of the entire determinant
gives the conclusion for every `z`. Alternatively the compression to
`n<=N` is nilpotent, with determinant 1. These compressions converge in trace
norm to `T`, and ordinary Fredholm determinants are continuous in that norm.
For completeness, the trace-norm convergence follows by first approximating
`T` by a finite-rank operator and using strong convergence of the bounded
projections on its finite-dimensional domain and range. **QED.**

This includes arbitrary forward SUCC edges, forward multiplication edges,
first-return edges, and their positive or signed mixtures, with arbitrary
internal finite multiplicity and diagonal weights, whenever every surviving
edge strictly raises the chosen proper carrier index. Signs and phases do
not create a closed path.

**Theorem RT2 (diagonal data cannot acquire a forward interaction).** Under
the same decomposition, let `A` be trace class and block triangular:
`P_mAP_n=0` for `m<n`. Write `A_n=P_nAP_n`. Then

\[
\boxed{\det(I-zA)=\prod_{n\ge1}\det(I-zA_n).}
\]

The product is the trace-norm limit of its initial finite products. Thus the
strictly height-increasing off-diagonal currents have no effect whatsoever
on this determinant.

**Proof.** Every finite carrier compression is block triangular and its
determinant is the product of the diagonal-block determinants. The diagonal
block operator is trace class: pinching onto a finite block partition is
trace-norm contractive, so `sum_n ||A_n||_1<=||A||_1`. Both compressions converge
in trace norm, and determinant continuity proves the identity. Equivalently,
a closed index chain in the trace of any power can use only constant-index
edges. **QED.**

This is a sharper discriminator than just testing the bare shift. Decorating
a diagonal Euler operator with forward SUCC/FUCC currents does not make its
determinant depend on the new carrier geometry. To escape RT2, a proposed
trace construction must exhibit a genuine index-decreasing interaction,
a nontrivial identification, or a different justified trace topology. It must
then calculate the new closed-path terms rather than inherit the Euler ones.

For `W_s` specifically, RT1 proves `det(I-zW_s)=1` throughout `Re(s)>1`.
Carrier cutoffs, `p^k<=N`, have exactly the same result at each `N`. Completing
individual towers instead does not help. The regularized `det_q` is also 1
whenever `W_s` belongs to an integer Schatten class `S_q`: its defining local
logarithmic series starts at `r=q` and all those traces vanish. Its use does
not create the Euler determinant either.

These are ordinary determinant statements. A strong-operator limit alone
does not license continuity of trace or determinant. A claimed renormalized
boundary trace must be derived separately and cannot be cited as an
exception already supplied by the forward geometry.

## 4. Why the Euler determinant is easy, and why it is a different object

Let `E=l2(P)` and `D_s e_p=p^{-s}e_p`. For `Re(s)>1`, this is trace class,
has norm below 1, and

\[
\det(I-D_s)=\prod_p(1-p^{-s})=\zeta(s)^{-1},
\qquad
-\log\det(I-D_s)=\sum_{k\ge1}\frac{\operatorname{Tr}(D_s^k)}k.
\]

The `k` in `Tr(D_s^k)` counts repetitions of an inserted self-loop on the
prime label. It does not count fixed points of `k -> k+1`, which has none.
Collapsing every jet to its label gives precisely that loop, or suspending
the identity on prime labels with roof `log p` gives circles of those lengths.
Both insert the primitive prime indexing and the orbit lengths. Their Euler
identity is classical and tautological in those inputs, not a nontrivial
transfer realization derived from the SUCC return dynamics.

There is also no nonzero bounded Hilbert-space quotient map intertwining one
unweighted jet shift with the scalar identity. A bounded linear functional
`ell` with `ell R=ell` has constant basis coefficients, and that constant
sequence belongs to `l2` only when it is zero. The same argument applies to
`L_s` versus its desired scalar weight `p^{-s}` on that jet. Finite normalized
orbit sums only give approximate intertwiners and vanish weakly as their
support grows. This rules out treating the orbit collapse as a bounded exact
compression without paying a new topology or boundary-state cost.

One can retain the carrier integer basis and write
`Tr(exp(-sH))=sum_{n>=1}n^{-s}=zeta(s)` for `Re(s)>1`. This is a genuine,
classical heat/partition trace with self-adjoint `H e_n=(log n)e_n`. It does
not make the zeros eigenvalues, continue a positive trace into the critical
strip, or supply the completed Weil square.

## 5. Adding the reverse orientation: an exact control

On a finite jet of depth `d`, add the backward shift and put
`J_d=a(R_d+R_d^*)`, with real constant `a`. Then the determinant
`F_d(z)=det(I-zJ_d)` satisfies

\[
F_0=F_1=1,\qquad
F_d=F_{d-1}-a^2z^2F_{d-2},
\qquad
\operatorname{Tr}(J_d^2)=2(d-1)a^2.
\]

Expansion along the last row proves the recurrence. Counting the two
orientations of each adjacent edge proves the trace formula. These are
backtracking closed walks, not primitive prime loops. The determinant is
even in `z` and the quadratic trace grows with the jet depth; neither matches
the Euler factor `1-z p^{-s}`. Other coupled chiral operators are not excluded
by this calculation, but their new cycles require their own trace theorem.

Thus backward orientation does escape the **hypothesis** of RT1, while the
most immediate symmetrization fails the **desired identity** exactly.

## 6. Primary literature: what actually applies

**Ruelle (1976), Theorems 1–3 and pp. 234–236.** The finite-symbol holomorphic
inverse branches map relatively compactly into their domains. Their nuclear
operators on exterior forms have alternating fixed-point traces; this yields
a quotient of entire Fredholm determinants. The geometric corollaries require
a real-analytic expanding map on a compact manifold, or a real-analytic
Anosov flow with analytic stable/unstable foliations. Our monotone countable
jet system satisfies none of these listed geometric hypotheses and has no
periodic points. The paper's determinant mechanism does not convert our open
paths into its closed symbolic words.

**Ruelle (1994), pp. 212–213.** For a continuous piecewise strictly monotone
interval map and bounded-variation weight, the transfer operator sums weighted
preimages. Under a generating partition, the periodic-point determinant is
holomorphic in the stated essential-spectral-radius disk, and its zeros
correspond to isolated eigenvalues outside that radius. The note extends the
periodic-point bookkeeping beyond that partition assumption. It supplies no
theorem that nonperiodic countable translation has an Euler zeta function.

**Connes (1994), Chapter V §11β, pp. 529–531, Lemma 6 and Propositions 7–8.**
The prime one-particle space, its bosonic space `l2(N*)`, multiplication
isometries, and logarithmic Hamiltonian are already present. The one-particle
Euler Fredholm identity and Gibbs partition function are classical here.
Unique factorization identifies the bosonic basis; it does not insert SUCC
into the tensor-product dynamics. The arithmetic coupling by SUCC is extra
structure to be audited, not a novelty claim for that Fock-space description.

The rendered book p. 530 literally prints positive powers in its Euler trace
formula although its preceding definitions are `T e_p=p e_p`, `ST e_n=n e_n`
and its domain is `Re(s)>1`. Those signs cannot be correct: both traces would
diverge. Our formula uses `T^{-s}` and `(ST)^{-s}`, as required directly by
the definitions and by the neighboring `exp(-beta H)` Gibbs formula. This is
a detected source typo, not silently inherited notation. The 1995 Bost–Connes
article was retrieved as a scan but was not fully audited; no additional
theorem from it is used here.

Sources, retrieved hashes, exact inspected scopes, and this typography issue
are recorded in `reviews/dynamics_sources.json`. All operator identities in
Sections 1–5 were derived here independently; the citations classify their
relationship to established constructions.

## 7. Reproducible finite controls and verdict

Run:

```bash
python -m unittest tests.test_round007_return_transfer -v
python -m scripts.round007_return_transfer
```

`evidence/return_transfer.json` contains exact rational matrices encoded by
their nonzero edges, determinants, power traces, and the reverse-orientation
control. Carrier horizons are `2,4,9,16,32,64`; these calibrate RT1, not prove
it. Deleting a prime, adding a composite jet, replacing primes by pairwise
coprime composite generators, and changing the return weights all leave the
forward determinant 1. This is the predicted insensitivity of the **failed**
constructor. Inserting self-loops changes the determinant exactly and adds a
fake Euler factor when a composite label is inserted.

**Refuted:** a nontrivial Euler/Riemann Fredholm determinant obtained from
genuine forward SUCC-induced prime-jet transfers by a trace-class limit;
also, the claim that adding only forward currents makes a diagonal Euler
determinant sensitive to the carrier path.

**Still open:** a bidirectional/chiral or completed boundary construction with
an independently proved trace/energy identity. Its first unpaid requirement
is to calculate a nonzero closed-path or boundary contribution that survives
the actual pushforward and has the completed Weil signs. Naming a suspension,
quotient, or Ruelle operator does not discharge that requirement.
