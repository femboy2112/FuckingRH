#!/usr/bin/env python3
"""Rigorous pinned-tail slack from exact sieving and Arb block Taylor sums.

The native helper uses integers only. It outputs the number and first two
centered moments of primes in each block. Arb evaluates the transcendental
weight sums with a proved third-derivative remainder. No zeta zeros enter
the prefix construction. See PINNED_TAIL_SLACK.md for the mathematical scope.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import gzip
import json
from pathlib import Path
import subprocess
import shutil
import tempfile
from math import isqrt
from flint import arb, ctx

SIEVE_CPP = r'''
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>
int main(int argc,char**argv) {
 if(argc<5) return 2;
 uint64_t limit=std::stoull(argv[1]), divisor=std::stoull(argv[2]);
 std::vector<uint64_t> cuts;
 for(int i=4;i<argc;i++) cuts.push_back(std::stoull(argv[i]));
 cuts.push_back(limit);std::sort(cuts.begin(),cuts.end());
 cuts.erase(std::unique(cuts.begin(),cuts.end()),cuts.end());
 uint64_t root=0;while((root+1)*(root+1)<=limit)++root;
 std::vector<uint8_t> base(root+1,1);base[0]=base[1]=0;
 for(uint64_t p=2;p*p<=root;p++)if(base[p])for(uint64_t j=p*p;j<=root;j+=p)base[j]=0;
 std::vector<uint64_t> ps;for(uint64_t p=2;p<=root;p++)if(base[p])ps.push_back(p);
 std::ofstream out(argv[3]);out<<"lo,hi,count,m1,m2\n";
 uint64_t lo=2,hi=2,n=0,m2=0;int64_t m1=0;size_t ci=0;
 auto set_hi=[&](){while(ci<cuts.size()&&cuts[ci]<lo)++ci;
  hi=std::min(limit,lo+std::max(uint64_t(0),lo/divisor));
  if(lo>cuts.front()+1)hi=std::min(hi,lo+uint64_t(2047));
  if(ci<cuts.size())hi=std::min(hi,cuts[ci]);};set_hi();
 auto flush=[&](){out<<lo<<','<<hi<<','<<n<<','<<m1<<','<<m2<<'\n';
  lo=hi+1;n=0;m1=0;m2=0;set_hi();};
 const uint64_t segment=1<<22;uint64_t total=0;
 for(uint64_t begin=2;begin<=limit;begin+=segment){
  uint64_t end=std::min(limit,begin+segment-1);
  std::vector<uint8_t> sieve(end-begin+1,1);
  for(uint64_t p:ps){if(p*p>end)break;
   uint64_t start=std::max(p*p,((begin+p-1)/p)*p);
   for(uint64_t j=start;j<=end;j+=p)sieve[j-begin]=0;
  }
  for(uint64_t p=begin;p<=end;p++)if(sieve[p-begin]){
   while(p>hi)flush();
   int64_t d=(int64_t)p-(int64_t)((lo+hi)/2);
   ++n;m1+=d;m2+=(uint64_t)(d*d);++total;
  }
  if((begin/segment)%32==0)std::cerr<<"sieved "<<end<<" primes "<<total<<'\n';
 }
 while(lo<=limit)flush();
 std::cerr<<"prime_count "<<total<<'\n';return 0;
}
'''

# Ordinary long-double candidate selector only. Its states are NEVER accepted
# as interval evidence; every selected prefix/path/slack is rebuilt above.
DIAGNOSTIC_CPP = r'''
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <vector>
struct Kahan{long double v,c=0;void add(long double z){long double y=z-c,t=v+y;c=(t-v)-y;v=t;}};
int main(int argc,char**argv){
 if(argc!=5&&argc!=6)return 2;
 bool recovery=(argc==6);uint64_t previous=std::stoull(argv[1]);
 uint64_t start=std::stoull(argv[1]),limit=std::stoull(argv[2]);
 Kahan W{strtold(argv[3],0)},L{strtold(argv[4],0)};
 long double pi=acosl(-1.L),alpha=(logl(8*pi)+0.577215664901532860606512090082402431L+pi/2)/2;
 long double CA=pi*pi/4+2*0.91596559417721901505460351493238411077L;
 long double T=1e7L,z=pi/(2*T),AT=pi/T/tanhl(z)+pi/(T-1),v=logl(T/(2*pi));
 long double dT=v*v/(2*pi)-v/(6*pi);
 uint64_t root=0;while((root+1)*(root+1)<=limit)++root;
 std::vector<uint8_t>b(root+1,1);b[0]=b[1]=0;
 for(uint64_t p=2;p*p<=root;p++)if(b[p])for(uint64_t j=p*p;j<=root;j+=p)b[j]=0;
 std::vector<uint64_t>base;std::vector<std::pair<uint64_t,uint64_t>>hp;
 for(uint64_t p=2;p<=root;p++)if(b[p]){base.push_back(p);uint64_t n=p*p;
  while(n<=limit){if(n>start)hp.push_back({n,p});if(n>limit/p)break;n*=p;}}
 std::sort(hp.begin(),hp.end());size_t hpidx=0;
 uint64_t entry=0,count=0;long double Wa=0,La=0,a=0;
 const uint64_t segment=1<<22;
 for(uint64_t lo=start+1;lo<=limit;lo+=segment){
  uint64_t hi=std::min(limit,lo+segment-1);std::vector<uint8_t>s(hi-lo+1,1);
  for(uint64_t p:base){if(p*p>hi)break;uint64_t first=std::max(p*p,((lo+p-1)/p)*p);
   for(uint64_t j=first;j<=hi;j+=p)s[j-lo]=0;}
  std::vector<std::pair<uint64_t,uint64_t>>events;
  for(uint64_t p=lo;p<=hi;p++)if(s[p-lo])events.push_back({p,p});
  while(hpidx<hp.size()&&hp[hpidx].first<=hi)events.push_back(hp[hpidx++]);
  std::sort(events.begin(),events.end());
  for(auto e:events){uint64_t q=e.first,p=e.second;long double sq=sqrtl(q),ell=logl(q),w=logl(p)/sq;
   long double iz=1/sq,ap=2*sq-alpha+atanhl(iz)+atanl(iz)-2*iz;
   long double pre=W.v-ap;
   if(recovery&&pre<=0){std::cout<<std::setprecision(22)<<"{\"q\":"<<previous<<",\"next_event\":"<<q
     <<",\"next_event_base\":"<<p<<",\"pre_next_workload\":"<<pre
     <<",\"diagnostic_only\":true,\"events_scanned\":"<<count<<"}\n";return 0;}
   W.add(w);L.add(w*ell);long double post=W.v-ap;++count;previous=q;
   if(pre<=0){if(post>0){entry=q;Wa=W.v;La=L.v;a=ell;}else entry=0;}
   if(!recovery&&entry>start&&post>0&&ell-a>0.003L){
    long double P=W.v-Wa,Pm=P-w,BT=dT-alpha-Wa;
    long double rx=AT*sqrtl(entry)+BT,rq=AT*sq+BT,len=ell-a,jhat;
    if(rx>=Pm)jhat=Pm*len;else if(rq<=Pm)jhat=2*AT*(sq-sqrtl(entry))+BT*len;
    else{long double u=(Pm-BT)/AT;u*=u;jhat=2*AT*(sqrtl(u)-sqrtl(entry))+BT*logl(u/entry)+Pm*logl(q/u);}
    long double J=P*ell-(L.v-La),Eq=4*sq-alpha*ell+CA-8-W.v*ell+L.v;
    long double approx=Eq+J-jhat;
    if(approx<-.1L){std::cout<<std::setprecision(22)<<"{\"x\":"<<entry<<",\"q\":"<<q
      <<",\"candidate_slack\":"<<approx<<",\"Yq\":"<<post<<",\"length\":"<<len
      <<",\"diagnostic_only\":true,\"events_scanned\":"<<count<<"}\n";return 0;}
   }
  }
  if(((lo-start-1)/segment)%16==0)std::cerr<<"diagnostic through "<<hi<<" events "<<count<<'\n';
 }
 std::cout<<"{\"found\":false,\"diagnostic_only\":true}\n";return 0;
}
'''


def select_tail_candidate(seed_path, limit, output_path, recovery=False):
    seed=json.loads(Path(seed_path).read_text())
    if limit>20_000_000_000 or limit<=seed["x"]:
        raise ValueError("Invalid diagnostic range")
    with tempfile.TemporaryDirectory(prefix="rh-pinned-diagnostic-") as tmp:
        source,exe=Path(tmp)/"diagnostic.cpp",Path(tmp)/"diagnostic"
        source.write_text(DIAGNOSTIC_CPP)
        subprocess.run(["g++","-O3","-std=c++17","-Wall","-Wextra",str(source),"-o",str(exe)],check=True)
        args=[str(exe),str(seed["x"]),str(limit),seed["W_mid"],seed["L_mid"]]
        if recovery:args.append("recovery")
        result=subprocess.run(args,
                              check=True,text=True,stdout=subprocess.PIPE)
    Path(output_path).write_text(result.stdout)
    return json.loads(result.stdout)


def simple_primes(n):
    mask = bytearray(b"\1") * (n + 1)
    if n >= 1: mask[:2] = b"\0\0"
    for p in range(2, isqrt(n) + 1):
        if mask[p]: mask[p*p:n+1:p] = b"\0" * ((n-p*p)//p+1)
    return [p for p in range(2, n + 1) if mask[p]]


def build_moments(limit, cuts, path, divisor=2048):
    """Native exact sieve; no libm/transcendental or floating-point operations."""
    width=limit//divisor+1 if divisor>0 else 0
    half=(width+1)//2
    if (limit>20_000_000_000 or divisor<1024 or width*half*half>=2**64
            or width*half>=2**63 or half*half>=2**63):
        raise ValueError("Outside audited integer range/moment overflow bounds")
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="rh-pinned-sieve-") as tmp:
        source, executable = Path(tmp)/"sieve.cpp", Path(tmp)/"sieve"
        source.write_text(SIEVE_CPP)
        subprocess.run(["g++", "-O3", "-std=c++17", "-Wall", "-Wextra", str(source), "-o", str(executable)], check=True)
        raw_path=Path(tmp)/"moments.csv" if path.suffix==".gz" else path
        subprocess.run([str(executable), str(limit), str(divisor), str(raw_path), *map(str, sorted(cuts))], check=True)
        if path.suffix==".gz":
            with raw_path.open("rb") as source,path.open("wb") as target:
                with gzip.GzipFile(fileobj=target,mode="wb",mtime=0) as zipped:
                    shutil.copyfileobj(source,zipped)


def open_moments(path):
    path=Path(path)
    return gzip.open(path,"rt",newline="") if path.suffix==".gz" else path.open(newline="")


def moment_bytes(path):
    path=Path(path)
    return gzip.decompress(path.read_bytes()) if path.suffix==".gz" else path.read_bytes()


def block_weight_sums(lo, hi, n, m1, m2):
    """Enclose sums f(p)=log(p)/sqrt(p), g(p)=log(p)^2/sqrt(p)."""
    if n == 0: return arb(0), arb(0)
    c = (lo + hi) // 2
    h = max(c - lo, hi - c)
    z, L = arb(c), arb(c).log()
    root = z.sqrt()
    f0 = L/root
    f1 = (1-L/2)/(z*root)
    f2 = (3*L/4-2)/(z*z*root)
    g0 = L*L/root
    g1 = (2*L-L*L/2)/(z*root)
    g2 = (2-4*L+3*L*L/4)/(z*z*root)
    H = arb(hi).log()
    scale = arb(n)*h**3/(6*arb(lo)**3*arb(lo).sqrt())
    ef = scale*(arb(23)/4 + arb(15)/8*H)
    eg = scale*(9 + arb(23)/2*H + arb(15)/8*H*H)
    sf = n*f0 + m1*f1 + arb(m2)*f2/2
    sg = n*g0 + m1*g1 + arb(m2)*g2/2
    return sf + arb(0, ef.upper()), sg + arb(0, eg.upper())


def prefixes_from_moments(path, cuts):
    cuts = sorted(set(cuts))
    states = {}
    W, L, count = arb(0), arb(0), 0
    rows = 0
    with open_moments(path) as stream:
        for row in csv.DictReader(stream):
            lo, hi, n, m1, m2 = (int(row[k]) for k in ["lo", "hi", "count", "m1", "m2"])
            sw, sl = block_weight_sums(lo, hi, n, m1, m2)
            W += sw; L += sl; count += n; rows += 1
            if hi in cuts: states[hi] = [W, L, count, 0]
    if sorted(states) != cuts:
        raise ValueError("Moment file does not end blocks at every requested prefix")
    # Higher powers are disjoint from prime rows and are enumerated independently.
    for p in simple_primes(isqrt(max(cuts))):
        power = p*p; k = 2; lp = arb(p).log()
        while power <= max(cuts):
            w = lp/arb(power).sqrt()
            for cutoff in cuts:
                if power <= cutoff:
                    states[cutoff][0] += w
                    states[cutoff][1] += k*lp*w
                    states[cutoff][3] += 1
            power *= p; k += 1
    return states, rows


def independent_event_counts(cuts):
    """Structurally separate combinatorial primepi/integer-root count control."""
    from sympy import primepi, integer_nthroot
    out={}
    for n in cuts:
        primes=int(primepi(n));higher=0;k=2
        while True:
            root=integer_nthroot(n,k)[0]
            if root<2:break
            higher+=int(primepi(root));k+=1
        out[str(n)]={"primes":primes,"higher_prime_powers":higher,"all_events":primes+higher}
    return out


def constants():
    pi = arb.pi()
    alpha = ((8*pi).log()+arb.const_euler()+pi/2)/2
    ca = pi*pi/4+2*arb.const_catalan()
    return alpha, ca


def smooth_at_integer(n):
    """Exact A(log n), A'(log n), A''(log n) with positive-series tail."""
    n = arb(n)
    alpha, ca = constants()
    # A=4 sqrt(n)-alpha log n+ca-8 -4 sum_{k>=1} n^{-(4k+1)/2}/(4k+1)^2.
    term = 4/(25*n*n*n.sqrt())
    tail_upper = term/(1-1/(n*n))
    tail = arb(term.lower(), 0)
    # Enclose the complete nonnegative tail, not an asymptotically dropped term.
    tail = arb(0, tail_upper.upper())
    A = 4*n.sqrt()-alpha*n.log()+ca-8-tail
    z = 1/n.sqrt()
    slope = 2*n.sqrt()-alpha + z.atanh()+z.atan()-2*z
    curvature = n.sqrt()-1/(n.sqrt()*(n*n-1))
    return A, slope, curvature


