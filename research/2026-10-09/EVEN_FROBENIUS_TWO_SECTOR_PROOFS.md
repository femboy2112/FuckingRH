# Even-Frobenius twistor reconstruction: an exact local obstruction and a minimal two-sector repair

**Date:** 2026-10-09. **Status:** three unconditional complex-point/local-algebra theorems, a source-faithfulness falsifier, and an explicitly unproved RH identification. **RH OPEN.**
**Parent:** branch research/2026-10-09/adelic-reversal-hodge-interface at d8c36e00891ecc60e05fd24013b3f82e4df947e0, itself two commits ahead of main f2fe8b3f2e2953061bcc64c51c86521a66e72bcf (Round 064). Do not merge to main.

## 0. User hypothesis versus repairs

The user's original axis (conversation 2026-10-08 to 2026-10-09): semantic arithmetic forms are not their realization map; SUCC and shadow-SUCC should retain a causally accessible history; coherent time reversal should reassemble the *complete* shattered-teacup history; finite and Archimedean perspectives should obey compatible global laws; the missing arithmetic-square/dualizing/Hodge structure could supply the complete Weil sign. Earlier constraints: **read genuine multiplicativity; read no zeros or scattering phase; reject fake connected impulse at n=6, nonunit unramified alpha_2, and shifted log 2; retain true Lambda(p^k), p^{-k/2}, log p and the 2-adic tower.**

Our interpretive repair, not a user claim: test the newly described **signed Archimedean twistor real structure** against the genuine even-degree Frobenius n=2. Instead of falsely making even Frobenius an endomorphism of the signed real structure, attempt a correspondence between **two distinct real structures**, with spin/parity and Hecke phase kept as separate fibers. This is a bounded *local* attack, not a construction of the desired arithmetic self-product.

**Pre-registered outcomes (before testing):** H0, signed single-sector even map should fail; H1, a two-sector monoid action should close under composition; H2, the half-Jacobian should need a double cover for even n but that cover should not trivially solve spinor equivariance; H3, an even-step coarse view should lose a source orientation bit, and a tagged history should recover injectivity; H4, a Dirichlet phase must not be inserted in a holomorphic point map if its monoid law disagrees; H5, all kinematic positive forms should remain sign-blind, while genuine Euler-source tests reject Davenport-Heilbronn/fake 6. Counteroutcomes would refute or demand revision of the corresponding construction.

## 1. Primary-source boundaries and competing versions

- Connes–Consani, *Riemann-Roch for Spec Z* (2023), Theorem 1.2 / §5, constructs model-specific Serre/Pontryagin duality with dualizing module U(1)_(1/4) and canonical-divisor analogue K=-2{2}: https://arxiv.org/html/2205.01391v2 . Connes–Consani, *Riemann–Roch for the ring Z*, Comptes Rendus Math. 362 (2024), DOI https://doi.org/10.5802/crmath.543, refines the base. **Thus “no Riemann–Roch or dualizing object anywhere over Spec Z” is false.**
- Connes–Consani, *The Absolute Twistor Line and the Geometry of the Compactification of Spec Z* (arXiv 2609.00299; 2026-08-31), states in the primary abstract that its signed absolute Archimedean component has an intrinsic odd-integer Frobenius/Adams restriction: https://arxiv.org/abs/2609.00299 . The complex-point anti-holomorphic j_-(z)=-1/conj(z) is the **model tested here**. We do not claim a construction in that paper's signed absolute topos, nor that our two-sector model extends its sheaf theory.
- Connes–Consani, *On the Absolute Geometry of Spec Z* (arXiv 2606.06604, June 2026), gives genuine complex Tate periodic orbits p with log p periods: https://arxiv.org/abs/2606.06604 . Our complex-point P1 coverings are not those curves.
- Standard odd-ramification spin pullback condition R_f/2 is recorded in Giacchetto–Kramer–Lewanski, *A new spin on Hurwitz theory and ELSV via theta characteristics*, Selecta Mathematica (2025), Definition 4.2: https://doi.org/10.1007/s00029-025-01077-y .
- Deninger's foliated-cohomological strategy asks for a *positive* polarization compatible with the generator; an adjoint symmetry alone is not RH: https://ems.press/books/dms/246/4682 .
- Repo instructions: README and wiki/07 require claims to be proved/observed/conjectured/refuted with provenance and hostile controls. Neither main nor the two extra parent-branch files contain an AGENTS.md or CLAUDE.md; CURRENT_STATE.md and CLAIM_LEDGER.md remain Round-006-stale. Use main's CRUCIFIXION_LEDGER Round 064 and wiki/06 F2–F6 as current score. On main, R62 disproved the automatic positivity of bare chiral boundary curvature; R63 verified Mellin reversal is sign-blind and works for Davenport–Heilbronn; R64 recovered a function-field genus-one Hodge-index control without any number-field bridge.

