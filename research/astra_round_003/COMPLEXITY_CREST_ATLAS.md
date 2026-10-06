# Finite complexity-crest atlas

**Status:** exact finite arithmetic tables; interval-enclosed descriptive contrasts;
seeded exploratory controls. No RH inference and no all-scale prime-separation
theorem. The primary IC signal survives this finite probe; the stronger idea of a
metric-independent crest does not receive support from the addition-chain probe.

## 1. Object and preregistered probe

`evidence/crest_protocol.json` was written before this round's atlas computation.
The atlas contains every integer `1 <= n <= 512`; exact shortest addition chains
are computed only through 128 and are `null` above 128. The primary population
is **odd** integers `9 <= n < 512`, preventing evenness alone from distinguishing
prime and composite labels. The ranges are fixed:

- IC training: `9 <= n < 256`; held out: `256 <= n < 512`.
- Addition-chain training: `9 <= n < 64`; held out: `64 <= n < 128`.
- Primary feature: `IC(n) - 3 log(n)/log(3)`.
- Secondary feature: `ell(n) - floor(log_2(n))`, the integer number of small steps.
- Within each dyadic bin, subtract the mean over every eligible integer, without
  using the labels. Compare the prime and composite residual means.
- Seed `20261006`; 199 realizations of each specified control.

The holdout is an unfitted continuation inside the same small integer regime,
not an independent source family or an asymptotic holdout. Neither a selected
large prime nor zero data enters the construction.

Each record includes factorization, prime and prime-power status, multiplicity
`Omega`, divisor count and strict divisor-record/highly-composite status, exact
complexity and an optimal root witness, exact shortest chain and search counts,
prime gaps, direct old-monoid midpoint count, Suzuki prime-power weight, full-tower
mass `M_p`, and service location `A'(log(n))`. All transcendental entries are Arb
balls at 160-bit precision. The unit `n=1` has no service node; no singular formula
is evaluated there. Complete raw output is `evidence/crest_atlas.json`.

`successor_cost` is deliberately `null`: integer complexity is not successor
execution work. The independently declared machine in
`SUCCESSOR_OPERATIONAL_GEOMETRY.md` owns that distinction.

## 2. Why the finite complexity computations are exact

For positive expressions built from `1`, binary `+`, and binary `*`, define
`c(1)=1`. An optimal expression for `n>1` has a root operation whose positive
children are strictly smaller than `n`; a multiplicative child equal to one can
be deleted. Hence

\[
c(n)=\min\left\{
 c(a)+c(n-a):1\le a\le n/2;
 \ c(a)+c(n/a):2\le a\le\sqrt n,\ a\mid n
\right\}.
\]

Conversely, every candidate is an actual expression. Induction on `n` proves
both lower and upper bounds. The script saves the minimizing root. A separate
forward search organized by number of leaves, rather than value, agrees through
64. The exact integer inequality `n^3 <= 3^c(n)` checks the classical lower bound
on the full atlas; powers of three attain it. The known instability
`c(107)=16`, `c(321)=18` is reproduced: factorization need not give minimal
expression complexity by simple additive bookkeeping.

An addition chain uses any two previous entries, including equal entries.
Positive chains can be sorted and duplicate entries removed: each summand is
strictly smaller than the resulting sum. No entry above the target can help
produce the target. The search therefore enumerates all increasing chains
ending at `n`, not only star chains. It tries lengths from
`ceil(log_2(n))` to the binary-expansion upper bound
`floor(log_2(n))+popcount(n)-1`. The only reachability pruning is

\[
 a_{\mathrm{last}}2^{\text{remaining steps}}<n,
\]

which is impossible because each step can at most double the largest entry.
The first successful depth is globally minimal. A breadth-first search without
this target-specific pruning independently agrees through 24. The saved witness
for 127 has length 10. Optimal lengths above 128 are **not** estimated or filled
with a heuristic.

