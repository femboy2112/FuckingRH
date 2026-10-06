# Pinned finite-height slack: a certified recovery-witness failure beyond `10^10`

**Verdict: the height-optimized pinned constructor fails at a rigorously
certified valid-domain recovery witness beyond the source's finite base. RH is not disproved or proved.**

Using the actual prime-power stream, take

\[
x=10{,}275{,}204{,}761,\qquad q=10{,}381{,}395{,}137,\qquad T_0=10^7.
\]

Both event labels are prime. The anchor is an actual excursion entry and the
workload stays strictly positive until the terminal event. The certified
values are

\[
V_q\in[0.031213\pm0.000000946],\qquad
C_q-\widehat J_{T_0,\mathrm{pin}}
\in[-0.28808\pm0.00000562].
\]

The notation `[m +/- r]` denotes the full enclosing interval `[m-r,m+r]`.
An analytic derivative estimate below proves that `T_0` minimizes the
constructor over **every admissible verified height**, not just a sampled
grid. Height optimization therefore cannot repair this failure.

**Scope matters.** This fresh arithmetic witness lies above `10^10`, the
external finite-certificate cutoff. It was selected by a new prime-stream scan,
then certified by exact integer moments and Arb, without importing diagnostic
floating-point states. Its immediate successor is `10,381,395,223`; the
post-event workload is positive and the pre-successor workload is negative,
so the actual recovery minimum lies strictly between them. Thus the present
height-optimized pinned constructor fails even at a *recovery witness* in the
proposed infinite tail, not merely at a redundant interior active event.

This refutes certification of every recovery witness beyond `10^10` using this
constructor. It does not refute RH, a stronger smoothed bound, or a different
constructor claimed only after some larger threshold. No universal eventual
failure theorem is asserted.

## 1. Exact object and valid external premise

Use Round 001's unmutated Suzuki normalization. Write

\[
W_z=\sum_{p^k\le z}\frac{\log p}{p^{k/2}},\qquad
L_z=\sum_{p^k\le z}\frac{k(\log p)^2}{p^{k/2}},
\]

\[
E_z=A(\log z)-W_z\log z+L_z,\qquad
Y_z=W_z-A'(\log z).
\]

At the terminal event, put `P=W_q-W_x`, `P^-=P-log(q)/sqrt(q)`,
`a=log x`, `s=log q`. The actual timing cost is exactly

\[
J_q=P\log q-(L_q-L_x).
\]

Chirre–Helfgott Proposition 9.1 supplies

\[
\Sigma_{1/2}(u)\le A_T\sqrt u-\alpha+d_T
\quad\left(u>\max(T,10^9),\quad T\ge10^7\right),
\]

provided RH has been verified through height `T`, where

\[
A_T=\frac\pi T\coth\frac\pi{2T}+\frac\pi{T-1},\qquad
d_T=\frac1{2\pi}\log^2\frac T{2\pi}
             -\frac1{6\pi}\log\frac T{2\pi}.
\]

For the derivative proof below, write
`c_T=(pi/T)coth(pi/(2T))`, `e_T=pi/(T-1)`, so `A_T=c_T+e_T`, and denote
the full prefix upper bound by `U_T(u)=A_T sqrt(u)-alpha+d_T`.

Platt–Trudgian's Theorem 1 verifies the needed finite-height premise through
`H_*=3,000,175,332,800`; their theorem was reopened as a primary source.
Their computation is an external theorem, not rerun in this repository.
Our choice `T_0=10^7` and every integration coordinate `u>=x>10^9` are strictly
inside the stated domain. No assumption of full RH is used.

The exact pinned constructor is

\[
R_{T,a}(u)=A_T\sqrt u+d_T-\alpha-W_x,
\qquad
\widehat J_{T,\mathrm{pin}}
=\int_x^q\min(P^-,R_{T,a}(u))\frac{du}{u}.
\]

This upper bound remains valid. The failed statement is that its additive
excess always fits inside the actual reserve. In this run the clipping point
lies strictly between `x` and `q`; the closed form from Part 3 equation (68)
is evaluated with interval arithmetic and certified branch comparisons.

All Archimedean terms are retained. In particular

\[
A'(\log z)=2\sqrt z-\alpha+h(z),\qquad
h(z)=\operatorname{atanh}(z^{-1/2})+\arctan(z^{-1/2})-2z^{-1/2}.
\]

