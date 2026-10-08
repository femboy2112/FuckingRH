> **2026-10-07 hostile correction:** The rank-one SUCC carry defect derived below is **exact for the chosen global mixed-radix section**, but **is not a representation/gauge-invariant arithmetic curvature**. An intrinsic local \(p\)-adic digit can give defect rank \(L/p^{v_p(L)}\) instead. The invariant theorem is the split/nonsplit class of the cyclic extension \(0\to\mathbb Z/p\to\mathbb Z/pL\to\mathbb Z/L\to0\), proved in [INTRINSIC_CARRY_EXTENSION_CLASS.md](INTRINSIC_CARRY_EXTENSION_CLASS.md): new primes split by CRT; higher prime powers carry a nontrivial extension. Both isometric births remain valid; neither gives RH. Do not promote the rank-one formula below without its section hypothesis.

# Fresh-digit isometric actualization and exact rank-one SUCC carry

**Date:** 2026-10-07
**Branch:** \`research/causal-filtration-energy-2026-10-07\`
**Status:** exact finite Hilbert-space theorem and source-parameterized chronological construction. **RH remains OPEN.**

## Provenance and priority

- **User-origin insight:** Only information already encountered at the wavefront event can affect the next actualization; the support state grows through fresh prime-power digits, and carry is the interaction between neighboring event histories.
- **Derivation in this note:** GPT-6 in direct response to that insight, using standard normalized-Haar CRT embeddings, elementary discrete Fourier characters, and shift/carry identities.
- **Previously known/in-repo:** LCM prime-power births, \(\omega\)-conductor factor \(1-p^{-2\omega}\), Gram innovation/superconnection (2026-10-07 repo notes), fresh-environment correction from the imported \`CUBE_ATOM_CRITICAL_AUDIT_IMPORTED.md\`, SUCC/Cuntz/affine carry from Round005–006. This is a **specific exact assembly of established pieces**, not a priority claim over these tools.
- **Primary RH criterion:** Masatoshi Suzuki, *A canonical system of differential equations arising from the Riemann zeta-function*, arXiv:1204.1827v2, Proposition 1.2 and Theorem 2.2; real-axis unitarity/finite causality is insufficient.
- **Finite controls:** \`scripts/rh_fresh_digit_isometry.py\`, independently executed in an isolated Python/NumPy container before commit. See \`CAUSAL_FILTRATION_EXECUTION.md\`; no CI or independent peer review claimed.

## 1. The fresh digit is forced by the LCM event

Let \(L_n=\operatorname{lcm}(1,\ldots,n)\). At a prime-power event \(n=p^k\),

\[
L_n=pL_{n-1}.
\]

This reveals exactly one new base-\(p\) digit over every old residue class. It is known using only \(L_{n-1}\) and the encountered \(n\); no future information is invoked.

Set \(L=L_{n-1}\). The refined Hilbert space \(H_{pL}=L^2(\mathbb Z/pL\mathbb Z,\text{normalized Haar})\) is naturally identified, relative to the canonical representatives \(0\le r<pL\), with

\[
\boxed{H_{pL}\cong H_L\otimes\mathbb C^p}
\]

using

\[
r=r_0+kL,\qquad 0\le r_0<L,\quad 0\le k<p.
\]

On \(\mathbb C^p\), use normalized Haar inner product \(p^{-1}\sum_{k=0}^{p-1}\overline u_kv_k\).

## 2. Exact old and new orthogonal embeddings

Let

\[
\zeta_p=e^{2\pi i/p}.
\]

Define \(J,V:H_L\to H_{pL}\) by

\[
(Jf)(r_0+kL)=f(r_0),
\]

\[
(Vf)(r_0+kL)=\zeta_p^k f(r_0).
\]

Then, exactly,

\[
\boxed{J^*J=V^*V=I,\qquad J^*V=0.}
\]

Proof: normalized Haar averages over the \(p\) lifts give \(p^{-1}\sum1=1\) for norms and \(p^{-1}\sum\zeta_p^k=0\) for the cross term.

The \(J\) channel retains exactly the previously accessible residue information. The \(V\) channel occupies one genuinely fresh Fourier digit of the refinement. This uses a *chosen* nontrivial Fourier character; for \(p>2\), other characters also exist and are not automatically physically equivalent.

## 3. The source-matched isometric birth

For every \(\omega\ge0\), define

\[
\boxed{
W_{L,p,\omega}
=
p^{-\omega}J+
\sqrt{1-p^{-2\omega}}\,V.
}
\]

Then

\[
\boxed{
W_{L,p,\omega}^*W_{L,p,\omega}
=
p^{-2\omega}I+(1-p^{-2\omega})I=I.
}
\]

So **each actualization is a genuine isometry**, not a merely positive source.

For a normalized old state \(f\), the orthogonal projection measurements of its refined image give

\[
\boxed{
\Pr(\text{inherited digit mode})=p^{-2\omega},
}
\]

\[
\boxed{
\Pr(\text{fresh innovation mode})=1-p^{-2\omega}.
}
\]

This is **exactly Suzuki's local conductor-support factor**.

As \(\omega\downarrow0\), the new-channel probability is

\[
1-p^{-2\omega}=2\omega\log p+O(\omega^2),
\]

and the amplitude scales as \(\sqrt{2\omega\log p}\), not as \(O(\omega)\). Thus this construction correctly evades the prior smooth finite-dimensional unitary activation no-go.

### Historical/causal interpretation

At each prime-power birth, a new tensor digit is introduced; \(W\) factors the state into the old state and an independently prepared two-mode vector in that **fresh** digit. Repeated refinements **without intervening carry mixing** produce independent fresh-digit measurement bits (as in the imported Markov audit). Do not claim independence persists under arbitrary subsequent SUCC/carry interactions.

Composition of the \(W\)'s along any fixed finite sequence of actual prime-power events is again isometric:

\[
\boxed{\|W_j\cdots W_1f\|=\|f\|.}
\]

This is an exact **causal, local, norm-preserving actualization law**, for the specified finite construction.

## 4. SUCC does not commute with the innovation: the entire defect is one carry boundary

Let \(S_L\) and \(S_{pL}\) be cyclic successors acting by

\[
(S_Lf)(r_0)=f(r_0-1\bmod L).
\]

The inherited embedding intertwines successor exactly:

\[
\boxed{S_{pL}J=JS_L.}
\]

For the new Fourier digit, a direct calculation gives

\[
\boxed{
[(S_{pL}V)-(VS_L)]f(r_0+kL)
=
(\zeta_p^{-1}-1)\,
\mathbf1_{\{r_0=0\}}\,
\zeta_p^k f(L-1).
}
\]

The defect has rank one as a map \(H_L\to H_{pL}\): only the old terminal residue \(L-1\) is involved, and its image lies in the new Fourier character over \(r_0=0\). No other state or future residue is touched.

Consequently,

\[
\boxed{
S_{pL}W_{L,p,\omega}-W_{L,p,\omega}S_L
=
\sqrt{1-p^{-2\omega}}\,
(S_{pL}V-VS_L).
}
\]

Since the boundary map above has norm \(1\) after dividing out \(\zeta_p^{-1}-1\), its exact operator norm is

\[
\boxed{
\bigl\|S_{pL}W_{L,p,\omega}
-W_{L,p,\omega}S_L\bigr\|
=
2\sin\frac{\pi}{p}
\sqrt{1-p^{-2\omega}}.
}
\]

**This is an exact finite carry defect, not an invented plaquette curvature.**

At \(\omega=0\), the map is the inherited old-data embedding and commutes with SUCC. The new channel opens with the correct square-root event amplitude, and the sole noncommutation is concentrated at the radix carry.

## 5. What it does NOT establish

This is a **finite local isometric lift**. It does not demonstrate that the *completed* scalar Suzuki/Gamma transfer is inner for every \(\omega>0\).

In particular:

- The choice of nontrivial Fourier digit \(\zeta_p^k\) is a modeling choice; another digit character changes the defect norm. A physical observation map must make this choice invariant or derive it.
- The probability \(1-p^{-2\omega}\) is one **local** factor. The full conductor coefficient additionally has \(n^{\omega-1/2}\), and the pole/Gamma sector has signed global corrections. These are **not** produced by \(W\) alone.
- A product of isometries preserves internal norm without making an arbitrary coherent scalar readout contractive.
- Internal carry commutators can generate mixed-conductor channels. A completed physical observation must eliminate forbidden extra \(\log(pq)\) and \(\log(p/q)\) Weil atoms.
- At \(\omega=1/2\) local passivity is especially transparent, but Suzuki's RH condition requires **all \(\omega>0\)**, not just the unconditional safe sector.

Thus a genuine proof would require an independently derived observation/storage operator \(\mathcal O_\omega\) producing exactly the true completed \(\Theta_\omega\), with a causal Hardy contraction estimate on all horizons. This remains unproved.

## 6. Proof-bearing next test

**Test the exact two-event square.** Given different prime event multipliers \(p,q\), compare the two chronological compositions into \(H_{pqL}\):

\[
W_{pL,q,\omega}W_{L,p,\omega}
\qquad\text{versus}\qquad
W_{qL,p,\omega}W_{L,q,\omega}.
\]

Use the same old input and final common arithmetic residue coordinates. Calculate their difference, its dependence on the choice of digit Fourier character, and its exact conductor/Fourier support.

No argument may interpret a nonzero difference as a physical curvature observable until **invariance under permitted digit-gauge choices** and **exact agreement with the completed Weil prime/Gamma coefficients** have both been checked.

This is the first concrete place where *strictly causal, isometric actualization* can produce a nontrivial chronological defect from source-derived data, while remaining falsifiable.

## 7. Claim ledger

**PROVED / CLASSICAL:** old/new Haar embeddings orthogonal; \(W\) is isometric; inherited successor intertwines; innovative successor has rank-one carry defect with the exact norm above; finite chronology preserves internal norm.

**PROVENANCE-SPECIFIC:** user-origin no-lookahead wavefront concept; exact local \(\omega\) innovation weight from Suzuki coefficient; Cuntz/affine carry lineage from previous repo rounds; classical finite Fourier/Hilbert algebra combined in this note.

**UNVERIFIED / RH:** a canonical gauge-independent physical observation of the chronological defect; the all-\(\omega\) completed Gamma/pole transfer; Hardy innerness; RH.
