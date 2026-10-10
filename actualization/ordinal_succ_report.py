"""Ordinal SUCC observer reports and the SECOND-ORDER Suzuki/Weil seam.

THIS MODULE DOES NOT EXECUTE AN INFINITE ORDINAL STAGE.

The mathematical observational diagram is

    O_2 --SUCC--> O_3 --SUCC--> ... --limit at omega--> O_omega
                         --formal report at omega+1--> Weil/Suzuki kernel

O_omega is a FILTERED COLIMIT of compatible prefixes, not a physical
observer returning after infinitely much elapsed time. Omega+1 names a
mathematical postprocessing operation, not a finite computational step.
For any bounded rational set of query times, arithmetic prime-event data
stabilize EXACTLY after a computable finite SUCC horizon. The archimedean
term is a separate, explicitly declared classical analytic model.

The correlation kernel K(t,u)=Psi(t)+Psi(u)-Psi(t-u) has
    d_t d_u K = Psi''(t-u) = Weil distribution
in the distributional sense (Masatoshi Suzuki, JLMS 2023).
A finite rectangle difference of K is an observed covariance-of-
increments PROBE, not a proof of nonnegative covariance.

That positivity (for all test functions) is RH-equivalent. Even
pointwise Psi>=0 and pointwise Psi''>=0 do NOT imply it.

Exact Fraction models give falsifiers independent of zeta zero data.
The finite source path can be supplied by an Engine journal;
unactualized future events must NOT be used as observations.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping


class OrdinalObservationError(ValueError):
    """A causal, finite resource, ordinal, or analytic boundary was violated."""


def _q(raw):
    if type(raw) is int or isinstance(raw, Fraction):
        return Fraction(raw)
    raise OrdinalObservationError("Ordinal query times and coefficients require exact rationals")


def _n(n, *, least=2, most=256):
    if type(n) is not int or not least <= n <= most:
        raise OrdinalObservationError(f"Stage must be an exact integer in [{least},{most}]")
    return n


def _query(q):
    t=_q(q)
    if abs(t)>5:
        raise OrdinalObservationError("Finite rational observer query limited to |t|<=5")
    return t


def _mp():
    try:
        import mpmath
    except ImportError as exc:
        raise OrdinalObservationError("mpmath required for archimedean response") from exc
    return mpmath


def _mpq(mp,q):
    z=_q(q)
    return mp.mpf(z.numerator)/z.denominator


def _ceil(q):
    v=_q(q)
    return -(-v.numerator//v.denominator)


def exact_bounded_time_horizon(times):
    """A proof-carrying WHOLE INTEGER ceiling for every named kernel query.

    For |t|<=M with rational M, exp(|t|)<=e^ceil(M)<3^ceil(M)
    when M>0. Consequently N=3^ceil(M) *certainly* contains ALL
    prime events needed at t, u and t-u. No floating exp/log
    threshold is consulted, so an event can never be lost to rounding.

    This is deliberately conservative and is NOT a bound on Gamma
    truncation: the classical archimedean term remains an explicitly
    modeled analytic response at each stage.
    """
    ts=tuple(_query(t) for t in times)
    if not ts:
        raise OrdinalObservationError("At least one finite rational observation time required")
    if len(ts)>10:
        raise OrdinalObservationError("Observation query budget exceeded (10)")
    M=max([abs(t) for t in ts]+[abs(t-u) for t in ts for u in ts])
    N=1 if M==0 else 3**_ceil(M)
    return {"rational_times":ts,
            "max_observable_log_displacement":M,
            "certified_source_SUCC_horizon":max(2,N),
            "derivation":"exp(M) < 3^ceil(M), proven from e<3",
            "archimedean_window_already_completed":True,
            "full_omega_stage_was_not_executed":True}


@dataclass(frozen=True)
class OrdinalFiniteStage:
    """SUCC observation stage n, preserving the complete coefficient prefix.

    Only n+1 is an accepted successor. A compatible family of these
    stages may have a mathematical colimit at omega; no finite instance
    pretends to represent O_omega.
    """
    n: int
    source: tuple[Fraction,...]
    head: str | None = None

    @classmethod
    def from_prefix(cls,source: Mapping[int,object],horizon,*,head=None):
        from .gamma_interferometer import GammaInterferometer,InterferometerError
        try:
            snapshot=GammaInterferometer.from_prefix(source,horizon,trace_head=head)
        except (InterferometerError,TypeError,ValueError) as exc:
            raise OrdinalObservationError("Requires complete actualized source prefix") from exc
        return cls(snapshot.horizon,snapshot.coefficients,snapshot.trace_head)

    @classmethod
    def from_engine(cls,engine,horizon=None):
        from .gamma_interferometer import GammaInterferometer,InterferometerError
        try:
            snap=GammaInterferometer.from_engine(engine,horizon)
        except (InterferometerError,TypeError,ValueError) as exc:
            raise OrdinalObservationError("Unactualized or incomplete source") from exc
        return cls(snap.horizon,snap.coefficients,snap.trace_head)

    @classmethod
    def genuine(cls,n):
        _n(n)
        return cls.from_prefix({k:1 for k in range(1,n+1)},n)

    def successor(self, coefficient, *, head=None):
        _n(self.n+1)
        v=_q(coefficient)
        return OrdinalFiniteStage(self.n+1,self.source+(v,),head)

    def restrict(self,smaller):
        _n(smaller,most=self.n)
        return OrdinalFiniteStage(smaller,self.source[:smaller+1],None)

    def agrees_with_earlier(self,older):
        if not isinstance(older,OrdinalFiniteStage):
            raise OrdinalObservationError("Compare only ordinal source snapshots")
        if older.n>self.n or self.source[:older.n+1]!=older.source:
            raise OrdinalObservationError("Finite observation histories are not compatible")
        return True

    def _gamma_snapshot(self):
        from .gamma_interferometer import GammaInterferometer
        return GammaInterferometer.from_prefix(
            {n:self.source[n] for n in range(1,self.n+1)},self.n,
            trace_head=self.head
        )

    def report(self,times,*,dps=60):
        """Omega+1-style report on a FINITE window, with explicit horizon.

        Only constructs an accessible finite restriction of the
        would-be omega+1 Weil/Suzuki report. Gamma's completed
        archimedean term is a separate classical analytic input.
        """
        w=exact_bounded_time_horizon(times)
        need=w["certified_source_SUCC_horizon"]
        if self.n<need:
            raise OrdinalObservationError(
                f"Observer stage {self.n} cannot read full prime wavefront requiring {need}")
        mp=_mp()
        with mp.workdps(dps):
            snap=self._gamma_snapshot()
            ts=w["rational_times"]
            psi={}
            for t in set(ts)|{t-u for t in ts for u in ts}|{Fraction(0)}:
                psi[t]=snap.at_time(abs(_mpq(mp,t)),dps=dps)["psi"]
            matrix=tuple(
                tuple(+(psi[t]+psi[u]-psi[t-u]) for u in ts)
                for t in ts
            )
            return {
                "ordinal_stage":"finite successor n",
                "formal_limit_stage":"omega = union/colimit of compatible records",
                "formal_report_stage":"omega+1 = mathematical postprocessing, NOT physical return",
                "finite_query_times":tuple(str(x) for x in ts),
                "source_horizon":self.n,
                "stabilization_horizon":need,
                "trace_head":self.head,
                "source_matches_zeta_prefix":snap.matches_zeta_prefix,
                "archimedean_term":"Suzuki exact classical Gamma+poles; not observed finite gamma cutoff",
                "kernel":matrix,
                "status":"FINITE_RESTRICTION_OF_ORDINAL_WEIL_REPORT_NOT_A_PSD_CERTIFICATE",
            }

    def rectangle_increment(self,t,u,h,k,*,dps=60):
        """Second mixed finite SUCC difference of the arithmetic report.

        Requires all four corners and their differences in actualized
        rational observation horizon. No positivity assumed.
        """
        t,u,h,k=map(_q,(t,u,h,k))
        if not h>0 or not k>0:
            raise OrdinalObservationError("Require positive finite difference increments")
        times=(t,t+h,u,u+k)
        grid=self.report(times,dps=dps)
        mat=grid["kernel"]
        # positions [t,t+h,u,u+k] with mixed finite difference
        return +(mat[1][3]-mat[1][2]-mat[0][3]+mat[0][2])


def quartic_observer_report():
    """Proof that nonnegative data and positive local second derivative
    fail to make the global observer's cross-correlation positive.

    Psi(t)=t^4, Psi''(t)=12t^2>=0.
    Times ±1: K = [[2,-14],[-14,2]], det=-192.
    Vector (1,1) has *negative* energy -24.
    All arithmetic here is exact Fraction.
    """
    f=lambda t: _q(t)**4
    k=lambda t,u: f(t)+f(u)-f(t-u)
    a,b=Fraction(1),Fraction(-1)
    m=((k(a,a),k(a,b)),(k(b,a),k(b,b)))
    return {
        "psi_at_1":f(a),"psi_second_derivative_at_1":Fraction(12),
        "kernel":m,"determinant":m[0][0]*m[1][1]-m[0][1]*m[1][0],
        "quadratic_vector_ones":sum(m[i][j] for i in range(2) for j in range(2)),
        "source":"counterexample to pointwise curvature implies correlation PSD",
    }


def exact_polynomial_rectangle(t,u,h,k):
    """Derive K_{quartic}'s mixed finite difference in TWO INDEPENDENT ways.

    Identity for any even Psi:
      Δ_t^h Δ_u^k K(t,u) =
         Psi(t+h-u)+Psi(t-u-k)-Psi(t+h-u-k)-Psi(t-u).
    This is the exact second-order observed-interaction probe, and
    equals hk Psi''(t-u)+O(hk(h+k)) when smooth.
    """
    t,u,h,k=map(_q,(t,u,h,k))
    if h<=0 or k<=0:
        raise OrdinalObservationError("Finite differences require positive h and k")
    psi=lambda z:z**4
    K=lambda x,y:psi(x)+psi(y)-psi(x-y)
    corners=K(t+h,u+k)-K(t+h,u)-K(t,u+k)+K(t,u)
    relative=psi(t+h-u)+psi(t-u-k)-psi(t+h-u-k)-psi(t-u)
    assert corners==relative
    return {"corners":corners,"relative":relative,
            "local_second_derivative":12*(t-u)**2,
            "normalized":corners/(h*k)}


def oscillator_observer_report(times,*,dps=65):
    """Positive observable trajectory Psi(t)=1-cos(t) explicitly in R².

    phi(t)=(cos t-1,sin t);
    K(t,u)=phi(t)·phi(u)=Psi(t)+Psi(u)-Psi(t-u).
    Psi''(t-u)=cos(t-u), which can be NEGATIVE pointwise despite
    a PSD stationary covariance kernel.
    """
    ts=tuple(_q(t) for t in times)
    if not ts or len(ts)>12:
        raise OrdinalObservationError("1..12 rational observation times expected")
    mp=_mp()
    with mp.workdps(dps):
        vectors=[(mp.cos(_mpq(mp,t))-1,mp.sin(_mpq(mp,t))) for t in ts]
        K=tuple(tuple(+(v[0]*w[0]+v[1]*w[1]) for w in vectors)
                for v in vectors)
        psi=lambda t:1-mp.cos(t)
        independent=tuple(
            tuple(+(psi(_mpq(mp,t))+psi(_mpq(mp,u))
                     -psi(_mpq(mp,t-u))) for u in ts)
            for t in ts)
        discrepancy=max(abs(K[i][j]-independent[i][j])
                        for i in range(len(ts)) for j in range(len(ts)))
        return {"kernel":K,"independent_k":independent,
                "identity_error":+discrepancy,
                "negative_pointwise_curvature_allowed":True,
                "source":"exact 2-dimensional positive feature embedding, NOT zeta"}


def synthetic_ordinal_semantics(horizon):
    """A FINITE demonstrator of the formal omega -> omega+1 distinction.

    Each stage n gives one additional observation; the
    mathematical union O_omega can be specified intensionally
    without computing the infinite run. Its K report is a
    separate universal predicate over finite test families.
    """
    _n(horizon)
    return {
        "finite_stage_count_observed":horizon,
        "last_physical_SUCC_stage":horizon,
        "omega":"limit ordinal, not a largest finite stage",
        "omega_plus_one":"successor of FORMALLY completed history, not an executable finish line",
        "completed_source_identity":"infinite compatible coefficient diagram",
        "report_property":"for all finite test sets, Suzuki K has nonnegative Gram",
        "report_property_is_RH_equivalent":True,
        "report_property_proved":False,
        "omega_computation_executed":False,
    }
