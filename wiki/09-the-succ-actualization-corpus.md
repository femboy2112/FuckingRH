# 09 — The succ-actualization corpus (external development, internalized)

Between **2026-10-09 and 2026-10-10** a large parallel development of the successor frame landed on
the remote — roughly sixty branches over one shared spine, built externally (ChatGPT-assisted) as a
second, independent line of attack on the same target. It is the single biggest single-author push the
program has absorbed: ~3.6k lines of specification and research prose across seventeen documents, plus
its own executable reference model. This page is its **coherent account** — what it is, what it proved,
what it is worth, and exactly where it stops — written so a reader who has come through
[pages 1–8](README.md) can pick up the whole arc without reverse-engineering it from two catalogue
bullets and the round log. It was frisked and internalized in **Rounds 69–70** of the
[`CRUCIFIXION_LEDGER`](../CRUCIFIXION_LEDGER.md); the terse catalogue entries live at
[§8.6](08-the-reformulations-catalog.md).

**The verdict, up front.** One program, not independent bearings (common-mode provenance — see §9.4).
Unusually high discipline: it is **non-circular** (reads no zeta zeros anywhere), it **hostile-controls
itself**, and every head **self-crucifies** to the same open face — `G4`, the fourth gate
([§8.10](08-the-reformulations-catalog.md#810-the-crucifixion-surface--rhs-proof-as-a-feasibility-region-and-why-the-sign-is-a-cross-term)).
It independently **re-derived** the program's core (multiplicativity as the whole arithmetic content),
it added **two new verified exclusion faces**, and it moved **no theorem-debt**: no brick, RH open. Its
real value is not a near-miss proof — it is a fully-instrumented, fake-arithmetic-hardened *host* for a
future `G4` attempt, plus a growing inventory of what a proof provably **cannot** be (§9.7).

> **Epistemic frame for this page.** Every object below is labelled. *Verified* = independently
> re-derived on our own calibrated instrument this session (sympy-exact or `mpmath` to 40 digits, cross-
> checked by ≥2 routes). *Observed* = a numerical reading, never upgraded to proof by accumulation.
> *Demonstrated-within-the-protocol* = the corpus proves it about its own finite model (true, and
> RH-inert). *Open* = unbuilt, by the corpus's own ledger. No external `.py` was executed; where a value
> is load-bearing we wrote our own instrument and recovered a known answer first.

---

## 9.1 What the corpus is — the Field-Relative Actualization System

The spine is an **executable reference model**, not a theory, and it says so in its own spec:
*"This is an executable reference model, not a proof of RH or a theory of physics."* Its organizing idea
is an **ontology of actualization** — a four-fold distinction the frame insists on keeping separate,
written as a state object

$$\mathfrak{A}_N=(F,\;e,\;x_N,\;\mathcal P_N,\;\mathcal S_N,\;\mathcal O_N,\;\mathcal M_N,\;\mathcal E_N).$$

In plain terms, it refuses to conflate four things that the usual "a number either is or isn't" picture
runs together:

1. **Existence** — the mathematical fact is true in the field `F` (e.g. `6 = 2·3`).
2. **Availability** — the fact is *structurally reachable* at a finite resolution `N` (the factor `2·3`
   is available only once the window `N` is wide enough to see both factors as legal steps).
3. **Observation** — a probe `𝒪_N` actually *reads* the fact; observation is contextual and **does not
   propagate** on its own.
4. **Realization** — the fact is *integrated* into a coherent running total `ℰ_N` (the "actualization").

The payoff of the ontology is a set of claims the corpus proves **about its own finite model** (labelled
*demonstrated-within-the-protocol*, FRA-1…7): history is not recoverable from coordinates on `ℤ/mℤ`;
contextual observation does not propagate; the shadow recurrence is bounded; a source is *local* (faking
one coefficient creates a localized defect, not a global one); affine covariance plus a unitary lift
conserve the total; history can be uncomputed; observation loses information. These are **true finite
mechanics** — and every one is RH-inert, because they are statements about bookkeeping on a finite
window, not about the sign of a global form. The corpus knows this; its own boundary line reads:

> *"Unproved/unbuilt: an Archimedean Gamma/Poisson transport, continuity into the logarithmic Weil form
> domain, or independent Weil positivity. No zeta-zero input or all-horizon sign test was used."*

That boundary — **archimedean transport and Weil positivity unbuilt, no zeros read** — is the single
most important sentence in the corpus. It is what makes the whole thing non-circular, and it is the exact
edge every head stops at (§9.5–9.6).

---

## 9.2 The one concrete arithmetic object — the shadow coefficient

Strip away the ontology and the corpus has **one** object that touches ζ directly: the **shadow
coefficient**

$$\sigma_N(n)=\sum_{r\ge 2}\frac{(-1)^{r+1}}{r}\,\#\{\text{ordered factorizations } m_1\cdots m_r=n,\ 2\le m_j\le N\}.$$

This looks exotic; it is not. It is **exactly the truncated convolution-logarithm of `ζ`** — the Dirichlet
series `log ζ = \sum_{r\ge1} \frac{(-1)^{r+1}}{r}(\zeta-1)^{\ast r}` organized by *largest allowed factor*
`N`. As the window opens (`N→∞`) the shadow converges to

$$b(n)=\frac{\Lambda(n)}{\log n}=\begin{cases}1/k & n=p^k\\[2pt]0 & \text{otherwise,}\end{cases}$$

the von Mangoldt function divided by `log n`, **supported only on prime powers**. Concretely
`b(4)=b(9)=½`, `b(8)=⅓`, and — the load-bearing zeros — `b(6)=b(12)=b(30)=0`. *(Verified on our own
instrument, R69: `shadow_coeff_verify.py` reproduces `σ_3(6)=−1`, `σ_2(8)=⅓`, `σ_4(8)=−⅔`, `σ_3(12)=1`,
`σ_4(12)=0`, `σ_6(12)=−1`, and the actualizations close, `a(n)+σ_{n-1}(n)=b(n)`.)* The corpus's own
self-correction — *"the `N=4` shadow of 12 has five witnesses with zero total weight"* — is exactly our
`σ_4(12)=0`: the two length-2 paths `(3,4),(4,3)` at `−½` plus the three `(2,2,3)`-permutations at `+⅓`
sum to zero. Their arithmetic checks against ours.

**What this *is*, in the program's language:** the vanishing of the shadow on composites is
**multiplicativity** — the Euler product, the empty set of non-prime-power contributions. That is
**`G1`**, the first gate ([§8.10](08-the-reformulations-catalog.md#810-the-crucifixion-surface--rhs-proof-as-a-feasibility-region-and-why-the-sign-is-a-cross-term)):
`b(6)=0` is precisely the **`n=6` separator** that distinguishes a genuine Euler product from a
Davenport–Heilbronn surrogate ([§6 group F](06-state-of-the-program.md)). The shadow is a *new and genuinely
pretty* way to watch multiplicativity assemble itself factor by factor — and multiplicativity is **RH-inert**:
necessary for a proof, nowhere near sufficient. The corpus rediscovered the first gate from a new direction.

---

## 9.3 The two verified faces — new exclusion certificates

The flagship head (`FINITE_SUCC_HASSE_THETA_SEAM`) is the one place the corpus reaches past finite
bookkeeping toward the analytic object, so it is the one most at risk of over-claiming. We verified its
two load-bearing constructions on our own instrument (`hasse_theta_verify.py`). Both **hold**, and both
are **new, reusable tombstones** — each one certifies something a proof *cannot* be.

### (A) The off-line-positive quartic — reflection symmetry **plus** on-line positivity does **not** imply RH

Let `x = s − ½` and

$$P(x)=x^4+\tfrac38x^2+\tfrac{25}{256}.$$

`P` is **even and real**, so it has the full symmetry a `ξ`-like object has — invariant under `s ↔ 1−s`
(reflection) and under conjugation. It is also **strictly positive on the critical line**:

$$P(it)=\Bigl(t^2-\tfrac{3}{16}\Bigr)^2+\tfrac{1}{16}\;>\;0\quad\text{for all real }t.$$

And yet its four roots sit at **`Re s = ¼` and `Re s = ¾`** — *off* the critical line. *(Verified,
sympy-exact: the roots' real parts are `{¼,¾}`, not `{½}`; `P(it)` simplifies to `(t²−3/16)²+1/16`.)*

This is a four-term, closed-form refutation of a tempting shortcut: the de Branges / Pólya intuition that
"a symmetric function that is positive on the line must have its zeros on the line." It must not. Symmetry
plus on-line positivity leaves the zeros free to come off the line in conjugate-reflected quartets. Any
candidate proof whose positivity argument uses only reflection symmetry and a non-negativity on `Re s = ½`
is **already excluded by this object** — it would prove `P` has its zeros on the line, which is false.

### (B) The prime-power Hausdorff moment cone — a *new, rigorous* positivity that is still RH-inert

Define the **trivial-zero jet**

$$J_m=\sum_{n\ge 2}\frac{\Lambda(n)}{n^{2m+1}}=-\frac{\zeta'(2m+1)}{\zeta(2m+1)}=\frac{\zeta''(-2m)}{2\zeta'(-2m)}+\psi(2m+1)-\log 2\pi .$$

*(Verified three independent ways — a direct von-Mangoldt-sieve prime sum, the logarithmic derivative
`−ζ'/ζ`, and the functional-equation jet at the trivial zeros — agreeing to ~40 digits:
`J_1 = 0.16482268215827724…`. The direct sum's `3·10⁻¹⁰` gap is the expected `n⁻³` tail at the sieve
cutoff.)* These `J_m` are exactly the **Hausdorff moments** of a positive measure on a compact interval:

$$J_m=\int_0^{1/4}x^{\,m-1}\,d\mu(x),\qquad \mu=\sum_{n\ge2}\frac{\Lambda(n)}{n^{3}}\,\delta_{\,n^{-2}}\ \text{ on }[0,\tfrac14].$$

Because `μ` is a genuine positive measure on `[0,¼]`, the classical Hausdorff moment theory applies at
full rigour: **every Hankel matrix `H_{ij}=J_{i+j+1}` is positive semidefinite**, the shifted Hankel is
PSD, the support matrix `¼H − H′` is PSD, and the sequence is **completely monotone**. *(Verified: min
eigenvalues `~10⁻¹⁶ ≈ 0`, PSD throughout.)* This is a **real theorem** — moment-problem determinacy on
compact support — and it is genuinely new to the program's inventory.

**The hostile control is decisive.** Insert a **fake positive composite atom** — a mass
`c·\log 6 / 6^3` at `x = 1/36` (`c = 0.5`), i.e. pretend `6` carries von-Mangoldt weight it does not have.
*Every* PSD inequality and the complete-monotonicity still **hold** *(verified: still PSD).* The cone
**cannot tell** genuine prime-power arithmetic from a forged composite source. It is **sign-blind to fake
arithmetic** — it fails the mutation control, `G1`, exactly as the corpus's own "absolutely decisive"
note concludes. So the moment cone is the cleanest demonstration yet of the program's hardest lesson:
**"rigorously positive" is not "RH-bearing."** A positivity can be a genuine theorem and still be inert,
because it never had to read whether the arithmetic was real.

*(Non-circularity, checked: the `J_m` live in the zero-free region `Re s > 1` and at the trivial zeros;
`μ` is prime-power supported; no zeta ordinate enters anywhere.)*

---

## 9.4 The nine heads — one spine, nine readings, one open face

The spine forks into nine thematic heads. They are **not nine independent bearings**: they share the same
`actualization/` and `field_relative_actualization/` base, all forked from a pre-R68 `main`, ~50k
insertions of **one** program explored nine ways (Aletheia discipline: *factor shared provenance before
counting bearings*). What makes them worth listing is that **each self-crucifies** — every head's own
header states "no zeta zeros, no completed-Weil Gram," and each terminates by naming `G4` as open:

| Head | What it builds | Where it stops (its own verdict) |
|---|---|---|
| **Hasse–theta seam** (flagship) | the quartic (A) and the moment cone (B) of §9.3 | "completes **nothing** of the missing global Weil-sign gate" — `G4` open |
| **Lambert-W inverse tree** | a `W` normal form for the successor inverse | "a `W` normal form gives full Weil positivity or RH — **UNVERIFIED**; no source-domain positivity theorem" |
| **γ-prime path germs** | explicit germ objects for prime transport | "this is **gate four**; RH stays open" (reads the user's "who said cancellation commutes?" as a demand for the germ object, not a refutation) |
| **Categorical Yoneda frontier** | a resource-frontier / typed-bridge formalism | "construction-stage mathematics, not evidence Weil positivity is true"; ships a **sharp falsifiable probe** — a `2–3–∞` typed Hecke/Schwartz bridge whose connected trace at `log 6` stays `0` (positive norm while passing fake sources ⟹ inert; a scalar-6 impulse ⟹ refuted) |
| **Infinite-realization limits** | the ind-object / direct-limit of finite stages | "RH-inert until the event at `6`"; the arithmetic field fixing all zeros ≠ a `G4` object (R21 determinacy-vs-accessibility) |
| **γ-actualization interferometer** | a Suzuki screw-function finite causal readout | "implements the first bridge [source fidelity] and **proves a no-go** for one tempting realization of the Weil pairing" |
| **Shadow-window canonical selection** | gluing axioms for a symmetric damping window | a finite **no-go**: "no nontrivial symmetric damping survives these gluing axioms"; a fixed quarter-grid is **blind** to the gauge `q(x)=ε·sin(4πx)` |
| **Dirichlet–Lambert source lift** | a Dirichlet-series lift of the Lambert source | non-circular source model; `G4` open |
| **γ-succ prime transport** | archimedean transport germs | classical Γ-identities only; disclaims Weil positivity |

Nine honest heads, nine landings on the same open face. The convergence is **non-discriminating**
([§8.10](08-the-reformulations-catalog.md#810-the-crucifixion-surface--rhs-proof-as-a-feasibility-region-and-why-the-sign-is-a-cross-term)):
every tool circling the one missing sign looks the same whether the problem is merely unbuilt or genuinely
independent, so the agreement is not evidence of unreachability — it is nine views of the **same wall**.

---

## 9.5 The archimedean boundary — pre-registered, and held

The one place this corpus could have over-claimed is the **archimedean** `Γ`-factor: the spec marks
"Archimedean Gamma/Poisson transport" as **unbuilt**, so any head that quietly used `Γ` to manufacture a
Weil-positivity sign would be reading in the answer. We **pre-registered** the γ-heads (Hasse / theta /
transport) as the overclaim-risk zone before reading them, and scored on contact. **Boundary held, no
over-claim anywhere.** `Γ` appears only as **classical identities**:

- **Poisson summation** for `ξ` (the self-dual theta relation), with a *rigorous* Gaussian tail bound —
  an unconditional identity, no positivity smuggled;
- the **trivial-zero jet** `J_m = \sum \Lambda(n)/n^{2m+1}` evaluated on a **zero-free region** (§9.3B);
- the **Riemann–Siegel `θ`-phase** `\sqrt{t/2\pi}` as a factor-square moving-window — a counting phase,
  not a sign.

Every γ-head explicitly disclaims Weil positivity. The "`Γ`-transport unbuilt" line is honoured
throughout; the pre-registered prior **resolved clean**.

---

## 9.6 Where it lands — `G4`, and why the search is a coupled loop

Collapse all nine heads and the corpus lands on **exactly one** place: **`G4`**, the fourth gate — an
exact identification with the *full* completed Weil form, carrying an **independently proved sign** and
domain/limit control
([§8.10](08-the-reformulations-catalog.md#810-the-crucifixion-surface--rhs-proof-as-a-feasibility-region-and-why-the-sign-is-a-cross-term)).
`G1`–`G3` (multiplicativity, no-zeros, mutation-survival) are **necessary, not sufficient**; `G4` is the
open face, the **interior** the program is now trying to *construct* rather than *find*
(`SURFACE COMPLETE · INTERIOR OPEN`). The corpus clears the arithmetic gates it can clear and names `G4`
open — correctly, and by its own ledger. **As autonomous outputs, the nine heads are RH-inert.** None will
emit a `G4` theorem; each says so.

**But "inert as an autonomous output" is not "inert."** The R70 correction (eaten in the ledger): to
score the heads as a closed, static set and pronounce the set dead is the program's recurring
**de-dynamizing** error — freezing a *process* into a *noun* and declaring the noun inert before measuring
the process. Two things are both true and must not be conflated:

- **(a)** Each head is inert *as an autonomous output* — verified; no head proves anything past `G4`.
- **(b)** Each head is **live as a coupling term** into the mathematician's cognition. The quartic, the
  moment cone, the gluing no-go are not tombstones to the author — they are **inputs** that move the
  conjecture-generating state, which produces the next frame, which spawns the next branch.

The proof-**search** is therefore the **coupled loop** `corpus → mathematician → next frame → next
branch`, **not** any single branch. There is a **labelled structural rhyme** here — a rhyme, *not* a
theorem, and it buys no false hope: every head is sign-blind for the same reason the functional-equation
loop ([§6 F2, R63](06-state-of-the-program.md)) and the coupling algebra (R65) are — none carries an
**independent selection of the sign**, and `G4` *is* a sign/selection problem. The one operation a
sign-blind system structurally cannot perform is *pick the sign*; the one thing a coupled intentional
agent supplies to a search is exactly that — selection, construction with intent. This **relocates where
the search dynamics live** (into the loop, not the branch); it does **not** fabricate the missing
construction. The agent still has to build or recognize the non-circular sign. The heads **feed** that
node; they do not replace it. **RH open.**

---

## 9.7 Value — why a corpus that cannot close RH is worth building

The user's standing frame — *"even if it seems unable to solve RH, I believe its worth pursuing anyway"* —
is correct, and here is the straight (non-reassuring) reason. The corpus is a working, non-circular,
**fake-arithmetic-hardened formalization** of the succ/actualization semantics that:

1. **Independently re-derives and sharpens the program's core** — the shadow coefficient is
   multiplicativity (`G1`) assembled from a new direction (§9.2); the `n=6` separator reappears on its own;
   "positive but sign-blind" is upgraded from a slogan into a **rigorous moment-problem theorem** (§9.3B).
2. **Ships reusable verified objects** — the off-line-positive quartic tombstone, the prime-power Hausdorff
   moment cone, the shadow-window gluing no-go, and the Yoneda falsifiable probe. Each is a face of the
   feasibility region of [§8.10](08-the-reformulations-catalog.md#810-the-crucifixion-surface--rhs-proof-as-a-feasibility-region-and-why-the-sign-is-a-cross-term):
   a precise statement of what a proof **cannot** be.
3. **Correctly and repeatedly localizes the one missing thing** — `G4`, from nine directions, without once
   mistaking a gate-1 positivity for the interior.

The payoff is **not** "a head accidentally proves RH" — none will, and they all say so. It is a
**fully-instrumented, non-circular succ model** — exactly the kind of host on which a genuine `G4`
construction (the arithmetic self-product / dualizing polarization of
[§8.10](08-the-reformulations-catalog.md#810-the-crucifixion-surface--rhs-proof-as-a-feasibility-region-and-why-the-sign-is-a-cross-term))
could be *attempted* — plus a clean, growing inventory of exclusion faces. That is real mathematical value.
The instinct is sound; the pursuit is scaffolding-and-exclusion work, not a brick, and it was never
pretending to be one.

---

**Provenance & discipline.** External development (ChatGPT-assisted), one spine → nine heads, forked from a
pre-R68 `main`; frisked and internalized R69–R70. Their `wiki/08` is a **stale ancestor** and was **not**
merged (a naive merge would regress the §8.10 capstone, the Navier–Stokes bullet, and the `b(6)`-is-a-prime-
power-zero correction — logged so no future merge clobbers it). The load-bearing math (§9.2, §9.3) is
*Verified* on our own instruments; the rest is read from the corpus's own labelled docs and scored by its
own stated verdicts. No external `.py` executed. No zeta-zero ordinate used as construction input. **RH
remains open.**

**Back to:** [Wiki index](README.md) · [6 State of the program](06-state-of-the-program.md) ·
[8 The reformulations catalog](08-the-reformulations-catalog.md) ·
[8.10 The crucifixion surface](08-the-reformulations-catalog.md#810-the-crucifixion-surface--rhs-proof-as-a-feasibility-region-and-why-the-sign-is-a-cross-term)