The omitted `-h(u)` from the source's equation (75) is never discarded or
used here. We evaluate the original constructor through `W_x` directly.

## 2. Exact integer enumeration, then rigorously bounded weights

The companion script embeds a newly written segmented integer sieve. It
uses no floating-point operations. For each integer block `[l,r]`, with
integer center `c=floor((l+r)/2)`, it records

\[
N=\#\{p\in[l,r]\},\qquad M_1=\sum(p-c),\qquad
M_2=\sum(p-c)^2.
\]

The full run enumerates `471,600,819` primes through `q`. Higher powers are
generated independently from primes through `floor(sqrt(q))`, adding `10,251`
events. Their weights are evaluated individually using Arb balls.

For ordinary primes use

\[
f(z)=z^{-1/2}\log z,\qquad g(z)=z^{-1/2}\log^2z.
\]

Taylor's theorem gives

\[
\sum f(p)=Nf(c)+M_1f'(c)+\tfrac12M_2f''(c)+\epsilon_f,
\]

and the same formula for `g`. With `h=max(c-l,r-c)`, exact derivative
calculations yield

\[
f'''(z)=z^{-7/2}\left(\tfrac{23}4-\tfrac{15}8\log z\right),
\]

\[
g'''(z)=z^{-7/2}\left(-9+\tfrac{23}2\log z-\tfrac{15}8\log^2z\right).
\]

Thus the explicit, conservative remainder bounds are

\[
|\epsilon_f|\le\frac{Nh^3}{6l^{7/2}}
  \left(\tfrac{23}4+\tfrac{15}8\log r\right),
\]

\[
|\epsilon_g|\le\frac{Nh^3}{6l^{7/2}}
  \left(9+\tfrac{23}2\log r+\tfrac{15}8\log^2r\right).
\]

Arb encloses every transcendental evaluation, polynomial operation, remainder,
and accumulation at 128-bit working precision. The certified run uses relative
block width at most approximately `1/8192`; after the anchor, blocks have at
most 2,048 integer coordinates to support excursion verification. There are
`171,619` integer-moment blocks in the retained raw file.

Integer safety is explicit. The helper rejects `limit>2*10^10`. Given
`width=floor(limit/divisor)+1` and `half=ceil(width/2)`, it also rejects
`width*half^2>=2^64`, `width*half>=2^63`, or `half^2>=2^63`. These bounds cover
the sum of squared centered displacements, the signed first moment, and each
individual squared displacement even if every integer is treated as prime.
At the retained divisor `8192`, all bounds hold throughout the permitted
range. Base-prime square products and all coordinates fit unsigned 64-bit.
The guard is evaluated with Python arbitrary-precision integers before native
execution; no overflow-prone native calculation is used to justify itself.

This is not a recomputation of the entire source's positivity certificate.
Only the chosen exact prefixes, excursion membership, and constructor slack
are certified.

## 3. Entry and same-excursion verification

The independently recomputed anchor has

\[
Y(\log x^- )\in[-0.0000022\pm0.0000000496],
\]

\[
Y(\log x^+ )\in[0.0002253\pm0.0000000617].
\]

So it is an actual negative-slope excursion entry. To verify persistence until
`q`, each block uses the sufficient lower bound

\[
Y(\log u)\ge W_{l-1}-A'(\log r),\qquad l\le u\le r,
\]

because the cumulative arithmetic weight increases and `A'` increases.
When this bound does not prove positivity, a separate Python segmented sieve
enumerates every event in that block. Arb then checks the pre-event workload,
adds the exact event weight, and checks the right block endpoint. Between
events the workload decreases, so these checks exhaust the interval.

The run checks `51,852` blocks. Of those, `332` require eventwise refinement,
covering `29,691` explicitly evaluated events. Every required lower bound is
positive, with the least certified bound greater than

\[
1.8120\cdot10^{-6}.
\]

The terminal workload is enclosed by `[0.0008369 +/- 0.0000000529]`.
A separate segmented-prime and higher-power enumeration proves that the next
event is exactly `10,381,395,223`; there is no intervening prime power. Its
pre-event workload is `[-0.0000072 +/- 0.0000000255]`. Strictly increasing
`A'` therefore crosses the frozen prefix weight once between those events.
This proves actual recovery and identifies `q` as the episode's terminal
recovery witness. Its frozen reserve equals the actual recovered minimum.

