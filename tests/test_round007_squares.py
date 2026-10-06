import unittest
import sympy as sp
from flint import arb,ctx
from scripts.round007_squares import carrier_channels,block_dirac,event_weights,kernel_parts,residual_matrix,gamma_linear

class SquareTests(unittest.TestCase):
    def test_rectangular_chiral_square_retains_boundary(self):
        for N in [1,2,7,13]:
            C=carrier_channels(N,{})['chiral']
            S=sp.zeros(N)
            for i in range(N-1):S[i+1,i]=1
            self.assertEqual(C.T*C,2*sp.eye(N)-S-S.T)
            bad=C[:N,:]
            self.assertNotEqual(bad.T*bad,C.T*C)

    def test_couple_before_square_changes_energy(self):
        c=carrier_channels(9,{2:sp.Integer(4),3:sp.Integer(9),4:sp.Integer(1)})
        A,B=c['chiral'],c['jet'];cross=A.T*B+B.T*A
        self.assertNotEqual(cross,sp.zeros(9))
        self.assertEqual((A-B).T*(A-B),A.T*A+B.T*B-cross)
        # This actual oriented cross term links affine integers, not just jets.
        self.assertNotEqual(cross[0,2],0)

    def test_doubled_dirac_grading(self):
        A=carrier_channels(4,{})['chiral'];D=block_dirac(A)
        G=sp.diag(*([1]*A.cols+[-1]*A.rows))
        self.assertEqual(D,D.T)
        self.assertEqual(G*D+D*G,sp.zeros(D.rows))
        self.assertEqual((D*D)[:A.cols,:A.cols],A.T*A)

    def test_flux_invisible_internal_jet_transition(self):
        c=carrier_channels(10,{})
        # 2->3 is inside one-support stratum, so current alone cannot count Lambda.
        self.assertEqual(c['flux'][2,1],0)
        self.assertNotEqual(c['flux'][5,4],0) # 5->6 exits.

    def test_exact_residual_and_negative_direction(self):
        ctx.prec=160
        for N in (8,27,125): # distinct from evidence construction horizons
            w=event_weights(N);L=arb(N).log();ts=[L/4,L/2,3*L/4]
            R=residual_matrix(ts,w)
            v=[(ts[1]/2).sinh(),-(ts[0]/2).sinh(),arb(0)]
            val=sum((v[i]*R[i][j]*v[j] for i in range(3) for j in range(3)),arb(0))
            self.assertTrue(val<0)
            for t in ts:
                for u in ts:
                    E,r,K=kernel_parts(t,u,w)
                    self.assertTrue((K-E-r).contains(0))

    def test_event_mutation_changes_target_not_identity(self):
        ctx.prec=160;N=16;t=arb(N).log();base=event_weights(N)
        for changes in ({3:None},{6:arb(2).log()},{2:2*base[2]}):
            mutated=event_weights(N,changes)
            eb,rb,kb=kernel_parts(t,t,base)
            e,r,k=kernel_parts(t,t,mutated)
            self.assertTrue((k-e-r).contains(0))
            self.assertFalse((k-kb).contains(0))

    def test_gamma_constant_certified_negative(self):
        ctx.prec=120
        self.assertTrue(gamma_linear()<0)

if __name__=='__main__':unittest.main()
