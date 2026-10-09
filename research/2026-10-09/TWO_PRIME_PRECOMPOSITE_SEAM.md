# The two-prime precomposite boundary seam

**2026-10-09. Proven local operator lemma; RH OPEN.**

A useful discriminating test exists *before* the first composite cross-prime event n=6 enters the explicit-formula lightcone.

## Statement

Let \(H_L=L^2(0,L)\) and let \(T_h\) be translation by \(h\ge0\) compressed to this interval, i.e. \(T_h f(x)=\mathbf1_{x>h}f(x-h)\), zero outside the interval. For \(0<a<b<L\),

\[
\boxed{
[T_a^*,T_b]f(x)=
\left(
\mathbf1_{b-a<x<L-a}
-
\mathbf1_{b<x<L}
\right)
f(x+a-b).
}
\]

Derivation is direct from \(T_a^*f(x)=\mathbf1_{x<L-a}f(x+a)\) and the zero extension. No zeta zeros or arithmetic conjecture are used.

In the regime

\[
\boxed{b<L<a+b}
\]

the two output intervals are disjoint, as are the corresponding input intervals. Their common length is \(\delta=L-b>0\). Consequently \([T_a^*,T_b]\) is a signed direct sum of two orthogonal translated partial isometries and

\[
\boxed{\|[T_a^*,T_b]\|=1.}
\]

At \(L\le b\), \(T_b=0\), so the commutator is zero. Thus its operator norm jumps from 0 to 1 when the second source event first becomes active. Strong convergence on fixed regular inputs is a different issue; do not infer operator-norm continuity.

## Arithmetic specialization

Take

\[
a=\log2,\qquad b=\log3,\qquad \log3<L<\log4.
\]

Then \(b<L<a+b=\log6\). The primitive source has exactly the two new prime channels \(2,3\) (there is not yet a 4 or 6 event), and

\[
\boxed{
\|[T_{\log2}^*,T_{\log3}]\|=1.
}
\]

Explicitly, with \(\delta=L-\log3\),

\[
[T_{\log2}^*,T_{\log3}]f(x)
=
\bigl(\mathbf1_{\log(3/2)<x<L-\log2}
-\mathbf1_{\log3<x<L}\bigr)
f(x-\log(3/2)).
\]

Both output strips have length \(\delta\).

This is an **infinite-rank, nonfactorized boundary interaction** produced by two authentic prime channels before their product integer is visible. It should not be mistaken for a forbidden new connected von-Mangoldt impulse at n=6.

## Interpretation and proposed test

The Dirichlet-logarithm/connected-source condition must keep \(b(6)=0\) for genuine Euler products. Yet the finite-window SUCC/FUCC boundary geometry *must* allow interactions between its 2 and 3 channels.

A global Hecke--Tate polarization should therefore obey both:

1. **primitive-source condition:** no independent \(6\)-impulse in the logarithmic derivative;
2. **precomposite boundary condition:** recognize the nonzero oriented \(2\)--\(3\) commutator from the shared finite window.

A construction that has no cross-place boundary interaction is likely too factorized. A construction that treats the interaction as an inserted \(\log6\) impulse violates Euler connectedness.

However, the raw boundary commutator is not positive: the companion note proves its chiral spectrum is symmetric about zero. The present result is a new exact **interface diagnostic**, not a positive completed Weil pairing.

## Next finite benchmark

Choose \(L=1.2\) (so \(A=0.6\) for the centered window). Compute the \(2\)--\(3\) mixed boundary response in the actual theta/Hecke-induced coupling, then compare its complete polarized contribution with the completed Weil form, including the Archimedean and bulk debit. Falsify any proposal that simply inserts a fake \(n=6\) source.

**No RH conclusion.**
