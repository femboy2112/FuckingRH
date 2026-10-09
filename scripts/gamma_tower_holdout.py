import mpmath as mp
mp.mp.dps=55
for eps in (0,1):
 c=mp.mpf('.5')+eps
 print('parity',eps,'lambda_0',c)
 for t in (mp.mpf('.731'),mp.mpf('3.7'),mp.mpf('17.25')):
  target=mp.re(mp.digamma((1+2*eps)/4+1j*t/2)-mp.digamma(mp.mpf((1+2*eps)/4)))
  for M in (16,64,256):
   partial=2*sum(t*t/((2*m+c)*((2*m+c)**2+t*t)) for m in range(M))
   tail=target-partial
   bound=2*t*t/(2*M+c)**3 + t*t/(2*(2*M+c)**2)
   assert tail >= -mp.mpf('1e-40') and tail < bound
   print(f't={float(t):6.3f} M={M:3d} residual={float(tail):.6g} analytic_bound={float(bound):.6g}')
 if eps==0:
  print('WRONG PARITY at t=3.7',mp.nstr(mp.re(mp.digamma(mp.mpf('.25')+mp.j*mp.mpf('3.7')/2)-mp.digamma(mp.mpf('.25')))-mp.re(mp.digamma(mp.mpf('.75')+mp.j*mp.mpf('3.7')/2)-mp.digamma(mp.mpf('.75'))),14))
print('PASS: fresh gamma tower holdouts')
