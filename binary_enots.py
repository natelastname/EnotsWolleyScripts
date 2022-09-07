#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 14 12:09:12 2022

@author: nate
"""
'''
    Computes the binary Enots Wolley sequence
'''

import bitlib as bl
from print_table import compute_tbl_fmt

cache = {1: 1, 2: 3}
found = {1: True, 3: True}


def enots(n):
    global cache, found
    if n in cache:
        return cache[n]
    
    A = enots(n-1)
    B = enots(n-2)
    ker_A = bl.ker_int(A)
    ker_B = bl.ker_int(B)
    
    candidate = 1
    while True:
        candidate = candidate + 1

        if candidate in found:
            continue

        ker_C = bl.ker_int(candidate)
        
        prop1 = len(ker_C.intersection(ker_A)) > 0
        prop2 = len(ker_C.intersection(ker_B)) == 0
        prop3 = len(ker_C - ker_A) > 0
        
        if prop1 and prop2 and prop3:
            cache[n] = candidate
            found[candidate] = True
            return candidate





N = 100

output = compute_tbl_fmt(enots, (1, N), "binary") 
print(output)
with open("./text_output/binary_enots.txt","w") as fp:
    fp.write(output)

    
    
    