## 2. Theorem: classification of signed real-structure-compatible monomial covers

Work on X = P1_C, initially on its dense chart C^×. For epsilon in {+1,-1}, define

  j_epsilon(z) = epsilon / conjugate(z).

These are anti-holomorphic involutions, extending across 0 and infinity. j_+ has the unit circle as fixed locus; j_- has **no fixed points**. Let

  f_(n,c)(z)=c z^n,  n in Z_{>=1}, c in C^×.

**Theorem 1 (exact).** f_(n,c) intertwines (X,j_epsilon) to (X,j_epsilon') iff

  epsilon' = epsilon^n  AND  |c|=1.

**Proof.** f_(n,c)(j_epsilon z)=c epsilon^n/conj(z)^n, whereas j_epsilon'(f_(n,c)z)=epsilon'/(conj(c) conj(z)^n). Equality for all nonzero z iff |c|^2 epsilon^n=epsilon'. Since |c|^2>0 and signs are ±1, both conclusions follow. Conversely they imply equality. The relations extend to P1. QED.

**Corollaries.** No even degree n can give an equivariant endomorphism of the *signed* j_- sector, regardless of scalar phase or amplitude c. All odd n with |c|=1 do. For n even the unique target type is **j_+**. This is stronger than noticing failure for the unphased map z↦z². These two real structures cannot be identified by a real isomorphism because their fixed loci differ.

**Minimal two-sector repair.** Define objects X_+,X_- and arrows f_n:X_epsilon→X_(epsilon^n), with c=1. Since f_m∘f_n=f_(mn) and (epsilon^n)^m=epsilon^(nm), this is a *strict action of the multiplicative monoid on the two-object correspondence category*. It preserves physical degree n exactly, in particular n=2,4,8,... . It is not an endomorphism monoid of the signed absolute twistor object, and no arithmetic self-product or Weil form follows.

## 3. Theorem: the double-cover spinor is necessary but insufficient

On C^× use the double cover z=w² with deck transformation d(w)=-w. Choose lifts

  tilde(j)_+(w)=1/conj(w),    tilde(j)_-(w)=i/conj(w).

They satisfy pi∘tilde(j)_epsilon=j_epsilon∘pi and

  tilde(j)_+² = identity,    tilde(j)_-² = deck d.

This is the local manifestation of real (+) versus quaternionic (-) half-spin reversal.

For f_n(z)=z^n, the square root of its Jacobian is on this cover

  sigma_n(w)=sqrt(n) w^(n-1).

**Theorem 2.** (i) sigma_m(w^n) sigma_n(w)=sigma_(mn)(w) exactly; (ii) sigma_n(-w)=(-1)^(n-1)sigma_n(w). Thus the spin Jacobian for even n is **deck-odd** and cannot descend as a scalar function on the z-plane, although it is single-valued on the double cover. The ramification divisor of z↦z^n on P1 is (n-1)([0]+[infinity]); its branch-supported half is integral exactly for odd n. Do NOT turn this local obstruction into the false claim that the total line bundle has no square root.

The square of a compatible antiunitary lift on the rank-two half-spin model is encoded by J_- v=A_- conjugate(v), J_+ v=A_+ conjugate(v), with

  A_-=[[0,-1],[1,0]], A_+=[[0,1],[1,0]].

Then J_-²=-I and J_+²=+I. If a complex-linear T obeyed T J_-=J_+ T, composing twice would give -T=T, hence T=0.

**Theorem 3 (strict spinorial no-go).** There is **no nonzero strict complex-linear intertwiner** between these chosen quaternionic and real half-spin reversals. This does NOT refute the base real-morphism f_2:X_-→X_+; it refutes the naive promotion to an untwisted spinor intertwiner. A graded/deck-twisted correspondence must be constructed rather than merely asserted. SymPy independently finds rank 8 for the eight-real-variable intertwiner system, nullity 0.

The deck sign is itself a coherent cocycle: set t_+=1,t_-=i. Then kappa(n,e)=t_e^n/t_(e^n) in {±1}, and

  kappa(mn,e)=kappa(n,e)^m kappa(m,e^n).

This follows algebraically and was tested on fresh composite-degree holdouts. It gives a *candidate obstruction bookkeeping*; it does not supply a positive polarization.

## 4. A literal time-reversal information defect

On the basis |epsilon,k>, define the coarse degree map |epsilon,k>↦|epsilon^n,nk>. For even n both |+,k> and |-,k> land in |+,nk>; its linearization has a kernel spanned by |+,k>-|-,k>. **A coarse inverse cannot reconstruct the source orientation.** Attach a source-history tag: |epsilon,k>↦|epsilon^n,nk;epsilon>. The images of distinct basis states are now orthogonal: a one-step Hilbert isometry. The tagged map is not onto and does not automatically supply a full unitary dynamics. Multi-step reconstruction must preserve a suitable history register rather than repeatedly deleting it.

This is the coherent shattered-teacup *kinematics* for the signed/unsigned transition. The generic missing-norm square of an isometry is still source-blind and cannot become Weil positivity by naming it so.

## 5. Hecke-phase falsifier: point-map phases are the WRONG implementation

For g_n(z)=c_n z^n, composition requires

  c_(mn)=c_m c_n^m

when g_m∘g_n=g_(mn). This is **not** ordinary Hecke-character multiplicativity c_(mn)=c_m c_n.

For the genuine quartic Dirichlet character mod 5, chi(2)=i, chi(3)=-i and chi(6)=1:

  g_3∘g_2 has scalar (-i)*i³ = -1;
  g_2∘g_3 has scalar i*(-i)² = -i;
  chi(6) = chi(2)chi(3) = +1.

So incorporating chi(n) as a *scalar coefficient in the point map* breaks the multiplicative monoid and even commutativity. **Refuted construction.**

**Revision.** Keep the covering map f_n(z)=z^n unphased. Put chi(n) in a separate one-dimensional Hecke fiber/local system, with character twist on pullback operators L_n=chi(n) f_n^*. Then L_m L_n=chi(m)chi(n) f_(mn)^* for ordinary multiplication (orientation conventions for pullback must be fixed). Anti-linear reversal conjugates fiber phases, so a genuinely complex character also requires its conjugate-character sector, not identification chi=conj(chi). This is a proposed *source-compatible tensor layer*, not a completed operator on an arithmetic surface.

Arithmetic source calibration remains separate: in the convolution logarithm of genuine Dirichlet coefficients, connected atoms vanish at every mixed composite; at 6 this coefficient is zero. For the normalized Davenport–Heilbronn conjugate-character mixture with kappa=sqrt(1+phi²)-phi and phi=(1+sqrt 5)/2, the connected log coefficient is 1+kappa²=1.080700903149283... . Changing a genuine character's coefficient at n=6 by .03 changes its connected logarithm there by exactly .03. This DOES distinguish multiplicativity, but the twistor geometry **alone** does not. Similarly an unramified |alpha_2| !=1 fails the unitary Hecke fiber test; shifted log 2 fails the separately pinned real Tate period/physical degree clock. Do not claim twistor covariance itself enforces the Weil half-density p^(-k/2).

## 6. Three construction/falsification/revision rounds

**Round A — naive single signed real structure.** Prediction: even degree should expose an obstruction. Construction f_(2,c) on X_-. Exact obstruction |c|²=-1 disproves every scalar rescue. Revise to a target X_+ rather than pretending j_- commutes with f_2.

**Round B — two sectors and spin.** Prediction: both signed and unsigned sectors restore multiplicative composition; may repair half-canonical transport. The base action passes. The square-root Jacobian becomes deck-odd for even n, and the strict real/quaternionic spinor intertwiner is ZERO. Revise to a graded spin/deck correspondence with environmental history, not a single untwisted line or a positive Gram.

**Round C — arithmetic source graft.** Prediction: geometric scalar phases might encode a genuine Hecke character and hence the needed zero-free source. They fail at (2,3). Revise to a separate multiplicative local-system twist; check exact convolution-logarithmic source separately. This passes the source discrimination test at 6, nonunit alpha_2 and shifted degree clocks, but the completed Weil identification and independent Hodge-index sign remain **UNVERIFIED**. The generic twistor construction also works for non-prime degree 6 and is not an RH discriminator on its own.

**Known-result controls:** odd-degree spin pullback, Riemann–Hurwitz, proper character multiplication, source logarithm. **Negative controls:** n=2 on single signed sector, even-n scalar-spin descent, strict quaternionic-to-real intertwiner, character in monomial coefficient, conjugate-character mixture, fake n=6, nonunit alpha_2, shifted log2. **Fresh holdouts** beyond calibration degrees 1..6: n=7,8,9,10,11,12,15,21,22,25,30; includes prime powers, coprime mixed composites, odd and even. No fresh test uses a zeta zero.

## 7. RH connection: exact boundary rather than a promised bridge

The locally repaired object provides geometric duality *and* a forced two-sector history, **but no nonnegative arithmetic intersection form**. In fact, the quaternionic/real distinction shows why simply transporting a positive metric across degree-2 cannot be assumed: no strict spinor intertwiner exists. A forced extra sector/graded twist is necessary.

The fourth gate would require ALL of the following, with independent sources and correct topology:
1. an actual absolute self-correspondence host, dualizing complex and degree-2/odd Frobenius correspondence on every finite place and infinity;
2. a globally defined Hecke character local system (including conjugation) and real/finite half-density, physical log p, exact Lambda and no false scalar connected 6/ratio atoms;
3. a source-derived degree-zero correspondence sector and *exact* pairing pushforward equal to the complete Q_L=P_L-K_L including pole, Gamma, origin and prime terms;
4. an independently proved Hodge-index/positive polarization on the completed primitive sector, with form-domain and infinite-wavefront controls.

Connes–Consani's curve-level RR/Serre duality does not imply any of these four jointly. A locally repaired spin-cover diagram is **not** the dualizing sheaf of Spec Z ×_(F1) Spec Z. An automatic positive source Gram and a bounded information-loss square are generic and may work for Davenport–Heilbronn; their existence is not RH progress.

## 8. Reproducibility and calibration

Scripts on this branch:
- scripts/twistor_even_frobenius_probe.py : standard-library source and twistor checks, seed 20261009, 60-term Dirichlet-convolution cutoff;
- scripts/twistor_spin_intertwiner_exact.py : exact SymPy linear system and parity audit.

Executed locally before publication using the mathematically equivalent local probes; committed command/output manifest is kept in research/2026-10-09/EVEN_FROBENIUS_RESEARCH_HANDOFF.md. The first exploratory probe **failed** because its expected conjugate-mixture coefficient at n=4 was incorrectly copied from the genuine character: it is -1 for the 50/50 mixture, not -1/2 (which is chi mod 5). After correcting the expectation, it passed. This is a test-harness mistake, not a new counterexample. No GitHub Actions run or entire-repository pytest run is claimed.

## Claim ledger

| Claim | Status |
|---|---|
| Classification f_(n,c): epsilon' = epsilon^n, |c|=1 | **DISCLOSED** (elementary proof) |
| No scalar signed j_- even-degree endomorphism | **DISCLOSED** |
| Two-sector base correspondence is compositional | **DISCLOSED** |
| Double-cover half-Jacobian composition, parity, and deck sign | **DISCLOSED** |
| No nonzero strict quaternionic-to-real spinor intertwiner | **DISCLOSED** (proof + exact linear algebra) |
| Even coarse map loses orientation; history-tagged one-step map is an isometry | **DISCLOSED** |
| Character phases used as monomial point-map scalars form a Hecke monoid | **REFUTED**, mod-5 (2,3) |
| Separately twisted Hecke fibers and connected source detect genuine arithmetic | **DISCLOSED locally**; no global sheaf supplied |
| This local correspondence supplies Q_W and an independent Hodge sign | **UNVERIFIED**; no such construction given |
| RH proved or approached monotonically | **NO** |

**Next verdict-changing experiment:** construct an honest graded dualizing/Hecke correspondence for the degree-2 *map of the two real-structure objects*, with an explicitly defined boundary trace (not a chosen scalar phase) and verify its local Gamma first three jets. Then independently compute its 2,3,6 connected-source trace and reject any new log6 or log(3/2) atom. If that passes, compare the *full* completed Weil form, including the negative polar debit, on an exact domain. Without that trace identification and independent polarization, the current apparatus is stage reconstruction, not RH progress.
