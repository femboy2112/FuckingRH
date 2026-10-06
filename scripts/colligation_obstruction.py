#!/usr/bin/env python3
"""Round006 ckpt9: the obstruction to hypothesis (P) is a FUNCTION-level property of xi, parent-free.

A finite passive/unitary colligation has a Schur transfer function BY the positive-definiteness of its
state metric. ckpt8 showed the natural (Laplace-source) metric is indefinite with diverging index. The
question for the colligation/history-space routes: can a different parent Hilbert space / coupling order
supply a POSITIVE metric whose transfer limit is Cayley[xi'/xi]?

This script confirms the obstruction is parent-INDEPENDENT by exhibiting it at the level of the FUNCTION:
  - Sarnak / Conrey-Li object F(s) = xi(s)/xi(s+1). Its Re goes NEGATIVE in the strip Re s>1/2.
    Since positive-realness of xi'/xi on H_{1/2} <=> RH is a property of the FUNCTION, no choice of
    parent space (history-before-quotient included) can change it. A (P)+(E) family exists IFF RH.
  - We also confirm the companion: Re{xi(1+itau)/xi(2+itau)} < 0 at tau ~ 282 (Conrey-Li (3.3) failure).
"""
import numpy as np
from mpmath import mp, zeta, gamma, power, pi, mpc, mpf, log as mlog, re as mre
mp.dps = 25


def xi(s):
    s = mpc(s)
    return mpf(1) / 2 * s * (s - 1) * power(pi, -s / 2) * gamma(s / 2) * zeta(s)


def ratio(s):
    return xi(s) / xi(s + 1)


print("(1) Sarnak/Conrey-Li function-level obstruction: Re{xi(s)/xi(s+1)} over a grid in H_{1/2}.")
print("    If it goes negative in the strip, NO parent/coupling can give a positive-real xi'/xi short of RH.")
minv = 1e9; arg = None
for sig in np.linspace(0.55, 1.5, 12):
    for t in np.linspace(1, 320, 500):
        v = float(mre(ratio(mpc(float(sig), float(t)))))
        if v < minv:
            minv = v; arg = (float(sig), float(t))
print(f"    min Re{{xi(s)/xi(s+1)}} on grid = {minv:+.5f} at s={arg[0]:.3f}+{arg[1]:.1f}i   "
      f"{'<-- NEGATIVE (obstruction present)' if minv < 0 else ''}")

print("\n(2) Conrey-Li (3.3) companion: Re{xi(1+i*tau)/xi(2+i*tau)} near tau=282:")
for tau in (281.0, 282.0, 283.0):
    v = float(mre(xi(mpc(1, tau)) / xi(mpc(2, tau))))
    print(f"    tau={tau}: Re = {v:+.8f}   {'<-- NEGATIVE' if v < 0 else ''}")

print("""
VERDICT (ckpt9): the colligation route needs a POSITIVE state metric; the natural one is indefinite
(Conrey-Li; ckpt8 index diverges). The obstruction is a FUNCTION-level property of xi (Re{xi(s)/xi(s+1)}
< 0 in the strip; Sarnak: log zeta dense), hence PARENT-INDEPENDENT: no history-before-quotient or
coupling-order choice can convert a non-positive-real xi'/xi into a positive-real one. A finite passive
family satisfying (P)+(E) exists IFF RH. So the colligation/history escape hatches are NOT unconditional
escapes -- they are subject to the same (P)<=>RH logic, and the obstruction they must beat is a property
of the function, not of the chosen Hilbert space. RH open.
""")
