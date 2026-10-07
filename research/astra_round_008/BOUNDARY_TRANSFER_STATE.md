# Small state: a true scalar closure, and a false Möbius identification

Fix `z` off the clock spectrum and put

\[
 g_L(z)=\langle L-1|(zI-C_L)^{-1}|0\rangle=\frac1{z^L-1}.
\]

Indeed `(zI-C_L)^(-1)=sum_(r=0)^(L-1) z^(L-1-r) C_L^r/(z^L-1)`.
Every resolvent entry is `z^(L-1-r)g_L`, with `r=a-b mod L`. Thus the
integer `L`, `z`, and this scalar determine the full clock resolvent; they
do not store an arbitrary vector or an arbitrary continuum input.

**Fixed clock, one twist.** Sherman–Morrison is an exact algebraic identity:

\[
 R_\omega=R+\frac{\omega-1}{1-(\omega-1)g_L}
 R|0\rangle\langle L-1|R,\qquad
 g\mapsto\frac{g}{1-(\omega-1)g}.                            \tag{BT1}
\]

This is Möbius and is represented by `[[1,0],[-(omega-1),1]]`.
It gives `g_(L,omega)=1/(z^L-omega)`. It is not the map that replaces the
clock by all `p` twisted blocks.

**Full refinement.** Eliminating `z^L=1+1/g` gives the exact scalar closure

\[
 g_{pL}=R_p(g_L),\qquad
 R_p(g)=\frac{g^p}{(g+1)^p-g^p}.                              \tag{BT2}
\]

For `p>1`, numerator and denominator are coprime of degrees `p` and `p-1`.
The rational map has degree `p`, so it is not Möbius, including after any
global rational invertible change of coordinate. Under the coordinate
`q=1+1/g` it is `q -> q^p`. Equations are meromorphic on the sphere:
`g=0` is removable and maps to zero; `g=infinity` maps to infinity. Poles
must be handled by these extensions rather than dividing numerical infinities.

There is nevertheless a **small nonlinear state**, and even a simple local
logarithmic state: choose a branch of `Log z`, put `u=L Log z`, evolve
`u -> p u`, and read out `g=1/(exp(u)-1)`. This is not a global Möbius
realization, but it refutes a universal claim that state dimension must grow.
The integer `L` itself is another one-register description with unbounded
information content. A compact formula is different from a fixed finite
autonomous linear input/output system.

Derivatives also close when `L` and `z` are retained:

\[
 \partial_zg_L=-\frac Lz g_L(g_L+1),\qquad
 \partial_z\log(z^L-1)=\frac Lz(1+g_L).                        \tag{BT3}
\]

Logarithms of determinants require a zero-free domain and a basepoint;
their logarithmic derivatives have the displayed meromorphic meaning.

**Sharp finite-linear scope.** An autonomous `d`-state resolvent
`c*(zI-A)^(-1)b` has at most `d` poles with multiplicity. Since `g_L` has
`L` distinct simple poles, `d>=L`, attained by the clock realization.
Likewise no finite-dimensional space of rational functions containing `q`
is invariant under substitution `q -> q²`: it would contain the linearly
independent powers `q^(2^j)`. These exclude specified linear realizations,
not finite transfer matrices along a growing chain, nonlinear state updates,
or time-dependent systems. Gamma has its separate finite-LTI obstruction
and explicit time-varying escape in `GAMMA_DRIFT.md`.

Thus the user's small-state intuition is partly correct at the scalar clock
level. What it has not supplied is a closed sufficient state for the full
prime/Gamma **pairing**. That is a different input/output problem.
