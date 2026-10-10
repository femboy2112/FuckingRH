"""Field-relative actualization research engine (bounded, exact, no RH claims)."""
from .core import (ActualizationError, AffineChart, BasisLift, BudgetExceeded,
                   DomainError, Execution, Frame, IncompleteObservation,
                   Operation, Scalar, ZERO, ONE, I, execute)
from .arithmetic import (Limits, ShadowIndex, clock_contract, conditional_mean,
                         conductor_growth, connected_audit, factorization,
                         mixed_probe, source_at, structure_birth)
from .engine import Engine, LossyHistoryError, run_arithmetic
from .yoneda import (Arrow, DivisibilityCategory, PathCategory, ValuationCategory,
                     FiniteFunctor, CompanionBridge, valuation_bridge,
                     forget_path_bridge, restricted_yoneda, validate_yoneda,
                     co_yoneda_companion, verify_companion_actions)
from .resource_probe import (ValuationWord, ProbeBudget, compare_observers,
                             execute_probe, lcm_word, budget_demo)
from .phenomenology import Phenomenology
from .local_global import compare_local_global, prefix_demo
from .circle_transport import (FiniteClock, FiniteDualRefinement, CyclicOneObjectCategory,
                               conductor_birth_2_to_6, verify_refinement_tower)

from .infinite_realization import (LCMIndRealization, RationalEnclosure,
                                   e_enclosure, pi_enclosure, zeta_euler_enclosure,
                                   escaping_defect_form, escaping_defect_limit,
                                   pinned_negative_form)

from .gamma_succ_path import (
    FactorialSuccPath, MomentChannel, PrimeMomentPath, PathDomainError,
    gamma_periodic_gauge, gamma_periodic_log_curvature,
)

from .succ_shadow_window import (
    ShadowWindowCertificate, WindingHistory, WindowError,
    WindowResourceExhausted, sine_gauge_witness, seam_gauge_witness,
    periodic_quarter_probe, same_cell_quadratic_gauge_curvature,
    observed_window, unseen_within_prefix, certified_window_penalty_lower_bound,
    quadratic_weight_gluing_defect,
)

__version__ = "0.3.0"
