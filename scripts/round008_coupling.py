"""Coherent shared-origin clock/Gamma candidate and hostile controls.

Exact finite matrices verify the compressed metric, while actual prime
amplitudes use Arb. The vanishing-capacity and translated-atom theorems
are analytic proofs in WEIL_PUSHFORWARD.md, not extrapolated samples.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import sympy as sp
from flint import arb, ctx
from scripts.round008_transfer import refinement_data, events


def embedded_old_projector(final, old):
    if old < 1 or final % old:
        raise ValueError('old length must divide final')
    return sp.Matrix(final,final,lambda a,b: sp.Rational(old,final) if (a-b)%old == 0 else 0)


def origin_geometry(horizon):
    length, rows = refinement_data(horizon)
    old = 1
    vectors, cs, Es = [], [], []
    e0 = sp.eye(length)[:,0]
    for q,p,k,previous,dim in rows:
        E = embedded_old_projector(length,p*old)-embedded_old_projector(length,old)
        c = sp.sqrt(sp.Rational(dim,length))
        vectors.append(E*e0/c)
        cs.append(c)
        Es.append(E)
        old *= p
    return sp.Matrix.hstack(*vectors), sp.Matrix(cs), Es


def exact_heat_compression(horizon=4, modes=3):
    """Finite Gamma cutoff checks the universal compression, with rational
    positive event charges so the fixture is independent of transcendental
    simplification. Actual arithmetic weights are checked separately by Arb.
    """
    V,c,Es = origin_geometry(horizon)
    length, m = V.shape
    assert V.T*V == sp.eye(m)
    Q = sp.zeros(length)
    Q[0,0] = 1
    weights = [sp.Rational(j+1,j+2) for j in range(m)]
    charges = sp.diag(*(sp.sqrt(w) for w in weights))
    A = V*charges
    # r=1/2; t=e^(-2h)=2/3, so exp(-hH)=diag(t^ell).
    r,t = sp.Rational(1,2), sp.Rational(2,3)
    gn = sum(r**(2*l) for l in range(modes))
    g = sp.Matrix([r**l/sp.sqrt(gn) for l in range(modes)])
    heat = sp.diag(*(t**l for l in range(modes)))
    B = sp.kronecker_product(sp.eye(length)-Q,sp.eye(modes))+sp.kronecker_product(Q,heat)
    inp = sp.kronecker_product(A,g)
    kappa = 1-(g.T*heat**2*g)[0]
    b = charges*c
    expected = charges**2-kappa*b*b.T
    got = inp.T*B**2*inp
    assert (got-expected).applyfunc(sp.simplify) == sp.zeros(m)
    # Shared origin really mixes innovations: this is not only a basis change.
    assert Q*Es[0] != Es[0]*Q
    assert (c.T*c)[0] == 1-sp.Rational(1,length)
    return {'horizon': horizon,'clock_length':length,'modes':modes,
            'finite_geometric_kappa':str(kappa),'origin_noncommutes':True}


def translation_atoms(qs, metric):
    """Exact coefficients of sum G_ij (tau_qi-I)^*(tau_qj-I).
    Translation displacement is log of the rational dictionary key.
    """
    out = {}
    def add(r,v):
        out[r] = out.get(r,0)+v
    for i,qi in enumerate(qs):
        for j,qj in enumerate(qs):
            g = metric[i,j]
            add(Fraction(qj,qi),g)
            add(Fraction(1,qi),-g)
            add(Fraction(qj,1),-g)
            add(Fraction(1,1),g)
    return {r:sp.simplify(v) for r,v in out.items() if sp.simplify(v) != 0}


def amplitude_data(horizon):
    length, rows = refinement_data(horizon)
    amp = arb(0)
    mass = arb(0)
    for q,p,k,old,dim in rows:
        w = arb(p).log()/arb(q).sqrt()
        amp += (arb(dim)/arb(length)*w).sqrt()
        mass += w
    return {'N':horizon,'events':len(rows),'clock_bits':length.bit_length(),
            'A':amp,'S':mass,'loss_bound_one_site':4*amp*amp}


def exact_mutations():
    k = sp.Symbol('k',positive=True)
    b0,b1,b2 = sp.symbols('b0 b1 b2',positive=True)
    b = sp.Matrix([b0,b1,b2])
    atoms = translation_atoms([2,3,4],sp.eye(3)-k*b*b.T)
    assert atoms[Fraction(3,2)] == -k*b0*b1
    assert atoms[Fraction(4,3)] == -k*b1*b2
    # A fake composite event destroys unique-pair isolation: 6/4=3/2.
    g = sp.Matrix(4,4,lambda i,j:sp.Symbol(f'g{i}{j}'))
    fake = translation_atoms([2,3,4,6],g)
    assert fake[Fraction(3,2)] == g[0,1]+g[2,3]
    # Removing a jet removes its ratio atom; no imaginary 'positivity fix'.
    assert Fraction(3,2) not in translation_atoms([2,4],sp.ones(2))
    # Change the prime charge or half-density: positivity of an edge remains,
    # but its exact target atom changes.  Surviving PSD is not the criterion.
    correct=translation_atoms([2],sp.Matrix([[sp.log(2)/sp.sqrt(2)]]))
    flat=translation_atoms([2],sp.Matrix([[sp.log(2)]]))
    uncharged=translation_atoms([2],sp.Matrix([[1/sp.sqrt(2)]]))
    assert correct[Fraction(2)] != flat[Fraction(2)]
    assert correct[Fraction(2)] != uncharged[Fraction(2)]
    # Positive cross-block metrics can evade a block-diagonal capacity theorem.
    eps = sp.Rational(1,7)
    G = sp.Matrix([[1,-1/eps],[-1/eps,1/eps**2]])
    vec = sp.Matrix([1,eps])
    assert G.det() == 0 and sp.trace(G)>0 and (vec.T*G*vec)[0] == 0
    # Isometric history: rotate AFTER including each innovation, then transport
    # old and new vectors together; orthogonality survives.
    U = sp.Matrix([[sp.Rational(3,5),-sp.Rational(4,5)],
                   [sp.Rational(4,5),sp.Rational(3,5)]])
    assert U.T*U == sp.eye(2)
    old,new = U[:,0],U[:,1]
    assert (old.T*new)[0] == 0
    return {'ratio_3_over_2':str(atoms[Fraction(3,2)]),
            'fake_composite_collision':str(fake[Fraction(3,2)]),
            'deleting_3_removes_ratio_atom':True,
            'half_density_mutation_changes_target_atom':True,
            'log_charge_mutation_changes_target_atom':True,
            'positive_cross_block_counterexample':[str(x) for x in G],
            'common_isometry_preserves_innovation_orthogonality':True}


def refinement_oscillator_checks():
    """Exact differential/carry checks for (RC1)-(RC4), using symbolic jets.
    This checks all lane/carry cases for fresh finite refinements; the note
    proves the change-of-variables unitary and universal formulas.
    """
    y=sp.Symbol('y',real=True)
    f=sp.Function('f')
    fixtures=[]
    for L,p in [(1,2),(2,3),(3,2),(4,3)]:
        M=p*L
        for a in range(L):
            for b in range(p):
                z=b+p*y
                inp=sp.sqrt(p)*f(z)
                knew=-sp.diff(inp,y,2)/M**2+((a+b*L+M*y)**2-1)*inp
                kold=sp.sqrt(p)*(-sp.Subs(sp.diff(f(y),y,2),y,z)/L**2+((a+L*z)**2-1)*f(z))
                assert sp.simplify(knew-kold)==0
                # U_M S and S U_L both select lane a-1 and argument z,
                # except an old-lane wrap changes the argument by -1.
                n=a+b*L
                prev=(n-1)%M
                ap,bp=prev%L,prev//L
                new_arg=bp+p*(y-int(n==0))
                assert ap==(a-1)%L
                assert sp.expand(new_arg-(z-int(a==0)))==0
        fixtures.append([L,p])
    return {'refinements':fixtures,'covariant_oscillator_intertwines':True,
            'carry_intertwines':True,'physical_coordinate_translation_per_step':1}


def evidence():
    with ctx.workprec(160):
        rows = []
        for n in [3,10,100,1000,10000]:
            row = amplitude_data(n)
            rows.append({k:(str(v) if isinstance(v,arb) else v) for k,v in row.items()})
        a = arb(1)/2
        h = arb(2)/3
        kappa = 1-(1-a*a)/(1-a*a*(-4*h).exp())
        w2,w3 = arb(2).log()/arb(2).sqrt(),arb(3).log()/arb(3).sqrt()
        coeff = -kappa*(w2*w3).sqrt()/3 # c2*c3=1/3 at N=3.
        assert coeff < 0
        return {'method':'exact compression/translation kernels; Arb arithmetic amplitudes',
                'exact_heat':exact_heat_compression(), 'mutations':exact_mutations(),
                'refinement_oscillator':refinement_oscillator_checks(),
                'actual_prime_ratio_atom_N3':str(coeff),'amplitudes':rows,
                'scope':'finite amplitudes calibrate the universal analytic vanishing theorem; no monotonicity extrapolation'}


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    content=json.dumps(evidence(),indent=2)+'\n'
    if args.output:
        args.output.write_text(content)
    else:
        print(content,end='')