Primary controls are Altman's [integer-complexity algorithms paper](https://arxiv.org/html/1606.03635v2),
Introduction and Section 2.2, and his [addition-chain paper](https://arxiv.org/html/1409.1627v2),
Introduction and Section 2. The [integer-defect paper](https://arxiv.org/abs/1804.07446)
is used only to avoid confusing its separate integer-valued defect with the
real IC defect used here. Source scope is recorded in
`reviews/complexity_sources.json`. These papers share an author; they do not
constitute independent empirical witnesses.

## 3. What the multiplicative coordinate does and does not reveal

With primes admitted as cost-free atomic leaves and only binary multiplication
counted, an integer with `Omega(n)` prime factors needs exactly

\[
 d_\times(n)=\lceil\log_2\Omega(n)\rceil
\]

levels for `Omega(n)>=1`, and depth zero for the unit. A binary tree of depth
`d` has at most `2^d` leaves, and a balanced tree attains the bound. Thus primes
have depth zero and composites positive depth **by definition**. This coordinate
records grammar structure but cannot independently validate prime crests.

Old-monoid membership is tested directly by factoring both endpoints for every
`1 <= d < p`. It agrees exactly with

\[
 |\mathcal D_p|=(p-1)-\#\{q\text{ prime}:p<q<2p\}
\]

at every prime in the atlas. This is a finite implementation check of the
separately proved theorem in `OLD_MONOID_MARTINGALE_DILATION.md`, not a numerical
proof of density tending to one.

## 4. Held-out results and hostile nulls

Numbers below are rounded displays; the JSON retains the enclosing Arb balls.
The primary observed contrasts have uncertainty below `6e-46`.

| Feature and range | Prime minus composite dyadic-residual mean | Nearest odd-composite difference | Shuffled statistics >= observed | Gap-permuted statistics >= observed |
|---|---:|---:|---:|---:|
| IC train | 0.674992 | 0.827854 | 0/199 | 0/199 |
| IC holdout | 0.732588 | 0.851661 | 0/199 | 0/199 |
| Chain small steps train | 0.321429 | 0.357143 | 38/199 | 38/199 |
| Chain small steps holdout | 0.190283 | 0.307692 | 40/199 | 104/199 |

Each nearest-size match chooses the nearest odd composite in the same declared
range, lower integer breaking ties; matching is with replacement. Shuffling
preserves exactly the prime count in every dyadic bin. Independently seeded
uniform sparse subsets with those same counts implement the **same null law**,
not a second independent statistical hypothesis: their counts at least the
observed value are `0,0,27,59`, respectively.

The gap control fixes the first and last selected integer in each dyadic bin
and permutes the exact consecutive prime-gap multiset. It preserves count,
endpoints, parity, and the full gap histogram, but changes the association to
integer-complexity values. For the IC holdout its maximum contrast is about
`0.430179`, below the actual `0.732588`. Addition-chain holdout is much weaker:
104 of 199 gap-preserving permutations tie or exceed the actual contrast.
No rank here is a probability that a mathematical mechanism is true. The raw
label sets and all control statistics are saved, permitting replay.

Fixed descriptive subgroups over `9 <= n < 512` give:

| Subgroup | Count | Mean IC defect | Mean dyadic residual, all-integer reference |
|---|---:|---:|---:|
| Primes | 93 | 2.513134 | 0.678555 |
| Higher prime powers | 17 | 1.000855 | -0.563164 |
| Odd higher prime powers | 12 | 1.149851 | -0.414264 |
| Highly composite divisor records | 9 | 0.633963 | -0.796484 |
| Other composites | 393 | 1.777060 | -0.136213 |

These broad subgroup means are descriptive, not matched causal effects. The
all-integer reference includes parity differences. Under the **odd-only**
dyadic reference, primes average `+0.441502` and odd higher prime powers average
`-0.643804`. Thus the prime-power support of Suzuki's measure is not one uniform
high-defect class in this finite atlas. Highly composite numbers are all even in
this range, so their separation cannot be presented as a parity-independent
control.

## 5. Verdict and exact boundary

The preregistered finite IC direction survives parity, size normalization,
nearest-composite matching, and the specified random and gap controls. It would
be false to say this atlas killed every prime-crest hypothesis. It also would
be false to extrapolate this finite association to all primes or all complexity
metrics. The addition-chain comparison shows why the metric is load-bearing.

There is an immediate arithmetic-weight blind spot. Changing one Suzuki weight
leaves factorization, integer complexity, addition chains, and every contrast
above unchanged. The test mutates the weight at 13 to `10^12` and confirms exact
identity of the diagnostic output. Consequently the atlas alone cannot supply
the exact prime/Archimedean compensation or pay Brownian debt. A theorem using
these strata must add a weight-sensitive map and prove its required nonlinear
moments and sign; otherwise it survives a mutation that the actual CND target
must detect.

No step here constructs such a map. The frontier is the moment-cone/primitive
projection problem in the neighboring documents, not a request for more
correlation plots.

## Reproduction

```bash
python -m unittest tests.test_complexity_crest_atlas
python -m scripts.complexity_crest_atlas \
  --output research/astra_round_003/evidence/crest_atlas.json
```

There are seven atlas tests: independent IC enumeration, root witnesses and
exact lower bound, independent chain breadth-first search, full chain witness
validation/missing-data honesty, monoid/depth conventions, surrogate marginal
checks, and Suzuki-weight mutation blindness. These are finite controls; the
algorithmic completeness arguments above establish what their outputs mean.
