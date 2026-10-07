# The clock filtration, with its measure fixed

All identities in this note are unconditional. They are elementary finite
harmonic analysis, not an RH reduction.

Let `L(N)=lcm(1,...,N)` and `H_L=L²(Z/LZ, da/L)`. Write `C_L e_a=e_(a+1)`
in the orthonormal point basis `e_a=sqrt(L) 1_{a}`. If `L|M`, the canonical
isometry is pullback `I_LM f(a)=f(a mod L)`. Its adjoint averages over the
`M/L` children. Consequently `C_M I_LM=I_LM C_L`. These are reducing old
spaces, not merely subspaces with matching eigenvalues.

The clock changes precisely at prime powers `q=p^k`: writing the preceding
length as `L=p^(k-1) M`, `p` does not divide `M`, and the new length is `pL`.
The innovation has dimension `(p-1)L`, not `p-1` unless `L=1`. In the
orthonormal point basis its projection is

\[
 E_{p,L}(a,b)=\delta_{ab}-\frac1p1_{a\equiv b\pmod L}.                 \tag{L1}
\]

Proof: the embedding has entries `1/sqrt(p)` on each child fiber, hence
`II*` has entries `1/p` on that fiber. Its complement is (L1). In each fiber,
projected point vectors have squared norm `1-1/p` and normalized pairwise
inner product `-1/(p-1)`. This is the exact simplex innovation. It is
independent of primality for an arbitrary integer refinement ratio; primality
enters in the LCM event schedule and the conductor classification.

For nested lengths, pullbacks compose exactly. Their inductive Hilbert limit
is `L²(Zhat)` with normalized Haar, because cylinder functions are dense and
LCM lengths are cofinal for divisibility. The compatible clocks extend to
translation by one. Their spectral dual is the discrete group `Q/Z`.
This is compact profinite translation, not a continuum Gamma channel.

The translation commutes with every conductor projection. Hence merely
retaining mixed conductors does not yet produce a noncommuting interaction.
The Fourier/continuum coupling and the shared-origin coupling are examined
separately; they must not be inferred from the existence of this filtration.

Reproduction: `tests.test_round008_clock`; no large LCM matrix is needed.
