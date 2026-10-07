# SUCC-loop census: terminal support is not enough; keep the support filtration

**Date:** 2026-10-07  
**Branch:** `aletheia/succ-loop-undertones-2026-10-07`  
**Status:** finite exact census / design diagnostic. **RH remains open.**

This supplement stress-tests the loop-support formalism introduced in
`SUCC_LOOP_UNDERTONES_SUPPORT_GEOMETRY.md`.

The concern is simple:

> If every closed rational-affine word is reduced only to its terminal congruence support, have we thrown away the very chronology/carry information that could matter for RH?

The answer is **yes**. Terminal support is a useful coarse invariant, but it is too coarse to be the final dynamical state descriptor.

---

## 1. Probe alphabet

Use the small generator alphabet

[
S_+(x)=x+1,qquad
S_-(x)=x-1,
]

[
M_2(x)=2x,qquad
D_2(x)=x/2,
]

[
M_3(x)=3x,qquad
D_3(x)=x/3,
]

where each (D_m) is admissible only when the current value is divisible by (m).

Immediate rational inverse pairs are forbidden:

[
S_+S_-,
quad
S_-S_+,
quad
M_2D_2,
quad
D_2M_2,
quad
M_3D_3,
quad
D_3M_3.
]

This removes the most trivial length-two backtracking while retaining nontrivial partial-domain loops.

Enumerate every remaining word of length at most (7), and keep only words whose rational-affine composite is exactly the identity.

Reproduce with:

[
	exttt{python scripts/succ_loop_census.py}.
]

---

## 2. Result

The bounded census gives

[
oxed{
236
}
]

non-backtracking rationally closed words.

At three resolutions:

[
oxed{
236
	ext{ words}
longrightarrow
17
	ext{ terminal support cylinders},
}
]

[
oxed{
236
	ext{ words}
longrightarrow
91
	ext{ cumulative support filtrations},
}
]

[
oxed{
236
	ext{ words}
longrightarrow
66
	ext{ conductor-growth profiles}.
}
]

So terminal support compresses extremely strongly:

[
236	o17.
]

But it also discards a large amount of chronological structure.

---

## 3. The correct dynamical refinement

For a word

[
gamma=(f_1,ldots,f_ell),
]

let the cumulative support after prefix (j) be

[
C_j
=
r_j+M_jmathbb Z.
]

Because new prefix constraints are intersected with old ones,

[
C_{j+1}subseteq C_j
]

whenever the path remains nonempty, and therefore

[
M_jmid M_{j+1}.
]

Define the **support filtration**

[
oxed{
mathfrak S(gamma)
=
(C_1,C_2,ldots,C_ell).
}
]

Its conductor-only shadow is

[
oxed{
mathfrak M(gamma)
=
(M_1,M_2,ldots,M_ell).
}
]

The terminal support is merely

[
C_ell.
]

Thus:

[
oxed{
	ext{support holonomy}
=
C_ell,
}
]

while

[
oxed{
	ext{support history}
=
(C_j)_{jleell}.
}
]

The finite census demonstrates that these are materially different invariants.

---

## 4. Why this matters for arithmetic interaction curvature

Two loops can end on the same support cylinder while acquiring their constraints in different chronological orders.

If one immediately quotients both to

[
1_{C_ell},
]

their distinction disappears.

This is directly analogous to the repository's earlier no-go:

> quotienting the LCM clock to its final Fourier-diagonal cyclic state discards the irregular carry/history that may contain the only noncommuting arithmetic information.

Therefore the loop program should obey the same rule.

### Dead order

[
	ext{word}
	o
	ext{terminal support cylinder}
	o
	ext{Fourier/conductor spectrum}.
]

This is useful classification but probably RH-inert.

### Live order

[
	ext{word}
	o
	ext{chronological support filtration}
	o
	ext{carry/history transport}
	o
	ext{exact-conductor tomography}.
]

This retains the order in which constraints become actual.

---

## 5. Conductor births

Since

[
M_jmid M_{j+1},
]

define the conductor birth ratio

[
oxed{
b_j(gamma)
=
rac{M_j}{M_{j-1}},
qquad
M_0=1.
}
]

Each (b_j) records the amount of new modular resolution forced by the (j)-th prefix.

The total logarithmic support cost telescopes:

[
sum_jlog b_j
=
log M_ell.
]

So the scalar support information

[
log M_ell
]

does **not** retain when the support cost was paid.

The ordered birth sequence

[
(b_1,ldots,b_ell)
]

does.

This is precisely the kind of distinction that chronology-sensitive SUCC dynamics can see and a terminal quotient cannot.

---

## 6. A useful analogy with the LCM tower

For the universal support tower

[
L_X=operatorname{lcm}(1,ldots,X),
]

the birth ratio is

[
rac{L_X}{L_{X-1}}
=
egin{cases}
p,&X=p^k,\
1,&	ext{otherwise}.
end{cases}
]

Thus the universal chronological birth sequence is the prime-power event stream, and

[
lograc{L_X}{L_{X-1}}
=
Lambda(X).
]

For a single loop, the finite support filtration is the path-local analogue:

[
oxed{
	ext{global LCM birth history}
leftrightarrow
	ext{loop support birth history}.
}
]

This makes it natural to compare loop-filtration births against the global von-Mangoldt event stream.

---

## 7. Minimal sweep proposal

A useful finite sweep should not enumerate raw integers and should not quotient immediately to terminal support.

For each generator budget (B):

1. enumerate reduced rational-affine words up to cost (B);
2. keep algebraically closed words;
3. compute:
   - terminal support (C_ell);
   - support filtration (mathfrak S(gamma));
   - conductor births (b_j);
   - exact-conductor spectrum of each new support innovation;
4. quotient words only after these invariants are recorded;
5. group by:
   [
   (mathcal H_{m alg},
   C_ell,
   mathfrak M,
   	ext{phase data}).
   ]

For RH-facing work, the actual features should be the **innovations**

[
1_{C_j}
-
mathbb E[1_{C_j}mid C_{j-1}],
]

or their exact-conductor projections, rather than repeatedly counting the inherited support.

This is the loop analogue of a martingale-difference / wavelet decomposition.

---

## 8. What is and is not learned from the census

### Learned

- Algebraically closed words proliferate even in a tiny alphabet.
- Terminal support provides strong compression.
- Terminal support is too coarse to retain chronological structure.
- The cumulative support filtration provides a natural next invariant.
- The conductor-birth stream is a path-local analogue of the LCM/von-Mangoldt birth stream.

### Not learned

- Nothing here establishes an RH-sensitive sign.
- Nothing here shows the support filtration determines Suzuki's (mu(A)).
- Nothing here overcomes the prime/Archimedean renormalization wall.
- Finite word counts are not asymptotic theorems.

---

## 9. Next discriminating probe

Construct the support innovations

[
eta_j
=
1_{C_j}
-
mathbb E[
1_{C_j}mid C_{j-1}
]
]

on a common LCM clock.

Then:

1. project (eta_j) onto exact conductor (W_q);
2. apply the chronological LCM carry operator;
3. form pair and higher interaction fields;
4. compare with the bare CRT null;
5. test whether the resulting signed residual correlates **structurally**, not merely numerically, with the critical Suzuki carry term

[
-sum_{dle X}
rac{mu(d)}d
left{
rac Xd
ight}.
]

The target is an exact identity or a controlled remainder.

---

## 10. House conclusion

[
oxed{
	ext{A loop's endpoint tells us where it closes.}
}
]

[
oxed{
	ext{Its support filtration tells us how arithmetic made closure possible.}
}
]

For the RH program, keep both.
