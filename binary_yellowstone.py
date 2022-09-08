#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 19:37:30 2022

@author: nate
"""
import bitlib as bl
from print_table import compute_tbl_fmt

cache = {1: 1, 2: 2}
found = {1: True, 2: True}


def binary_yellowstone(n):
    global cache, found
    if n in cache:
        return cache[n]
    
    A = binary_yellowstone(n-1)
    B = binary_yellowstone(n-2)
    ker_A = bl.ker_int(A)
    ker_B = bl.ker_int(B)
    
    candidate = 1
    while True:
        candidate = candidate + 1

        if candidate in found:
            continue

        ker_candidate = bl.ker_int(candidate)
        
        prop1 = len(ker_candidate.intersection(ker_B)) > 0
        prop2 = len(ker_candidate.intersection(ker_A)) == 0
        
        if prop1 and prop2:
            cache[n] = candidate
            found[candidate] = True
            return candidate







N = 250

output = compute_tbl_fmt(binary_yellowstone, (1, N), "binary") 
print(output)
with open("./text_output/binary_yellowstone.txt","w") as fp:
    fp.write(output)
