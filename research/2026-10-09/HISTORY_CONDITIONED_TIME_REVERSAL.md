# History-conditioned time reversal: the shattered-teacup test

**2026-10-09. Status:** unconditional structural lemmas, a zero-free inverse/retrodiction construction, an exact two-prime rational-echo computation, and an explicit fourth-gate frontier. **RH OPEN.** Built on main after Round 062, including its correction that three source-fidelity gates are necessary but **not sufficient** for RH.

## 0. Hypothesis and non-cheating distinction

The user's analogy: dynamically reverse the shattering of a teacup while reconstructing the correlations carried away by fragments, air, floor, photons, and the full environment. A reversal of the visible scalar cup coordinate is NOT reversal of its physical history.

This leads to **three mathematically different operations**:

1. **Microscopic inverse:** if a complete flow \(U\) is invertible/unitary on cup plus environment, then \(U^{-1}=U^*\) (in the unitary case), with appropriate physical time-reversal conjugation \(\Theta\) and reversal of fields/momenta for an actual time-reversed experiment.
2. **Shadow inversion:** for a projection/observation \(\pi:X_{\rm full}\to Y\), \(\pi U^{-1}\) generally does not factor through \(Y\). The final shadow has no unique antecedent.
3. **Bayesian retrodiction:** once a reference probability/measure on complete histories has been specified, the reverse transition is a **conditional probability**, not the naive transpose or inverse of the projected transition.

The key proposition is elementary but load-bearing for the language:

> The environment carries the complementary correlations. A projected backward adjoint is a *recovery channel* at best, not a two-sided inverse unless a reversibility/sufficiency condition is proved.

## 1. The full path involution

For a complete reversible microscopic evolution \(x_{j+1}=U_j x_j\), the forward trajectory is \((x_0,\dots,x_N)\), with \(U_{N:0}=U_{N-1}\cdots U_0\).

The actual inverse sequence is

\[
U_{N:0}^{-1}=U_0^{-1}\cdots U_{N-1}^{-1},
\]

NOT \(U_{N-1}^{-1}\cdots U_0^{-1}\). The individual inverse operators act in **reversed chronological order**.

For an appropriate physical time-reversal involution \(\Theta\), the reversed path is

\[
\boxed{\mathcal R(x_0,\ldots,x_N)=(\Theta x_N,\ldots,\Theta x_0).}
\]

It is meaningful only on the complete state, including environment/interaction channels.

For a coarse observation \(\pi(x_j)\), most of the information required by \(\mathcal R\) may have already moved into the kernel of the observation.

This is a rigorous groupoid/path-space version of inverse shadow-SUCC.

## 2. Exact causal \(p\)-ary refinement and half-density

At a prime-power event \(p^k\), the normalized Haar LCM clock adds one \(p\)-digit.

Write the old Hilbert space as \(H\) and the new space as \(H\otimes\mathbb C^p\). The canonical uniform refinement isometry is

\[
\boxed{
J_p f=f\otimes u_p,
\qquad
u_p=\frac1{\sqrt p}\sum_{j=0}^{p-1}|j\rangle.
}
\]

This is exactly the half-density normalization: \(J_p^*J_p=I\).

For an arbitrary new state \(\eta\in H\otimes\mathbb C^p\),

\[
\boxed{
J_p^*\eta=\frac1{\sqrt p}\sum_{j=0}^{p-1}\eta_j.
}
\]

Hence

\[
J_pJ_p^*
\]

is the orthogonal projector onto the uniform coherent child subspace. In general \(J_pJ_p^*\ne I\). The lost orthogonal sector \(u_p^\perp\) is precisely the **new-detail/environment channel**.

For \(\eta=f\otimes\frac1{\sqrt p}\sum_j e^{i\theta_j}|j\rangle\), with \(\|f\|=1\), the recovered amplitude is

\[
\boxed{
J_p^*\eta=\left(\frac1p\sum_{j=0}^{p-1}e^{i\theta_j}\right)f.
}
\]

The recovery probability is

\[
\boxed{
\|J_p^*\eta\|^2
=\left|\frac1p\sum_je^{i\theta_j}\right|^2\le1.
}
\]

Equality iff the child phases align. At \(p=2\), opposite phases \((0,\pi)\) yield zero recovery. A uniformly phased state recovers perfectly.

