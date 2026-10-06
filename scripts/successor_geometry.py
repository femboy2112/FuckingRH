"""Exact abstract successor work, Pareto programs, and history cocycles.

No wall-clock timing. See SUCCESSOR_OPERATIONAL_GEOMETRY.md for the machine.
"""
from __future__ import annotations
from dataclasses import dataclass
import argparse
import json
from pathlib import Path


@dataclass(frozen=True)
class Program:
    value: int
    work: int
    control: int
    length: int
    expression: str


def one():
    return Program(1, 1, 1, 1, '1')


def succ(a):
    return Program(a.value+1, a.work+1, a.control+1, a.length+1,
                   f'S({a.expression})')


def add(a, b):
    return Program(a.value+b.value, a.work+b.work+b.value,
                   a.control+b.control+b.value+2, a.length+b.length+1,
                   f'({a.expression}+{b.expression})')


def mul(a, b):
    n, m = a.value, b.value
    return Program(n*m, a.work+b.work+n*m,
                   a.control+b.control+n*m+2*m+2, a.length+b.length+1,
                   f'({a.expression}*{b.expression})')


def add_steps(n, m):
    """Actual small-step addition loop: (result, successor work, controls)."""
    if min(n, m) < 0:
        raise ValueError('natural inputs only')
    value, work, control = n, 0, 0
    while True:
        control += 1
        if m == 0:
            return value, work, control
        value += 1  # the only value-creating arithmetic instruction
        work += 1
        m -= 1      # consume an existing unary input cell, not new arithmetic


def mul_steps(n, m):
    """Repeated addition, including terminal and loop control steps."""
    if min(n, m) < 0:
        raise ValueError('natural inputs only')
    value, work, control = 0, 0, 0
    while True:
        control += 1
        if m == 0:
            return value, work, control
        value, w, c = add_steps(value, n)
        work += w
        control += c
        m -= 1


def prune(programs):
    """Pareto frontier in (description length, work, control), exact integers."""
    unique = {}
    for p in programs:
        unique.setdefault((p.length, p.work, p.control), p)
    keep = []
    for key, p in sorted(unique.items()):
        if not any(q.length <= p.length and q.work <= p.work
                   and q.control <= p.control for q in keep):
            keep.append(p)
    return keep


def frontiers(limit):
    if limit < 1:
        raise ValueError('positive limit required')
    out = {1: [one()]}
    for n in range(2, limit+1):
        candidates = [succ(a) for a in out[n-1]]
        for i in range(1, n):
            candidates.extend(add(a, b) for a in out[i] for b in out[n-i])
        for i in range(2, n):
            if n % i == 0:
                candidates.extend(mul(a, b) for a in out[i] for b in out[n//i])
        out[n] = prune(candidates)
    return out


@dataclass(frozen=True)
class Edge:
    label: str
    source: int
    target: int
    work: int
    control: int
    length: int


def reduce_history(history):
    """Free-groupoid reduction; (edge, orientation +/-1) letters."""
    stack = []
    current = None
    for edge, sign in history:
        if sign not in (-1, 1):
            raise ValueError('orientation must be +/-1')
        source, target = ((edge.source, edge.target) if sign == 1
                          else (edge.target, edge.source))
        if current is not None and source != current:
            raise ValueError('noncomposable history')
        current = target
        if stack and stack[-1] == (edge, -sign):
            stack.pop()
        else:
            stack.append((edge, sign))
    return tuple(stack)


def action(history):
    """Signed excess-work, control and length additive cocycles."""
    return tuple(sum(sign*x for e, sign in history
                     for x in [(e.work-(e.target-e.source), e.control,
                                e.length)[axis]]) for axis in range(3))


def finite_arrow(source, target, history, modulus=7):
    """A finite quotient control: pair groupoid times (Z/modulus Z)^3."""
    if modulus < 2:
        raise ValueError('modulus >=2 required')
    history = tuple(history)
    reduce_history(history)  # validates composability before cancellations
    if history:
        e, sign = history[0]
        start = e.source if sign == 1 else e.target
        e, sign = history[-1]
        end = e.target if sign == 1 else e.source
        if (start, end) != (source, target):
            raise ValueError('history endpoints do not match')
    elif source != target:
        raise ValueError('empty history must be an identity')
    return source, target, tuple(x % modulus for x in action(history))


def compose_finite(first, second, modulus=7):
    if first[1] != second[0]:
        raise ValueError('noncomposable finite arrows')
    return first[0], second[1], tuple((x+y) % modulus
                                    for x,y in zip(first[2],second[2]))


def run(limit=64):
    return {'scope': f'exact restricted positive grammar, n<= {limit}',
            'wall_clock_used': False,
            'frontiers': {str(n): [p.__dict__ for p in ps]
                          for n, ps in frontiers(limit).items()}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=64)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(run(args.limit), indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text)
