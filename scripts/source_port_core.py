#!/usr/bin/env python3
"""Round006 core: source-ray incidence, event-weight factorization, source correlation.

Independent re-derivation (as finite matrices) of the Aletheia source-wired identities,
plus the operator-level checks Aletheia only did scalar-wise.

Spaces (truncated):
  H_add = span{|n>: 1<=n<=N}
  H_ray = span{|p,k>: p prime, k>=1, p^k<=N}
  E: H_ray -> H_add,  E|p,k> = |p^k>          (incidence isometry)
  Q|p,k> = (log p)|p,k>                         (primitive-generator charge)
  H|p,k> = (k log p)|p,k>                       (total log-energy/depth)
  W_beta = E Q exp(-beta H) E^*                 (event-weight operator on H_add)
  B_beta = Q^{1/2} exp(-beta H/2) E^*           (candidate factor H_add -> H_ray)
  J_sigma = sum sqrt(log p) p^{-k sigma/2} |p,k><Omega|,   Omega=|1>

Checks (all exact up to float/prime-tail):
  (I)   E^*E = I_ray                            (unique factorization)
  (II)  W_beta|n> = Lambda(n) n^{-beta}|n>      (diagonal event weight)
  (III) B_beta^*B_beta = W_beta                 (NON-circular factorization of the weight)
  (IV)  J_sigma^*J_sigma      = (-zeta'/zeta(sigma))     |Omega><Omega|
  (V)   J_sigma^* e^{itH} J_sigma = (-zeta'/zeta(sigma-it)) |Omega><Omega|

CAVEAT (made precise in SOURCE_CORRELATION_LOG_DERIVATIVE.md):
  (IV)-(V) are rank-1 AUTOCORRELATIONS / matrix elements <Omega|...|Omega>, NOT Weyl
  m-functions or driving-point impedances. -zeta'/zeta(sigma-it) is positive-DEFINITE in t
  (Bochner; weights Lambda(n)n^{-sigma}>0 on frequencies log n) but that is NOT the same as
  positive-REAL in s. The whole round is about bridging that gap.
"""
import numpy as np
from sympy import primerange, factorint, isprime
from mpmath import mp, zeta, diff, log as mlog, mpc
mp.dps = 30


def mangoldt(n):
    f = factorint(n)
    if len(f) == 1:
        return float(mlog(list(f)[0]))
    return 0.0


def build(N):
    rays = []
    for p in primerange(2, N + 1):
        pk, k = p, 1
        while pk <= N:
            rays.append((int(p), k, pk))
            pk *= p
            k += 1
    R = len(rays)
    logp = np.array([np.log(p) for (p, k, pk) in rays])
    depth = np.array([k for (p, k, pk) in rays], float)
    idx = {pk: j for j, (p, k, pk) in enumerate(rays)}          # p^k -> ray index
    # E: N x R ; column j is e_{p^k}
    E = np.zeros((N, R))
    for j, (p, k, pk) in enumerate(rays):
        E[pk - 1, j] = 1.0                                       # |n> indexed by n-1
    return rays, logp, depth, E


def neg_zeta_ratio(s):
    return complex(-diff(lambda z: mlog(zeta(z)), mpc(s.real, s.imag)))


if __name__ == "__main__":
    N = 400
    rays, logp, depth, E = build(N)
    R = len(rays)
    Q = np.diag(logp)
    Hdepth = np.diag(depth * logp)                               # H|p,k> = k log p

    # (I) incidence isometry
    EtE = E.T @ E
    print(f"(I)  ||E^*E - I_ray|| = {np.linalg.norm(EtE - np.eye(R)):.2e}   (R={R} rays, N={N})")

    # (II)+(III) for a few beta
    for beta in (0.5, 1.0, 2.0):
        expβH = np.diag(np.exp(-beta * depth * logp))
        W = E @ Q @ expβH @ E.T                                  # N x N
        # target diagonal: Lambda(n) n^{-beta}
        tgt = np.array([mangoldt(n) * n ** (-beta) for n in range(1, N + 1)])
        offdiag = np.linalg.norm(W - np.diag(np.diag(W)))
        diagerr = np.linalg.norm(np.diag(W) - tgt)
        # factor B_beta = Q^{1/2} exp(-beta H/2) E^*   (R x N)
        B = np.diag(np.sqrt(logp)) @ np.diag(np.exp(-beta * depth * logp / 2)) @ E.T
        facerr = np.linalg.norm(B.T @ B - W)
        print(f"(II) beta={beta}: W diagonal? offdiag={offdiag:.1e}; "
              f"||diag(W)-Lambda*n^-b||={diagerr:.1e}   (III) ||B^*B-W||={facerr:.1e}")

    # (IV)+(V) source correlation (sigma>1 so prime tail is small)
    print("\n(IV)/(V) source correlation  J^* e^{itH} J  (coeff of |Omega><Omega|):")
    for sigma, t in [(2.0, 0.0), (2.0, 1.3), (1.5, 2.0), (3.0, 5.0)]:
        c = np.sqrt(logp) * np.exp(-depth * logp * sigma / 2)    # amplitudes c_{p,k}
        phase = np.exp(1j * t * depth * logp)                    # e^{itH} on rays
        coeff = np.sum(np.abs(c) ** 2 * phase)                   # = sum log p p^{-k(sigma-it)}
        tgt = neg_zeta_ratio(complex(sigma, -t))                 # -zeta'/zeta(sigma - it)
        print(f"   sigma={sigma}, t={t}: J-coeff={coeff: .6f}   "
              f"-zeta'/zeta(sigma-it)={tgt: .6f}   err={abs(coeff - tgt):.2e}  "
              f"(Re={coeff.real:+.4f})")

    # positive-definiteness of -zeta'/zeta(sigma-it) in t (Bochner), as a function datum
    print("\n   Bochner datum: -zeta'/zeta(sigma-it) = sum_n Lambda(n) n^{-sigma} e^{i t log n},")
    print("   weights Lambda(n)n^-sigma > 0  => positive-DEFINITE in t (NOT positive-real in s).")
    print("\nRH remains open: this factors the event/source/correlation layer only.")
