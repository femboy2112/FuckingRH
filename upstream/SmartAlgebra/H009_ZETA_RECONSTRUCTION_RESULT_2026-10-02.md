# H-009 result: blind local/global zeta reconstruction — RECONSTRUCTED

**Date:** 2026-10-02. **Target** (blind, strict frozen rule — `BLIND_TARGET.md`):
`C: y^2 = x^5 + 4x^4 + x^2 + 4x + 1` over `F_5`, genus 2. **Graded run:**
`tests/test_h009_zeta_reconstruction.py`. **Verdict: RECONSTRUCTED** — both independent
routes build the same numerator, and every hostile control fires.

## The reconstruction

| quantity | value |
|---|---|
| point counts `N_1..N_4` | `11, 31, 101, 651` |
| **Route A** (point counts → full Newton) | `P = 1 + 5T + 15T^2 + 25T^3 + 25T^4` |
| **Route B** (host-bound local Euler product) | `P = 1 + 5T + 15T^2 + 25T^3 + 25T^4` |
| routes agree | **yes** |
| self-dual (functional equation, downstream) | yes (`c_4=25=5^2 c_0`, `c_3=25=5 c_1`) |
| purity (exact PSD localizer) | **PURE** |
| Euler admissibility (finite horizon) | **ADMISSIBLE** |
| all host bindings pass | yes |
| all local decompositions re-derive | yes |

Route B assembled the Euler product over every base place of degree `<= 4` and `oo`; each
place's completion node was bound to its local host by an H-008 witness, and a fiber
entered the product only after admission tied together (i) its decomposition is of the
**target** `f` at **this** place and re-derives, (ii) the context artifact describes this
place, (iii) the witness is for this place's completion node, and (iv) the host binding
passes. The two routes share no construction code (verified by profiler trace and by the
monkeypatch controls).

## Hostile controls

The preregistered controls (`PREREGISTRATION.md` §7, frozen controls 1–11, mapped here to
C2–C11) all fired. **C5' and C5'' were not preregistered**: they were added *after the
result*, when the independent grader found that a host binding was not tied to the fiber it
gated (see "Independent grader" below). They are post-result grader-hardening controls, and
they are marked as such in the table.

| control | outcome |
|---|---|
| **C2** Route-B independence (monkeypatch `count_points`/`l_polynomial`/… to raise) | Route B still builds `P` ✓ |
| **C3** Route-A independence (monkeypatch `place_decomposition`/`verify_host_binding` to raise) | Route A still builds `P` ✓ |
| **C4** forged local decomposition (flip SPLIT→INERT) | `AssemblyRefused` — math verifier (FIBER) ✓ |
| **C5** tampered witness (host swapped) | binding fails → `AssemblyRefused` (HOST) ✓ |
| **C5'** *(post-result grader hardening, not preregistered)* *valid* binding for the **wrong place** attached to a fiber | `AssemblyRefused` — the artifact does not describe this fiber's place ✓ |
| **C5''** *(post-result grader hardening, not preregistered)* a fiber decomposing a **different curve** | `AssemblyRefused` — admission ties the fiber to the target `f` ✓ |
| **C6** remove one local factor | `P` changes → routes disagree ✓ |
| **C7** duplicate one local factor | `P` changes → routes disagree ✓ |
| **C9** pure-but-Euler-impossible distractor `(1+3T+3T^2)^2` | purity PASS, Euler **NOT_ADMISSIBLE** ✓ |
| **C10** functional-equation visibility | a non-self-dual mutation of `P` is detected downstream ✓ |
| **C11** truncation horizon (degree `> 2g` places) | no effect on `P` (lemma, pinned) ✓ |

C4, C5, C5', C5'' together establish that the math content **and** the host provenance are
*each* load-bearing, and that a binding is **tied to the fiber it gates**: a *valid* host
binding for the wrong place, or a decomposition of the wrong curve, is refused — not
silently admitted. (An independent grader found the earlier version admitted a valid
binding for the wrong place; this is the fix.)

## Claim (deliberately weak)

> SmartAlgebra independently reconstructed the zeta numerator of a withheld genus-2 curve
> from two different exact data presentations — extension-field rational-point counts, and
> host-bound local place decomposition / Euler factors — reaching the same `P`, with host
> provenance load-bearing on the local route and each local fiber's binding tied to its
> place and to the target curve.

This is an **architecture** result. It is **not** a mathematical discovery (the curve and
Weil purity are inputs), carries **no** number-field RH implication, and whether it counts
as the repository's Section-6 STRONG PASS is for the existing protocol to decide, not
asserted here. Frozen `MathematicalNode` / `Transformation` / v0.1-receipt records are
untouched; the host-binding layer is the orthogonal `host-binding-witness.v0.1`.

## Independent grader

A read-only independent grader replayed both routes from its own code (matching `P` and
`N`), confirmed route independence by profiler trace (no cross-route calls; agreement is a
post-hoc `==`), found no stored target polynomial and no target-specific branch, and
confirmed the blind-selection arithmetic. It flagged two issues, both now resolved: (1) the
host binding was not tied to the fiber it gated — fixed (C5'/C5'' above); (2) the blind
target used a post-SHA exclusion — corrected to the strict frozen rule (`BLIND_TARGET.md`).

## Boundary / residual

* One target, one genus, `q=5`. Not a family claim (the next probe is an H-009 family
  generalization).
* Curve existence is supplied by the input model; nothing certifies realizability beyond
  the necessary purity + Euler-admissibility conditions.
* The host *fan* still does not itself encode the decomposition (HPA-021); the binding is
  carried by the H-008 witness + the fiber artifact, not by the host vocabulary.
