# Template — rigorous mathematical claim + provenance

Copy this into every load-bearing new research note/PR. This is a **research quality gate**, not a claim of peer review or of solving RH.

## Identity

- **Claim ID:** stable ID, linked from \`research/audits/2026-10-07/RH_CLAIM_PROVENANCE_LEDGER.md\`.
- **Title / exact theorem:** quantifiers, parameter ranges, operator topology, core/domain, normalization.
- **Claim class:** external theorem | in-repo derived | independent finite check | observed-only | RH-equivalent reformulation | conjecture | refuted.
- **Originating idea:** user hypothesis/analogy, assistant proof derivation, inherited Claude/Astra branch, or cited literature — **separate these**.
- **First-derivation ref:** exact git branch, commit SHA and file section.
- **Correcting refs:** subsequent commits that weakened/repaired claims.
- **Primary source:** author, title, stable URL, publication/arXiv **version**, theorem or equation number and page.

## Proof

1. **Definitions and source normalization:** include all sign and \(2\pi\) conventions.
2. **Independent derivation:** complete mathematical proof, with lemmas and domain justifications.
3. **External mathematical tools:** name theorem/source and conditions; do not claim classical techniques as novel.
4. **Dependency DAG:** identify any PNT, Hardy space, compactness, Weil, Suzuki, or RH-equivalent hypotheses.
5. **Unpaid step:** state the *exact* inequality/limit/spectral estimate still required; mark RH-equivalent subclaims.
6. **Hostile counterexamples:** fake primes/composites, off-axis zero quartets, endpoint/UV and full \(\omega>0\) tests.
7. **Negative controls:** show why the claimed signal is not automatic for arbitrary positive Gram, finite unitary, CRT, or probability source.

## Execution

- **Test code path:** 
- **Run command:** 
- **Interpreter/dependencies & versions:** 
- **Executed?** yes/no; local/CI; time/date; exit status; relevant stdout or artifact.
- **Independence:** independent mathematical computation vs same closed-form transcription vs independent paper.
- **Scope:** finite check, interval certificate, exact theorem, or all-horizon argument.
- **Any mutation test failed?** list result and how claim changed.
- **Input zeros?** yes/no; zero-ordinate fitting disqualifies a purported independent RH proof.

## Final status

- [ ] Source and version verified.
- [ ] Statement precisely scoped.
- [ ] Proof independently re-derived or marked unreviewed.
- [ ] Tests actually executed, or marked unexecuted.
- [ ] Provenance recorded in both the note and claim ledger.
- [ ] RH-equivalent conclusion **not** assumed upstream.
- [ ] No invented priority or inference from connected-account Git commit author.
- [ ] Novelty/proof-bearing consequence separated from coordinate repackaging.

**Conventions:** A complete RH proof requires the full global positivity/innerness gate, not finite positivity, unimodularity, compact spectrum, or an RH-equivalent restatement.
