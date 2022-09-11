#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:07:13 2022

@author: nate
"""
'''
    Generate a table of formatted terms of the Enots Wolley sequence (A336957)
'''



import factlib as fl
from print_table import compute_tbl_fmt

cache = {1: 1, 2: 2, 3: 6}
found = {1: True, 2: True, 6: True}


def primefact_enots(n):    
    global cache, found
    if n in cache:
        return cache[n]
    
    A = primefact_enots(n-1)
    B = primefact_enots(n-2)
    ker_A = fl.kernel(A)
    ker_B = fl.kernel(B)
    
    candidate = 1
    while True:
        candidate = candidate + 1

        if candidate in found:
            continue

        ker_C = fl.kernel(candidate)
        
        prop1 = len(ker_C.intersection(ker_A)) > 0
        prop2 = len(ker_C.intersection(ker_B)) == 0
        prop3 = len(ker_C - ker_A) > 0
        
        if prop1 and prop2 and prop3:
            cache[n] = candidate
            found[candidate] = True
            return candidate



N = 250
output = compute_tbl_fmt(primefact_enots, (1, N), "primefact") 
print(output)

with open("./text_output/primefact_enots.txt","w") as fp:
    fp.write(output)

