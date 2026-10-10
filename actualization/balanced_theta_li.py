"""Balanced arithmetic/Archimedean theta windows and zero-free Li-jet transport.

Classical data only. The full theta modular relation is exact; finite
symmetric arithmetic cutoffs fail it at large logarithmic displacement.
We derive an explicit joint cutoff N(u,epsilon) instead of treating the
integer N -> infinity and Archimedean |u| -> infinity limits separately.

We also derive a source-only, all-degree finite-approximation *error bound*
for Keiper-Li coefficients using a compact zero-free DISK AROUND s=1,
not any RH-zero ordinates. The resulting factor r^-degree is the open
uniformity obstruction, not a claim that positivity follows.

All mpmath displays are high-precision diagnostics; bounds are proved
analytically, but floating evaluation is NOT directed interval arithmetic.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb

class BalancedWindowError(ValueError):
    pass


def _mp():
    try:
        import mpmath as mp
    except ImportError as exc:
        raise BalancedWindowError("mpmath is required for analytic readouts") from exc
    return mp


def _nat(n,lo=1,hi=4096,name="horizon"):
    if type(n) is not int or not lo <= n <= hi:
        raise BalancedWindowError(f"{name} must be an integer in {lo}..{hi}")
    return n


def _frac(q):
    if type(q) is int or isinstance(q,Fraction):
        return Fraction(q)
    raise BalancedWindowError("Theta/Li weights and radii must be exact rationals")


def _mpq(mp,q):
    q=_frac(q)
    return mp.mpf(q.numerator)/q.denominator


def _weight(source,n,N):
    if source is None:
        return Fraction(1)
    from .hasse_theta_seam import SUCCDifferenceSource
    if not isinstance(source,SUCCDifferenceSource) or source.horizon<N:
        raise BalancedWindowError("Require complete, actualized arithmetic coefficient prefix")
    return _frac(source.coefficients[n])


def theta_finite(u,N,*,source=None,dps=75):
    """Theta_N(u)=1+2Σ_(n<=N) a(n) exp(-π n² exp(2u)).

    For source!=None this is a *fake weighted theta diagnostic*, NOT
    necessarily a Poisson-self-dual theta function or genuine completion
    of Σ a(n)n^-s. Source a(6)=2 is a hostile example.
    """
    _nat(N,lo=1,hi=4096,name="theta integer cutoff")
    mp=_mp()
    with mp.workdps(dps):
        u=mp.mpf(u)
        if not mp.isfinite(u) or abs(u)>8:
            raise BalancedWindowError("Finite theta log position must satisfy |u|<=8")
        x=mp.pi*mp.exp(2*u)
        return +(1+2*mp.fsum(
            _mpq(mp,_weight(source,n,N))*mp.exp(-x*n*n)
            for n in range(1,N+1)))


def theta_defect(u,N,*,source=None,half_density=Fraction(1,2),dps=75):
    """Finite half-density reflected theta defect.

    For genuine theta and a=1/2 its exact infinite realization is 0.
    Arbitrary a != 1/2 and weighted-fake sources retain defects.
    """
    a=_frac(half_density)
    mp=_mp()
    with mp.workdps(dps):
        u=mp.mpf(u)
        up=theta_finite(u,N,source=source,dps=dps)
        down=theta_finite(-u,N,source=source,dps=dps)
        return +(mp.exp(_mpq(mp,a)*u)*up-mp.exp(-_mpq(mp,a)*u)*down)


def theta_defect_tail_envelope(u,N,*,dps=75):
    """UNCONDITIONAL true-source bound for D_N at half density:

       |D_N(u)| <= exp(|u|/2) erfc(sqrt(pi) N exp(-|u|))
                  +exp(-|u|/2) erfc(sqrt(pi) N exp(|u|)).

    Proof: Poisson theta relation and integral comparison on the two
    omitted Gaussian tails (n>N), where Σ_(n>N)f(n)<=∫_N^∞f(x)dx.
    Gaussian integral gives erfc. This is an analytic theorem;
    output is a nondirected mpmath approximation to its RHS.
    """
    _nat(N,hi=4096,name="theta integer cutoff")
    mp=_mp()
    with mp.workdps(dps):
        v=abs(mp.mpf(u))
        if not mp.isfinite(v) or v>8:
            raise BalancedWindowError("The balanced window is restricted to |u|<=8")
        a=mp.sqrt(mp.pi)*N*mp.exp(-v)
        b=mp.sqrt(mp.pi)*N*mp.exp(v)
        return +(mp.exp(v/2)*mp.erfc(a)+mp.exp(-v/2)*mp.erfc(b))


def matched_theta_cutoff(u,tolerance,*,cap=4096,dps=80):
    """A zero-blind SUCC arithmetic horizon coevolving with Gamma's log u.

    erfc(x)<=exp(-x²); hence both reflected tails sum to <= ε whenever
      π (N exp(-|u|))² >= |u|/2 + log(2/ε).
    We round UP and independently verify the sharper erfc bound.
    """
    _nat(cap,lo=1,hi=4096,name="matched cutoff cap")
    mp=_mp()
    with mp.workdps(dps):
        v=abs(mp.mpf(u))
        eps=mp.mpf(tolerance)
        if not mp.isfinite(v) or v>8 or not mp.isfinite(eps) or not 0<eps<1:
            raise BalancedWindowError("Require |u|<=8 and 0<tolerance<1")
        target=mp.exp(v)*mp.sqrt((v/2+mp.log(2/eps))/mp.pi)
        n=max(1,int(mp.ceil(target))+1) # guard nondirected rounding
        if n>cap:
            raise BalancedWindowError("Required arithmetic horizon exceeds declared finite budget")
        bound=theta_defect_tail_envelope(v,n,dps=dps)
        if bound>eps:
            raise ArithmeticError("Internal analytic theta matching bound failed")
        return {"u":+v,"horizon":n,"requested_tolerance":+eps,
                "analytic_tail_bound":+bound,
                "ratio_N_over_exp_u":+(n/mp.exp(v)),
                "scope":"true Gaussian theta only; zero-blind coevolving window"}


def one_prime_fake_defect(u,n,delta,*,dps=75):
    """Exact anomaly relative to genuine theta for ±n Gaussian weights.

    Adds weight (1+delta) to both signed lattice locations ±n. The
    full weighted theta difference is
      2δ[e^(u/2-πn²e^(2u))-e^(-u/2-πn²e^(-2u))].
    It does NOT decay by increasing N: the source is NOT a genuine
    Poisson-invariant lattice theta after this arbitrary injection.
    """
    _nat(n,lo=1,hi=4096,name="mutated integer event")
    d=_frac(delta)
    mp=_mp()
    with mp.workdps(dps):
        v=mp.mpf(u)
        return +(2*_mpq(mp,d)*(
            mp.exp(v/2-mp.pi*n*n*mp.exp(2*v))-
            mp.exp(-v/2-mp.pi*n*n*mp.exp(-2*v))))


def wrong_half_density_limit(u,alpha,*,dps=75):
    """Full theta obstruction when half density alpha != 1/2.

    Full theta is numerically evaluated with 64 positive-side lattice
    terms and reflected analytically; not an interval certificate.

    D_alpha(u)=Theta(u)(exp(alpha*u)-exp((1-alpha)*u));
    by modularity this is zero for ALL u iff alpha=1/2.
    """
    a=_frac(alpha)
    mp=_mp()
    with mp.workdps(dps):
        v=mp.mpf(u)
        # Evaluate the actual theta function through the rapidly
        # convergent positive-|u| side and exact Poisson reflection.
        positive=theta_finite(abs(v),64,dps=dps)
        full=positive if v>=0 else mp.exp(-v)*positive
        return +(full*(mp.exp(_mpq(mp,a)*v)-
                       mp.exp((1-_mpq(mp,a))*v)))


def finite_gamma_window(s,A,B,*,dps=75):
    """A_[A,B](s) = 2 ∫_A^B exp(su-πexp(2u))du, exact via Γ(a,x,y)."""
    mp=_mp()
    with mp.workdps(dps):
        s=mp.mpc(s)
        A,B=mp.mpf(A),mp.mpf(B)
        if not mp.isfinite(A) or not mp.isfinite(B) or not A<B:
            raise BalancedWindowError("Require finite gamma window A<B")
        a=mp.pi*mp.exp(2*A)
        b=mp.pi*mp.exp(2*B)
        return +(mp.power(mp.pi,-s/2)*mp.gammainc(s/2,a,b))


def finite_gamma_succ_defect(s,A,B,*,dps=75):
    """Check exact finite Gamma shift with explicit endpoint triangle.

    A_[A,B](s+2) - s/(2π) A_[A,B](s)
      = [e^(sA-πe^(2A))-e^(sB-πe^(2B))]/π.
    This is a classical integration-by-parts identity, not Weil sign.
    """
    mp=_mp()
    with mp.workdps(dps):
        s=mp.mpc(s)
        A,B=mp.mpf(A),mp.mpf(B)
        now=finite_gamma_window(s,A,B,dps=dps)
        next=finite_gamma_window(s+2,A,B,dps=dps)
        boundary=(mp.exp(s*A-mp.pi*mp.exp(2*A))-
                  mp.exp(s*B-mp.pi*mp.exp(2*B)))/mp.pi
        return {"A_s":+now,"A_succ":+next,"endpoint_boundary":+boundary,
                "residual":+(next-s*now/(2*mp.pi)-boundary)}


def truncated_xi(s,N,T,*,dps=75):
    """Reuse pre-existing classically exact finite theta xi construction."""
    _nat(N,lo=1,hi=40,name="xi integer cutoff")
    mp=_mp()
    with mp.workdps(dps):
        T=mp.mpf(T)
        if not mp.isfinite(T) or not 0<=T<=5:
            raise BalancedWindowError("Finite xi log window requires 0<=T<=5")
        return +_xi_cut(s,N,T,dps)


def _xi_cut(s,N,T,dps):
    """Finite time theta integral via upper incomplete gamma differences."""
    mp=_mp()
    with mp.workdps(dps):
        s=mp.mpc(s)
        total=mp.mpc(0)
        for n in range(1,N+1):
            a=mp.pi*n*n
            b=a*mp.exp(2*T)
            for z in (s,1-s):
                total+=mp.power(a,-z/2)*mp.gammainc(z/2,a,b)
        return +(mp.mpf(1)/2+s*(s-1)*total/2)


def finite_li_coefficients(N,T,degree,*,dps=85):
    """Zero-free finite Li jets FROM the theta heat-source moments.

    Xi_[N,T](1+y) = 1/2 + y(1+y) Σ_(j>=0) A_j y^j, with
       A_j=1/j! Σ_(n<=N) ∫_0^T
         e^(-πn²e^(2u)) u^j [e^u+(-1)^j]du.
    Let C_m=2(A_(m-1)+A_(m-2)); y=w/(1-w).
    B_k=[w^k]2Xi(1/(1-w)) = Σ_(m=1)^k C_m C(k-1,m-1).
    Li_k = k[w^k]log(2Xi(1/(1-w))) via formal logarithm recursion.

    Every stage is finite analytic integration; **no nontrivial zeros**,
    contour roots, or analytic continuation fits enter the input.
    For a finite X, these are its Li-like jet coefficients; only in
    the N,T infinite limit are they THE true Li coefficients.
    """
    _nat(N,lo=1,hi=32,name="Li integer cutoff")
    _nat(degree,lo=1,hi=24,name="Li coefficient degree")
    mp=_mp()
    with mp.workdps(dps):
        T=mp.mpf(T)
        if not 0<=T<=5 or not mp.isfinite(T):
            raise BalancedWindowError("Li window T must be in [0,5]")
        A=[]
        for j in range(degree):
            weight=lambda u:(mp.power(u,j)*(mp.exp(u)+(-1)**j))
            value=mp.fsum(mp.quad(
                lambda u,n=n:mp.exp(-mp.pi*n*n*mp.exp(2*u))*weight(u),
                [0,T]) for n in range(1,N+1))/mp.factorial(j)
            A.append(value)
        C=[mp.mpf(0)]+[2*(A[m-1]+(A[m-2] if m>=2 else 0))
                        for m in range(1,degree+1)]
        B=[mp.mpf(1)]+[mp.fsum(C[m]*comb(k-1,m-1)
                                for m in range(1,k+1))
                        for k in range(1,degree+1)]
        Li=[mp.mpf(0)]*(degree+1)
        for k in range(1,degree+1):
            Li[k]=k*B[k]-mp.fsum(Li[j]*B[k-j] for j in range(1,k))
        return tuple(+v for v in Li[1:])


def li_all_degree_bound(N,T,degree,*,radius=Fraction(1,2),dps=85):
    """UNCONDITIONAL fixed-degree Xi theta-tail to Li-coefficient bound.

    s=1/(1-w), |w|<=r<=1/2 => 2/3<=Re(s)<=2 and
       |s(s-1)|<=B=r/(1-r)^2.
    For u>=0, |e^(su)|+|e^((1-s)u)|<=2e^(2u).
    Let L=exp(-π)/(π(1-exp(-3π))). Then for Xi and finite X
       |2Xi(s)-1|,|2X(s)-1| <= δ=2 B L <1.
    For the omitted INTEGER and WINDOW parts:
       |Xi(s)-X_[N,T](s)| <= E=B/π*(spatial+temporal)
       spatial = e^(-π(N+1)^2)/(N+1)^2/(1-e^(-π(2N+3)))
       temporal=e^(-π e^(2T))/(1-e^(-3π e^(2T))).
    Since analytic logs are well-defined on this disk and Cauchy
    controls coefficients,
       |lambda_k(xi)-lambda_k(X)| <= 2k E /((1-δ)r^k).
    This bound is zero-blind but NOT UNIFORM IN DEGREE: r^-k explodes.
    Numerical mp evaluation is not a directed-rounding certificate.
    """
    _nat(N,lo=1,hi=256,name="Li integer cutoff")
    _nat(degree,lo=1,hi=1000,name="Li degree")
    r=_frac(radius)
    if not Fraction(0)<r<=Fraction(1,2):
        raise BalancedWindowError("Certified Li disk radius must satisfy 0<r<=1/2")
    mp=_mp()
    with mp.workdps(dps):
        T=mp.mpf(T)
        if not mp.isfinite(T) or not 0<=T<=5:
            raise BalancedWindowError("Theta finite window 0<=T<=5 required")
        rr=_mpq(mp,r)
        B=rr/(1-rr)**2
        e0=mp.exp(-mp.pi)
        L=e0/(mp.pi*(1-mp.exp(-3*mp.pi)))
        delta=2*B*L
        if delta>=1:
            raise ArithmeticError("Analytic log disk nonvanishing condition failed")
        a=mp.exp(-mp.pi*(N+1)**2) /(
            (N+1)**2*(1-mp.exp(-mp.pi*(2*N+3))))
        e=mp.exp(2*T)
        b=mp.exp(-mp.pi*e)/(1-mp.exp(-3*mp.pi*e))
        E=B*(a+b)/mp.pi
        bound=2*degree*E/((1-delta)*mp.power(rr,degree))
        return {"degree":degree,"disk_radius":+rr,
                "xi_uniform_source_error":+E,
                "analytic_log_nonzero_margin":+(1-delta),
                "li_coefficient_error_bound":+bound,
                "gaussian_integer_tail":+a,
                "archimedean_window_tail":+b,
                "claim":"proved for exact finite integrals; printed mpmath bound not directed",
                "uniform_all_degrees":False}


def finite_double_zero(N=4,*,dps=48,init_t="11.210",init_T="0.32478"):
    """Hostile finite-zero collision calibration, not a zero input to RH.

    Solve X(1/2+i*t,T)=d/dt X(1/2+i*t,T)=0 in the
    *FINITE* Poisson theta model. Never fit actual zeta zero ordinates.
    """
    _nat(N,lo=1,hi=8,name="finite collision integer cutoff")
    mp=_mp()
    with mp.workdps(dps):
        fn=lambda t,T:mp.re(_xi_cut(mp.mpf("0.5")+mp.j*t,N,T,mp.mp.dps))
        slope=lambda t,T:mp.diff(lambda v:fn(v,T),t)
        t,T=mp.findroot((fn,slope),(mp.mpf(init_t),mp.mpf(init_T)),
                        tol=mp.power(10,-(dps-12)),maxsteps=20)
        s=mp.mpf("0.5")+mp.j*t
        a=mp.diff(lambda u:_xi_cut(s,N,u,mp.mp.dps),T)
        b=mp.diff(lambda x:_xi_cut(x,N,T,mp.mp.dps),s,2)/2
        if abs(mp.im(a))>mp.power(10,-(dps//2)) or abs(mp.im(b))>mp.power(10,-(dps//2)):
            raise ArithmeticError("Expected real symmetry at the finite double zero")
        return {"N":N,"t_star":+t,"T_star":+T,"linear_T":+mp.re(a),
                "quadratic_s":+mp.re(b),
                "off_line_splitting_coefficient":+mp.sqrt(-mp.re(a)/mp.re(b)),
                "residual":+abs(fn(t,T)),"slope_residual":+abs(slope(t,T)),
                "scope":"finite reflected theta approximant, NOT xi spectral zeros"}
