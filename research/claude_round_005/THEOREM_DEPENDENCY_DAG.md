# Round 005 dependency DAG

```
SUCC n->n+1
  |
  |-- radix-m: S~_m = I(x)C_m + (S-I)(x)|0><m-1|   [carry decomposition, C95]
  |     |-- Fourier: diag characters + rank-1 carry coupling (DC channel a=0)
  |     |-- m=2: full adder (bit XOR carry, bit AND carry)
  |     \-- branches R_{m,r}: V_m S=S^m V_m, sum_r R_r R_r^*=I (Cuntz O_m) [C97]
  |            => "affine noncommutativity = carry curvature"
  |
  |-- carry-depth hierarchy (p-adic)
  |     |-- records R_p(N)=floor(log_p N): sum_p log p [R_p(N)-R_p(N-1)]=Lambda(N) [C96]
  |     |-- Haar cylinder => r=p^{-1/2} (half-density forced) [C96]
  |     \-- B_p = c_p (I-U_depth)(I-p^{-1/2}U_depth)^{-1} = C90 sigma_p [C96, carry filter]
  |            => CARRY^*CARRY = (2I-S-S^*)(x)|m-1><m-1| ; Suzuki event measure = carre-du-champ (local) [C99]
  |
  |-- self-sieve (clocks at p^2) correct [C99]; causal vs static => same K_Psi (RH-inert) [C99]
  |
  |-- GLOBAL attempts
  |     |-- shared-DC telescoping: REFUTED (sigma_p(0)=0, divergence bulk+analytic) [C98, no-go]
  |     |-- quotient filtration Z/L_N: circulant = RH-inert [C97, no-go]
  |     \-- => wall = Round-004 C91 (bulk+analytic renorm vs indefinite pole = Weil)
  |
  \-- dyadic clock graph: F^n(q)=s+2^n(q-s), order-clocks period ord_ell(2) [probe, tangential]
```
RH: OPEN.