## 4. Reserve enclosure without an uncertified root solve

Since `Y_q>0`, the frozen branch has its minimizer after `s=log q`. Round 001
proved that `A''` is positive and increasing there. The strong-convexity bound
therefore gives the exact enclosure

\[
E_q-\frac{Y_q^2}{2A''(s)}\le V_q\le E_q.
\]

No floating-point inverse-clock root is accepted as exact. Combining this
bound with the identity `C_q=V_q+J_q` produces the slack enclosure.

| Recomputed quantity | Certified enclosure |
|---|---|
| `W_x` | `[202730.6834737 +/- 0.0000000452]` |
| `L_x` | `[4268149.267532 +/- 0.000000876]` |
| `W_q` | `[203775.5779334 +/- 0.0000000608]` |
| `L_q` | `[4292242.593212 +/- 0.000000885]` |
| Entry value `E_x` | `[0.03321 +/- 0.00000125]` |
| Actual timing cost `J_q` | `[5.36898 +/- 0.00000558]` |
| Pinned cost upper bound | `[5.688272 +/- 0.000000425]` |
| Frozen reserve `V_q` | `[0.031213 +/- 0.000000946]` |
| `C_q-Jhat` | `[-0.28808 +/- 0.00000562]` |

The failure is not a rounding-scale disagreement: the additive overestimate
is about `0.31929`, while the actual reserve is about `0.031213`.

## 5. All admissible heights: optimization cannot rescue this witness

Put `z=pi/(2T)`. The partial fraction expansion
`coth z=1/z+2z sum_{n>=1}(z^2+pi^2 n^2)^{-1}` gives

\[
0<-c_T'\le\frac{\pi^2}{3T^3},\qquad
-e_T'=\frac\pi{(T-1)^2},\qquad
d_T'=\frac{\log(T/(2\pi))-1/6}{\pi T}.
\]

For `T>=T_0` and `u<=q`, it follows that

\[
T\,\partial_T U_T(u)\ge
\frac{\log(T_0/(2\pi))-1/6}{\pi}
-\sqrt q\left[\frac{\pi^2}{3T_0^2}
 +\frac{\pi T_0}{(T_0-1)^2}\right].
\]

Here `log(T/(2pi))` increases, `T^-2` decreases, and
`T/(T-1)^2` decreases for `T>1`. Arb encloses the right side by

\[
[4.4604736801465688192668037119088476196\pm9.01\cdot10^{-38}]>0.
\]

Hence `U_T(u)` increases strictly with `T` throughout the entire integration
interval and throughout all `T>=T_0`. Subtracting the fixed exact `W_x`, clipping
by the fixed `P^-`, and integrating preserve nondecreasing order. Consequently

\[
\inf_{10^7\le T\le H_*,\ T<x}\widehat J_{T,\mathrm{pin}}
=\widehat J_{10^7,\mathrm{pin}}.
\]

This proves the all-height failure for the chosen actual state. It does not
use the source's continuum model or assume its approximate optimal height.

## 6. Exact loss propagation within an episode

Fix the anchor `x` and an admissible height `T`; write the terminal cap at
an event `q_j` as `P_j^-` and the total post-event incremental load as
`P_j=P_j^-+w_j`. Let `q_{j+1}` be its immediate successor. The next
preterminal cap is exactly `P_j`. On the added interval `(q_j,q_{j+1})`, the
actual incremental load is constant `P_j`, and the proved spectral envelope
is at least `P_j`. Therefore the added contributions to the true cost and
pinned upper cost are identical. Subtracting the old integrals gives exactly

\[
(\widehat J-J)_{j+1}-(\widehat J-J)_j
=\int_x^{q_j}
 [\min(P_j,R_{T,a}(u))-\min(P_j^-,R_{T,a}(u))]\frac{du}{u}
\ge0.
\]

Thus the pinned additive loss is nondecreasing along the event stream. If the
successor stays in the same active episode, the convex-dual event formula gives

