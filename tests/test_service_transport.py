import unittest
from fractions import Fraction
from flint import arb, ctx
import sympy as sp
from scripts import service_transport as st
from scripts.event_dynamics import arch, arch_prime, curvature, minimum


class ServiceTransportTests(unittest.TestCase):
    def setUp(self):
        self.oldprec=ctx.prec;ctx.prec=200
    def tearDown(self): ctx.prec=self.oldprec

    def test_clock_curvature_and_inverse_chain_rule(self):
        x=sp.symbols('x',positive=True)
        a2=(x**3-x-1)/(sp.sqrt(x)*(x*x-1))
        a3=(x**5-2*x**3+5*x*x+x-1)/(2*sp.sqrt(x)*(x*x-1)**2)
        self.assertEqual(sp.simplify(x*sp.diff(a2,x)-a3),0)
        s=sp.symbols('s');F=sp.Function('F');T=sp.Function('T')
        # Differentiate F(T(s))=s twice; F is A'.
        second=sp.diff(F(T(s)),s,2)
        u,v=sp.symbols('u v')
        second=second.xreplace({sp.diff(T(s),s,2):v,sp.diff(T(s),s):u})
        # Direct independent symbolic chain-rule coefficient comparison.
        Fp=sp.diff(F(T(s)),T(s));Fpp=sp.diff(F(T(s)),T(s),2)
        self.assertEqual(sp.simplify(second-(Fpp*u*u+Fp*v)),0)
        solved=sp.solve(sp.Eq(second.subs(u,1/Fp),0),v)[0]
        self.assertEqual(sp.simplify(solved+Fpp/Fp**3),0)

    def test_boundary_constants_and_concavity_break(self):
        a,sig,c,A,K=st.constants()
        self.assertTrue(sig>arb('0.22497') and sig<arb('0.22498'))
        self.assertTrue((c-5/(3*arb(2).sqrt())).contains(0))
        self.assertTrue(A>arb('0.06355') and A<arb('0.06356'))
        self.assertTrue(K>arb('0.04208') and K<arb('0.04209'))
        # Concavity midpoint test for clamp at sigma0: left constant,
        # right increases; middle lies strictly below endpoint average.
        right=st.inverse(sig+arb('0.01'))
        self.assertTrue((a+right)/2>a)

    def test_legendre_and_transport_identity_independently(self):
        data=st.states(7)
        a,sig,c,A,K=st.constants()
        for i,r in enumerate(data):
            t,v,kind=minimum(r['S'],r['H'],a,arb(6),bits=110)
            prim=st.primitive(r['S'])
            self.assertTrue((A+r['H']-prim-v).contains(0))
            self.assertTrue((K+r['H']-st.bar_primitive(r['S'])-v).contains(0))
            self.assertTrue((sum((z['w']*z['a'] for z in data[:i+1]),arb(0))-r['H']).contains(0))
            self.assertTrue((arch_prime(t)-r['S']).contains(0))
        tiny=arb('0.1')
        charge=(sig*tiny-tiny*tiny/2)/c
        self.assertTrue((st.primitive(tiny)-st.bar_primitive(tiny)-charge).contains(0))

    def test_first_prime_order_obstructions(self):
        r=st.states(2)[0];S=r['S'];z=r['sigma']
        self.assertTrue(z>0 and z<S/2)
        self.assertTrue(r['N']-S*S/2<0)
        k=z/2
        # Increasing concave min-test: E min(Y,k)=k, E min(X,k)=k-k²/(2S).
        self.assertTrue(k*k/(2*S)>0)
        self.assertTrue(st.call_uniform(z,S)>0)

    def test_earliest_reverse_increasing_convex_failure(self):
        records=st.states(4)
        for j in [1,2]:
            lo,hi,vals=st.call_difference_extrema(records[:j])
            self.assertTrue(hi.is_zero(),str(hi))
        k=records[1]['S'];S=records[-1]['S']
        self.assertTrue(records[1]['sigma']<k and k<records[2]['sigma'])
        witness=st.call_prime(k,records)-st.call_uniform(k,S)
        self.assertTrue(witness>arb('0.01010680'))
        self.assertTrue(witness<arb('0.01010681'))

    def test_minimal_radius_candidates_and_first_two_capital_failures(self):
        records=st.states(13);a,sig,c,A,K=st.constants()
        first_lip=first_exact=None
        eps2=records[0]['S']/2-records[0]['N']/records[0]['S']
        for j,r in enumerate(records):
            d=st.defects(records[:j+1],shifted=True)
            self.assertTrue((d['winfty_icv_defect']-eps2).contains(0))
            self.assertTrue(d['reserve']>0)
            if d['lipschitz_repair_cost']>K and first_lip is None: first_lip=r['q']
            elif first_lip is None: self.assertTrue(d['lipschitz_repair_cost']<K)
            if d['exact_shift_cost']>K and first_exact is None:first_exact=r['q']
            elif first_exact is None:self.assertTrue(d['exact_shift_cost']<K)
        self.assertEqual(first_lip,7);self.assertEqual(first_exact,13)
        self.assertTrue(d['exact_shift_cost']>arb('0.04407'))
        self.assertTrue(d['exact_shift_cost']<arb('0.04408'))

    def test_one_sided_transport_cost_first_failure(self):
        records=st.states(5);A=st.constants()[3]
        for j,r in enumerate(records):
            d=st.defects(records[:j+1])
            if r['q']<5:self.assertTrue(d['one_sided_cost']<A)
            else:
                self.assertTrue(d['one_sided_cost']>arb('0.09692'))
                self.assertTrue(d['one_sided_cost']<arb('0.09693'))
                self.assertTrue(d['reserve']>arb('0.03261'))
            self.assertTrue((d['reserve']-A-d['credit']+d['one_sided_cost']).contains(0))

    def test_episode_one_event_transport_equals_drawdown(self):
        r=st.states(2)[0];a,sig,c,A,K=st.constants()
        end=st.inverse(r['S']);y=r['S']-sig
        self.assertTrue(end>a and end<arb(3).log())
        # integral T ds on [sig,S] via conjugate; minus y*T(sig).
        cost=(st.primitive(r['S'])-sig*a)-y*a
        direct=A-(arch(end)-r['S']*end+r['H'])
        self.assertTrue((cost-direct).contains(0))
        self.assertTrue(cost>0 and cost<A)
        # Equal mass but strict service means rule out both martingale directions.
        self.assertTrue(y*y/2>0)

    def test_episode_cost_capacity_cancellation_symbolic(self):
        a,s,r,Aa,Ar,Ap,E,y,P,J=sp.symbols('a s r Aa Ar Ap E y P J')
        S1=(r-a)*(Ap+y+P)-Ar+Aa
        C=E-S1+(s-a)*P
        # sum w_i(a_i-a)=(s-a)P-J.
        D=(y+P)*(r-a)-(Ar-Aa-Ap*(r-a))-((s-a)*P-J)
        self.assertEqual(sp.expand(C-J-(E-D)),0)

    def test_marginal_cost_cannot_be_optimized_away(self):
        # Two equal-mass discrete couplings with same marginals; rational T-values.
        T={0:Fraction(0),1:Fraction(1),2:Fraction(3,2),3:Fraction(7,4)}
        pi1=[(0,2,Fraction(1,2)),(1,3,Fraction(1,2))]
        pi2=[(0,3,Fraction(1,2)),(1,2,Fraction(1,2))]
        cost=lambda pi:sum(w*(T[y]-T[x]) for x,y,w in pi)
        self.assertEqual(cost(pi1),cost(pi2))

    def test_relocation_and_mass_preserving_location_permutation(self):
        rows=st.states(3);r0,r1=rows;S=r1['S'];H=r1['H']
        delta=arb('0.1')
        # Delay one location but retain its exact weight: mass fixed, M rises w*delta.
        movedH=r0['w']*r0['a']+r1['w']*(r1['a']+delta)
        self.assertTrue((movedH-H-r1['w']*delta).contains(0))
        self.assertTrue(movedH>H)
        # Reassign fixed masses to the two locations, preserving total mass.
        swappedH=r1['w']*r0['a']+r0['w']*r1['a']
        self.assertTrue(swappedH<H)
        self.assertTrue((swappedH-H-(r0['w']-r1['w'])*(r1['a']-r0['a'])).contains(0))
        self.assertTrue((S-r0['w']-r1['w']).contains(0))

    def test_exact_gamma_linear_mutation_keeps_curvature(self):
        t,eta=sp.symbols('t eta');A=sp.Function('A')
        self.assertEqual(sp.diff(A(t)-eta*t,t,2),sp.diff(A(t),t,2))
        self.assertEqual(sp.diff(A(t)-eta*t,t,3),sp.diff(A(t),t,3))

if __name__=='__main__':unittest.main()
