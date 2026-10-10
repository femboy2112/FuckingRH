"""Field-relative actualization research engine (bounded, exact, no RH claims)."""
from .core import (ActualizationError, AffineChart, BasisLift, BudgetExceeded,
                   DomainError, Execution, Frame, IncompleteObservation,
                   Operation, Scalar, ZERO, ONE, I, execute)
from .arithmetic import (Limits, ShadowIndex, clock_contract, conditional_mean,
                         conductor_growth, connected_audit, factorization,
                         mixed_probe, source_at, structure_birth)
from .engine import Engine, LossyHistoryError, run_arithmetic

__version__ = "0.1.0"
