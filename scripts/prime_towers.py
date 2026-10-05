"""Exact geometric algebra and Arb controls for full prime-power towers.

No primality inference from floating point, no zero ordinates, no automatic
exp/log rounding to select active events. Callers supply the integer horizon.
"""

from flint import arb

from scripts.event_dynamics import arch_prime, gamma_linear
from scripts.suzuki_psi import primes_up_to, prime_power_events_up_to


def geometric_moments(r, k):
    """Return sum_{j=1}^k r^j and sum_{j=1}^k j*r^j, generically."""
    if k < 0:
        raise ValueError('k must be nonnegative')
    return (r*(1-r**k)/(1-r),
            r*(1-(k+1)*r**k+k*r**(k+1))/(1-r)**2)


def geometric_tails(r, k):
    """Return the corresponding exact tails after k."""
    if k < 0:
        raise ValueError('k must be nonnegative')
    return (r**(k+1)/(1-r),
            r**(k+1)*((k+1)-k*r)/(1-r)**2)


def cosine_sum(r, cosine):
    """Closed form sum_{k>=1} r^k cos(k theta), cosine=cos(theta)."""
    return (r*cosine-r*r)/(1-2*r*cosine+r*r)


def tower_parameters(p):
    if p < 2:
        raise ValueError('p must be at least two; primality is caller-owned')
    ell = arb(p).log()
    r = 1/arb(p).sqrt()
    return ell, r


def tower_totals(p):
    ell, r = tower_parameters(p)
    return ell*r/(1-r), ell*ell*r/(1-r)**2


def active_power_count(p, horizon):
    """Exact number of positive powers of p at most an integer horizon."""
    q, k = p, 0
    while q <= horizon:
        k += 1
        q *= p
    return k


def tower_ramp_at_horizon(p, horizon):
    """h_p(log(horizon)), with active powers selected in integer arithmetic."""
    if horizon < 1:
        raise ValueError('horizon must be positive')
    ell, r = tower_parameters(p)
    k = active_power_count(p, horizon)
    zeroth, first = geometric_moments(r, k)
    return arb(horizon).log()*ell*zeroth-ell*ell*first


def tower_repaired_at_horizon(p, horizon):
    mass, _ = tower_totals(p)
    return mass*arb(horizon).log()-tower_ramp_at_horizon(p, horizon)


def service_partial_and_remainder_bound(p, k):
    """Return exact Arb prefix service moment and the positive remainder cap."""
    if k < 1:
        raise ValueError('k must be positive')
    ell, r = tower_parameters(p)
    mass_prefix = ell*geometric_moments(r, k)[0]
    service = sum(ell*r**j*arch_prime(j*ell) for j in range(1, k+1))
    correction = service-2*ell*k-gamma_linear()*mass_prefix
    bound = 2*ell/(5*(1-r**4))*r**6*(1-r**(6*k))/(1-r**6)
    return service, correction, bound


def aggregate_at_horizon(prime_cutoff, horizon):
    """Return M_X, D_X(log horizon), P(log horizon), computed separately."""
    if prime_cutoff < horizon:
        raise ValueError('cutoff must cover the event horizon')
    primes = primes_up_to(prime_cutoff)
    mass = sum(tower_totals(p)[0] for p in primes)
    repaired = sum(tower_repaired_at_horizon(p, horizon) for p in primes)
    t = arb(horizon).log()
    ramp = sum(arb(e.prime).log()/arb(e.n).sqrt()*(t-arb(e.n).log())
               for e in prime_power_events_up_to(horizon))
    return mass, repaired, ramp
