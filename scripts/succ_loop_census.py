#!/usr/bin/env python3
"""Bounded census of rationally closed SUCC/FUCC words.

This is a finite structural probe, not evidence for RH.  It deliberately
removes immediate rational backtracking g,g^{-1}.  Words are then classified
at three resolutions:

  1. terminal support cylinder (r,M);
  2. cumulative support-filtration ((r_j,M_j))_j;
  3. conductor-growth profile (M_j)_j.

The point is to test whether terminal support alone is too coarse to retain
chronological information.
"""
from __future__ import annotations

from collections import defaultdict

from succ_loop_undertones import Affine, word_support


GENERATORS = {
    "S+": Affine.make(1, 1, 1, "S+"),
    "S-": Affine.make(1, -1, 1, "S-"),
    "M2": Affine.make(2, 0, 1, "M2"),
    "D2": Affine.make(1, 0, 2, "D2"),
    "M3": Affine.make(3, 0, 1, "M3"),
    "D3": Affine.make(1, 0, 3, "D3"),
}

INVERSE = {
    "S+": "S-",
    "S-": "S+",
    "M2": "D2",
    "D2": "M2",
    "M3": "D3",
    "D3": "M3",
}


def closed_words(max_length: int = 7):
    loops = []

    def visit(target_length: int, prefix: list[str]) -> None:
        if len(prefix) == target_length:
            word = [GENERATORS[g] for g in prefix]
            support, final, prefixes = word_support(word)
            if (
                support is not None
                and final.a == 1
                and final.b == 0
            ):
                loops.append((tuple(prefix), support, prefixes))
            return

        for g in GENERATORS:
            if prefix and INVERSE[prefix[-1]] == g:
                continue
            visit(target_length, prefix + [g])

    for length in range(2, max_length + 1):
        visit(length, [])
    return loops


def census(max_length: int = 7):
    loops = closed_words(max_length)
    terminal = defaultdict(list)
    filtration = defaultdict(list)
    growth = defaultdict(list)

    for word, support, prefixes in loops:
        terminal[support].append(word)
        filtration[tuple(p[2] for p in prefixes)].append(word)
        growth[tuple(p[2][1] for p in prefixes)].append(word)

    return loops, terminal, filtration, growth


def main() -> None:
    loops, terminal, filtration, growth = census(7)

    assert len(loops) == 236
    assert len(terminal) == 17
    assert len(filtration) == 91
    assert len(growth) == 66

    print("Alphabet: S+, S-, M2, D2, M3, D3")
    print("Immediate rational inverse pairs removed.")
    print("Closed non-backtracking words of length <= 7:", len(loops))
    print("Distinct terminal support cylinders:", len(terminal))
    print("Distinct cumulative support filtrations:", len(filtration))
    print("Distinct conductor-growth profiles:", len(growth))
    print()
    print("Shortest representative of each terminal support class:")
    reps = []
    for support, words in terminal.items():
        rep = min(words, key=lambda w: (len(w), w))
        reps.append((support[1], support[0], len(rep), rep))
    for modulus, residue, length, rep in sorted(reps):
        print(f"  x == {residue} (mod {modulus}): L={length}  {' '.join(rep)}")

    print()
    print("Interpretation:")
    print("  terminal support is a strong compression (236 -> 17),")
    print("  but it discards chronology: retaining the cumulative support")
    print("  filtration separates 91 classes.  Therefore an RH-facing")
    print("  loop theory should keep support holonomy AND support history.")


if __name__ == "__main__":
    main()
