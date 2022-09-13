#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 19:37:30 2022

@author: nate
"""
import bitlib as bl
from print_table import compute_tbl_fmt


from cached_sequence import *

cache = {0: 0, 1: 1, 2: 2}
found = {0: True, 1: True, 2: True}


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


from print_table import gen_files_fmt
N = 257
gen_files_fmt(binary_yellowstone, "binary", "yellowstone", irange1=(0, N))
    
    
    
    
    
    
    
    
    