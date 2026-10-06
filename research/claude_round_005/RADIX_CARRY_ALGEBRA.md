# Radix-m carry algebra: SUCC = harmonic carrier + boundary carry

**Date:** 2026-10-06. **Status:** exact (DISCLOSED), verified `scripts/radix_carry_algebra.py`. RH open.

## 1. The central carry decomposition (exact)

With the radix-m coordinate $D_m|mq+r\rangle=|q\rangle\otimes|r\rangle$ ($0\le r<m$), successor
$S|n\rangle=|n+1\rangle$, and the cyclic residue shift $C_m|r\rangle=|r+1\bmod m\rangle$:
\[
\boxed{\ \tilde S_m:=D_mSD_m^\*=I\otimes C_m+(S-I)\otimes|0\rangle\langle m-1|\ .}
\]
*Proof.* $\tilde S_m|q,r\rangle=D_m|mq+r+1\rangle$. For $r<m-1$: $=|q,r+1\rangle$, matched by $I\otimes C_m$
(the carry term vanishes, $\langle m-1|r\rangle=0$). For $r=m-1$: $mq+m=m(q+1)$, so $=|q+1,0\rangle$;
$I\otimes C_m$ gives $|q,0\rangle$ and the carry $(S-I)\otimes|0\rangle\langle m-1|$ gives
$(|q+1\rangle-|q\rangle)\otimes|0\rangle$, summing to $|q+1,0\rangle$. $\square$ (Verified exactly, m=2,3,5.)

**Reading.** $I\otimes C_m$ = pure **m-phase clock / harmonic carrier** (unitary); $(S-I)\otimes|0\rangle\langle m-1|$
= **boundary carry correction**, nonzero only at the top residue $m-1$, where it emits the quotient
innovation $S-I$ and resets the residue. SUCC = harmonic carrier + carry.

## 2. Binary (m=2): the full adder

Residue = low bit. The increment $n\mapsto n+1$ on $(q,\text{bit})$ realizes
\[
\text{bit}'=\text{bit}\oplus\text{carry}_{\rm in},\qquad \text{carry}_{\rm out}=\text{bit}\wedge\text{carry}_{\rm in},
\]
with $\text{carry}_{\rm in}=1$ (incrementing). The carry term $(S-I)\otimes|0\rangle\langle1|$ fires exactly
when bit$=1$ (carry out), advancing the quotient. Projecting $\mathbb Z_2\to\mathbb Z/2^K$ is the finite-width
binary odometer. Under the 2-point Hadamard on the residue leg, $|0\rangle\pm|1\rangle$ are the DC/parity
channels — so **2 is the first nontrivial harmonic/refinement clock of SUCC** (an implementation/hierarchy
statement, not a worship claim; see §13 of the round plan).

## 3. Polyphase Fourier form (exact)

Under the DFT $F_m$ on the residue leg, $C_m$ diagonalizes to the characters $e^{-2\pi i a/m}$
($a=0,\dots,m-1$), and the carry $|0\rangle\langle m-1|$ becomes a **rank-1** operator coupling all $m$
harmonic channels (verified: single nonzero singular value). Hence
\[
\boxed{\ F_m\tilde S_mF_m^\*=\underbrace{\mathrm{diag}(e^{-2\pi i a/m})}_{\text{harmonic carrier}}
+\underbrace{(S-I)\otimes \tfrac1m|\hat0\rangle\langle\hat v|}_{\text{rank-1 carry coupling }\otim:\text{ quotient-SUCC diff}}.\ }
\]
The $a=0$ channel is the unique DC/coarse channel; $a\ne0$ are orthogonal detail/carry channels. For
$m=2$ this is Haar average/detail + carry; for prime $p$ it is a $p$-ary filter bank. The carry coupling
is exactly the "harmonic carrier + low-rank residue coupling $\otimes$ quotient-SUCC difference" target.
