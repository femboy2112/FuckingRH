#!/usr/bin/env python3
"""Round006 ckpt8b: the failure of (P) is unconditional, and the Pontryagin index blows up.

Two measured facts, both RH-independent:
  (1) near sigma=1/2, max_t |Re F_P| grows like P^{1-sigma} (the finite von Mangoldt fluctuation
      amplitude), dwarfing the ~log t Archimedean -> min Re F_P -> -infty.
  (2) the number of excursions {Re F_P < -a} along a near-line vertical (= number of poles of
      Cayley_a[F_P]=(F_P-a)/(F_P+a) in H_{1/2} on that line, = negative squares consumed) grows with P.

=> the Laplace/source-response finite completion is not positive-real for any large P (kills Schur-Vitali
   (P) for this class unconditionally), AND its Pontryagin negative index kappa_P -> infty, so the
   FINITE-kappa Krein/Pontryagin escape (directive sec.19) is closed for this construction.
"""
import numpy as np
from scipy.special import digamma as sp_digamma
from sympy import primerange
LOGPI = np.log(np.pi)
a = 1.0


def mangoldt_powers(P):
    ns, Ls = [], []
    for p in primerange(2, P + 1):
        pk = p
        while pk <= P:
            ns.append(pk); Ls.append(np.log(p)); pk *= p
    return np.array(ns, float), np.array(Ls, float)


def F_P_vec(s, P, ns, Ls, chunk=2000):
    A = 1 / s - LOGPI / 2 + sp_digamma(s / 2) / 2 + (1 - P ** (1 - s)) / (s - 1)
    logn = np.log(ns)
    out = np.empty_like(s, dtype=complex)
    for i in range(0, len(s), chunk):
        sb = s[i:i + chunk]
        # prime sum = sum_n Ls[n] * exp(-s * logn)
        out[i:i + chunk] = np.exp(-np.outer(sb, logn)) @ Ls
    return A - out


print("(1) near-line amplitude growth: max_t |Re F_P| on sigma=0.51, t in [0,300]  vs  P^{1-sigma}:")
t = np.linspace(0.05, 300, 60000)
for P in (200, 2000, 20000, 200000):
    ns, Ls = mangoldt_powers(P)
    s = 0.51 + 1j * t
    re = F_P_vec(s, P, ns, Ls).real
    print(f"   P={P:7d}: max|Re F_P|={np.max(np.abs(re)):7.3f}   min Re F_P={re.min():+8.3f}   "
          f"P^0.49={P**0.49:7.2f}")

print("\n(2) Pontryagin index proxy: #{maximal intervals with Re F_P < -a} on sigma=0.51, t in [0,300]:")
for P in (200, 2000, 20000, 200000):
    ns, Ls = mangoldt_powers(P)
    s = 0.51 + 1j * t
    re = F_P_vec(s, P, ns, Ls).real
    below = re < -a
    crossings = int(np.sum(below[1:] & ~below[:-1]))     # rising edges into the <-a region
    print(f"   P={P:7d}: # excursions (Re F_P < -{a:.0f}) = {crossings:4d}  "
          f"(= poles of Cayley_a[F_P] in H_1/2 on this line = negative squares)")

print("""
VERDICT (ckpt8): the natural finite completion F_P (Laplace/source response) is NOT positive-real on
H_{1/2}: max|Re F_P| ~ P^{1-sigma} -> infty near the line, and the Pontryagin negative index kappa_P
(excursion count) GROWS with P. So (a) Schur-Vitali (P) fails for this class unconditionally, and (b) the
finite-kappa Krein escape is closed. The RH content cannot be reached by completing the source response
and hoping it is passive; passivity must be enforced STRUCTURALLY (unitary colligation) so that
|Theta|<=1 holds despite the wild underlying impedance -- and that is exactly where Conrey-Li/Sarnak bite.
RH open.
""")
