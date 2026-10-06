# Stochastic-order audit on actual service laws

**REFUTED:** a universal uncompensated order or martingale coupling of the
prescribed prefix laws. These counterexamples use actual primes and the
unmutated Archimedean term. No infinite inference is made from samples.

Use `X~Unif(0,Sj)` and `Y=Qsvc(X)` as *marginal laws*. The displayed quantile
coupling need not be a martingale; all coupling existence statements below
allow every joint law with those marginals. Order `U<=icv V` means
`E f(U)<=E f(V)` for every increasing concave `f`; `icx` uses increasing
convex functions; `cx` uses all convex functions. Concave order reverses `cx`.

Put `Nj=sum_{i<=j}wi sigmai`. The mean difference is
`E Y-E X=Nj/Sj-Sj/2`. At the first prefix,

\[
 Y=\sigma_0,\quad 0<\sigma_0<S_1/2<S_1,
 \quad \mathbb EY-\mathbb EX\in(-0.020090,-0.020089).
\]

This single certified inequality gives most earliest counterexamples.

| Proposed relation for every prefix | Earliest failure | Exact obstruction |
|---|---:|---|
| `X<=st Y` | q=2 | X has positive mass above sigma0. |
| `Y<=st X` | q=2 | X has positive mass below sigma0. |
| `X<=cx Y` or `Y<=cx X` | q=2 | Means differ. |
| Either full concave order | q=2 | Affine tests again force equal means. |
| `X<=icx Y` (upper stop-loss order) | q=2 | Mean X exceeds mean Y; also upper-support call witness. |
| `Y<=icx X` | q=4 | A call test is larger for Y, although mean Y remains smaller. It holds at q=2 and q=3. |
| `X<=icv Y` | q=2 | Mean inequality fails. |
| `Y<=icv X` | q=2 | Test `min(z,sigma0/2)` is strictly larger for Y. |
| Martingale X→Y or Y→X | q=2 | Equality of means necessary. |
| Submartingale X→Y | q=2 | Equivalent to `X<=icx Y`. |
| Submartingale Y→X | q=4 | Equivalent to `Y<=icx X`. |
| Supermartingale X→Y | q=2 | Equivalent to `Y<=icv X`. |
| Supermartingale Y→X | q=2 | Equivalent to `X<=icv Y`. |

The coupling equivalences use Strassen, explicitly stated with hypotheses
(finite first moments) in Leskela–Vihola, arXiv:1404.0999v3, Theorems 1.1–1.2:
<https://arxiv.org/pdf/1404.0999v3>. Reflection gives the supermartingale case.
These sources supply existence *after* order is proved, not order for primes.

## Exact finite test for the nontrivial earliest failure

Use unnormalized call functions

\[
 C_P(k)=\sum_{i\le j}w_i(\sigma_i-k)_+,\qquad
 C_F(k)=\begin{cases}S_j^2/2-S_jk,&k\le0,\\
 (S_j-k)^2/2,&0<k<S_j,\\0,&k\ge S_j.\end{cases}
\]

`Y<=icx X` iff `D(k)=CP(k)-CF(k)<=0` for every real strike. Between
nodes inside `[0,Sj]`, `D` is a concave quadratic and `D'(k)=S_i-k`,
where `i` is the last node below k. Thus all extrema occur among
`0,Sj,sigmai,Si`; outside this region the functions are affine or zero.
Testing extra `Si` outside their associated gaps cannot create a false
extremum. The two exterior constants are included at the boundary.

At q=2 and q=3 all candidate values are nonpositive (maximum exactly zero
on the common zero tail), proving the relation there. At q=4,
`k=S_2` lies strictly between `sigma_2` and `sigma_3`, and

\[
 C_P(S_2)-C_F(S_2)\in(0.01010680,0.01010681).
\]

This is a rigorous earliest counterexample, not a sampled search. The reverse
call orientation already fails at q=2. Lower stop-loss functions satisfy
`PutP-PutF=D-(Nj-Sj^2/2)`, so all orientations can be checked consistently.
Evidence: `evidence/service_transport.json`; tests recompute signs in Arb.

## What weaker statement survives?

Neither the changing prefix means nor the changing call differences form a
peacock. Recentring would change `T`'s test and the reserve identity; it cannot
be done for free. Even q=7 changes the sign of the mean discrepancy from the
earlier negative values. The desired sign for the single concave `barT` is
strictly weaker than increasing-concave order, and the available positive
`K0` weakens it further. There is no canonical "weakest stochastic order"
other than a custom one-test preorder, which would just rename the target.

`COMPENSATED_CONVEX_ORDER.md` instead defines independent optimal-transport
repair costs and tests actual capital bounds. `MARTINGALE_TRANSPORT_COST.md`
shows that recovered episodes do have an ordered coupling, but its positive
cost is exactly the drawdown still needing payment.
