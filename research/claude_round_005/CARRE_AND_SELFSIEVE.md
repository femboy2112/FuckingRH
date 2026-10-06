# Carré-du-champ of carry = Suzuki event measure (locally); self-sieve; causality is RH-inert

**Date:** 2026-10-06. **Status:** DISCLOSED, verified `scripts/carre_selfsieve.py`. RH open.

## §15/22-E — the von-Mangoldt event measure is the carré-du-champ of carry curvature (local)

The elementary carry-curvature operator is $\mathrm{CARRY}_m=(S-I)\otimes|0\rangle\langle m-1|$. Its carré is
exact (verified to machine zero):
\[
\boxed{\ \mathrm{CARRY}_m^\*\mathrm{CARRY}_m=(S-I)^\*(S-I)\otimes|m-1\rangle\langle m-1|
=(2I-S-S^\*)\otimes|m-1\rangle\langle m-1|.\ }
\]
The quotient factor $2I-S-S^\*=|I-U|^2$ is the **high-pass innovation energy** (symbol $2(1-\cos\xi)$) — i.e.
exactly the $(I-U_{\rm depth})^\*(I-U_{\rm depth})$ that opens the local filter $B_p$ (LOCAL_BP_FROM_CARRY §3).
Weighting by $\log p$ (record-carry cost, §7) and the half-density $p^{-1/2}$ (Haar, §12) over the p-adic
depth hierarchy reconstructs $\sigma_p$ (C90). So:

> The Suzuki/von-Mangoldt event measure is the **carré-du-champ of the carry curvature**, prime by prime.
> (§22-E holds **locally** — a clean positive identification. The *global* assembly is the wall below.)

## §6 — the self-sieve is correct

An online sieve that (i) makes each survivor a new clock and (ii) activates a prime $p$'s clock at $p^2$,
firing on multiples, leaves exactly the primes: verified primes$\le500$ match. (Standard
smallest-factor$\le\sqrt n$ correctness, now as a causal state machine.)

## §18-E — causality/birth-order is RH-inert for the kernel (control)

The Suzuki kernel $K_{\Psi,L}$ sums $\Lambda$ over the **set** of prime powers $\le e^L$. The causal
self-sieve (primes born $2,3,5,\dots$) and a static preloaded prime set yield the identical set, hence the
identical $K_{\Psi,L}$. **Birth order does not change the kernel** — causality is a dynamics statement, not
a kernel statement; the RH content is in *which* $p^k$ enter and *how they couple*, not the order of
discovery. (So the "the causal machine is the right primitive" thesis buys exact local structure and the
carré-du-champ picture, but no new kernel-level handle beyond Round-004.)
