# Prime ancestry = dyadic carrier + character-routed order-clocks

**Date:** 2026-10-06. **Status:** exact (DISCLOSED), verified `scripts/prime_dyadic_clock_graph.py`.
RH open. A distinguished dynamical skeleton / probe of the self-sieve (NOT a prime generator).

## The exact structure

For an odd prime $p$, set $q=(p+\chi_4(p))/2$ (so $p=2q-\chi_4(p)$). For a prime $q>3$ with
$s:=\chi_3(q)\in\{\pm1\}$, the unique possible prime child is
\[
\boxed{\ F(q)=2q-s,\qquad s=\chi_3(q)\ }
\]
(the other branch $2q+s$ is divisible by 3). **The routing character is invariant:** since $q\equiv s\ (3)$,
$F(q)=2q-s\equiv s\ (3)$, so $\chi_3(F(q))=\chi_3(q)=s$. Hence $F(q)-s=2(q-s)$ and, exactly,
\[
\boxed{\ F^n(q)=s+2^n(q-s)\ }\qquad\text{(wheel-6: }q=s+6a\Rightarrow F^n(q)=s+6\cdot2^n a,\ (s,a)\mapsto(s,2a)).
\]
**The branching prime graph is conjugate, on each $\chi_3$ sector, to pure binary doubling** $y\mapsto2y$
($y=q-s$). Verified for all primes $5\le q<2000$.

## Character transport (exact inter-clock wiring)

For a prime edge $p=2q-s$ (both $>3$): $\chi_4(p)=\chi_3(q)$ — the lower prime's mod-3 phase becomes the
upper prime's mod-4 phase (0 violations in 220 edges). The smallest nontrivial clock-to-clock wiring.

## Order-clocks: later primes sieve the dyadic depth

Along $q_n=s+2^n(q_0-s)$, a sieve prime $\ell\ne2$ divides $q_n$ iff $2^n\equiv -s(q_0-s)^{-1}\ (\ell)$.
So $\ell$ fires at **one residue class of $n$ modulo $\operatorname{ord}_\ell(2)$** (or never, if the target
$\notin\langle2\rangle$). Verified: $\ell=5$ at $n\equiv0\ (4)$, $\ell=11$ at $n\equiv1\ (10)$, $\ell=13$ at
$n\equiv7\ (12)$; $\ell=7,17$ never (for the orbit of $q_0=5$). So the prime graph **is** a clock network:
binary doubling carrier + one periodic kill-clock per sieve prime, period $\operatorname{ord}_\ell(2)$, with
a character-determined phase. CRT of finitely many orders gives an exact finite automaton.

Control (exact): $(p^2-1)/8$ is a semiprime iff $p\in\{7,11,13\}$ (verified $p<200$) — a tiny residue-clock
set almost completely routes the factorization.

## Honest scope (hostile caveat, per addendum F)

This is "2 carries, 3 chooses the rail, every later prime clocks the dyadic depth" — an exact, elegant
skeleton. But it is **not** the full self-sieve: many primes have no prime child/parent; components are
truncated Cunningham-style chains ($x\mapsto2x\pm1$). The clock periods are $\operatorname{ord}_\ell(2)$
(multiplicative-order / Artin territory), which is **not** the Riemann-zeta spectrum. So as a route to
$K_\Psi$ this is most likely **tangential/RH-inert** (the relevant arithmetic is orders of 2, not zeta
zeros); it is retained as a probe and a clean finite-automaton model of "interconnected prime clocks on
the dyadic carrier," to be tested against the carry-energy B in later checkpoints, not promoted.
