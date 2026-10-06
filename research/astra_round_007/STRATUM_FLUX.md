# Exact support-stratum carrier currents

Status: proved identities on the full Hilbert space. The arithmetic pattern of
consecutive prime powers is retained rather than replaced by a density model.

Write \(\omega(n)=|\operatorname{supp}\nu(n)|\), including \(\omega(1)=0\),
and \(\chi_r(n)=1_{\omega(n)=r}\). The orthogonal strata satisfy
\(\sum_{r\ge0}P_r=I\) strongly. Define
\(E_{s,r}=P_s\Sigma P_r\). Then
\[
E_{s,r}\delta_{\nu(n)}
=1_{\omega(n)=r,\;\omega(n+1)=s}\delta_{\nu(n+1)}.
\]
Every \(E_{s,r}\) is a partial isometry; its initial projection is the
displayed indicator on \(n\), and its final projection the same indicator
shifted to \(n+1\). The sum over \((s,r)\) reconstructs \(\Sigma\) strongly.

For the commutator convention \([A,B]=AB-BA\),
\[
C_r=[\Sigma,P_r],\qquad
C_r\delta_{\nu(n)}=(\chi_r(n)-\chi_r(n+1))\delta_{\nu(n+1)},
\]
or, equivalently,
\[
C_r=(I-P_r)\Sigma P_r-P_r\Sigma(I-P_r).
\]
The first term is **exit** with positive orientation; the second is **entry**
with negative orientation. Motion within the stratum is \(P_r\Sigma P_r\)
and vanishes from the current. The two crossing terms have orthogonal initial
and final supports. Consequently
\[
C_r^*C_r\delta_{\nu(n)}
=1_{\chi_r(n)\ne\chi_r(n+1)}\delta_{\nu(n)}.
\]
Squaring loses whether the crossing entered or exited. The current is bounded
with norm at most one. This is a forced incidence square, but it is a
crossing indicator, not the von Mangoldt weight and not a completed Weil
energy.

## The prime-power stratum

For \(r=1\), the formula separates the following exact cases:

| Transition | Condition on carrier state \(n\) | Current coefficient |
|---|---|---:|
| Entry | \(n\) is not a prime power, \(n+1=q^\ell\) | \(-1\) |
| Exit | \(n=p^k\), \(n+1\) is not a prime power | \(+1\) |
| Internal | \(n=p^k,\ n+1=q^\ell\) | \(0\) |
| Exterior | Neither is a prime power | \(0\) |

Here all exponents are positive; \(1\) is not a prime power. Thus \(1\to2\)
is entry. In an internal transition \(p\ne q\) by coprimality, and exactly
one base is 2 because one of two consecutive integers is even. The exact
operator keeps the Diophantine condition \(q^\ell-p^k=1\); no unproved
classification of such pairs is needed or asserted.

Let \(R_p^+=\sum_{k\ge1}|\nu(p^k)\rangle\langle\nu(p^k)|\) project onto a
jet excluding its source. Then
\[
R_p^+\Sigma R_p^+=0,
\quad
R_q^+\Sigma R_p^+
=\sum_{q^\ell=p^k+1}|\ell e_q\rangle\langle k e_p|\quad(p\ne q).
\]
The first equality follows from \(p^{k+1}-p^k=(p-1)p^k\ge2\) for \(k\ge1\).
If the common origin is included, write
\(R_p=R_p^++|0\rangle\langle0|\). Now
\[
R_p\Sigma R_p=
\begin{cases}|e_2\rangle\langle0|,&p=2,\\0,&p>2.\end{cases}
\]
These source-inclusive jet projections overlap at the origin and must not be
summed as an orthogonal decomposition. In contrast \(P_1=\sum_pR_p^+\)
is an orthogonal strong sum.

This is the whole first-order prime-power current. A charge-weighted current
can subsequently be formed, but its squared diagonal will include crossing
indicators and shifted weights. It does not automatically become
\(Q_1e^{-H/2}\). Any proposed identification must pay for the missing
internal events such as \(2\to3\) and \(3\to4\).

The exact tests compare the formula with independently assembled matrix
commutators and check the entry/exit signs explicitly.
