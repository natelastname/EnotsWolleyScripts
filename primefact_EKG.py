#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 08:45:28 2022

@author: nate
"""

import primefac as pf
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
        



import sys
from print_table import compute_tbl_fmt

N = 250

output = compute_tbl_fmt(EKG, (1, N), "primefact") 
print(output)
with open("./text_output/primefact_EKG.txt","w") as fp:
    fp.write(output)



















