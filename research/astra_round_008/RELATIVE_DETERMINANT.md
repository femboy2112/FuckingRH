# Which determinant is available?

Finite clock determinants are ordinary determinants. Their limits require
an explicit convention. On the direct sum of the primitive `(p,k)` blocks,
put `A(s)=direct_sum p^(-s) C_(p^k)|primitive`. For each fixed prime `p`,
there are infinitely many nonzero orthogonal blocks of norm `p^(-Re s)`.
Selecting one unit vector in each proves that `A(s)` is not compact at any
finite `Re s>0`; in particular it is in no Schatten class. The same argument
applies to global innovations weighted by their birth prime, since every
prime occurs at infinitely many prime-power events.

Consequently `det(I-A(s))` is **not an ordinary Fredholm determinant**.
The grouped finite-block products in (CE1) and (GI3) have the stated limits,
but grouping is load-bearing. The sum of absolute eigenvalue moduli already
diverges within one fixed prime tower; one cannot freely reorder individual
eigenvalue factors or appeal to trace-class determinant identities.

At finite dimension a determinant quotient is exact because the old space
reduces the clock. This does not justify a quotient of two undefined infinite
determinants. The local telescope and the global product each define their
own specific relative/grouped regularization, and they give different
functions. The difference cannot be erased by calling both 'relative'.

For the Gamma ladder, by contrast, `(H+s0)^(-1)` is Hilbert–Schmidt. Its
`det_2` and zeta determinant are explicitly normalized in `GAMMA_DRIFT.md`.
Those determinant notions likewise differ by a calculated linear exponential.
Multiplying a local grouped Euler determinant by a Gamma determinant recovers
the classical completion algebraically; no common positive operator is
thereby constructed.
