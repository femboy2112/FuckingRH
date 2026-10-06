# Round006 theorem dependency DAG

**Date:** 2026-10-06. **RH open.** Nodes are claims; edges `A -> B` mean "A is used by / feeds B".
Status tags: [THM] proved theorem, [EXACT] exact identity, [NOGO] obstruction, [META] scope/logic.

```
CLASSICAL INTERFACE (literature-locked, LITERATURE_INTERFACE.md)
  Lagarias(1999)(1.5)/(1.19) [Hinkkanen]: RH <=> xi'/xi positive-real (Pick) on H_{1/2}
  Lagarias(1.4): Re xi'/xi>0 on Re s>1 (unconditional)
  Conrey-Li(2000)+Sarnak: de Branges space positivity FAILS for zeta; Re{xi(s)/xi(s+1)}<0 in strip
        |
        v
SOURCE LAYER [EXACT]                         ARCHIMEDEAN PORT [EXACT] (C105, ckpt7)
  C-ray incidence (ckpt3):                     A_inf = passive Gamma-channel (resolvent of D_Gamma=2N,
    E^*E=I, Lambda=incidence,                    poles at trivial zeros, outside H_{1/2})
    W_b|n>=Lambda n^{-b}|n>, B^*B=W               + pole part: ONLY H_{1/2} pole at s=1 (kappa=1)
  C-corr (ckpt4):                              xi'/xi = A_inf + zeta'/zeta ; xi'/xi(1) = -B = 0.023096
    J^* e^{itH} J = -zeta'/zeta(s-it)                |
    (positive-DEFINITE in t, NOT                     |
     positive-REAL in s)                             |
        |                                            |
        v                                            v
  C103 [NOGO] (ckpt5): m_p and sum_p m_p NOT positive-real on H_{1/2}
    (s|->p^s periodic; Cauchy-Herglotz-in-w and real-axis complete monotonicity do not transport).
    KILLS one-port / direct-sum class.
        |
        v
  C104 [THM] Schur-Vitali continuation (ckpt6): (P) contractive on H_{1/2} + (E) Euler-limit
             => xi'/xi positive-real on H_{1/2} => RH.  NON-CIRCULAR.  <-- the round's reduction
        |         (whole RH content compressed into hypothesis (P))
        v
  C106 [NOGO] (ckpt8): finite completion F_P = A_{inf,P} - sum_{p^k<=P} Lambda n^{-s}
    (Euler-Maclaurin boundary reg_P cancels the s=1 pole; F_P holomorphic, ->xi'/xi on Re s>1 = (E) ok)
    BUT NOT positive-real: max|Re F_P|~P^{1-sigma}->inf, kappa_P grows (108->362; finite-but-unbounded).
    KILLS Laplace/source-response completion class for (P); closes fixed-finite-kappa Krein escape (sec.19).
        |
        v
  OBSTRUCTION THEOREM (sec.18, PROOF_ATTEMPT_006): inf_{H_{1/2}} Re F_P -> -inf (Dirichlet simult.
    approx + PNT), unconditional. Escape requires a colligation Theta_X bounded BY CONSTRUCTION, not F_P.
        |
        v
  C107 [NOGO] (ckpt9): colligation needs positive-definite arithmetic state metric; every natural
    realization indefinite (Laplace-source index diverges; de Branges H(E) Conrey-Li failure,
    verified Re{xi(1+282i)/xi(2+282i)}=-0.000132).
        |
        v
  C108 [META/NOGO] (ckpt10): PARENT-INDEPENDENCE LEMMA. RH-positivity is a property of the FUNCTION xi
    (Re{xi(s)/xi(s+1)}=-0.161 at 0.55+110i). => history-before-quotient & all coupling orders are NOT
    unconditional escapes; (P)+(E) <=> RH from ANY parent.
        |
        v
  C109 [controls] (ckpt11): source corr=-zeta'/zeta and completion=xi'/xi are mutation-sensitive
    (every arithmetic mutation breaks them O(0.1-0.5)) => the no-go is about the GENUINE target.

SCOPE CORRECTIONS [META] (ckpt2): C100 (C98 was only shared-DC, not all algebraic renorm),
  C101 (carre = weighted/repaired local energy, not raw Lambda), C102 (birth-order kernel-invariance
  != parent-space irrelevance) -- these OPENED the doors C104/C106/C108 then walked through.
```

## One-line summary of the logic

`RH  <=>  xi'/xi positive-real on H_{1/2}  <=>  hypothesis (P) [a positive-definite arithmetic state
metric with Euler-limit Cayley[xi'/xi]]`. Round006 proved the reduction (C104) is clean and non-circular,
realized the Archimedean port (C105), and then killed every natural route to (P): the impedance/
Laplace-completion class (C106 + obstruction theorem, unconditional), the fixed-finite-`κ` Krein escape
(C106), and — via the parent-independence lemma (C108) — the colligation and history-before-quotient
escapes, all blocked by the **function-level** Conrey–Li/Sarnak obstruction (C107/C108). Surviving class:
a positivity structure orthogonal to the single-space de Branges condition and still arithmetically
forced — the actual open problem.
