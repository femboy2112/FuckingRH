# Prime-jet first-return maps and time cocycles

Status: exact induced dynamics. This is not a recurrence theorem or a new
Euler product.

## Return to a section, not return to a point

The deterministic carrier is \(T(n)=n+1\). For a prime \(p\), its section
\(J_p=\{p^k:k\ge0\}\) has a first forward return from every section point.
There is no other section point between \(p^k\) and \(p^{k+1}\), so
\[
\tau_p(p^k)=(p-1)p^k,\qquad T^{\tau_p(p^k)}(p^k)=p^{k+1}.
\]
The induced map is exactly multiplication by \(p\) on this section. The
corresponding Hilbert-space identity is
\[
V_p\delta_{p^k}=S^{(p-1)p^k}\delta_{p^k}.
\]
This is a state-dependent iteration, not the assertion \(V_p=S^c\) for a
fixed time \(c\). More generally,
\[
V_m=\sum_{n\ge1}S^{(m-1)n}|n\rangle\langle n|
\]
with strong convergence; the columns have distinct outputs and define an
isometry. For composite \(m\) this remains valid. Each section
\(\{r m^k:k\ge0\}\), \(m\nmid r\), has multiplication by \(m\) as its
first-return map, and these sections partition the positive integers.

For \(a,b\ge0\), define the elapsed carrier time of \(a\) induced steps by
\[
\tau_p(k,a)=p^{k+a}-p^k.
\]
Its exact additive cocycle is
\[
\tau_p(k,a+b)=\tau_p(k,a)+\tau_p(k+a,b).
\]
Under the clock \(h(n)=\log n\), the same elapsed time becomes
\(a\log p\). The linear spacing in log time is forced by multiplicativity;
the exponential spacing in carrier time is not removed, just reparametrized.

The carrier has no invariant probability measure on \(\mathbb N_{>0}\):
invariance gives mass zero to \(\{1\}\), then successively to every
singleton. The section map similarly has no invariant probability on its
one-way orbit. Poincare recurrence and measure-preserving suspension-flow
theorems therefore do not apply without additional structure. In particular,
the forward-return sections here are not periodic orbits.

## Latent log action and the exact observable

The strongly continuous unitary group \(U_t=e^{itH}\) exists before a
carrier cutoff is imposed and acts by
\[
U_t\delta_{ke_p}=e^{itk\log p}\delta_{ke_p}.
\]
The carrier samples the already-defined diagonal observables. Counting the
charged positive-depth section hits gives
\[
\mu_{\rm jet}=\sum_{p,k\ge1}\log p\,\delta_{k\log p}.
\]
For \(\Re s>1\), absolute convergence permits
\[
\int e^{-su}\,d\mu_{\rm jet}(u)
=\sum_{p,k\ge1}\log p\,p^{-ks}
=-\frac{\zeta'}{\zeta}(s).
\]
The final equality follows by differentiating the absolutely convergent
Euler-product logarithm. It is classical and requires precisely the prime
sections and their exact logarithmic weights. The same induced-return
construction on a selected family of composite geometric sections would
yield that family's corresponding series, not zeta.

At carrier horizon \(N\), section depth is exactly \(p^k\le N\). The
factor-test threshold \(p^2\le N\) is a different activation rule: a prime
\(p\le N<p^2\) already contributes its depth-one jet event but has not yet
become a trial-factor channel of the square-root cone. They should not be
silently identified or one of the two prime contributions will be lost.

The transfer/trace audit is recorded separately in `DYNAMICAL_ZETA_AUDIT.md`.
Nothing in the first-return theorem alone provides an invariant equilibrium
measure, periodic-orbit determinant, self-adjoint spectrum, or Archimedean
completion.

The controls search for the earliest section hit directly, then verify the
cocycle for independent step counts. Their role is to catch implementation
and indexing errors; the displayed argument proves all returns.
