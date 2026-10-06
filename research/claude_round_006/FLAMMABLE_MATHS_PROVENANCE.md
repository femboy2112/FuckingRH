# Flammable Maths provenance (curiosity note only)

**Round 006 addendum. Historical/provenance note. Nothing here implies priority, influence, or
anticipation of this RH program.** Provenance and mathematics are kept strictly separate. The
mathematically relevant content (the Grünwald–Letnikov fractional derivative of `ζ`) is treated on its own
merits in `FRACTIONAL_SUCC_GAMMA_INTERTWINER.md §K`.

## 1. The "succ" notation — what is documented

The user recalls first meeting "succ" (successor, `n ↦ n+1`) via *Flammable Maths* (Jens Fehlau; formerly
*Fappable Maths* / "Papa Flammy"). Documented:

- **CONFIRMED:** the CTAN joke package **`realtranspose`** (https://ctan.org/pkg/realtranspose; authors
  L. Quentin, M. Scroggs, A. Townsend; v1.1, 2020-10-11, MIT; homage to `realhats`). Its README contains
  verbatim the example *"It's as easy as `1 succ(1) succ(succ(1))`!"* and the acknowledgment
  *"Papa Flammy … for all the math ideas"* with two FlammableMaths tweet links.
- **UNVERIFIED:** the separately-recalled "archived 2019 discussion" that attributes its `succ` notation to
  "PAPA from Flammable Maths" could not be reached (the inspiration tweets return an X login wall; broad
  code search was unavailable in-session). Recorded as an honest gap. (`realtranspose` itself is 2020, a
  distinct source from the recalled 2019 one.)
- **NOT FOUND:** a specific original Flammable/Fappable video first using "succ." On substance, "succ" is
  simply the century-old standard **Peano/type-theory successor** `succ(n)=n+1`, used by Fehlau as a running
  meme, not a developed construction. The Flammable Maths connection is **memetic popularization, not
  invention** of either the notation or any mathematics.

## 2. Mathematical overlap — the one real finding

Fehlau's public Math.SE / MathOverflow posts (account "Flammable Maths", posts signed "--Jens") include a
genuine match to the fractional-SUCC chain of `FRACTIONAL_SUCC_GAMMA_INTERTWINER.md §K`:

- **Math.SE 3559931 / MathOverflow 353539** (both 2020-02-25; tags incl. fractional-calculus, riemann-zeta,
  binomial-theorem). He states a fractional-derivative-of-`ζ` "theorem"
  `ζ^{(α)}(s) ≡ Σ_{k≥2} e^{iπα} log^α(k) / k^s`, and proves it via exactly the **Grünwald–Letnikov**
  operator
  `D_s^α ζ_N(s) = lim_{h→0+} h^{-α} Σ_{m≥0} (−1)^m C(α,m) ζ_N(s−mh)`,
  substituting `ζ_N(s−mh)=Σ_k k^{-s}(k^h)^m`, recognizing `Σ_m C(α,m)(−k^h)^m = (1−k^h)^α`, and using
  `lim_{h→0}(k^h−1)/h = log k`. He **himself flags** the convergence gap (the generalized binomial series
  needs `|−k^h|<1`, which fails, yet the `h→0` limit "regularizes" it) and asks for rigor; both posts went
  essentially unanswered.
- He **attributes the identity to prior published work** — *"Research by Guariglia showed that this is
  indeed the desired expression"* (Emanuel Guariglia's fractional-derivative-of-`ζ` / Dirichlet-eta
  results). So in his own framing it is **reproduction/verification of a known formula**, student-style, not
  an original discovery and **not any RH program**.
- Related but **separate**: a `k`-th-derivative-of-`ζ` question (Math.SE 3549101, 2020) stating
  `ζ^{(k)}(s) = e^{iπk} Σ_{n≥2} log^k n / n^s` (standard integer order), and reciprocal-Gamma integral
  identities (Math.SE 3285701 / MO 335756, 2019) — the latter **not** connected to the fractional-`ζ`
  derivation in his posts.

### The yes/no

**YES**, the Grünwald–Letnikov fractional-derivative-of-`ζ` construction is explicitly present in his public
posts, and it matches **three of the four** nodes of our §K chain in his own notation: the GL operator
`(I−S)^α = Σ(−1)^k C(α,k)S^k`; the `(log n)^α`-on-`n^{-s}` outcome; and the precise identity
`ζ^{(α)}(s)=Σ(−log n)^α n^{-s}` for `Re s>1`. The **fourth node — the Gamma/Mellin intertwiner — is NOT
wired up** in his work (he has Gamma integrals elsewhere but does not connect them). This is the same leg
our §G/§K identify as the missing analytic datum.

## 3. The honest takeaway

The fractional-`ζ` / Grünwald–Letnikov identity is **classical** (Guariglia et al.), appears in Fehlau's
2020 posts as student verification, and sits in the `Re s>1` Dirichlet region — **RH-inert**, exactly as our
§K concludes independently. The "succ" notation is standard Peano notation popularized memetically. Neither
the notation nor the fractional-calculus posts anticipate, or bear on, the RH content of this program; they
are a pleasant historical coincidence that the fractional-SUCC boundary `(I−S)^α` lands on the same
classical GL fractional-`ζ` formula.
