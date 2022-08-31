#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 08:45:28 2022

@author: nate
"""

import primefac as pf
import sys
import factlib as fl
from tabulate import tabulate


cache = {1: 1, 2: 2}
found = {1: True, 2: True}

def kernel(input_n):
    factors = [x for x in pf.primefac(input_n)]
    return set(factors)

def EKG(input_n):
    global cache, found
    
    if input_n in cache:
        return cache[input_n]
    
    i = 3
    ker_A = kernel(EKG(input_n - 1))
    while True:
        if i in found:
            i = i + 1
            continue
        
        ker_B = kernel(i)
        
        if len(ker_A.intersection(ker_B)) > 0:
            found[i] = True
            cache[input_n] = i
            return i
        
        i = i + 1
        


N = 34

rows = []

for i in range(1, N+1):
    term = i
    fact_arr = fl.int_to_fact_arr(term)    
    lbl1 = f"a({i}) = "
    lbl2 = f"{term} = "
    lbl1 = lbl1 + lbl2
    fact_arr.insert(0, lbl1)
    fact_arr = list(map(lambda x: " " if x == 0 else x, fact_arr))
    rows.append(fact_arr)
    
rows.insert(0, [" "] + fl.get_primes())

print(tabulate(rows))
sys.exit(0)
    
    
    
    





















