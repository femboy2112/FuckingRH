# Source-ray incidence and the non-circular event-weight factorization (ckpt3)

**Date:** 2026-10-06. **Status:** DISCLOSED (exact). **RH open.**
**Reproduce:** `scripts/source_port_core.py` (checks I–III, all to machine precision).

Independent re-derivation of the Aletheia source-wiring, taken to the **operator** level (Aletheia
verified the scalar incidence; here the full operator identities `E^*E=I` and `B_beta^*B_beta=W_beta` are
confirmed as matrices).

## The primitive picture (no dynamical prime-creation)

Additive carrier `H_add = l^2(N)`, shift `S|n> = |n+1>`. The **first SUCC pulse** boots the source:

    Omega := S|0> = |1>   (the multiplicative identity).

Prime dilations `V_p|n> = |pn>` are **prewired**; the prime ray through the source is
`V_p^k Omega = |p^k>`. The additive worldline is `S^n|0> = |n>`. Hence the exact incidence:

    <n | V_p^k Omega> = delta_{n, p^k}.                                   (1)

## Theorem 1 (incidence ⇒ von Mangoldt)

    Lambda(n) = sum_{p, k>=1} (log p) <n | V_p^k Omega>.                  (2)

*Proof.* By (1) the sum has at most one nonzero term: the one with `p^k=n`, present iff `n` is a prime
power, contributing `log p = Lambda(n)`; otherwise `0`. ∎

**Reading.** `Lambda` is the `log p`-weighted **intersection number** of the SUCC worldline with the
prewired FUCC rays. This is upstream of "primality": it is the incidence geometry of two orbit families
(additive `S`-orbit of `|0>`, multiplicative `V_p`-orbit of `Omega`) in one space.

## The ray Hilbert space

    H_ray = l^2{(p,k): p prime, k>=1},   basis |p,k>.
    E|p,k> = |p^k>          incidence isometry (H_ray -> H_add)
    H|p,k> = k log(p)|p,k>  total log-energy / depth
    Q|p,k> = log(p)|p,k>    primitive-generator charge

## Theorem 2 (E is an isometry)

    E^*E = I_ray.                                                        (3)

*Proof.* `(E^*E)_{(p,k),(p',k')} = <p^k | p'^{k'}>`. By unique factorization `p^k = p'^{k'}` iff
`(p,k)=(p',k')`, so `E^*E = I`. ∎  (`EE^*` = orthogonal projector onto `span{|p^k>}`, the prime-power
subspace of `H_add`.) Verified: `||E^*E - I_ray|| = 0` exactly (N=400, 97 rays).

## Theorem 3 (event-weight operator and its non-circular square)

For `beta>0` put `W_beta := E Q e^{-beta H} E^*` on `H_add`. Then

    W_beta |n> = Lambda(n) n^{-beta} |n>.                                (4)

In particular `W_{1/2}|n> = (Lambda(n)/sqrt n)|n>` is the **critical Suzuki event weight**.
Defining `B_beta := Q^{1/2} e^{-beta H/2} E^* : H_add -> H_ray`,

    B_beta^* B_beta = W_beta.                                            (5)

*Proof.* `E^*|n> = |p,k>` if `n=p^k` else `0`; then `e^{-beta H}|p,k> = p^{-beta k}|p,k> = n^{-beta}|p,k>`,
`Q` multiplies by `log p = Lambda(n)`, and `E` returns `|n>`, giving (4). (5) is immediate:
`B_beta^*B_beta = E e^{-beta H/2} Q^{1/2}\,Q^{1/2} e^{-beta H/2} E^* = E Q e^{-beta H} E^* = W_beta`,
using `Q,H` diagonal (commute). ∎  Verified: `offdiag(W)=0`, `||diag(W)-Lambda n^{-beta}||<5e-16`,
`||B^*B-W||<1e-15` for `beta in {0.5,1,2}`.

`B_beta|n> = sqrt(Lambda(n))\, n^{-beta/2}\,|p,k>` is the **emission amplitude** of integer `n` into its
unique ray.

## Scope (honest)

- (5) is a **genuine, non-circular factorization of the diagonal event-weight operator** `W_beta`. It uses
  no zeros, no `K_Psi` spectral data, no positivity assumption. It is exact.
- It is **NOT** a factorization of the Suzuki screw kernel `K_Psi`. `W_beta` is diagonal in `|n>`; `K_Psi`
  is the full screw kernel. The round's job is to climb from this diagonal weight to the completed,
  off-diagonal, positive object. Keeping these layers apart is mandatory (directive §3).
- `B_{1/2}` is bounded: `||B_{1/2}|n>||^2 = Lambda(n)/n -> 0`. The source vector problem (the state
  leaving Hilbert space as `sigma -> 1/2`) appears not here but in the **correlation** layer (ckpt4),
  where the relevant sum `sum Lambda(n) n^{-sigma}` diverges as `sigma -> 1`.
