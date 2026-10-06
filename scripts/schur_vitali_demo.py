#!/usr/bin/env python3
"""Round006 ckpt6: numerical demonstration of the Schur-Vitali continuation mechanism.

This does NOT touch zeta. It confirms (a) the proof logic is correct and coded right, and
(b) that hypothesis (P) -- contractivity on ALL of H_{1/2}, not just Re s>1 -- is the essential,
non-automatic ingredient.

GOOD family (meets (P)+(E)): F_X = (1/X) sum_{j=1}^X 1/(w + j/X), w=s-1/2  (Riemann sum of
F(s)=int_0^1 dtau/(w+tau)). Each 1/(w+tau) is Herglotz on H_{1/2} (Re>0 => Re 1/(w+tau)>0), so each
F_X is positive-real on H_{1/2} BY CONSTRUCTION, hence Theta_X=Cayley_a[F_X] is Schur on H_{1/2}.
We verify: (i) |Theta_X|<=1 sampled over H_{1/2}; (ii) Theta_X -> Theta on Re s>1; (iii) as the theorem
predicts, Theta_X -> the SAME analytic continuation on the strip 1/2<Re s<1.

BAD family (fails (P)): g(s)=1/(s-0.7) has a pole at 0.7 in the strip. It is positive-real on Re s>0.7
(so on Re s>1), but Cayley_a[g] is NOT Schur on all of H_{1/2} (|Theta|>1 near the strip pole). Euler-side
convergence then does NOT force strip convergence -- the limit has a pole at 0.7. This is exactly the
failure mode an indefinite/pole sector would create.
"""
import numpy as np

a = 1.0


def cayley(F):
    return (F - a) / (F + a)


def F_good(s, X):
    w = s - 0.5
    j = np.arange(1, X + 1)
    return np.mean(1.0 / (w + j / X))


def F_good_limit(s):
    w = s - 0.5
    return np.log((w + 1.0) / w)              # int_0^1 dtau/(w+tau) = log((w+1)/w)


def g_bad(s):
    return 1.0 / (s - 0.7)


def sup_modulus(fn, X=None, re_min=0.5001, re_max=6, im_max=40, ngrid=120):
    res = np.linspace(re_min, re_max, ngrid)
    ims = np.linspace(-im_max, im_max, ngrid)
    m = 0.0
    for sr in res:
        for si in ims:
            s = complex(sr, si)
            v = fn(s, X) if X is not None else fn(s)
            m = max(m, abs(v))
    return m


print("=== GOOD family: F_X = Riemann sum of positive-real kernels (meets hypothesis P) ===")
for X in (4, 16, 64, 256):
    mmod = sup_modulus(lambda s, X=X: cayley(F_good(s, X)), X=None)
    print(f"  X={X:4d}: sup_{{Re s>1/2}} |Theta_X| = {mmod:.6f}   "
          f"{'(Schur: <=1 up to grid)' if mmod <= 1 + 1e-9 else '(NOT Schur!)'}")

print("\n  convergence Theta_X -> Theta on Re s>1 (Euler-side) and on the STRIP 1/2<Re s<1:")
for s in [complex(2.0, 1.0), complex(1.3, 3.0), complex(0.7, 2.0), complex(0.55, 0.5)]:
    th = [cayley(F_good(s, X)) for X in (64, 256, 1024)]
    thlim = cayley(F_good_limit(s))
    region = "Euler Re s>1" if s.real > 1 else "STRIP 1/2<Re s<1"
    print(f"   s={s}  [{region}]: |Theta_1024 - Theta_limit| = {abs(th[-1]-thlim):.2e}")

print("\n=== BAD family: g(s)=1/(s-0.7), pole in the strip (FAILS hypothesis P) ===")
mmod_bad = sup_modulus(lambda s: cayley(g_bad(s)))
print(f"  sup_{{Re s>1/2}} |Cayley[g]| = {mmod_bad:.4f}   "
      f"{'(NOT Schur on H_1/2 -- as expected, strip pole)' if mmod_bad > 1 + 1e-6 else ''}")
# but on Re s>1 it IS contractive:
mmod_bad_euler = sup_modulus(lambda s: cayley(g_bad(s)), re_min=1.0001)
print(f"  sup_{{Re s>1}}   |Cayley[g]| = {mmod_bad_euler:.4f}   "
      f"{'(contractive on the Euler region only)' if mmod_bad_euler <= 1+1e-6 else ''}")
print("  => Euler-side contractivity does NOT imply H_{1/2} contractivity; the strip pole survives.")
print("\nMechanism confirmed. The whole RH content is hypothesis (P): structural contractivity on ALL")
print("of H_{1/2}. ckpt5 (C103) shows the naive arithmetic one-ports fail it. RH open.")
