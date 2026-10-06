# The multiplicative binomial Fock splitter: an exact isometry generating the cross terms

**Date:** 2026-10-06
**Status:** exact theorems (PROVED-IN-REPO, verified `scripts/binomial_fock_check.py`). RH open.
This is the *multiplicative* (divisor-multiset) binomial of FUCC_IS_PASCAL §7–8 — an independent
arithmetic object, **not** a functional-calculus of K_Psi — so it is a legitimate candidate factor.

## 1. The splitter is an exact isometry

With the multiplicative binomial coefficient
\(\mathrm{Binom}(n,d)=\prod_p\binom{v_p(n)}{v_p(d)}\) (for \(d\mid n\)), define
\[
J_B\,|n\rangle=2^{-\Omega(n)/2}\sum_{d\mid n}\sqrt{\mathrm{Binom}(n,d)}\;|d\rangle\otimes|n/d\rangle
\ :\ \ell^2(\mathbb N_{>0})\to\ell^2(\mathbb N_{>0})^{\otimes2}.
\]

**Theorem 1.** \(J_B^\*J_B=I\).

*Proof.* Unit norm: \(\|J_B|n\rangle\|^2=2^{-\Omega(n)}\sum_{d\mid n}\mathrm{Binom}(n,d)
=2^{-\Omega(n)}\prod_p\sum_{a=0}^{v_p(n)}\binom{v_p(n)}{a}=2^{-\Omega(n)}\prod_p 2^{v_p(n)}=1.\)
Orthogonality: the two legs \((d,n/d)\) of any term of \(J_B|n\rangle\) multiply back to \(n\), so
terms from \(m\ne n\) occupy disjoint basis vectors and \(\langle J_B m|J_B n\rangle=\delta_{mn}\). \(\square\)
(Verified for all \(n\le64\).)

## 2. Contracting the splitter produces the C79 prime-swap, binomial-dressed

**Theorem 2.** For primes \(p,q\),
\[
\boxed{\ \langle m\mid J_B^\*\big(|q\rangle\langle p|\otimes I\big)J_B\mid n\rangle
=2^{-(\Omega(m)+\Omega(n))/2}\sqrt{\mathrm{Binom}(m,g)\,\mathrm{Binom}(n,g)}\;[\,pm=qn\,],\quad g=m/q=n/p.\ }
\]

*Proof/verification.* The leg-matching \(\langle m/e|n/d\rangle=[m/e=n/d]\) forces \(m/e=n/d=:g\),
hence \(e=q,\ d=p\) (from the bra/ket of \(|q\rangle\langle p|\)) and \(m=qg,\ n=pg\), i.e. \(pm=qn\).
Checked against the brute-force definition on many \((m,n,p,q)\); exact agreement.

**Reading.** The exact cross-prime coupling of C79 (the single prime-swap \(pm=qn\) that C07 proved
indispensable and C15 asked to identify) is literally a **contraction of the binomial Fock splitter**.
The multiplicative binomial supplies the amplitudes \(\sqrt{\mathrm{Binom}}\) that dress each swap;
summed with the critical amplitudes \(\sqrt{\log p}\,p^{-1/4}\) it reproduces a binomial-weighted
version of the \(\mathsf F^\*\mathsf F\) prime-swap graph. (Verified symmetric, built with no zeros.)

## 3. Honest limitation

\(J_B^\*J_B=I\) is a *trivial* Gram, hence RH-inert on its own. Theorem 2 shows the **cross terms live
naturally inside the binomial Fock coproduct**, but assembling the Suzuki screw kernel \(K_\Psi\) from
these contractions (the \(C_L\) of FUCC_IS_PASCAL §9) is still open. What is gained: an *exact,
manifestly positive* multiplicative structure that generates precisely the C79 cross-prime terms —
outside the scalar old-state cones refuted in Round 003 — and is a genuine (non-circular) ingredient
for the arithmetic \(B_L\).