def all_higher_powers(limit):
    out = []
    for p in simple_primes(isqrt(limit)):
        power = p*p
        while power <= limit:
            out.append((power, p))
            power *= p
    return sorted(out)


def interval_primes(lo, hi, bases):
    mask = bytearray(b"\1")*(hi-lo+1)
    for p in bases:
        if p*p>hi: break
        start = max(p*p, ((lo+p-1)//p)*p)
        if start<=hi:
            mask[start-lo:hi-lo+1:p]=b"\0"*((hi-start)//p+1)
    return [lo+i for i,v in enumerate(mask) if v and lo+i>=2]


def certify_same_excursion(path, x, q):
    """Prove Y>0 throughout (log x,log q], refining uncertain bins eventwise."""
    hp = all_higher_powers(q); hp_index=0
    bases = simple_primes(isqrt(q))
    Wp, Wh = arb(0), arb(0)
    checked=refined=events=0
    minimum=None
    with open_moments(path) as stream:
        for row in csv.DictReader(stream):
            lo,hi,n,m1,m2=(int(row[k]) for k in ["lo","hi","count","m1","m2"])
            block_hp=[]
            while hp_index<len(hp) and hp[hp_index][0]<=hi:
                block_hp.append(hp[hp_index]);hp_index+=1
            if lo>x and hi<=q:
                checked+=1
                margin=Wp+Wh-smooth_at_integer(hi)[1]
                if not margin>0:
                    refined+=1
                    event_list=[(p,p) for p in interval_primes(lo,hi,bases)]+block_hp
                    event_list.sort()
                    Wlocal=Wp+Wh
                    for event,prime in event_list:
                        pre=Wlocal-smooth_at_integer(event)[1]
                        if not pre>0:
                            return {"verified":False,"unresolved_coordinate":event,"workload":str(pre),
                                    "checked_blocks":checked,"refined_blocks":refined,"refined_events":events}
                        minimum=pre.lower() if minimum is None else min(minimum,pre.lower())
                        Wlocal+=arb(prime).log()/arb(event).sqrt();events+=1
                    endmargin=Wlocal-smooth_at_integer(hi)[1]
                    if not endmargin>0:
                        return {"verified":False,"unresolved_coordinate":hi,"workload":str(endmargin),
                                "checked_blocks":checked,"refined_blocks":refined,"refined_events":events}
                    minimum=endmargin.lower() if minimum is None else min(minimum,endmargin.lower())
                else:
                    minimum=margin.lower() if minimum is None else min(minimum,margin.lower())
            Wp+=block_weight_sums(lo,hi,n,m1,m2)[0]
            for event,prime in block_hp:
                Wh+=arb(prime).log()/arb(event).sqrt()
    return {"verified":True,"checked_blocks":checked,"refined_blocks":refined,
            "refined_events":events,"minimum_certified_workload_lower_bound":str(minimum)}


def pinned_constructor(x, q, Wx, Wq, T=10_000_000):
    if not (10_000_000 <= T <= 3_000_175_332_800 and x > max(T, 1_000_000_000) and q > x):
        raise ValueError("Outside independently verified-height / finite-spectral theorem domain")
    alpha, _ = constants()
    t = arb(T); pi = arb.pi()
    z = pi/(2*t)
    AT = pi/t/z.tanh()+pi/(t-1)
    v = (t/(2*pi)).log()
    dT = v*v/(2*pi)-v/(6*pi)
    BT = dT-alpha-Wx
    wq = arb(q).log()/arb(q).sqrt()  # Caller certifies that q is prime.
    Pm = Wq-Wx-wq
    Rx, Rq = AT*arb(x).sqrt()+BT, AT*arb(q).sqrt()+BT
    ell = (arb(q)/x).log()
    if Rx >= Pm:
        value, branch = Pm*ell, "terminal-cap"
    elif Rq <= Pm:
        value, branch = 2*AT*(arb(q).sqrt()-arb(x).sqrt())+BT*ell, "spectral-only"
    elif Rx < Pm and Rq > Pm:
        ustar = ((Pm-BT)/AT)**2
        value = 2*AT*(ustar.sqrt()-arb(x).sqrt())+BT*(ustar/x).log()+Pm*(arb(q)/ustar).log()
        branch = "crossing"
    else:
        raise ArithmeticError("Intervals do not determine the clipping branch")
    # Sufficient derivative bound proving U_T(u) increases with T for all u<=q.
    K = ((arb(T)/(2*pi)).log()-arb(1)/6)/pi
    derivative_margin = K-arb(q).sqrt()*(pi*pi/(3*arb(T)**2)+pi*arb(T)/(arb(T)-1)**2)
    return value, branch, derivative_margin


def certify_candidate(states, x, q, T=10_000_000, next_event=None):
    # Deterministic trial division establishes the two event labels are primes.
    for n in [x, q]:
        if n < 2 or any(n % p == 0 for p in simple_primes(isqrt(n))):
            raise ValueError("This narrow candidate evaluator requires prime anchor and terminal")
    Wx, Lx = states[x][:2]; Wq, Lq = states[q][:2]
    Ax, Apx, _ = smooth_at_integer(x)
    Aq, Apq, mq = smooth_at_integer(q)
    a, s = arb(x).log(), arb(q).log()
    E, Eq = Ax-Wx*a+Lx, Aq-Wq*s+Lq
    Ya, Yq = Wx-Apx, Wq-Apq
    if not (Ya > 0 and Yq > 0):
        raise ArithmeticError("Active anchor/terminal not certified")
    P = Wq-Wx
    J = P*s-(Lq-Lx)
    Jhat, branch, height_margin = pinned_constructor(x, q, Wx, Wq, T)
    # A'' is increasing after log 2. Frozen drawdown is between 0 and Yq²/(2mq).
    drawdown_bound = (Yq*Yq/(2*mq)).upper()
    V = Eq-arb(drawdown_bound/2, drawdown_bound/2)
    slack = V+J-Jhat
    result = {"x":x,"q":q,"T":T,"branch":branch,
              "Wx":str(Wx),"Lx":str(Lx),"Wq":str(Wq),"Lq":str(Lq),
              "anchor_value":str(E),"terminal_value":str(Eq),
              "anchor_workload":str(Ya),"terminal_workload":str(Yq),
              "true_cost":str(J),"pinned_upper_cost":str(Jhat),
              "frozen_reserve":str(V),"slack":str(slack),
              "slack_negative_certified": bool(slack < 0),
              "height_derivative_margin":str(height_margin),
              "all_admissible_heights_minimized_at_T": bool(T==10_000_000 and height_margin > 0),
              "prefix_prime_counts":{str(c):v[2] for c,v in states.items()},
              "prefix_higher_power_counts":{str(c):v[3] for c,v in states.items()},
              "episode_continuity_verified":False,
              "rh_proved":False}
    if x-1 in states:
        pre = states[x-1][0]-Apx
        result["anchor_pre_event_workload"] = str(pre)
        result["anchor_entry_certified"] = bool(pre <= 0 and Ya > 0)
    if next_event is not None:
        bases=simple_primes(isqrt(next_event))
        events=[(p,p) for p in interval_primes(q+1,next_event,bases)]
        events.extend((n,p) for n,p in all_higher_powers(next_event) if q<n<=next_event)
        events.sort()
        if not events or events[0][0]!=next_event:
            raise ValueError("The supplied next event is not the immediate prime-power successor")
        pre_next=Wq-smooth_at_integer(next_event)[1]
        result["next_event"]=next_event
        result["next_event_base"]=events[0][1]
        result["pre_next_workload"]=str(pre_next)
        result["strict_recovery_witness_certified"]=bool(Yq>0 and pre_next<0)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--x",type=int,default=1_066_070_623)
    parser.add_argument("--q",type=int,default=1_136_726_333)
    parser.add_argument("--next-event",type=int)
    parser.add_argument("--extra-cut",type=int,action="append",default=[])
    parser.add_argument("--divisor",type=int,default=2048)
    parser.add_argument("--precision",type=int,default=128)
    parser.add_argument("--moments",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--reuse-moments",action="store_true")
    parser.add_argument("--verify-episode",action="store_true")
    parser.add_argument("--independent-counts",action="store_true")
    args=parser.parse_args();ctx.prec=args.precision
    cuts=sorted(set([args.x-1,args.x,args.q]+args.extra_cut))
    if not args.reuse_moments: build_moments(args.q,cuts,args.moments,args.divisor)
    states,rows=prefixes_from_moments(args.moments,cuts)
    result=certify_candidate(states,args.x,args.q,next_event=args.next_event)
    if args.verify_episode:
        episode=certify_same_excursion(args.moments,args.x,args.q)
        result["episode_certificate"]=episode
        result["episode_continuity_verified"]=episode["verified"]
    if args.independent_counts:
        counts=independent_event_counts(cuts)
        for cut in cuts:
            if (counts[str(cut)]["primes"]!=states[cut][2]
                    or counts[str(cut)]["higher_prime_powers"]!=states[cut][3]):
                raise ArithmeticError("Independent event count disagrees")
        result["independent_counts"]=counts
    result.update({"precision_bits":ctx.prec,"taylor_divisor":args.divisor,"moment_blocks":rows,
                   "moment_sha256":hashlib.sha256(moment_bytes(args.moments)).hexdigest(),
                   "sieve_cpp_sha256":hashlib.sha256(SIEVE_CPP.encode()).hexdigest()})
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":main()
