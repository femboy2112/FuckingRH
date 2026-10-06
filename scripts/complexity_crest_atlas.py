"""Finite exact arithmetic atlas and predeclared exploratory controls.

Integer complexity: exhaustive root-decomposition dynamic programming.
Addition chains: exhaustive iterative deepening over ALL preceding pairs,
not star chains. Floating summary statistics make no asymptotic claim.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction
import json
import math
from pathlib import Path
import random
from flint import arb, ctx
from scripts.event_dynamics import arch_prime
from scripts.prime_towers import tower_totals
from scripts.suzuki_psi import primes_up_to


def integer_complexities(limit):
    if limit < 1:
        raise ValueError('positive limit required')
    cost = [0] * (limit+1)
    witness = [None] * (limit+1)
    cost[1], witness[1] = 1, ('one',)
    for n in range(2, limit+1):
        choices = [(cost[a]+cost[n-a], '+', a, n-a)
                   for a in range(1, n//2+1)]
        choices.extend((cost[a]+cost[n//a], '*', a, n//a)
                       for a in range(2, math.isqrt(n)+1) if n % a == 0)
        c, op, a, b = min(choices)
        cost[n], witness[n] = c, (op, a, b)
    return cost, witness


def addition_chain(n):
    """Return a globally shortest increasing addition chain and search counts.

    Any positive addition-only chain can be sorted and duplicates removed:
    both summands of each element are smaller than that element. Values
    beyond n cannot contribute to n. Thus this search covers all optima.
    The only nontrivial pruning is the proven remaining-doubling bound.
    """
    if n < 1:
        raise ValueError('positive target required')
    if n == 1:
        return [1], {'lower_bound': 0, 'rejected_depths': [], 'visited': 1}
    lower = (n-1).bit_length()
    rejected, visited = [], 0

    def search(chain, remaining):
        nonlocal visited
        visited += 1
        last = chain[-1]
        if last == n:
            return chain
        if remaining == 0 or last * (1 << remaining) < n:
            return None
        candidates = sorted({a+b for i, a in enumerate(chain)
                             for b in chain[i:] if last < a+b <= n}, reverse=True)
        for value in candidates:
            if value * (1 << (remaining-1)) < n:
                continue
            answer = search(chain+[value], remaining-1)
            if answer is not None:
                return answer
        return None

    # Binary expansion constructs a chain of this length.
    upper = n.bit_length()-1+n.bit_count()-1
    for length in range(lower, upper+1):
        answer = search([1], length)
        if answer is not None:
            return answer, {'lower_bound': lower, 'rejected_depths': rejected,
                            'visited': visited}
        rejected.append(length)
    raise AssertionError('binary-chain upper bound violated')


def factor(n):
    if n < 1:
        raise ValueError('positive n required')
    out = []
    d = 2
    while d*d <= n:
        exponent = 0
        while n % d == 0:
            n //= d
            exponent += 1
        if exponent:
            out.append((d, exponent))
        d += 1
    if n > 1:
        out.append((n, 1))
    return out


def multiplication_depth(omega):
    """Primes are cost-free leaves; only binary multiplication is counted."""
    if omega < 0:
        raise ValueError('nonnegative multiplicity required')
    return 0 if omega <= 1 else (omega-1).bit_length()


def midpoint_distances(p):
    """Direct old-prime-monoid membership, independent of the count formula."""
    if factor(p) != [(p, 1)]:
        raise ValueError('prime required')
    def old(n):
        return all(q < p for q, _ in factor(n))
    return [d for d in range(1, p) if old(p-d) and old(p+d)]


def build_atlas(limit=512, chain_limit=128):
    costs, witnesses = integer_complexities(limit)
    prime_list = primes_up_to(2*limit+1)
    prime_set = set(prime_list)
    rows, divisor_record = [], 0
    for n in range(1, limit+1):
        factors = factor(n)
        omega = sum(k for _, k in factors)
        divisors = math.prod(k+1 for _, k in factors)
        high = divisors > divisor_record
        divisor_record = max(divisor_record, divisors)
        p = factors[0][0] if len(factors) == 1 else None
        k = factors[0][1] if p is not None else None
        ic_defect = arb(costs[n])-3*arb(n).log()/arb(3).log()
        chain, stats = addition_chain(n) if n <= chain_limit else (None, None)
        prime = n in prime_set
        prev = max((q for q in prime_list if q < n), default=None)
        nxt = next(q for q in prime_list if q > n)
        record = dict(n=n, log_n=str(arb(n).log()), prime=prime,
                      composite=n > 1 and not prime,
                      prime_power=p is not None, prime_base=p, power=k,
                      factorization=factors, omega=omega, divisor_count=divisors,
                      highly_composite=high, integer_complexity=costs[n],
                      complexity_witness=witnesses[n],
                      ic_defect=str(ic_defect), ic_defect_display=float(ic_defect),
                      addition_chain=chain,
                      addition_chain_length=None if chain is None else len(chain)-1,
                      addition_chain_small_steps=None if chain is None else len(chain)-n.bit_length(),
                      addition_chain_search=stats,
                      multiplicative_binary_depth=multiplication_depth(omega),
                      successor_cost=None,
                      previous_prime=prev, next_prime=nxt,
                      next_prime_gap=nxt-n if prime else None,
                      enclosing_prime_gap=nxt-prev if prev is not None else None,
                      old_midpoint_count=None, old_midpoint_saturation=None,
                      suzuki_weight=str(arb(p).log()/arb(n).sqrt()) if p else '0',
                      M_p=str(tower_totals(n)[0]) if prime else None,
                      service_node=str(arch_prime(arb(n).log())) if n >= 2 else None)
        if prime:
            distances = midpoint_distances(n)
            formula = n-1-sum(n < q < 2*n for q in prime_list)
            if len(distances) != formula:
                raise AssertionError('midpoint count identity failed')
            record['old_midpoint_count'] = len(distances)
            record['old_midpoint_saturation'] = str(Fraction(len(distances), n-1))
        rows.append(record)
    return rows


def _feature(row, name):
    if name == 'ic_defect':
        return arb(row['integer_complexity'])-3*arb(row['n']).log()/arb(3).log()
    return arb(row[name])


def residuals(rows, feature):
    bins = defaultdict(list)
    for row in rows:
        bins[row['n'].bit_length()-1].append(row)
    out = {}
    for group in bins.values():
        mean = sum((_feature(r, feature) for r in group), arb(0))/len(group)
        for r in group:
            out[r['n']] = _feature(r, feature)-mean
    return out


def contrast(values, selected):
    chosen = [v for n, v in values.items() if n in selected]
    others = [v for n, v in values.items() if n not in selected]
    if not chosen or not others:
        raise ValueError('both populations must be nonempty')
    return sum(chosen, arb(0))/len(chosen)-sum(others, arb(0))/len(others)


def gap_permutation(points, rng):
    if len(points) <= 1:
        return list(points)
    gaps = [b-a for a, b in zip(points, points[1:])]
    rng.shuffle(gaps)
    out = [points[0]]
    for gap in gaps:
        out.append(out[-1]+gap)
    return out


def comparison(rows, feature, seed, repeats):
    values = residuals(rows, feature)
    labels = {r['n'] for r in rows if r['prime']}
    bins = defaultdict(list)
    for n in values:
        bins[n.bit_length()-1].append(n)
    observed = contrast(values, labels)
    rng = random.Random(seed)
    shuffled, sparse, permuted = [], [], []
    shuffled_labels, sparse_labels, permuted_labels = [], [], []
    for _ in range(repeats):
        s1, s2, s3 = set(), set(), set()
        for points in bins.values():
            originals = sorted(labels.intersection(points))
            label_vector = [n in labels for n in points]
            rng.shuffle(label_vector)
            s1.update(n for n, marked in zip(points, label_vector) if marked)
            s2.update(rng.sample(points, len(originals)))
            s3.update(gap_permutation(originals, rng))
        for result, selected, stored in ((shuffled,s1,shuffled_labels),
                                          (sparse,s2,sparse_labels),
                                          (permuted,s3,permuted_labels)):
            result.append(float(contrast(values, selected)))
            stored.append(sorted(selected))
    composites = [r for r in rows if r['composite']]
    matches = []
    for row in rows:
        if not row['prime']:
            continue
        nearest = min(composites, key=lambda r: (abs(row['n']-r['n']), r['n']))
        matches.append((row['n'], nearest['n'],
                        _feature(row,feature)-_feature(nearest,feature)))
    matched = sum((v for _, _, v in matches),arb(0))/len(matches)
    def summarize(array):
        ordered = sorted(array)
        return dict(minimum=ordered[0], median=ordered[len(array)//2],
                    maximum=ordered[-1],
                    count_at_least_observed=sum(x >= float(observed) for x in array))
    return dict(feature=feature, count=len(rows), prime_count=len(labels),
                observed_contrast=str(observed), observed_display=float(observed),
                nearest_composite_mean=str(matched),
                nearest_pairs=[[p,c,str(v)] for p,c,v in matches],
                shuffle_summary=summarize(shuffled), sparse_summary=summarize(sparse),
                gap_permutation_summary=summarize(permuted),
                shuffle_statistics=shuffled, sparse_statistics=sparse,
                gap_permutation_statistics=permuted,
                shuffle_labels=shuffled_labels, sparse_labels=sparse_labels,
                gap_permutation_labels=permuted_labels)


def subgroup_comparisons(rows):
    """Fixed subgroup descriptive summaries, matched by log-size locally."""
    output = {}
    eligible = [r for r in rows if 9 <= r['n'] < 512]
    normalized = residuals(eligible, 'ic_defect')
    odd_normalized = residuals([r for r in eligible if r['n'] % 2], 'ic_defect')
    for name, predicate in [
        ('primes', lambda r:r['prime']),
        ('higher_prime_powers', lambda r:r['prime_power'] and r['power'] > 1),
        ('odd_higher_prime_powers', lambda r:r['prime_power'] and r['power'] > 1 and r['n'] % 2),
        ('highly_composite', lambda r:r['highly_composite']),
        ('other_composites', lambda r:r['composite'] and not r['prime_power'])]:
        selected = [r for r in eligible if predicate(r)]
        if selected:
            output[name] = dict(count=len(selected), integers=[r['n'] for r in selected],
                mean_ic_defect=str(sum((_feature(r,'ic_defect') for r in selected),arb(0))/len(selected)),
                dyadic_residual_mean=str(sum((normalized[r['n']] for r in selected),arb(0))/len(selected)),
                odd_dyadic_residual_mean=(str(sum((odd_normalized[r['n']] for r in selected),arb(0))/len(selected))
                    if all(r['n'] % 2 for r in selected) else None))
    return output


def run(limit=512, chain_limit=128, seed=20261006, repeats=199):
    if limit != 512 or chain_limit != 128:
        raise ValueError('registered run fixes limits at512 and128')
    rows = build_atlas(limit, chain_limit)
    comparisons = {}
    for name, low, high, feature in [
        ('ic_train',9,256,'ic_defect'), ('ic_holdout',256,512,'ic_defect'),
        ('chain_train',9,64,'addition_chain_small_steps'),
        ('chain_holdout',64,128,'addition_chain_small_steps')]:
        eligible = [r for r in rows if low <= r['n'] < high and r['n'] % 2]
        comparisons[name] = comparison(eligible,feature,seed,repeats)
    return dict(scope='finite atlas only, no RH or asymptotic claim',
                precision_bits=ctx.prec, integer_limit=limit, chain_limit=chain_limit,
                random_seed=seed, repeats=repeats, records=rows,
                comparisons=comparisons, subgroups=subgroup_comparisons(rows))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    with ctx.workprec(160):
        data = run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,indent=2)+'\n')

if __name__ == '__main__':
    main()
