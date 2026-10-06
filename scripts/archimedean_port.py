#!/usr/bin/env python3
"""Round006 ckpt7: structure of the Archimedean source port A_inf(s).

A_inf(s) = 1/s + 1/(s-1) - (1/2)log pi + (1/2) psi(s/2),   xi'/xi = A_inf - sum_p m_p  (Re s>1).

Established here:
  (1) xi'/xi = A_inf + zeta'/zeta  (numerically, Re s>1);
  (2) xi'/xi is REGULAR at s=1 (A_inf's +1/(s-1) pole cancels zeta'/zeta's -1/(s-1));
  (3) A_inf is REGULAR at s=0 too: the explicit 1/s cancels the -1/s of (1/2)psi(s/2)
      (psi(z) ~ -1/z near 0);
  (4) (1/2)psi(s/2) = const + sum_{n>=0}[1/(2n+2) - 1/(2n+s)]: a PASSIVE resolvent channel whose
      poles sit at the TRIVIAL zeros s=0,-2,-4,... all with Re<=0 < 1/2 (outside H_{1/2});
  (5) the ONLY pole of A_inf inside H_{1/2} is the SINGLE pole at s=1 (the 1/(s-1) term);
  (6) the finite truncation F_P = A_inf - sum_{p<=P} m_p has a genuine pole at s=1 (residue 1) for
      EVERY finite P, because the finite prime sum has no s=1 pole -- it emerges only as P->infty.

=> The whole indefinite/non-holomorphic obstruction in H_{1/2} is concentrated in ONE pole at s=1
   (one negative square, kappa=1). The Gamma channel is genuinely passive. RH open.
"""
import numpy as np
from mpmath import mp, zeta, digamma, loggamma, diff, log as mlog, mpc, mpf, pi, euler
mp.dps = 30


def A_inf(s):
    return 1 / s + 1 / (s - 1) - mlog(pi) / 2 + digamma(s / 2) / 2


def xi_log_deriv(s):
    # xi'/xi via d/ds log xi, xi = 1/2 s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)
    def logxi(z):
        return (mlog(mpf(1) / 2) + mlog(z) + mlog(z - 1) - z * mlog(pi) / 2
                + loggamma(z / 2) + mlog(zeta(z)))
    return diff(logxi, s)


def zeta_log_deriv(s):
    return diff(lambda z: mlog(zeta(z)), s)


print("(1) xi'/xi = A_inf + zeta'/zeta  (Re s>1):")
for s in [mpc(2, 1), mpc(1.5, 3), mpc(3, 0)]:
    lhs = xi_log_deriv(s)
    rhs = A_inf(s) + zeta_log_deriv(s)
    print(f"    s={complex(s)}: xi'/xi={complex(lhs): .6f}  A_inf+zeta'/zeta={complex(rhs): .6f}  "
          f"err={float(abs(lhs-rhs)):.1e}")

print("\n(2) xi'/xi regular at s=1 (pole cancellation):")
for eps in (0.1, 0.01, 0.001):
    v = xi_log_deriv(mpc(1 + eps, 0))
    print(f"    xi'/xi(1+{eps}) = {complex(v): .6f}   (finite, -> xi'/xi(1))")
print(f"    A_inf alone near 1: A_inf(1.001)={complex(A_inf(mpc(1.001,0))): .3f} (blows up: +1/(s-1) pole)")

print("\n(3) A_inf regular at s=0 (1/s cancels -1/s from psi/2):")
for eps in (0.1, 0.01):
    v = A_inf(mpc(eps, 0))
    print(f"    A_inf({eps}) = {complex(v): .6f}   (finite => s=0 pole cancels)")

print("\n(4) (1/2)psi(s/2) = C0 + sum_{n>=0}[1/(2n+2) - 1/(2n+s)], poles at s=0,-2,-4,... (Re<=0):")
for s in [mpc(0.6, 1.0), mpc(2.0, 0.5)]:
    C0 = -euler / 2
    partial = C0 + sum(mpf(1) / (2 * n + 2) - 1 / (2 * n + s) for n in range(20000))
    direct = digamma(s / 2) / 2
    print(f"    s={complex(s)}: series={complex(partial): .6f}  (1/2)psi(s/2)={complex(direct): .6f}  "
          f"err={float(abs(partial-direct)):.1e}")
print("    => Gamma channel poles all at Re<=0, OUTSIDE H_{1/2}: a genuinely passive resolvent channel.")

print("\n(5)+(6) finite truncation F_P = A_inf - sum_{p<=P} m_p has a pole at s=1 for every finite P:")
from sympy import primerange


def m_sum(s, P):
    return sum(mlog(p) / (mpf(int(p)) ** s - 1) for p in primerange(2, P + 1))


for P in (50, 500):
    for eps in (0.1, 0.01):
        FP = A_inf(mpc(1 + eps, 0)) - m_sum(mpc(1 + eps, 0), P)
        print(f"    P={P:4d}: F_P(1+{eps}) = {complex(FP): .4f}  "
              f"(~ +1/(s-1)={1/eps:.1f}: finite-P pole at s=1 INSIDE H_1/2)")
print("    xi'/xi(1+eps) stays finite (pole emerges only as P->infty). The finite completion MUST")
print("    cancel this s=1 pole with a cutoff-dependent boundary A_{inf,P}.")

print("""
VERDICT (ckpt7): the Archimedean port splits as A_inf = [passive Gamma channel: poles at trivial
zeros, all Re<=0, outside H_{1/2}] + [indefinite pole part 1/s+1/(s-1), whose ONLY H_{1/2} pole is the
SINGLE pole at s=1]. The entire non-holomorphic/indefinite obstruction in H_{1/2} is ONE pole at s=1
(one negative square, kappa=1). At finite cutoff the prime sum cannot cancel it; only the P->infty limit
does. RH open.
""")
