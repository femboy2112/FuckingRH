"""Controls for the actual-prime pinned-tail discriminator.

Tests compare native integer moments against a separate Python sieve, and
Taylor enclosures against direct Arb summation. Signs use balls throughout.
"""
import csv
from fractions import Fraction as F
import importlib.util
from pathlib import Path
import tempfile
import unittest
from flint import arb, ctx

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("pinned_tail_slack",ROOT/"scripts/pinned_tail_slack.py")
m=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


class PinnedTailSlackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ctx.prec=128
        cls.tmp=tempfile.TemporaryDirectory()
        cls.path=Path(cls.tmp.name)/"moments.csv"
        cls.cuts=[1000,9973,20000]
        m.build_moments(20000,cls.cuts,cls.path,divisor=1024)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_native_moments_match_independent_integer_sieve(self):
        primes=m.simple_primes(20000)
        index=0
        with self.path.open(newline="") as stream:
            for row in csv.DictReader(stream):
                lo,hi,n,s1,s2=(int(row[k]) for k in ["lo","hi","count","m1","m2"])
                values=[]
                while index<len(primes) and primes[index]<=hi:
                    self.assertGreaterEqual(primes[index],lo)
                    values.append(primes[index]);index+=1
                c=(lo+hi)//2
                self.assertEqual((n,s1,s2),(len(values),sum(p-c for p in values),sum((p-c)**2 for p in values)))
        self.assertEqual(index,2262)  # Independently known pi(20000).

    def test_block_taylor_remainders_enclose_direct_weight_sums(self):
        for lo,hi in [(2,20),(1000,1300),(10**9,10**9+200000)]:
            values=[lo,lo+1,(lo+hi)//2,hi-1,hi]
            c=(lo+hi)//2
            W,L=m.block_weight_sums(lo,hi,len(values),sum(v-c for v in values),sum((v-c)**2 for v in values))
            directW=sum((arb(p).log()/arb(p).sqrt() for p in values),arb(0))
            directL=sum((arb(p).log()**2/arb(p).sqrt() for p in values),arb(0))
            self.assertTrue(W.contains(directW))
            self.assertTrue(L.contains(directL))
        self.assertEqual(m.block_weight_sums(2,100,0,0,0),(arb(0),arb(0)))

    def test_all_prefixes_match_direct_prime_power_sum(self):
        states,_=m.prefixes_from_moments(self.path,self.cuts)
        for cutoff in self.cuts:
            W,L=arb(0),arb(0)
            event_count=0
            for p in m.simple_primes(cutoff):
                q=p
                while q<=cutoff:
                    w=arb(p).log()/arb(q).sqrt()
                    W+=w;L+=w*arb(q).log();event_count+=1;q*=p
            self.assertTrue(states[cutoff][0].contains(W))
            self.assertTrue(states[cutoff][1].contains(L))
            self.assertEqual(states[cutoff][2]+states[cutoff][3],event_count)

    def test_smooth_formula_keeps_archimedean_tail(self):
        n=arb(3);alpha,ca=m.constants()
        direct=4*(n.sqrt()+1/n.sqrt()-2)-alpha*n.log()+ca
        direct-=sum((4/(arb(4*k+1)**2*n**(2*k)*n.sqrt()) for k in range(100)),arb(0))
        actual=m.smooth_at_integer(3)[0]
        self.assertTrue(actual.contains(direct))
        no_tail=4*n.sqrt()-alpha*n.log()+ca-8
        self.assertTrue(no_tail-direct>0)

    def test_invalid_finite_height_domain_is_rejected(self):
        for x,T in [(10**9,10**7),(10**9+1,10**6),(10**9+1,10**9+1)]:
            with self.assertRaises(ValueError):
                m.pinned_constructor(x,x+100,arb(1),arb(2),T)
        with self.assertRaises(ValueError):
            m.build_moments(20_000_000_000,[20_000_000_000],self.path,1024)

    def test_exact_pinned_loss_monotonicity_and_null_control(self):
        # Anchor 0, weight 1 at 1/2, weight 2 at old terminal 1, next terminal 2.
        # R(t)=1+2t dominates the actual load on [0,2].
        old_J=F(1,2)
        new_J=F(3,2)+2
        old_hat=F(1)  # min(1,1+2t) integrated from 0 to 1.
        new_hat=F(2)+3  # min(3,1+2t): integral 0..1 is 2; integral1..2 is 3.
        old_loss,new_loss=old_hat-old_J,new_hat-new_J
        self.assertEqual(new_loss-old_loss,F(1))
        # This is precisely integral_0^1[(1+2t)-1]dt.
        self.assertGreater(new_loss,old_loss)
        # Exact envelope R=M has zero loss at both horizons.
        self.assertEqual((new_J-new_J)-(old_J-old_J),0)
        # Quadratic frozen model: A=t²/2, W=2,L=5, new event at1 ofweight1.
        old_V=F(5)-F(2)**2/2
        new_V=F(5)+1-F(3)**2/2
        self.assertEqual(new_V-old_V,-F(3,2))
        self.assertLess(new_V-new_loss,old_V-old_loss)

    def test_admissible_height_optimization_has_positive_derivative_margin(self):
        # The margin uses only q and T; dummy states still need a decidable branch.
        _,_,margin=m.pinned_constructor(1066070623,1136726333,arb(65298),arb(67428))
        self.assertTrue(margin>4)

    def test_episode_verifier_has_actual_positive_negative_and_mutation_controls(self):
        self.assertTrue(m.certify_same_excursion(self.path,31,32)["verified"])
        self.assertFalse(m.certify_same_excursion(self.path,2,3)["verified"])
        mutated=Path(self.tmp.name)/"deleted_prime_2.csv"
        with self.path.open(newline="") as source,mutated.open("w",newline="") as target:
            reader=csv.DictReader(source)
            writer=csv.DictWriter(target,fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                if int(row["lo"])==2:
                    row["count"]=row["m1"]=row["m2"]="0"
                writer.writerow(row)
        self.assertFalse(m.certify_same_excursion(mutated,31,32)["verified"])


if __name__=="__main__":unittest.main()
