#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:26:17 2022

@author: nate
"""

import sys
import bitlib as bl
from tabulate import tabulate


cache = {1: 1}
found = {1: True}

def binary_EKG(input_n):
    global cache, found
    
    if input_n in cache:
        return cache[input_n]
    
    i = 1
    ker_A = bl.ker_int(binary_EKG(input_n-1))

    while True:
        if i in found:
            i = i + 1
            continue
        
        ker_B = bl.ker_int(i)
        
        if len(ker_A.intersection(ker_B)) > 0:
            found[i] = True
            cache[input_n] = i
            return i
        
        i = i + 1
        


N = 34

rows = []

for i in range(1, N):
    term = binary_EKG(i)
    fact_arr = bl.int_to_bit_arr(term)    
    lbl1 = f"a({i}) = "
    lbl2 = f"{term} = "
    lbl1 = lbl1 + lbl2
    fact_arr.insert(0, lbl1)
    fact_arr = list(map(lambda x: " " if x == 0 else x, fact_arr))
    rows.append(fact_arr)
    

num_cols = max(list(map(lambda x: len(x), rows))) - 1
print(num_cols)
rows.insert(0, [" "] + [2**i for i in range(0, num_cols)])
print(tabulate(rows))

    
    
    