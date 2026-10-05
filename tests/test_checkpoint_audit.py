from fractions import Fraction
import json
import unittest
import sympy as s

class CheckpointAudit(unittest.TestCase):
    def test_curvature_from_slope(self):
        x=s.symbols('x',positive=True)
        slope=2*(s.sqrt(x)-1/s.sqrt(x))+s.atanh(1/s.sqrt(x))+s.atan(1/s.sqrt(x))
        curvature=x*s.diff(slope,x)
        target=(x**3-x-1)/(s.sqrt(x)*(x**2-1))
        self.assertEqual(s.simplify(curvature-target),0)
        derivative=s.factor(x*s.diff(target,x))
        expected=(x**5-2*x**3+5*x**2+x-1)/(2*s.sqrt(x)*(x**2-1)**2)
        self.assertEqual(s.simplify(derivative-expected),0)
    def test_eq75_exact_missing_residual(self):
        v=s.symbols('v',positive=True)
        # h(v)=atanh(v)+atan(v)-2v. Its derivative is positive on (0,1).
        h=s.atanh(v)+s.atan(v)-2*v
        self.assertEqual(s.simplify(s.diff(h,v)-2*v**4/(1-v**4)),0)
        self.assertEqual(s.series(h,v,0,14).removeO(),2*v**5/5+2*v**9/9+2*v**13/13)
        # Source domain x>1e9: choose x=1e10, so v=1e-5 exactly.
        v0=Fraction(1,100000)
        lower=2*v0**5/5
        upper=lower/(1-v0**4)
        self.assertGreater(lower,0)
        self.assertLess(lower,upper)
        # Therefore claimed residual 0 is impossible in its valid theorem range.
    def test_positive_kernel_primitive(self):
        y,q=s.symbols('y q',positive=True)
        f=s.log(q/y)/s.sqrt(y)
        self.assertEqual(s.simplify(-s.diff(f,y)-y**s.Rational(-3,2)*(1+s.log(q/y)/2)),0)
    def test_capacity_balance_formal(self):
        E,Y,a,tau,t,P,Aa,At,Apa,Apt=s.symbols('E Y a tau t P Aa At Apa Apt')
        # tau solves Apt=Apa+Y+P, and frozen drawdown integrates Y+P - (A'-Apa).
        S1=(tau-a)*Apt-At+Aa
        J,first=s.symbols('J first')
        V=E-(tau-a)*Y+(At-Aa)-(tau-a)*Apa-P*(tau-a)+first
        CminusJ=E-S1+(t-a)*P-J
        self.assertEqual(s.expand((V-CminusJ).subs(Apt,Apa+Y+P).subs(first,(t-a)*P-J)),0)

if __name__=='__main__':
 unittest.main()
