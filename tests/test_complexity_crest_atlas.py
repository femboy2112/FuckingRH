"""Exact controls for finite atlas; observational correlations do not prove RH."""
import copy
from collections import defaultdict
import random
import unittest
from flint import arb, ctx
from scripts.complexity_crest_atlas import (
    addition_chain, build_atlas, comparison, factor, gap_permutation,
    integer_complexities, midpoint_distances, multiplication_depth,
)


class ComplexityCrestTests(unittest.TestCase):
    def test_integer_complexity_independent_enumeration_by_leaf_count(self):
        # Forward expression enumeration is independent of descending-value DP.
        limit, max_cost = 64, 14
        by_cost = [set() for _ in range(max_cost+1)]
        by_cost[1] = {1}
        first = {1:1}
        for k in range(2,max_cost+1):
            for i in range(1,k):
                for a in by_cost[i]:
                    for b in by_cost[k-i]:
                        for value in (a+b,a*b):
                            if value <= limit:
                                by_cost[k].add(value)
            for n in by_cost[k]:
                first.setdefault(n,k)
        costs,_ = integer_complexities(limit)
        self.assertEqual(len(first),limit)
        self.assertEqual(costs[1:],[first[n] for n in range(1,limit+1)])

    def test_integer_complexity_exact_lower_bound_and_witnesses(self):
        costs,witnesses = integer_complexities(512)
        for n in range(1,513):
            self.assertLessEqual(n**3,3**costs[n])
            if n > 1:
                op,a,b = witnesses[n]
                self.assertEqual(a+b if op == '+' else a*b,n)
                self.assertEqual(costs[a]+costs[b],costs[n])
        for k in range(1,6):
            self.assertEqual(costs[3**k],3*k)
        # Published instability control, not naive additive factor complexity.
        self.assertEqual((costs[107],costs[321]),(16,18))

    def test_addition_chains_independent_breadth_first_all_pairs(self):
        # Breadth-first enumeration has no target-specific doubling pruning.
        limit = 24
        chains = {(1,)}
        shortest = {1:0}
        depth = 0
        while len(shortest) < limit:
            depth += 1
            next_chains = set()
            for chain in chains:
                possible = {a+b for a in chain for b in chain
                            if chain[-1] < a+b <= limit}
                for n in possible:
                    next_chains.add(chain+(n,))
                    shortest.setdefault(n,depth)
            chains = next_chains
        for n in range(1,limit+1):
            chain,_ = addition_chain(n)
            self.assertEqual(len(chain)-1,shortest[n])

    def test_addition_chain_witnesses_and_missing_data_are_honest(self):
        for n in range(1,129):
            chain,stats = addition_chain(n)
            self.assertEqual((chain[0],chain[-1]),(1,n))
            for i,value in enumerate(chain[1:],1):
                self.assertGreater(value,chain[i-1])
                self.assertTrue(any(a+b == value for a in chain[:i] for b in chain[:i]))
            self.assertEqual(stats['rejected_depths'],list(range(stats['lower_bound'],len(chain)-1)))
        self.assertEqual(len(addition_chain(127)[0])-1,10)
        with ctx.workprec(100):
            rows=build_atlas(130,128)
            self.assertIsNone(rows[128]['addition_chain_length'])
            self.assertIsNone(rows[129]['addition_chain_search'])

    def test_prime_monoid_and_depth_conventions(self):
        self.assertEqual(factor(360),[(2,3),(3,2),(5,1)])
        self.assertEqual([multiplication_depth(i) for i in range(9)],[0,0,1,2,2,3,3,3,3])
        self.assertEqual(midpoint_distances(2),[])
        self.assertEqual(midpoint_distances(3),[1])
        for p in (5,7,11,17,31):
            distances=midpoint_distances(p)
            primes_in_interval=sum(factor(n)==[(n,1)] for n in range(p+1,2*p))
            self.assertEqual(len(distances),p-1-primes_in_interval)

    def test_surrogates_preserve_declared_marginals(self):
        points=[11,13,17,19,23,29,31]
        changed=gap_permutation(points,random.Random(70))
        self.assertEqual((changed[0],changed[-1],len(changed)),(points[0],points[-1],len(points)))
        self.assertEqual(sorted(b-a for a,b in zip(points,points[1:])),
                         sorted(b-a for a,b in zip(changed,changed[1:])))
        with ctx.workprec(100):
            rows=[r for r in build_atlas(64,64) if 9 <= r['n'] < 64 and r['n'] % 2]
            result=comparison(rows,'ic_defect',123,5)
            bins=defaultdict(int)
            for r in rows:
                if r['prime']:
                    bins[r['n'].bit_length()-1]+=1
            for key in ('shuffle_labels','sparse_labels','gap_permutation_labels'):
                for labels in result[key]:
                    counts=defaultdict(int)
                    for n in labels:
                        self.assertTrue(n % 2)
                        counts[n.bit_length()-1]+=1
                    self.assertEqual(counts,bins)

    def test_weight_mutation_is_invisible_to_complexity_contrast(self):
        with ctx.workprec(100):
            rows=[r for r in build_atlas(64,64) if 9 <= r['n'] < 64 and r['n'] % 2]
            mutated=copy.deepcopy(rows)
            for r in mutated:
                if r['n']==13:
                    r['suzuki_weight']='1000000000000'
            original=comparison(rows,'ic_defect',123,3)
            changed=comparison(mutated,'ic_defect',123,3)
            self.assertEqual(original,changed)
            self.assertTrue(arb(original['observed_contrast']) > 0)


if __name__ == '__main__':
    unittest.main()
