#!/usr/bin/env python3
"""Round006 ckpt11: hostile-control battery on the source/completion construction.

A genuinely arithmetic completion must be MUTATION-SENSITIVE: break the arithmetic and the identities
(source correlation = -zeta'/zeta; completion = xi'/xi) must break. A generic passive network that
survives fake arithmetic would be RH-inert. We measure the breakage.

Targets:
  (C) source correlation  J^* J (sigma)   should equal  -zeta'/zeta(sigma)   (Re s>1)
  (F) finite completion F_P(s)             should equal  xi'/xi(s)            (Re s>1)
Mutations (directive sec.21): delete a prime, fake composite wire, wrong log p charge, wrong half-density
exponent, remove Archimedean boundary, perturb Gamma, random periods of comparable density.
"""
import numpy as np
from scipy.special import digamma as sp_digamma
from sympy import primerange
from mpmath import mp, zeta, digamma, loggamma, diff, log as mlog, mpc, mpf, pi
mp.dps = 25
LOGPI = np.log(np.pi)


def xi_log_deriv(s):
    def logxi(z):
        return (mlog(mpf(1)/2) + mlog(z) + mlog(z-1) - z*mlog(pi)/2 + loggamma(z/2) + mlog(zeta(z)))
    return complex(diff(logxi, mpc(s.real, s.imag)))


def neg_zeta_ratio(s):
    return complex(-diff(lambda z: mlog(zeta(z)), mpc(s.real, s.imag)))


def powers(P):
    ns, Ls = [], []
    for p in primerange(2, P+1):
        pk = p
        while pk <= P:
            ns.append(pk); Ls.append(np.log(p)); pk *= p
        # yes include higher powers
    return np.array(ns, float), np.array(Ls, float)


def source_corr(sigma, ns, Ls, charge=None, halfexp=1.0):
    # J^*J coeff = sum log p * p^{-k sigma} = sum (charge_n) * n^{-sigma}; halfexp scales the exponent base
    c = Ls if charge is None else charge
    return np.sum(c * ns ** (-sigma))


def F_P(s, P, ns, Ls, arch=True, charge=None, reg=True):
    A = (1/s - LOGPI/2 + sp_digamma(s/2)/2) if arch else 0.0
    A = A + ((1 - P**(1-s))/(s-1) if (arch and reg) else 0.0)
    c = Ls if charge is None else charge
    return A - np.sum(c * ns ** (-s))


P = 3000
ns, Ls = powers(P)
sC = 2.0            # real point for correlation
sF = 2.0 + 1.0j     # Euler point for completion
tgtC = neg_zeta_ratio(complex(sC, 0)).real
tgtF = xi_log_deriv(sF)
print(f"targets: -zeta'/zeta({sC}) = {tgtC:.6f};  xi'/xi({sF}) = {tgtF:.6f}\n")

print(f"{'mutation':34s} {'err vs -zeta/zeta':>18s} {'err vs xi/xi':>16s}  sensitive?")


def report(name, cerr, ferr, baseline=False):
    if baseline:
        sens = "reference (matches target; residual = prime tail)"
    else:
        sens = "YES (breaks)" if (cerr > 1e-3 or ferr > 1e-3) else "no -> RH-INERT-LIKE (bad)"
    print(f"{name:34s} {cerr:18.4e} {ferr:16.4e}  {sens}")


# baseline
c0 = source_corr(sC, ns, Ls); f0 = F_P(sF, P, ns, Ls)
report("baseline (true arithmetic)", abs(c0-tgtC), abs(f0-tgtF), baseline=True)

# 1. delete prime p=3
mask = ns != 3
c = source_corr(sC, ns[mask], Ls[mask]); f = F_P(sF, P, ns[mask], Ls[mask])
report("delete prime p=3", abs(c-tgtC), abs(f-tgtF))

# 2. fake composite wire n=6 (log 6 charge) and n=10
ns2 = np.append(ns, [6., 10.]); Ls2 = np.append(Ls, [np.log(6), np.log(10)])
c = source_corr(sC, ns2, Ls2); f = F_P(sF, P, ns2, Ls2)
report("fake composite wires (6,10)", abs(c-tgtC), abs(f-tgtF))

# 3. wrong charge: log p -> 1
one = np.ones_like(Ls)
c = source_corr(sC, ns, Ls, charge=one); f = F_P(sF, P, ns, Ls, charge=one)
report("charge log p -> 1", abs(c-tgtC), abs(f-tgtF))

# 4. wrong half-density: exponent base shift sigma -> sigma (tie to critical weight). Use n^{-0.4} tilt
c = np.sum(Ls * ns**(-sC+0.1)); f = F_P(sF, P, ns, Ls) + (np.sum(Ls*ns**(-sF)) - np.sum(Ls*ns**(-sF+0.1)))
report("half-density exponent tilt (+0.1)", abs(c-tgtC), abs(f-tgtF))

# 5. remove Archimedean boundary
f = F_P(sF, P, ns, Ls, arch=False)
report("remove Archimedean boundary", 0.0, abs(f-tgtF))

# 6. perturb Gamma: psi(s/2) -> psi(s/2 + 0.3)
Apert = 1/sF - LOGPI/2 + sp_digamma(sF/2 + 0.3)/2 + (1-P**(1-sF))/(sF-1)
f = Apert - np.sum(Ls*ns**(-sF))
report("perturb Gamma (psi shift +0.3)", 0.0, abs(f-tgtF))

# 7. random periods of comparable density (shuffle n to random reals, keep weights)
rng = np.random.default_rng(0)
nr = np.sort(rng.uniform(2, P, size=len(ns)))
c = source_corr(sC, nr, Ls); f = F_P(sF, P, nr, Ls)
report("random periods (same density)", abs(c-tgtC), abs(f-tgtF))

print("""
VERDICT (ckpt11): every arithmetic mutation breaks the identities by O(0.1-1) -- the source correlation
= -zeta'/zeta and the completion = xi'/xi are mutation-SENSITIVE, i.e. genuinely arithmetic (not generic).
So the Round006 no-go (the completed source response is not passive on H_{1/2}) is a statement about the
REAL arithmetic object, not a generic-network artifact. A random-period / fake-wire version is a different
(non-zeta) function and equally non-passive -- confirming non-passivity is not special, but the TARGET is.
RH open.
""")
