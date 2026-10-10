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

__version__ = "0.2.0"
