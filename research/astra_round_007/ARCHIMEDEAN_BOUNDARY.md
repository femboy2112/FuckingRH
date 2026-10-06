# Archimedean completion inside the lifted square

The exact inherited source formula is retained; its passivity label is not.
See `PARENT_AUDIT.md` for the distinction and certified correction.

For the present quadratic-form program the useful first-order object is
\[
D_\Gamma f(u,x)=
\sqrt{e^{-u/2}/(1-e^{-2u})}\,[f(x-u)-f(x)],\quad u>0.
\]
Its norm square is exactly the nonnegative digamma **difference** multiplier.
The remaining Archimedean scalar is
`c0=psi(1/4)-log pi<0`; the pole form is the rank-two cross pairing
`2Re ell_+ conj(ell_-)`. All pieces enter the finite-horizon identity before
any passage to infinity. The complete derivation is in `WEIL_SQUARE_ATTEMPT.md`.

This construction reuses the valid regularized Gamma data without taking a
positive-real source response. The measure has infinitely much mass at zero
(`k(u)~1/(2u)`), but translation differences make the energy finite. Replacing
it by a finite set of event channels or omitting its small-u sector changes
Suzuki's origin behavior `Psi(t)~(t/2)log(1/t)`.

A cone supported only at square thresholds cannot manufacture this smooth
continuum: its jump measure is atomic, while the Gamma difference density is
positive for every u>0. This is an exact mismatch for the literal measure
identification, not a theorem against a separately constructed integral
transform. An infinite continuous boundary space could supply it; its metric
and cross pairing would still need derivation.

The half-height cone gives the geometric equation `2u=t`. It does not derive
the Gamma density, the scale constant `log pi`, or `w_n=Lambda(n)/sqrt n`.
The factor audit supplies a continuum of weights preserving cone/swap while
changing the amplitude. The analytic half-density follows from a chosen
L2 measure and dilation unitarity; linking that choice to this discrete cone
is an additional, presently unpaid identity.
