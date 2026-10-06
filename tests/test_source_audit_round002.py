"""Exact hostile controls for the Parts 4/5 source audit.

These tests check source-level logical interfaces, not RH or prime statistics.
"""
from fractions import Fraction as F
import unittest


def source_part2_drawdown_classification(left_lower, right_lower, right_upper):
    """Control flow in Part2v4 ppc_certify.c close_previous_interval."""
    if left_lower >= 0:
        return "left", False
    if right_upper <= 0:
        return "right", False
    return "drawdown", right_lower <= 0


class SourceAuditRound002Tests(unittest.TestCase):
    def test_missing_left_upper_guard_invalidates_recovery_count_inference(self):
        # True derivative r(v)=1/4+v on [0,1]: strictly increasing,
        # no zero, hence no recovery. All four bounds are valid enclosures.
        left_actual, left_lower, left_upper = F(1,4), F(-1,4), F(3,4)
        right_actual, right_lower, right_upper = F(5,4), F(1), F(3,2)
        self.assertLessEqual(left_lower, left_actual)
        self.assertLessEqual(left_actual, left_upper)
        self.assertLessEqual(right_lower, right_actual)
        self.assertLessEqual(right_actual, right_upper)
        branch, overlap = source_part2_drawdown_classification(
            left_lower, right_lower, right_upper)
        self.assertEqual(branch, "drawdown")
        self.assertFalse(overlap)
        strict_recovery = left_actual < 0 < right_actual
        self.assertFalse(strict_recovery)
        self.assertNotEqual(int(branch == "drawdown") - int(overlap),
                            int(strict_recovery))

    def test_true_recovery_and_right_ambiguity_controls(self):
        self.assertEqual(source_part2_drawdown_classification(
            F(-2), F(1), F(2)), ("drawdown", False))
        self.assertEqual(source_part2_drawdown_classification(
            F(-2), F(-1), F(2)), ("drawdown", True))
        self.assertEqual(source_part2_drawdown_classification(
            F(0), F(1), F(2)), ("left", False))

    def test_negative_potential_need_not_be_active(self):
        # A(t)=t^2/2 and one hinge of weight 3 at t=1.
        # Psi starts at 0, initially positive, recovers at t=3,
        # but is still negative and idle at t=4.
        t = F(4)
        psi = t*t/2 - 3*(t-1)
        workload = 3-t
        self.assertLess(psi, 0)
        self.assertLess(workload, 0)
        self.assertEqual(F(3)*F(3)/2-3*(F(3)-1), F(-3,2))

    def test_recovery_window_boundary_is_distinct(self):
        service_gap = F(3,2)
        post_event_workload = service_gap
        self.assertFalse(0 < post_event_workload < service_gap)
        self.assertTrue(0 < post_event_workload <= service_gap)
        # At a simultaneous next jump, right-continuous Y is positive again.
        next_weight = F(1,3)
        self.assertEqual(post_event_workload-service_gap, 0)
        self.assertGreater(post_event_workload-service_gap+next_weight, 0)

    def test_service_area_identity_exact_toy_episode(self):
        y0 = F(2)
        arrivals = [(F(1), F(1)), (F(2), F(1,2))]
        recovery = y0 + sum((w for _,w in arrivals), F(0))
        # Integrate each affine piece independently using trapezoids.
        nodes = [F(0)] + [t for t,_ in arrivals] + [recovery]
        area = F(0)
        for left, right in zip(nodes, nodes[1:]):
            load = y0 + sum((w for t,w in arrivals if t<=left), F(0))
            area += ((load-left)+(load-right))*(right-left)/2
        formula = recovery*recovery/2-sum((w*t for t,w in arrivals),F(0))
        self.assertEqual(area, formula)

    def test_no_floor_implies_subsequence_slack_not_full_limit(self):
        # Every certificate inequality 0<=error<=reserve holds, with
        # arbitrarily small reserves, but errors on odd indices stay 1/2.
        for n in range(1, 101):
            reserve = F(1, n) if n % 2 == 0 else F(1)
            error = reserve/2
            self.assertLessEqual(0, error)
            self.assertLessEqual(error, reserve)
            if n % 2:
                self.assertEqual(error, F(1,2))
        self.assertEqual(F(1,100)/2, F(1,200))

    def test_mellin_principal_parts_cancel_exactly(self):
        alpha, c0 = F(7,3), F(-2,5)
        for epsilon in [F(1,10), F(1,100), F(1,1000)]:
            s = F(1,2)+epsilon
            # Pole of -zeta'/zeta at s+1/2=1 has residue +1.
            value = (1/epsilon+c0)/s-2/epsilon+alpha/s
            self.assertEqual(value, (-2+c0+alpha)/s)
            # At s=0, constant term -alpha cancels alpha/s.
            b = F(3,7)
            value0 = (-alpha+b*epsilon)/epsilon-2/(epsilon-F(1,2))+alpha/epsilon
            self.assertEqual(value0, b-2/(epsilon-F(1,2)))


if __name__ == '__main__':
    unittest.main()
