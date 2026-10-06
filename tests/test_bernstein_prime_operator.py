"""Exact/interval controls for the round002 Bernstein operator audit.

These are finite counterexample certificates, not an all-prime assertion.
No zeta zero data and no fitted transport plans are used.
"""

from fractions import Fraction as Q
from itertools import combinations
from math import comb, prod
import unittest

from flint import arb, ctx

from scripts.event_dynamics import arch_prime
from scripts.suzuki_psi import prime_power_events_up_to


def binomial_probabilities(weights, p):
    n = len(weights) - 1
    terms = [w * comb(n, i) * p**i * (1-p)**(n-i)
             for i, w in enumerate(weights)]
    z = sum(terms)
    return [term/z for term in terms]


def mean(nodes, probabilities):
    return sum(x*p for x, p in zip(nodes, probabilities))


def call(nodes, weights, strike):
    return sum(w*max(x-strike, Q(0)) for x, w in zip(nodes, weights))


class BernsteinPrimeOperatorTests(unittest.TestCase):
    def test_weighted_binomial_constants_barycenter_and_strict_monotonicity(self):
        nodes = list(map(Q, (1, 2, 4, 7)))
        weights = list(map(Q, (1, 3, 2, 5)))
        previous = None
        for p in (Q(1, 7), Q(2, 7), Q(4, 7), Q(6, 7)):
            probabilities = binomial_probabilities(weights, p)
            self.assertEqual(sum(probabilities), Q(1))
            self.assertTrue(all(k > 0 for k in probabilities))
            b = mean(nodes, probabilities)
            covariance = sum(
                probabilities[i]*probabilities[j]*(nodes[i]-nodes[j])*(i-j)
                for i in range(4) for j in range(4)) / 2
            self.assertGreater(covariance, 0)
            if previous is not None:
                self.assertGreater(b, previous)
            previous = b

    def test_all_ordered_two_by_two_minors_are_positive(self):
        weights = list(map(Q, (1, 3, 2, 5)))
        low = binomial_probabilities(weights, Q(2, 7))
        high = binomial_probabilities(weights, Q(4, 7))
        for i, j in combinations(range(4), 2):
            self.assertGreater(low[i]*high[j] - low[j]*high[i], 0)

    def test_two_node_reparameterization_forgets_input_weights(self):
        nodes = (Q(1), Q(4))
        for weights in ((Q(1), Q(9)), (Q(7), Q(2))):
            for p in (Q(1, 5), Q(1, 2), Q(4, 5)):
                probabilities = binomial_probabilities(weights, p)
                b = mean(nodes, probabilities)
                self.assertEqual(probabilities[0], (nodes[1]-b)/(nodes[1]-nodes[0]))
                self.assertEqual(probabilities[1], (b-nodes[0])/(nodes[1]-nodes[0]))
        # Integrating either forced linear hat over the node hull gives
        # half of its length, regardless of the inserted weights.
        self.assertEqual((nodes[1]-nodes[0])/2, Q(3, 2))

    def test_unreparameterized_pascal_grid_does_not_fix_linear_coordinate(self):
        nodes = (Q(0), Q(1), Q(3))
        p = Q(1, 2)
        probabilities = binomial_probabilities((Q(1),)*3, p)
        self.assertEqual(mean(nodes, probabilities), Q(5, 4))
        self.assertNotEqual(mean(nodes, probabilities), Q(3)*p)

    def test_adjacent_kernel_minimum_variance_and_jensen_orientation(self):
        b = Q(3, 2)
        adjacent_nodes, adjacent_weights = (Q(1), Q(3)), (Q(3, 4), Q(1, 4))
        spread_nodes, spread_weights = (Q(0), Q(3)), (Q(1, 2), Q(1, 2))
        self.assertEqual(mean(adjacent_nodes, adjacent_weights), b)
        self.assertEqual(mean(spread_nodes, spread_weights), b)
        adjacent_var = sum(w*(x-b)**2 for x, w in zip(adjacent_nodes, adjacent_weights))
        spread_var = sum(w*(x-b)**2 for x, w in zip(spread_nodes, spread_weights))
        self.assertEqual(adjacent_var, (b-1)*(3-b))
        self.assertLess(adjacent_var, spread_var)
        # Concave T=-x^2: forward barycentric averaging is a strict debit.
        self.assertLess(sum(-w*x*x for x, w in zip(adjacent_nodes, adjacent_weights)),
                        -b*b)

    def test_sharp_boundary_bias_is_positive(self):
        left, right, total = Q(1, 4), Q(5, 4), Q(3, 2)
        debit = left*left/2 + (total-right)**2/2
        self.assertEqual(debit, Q(1, 16))
        self.assertGreater(debit, 0)

    def test_first_two_moments_do_not_determine_convex_order(self):
        nodes = list(map(Q, (1, 2, 4, 7)))
        mutation = [Q(1)/prod(x-y for j, y in enumerate(nodes) if j != i)
                    for i, x in enumerate(nodes)]
        for degree in (0, 1, 2):
            self.assertEqual(sum(v*x**degree for v, x in zip(mutation, nodes)), 0)
        epsilon = Q(1, 100)
        base = [Q(1)]*4
        changed = [w+epsilon*v for w, v in zip(base, mutation)]
        self.assertTrue(all(w > 0 for w in changed))
        self.assertLess(call(nodes, changed, nodes[1])-call(nodes, base, nodes[1]), 0)
        self.assertGreater(call(nodes, changed, nodes[2])-call(nodes, base, nodes[2]), 0)

    def test_actual_prime_martingale_moment_failures_are_interval_certified(self):
        enclosures = {
            2: ('-0.009847', '-0.009846'),
            7: ('0.008874', '0.008875'),
            8: ('-0.009696', '-0.009695'),
            11: ('0.011625', '0.011626'),
        }
        with ctx.workprec(180):
            s = arb(0)
            first = arb(0)
            sigmas = []
            weights = []
            for event in prime_power_events_up_to(11):
                w = arb(event.prime).log()/arb(event.n).sqrt()
                sigma = arch_prime(arb(event.n).log())
                sigmas.append(sigma)
                weights.append(w)
                s += w
                first += w*sigma
                if event.n in enclosures:
                    lower, upper = enclosures[event.n]
                    defect = first-s*s/2
                    self.assertTrue(defect > arb(lower))
                    self.assertTrue(defect < arb(upper))
            self.assertTrue(sigmas[0] > arb('0.224975'))
            self.assertTrue(sigmas[0] < arb('0.224976'))
            self.assertTrue(weights[0] > sigmas[0])
            self.assertTrue(weights[1] > weights[0])
            spacing_difference = sigmas[2]-2*sigmas[1]+sigmas[0]
            self.assertTrue(spacing_difference > arb('-0.058938'))
            self.assertTrue(spacing_difference < arb('-0.058936'))


if __name__ == '__main__':
    unittest.main()