**Interpretation:** inverse SUCC is coherent reassembly, not flipping a sign or a label. If the environment detail channels are retained, a full unitary dilation can reverse the event exactly; after discarding them, the projected adjoint cannot.

**No RH inference:** the same isometry/recovery statement holds for any artificial branching schedule. The arithmetic source and completed Weil identity are separate conditions.

## 3. General Bayesian time reversal selects an actual dagger

Let \(P_t(y|x)\) be a finite-state forward Markov transition and let \(\mu_t(x)>0\) be its reference distribution. Set

\[
\mu_{t+1}(y)=\sum_xP_t(y|x)\mu_t(x).
\]

The *reverse* conditional probability is

\[
\boxed{
P_t^{\rm rev}(x|y)=
\frac{\mu_t(x)P_t(y|x)}{\mu_{t+1}(y)}.
}
\]

This depends on the forward measure and is generally NOT \(P_t^T\) and NOT \(P_t^{-1}\).

With \(D_{\mu}\) the diagonal mass matrix, let \(P_t\) act on probability columns and define the half-density representation

\[
\boxed{
K_t=D_{\mu_{t+1}}^{-1/2}P_tD_{\mu_t}^{1/2}.
}
\]

Then the half-density representation of the Bayes reverse is exactly

\[
\boxed{
D_{\mu_t}^{-1/2}P_t^{\rm rev}D_{\mu_{t+1}}^{1/2}=K_t^*.
}
\]

Thus, **once the full path measure is independently fixed**, its *weighted* reverse genuinely becomes the Hilbert adjoint in half-density coordinates.

For uniform \(p\)-ary refinement, \(P((x,j)|x)=1/p\), with \(\mu_{t+1}(x,j)=\mu_t(x)/p\), the matrix \(K_t\) is \(J_p\) and has \(1/\sqrt p\) entries.

But even a canonical Bayes inverse is still a retrodictive channel; the full mechanical inverse requires the omitted environmental degrees of freedom.

The reference measure must come from actual SUCC/FUCC Haar/Hecke/Gamma data; choosing it to produce Weil positivity is circular.

## 4. The exact two-prime reverse/forward echo

Let \(H_L=L^2(0,L)\) and \(T_h\) be right translation by \(h>0\), with zero extension and compression:

\[
(T_hf)(x)=1_{h<x<L}f(x-h).
\]

Its adjoint is

\[
(T_h^*f)(x)=1_{0<x<L-h}f(x+h).
\]

Thus

\[
\boxed{
T_h^*T_h=M_{1_{(0,L-h)}}\ne I.
}
\]

The missing strip \((L-h,L)\) is exactly the information that leaves the visible finite-horizon window. This is an operational model of scattering into the environment.

For \(0<a<b<L<a+b\),

\[
T_aT_b=T_{a+b}=0,
\]

but

\[
\boxed{
(T_a^*T_bf)(x)
=1_{b-a<x<L-a}f(x+a-b)\ne0.
}
\]

And

\[
(T_bT_a^*f)(x)
=1_{b<x<L}f(x+a-b).
\]

The output and input strips of these two partial isometries are pairwise disjoint, each with length \(L-b\). Hence

\[
\boxed{
\|[T_a^*,T_b]\|=1.
}
\]

For the authentic prime events

\[
a=\log2,\quad b=\log3,\quad \log3<L<\log4,
\]

the composite *forward* event \(T_{\log6}\) is invisible/zero, but the mixed reverse/forward echo survives:

\[
\boxed{
T_{\log2}^*T_{\log3}\ne0,\qquad
[T_{\log2}^*,T_{\log3}]\ne0.
}
\]

Its internal translation is

\[
\boxed{
b-a=\log(3/2).
}
\]

**This is inverse FUCC generating a rational fractional-SUCC history.** The interaction is a ratio/echo path, *not* a new connected primitive impulse at integer \(6\). It is exactly compatible with the source-fidelity discriminator \(b(6)=0\) for Euler products.

The repository's Round 061/062 already proved this commutator norm-one seam; this note supplies the time-reversal/recovery interpretation and does not claim priority.

## 5. For complex Hecke characters, reversal changes the dual sector

A primitive Dirichlet character phase must reverse as

\[
\chi(p)^k\longmapsto \overline{\chi(p)^k}
\]

in a conjugate-dual channel. The completed functional equation pairs \(\chi\) with \(\bar\chi\):

