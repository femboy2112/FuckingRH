#!/usr/bin/env python3
"""Exact finite chain tests for causal compressed-shift boundary commutators.

Finite integer displacements are a faithful matrix model of the algebraic
interval-projection formulas; no zeta zeros are involved.
"""
import numpy as np


def shift(n:int):
    S=np.zeros((n,n))
    for i in range(1,n):
        S[i,i-1]=1
    return S


def test_one(n:int,h:int,k:int):
    S=shift(n)
    Th=np.linalg.matrix_power(S,h)
    Tk=np.linalg.matrix_power(S,k)
    assert np.array_equal(Th@Tk, Tk@Th)
    assert np.array_equal(Th@Tk, np.linalg.matrix_power(S,h+k))

    comm=Th.T@Tk-Tk@Th.T
    formula=np.zeros((n,n))
    for x in range(n):
        y=x+h-k
        if 0<=y<n:
            formula[x,y]=int(0<=x+h<n)-int(0<=x-k<n)
    assert np.array_equal(comm,formula)
    return int(np.count_nonzero(comm)),float(np.linalg.norm(comm,ord=2))


def main():
    for n in [6,12,20]:
        for h,k in [(1,2),(2,3),(3,1),(4,4)]:
            if max(h,k)>=n:
                continue
            entries,norm=test_one(n,h,k)
            print(f"chain={n:2d} h={h} k={k} nonzero={entries} norm={norm:.6g}")
    print("PASS: forward shifts commute, mixed adjoints produce only boundary partial shifts.")


if __name__=="__main__":
    main()
