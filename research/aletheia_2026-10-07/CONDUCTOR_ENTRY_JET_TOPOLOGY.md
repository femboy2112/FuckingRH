# Conductor-entry actualization jets: cubic on Dirichlet states, linear on logarithmic states, discontinuous in operator norm

**Date:** 2026-10-07  
**Branch:** \`research/rh-log-bathtub-prime-shift-2026-10-07\`  
**Status:** exact finite-horizon theorem and hostile topology control. **RH remains OPEN.**

This is the correct mathematical distinction behind the "first domino" intuition. A prime-power translation term starts acting as soon as the interval becomes longer than its displacement, but the apparent smoothness of that birth depends drastically on the class of states and the topology.

A cubic actualization law on smoothly transported Dirichlet states is correct. It is **false** on the full logarithmic Weil form domain, and the operator itself has an immediate norm jump.

That is not a contradiction; it is the sort of nonuniform finite-to-infinite behavior a valid RH proof must not hide.

## 1. Prime event enters the localized Weil form

Fix a genuine prime power \(q=p^k\). Write

\[
h=\log q,\qquad
w_q=\frac{\log p}{\sqrt q},\qquad
a_0=\frac h2.
\]

Let \(I_a=(-a,a)\), and let \(v_a\in L^2(I_a)\) be zero extended.

The new prime correlation in Suzuki's form is

\[
\boxed{
\mathcal P_q(a;v_a)
=
-2w_q\,\Re C_h(a;v_a)
}
\]

with

\[
C_h(a;v_a)
=
\int_{\mathbb R}
v_a(x+h)\overline{v_a(x)}\,dx.
\]

For \(a\le a_0\), the intervals do not overlap and

\[
C_h(a;v_a)=0.
\]

Let

\[
a=a_0+\delta,\qquad
\varepsilon=2a-h=2\delta>0.
\]

Then the first overlap is the strip

\[
-a\le x\le-a+\varepsilon,
\]

and

\[
\boxed{
C_h(a;v_a)
=
\int_0^\varepsilon
v_a(a-\varepsilon+s)
\overline{v_a(-a+s)}\,ds.
}
\]

No approximation has been made.

## 2. Smooth Dirichlet states: cubic actualization

Take a fixed \(f\in C^2([-1,1])\) satisfying

\[
f(-1)=f(1)=0.
\]

Transport it with the interval:

\[
v_a(x)=a^{-1/2}f(x/a).
\]

As \(\delta\downarrow0\),

\[
f(-1+s/a)=f'(-1)s/a+O(\varepsilon^2/a^2),
\]

\[
f(1-(\varepsilon-s)/a)
=-f'(1)(\varepsilon-s)/a+O(\varepsilon^2/a^2).
\]

Insert into the exact overlap:

\[
\boxed{
C_h(a;v_a)
=
-\frac{4}{3}
\frac{\delta^3}{a_0^3}
f'(1)\overline{f'(-1)}
+
O_{f,h}(\delta^4).
}
\]

Hence

\[
\boxed{
\mathcal P_q(a;v_a)
=
\frac83
\frac{w_q\,\delta^3}{a_0^3}
\Re\bigl(f'(1)\overline{f'(-1)}\bigr)
+
O_{f,h}(\delta^4).
}
\]

**The first two conductor-entry derivatives vanish on this transported smooth Dirichlet class.**

### Exact polynomial check

For \(f(t)=1-t^2\), the overlap integral is a polynomial in \(\varepsilon=2\delta\):

\[
\boxed{
C_h(a;v_a)
=
\frac{2\varepsilon^3}{3a^3}
-\frac{\varepsilon^4}{3a^4}
+\frac{\varepsilon^5}{30a^5}.
}
\]

Its leading term is exactly \(16\delta^3/(3a_0^3)\), in agreement with the general theorem.

## 3. Uniform \(H_0^1\) bound: quadratic, not cubic

For a general \(v\in H_0^1(-a,a)\), its Dirichlet boundary traces are zero.

The one-sided Cauchy–Schwarz inequality gives

\[
\int_{-a}^{-a+\varepsilon}|v(x)|^2dx
\le
\frac{\varepsilon^2}{2}
\int_{-a}^{-a+\varepsilon}|v'(x)|^2dx,
\]

and analogously at the other endpoint.

Applying Cauchy–Schwarz to the overlap yields

\[
\boxed{
|C_h(a;v)|
\le
\frac{\varepsilon^2}{2}\,\|v'\|_2^2
=
2\delta^2\|v'\|_2^2.
}
\]

Consequently

\[
\boxed{
|\mathcal P_q(a;v)|
\le4w_q\delta^2\|v'\|_2^2.
}
\]

This uniform quadratic estimate is useful for form convergence on bounded \(H_0^1\) balls.

It does not imply a cubic bound there: smoothness and fixed-shape control are additional hypotheses.

## 4. Hostile counterexample: the full logarithmic domain has linear onset

The closed logarithmic Weil form domain allows functions with nonzero one-sided boundary traces, including zero-extended interval indicators (as discussed in Suzuki 2026, Section 3).

Take

\[
v_a(x)=\frac1{\sqrt{2a}}\,1_{(-a,a)}(x).
\]

Then exactly, for \(a>a_0\),

\[
\boxed{
C_h(a;v_a)
=
\frac{2a-h}{2a}
=
\frac{\delta}{a}.
}
\]

Thus

\[
\boxed{
\mathcal P_q(a;v_a)
=
-2w_q\frac{\delta}{a},
}
\]

which has a nonzero first derivative at \(a=a_0\).

Therefore the tempting global claim

> every conductor event enters only at cubic order

is **false**. Cubic onset is a Dirichlet-core phenomenon, not a statement about the actual spectral form domain.

## 5. Stronger hostile control: the shift operator jumps in norm

Let \(P_a\) be restriction to \((-a,a)\) and define the compressed shift

\[
T_{h,a}=P_a\tau_hP_a
\]

on \(L^2(-a,a)\).

For \(2a\le h\),

\[
T_{h,a}=0.
\]

For **every** \(2a>h\), even an arbitrarily small overlap interval, \(T_{h,a}\) is a nonzero partial isometry of norm one:

\[
\boxed{
\|T_{h,a}\|_{2\to2}=1.
}
\]

The symmetric correlation operator is

\[
T_{h,a}+T_{h,a}^*.
\]

Immediately above the threshold, with \(1<2a/h<2\), the residue-mod-\(h\) decomposition consists of two-point chains. Its operator norm is exactly one:

\[
\boxed{
\|T_{h,a}+T_{h,a}^*\|=1
\qquad(h/2<a<h).
}
\]

At the threshold it is zero.

Hence the \(q\)-prime contribution to the localized Weil operator jumps from norm zero to norm \(w_q\) at its birth, although its quadratic form on transported smooth Dirichlet states is only \(O(\delta^3)\).

There is no contradiction: the operator-norm maximizers concentrate inside a shrinking boundary strip and are not bounded in the Dirichlet/energy norm.

## 6. Actualization is topology-dependent

The precise picture is:

\[
\boxed{
\text{smooth Dirichlet jets: cubic onset}
}
\]

\[
\boxed{
H_0^1\text{ bounded sets: at most quadratic onset}
}
\]

\[
\boxed{
\text{full logarithmic domain: linear onset possible}
}
\]

\[
\boxed{
L^2\text{ operator norm: instantaneous nonzero jump}
}
\]

This is a real mathematical reason why the globally completed spectrum cannot be controlled from one smooth test trajectory or one finite-state numerical calculation.

The other smooth Archimedean and pole terms are essential when studying the full operator. This note concerns the isolated arithmetic event contribution and does not claim that the **total** Weil operator has a norm jump in some canonical moving-space identification.

## 7. Proof implications

- Use \(H_0^1\) seam jets to obtain **valid local continuation estimates** for fixed smooth test families.
- Do not extrapolate those jets to the ground-state eigenfunction, which lives in the larger logarithmic form domain.
- Do not use operator-norm continuity of isolated arithmetic event blocks at their birth; it is false.
- Any all-horizon spectral-flow theorem must track the moving domain/graph norm and the exact sum of prime, Gamma and pole terms.

**DISCLOSED:** cubic Dirichlet jet, quadratic \(H_0^1\) bound, linear indicator counterexample, operator-norm jump.

**RH:** OPEN.
