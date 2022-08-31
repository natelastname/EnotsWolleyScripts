#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 09:11:33 2022

@author: nate
"""

'''
Compute A352200, the binary version of sequence A352187 and print the results
as a human-readable table.
'''



import sys
import bitlib as bl
from tabulate import tabulate



cache = {0: 0, 1: 1}
found = {0: True, 1: True}

def EKWolley(input_n):
    global cache, found
    
    if input_n in cache:
        return cache[input_n]
    
    i = 1
    ker_A = bl.ker_int(EKWolley(input_n-1))
    ker_B = bl.ker_int(EKWolley(input_n-2))


    while True:
        if i in found:
            i = i + 1
            continue
        
        ker_I = bl.ker_int(i)
        
        cond_A = len(ker_I.intersection(ker_A)) > 0
        
        cond_B = len(ker_I.intersection(ker_B)) == 0
        
        if ker_A.issubset(ker_B):
            cond_B = True
        
        if cond_A == True and cond_B == True:
            cache[input_n] = i
            found[i] = True
            return i
        
        i = i + 1
        


N = 250

rows = []

for i in range(0, N):
    term = EKWolley(i)
    fact_arr = bl.int_to_bit_arr(term)    
    lbl1 = f"a({i:5}) = "
    lbl2 = f"{term:5} = "
    lbl1 = lbl1 + lbl2
    fact_arr.insert(0, lbl1)
    fact_arr = list(map(lambda x: " " if x == 0 else x, fact_arr))
    rows.append(fact_arr)
    

num_cols = max(list(map(lambda x: len(x), rows))) - 1
print(num_cols)
rows.insert(0, [" "] + [2**i for i in range(0, num_cols)])
print(tabulate(rows))

    