\[
V_{j+1}-V_j=\int_0^{w_{j+1}}
 [\log q_{j+1}-(A')^{-1}(W_j+v)]\,dv<0,
\]

because the pre-event workload is positive. Consequently the certified slack
`V-(Jhat-J)` decreases within that episode. This is an exact arithmetic and
convexity statement, not a continuum or stochastic approximation. It explains
why the first negative interior witness in the new scan remains negative at
the eventual recovery. The explicit recovery certificate above does not need
an unproved assumption that the excursion ends.

## 7. Reproduction, controls, provenance and boundary

Run from the repository root:

```sh
python -m unittest tests/test_pinned_tail_slack.py
python scripts/pinned_tail_slack.py --x 10275204761 --q 10381395137 \
  --next-event 10381395223 --extra-cut 10320015703 --divisor 8192 \
  --verify-episode \
  --moments research/astra_round_002/evidence/pinned_tail_recovery_moments_8192.csv.gz \
  --output research/astra_round_002/evidence/pinned_tail_recovery_certificate_8192.json
```

Add `--reuse-moments` to recompute the ball certificate from the retained
compressed integer moments without rerunning the native sieve. The stored
`moment_sha256` hashes the decompressed canonical CSV bytes.
The displayed `--extra-cut 10320015703` retains the intermediate witness's
block split and reproduces the exact original CSV hash. That exact command
with `--reuse-moments` was rerun successfully. Add `--independent-counts` to
repeat the separate combinatorial event-count control inside the output JSON.

The code needs `python-flint`, `sympy` for the optional independent count,
and a C++17 compiler. Eight tests passed. Controls include independent
native-versus-Python prime enumeration, exact moment comparisons, direct Arb
prime-power sums, wide-block Taylor checks, invalid theorem domains, integer
overflow guards, the retained Archimedean tail, exact loss-monotonicity examples,
and actual positive/negative episode controls. Deleting the prime-2 event
makes the positive episode control fail, as required. Large-event counts are
also checked separately by SymPy's combinatorial `primepi` plus exact integer
roots, rather than the segmented sieve used for weighted sums.

The primary retained certificate is
`evidence/pinned_tail_recovery_certificate_8192.json`; the accompanying
compressed moment stream contains all raw integer block data. Earlier JSON
outputs retain the discovery trail, including the first beyond-base interior
failure at `q=10,320,015,703`, whose slack is `[-0.10000 +/- 0.00000301]`.
That candidate came from a new ordinary-long-double prime-stream scan after
an independently computed `10^10` prefix; its floating-point states were not
accepted into any certificate. The scan then continued to the first recovery,
which was independently checked with ball arithmetic and exact event labels.
This is a fresh beyond-source-calibration test; it is not a statistical
out-of-sample estimate or a universal extrapolation.

A preliminary calibration reconstructed the source's known long excursion
`x=1,066,070,623`, `q=1,136,726,333` and certified slack
`[-1.96745 +/- 0.00000343]`, including same-excursion membership. That point
lies below `10^10` and cannot alone refute a later-tail claim. It was used to
validate the method before the new beyond-base scan. Intermediate integer
CSV files are reproducible from the script and may be omitted; their hashes
and interval JSON outputs are retained, while the final recovery's complete
raw compressed moment stream is retained.

Source lineage:

- Mittermeier Part 3 v3, pinned in Round 001 at
  https://zenodo.org/records/22076071, equations (61)–(70), pp. 15–18.
  Its page-18 diagnostic and `part5v1.zip/source_inputs/episodes_2e9.npy`
  supplied only the initial *calibration* labels. The beyond-`10^10` candidate
  was found by a new actual-prime scan.
- Chirre–Helfgott, https://arxiv.org/abs/2512.15709, Proposition 9.1,
  specialized to `sigma=1/2` with the exact domain. The primary PDF was read
  in Round 001 and reopened locally this round.
- Platt–Trudgian, https://arxiv.org/pdf/2004.09765, Theorem 1: rigorously
  verified RH through height `3,000,175,332,800`. Reopened this round. No
  individual zero ordinate enters any arithmetic prefix computation.
- NIST DLMF 4.36.3, https://dlmf.nist.gov/4.36.E3, reopened for the exact
  coth partial-fraction formula used in the all-height derivative bound.

**Next discriminating requirement:** a stronger actual-arithmetic cost
bound must reduce its additive excess from about `0.31929` to at most about
`0.031213` at this recovery witness. Relabeling the same envelope or optimizing
its height cannot meet that requirement. This is a decisive failure of the
specific proposed certificate after its finite base, with a still-positive
actual reserve; the genuine arithmetic sign theorem remains open.