\[
\Lambda(s,\chi)=\varepsilon_\chi\Lambda(1-s,\bar\chi).
\]

This is **not literally mechanical time reversal**; it is an arithmetic Fourier/Mellin duality that exhibits the same need to swap input/output orientation and conjugate the phases. The Gamma factor and conductor/parity are part of that duality, not optional background.

For zeta (real trivial character) this conjugation is invisible; for a complex quartic character it is essential. Davenport--Heilbronn mixtures can obey a functional equation despite failing connected Euler multiplicativity, so any proposed reverse dynamics must still pass the source-fidelity tests.

## 6. The full-history recovery candidate and the fourth gate

The existing Round007 square has positive local prime/Gamma edge energies, but

\[
Q_W(f)=E_\Gamma(f)+E_{\rm prime}(f)+2|C(f)|^2-2|S(f)|^2-d_A\|f\|^2.
\]

The natural adjoint reverses translations, but independent edge squares charge the *unavoidable* \(2\sum w_n\|f\|^2\) diagonal tax. This is the proved bulk obstruction.

The "teacup" suggests a precise new **research proposal**:

> Build a globally correlated two-sided arithmetic history Hilbert space, with incoming/outgoing prime rays and a genuinely infinite-dimensional Archimedean environment. Derive the time-reflected conditional/recovery operator from a canonical Haar/Tate/Poisson path state **before** evaluating the Weil form.

One natural mathematical structure for eliminating an environment is a *Schur complement*:

\[
\boxed{
\mathsf G=
\begin{pmatrix}
A&B\\
B^*&C
\end{pmatrix}\succeq0,\quad C>0
\quad\Longrightarrow\quad
A-BC^{-1}B^*\succeq0.
}
\]

The **negative self-energy** comes from coherent environmental feedback and is not inserted as a separate negative scalar by fiat.

However, the choice \(A=P_A,C=I,B=D_A^{1/2}\) is **circular**: then the Schur complement is simply \(Q_W=P_A-D_A\), with positivity of \(\mathsf G\) *equivalent* to RH. This construction is not a proof. The environmental coupling \(B\) and its positive joint covariance must be derived independently from the true global prime/Gamma state and must then agree with the complete Weil form.

The Round007 no-go forces any successful environmental coupling to be **infinite rank/continuum-capable**, not merely finite boundary ports. The raw chiral curvature \([C^*,C]\) cannot be the positive parent because its spectrum is sign-symmetric (Round 062).

## 7. What was already reversed in Weil

The Weil test uses

\[
\widetilde f(t)=\overline{f(-t)},\qquad
Q_W(f)=W(f*\widetilde f).
\]

Thus *test-function involution* is already present. It would be an error to claim RH has remained open merely because nobody flipped \(t\mapsto-t\).

What is **not yet derived** is a positive Hilbert/GNS inner product on completed history states, from genuine arithmetic dynamics alone, whose boundary Gram is \(Q_W\).

**The fourth gate remains:** exact identification with the entire completed Weil form PLUS an independently established sign. The first three gates (multiplicativity/no zeros/mutation fidelity) are necessary and insufficient.

## 8. Honest next experiment

Use the small nontrivial window \(\log3<L<\log4\).

1. Keep only authentic connected arithmetic impulses at 2 and 3; the source has no independent 6 impulse.
2. Retain both forward and reverse chiral boundary channels; verify the exact \(\log(3/2)\) ratio echo and norm-one commutator.
3. Couple these to the **untruncated** Gamma environment using the canonical Gaussian/Poisson state, not guessed phases or fitted metrics.
4. Derive the induced two-sided reflection/conditional-recovery pairing and compare its **polarized** quadratic form on a declared common core to the completed Weil form.
5. Compute the full residual, including the negative bulk debit and pole cross term. Test fake 6, nonunit alpha2, shifted log2, and the Davenport--Heilbronn mixture.
6. If positivity survives mutants or the Weil residual is nonzero, retire that candidate. If the identification succeeds, the independent sign is still the genuine RH-hard lemma.

### Conclusion

**True reversal is of the entire interacting history, not of the visible SUCC value.** The missing data live in complementary environment/detail channels; the weighted dagger is selected by a canonical measure; inverse/forward mixed paths generate rational log ratios before composite integer events. These are rigorous, zero-free structural ingredients, **not yet the Hodge/Weil positive polarization**.
